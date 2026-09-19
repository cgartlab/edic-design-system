#!/usr/bin/env python3
"""scripts/package_release.py — Package EDIC Design System distribution ZIP.

Creates assets/downloads/edic-design-system-v{VERSION}.zip containing:
  - styles.css          (core stylesheet)
  - scripts.js          (progressive enhancement)
  - tokens.json        (machine-readable design tokens)
  - icons.svg          (icon sprite)
  - SKILL.md           (agent skill instructions)
  - system-prompt.md   (full system prompt)
  - quick-prompt.md    (quick prompt)
  - README.md          (installation guide)

Usage:
  python3 scripts/package_release.py          # package
  python3 scripts/package_release.py --check  # verify ZIP is up-to-date
  python3 scripts/package_release.py --diff    # show stale files
"""
from __future__ import annotations

import hashlib
import sys
import zipfile
from pathlib import Path
import argparse
import re

ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT / "VERSION"
DIST_DIR = ROOT / "assets" / "downloads"

SOURCES: list[tuple[Path, str]] = [
    (ROOT / "styles.css", "styles.css"),
    (ROOT / "scripts.js", "scripts.js"),
    (ROOT / "tokens.json", "tokens.json"),
    (ROOT / "icons.svg", "icons.svg"),
    (ROOT / "skills" / "edic-design-system" / "SKILL.md", "SKILL.md"),
    (ROOT / "prompts" / "system-prompt.md", "system-prompt.md"),
    (ROOT / "prompts" / "quick-prompt.md", "quick-prompt.md"),
    (ROOT / "README.md", "README.md"),
]


def read_version() -> str:
    """Read version from VERSION file."""
    try:
        text = VERSION_FILE.read_text(encoding="utf-8").strip().splitlines()[0].strip()
        if not text:
            raise ValueError("VERSION 文件为空")
        if not re.match(r"^[0-9]+\.[0-9]+\.[0-9]+(?:-[a-zA-Z0-9.]+)?$", text):
            raise ValueError(f"非法版本号: {text!r}")
        return text
    except OSError as e:
        raise RuntimeError(f"无法读取 VERSION 文件: {e}") from e


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def preflight() -> list[str]:
    """Check all source files exist. Returns list of missing files."""
    missing = []
    for src, _ in SOURCES:
        if not src.exists():
            missing.append(str(src))
    return missing


def build_zip() -> None:
    """Package sources into distribution ZIP."""
    version = read_version()
    missing = preflight()
    if missing:
        print("ERROR: missing required files:")
        for f in missing:
            print(f"  - {f}")
        sys.exit(1)

    zip_name = f"edic-design-system-v{version}.zip"
    zip_path = DIST_DIR / zip_name
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    zip_path.unlink(missing_ok=True)

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for src, arcname in SOURCES:
            zf.write(src, arcname)

    size = zip_path.stat().st_size
    print(f"✅ {zip_path} created ({size} bytes)")


def check_zip() -> int:
    """Verify ZIP contents match source files. Returns 0 if OK, 2 if stale."""
    version = read_version()
    zip_name = f"edic-design-system-v{version}.zip"
    zip_path = DIST_DIR / zip_name

    missing = preflight()
    if missing:
        print("ERROR: missing required files:")
        for f in missing:
            print(f"  - {f}")
        sys.exit(1)

    if not zip_path.exists():
        print(f"ERROR: {zip_path} does not exist — run without --check first")
        return 2

    with zipfile.ZipFile(zip_path, "r") as zf:
        actual_names = set(zf.namelist())
        expected_names = {arcname for _, arcname in SOURCES}

        if actual_names != expected_names:
            print("ERROR: ZIP contents mismatch")
            print(f"  expected: {sorted(expected_names)}")
            print(f"  actual:   {sorted(actual_names)}")
            return 2

        for src, arcname in SOURCES:
            expected_hash = sha256(src)
            actual_hash = hashlib.sha256(zf.read(arcname)).hexdigest()
            if actual_hash != expected_hash:
                print(f"ERROR: {arcname} — content hash mismatch (stale ZIP)")
                return 2

    print(f"✅ {zip_path} — contents match sources (OK)")
    return 0


def diff() -> int:
    """Show which files would trigger a rebuild."""
    version = read_version()
    zip_name = f"edic-design-system-v{version}.zip"
    zip_path = DIST_DIR / zip_name

    missing = preflight()
    if missing:
        print("Missing files (would fail):")
        for f in missing:
            print(f"  - {f}")
        return 2

    if not zip_path.exists():
        print(f"{zip_path} does not exist — all files would be packaged")
        return 2

    stale: list[str] = []
    with zipfile.ZipFile(zip_path, "r") as zf:
        for src, arcname in SOURCES:
            expected_hash = sha256(src)
            actual_hash = hashlib.sha256(zf.read(arcname)).hexdigest()
            if actual_hash != expected_hash:
                stale.append(arcname)

    if stale:
        print("Stale files (ZIP would change):")
        for name in stale:
            print(f"  - {name}")
        return 2
    else:
        print("ZIP is up-to-date — no changes needed")
        return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Package EDIC distribution ZIP")
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