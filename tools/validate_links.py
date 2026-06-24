#!/usr/bin/env python3
"""validate_links.py — 链接与引用有效性校验

检查项：
  1. 内部锚点（href="#xxx"）的目标 id 在同文件存在
  2. 跨页锚点（href="page.html#xxx"）的目标 id 在目标文件存在
  3. 资源引用（href="assets/..."）的文件存在
  4. CSS / JS 引用（href="styles.css", src="scripts.js"）的文件存在
  5. 邮件链接（mailto:）格式合法（仅警告）
  6. 外链（http/https）格式合法（不实际请求）
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
HTML_GLOB = "*.html"


class IDCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.name_anchors: set[str] = set()  # <a name="...">

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_d = dict(attrs)
        if "id" in attr_d:
            self.ids.add(attr_d["id"])
        if tag == "a" and "name" in attr_d:
            self.name_anchors.add(attr_d["name"])


def collect_ids(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    parser = IDCollector()
    try:
        parser.feed(text)
    except Exception:
        return set()
    return parser.ids | parser.name_anchors


class LinkExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str | None]] = []  # (href, id_anchor)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_d = dict(attrs)
        if tag == "a" and "href" in attr_d:
            self.links.append((attr_d["href"], None))
        elif tag == "link" and "href" in attr_d:
            self.links.append((attr_d["href"], None))
        elif tag == "script" and "src" in attr_d:
            self.links.append((attr_d["src"], None))


def extract_links(path: Path) -> list[tuple[str, str | None]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    parser = LinkExtractor()
    try:
        parser.feed(text)
    except Exception:
        return []
    return parser.links


def main() -> int:
    html_files = sorted(ROOT.glob(HTML_GLOB))
    if not html_files:
        print(f"[WARN] 未发现 HTML 文件（{HTML_GLOB}）")
        return 0

    # 预收集所有 id
    ids_cache: dict[Path, set[str]] = {p: collect_ids(p) for p in html_files}

    errors = 0
    warnings = 0

    print(f"─── 链接校验 ───")
    print(f"扫描 {len(html_files)} 个 HTML")

    for path in html_files:
        links = extract_links(path)
        page_errors = 0
        page_warnings = 0

        for href, _ in links:
            # 解析 href
            if href.startswith(("#", "javascript:", "data:", "mailto:", "tel:")):
                # 内部锚点
                if href.startswith("#"):
                    target = href[1:]
                    if target and target not in ids_cache[path]:
                        print(f"  [ERROR] {path.name}: 锚点 #{target} 不存在")
                        page_errors += 1
                elif href.startswith("mailto:"):
                    email = href[7:].split("?")[0]
                    if email and not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
                        print(f"  [WARN] {path.name}: mailto 格式可疑：{email}")
                        page_warnings += 1
                continue

            if href.startswith(("http://", "https://", "//")):
                parsed = urlparse(
                    href if not href.startswith("//") else "https:" + href
                )
                if not parsed.netloc:
                    print(f"  [WARN] {path.name}: 外链格式异常：{href[:80]}")
                    page_warnings += 1
                continue

            # 内部路径（含跨页锚点）
            if "#" in href:
                file_part, anchor = href.split("#", 1)
            else:
                file_part, anchor = href, None

            # 去除查询字符串（如 ?v=1.3.1），避免把版本化引用误判为不存在的文件
            file_part = file_part.split("?")[0]

            # 跳过含 {{DS_VERSION}} 占位符的链接（stamp 后替换为实际版本号）
            if "{{DS_VERSION}}" in href:
                continue

            # 跳过 assets/downloads/（构建产物，仅 release pipeline 生成）
            if href.startswith("assets/downloads/") or "/assets/downloads/" in href:
                continue

            # 文件存在性
            target_path = (path.parent / file_part).resolve()
            if not target_path.exists():
                # 可能是站点根的相对路径
                alt = (ROOT / file_part).resolve()
                if not alt.exists():
                    print(f"  [ERROR] {path.name}: 引用不存在：{href}")
                    page_errors += 1
                    continue
                target_path = alt

            # 跨页锚点
            if anchor and target_path.suffix in (".html", ".htm"):
                target_ids = ids_cache.get(target_path) or collect_ids(target_path)
                if anchor not in target_ids:
                    print(f"  [ERROR] {path.name}: 跨页锚点不存在：{href}")
                    page_errors += 1

        errors += page_errors
        warnings += page_warnings
        if page_errors == 0 and page_warnings == 0:
            print(f"[OK] {path.name}")

    print()
    print(f"错误: {errors}  警告: {warnings}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
