# justin-figma-design

`justin-figma-design` is a reusable Agent Skill for inspecting, editing, and
visually QAing Figma files through Figma Console MCP. It is also available as
`/jfd`.

Use it when you need to work with Figma screens, components, variants,
variables, themes, Auto Layout, responsive states, annotated screenshots, or
design-system consistency. The skill measures the target file and records
project-specific facts instead of relying on fixed device sizes, fonts, or
spacing assumptions.

## Requirements

- An Agent Skills-compatible host such as Cursor
- [Figma Console MCP](https://github.com/southleft/figma-console-mcp)
  connected as `user-figma-console`
- Figma Desktop with the Desktop Bridge connected to the target file for
  writes and screenshots

The hosted MCP mode supports read-only investigation. Local/NPX mode with the
Desktop Bridge is required for mutations and visual verification.

## Install

Copy this directory into the project-local skill root:

```text
.agents/skills/justin-figma-design/
```

`.agents/skills/` is the portable canonical location. Hosts that use the
Cursor-compatible convention can also discover:

```text
.cursor/skills/justin-figma-design/
```

## Initialize a workspace

From an empty or existing workspace, run:

```text
jfd init
```

If slash aliases are unavailable, use the bundled helper:

```bash
python3 scripts/init_project.py
```

See [references/getting-started.md](references/getting-started.md) for the
initialization flow and first design session.

## Package layout

This follows the typical Agent Skills structure: `SKILL.md` contains the
trigger metadata and core instructions, while bundled resources are loaded as
needed.

```text
justin-figma-design/
├── SKILL.md
├── scripts/
├── references/
├── assets/
└── examples/
```

## References

- [Getting started](references/getting-started.md)
- [Figma execution conventions](references/figma-execute.md)
- [Modes and workflow](references/modes-and-workflow.md)
- [Components and design systems](references/components-and-design-system.md)
- [Layout and Auto Layout](references/layout-and-autolayout.md)
- [Variables and theming](references/variables-and-theming.md)

The skill contains procedures, not project facts. Workspace memory belongs in
the generated `docs/` files, and the Figma file remains the source of truth.
