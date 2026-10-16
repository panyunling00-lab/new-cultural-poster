---
name: new-cultural-en
description: Create posters for cultural exhibitions, performances, heritage crafts, workshops, and festivals from supplied content and verified cultural context, with three visual directions, human selection, iterative refinement, tiered quality review, and final confirmation. Excludes ordinary product advertising.
---

# Cultural Event Poster Generator

Create cultural exhibition, performance, heritage craft, workshop, and festival posters without treating a test case, canvas, or single aesthetic as the default.

## File resolution and reference reading

Resolve every path relative to this SKILL.md, not the task working directory. Preserve plural `assets/`, lowercase `references/style/` and `references/layout/`, and the capitalization of `base-prompt-EN.md`. IDs are filename stems. Read each selected definition in full; do not infer contents from its name or load the entire library indiscriminately. For example, `organic-craft` requires `references/style/organic-craft.md`.

| When to read | Path | Purpose |
|---|---|---|
| Before step 1 | `references/content-analysis-en.md` | Facts, complete copy, asset roles, hierarchy, preflight contract, creative interpretation brief |
| Start of step 4 | `references/event-layout-map.md` | Route content to visual relationships and binding category pools |
| Start of step 4 | `references/selection-guide.md` | Candidate pools, decision tree, style spectrum, reference modes; R7 is machine-parsed |
| Before any direction or generation | `references/typography-constraints.md` | Profile entry point, switching table, free-design rules |
| Only under `small-type-refined-v1` | `references/typography-system.md` | Numeric rules, pairings, text–image relationships |
| When choosing letterform techniques | `references/typography-moves.md` | Optional profile-neutral menu; active caps prevail |
| During step 4 selection | `references/style/<style_id>.md` | Typography, palette, materials, imagery, limits |
| During step 4 selection | `references/layout/<layout_id>.md` | Composition, reading order, placement, ratio adaptation |
| During step 4 selection | `assets/style-references/previews/<style_id>-contact-sheet.jpg` | Visual style evidence |
| During steps 4–5 | `assets/composition-references/<group>/<layout_id>/` | Composition evidence |
| Before steps 3 and 6 | `references/quality-rubric-en.md` | Cultural verification, hard gates, visual review, scoring |
| Step 2 and before prompts in steps 4–5 | `references/font-pairing-guide.md` | Eight descriptive pairings, no fonts needed |
| Before prompts in steps 4–5 | `references/base-prompt-EN.md` | Assembly; TEMPLATE blocks are script inputs |
| Before assembly in steps 4–5 | `assets/negative-prompt.txt` | Paired Chinese/English prohibitions; inject one language once |
| Before overlay typesetting | `references/text-layer-rendering.md` | Render contract and asset compositing |
| Before composite production | `references/composite-text-layer.md` | Model-rendered text and screen/multiply blending |
| Step 5, after HG3 | `references/design-refinement-en.md` | Targeted refinement preserving the direction |
| Before first quality-script use | `references/quality-script-usage.md` | Request/report contract and exit codes |
| Before first gate operation | `references/human-gate-usage.md` | Gate-state actions |
| When maintaining the skill | `references/test-learnings.md` | Traceable evidence, never automatic prompt rules |
| When resolving profiles | `assets/typography-defaults.json` | Default/profile-file pointer |
| When reading style references | `assets/style-references/` | 38 style folders, contact sheets, `index.md`, `index.csv` |
| When reading composition references | `assets/composition-references/` | Seven principle groups, one folder per layout ID |
| When assembling briefs | `templates/prompt-brief-example.json` | Illustrative input, references and profile fields |
| Before generation | `scripts/preflight.py` | Source, canvas, and copy validation |
| Direction planning | `scripts/decision_tree.py` | Deterministic layout routing |
| Before steps 4–5 | `scripts/build_prompt.py` | Prompt assembly, R7/TEMPLATE parsing |
| When a profile applies | `scripts/typography_policy.py` | Resolve values and prompt constraints |
| Overlay path | `scripts/render_text_layers.py` | Measured typesetting with supplied fonts |
| Composite path | `scripts/composite_text_layer.py` | Blend model-rendered text onto a base |
| With original assets | `scripts/overlay_assets.py` | Composite supplied logo/QR PNGs |
| Steps 6–7 | `scripts/check_poster.py` | Decode pixels and evaluate quality evidence |
| Gate operations | `scripts/human_gate.py` | Sequential state helper |
| Skill validation only | `scripts/test_typography.py`, `scripts/test_design_free.py` | Typography, rendering, exact-copy and gate regressions |

