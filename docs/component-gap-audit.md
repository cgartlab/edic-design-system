# EDIC Component Gap Audit

This audit is the planning source for the 2.0 component expansion. It records
coverage against the current static, framework-agnostic design system.

## Existing Core Coverage

The current `styles.css`, `docs.html`, and `scripts.js` already provide broad
coverage for the following areas:

- Layout and documentation shell: `ds-wrapper`, `ds-section`, `ds-docs`.
- Interactive controls: buttons, inputs, selects, checkboxes, radios, toggles,
  sliders, date fields.
- Feedback: alerts, badges, chips, toast, progress, skeleton.
- Navigation: navbar, breadcrumb, pagination, steps, sidebar nav.
- Data display: table, timeline, stat, avatar, code, swatches.
- Overlay: modal, dropdown, tooltip, drawer patterns.

## 2.0 Expansion Targets

Market benchmarked against Radix, shadcn/ui, Headless UI, Chakra, Ant Design,
Material Design, and Fluent. EDIC keeps its framework-agnostic, editorial scope;
this list identifies where the component system is still incomplete or needs
deeper contracts.

| Category | Existing coverage | Missing or underdocumented | 2.0 action |
| --- | --- | --- | --- |
| Layout and shells | `ds-wrapper`, `ds-section`, `ds-docs`, grids | `Container`, documented grid primitive, `Divider` example, `Card Actions`, navigation drawer | Document primitives and decide which deserve first-class classes |
| Buttons and controls | `ds-btn`, icon button, copy button, dropdown | Menu, context menu, segmented control, toggle button group, checkbox button | Add contracts and examples for composite controls |
| Forms and input | inputs, selects, checkboxes, radios, toggles, sliders, date fields | File upload, search input, OTP/password, time picker, date range, rich text toolbar, form field wrapper | Expand forms with contract-driven examples |
| Data display | table, timeline, stat, avatar, code, swatches | Description list, list/list item, tree, avatar group, image fallback, horizontal timeline | Add enterprise data display patterns |
| Feedback and loading | alert, badge, chip, toast, progress, skeleton | Spinner, empty state docs/example, progress ring, notification center, error boundary | Add loading/empty/error patterns |
| Navigation | navbar, breadcrumb, pagination, steps, sidebar nav, tabs | Current page state, focus behavior, mobile navigation drawer, context menu | Document ARIA and keyboard behavior |
| Overlays and dialogs | modal, dropdown, tooltip, drawer, popover, command palette | Alert dialog, stronger focus trap/Esc contracts, trigger relationship for popover/drawer, loading state contracts | Formalize contract examples |

## Existing But Needs Quality Contracts

- Combobox: listbox role, active option, keyboard search, reset behavior.
- Date Picker and Calendar: selected/today/outside/month keyboard contract.
- Slider: aria-valuenow/min/max/text, disabled and invalid states.
- Switch and Radio Group: grouping, required state, disabled propagation.
- Toast, Tooltip, Drawer, Popover, Command Palette: trigger relation, live region, Esc, focus recovery.
- Table, Pagination, Timeline, Stat, Avatar, Skeleton: state and ARIA documentation.

## Missing Or Partial Coverage

- Missing: file upload, search input, OTP/password input, time picker,
  date range picker, rich text toolbar, menu, context menu, segmented control,
  toggle button group, checkbox button, navigation drawer, avatar group,
  list/list item, tree, container/grid primitive, image fallback, horizontal
  timeline, alert dialog, error boundary, notification center.
- Partial: `ds-empty-state`, `ds-avatar`, `ds-progress`, `ds-divider`,
  `ds-calendar`, `ds-menu`-style dropdown coverage should be verified against
  docs and manifest before being promoted as complete.

## Execution Queue

The detailed development queue lives in
[component-2.0-backlog.md](./component-2.0-backlog.md). Use the backlog when
choosing the next implementation task.

## Acceptance Criteria

- Every expanded component has a CSS class family in `styles.css` before any
  HTML example references it.
- Every interactive component includes keyboard behavior and ARIA notes.
- Every example links only to `../styles.css?v=...` and avoids runtime
  dependencies.
- `npm run audit` validates manifest, icons, CSS references, dark mode,
  accessibility, and unit tests.

## Naming Policy

Keep the established `ds-*` prefix for compatibility. 2.0 names are additive;
they do not rename existing 1.x classes.
