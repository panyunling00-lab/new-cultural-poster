# Human-gate script integration

From the skill root, use absolute task-state/request paths:

```text
python scripts/human_gate.py --state <task-output>/hg-state.json --request <task-output>/hg-request.json
```

Write JSON requests with normal file tools; do not interpolate verbatim user messages into shell commands. State belongs in task output, not shared skill files. Separate state per language; one active writer per task. This is a sequential host helper, not a concurrent server.

Except initialization, state-changing requests need the current integer `revision` returned by `status`. Registration returns image-version IDs. Failed requests exit 2 without changing saved state. Read results and never ignore a blocked check.

The workflow has HG1 copy confirmation, HG2 typography choice, HG3 three-draft selection, and final `confirm_final`. No independent export approval.

## Actions

| Workflow point | Action | Required data |
|---|---|---|
| First use | `init` | No existing state |
| Any time | `status` | No revision required |
| Step 1/HG1 | `brief` | `brief` object, `theme_status` = clear/missing/unclear/conflict |
| Before direction registration | `check` | `target=directions` |
| Step 4/HG3 | `directions` | Exactly three objects in `directions`, each `id` A/B/C, `path`, `style_id`, `layout_id`, `fit_evidence` |
| After real selection | `select` | `direction`, current candidate `version`, verbatim `human_message`; optional `refinement_feedback` |
| Before poster completion | `check` | `target=complete` |
| Step 5 | `poster` | `path`, `selected_version`, `production_mode=edit` or `composite` |
| Step 6 | `review` | Current poster `version`, `decision`, `review_evidence` |
| Step 7 | `confirm_final` | `confirm=true`, current `version`, verbatim `human_message` |
| Before delivery | `check` | `target=export` |
| Step 8 | `exported` | Current `version`, export `path` |
| Rejection/change | `feedback` | `route=new_directions` or `local_revision`, verbatim `human_message` |

Decision enums: `pass`, `revise`, `rework direction`, `needs verification`, `not assessed`. Registered images must exist, be nonempty, and use `.png`, `.jpg`, `.jpeg`, or `.webp`.

Directions also require real style definitions, category-eligible layouts, exact confirmed pixel ratio, and three distinct file hashes. Use current revision for mutations, including checks where required; stale revisions fail. Missing title/time/venue does not justify inventing facts. The host judges theme clarity; Python stores, not understands, the judgment. `approve` aliases `confirm_final`; legacy `awaiting_export_approval`/`export_allowed` names do not add a gate.

## Request examples

```json
{"action":"init"}
```

```json
{"action":"status"}
```

```json
{"action":"check","revision":1,"target":"directions"}
```

These illustrate syntax only. Read the actual current revision; do not copy the example value blindly. A `brief` request must include a full preflight-valid analyzed brief, not just a theme. A `directions` request must use the current brief's eligible IDs, actual inspected files, and real fit evidence. See the main skill and content-analysis contract.

## Gate behavior

HG1 shows all extracted copy—title, official designations, times, venue, organizers, participation—asks confirmation/correction, then ends the turn with zero images. Run `brief` only after a real reply and use the actual updated theme status.

HG2 offers 2–4 written typography options describing weight, forms, spacing, techniques, and fit; ask a choice and end the turn, zero images. Record the decision in the conversational brief; no dedicated action.

HG3 registers/shows exactly three actual low-fidelity compositions with the candidate version. Ask A/B/C or feedback for a new set, then end the turn. A real reply permits `select` with returned version and verbatim message. Rejection invokes new_directions and a new set/HG3; ambiguity or silence never permits automatic choice.

After selection, complete/register one high-fidelity poster, review with at most two total correction rounds, and stop for a user decision if still failing. After pass, show the actual completed version/specifications and request final confirmation. Only a real reply for the current version permits confirm_final. Local changes return to production/review; new directions return to step 4/HG3. Users need not type action names or version IDs; map clear replies to the currently shown version. Silence, tool output, elapsed time, preselected options, recommendations, and previous approval are not consent.

For replacement candidates, register a new complete set and obtain selection again. If only one changed, retain the other two files but register all three as a new set. Local edits preserve the selected source and invalidate final confirmation. New directions clear selection and confirmation.

## Capabilities and limits

Registration checks existence, extension, nonzero bytes, hashes, and the direction ratio checks implemented by the helper. It does not prove meaningful visual difference, actual display, genuine replies, cultural accuracy, production fidelity, or quality. Those remain the host's responsibility. It never generates images, waits on stdin, or builds UI.

The host must invoke checks; the helper cannot prevent bypass. Approval messages must come from real conversation evidence, with provenance retained. Changed image hashes/versions cannot inherit old confirmations. Export verification supports byte-identical copies only; even visually identical format conversions need separate verification and renewed confirmation.

Exit 0 means success/allowed; 2 means blocked/input error. Read before continuing.
