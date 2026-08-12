# Getting started with `/jfd`

This guide covers installing and initializing the skill in a new workspace.
It is written for Agent Skills-compatible hosts on macOS, Windows, and
Linux.

## What the package provides

`justin-figma-design` is the reusable workflow: the mode router, the
resolution order, `figma_execute` script conventions, design-system and
layout guidance, variable/theming rules, graphics guidance, and visual QA
checklists. It deliberately contains **no project facts** — no device sizes,
fonts, or style preferences.

The workspace owns the project-specific memory:

- `AGENTS.md` — always-on project facts and the skill/MCP relationship
- `docs/preferences.md` — stable collaboration preferences
- `docs/FILES.md` — registered Figma files and authority
- `docs/files/<alias>/design.md` — living context for each Figma file
- `docs/files/<alias>/screens.md` — screen and state inventory
- `docs/sessions/` — dated work notes
- `docs/assets/` — graphics guidance and user-provided placeholders

Procedures live in the skill. Project facts live in workspace memory. Truth
lives in the Figma file.

## Install the skill

Use a project-local skill root when the workspace should travel with its
configuration:

```text
.agents/skills/justin-figma-design/
```

`.agents/skills/` is the portable canonical target. A host may also discover
compatible roots such as `.cursor/skills/justin-figma-design/` or an
agent-specific user skill root. Use the host's documented discovery root
when installing globally. Do not hard-code a home directory, shell profile,
package manager, or operating-system path into the project. The `/jfd`
alias is a convenience; agents should also recognize the skill by name and
description.

## Set up Figma Console MCP

For any actual Figma work, install and connect
[Figma Console MCP](https://github.com/southleft/figma-console-mcp)
(`user-figma-console`):

- Run the **local/NPX server** and connect the **Desktop Bridge** to the
  target Figma Desktop file. This is required for `figma_execute` writes and
  screenshots.
- The hosted remote mode is **read-only**; it can support investigation but
  not mutation.
- Follow the repository's own setup documentation for the current install
  steps and tool list — the tool surface evolves between versions.

Init itself is local and does not require an active Figma connection.

## Initialize an empty folder

1. Open the target folder as the agent workspace.
2. Invoke `jfd init`, or `/jfd init` when slash aliases are supported.
3. If the folder is not empty, review the missing-path list and confirm
   before writing. Existing files, directories, symlinks, and skill
   installations are always preserved.
4. Copy the missing files from this skill's `assets/templates/` directory:
   `AGENTS.md`, the `docs/` memory scaffold, and
   `docs/files/_template/{design.md,screens.md}`.
5. Install missing project-local skill copies under `.agents/skills/` and
   the host-compatible `.cursor/skills/` location when appropriate.
6. Verify the scaffold and keep the first Figma file deferred until the user
   provides a link or file key.

The agent's normal file tools are the primary init path. When using that
path, copy files only when the destination is missing, preserve relative
forward-slash paths in documentation, and report every created or skipped
path. The scaffold does not require a project display name or a Figma file;
never invent a file key, URL, credential, or private project data.

## Optional Python helper

`scripts/init_project.py` performs the same scaffold in one bulk operation.
It uses only Python's standard library and is portable across macOS,
Windows, and Linux:

```text
python scripts/init_project.py
python3 scripts/init_project.py --root path/to/workspace
```

Use `--dry-run` to list missing files without writing, and `--yes` only
after reviewing a non-empty target. The helper is idempotent: rerunning it
skips every existing destination and never overwrites content. It does not
install MCP, connect to Figma, or mutate a Figma file.

## First design session

After init, read `docs/preferences.md`, `docs/FILES.md`, and the latest
relevant session note, then fork:

**Existing Figma file** (the default):

1. Ask the user for the Figma link or file key and a useful alias.
2. Register the file in `docs/FILES.md`.
3. Create `docs/files/<alias>/design.md` — and `screens.md` for composed
   screens — as a **read-only investigation baseline**: measure root sizes,
   typography, tokens, and conventions before proposing anything.
4. Only then begin the normal non-YOLO loop.

**New design from scratch** (nothing to measure): follow
[starting-from-scratch.md](starting-from-scratch.md) — establish intent,
resolve and confirm foundation values with the user, build foundations
first, and record the new authority in `design.md` before the session ends.

Either way, read `docs/tools/figma-console.md` and
[figma-execute.md](figma-execute.md) before Console work. Init never mutates
Figma; normal design work follows the inspection, small-write, screenshot,
and family-level QA contract.
