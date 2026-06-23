#!/usr/bin/env python3
"""scripts/package_skill.py — Package EDIC Design System Skill for distribution.

Creates assets/downloads/edic-design-system-skill.zip containing:
  - SKILL.md      (agent skill instructions)
  - README.md     (installation guide)
  - tokens.json   (design tokens reference)

Usage:
  python3 scripts/package_skill.py          # package
  python3 scripts/package_skill.py --check  # verify ZIP matches sources
  python3 scripts/package_skill.py --diff  # show what would change
"""

from __future__ import annotations

import hashlib
import os
import sys
import zipfile
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT / "VERSION"
SKILL_DIR = ROOT / "skills" / "edic-design-system"
DIST_DIR = ROOT / "assets" / "downloads"
PKG_NAME = f"edic-design-system-skill-v{VERSION_FILE.read_text().strip().splitlines()[0].strip()}"
ZIP_PATH = DIST_DIR / f"{PKG_NAME}.zip"
SOURCES = [
    SKILL_DIR / "SKILL.md",
    SKILL_DIR / "README.md",
    ROOT / "tokens.json",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def preflight() -> list[str]:
    """Check all source files exist. Returns list of missing files."""
    missing = []
    for src in SOURCES:
        if not src.exists():
            missing.append(str(src))
    return missing


def build_zip() -> None:
    """Package sources into ZIP."""
    missing = preflight()
    if missing:
        print("ERROR: missing required files:")
        for f in missing:
            print(f"  - {f}")
        sys.exit(1)

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for src in SOURCES:
            zf.write(src, src.name)

    size = ZIP_PATH.stat().st_size
    print(f"✅ {ZIP_PATH} created ({size} bytes)")


def check_zip() -> int:
    """Verify ZIP contents match source files. Returns 0 if OK, 2 if stale."""
    missing = preflight()
    if missing:
        print("ERROR: missing required files:")
        for f in missing:
            print(f"  - {f}")
        sys.exit(1)

    if not ZIP_PATH.exists():
        print(f"ERROR: {ZIP_PATH} does not exist — run without --check first")
        return 2

    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        actual_names = set(zf.namelist())
        expected_names = {src.name for src in SOURCES}

        if actual_names != expected_names:
            print("ERROR: ZIP contents mismatch")
            print(f"  expected: {sorted(expected_names)}")
            print(f"  actual:   {sorted(actual_names)}")
            return 2

        for src in SOURCES:
            expected_hash = sha256(src)
            with zipfile.ZipFile(ZIP_PATH, "r") as zf_check:
                actual_bytes = zf_check.read(src.name)
                actual_hash = hashlib.sha256(actual_bytes).hexdigest()
                if actual_hash != expected_hash:
                    print(f"ERROR: {src.name} — content hash mismatch (stale ZIP)")
                    return 2

    print(f"✅ {ZIP_PATH} — contents match sources (OK)")
    return 0


def diff() -> int:
    """Show which files would trigger a rebuild."""
    missing = preflight()
    if missing:
        print("Missing files (would fail):")
        for f in missing:
            print(f"  - {f}")
        return 2

    if not ZIP_PATH.exists():
        print(f"{ZIP_PATH} does not exist — all files would be packaged")
        return 2

    stale: list[str] = []
    with zipfile.ZipFile(ZIP_PATH, "r") as zf:
        for src in SOURCES:
            expected_hash = sha256(src)
            actual_hash = hashlib.sha256(zf.read(src.name)).hexdigest()
            if actual_hash != expected_hash:
                stale.append(src.name)

    if stale:
        print("Stale files (ZIP would change):")
        for name in stale:
            print(f"  - {name}")
        return 2
    else:
        print("ZIP is up-to-date — no changes needed")
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Package EDIC Skill ZIP")
    parser.add_argument("--check", action="store_true", help="verify ZIP is up-to-date")
    parser.add_argument("--diff", action="store_true", help="show stale files")
    args = parser.parse_args()

    if args.check:
        return check_zip()
    if args.diff:
        return diff()
    build_zip()
    return 0


if __name__ == "__main__":
    sys.exit(main())
