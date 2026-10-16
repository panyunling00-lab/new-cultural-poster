# Model-rendered typography and local blending — composite path

This third text path complements integrated and font-based overlay. Use when copy revisions must preserve the base or multiple languages share an approved base. Read before first composite production. No font files are involved. The active typography profile governs geometry; the quality rubric governs review scope.

## Responsibilities

- The image model draws the text layer: type design, pairing-described letterforms, and exact copy.
- Local code only crops, scales, positions, blends, and adjusts opacity. Never redraw, re-typeset, vectorize, or repair letters locally.
- Generate the text-free base once, following overlay rules: quiet regions, no letters or pseudo-text.
- Composite original logo/QR assets separately; never ask the model to redraw them.
- All type scale, margins, and measurements come from the active profile.

## When to choose composite

Use for likely copy revisions, multiple language versions, or a base containing faithful supplied photography or expensive image-to-image work that must not drift. Language versions share the base but independently complete production, review, confirmation, and delivery. Integrated remains the simpler default for uncomplicated single versions; the source's illustrative generation counts are four rather than five, not a guaranteed budget.

## Text-layer input

Supply exact copy, letterform descriptions, regions, canvas, reading order, and relationship to the base. Add no translations, slogans, signatures, dates, or organizations. Include only requested languages.

Transparent layers are preferable where supported. For the bundled blending script, use pure black with light text or pure white with dark text, without scenery, gradients, or background texture. Text material may be expressive if exactness and recognition survive.

## Generation rules

Generate one text-layer image per call:

- Match the confirmed poster ratio. A full-canvas layer is most predictable; a local layer is allowed with an explicit placement box.
- Use `#000000` with light/white type for screen, or `#FFFFFF` with dark type for multiply. No background texture, gradient, scene, border, vignette, or shadow that loses neutrality under blending.
- Include only exact manifest strings, with every required item. No pseudo-text, invented signatures, duplication, or filler letters.
- Follow pairing descriptions; no font names/files/paths.
- Measure the complete title block and role sizes on the composite. Small-type follows its JSON caps for title/subtitle/body/margins/negative space. Free design has no numeric design cap; exact copy and intended-size readability still apply.

## Local compositing

```text
python scripts/composite_text_layer.py --base <task>/base.png --layer <task>/type-layer.png --out <task>/version-02/composite.png --config-out <task>/version-02/composite-config.json --box 0.06,0.05,0.88,0.30
```

`--mode auto` reads corner luminance: near-black selects screen, near-white multiply, all others are rejected. A gray base means regenerate the text layer, not local extraction. Screen leaves black neutral and multiply leaves white neutral; unprinted areas should preserve the base. Incorrect matching darkens/whitens the image; rejection is a hard guardrail.

Preserve the original base. Regenerate only affected text layers for errors. Use separate foreground/masks for occlusion, not blind overprinting. The script refuses to overwrite base/layer and records paths, SHA-256, mode, placement, opacity, and output hash in JSON. Identical inputs are reproducible; replace only text to revise copy.

## Artifacts and review

Save versioned base, text layer, composite, and `composite-config.json` in task output. Shared multilingual bases are allowed, with independently arranged text layers. Config is an internal production record, not a form the user must fill. Follow normal final confirmation; no additional approval.

Before blending, inspect every glyph at full resolution against the manifest. Wrong/missing glyphs require text-layer regeneration, never a new base or local letter repair. After blending, submit typography measurements from the composite pixels to `check_poster.py`. Blending success does not prove scale, spacing, readability, exactness, or aesthetics. The low-cost text layer protects the more costly base.

Perform the first full review, then affected-scope reviews. Deliver the confirmed version unchanged.
