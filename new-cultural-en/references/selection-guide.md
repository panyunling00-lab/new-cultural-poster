# Cultural classification and visual decision-tree rules

Read at direction planning. The model first understands actual documents/images; scripts execute explicit rules, not cultural recognition from filenames. Explicit user choices prevail. The tree filters candidates, not aesthetics, cultural verification, HG2/HG3, or final confirmation.

## 1. Inputs and unknowns

Run `python scripts/decision_tree.py <brief.json>`.

- `categories`: A–H array, main category first; mixed events merge pools.
- `relation`: `single`, `many`, `process`, `comparison`, `space`, `transformation`, `movement`, `gathering`, `framed`, `symbol`, `reading`, `immersive`, `experimental`.
- `motion`: `static`/`dynamic`; `copy_density`: `low`/`high`; `mood`: `quiet`/`expressive`.
- Optional `specialism`: `calligraphy`, `seal-carving`, `market`.
- Optional `user_layout`: genuine explicitly requested ID; `confirmed_layout`: selected layout.
- `excluded_layouts`: layouts actually found unusable after copy-capacity, asset, or reference checks. Unchecked is neither unusable nor approved.

Missing category/relation/motion/density/mood returns `needs_analysis` with missing fields. Invalid enums are input errors. Do not invent defaults for unknowns.

## 2. Decision order

1. Check user-specified, then confirmed layout: real definition and compliant profile required. It may override automatic category pools with a recorded reason; never change user choice through routing.
2. Union relevant R7 primary/secondary pools, preserving main-category priority. A calligraphy/seal-carving adds diagonal-dynamic; C market adds modular-grid before global exclusions.
3. Rank relationship matches inside the pool; routing never changes eligibility.
4. Dense copy prioritizes checking column/grid/region capacity, movement prioritizes directional/gathering relationships. Ranking does not guarantee fit.
5. Remove confirmed exclusions and ineligible big-type-only, plus global montage exclusions. Empty pool means `conflict`; never silently cross pools or delete copy.
6. Return ranked candidates and three suggestions. Check text zones/visual differences; fewer than three returns `needs_adjustment`, not a false three-direction claim. Fixed layouts can support independently designed spatial/subject/material alternatives.

## 3. Relationship branches

| relation | Preferred relationships/layouts |
|---|---|
| single | `centered-hero`, `off-center-hero` |
| many | `modular-grid` |
| process | `layered-depth`, `frame-within-frame` |
| comparison | `split-horizontal`, `split-vertical` |
| space | `axonometric-spatial`, `large-geometry`, `layered-depth` |
| transformation | `folded-space`, `layered-depth` |
| movement | `diagonal-dynamic`, `radial-composition` |
| gathering | `radial-composition`, `modular-grid` |
| framed | `frame-within-frame` |
| symbol | `minimal-white-space`, `large-geometry` |
| reading | `editorial-column`, `split-vertical` |
| immersive | `full-bleed-image-overlay` |
| experimental | `disorder-layout`, `folded-space` |

Branches describe relationships; globally excluded layouts remain excluded.

## 4. Design judgment after routing

Candidates are structural options. Specify cultural core, theme-to-visual relationship, subject scale, composition evidence, and text regions. Vague claims of refinement/cultural atmosphere are insufficient.

Use canonical filenames, read definitions, and inspect images. A path is not inspection; inspection is not submission. Style governs color, letterform character, materials/light; layout governs placement, scale, space, reading. Choose one main style and one dominant mechanism, not every effect.

Default profile is free design; switch through the brief. Read typography-constraints and small-type system where applicable; JSON files supply numbers. Do not repeat caps here. Quiet institutional events must not silently become high-energy live-event posters. Energetic/experimental treatments require thematic fit or explicit choice. Exhibitions/museums/heritage require at least one open-space, restrained-color direction. General style preference does not remove mapped primary layouts.

### Depth-first candidates

For exhibitions, performances, and spatial events, first assess eligible layered-depth, frame-within-frame, off-center-hero, full-bleed-image-overlay, folded-space, and axonometric-spatial. Explicit user choice prevails. A/B/C must vary depth mechanisms—paper occlusion, openings, folds, projection—not merely color or information placement.

### Theme-led style spectrum

Normally spread A/B/C across a spectrum:

- Quiet/minimal/pale: japanese-ma, swiss-editorial, minimal-graphic, luxury-minimal, botanical-premium, cultural-editorial; minimal-white-space where eligible. Low saturation, high value, ample space; ivory, pale cyan, mist gray, pale ochre, small ink accents or restrained neutrals. Small precise imagery/type stays readable. A tiny object/building/figure may anchor atmosphere only if theme and people policy allow. Do not fill this route with dark blue, bright red/gold, fluorescence, or saturated close-ups.
- Moderate editorial design: editorial-collage, image-led-editorial, cultural-editorial, organic-craft, screenprint; inventive without excessive visual noise.
- Impact/experimental: neo-brutalist, constructivist-impact, pop-commercial, futurist-gradient, y2k, glitch-art, kinetic-typography, distorted-type; bold scale, contrast, distortion, halftones, dimensionality as profile permits.

