# EDIC 2.0 Component Backlog

This backlog converts the component gap audit into sequential, auditable tasks.

## P0 — Skill And Contract Foundation

| Task | Status | Depends on | Acceptance |
| --- | --- | --- | --- |
| Define component contract template | Done | none | `skills/edic-design-system/references/CONTRACTS.md` exists |
| Make Skill manifest-first | Done | none | `SKILL.md` requires `edic-manifest.json`, `tokens.json`, `icons.json`, `AGENT-GUIDE.md`, gap audit, backlog, contracts, anti-patterns |
| Register 2.0 governance files in manifest | Done | none | `edic-manifest.json` deliverables include backlog and contracts |
| Add interactive anti-pattern rules | Done | none | `references/ANTI-PATTERNS.md` covers menus, toasts, pagination, overlays, loading and icon labels |

## P1 — Missing High-Frequency Components

| Component | Priority | Contract owner | Notes |
| --- | --- | --- | --- |
| Spinner / Loader | P1 | P1 | CSS-only loader with reduced-motion fallback |
| Menu | P1 | P1 | `aria-haspopup`, `aria-expanded`, menu item roles |
| Form Field | P1 | P1 | label, hint, error, disabled, required field wrapper |
| Empty State | P1 | P1 | existing `ds-empty-state` may need docs/example completion |
| Alert Dialog | P1 | P1 | modal-like confirmation with focus trap and Esc behavior |
| File Upload | P1 | P1 | drag area, filename list, progress/error state |
| Calendar | P1 | P1 | existing date-calendar may need standalone calendar component docs |
| Description List | P1 | P1 | table-like definition list for settings/profile views |

## P2 — Quality And Breadth Expansion

| Component | Priority | Contract owner | Notes |
| --- | --- | --- | --- |
| Combobox | P1 quality | P2 | improve listbox, active option, keyboard search contract |
| Date Range | P2 | P2 | dual calendars and clear button |
| Time Picker | P2 | P2 | hour/minute/second list or input variant |
| Rich Text Toolbar | P2 | P2 | static toolbar with labels and disabled states |
| Context Menu | P2 | P2 | portal-like HTML example plus trigger relationship |
| Mobile Navigation Drawer | P2 | P2 | mobile-only drawer using existing drawer contract |
| Segmented Control | P2 | P2 | tab/radio hybrid with current-state ARIA |
| Toggle Button Group | P2 | P2 | pressed state and grouping semantics |
| Checkbox Button | P2 | P2 | button-style selected state |
| Avatar Group | P2 | P2 | overflow count and stack order |
| List / ListItem | P2 | P2 | dense data row patterns |
| Tree | P2 | P2 | expand/collapse and keyboard support |
| Container / Grid primitive | P2 | P2 | documented layout primitives |
| Divider | P2 | P2 | existing CSS may need example/docs completion |
| Card Actions | P2 | P2 | action footer pattern for cards |
| Image fallback | P2 | P2 | alt/error/placeholder states |
| Horizontal Timeline | P2 | P2 | variant of existing vertical timeline |
| Error Boundary | P2 | P2 | static fallback pattern for framework consumers |
| Notification Center | P2 | P2 | panel/list pattern with empty and unread states |

## Execution Rules

- CSS before HTML.
- Token-only visual values.
- Dark mode coverage required.
- ARIA and keyboard behavior required for interactive components.
- Run `npm run audit` before marking a task done.
