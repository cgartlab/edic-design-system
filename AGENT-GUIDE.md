# EDIC Design System — Agent Guide

> Read this file before producing any EDIC UI. Companion machine-readable data:
> [edic-manifest.json](./edic-manifest.json), [tokens.json](./tokens.json),
> [icons.svg](./icons.svg), [icons.json](./icons.json).

## What EDIC is

EDIC is a static, framework-agnostic design system. Its output is pure
HTML/CSS/JS: no runtime dependency, no build step. The visual language is
editorial restraint with a warm paper background, serif headings, sans body
text, and an olive-green accent.

## Non-negotiable rules

1. Use `var(--ds-*)` tokens for every web/UI visual value. No hardcoded hex/rgb/hsl in stylesheet component rules.
2. Web/UI color tokens are OKLch. Bare `oklch()` is only allowed inside `:root`
   token declarations and `@keyframes`.
3. Spacing, type size, radius, shadow, and motion come from tokens.
4. Email and rich-text output is the compatibility exception: use inline sRGB static styles, not `var(--ds-*)` or `oklch()`.
5. Every color component needs a `[data-theme="dark"]` appearance.
6. Dark mode uses warm gray, never pure black.
7. Use BEM classes: `ds-{component}`, `ds-{component}--{variant}`,
   `ds-{component}-{element}`. Never write a dangling modifier such as
   `.ds-card a--active`.
8. Interactive elements must be keyboard accessible and carry ARIA roles and
   states. Icon-only buttons need `aria-label`; decorative SVG needs
   `aria-hidden="true"`.
9. One `<h1>` per page; do not skip heading levels.
10. Do not overwrite EDIC token variables in consumer projects. Override only
   through documented theme hooks.
11. Do not delete or rename existing tokens, components, or icons. Mark legacy
    items `deprecated` when a v2 alternative exists.
12. Do not introduce a runtime framework. Output remains static HTML/CSS/JS.

## Prefer semantic tokens

When both a semantic alias and a raw category token exist, use the semantic
alias first. Examples:

```css
.my-surface {
  background: var(--ds-color-surface);
  color: var(--ds-color-fg);
  border-color: var(--ds-color-border);
}
```

If a token does not exist, define it once in `:root` plus the dark override,
then add it to `tokens.json` and `scripts.js` TOKENS.

## Semantic token aliases

EDIC keeps the compatible `--ds-*` prefix and adds semantic aliases.
When choosing a token, prefer this order:

1. semantic alias, for example `--ds-color-surface-primary`;
2. established component-safe token, for example `--ds-color-surface`;
3. raw scale token, for example `--ds-color-olive-400`, only when the raw
   value is explicitly needed.

New alias categories include border width/style/radius aliases, depth aliases,
delay and motion aliases, opacity and state aliases, focus aliases, skeleton
aliases, grid aliases, gutter aliases, and breakpoint aliases.

## Component contract

Every new component must include:

- default, hover, `:focus-visible`, `:active`, and disabled states where
  applicable;
- dark-mode adaptation through tokens;
- keyboard navigation notes and ARIA attributes;
- a docs.html preview and, when practical, an `examples/components/*.html`
  page;
- CSS before HTML, so `validate-cssref` stays green.

## Icons

- Add icons to the `ICONS` array in `scripts.js`, never directly to
  `icons.svg`.
- Run the generator after adding icons so `icons.svg` stays in sync.
- Icon SVG uses `viewBox="0 0 24 24"`, `fill="none"`,
  `stroke="currentColor"`, `stroke-width="1.5"`.

## Page structure

```html
<a href="#ds-main" class="ds-skip">跳至主要内容</a>
<main id="ds-main" tabindex="-1">
  <section class="ds-section">
    <div class="ds-wrapper">
      ...
    </div>
  </section>
</main>
```

## Verification

Before finishing any change, run:

```bash
npm run audit
```

The audit covers validators, version sync, manifest integrity, icon sync,
size budget, unit tests, and the current token/component/icon references.
