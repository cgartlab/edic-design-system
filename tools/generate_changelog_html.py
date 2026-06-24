#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/generate_changelog_html.py
从 docs/changelog_human/*.md 自动生成 changelog.html 中的内容块。

工作方式：
  1. 扫描 docs/changelog_human/ 目录，按版本号排序（最新在前）
  2. 将每个 Markdown 文件转换为 changelog.html 中的 <section> 块
  3. 替换 changelog.html 里 <!-- CHANGELOG_CONTENT_START --> 至
     <!-- CHANGELOG_CONTENT_END --> 之间的内容（含侧边导航）

Markdown 文件命名规范：
  vX.Y.Z.md         → 正式版本
  vX.Y.Z-patch.md   → 补丁（用 "-patch" 后缀，不是 semver）

文件第一行可包含日期注释（括号内），例如：
  (2026-06-23)
其余行是 "## 分类" + "- 条目" 形式的 Markdown。

用法：
  python3 tools/generate_changelog_html.py           # 原地更新 changelog.html
  python3 tools/generate_changelog_html.py --check   # 仅检查是否需要更新（CI 用）
  python3 tools/generate_changelog_html.py --dry-run # 打印将要写入的内容，不修改文件

退出码：
  0  成功（--check 模式下：内容已是最新）
  1  错误
  2  --check 模式下：内容需要更新
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import NamedTuple

ROOT = Path(__file__).resolve().parent.parent
CHANGELOG_HTML = ROOT / "changelog.html"
HUMAN_DIR = ROOT / "docs" / "changelog_human"

CONTENT_START = "<!-- CHANGELOG_CONTENT_START -->"
CONTENT_END = "<!-- CHANGELOG_CONTENT_END -->"


class VersionEntry(NamedTuple):
    sort_key: tuple          # 用于排序（倒序：最新在前）
    version_str: str         # 例 "1.8.1" 或 "1.8.1-patch"
    display_version: str     # 例 "v1.8.1" 或 "v1.8.1-patch"
    date: str                # 例 "2026-06-23"，可为空
    anchor: str              # 例 "v181" 或 "v181patch"
    sections: dict           # { "修复": ["…", "…"], "新增": ["…"] }
    path: Path


# ── 版本排序键 ──────────────────────────────────────────────────────────────


def _parse_sort_key(version_str: str) -> tuple:
    """
    将版本字符串转为可排序的元组，确保：
      1.9.0 > 1.8.1 > 1.8.1-patch > 1.8.0
    patch 后缀视为比正版本低一级（用 -0.5 近似）。
    """
    base = version_str.replace("-patch", "")
    parts = base.split(".")
    try:
        nums = tuple(int(p) for p in parts)
    except ValueError:
        nums = (0, 0, 0)
    # patch 后缀让其排在正版本之前（显示时更新的 patch 在上方）
    suffix = 0 if "-patch" not in version_str else -1
    return nums + (suffix,)


# ── Markdown 解析 ─────────────────────────────────────────────────────────────


def _anchor(version_str: str) -> str:
    """把版本字符串转为合法 HTML id（去掉所有非字母数字字符）。"""
    return "v" + re.sub(r"[^a-z0-9]", "", version_str.lower())


def parse_md_file(path: Path) -> VersionEntry:
    """解析单个 docs/changelog_human/*.md 文件，返回 VersionEntry。"""
    stem = path.stem  # 例 "v1.8.1" 或 "v1.8.1-patch"
    version_str = stem.lstrip("v")  # "1.8.1" 或 "1.8.1-patch"
    display_version = "v" + version_str
    anchor = _anchor(version_str)
    sort_key = _parse_sort_key(version_str)

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    date = ""
    start_idx = 0
    if lines and lines[0].strip().startswith("(") and lines[0].strip().endswith(")"):
        date = lines[0].strip().strip("()")
        start_idx = 1

    sections: dict[str, list[str]] = {}
    current_section: str | None = None

    for line in lines[start_idx:]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("## "):
            current_section = stripped[3:].strip()
            sections.setdefault(current_section, [])
        elif stripped.startswith("- ") and current_section is not None:
            sections[current_section].append(stripped[2:])
        elif stripped.startswith("### "):
            # 支持三级标题作为子分类（忽略，并入上个分类）
            pass

    return VersionEntry(
        sort_key=sort_key,
        version_str=version_str,
        display_version=display_version,
        date=date,
        anchor=anchor,
        sections=sections,
        path=path,
    )


# ── HTML 生成 ─────────────────────────────────────────────────────────────────

_SECTION_ORDER = ["新增", "修复", "性能优化", "重构", "变更", "文档", "注意", "其他"]


def _escape(text: str) -> str:
    """最小化 HTML 转义。"""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _render_section(entry: VersionEntry) -> str:
    """渲染单个版本的 <section> HTML 块。"""
    heading_date = f" — {entry.date}" if entry.date else ""
    lines = [
        f'        <section class="ds-doc-block" id="{entry.anchor}">',
        f"          <h2>{_escape(entry.display_version)}{_escape(heading_date)}</h2>",
    ]

    # 按预定顺序输出各分类
    ordered_keys = [k for k in _SECTION_ORDER if k in entry.sections]
    remaining_keys = [k for k in entry.sections if k not in _SECTION_ORDER]
    all_keys = ordered_keys + remaining_keys

    for key in all_keys:
        items = entry.sections[key]
        if not items:
            continue
        lines.append(f"          <h3>{_escape(key)}</h3>")
        lines.append("          <ul>")
        for item in items:
            lines.append(f"            <li>{_escape(item)}</li>")
        lines.append("          </ul>")

    lines.append("        </section>")
    return "\n".join(lines)


def _render_nav_item(entry: VersionEntry, index: int) -> str:
    """渲染侧边导航中的单个 <li> 项。"""
    num = str(index).zfill(2)
    return (
        f'              <li><a class="ds-pagenav-link" href="#{entry.anchor}">'
        f'<span class="ds-pagenav-num">{num}</span>'
        f'<span class="ds-pagenav-text">{_escape(entry.display_version)}</span>'
        f"</a></li>"
    )


def generate_content(entries: list[VersionEntry]) -> str:
    """生成完整的 CHANGELOG_CONTENT 替换块（含侧边导航和内容区）。"""
    # ── 侧边导航 ──
    nav_items = "\n".join(_render_nav_item(e, i + 1) for i, e in enumerate(entries))

    # ── 内容区 ──
    sections_html = "\n".join(_render_section(e) for e in entries)

    content = f"""      <aside class="ds-docs-aside">
        <nav class="ds-pagenav" aria-label="文档目录">
          <details class="ds-pagenav-disclosure" open>
            <summary class="ds-pagenav-summary"><span>版本</span><svg class="ds-pagenav-chevron" width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="4 6 8 10 12 6"/></svg></summary>
            <ol class="ds-pagenav-list">
{nav_items}
            </ol>
          </details>
        </nav>
      </aside>
      <div class="ds-docs-main">
        <div class="ds-prose">
{sections_html}
        </div>
      </div>"""

    return content


# ── 主逻辑 ────────────────────────────────────────────────────────────────────


def load_entries() -> list[VersionEntry]:
    """从 docs/changelog_human/ 加载所有版本条目，按最新版本排在前面。"""
    if not HUMAN_DIR.exists():
        raise FileNotFoundError(f"目录不存在：{HUMAN_DIR}")

    md_files = list(HUMAN_DIR.glob("*.md"))
    if not md_files:
        raise ValueError(f"docs/changelog_human/ 中没有 .md 文件")

    entries = [parse_md_file(p) for p in md_files]
    # 最新版本排最前面（倒序）
    entries.sort(key=lambda e: e.sort_key, reverse=True)
    return entries


def update_changelog_html(new_content: str, dry_run: bool = False, check: bool = False) -> int:
    """替换 changelog.html 中两个注释标记之间的内容。"""
    if not CHANGELOG_HTML.exists():
        print(f"[ERROR] 未找到 {CHANGELOG_HTML}", file=sys.stderr)
        return 1

    original = CHANGELOG_HTML.read_text(encoding="utf-8")

    if CONTENT_START not in original or CONTENT_END not in original:
        print(
            f"[ERROR] changelog.html 中未找到标记：\n"
            f"  {CONTENT_START}\n  {CONTENT_END}",
            file=sys.stderr,
        )
        return 1

    # 构造替换后文本
    before = original[: original.index(CONTENT_START) + len(CONTENT_START)]
    after = original[original.index(CONTENT_END) :]
    updated = before + "\n" + new_content + "\n      " + after

    if check:
        if updated == original:
            print("✓ changelog.html 已是最新，无需更新。")
            return 0
        else:
            print("✗ changelog.html 内容需要更新，请运行：")
            print("  python3 tools/generate_changelog_html.py")
            return 2

    if dry_run:
        print("=== 将要写入 changelog.html（CHANGELOG_CONTENT_START 至 END）===")
        print(new_content[:3000])
        if len(new_content) > 3000:
            print(f"... [已截断，共 {len(new_content)} 字符]")
        return 0

    if updated == original:
        print("✓ changelog.html 已是最新，无需更新。")
        return 0

    CHANGELOG_HTML.write_text(updated, encoding="utf-8")
    print(f"✓ changelog.html 已更新（{len(entries_cache)} 个版本条目）。")
    return 0


entries_cache: list[VersionEntry] = []


def main() -> int:
    global entries_cache

    parser = argparse.ArgumentParser(
        description="从 docs/changelog_human/ 生成 changelog.html 内容",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--check", action="store_true", help="仅检查，不修改（CI 用，不一致返回 exit 2）")
    parser.add_argument("--dry-run", action="store_true", help="打印将要写入的内容，不修改文件")
    args = parser.parse_args()

    try:
        entries_cache = load_entries()
    except (FileNotFoundError, ValueError) as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 1

    print(f"发现 {len(entries_cache)} 个版本条目：", ", ".join(e.display_version for e in entries_cache))

    new_content = generate_content(entries_cache)
    return update_changelog_html(new_content, dry_run=args.dry_run, check=args.check)


if __name__ == "__main__":
    sys.exit(main())
