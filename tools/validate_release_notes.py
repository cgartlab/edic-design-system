#!/usr/bin/env python3
"""tools/validate_release_notes.py — Verify CHANGELOG.md has notes for the release.

Single-source model: CHANGELOG.md (maintained by release-please) is the only
changelog source. This validator confirms CHANGELOG.md contains a version
section for the version being released, so the website changelog page
(generated from CHANGELOG.md) and the GitHub Release notes are non-empty.

Exit 1 if the version section is missing — blocks the Release PR from merging.

Usage:
  python3 tools/validate_release_notes.py          # validate
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT / "VERSION"
MANIFEST_FILE = ROOT / ".release-please-manifest.json"
CHANGELOG_MD = ROOT / "CHANGELOG.md"


def read_version() -> str:
    """Read version from release-please manifest first, fall back to VERSION file.

    On release-please branches, the manifest has the correct new version (e.g. 1.8.1),
    while the VERSION file may still be the old version."""
    if MANIFEST_FILE.exists():
        try:
            data = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
            if "." in data:
                return data["."]
        except (json.JSONDecodeError, KeyError):
            pass
    text = VERSION_FILE.read_text(encoding="utf-8").strip()
    return text.splitlines()[0].strip()


def changelog_has_version(version: str) -> bool:
    """True if CHANGELOG.md contains a '## [version]' section header."""
    if not CHANGELOG_MD.exists():
        return False
    # Match: ## [1.8.1] ...  (with or without compare-url / date)
    pattern = re.compile(
        r"^##\s*\[?" + re.escape(version) + r"\]?",
        re.MULTILINE,
    )
    return bool(pattern.search(CHANGELOG_MD.read_text(encoding="utf-8")))


def main() -> int:
    version = read_version()

    if changelog_has_version(version):
        print(f"[OK] CHANGELOG.md contains a release section for v{version}.")
        return 0

    print(f"[FATAL] CHANGELOG.md has no section for v{version}.")
    print( "        release-please normally writes this automatically.")
    print( "        Ensure the Release PR's CHANGELOG.md update is present before releasing.")
    print( "        (The website changelog page and GitHub Release notes are both")
    print( "         generated from CHANGELOG.md — an empty section means empty notes.)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
