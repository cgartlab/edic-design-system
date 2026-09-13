# EDIC Token System 2.0 Matrix

Token 2.0 keeps the existing `--ds-*` prefix for backward compatibility while
adding semantic aliases and missing categories.

## Category Coverage

| Category | 1.x baseline | 2.0 additions |
| --- | --- | --- |
| Color | raw surfaces, olive ramp, status colors | semantic surface/text/border aliases |
| Typography | font, text scale, weight, leading, tracking | unchanged, documented usage retained |
| Spacing | `--ds-space-*` scale | gutter semantic aliases |
| Radius | `--ds-radius-*` scale | control/card aliases |
| Border | component-level widths | `--ds-border-width-*`, `--ds-border-style-default` |
| Shadow/depth | `--ds-shadow-*` | `--ds-depth-*` aliases |
| Motion | `--ds-duration-*`, `--ds-ease-*` | `--ds-duration-*` aliases, `--ds-delay-*`, `--ds-motion-*` |
| Layering | `--ds-z-*` | retained and documented |
| Opacity/state | component-level alpha | `--ds-opacity-*`, `--ds-disabled-*`, `--ds-focus-*` |
| Grid/layout | breakpoint tokens `--ds-bp-*` | `--ds-grid-*`, `--ds-gutter-*`, `--ds-breakpoint-*` |

## Semantic Alias Strategy

Consumers should prefer semantic aliases where available:

```css
.example {
  background: var(--ds-color-surface-primary);
  color: var(--ds-color-text-primary);
  border: var(--ds-border-width-default) var(--ds-border-style-default) var(--ds-color-border-default);
  border-radius: var(--ds-border-radius-control);
  transition: transform var(--ds-motion-default);
}
```

Raw tokens remain valid for theme implementation, component internals, and
advanced chart configuration.

## Compatibility Rules

- Do not remove or rename 1.x tokens.
- Add semantic aliases before raw values when possible.
- Keep all color values OKLch.
- Component rules should reference `var(--ds-*)` tokens, not bare color values.
- Every token added to `styles.css :root` must be represented in
  `tokens.json`.
