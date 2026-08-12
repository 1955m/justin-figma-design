# Icon library

## Approved sources

Record the project's actual icon authority here as it is decided. Until
then, reasonable open-source defaults when the target file has no closer
local authority:

- [Iconoir](https://iconoir.com) — designed around a 24px grid.
- [Lucide](https://lucide.dev) — a consistent open-source outline
  vocabulary.

Search the target file's local components and existing screens first.
Prefer existing icon instances over importing a visually similar
replacement. Do not invent a custom icon when an approved library covers
the metaphor.

## Figma placement

- Default to the icon frame size already used by the target file (measure
  it); use a `24 × 24` frame only when the file establishes no size.
- Keep frame and vector positions on whole pixels where possible.
- Preserve the source viewBox and proportions; resizing a wrapper does not
  guarantee that its vector children are correctly scaled.
- Keep stroke/fill, weight, caps, joins, and optical weight consistent with
  neighboring icons.
- Use component instances or instance-swap properties for reusable icons.
- Bind icon color to semantic theme variables when the target system
  supports them.

## Icon QA

- [ ] Frame and descendant vector bounds are correct.
- [ ] No vector is outside the frame or unintentionally clipped.
- [ ] Stroke/fill and visual weight match neighboring icons.
- [ ] The icon is optically centered and legible at actual UI size.
- [ ] Light/Dark contrast and semantic color binding are correct.
- [ ] The icon does not collide with labels, dividers, or controls.
- [ ] Focused component and full-board screenshots have been checked.