Media/treatment, composition, and letterform handling must visibly differ; moving elements or changing color alone is insufficient. No universal same-cluster rule. Strong themes may justify three energetic directions; quiet themes three restrained ones. Explicit style requirements prevail. Quiet-route palette restrictions do not govern the other routes.

### East Asian elegance route

Use as a quiet candidate only where theme/context supports it, not a universal paper aesthetic. Combine modern composition with atmospheric space: a minimal object/building/allowed silhouette sets scale, restrained color fields and geometric voids organize, relevant natural imagery/curves connect. People are optional and remain policy-bound.

Use subdued turmeric, ochre, mineral blue-green, ivory, and ink, maintaining lightness and breathing space. Avoid full red/green saturation and filling every area. Subtle paper/silk texture is optional; fibers plus nature imagery alone are not a completed concept. Song/serif/Kai characteristics may combine with vertical/staggered/interleaved type, or one larger title answering open space. Quality comes from proportion, fields, motion, and text–image relationships, not decoration count or filters.

### Observation checklist

For each candidate record relevance, observed mechanism, essential traits, replaceable content, and conflict risks: main/accent colors and value/saturation; weight/proportion/spacing/distortion; photography/illustration/graphics/3D; material/edges/light/shadows/reflection; one dominant print/digital/deformation/spatial mechanism.

Do not replace observations with vague adjectives. Listed effects are options, not cumulative requirements. Reference mechanisms determine branches; materials/media should differ across A/B/C. Resolve definition/image conflicts before selection.

## 5. Availability and conflict checks

Confirm complete copy, asset roles/permission, canvas, and channel. Invent no facts, translations, marks, symbols, or deletions. Reference text/subjects do not become task content.

Inspect relevant originals using assets/style-references/index.md and composition folders. Do not load everything or silently replace the library. Direct submission or observed-feature extraction are valid; record what tools actually receive.

Check copy capacity under the profile, sufficient zones, and at least two visual differences. Resolve fit through layout/grouping/canvas, not indefinite shrinking. Sparse references cannot carry dense copy through microtype. Centering is not radial composition, tilting is not folding, flat mapping is not depth. Pixel/screenprint/liquid mechanisms must be coherent; Japanese inspiration does not authorize Japanese copy.

### Generation gate

Establish objective, theme, audience, all required copy, subject assets, transformation permissions, language, channel, dimensions, ratio, and identity constraints. Theme-based interpretation is allowed, labeled Inferred, but never event facts/data/attribution/prices/slogans. Reference posters' text/logos are not current content.

Assess density from real copy: long/bilingual titles, schedules, and multiple marks increase it. Never delete or shrink required content to imitate a sparse reference.

Before generating confirm real/read definitions, unambiguous mappings, existing accessible decodable images, actual inspection and consistency, subject/copy/ratio fit, and supported reference mode. Directory listings are not inspection. Stop on failed mandatory gates and state the exact blocker. Do not replace actual observation with unsupported improvisation or another library.

### Roles and conflicts

Style references control palette/type character/treatment/material/light/effect; layout references control positions/scale/zones/negative space/depth/reading. Do not copy two independent compositions.

Replace conflicting automatic candidates. For explicit combinations, describe the conflict and obtain necessary tradeoffs before rendering. Sparse references cannot accommodate density via tiny type; monochrome typographic styles cannot acquire dominant color photos; physical print error is not arbitrary digital glitch; pixels need consistent grids and screenprint credible ink layers; liquid must choose 2D/3D; Y2K needs a specific branch rather than all motifs; Japanese inspiration adds no Japanese text; axial order and dominant disorder do not automatically combine.

### Reference modes

Choose one main style and one main composition image, adding support only as needed. Prefer fit, compatible ratio/capacity, and clear features over averaging a whole category. Obey tool limits.

1. **features:** inspect originals, describe observed mechanisms, record inspected rather than submitted. Use when direct image input is unavailable or unnecessary.
2. **direct:** submit supported inputs with order/role. Paths/descriptions are not submission. Do not inherit reference copy, marks, subjects, or unrelated motifs.

An inaccessible Windows path is not renderer input. Use features for unsupported roles, do not assume reference-board support or claim unverified workarounds. Subject assets and reference images have different roles; permission to create a subject does not waive references.

## 6. Records and results

Keep input judgments, sources, script reasons, IDs, reference roles, complete copy, and canvas in ordinary task records, not private reasoning. Inspect actual output for facts, culture, composition, material, text, and extras. Script success is not quality approval. Local refinement never silently redesigns approved work.

### Generation contract

