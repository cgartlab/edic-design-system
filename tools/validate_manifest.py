#!/usr/bin/env python3
"""validate_manifest.py — validate edic-manifest.json integrity.

Exit codes:
  0 = pass
  1 = blocking error (missing file, version mismatch, invalid structure)
  2 = warnings only
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "edic-manifest.json"
VERSION_FILE = ROOT / "VERSION"

REQUIRED_SECTIONS = {
    "$schema",
    "name",
    "version",
    "description",
    "philosophy",
    "deliverables",
    "token",
    "components",
    "icons",
    "constraints",
    "validators",
    "audit",
}

REQUIRED_TOKEN_KEYS = {"prefix", "semanticPrefix", "categories", "rules"}
REQUIRED_COMPONENT_KEYS = {"prefix", "modifierPattern", "core", "rules"}
REQUIRED_ICON_KEYS = {"count", "sprite", "source", "viewBox", "strokeWidth", "naming", "rules"}

CSS_VAR_CATEGORY_RE = re.compile(r"^[a-z][a-z0-9-]*$")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if not MANIFEST.exists():
        print(f"[ERROR] {MANIFEST} 不存在")
        return 1
    if not VERSION_FILE.exists():
        print(f"[ERROR] {VERSION_FILE} 不存在")
        return 1

    expected_version = VERSION_FILE.read_text(encoding="utf-8").strip().splitlines()[0].strip()
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[ERROR] edic-manifest.json JSON 解析失败：{exc}")
        return 1

    missing_sections = sorted(REQUIRED_SECTIONS - set(data))
    if missing_sections:
        errors.append(f"缺少必需字段: {', '.join(missing_sections)}")

    if data.get("version") != expected_version:
        errors.append(
            f"version={data.get('version')!r}，与 VERSION {expected_version!r} 不一致"
        )

    for name in (data.get("deliverables") or {}).keys():
        path = ROOT / name
        if not path.exists():
            errors.append(f"deliverables 引用的文件不存在: {name}")

    for name in (data.get("validators") or []):
        path = ROOT / "tools" / name
        if not path.exists():
            errors.append(f"validators 引用的脚本不存在: tools/{name}")

    token = data.get("token") or {}
    if not REQUIRED_TOKEN_KEYS <= set(token):
        errors.append("token 段缺少必要键 (prefix/semanticPrefix/categories/rules)")
    for category in token.get("categories", []):
        if not CSS_VAR_CATEGORY_RE.match(str(category)):
            warnings.append(f"token 类别命名不规范: {category!r}")

    components = data.get("components") or {}
    if not REQUIRED_COMPONENT_KEYS <= set(components):
        errors.append("components 段缺少必要键 (prefix/modifierPattern/core/rules)")

    icons = data.get("icons") or {}
    if not REQUIRED_ICON_KEYS <= set(icons):
        errors.append("icons 段缺少必要键")
    else:
        sprite = ROOT / icons.get("sprite", "")
        if not sprite.exists():
            errors.append(f"icons.sprite 不存在: {sprite}")
    if not isinstance(icons.get("count"), int) or icons["count"] < 0:
        errors.append(f"icons.count 非法: {icons.get('count')!r}")
    manifest_icon_path = ROOT / "icons.json"
    if manifest_icon_path.exists():
        try:
            icon_manifest = json.loads(manifest_icon_path.read_text(encoding="utf-8"))
            icon_count = len(icon_manifest.get("icons", [])) if isinstance(icon_manifest.get("icons"), list) else 0
            sprite_symbol_count = len(re.findall(r"<symbol\s+id=\"[^\"]+\"", (ROOT / icons.get("sprite", "icons.svg")).read_text(encoding="utf-8"))) if (ROOT / icons.get("sprite", "icons.svg")).exists() else 0
            if icon_count != icons.get("count"):
                errors.append(f"edic-manifest.json icons.count={icons.get('count')}，与 icons.json {icon_count} 不一致")
            if sprite_symbol_count != icons.get("count"):
                errors.append(f"edic-manifest.json icons.count={icons.get('count')}，与 icons.svg {sprite_symbol_count} 不一致")
        except json.JSONDecodeError as exc:
            errors.append(f"icons.json JSON 解析失败：{exc}")

    print("─── edic-manifest.json 校验 ───")
    print(f"期望版本: {expected_version}")
    print(f"manifest 版本: {data.get('version')!r}")
    print(f"组件清单: {len((data.get('components') or {}).get('core', []))} 项")
    print(f"图标数量声明: {(data.get('icons') or {}).get('count', 'N/A')}")
    if (ROOT / "icons.json").exists():
        icon_manifest = json.loads((ROOT / "icons.json").read_text(encoding="utf-8"))
        print(f"icons.json: {len(icon_manifest.get('icons', []))} 条索引")
    print()

    for message in errors:
        print(f"[ERROR] {message}")
    for message in warnings:
        print(f"[WARN] {message}")

    if not errors and not warnings:
        print("[OK] manifest 结构完整且引用有效")

    print()
    print(f"错误: {len(errors)}  警告: {len(warnings)}")
    if errors:
        return 1
    if warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
