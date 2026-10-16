# Typography profile entry point and design-free-v1 rules

This is the single entry point for typography rules. Headers in all 55 style/layout definitions point here. Switching profiles changes configuration, not those definitions.

## Profiles and switching

| Profile ID | Numeric file | Meaning |
|---|---|---|
| `design-free-v1` | `assets/typography-design-free.json` | Default; zero margins/gaps do not produce geometry failures |
| `small-type-refined-v1` | `assets/typography-small-type.json` | Sixteen numeric limits; geometry produces decisions |

Select with `brief.typography_profile`; omission uses `design-free-v1`. `assets/typography-defaults.json` points scripts to the default and profile files. Basic renderer starting values are adjustable, not design caps. `scripts/typography_policy.py` reads values from the active profile file.

| Switching rule | Free design | Small-type refined |
|---|---|---|
| Title size | No cap | ≤0.055S; title block target 15%, hard max 20% |
| Text-block area | No cap | Combined ≤20% of canvas |
| Negative space | No minimum | ≥30% |
| Margins | 0; not required | ≥8% W/H |
| Clearance | 0; not required | Block gap ≥2%; subject clearance ≥4% of short side |
| Geometry | Descriptive only | Pass/fail |
| `big-type-only` | Explicit `user_layout_override` only, outside category pools | Ineligible |
| Negative rules | People conditional on theme/references; visible panels always excluded | Same global rules |

`references/typography-system.md` applies only under small-type. `references/typography-moves.md` is an optional, profile-neutral menu.

## design-free-v1

Choose size, letterform, deformation, overlap, staggering, leading, tracking, and regions according to theme, medium, viewing size, and content. There is no default small type, paper texture, people, or restrained aesthetic. Category-eligible layouts remain available; big-type requires override, and three divided montage layouts remain excluded. Numbers in historical previews are not current hard rules.

Two hard typography requirements:

1. Every required string is exact and readable at normal viewing size. Effects must not change meaning, character order, or facts. Missing information remains missing.
2. No pseudo-text/garbled glyphs or invented names, dates, venues, organizations, cultural attribution, awards, or quotes. Check against `copy_items` item by item.

Text over full-bleed imagery is allowed and encouraged where appropriate. Foreground occlusion is allowed if required characters remain identifiable. Overlap, interleaving, cross-layer placement, paths, and vertical writing are options. Occlusion/crop/distortion/low contrast must not erase required strokes or the only instance of required copy. Decorative extensions or redundant noninformation forms may be cropped. Overlap is not an automatic failure.

Type is design material. Choose 0–2 relevant moves rather than stacking effects. The title may be the primary visual object. Set functional information for actual reading needs, without forcing it tiny or scaling it indefinitely with the title. Judge viewing size, contrast, and exact copy rather than fixed size ratios or whitespace area.

## Rendering and review

The basic renderer supports horizontal/vertical type; it does not automatically create distortion, dry-brush texture, path text, or foreground masks. Use integrated generation, editing, or suitable compositing for those effects. Renderer limitations are not design limits.

In the current image's `visual_review.typography`, record `profile_id=design-free-v1`, `evidence`, `intended_size_readable`, `exact_copy_verified`, `no_pseudo_text`, and `facts_preserved`. Boolean judgments must come from current pixels, copy, and facts. Missing evidence is unknown; confirmed error fails. Optional `items` record valid bounds/size/direction measurements without rejecting design by ratio. For key visuals, check only text actually present; do not claim complete-poster review. Reassess current versions under this specification rather than inheriting old records.