Include the full active typography block in every generation/edit prompt and overlay notes. Record title treatment, reading order, intended display size, and overlap plan. Type may be primary only as the profile allows.

Establish concept, one anchor, two IDs, reference roles, required traits, information zones, reading path, ratio, and full copy. Assemble only confirmed content, selected definitions, observed traits, and necessary adaptations. Allow bounded variation in color nuance/local form/material/scenes, preserving composition, verified cultural meaning, copy, and approvals.

Confirmed substitutions, ratio adaptation, and readability repairs are allowed within the approved language. No silent style/layout change, second dominant mechanism, unsupported decoration, unrelated branding, invented facts, or omission. Claims of polish do not authorize redesign; irreconcilable requirements return to selection.

### Output review

Open the result and compare against inspected references, recorded traits, and actual submissions: facts/copy; subject/regions/scale/space/reading; palette/type/material/light/effect; intended-size readability; extra styles/decoration/branding/inventions. Record pass/fail/unverified and concrete discrepancies for each. Successful prompting/rendering is not satisfaction.

Do not deliver completed work with factual errors, unreadable required text, layout deviation, or missing stylistic mechanisms. Keep original references during targeted repairs. Stop unrelated changes once requirements pass; report persistent tool limitations without promising exact reproduction.

## R6. Event categories

| ID | Category | Typical events | Visual core |
|---|---|---|---|
| A | Static visual art | Calligraphy, painting, photography, sculpture, illustration, design exhibitions | Original work, editorial/curatorial presentation |
| B | Performance and dynamic arts | Concerts, theater, dance, opera, music festivals, live shows | Movement, rhythm, stage tension |
| C | Heritage and traditional crafts | Papercutting, ceramics, weaving, embroidery, carving, lacquer, craft markets | Material, handmade layers, warmth |
| D | Knowledge and academic events | Talks, forums, readings, seminars, workshops, signings | Density, order, text |
| E | Festivals and multicultural events | Folk/cultural/food/film festivals, carnivals | Diversity, gathering, participation |
| F | Contemporary and experimental art | New media, installations, performance art, avant-garde design, digital art | Concepts, unconventional relationships, experimentation |
| G | Museums and collections | Artifacts, archaeology, rare books, collection highlights | Object authority and historical depth |
| H | Space and architectural culture | Architecture, gardens, urban renewal, public art, heritage walks | Spatial relationships and structure |

## R7. Category-to-Layout Mapping

**Machine contract:** build_prompt.py parses these rows. Preserve four visible columns (six pipe-split segments), eight A–H rows, and backticks around every layout ID. Additional columns, missing rows, or unquoted IDs break mapping. Specialist IDs occur in the final column.

| Category | Primary layouts | Secondary layouts | Rationale and specialist additions |
|---|---|---|---|
| A | `editorial-column`, `off-center-hero` | `minimal-white-space`, `frame-within-frame` | Juxtapose original work and curatorial copy. For calligraphy/seal carving add `diagonal-dynamic` for stroke movement; original writing remains an image subject and event copy obeys the profile. |
| B | `diagonal-dynamic`, `radial-composition` | `layered-depth`, `full-bleed-image-overlay` | Express movement/rhythm through stage-like focus. |
| C | `layered-depth`, `frame-within-frame` | `editorial-column`, `minimal-white-space` | Combine layered materials and objects. Markets may add `modular-grid`. |
| D | `editorial-column`, `modular-grid` | `minimal-white-space`, `split-vertical` | Build reading paths and a prominent talk topic. |
| E | `modular-grid`, `radial-composition` | `diagonal-dynamic`, `full-bleed-image-overlay` | Organize multiple activities and collective celebration. |
| F | `disorder-layout`, `large-geometry` | `off-center-hero`, `folded-space` | Support experimental deconstruction and geometric concepts. |
| G | `centered-hero`, `frame-within-frame` | `axonometric-spatial`, `editorial-column` | Present collection highlights centrally or through a display-case frame. |
| H | `axonometric-spatial`, `layered-depth` | `large-geometry`, `folded-space` | Express axonometric structure and spatial layers. |

## People and continuous space

Apply under both profiles to all directions/refinements. Resolve people_policy: B/E/market or people-only references allow people; mixed references favor nonhuman subjects unless nothing else can carry the theme; otherwise no generated people, silhouettes, hands, or miniature figures. Prefer objects/materials/craft/nature/abstraction, not human-shaped substitute exhibits. Required supplied people-bearing assets need an explicit conflict decision, not removal or alteration. If nonhuman assets are insufficient, use verified materials/structure, not invented exhibits.

No visible multi-panel grids/card walls/detail collages or separator lines. Use one continuous space; hidden alignment grids are allowed. Exclude modular-grid/split-horizontal/split-vertical, with one continuous frame-within-frame window. Choose distinct styles/compositions from remaining candidates; explain shortages rather than restoring exclusions. Only later explicit user instructions waive these restrictions.
