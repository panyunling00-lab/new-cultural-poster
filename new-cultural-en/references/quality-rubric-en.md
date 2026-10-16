# Image quality rubric for cultural event posters

Version 1.2 · 2026-10-13

## Tiered review — first complete, later by affected scope

This section overrides wording elsewhere that would require repeated full scoring/review after every change.

- First completed poster: full review, establishing baseline version/hash, facts/copy inventory, typography measurements, and conclusion. A concept preview is not a complete baseline.
- Later revisions: inspect actual changed regions, relevant text/assets, adjacent effects, and global relationships potentially affected. Do not automatically reread all cultural sources, repeat all scoring, or perform an unchanged full review immediately before confirmation.
- Date/typo changes require new copy, wrapping, glyph, alignment, and nearby information checks. Tracking/position changes require bounds/collision/safety/reading checks. Local material/color changes require contrast/material/occlusion checks. Cultural changes require affected/new fact and symbol verification.
- Full regeneration, main composition/subject/canvas changes, uncertain change scope, or missing valid baseline require full review. Compare actual before/after images: models may change more than requested. Do not reuse pixel conclusions where unchanged regions cannot be established.
- Record baseline/current versions and hashes, actual changes, reviewed items, outcomes, and reuse basis. Confirmed unaffected items may carry forward as evidence, but never present an old hash as the new image's review. Cheap dimensions/format/hash checks can run every version.
- After final confirmation deliver unchanged, with no extra edits/review/export approval. Later user changes resume affected-scope review.

## 1. Scope and review inputs

For cultural festivals, public culture events, exhibitions, and other cultural-communication posters. Review cultural accuracy, complete required material presentation, visual quality, readability, and delivery readiness.

| Source | Required input | Review focus |
|---|---|---|
| content-analysis-en.md | Theme, audience, objective, approved copy, cultural references | Accuracy and expression |
| selection-guide.md | Selected style/layout and reasons | Fit to content/use |
| Selected style definition | Palette, line, texture, typography, space | Coherence and recognition |
| Selected layout definition | Focus, reading, zones, crop limits | Hierarchy and capacity |
| User material and actual files | Text/images/marks/attachments/use/dimensions/ratio/format | Complete presentation and specifications |

Use confirmed needs and original assets as the baseline. Style IDs map exactly to `references/style/<ID>.md`: art-deco-luxe, bauhaus-modular, botanical-premium, cinematic-key-art, constructivist-impact, contemporary-art, cultural-editorial, data-editorial, digital-experimental-type, distorted-type, dreamcore-softcore, editorial-collage, emo-visual, futurist-gradient, glassmorphism-ui, glitch-art, hyperreal-product, image-led-editorial, japanese-ma, japanese-modernism, kinetic-typography, liquid-visual, luxury-minimal, minimal-graphic, monochrome-typographic, neo-brutalist, organic-craft, pixel-art, pop-commercial, print-error, retro-futurism, risograph-zine, screenprint, surreal-3d-editorial, swiss-editorial, webcore, xerox-punk, y2k.

Layout IDs map exactly to `references/layout/<ID>.md`: axonometric-spatial, big-type-only, centered-hero, diagonal-dynamic, disorder-layout, editorial-column, folded-space, frame-within-frame, full-bleed-image-overlay, large-geometry, layered-depth, minimal-white-space, modular-grid, off-center-hero, radial-composition, split-horizontal, split-vertical.

Review selected definitions only. Listing an ID does not require or permit its use; category/profile/global exclusions apply. Missing selected files are missing inputs, never rules inferred from names.

## 2. Review stages

- `key_visual`: text-free visual/base. Review aesthetics and capacity for later typography. Do not penalize absence of final dates/venue.
- `final_poster`: composed output. Review actual copy, hierarchy, and file. Background approval is not completed-poster approval.

A text-free base is intermediate. Final posters must clearly present all required supplied content, checked item by item. Stage scores are not directly comparable. Material explicitly supplied as reference-only remains reference-only under the main skill; it is not automatically a required exhibit.

## 3. Principles