There are 38 style and 17 layout definitions. Valid IDs include `neo-brutalist` and `full-bleed-image-overlay`, not `neo-brutalism` or `full-bleed`. `cultural.txt` is a flat inventory, not workflow instructions. Regression scripts are never called during normal poster production.

**Visual references are part of the definitions.** The source estimates approximately 220 style images; the supplied archive contains 177 individual images, 38 contact sheets, and an overview. Composition references contain 79 images in division, imagery, motion, space, structure, subject, and typography groups. Inspect selected images before proposing directions and let them constrain palette, materials, texture, and composition. They are references, not exhibits to insert. Reference typography never waives the active profile.

## Pluggable typography profiles

`design-free-v1` is the default, defined in `assets/typography-design-free.json`. `small-type-refined-v1` is defined in `assets/typography-small-type.json`. `assets/typography-defaults.json` contains `default_profile` and `profiles` mappings. Select with `brief.typography_profile`; omission uses the default.

Switching profiles changes configuration, not the 55 style/layout definitions, whose headers point to `references/typography-constraints.md`. The typography system applies only to small-type; optional moves remain subject to active caps.

| Rule | `design-free-v1` | `small-type-refined-v1` |
|---|---|---|
| Title cap | None | ≤0.055S; title block target 15%, hard max 20% |
| Total text-block area | No cap | ≤20% of canvas |
| Negative space | No minimum | ≥30% |
| Edge margin | 0; not required | ≥8% W/H |
| Clearance | 0; not required | Text gap ≥2%; core-subject clearance ≥4% of short side |
| Geometry | Descriptive only | Enforced pass/fail |
| `big-type-only` | Explicit `user_layout_override` only; in no category pool | Ineligible, retained as legacy ID |

Free design requires exact required strings, normal-size readability, no pseudo-text, and no invented facts. The AI chooses size, letterforms, distortion, overlap, staggering, leading, tracking, and regions according to theme, medium, viewing size, and content. There is no default small type or restraint. Small-type enforces every numeric cap. Inspect actual pixels in both profiles; wording alone proves nothing.

## Global composition rules — both profiles

Apply to every A/B/C direction and refinement. Only a later explicit user instruction can waive a rule; record its scope.

- Resolve people policy with `build_prompt.py::people_policy`. Performance (B), festival/carnival (E), market themes, or people-only references (`reference_people: "only-people"`) allow people. Mixed references (`reference_people: "people-plus-content"`) favor other subjects; use people only if nothing else carries the theme. Otherwise generate no real/illustrated people, silhouettes, hand close-ups, or miniature human scenes. Prefer objects, materials, craft structures, natural forms, and abstract relationships. If required original assets contain people, explain the conflict and obtain a decision rather than altering/removing them. Explicit later instructions may tighten or loosen this rule.
- No visibly divided multi-image layouts: nine-cell grids, card walls, stacked detail panels, or collages separated by lines. Use continuous space, large forms, scale, negative space, and depth. Hidden alignment grids are allowed.
- Exclude `modular-grid`, `split-horizontal`, and `split-vertical`. `frame-within-frame` permits one continuous window. If too few candidates remain, explain and adjust category fit; never silently restore exclusions.
- Use category mapping R7 under both profiles: relevant primary/secondary layouts plus specialist additions. Do not append universal layouts. `big-type-only` is override-only in free design and forbidden in small-type. All 38 styles remain available.

