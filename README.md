# EDIC Design System

Editorial Design Interface for Content. A framework-agnostic design system for building warm, restrained, ordered interfaces — with OKLch color science and design tokens. For humans and AI alike: even if you don't know design, EDIC helps any AI assistant produce professional-grade interfaces and documents.

**Site:** https://edic.cgartlab.com
[![Version](https://img.shields.io/github/release/cgartlab/edic-design-system.svg)](https://github.com/cgartlab/edic-design-system/releases/latest)
**License:** CC BY 4.0

---

## What it is

- **200+ design tokens** — color, typography, spacing, radius, shadow, motion; change once, update everywhere.
- **20 core + 5 add-on components** — semantic `ds-*` classes with full dark-mode coverage.
- **100 SVG icons** — 1.5px stroke, `aria-hidden`, inline-rendered from `scripts.js`.
- **OKLch-only colors** — perceptually uniform, no more hex/rgb guesswork.
- **Zero runtime dependencies** — pure HTML/CSS/JS. Use anywhere: React, Vue, Svelte, email, print.
- **AI-ready** — prompts and Skill package in `prompts/` and `skills/edic-design-system/`. No design background needed — just tell the AI what you want.
- **Engineering governance** — 6 Python validators, CI on every PR/push, process docs in `docs/`.

---

## File layout

```
styles.css         — all tokens, components, dark mode, animations
scripts.js        — icons, token table, theme toggle, scroll reveal, copy
tokens.json       — structured token data (JSON)
VERSION           — single-line version source of truth
favicon.svg       — site icon (pen-nib monogram)

index.html — homepage
docs.html         — usage guide + visual catalog (live component previews)
prompts.html      — AI prompts & Skill
downloads.html    — PDF references, token exports, brand assets
terms.html — CC BY 4.0 license

blog.html         — article layout with TOC
company.html      — company landing page
resume.html      — printable A4 resume
report.html       — multi-page report layout

prompts/                      — system-prompt.md, quick-prompt.md
skills/edic-design-system/     — SKILL.md (Claude Code agent package)
docs/ — VERSIONING, COMPONENT-DEVELOPMENT, TESTING, RELEASE-CHECKLIST
tools/                         — validate_*.py (tokens, naming, html, a11y, versions, links)
scripts/                       — lint.py (unified validator), build.py (pipeline), dev.sh, dev.ps1, pre-commit.sh
.github/ — issue templates, PR template, CI workflow
```

---

## Quick start

```html
<!doctype html>
<html lang="zh-CN" data-theme="">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <button class="ds-btn ds-btn--primary">Get started</button>
    <script src="scripts.js"></script>
  </body>
</html>
```

Full docs at https://edic.cgartlab.com/docs.html

---

## Local development

```bash
make serve     # http://localhost:8000
make lint      # unified lint (10 validators, one command)
make build     # full pipeline: lint → stamp → icons → PDFs → SKILL zip
make validate  # all 10 validators individually
make clean     # remove temp files
```

All validators pass before merge; CI runs on every PR and push.

---

## Theme

Three modes — `system` (follows OS preference), `light`, `dark` — toggled via the navbar button or mobile floating button. Choice persists in localStorage.

---

## Deploy to GitHub Pages

Repository includes `CNAME` (`edic.cgartlab.com`) and `.nojekyll`.

1. **Settings → Pages** — Source: Deploy from branch `main`, directory `/ (root)`.
2. **DNS** — Add a CNAME record for `edic` pointing to `cgartlab.github.io`.
3. Wait for certificate, then visit https://edic.cgartlab.com.

---

## License

CC BY 4.0 — free to use, modify, and distribute with attribution. See `terms.html` or https://creativecommons.org/licenses/by/4.0/.test: 冒烟测试
