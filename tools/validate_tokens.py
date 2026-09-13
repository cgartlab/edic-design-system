#!/usr/bin/env python3
"""validate_tokens.py — 校验 tokens.json 与 styles.css 的一致性

设计原则：
  • ERRORS（阻塞 CI）— 真正的不一致
  • WARNINGS（不阻塞）— 已知合理的不匹配 / 提示性信息
  • 退出码：0 = 通过 / 1 = 有错误

检查项（按严重度分级）：
  ERRORS:
    - tokens.json 无法解析
    - styles.css 缺少 :root 块
    - styles.css 中存在明显非 OKLch 颜色（hex / rgb / hsl）

  WARNINGS:
    - tokens.json 定义但 styles.css :root 缺少（可能 token 在组件局部定义）
    - styles.css :root 颜色 token 在 tokens.json 缺失
    - 暗色块有但浅色块无对应的孤立变量
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS_JSON = ROOT / "tokens.json"
STYLES_CSS = ROOT / "styles.css"

CSS_VAR_DECL = re.compile(r"--ds-([a-z0-9-]+)\s*:\s*([^;]+);")
HEX_COLOR = re.compile(r"#[0-9a-fA-F]{3,8}\b")
RGB_COLOR = re.compile(r"\brgb[a]?\s*\(", re.IGNORECASE)
HSL_COLOR = re.compile(r"\bhsl[a]?\s*\(", re.IGNORECASE)


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
        # Find next occurrence of selector
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
        # Make sure there's no closing brace before it (shouldn't happen for valid match)
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
        name = "--ds-" + match.group(1)
        value = match.group(2).strip()
        vars_[name] = value
    return vars_


def extract_vars_from_json(data: dict) -> dict[str, str]:
    """从 tokens.json v2 或 v1 结构提取 token 名 → 值。"""
    out = {}
    tokens = data.get("tokens", data.get("_legacyTokens", {}))

    if isinstance(tokens, list):
        for token in tokens:
            if isinstance(token, dict) and token.get("name") and token.get("value") is not None:
                out["--ds-" + str(token["name"])] = str(token["value"])
        return out

    if not isinstance(tokens, dict):
        return out

    def walk(node: dict, prefix: str = "") -> None:
        for key, val in node.items():
            path = f"{prefix}{key}" if not prefix else f"{prefix}-{key}"
            if isinstance(val, dict):
                walk(val, path)
            elif isinstance(val, str):
                out["--ds-" + path] = val
            elif isinstance(val, list):
                out["--ds-" + path] = " · ".join(val)
            elif isinstance(val, (int, float)):
                out["--ds-" + path] = str(val)

    walk(tokens)
    return out


def is_color_token(name: str) -> bool:
    """判断是否是颜色类 token。"""
    return (
        name.startswith("--ds-color-")
        or "-bg" in name
        or name.endswith("-color")
    )


def main() -> int:
    # ─── 严重错误检查 ─────────────────────────────────────
    if not TOKENS_JSON.exists():
        print(f"[ERROR] tokens.json 不存在：{TOKENS_JSON}")
        return 1
    if not STYLES_CSS.exists():
        print(f"[ERROR] styles.css 不存在：{STYLES_CSS}")
        return 1

    try:
        with TOKENS_JSON.open(encoding="utf-8-sig") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        print(f"[ERROR] tokens.json JSON 解析失败：{exc}")
        return 1

    try:
        css = STYLES_CSS.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        print(f"[ERROR] styles.css 编码失败：{exc}")
        return 1

    json_tokens = extract_vars_from_json(data)
    root_vars_raw = extract_block_by_selector(css, ":root")
    dark_vars_raw = extract_block_by_selector(css, '[data-theme="dark"]')

    if not root_vars_raw:
        print("[ERROR] styles.css 缺少 :root 块")
        return 1

    root_vars = extract_vars_from_block(root_vars_raw)
    dark_vars = extract_vars_from_block(dark_vars_raw) if dark_vars_raw else {}

    has_error = False
    warning_count = 0

    # ─── 严重错误：旧格式颜色 ────────────────────────────
    hex_hits = list(HEX_COLOR.finditer(css))
    rgb_hits = list(RGB_COLOR.finditer(css))
    hsl_hits = list(HSL_COLOR.finditer(css))

    if hex_hits:
        for match in hex_hits[:3]:
            line_no = css[: match.start()].count("\n") + 1
            print(f"[ERROR] styles.css 第 {line_no} 行仍用 hex 颜色：{match.group()}")
            has_error = True
        if len(hex_hits) > 3:
            print(f"[ERROR] ... 还有 {len(hex_hits) - 3} 处 hex 颜色")
            has_error = True
    if rgb_hits:
        for match in rgb_hits[:3]:
            line_no = css[: match.start()].count("\n") + 1
            print(f"[ERROR] styles.css 第 {line_no} 行用 rgb()：{match.group()}")
            has_error = True
    if hsl_hits:
        for match in hsl_hits[:3]:
            line_no = css[: match.start()].count("\n") + 1
            print(f"[ERROR] styles.css 第 {line_no} 行用 hsl()：{match.group()}")
            has_error = True

    if not (hex_hits or rgb_hits or hsl_hits):
        print("[OK] styles.css 全部使用 OKLch 表达颜色")

    # ─── 警告：tokens.json → styles.css 覆盖 ──────────────
    # -dark 后缀的 token 属于 [data-theme="dark"] 块，不在 :root，排除
    missing_in_css = [name for name in json_tokens if name not in root_vars and not name.endswith("-dark")]
    if missing_in_css:
        for name in missing_in_css[:5]:
            print(f"[WARN] tokens.json 定义但 :root 缺少：{name}（可能在组件局部 CSS）")
            warning_count += 1
        if len(missing_in_css) > 5:
            print(f"[WARN] ... 还有 {len(missing_in_css) - 5} 个 token 仅在 JSON 中")
            warning_count += 1
    else:
        print(f"[OK] tokens.json 中 {len(json_tokens)} 个 token 全部出现在 :root")

    # ─── 警告：styles.css → tokens.json 覆盖 ──────────────
    css_color_tokens = [name for name in root_vars if is_color_token(name)]
    missing_in_json = [name for name in css_color_tokens if name not in json_tokens]
    if missing_in_json:
        for name in missing_in_json[:5]:
            print(f"[WARN] styles.css 颜色 token 在 tokens.json 缺失：{name}")
            warning_count += 1
        if len(missing_in_json) > 5:
            print(f"[WARN] ... 还有 {len(missing_in_json) - 5} 个颜色 token 未收录")
            warning_count += 1
    else:
        print(f"[OK] styles.css 中 {len(css_color_tokens)} 个颜色 token 全部在 tokens.json")

    # ─── 警告：暗色 / 浅色孤立 ──────────────────────────
    orphan_dark = [n for n in dark_vars if n not in root_vars]
    if orphan_dark:
        for name in orphan_dark[:3]:
            print(f"[WARN] 暗色定义但浅色无对应：{name}")
            warning_count += 1

    # ─── 总结 ────────────────────────────────────────────
    print()
    print(f"─── 总结 ───")
    print(f"tokens.json  : {len(json_tokens)} 个 token")
    print(f"styles.css   : {len(root_vars)} 个 :root 变量, {len(dark_vars)} 个暗色变量")
    print(f"错误         : {'有' if has_error else '无'}")
    print(f"警告         : {warning_count}")

    return 1 if has_error else 0


if __name__ == "__main__":
    sys.exit(main())