## Core requirements and records

Use the eight visual pairings in `references/font-pairing-guide.md`. No fonts are bundled: the mechanism is language. Match shape, stroke contrast, weight, proportion, and spacing to style, palette, materials, and cultural register. Put no font-family names, filenames, or paths in image prompts.

Integrated text is default. Composite supports copy revisions or language versions sharing an approved base without fonts. Overlay is available only with user-supplied task fonts, registered in `supplied_fonts` and checked for glyph coverage. No system-font fallback; do not install, download, or silently bundle fonts.

- Preserve required display items and facts. Invent no event details, cultural attribution, translations, endorsements, or heritage status. Do not delete content for visual simplicity. Explicitly authorized sentence condensation must retain required names, titles, official designations, dates, venues, hours, and admission terms; record each change and verify meaning.
- Official designations are exact strings in the required language, with supplied counterparts as required. Never paraphrase, independently translate, or shorten them. Check character by character before quality pass.
- Supplied photography may be the base. Prefer image-to-image with one to three supplied photos or direct compositing to preserve real crafts. If a crop already supports the design, use the original directly and record it.
- Faithfully rasterize supplied SVG marks at delivery resolution; verify nonempty transparent results and composite unchanged. Composite original raster marks similarly. Never redraw or approximate logos with a model.
- Distinguish required display material from style references; resolve ambiguous roles at HG1.
- Keep briefs, numbered inventories, versions, evidence, and decisions in conversation by default. Do not require separate analysis/inventory/gate documents. Use reference schemas as organization guides; save records only when requested or needed for recovery, not as extra skill modules.
- Current explicit user instructions prevail. Generic requests to proceed do not cancel agreed human gates; record specific waivers.
- Review completed images. Good prompts, text-free backgrounds, or model scores do not establish final readiness.

## Human gates and task state

Read `references/human-gate-usage.md`. Actions: `init`, `status`, `brief`, `directions`, `select`, `poster`, `review`, `confirm_final`, `feedback`, `check`, `exported`; `approve` is a legacy alias.

Three human gates plus final confirmation: HG1 copy, HG2 typography, HG3 three-way composition/draft selection, then `confirm_final`. No separate export gate exists. A recorded review pass permits final confirmation; confirmation authorizes export.

Save `hg-state.json` in task output, the only required recovery record. Use independent state per language so approvals never transfer. Run `check` before direction registration, poster completion, and export; stop on failure. The helper checks state and versions, not conversation authenticity or visual quality.

At each gate, show decision material/actual images with the current version, ask one clear question in the user's language, and end the turn. Tool results, silence, elapsed time, preselection, model recommendations, and earlier approvals are not replies. Interpret yes/no for the current question and A/B/C for the current registered set. Clear natural language is valid; ambiguity leaves the gate pending. Record genuine replies verbatim only after arrival. HG1/HG2 generate zero images; HG3 presents exactly three drafts.

## Workflow

### 1. Analyze materials and HG1 — confirm copy, zero images

Read content-analysis. Extract theme, title, full copy, time, venue, organizers, participation, use, language, ratio, dimensions, and assets. Mark explicit, inferred, missing, or conflicting. Preserve supplied content; never guess unreadable attachment text.

Produce the separately labeled Creative Interpretation Brief in analysis §11: nine Inferred slots plus composition method, spatial layers, material texture, and accent proposals. Apply people policy and separate interpretation from facts.

Record preflight fields: `source_audit` with each document's `path`, `pages`, `read_pages` and unresolved list; `canvas_spec`; `source_copy`; `copy_items`. Validate before prompt building or `brief`/`check`/`directions`. Missing copy/pages, unknown canvas, or ratio conflicts block generation.

