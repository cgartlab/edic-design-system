#!/usr/bin/env python3
"""
Validate version-related consistency:

1. VERSION file matches the top CHANGELOG.md header [version]
2. CHANGELOG entry has at least one non-empty section (### Added / Changed / Fixed / etc.)
3. Core files exist: AGENTS.md, README.md, VERSION, tokens.json, package.json

Exit codes:
    0 = pass
    1 = blocking error
    2 = non-blocking warning
"""

import re
import sys
from pathlib import Path

VERSION_FILE = Path("VERSION")
CHANGELOG_FILE = Path("CHANGELOG.md")
AGENTS_FILE = Path("AGENTS.md")
README_FILE = Path("README.md")
TOKENS_FILE = Path("tokens.json")
PACKAGE_FILE = Path("package.json")

ALL_CORE_FILES = [
    (AGENTS_FILE, "AGENTS.md"),
    (README_FILE, "README.md"),
    (VERSION_FILE, "VERSION"),
    (TOKENS_FILE, "tokens.json"),
    (PACKAGE_FILE, "package.json"),
]


def read_version_file() -> str:
    return VERSION_FILE.read_text().strip()


def read_changelog_top_version() -> str | None:
    """
    Extract the version from the first `## [version]` or `## [version] — date`
    header in CHANGELOG.md.
    Returns None if no header found.
    """
    if not CHANGELOG_FILE.exists():
        return None
    text = CHANGELOG_FILE.read_text()
    m = re.search(r"^##\s+\[(\d+\.\d+\.\d+)\]", text, re.MULTILINE)
    if m:
        return m.group(1)
    return None


def check_changelog_has_content() -> bool:
    """
    After the top version header, check that at least one non-empty section
    (### Added / Changed / Fixed / etc.) exists before the next section or divider.
    """
    if not CHANGELOG_FILE.exists():
        return False
    text = CHANGELOG_FILE.read_text()

    # Find the top header + everything until the next top-level header or end
    m = re.search(
        r"^##\s+\[(\d+\.\d+\.\d+)\].*?\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not m:
        return False

    body = m.group(2)
    # Strip section headers and horizontal rules, then check non-whitespace remains
    body = re.sub(r"^### .+$", "", body, flags=re.MULTILINE)
    body = re.sub(r"^---+$", "", body, flags=re.MULTILINE)
    return bool(body.strip())


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []

    # 1. VERSION vs CHANGELOG header
    try:
        version = read_version_file()
    except FileNotFoundError:
        errors.append(f"VERSION file not found")
        version = None

    changelog_version = read_changelog_top_version()
    if changelog_version is None:
        warnings.append(
            "No ## [version] header found in CHANGELOG.md — cannot verify consistency"
        )
    elif version is not None and version != changelog_version:
        errors.append(
            f"VERSION ({version}) does not match CHANGELOG.md top header [{changelog_version}]"
        )

    # 2. CHANGELOG entry has content
    if changelog_version is not None:
        if not check_changelog_has_content():
            warnings.append(
                f"CHANGELOG.md top entry ## [{changelog_version}] appears empty "
                f"(no content under section headers)"
            )

    # 3. Core files exist
    for path, name in ALL_CORE_FILES:
        if not path.exists():
            errors.append(f"Core file missing: {name}")

    # Report
    for e in errors:
        print(f"✗ {e}")
    for w in warnings:
        print(f"⚠ {w}")

    if errors:
        print(f"\n✗ Validation failed ({len(errors)} error(s), {len(warnings)} warning(s))")
        sys.exit(1)
    elif warnings:
        print(f"\n⚠ Validation passed with {len(warnings)} warning(s)")
        sys.exit(2)
    else:
        print("✓ Versioning validation passed")
        sys.exit(0)


if __name__ == "__main__":
    main()
