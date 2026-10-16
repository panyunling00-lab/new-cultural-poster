# Modular Grid — excluded by the continuous-image rule

> **Typography profile:** read [typography-constraints.md](../typography-constraints.md) first. Type scale, density, margins, negative space and hierarchy come only from the active profile: `assets/typography-defaults.json` names the default profile and links its file, and the numbers live in that profile's own file under `assets/`. Under `small-type-refined-v1` the profile's caps override any scale, density, type-dominance, cropping or edge-placement wording below; under `design-free-v1` this definition applies as written.

## Use Cases

Use for exhibitions, museums, design events, arts festivals, and cultural programs with multiple works, themes, or information groups. Suitable for series, collections, and event information sets.

## Selection Signals

Choose when several content units have comparable importance, multiple images or works need simultaneous presentation, and information naturally belongs in categories or modules.

## Composition Structure

- Divide the canvas into a regular grid.
- Place images, text, and details in independent modules.
- Maintain consistent dimensions or proportional relationships.
- Use combinations of modules to create a unified whole; vary the grid when the content requires it.

## Hierarchy Rules

1. Overall grid establishes visual order.
2. A highlighted module identifies the main content.
3. Each module has its own title, image, and description hierarchy.

## Text Placement

- Follow consistent module rules for placement, type size, and spacing.
- Keep each unit understandable on its own.
- Allocate modules for complete supplied copy and retain the global small-type scale.

## Image Treatment

Use multiple photographs, illustrations, artworks, or information graphics. Consistent image ratios can reinforce the overall visual system.

## Spacing Rules

Maintain clear gutters between modules. Leave some cells open when useful and use negative space to define module boundaries.

## Aspect-Ratio Behavior

Works in `2:3`, `3:4`, `4:5`, and `16:9`. Landscape formats accommodate more modules.

## Avoid

- Too many modules that fragment attention.
- Equal emphasis everywhere with no focal point.
- An image array without information logic.
- A layout reduced to a generic table.

## Compatibility

This layout composes multiple visible frames or panels. The global continuous-image rule excludes it from default A/B/C selection, single posters, selected variants and edits in every typography profile, and `scripts/build_prompt.py` keeps it out of the candidate pool. Only a later explicit user instruction can lift the exclusion; record the scope of that instruction. Hidden alignment grids remain available — only a drawn, visible grid is excluded.
