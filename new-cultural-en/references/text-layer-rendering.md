# Measured text-layer rendering — overlay path

Use for overlay completion in step 5. Read typography-constraints first; scale/margins/space/caps come from the active JSON file, not this guide. Free design has no numeric design caps. The helper uses Pillow and built-in Unicode cmap checks. If unavailable, use a verified glyph-measuring equivalent or integrated plus pixel review. Claim only rendering actually performed.

```text
python scripts/render_text_layers.py --request <task>/render-request.json --out-dir <task>/version-02
```

Supply a text-free background/graphic and exact copy. Overlay requires explicitly supplied fonts; no system searching or guessing. cmap formats 4/12 in TTF/OTF or first TTC face check every nonwhitespace codepoint. Unsupported mappings require an equivalent verified renderer, not assumed success. Use another supplied font for missing glyphs and report unresolved characters. The simple helper supports one font per item, horizontal wrapping, and vertical columns. Complex shaping, multifont runs, path type, or deformation may use an equivalent renderer retaining bounds/profile requirements.

## Input contract

- `background`: absolute existing graphic/illustration path with quiet text areas.
- `supplied_fonts`: absolute files actually provided by the user and registered for this task; each item font must resolve to one.
- `subject_boxes`: protected core details as pixel rectangles `[left,top,right,bottom]`, tight or several smaller rectangles for irregular shapes. The main graphic may extend beyond them. In free design these are measurements, not exclusion zones; overlap is allowed.
- `min_font_px`: optional integer floor, default 12, increase for the channel. Values below 12 are rejected. This is not a physical-viewing guarantee.
- `items`: complete copy with unique `id`, exact `text`, `role`, `font`, pixel `region`. Title/subtitle map directly; dates, body, venue, organizer, captions, CTA, and other roles use body scale.
- Optional per item: `direction` horizontal(default)/vertical; `align` left(default)/center/right; `color` default #202020; integer `font_size_px` within profile caps (uncapped free design); `leading` at least the role default. Vertical overflow creates right-to-left columns. Wrapping changes visual lines, not words/punctuation.

Automatic size uses the short side. Small-type uses Text Scale 0.35, insets regions by 2% of short side, clips to 8% edge-safe bounds, and measures full title/role sizes/gaps/4% subject clearance. Free design uses renderer starting values, zero gaps/margins, and descriptive geometry without design rejection. Copy cannot silently overflow regions. If it cannot fit above the readable floor or combined active checks fail, the helper errors without a preview; revise layout/canvas.

Illustrative schema, not runnable font assets:

```json
{
  "background": "C:/task/selected-background.png",
  "supplied_fonts": ["C:/task/user-supplied-font.ttf"],
  "subject_boxes": [[250,450,750,1100]],
  "min_font_px": 12,
  "items": [
    {"id":"title","role":"title","text":"Exact supplied title","font":"C:/task/user-supplied-font.ttf","region":[80,120,920,380],"direction":"horizontal"},
    {"id":"venue","role":"venue","text":"Exact supplied venue","font":"C:/task/user-supplied-font.ttf","region":[80,1200,920,1380]}
  ]
}
```

## Outputs and review

Use a new version directory; never overwrite source/background/previous previews. Outputs:

- `text-layer.png`: transparent full-canvas type, graphic separate.
- `composed-preview.png`: background plus type, awaiting review/final confirmation.
- `typography-geometry.json`: actual bounds, nominal sizes, copy, font files, checks, composite hash.

## Composite required original assets

Use overlay_assets to composite original logo/QR PNGs; no generated replacements or model-drawn placeholder boxes. It reads actual dimensions, composites onto the existing canvas without padding/enlargement, and preserves originals. Faithfully rasterize SVGs to transparent PNG with original geometry/colors first. The helper accepts PNG inputs only; convert other formats faithfully before use as appropriate.

```text
python scripts/overlay_assets.py --request <task>/assets-request.json --out-dir <task>/assets-version-02
```

```json
{
  "background":"C:/task/composed-preview.png",
  "assets":[
    {"id":"institution-logo","path":"C:/task/user-supplied-logo.png","position":"top-right","scale":0.08,"margin":0.03,"opacity":1.0},
    {"id":"reservation-qr","path":"C:/task/user-supplied-qr.png","position":"bottom-left","scale":0.12,"margin":0.03,"opacity":1.0}
  ]
}
```

Positions: top-right/top-left/bottom-left/bottom-right/center. Scale is longest asset edge / poster short side, default .08, preserving ratio. Margin is short-side fraction, default .03. Opacity is [0,1], default 1. List order controls alpha_composite. It writes new assets-overlay.png in out-dir without overwriting originals/existing files, and reports canvas dimensions, pixel bounds (right/bottom exclusive), and hashes. Inspect and verify QR decoding; compositing success is not usability/approval.

Copy measured items into visual_review.typography only for matching current pixels. Independently inspect and add profile flags: small-type graphic_primary/subject_clearance_verified/negative_space_ratio/intended_size_readable; free design intended_size_readable/exact_copy_verified/no_pseudo_text/facts_preserved, plus concrete evidence and profile_id. Never infer these from successful geometry. Then run check_poster. Readability, contrast, aesthetics, and actual negative-space area need pixel inspection. Large type and overlap do not fail free design.
