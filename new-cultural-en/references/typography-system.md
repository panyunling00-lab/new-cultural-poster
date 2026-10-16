# Cultural poster typography system

## Active profile

This file applies only when `typography_profile=small-type-refined-v1`. Default free design uses typography-constraints instead; these numeric caps do not apply there. The numeric source is `assets/typography-small-type.json`, loaded by typography_policy for prompts, rendering, and review. Pairings, tonal clusters, and text–image guidance here describe this profile.

Read during planning, assembly, refinement, and review, after category/layout routing. Paths are relative to the skill root.

## 1. Quick selection — event to composition to type

These are starting points, not templates. Explicit user choices, theme, copy length, and style determine the final system. IDs must exist; global exclusions still apply to legacy suggestions below.

| Event/theme | Starting composition | Title pairing | Information and relationship |
|---|---|---|---|
| Technology/design methods/public issues talk | editorial-column / modular-grid | Neutral Modern; Heavy Impact for emphasis | Neutral Modern; aligned columns and grouped information |
| Literature/history/philosophy talk or reading | editorial-column / minimal-white-space | Bookish Print; Warm Handwritten for casual groups | Neutral Modern or Bookish Print, beside pages/images |
| Art/design exhibition A | off-center-hero / editorial-column | Contrast Serif or Neutral Modern | Neutral Modern in a quiet side region |
| Performance/music/dance B | diagonal-dynamic / radial-composition | Heavy Impact or Ornate Serif | Neutral Modern along motion axes, stable functional copy |
| Heritage/ceramics/weaving/crafts C | layered-depth / frame-within-frame | Bookish Print or Warm Handwritten | Neutral Modern linked through edges/material/space |
| Forum/seminar/workshop D | modular-grid / split-vertical | Neutral Modern | Shared alignment for title, program, participation |
| Festival/family/market E | modular-grid / radial-composition | Rounded Geometric or Warm Handwritten | Neutral Modern; clear grouping, no separate type system per activity |
| New media/experimental art F | large-geometry / folded-space | Neutral Modern or Contrast Serif | May offset/embed, preserving accurate reading areas |
| Artifacts/rare books/museum G | centered-hero / frame-within-frame | Bookish Print or Elegant Serif | Bookish/Neutral, clear of identifying artifact details |
| Architecture/gardens/urban culture H | axonometric-spatial / layered-depth | Neutral Modern or Contrast Serif | Echo axes, boundaries, perspective |

Choose one title and one information pairing, not the whole library. A/B/C may share pairings but must differ in composition/relationships; swapping fonts alone is not a direction. Category never automatically authorizes calligraphy, seals, or unverified cultural symbols.

## 2. Family, scale, and weight budgets

- At most three actual families, preferably one or two. Count Chinese/Latin separately, not weights within one family. Bilingual work may use two Chinese families plus one shared Latin family.
- At most three size levels: title, subtitle, body/functional. Not three per language; optical matching must not create extra hierarchy.
- At most three weights, preferably regular/medium; bold for short titles. Information strokes must remain visible.
- With no subtitle, use two levels; invent no copy to fill a level. Body, dates, venue, and organizer share an information system differentiated by grouping/position/space.

## 3. Size, spacing, and measurement

Use the execution specification below and the profile JSON. Pairings/effects never override it.

## 5. Text–image relationships and execution

Choose one main relationship: juxtaposition, axis-following, framing, surface embedding, or local depth overlap. Follow the chosen layout rather than always using one corner. Do not damage/obscure cultural facts, original art, marks, or QR codes.

Integrated uses descriptive letterforms/strokes/spacing/weight, not font filenames, and requires character checking. Overlay uses supplied fonts with actual family/coverage records; no silent substitution. Artful titles and accurate information may use separate production methods while obeying this profile.

## 6. Compact record and edit checks

Record category, layout ID, title/information pairings, actual family budget, 2–3 sizes, weights, relationship, and regions. Send only the current scheme's concrete forms/copy/locations/profile constraints to prompts, not full mapping tables.

After HG3 preserve the selected system. Specify 1–3 changes with location/action/expected result. Compare actual before/after images; mark implemented/partial/unimplemented and check new errors, occlusion, or drift. No change cannot be called completed refinement.

Check exact complete copy, ≤3 families/levels/weights, title bounds/sizes, leading, margins, subject clearance, negative space, and actual-size readability. Unknowns remain unknown. Follow existing review/confirmation; add no gates.

## 7. Eight pairings

Chinese establishes tone; Latin follows. Include only supplied languages. At most two pairings and three families. Inspiration labels never go into image prompts. Numbered headings and the following description labels are parsed by build_prompt.py; preserve them.

### 1. Neutral Modern

- Inspiration: Satoshi + MiSans.
- Prompt-ready visual description: Chinese: geometric sans-serif forms, even proportions, light-to-medium strokes; Latin: geometric sans-serif, balanced widths and matching stroke weight; restrained, open tracking.
- Character/themes: calm neutrality; exhibitions, galleries, technology culture.
- Rule: coordinated weights and quiet spacing; small information remains readable.