Initialize with `init`. Show complete extracted copy and missing/conflicting/unverified items; ask confirmation/correction and end the turn. Only after a real reply update the brief, validate, and run `brief`, honestly setting `theme_status` to `clear`, `missing`, `unclear`, or `conflict`. Never invent facts to pass HG1.

### 2. HG2 — typography choice, zero images

After genuine HG1 confirmation, read pairing/moves guides. Offer 2–4 written typography directions covering weight, letterform, spacing, technique, and fit under the profile. Ask a choice/preference and end the turn. No images or silent choice. Record chosen typography and verbatim reply in the brief; no new script action.

### 3. Verify cultural meaning and use

Read the rubric's cultural sections. Verify significant elements' meaning, attribution, region, era, religious/ritual context, and proposed use with actual sources. Examine combinations, crops, and distortions. Replace unverified new decoration with supported theme-related expression and verify replacements. Changes to user assets/core themes require confirmation. Necessary unresolved questions suspend affected directions.

### 4. Plan three compositions, generate three drafts, and HG3

Proceed only after HG2 and step 3, preserving selected typography.

1. Answer event-layout-map §2's four questions; obtain binding category pools in §§6–7. Routing narrows only; selection-guide R7 is the machine source, the map a reading copy.
2. Read selection-guide fully; run decision_tree on the analyzed brief. Resolve `needs_analysis`, `conflict`, and `needs_adjustment`.
3. List actual style/layout files; choose genuine filename-stem IDs.
4. Read every selected definition fully.
5. Inspect its contact sheet and composition images. Images govern palette/material/graphic language where definitions disagree; the profile governs typography.
6. Record `references` (`path`, `role`, `definition_id`, `inspected`, `borrowed_features`), `fit_evidence`, `reference_mode` (`direct`/`features`), `typography_profile`, title region, role sizes, safe areas, and layer separation.

A/B/C require three distinct styles and three distinct eligible layouts after exclusions, differing on at least two visual dimensions. Their title/information zones must be spatially different and drawn from each layout's Text Placement. Color alone is insufficient. Ratio affects implementation, not category eligibility. If the user fixes style/layout, distinguish independent directions through other spatial/visual relationships.

Read moves where applicable, pairings, and base-prompt. Assemble each prompt with `build_prompt.py`, injected profile block, and one language's negative rules. Preserve confirmed `canvas` verbatim, e.g. `landscape 16:9`; no implicit default. Attach inspected references when supported; otherwise describe borrowed features.

Generate exactly three separate low-fidelity drafts, one call per direction, showing full composition, depth, color, and style. Hard strings such as titles/official names stay exact; lengthy secondary copy may be indicated by placeholders here. Low fidelity changes detail and secondary-copy completion, not generation quality, profile, or assembly. Never use a contact sheet/triptych instead.

**Ratio gate:** open actual files and read pixels. Reduce target to integer `p:q`; require `width*q == height*p`, zero tolerance. If unequal, center-crop the largest exact rectangle with `k=min(width//p,height//q)`, size `k*p` × `k*q`; stop if `k<1`. Save a new version, reopen, and verify ratio, required copy, and subject coverage. No padding or larger-canvas workaround. Cropping required content fails. Check all edges for full bleed.

**Original assets:** generate full bleed, then use `overlay_assets.py` to composite supplied logo/QR PNGs. Rasterize SVG faithfully to nonempty transparent PNG first. Exclude identity assets, placement requests, and placeholder terms—logo, badge, seal, QR, reserved box/position, top-right mark—from image and negative prompts. With no logo file, never mention or invent one. A bare base is not a candidate: complete this stage's copy/assets before registration. Placeholder permission does not cover identity assets.

Register actual files with `directions`; these are pending selection, not approved deliveries. Historical preview naming remains. Show three images, differences, and candidate `version`; ask A/B/C or feedback for a new set, then end the turn. Only after genuine reply run `select` with current version and verbatim reply.

