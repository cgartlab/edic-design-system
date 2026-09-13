#!/usr/bin/env python3
"""validate_manifest_css.py — 校验 edic-manifest.json 中 components.core 每项在 styles.css 中有对应 CSS 类。

Exit codes:
  0 = pass
  1 = blocking error (component in manifest has no CSS class in styles.css)
  2 = warnings only
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "edic-manifest.json"
STYLES = ROOT / "styles.css"


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not MANIFEST.exists():
        print(f"[ERROR] {MANIFEST} 不存在")
        return 1
    if not STYLES.exists():
        print(f"[ERROR] {STYLES} 不存在")
        return 1

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[ERROR] edic-manifest.json JSON 解析失败: {exc}")
        return 1

    css_text = STYLES.read_text(encoding="utf-8", errors="replace")

    components_section = manifest.get("components") or {}
    core_list = components_section.get("core") or []
    prefix = components_section.get("prefix", "ds-")

    if not core_list:
        print("[WARN] manifest components.core 为空")
        return 2

    missing = []
    found = 0
    for component_name in core_list:
        css_class = f"{prefix}{component_name}"
        # Check if the CSS class exists as a selector in styles.css
        pattern = re.compile(r"[.#]" + re.escape(css_class) + r"(?:\b|[-:])")
        if pattern.search(css_text):
            found += 1
        else:
            missing.append(css_class)

    print("─── manifest ↔ CSS 组件校验 ───")
    print(f"manifest 核心组件: {len(core_list)} 项")
    print(f"styles.css 中找到: {found} 项")
    print(f"缺失: {len(missing)} 项")

    if missing:
        for cls in missing:
            print(f"[ERROR] manifest 声明但 styles.css 无 CSS 类: {cls}")
        errors.append(f"{len(missing)} 个 manifest 组件在 styles.css 中缺少 CSS 实现")

    if not errors and not warnings:
        print("[OK] 所有 manifest 核心组件在 styles.css 中都有 CSS 类定义")

    print()
    print(f"错误: {len(errors)}  警告: {len(warnings)}")
    if errors:
        return 1
    if warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
