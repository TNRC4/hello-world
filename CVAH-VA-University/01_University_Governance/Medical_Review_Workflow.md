# Medical Review Workflow

Version 1.0 · 2026-08-17

## What requires medical review
| Content class | Reviewer | Cadence |
|---|---|---|
| Controlled Reference Cards (all numeric clinical guidance) | Medical Reviewer (DVM), signature required | Before first use; at each card's next-review date; on any revision |
| New or MAJOR-revised clinical lessons | Medical Reviewer | Before LMS publication |
| Question-bank items flagged safety-critical | Medical Reviewer or delegated CVT with DVM countersign | Before entering exam pools |
| Practical rubrics & critical-fail lists | Medical Reviewer | Before first use; annually |
| Scope matrix rows | Medical Reviewer + Program Administrator (regulatory check) | Annually; immediately on regulatory change |
| MINOR/PATCH edits to approved content | Program Administrator (log only) | At release |

## Workflow states
`DRAFT → SOURCE-CHECKED → MEDICAL REVIEW → APPROVED → PUBLISHED → REVIEW DUE → (loop)`

Recorded per-file in `00_Project_Control/BUILD_MANIFEST.json` (`medical_review` field: `pending`, `approved:YYYY-MM-DD:reviewer`, `expired`).

## Review checklist (the reviewer attests to each)
1. Clinically accurate and current per cited sources.
2. Within Arizona assistant scope as classified; supervision language correct; no accidental implication of veterinary authority.
3. Safe: stop criteria and escalation criteria present and correct.
4. Consistent with CVAH protocols.
5. No copyrighted material reproduced beyond fair paraphrase-and-cite.

## Emergency correction path
Patient-safety errors found in published content: pull content from circulation immediately (any DVM/CVT can flag; Program Administrator pulls), correct, same-day DVM review, republish, log in manifest with `emergency_correction: true`.
