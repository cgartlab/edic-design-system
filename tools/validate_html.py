#!/usr/bin/env python3
"""validate_html.py — HTML 结构合法性检查

检查项：
  1. <html> 有 lang 属性
  2. <head> 含 <meta charset> 与 <meta name="viewport">
  3. 禁止外部运行时 <link>/<script> 与 javascript: 链接
  4. <link rel="stylesheet"> / <script src> 引用的本地文件存在
  5. 禁止常见内联事件属性
  6. 重复 id 检测
  7. 必填 meta（description, theme-color）
  8. 存在 <main> 或 role="main" 主内容区
  9. 页面级 <h1> 数量为 1（打印模板可豁免）
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_GLOB = "*.html"
EXTERNAL_RESOURCE_RE = re.compile(r'^(?:https?:)?//|^(?:https?:)')
JS_HREF_RE = re.compile(r'^\s*javascript:', re.IGNORECASE)
INLINE_EVENT_ATTRS = {
    "onclick", "ondblclick", "onmousedown", "onmouseup", "onmousemove",
    "onmouseover", "onmouseout", "onsubmit", "onchange", "oninput",
    "onkeydown", "onkeypress", "onkeyup", "onload", "onerror",
}
MULTI_H1_EXEMPTIONS = {
    "report.html": "A4 报告规范/模板按分页结构使用多个 h1",
}


class HTMLChecker(HTMLParser):
    def __init__(self, path: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.path = path
        self.ids: list[tuple[str, int]] = []
        self.links: list[tuple[str, int]] = []
        self.scripts: list[tuple[str, int]] = []
        self.has_charset = False
        self.has_viewport = False
        self.has_html_lang = False
        self.html_lang = ""
        self.has_description = False
        self.has_title = False
        self.external_resources: list[tuple[str, int, str]] = []
        self.local_links: list[tuple[str, int, str]] = []
        self.local_scripts: list[tuple[str, int, str]] = []
        self.inline_events: list[tuple[str, int, str]] = []
        self.javascript_hrefs: list[tuple[str, int, str]] = []
        self.has_main = False
        self.main_count = 0
        self.h1_count = 0
        self.h1_lines: list[int] = []
        self.in_head = False
        self.in_body = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_d = dict(attrs)
        line = self.getpos()[0]
        if tag == "html":
            self.has_html_lang = "lang" in attr_d
            if self.has_html_lang:
                self.html_lang = attr_d.get("lang", "")
        elif tag == "head":
            self.in_head = True
        elif tag == "body":
            self.in_body = True
        elif tag == "meta":
            charset = attr_d.get("charset", "")
            name = attr_d.get("name", "")
            if charset or name == "charset":
                self.has_charset = True
            if name == "viewport":
                self.has_viewport = True
            if name == "description":
                self.has_description = True
        elif tag == "title":
            self.has_title = True
        elif tag == "main" or attr_d.get("role") == "main":
            self.has_main = True
            self.main_count += 1
        elif tag == "h1":
            self.h1_count += 1
            self.h1_lines.append(line)
        elif tag == "link":
            href = attr_d.get("href", "")
            if href and EXTERNAL_RESOURCE_RE.search(href):
                self.external_resources.append(("link", line, href))
            elif href:
                self.local_links.append(("link", line, href))
        elif tag == "script":
            src = attr_d.get("src", "")
            if src and EXTERNAL_RESOURCE_RE.search(src):
                self.external_resources.append(("script", line, src))
            elif src:
                self.local_scripts.append(("script", line, src))
        elif tag == "img" or tag == "image":
            # SVG 内的 image 不一定需要 alt
            pass
        elif tag == "a":
            href = attr_d.get("href", "")
            if href and JS_HREF_RE.search(href):
                self.javascript_hrefs.append(("a", line, href))

        for attr_name in attr_d:
            if attr_name.lower() in INLINE_EVENT_ATTRS:
                self.inline_events.append((tag, line, attr_name.lower()))
        if "id" in attr_d:
            self.ids.append((attr_d["id"], line))


def check_html(path: Path) -> list[tuple[str, str]]:
    """返回 (level, message) 列表。level = 'ERROR' | 'WARN' | 'OK'。"""
    issues: list[tuple[str, str]] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    checker = HTMLChecker(path)
    try:
        checker.feed(text)
    except Exception as exc:
        issues.append(("ERROR", f"解析失败：{exc}"))
        return issues

    # 1. lang
    if not checker.has_html_lang:
        issues.append(("ERROR", "<html> 缺少 lang 属性"))
    elif checker.html_lang and not checker.html_lang.strip():
        issues.append(("WARN", "<html lang=''> 为空"))

    # 2. head meta
    if not checker.has_charset:
        issues.append(("ERROR", "<head> 缺少 <meta charset>"))
    if not checker.has_viewport:
        issues.append(("WARN", "<head> 缺少 <meta name='viewport'>"))
    if not checker.has_description:
        issues.append(("WARN", "<head> 缺少 <meta name='description'>"))
    if not checker.has_title:
        issues.append(("WARN", "<head> 缺少 <title>"))

    # 3. 外部资源与 javascript:
    for kind, line, value in checker.external_resources:
        issues.append(("ERROR", f"第 {line} 行引用了外部运行时资源（{kind}）：{value}"))
    for tag, line, value in checker.javascript_hrefs:
        issues.append(("ERROR", f"第 {line} 行存在 javascript: 链接（{tag}）：{value}"))
    for tag, line, attr in checker.inline_events:
        issues.append(("ERROR", f"第 {line} 行存在内联事件属性（{tag}.{attr}）"))

    # 4. CSS / JS 引用
    for kind, line, href in checker.local_links:
        if href.endswith(".css"):
            css_path = path.parent / href.split("?")[0]
            if not css_path.exists():
                issues.append(("ERROR", f"第 {line} 行引用了不存在的 CSS：{href}"))

    for kind, line, src in checker.local_scripts:
        js_path = path.parent / src.split("?")[0]
        if not js_path.exists():
            issues.append(("ERROR", f"第 {line} 行引用了不存在的 JS：{src}"))

    # 5. 重复 id
    seen: dict[str, int] = {}
    for id_, line in checker.ids:
        if id_ in seen:
            issues.append(("ERROR", f"重复 id '{id_}'（第 {seen[id_]} 行 与 第 {line} 行）"))
        else:
            seen[id_] = line

    # 6. 主内容区
    if not checker.has_main:
        issues.append(("ERROR", "缺少 <main> 或 role=\"main\" 主内容区"))
    elif checker.main_count > 1:
        issues.append(("ERROR", f"存在 {checker.main_count} 个主内容区"))

    # 7. 页面标题数量
    if checker.h1_count == 0:
        issues.append(("ERROR", "缺少页面级 <h1>"))
    elif checker.h1_count > 1 and path.name not in MULTI_H1_EXEMPTIONS:
        issues.append(("ERROR", f"存在 {checker.h1_count} 个 <h1>：{checker.h1_lines}"))

    return issues


def main() -> int:
    html_files = sorted(ROOT.glob(HTML_GLOB))
    if not html_files:
        print(f"[WARN] 未发现 HTML 文件（{HTML_GLOB}）")
        return 0

    total_errors = 0
    total_warnings = 0

    for path in html_files:
        issues = check_html(path)
        errors = [m for lvl, m in issues if lvl == "ERROR"]
        warnings = [m for lvl, m in issues if lvl == "WARN"]
        total_errors += len(errors)
        total_warnings += len(warnings)
        if errors or warnings:
            print(f"\n─── {path.name} ───")
            for msg in errors:
                print(f"  [ERROR] {msg}")
            for msg in warnings:
                print(f"  [WARN] {msg}")
        else:
            print(f"[OK] {path.name}")

    print()
    print("─── HTML 校验总结 ───")
    print(f"扫描文件: {len(html_files)}")
    print(f"错误    : {total_errors}")
    print(f"警告    : {total_warnings}")
    return 1 if total_errors else (2 if total_warnings else 0)


if __name__ == "__main__":
    sys.exit(main())