### 2. Rounded Geometric

- Inspiration: ITC Avant Garde Gothic + Alibaba PuHuiTi 2.0.
- Prompt-ready visual description: Chinese: friendly geometric sans-serif, softened terminals, medium-to-bold weight; Latin: circular geometric structures, rounded appearance, matching medium-to-bold strokes.
- Character/themes: youthful friendliness; family activities and creative markets.
- Rule: match rounded rhythm and optical weight; no unsupported childish decoration.

### 3. Heavy Impact

- Inspiration: Helvetica Neue + Plix.
- Prompt-ready visual description: Chinese: extremely heavy compact strokes and compressed proportions; Latin: extra-bold condensed capitals, dense downward visual weight; marked contrast between title and information.
- Character/themes: forceful solidity; music festivals, contemporary culture, talks.
- Rule: title impact, calmer information; do not shrink functional copy.

### 4. Elegant Serif

- Inspiration: PingFang + MingLiU.
- Prompt-ready visual description: Chinese: slender Song/Ming-style forms with thin horizontals and stronger verticals; Latin: refined serif forms, elongated proportions, open tracking.
- Character/themes: formal elegance; openings, awards, fine arts.
- Rule: labels are inspiration; PingFang is not a serif. Integrated follows the described appearance, overlay matching supplied fonts.

### 5. Contrast Serif

- Inspiration: Classy Vogue + Source Han Serif CN.
- Prompt-ready visual description: Chinese: high-contrast Song strokes and sharp serifs; Latin: high-contrast editorial serifs, fine hairlines against strong verticals; refined magazine spacing.
- Character/themes: fashion/editorial; design exhibitions and fashion culture.
- Rule: coordinate script contrast; hairlines remain readable at delivery size.

### 6. Warm Handwritten

- Inspiration: FontQu Smile.
- Prompt-ready visual description: Chinese: warm handwritten strokes, rounded connected movement, slightly irregular rhythm; Latin, if supplied: matching soft handwritten forms with the same casual rhythm.
- Character/themes: approachable warmth; craft markets, reading groups, coffee culture.
- Rule: handwriting for short titles, neutral readable information; add no Latin copy.

### 7. Bookish Print

- Inspiration: HWMCT.
- Prompt-ready visual description: Chinese: printed Ming/Song forms, moderate stroke contrast and balanced bookish rhythm; Latin, if supplied: restrained book serifs with comparable weight and spacing.
- Character/themes: traditional literary; rare books, calligraphy, heritage.
- Rule: serif Latin follows bookish Chinese; no automatic aged paper/patterns.

### 8. Ornate Serif

- Inspiration: Kudry + Source Han Serif CN.
- Prompt-ready visual description: Chinese: expressive high-contrast Song display forms; Latin: ornate serif display forms, exaggerated curves and tightly controlled spacing; dramatic emphasis.
- Character/themes: theatrical ornament; galas, anniversaries, brand evenings.
- Rule: ornament limited to titles; functional information simple/readable.

## 8. Style and pairing coordination

| Cluster | Styles | Layouts | Pairings | Restrained decorations |
|---|---|---|---|---|
| Traditional literary | japanese-ma, cultural-editorial, botanical-premium, art-deco-luxe | editorial-column, frame-within-frame, minimal-white-space | Elegant Serif, Bookish Print, Ornate Serif | Fine frames, small seals, vertical dates, corner marks |
| Modern restrained | swiss-editorial, minimal-graphic, bauhaus-modular, monochrome-typographic | off-center-hero, modular-grid, split-vertical, large-geometry | Neutral Modern, Contrast Serif | Geometry, corner marks, icons, dividers |
| Expressive impact | neo-brutalist, constructivist-impact, pop-commercial, futurist-gradient | diagonal-dynamic, radial-composition, large-geometry | Heavy Impact, Rounded Geometric | Diagonal slices, supplied small numerals, stamp-like tags |
| Handmade warmth | organic-craft, screenprint, risograph-zine | layered-depth, frame-within-frame, folded-space | Warm Handwritten, Bookish Print | Hand strokes, postmarks, notes, paper |

Under this profile, assemble one style/layout/pairing within a tonal cluster; category mapping sets priority, and directions should cover distinct preferred structures. The source small-type guidance disallows cross-cluster mixing unless explicitly requested; record exceptions. Global exclusions and the main workflow prevail over legacy table suggestions. Resolve style/layout conflicts through selection-guide.

## 9. Text–image relationships

| Relationship | Operation | Boundary |
|---|---|---|
| Overprint | Title over quiet noncore imagery | Do not hide protected subject/functional copy |
| Interweave | Lines pass in front of/behind title | Keep glyphs complete; not for functional copy |
| Embed | Title joins paper/wall/geometry | Do not forge original artwork, inscriptions, or marks |
| Separate | Space/divider separates text/image | Keep shared reading axis and grouping |
| Recede | Lower supporting visual weight | Stay readable; no indefinite shrinking |

