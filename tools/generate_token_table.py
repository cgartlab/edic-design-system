#!/usr/bin/env python3
"""generate_token_table.py — 从 styles.css 生成 docs.html 令牌表的完整数据。

单一真源：styles.css 的 `:root` 与 `[data-theme="dark"]`。
输出：scripts.js 中 `TOKEN_TABLE_DATA` 常量（浅色值 + 暗色覆盖 + 是否有暗色差异）。

为什么不用 tokens.json：
  - tokens.json 只有 64 个条目带 `dark` 字段，其余暗色值以独立
    `-dark` 后缀 token 形式存在（非标准表示，易与真源漂移）
  - styles.css 是浏览器实际执行的真源

用法：
  python3 tools/generate_token_table.py           # 写入 scripts.js
  python3 tools/generate_token_table.py --check   # 仅检查是否与 CSS 同步（CI 用）
  python3 tools/generate_token_table.py --diff    # 打印将要变更的内容

退出码：0 = 成功/已同步，1 = 检查失败（--check 模式下不同步）
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLES_CSS = ROOT / "styles.css"
SCRIPTS_JS = ROOT / "scripts.js"

# --ds-xxx: value;
# Value may contain nested functions (rgba/oklch inside gradient), quoted strings,
# and commas. Semicolons inside parens/quotes are tolerated; only a top-level ';'
# terminates. Scanned in code because CSS nesting depth is unbounded.
CSS_VAR_START = re.compile(r"(--ds-[\w-]+)\s*:\s*")


def iter_var_decls(block: str):
    """Yield (name, value) for each top-level --ds-* declaration in a CSS block.

    Walks the text tracking paren depth and quote state, so values containing
    nested functions (e.g. radial-gradient(..., oklch(...) ...)) or semicolons
    inside strings are captured intact.
    """
    pos = 0
    n = len(block)
    while pos < n:
        m = CSS_VAR_START.search(block, pos)
        if not m:
            return
        name = m.group(1)
        i = m.end()
        depth = 0
        quote = ""
        buf_start = i
        while i < n:
            ch = block[i]
            if quote:
                if ch == quote and block[i - 1] != "\\":
                    quote = ""
            elif ch in "\"'":
                quote = ch
            elif ch == "(":
                depth += 1
            elif ch == ")":
                if depth > 0:
                    depth -= 1
            elif ch == ";" and depth == 0:
                break
            elif ch == "}" and depth == 0:
                break
            i += 1
        value = " ".join(block[buf_start:i].split())
        if value:
            yield name, value
        pos = i + 1 if i < n and block[i] == ";" else i + 1

BEGIN_MARKER = "/* @generated:token-table:begin — 由 tools/generate_token_table.py 生成，勿手改 */"
END_MARKER = "/* @generated:token-table:end */"


def extract_block(css: str, selector: str) -> str:
    """按大括号深度提取 selector 的规则块内容（支持嵌套 @media）。"""
    idx = 0
    while True:
        pos = css.find(selector, idx)
        if pos == -1:
            return ""
        if pos > 0 and (css[pos - 1].isalnum() or css[pos - 1] == "-"):
            idx = pos + 1
            continue
        rest = css[pos + len(selector):]
        brace = rest.find("{")
        if brace == -1:
            return ""
        # 确保选择器与 { 之间只有空白
        between = rest[:brace].strip()
        if between:
            idx = pos + 1
            continue
        block_start = pos + len(selector) + brace + 1
        depth = 1
        i = block_start
        while i < len(css) and depth > 0:
            if css[i] == "{":
                depth += 1
            elif css[i] == "}":
                depth -= 1
            i += 1
        if depth == 0:
            return css[block_start:i - 1]
        return ""


def extract_vars(block: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for name, value in iter_var_decls(block):
        out[name] = value
    return out


def build_table() -> list[list[str]]:
    """返回 [name, light, dark] 三元组列表，按 :root 声明顺序。

    dark 为空字符串表示该 token 在暗色模式下无覆盖（值沿用浅色）。
    """
    css = STYLES_CSS.read_text(encoding="utf-8")

    # :root 可能出现在多处（主定义 + 后置补充）。后出现的覆盖前者，与 CSS 级联
    # 语义一致；但重复定义通常是合并残留，因此显式告警而不是静默覆盖。
    root_vars: dict[str, str] = {}
    seen_in: dict[str, int] = {}
    for m in re.finditer(r":root\s*\{", css):
        # 排除 :root 作为后代选择器一部分的情况
        line_start = css.rfind("\n", 0, m.start()) + 1
        if css[line_start:m.start()].strip():
            continue
        line_no = css.count("\n", 0, m.start()) + 1
        block = extract_block(css[m.start():], ":root")
        for k, v in extract_vars(block).items():
            if k in seen_in:
                print(
                    f"[WARN] {k} 重复定义：:root 第 {seen_in[k]} 行与第 {line_no} 行，"
                    f"采用后者（CSS 级联语义）",
                    file=sys.stderr,
                )
            seen_in[k] = line_no
            root_vars[k] = v

    dark_vars: dict[str, str] = {}
    for m in re.finditer(r'\[data-theme="dark"\]\s*\{', css):
        line_start = css.rfind("\n", 0, m.start()) + 1
        if css[line_start:m.start()].strip():
            continue
        block = extract_block(css[m.start():], '[data-theme="dark"]')
        dark_vars.update(extract_vars(block))

    rows: list[list[str]] = []
    for name, light in root_vars.items():
        dark = dark_vars.get(name, "")
        rows.append([name, light, dark])
    return rows


def render_js(rows: list[list[str]]) -> str:
    """生成写入 scripts.js 的 JS 代码块。"""
    payload = json.dumps(rows, ensure_ascii=False, separators=(",", ":"))
    return (
        f"{BEGIN_MARKER}\n"
        f"const TOKEN_TABLE_DATA = {payload};\n"
        f"{END_MARKER}"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="从 styles.css 生成令牌表数据")
    ap.add_argument("--check", action="store_true", help="仅校验 scripts.js 是否与 styles.css 同步")
    ap.add_argument("--diff", action="store_true", help="打印将要写入的内容摘要")
    args = ap.parse_args()

    rows = build_table()
    if not rows:
        print("[ERROR] 未能从 styles.css 提取到任何 token", file=sys.stderr)
        return 1

    themed = sum(1 for r in rows if r[2])
    generated = render_js(rows)

    js = SCRIPTS_JS.read_text(encoding="utf-8")

    if BEGIN_MARKER in js and END_MARKER in js:
        start = js.index(BEGIN_MARKER)
        end = js.index(END_MARKER) + len(END_MARKER)
        current = js[start:end]
    else:
        current = ""

    if args.check:
        if current == generated:
            print(f"[OK] 令牌表已同步（{len(rows)} 个 token，{themed} 个有暗色覆盖）")
            return 0
        print("[ERROR] 令牌表与 styles.css 不同步，请运行：python3 tools/generate_token_table.py", file=sys.stderr)
        return 1

    if args.diff:
        print(f"token 总数: {len(rows)}")
        print(f"有暗色覆盖: {themed}")
        print(f"仅浅色: {len(rows) - themed}")
        return 0

    if current == generated:
        print(f"[OK] 无需更新（{len(rows)} 个 token，{themed} 个有暗色覆盖）")
        return 0

    if current:
        js = js[:start] + generated + js[end:]
    else:
        # 首次插入：放在 TOKENS 常量之后
        anchor = "const TOKENS = ["
        aidx = js.find(anchor)
        if aidx == -1:
            print("[ERROR] scripts.js 中未找到锚点 const TOKENS", file=sys.stderr)
            return 1
        # 找到 TOKENS 数组结束
        close = js.find("\n];", aidx)
        if close == -1:
            print("[ERROR] 未找到 TOKENS 数组结尾", file=sys.stderr)
            return 1
        insert_at = close + 3
        js = js[:insert_at] + "\n\n" + generated + js[insert_at:]

    SCRIPTS_JS.write_text(js, encoding="utf-8", newline="")
    print(f"[OK] 已更新 scripts.js（{len(rows)} 个 token，{themed} 个有暗色覆盖）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
