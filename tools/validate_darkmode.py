#!/usr/bin/env python3
"""validate_darkmode.py — 校验暗色模式令牌完整性

检查项：
  ERRORS (退出码 1):
    - pure black oklch(0% ...) / oklch(0 ...) 出现在 [data-theme="dark"] 值中

  WARNINGS (退出码 2):
    - 浅色 token 在暗色模式中缺少对应覆盖
    - 暗色模式独有孤立 token（dark-only，无浅色对应）
    - pure white oklch(100% ...) 出现在暗色值中
    - 暗色基础色使用近零 chroma 的中性灰（非暖灰）

  退出码：0 = 全部通过 / 1 = 错误 / 2 = 警告
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLES_CSS = ROOT / "styles.css"

# Token 类别：需要在暗色模式中有对应覆盖
COLOR_CATEGORIES = {
    "color", "fg", "surface", "border", "glass", "glow", "blur", "accent",
}

# Token 类别：不检查暗色覆盖（这些类别在深色下需要不同处理策略）
EXCLUDED_CATEGORIES = {
    "shadow", "duration", "ease", "bp", "z", "space", "radius",
    "font", "weight", "leading", "tracking", "code", "token",
    "text", "cjk", "reveal", "draw", "stack", "brand",
}

# 匹配 oklch(...) 颜色表达式
OKLCH_COLOR = re.compile(
    r"oklch\s*\(\s*"
    r"([\d.]+)%\s+([\d.]+)\s+([\d.]+)"
    r"(\s*/\s*[\d.]+%)?"
    r"\s*\)",
    re.IGNORECASE,
)

# 匹配纯黑（luminance = 0）
PURE_BLACK = re.compile(r"oklch\s*\(\s*0(?!\.\d)\s*[\d.]+\s+[\d.]+\s*\)", re.IGNORECASE)

# 匹配纯白（luminance = 100）
PURE_WHITE = re.compile(r"oklch\s*\(\s*100[\d.]*\s+[\d.]+\s+[\d.]+\s*\)", re.IGNORECASE)

# 匹配近零 chroma（< 0.005）
NEAR_ZERO_CHROMA = re.compile(
    r"oklch\s*\(\s*[\d.]+\s+([\d.]+)\s+[\d.]+\s*\)",
    re.IGNORECASE,
)

CSS_VAR_DECL = re.compile(r"(--ds-[a-z0-9-]+)\s*:\s*([^;]+);")


def extract_block_by_selector(css: str, selector: str) -> str:
    """Extract CSS block content for a given selector using brace-depth scanning.

    Handles properly nested CSS (e.g. @media queries inside :root) by counting
    brace depth instead of assuming a flat structure.
    Returns the block content (without the selector + braces) or empty string
    if the selector is not found.
    """
    # Find the selector start
    idx = 0
    while True:
        pos = css.find(selector, idx)
        if pos == -1:
            return ""
        # Verify it's at a word boundary (not inside another selector)
        if pos > 0:
            ch = css[pos - 1]
            if ch.isalnum() or ch == "-":
                idx = pos + 1
                continue
        # Verify it's followed by optional whitespace then {
        rest = css[pos + len(selector):]
        if not rest.startswith(" ") and not rest.startswith("\n") and not rest.startswith("\t"):
            idx = pos + 1
            continue
        # Find the opening brace
        brace_pos = rest.find("{")
        if brace_pos == -1:
            return ""
        block_start = pos + len(selector) + brace_pos + 1
        break

    # Scan by brace depth to find the matching closing brace
    depth = 1
    i = block_start
    while i < len(css) and depth > 0:
        ch = css[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        i += 1

    if depth == 0:
        return css[block_start : i - 1]
    return ""


def extract_vars_from_block(block: str) -> dict[str, str]:
    """从 CSS 块中提取所有 --ds-* 变量。"""
    vars_ = {}
    for match in CSS_VAR_DECL.finditer(block):
        name = match.group(1)
        value = match.group(2).strip()
        vars_[name] = value
    return vars_


def is_color_related_token(name: str) -> bool:
    """判断 token 是否属于需要在暗色模式中覆盖的颜色相关类别。"""
    if not name.startswith("--ds-"):
        return False
    # 去掉前缀
    rest = name[5:]
    # 截取类别名（第一个段）
    category = rest.split("-")[0] if "-" in rest else rest
    return category in COLOR_CATEGORIES


def is_excluded_token(name: str) -> bool:
    """判断 token 是否属于故意不做深色覆盖检查的类别。"""
    if not name.startswith("--ds-"):
        return False
    rest = name[5:]
    category = rest.split("-")[0] if "-" in rest else rest
    return category in EXCLUDED_CATEGORIES


def check_pure_black(value: str, filename: str, line_no: int) -> list[str]:
    """检测 oklch 值是否为 pure black (luminance=0)。"""
    issues = []
    for match in PURE_BLACK.finditer(value):
        issues.append(
            f"{filename}:{line_no} pure black oklch in dark mode value: "
            f"{match.group()} (use warm dark base, not pure black)"
        )
    return issues


def check_pure_white(value: str, filename: str, line_no: int) -> list[str]:
    """检测 oklch 值是否为 pure white (luminance=100)。"""
    issues = []
    for match in PURE_WHITE.finditer(value):
        issues.append(
            f"{filename}:{line_no} pure white oklch in dark mode value: "
            f"{match.group()} (dark mode should not have pure white)"
        )
    return issues


def check_near_zero_chroma(value: str, filename: str, line_no: int) -> list[str]:
    """检测暗色模式 oklch 值是否使用近零 chroma 的中性灰（应使用暖灰）。"""
    issues = []
    for match in OKLCH_COLOR.finditer(value):
        luminance = float(match.group(1))
        chroma = float(match.group(2))
        # 仅对暗色范围的明度（L < 30%）发出此警告
        if luminance < 30 and 0 < chroma < 0.005:
            issues.append(
                f"{filename}:{line_no} near-zero chroma in dark value: "
                f"{match.group()} (dark base should be warm gray, not neutral gray)"
            )
    return issues


def check_oklch_in_value(value: str) -> list[str]:
    """检测 oklch 颜色值中的 pure black/white 问题。"""
    issues = []
    for m in OKLCH_COLOR.finditer(value):
        luminance = float(m.group(1))
        chroma = float(m.group(2))
        # Pure black: luminance = 0
        if luminance == 0:
            issues.append(f"pure black oklch(0 ...)")
        # Pure white: luminance = 100
        if luminance == 100:
            issues.append(f"pure white oklch(100 ...)")
    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate dark mode token completeness")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    args = parser.parse_args()

    if not STYLES_CSS.exists():
        print(f"[ERROR] styles.css 不存在：{STYLES_CSS}")
        return 1

    try:
        css = STYLES_CSS.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        print(f"[ERROR] styles.css 编码失败：{exc}")
        return 1

    # 提取 :root 块
    root_block = extract_block_by_selector(css, ":root")
    if not root_block:
        print("[ERROR] styles.css 缺少 :root 块")
        return 1

    # 提取 [data-theme="dark"] 块
    dark_block = extract_block_by_selector(css, '[data-theme="dark"]')
    if not dark_block:
        print("[ERROR] styles.css 缺少 [data-theme=\"dark\"] 块")
        return 1

    root_vars = extract_vars_from_block(root_block)
    dark_vars = extract_vars_from_block(dark_block)

    errors: list[str] = []
    warnings: list[str] = []

    # ─── 1. Pure black / pure white in dark mode values ───────────────
    dark_lines = dark_block.splitlines()
    for line_no, line in enumerate(dark_lines, 1):
        for m in CSS_VAR_DECL.finditer(line):
            value = m.group(2).strip()
            # Pure black → ERROR
            for pm in PURE_BLACK.finditer(value):
                errors.append(
                    f"[data-theme=\"dark\"] line ~{line_no} {m.group(1)}: "
                    f"pure black oklch found (use warm dark base, not pure black)"
                )
            # Pure white → WARNING
            for pm in PURE_WHITE.finditer(value):
                warnings.append(
                    f"[data-theme=\"dark\"] line ~{line_no} {m.group(1)}: "
                    f"pure white oklch found (dark mode should not have pure white)"
                )

    # ─── 2. Near-zero chroma warm gray check in dark mode ─────────────
    for line_no, line in enumerate(dark_lines, 1):
        for m in OKLCH_COLOR.finditer(line):
            luminance = float(m.group(1))
            chroma = float(m.group(2))
            # L < 20% 且 chroma < 0.005 → 警告（应使用暖灰）
            if luminance < 20 and 0 < chroma < 0.005:
                warnings.append(
                    f"[data-theme=\"dark\"] line ~{line_no}: "
                    f"near-zero chroma ({chroma:.3f}) in dark base — "
                    f"should be warm gray, not neutral gray"
                )

    # ─── 3. Missing dark overrides ────────────────────────────────────
    missing_overrides: list[str] = []
    for name, value in root_vars.items():
        # 跳过排除类别
        if is_excluded_token(name):
            continue
        # 跳过非颜色相关 token
        if not is_color_related_token(name):
            continue
        # 跳过 var() 引用（它们会继承，无需显式覆盖）
        if value.startswith("var("):
            continue
        # 浅色有但暗色无
        if name not in dark_vars:
            missing_overrides.append(name)

    if missing_overrides:
        for name in sorted(missing_overrides)[:10]:
            warnings.append(
                f":root has {name} but [data-theme=\"dark\"] is missing its override"
            )
        if len(missing_overrides) > 10:
            warnings.append(
                f"... 还有 {len(missing_overrides) - 10} 个 missing dark overrides"
            )
    elif args.verbose:
        print("[OK] 所有颜色相关 token 均有暗色覆盖")

    # ─── 4. Orphan dark-only tokens ───────────────────────────────────
    orphan_dark: list[str] = []
    for name in dark_vars:
        if name not in root_vars:
            orphan_dark.append(name)

    if orphan_dark:
        for name in sorted(orphan_dark)[:5]:
            warnings.append(
                f"[data-theme=\"dark\"] has {name} with no :root counterpart (orphan)"
            )
        if len(orphan_dark) > 5:
            warnings.append(
                f"... 还有 {len(orphan_dark) - 5} 个 orphan dark tokens"
            )
    elif args.verbose:
        print("[OK] 无 orphan dark-only tokens")

    # ─── 5. Dark base warm gray check (the specific oklch values) ───────
    # 检查 [data-theme="dark"] 顶部的背景色定义
    dark_bg_pattern = re.compile(
        r"--ds-color-bg\s*:\s*oklch\s*\(\s*([\d.]+)%\s+([\d.]+)\s+([\d.]+)"
    )
    for m in dark_bg_pattern.finditer(dark_block[:500]):  # 只检查前 500 字符
        luminance = float(m.group(1))
        chroma = float(m.group(2))
        if luminance < 30 and chroma < 0.005:
            warnings.append(
                f"[data-theme=\"dark\"] --ds-color-bg uses neutral gray "
                f"oklch({luminance}% {chroma} ...) — should be warm gray"
            )

    # ─── Summary ───────────────────────────────────────────────────────
    print(f"─── 暗色模式检查 ───")
    print(f":root tokens       : {len(root_vars)}")
    print(f"[data-theme=dark]: {len(dark_vars)}")
    print(f"missing overrides : {len(missing_overrides)}")
    print(f"orphan dark tokens: {len(orphan_dark)}")
    print()

    if errors:
        for e in errors:
            print(f"[ERROR] {e}")
    if warnings:
        for w in warnings:
            print(f"[WARN] {w}")

    if not errors and not warnings:
        print("[OK] 暗色模式检查全部通过")
        return 0
    if errors:
        print()
        print(f"错误: {len(errors)}  警告: {len(warnings)}")
        return 1
    # Warnings only
    print()
    print(f"错误: {len(errors)}  警告: {len(warnings)}")
    return 2


if __name__ == "__main__":
    sys.exit(main())
