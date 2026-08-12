# Figma Files and Boards

Register each Figma file before editing it. File keys and node IDs are
operational context, not secrets.

## Registered files

| Alias | File key | Primary page(s) | Status / context |
|---|---|---|---|
| _none yet_ | — | — | Provide a Figma link or file key, then create a living baseline |

## File context

Each registered alias should have:

- `docs/files/<alias>/design.md` — authority, design language, measured
  root sizes, components, variables, drift, and QA rules
- `docs/files/<alias>/screens.md` — screen inventory and golden references
  when the file contains composed surfaces

## Scope notes

- Re-search node IDs in the connected file at the start of each session.
- Do not assume another file's style system, root sizes, or page authority
  applies here.
- Do not store access tokens, pairing codes, or private credentials.
