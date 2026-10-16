# Cultural Event Poster Generator

`new-cultural-en` is an AI assistant skill for creating posters for cultural exhibitions, performances, heritage crafts, workshops, and festivals. It turns supplied content and verified cultural context into three visual directions, then develops the user's selected direction into a reviewed final poster.

The package combines creative guidance, visual references, typography policies, and Python workflow helpers. This English edition includes an English `SKILL.md`, 15 English workflow references, an English example brief, and shared original scripts and assets. See `TRANSLATION-NOTES.md` for the localization boundary.

## What it is designed for

- Cultural exhibitions and museum programs.
- Performances and cultural festivals.
- Traditional crafts and intangible cultural heritage events.
- Workshops and related cultural programming.
- Multiple language versions using supplied copy and a shared visual system.

Ordinary product advertising is outside the skill's scope. The workflow does not impose one cultural aesthetic, canvas ratio, or visual style on every project.

## Key features

**Reference-guided art direction.** The package includes 38 style definitions and 17 layout definitions, with style contact sheets and composition references. The assistant reads the selected definitions and inspects their images before proposing or generating directions.

**Three meaningful alternatives.** A/B/C drafts should differ in composition and visual treatment, rather than merely changing color. Each is generated as a separate image.

**Exact copy and cultural context.** Required wording, official names, dates, venues, and participation terms are preserved. Cultural meanings and uses require evidence; missing facts and unsupported translations are not invented.

**Configurable typography.** A flexible default profile supports expressive typography; an optional restrained profile enforces measurable size, spacing, and area limits.

**Asset fidelity.** Supplied photographs may become the visual base. Logos and QR codes are composited from original assets rather than redrawn by an image model.

**Version-specific review.** Quality evidence and approval records are tied to actual image versions. Final delivery uses the confirmed file or a byte-identical copy.

## Package contents

```text
new-cultural-en/
├── SKILL.md                       Main workflow and operating rules
├── cultural.txt                   Flat file inventory
├── assets/
│   ├── style-references/          Style images, contact sheets, and indexes
│   ├── composition-references/    Layout images in seven principle groups
│   ├── negative-prompt.txt        Paired Chinese/English negative rules
│   └── typography-*.json          Profile pointer and policy values
├── references/
│   ├── style/                     38 style definitions
│   ├── layout/                    17 layout definitions
│   └── *.md                       Analysis, selection, rendering, and review guides
├── scripts/                       Python helpers and regression checks
└── templates/
    └── prompt-brief-example.json  Illustrative prompt brief
```

In the supplied archive, the style folders contain **177 individual reference images**, plus **38 style contact sheets** and an overview image. The composition library contains **79 images**. These counts describe the inspected archive; the main skill text uses an approximate style-image count.

Resolve package paths relative to the directory containing `SKILL.md`. Preserve filenames, capitalization, and directory names when moving the package. To add this README to the package, place it beside `SKILL.md`.

## Requirements and setup

Use the intact skill folder with an AI assistant environment that can read local files, inspect images, generate and edit images, and consult sources for cultural verification. Configure skill discovery according to that environment's own instructions.

The included helpers use Python 3. Pixel inspection, text rendering, image compositing, and the regression scripts require Pillow. The package does not bundle an image-generation model, an OCR engine, a cultural research service, or font files. SVG rasterization requires a separate suitable capability in the host environment.

No specific Python or Pillow minimum version is declared in the supplied package. The translation was checked with the bundled design-free and typography regression suites; see `TRANSLATION-NOTES.md` for results and limits.

## Getting started

Give the assistant the event brief, all required wording, the intended format and dimensions, and relevant assets. Specify which assets must appear and which serve only as references. If several language versions are needed, supply approved copy for each language.

Example request:

```text
Use new-cultural-en to design a poster for a traditional paper-craft exhibition.
Use the attached event brief as the source of all required copy.
The confirmed canvas ratio is 2:3, portrait, for digital display.
Use the supplied craft photographs as subject material and preserve the supplied
logo as an original asset. Use the default typography profile.
Start by extracting the complete copy for my confirmation.
```

Expect copy confirmation and a typography choice before image generation. The standard workflow includes three human checkpoints and a final confirmation.

### What to provide

