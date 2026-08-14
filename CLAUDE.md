# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**EDIC Design System** (formerly CGArtLab) — Editorial × Olive Green, a zero-runtime-dependency static design system driven by OKLch color science and design tokens. Current version: **v1.10.2**.

- **Website:** https://edic.cgartlab.com
- **License:** CC BY 4.0
- **Tech:** Pure HTML + CSS (Custom Properties + OKLch) + Vanilla JS — no build tools, no framework

## Architecture

### Core Files (the "big three")

| File | Role |
|------|------|
| `styles.css` | All design tokens (`:root` + `[data-theme="dark"]`), 20 core + 5 add-on components, animations, site shell |
| `scripts.js` | Icon rendering, token table rendering, theme toggle, scroll reveal, copy actions, tab panels |
| `tokens.json` | Structured JSON of all design tokens — source of truth for programmatic consumption |

### Key Design Decisions

1. **OKLch-only colors** — every color defined as `oklch(L C H)`. Never use hex/rgb/hsl in CSS.
2. **Token-first** — every visual value must use `var(--ds-*)`. No magic numbers (`#fff`, `16px`, etc.).
3. **BEM class naming** — `ds-component` / `ds-component--variant` / `ds-component-element`.
4. **Semantic versioning** adapted for design systems — see `docs/VERSIONING.md`.
5. **Stamp tool** — `tools/stamp_version.py` reads `VERSION` and stamps it into all HTML/MD/CSS/JS/JSON files. Always run `make stamp-version` after bumping `VERSION`.
6. **`?v=` cache busting** — all HTML references to `styles.css` and `scripts.js` include `?v=VERSION`. `validate_versions.py` checks consistency.

### Token Naming Convention

```
--ds-{category}-{name}[-{modifier}]

Categories: color | font | text | weight | leading | tracking |
            space | radius | shadow | duration | ease | bp | z | blur | glass
```

### Dark Mode

Always define both `:root` and `[data-theme="dark"]` for every color token. Dark mode never uses pure black `oklch(0% 0 0)` — use warm grey `oklch(15% 0.008 75)`.

### Icon System

All icons are inline SVG in `scripts.js` `ICONS` array. ViewBox must be `0 0 24 24`, stroke-width `1.5`, `aria-hidden="true"`. New icons must be registered in `scripts.js` and rendered via the icon system.

### Branch Workflow

- `main` — stable releases, tagged `vX.Y.Z`
- `dev-{feature-name}` — new features
- `fix-{bug-name}` — bug fixes
- `write-{topic}` — docs / content / writing
- `chore-{scope}` — refactor / perf / format / tools / deps
- `release/v<X>.<Y>.<Z>` — version release

## Common Commands

```bash
# Start local dev server
make serve                    # http://localhost:8000

# Run all 10 validators
make validate
npm run validate

# Run a single validator
make validate-tokens          # tokens.json ↔ styles.css consistency
make validate-naming          # BEM / token naming + anti-patterns
make validate-html            # HTML structure + reference validity
make validate-a11y            # Accessibility (alt, heading hierarchy, contrast)
make validate-versions        # ?v= sync with VERSION file
make validate-links           # Internal anchors + resource references

# Sync VERSION to all HTML/MD files
make stamp-version

# Preview diff before stamping
python3 tools/stamp_version.py --diff

# Check if stamp is needed
python3 tools/stamp_version.py --check

# Generate example PDFs
make generate-pdfs

# Clean temp files
make clean

# Run CI validators locally
./scripts/dev.sh validate
```

## CI / GitHub Actions

- **`.github/workflows/ci.yml`** — runs all 10 validators on push/PR/schedule (weekly Monday UTC 0:00)
- Exit codes: 0 = OK, 1 = errors (fail), 2 = warnings-only (pass)
- **`.github/workflows/release.yml`** — `release: published`-triggered: builds PDF/ZIP and uploads to the release-please-created GitHub Release

## Release Workflow

正常发布完全自动化（release-please 自动 tag + GitHub Release），无需手动执行 `git tag`：

```
Feature PR merge → main
    ↓
release-please 创建/更新 Release PR（更新 CHANGELOG.md + 版本 bump）
    ↓
人类审查 Release PR（如需润色，直接编辑 CHANGELOG.md 对应节）
    ↓
合并 Release PR
    ↓
release-please 自动：
  ① 创建 git tag vX.Y.Z（GitHub 后台签名，无需本地 GPG）
  ② 创建 GitHub Release（notes 取自 CHANGELOG.md）
    ↓
post-merge-stamp 自动：
  ① 从 release-please 的 `version` output 同步 VERSION 文件
  ② stamp_version.py 同步所有 HTML/MD 中的 `?v=` 缓存戳
    ↓
release.yml（release: published 事件触发）→ 构建 PDF/ZIP → 上传到已创建的 GitHub Release
```

紧急热修复：当自动链路不可用时，通过 `workflow_dispatch` 手动触发 `release.yml`：

```bash
gh workflow run release.yml -f version=X.Y.Z+1
```

详见 `AGENTS.md` §发布策略/§紧急热修复，以及 `docs/VERSIONING.md`。

## Adding a New Component

1. **Open an Issue** first — describe component name, use cases, variants, states.
2. **Check existing tokens** — reuse before adding new ones. If new token needed, add to both `styles.css` (`:root` + `[data-theme="dark"]`) and `tokens.json`.
3. **Implement in `styles.css`** using BEM naming, OKLch colors, `var(--ds-*)` tokens.
4. **Add preview to `docs.html`**.
5. **Update `scripts.js`** `TOKENS` array if new tokens added.
6. **Update `AGENTS.md`** component catalog.
7. **Update `CHANGELOG.md`** under `[未发布]`.
8. **Run `make validate`** — all must pass.
9. **Bump `?v=`** in all HTML files (use `make stamp-version`).

## Anti-Patterns (Never Do)

- ❌ Hard-code any color, size, or spacing value — always use `var(--ds-*)`
- ❌ Use hex/rgb/hsl — only OKLch
- ❌ Use pure black `oklch(0% 0 0)` in dark mode
- ❌ Inline `style=` except for genuinely dynamic values (stagger delays, etc.)
- ❌ Inline `onclick` — use `addEventListener`
- ❌ Introduce new hue families beyond olive + semantic colors
- ❌ Modify `company.html` or other example pages directly — they are production-grade demos
- ❌ Commit without bumping `?v=` after changing CSS/JS
- ❌ Skip `prefers-reduced-motion: reduce` handling

## Key Documentation

| File | Purpose |
|------|---------|
| `docs/VERSIONING.md` | SemVer strategy adapted for design systems, stamp tool usage |
| `docs/COMPONENT-DEVELOPMENT.md` | Full component development workflow |
| `docs/RELEASE-CHECKLIST.md` | Pre-release checklist |
| `docs/TESTING.md` | Testing strategy per validator |
| `DEVELOPMENT-GUIDE.md` | Deep technical reference (CSS architecture, token system, rendering) |
| `AGENTS.md` | Project knowledge base, component catalog, AI prompt/Skill references |
| `skills/edic-design-system/SKILL.md` | Claude Code skill — strict design system compliance rules |

## Pending Work

- See `CHANGELOG.md` `[未发布]` section for planned changes
