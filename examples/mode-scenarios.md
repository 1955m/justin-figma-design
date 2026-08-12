# Mode scenarios

Six worked scenarios illustrating mode choice and required evidence. They
are generic patterns, not project history: as your own workspace accumulates
dated session notes under `docs/sessions/`, cite those instead — real
evidence from the target project always outranks these illustrations.

## 1. YOLO: one disposable feature board

**Request:** "Make a quick demo of one standings board for tomorrow's
pitch."

**Mode:** YOLO, if the user confirms the board is disposable.

**Allowed approach:**

- Use an existing screen shell in the file as a visual starting point.
- Build one named board with editable local content.
- Reuse an existing asset when immediately available, but do not create a
  new component set, variable collection, or published library asset.
- Keep the requested columns and content scope only.

**Still required:**

- Verify the target file, section, and shell authority in `design.md`.
- Preserve the file's existing chrome and copy conventions.
- Use a small scoped script and return node IDs/geometry.
- Screenshot the board and its section.
- Check column alignment, active states, clipping, legibility, and scope.

**Escalate if:** the same pattern will be reused across surfaces, needs
Light/Dark bindings, or should become a maintained component/template.

## 2. Non-YOLO: same-frame state family

**Request:** "Fix the row treatment on the bound-account state."

**Mode:** Non-YOLO. The rows are a shared family across several screens and
states.

**Required approach:**

- Read the file's authority and current family notes in `design.md`.
- Inventory every family member — each screen and state that shows the row,
  including underlays and flow lanes.
- Search for the approved row component and its icons before drawing
  anything.
- Apply the shared treatment to every intentional family member; keep
  intentionally different states (e.g., already-bound vs. unbound) correct
  rather than uniform.
- Screenshot each member, the flow lane, and the section overview.
- Check icon provenance, state typography, dividers, copy, and the measured
  root size.

The classic failure: updating only the first screen that exposed the bug
and leaving a sibling state stale. The family is the unit of work.

## 3. Non-YOLO: Light/Dark sidebar collapse across a state matrix

**Request:** "Collapse the dashboard sidebar and keep the active nested
route correct."

**Mode:** Non-YOLO. Shared chrome across a multi-state matrix (e.g., six
expanded and six collapsed states × Light and Dark = twelve boards).

**Required approach:**

- Read the file's authority and enumerate the full matrix before editing.
- Reflow the main content, headers, widgets, tables, forms, and controls —
  not only the outer sidebar width.
- Hide labels, chevrons, submenu children, and wordmarks intentionally in
  the collapsed state.
- Promote the active parent icon when the active route is a sub-item.
- Verify semantic token and contrast behavior in both themes if variables
  are present; do not maintain arbitrary hard-coded theme drift.
- Capture focused component, full-screen, and family-overview evidence.

The acceptance scope is every state, not the first dashboard that looks
right.

## 4. Non-YOLO: missing reusable component with themes

**Request:** "Add a reusable input component for the new screen in Light and
Dark."

**Mode:** Non-YOLO.

**Required approach:**

1. Search target-file instances, local components, enabled libraries, and
   remote variables before creating anything.
2. Document the gap and define only the needed foundation: semantic
   surface, text, border, focus, disabled, spacing, radius, and typography
   values with Light/Dark modes.
3. Bind the component to semantic variables and use Auto Layout.
4. Use properties for label, helper/error visibility, and icon swaps; use
   variants for meaningful size/state differences.
5. Add descriptions for usage, validation, focus, and contrast behavior.
6. Test representative property combinations and existing instances before
   publishing or treating the component as authoritative.
7. Instantiate it on the screen and screenshot the component in both
   themes.

Do not create a component set first and retrofit variables later.

## 5. QA escalation: nested overflow

**Finding:** The board screenshot looks correct, but a two-column form's
nested label/input descendants are wider than their owning fields — a
sibling paints over the overflow.

**Action:** Stop the board pass and switch to focused component QA. Audit
every descendant width against the complete parent chain, repair the
width-owning component rows, then recapture focused and full-board
screenshots. A board screenshot alone is never proof that the constraint
chain is correct.

## 6. QA escalation: Auto Layout conversion

**Finding:** An Auto Layout conversion contains invisible spacer frames and
fixed-height content preserved from the old absolute composition.

**Action:** Stop preserving coordinates. Group content semantically, replace
spacers with padding/gap, choose Hug/Fill/Fixed per axis, re-anchor sheets
and dialogs, then run family screenshots plus a zero-spacer audit.
