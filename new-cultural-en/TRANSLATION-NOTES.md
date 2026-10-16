# English edition notes

## Source and scope

This edition, `new-cultural-en`, was derived from the user-supplied `new-cultural-zh.zip` on 2026-10-16.

English content includes:

- SKILL.md, with skill name changed to new-cultural-en.
- All 15 top-level workflow reference documents.
- The six machine-readable prompt templates and eight script-readable typography descriptions.
- The illustrative brief in templates/prompt-brief-example.json, using language=en.
- README.md and INTRODUCTION.md.

The English prose preserves the operating requirements, workflows, schemas, limits, and decision criteria, while consolidating some repetitive explanation and aligning outdated cross-references. It is an English working edition, not a certified line-by-line or typographically identical translation.

## Preserved shared files

Following the source package's twin convention, 370 files were verified byte-for-byte identical:

- All scripts and assets.
- All 38 style definitions and 17 layout definitions.
- cultural.txt, the original flat inventory.

Consequently, bilingual asset indexes, original reference-image text, code comments, diagnostics, fixed script-generated labels, and some prompt fragments may still contain Chinese. This is documentation/template localization, not a fully English-only software fork. Set language=en in real English briefs; event copy remains exactly the supplied language master rather than being automatically translated. The original cultural.txt is a historical shared inventory and does not list the added English-edition documentation.

## Consistency clarifications

- Human gates consistently mean HG1 copy confirmation, HG2 typography choice, HG3 three-composition selection, then final confirmation. The authoritative eight-step workflow replaces older supporting-guide step numbers.
- Low-fidelity A/B/C exploration is followed by one high-fidelity development of the selected actual draft; older immediate-final wording is reconciled with the main workflow.
- Typography instructions consistently distinguish the default free-design profile from the optional small-type profile. Numeric values remain in the unchanged profile files.
- Current code checks submitted H1–H8 records. The source quality-script guide's H1–H7 loop description was outdated; H8 remains human/assistant visual judgment, not an independent image assessment by the script.
- Actual reference-image counts are 177 individual style images, 38 style contact sheets plus an overview, and 79 composition images.
- Illustrative briefs are not production-ready. Replace placeholder paths, inspect real references, and add complete preflight data before generation.

No script algorithm, profile configuration, reference asset, or style/layout ID was changed.

## Validation

- test_design_free.py: 23 passed.
- test_typography.py: 31 passed, including synthetic rendering checks using an existing local Latin test font. No font is packaged or used for a real poster.
- Eight category mappings match the source after parsing; the human-readable mapping mirror matches too.
- All eight typography descriptions and six machine-template blocks parse; placeholder names match the source.
- Example JSON, frontmatter fields/naming, Markdown fences, document coverage, and absence of untranslated Chinese in localized prose were checked.
- All shared files match source SHA-256 values.
- The stock skill-creator quick validator could not run because its PyYAML dependency was unavailable. Equivalent checks of this simple frontmatter and scaffold/fence structure were performed without installing packages.

These checks establish packaging and helper compatibility. They do not certify real poster quality, cultural correctness for a future task, visual reference permissions, or print readiness. No live image-generation workflow was run for this translation.
