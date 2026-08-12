# Starting from scratch

Use this workflow when there is nothing to measure: a brand-new Figma file,
an empty page intended as a new product surface, or a new form factor with no
existing frames, tokens, or `design.md` authority. The moment the first
frames exist, switch back to the default measure-first workflow — from then
on the file itself is the authority.

Scratch mode's whole job is to **create the authority** that every later
session will measure.

## 1. Establish intent

Ask the user (or confirm from the request) before proposing anything:

- Platform(s) and form factor: phone, responsive web, tablet, foldable,
  desktop — and which of these the file must cover.
- Orientation(s) and whether multiple widths/states are in scope now or
  later.
- Theme support: light only, or light/dark from day one.
- Any existing brand, product, or reference material the user wants honored.

## 2. Resolve the foundation values

Nothing exists to measure, so the resolution order starts at workspace
memory:

1. Check `docs/preferences.md` for standing decisions (default font,
   spacing preferences, icon sources).
2. For anything unset — root frame size, base typography, spacing step,
   color direction — **ask the user or look up current platform guidance**
   for the stated form factor. Device generations change; never reuse a
   remembered size or a default from this skill's text.
3. Propose concrete values with a one-line rationale each.

## 3. Confirm before building

Get explicit user confirmation on, at minimum:

- Root frame size(s) per target form factor.
- Base font family and how weights map.
- Theme support (and therefore whether modes are created now).
- Spacing step and radius direction, if the user cares to decide now.

Do not begin creating nodes until these are confirmed. This is the scratch
equivalent of the plan gate.

## 4. Build foundations first

Scratch work is always non-YOLO unless the user explicitly requests a
disposable YOLO board. Build in this order:

1. **Variables and modes** — the smallest coherent primitive + semantic
   token set for the approved scope; Light/Dark modes if confirmed. See
   [variables-and-theming.md](variables-and-theming.md).
2. **Styles and components** — bound to semantic variables, Auto Layout
   inside, variants and properties per
   [components-and-design-system.md](components-and-design-system.md).
3. **Screens** — instances composed on root frames of the confirmed size,
   laid out per [layout-and-autolayout.md](layout-and-autolayout.md).

Keep the standard execute-and-verify loop throughout: small `figma_execute`
scripts, returned IDs, immediate screenshots.

## 5. Record the authority immediately

Before ending the first scratch session:

- Register the file in `docs/FILES.md`.
- Create `docs/files/<alias>/design.md` recording every confirmed decision —
  root sizes, typography, spacing, theme model, naming — each with today's
  date.
- Create `screens.md` once composed screens exist.
- Write a dated session note.

## Scratch-mode QA

There is no family to compare against yet, so QA is self-consistency:

- Every foundation value used on canvas matches the confirmed decisions and
  is bound to variables, not hard-coded.
- Both themes resolve on every component and screen state, if modes exist.
- Long-copy, empty, and disabled states behave inside the new components.
- The recorded `design.md` matches what is actually on canvas — the next
  session will trust it.
