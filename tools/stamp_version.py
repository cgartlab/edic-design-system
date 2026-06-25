#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stamp_version.py — 将 VERSION 同步到所有项目资源

目的：消除仓库内所有"硬编码版本号"造成的版本漂移问题。VERSION 是唯一真相源。

可标记（stamp）的目标：

  ┌────────────────────┬────────────────────────────────────────────┐
  │ 目标                │ 占位符（源码中写此占位符）                  │
  ├────────────────────┼────────────────────────────────────────────┤
  │ HTML ?v=           │ ?v={{DS_VERSION}}                           │
  │ HTML 可见文本      │ v{{DS_VERSION}} / {{DS_VERSION}}            │
  │ CSS 注释           │ {{DS_VERSION}}（头部/底部版本注释）          │
  │ JSON version 字段  │ "{{DS_VERSION}}"                            │
  │ MD 可见文本        │ v{{DS_VERSION}} / {{DS_VERSION}}            │
  │ README.md badge    │ v{{DS_VERSION}} + {{DS_VERSION}}（两处替换）│
  │ AGENTS.md 状态     │ v{{DS_VERSION}}                             │
  └────────────────────┴────────────────────────────────────────────┘

占位符设计的取舍：源文件保留 `{{DS_VERSION}}` 字面量，stamp 时一次性替换为真实版本号。
"DS_" 前缀避免与文档中说明占位符语法的示例（"{{VERSION}}" 等通用写法）发生冲突。
已提交的文件呈现"已 stamp"的状态——这样：

  - GitHub Pages 部署时无需运行任何脚本（HTML 是静态的）
  - 本地开发 / CI 都能用 stamp --check 验证一致性
  - pre-commit / pre-release 可自动 stamp，避免漏改

退出码：
  0  成功（或仅有已 stamp 的文件，无需变更）
  1  错误（参数错误、VERSION 文件缺失、占位符找不到等）
  2  警告（--check 模式发现文件与 VERSION 不一致）

用法：
  python3 tools/stamp_version.py             # 应用变更
  python3 tools/stamp_version.py --check     # 检查模式（不修改，CI 用）
  python3 tools/stamp_version.py --diff      # 显示 diff 预览（不修改）
  python3 tools/stamp_version.py --restore   # 把当前 stamp 反向还原为占位符
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT / "VERSION"

PLACEHOLDER = "{{DS_VERSION}}"
PLACEHOLDER_RE = re.compile(r"\{\{DS_VERSION\}\}")

HTML_TARGETS = [
    "index.html",
    "terms.html",
    "prompts.html",
    "downloads.html",
    "docs.html",
    "changelog.html",
    "blog.html",
    "company.html",
    "resume.html",
    "report.html",
]

CSS_TARGETS = ["styles.css"]

JS_TARGETS = ["scripts.js"]

JSON_TARGETS = ["package.json", "tokens.json"]

MD_TARGETS = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "skills/edic-design-system/README.md",
    "skills/edic-design-system/SKILL.md",
    "docs/VERSIONING.md",
    "DEVELOPMENT-GUIDE.md",
]


def read_version() -> str:
    """读取 VERSION 文件（单行文本）。失败抛错。"""
    if not VERSION_FILE.exists():
        raise FileNotFoundError(f"VERSION 文件不存在: {VERSION_FILE}")
    text = VERSION_FILE.read_text(encoding="utf-8")
    first_line = text.strip().splitlines()[0].strip() if text.strip() else ""
    if not first_line:
        raise ValueError(f"VERSION 文件为空: {VERSION_FILE}")
    if not re.match(r"^[0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9.]+)?$", first_line):
        raise ValueError(f"VERSION 文件内容非法（需 semver）: '{first_line}'")
    return first_line


def restore_placeholders(text: str, version: str) -> tuple[str, int]:
    """反向操作：把已 stamp 的值还原为 {{DS_VERSION}} 占位符。

    仅在 --restore 模式使用，便于将源码重新切回"未 stamp"状态。
    会替换：
      - ?v=VERSION  →  ?v={{DS_VERSION}}
      - v{VERSION} （作为整词）  →  v{{DS_VERSION}}
      - "VERSION"（JSON version 字段）  →  "{{DS_VERSION}}"
    """
    count = 0

    def _sub(pattern: str, repl: str, s: str) -> tuple[str, int]:
        new, n = re.subn(pattern, repl, s)
        return new, n

    quote_class = r"""["']"""
    text, n = _sub(
        rf"\?v={re.escape(version)}(?={quote_class})", f"?v={PLACEHOLDER}", text
    )
    count += n
    text, n = _sub(rf"\bv{re.escape(version)}\b", f"v{PLACEHOLDER}", text)
    count += n
    text, n = _sub(
        rf'"version":\s*"{re.escape(version)}"', f'"version": "{PLACEHOLDER}"', text
    )
    count += n
    return text, count