1. Review actual images before scoring; without images report missing inputs and no image score.
2. Cite visible region/object/relationship and effect on meaning/reading, not unsupported labels such as refined/not artistic/AI-looking.
3. Respect artistic language: abstraction, roughness, asymmetry, collage, grain, and intentional distortion can be valid. Realism/symmetry/polish/detail do not automatically mean quality; global panel exclusions still apply.
4. Separate intent from defects. Treatment must fit brief/message and function coherently. Accidental fusions, pseudo-text, broken edges, and uncontrolled structures are defects.
5. Anchor culture to the actual subject. Red/gold/clouds/ink/calligraphy/seals are neither automatic culture nor automatic failures; assess relevance.
6. Aesthetics cannot compensate for spelling, dates, culture, or specification errors.
7. Label unverified history/permission/resolution/QR claims; pixels alone cannot establish them.
8. Inventory and visibly include all required user text/images/marks/QR/attachments. Reading an asset or borrowing its style is not presentation. No unauthorized omission, summary, hiding, or removal for simplicity.
9. Respect explicit user style preferences and clearly record conceptual/experimental approvals; the rubric does not override user choices.

## 4. Acceptance checklist

Record must-have versus flexible requirements:

```text
Theme and core message:
Target audience and channel:
Stage: key_visual / final_poster
Required content and elements to preserve:
Complete user-material inventory and IDs:
Full content, presentation method, and final location for each item:
Approved copy and reference material that must remain faithful:
Cultural basis and permitted artistic interpretation:
Selected style and its key visual traits:
Composition, graphic focal point, and reserved text areas:
Typography profile, title orientation, actual complete bounds and role sizes:
Safe margins, block gaps, subject clearance and negative-space estimate:
Aspect ratio, dimensions, format, and crop requirements:
Facts or conditions still awaiting confirmation:
```

Check conflicts such as complex imagery and dense copy sharing a region. Translate vague goals into observable form/material/rhythm/space/proportion/type/color. Do not delete required copy/change facts to ease generation. Concepts may expose missing facts but cannot present them as final truth.

### Material-by-material verification

Assign unique IDs to text paragraphs/information items and individual images/attachments. Extract and verify event facts inside attachments too.

| Material ID | Original/full content | Presentation method | Final location | Verification |
|---|---|---|---|---|
| Actual ID | Original text/image/other content | Complete typesetting/compositing/visible content | Identifiable region | pass/fail/unknown |

Preserve text/meaning; wrapping/hierarchy may change but not unauthorized summaries/fact edits/body omissions. Required images must actually appear recognizably; palette borrowing is insufficient. Crop/mask/scale preserves key information. Faithful portraits/art/marks/QR use originals, not redraws. Convert other material to inspectable content; unreadable/unconvertible/ambiguous files remain pending by ID.

If capacity is exceeded, change layout/production. If one poster still cannot show everything clearly, explain and propose a series/larger format for user decision before implementing. Do not delete or independently switch deliverables. Conflicting facts/cultural risks remain recorded and block final delivery; completeness never justifies known errors. Check every delivered version. Missing/uncertain inventory is unknown; complete coverage passes only at final_poster.

## 5. Hard gates — before scoring

Status: pass/fail/unknown/not_applicable, with evidence and applicability reasons. Applicable fail blocks pass; necessary unknown blocks confirmed delivery. Use quality-script-usage schema.

| ID | Check | Failure/evidence |
|---|---|---|
| H1 | Core requirements and active typography | Wrong theme/subject, missing required content, text/no-text violation, profile failure. Free design: required exact/readable strings, no numeric design caps. Small-type: enforce active JSON numeric limits. |
| H2 | Copy and facts | Missing/incorrect names, dates, venue, organizations, tickets, facts; garbled/repeated/misspelled/unreadable key copy |
| H3 | Cultural accuracy | Objects/dress/scripts/period/ritual/attribution conflict with sources, or invented details presented as fact |
| H4 | Subject and structure | Severe accidental fusion/deformation affecting recognition/meaning at intended size |
| H5 | Use requirements | Wrong ratio/dimensions/format, lost key crop content, insufficient copy capacity, required QR undecodable/wrong destination |
| H6 | Designated assets | Material alteration of fidelity-required portraits/art/marks, unrelated watermark/signature/logo, missing required permission |
| H7 | Complete user-material presentation | Missing item, unauthorized shortening, reference influence without required display, unreadable tiny/occluded/cropped content; map every required ID to location |
| H8 | Memorable visual core | No identifiable primary core; an undesigned ordinary title alone supports the image; strong resemblance to same-theme template. Identify object/location and independent thematic graphic/letterform mechanism, or concrete repetitive comparison. |

H8 is reviewer judgment, not an automatic visual calculation. Designed type may legitimately be the core; neither exempt nor fail it solely for text dominance. Use not_applicable only with justified absence of relevant visual requirements. Missing H8 evidence is unknown and blocks compliance. The bundled script checks submitted H1–H8 records but cannot establish their visual truth.

