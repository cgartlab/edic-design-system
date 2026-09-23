#!/usr/bin/env python3
"""validate_cssref.py — Cross-references HTML class usage against CSS class definitions.

检查项：
  1. HTML 中使用的 ds-* class 是否在 styles.css 中定义
  2. 跳过<pre><code> 和 .ds-code 块中的示例代码
  3. 处理多行 class 属性、跨行 CSS 选择器、复合选择器、@media 嵌套
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_GLOB = "*.html"
CSS_FILE = ROOT / "styles.css"
JS_FILE = ROOT / "scripts.js"

# 需要检查的 class 前缀
TARGET_PREFIXES = ("ds-",)

# 匹配 HTML class 属性（支持多行）
HTML_CLASS_PATTERN = re.compile(r'\bclass\s*=\s*["\']([^"\']*)["\']', re.DOTALL)

# 匹配 CSS class 选择器（包括复合选择器、@media 嵌套内的选择器）
# 匹配以 . 开头的 class 选择器，支持跨行
CSS_CLASS_SELECTOR_PATTERN = re.compile(
    r'(?:^|[,\s}\n])(\.(?:[a-zA-Z_][a-zA-Z0-9_-]*|' +
    r'\[[^\]]+\]|\:[a-zA-Z_][a-zA-Z0-9_-]*(?:\([^)]*\))?)+)',
    re.MULTILINE
)

# 匹配 CSS 选择器中的 class 名（提取 .classname）
SELECTED_CLASS_PATTERN = re.compile(r'\.([a-zA-Z_][a-zA-Z0-9_-]*)')

# 跳过块标记（这些块内的是示例代码，不是实际使用）
SKIP_BLOCK_PATTERNS = (
    re.compile(r'<pre[^>]*>.*?</pre>', re.DOTALL | re.IGNORECASE),
    re.compile(r'<code[^>]*>.*?</code>', re.DOTALL | re.IGNORECASE),
    re.compile(r'<figure[^>]*class\s*=\s*["\'][^"\']*ds-code[^"\']*["\']', re.DOTALL | re.IGNORECASE),
)

# SVG style 标签内嵌 CSS（需额外扫描）
SVG_STYLE_PATTERN = re.compile(r'<style[^>]*>(.*?)</style>', re.DOTALL | re.IGNORECASE)


def extract_html_classes(html_text: str, verbose: bool = False) -> dict[tuple[str, int], set[str]]:
    """从 HTML 中提取 class，忽略示例代码块。

    Returns:
        dict[(filename, line_no), set_of_classes]
    """
    # 先移除需要跳过的块
    cleaned = html_text
    for pattern in SKIP_BLOCK_PATTERNS:
        cleaned = pattern.sub('', cleaned)

    classes_map: dict[tuple[str, int], set[str]] = {}
    for match in HTML_CLASS_PATTERN.finditer(cleaned):
        value = match.group(1)
        # 支持多行 class 属性，按空白分割
        line_no = cleaned[:match.start()].count("\n") + 1
        classes = set()
        for cls in value.split():
            cls = cls.strip()
            if cls and any(cls.startswith(p) for p in TARGET_PREFIXES):
                classes.add(cls)
        if classes:
            key = (match.group(0), line_no)
            classes_map[key] = classes

    # 也扫描 SVG <style> 标签
    for svg_match in SVG_STYLE_PATTERN.finditer(html_text):
        svg_style_content = svg_match.group(1)
        svg_line_offset = html_text[:svg_match.start()].count("\n") + 1
        for css_cls_match in SELECTED_CLASS_PATTERN.finditer(svg_style_content):
            cls = css_cls_match.group(1)
            if any(cls.startswith(p) for p in TARGET_PREFIXES):
                key = (f"<svg:style> at line {svg_line_offset}", svg_line_offset)
                if key not in classes_map:
                    classes_map[key] = set()
                classes_map[key].add(cls)

    return classes_map


def extract_css_classes(css_text: str) -> set[str]:
    """从 CSS 文件中提取所有 class 选择器名称。

    直接扫描整个 CSS 文本，提取所有 `.classname` 模式。
    不需要剥离 @media 块——每个 block 内的选择器仍然被 `.xxxx` 格式覆盖。
    注意排除：
    - url() / data: URI 内的 class 名
    - CSS 注释内的 class 名
    - @import / @font-face / @supports 等 at-rule 中的无关 class 名
    """
    # 移除 CSS 注释
    cleaned = re.sub(r'/\*.*?\*/', '', css_text, flags=re.DOTALL)

    classes: set[str] = set()
    for match in SELECTED_CLASS_PATTERN.finditer(cleaned):
        cls = match.group(1)
        start = max(0, match.start() - 20)
        prefix = cleaned[start:match.start()].strip()
        if prefix.rstrip(',').endswith('url('):
            continue
        if prefix and not prefix[0].isalpha() and '@' in prefix:
            continue
        classes.add(cls)

    return classes


def extract_js_hook_classes(js_path: Path) -> set[str]:
    """从 scripts.js 提取通过 querySelector 引用的 class 名。
    这些 class 是 JS 钩子（非样式 hook），即使不在 CSS 定义也是合理的。
    """
    if not js_path.exists():
        return set()
    text = js_path.read_text(encoding="utf-8", errors="replace")
    hooks: set[str] = set()
    for m in re.finditer(r"""['"]\.([a-zA-Z_][a-zA-Z0-9_-]*)['"]""", text):
        hooks.add(m.group(1))
    return hooks