Choose one main relationship. Overprint/interweave/embed only affect noncore imagery or independent decoration. Follow protected-subject clearance, title bounds, and size rules below.

## Execution and measurement specification

Read before planning, prompt assembly, rendering, and review. This profile's numeric source is `assets/typography-small-type.json`; `scripts/typography_policy.py` loads it for prompts, rendering, and quality checks. This profile applies to every single poster, each A/B/C candidate, selected-direction variant, edit, and derivative. Library references and existing previews never waive it. Preserve all required copy and original assets. Only a later explicit user instruction can change the constraint; the bundled tools deliberately enforce the current profile.

## Measurement and defaults

- Use the entire canvas W × H, including full-bleed backgrounds; S=min(W,H). A title block includes all title lines, bilingual title items, tracking, leading, outlines, and shadows. Measure actual rendered bounds, not only the nominal font size or one glyph.
- Horizontal title: total title-block height / H targets at most 15% and must never exceed 20%. Vertical title: total title-block width / W targets at most 15% and must never exceed 20%. The 15% value is a preferred upper target, never a minimum to fill. The other axis must remain inside the safe zone. Do not test width OR height and choose whichever happens to pass. Mixed writing directions within one title require a separate layout decision.
- Internal Text Scale weight defaults to 0.35; nominal title S_title=0.14 × 0.35 × S=0.049S, with a hard maximum 0.055S. This is this package's local weight, not an undocumented image-generation API parameter. For image models express the same values in natural-language instructions; their pixels still require inspection.
- Subtitle defaults to 0.45 × S_title, maximum 0.50. Body, captions, dates, venue, organizer and other functional copy default to 0.25 × S_title, maximum 0.30. Use light/regular readable strokes and precise alignment; never use large display type for paragraphs. If titles are reduced to fit, recalculate supporting roles from the actual title size. If no title is supplied, use the nominal title size as the reference; do not invent one.
- Default leading: title 1.20, subtitle 1.40, body/functional copy 1.60 times nominal size. Leave at least 0.02S clear space between text blocks, at least 0.04S from protected core-subject bounds, and at least 8% of W/H from the respective canvas edges. Honor larger confirmed safe areas. This is optical text clearance, not printer bleed.
- Reserve at least 30% of the canvas as purposeful low-detail negative space. Empty atmosphere, plain paper and calm full-bleed image regions count; white pixels alone are not the measure. Text-block bounding rectangles together may occupy at most 20% of canvas area. Do not count whitespace inside a large bounding rectangle as permission to enlarge lettering.
- Keep text readable at the intended delivery size. The overlay helper defaults to a 12px nominal floor at native output size; this floor is a starting point, not a print-point or viewing-distance guarantee. Set a higher `min_font_px` when the channel requires it. If complete copy cannot fit above the floor and within caps, revise regions, line breaks, subject placement or canvas; never drop copy, enlarge body type, or silently shrink below the floor.

## Layers and visual priority

Build background and graphic/illustration layers first. The visual subject or thematic graphic carries the composition, may span or support the canvas, and remains the first focus. Text is a separate transparent layer placed according to the selected layout's Text Placement zones (columns, the side opposite an offset subject, footer/corners, or along a diagonal) as a restrained editorial accent. Original calligraphy/artwork may be a subject asset; it is not permission to enlarge event-title copy. Do not add dummy lettering as a graphic workaround.

Use modern minimal, refined, spacious composition across the library. Borrow selected palette, material, form and cultural vocabulary, but suppress conflicting giant-letter, headline-dominant, dense-copy, cropped-title and edge-hugging instructions. The legacy `big-type-only` layout is ineligible under this profile; use a graphic-led eligible layout. Expressive font character can remain at the constrained size.

Overlay: `scripts/render_text_layers.py` measures actual glyph bounds, fits complete copy within supplied regions and the role caps, rejects collisions/unsafe bounds/oversized titles, and saves a transparent text layer plus a versioned composed preview and geometry report. Supply fonts yourself; no automatic system-font fallback. It does not certify aesthetics, contrast or negative-space area. Inspect the completed pixels.

Integrated: append the complete profile to every generation/edit prompt. Measure the completed title block and supporting type; repair failures. Prompt wording alone never proves compliance.

## Review evidence

In `visual_review.typography`, record `profile_id`, `items` (each item's id, role, direction, actual pixel bbox and nominal/equivalent font_size_px), `graphic_primary`, `subject_clearance_verified`, `negative_space_ratio`, `intended_size_readable`, and location-specific `evidence`. Use one of title/subtitle/body for metrics; map every other copy role to body. The renderer supplies geometry but the reviewer must independently inspect graphic priority, negative space, subject clearance, contrast and readability. Integrated approximate size estimates must name their measurement method and uncertainty. Missing evidence is unknown; a breached cap fails H1 and blocks pass. Do not inherit measurements from another version.

Text-free key visuals omit `items` (or use an empty list) and review reserved-area capacity, graphic priority and negative space. Do not demand a nonexistent title. No text is required solely for this profile. Required assets, glyph fidelity and human gates continue to follow the main workflow.

