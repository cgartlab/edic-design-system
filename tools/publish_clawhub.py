#!/usr/bin/env python3
"""
Prepare and validate the EDIC Design System skill package for ClawHub publishing.

ClawHub (the OpenClaw skill registry) publishes from a skill *directory*
containing a valid SKILL.md — not a zip. This helper does the repo-specific
work before CI runs `clawhub skill publish`:
  1. extract assets/downloads/edic-design-system-skill-v{VERSION}.zip into a clean directory
  2. validate required ClawHub frontmatter (name / description / version)
  3. HARD GUARD: SKILL.md name must equal the unique publish ID `edic-design-system`
  4. ensure SKILL.md version matches the VERSION file
  5. optionally write a reader-friendly update summary from the CHANGELOG.md
     section for this version (passed to `clawhub skill publish --changelog`):
     commit hashes / markdown links / bold-code markers are stripped so the
     published summary reads as plain prose.

It does not contact ClawHub and does not need the API token. CI still runs
`clawhub login`, `clawhub whoami`, `clawhub skill publish --dry-run`, and
`clawhub skill publish`.

Usage:
    python3 tools/publish_clawhub.py prepare \
        assets/downloads/edic-design-system-skill-v2.8.0.zip \
        --out dist/clawhub-edic \
        --changelog-out dist/clawhub-changelog.txt
"""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

# The unique publish ID on ClawHub — never let a typo create a second skill.
EXPECTED_SLUG = "edic-design-system"

# ClawHub requires a portable `name`: 1-64 lowercase letters, digits, or hyphens.
NAME_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$|^[a-z0-9]$")
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$"
)
FOLD_MARKERS = (">-", ">", "|-", "|")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    sys.exit(1)


def read_frontmatter(path: Path) -> dict[str, str]:
    """Read top-level YAML frontmatter, including folded scalars (description: >-)."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md missing YAML frontmatter")

    fields: dict[str, str] = {}
    lines = match.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line or line.startswith("#"):
            i += 1
            continue
        if line[0] in " \t":
            # Nested key (e.g. metadata.*) — only top-level fields are read here.
            i += 1
            continue
        if ":" not in line:
            fail(f"invalid SKILL.md frontmatter line: {line}")
        key, value = line.split(":", 1)
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        if value in FOLD_MARKERS:
            parts: list[str] = []
            i += 1
            while i < len(lines) and lines[i] and lines[i][0] in " \t":
                parts.append(lines[i].strip())
                i += 1
            fields[key.strip()] = " ".join(parts)
            continue
        fields[key.strip()] = value
        i += 1
    return fields


def validate_frontmatter(fields: dict[str, str]) -> str:
    """Validate ClawHub-required frontmatter; return the ClawHub slug (= name)."""
    required = ("name", "description", "version")
    missing = [field for field in required if not fields.get(field)]
    if missing:
        fail(f"SKILL.md missing required ClawHub field(s): {', '.join(missing)}")

    name = fields["name"]
    if not (1 <= len(name) <= 64):
        fail(f"name must be 1-64 chars, got {len(name)}")
    if not NAME_RE.fullmatch(name):
        fail(f"name must be lowercase kebab-case [a-z0-9-], got {name!r}")
    if name != EXPECTED_SLUG:
        fail(
            f"SKILL.md name {name!r} != unique publish ID {EXPECTED_SLUG!r} — "
            "refusing to publish a differently-identified skill"
        )

    version = fields["version"]
    if not SEMVER_RE.fullmatch(version):
        fail(f"version must be valid SemVer, got {version!r}")

    description = fields["description"]
    if len(description) < 10:
        fail(
            f"description too short ({len(description)} chars) — "
            "ClawHub uses it as the search summary"
        )

    print(f"ClawHub metadata ok: {name} ({name}@{version}, description {len(description)} chars)")
    return name


def extract_skill_zip(archive: Path, out_dir: Path) -> None:
    if not archive.is_file():
        fail(f"skill package not found: {archive}")

    out_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as zf:
        zf.extractall(out_dir)

    skill_md = out_dir / "SKILL.md"
    if not skill_md.is_file():
        fail("extracted skill package has no SKILL.md")


def friendly_changelog(changelog_path: Path, version: str) -> str:
    """Reader-friendly update summary for the CHANGELOG section of `version`.

    Produces plain prose suitable for `clawhub skill publish --changelog`:
      * drops commit-hash references (63bc6fa style links)
      * turns PR references into plain (#123)
      * unwraps **bold** / `code` / other markdown links
      * demotes ### headings to plain lines and bullets to "·"
    """
    text = changelog_path.read_text(encoding="utf-8")
    parts = re.split(r"^## ", text, flags=re.MULTILINE)
    body = ""
    for part in parts[1:]:
        if part.startswith(f"[{version}]"):
            body = "\n".join(part.splitlines()[1:])
            break
    if not body:
        fail(f"CHANGELOG.md has no section for v{version}")

    out: list[str] = []
    for line in body.splitlines():
        s = line.rstrip()
        if not s.strip():
            continue
        # commit refs: " ([63bc6fa](url))" → remove entirely
        s = re.sub(r"\s*\(\[[0-9a-f]{7,40}\]\([^)]*\)\)", "", s)
        # PR refs: "([#297](url))" → "(#297)"
        s = re.sub(r"\(\[#(\d+)\]\([^)]*\)\)", r"(#\1)", s)
        # remaining markdown links: [text](url) → text
        s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)
        # headings → plain text
        s = re.sub(r"^#{1,6}\s*", "", s)
        # bold / code markers → plain text
        s = s.replace("**", "").replace("`", "")
        # bullets "* " / "- " → "· "
        s = re.sub(r"^(\s*)[*-]\s+", r"\1· ", s)
        out.append(s.strip())

    summary = "\n".join(out).strip()
    if not summary:
        fail(f"CHANGELOG.md section for v{version} produced an empty summary")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare EDIC Design System for ClawHub publish")
    parser.add_argument("command", choices=("prepare",))
    parser.add_argument("skill_zip", type=Path)
    parser.add_argument("--out", type=Path, required=True, help="Directory to publish from")
    parser.add_argument("--changelog-out", type=Path, help="File for publish --changelog (reader-friendly summary)")
    parser.add_argument("--version", help="Expected version; defaults to VERSION file")
    args = parser.parse_args()

    repo_root = Path.cwd()
    version = args.version
    if not version:
        version_file = repo_root / "VERSION"
        if not version_file.is_file():
            fail("VERSION file not found; pass --version")
        version = version_file.read_text(encoding="utf-8").strip()

    extract_skill_zip(args.skill_zip.resolve(), args.out.resolve())
    fields = read_frontmatter(args.out.resolve() / "SKILL.md")
    slug = validate_frontmatter(fields)

    if fields["version"] != version:
        fail(f"SKILL.md version {fields['version']} != VERSION {version}")

    if args.changelog_out:
        summary = friendly_changelog(repo_root / "CHANGELOG.md", version)
        args.changelog_out.parent.mkdir(parents=True, exist_ok=True)
        args.changelog_out.write_text(summary + "\n", encoding="utf-8")

    print(f"Publish directory: {args.out.resolve()}")
    print(f"ClawHub slug: {slug}  (publish as @<owner>/{slug})")
    if args.changelog_out:
        print(f"Changelog file: {args.changelog_out.resolve()}")


if __name__ == "__main__":
    main()
