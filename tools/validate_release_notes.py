#!/usr/bin/env python3
"""tools/validate_release_notes.py — Verify human-readable release notes exist.

Checks that docs/changelog_human/v{VERSION}.md exists for the current release.
Exit 1 if missing — blocks the Release PR from merging.

Usage:
  python3 tools/validate_release_notes.py          # validate
  python3 tools/validate_release_notes.py --check   # CI mode (returns 0 even if missing)
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT / "VERSION"
CHANGELOG_HUMAN_DIR = ROOT / "docs" / "changelog_human"


def read_version() -> str:
    text = VERSION_FILE.read_text(encoding="utf-8").strip()
    return text.splitlines()[0].strip()


def main() -> int:
    version = read_version()
    md_file = CHANGELOG_HUMAN_DIR / f"v{version}.md"

    if md_file.exists():
        print(
            f"[OK] Human-readable release notes found: docs/changelog_human/v{version}.md"
        )
        return 0
    else:
        print(f"[FATAL] Missing human-readable release notes for v{version}")
        print(
            f"        Please create docs/changelog_human/v{version}.md before releasing."
        )
        print(
            f"        This file should contain a concise human-readable summary of changes."
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
