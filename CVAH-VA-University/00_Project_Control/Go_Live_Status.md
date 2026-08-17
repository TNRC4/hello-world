# Go-Live Status

**Current stage: `LOCALIZATION REQUIRED`** · assessed 2026-08 · next assessment when Stage 2 exits are met

The phrase "deployment-ready pending localization" was doing too much work. It let a project with unverified regulatory rows, unapproved clinical numbers, and zero hours of real-world use describe itself as nearly finished. This ladder replaces it. **The stage name is a claim about safety, not about effort spent.**

## The ladder

| # | Stage | What it means | Exit criteria |
|---|---|---|---|
| 1 | **CONTENT COMPLETE** | The curriculum exists and is internally coherent. Says nothing about correctness for *this* hospital. | Core Academy, skills library, assessments, rubrics, specialty structure all present; QA suite passes structurally. ✅ **met** |
| 2 | **LOCALIZATION REQUIRED** | Content exists but carries placeholders, generic assumptions, and unverified equipment references. **← we are here** | All `[CVAH-SPECIFIC INPUT REQUIRED]` items resolved; equipment survey complete and registry populated; house protocols attached; roles named. |
| 3 | **MEDICAL / REGULATORY REVIEW** | Localized, awaiting the two sign-offs that make it safe to act on. | Every T2 scope row verified against current Board rule with a date and verifier; all Controlled Reference Cards approved and signed; flagship material R1a-reviewed by a CVAH technician; safety-critical question-bank items DVM-reviewed. |
| 4 | **PILOT READY** | Cleared for supervised use with a small number of real learners. | Stage 3 complete; assessors calibrated against each other; pilot feedback instruments in place; a named person owns the pilot. |
| 5 | **PILOT VALIDATED** | It has survived contact with real learners and real shifts, and the findings have been acted on. | ≥2 learners through Weeks 0–4 minimum; feedback loop closed at least once; identified defects fixed or formally accepted; assessor disagreement rate reviewed. |
| 6 | **LIVE** | The operating training system of this hospital. | All of the above, plus: full Core cohort completed, graduation gates exercised end-to-end at least once, revalidation calendar running, and the Medical Director signs the go-live attestation. |

## Rules about the label

1. **Only a human may advance the stage.** No script, and no AI contributor, may edit this file to a higher stage. An AI may propose an advancement with evidence; a person accepts it.
2. **The stage can go down.** A lapsed reference card, a Board rule change, or a failed audit drops the project back to the stage whose exit criteria are no longer met.
3. **The console displays the current stage** and refuses to present unapproved clinical values in the production build regardless of stage.
4. **No stage above 3 may be claimed while any T2 scope row is unverified.** Scope is not a detail to be tidied later; it is the boundary of what the hospital is asking people to do.

## What is blocking Stage 3 right now

| Blocker | Owner | Detail |
|---|---|---|
| 10 T2 scope rows unverified | Medical Director + Program Administrator | `02_Scope_and_Regulatory/Arizona_Scope_Matrix.csv` — each needs current A.A.C. Title 3 Ch. 11 verification plus a written policy decision |
| 4 Controlled Reference Cards unapproved | Medical Director | CRC-001, 002, 003, 005 — draft values, absent from the production console by design |
| 2 cards not yet drafted | Medical Director | CRC-004 fluid rates, CRC-006 disinfectant chart — need house protocol input first |
| 10 CSCs awaiting R1a human review | Senior CVT | "Would we actually teach it this way?" — until answered, these teach but cannot fail anyone |
| `[CVAH-SPECIFIC INPUT REQUIRED]` items outstanding | Program Administrator | Count generated live by `qa_check.py`; Stage 2 does not exit until zero |
| Equipment survey not run | Program Administrator | Registry rows are placeholders; Lab/Imaging/Anesthesia equipment modules are blocked on it |

## What is genuinely safe to do today

Teach. Weeks 0–2 lessons, the ten Clinical Skill Courses, restraint and TPR practicals, case logging, and the whole competency framework work now and need no signature to be useful. What must wait is anything numeric-and-clinical, anything that fails a learner against unreviewed material, and any T2 task.
