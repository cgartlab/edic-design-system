#!/usr/bin/env python3
"""Validate that .release-please-manifest.json version matches VERSION file."""
import json
import sys

def main():
    with open("VERSION", "r", encoding="utf-8") as f:
        version = f.read().strip()

    with open(".release-please-manifest.json", "r", encoding="utf-8") as f:
        manifest = json.load(f)

    manifest_version = manifest.get(".", "")

    if manifest_version != version:
        print(
            f"[ERROR] Manifest version ({manifest_version}) != "
            f"VERSION ({version}). Run `make stamp-version` to sync."
        )
        sys.exit(1)

    print(f"[OK] Manifest version ({manifest_version}) == VERSION ({version})")
    sys.exit(0)


if __name__ == "__main__":
    main()
