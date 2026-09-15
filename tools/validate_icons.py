#!/usr/bin/env python3
"""validate_icons.py — validate icons.json against scripts.js and icons.svg.

Exit codes:
  0 = pass
  1 = blocking error
  2 = warnings only
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ICONS_JSON = ROOT / "icons.json"
ICONS_SVG = ROOT / "icons.svg"
SCRIPTS_JS = ROOT / "scripts.js"
VERSION_FILE = ROOT / "VERSION"

ICONS_ARRAY_RE = re.compile(r"const\s+ICONS\s*=\s*\[(.*?)\];", re.DOTALL)
ICON_ENTRY_RE = re.compile(r"\{\s*id\s*:\s*\"(?P<id>[a-z0-9-]+)\"", re.DOTALL)


def extract_scripts_icons() -> list[str]:
    text = SCRIPTS_JS.read_text(encoding="utf-8")
    match = ICONS_ARRAY_RE.search(text)
    if not match:
        raise ValueError("scripts.js 缺少 ICONS 数组")
    return [match.group("id") for match in ICON_ENTRY_RE.finditer(match.group(1))]


def main() -> int:
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    errors: list[str] = []
    warnings: list[str] = []

    for path in (ICONS_JSON, ICONS_SVG, SCRIPTS_JS, VERSION_FILE):
        if not path.exists():
            errors.append(f"缺少文件: {path.relative_to(ROOT)}")
    if errors:
        print("─── icons.json 校验 ───")
        for message in errors:
            print(f"[ERROR] {message}")
        return 1

    try:
        manifest = json.loads(ICONS_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"[ERROR] icons.json JSON 解析失败：{exc}")
        return 1

    icons = manifest.get("icons")
    if not isinstance(icons, list) or not icons:
        errors.append("icons.json 缺少非空 icons 数组")
        icons = []

    version = manifest.get("version")
    expected_version = VERSION_FILE.read_text(encoding="utf-8").strip().splitlines()[0].strip()
    if version != expected_version:
        errors.append(f"icons.json version={version!r}，与 VERSION {expected_version!r} 不一致")

    names = [icon.get("name") for icon in icons]
    duplicates = [name for name, count in Counter(names).items() if count and count > 1]
    if duplicates:
        errors.append(f"icons.json 存在重复图标: {', '.join(duplicates[:10])}")

    for index, icon in enumerate(icons):
        required = {"name", "category", "style", "viewBox", "keywords", "aliases", "deprecated"}
        missing = sorted(required - set(icon))
        if missing:
            errors.append(f"icons.json[{index}] 缺少字段: {', '.join(missing)}")
        if icon.get("viewBox") != "0 0 24 24":
            errors.append(f"icons.json[{index}] viewBox 必须是 0 0 24 24")
        if not isinstance(icon.get("keywords"), list):
            errors.append(f"icons.json[{index}].keywords 必须是数组")

    script_ids = extract_scripts_icons()
    json_names = [name for name in names if name]
    svg_symbols = re.findall(r"<symbol\s+id=\"([^\"]+)\"", ICONS_SVG.read_text(encoding="utf-8"))

    if len(script_ids) != len(json_names):
        errors.append(f"scripts.js ICONS 数量 {len(script_ids)} 与 icons.json 数量 {len(json_names)} 不一致")
    if len(svg_symbols) != len(json_names):
        errors.append(f"icons.svg symbol 数量 {len(svg_symbols)} 与 icons.json 数量 {len(json_names)} 不一致")
    if set(script_ids) != set(json_names):
        errors.append("scripts.js ICONS 与 icons.json name 集合不一致")
    if set(svg_symbols) != set(json_names):
        errors.append("icons.svg symbol 与 icons.json name 集合不一致")

    if manifest.get("sprite") != "icons.svg":
        warnings.append("icons.json sprite 应指向 icons.svg")
    if manifest.get("source") != "scripts.js ICONS array":
        warnings.append("icons.json source 应声明为 scripts.js ICONS array")

    print("─── icons.json 校验 ───")
    print(f"脚本图标: {len(script_ids)}")
    print(f"JSON 索引: {len(json_names)}")
    print(f"SVG symbol: {len(svg_symbols)}")

    for message in errors:
        print(f"[ERROR] {message}")
    for message in warnings:
        print(f"[WARN] {message}")
    if not errors and not warnings:
        print("[OK] icons.json / icons.svg / scripts.js 三者一致")
    print()
    print(f"错误: {len(errors)}  警告: {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