- All rejected/no/new set: `feedback` → `new_directions`; rebuild three and repeat HG3.
- Selection plus local feedback: record both, refine in step 5.
- Yes alone/ambiguous/no reply: remain pending, never silently select.

### 5. One high-fidelity final poster

Read design-refinement. Edit/composite the approved actual draft with the same prompt pipeline/profile/negative rules/canvas. Complete exact required copy, detail, and assets. Preserve composition, subject, style, palette, view, space, information positions, and HG2 typography. Apply ratio/asset gates.

Work on the actual image, including composite/overlay helpers as appropriate; never regenerate a similar substitute from text. Local repairs include wrong/missing characters, pseudo-text, accidental defects, required-copy completion, and necessary readability.

Register with `poster`, link selected preview `version`, and honestly use `production_mode=edit` or `composite`. A local change is a version, not an extra direction. Major changes return to step 4/HG3. Even without requested changes, complete final production and quality review before confirmation.

### 6. Quality review — at most two correction rounds

Read quality-script-usage and the full rubric. Inspect actual pixels; submit current hash, stage, H1–H8 evidence, active-profile typography, dimension scores, and confirmed specs to `check_poster.py`. Missing decoding/evidence cannot pass. Match report hash to registered poster, then send decision/path to `review`.

Complete the first full-poster review and baseline; later local changes require affected-scope review. Cover completeness, cultural evidence, exact characters/official names, structure, hierarchy, readability, and actual properties. Mark unverified items unknown. Continue only after recorded pass.

Target the most consequential defect per round, rerun pixel review and `review`. At most two rounds for the entire quality phase; versions do not reset it. If still failing, stop, explain, and request a user decision. Never lower standards or award aesthetic points merely for completeness. Local defects return to step 5, culture to step 3, concepts to step 4/HG3.

### 7. Final confirmation

Show the actual complete version and verified dimensions/format; ask if final. Only a genuine current-version confirmation permits `confirm_final` with `confirm=true` and verbatim reply. It authorizes export; direction selection does not.

- Confirm: step 8.
- Local changes: `feedback=local_revision`, step 5 and affected-scope review before asking again.
- New direction: `feedback=new_directions`, step 4/HG3.
- Ambiguity/no reply: remain pending.

### 8. Deliver unchanged

Immediately before delivery run `check` target `export`; register byte-identical copies with `exported`. Deliver confirmed original or identical copy. No generation, polishing, copy edit, crop, recolor, or format conversion after confirmation. Visible changes invalidate it and require review/new confirmation. Give real links, verified specs, and quality conclusion; preserve approved version and never claim unverified print readiness.

## Machine contracts

Change interfaces only together with consumers.

- R7 is parsed by `build_prompt.py::mapping()`: splitting each data row on `|` yields six segments, segment 2 is one A–H letter, IDs retain backticks, and eight category rows exist. Do not add columns/remove rows/strip backticks.
- Preserve base-prompt `<!-- TEMPLATE:... -->` blocks and `{{field}}` names.
- Negative-prompt noncomment lines are `<Chinese> | <English>`; split at the first `|`, no second separator, neither side empty.
- Preserve preflight canonical keys and nested fields.
- `approve` aliases `confirm_final`; `awaiting_export_approval` / `export_allowed` are legacy labels, not another gate.

## Language versions and twin packages

Language versions share HG3's selected visual asset: subject, composition, palette, material, and information regions remain identical. Use separate state tasks linked to the shared selected version; approvals never transfer. Rebuild each copy manifest from supplied language masters; never independently translate missing event copy. Apply the same profile, measured separately. Official designations remain exact. Each language independently completes steps 5–8.

Twin convention: `scripts/`, `assets/`, and `cultural.txt` remain byte-identical. The 55 style/layout definitions are untranslated, identical ID libraries. SKILL.md and other human-readable references are English here and Chinese in the twin. This edition resolves obsolete supporting-guide gate/step references against the main eight-step workflow; functional interfaces remain unchanged.
