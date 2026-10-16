# Split Horizontal — excluded by the continuous-image rule

> **Typography profile:** read [typography-constraints.md](../typography-constraints.md) first. Type scale, density, margins, negative space and hierarchy come only from the active profile: `assets/typography-defaults.json` names the default profile and links its file, and the numbers live in that profile's own file under `assets/`. Under `small-type-refined-v1` the profile's caps override any scale, density, type-dominance, cropping or edge-placement wording below; under `design-free-v1` this definition applies as written.

## Use Cases

Use for cultural events, exhibitions, performances, and campaigns with clear upper–lower relationships. Suitable for connecting an atmospheric scene or theme visual with event information.

## Selection Signals

Choose when a wide scene, architecture, landscape, group photograph, or exhibition space needs an intact image zone. Appropriate for top-to-bottom progression, such as concept to example, context to subject, atmosphere to information, or historical background to contemporary interpretation.

## Composition Structure

- Divide the canvas into upper and lower zones.
- Assign one to the main visual and the other to title, explanation, and supporting information.
- Use unequal heights to establish priority.
- Connect zones through color, boundaries, gradients, or spatial continuity.

## Hierarchy Rules

1. Main visual attracts attention.
2. Title and theme statement establish understanding.
3. Date and venue remain supporting information.

## Text Placement

- Concentrate text in the information zone.
- Keep reading horizontal.
- Avoid running text across the division.

## Image Treatment

Use a wide image or scene as an independent zone or an extended background. Preserve its visual integrity rather than fragmenting it into excessive crops.

## Spacing Rules

Maintain a clear relationship between upper and lower zones. Vary information density instead of making both equally busy.

## Aspect-Ratio Behavior

Works in `16:9`, `4:5`, and `3:4`. Landscape supports broad image zones; portrait layouts need sufficient vertical spacing to prevent crowding.

## Avoid

- Equal-height zones without visual priority.
- Image and text interfering with each other.
- An information zone too shallow for readable text.
- Forcing a left–right comparison into an upper–lower split.

## Compatibility

This layout divides the canvas into visible horizontal panels. The global continuous-image rule excludes it from default A/B/C selection, single posters, selected variants and edits in every typography profile, and `scripts/build_prompt.py` keeps it out of the candidate pool. Only a later explicit user instruction can lift the exclusion; record the scope of that instruction. Organise a continuous visual space with large form, scale, negative space and depth order instead.