| Input | What to include |
|---|---|
| Event content | Theme, title, official names, dates, venue, organizer, and participation details as applicable |
| Required copy | Exact wording and approved language versions |
| Output specification | Orientation, exact aspect ratio, dimensions where required, channel, and viewing context |
| Assets | Photographs, logos, QR codes, and any task-supplied font files |
| Asset roles | Required display material versus style reference, with permitted transformations |
| Preferences | Visual tone, style constraints, people policy overrides, and typography profile if desired |

Missing facts remain missing until resolved. Unread source pages, unresolved content, incomplete required copy, or an unknown or conflicting canvas ratio block generation.

## Workflow

| Stage | What happens | User involvement |
|---|---|---|
| 1. Content analysis | Read source material, inventory assets, extract exact copy, and separate facts from creative interpretation | **HG1:** confirm or correct the copy; no images |
| 2. Typography direction | Describe 2–4 options for weight, letterform, spacing, and treatment | **HG2:** choose a typography direction; no images |
| 3. Cultural verification | Check significant elements, attribution, context, and intended use against sources | Resolve material cultural questions where necessary |
| 4. Composition exploration | Select eligible styles and layouts, inspect references, and generate exactly three separate low-fidelity drafts | **HG3:** choose A/B/C or request a new set |
| 5. Final production | Edit or composite the selected actual draft into one high-fidelity poster with complete copy and assets | Feedback informs refinement |
| 6. Quality review | Inspect actual pixels, exact text, cultural evidence, typography, and technical specifications | At most two correction rounds during quality review |
| 7. Final confirmation | Show the reviewed complete image and verified dimensions and format | Confirm the current final version |
| 8. Delivery | Check export eligibility and deliver the confirmed file or a byte-identical copy | No separate export approval |

Low fidelity refers to draft detail and secondary-copy completeness. Required title strings and official names must still be exact. The final poster must include all required copy.

Final production preserves the selected composition, subject, palette, perspective, information placement, and typography direction. A major change returns to composition exploration and a new selection. Changes after final confirmation require renewed review and confirmation.

## Typography profiles

Set `brief.typography_profile` to choose a profile. If omitted, the default is `design-free-v1`.

| Rule | `design-free-v1` | `small-type-refined-v1` |
|---|---|---|
| Approach | Expressive typography guided by the brief | Restrained typography with enforced geometry |
| Title size | No fixed profile cap | At most 5.5% of the canvas short side |
| Title block area | No fixed profile cap | 15% target; 20% hard maximum |
| Total text-block area | No fixed profile cap | At most 20% of the canvas |
| Negative space | No fixed profile minimum | At least 30% |
| Edge safety margin | No fixed profile minimum | At least 8% of canvas width/height |
| Text and subject clearance | Design judgment | Text-block gap at least 2%; core subject clearance at least 4% of the short side |

Both profiles require exact required text, readability at the intended viewing size, no pseudo-text, and preservation of facts. The profile JSON files and typography references contain the detailed measurement rules.

### Text production modes

- **Integrated — default:** the image model renders text using visual descriptions of letterforms. No font files are required.
- **Composite:** the model produces a separate typography layer, which is blended onto an approved base. Useful for copy changes or language versions sharing the same base image; no font files are required.
- **Overlay:** local rendering uses font files explicitly supplied by the user for the task. Glyph coverage must be checked. The package permits no system-font fallback or unsolicited font installation.

The font-pairing guide describes eight visual pairings. Font family names and file paths are not inserted into image-generation prompts.

## Composition and asset rules

The 17 layout definitions form a library, not an unrestricted candidate pool. Eligibility follows the event-category mapping and active typography profile.

- `modular-grid`, `split-horizontal`, and `split-vertical` are globally excluded by the current main workflow.
- Visible multi-panel collages and card-wall arrangements are prohibited; a hidden alignment grid is allowed.
- `frame-within-frame` permits one continuous window.
- `big-type-only` requires an explicit user layout override under `design-free-v1` and is ineligible under `small-type-refined-v1`.
- People are allowed for performance, festival/carnival, and market contexts, or people-only reference material. Mixed reference material favors other subject matter; other contexts exclude generated people unless explicitly overridden. Required supplied assets containing people need a clear decision if they conflict with this policy.

The assistant checks actual image dimensions after generation. Aspect ratio must match exactly; any corrective crop must preserve required content. Padding or border strips are not used to force a match.

