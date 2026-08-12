# Figma Console MCP

Use [Figma Console MCP](https://github.com/southleft/figma-console-mcp)
with `/jfd` for all Figma inspection, editing, and screenshot QA.

## Connection

- MCP server: `user-figma-console`
- Desktop Bridge: run the local/NPX server and connect the target Figma
  Desktop file before any mutation. The hosted remote mode is read-only.
- Core tools: `figma_execute`, `figma_take_screenshot`, `figma_get_status`,
  and `figma_reconnect`. Current releases also ship higher-level token and
  batch tools — check the connected server's tool list.

## Required loop

1. Inspect the target file, page, section, and node structure.
2. Run one small, targeted `figma_execute` script.
3. Return all mutated/created node IDs and useful geometry.
4. Capture a screenshot immediately.
5. Check alignment, spacing, proportions, contrast, clipping, and
   legibility.
6. Iterate only when measurements or screenshots show a remaining issue.

Read the skill's `references/figma-execute.md` before writing any script:
it is the single contract for script conventions (top-level
`await`/`return`, font loading before text mutation, 0–1 color channels,
identity assertions, returned IDs) and for recovery from partial failures.

Do not put personal access tokens, pairing codes, or credentials in project
memory.
