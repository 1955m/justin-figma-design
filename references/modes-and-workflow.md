# Modes and workflow

## Workflow fork

- An existing file or frame family to change → **measure-first editing**,
  routed by the mode table below.
- Nothing to measure (new file, empty page, new surface) →
  [starting-from-scratch.md](starting-from-scratch.md), which is always
  non-YOLO unless the user explicitly requests a disposable board.

## Mode decision

| Signal | Mode | Rule |
|---|---|---|
| User asks for explanation, status, or diagnosis only | Read-only | Inspect and report; do not mutate Figma. |
| User explicitly asks for YOLO, a quick demo, or a disposable prototype | YOLO | Only if the scope is one named board or state. |
| User asks for a component, library, theme, responsive behavior, or shared chrome | Non-YOLO | Component and family discipline is required even if the requested edit is small. |
| Any other implementation request | Non-YOLO | The production default. |

Do not silently infer YOLO from urgency. If "quick" is ambiguous, use
non-YOLO and state the intended scope before execution.

## Shared preflight

Run the SKILL.md "Before any Figma mutation" checklist. In addition:

- Confirm the active Desktop Bridge file before relying on screenshots
  (`figma_get_status`).
- Treat historical node IDs as evidence, not authorization: re-search IDs,
  components, variables, styles, and library assets in the connected file.
- Read [figma-execute.md](figma-execute.md) before writing any script.
- If `docs/files/<alias>/design.md` is missing, perform a read-only baseline
  and record the missing context before editing the file.

## Non-YOLO workflow

### 1. Discovery

Establish:

- the authoritative page and golden reference;
- the exact mutation boundary and protected source/reference nodes;
- the component, variable, style, and font inventory;
- the complete related-state matrix;
- measured root frame sizes, axis sizing, spacing, alignment, and responsive
  constraints;
- expected semantic behavior and accessibility states.

For a shared change, the unit of work is the state family, not the first
frame that exposes the bug.

### 2. Plan gate

Before mutation, the plan must state:

- target file, page, section, and re-verified nodes;
- what is explicitly out of scope;
- reuse/create decisions for components and variables;
- family members that will be updated and screenshot-QA'd;
- layout and theme assumptions, including any value resolved via the
  resolution order this session;
- design-detail QA: shared edges, active states, hidden controls, spacing,
  clipping, contrast, legibility, and light/dark twins;
- documentation and session-note updates.

Do not begin Figma writes until the user asks to execute or approves the
plan.

### 3. Incremental execution

Use small, scoped, idempotent scripts per
[figma-execute.md](figma-execute.md). Each write should:

- assert the expected node type, name, parent, and screen ancestor;
- avoid name-only global lookups when duplicate names can exist;
- make one logical change or one tightly related family pass;
- return all mutated/created IDs plus useful geometry;
- be followed by structural inspection and an immediate screenshot.

Apply a shared visual change to every family member before moving to an
unrelated board. Keep screenshot/navigation calls sequential when the active
file determines their routing.

### 4. QA and closeout

Use the structural and visual checklists in
[qa-and-recovery.md](qa-and-recovery.md). Do not call the pass complete
because the API returned success. Update living context and write a dated
session note when the change is meaningful.

## YOLO workflow

YOLO may:

- use local editable primitives or a one-off frame;
- skip creating a component, variant set, variable collection, or library;
- skip the full historical audit and formal documentation when the change is
  genuinely disposable and the user accepts the tradeoff.

YOLO must still:

- verify the target file/page and read the target `design.md` authority and
  safety notes;
- keep the mutation to one named board/state;
- load current fonts before text mutation;
- preserve protected originals, removed styles, existing copy, and file
  structure documented in `design.md`;
- use a small targeted script, return IDs/geometry, and screenshot the
  result;
- check overflow, clipping, alignment, contrast, and legibility;
- stop rather than guess when node identity, parentage, or active-file
  routing is uncertain.

YOLO may not:

- change shared navigation, shell chrome, a master component, or a variable
  mode;
- create or refactor Auto Layout across a family;
- alter a light/dark pair, responsive behavior, or business-rule state;
- touch more than one board/state unless the user explicitly lists the exact
  set and the work is still disposable.

Escalate immediately to non-YOLO when any of those conditions appears. Do
not continue a quick pass by copying the same fix manually into related
states.
