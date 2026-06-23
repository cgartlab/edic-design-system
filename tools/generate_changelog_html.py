#!/usr/bin/env python3
"""tools/generate_changelog_html.py — Auto-generate changelog.html from human-readable Markdown summaries.

This script reads all docs/changelog_human/v*.md files, converts them to HTML,
and replaces the content section of changelog.html.

Usage:
  python3 tools/generate_changelog_html.py          # generate
  python3 tools/generate_changelog_html.py --check   # verify changelog.html is up-to-date
  python3 tools/generate_changelog_html.py --diff   # show what would change
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHANGELOG_HUMAN_DIR = ROOT / "docs" / "changelog_human"
CHANGELOG_HTML = ROOT / "changelog.html"
VERSION_FILE = ROOT / "VERSION"

# Regex to extract version from filename like v1.7.0.md or v1.7.0-patch.md
VERSION_PATTERN = re.compile(r"v(\d+\.\d+\.\d+(?:-\d+)?(?:-[a-zA-Z0-9.]+)?)\.md$")


def extract_version(filename: str) -> str | None:
    """Extract version string from markdown filename."""
    match = VERSION_PATTERN.search(filename)
    return match.group(1) if match else None


def parse_version(version: str):
    """Parse version string into comparable tuple. Handles semantic versioning."""
    # Remove 'v' prefix if present
    v = version.lstrip("v")
    parts = []
    for part in re.split(r"[.\-]", v):
        # Try to extract numeric portion
        num_match = re.match(r"(\d+)", part)
        if num_match:
            parts.append((0, int(num_match.group(1)), part))
        else:
            parts.append((1, part, part))
    return tuple(parts)


def version_key(version: str):
    """Sort key for semantic versioning."""
    return parse_version(version)


def markdown_to_html(text: str, version: str) -> str:
    """Convert Markdown to HTML with simple transformations."""
    lines = text.strip().split("\n")
    html_parts = []
    in_list = False
    current_list_items = []

    def flush_list():
        nonlocal in_list, current_list_items
        if current_list_items:
            html_parts.append("          <ul>")
            for item in current_list_items:
                html_parts.append(f"            <li>{item}</li>")
            html_parts.append("          </ul>")
            current_list_items = []
        in_list = False

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Empty line - paragraph break
        if not line:
            if in_list:
                flush_list()
            html_parts.append("")
            i += 1
            continue

        # H2 heading (## 新增 / ## 修复 / ## 变更)
        if line.startswith("## "):
            if in_list:
                flush_list()
            heading_text = line[3:].strip()
            html_parts.append(f"          <h3>{heading_text}</h3>")
            i += 1
            continue

        # List item (- item)
        if line.startswith("- "):
            if in_list and lines[i - 1].strip().startswith("- "):
                current_list_items.append(process_inline(line[2:]))
            else:
                if in_list:
                    flush_list()
                in_list = True
                current_list_items.append(process_inline(line[2:]))
            i += 1
            continue

        # Fallback - treat as paragraph
        if in_list:
            flush_list()
        if line:
            html_parts.append(f"          <p>{process_inline(line)}</p>")

        i += 1

    # Flush any remaining list
    if in_list:
        flush_list()

    return "\n".join(html_parts)


def process_inline(text: str) -> str:
    """Process inline elements: bold, code."""
    # **bold** -> <strong>bold</strong>
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # `code` -> <code>code</code>
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    return text


def generate_section_id(version: str) -> str:
    """Generate section ID from version string (remove dots and dashes)."""
    return "v" + version.replace(".", "").replace("-", "")


def read_changelog_files():
    """Read all markdown files from changelog_human directory."""
    if not CHANGELOG_HUMAN_DIR.exists():
        return []

    files = sorted(
        CHANGELOG_HUMAN_DIR.glob("v*.md"), key=lambda f: extract_version(f.name) or ""
    )

    versions_data = []
    for filepath in files:
        version = extract_version(filepath.name)
        if not version:
            continue
        content = filepath.read_text(encoding="utf-8")
        versions_data.append(
            {"version": version, "filepath": filepath, "content": content}
        )

    # Sort by semantic version
    versions_data.sort(key=lambda x: version_key(x["version"]))
    return versions_data


def generate_nav(versions_data: list) -> str:
    """Generate left navigation HTML."""
    nav_items = []
    for idx, vdata in enumerate(versions_data, 1):
        version = vdata["version"]
        section_id = generate_section_id(version)
        num = f"{idx:02d}"
        nav_items.append(
            f'              <li><a class="ds-pagenav-link" href="#{section_id}">'
            f'<span class="ds-pagenav-num">{num}</span>'
            f'<span class="ds-pagenav-text">v{version}</span></a></li>'
        )

    return "\n".join(nav_items)


def generate_sections(versions_data: list) -> str:
    """Generate HTML sections for each version."""
    sections = []
    for vdata in versions_data:
        version = vdata["version"]
        content = vdata["content"]
        section_id = generate_section_id(version)

        # Extract date from file or use placeholder
        date_match = re.search(r"\((\d{4}-\d{2}-\d{2})\)", content)
        date_str = date_match.group(1) if date_match else "2026-06-23"

        sections.append(f'        <section class="ds-doc-block" id="{section_id}">')
        sections.append(f"          <h2>v{version} — {date_str}</h2>")

        # Extract description from first paragraph, skipping date lines
        lines = content.strip().split("\n")
        first_para = None
        remaining_lines = []
        date_pattern = re.compile(r"^\(\d{4}-\d{2}-\d{2}\)$")

        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            # Skip standalone date lines
            if date_pattern.match(stripped):
                continue
            if stripped.startswith("## "):
                remaining_lines.append(line)
            elif first_para is None and not stripped.startswith("-"):
                first_para = stripped
            else:
                remaining_lines.append(line)

        if first_para:
            sections.append(f"          <p>{process_inline(first_para)}</p>")

        # Convert remaining content to HTML
        if remaining_lines:
            html_content = markdown_to_html("\n".join(remaining_lines), version)
            sections.append(html_content)

        sections.append("        </section>")

    return "\n".join(sections)


def get_current_html_nav() -> str:
    """Extract current navigation from changelog.html."""
    if not CHANGELOG_HTML.exists():
        return ""

    content = CHANGELOG_HTML.read_text(encoding="utf-8")
    # Find nav list
    match = re.search(r'<ol class="ds-pagenav-list">(.*?)</ol>', content, re.DOTALL)
    return match.group(1) if match else ""


def update_changelog_html():
    """Main function to update changelog.html."""
    versions_data = read_changelog_files()

    if not versions_data:
        print("Error: No version files found in docs/changelog_human/", file=sys.stderr)
        sys.exit(1)

    # Generate new content
    new_nav = generate_nav(versions_data)
    new_sections = generate_sections(versions_data)

    if not CHANGELOG_HTML.exists():
        print(f"Error: {CHANGELOG_HTML} not found", file=sys.stderr)
        sys.exit(1)

    html_content = CHANGELOG_HTML.read_text(encoding="utf-8")

    # Check if markers exist
    if "<!-- CHANGELOG_CONTENT_START -->" not in html_content:
        print("Error: Start marker not found in changelog.html", file=sys.stderr)
        print(
            'Please add <!-- CHANGELOG_CONTENT_START --> before <div class="ds-prose">',
            file=sys.stderr,
        )
        sys.exit(1)

    if "<!-- CHANGELOG_CONTENT_END -->" not in html_content:
        print("Error: End marker not found in changelog.html", file=sys.stderr)
        print(
            "Please add <!-- CHANGELOG_CONTENT_END --> after the closing </div> of the prose section",
            file=sys.stderr,
        )
        sys.exit(1)

    # Replace navigation list content
    html_content = re.sub(
        r'<ol class="ds-pagenav-list">.*?</ol>',
        f'<ol class="ds-pagenav-list">\n{new_nav}\n            </ol>',
        html_content,
        flags=re.DOTALL,
    )

    # Replace prose content between markers
    pattern = r"<!-- CHANGELOG_CONTENT_START -->.*?<!-- CHANGELOG_CONTENT_END -->"
    replacement = f"""<!-- CHANGELOG_CONTENT_START -->
        <div class="ds-prose">
{new_sections}
        </div>
        <!-- CHANGELOG_CONTENT_END -->"""

    new_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

    # Write updated content
    CHANGELOG_HTML.write_text(new_html, encoding="utf-8")
    print(f"Updated {CHANGELOG_HTML}")


def check_changelog_html() -> bool:
    """Check if changelog.html is up-to-date. Returns True if up-to-date."""
    versions_data = read_changelog_files()

    if not versions_data:
        print("Error: No version files found", file=sys.stderr)
        sys.exit(1)

    # Generate expected content
    new_nav = generate_nav(versions_data)
    new_sections = generate_sections(versions_data)

    if not CHANGELOG_HTML.exists():
        print("Error: changelog.html not found", file=sys.stderr)
        sys.exit(1)

    html_content = CHANGELOG_HTML.read_text(encoding="utf-8")

    # Extract current navigation
    nav_match = re.search(
        r'<ol class="ds-pagenav-list">(.*?)</ol>', html_content, re.DOTALL
    )
    current_nav = nav_match.group(1).strip() if nav_match else ""

    # Extract current prose content
    prose_match = re.search(
        r'<div class="ds-prose">(.*?)</div>', html_content, re.DOTALL
    )
    current_prose = prose_match.group(1).strip() if prose_match else ""

    # Compare
    expected_nav = new_nav.strip()
    expected_prose = new_sections.strip()

    if current_nav != expected_nav or current_prose != expected_prose:
        return False
    return True


def show_diff():
    """Show what would change if update was run."""
    versions_data = read_changelog_files()

    if not versions_data:
        print("Error: No version files found", file=sys.stderr)
        sys.exit(1)

    new_nav = generate_nav(versions_data)
    new_sections = generate_sections(versions_data)

    print("=== Navigation would change to: ===")
    print(new_nav)
    print("\n=== Sections would change to: ===")
    print(new_sections)


def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "--check":
            if check_changelog_html():
                print("changelog.html is up-to-date")
                sys.exit(0)
            else:
                print("changelog.html needs regeneration")
                sys.exit(2)
        elif arg == "--diff":
            show_diff()
            sys.exit(0)
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            print(
                "Usage: python3 tools/generate_changelog_html.py [--check|--diff]",
                file=sys.stderr,
            )
            sys.exit(1)

    update_changelog_html()
    sys.exit(0)


if __name__ == "__main__":
    main()
