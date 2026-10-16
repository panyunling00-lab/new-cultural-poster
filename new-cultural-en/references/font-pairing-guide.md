# Font pairing guide

Read at HG2 and before prompt assembly in steps 4–5. Choose according to cultural theme, purpose, approved concept, copy length, and readability. Theme lists are starting points, not fixed assignments. Family names identify inspiration, not fonts the image model must load.

## Eight pairings are inspiration, not eligibility rules

Distortion, stretching, halftones, dimensionality, and mixing are available within the active profile. Free design permits expressive handling; small-type keeps it within caps. Default `design-free-v1`; switch with `brief.typography_profile`. Scale, role ratios, weights, leading, tracking, family budgets, negative space, and clearance come from the active profile. Read typography-constraints, the small-type system where applicable, and typography-moves. Exact copy and normal-size readability are fundamental.

## Pairing rules

- Coordinate scripts: Chinese establishes character, Latin follows. Pair bookish print with serif Latin and heavy impact with extra-bold Latin, rather than unrelated treatments. Include only scripts present in supplied copy.
- Pairings are optional; number and treatment serve theme/readability and active profile.
- Integrated prompts use visual features only, omitting family names, filenames, and paths. They work without a font library; generated glyphs still need inspection.

## 1. Neutral Modern

- Inspiration: Satoshi + MiSans.
- Prompt-ready visual description: Chinese: geometric sans-serif forms, even face proportions, light-to-medium strokes; Latin: geometric sans-serif, balanced widths and matching stroke weight; restrained, comfortably open tracking.
- Character: calm, neutral.
- Themes: exhibitions, galleries, technology culture.
- Use: matched weights and quiet spacing; smaller information remains readable.

## 2. Rounded Geometric

- Inspiration: ITC Avant Garde Gothic + Alibaba PuHuiTi 2.0.
- Prompt-ready visual description: Chinese: friendly geometric sans-serif, softened terminals, medium-to-bold weight; Latin: circular geometric forms, rounded appearance, matching medium-to-bold strokes.
- Character: youthful, friendly.
- Themes: family activities, creative markets.
- Use: coordinate rounded rhythm and optical weight; avoid childish decoration unless supported.

## 3. Heavy Impact

- Inspiration: Helvetica Neue + Plix.
- Prompt-ready visual description: Chinese: extremely heavy, compact black strokes and compressed proportions; Latin: extra-bold condensed capitals, dense downward visual weight; strong contrast between headline and information.
- Character: forceful, solid.
- Themes: music festivals, contemporary culture, talks.
- Use: impact in the title, calmer information; do not make functional copy tiny.

## 4. Elegant Serif

- Inspiration: PingFang + MingLiU.
- Prompt-ready visual description: Chinese: slender Song/Ming forms, thin horizontals and stronger verticals; Latin: refined serif forms, elongated proportions, open tracking.
- Character: elegant, formal.
- Themes: openings, awards, fine arts.
- Use: inspiration labels are not literal classification—PingFang is not a serif. Integrated follows the described serif appearance. Overlay uses matching user-supplied fonts; the source suggests MiSans with a serif substitute where supplied.

## 5. Contrast Serif

- Inspiration: Classy Vogue + Source Han Serif CN.
- Prompt-ready visual description: Chinese: high-contrast Song strokes and sharp serifs; Latin: high-contrast editorial serifs, fine hairlines and strong verticals; refined magazine-like spacing.
- Character: fashion/editorial.
- Themes: design exhibitions, fashion culture.
- Use: coordinate stroke contrast across scripts; hairlines must survive at delivery size.

## 6. Warm Handwritten

- Inspiration: FontQu Smile.
- Prompt-ready visual description: Chinese: warm handwritten strokes, rounded connected movement, slightly irregular rhythm; Latin, if supplied: matching soft handwritten forms with the same casual rhythm.
- Character: approachable, comforting.
- Themes: craft markets, reading groups, coffee culture.
- Use: handwriting follows the theme; information remains readable. Add no unrequested Latin copy.

## 7. Bookish Print

- Inspiration: HWMCT.
- Prompt-ready visual description: Chinese: printed Ming/Song forms, moderate stroke contrast, balanced bookish rhythm; Latin, if supplied: restrained book serifs with comparable weight and spacing.
- Character: traditional, literary.
- Themes: rare books, calligraphy, heritage.
- Use: pair bookish Chinese with serif Latin; do not automatically add aged paper or historical patterns.

## 8. Ornate Serif

- Inspiration: Kudry + Source Han Serif CN.
- Prompt-ready visual description: Chinese: expressive high-contrast Song display forms; Latin: ornate serif display forms, exaggerated curves, tightly controlled spacing; dramatic emphasis.
- Character: ornate, theatrical.
- Themes: galas, anniversaries, brand evenings.
- Use: ornament belongs in titles; functional information stays simple/readable.

## Selecting and expressing typography

No font files are bundled. Select and apply through language:

1. Choose by description, matching the approved palette, materials, cultural register, copy tone, and channel. Labels describe an appearance achievable by multiple real fonts, not files to load.
2. Use the pairing's visual description in the typography prompt: stroke contrast, weight, face proportion, tracking, serif/handwriting character. Never include family names or paths.
3. Match scripts to the language version. Chinese versions use Chinese descriptions; English-only versions use Latin descriptions. Do not leave Latin placeholder forms in Chinese posters or impose Chinese letterform instructions on English-only posters.
4. Record choice and reason, so revisions adjust descriptions without restarting selection.

Overlay exists only when the user explicitly supplies task fonts. Register matching files in `supplied_fonts`, verify coverage, and record substitutions from inspiration labels to actual files. No system fallback, download, installation, or silent bundling. Without supplied files use integrated or composite and review pixels.

## Direction assembly — style, layout, and pairing

| Tonal cluster | Style IDs | Layout IDs | Pairings | Decoration, restrained by default |
|---|---|---|---|---|
| Traditional literary | `japanese-ma`, `cultural-editorial`, `botanical-premium`, `art-deco-luxe` | `editorial-column`, `frame-within-frame`, `minimal-white-space` | Elegant Serif, Bookish Print, Ornate Serif | Hairline frame, small seals, vertical date tags, corner marks |
| Modern restrained | `swiss-editorial`, `minimal-graphic`, `bauhaus-modular`, `monochrome-typographic` | `off-center-hero`, `modular-grid`, `split-vertical`, `large-geometry` | Neutral Modern, Contrast Serif | Geometry lines, corner marks, information icons, dividers |
| Expressive impact | `neo-brutalist`, `constructivist-impact`, `pop-commercial`, `futurist-gradient` | `diagonal-dynamic`, `radial-composition`, `large-geometry` | Heavy Impact, Rounded Geometric | Diagonal cuts, small supplied numerals, stamp-like tags |
| Handmade warmth | `organic-craft`, `screenprint`, `risograph-zine` | `layered-depth`, `frame-within-frame`, `folded-space` | Warm Handwritten, Bookish Print | Hand strokes, postmarks, handwritten notes, paper texture |

Clusters guide inspiration, not admission. Cross-cluster treatments or no pairing are possible where the theme supports them. Choose style/layout/optional letterforms by theme; category mapping sets layout priority; three directions should avoid equivalent structures. Reasoned cross-cluster experiments preserve copy/facts. Resolve conflicts through selection-guide. Listed legacy layout suggestions remain subject to the main global exclusions. Identity-asset terms belong in compositing records, not generation prompts.