Original logos and QR codes are composited onto the actual image. SVG assets are first faithfully rasterized and checked. Style-reference images are not automatically authorized as exhibition content.

## Python helpers

Run commands from the skill root. Replace placeholder paths with real task paths. The commands below are separate helper operations, not an unattended end-to-end pipeline.

| Script | Purpose |
|---|---|
| `preflight.py` | Validate source coverage, canvas agreement, and required-copy completeness; called by other helpers |
| `decision_tree.py` | Route an analyzed brief to eligible layout candidates |
| `build_prompt.py` | Assemble image prompts, reference plans, typography rules, and production notes |
| `typography_policy.py` | Resolve profiles and supply typography constraints and review logic |
| `human_gate.py` | Track sequential workflow state, versions, and supplied approval evidence |
| `render_text_layers.py` | Render overlay text using task-supplied fonts |
| `composite_text_layer.py` | Blend a model-rendered typography layer onto a base image |
| `overlay_assets.py` | Composite original raster assets |
| `check_poster.py` | Inspect file properties and evaluate submitted review evidence |
| `test_typography.py`, `test_design_free.py` | Regression checks for maintenance |

Example invocations:

```text
python scripts/decision_tree.py <task>/brief.json
python scripts/build_prompt.py <task>/brief.json --candidates
python scripts/build_prompt.py <task>/brief.json
python scripts/human_gate.py --state <task>/hg-state.json --request <task>/hg-request.json
python scripts/check_poster.py --request <task>/quality-request.json --out <task>/quality-report.json
```

`build_prompt.py` prints JSON; the host assistant uses that output with its image tools. Consult the relevant rendering reference before using the compositing helpers.

### Brief and state contracts

The example brief is an illustrative starting point, **not a ready-to-run production input**. It contains placeholder reference paths and uninspected references, and omits mandatory preflight information. A real brief must include:

- `source_audit`: completion status, source documents, all read page numbers, and unresolved items.
- `canvas_spec`: the ratio, source, and verbatim specification, consistent with `canvas`.
- `source_copy`: exact text, source, IDs, and required/optional status, with omission reasons where applicable.
- `copy_items`: every required source item, matched by ID and exact text.
- Selected style/layout IDs, inspected references, design fields, and typography settings required by the relevant helper.

Keep runtime state in the task output directory, with a separate state file for each language version. Mutating state requests require the current revision. HG2 is recorded in the conversational brief; it has no dedicated script action.

The state helper cannot prove that the user actually approved a choice. Approval evidence must come from the real conversation.

## Quality review and delivery

Review the actual completed image. Evidence covers H1–H8: requirements and typography, copy and facts, cultural accuracy, subject and structure, use specifications, designated assets, complete presentation of user material, and a memorable visual core.

The rubric requires applicable hard gates to pass, a total score of at least 85, and at least 3/5 in each weighted dimension. Unknown evidence blocks readiness. The review is tied to the current image's SHA-256 and stage.

`check_poster.py` checks technical properties and evaluates supplied evidence and scores for H1–H8. It does not independently perform OCR, verify cultural truth, decode QR codes, judge aesthetics, or certify print readiness. H8's visual judgment must be supplied by the reviewer; a script pass does not prove the evidence is true.

After no more than two quality-correction rounds, unresolved failures are reported for a user decision. A passing report permits final confirmation; it does not replace that confirmation.

## Multiple language versions

Use the selected direction as a shared visual system, preserving composition, subject, color, materials, and information regions. Rebuild each version's copy manifest from its supplied approved wording. Do not independently invent translations. Each language version has its own state, review, and final confirmation.

## Maintenance notes

Preserve the machine-readable contracts: the R7 category table in `references/selection-guide.md`, `TEMPLATE` markers and placeholders in `references/base-prompt-EN.md`, the paired-line format of `assets/negative-prompt.txt`, and canonical preflight field names.

The English guides align older step/gate references with the eight-stage sequence in `SKILL.md`. Illustrative examples still require real task data and current helper contracts before production. `approve` and export-related legacy state labels do not introduce a separate export approval gate.

This English edition was derived from the supplied Chinese archive. Scripts, assets, the 55 style/layout definitions, and cultural.txt were preserved byte-for-byte. Reference-image ownership and redistribution permissions are not established by this README.
