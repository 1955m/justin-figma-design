# Figma Design Workspace

This is a Figma-first collaboration workspace, not an application codebase.
Use the `justin-figma-design` skill (alias `/jfd` when the host supports
aliases) alongside [Figma Console MCP](https://github.com/southleft/figma-console-mcp)
for inspection, mutation, and screenshot QA.

The skill can be installed in the project under
`.agents/skills/justin-figma-design/` or a host-specific compatible skill
root. The alias is a convenience; agents should also recognize the skill
name and its description.

## Before Figma work

Read, in order:

1. `docs/preferences.md`
2. `docs/FILES.md`
3. the latest relevant note in `docs/sessions/`
4. `docs/tools/figma-console.md`
5. the target `docs/files/<alias>/design.md`
6. the target `docs/files/<alias>/screens.md` for screen or flow work

If `docs/preferences.md` or `docs/FILES.md` is missing, run `jfd init` (or
`/jfd init` when supported) before design work. Init is a local scaffold
only: it does not connect to Figma or mutate a canvas. If a target file has
no living context, create a read-only baseline before making visual
mutations.

## Operating rules

- Non-YOLO is the default; use YOLO only when the user explicitly requests a
  narrow disposable demo.
- Resolve sizes, fonts, and style preferences by measuring the target file
  first, then workspace memory, then asking or looking up current guidance —
  never from remembered defaults. Record resolved values in the file's
  `design.md`.
- Inspect before editing. Prefer measured node IDs and geometry.
- Screenshot every visual mutation before moving to another board.
- Load existing text fonts before text mutation.
- Preserve the target file's visual language, copy, page authority, and
  protected originals as documented in its `design.md`.
- Do not generate React, HTML, or CSS unless design-to-code is explicitly
  requested.
- Do not store credentials, access tokens, or private design data in memory.
