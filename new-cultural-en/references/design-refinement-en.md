# Design refinement for cultural event visuals

## 1. When and why

Read after HG3's genuine selection, before completing the poster. The selected actual image is the final baseline, not an invitation to regenerate variants. Repair typos, missing glyphs/copy, pseudo-text, accidental structural defects, and necessary local readability only. Do not change subject angle, palette, or information placement. Major composition/style changes return to step 4 and new HG3 selection.

Edit/composite the selected image, preserving theme, subject, composition, palette, and major materials. Identify the most consequential 1–3 issues and target them. Do not add/remove intentional decoration or rearrange approved design in the name of refinement. Mature designs need only necessary improvements.

Load active profile from the brief, default free design; typography-constraints is the entry point, typography-system applies only to small-type, and profile JSON supplies values. Scale/ratios/weight/leading/tracking/family/space/clearance follow it, not optional grids below. The main skill/rubric govern culture, facts, and completeness. Invent no missing names/dates/venues or filler copy.

## 2. Five principles

### 2.1 Limit font families

Follow profile budgets and preserve selected letterforms. Weights within a family are not new families; count Chinese/Latin separately. Variations serve roles, not decoration. Consider theme/format/length/readability. Integrated uses visual pairings, overlay registered supplied fonts. Style language never authorizes loading other fonts.

### 2.2 Establish the primary focus

Focus may be designed type, object, space, graphic, or illustration. People require the resolved policy. Preserve selected overlap/full-bleed/recognizable partial occlusion. Place title in the layout's text zone and obey active subject clearance.

### 2.3 Organize negative space

Space supports emphasis/grouping/reading. Prefer intentional continuous space over accidental fragmented gaps. More or less is not inherently better; obey active ratios/insets.

### 2.4 Control color roles

Start with 1–3 main roles: primary, secondary, accent. Value variations may share a hue role; black/white/gray count by function, not every natural photo color. Multicolor/festival/experimental work may use more where dominance remains clear, though rubric color-role caps still apply. Do not make all culture red/gold, muted, or beige.

### 2.5 Manage scale contrast

Low largest-to-smallest contrast can support restraint/sustained reading; high contrast energy. Follow purpose/approved direction. Never shrink dates/venue/body indefinitely to manufacture contrast. Repair local readability within active caps/ratios.

## 3. Size and leading relationships

### 3.1 Visible glyph height, font size, and leading differ

Reference diagrams show visible heights/block bounds, not software point sizes. Glyph/em ratio, capitals, ascenders/descenders, and perceived Chinese/Latin weight vary.

- a: main-title visible glyph height.
- b/c: secondary/tertiary visible height.
- x/y: clear gaps between visible glyph edges.
- L: baseline distance (leading), approximately b+x or c+y for comparable lines; real metrics/inspection prevail.

### 3.2 Equal-height blocks — source figures 1–2

```text
Main title: a
Secondary: 2b + x = a
Tertiary: 3c + 2y = a
General: n*h + (n-1)*g = H
b=(a-x)/2; c=(a-2y)/3
If x=k2*b and y=k3*c:
b/a=1/(2+k2); c/a=1/(3+2*k3)
```

Do not assume forced 1:.5:.333 size ratios; gaps occupy space. Illustrative chosen numbers, not image measurements: a=120, k2=.4, k3=.6 gives b=50, x=20, c≈28.6, y≈17.1; blocks are 120 high, baseline distances about 70/45.7. Equal modules are optional for editorial juxtaposition; do not change copy to force two/three lines or make tertiary copy unreadable.

### 3.3 Within-level consistency, between-level clarity — figures 2–4

Adjacent blocks share top/bottom/axis; stacked blocks keep rhythmic distance. Figure 3 juxtaposes a large title with a tertiary block and a separate secondary line; figure 4 centers a vertical hierarchy. Similar scales support different structures. Diagram colors explain structure, not required decoration or universal spacing; use actual blocks/groups.

