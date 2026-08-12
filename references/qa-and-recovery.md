# QA and recovery

## Structural QA

After each mutation, inspect the returned nodes before starting another
board. At minimum verify:

- expected parent, page, section, and screen ancestor;
- node type, name, visibility, and component/instance relationship;
- width, height, x/y, and sibling order;
- Auto Layout flow, padding, gap, alignment, and axis sizing;
- descendant bounds against every owning container;
- expected variant/property counts and variable bindings;
- no unintended new top-level nodes, helper artifacts, or moved source
  cards.

For reparenting, assert the old parent, new parent, target screen ancestor,
node type, and node name before the operation. Re-audit the full parent
chain afterward. Never authorize a move from a stale ID or a name-only
global match.

For shared changes, maintain a family matrix and mark every member
inspected:

- Light and Dark;
- expanded and collapsed;
- parent-active and nested-sub-item-active;
- empty, loading, error, success, and overlay states;
- supported device widths or responsive variants;
- intentionally removed states, which must remain absent.

## Visual QA tiers

Use the smallest set that still proves the change:

1. **Focused component crop** — catches nested width overflow, icon bounds,
   font clipping, stroke/fill mistakes, and control-level spacing.
2. **Full board** — catches composition, shared content edges, balance, and
   underlay/overlay truth.
3. **Family or section overview** — catches stale siblings, inconsistent
   variants, wrong lane order, accidental movement, and state drift.

Use 1× or a focused crop for text, icon, and clipping review. Use an
overview scale for composition only; a tiny screenshot cannot prove
legibility. Screenshot after every visual mutation before moving to an
unrelated board. When active-file routing can change, navigate and confirm
the target before capturing; do not parallelize routing-dependent
screenshots.

## Design-detail checklist

Check the details most likely to regress:

- left/right shared content edges after width reflow;
- equal gaps, padding rhythm, and useful space utilization;
- clipping, overflow, and long-copy wrapping;
- text family, weight, size, tracking, and font loading;
- icon wrapper and vector bounds, scale, stroke/fill, and optical centering;
- contrast and theme-specific surface/text/icon treatment;
- visible versus hidden labels, chevrons, toggles, submenus, and wordmarks;
- active, selected, expanded, collapsed, disabled, loading, and error
  states;
- semantic correctness of copy, route, chart, action, and underlay;
- interactive target size and focus-state intent where the surface is
  interactive: measure the target's geometry against the platform minimum
  recorded in the file's `design.md`, or resolve the current platform
  guidance (Apple HIG, Material, WCAG target-size criteria) via the
  resolution order and record it — do not rely on remembered numbers.

Do not call a mutation complete because IDs and dimensions look plausible.
Tool success proves execution, not design correctness.

## Hard-coded and binding checks

For non-YOLO work, check whether production UI contains:

- hard-coded colors, spacing, radius, typography, or dimensions that should
  use existing variables/styles;
- detached instances or incorrect-library assets;
- missing Light/Dark values or unresolved aliases;
- inconsistent component properties or variant naming.

Use Figma Check designs when the account/file supports it. It is page-scoped
and plan-dependent; use measured Plugin API inspection and manual
screenshots as the fallback. Do not treat Check designs as a replacement for
family, semantic, or visual QA.

## Recovery

Follow the single recovery contract in
[figma-execute.md](figma-execute.md): a failed `figma_execute` may be
partially applied. Stop, read the error, inspect the target section and
every created/mutated ID, check for partial nodes, changed parents,
duplicate names, and geometry drift, repair only by exact returned IDs or
deterministic verified lookups, then re-run structural QA and screenshots.

Questionable API calls should be runtime-checked before a creation pass.
Scripts should be small, idempotent, and return all created/mutated IDs.
Never use a fresh guessed ID in a follow-up script without re-reading its
name, type, and parent.

## Completion record

Before reporting done, record:

- mutated and screenshot-verified node IDs;
- structural assertions and their result;
- visual QA tiers used;
- Light/Dark and family coverage;
- intentional exceptions and placeholders;
- remaining issues or documentation debt;
- updates made to `design.md`, `screens.md`, and the dated session note,
  including any value resolved via the resolution order this session.
