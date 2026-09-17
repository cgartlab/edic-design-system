#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_icons.py — 从 scripts.js 提取 ICONS 数组并生成 SVG sprite

目的：兑现 handbook.html 第 5 章"配套生成 icons.svg"的承诺。
scripts.js 的 ICONS 数组是单一真相源；本脚本读取它，
输出一个可独立引用的 SVG sprite（icons.svg）。

输出文件 icons.svg 用途：
  - Penpot 直接导入（每个 <symbol> 是独立图形）
  - 外部 HTML 通过 <svg><use href="icons.svg#archive"/></svg> 引用
  - 设计师逐枚复制 SVG 源码

icons.svg 应当被 commit 到仓库（GitHub Pages 静态托管）。

退出码：
  0  成功（生成或 --check 模式下已同步）
  1  错误（解析失败、I/O 错误等）
  2  --check/--diff 模式下 icons.svg 与 ICONS 不同步

用法：
  python3 tools/generate_icons.py           # 生成 icons.svg
  python3 tools/generate_icons.py --check   # 检查模式（CI 用）
  python3 tools/generate_icons.py --diff    # 显示差异预览（不修改文件）
"""
from __future__ import annotations

import argparse
import re
import sys
import json
import os
from collections import Counter
from difflib import unified_diff
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")
SCRIPTS_JS = ROOT / "scripts.js"
ICONS_SVG = ROOT / "icons.svg"
ICONS_JSON = ROOT / "icons.json"

# 匹配 ICONS 数组的起止（DOTALL 让 . 能跨行匹配 svg 字符串内的换行）
ICONS_ARRAY_RE = re.compile(
    r"const\s+ICONS\s*=\s*\[(.*?)\];",
    re.DOTALL,
)

# 匹配单个条目：{id:"X",svg:'<svg ...>...</svg>'}
# id 约束：小写字母/数字/连字符（与已有数据一致）
# svg 约束：以单引号包裹；非贪婪匹配首个 </svg>
ICON_ENTRY_RE = re.compile(
    r"\{\s*id\s*:\s*\"(?P<id>[a-z0-9-]+)\""
    r"\s*,\s*"
    r"svg\s*:\s*'(?P<svg><svg[^>]*>.*?</svg>)'"
    r"\s*\}",
    re.DOTALL,
)

# 提取 viewBox 属性
VIEWBOX_RE = re.compile(r'viewBox\s*=\s*"([^"]*)"')

# 用于 strip 外层 <svg> 标签
SVG_OPEN_RE = re.compile(r"^<svg[^>]*>")
SVG_CLOSE_RE = re.compile(r"</svg>\s*$")


def extract_icons(scripts_text: str) -> list[dict]:
    """从 scripts.js 文本中提取 ICONS 数组的所有条目。

    Returns:
        [{"id": "archive", "svg": "<svg ...>...</svg>"}, ...]

    Raises:
        ValueError: ICONS 数组未找到、为空或条目解析失败
    """
    match = ICONS_ARRAY_RE.search(scripts_text)
    if not match:
        raise ValueError("未在 scripts.js 中找到 'const ICONS = [...]' 数组")

    array_body = match.group(1)
    icons: list[dict] = []
    for m in ICON_ENTRY_RE.finditer(array_body):
        icons.append({
            "id": m.group("id"),
            "svg": m.group("svg"),
        })

    if not icons:
        raise ValueError("ICONS 数组为空或所有条目解析失败")

    # 校验 ID 唯一性
    ids = [ic["id"] for ic in icons]
    dupes = [k for k, v in Counter(ids).items() if v > 1]
    if dupes:
        raise ValueError(f"ICONS 数组存在重复 ID: {dupes}")

    return icons


def icon_category(icon_id: str) -> str:
    id_ = icon_id.lower()
    if id_.startswith(("arrow-", "chevron-", "navigation", "menu", "grid", "sidebar", "list")):
        return "nav"
    if id_ in {"check", "x", "plus", "minus", "search", "filter", "edit", "trash", "download", "upload", "copy", "save"}:
        return "action"
    if id_ in {"bell", "star", "bookmark", "heart", "flag", "alert", "info", "help", "warning", "success", "error", "circle", "square", "dot"}:
        return "status"
    if id_ in {"calendar", "clock", "user", "users", "mail", "phone", "message", "send", "share", "at-sign", "globe"}:
        return "communication"
    if id_ in {"camera", "image", "video", "play", "pause", "music", "speaker", "headphones", "zoom-in", "zoom-out", "maximize", "minimize"}:
        return "media"
    if id_ in {"bar-chart", "pie-chart", "activity", "trending-up", "trending-down", "database", "server", "code", "terminal", "cpu", "wifi"}:
        return "data"
    if id_ in {"archive", "box", "briefcase", "credit-card", "shopping-cart", "shopping-bag", "package", "gift", "dollar-sign", "tag"}:
        return "commerce"
    if id_ in {"home", "map-pin", "map", "compass", "book", "file", "folder", "layers", "settings", "tool", "trash"}:
        return "system"
    return "action"


def icon_keywords(icon_id: str) -> list[str]:
    words = icon_id.replace("-", " ").split()
    aliases = {"user": "profile", "mail": "email", "phone": "call", "map": "location"}
    return words + [aliases[word] for word in words if word in aliases]


def build_icon_manifest(icons: list[dict]) -> str:
    # 版本单一来源：VERSION 文件（此前硬编码 2.0.0，发布后会导致 icons.json 版本回退）
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip() or "0.0.0"
    payload = {
        "version": version,
        "source": "scripts.js ICONS array",
        "sprite": "icons.svg",
        "naming": {
            "legacy": "{name}-{variant}",
            "v2": "{category}-{name}-{style}",
            "style": "outline",
        },
        "icons": [
            {
                "name": icon["id"],
                "category": icon_category(icon["id"]),
                "style": "outline",
                "viewBox": "0 0 24 24",
                "keywords": icon_keywords(icon["id"]),
                "aliases": [],
                "deprecated": False,
            }
            for icon in icons
        ],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2) + "\n"


def build_symbol(icon_id: str, svg: str) -> str:
    """将 <svg viewBox="...">CONTENT</svg> 转换为带 presentation attributes 的 <symbol>。

    所有图标源 SVG 均为纯几何元素（line / polyline / path），不携带任何
    stroke / fill 属性。SVG 规范默认值是 fill="black" stroke="none"，
    因此在没有外部 CSS 的环境下（Penpot 导入、<use> 裸引用等）：
      - line / polyline 元素因 stroke:none 完全不可见
      - path 元素因 fill:black 渲染为填充色块而非描边线条

    修复方式（与 Feather Icons / Lucide 标准一致）：
      在 <symbol> 元素本身注入 presentation attributes，
      子元素通过 SVG 继承机制自动获得这些默认值；
      外部 CSS（如 .ds-icon-box svg）仍可通过 currentColor 覆盖颜色，
      行为与修复前完全向后兼容。
    """
    vb_match = VIEWBOX_RE.search(svg)
    viewbox = vb_match.group(1) if vb_match else "0 0 24 24"
    content = SVG_OPEN_RE.sub("", svg)
    content = SVG_CLOSE_RE.sub("", content)
    return (
        f'<symbol id="{icon_id}" viewBox="{viewbox}"'
        f' stroke="currentColor" fill="none"'
        f' stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"'
        f'>{content}</symbol>'
    )


def build_sprite(icons: list[dict]) -> str:
    """构造完整的 SVG sprite 字符串。"""
    symbols = "\n  ".join(
        build_symbol(icon["id"], icon["svg"])
        for icon in icons
    )

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<!--
  icons.svg — EDIC Design System 图标 sprite
  {len(icons)} 枚线性 SVG 图标（24×24 viewBox），可独立引用。

  ⚠ 由 tools/generate_icons.py 从 scripts.js 的 ICONS 数组自动生成。
  ⚠ 请勿手动编辑；修改图标请改 scripts.js，然后跑 `make icons`。
  ⚠ 验证同步：跑 `make icons-check`（CI 用）。

  每个 <symbol> 携带 presentation attributes（stroke="currentColor" fill="none"
  stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"），
  无需外部 CSS 即可正确渲染线性图标；颜色通过 currentColor 继承父级。

  用法：
    <svg width="24" height="24"><use href="icons.svg#archive"/></svg>

  导入 Penpot：将本文件拖入设计稿即可（每个 <symbol> 是一枚独立图形）。
-->
<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">
  {symbols}
</svg>
'''


def main() -> int:
    parser = argparse.ArgumentParser(
        description="从 scripts.js 的 ICONS 数组生成 icons.svg sprite",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="检查模式：仅校验 icons.svg 是否与 ICONS 同步（CI 用，0=同步 / 2=不同步）",
    )
    parser.add_argument(
        "--diff",
        action="store_true",
        help="diff 模式：若不同步则打印差异预览（不修改文件）",
    )
    args = parser.parse_args()

    if not SCRIPTS_JS.exists():
        print(f"[ERROR] scripts.js 不存在: {SCRIPTS_JS}")
        return 1

    print("─── icons.svg 生成 ───")
    scripts_text = SCRIPTS_JS.read_text(encoding="utf-8")

    try:
        icons = extract_icons(scripts_text)
    except ValueError as e:
        print(f"[ERROR] {e}")
        return 1

    # 预览：首 3 + 末 3 个 ID
    head_ids = ", ".join(ic["id"] for ic in icons[:3])
    tail_ids = ", ".join(ic["id"] for ic in icons[-3:])
    print(f"scripts.js ICONS 数组: {len(icons)} 个图标（{head_ids} ... {tail_ids}）")

    sprite = build_sprite(icons)
    icon_manifest = build_icon_manifest(icons)

    if args.check or args.diff:
        if not ICONS_SVG.exists():
            print(f"[ERROR] icons.svg 不存在，需运行生成: {ICONS_SVG}")
            return 2
        if not ICONS_JSON.exists():
            print(f"[ERROR] icons.json 不存在，需运行生成: {ICONS_JSON}")
            return 2
        existing = ICONS_SVG.read_text(encoding="utf-8")
        existing_manifest = ICONS_JSON.read_text(encoding="utf-8")
        if existing == sprite:
            if existing_manifest == icon_manifest:
                print(f"icons.svg: 已同步（{len(icons)} 个 <symbol>）")
                return 0
        print(f"[ERROR] icons.svg/icons.json 与 ICONS 不同步（{len(icons)} 个图标）")
        if args.diff:
            diff = unified_diff(
                existing.splitlines(keepends=True),
                sprite.splitlines(keepends=True),
                fromfile="icons.svg (current)",
                tofile="icons.svg (expected)",
                n=2,
            )
            sys.stdout.writelines(diff)
            diff = unified_diff(
                existing_manifest.splitlines(keepends=True),
                icon_manifest.splitlines(keepends=True),
                fromfile="icons.json (current)",
                tofile="icons.json (expected)",
                n=2,
            )
            sys.stdout.writelines(diff)
        return 2

    # 生成模式
    ICONS_SVG.write_text(sprite, encoding="utf-8")
    ICONS_JSON.write_text(icon_manifest, encoding="utf-8")
    print(f"✓ 已生成 {ICONS_SVG.relative_to(ROOT)}（{len(icons)} 个 <symbol>）")
    print(f"✓ 已生成 {ICONS_JSON.relative_to(ROOT)}（{len(icons)} 条索引）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
