#!/usr/bin/env python3
"""validate_components.py - EDIC 2.0 component example coverage.

Exit codes:
  0 = pass
  1 = blocking error (missing example pages or required accessibility metadata)
  2 = warnings only
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
EXAMPLES_DIR = ROOT / "examples" / "components"
STYLES = ROOT / "styles.css"


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not EXAMPLES_DIR.exists():
        errors.append(f"缺少组件示例目录: {EXAMPLES_DIR.relative_to(ROOT)}")
        examples = []
    else:
        examples = sorted(EXAMPLES_DIR.glob("*.html"))

    if not examples:
        errors.append("examples/components/ 下没有 .html 示例页")

    if not STYLES.exists():
        errors.append("缺少 styles.css")
        styles = ""
    else:
        styles = STYLES.read_text(encoding="utf-8")

    for path in examples:
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = path.relative_to(ROOT)

        if not re.search(r"<h1\b", text, re.I):
            errors.append(f"{rel}: 缺少 <h1>")
        if not re.search(r'<main\b', text, re.I):
            errors.append(f"{rel}: 缺少 <main>")
        if "styles.css?v=" not in text:
            errors.append(f"{rel}: 未链接 styles.css?v=...")

        aria_signals = ("aria-", "role=")
        if not any(signal in text for signal in aria_signals):
            errors.append(f"{rel}: 缺少 ARIA role/state 或 aria-* 属性")

        keyboard_signals = ("aria-current", "tabindex", "焦点", "键盘", "keyboard", "aria-expanded")
        if not any(signal in text for signal in keyboard_signals):
            errors.append(f"{rel}: 缺少键盘行为、焦点或展开状态说明/属性")

        if not re.search(r"<code\b", text, re.I):
            errors.append(f"{rel}: 缺少可复制/可审阅的 ds-* class 代码片段")

        if "[data-theme=\"dark\"]" in text or "[data-theme=dark]" in text:
            has_dark_scope = True
        elif styles and "[data-theme=\"dark\"]" in styles:
            has_dark_scope = True
        else:
            has_dark_scope = False
        if not has_dark_scope:
            warnings.append(f"{rel}: 未发现暗色模式 scope，确认 styles.css 已覆盖 [data-theme=\"dark\"]")

    print("─── EDIC 组件示例校验 ───")
    print(f"扫描示例页: {len(examples)} 个")

    for message in errors:
        print(f"[ERROR] {message}")
    for message in warnings:
        print(f"[WARN] {message}")

    if not errors and not warnings:
        print("[OK] 组件示例、ARIA、键盘与暗色覆盖信号齐全")

    print()
    print(f"错误: {len(errors)}  警告: {len(warnings)}")
    if errors:
        return 1
    if warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
