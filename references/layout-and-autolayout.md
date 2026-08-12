# Layout and Auto Layout

## Encode intent, not coordinates

Use Auto Layout when children have a semantic relationship: stacked content,
rows, columns, buttons, lists, forms, tables, or repeated cards. Use nested
vertical, horizontal, or grid flows to express reading order and reflow.

Use padding and gap/item spacing for designed rhythm. Do not create
invisible rectangles or "spacer" frames to preserve the Y positions of an
old absolute layout. After conversion, reassess density and re-anchor
content rather than fossilizing accidental gaps.

Absolute positioning, exposed as **Ignore auto layout**, is appropriate only
for intentional overlays, masks, home indicators, decorative layers,
calibrated chrome, captions/connectors around a flow, or a documented legacy
exception. Keep a structural screen root fixed when the target file requires
it, while using Auto Layout inside semantic content regions.

## Choose sizing per axis

| Situation | Width / height intent |
|---|---|
| Content-driven button, badge, dialog group, or stack | Hug contents |
| Child that should consume its parent's available space | Fill container |
| Measured screen root, icon box, CTA, calibrated shell, or fixed column | Fixed |
| A responsive boundary with meaningful limits | Min/max plus the appropriate base sizing |
| Text that should reflow with copy | Hug / auto width and auto height unless the design explicitly constrains it |

The choice is independent per axis: a frame can be fixed in width and hug in
height. Fill only makes sense for a child in an Auto Layout parent with
available space; a Fill child can prevent its parent from hugging that axis.
Do not use Fill as a generic "make it wide" instruction.

When creating nodes through the Plugin API, parent them into the intended
Auto Layout context before assigning HUG or FILL — see
[figma-execute.md](figma-execute.md).

## File-specific patterns live in design.md

Every file develops recurring layout authorities: its root frame sizes,
sheet and dialog widths, row heights, column rules, and deliberate absolute
compositions. This skill ships **none of them** — they drift as devices and
products change. Instead:

- Measure the pattern in the file, or resolve it via the resolution order.
- Record it in the target `docs/files/<alias>/design.md` with the date, e.g.
  "phone roots in this file are W×H (measured YYYY-MM-DD); sheets stay fixed
  at the root width and re-anchor to the bottom after height changes."
- Apply a recorded pattern only after confirming the target file's living
  context still asserts it.

A pattern recorded for one file is never authority for another file.

## Reflow audit after resizing

For every resized parent, inspect:

1. all fixed-width and Fill descendants;
2. text box sizing, line wrapping, and max dimensions;
3. charts, plot areas, tables, column widths, and progress bars;
4. form fields, inputs, and nested labels;
5. header spacers, action groups, icons, and empty states;
6. left/right content edges and alignment with sibling sections;
7. overflow, clipping, and useful space utilization at each supported width.

Compare descendant bounds with every relevant ancestor, not only the
top-level board. A clean board screenshot can hide a nested field twice as
wide as its owning column when a sibling paints over the overflow.

## Layout anti-patterns

- Making every frame Auto Layout without separating semantic content from
  overlays and calibrated chrome.
- Preserving absolute Y gaps with empty helper frames.
- Resizing a parent while leaving fixed descendants at the old width.
- Setting Fill on a child with no meaningful available parent dimension.
- Using fixed-height text boxes that clip longer copy.
- Treating a screenshot as proof that the constraint chain is correct.
- Reparenting by name or guessed ID without checking the complete ancestor
  chain.

Validate structure after the mutation and use focused, board, and family
screenshots as appropriate. See [qa-and-recovery.md](qa-and-recovery.md).
