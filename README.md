# Justin Figma Design

`justin-figma-design` gives Cursor a repeatable way to work with Figma:
inspect screens, refine layouts, review components, check themes, and
visually QA the result. You do not need to write code to use it. In Cursor,
you can also call it `/jfd`.

## What you need

- Cursor, or another app that supports Agent Skills
- Figma Desktop
- Node.js (only needed for the one-line install and NPX setup steps)
- Figma Console MCP, which connects the AI to the Figma file

Download [Node.js LTS](https://nodejs.org/en/download/) if it is not already
installed. You can skip Node.js only if someone has already installed the
skill and connected Figma for you.

## Install the skill

### Recommended: one-line install

Open your computer's Terminal and paste:

```bash
npx skills add 1955m/justin-figma-design
```

The installer may ask where to install it. Choose **Cursor** and the current
project for a project-only install. To make it available in every project,
use:

```bash
npx skills add 1955m/justin-figma-design --global --agent cursor
```

You can also use the full GitHub URL:

```bash
npx skills add https://github.com/1955m/justin-figma-design
```

### Manual install: no command line

1. Open the repository on
   [GitHub](https://github.com/1955m/justin-figma-design).
2. Choose **Code → Download ZIP**, then unzip the download.
3. Copy the unzipped skill folder into your project's skill folder:

   ```text
   .agents/skills/justin-figma-design/
   ```

   Cursor can also read:

   ```text
   .cursor/skills/justin-figma-design/
   ```

4. Restart or reload Cursor so it can discover the skill.

The `npx skills` installer handles these folders for you. Manual copying is
useful when you do not want to install Node.js.

## Connect Figma for real editing

Installing the skill gives Cursor the workflow instructions. Connecting
Figma Console MCP gives it access to the canvas.

1. Install or enable
   [Figma Console MCP](https://github.com/southleft/figma-console-mcp) in
   Cursor as `user-figma-console`.
2. Open the Figma file you want to work on in **Figma Desktop**.
3. Start the local/NPX MCP server and connect its **Desktop Bridge** to the
   open file. Follow the current setup instructions in the Figma Console MCP
   repository; its setup steps can change over time.
4. Return to Cursor and confirm that the target Figma file is active.

The hosted or remote connection is suitable for looking and investigating.
The local server plus Desktop Bridge is required for edits and screenshots.

## Start your first session

1. Open your design project folder in Cursor.
2. In Cursor Chat, type:

   ```text
   jfd init
   ```

   You can use `/jfd init` if slash commands are enabled. This creates the
   project's `docs/` memory files and does not change anything in Figma.
3. Paste your Figma link or say which open Figma file you want to work on.
4. Describe the design task in plain language.

For example:

```text
Audit this screen for spacing, alignment, and clipping.
```

```text
Compare the Light and Dark versions and fix the inconsistent component state.
```

```text
Review this flow first and create a read-only design baseline before editing.
```

## What to expect

The skill asks the AI to inspect the current Figma file before changing it,
reuse existing components and styles, make focused edits, and check the
result with screenshots. It keeps project notes separate from the reusable
skill instructions, so your workspace can remember its own fonts, layouts,
screens, and design decisions.

## Package contents

```text
justin-figma-design/
├── SKILL.md       # Core instructions for the AI
├── references/    # Detailed workflow and QA guidance
├── scripts/       # Workspace initialization helper
├── assets/        # Templates and graphics guidance
└── examples/      # Example operating scenarios
```

For the detailed setup and first-session workflow, see
[references/getting-started.md](references/getting-started.md).
