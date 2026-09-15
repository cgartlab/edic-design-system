# EDIC Component Contracts

Use this template before adding or modifying any component.

## Component Contract Template

```text
Component:
Purpose:
Classes:
Required ARIA:
Keyboard behavior:
States:
Dark mode:
Minimum HTML example:
Verification checklist:
```

## Required Contract Fields

- **Component:** one stable English or bilingual name.
- **Purpose:** the UI job it solves in one sentence.
- **Classes:** base class, modifiers, and optional companion classes.
- **Required ARIA:** roles, labels, states, relationships, and live regions.
- **Keyboard behavior:** focus order, Enter/Space, arrow keys, Esc, focus recovery.
- **States:** default, hover, `:focus-visible`, active, disabled, loading, error, empty, selected, expanded, collapsed.
- **Dark mode:** how color, border, shadow, and accent tokens adapt.
- **Minimum HTML example:** smallest markup that still demonstrates the contract.
- **Verification checklist:** ARIA, keyboard, dark mode, token-only visuals, no runtime dependencies.

## Minimum Example

```html
<div class="ds-button-group" role="group" aria-label="视图切换">
  <button type="button" class="ds-btn ds-btn--ghost" aria-pressed="false">列表</button>
  <button type="button" class="ds-btn ds-btn--primary" aria-pressed="true">网格</button>
</div>
```

## Verification Checklist

- CSS class family exists in `styles.css` before HTML references it.
- No hardcoded hex, rgb, hsl, raw px, or raw rem visual values.
- Dark mode uses `var(--ds-*)` tokens, not duplicated raw values.
- Interactive controls are buttons, links, or form controls with correct roles.
- Keyboard focus is visible and recoverable.
- Required ARIA states are included in markup or documented JS behavior.
- `npm run audit` passes before marking the task complete.
