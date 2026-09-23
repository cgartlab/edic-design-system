#!/usr/bin/env python3
"""validate_hardcode.py — 检测 HTML/CSS 中硬编码的颜色值（oklch/hex/rgb/hsl）

原则：所有颜色必须使用 --ds-* 设计令牌，禁止在 token 定义以外的任何地方
硬编码 oklch(...) / #hex / rgb(...) / rgba(...) / hsl(...) / hsla(...)。

排除项（不报告）：
  1. --ds-* 变量声明的值（如 --ds-color-fg: oklch(20% 0.02 60);）
  2. <pre><code> / <code> / .ds-code 块（代码示例中的样本颜色）
  3. SVG data: URL（data:image/svg+xml,...）
  4. CSS @keyframes 及 animation 定义中的颜色
  5. var(--ds-*) 引用（引用 token 是正确的）

报告规则：
  - ERROR : CSS 文件中（非 --ds-* 声明、非 animation）硬编码颜色
  - WARNING : HTML 文件中 style="color:..." 内联样式，或 SVG fill/stroke 属性硬编码颜色
  - exit0  : 全部干净
  - exit 1  :存在 ERROR
  - exit 2  : 仅 WARNING，无 ERROR
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_GLOB = "*.html"
CSS_FILE = ROOT / "styles.css"

# ---------------------------------------------------------------
# 正则：匹配所有需要检测的颜色格式
# ---------------------------------------------------------------
# oklch(<values> [ / alpha]) — 匹配百分比或小数点数值，alpha 通道可选
RE_OKLCH = re.compile(r'\boklch\(\s*[\d.]+%?\s+[\d.]+\s+[\d.]+\s*(?:/\s*[\d.]+%?)?\s*\)', re.I)
# 十六进制：3位、4位、6位、8位
RE_HEX = re.compile(r'#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b')
# rgb / rgba / hsl / hsla
RE_RGB = re.compile(r'\brgba?\s*\([^)]+\)', re.I)
RE_HSL = re.compile(r'\bhsla?\s*\([^)]+\)', re.I)

COLOR_PATTERNS = [RE_OKLCH, RE_HEX, RE_RGB, RE_HSL]

# 匹配 --ds-* 变量名（用于排除 token 定义行）
RE_DS_VAR_DEF = re.compile(r'--ds-[a-zA-Z0-9_-]+\s*:')

# 匹配 CSS变量引用 var(--ds-...)
RE_VAR_REF = re.compile(r'\bvar\(--ds-[^)]+\)', re.I)

# 匹配 @keyframes（整行或 selector 块）
RE_KEYFRAMES = re.compile(r'@[a-z]+(-[a-z]+)*\s*\{', re.I)

# 匹配 animation 相关属性（用于在 rule 内排除）
RE_ANIM_PROP = re.compile(
    r'\banimation(?:-name|-duration|-timing-function|-delay|-iteration-count|-direction|-fill-mode|-play-state)?\s*:',
    re.I,
)
# 匹配 CSS 属性名（用于判断当前 rule 是否为 animation 相关）
RE_CSS_PROP = re.compile(r'^\s*([a-z-]+)\s*:')

# ---------------------------------------------------------------
# 工具函数
# ---------------------------------------------------------------

def find_color_matches(text: str):
    """返回所有颜色匹配的 (match, line_no) 列表。"""
    results = []
    for pat in COLOR_PATTERNS:
        for m in pat.finditer(text):
            line_no = text[:m.start()].count('\n') + 1
            results.append((m.group(), m.start(), line_no))
    # 按文本位置排序（处理同一位置被多个模式匹配的情况）
    results.sort(key=lambda x: x[1])
    return results


def strip_css_comments(line: str) -> str:
    """移除行内 CSS块注释 /* ... */（保留注释外字符）。"""
    if '/*' not in line:
        return line
    before, _, rest = line.partition('/*')
    if '*/' in rest:
        after = rest.split('*/', 1)[1]
        return before + after
    return before


def find_html_code_blocks(text: str) -> list[tuple[int, int]]:
    """返回 HTML 中 <pre>...<code>...</pre> 和 <code>...</code> 及 .ds-code 的起止行号区间。
    返回 [(start_line, end_line), ...]，行号从 1 开始。
    """
    intervals = []
    # 匹配 <pre...> 和</pre>
    for m in re.finditer(r'<pre\b[^>]*>.*?</pre>', text, re.DOTALL | re.I):
        start = text[:m.start()].count('\n') + 1
        end = text[:m.end()].count('\n') + 1
        intervals.append((start, end))
    # 匹配 <code>（不在 <pre> 内，独立一行或 inline）
    for m in re.finditer(r'<code\b[^>]*>(?:(?!</code>).)*</code>', text, re.DOTALL | re.I):
        start = text[:m.start()].count('\n') + 1
        end = text[:m.end()].count('\n') + 1
        intervals.append((start, end))
    # 匹配 class="ds-code" 或 class="... ds-code ..."
    for m in re.finditer(r'class="[^"]*\bds-code\b[^"]*"[^>]*>.*?</[^>]+>', text, re.DOTALL | re.I):
        start = text[:m.start()].count('\n') + 1
        end = text[:m.end()].count('\n') + 1
        intervals.append((start, end))
    return intervals


def in_code_block(line_no: int, intervals: list[tuple[int, int]]) -> bool:
    """判断行号是否落在代码块区间内。"""
    for s, e in intervals:
        if s <= line_no <= e:
            return True
    return False


def find_svg_data_urls(text: str) -> set[int]:
    """返回 SVG data: URL所在行号集合（这些行内的颜色会被排除）。"""
    lines_with_data_url = set()
    for m in re.finditer(r'data:image/svg\+xml', text, re.I):
        line_no = text[:m.start()].count('\n') + 1
        lines_with_data_url.add(line_no)
    return lines_with_data_url


def is_inline_style_line(line_no: int, html_lines: list[str]) -> bool:
    """判断指定行是否包含 style="..." 内联样式（不跨越多行）。"""
    if 0 <= line_no - 1 < len(html_lines):
        return 'style=' in html_lines[line_no - 1]
    return False


def is_svg_attr_context(line_no: int, html_lines: list[str]) -> bool:
    """判断行是否在 SVG 元素上下文中（包含 fill=/stroke= 属性）。"""
    if 0 <= line_no - 1 < len(html_lines):
        line = html_lines[line_no - 1].lower()
        return 'fill=' in line or 'stroke=' in line
    return False


# ---------------------------------------------------------------
# CSS 扫描
# ---------------------------------------------------------------

def check_css(path: Path, verbose: bool) -> tuple[list[str], list[str]]:
    """扫描 CSS 文件中的硬编码颜色。返回 (errors, warnings)。"""
    errors: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        return errors, warnings

    text = path.read_text(encoding='utf-8', errors='replace')
    lines = text.splitlines()

    brace_depth = 0
    in_keyframes = False
    keyframes_depth = 0

    for i, raw in enumerate(lines):
        line_no = i + 1
        line = strip_css_comments(raw)
        if not line.strip():
            continue

        # --ds-* 变量定义行：`--ds-color-fg: oklch(20% 0.02 60);` → 跳过
        if RE_DS_VAR_DEF.search(line):
            continue

        # var(--ds-*) 引用行但不含其他颜色 → 跳过
        if RE_VAR_REF.search(line) and not any(p.search(line) for p in COLOR_PATTERNS):
            continue

        # 计算括号深度变化
        delta = 0
        j = 0
        in_str = False
        str_char = None
        while j < len(line):
            c = line[j]
            if not in_str:
                if c in ('"', "'"):
                    in_str = True
                    str_char = c
                elif c == '{':
                    delta += 1
                elif c == '}':
                    delta -= 1
            else:
                if c == '\\':
                    j += 2
                    continue
                if c == str_char:
                    in_str = False
            j += 1

        # 检测 @keyframes 或 @-prefix-keyframes 开始
        if re.match(r'@-?\w*-?keyframes\b', line, re.I):
            if delta > 0:
                # 多行 keyframes：跟踪进入的 brace 深度，直到退出时清除
                in_keyframes = True
                keyframes_depth = brace_depth + delta
            # 单行 keyframes（所有 { } 在同一行，delta=0）：不进入跟踪模式
            # 直接跳过该行（已是 @keyframes token 声明行，不触发重复检测）
            continue

        brace_depth += delta
        brace_depth = max(brace_depth, 0)

        # 判断是否退出 keyframes 块
        if in_keyframes and brace_depth <= keyframes_depth - 1:
            in_keyframes = False

        # 在 @keyframes 块内 → 跳过
        if in_keyframes:
            continue

        # 检测颜色
        for color_matched, _, _ in find_color_matches(line):
            if RE_VAR_REF.search(line):
                continue
            errors.append(
                f"{path.name}:{line_no} bare {color_matched} — "
                f"use --ds-* token"
            )

    return errors, warnings


# ---------------------------------------------------------------
# HTML 扫描
# ---------------------------------------------------------------

def check_html(path: Path, verbose: bool) -> tuple[list[str], list[str]]:
    """扫描 HTML 文件中的硬编码颜色。返回 (errors, warnings)。"""
    errors: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        return errors, warnings

    text = path.read_text(encoding='utf-8', errors='replace')
    html_lines = text.splitlines()

    code_block_intervals = find_html_code_blocks(text)
    data_url_lines = find_svg_data_urls(text)

    #逐行分析
    for line_no, line in enumerate(html_lines, 1):
        # 跳过代码块
        if in_code_block(line_no, code_block_intervals):
            continue

        # 跳过 SVG data: URL 行
        if line_no in data_url_lines:
            continue

        # 检测内联 style= 属性
        has_inline_style = 'style=' in line

        # 检测 SVG fill/stroke 属性
        is_svg_context = is_svg_attr_context(line_no, html_lines)

        for color_matched, _, _ in find_color_matches(line):
            # 排除 var(--ds-*) 引用
            if RE_VAR_REF.search(line):
                continue

            if has_inline_style:
                # style="color: xxx" → WARNING
                warnings.append(
                    f"{path.name}:{line_no} inline style contains bare "
                    f"{color_matched} — use --ds-* token"
                )
            elif is_svg_context:
                # SVG fill/stroke → WARNING
                warnings.append(
                    f"{path.name}:{line_no} SVG attribute bare "
                    f"{color_matched} — use --ds-* token"
                )
            else:
                # 其他 → ERROR
                errors.append(
                    f"{path.name}:{line_no} bare {color_matched} — "
                    f"use --ds-* token"
                )

    return errors, warnings


# ---------------------------------------------------------------
# main
# ---------------------------------------------------------------

# 示例页面列表：这些页面是独立演示页面，自带嵌入 CSS，
# 硬编码颜色仅报告为 WARNING 不阻塞 CI
EXAMPLE_PAGES = {"blog.html", "company.html", "report.html", "resume.html"}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="检测 HTML/CSS 中硬编码的颜色值，强制使用 --ds-* 设计令牌"
    )
    parser.add_argument('--verbose', '-v', action='store_true', help='详细输出')
    parser.add_argument('paths', nargs='*', type=Path,
                        help='指定扫描文件路径（默认扫描全部 *.html + styles.css）')
    args = parser.parse_args()

    # 确定扫描目标
    if args.paths:
        html_files = [p for p in args.paths if p.suffix == '.html']
        css_files = [p for p in args.paths if p.suffix == '.css']
    else:
        html_files = sorted(ROOT.glob(HTML_GLOB))
        css_files = [CSS_FILE]

    if not html_files and not css_files:
        print("[WARN] 未发现扫描目标文件")
        return 2

    all_errors: list[str] = []
    all_warnings: list[str] = []

    for p in html_files:
        errs, warns = check_html(p, args.verbose)
        # 示例页面中的硬编码颜色降级为 WARNING（不阻塞 CI）
        if p.name in EXAMPLE_PAGES:
            all_warnings.extend(errs)
            all_warnings.extend(warns)
        else:
            all_errors.extend(errs)
            all_warnings.extend(warns)

    for p in css_files:
        errs, warns = check_css(p, args.verbose)
        all_errors.extend(errs)
        all_warnings.extend(warns)

    print("─── 硬编码颜色检查 ───")
    print(f"扫描 HTML : {len(html_files)} 个")
    print(f"扫描 CSS  : {[p.name for p in css_files]}")
    print()

    if all_errors:
        for e in all_errors:
            print(f"[ERROR] {e}")
    if all_warnings:
        for w in all_warnings:
            print(f"[WARN] {w}")
    if not all_errors and not all_warnings:
        print("[OK] 未发现硬编码颜色")

    print()
    print(f"错误: {len(all_errors)}  警告: {len(all_warnings)}")

    if all_errors:
        return 1
    if all_warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())