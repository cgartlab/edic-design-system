#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tools/generate_changelog_html.py — 从 CHANGELOG.md 单源生成 changelog.html 内容。

设计（方案 A · 单一来源）：
  CHANGELOG.md 是版本变更的唯一真相源（由 release-please 自动维护）。
  本脚本解析其中每个版本节，生成人类友好的 HTML，写入 changelog.html 中
  <!-- CHANGELOG_CONTENT_START --> 与 <!-- CHANGELOG_CONTENT_END --> 之间。

  这样彻底消除了"机器 CHANGELOG.md + 手写 changelog_human/"双轨漂移问题：
    - 自动覆盖所有历史版本（无窟窿）
    - 永不漂移（结构性一致）
    - 无需人工为每个版本写摘要

解析的 CHANGELOG.md 格式（release-please / conventional-changelog）：
    ## [1.8.1](compare-url) (2026-06-24)      ← 版本头（也兼容 "## [1.8.1] — 2026-06-04"）
    ### 修复                                   ← 分类
    * **scope:** subject ([hash](url))        ← 条目（去除 commit/PR 引用噪音）

用法：
  python3 tools/generate_changelog_html.py            # 原地更新 changelog.html
  python3 tools/generate_changelog_html.py --check     # 仅检查（CI 用，不一致返回 exit 2）
  python3 tools/generate_changelog_html.py --dry-run   # 打印将写入的内容，不修改文件

退出码：
  0  成功（--check：已是最新）
  1  错误
  2  --check：内容需要更新
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from typing import NamedTuple

ROOT = Path(__file__).resolve().parent.parent
CHANGELOG_HTML = ROOT / "changelog.html"
CHANGELOG_MD = ROOT / "CHANGELOG.md"

CONTENT_START = "<!-- CHANGELOG_CONTENT_START -->"
CONTENT_END = "<!-- CHANGELOG_CONTENT_END -->"

# 分类显示顺序（CHANGELOG.md 中实际出现的中文章节）
_SECTION_ORDER = ["新增", "修复", "性能优化", "重构", "变更", "文档", "样式", "测试", "构建", "其他", "注意"]


class Version(NamedTuple):
    version: str       # "1.8.1"
    date: str          # "2026-06-24"（可空）
    anchor: str        # "v181"
    sections: list     # [("修复", ["item1", "item2"]), ...] 保序
    is_prerelease: bool


# ── 行内 Markdown → HTML / 纯文本清洗 ────────────────────────────────────────


_REF_GROUP_RE = re.compile(r"\s*\(\[[^\]]+\]\([^)]*\)(?:[,\s]+\[[^\]]+\]\([^)]*\))*\)")
_HASHLIKE_RE = re.compile(r"^(?:[0-9a-f]{6,40}|#\d+)$", re.I)
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
_BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
_CODE_RE = re.compile(r"`([^`]+)`")