At key_visual, H7 is not_applicable pending final review, but inventory/plan still exist. H2 checks accidental lettering/facts actually present, not absent final copy. Uncertain culture without reliable evidence makes H3 unknown, not intuition-based fail/pass. Approved fictional period mixtures/symbolic changes follow the agreed premise, not documentary standards. Permission requires records; appearance proves neither infringement nor authorization. Minor defects belong in scores/fix notes rather than every texture becoming a hard failure.

### Global content rules — both profiles

| ID | Check | Decision |
|---|---|---|
| GC1 | People as subject | Unexpected primary human focus fails under default forbidden policy. B/E/market/people-only references or explicit request may allow with reason. Under avoid, unjustified primary people require revision. |
| GC2 | One continuous space | Visible divided grids/triptychs/independent image frames fail. Hidden alignment grids remain allowed. |

These feed H1/H4 and apply before scoring. Only later explicit user instructions waive them, with scope recorded.

## 6. Weighted scoring — 100 points

These are project starting values, not universal industry standards; calibrate with real samples. Scores are integers 0–5: 0 absent/failed; 1 major deviation; 2 partial with clear problems; 3 usable/basic success with improvement needed; 4 complete/convincing with minor issues; 5 precise, mutually reinforcing form/content and strong execution.

Total = sum(score/5 × stage weight), one decimal. Missing evidence means not assessed, not zero. No complete total with missing weighted dimensions.

| Dimension | Key visual | Final | Assessment/high anchor |
|---|---:|---:|---|
| A Theme and cultural expression | 25 | 20 | Specific cultural/artistic relationship; form/process/action/concept clearly translated with understandable basis/interpretation |
| B Concept and distinction | 20 | 15 | Primary core recognizable in ~3 seconds, including designed type; independently expresses theme, avoids generic templates/aimless accumulation, distinct viewpoint |
| C Composition and hierarchy | 20 | 20 | Priority, flow, density, proportion, zones; deliberate space and clear target-size reading |
| D Style and visual language | 15 | 10 | Coherent palette/line/texture/light/space/type or clearly reasoned mixture |
| E Image execution | 10 | 10 | Structures/edges/seams/material support intent, no accidental key collapse |
| F Typography capacity/quality | 10 | 20 | Base supports actual copy; final glyphs/spacing/alignment/wrap/contrast accurate and readable with natural language hierarchy |
| G Channel/delivery fit | 0 | 5 | Stable recognition at actual display/crop/derivative sizes, all key content preserved |
| Total | 100 | 100 | |

Technical specs still apply through H5 at key_visual. Final work checks all required material/specs; invent no missing dates/venues/QR/details.

### Mandatory anchors and decisions

Use measured/visible evidence, not impression alone. Apply the lowest relevant score cap before weighting:

- B max 3/5 if the sole core is ordinary undesigned title text or a strongly generic template; cite specific evidence/comparison.
- D max 3/5 for more than three main color roles or equally dominant large saturated clashes.
- H8 fail blocks pass even with ≥85 and all dimensions ≥3.
- Active H1 failure blocks pass: inaccurate/unreadable required strings under free design; any profile cap violation under small-type. Missing required measurements/priority evidence is unknown. Aesthetics cannot compensate.
- C max 3/5 for near-duplicate candidates (same subject/main palette/decoration, only copy differs).
- C max 3/5 if A/B/C share the same background/primary color family, subject to explicit user constraints resolved in the main workflow.

Read typography-constraints, small-type system only where active, and numeric profile files via defaults. Record current profile_id; mismatched evidence is unknown. Small-type requires complete title bounds/role sizes/margins/gaps/subject clearance/graphic priority/negative space/intended-size readability. Measure the title on its correct axis with all effects/lines. Estimate intentional open space with supporting regions, not white-pixel count. State uncertainty/method; missing required evidence marks affected dimensions not assessed.

Apply outcomes in order:

1. Not assessed: no actual image or insufficient visual inputs; report missing data/prechecks.
2. Needs verification: necessary unknown hard gate; provisional visual scores may include known defects but cannot pass.
3. Rework direction: complete score <70; return to content/concept/style/layout.
4. Revise: any hard fail, score 70–84.9, or weighted dimension <3.
5. Pass: applicable gates pass, score ≥85, every weighted dimension ≥3; only for that stage/file/version.

Missing facts do not prevent recommending known visual repairs. A 95 visual score cannot override H2 fail.

## 7. Cultural poster review

### 7.1 Culture and theme

