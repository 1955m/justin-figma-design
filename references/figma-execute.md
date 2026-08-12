# Writing figma_execute scripts

This skill runs entirely on [Figma Console MCP](https://github.com/southleft/figma-console-mcp).
`figma_execute` runs Plugin API JavaScript inside the connected Figma Desktop
file through the Desktop Bridge. This file is the single contract for writing
and recovering those scripts. Do not import conventions from other Figma MCPs
or skills; their tool surfaces and failure models differ.

## Connection and routing

- Check `figma_get_status` before the first Figma call of a session. Use
  `figma_reconnect` when the bridge is stale.
- The Desktop Bridge targets the **active** desktop file. Confirm the active
  file, page, and section before any write or screenshot, and re-confirm
  after the user switches files.
- Keep writes and screenshots **sequential** whenever routing depends on the
  active file. Never parallelize routing-dependent calls.
- Write work requires the local/NPX server plus Desktop Bridge. The hosted
  remote mode is read-only; if only remote is available, stay in read-only
  investigation and tell the user.

## Script conventions

- **One logical change per script** — one node, one property pass, or one
  tightly related family pass. Small scripts localize failure.
- **Assert identity before mutating.** Verify the node's type, name, parent,
  and screen ancestor inside the script before changing it. Abort with a
  clear message when an assertion fails. Never mutate from a name-only global
  lookup when duplicate names can exist.
- **Return everything you touched.** End every script by returning the IDs of
  all created/mutated nodes plus useful geometry (x, y, width, height,
  parent). Follow-up scripts must use these returned IDs, re-verified — never
  guessed IDs.
- **Top-level `await` and `return` are available.** Use them; do not wrap in
  IIFEs.
- **Fonts:** call `figma.loadFontAsync` for every styled segment's font
  before any text mutation. Mixed-style text has multiple fonts — inspect
  segments first.
- **Colors are 0–1 channels**, not 0–255. Convert hex before assigning.
- **Auto Layout sizing:** append a node into its intended Auto Layout parent
  **before** assigning `layoutSizingHorizontal`/`layoutSizingVertical`
  (`FIXED` / `HUG` / `FILL`); those child values are distinct from the
  frame's own axis sizing modes.
- **Idempotence:** prefer scripts that check current state and no-op when the
  target is already correct, so a safe re-run is possible after inspection.
- **Chunk large batches.** Many nodes or variables means several small
  scripts with inspection between them, not one giant script.
- **Runtime-check questionable APIs** on a throwaway node before a large
  creation pass; the Plugin API evolves.

## Prefer dedicated Console tools when they exist

Current Console MCP releases ship higher-level tools beyond `figma_execute`
(for example design-token setup and batch variable operations). When the
connected server's tool list includes a dedicated tool for the job, prefer it
over a hand-rolled script — it is atomic and returns structured IDs. Check
the connected server's actual tool list rather than assuming; the surface
changes between versions. Fall back to `figma_execute` when no dedicated tool
fits.

## The screenshot loop

After every visual mutation, before moving to an unrelated board:

1. Inspect the returned nodes structurally (parent, geometry, bindings).
2. `figma_take_screenshot` of the affected component, board, or family view.
3. Compare the evidence against the intended change and the QA checklist in
   [qa-and-recovery.md](qa-and-recovery.md).

## Recovery contract

A failed `figma_execute` may have **partially applied** — earlier statements
in the script can have committed before the error. On any failure:

1. **Stop.** Do not blindly rerun.
2. Read the error and record what the script intended.
3. Inspect the target section and every ID the script created or may have
   mutated.
4. Look for partial nodes, changed parents, duplicate names, and geometry
   drift.
5. Repair or clean up only by **exact returned IDs** or deterministic,
   verified lookups.
6. Re-run structural QA, then screenshot the affected component, board, and
   family as needed.

Never authorize a follow-up mutation from a stale or guessed ID without
re-reading its name, type, and parent first.
