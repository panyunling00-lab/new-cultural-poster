# Big Type Only — profile-conditional

> **Typography profile:** read [typography-constraints.md](../typography-constraints.md) first. Type scale, density, margins, negative space and hierarchy come only from the active profile: `assets/typography-defaults.json` names the default profile and links its file, and the numbers live in that profile's own file under `assets/`. Under `small-type-refined-v1` the profile's caps override any scale, density, type-dominance, cropping or edge-placement wording below; under `design-free-v1` this definition applies as written.

## Use Cases
Typographic cultural posters whose designed lettering carries the concept.
## Composition Structure
Use expressive large lettering as the main visual: deconstruct, brush, extrude, outline, stipple or sketch by theme. Introduce scale contrast, uneven rhythm, vertical reading or a purposeful path. Do not enlarge an untouched font as the only concept.
## Text Placement
Title may span the canvas, cross layers and overlap graphic shapes. Supporting copy remains complete and readable at normal size; clipping must not remove unique required characters.
## Aspect-Ratio Behavior
Adapt to portrait or landscape; no type-area caps.
## Avoid
Pseudo-text, incorrect glyphs, invented facts and unreadable mandatory information.

## Compatibility

Under `small-type-refined-v1` this layout is legacy and ineligible: it requires event lettering to dominate, which conflicts with the graphic-led, small-type profile. Do not select it for A/B/C candidates, single posters, selected variants or edits, and `scripts/build_prompt.py` keeps it out of the candidate pool. Under `design-free-v1` it is fully eligible and the definition above applies as written, including `Typography moves` lettering treatment.

If the active profile is small-type and the user explicitly requests this layout, explain the concrete conflict with the active typography profile before choosing a compatible direction, for example `large-geometry`, `off-center-hero`, `editorial-column` or `modular-grid`. Original calligraphy supplied as artwork can be the image subject; typeset event copy still follows the active profile.
