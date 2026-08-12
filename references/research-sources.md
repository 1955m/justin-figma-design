# Research sources

This skill combines project memory with current external guidance. Project
memory wins when a file has an explicit authority or a documented exception.
External guidance supplies defaults for new or undocumented work — resolved
at run time via the resolution order, never baked into this package.

## Official Figma guidance

- [Guide to Auto Layout](https://help.figma.com/hc/en-us/articles/360040451373-Guide-to-auto-layout)
  — flow, padding, gap, alignment, nesting, and axis-specific Hug, Fill,
  Fixed, and min/max sizing encode responsive intent. Ignore auto layout is
  an intentional exception, not a substitute for structure.
- [Guide to variables in Figma](https://help.figma.com/hc/en-us/articles/15339657135383-Guide-to-variables-in-Figma)
  — variables store reusable design values and support design systems,
  themes, responsive contexts, prototypes, and the Plugin/REST APIs.
- [Overview of variables, collections, and modes](https://help.figma.com/hc/en-us/articles/14506821864087-Overview-of-variables-collections-and-modes)
  — collections organize variables; modes represent contexts such as
  Light/Dark, device sizes, or languages; aliases support token systems.
- [Components collection: Tips for component management](https://help.figma.com/hc/en-us/articles/39747637290263-Components-collection-Tips-for-component-management)
  — semantic names, slash hierarchy, properties, state documentation,
  accessibility guidance, safe updates, and deprecation.
- [Component property fundamentals](https://help.figma.com/hc/en-us/articles/39636407507735-Components-collection-Component-property-fundamentals)
  — Boolean, Text, Instance swap, Slot, and Variant properties expose
  intended customization without multiplying variants.
- [Guide to libraries](https://help.figma.com/hc/en-us/articles/360041051154-Guide-to-libraries-in-Figma)
  — libraries publish reusable components, styles, and variables; instances
  receive reviewed updates from the main component.
- [Check designs](https://help.figma.com/hc/en-us/articles/39592284074263-Check-designs-in-Figma)
  — checks hard-coded colors, dimensions, typography, contrast, and
  incorrect/detached library assets. Page-scoped and plan-dependent, so the
  skill requires a manual/MCP fallback.
- [Add measurements and annotate designs](https://help.figma.com/hc/en-us/articles/20774752502935-Add-measurements-and-annotate-designs)
  — annotations communicate spacing, sizing, accessibility, content, and
  interaction intent where rendered pixels cannot.
- [Optimize design files for developer handoff](https://help.figma.com/hc/en-us/articles/360040521453-Optimize-design-files-for-developer-handoff)
  — descriptive pages/layers, organized sections, component documentation,
  canonical examples, and handoff statuses.
- [Plugin API documentation](https://www.figma.com/plugin-docs/)
  — the API surface that `figma_execute` scripts call. Runtime-check
  anything questionable; the API evolves.

## Execution stack

- [Figma Console MCP](https://github.com/southleft/figma-console-mcp) — the
  required execution stack: `figma_execute`, `figma_take_screenshot`,
  `figma_get_status`, `figma_reconnect`, plus higher-level token/batch tools
  in current releases. Read the repository docs for the current tool list
  and Desktop Bridge setup; the surface changes between versions.

## Accessibility

- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
  — contrast, focus, target size, keyboard behavior, and non-color
  communication. Resolve the current criteria relevant to the product
  surface and platform at run time, and record the standard applied in the
  target file's `design.md`.

## Workspace evidence

Rules in this skill were distilled from real design sessions. That evidence
lives — and keeps accumulating — in each workspace's `docs/sessions/` notes
and per-file `design.md` histories, not in this package. When a session
teaches a reusable lesson, record it there; when it teaches a universal
lesson, consider promoting it into a reference file here.

Sources reviewed 2026-08-12. Re-check official links when Figma changes the
feature model or terminology, and re-verify any platform value (device
sizes, target minimums) at the moment of use rather than trusting this
date.