Complete: This visual relationship belongs to the theme because… If the answer is only beautiful/traditional/artistic, check whether the connection is generic. Abstract rhythm/movement/material/space/concepts can be sufficient without figurative symbols. Tradition may be contemporary, and contemporary art need not use abstract geometry.

Where accuracy is required, compare artifacts/dress/buildings to references. Actual artworks require form/color/crop checks; reinterpretation follows approved adaptation scope.

#### 7.1.1 Cultural verification inventory

Establish a specific subject before generation; broad Chinese/Eastern/ethnic labels are insufficient. Record each major element's name, region/community, era, use context, source, permitted interpretation, and status. After generation inspect all actual elements, including model-added symbols.

| Area | Check |
|---|---|
| Region/group/community | Do not exchange names/dress/patterns/languages/customs without evidence or universalize local traits |
| History/material culture | Verify era/object form/dress/architecture/instrument/process for accuracy claims; artful mixtures are not reconstruction |
| Religion/sacred/ritual | Verify meanings/context and documented project-relevant placement/orientation/role/access restrictions; invent no universal taboo |
| Writing/symbols | Verify historical scripts/calligraphy/seals/community languages/religious text, order/direction; no plausible fake writing as authentic culture |
| Identity/depiction | Avoid reductive exaggerated appearance/dress/poverty/primitivism/mystification; appearance does not establish identity |
| Sensitive history/memory | Verify war/disaster/colonialism/persecution/funerary/memorial context; flag mocking/sensational/celebratory treatments conflicting with purpose |
| Provenance/practitioners/attribution | Invent no author/practitioner/source/recognition/endorsement; heritage/authenticity/reconstruction needs evidence |
| Interpretation boundaries | Distinguish sourced details and design; approved mixtures must not imply false attribution/facts |

#### 7.1.2 Sources

Prefer relevant museum/archive records, research, cultural institutions, and related communities/practitioners/custodians. Each supports specific facts/context, not an entire community. Record title/link/file, supported detail, and online access date. Generated images/search thumbnails/unattributed stock/model memory do not establish truth. Cross-check contested/conflicting/core details and record disagreement. Era verification does not establish permission or community acceptance. Insufficient evidence is unknown; unavailable research means disclose missing sources, never fabricate or claim completed checks.

#### 7.1.3 Risk decisions and response

H3 fails for sourced contradictions in core attribution/facts, fake scripture/script as authentic, invented official/community endorsement, degrading group depiction, or violated applicable confirmed use restrictions. Other scores cannot compensate. Unresolved evidence/context is unknown, not presumed safe.

Identify object/location/risk/evidence, not vague possible offense. Route factual issues to source verification/correction and local symbol misuse to editing. If core concept depends on unverified ritual/restricted elements, suspend final delivery and seek the specific project-owner/subject/community decision. Prefer verified thematic objects/material/process/space/rhythm alternatives and verify those too. After repair inspect combined meaning, copy, and derivatives; crops/local edits may change meaning. Report checked scope/sources/uncertainty; model review cannot guarantee no risk. Necessary H3 items must resolve before final delivery.

#### 7.1.4 Meaning and use context

Check recognizable elements from user material/references/generated symbols/text/dress/objects/people. Attractiveness/cultural appearance does not establish fit. Explain meaning/community with evidence; check religious/ritual/funerary/memorial context and event/placement/role/caption conflicts; verify attribution, misleading combinations/crops/distortion/color/text, and clear fact-versus-adaptation boundaries. Never present adaptation as authentic tradition/reconstruction/recognition.

H3 pass requires supported meaning/use fit; fail requires evidenced misuse/false attribution/degradation/restriction breach; unknown means unconfirmed; not_applicable requires justified absence of specialist issues. No visible problem is not verification. Record element/location/original meaning/current use/source/status/recommendation and recheck after resolution.

#### 7.1.5 Uncertain elements

Autonomously verify model-added/system-selected decoration rather than making the user decide every uncertainty. Research directly relevant reliable sources first. Keep only supported use; thumbnails/stock/motif collections are insufficient. Replace unresolved/conflicting elements with verified thematic objects/materials/process/architecture/nature, or supported abstract rhythm/space/material when no figurative option fits. Verify replacements and combined meaning; record original/reason/replacement/evidence. If none works, retain unknown and needed evidence, never pretend research happened.

User material cannot be silently replaced/deleted. Preserve originals, identify issues, and present a verified alternative for confirmation before changes/inventory updates. Core theme/facts/explicit requirements also need confirmation for substantive replacement. Suspend final delivery while unresolved.

### 7.2 Style and composition