def check_cssref(html_files: list[Path], css_file: Path, js_file: Path, verbose: bool = False) -> tuple[list[str], list[str]]:
    """交叉引用检查：HTML class vs CSS 定义。"""
    errors: list[str] = []
    warnings: list[str] = []

    if verbose:
        print(f"读取 CSS: {css_file}")

    css_text = css_file.read_text(encoding="utf-8", errors="replace")
    defined_classes = extract_css_classes(css_text)
    js_hooks = extract_js_hook_classes(js_file)

    if verbose:
        print(f"CSS 中定义的选择器: {len(defined_classes)} 个")
        print(f"JS 钩子 class : {len(js_hooks)} 个")

    html_classes: dict[tuple[str, int], set[str]] = {}
    for html_path in html_files:
        html_text = html_path.read_text(encoding="utf-8", errors="replace")
        found = extract_html_classes(html_text, verbose)
        for (key, line), classes in found.items():
            html_classes[(str(html_path.name), line)] = classes

    if verbose:
        print(f"扫描 HTML 文件: {len(html_files)} 个")

    for (filename, line_no), classes in html_classes.items():
        for cls in classes:
            if cls not in defined_classes:
                # 排除 JS 钩子 class（用于 querySelector，不需要 CSS 定义）
                if cls in js_hooks:
                    continue
                errors.append(f"{filename}:{line_no} [ERROR] 未定义的 class: {cls}")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Cross-references HTML class usage against CSS class definitions."
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    args = parser.parse_args()

    html_files = list(ROOT.glob(HTML_GLOB))

    if args.verbose:
        print(f"扫描 HTML 文件: {[f.name for f in html_files]}")

    if not html_files:
        print("[WARN] 未找到 HTML 文件")
        return 2

    if not CSS_FILE.exists():
        print(f"[ERROR] CSS 文件不存在: {CSS_FILE}")
        return 1

    errors, warnings = check_cssref(html_files, CSS_FILE, JS_FILE, verbose=args.verbose)

    print("─── CSS 引用检查 ───")
    print(f"扫描 HTML: {len(html_files)} 个")
    print(f"扫描 CSS : {CSS_FILE.name}")
    print()

    if errors:
        for issue in errors:
            print(issue)
    else:
        print("[OK] 所有 ds-* class 均已在 CSS 中定义")

    if warnings and args.verbose:
        for issue in warnings:
            print(issue)

    print()
    print(f"错误: {len(errors)}  警告: {len(warnings)}")
    return 1 if errors else (2 if warnings else 0)


if __name__ == "__main__":
    sys.exit(main())