### 3.4 Starting values elsewhere

Suggestions, not image measurements or universal standards. Binding role sizes/leading come from the profile. S here is nominal title size, not the short-side symbol used in profile measurement.

| Role | Initial size | Baseline distance / nominal size |
|---|---|---|
| Main title | S | Multiline Chinese 1.05–1.25 |
| Subtitle/theme | Active profile | 1.20–1.45 |
| Key date/venue | Active profile | 1.25–1.55 |
| Longer Chinese body | Profile, checked at target size | 1.40–1.70 |

Latin capitals may use tighter spacing where suitable; check strokes/extents. Equal nominal Chinese/Latin sizes do not assure optical equality. Reconsider for long/vertical/calligraphic/heavy/bilingual/dense text. Baseline distance differs from clear glyph gap.

Within-group gaps should be smaller than between groups; 1.5–2× is an optional starting relationship where comparable internal gaps exist, not a rule for single-line groups or approved experiments. Alignment/dividers/fields also group.

Check complete title blocks, not single glyphs. Size caps follow profile, readable floor follows channel, viewing distance, proportion, and copy. Inspect target size and full resolution. Pixels are not print points.

## 4. Grids, margins, proportion

Source figure 5 illustrates optional golden-ratio guides near 38.2%/61.8% of usable dimensions, from approximately 1:1.618. Not every canvas/element needs them. Follow approved composition/information before choosing modular/axis/column/golden guides. Keep construction grids invisible, consistent with the global no-visible-panels rule. Do not require multiple grids. Repeat margin/gutter/group rhythm with optical adjustment for curves/calligraphy/irregular subjects.

## 5. Design title and imagery together

Preserve approved overlap, foreground masks, silhouette alignment, interweaving, or quiet juxtaposition. No visible multi-panel collage; framed viewing uses one continuous window. Material-like letterforms may express craft while retaining names. Required copy stays identifiable; partial occlusion is permitted only where reading survives and the profile allows it. Connect scale/contour/direction/material instead of floating labels.

Purpose guides emphasis: exhibitions relate theme/work, talks topic/information, festivals participation/atmosphere, workshops making/experience. These are clues, not fixed style assignments. Use objects/material/action/space/concepts for culture, not unsupported symbols. Distinguish interpretation from reconstruction; verify motifs/dress/religious/historical details under the rubric.

## 6. Pairings and production

### 6.1 Integrated

Use pairing visual descriptions for coordinated scripts, within profile budgets; no family/file/path names. Removing fonts does not break selection/assembly. Descriptions guide appearance, not exactness. Inspect generated glyphs and repair through editing; use overlay only when supplied fonts and reliable typesetting are needed, not for every integrated poster.

### 6.2 Overlay

No fonts bundled. Register user-supplied files, record actual families and coverage, use another supplied match for missing glyphs, and report unresolved copy. No silent system fallback. Composite is also available without fonts; follow its guide.

## 7. Supplied venue and other imagery

Distinguish actual subjects, fidelity-sensitive photos, style references, and composition references. Reference text/marks are not current copy. Crop/grade/type/edit venue imagery within approved direction while preserving recognizable architecture. Invent no alterations, exhibits, or signage. Strong abstraction/illustration requires confirmed intent; core direction changes return to HG3.

## 8. Refinement plan and next steps

Record selected file/version; preserved subject/concept/composition/palette/material; up to three location/problem/action priorities; profile; families/features/weights/sizes/ratios; preserved title treatment/reading; intended-size glyph accuracy/contrast; overlap/masks; leading/gaps with units; one text–image relationship; actual edit/typeset/composite method; verification at target size/overview/detail/file level.

Pass the plan to base-prompt assembly, not this entire guide, scoring language, or example copy. Compare actual before/after and retain the previous version. Continue main quality review/final confirmation. This module does not approve, bypass helpers, or auto-export. Numeric relationships inform design, never replace pixel inspection.