def clean_item(text: str) -> str:
    """
    将一条 CHANGELOG 条目（Markdown）转为人类友好的 HTML 片段：
      - 去除尾部 commit/PR 引用括号组：([abc1234](url)) ([#147](url) [#148](url))
      - 余下的 [label](url)：label 是 hash/#num 则删去，否则保留为 <a>
      - **bold** → <strong>，`code` → <code>
      - 其余文本做 HTML 转义
    """
    s = text.strip()

    # 0) 去掉以 # 开头的 issue 编号"scope"（如 **#124:** / **#167 #175:**）——
    #    对人类读者无意义的 git 噪音，且 #124 会被硬编码校验器误判为 hex 颜色。
    s = re.sub(r"^\*\*#[^*]*\*\*[:：]?\s*", "", s).strip()

    # 1) 去掉尾部的引用括号组（可能有多组），如 " ([abc](u)) ([#1](u))"
    prev = None
    while prev != s:
        prev = s
        s = _REF_GROUP_RE.sub("", s).rstrip()

    # 2) 处理剩余的 inline 链接：hash/#num 丢弃，其它保留文字（不带链接，避免噪音）
    def _link_repl(m: re.Match) -> str:
        label = m.group(1)
        if _HASHLIKE_RE.match(label.strip()):
            return ""
        return label  # 保留可读文字，去掉 URL
    s = _LINK_RE.sub(_link_repl, s)

    # 3) 先按 ** 和 ` 切分出"受保护"片段，分别处理，避免转义破坏标签
    #    做法：用占位符提取 bold/code 内容，转义其余，再回填为标签。
    tokens: list[tuple[str, str]] = []  # (kind, content)

    def _tokenize(src: str) -> None:
        idx = 0
        pattern = re.compile(r"\*\*([^*]+)\*\*|`([^`]+)`")
        for m in pattern.finditer(src):
            if m.start() > idx:
                tokens.append(("text", src[idx:m.start()]))
            if m.group(1) is not None:
                tokens.append(("strong", m.group(1)))
            else:
                tokens.append(("code", m.group(2)))
            idx = m.end()
        if idx < len(src):
            tokens.append(("text", src[idx:]))

    _tokenize(s)

    out = []
    for kind, content in tokens:
        esc = html.escape(content)
        if kind == "strong":
            out.append(f"<strong>{esc}</strong>")
        elif kind == "code":
            out.append(f"<code>{esc}</code>")
        else:
            out.append(esc)
    result = "".join(out)

    # 4) 收尾：去掉多余空格、孤立空括号、尾部连字符
    result = re.sub(r"\s{2,}", " ", result).strip()
    result = re.sub(r"\s*\(\s*\)\s*$", "", result)
    result = result.rstrip(" -—·,，")
    return result


# ── CHANGELOG.md 解析 ────────────────────────────────────────────────────────


def anchor_for(version: str) -> str:
    return "v" + re.sub(r"[^0-9a-z]", "", version.lower())


_HEADER_RE = re.compile(
    r"^##\s*\[(?P<ver>\d+\.\d+\.\d+(?:-[0-9A-Za-z.\-]+)?)\]"   # [1.8.1] 或 [1.8.1-beta.1]
    r"(?:\([^)]*\))?"                                          # 可选 (compare-url)
    r".*?"                                                     # 中间杂项
    r"(?P<date>\d{4}-\d{2}-\d{2})?\s*$"                        # 可选日期
)
_SECTION_RE = re.compile(r"^###\s+(.+?)\s*$")
_ITEM_RE = re.compile(r"^\s*[*\-]\s+(.+?)\s*$")


def parse_changelog() -> list[Version]:
    if not CHANGELOG_MD.exists():
        raise FileNotFoundError(f"未找到 {CHANGELOG_MD}")

    versions: list[Version] = []
    seen: set[str] = set()

    cur: Version | None = None
    cur_section: str | None = None
    cur_items: list[str] = []
    sections: list[tuple[str, list[str]]] = []

    def flush_section():
        nonlocal cur_section, cur_items
        if cur_section is not None and cur_items:
            sections.append((cur_section, cur_items))
        cur_section, cur_items = None, []

    def flush_version():
        nonlocal cur, sections
        if cur is not None and sections:
            versions.append(cur._replace(sections=sections))
        cur, sections = None, []

    for raw in CHANGELOG_MD.read_text(encoding="utf-8").splitlines():
        hm = _HEADER_RE.match(raw)
        if hm:
            flush_section()
            flush_version()
            ver = hm.group("ver")
            base = ver.split("-")[0]
            # 跳过未发布占位与重复版本（保留首次出现 = 最新）
            if base in seen:
                cur = None
                continue
            seen.add(base)
            cur = Version(
                version=ver,
                date=hm.group("date") or "",
                anchor=anchor_for(ver),
                sections=[],
                is_prerelease="-" in ver,
            )
            sections = []
            cur_section, cur_items = None, []
            continue

        if cur is None:
            continue

        sm = _SECTION_RE.match(raw)
        if sm:
            flush_section()
            cur_section = sm.group(1).strip()
            cur_items = []
            continue

        im = _ITEM_RE.match(raw)
        if im and cur_section is not None:
            cleaned = clean_item(im.group(1))
            if cleaned:
                cur_items.append(cleaned)

    flush_section()
    flush_version()
    return versions


# ── HTML 生成 ─────────────────────────────────────────────────────────────────


