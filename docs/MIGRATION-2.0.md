# Migrating to EDIC Design System 2.0

## Default path

Most projects can upgrade without changing markup. EDIC 2.0 is additive:
existing `--ds-*` tokens, component classes, SVG icons, `styles.css`, and
`scripts.js` remain valid.

Keep the same integration pattern:

```html
<link rel="stylesheet" href="styles.css?v=2.0.0">
<script src="scripts.js?v=2.0.0"></script>
```

## What changed

- Token coverage expanded across motion, delay, z-index, depth, border,
  opacity, grid, breakpoint, skeleton, and overlay categories.
- Semantic aliases were added while preserving original raw and 1.x names.
- Component coverage expanded to 39 core component families, including
  table, description list, stat, timeline, breadcrumb, pagination, sidebar
  navigation, steps, toast, alert, progress, skeleton, popover, tooltip,
  drawer, and command palette.
- Icon coverage expanded to 209 icons in `icons.svg` and `icons.json`.
- `edic-manifest.json`, `AGENT-GUIDE.md`, and `SKILL.md` provide machine-
  and agent-readable constraints.
- `npm run audit` now aggregates validators, visual baseline, size checks,
  changelog checks, and unit tests.

## Optional improvements

1. Prefer semantic aliases for new work, for example `--ds-color-surface-primary`
   instead of reaching for a raw palette token.
2. Use `icons.json` as the source for icon search and recommendation.
3. Follow `AGENT-GUIDE.md` when generating EDIC UI in prompts or agents.
4. Use `docs.html#visual-components` as the compatibility reference for the
   expanded component families.

## Compatibility notes

- No 1.x token, component, or icon has been removed.
- The CSS prefix remains `--ds-` and the class prefix remains `ds-`.
- No runtime framework dependency is required.
- Dark mode continues to use `data-theme="dark"` and system preferences.
