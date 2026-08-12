# Design and Workflow Preferences

Stable, project-wide preferences. Per-file facts (root sizes, typography,
protected content) live in each file's `docs/files/<alias>/design.md`.

## Collaboration

- Inspect the connected Figma design before proposing or applying changes.
- Treat annotated screenshots and short notes such as "alignment", "empty
  space", and "equal spacing" as actionable feedback.
- Stay in plan mode while requirements are refined; mutate Figma only after
  the user clearly asks to implement or execute.
- Keep each pass focused on the requested board, component, or family.

## Operating modes

- Non-YOLO is the default for production screens, shared patterns,
  components, variables, Light/Dark themes, and responsive behavior.
- YOLO is opt-in only for a named, disposable board or state. It may skip
  creating components and variables, but it still requires file
  verification, font safety, scoped writes, screenshots, and visual QA.
- Escalate YOLO when work affects shared chrome, reusable patterns, multiple
  states, themes, responsive behavior, Auto Layout architecture, or business
  rules.

## Resolving values

- Resolve sizes, fonts, spacing, and style preferences by measuring the
  target file first, then this memory, then asking the user or looking up
  current platform guidance. Record every resolved value, with a date, in
  the target file's `design.md`.
- Standing project-wide decisions (set these as the project makes them):
  - Preferred product font when a file has no authority: _unset — propose
    and confirm with the user, then record here and per file._
  - Preferred spacing step / grid: _unset_
  - Target platforms and form factors: _unset_

## Related-screen QA

- Inventory every related state in the same frame, section, or flow family
  before a shared change.
- Include Light/Dark, expanded/collapsed, active parent/sub-item, overlays,
  responsive widths, and empty/loading/error/success states where
  applicable.
- Apply shared changes to the family, then screenshot-QA every intentional
  member.

## Visual and Figma safety

- Preserve the target file's established visual language and existing copy.
- Prefer measured node IDs and geometry over screenshot guesses.
- Do not move protected source/style frames or edit locked originals
  without explicit instruction; record such protections in the file's
  `design.md`.
- Screenshot each visual mutation before moving to another board.

## Typography and graphics

- Measure existing styled text before any font decision; load current
  fonts before text mutation.
- When a file has no typography authority, propose a font, confirm with the
  user, and record the decision in that file's `design.md`.
- Read [`assets/README.md`](assets/README.md) before importing graphics and
  [`assets/icons.md`](assets/icons.md) before placing icons.
- Avatars must be user-provided approved images; agents must not generate
  them.
