#!/usr/bin/env python3
"""validate_versions.py — 资源 ?v= 版本号同步校验

检查项：
  1. 所有 HTML 中 styles.css?v=... 与 scripts.js?v=... 一致
  2. ?v= 值与 VERSION 最新稳定版本号一致
  3. ?v= 格式合法（X.Y.Z 或 X.Y.Z-{prerelease}）
  4. 同一资源在所有 HTML 中 ?v= 一致
  5. 占位符 {{DS_VERSION}} 已被 stamp（不应有遗留）
  6. HTML 用户可见版本（hero badge / footer v{{DS_VERSION}}）已被 stamp
  7. README.md 顶部版本 badge 已被 stamp
  8. AGENTS.md 状态行版本号已被 stamp
  9. CSS/JSON/MD 中 {{DS_VERSION}} 占位符已被 stamp
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_GLOB = "*.html"
VERSION_FILE = ROOT / "VERSION"
README_FILE = ROOT / "README.md"
AGENTS_FILE = ROOT / "AGENTS.md"

VERSION_RE = re.compile(r"\?v=([0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9.]+)?)")
SEMVER_RE = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9.]+)?$")
PLACEHOLDER_RE = re.compile(r"\{\{DS_VERSION\}\}")

STAMP_TARGETS = [
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
    "styles.css",
    "scripts.js",
    "package.json",
    "tokens.json",
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "skills/edic-design-system/README.md",
    "skills/edic-design-system/SKILL.md",
    "docs/VERSIONING.md",
    "DEVELOPMENT-GUIDE.md",
]

HARDCODED_SCAN_TARGETS = [
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "skills/edic-design-system/README.md",
    "skills/edic-design-system/SKILL.md",
    "docs/VERSIONING.md",
    "DEVELOPMENT-GUIDE.md",
    "package.json",
    "tokens.json",
]

HARDCODED_SCAN_EXCEPTIONS = [
    re.compile(r"\{\{DS_VERSION\}\}"),
    re.compile(r"^##\s+\["),
    re.compile(r"^<!--.*-->\s*$"),
    re.compile(r"https?://[^\s]*v?\d+\.\d+\.\d+"),
    re.compile(r"\?v=\d"),
    re.compile(r"^---$"),
]


def check_hardcoded_semver(expected: str) -> list[tuple[str, int, str]]:
    """Find hardcoded X.Y.Z semver strings that should equal `expected`."""
    expected_major_minor = ".".join(expected.split(".")[:2])
    violations: list[tuple[str, int, str]] = []
    for name in HARDCODED_SCAN_TARGETS:
        p = Path(name)
        if not p.exists():
            continue
        for lineno, line in enumerate(
            p.read_text(encoding="utf-8", errors="replace").splitlines(), 1
        ):
            if any(pat.search(line) for pat in HARDCODED_SCAN_EXCEPTIONS):
                continue
            for m in re.finditer(r"\b(\d+\.\d+\.\d+(?:-[a-zA-Z0-9.]+)?)\b", line):
                found = m.group(1)
                if found != expected and found.startswith(expected_major_minor + "."):
                    violations.append((name, lineno, line.strip()))
                    break
    return violations


# Files/patterns where {{DS_VERSION}} is intentional and should NOT be flagged
# Example: downloads.html uses {{DS_VERSION}} in ZIP filename as a template placeholder
PLACEHOLDER_EXCEPTIONS: dict[str, list[str]] = {
    "downloads.html": [r"edic-design-system-skill-v\{\{DS_VERSION\}\}\.zip"],
}


def get_expected_version() -> str | None:
    """从 VERSION 文件读取最新稳定版本。"""
    if VERSION_FILE.exists():
        return VERSION_FILE.read_text(encoding="utf-8").strip().splitlines()[0].strip()
    return None


def check_html(path: Path) -> dict[str, str]:
    """返回 {资源名: ?v= 值}。"""
    text = path.read_text(encoding="utf-8", errors="replace")
    found: dict[str, str] = {}
    for match in re.finditer(r'(?:href|src)="([^"?]+\.(?:css|js))\?v=([^"]+)"', text):
        resource = match.group(1)
        version = match.group(2)
        found[resource] = version
    return found


def count_placeholders(path: Path) -> int:
    """统计文件中残留的 {{DS_VERSION}} 占位符数量。"""
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")
    return len(PLACEHOLDER_RE.findall(text))


def main() -> int:
    html_files = sorted(ROOT.glob(HTML_GLOB))
    if not html_files:
        print(f"[WARN] 未发现 HTML 文件（{HTML_GLOB}）")
        return 2

    expected = get_expected_version()
    print(f"─── 版本号同步校验 ───")
    if expected:
        print(f"期望版本（来自 VERSION）: {expected}")
    else:
        print(f"[WARN] 未发现期望版本（VERSION 文件缺失）")
        return 1

    by_resource: dict[str, dict[str, list[str]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for path in html_files:
        versions = check_html(path)
        for resource, version in versions.items():
            by_resource[resource][version].append(path.name)

    errors = 0
    warnings = 0

    for resource, version_map in sorted(by_resource.items()):
        if len(version_map) > 1:
            print(f"\n[ERROR] 资源 {resource} 版本不一致：")
            for version, files in version_map.items():
                print(f"  v{version}: {', '.join(files)}")
            errors += 1
        else:
            version = list(version_map.keys())[0]
            files = version_map[version]
            print(f"[OK] {resource} v{version}（{len(files)} 个文件）")

            if not SEMVER_RE.match(version):
                print(f"  [ERROR] 版本号格式非法：{version}")
                errors += 1

            if version != expected:
                print(f"  [ERROR] 与 VERSION {expected} 不一致（需 stamp）")
                errors += 1

    hardcoded_violations = check_hardcoded_semver(expected)
    if hardcoded_violations:
        print(f"\n[ERROR] 发现硬编码过期版本号：")
        for name, lineno, content in hardcoded_violations:
            print(f"  {name}:{lineno}: {content[:100]}")
        errors += len(hardcoded_violations)

    no_version = []
    for path in html_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in re.finditer(
            r'<(?:link[^>]+href|script[^>]+src)="(styles\.css|scripts\.js)"', text
        ):
            no_version.append((path.name, match.group(1)))
    if no_version:
        print(f"\n[WARN] 以下资源未使用 ?v= 版本号：")
        for file, resource in no_version:
            print(f"  {file}: {resource}")
        warnings += 1

    placeholder_files = []
    for name in STAMP_TARGETS:
        p = ROOT / name
        n_total = count_placeholders(p)

        # Subtract exceptions for intentional placeholders (e.g., ZIP filename templates)
        if name in PLACEHOLDER_EXCEPTIONS and p.exists():
            text = p.read_text(encoding="utf-8", errors="replace")
            for pattern in PLACEHOLDER_EXCEPTIONS[name]:
                matches = re.findall(pattern, text)
                n_total -= len(matches)

        if n_total > 0:
            placeholder_files.append((name, n_total))
    if placeholder_files:
        print(f"\n[ERROR] 以下文件残留 {{{{DS_VERSION}}}} 占位符，需 stamp：")
        for name, n in placeholder_files:
            print(f"  {name}: {n} 处")
        errors += len(placeholder_files)

    print()
    print(f"错误: {errors}  警告: {warnings}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