def collect_targets() -> list[Path]:
    """收集所有需要 stamp 的文件路径（HTML → CSS → JS → JSON → MD 顺序）。"""
    paths: list[Path] = []
    for name in HTML_TARGETS:
        p = ROOT / name
        if p.exists():
            paths.append(p)
    for name in CSS_TARGETS:
        p = ROOT / name
        if p.exists():
            paths.append(p)
    for name in JS_TARGETS:
        p = ROOT / name
        if p.exists():
            paths.append(p)
    for name in JSON_TARGETS:
        p = ROOT / name
        if p.exists():
            paths.append(p)
    for name in MD_TARGETS:
        p = ROOT / name
        if p.exists():
            paths.append(p)
    return paths


def diff_text(old: str, new: str) -> list[str]:
    """简单行级 diff（无需 difflib 依赖）。"""
    old_lines = old.splitlines(keepends=True)
    new_lines = new.splitlines(keepends=True)
    out: list[str] = []
    i = j = 0
    while i < len(old_lines) and j < len(new_lines):
        if old_lines[i] == new_lines[j]:
            i += 1
            j += 1
            continue
        out.append(f"  - {old_lines[i].rstrip()}")
        out.append(f"  + {new_lines[j].rstrip()}")
        i += 1
        j += 1
    while i < len(old_lines):
        out.append(f"  - {old_lines[i].rstrip()}")
        i += 1
    while j < len(new_lines):
        out.append(f"  + {new_lines[j].rstrip()}")
        j += 1
    return out


def extract_changelog_section(version: str) -> str | None:
    """从 CHANGELOG.md 提取指定版本的 changelog section 文本。

    解析 Keep a Changelog 格式：
      ## [1.6.0] — 2026-06-22
      ### 新增
      ...

    返回该版本的所有内容（不含下一版本的标题），或 None（未找到）。
    """
    changelog_path = ROOT / "CHANGELOG.md"
    if not changelog_path.exists():
        return None

    content = changelog_path.read_text(encoding="utf-8")

    # 转义版本号用于正则（处理 semver prerelease 等特殊字符）
    escaped_version = re.escape(version)

    # 匹配 ## [version] 或 ## [version] — date 开头
    # 使用普通字符串拼接避免 rf-string 中 \{ 转义与 f-string 格式化的冲突
    pattern = re.compile(
        "^##\\s+\\[" + escaped_version + "\\](?:[^\\n]*\\n)(.*?)(?=^##\\s+\\[|\\Z)",
        re.MULTILINE | re.DOTALL,
    )
    m = pattern.search(content)
    if not m:
        return None

    section = m.group(1).rstrip()
    return section


def replace_old_version(
    text: str, old_version: str, new_version: str
) -> tuple[str, int]:
    """在已提交（已 stamp）的文件中把旧版本号替换为新版本号。

    处理三种形式：
      - ?v=OLD  （cache-busting query string）
      - vOLD    （可见的版本文字，仅在词边界处）
      - "version": "OLD"（JSON version 字段）
    """
    count = 0

    def _sub(pattern: str, repl: str, s: str) -> tuple[str, int]:
        new, n = re.subn(pattern, repl, s)
        return new, n

    quote_class = r"""["']"""
    text, n = _sub(
        rf"\?v={re.escape(old_version)}(?={quote_class})",
        f"?v={new_version}",
        text,
    )
    count += n
    text, n = _sub(rf"\bv{re.escape(old_version)}\b", f"v{new_version}", text)
    count += n
    text, n = _sub(
        rf'"version":\s*"{re.escape(old_version)}"',
        f'"version": "{new_version}"',
        text,
    )
    count += n

    # Pattern 4: version: X.Y.Z (YAML frontmatter, no v prefix, no quotes)
    text, n = _sub(
        rf"(?m)^version:\s*['\"]?{re.escape(old_version)}['\"]?(?:\s+#.*)?$",
        f"version: {new_version}",
        text,
    )
    count += n

    # Pattern 5: **Version:** X.Y.Z (visible markdown text, no v prefix)
    text, n = _sub(
        rf"\*\*Version:\*\*\s*{re.escape(old_version)}\b",
        f"**Version:** {new_version}",
        text,
    )
    count += n
    return text, count


def find_previous_version(paths: list[Path], current_version: str) -> str | None:
    """从已提交的文件中探测现有的版本号，用于版本 bump 场景。

    仅扫描两种 stamp 目标字段：
      - ?v=X.Y.Z（HTML cache-busting）
      - "version": "X.Y.Z"（JSON）
    不扫描可见版本文字，避免从历史记录（如 docs.html 时间线）中误检旧版本。
    """
    patterns = [
        re.compile(r'\?v=([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9.]+)?)["\']'),
        re.compile(r'"version":\s*"([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9.]+)?)"'),
    ]
    for path in paths:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in patterns:
            m = pattern.search(text)
            if m:
                v = m.group(1)
                if v != current_version:
                    return v
    return None


