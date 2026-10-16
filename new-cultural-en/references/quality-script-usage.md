# Quality-script integration

At step 6, inspect the actual poster with the complete rubric, then run the helper. Read before first use. It supplements cultural verification, pixel inspection, OCR, and human approval; it replaces none. This document owns the request/report contract; the rubric owns standards and thresholds.

```text
python scripts/check_poster.py --request <task>/quality-request.json --out <task>/quality-report.json
```

Decoding and size checks require Pillow. If unavailable, H5 remains unknown; report missing capability, never automatic success. Do not install packages without appropriate authorization. No other third-party dependency is required by this helper.

## Request fields

| Field | Required | Meaning |
|---|---|---|
| `image` | Yes | Absolute current image path; helper computes SHA-256 and, with Pillow, dimensions/format |
| `stage` | Yes | `key_visual` or `final_poster`; other values invalid |
| `spec` | No | Confirmed/existing specifications only: integer width/height, format PNG/JPG/JPEG, ratio such as 2:3; mismatch fails H5 |
| `visual_review` | Yes | Reviewer evidence for the current image |

### visual_review

Before visual review obtain the current SHA-256 with a host hashing tool. Bind review to these exact pixels and stage, not earlier measurements.

| Field | Required | Meaning |
|---|---|---|
| `image_sha256` | Yes | Must match script-computed image hash; mismatch unbinds all gates/scores |
| `stage` | Yes | Must match request stage; mismatch also unbinds review |
| `hard_gates` | Yes | H1–H8 objects |
| `dimensions` | Yes | A–G objects |
| `typography` | Profile-dependent | Active-profile evidence |

## Hard gates

Each is `{"status": ..., "evidence": ...}`. Allowed status: `pass`, `fail`, `unknown`, `not_applicable`. Other statuses are invalid. Evidence must be nonempty or the gate becomes unknown.

| Gate | Check |
|---|---|
| H1 | Core requirements and mandatory typography profile |
| H2 | Copy and facts |
| H3 | Cultural accuracy |
| H4 | Subject and structure |
| H5 | Use requirements, also overridden by technical checks |
| H6 | Designated assets |
| H7 | Complete presentation of user material |
| H8 | Memorable visual core |

The bundled loop validates supplied records for H1–H8; H8's aesthetic assessment is still an explicit reviewer judgment under rubric §5, not independently computed from pixels. Record all eight using the same structure. A script pass cannot prove submitted evidence true. In final_poster, H1/H5/H7 cannot be not_applicable; the helper changes that to unknown. In key_visual H7 becomes not_applicable, pending final verification. Spec failures override H5 to fail; missing Pillow makes H5 unknown unless already failed. This reflects the actual bundled code rather than the source guide's outdated H1–H7 loop description.

## Dimension scores

Each A–G dimension is `{"score": ..., "evidence": ...}`. Scores are integers 0–5 with nonempty evidence; otherwise not assessed. Zero-weight dimensions such as key_visual G may be omitted. The helper uses rubric 1.2 weights, 70/85 thresholds, minimum 3, and hard-gate priority. Recheck code if rubric values change.

## Typography evidence

Active profile comes from brief.typography_profile, default free design. `visual_review.typography.profile_id` must match it. Wrong-profile evidence is unknown. Typography-constraints is the entry point; small-type system describes caps; defaults JSON points to numeric files. Missing required fields make H1 unknown; measured violations/failed visual flags fail H1 regardless of score. Geometry does not establish negative space or visual priority.

| Common field | Meaning |
|---|---|
| `profile_id` | Current profile ID |
| `evidence` | Nonempty, current-image, location-specific evidence |
| `intended_size_readable` | true passes, false fails, missing unknown |

Free design additionally requires true `exact_copy_verified`, `no_pseudo_text`, and `facts_preserved`.

Small-type additionally requires:

- `items`: measured list with `id`, `role` title/subtitle/body, `direction`, pixel `bbox=[x0,y0,x1,y1]`, `font_size_px`.
- `graphic_primary`: graphic/illustration is first focus.
- `subject_clearance_verified`: confirmed on actual pixels.
- `negative_space_ratio`: intentional low-detail space/canvas area.
- `intended_size_readable` as above.

Small-type key visuals may omit items. An explicitly text-free final brief uses empty items and `text_free_confirmed=true`.

## Example request

This deliberately incomplete request cannot pass. Replace placeholders/unknowns with actual observations and integer scores. Explain every not_applicable.

```json
{
  "image": "C:/task/poster-preview.png",
  "stage": "final_poster",
  "spec": {"ratio": "2:3", "format": "PNG"},
  "visual_review": {
    "image_sha256": "CURRENT_ACTUAL_FILE_HASH",
    "stage": "final_poster",
    "hard_gates": {
      "H1": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H2": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H3": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H4": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H5": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H6": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H7": {"status": "unknown", "evidence": "Not reviewed yet"},
      "H8": {"status": "unknown", "evidence": "Visual core not reviewed yet"}
    },
    "dimensions": {
      "A": {"score": null, "evidence": ""},
      "B": {"score": null, "evidence": ""},
      "C": {"score": null, "evidence": ""},
      "D": {"score": null, "evidence": ""},
      "E": {"score": null, "evidence": ""},
      "F": {"score": null, "evidence": ""},
      "G": {"score": null, "evidence": ""}
    },
    "typography": {
      "profile_id": "design-free-v1",
      "intended_size_readable": null,
      "exact_copy_verified": null,
      "no_pseudo_text": null,
      "facts_preserved": null,
      "evidence": ""
    }
  }
}
```

## Report and exit codes

Report keys: `rubric_version`, `stage`, `image`, `image_sha256`, `inspection`, `technical_checks`, `visual_review_bound_to_image`, `hard_gates`, `typography_checks`, `dimensions`, `total`, `decision`, `known_failures`, `human_approval`, `limitations`.

Exit 0: stage passes; 2: assessed but not passed; 1: invalid input/execution error.

## Missing evidence is not a pass

Missing status/evidence is unknown and blocks confirmed delivery. Missing weighted scores means not assessed/no complete total. Missing/mismatched hash unbinds all evidence. Unknown required gates or unscored weighted dimensions cannot yield pass. Report known failures even when not assessed. A key_visual pass never approves final delivery. The helper does not do OCR, decode QR codes, or check print production; submitted scores/evidence are evaluated for rules, not independently proven true.

## Sending review to the gate helper

For final_poster send the actual decision/report path to human_gate review with matching registered poster version:

| Field | Required value |
|---|---|
| `action` | `review` |
| `revision` | Current integer from status |
| `version` | Current registered poster |
| `decision` | pass / revise / rework direction / needs verification / not assessed |
| `review_evidence` | Nonempty evidence or report path |

First verify report hash against registered poster. Only pass advances to legacy-named awaiting_export_approval; that is readiness for final confirmation, not user consent. Other results remain review_poster and return to the relevant cultural, direction, or production step.