Extract observed traits, not names alone. Swiss editorial: grid/alignment/hierarchy. Neo-brutalist: controlled contrast/roughness/tension and reading. Luxury minimal: proportion/space/material that serve theme, not automatic quality through emptiness. These are criteria, not templates.

Free design permits theme-led scale/material/style/overlap and designed type as core without default restraint. Small-type imposes its JSON caps. Assess focus/text–image/crop under the selected layout. Dense real copy requires layout/production adjustment, not unreadable shrinking to imitate a template.

### 7.3 Text and information

Compare every required string, especially names/organizations/dates/numbers/punctuation/simplified-traditional forms. Check bilingual factual alignment, hierarchy, reading. OCR finds candidates but does not prove comfortable reading; calligraphy/vertical/small text needs visual review. Artistic titles may be stylized while required information stays readable. Persistent generation failures favor preserving base and reliable typesetting/composite, with supplied-font requirements respected. No unauthorized title shortening/fact deletion. Use real supplied/generated functional QR assets and verify decoding/destination; model-drawn imitations are unusable.

### 7.4 Multiple scales

Overview: focus/theme/hierarchy/balance. Target display: contextual reading; ~320px short-side thumbnails can simulate a feed, not a universal standard. Full resolution 100%: text/faces/hands/joints/seams/edges, judged by the chosen language. File properties: actual pixels/format/required color data; 8K/HD/300dpi labels are not proof. Print requires effective resolution/bleed against physical size/printer specs. Record unavailable tools/files/display checks instead of claiming completion.

## 8. Candidate comparison and revisions

Inspect/score candidates individually before comparison, not only the first. If none passes, do not approve the least bad. Same-stage differences ≤3 points are close; compare expression/hierarchy/type capacity/repair cost rather than objective aesthetic ranking.

| Issue | Return to | Action |
|---|---|---|
| Wrong culture/missing facts | Content verification | Verify source/fact and redefine visuals |
| Generic concept/style mismatch | Direction | Revise concept/concrete traits, not more keywords |
| Subject/title clash or no copy area | Layout | Rebalance using actual copy |
| Local structure/material/edge | Image editing | Specify location/object and preservation |
| Missing/unreadable user material | Asset/layout/compositing | Restore by ID, adjust, recheck inventory |
| Spelling/wrap/bilingual type | Typesetting/layout | Restore exact copy and relationships |
| Crop/size/format | Output production | Correct layout/crop/output within exact-ratio rules, no simple stretch |

Record all defects, prioritize the top 1–3, hard failures first. Instructions state location/object → visible problem → effect → change → preservation → recheck. Example: a performer's hand fuses with a fan handle at lower right, obscuring the gesture; repair only that joint using supplied reference, preserving fan shape/face/costume/palette/title, then inspect native-size detail and unchanged overview. People policy still applies to the actual task.

After revisions recheck target and regressions in facts/text/subject/ratio, retaining prior best. Main workflow permits at most two quality-correction rounds, without resetting through versions. If unresolved, report status/defects and obtain a decision; never lower standards. Production-method/direction changes follow their normal gates.

## 9. Standard review output

```text
Version/file:
Review stage: key_visual / final_poster
Decision: pass / revise / rework direction / needs verification / not assessed
Total: __/100; label provisional visual score or not assessed when applicable

Hard gates:
H1–H8: each status/evidence; applicability reason or needed source
Typography: profile ID, current bounds/sizes, title-axis ratio, text area,
negative space, priority/readability evidence as required by the active profile

Material coverage: every required ID, location, status; missing/unverified items
Dimension scores: A–G, score/weight/specific evidence; omit zero-weight dimensions
Keep: concrete visual relationships worth preserving
Priority fixes: at most 3, by impact
Revision instruction: object/location/action/preservation/recheck
Limitations: unverified facts/properties/display conditions
Next step: deliver current stage / return to relevant step / obtain information
```

## 10. Examples and calibration

- Attractive output missing one of three required supplied images: H7 fail even at 95; restore/check.
- Attractive final poster with wrong date: H2 fail, revise even at 91.
- Requested text-free background with usable zones/no accidental text: do not fail for absent dates; key_visual only.
- Grain consistent with print language and recognition is intentional, not noise; fused hands are separate defects.
- Uncertain artifact era without evidence: H3 unknown, identify object/source needed, needs verification.

Calibrate on real cultural subjects/styles/Chinese-bilingual/channel samples with independent designer review. Address false passes/rejections/disagreements before changing weights/thresholds. Use the same rubric version within a batch. Isolated problems become case notes; generalize only when repeated across themes. AI scores support decisions, not objective artistic worth.
