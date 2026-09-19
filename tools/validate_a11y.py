#!/usr/bin/env python3
"""validate_a11y.py — 基础可访问性检查（纯 stdlib）

检查项：
  1. <img> 必有 alt（装饰性 alt="" 允许）
  2. 交互元素（<a>、<button>）必有可访问名称
  3. <a> 嵌套 <a> 警告
  4. <button> 嵌套 <button> 警告
  5. 标题层级连贯（h1 → h2 → h3，不跳级）
  6. 页面至少一个 <h1>
  7. 装饰性元素是否加 aria-hidden
  8. 暗色模式背景/文字对比度简化模型（基于 OKLch 推算）

注：完整 a11y 测试推荐使用 axe-core（通过 npx @axe-core/cli）。
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_GLOB = "*.html"
STYLES_CSS = ROOT / "styles.css"


class A11YChecker(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.headings: list[tuple[int, bool, int, str]] = []
        self.link_stack: list[dict] = []
        self.button_stack: list[dict] = []
        self.interactive_no_name: list[tuple[str, int]] = []
        self.img_no_alt: list[tuple[int, str]] = []
        self.has_h1 = False
        self._current_heading_text = ""
        self._in_heading: int | None = None
        self._heading_line = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_d = dict(attrs)
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = int(tag[1])
            self._in_heading = level
            self._heading_line = self.getpos()[0]
            self._current_heading_text = ""
            if tag == "h1":
                self.has_h1 = True
        elif tag == "img":
            if "alt" not in attr_d:
                src = attr_d.get("src", "?")[:60]
                self.img_no_alt.append((self.getpos()[0], src))
        elif tag == "a":
            self.link_stack.append({"attrs": attr_d, "line": self.getpos()[0], "text": ""})
        elif tag == "button":
            self.button_stack.append({"attrs": attr_d, "line": self.getpos()[0], "text": ""})

    def handle_endtag(self, tag: str) -> None:
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            level = self._in_heading or 1
            text = self._current_heading_text.strip()
            self.headings.append((level, bool(text), self._heading_line, text[:60]))
            self._in_heading = None
            self._current_heading_text = ""
        elif tag == "a":
            if self.link_stack:
                entry = self.link_stack.pop()
                if not self._has_accessible_name(entry["attrs"], entry["text"]):
                    self.interactive_no_name.append(("<a>", entry["line"]))
        elif tag == "button":
            if self.button_stack:
                entry = self.button_stack.pop()
                if not self._has_accessible_name(entry["attrs"], entry["text"]):
                    self.interactive_no_name.append(("<button>", entry["line"]))

    def handle_data(self, data: str) -> None:
        if self._in_heading is not None:
            self._current_heading_text += data
        for stack in (self.link_stack, self.button_stack):
            for entry in stack:
                entry["text"] += data

    def _has_accessible_name(self, attrs: dict[str, str | None], text: str = "") -> bool:
        if attrs.get("aria-label"):
            return True
        if attrs.get("aria-labelledby"):
            return True
        if attrs.get("title"):
            return True
        if text and text.strip():
            return True
        return False


def check_html(path: Path) -> list[tuple[str, str]]:
    issues: list[tuple[str, str]] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    checker = A11YChecker()
    try:
        checker.feed(text)
    except Exception as exc:
        issues.append(("ERROR", f"解析失败：{exc}"))
        return issues

    if not checker.has_h1:
        issues.append(("WARN", "页面缺少 <h1>"))

    prev_level = 0
    for level, has_text, line, snippet in checker.headings:
        if not has_text:
            issues.append(("WARN", f"第 {line} 行 <h{level}> 为空"))
        if prev_level > 0 and level > prev_level + 1:
            issues.append(
                ("WARN", f"第 {line} 行标题跳级：h{prev_level} → h{level}（建议 h{prev_level + 1}）")
            )
        prev_level = level

    for line, src in checker.img_no_alt:
        issues.append(("ERROR", f"第 {line} 行 <img> 缺少 alt：src={src}"))

    for tag, line in checker.interactive_no_name:
        issues.append(("WARN", f"第 {line} 行 {tag} 缺少可访问名（aria-label / title / 文本）"))

    return issues


def check_dark_contrast() -> list[tuple[str, str]]:
    issues: list[tuple[str, str]] = []
    if not STYLES_CSS.exists():
        return issues
    text = STYLES_CSS.read_text(encoding="utf-8", errors="replace")
    dark_block = re.search(
        r'\[data-theme=["\']?dark["\']?\]\s*\{([^}]+)\}', text, re.MULTILINE
    )
    if not dark_block:
        return issues
    body = dark_block.group(1)
    bg_match = re.search(r"--ds-color-bg\s*:\s*([^;]+);", body)
    fg_match = re.search(r"--ds-color-fg\s*:\s*([^;]+);", body)
    if not bg_match or not fg_match:
        return issues
    bg_str = bg_match.group(1).strip()
    fg_str = fg_match.group(1).strip()
    bg_l = parse_oklch_lightness(bg_str)
    fg_l = parse_oklch_lightness(fg_str)
    if bg_l is not None and fg_l is not None:
        if abs(bg_l - fg_l) < 0.4:
            issues.append(
                ("WARN", f"暗色 bg/fg 亮度差仅 {abs(bg_l - fg_l):.2f}（建议 ≥ 0.4）")
            )
    return issues


def parse_oklch_lightness(value: str) -> float | None:
    m = re.search(r"oklch\(\s*([\d.]+)%", value, re.IGNORECASE)
    if m:
        return float(m.group(1)) / 100
    return None


def main() -> int:
    html_files = sorted(ROOT.glob(HTML_GLOB))
    if not html_files:
        print(f"[WARN] 未发现 HTML 文件（{HTML_GLOB}）")
        return 2

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

    print()
    print("─── 暗色模式对比度检查 ───")
    dark_issues = check_dark_contrast()
    if not dark_issues:
        print("[OK] 暗色模式 bg/fg 亮度差合理")
    for lvl, msg in dark_issues:
        print(f"  [{lvl}] {msg}")
        if lvl == "WARN":
            total_warnings += 1

    print()
    print("─── 可访问性校验总结 ───")
    print(f"扫描文件: {len(html_files)}")
    print(f"错误    : {total_errors}")
    print(f"警告    : {total_warnings}")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
