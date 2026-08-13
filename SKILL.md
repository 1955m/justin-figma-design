---
name: justin-figma-design
description: >-
  Inspects and edits Figma design files on the canvas — screens, components,
  variants, variables and themes, Auto Layout, responsive states, annotated
  screenshots, and visual QA — by driving Figma Console MCP
  (https://github.com/southleft/figma-console-mcp) with small figma_execute
  Plugin API scripts verified by screenshots. Use whenever the user wants to
  inspect, edit, refactor, audit, or QA anything in a Figma file, start a new
  Figma design from scratch, or bootstrap a Figma-first workspace, even if
  they don't name this skill. Resolves screen sizes, fonts, spacing, and
  style preferences by measuring the target file and workspace memory, never
  from fixed rules. Defaults to production-quality non-YOLO work behind a
  plan gate; supports an explicitly requested YOLO path for one disposable
  board. Supports human–AI collaboration and can run as a full designer
  replacement when no human is present. Does not generate design-to-code
  unless requested. Also invoked as justin-figma-design or /jfd.
compatibility: >-
  All Figma inspection, mutation, and screenshots require Figma Console MCP
  (user-figma-console). Write work needs the local/NPX server with the Figma
  Desktop Bridge connected to the target file; the hosted remote mode is
  read-only. Init is local-only. Works on macOS, Windows, and Linux with
  Agent Skills-compatible hosts.
metadata:
  alias: "/jfd"
---

# Justin Figma Design (/jfd)

This workspace is a Figma-first collaboration workspace, not an application
codebase. This skill is a human–AI collaboration process tool and an
orchestration layer: workspace memory, the Figma Console workflow,
design-system discipline, and evidence-based visual QA. It can also run as a
full designer replacement: inspect, restyle, QA, and close out without a
human on the canvas. A human may or may not join; either way, keep the same
finish bar to speed up design without lowering quality. Do not generate React,
HTML, or CSS unless the user explicitly requests design-to-code.

## Required MCP companion

All Figma work runs on [Figma Console MCP](https://github.com/southleft/figma-console-mcp)
(`user-figma-console`): `figma_execute` for inspect and mutate,
`figma_take_screenshot` for evidence, `figma_get_status` and `figma_reconnect`
for the Desktop Bridge connection. Write work requires the local/NPX server
with the Desktop Bridge connected; the hosted remote mode is read-only. Read
[references/figma-execute.md](references/figma-execute.md) before writing any
script, and the workspace file `docs/tools/figma-console.md` (at the workspace
root) for connection specifics. Do not treat `/jfd` as a standalone Figma
editor without that MCP connection.

## Resolve facts from the design, not from this skill

This skill ships procedures, not facts. Device sizes, fonts, spacing, and
style preferences drift over time; the target file is always current. Resolve
any needed value — a dimension, font, spacing step, color, name, or
convention — in this order:

1. **The target file.** Measure the actual frame, text, token, or component.
2. **The family.** Sibling frames, states, and screens in the same section.
3. **Workspace memory.** The file's `docs/files/<alias>/design.md` and
   `docs/preferences.md`, respecting their "Last verified" dates.
4. **The user or a current lookup.** Ask, or look up present-day platform
   guidance. Never trust remembered device sizes or old defaults.
5. **Write back.** Record the resolved value with today's date in the target
   `design.md` so the next session can trust it.

Never resolve a project value from this skill's own text.

## Two workflows

- **Editing an existing file** (the default): there is something to measure.
  Follow the full loop below, and never assume a root frame size — measure
  the actual root of the family being edited.
- **Starting from scratch**: nothing exists to measure, so the resolution
  order runs on steps 3–5. Read
  [references/starting-from-scratch.md](references/starting-from-scratch.md).
  Confirm root frame size, typography, and theme support with the user before
  building, then create the file's `design.md` immediately so every later
  session can measure instead of guess.

## Initialize an empty workspace

Use **init mode** when the workspace lacks `docs/preferences.md` and
`docs/FILES.md`. Init is a local, idempotent scaffold; it never opens Figma,
calls the MCP, or mutates a canvas.

1. Treat `jfd init` the same as `/jfd init` when the host lacks slash aliases.
2. List missing scaffold paths before writing. In a non-empty workspace, ask
   for confirmation first. Never overwrite an existing file, directory,
   symlink, or skill installation.
3. Copy only the missing files from this skill's `assets/templates/`.
4. Install a missing skill copy at `.agents/skills/justin-figma-design/`
   (canonical) and `.cursor/skills/justin-figma-design/` when appropriate.
5. Optionally run `scripts/init_project.py` (Python 3, stdlib only) for one
   bulk pass; agent file tools remain the primary path.
6. Verify the scaffold, then ask for a Figma link or file key. Never invent
   credentials or file data.

Details: [references/getting-started.md](references/getting-started.md).

## Choose the operating mode

Non-YOLO is the default.

- **Non-YOLO** for production work: shared patterns, screens, components,
  variables, themes, responsive changes, and any scope not explicitly
  disposable.
- **YOLO** only when the user explicitly says "YOLO", "quick demo", "rapid
  prototype", or equivalent, and the scope is one named board or state.
- "Make a component", "update a library", "support light and dark", or a
  shared-chrome change is never YOLO merely because it is small.
- Stay in plan mode until the user clearly asks to implement or execute.

YOLO reduces library overhead; it does not remove safety or visual QA.
Escalate to non-YOLO on discovering shared chrome, a reusable pattern,
multiple related states, light/dark or responsive propagation, a
master-component change, an Auto Layout refactor, a business-rule change, or
a second board. Full router and checklists:
[references/modes-and-workflow.md](references/modes-and-workflow.md).

## Before any Figma mutation

1. Read `docs/preferences.md` and `docs/FILES.md` at the workspace root.
2. Resolve the target file alias and read its `docs/files/<alias>/design.md`;
   read `screens.md` for screen, flow, or composed-surface work.
3. Read the latest relevant session note. The living `design.md` and current
   authority outrank stale historical notes.
4. Confirm the active Figma file, page, target section/frame, mutation
   boundary, and **split authorities**: shell/chrome, content/components,
   and any attached screenshot. Historical and reference sections are
   read-only unless the user puts them in scope. An attached image is names
   and scope only unless the user says it is visual authority. Measure copy
   locale from the product screens, not from a nearby extra page or the
   request's script.
5. Re-search node IDs, components, variables, and styles in the connected
   file; IDs from prior sessions are stale evidence, not authorization.
   Inspect the source screen's instance tree — an empty name search is not
   "no components."
6. Inventory the whole same-frame/state family before a shared change:
   light/dark, expanded/collapsed, nested active routes, overlays, responsive
   variants, and intentionally removed states.
7. Measure the root frame(s) of the family being edited. Never assume a
   device size.
8. Before text mutation, inspect styled font segments and load the current
   fonts. Choose any replacement font via the resolution order — measured
   text, then `design.md`, then the user — never from this skill.

If the target file has no `design.md`, complete a read-only investigation
baseline first. If the active file or authority cannot be verified, stop and
ask.

## Common graphics

Before placing icons or imported imagery, read `docs/assets/README.md` and
`docs/assets/icons.md` at the workspace root. Prefer existing file components
and the project's approved icon sources; inspect vector bounds, sizing, and
theme contrast before accepting a new graphic. Never use a character,
punctuation glyph, or letter initials as an icon, chevron, or image
substitute. Search instances on the source screen first; if a variant is
missing, use another file-backed graphic, not invented text. Avatars are
user-provided only; never generate them.

## Non-YOLO contract

- Search authoritative local instances/components first, then enabled
  libraries, then broader library search. Create only after documenting the
  gap. Name-search returning empty is not proof the file has no components.
- Preserve the measured nested chrome tree (nav, category bar, overflow and
  clip). Do not replace it with a hand-built twin. After cloning a shell,
  audit hidden and inherited children and remove out-of-scope leftovers
  before restyling content.
- Build the minimum coherent design system for the approved scope: variables
  and modes first, then styles and components, then screen instances.
- Use variants for structural/visual states and component properties for
  content flexibility. Prefer instances, instance swaps, and controlled
  wrappers over detached redraws.
- Make layout intent legible: semantic names, meaningful hierarchy, Auto
  Layout where children relate, token bindings, component descriptions, and
  documented accessibility/state behavior.
- Treat Light/Dark as a variable-mode matrix, not two hard-coded screens. See
  [references/variables-and-theming.md](references/variables-and-theming.md).
- Apply shared changes to the complete related-screen family in one pass,
  then QA every member. A single-frame fix is not complete while siblings
  are stale.

Read [references/components-and-design-system.md](references/components-and-design-system.md)
and [references/layout-and-autolayout.md](references/layout-and-autolayout.md)
before complex work.

## Layout rules

Choose Hug, Fill, Fixed, and min/max independently per axis: Hug for
content-driven stacks and controls; Fill only for a child with meaningful
available space in an Auto Layout parent; Fixed for intentional structural
boundaries (measured screen roots, icon boxes, CTAs, calibrated shells);
min/max for approved responsive limits. Encode relationships with nested Auto
Layout, padding, and gap — never invisible spacer frames preserving old
coordinates. Keep absolute / Ignore-auto-layout layers only for justified
overlays, chrome, decoration, or exceptions documented in the target
`design.md`. After resizing a container, audit width-owning descendants; a
wider parent is not a complete reflow. Details:
[references/layout-and-autolayout.md](references/layout-and-autolayout.md).

## Execute and verify

Inspect, run one small targeted `figma_execute`, return every mutated ID and
useful geometry, then capture a screenshot immediately with
`figma_take_screenshot`. Keep writes and screenshots sequential when routing
depends on the active file. QA combines measured structure with visual
evidence — capture, as applicable: (1) a focused component crop, (2) the full
board, (3) the related family or section overview. Check shared edges,
spacing, clipping, overflow, long-copy behavior, icon/vector bounds,
contrast, typography, hidden controls, semantic state, related-state parity,
hard-coded values, unresolved bindings, and Light/Dark resolution. Treat this
structural/family pass as incomplete until the agent runs the
designer-detail finish pass itself: check placeholders, copy-count parity,
control affordances, material transparency, and image-fill legibility. Do
not defer that pass to a human. Use Figma Check designs when available;
otherwise run equivalent structural and manual checks.

Treat a failed `figma_execute` as potentially partial until the target is
inspected; never blindly rerun a failed creation or reparenting script.
Recovery contract: [references/figma-execute.md](references/figma-execute.md).
Full checklists: [references/qa-and-recovery.md](references/qa-and-recovery.md).

## Closeout

- Capture final screenshots for every mutated board and required family
  member.
- Record intentional exceptions, placeholders, unresolved issues, and scope
  boundaries.
- Name intentionally deferred family members and stale siblings not updated.
  Do not report done while placeholder markers remain.
- Update the target `design.md` and `screens.md` when authority, components,
  variables, screens, root sizes, or drift changed — including any value
  resolved during the session. If the authority *role* changed (shell vs
  content vs screenshot), update `docs/FILES.md` too.
- Write a dated note under `docs/sessions/` for meaningful work.

Honor the target file's documented protections in its `design.md`: locked or
protected originals, styles or states that must stay removed, copy and
language that must be preserved. Never store credentials or private tokens in
project memory.

For external guidance behind this skill, read
[references/research-sources.md](references/research-sources.md).
