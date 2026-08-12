# Components and design systems

## Reuse decision order

For non-YOLO work, search in this order:

1. Existing instances and main components on the authoritative target pages.
2. Local variables, styles, and component sets in the target file.
3. Enabled/published libraries already connected to the file.
4. Broader library search, scoped to the relevant library where possible.
5. A new local component only after the gap and ownership decision are
   documented.

Do not treat an old archive page or a visually similar component in another
file as authoritative without checking the target file's `design.md`.

If a compatible component exists, instantiate it and preserve its link. Do
not detach it merely to make a local edit. If the API is close but not
sufficient, prefer a controlled wrapper or an extension with an explicit
ownership and maintenance decision.

## Foundations before new components

If the target file has no adequate foundation for the approved scope:

1. Inspect existing local and remote variables, styles, and modes first.
2. Define the smallest coherent primitive and semantic token set.
3. Create Light/Dark modes when the product supports both.
4. Bind component properties to semantic variables.
5. Build components only after the foundation is inspectable.
6. Add instances to screens and verify both themes and all relevant states.

Do not create a parallel design system because local variable discovery is
empty; remote/published libraries may still contain the authoritative
assets. Use the appropriate library search and inspect existing screens.

For variable construction and mode QA, read
[variables-and-theming.md](variables-and-theming.md). For script conventions
when creating nodes, variables, and components, read
[figma-execute.md](figma-execute.md).

## Component shape

Use Auto Layout for containers whose children relate. Choose sizing per axis
and keep the component resilient to longer copy, optional content, and
instance swaps.

Use:

- **Variants** for predictable visual or structural differences such as
  type, size, state, theme, or density.
- **Boolean properties** for optional visibility.
- **Text properties** for intended editable copy.
- **Instance swap properties** for curated nested assets such as icons.
- **Slot properties** for flexible repeated or content areas where
  supported.

Keep variant axes separate. Prefer `Type=Primary`, `Size=Medium`, and
`State=Default` over a single compound value such as
`Primary Medium Default`. Avoid a variant matrix that grows combinatorially;
move content flexibility into properties or split the component.

## Naming and documentation

Match the target file's terminology. When there is no established
convention, use semantic slash-separated names such as:

```text
button/primary
input/text/default
navigation/sidebar/item
```

Name structural child layers by purpose, not appearance or creation order.
Avoid `Rectangle 12`, `Frame 427`, and color-based names that become wrong
after a theme change.

Add a concise component description covering:

- intended use and non-use;
- supported variants and properties;
- state behavior and validation;
- accessibility/contrast or focus guidance;
- important layout constraints;
- links to external documentation when available.

## Safe library evolution

Before changing a main component or published asset, classify the change:

- Non-breaking: an optional hidden-by-default property or an internal visual
  refinement that preserves existing overrides.
- Breaking: removing/renaming properties, changing variant resolution, or
  renaming layers that instances override.

For breaking work, inspect usage, test representative existing instances,
and record the impact before publishing. Never remove a used component
without a deprecation path unless the user explicitly directs it.

## YOLO boundary

YOLO never creates a new component, variant set, variable collection, or
library asset — see the full rules in
[modes-and-workflow.md](modes-and-workflow.md). If a quick result is likely
to be reused, or the same pattern appears in another state, stop and
escalate to non-YOLO before copying it.
