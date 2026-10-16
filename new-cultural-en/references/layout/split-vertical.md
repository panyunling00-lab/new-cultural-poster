# Split Vertical — excluded by the continuous-image rule

> **Typography profile:** read [typography-constraints.md](../typography-constraints.md) first. Type scale, density, margins, negative space and hierarchy come only from the active profile: `assets/typography-defaults.json` names the default profile and links its file, and the numbers live in that profile's own file under `assets/`. Under `small-type-refined-v1` the profile's caps override any scale, density, type-dominance, cropping or edge-placement wording below; under `design-free-v1` this definition applies as written.

## Use Cases

Use for exhibitions, lectures, arts festivals, and cultural events where imagery and explanation both matter. Suitable for two subjects, concepts, or information groups that benefit from comparison or association.

## Selection Signals

Choose when two related zones need simultaneous visibility, or the theme compares ancient and modern, old and new, different cultures, or tradition and innovation. Use when clear information organization and reading order are important.

## Composition Structure

- Divide the canvas into two vertical zones.
- Assign one to the main image and the other to title and information, or use both for related subjects.
- Use unequal widths to establish priority.
- Connect the zones through a boundary, gradient, or carefully interwoven element.

## Hierarchy Rules

1. The relationship between the two zones provides the first read.
2. Title explains their thematic connection.
3. Date, venue, and organizer details sit at the bottom or in a corner.

## Text Placement

- Align title, body copy, and date to a consistent vertical grid.
- Keep a complete headline within one zone.
- Group supporting text rather than distributing it across both areas.

## Image Treatment

Use photography, people, objects, artifacts, or artworks. Crop, enlarge, or show details to strengthen the comparison. Keep a text-bearing zone visually calm.

## Spacing Rules

Make the division clear. Leave breathing room at the boundary and use space to clarify how the two contents relate.

## Aspect-Ratio Behavior

Works in `2:3`, `3:4`, `4:5`, and `16:9`. For narrow formats, consider a `40/60` or `35/65` width split.

## Avoid

- An automatic `50/50` split with no priority.
- Dense information on both sides or unrelated side-by-side content.
- Text and image competing for one focal point.
- Forcing a continuous timeline into a left–right comparison.

## Compatibility

This layout divides the canvas into visible vertical panels. The global continuous-image rule excludes it from default A/B/C selection, single posters, selected variants and edits in every typography profile, and `scripts/build_prompt.py` keeps it out of the candidate pool. Only a later explicit user instruction can lift the exclusion; record the scope of that instruction. Organise a continuous visual space with large form, scale, negative space and depth order instead.
