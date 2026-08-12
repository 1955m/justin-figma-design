# Variables and theming

Variables are the non-YOLO source of truth for reusable values and
contextual themes. Figma collections group variables; modes provide
alternate definitions for the same variable. Use them to encode context, not
to hide arbitrary one-off geometry.

## Audit before creating

Before adding a collection or variable:

1. Inspect local collections, modes, bound variables, styles, and existing
   component instances in the authoritative target page.
2. Inspect enabled/published libraries and search remote variables when
   local results are incomplete.
3. Identify whether the target file already has a primitive/semantic model,
   theme modes, naming convention, and code syntax.
4. Reuse or extend the authoritative system. Do not create duplicate
   same-purpose collections because a local query returned no result.

Record the gap when a new collection or token is truly needed.

## Token model

Prefer two layers:

```text
primitive/color/blue/500
primitive/spacing/16
semantic/color/surface/default
semantic/color/text/primary
semantic/spacing/control/gap
```

Semantic variables alias primitives rather than duplicating raw values. Bind
production component properties to semantic variables. Keep primitives
scoped/hidden from ordinary pickers where supported, and scope semantic
variables to the properties they are intended to control, for example:

- fills and surfaces;
- text fills;
- strokes;
- gap/padding;
- corner radius;
- dimensions or min/max bounds.

Use the target file's naming vocabulary when it differs. A token name should
describe role and purpose, not its current appearance.

## Light and Dark modes

For a product that supports both themes:

1. Create or reuse Light and Dark modes on the semantic collections.
2. Define the semantic value in every required mode; do not leave accidental
   fallbacks.
3. Bind fills, strokes, text, effects, icons, and component properties to
   semantic variables where the property supports binding.
4. Apply the intended mode at the relevant frame/component context and
   verify nested inheritance and deliberate overrides.
5. Test every affected state in both modes: default, selected, active,
   expanded, collapsed, disabled, loading, error, empty, and overlay states
   where they exist.
6. Check contrast and icon treatment in both modes. A visually similar dark
   twin is not proof that the same semantic binding is present.

Do not maintain Light/Dark as unrelated hard-coded paint when a mode model
is appropriate. Preserve a documented hard-coded exception when the target
file's authority requires it, such as a deliberately distinct asset or
legacy shell.

## Other useful modes

Use number-variable modes for approved device, density, or
responsive-spacing contexts when the file has a coherent system for them.
Use string variables for approved localization or typography contexts when
that is part of the file's model. Modes do not replace Auto Layout,
breakpoint reasoning, or content QA.

Do not create a variable for a single one-off value that has no reuse,
contextual variation, or system meaning.

## Binding and validation

After binding:

- inspect the node's bound-variable metadata, not only its rendered color;
- verify mode resolution on representative instances and nested components;
- check that mode changes do not alter unrelated typography, spacing, or
  copy;
- scan for hard-coded values where semantic bindings are expected;
- verify detached instances and local overrides intentionally, not
  accidentally;
- run Figma Check designs when available, then manually resolve any
  remaining hard-coded or incorrect-library values.

When creating many variables, prefer the Console MCP's dedicated batch and
design-token tools where the connected server provides them (see
[figma-execute.md](figma-execute.md)); otherwise use small chunked scripts.
Set explicit scopes and modes. Return every created/updated ID and the
collection/mode map so later work does not depend on guessed IDs.

## Theme QA matrix

The minimum useful matrix is:

```text
component × state × theme
screen family × responsive state × theme
```

For each cell, check:

- surface/text/stroke/icon contrast;
- selected and disabled affordances;
- visibility of labels, chevrons, wordmarks, and toggles;
- shared content edges and sizing;
- nested instance overrides;
- clipping, overflow, and long-copy behavior.

If the change affects shared chrome, do not validate only the first Light
screen. Update and screenshot every related Light/Dark family member.
