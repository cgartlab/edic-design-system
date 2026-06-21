#!/usr/bin/env python3
"""
Bump the semantic version in VERSION and prepend a CHANGELOG entry if needed.

Usage:
    python3 tools/bump_version.py patch   # 0.1.0 → 0.1.1
    python3 tools/bump_version.py minor   # 0.1.0 → 0.2.0
    python3 tools/bump_version.py major   # 0.1.0 → 1.0.0
"""

import re
import sys
from pathlib import Path

VERSION_FILE = Path("VERSION")
CHANGELOG_FILE = Path("CHANGELOG.md")


def read_version() -> str:
    return VERSION_FILE.read_text().strip()


def write_version(version: str) -> None:
    VERSION_FILE.write_text(version + "\n")


def bump(version: str, kind: str) -> str:
    m = re.match(r"^(\d+)\.(\d+)\.(\d+)$", version)
    if not m:
        raise ValueError(f"Invalid version format: {version}")
    major, minor, patch = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if kind == "major":
        major += 1
        minor = 0
        patch = 0
    elif kind == "minor":
        minor += 1
        patch = 0
    elif kind == "patch":
        patch += 1
    else:
        raise ValueError(f"Invalid bump kind: {kind}")
    return f"{major}.{minor}.{patch}"


def changelog_has_version_header(version: str) -> bool:
    """Return True if CHANGELOG.md already contains a header for `version`."""
    if not CHANGELOG_FILE.exists():
        return False
    content = CHANGELOG_FILE.read_text()
    # matches ## [1.2.3] or ## [1.2.3] — 2026-06-22
    escaped = re.escape(version)
    pattern = re.compile(r"^##\s+\[" + escaped + r"\]", re.MULTILINE)
    return bool(pattern.search(content))


def prepend_changelog_entry(version: str) -> None:
    """Prepend an empty ## [version] — date section to CHANGELOG.md."""
    from datetime import date

    today = date.today().strftime("%Y-%m-%d")
    new_header = f"## [{version}] — {today}\n\n### 新增\n\n- \n\n---\n\n"
    content = CHANGELOG_FILE.read_text()

    # Strip any existing "## [未发布]" section before prepending
    content = re.sub(r"^## \[未发布\].*?\n---\n\n", "", content, flags=re.DOTALL)

    # Also remove the top-of-file "## [未发布]" marker if present
    content = content.lstrip()

    new_content = new_header + content
    CHANGELOG_FILE.write_text(new_content)


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} patch|minor|major")
        sys.exit(1)

    kind = sys.argv[1].lower()
    if kind not in ("patch", "minor", "major"):
        print(f"Error: kind must be patch, minor, or major; got '{kind}'")
        sys.exit(1)

    old_version = read_version()
    new_version = bump(old_version, kind)
    write_version(new_version)
    print(f"VERSION: {old_version} → {new_version}")

    if not changelog_has_version_header(new_version):
        prepend_changelog_entry(new_version)
        print(f"CHANGELOG.md: prepended ## [{new_version}] entry")
    else:
        print(f"CHANGELOG.md: ## [{new_version}] entry already exists, skipping")


if __name__ == "__main__":
    main()