def _ordered_sections(sections: list[tuple[str, list[str]]]) -> list[tuple[str, list[str]]]:
    def key(item):
        name = item[0]
        return (_SECTION_ORDER.index(name) if name in _SECTION_ORDER else len(_SECTION_ORDER), name)
    return sorted(sections, key=key)


def render_section(v: Version) -> str:
    date_suffix = f" — {v.date}" if v.date else ""
    lines = [
        f'        <section class="ds-doc-block" id="{v.anchor}">',
        f"          <h2>v{html.escape(v.version)}{html.escape(date_suffix)}</h2>",
    ]
    for name, items in _ordered_sections(v.sections):
        if not items:
            continue
        lines.append(f"          <h3>{html.escape(name)}</h3>")
        lines.append("          <ul>")
        for it in items:
            lines.append(f"            <li>{it}</li>")
        lines.append("          </ul>")
    lines.append("        </section>")
    return "\n".join(lines)


def render_nav_item(v: Version, idx: int) -> str:
    num = str(idx).zfill(2)
    return (
        f'              <li><a class="ds-pagenav-link" href="#{v.anchor}">'
        f'<span class="ds-pagenav-num">{num}</span>'
        f'<span class="ds-pagenav-text">v{html.escape(v.version)}</span></a></li>'
    )


def generate_content(versions: list[Version]) -> str:
    nav = "\n".join(render_nav_item(v, i + 1) for i, v in enumerate(versions))
    body = "\n".join(render_section(v) for v in versions)
    return f"""      <aside class="ds-docs-aside">
        <nav class="ds-pagenav" aria-label="文档目录">
          <details class="ds-pagenav-disclosure" open>
            <summary class="ds-pagenav-summary"><span>版本</span><svg class="ds-pagenav-chevron" width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="4 6 8 10 12 6"/></svg></summary>
            <ol class="ds-pagenav-list">
{nav}
            </ol>
          </details>
        </nav>
      </aside>
      <div class="ds-docs-main">
        <div class="ds-prose">
{body}
        </div>
      </div>"""


def update_html(new_content: str, dry_run: bool, check: bool) -> int:
    if not CHANGELOG_HTML.exists():
        print(f"[ERROR] 未找到 {CHANGELOG_HTML}", file=sys.stderr)
        return 1
    original = CHANGELOG_HTML.read_text(encoding="utf-8")
    if CONTENT_START not in original or CONTENT_END not in original:
        print(f"[ERROR] changelog.html 缺少标记 {CONTENT_START} / {CONTENT_END}", file=sys.stderr)
        return 1

    before = original[: original.index(CONTENT_START) + len(CONTENT_START)]
    after = original[original.index(CONTENT_END):]
    updated = before + "\n" + new_content + "\n      " + after

    if check:
        if updated == original:
            print("✓ changelog.html 已是最新。")
            return 0
        print("✗ changelog.html 需要更新：python3 tools/generate_changelog_html.py", file=sys.stderr)
        return 2
    if dry_run:
        print(new_content[:4000])
        return 0
    if updated == original:
        print("✓ changelog.html 已是最新，无需更新。")
        return 0
    CHANGELOG_HTML.write_text(updated, encoding="utf-8")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="从 CHANGELOG.md 单源生成 changelog.html")
    ap.add_argument("--check", action="store_true", help="仅检查（CI 用，不一致返回 exit 2）")
    ap.add_argument("--dry-run", action="store_true", help="打印将写入的内容，不修改文件")
    args = ap.parse_args()

    try:
        versions = parse_changelog()
    except FileNotFoundError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 1

    if not versions:
        print("[ERROR] CHANGELOG.md 中未解析到任何版本节。", file=sys.stderr)
        return 1

    print(f"从 CHANGELOG.md 解析到 {len(versions)} 个版本：",
          ", ".join(f"v{v.version}" for v in versions))
    rc = update_html(generate_content(versions), dry_run=args.dry_run, check=args.check)
    if rc == 0 and not args.check and not args.dry_run:
        print(f"✓ changelog.html 已更新（{len(versions)} 个版本，单源自 CHANGELOG.md）。")
    return rc


if __name__ == "__main__":
    sys.exit(main())