def apply_stamp(paths: Iterable[Path], version: str, mode: str) -> int:
    """执行 stamp 主体逻辑。

    mode ∈ {"write", "check", "diff", "restore"}
    返回：0 = 成功 / 一致；1 = 错误；2 = check 模式发现不一致

    两段式策略（write / check / diff）：
      第一段：将 {{DS_VERSION}} 占位符替换为 version（初次 stamp）
      第二段：将已 stamp 的旧版本号替换为 version（版本 bump）
    两段合并后得到最终的变更数，确保无论源文件处于哪种状态都能正确更新。
    """
    paths = list(paths)

    old_version: str | None = None
    if mode in ("write", "check", "diff"):
        old_version = find_previous_version(paths, version)
        if old_version:
            print(f"检测到旧版本号: v{old_version}（将同步为 v{version}）")

    total_changes = 0
    files_changed = 0
    files_checked = 0
    inconsistencies = 0

    for path in paths:
        original = path.read_text(encoding="utf-8", errors="replace")

        if mode == "restore":
            new_text, n = restore_placeholders(original, version)
            if n == 0:
                print(f"  [skip] {path.name}: 无需还原")
                continue
            print(f"  [restore] {path.name}: {n} 处替换")
            total_changes += n
            files_changed += 1
            if new_text != original:
                path.write_text(new_text, encoding="utf-8")
            continue

        new_text, n_placeholder = PLACEHOLDER_RE.subn(version, original)

        n_bump = 0
        if old_version:
            new_text, n_bump = replace_old_version(new_text, old_version, version)

        n = n_placeholder + n_bump
        files_checked += 1

        if n == 0:
            continue

        if mode == "check":
            reasons = []
            if n_placeholder:
                reasons.append(f"{n_placeholder} 个 {PLACEHOLDER} 占位符")
            if n_bump:
                reasons.append(f"{n_bump} 处旧版本号 v{old_version}")
            print(f"  [STAMP NEEDED] {path.name}: {', '.join(reasons)}")
            inconsistencies += 1
            total_changes += n
            continue

        if mode == "diff":
            print(f"  [diff] {path.name}: {n} 处变更")
            for line in diff_text(original, new_text):
                print(line)
            inconsistencies += n
            total_changes += n
            continue

        reasons = []
        if n_placeholder:
            reasons.append(f"{n_placeholder} 个占位符")
        if n_bump:
            reasons.append(f"{n_bump} 处旧版本号 v{old_version}")
        print(f"  [stamp] {path.name}: {', '.join(reasons)} → v{version}")
        total_changes += n
        files_changed += 1
        if new_text != original:
            path.write_text(new_text, encoding="utf-8")

    print()
    if mode == "check":
        if inconsistencies:
            print(f"✗ {files_checked} 个文件检查，{inconsistencies} 个需要 stamp")
            print(f"  运行: python3 tools/stamp_version.py")
            return 2
        print(f"✓ {files_checked} 个文件全部一致（VERSION = {version}）")
        return 0

    if mode == "diff":
        if inconsistencies:
            print(f"⚠ {files_checked} 个文件待 stamp，共 {inconsistencies} 处变更")
        else:
            print(f"✓ {files_checked} 个文件全部一致")
        return 0

    if mode == "restore":
        print(f"✓ 还原完成：{files_changed} 个文件，{total_changes} 处占位符恢复")
        return 0

    print(
        f"✓ stamp 完成：{files_changed} 个文件，{total_changes} 处替换（VERSION = v{version}）"
    )
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="将 VERSION 同步到所有项目资源",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="仅检查，不修改（CI 用）")
    group.add_argument("--diff", action="store_true", help="显示 diff 预览")
    group.add_argument(
        "--restore",
        action="store_true",
        help="反向：把 stamp 值还原为 {{DS_VERSION}} 占位符",
    )
    parser.add_argument(
        "--changelog-section",
        metavar="VERSION",
        help="提取 CHANGELOG.md 中指定版本的 section 内容（供 release.yml 生成 Release Notes 用）",
    )
    args = parser.parse_args()

    # --changelog-section 是独立模式，不与 group 互斥
    if args.changelog_section:
        section = extract_changelog_section(args.changelog_section)
        if section is None:
            print(
                f"[ERROR] CHANGELOG.md 中未找到版本 {args.changelog_section}",
                file=sys.stderr,
            )
            return 1
        print(section)
        return 0

    if args.restore and (args.check or args.diff):
        parser.error("--restore 与 --check / --diff 互斥")

    try:
        version = read_version()
    except (FileNotFoundError, ValueError) as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return 1

    mode = "write"
    if args.check:
        mode = "check"
    elif args.diff:
        mode = "diff"
    elif args.restore:
        mode = "restore"

    print(f"─── stamp_version.py ───")
    print(f"VERSION: v{version}")
    print(f"模式: {mode}")
    print()

    paths = collect_targets()
    if not paths:
        print("[WARN] 未发现 stamp 目标文件")
        return 0

    return apply_stamp(paths, version, mode)


if __name__ == "__main__":
    sys.exit(main())
