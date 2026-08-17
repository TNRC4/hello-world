# Continuation State

Last session: 2026-08 — **go-live maturation pass** (branch `agent/cvah-go-live-readiness`). Not a content-expansion pass: no new lessons, no new academies. Correctness, usability, adaptability, human review, and making the software harder to misuse.

**Stage: `LOCALIZATION REQUIRED`** — see `Go_Live_Status.md`. That file, not this one, is the authority on readiness.

Last build session: 2026-08-17 (second pass — depth & assessment directives applied). Build v1.1: v1.0 architecture + 10 benchmark Clinical Skill Courses, full question-bank anti-giveaway rewrite (294 items), perioperative flagship deepening (tiers, fault-finding, ECG/BP, sim library II, PA-PERIOP-EXAM). See Depth_and_Assessment_Audit_2026-08.md. The project is resumable from the manifest; nothing requires re-architecting.

## What changed in this pass
Regulatory citations corrected repo-wide (§32-2281 → §32-2211(5); §32-2201 definitions added; supervision remapped to Arizona's two statutory states; T1/T2/T3 risk tiers with hard verification blockers) · Human-Centered Instruction Standard (binding on all future contributors) · CSC standard amended with technique-variation, what-may-vary, and precision-audit sections, retrofitted to all ten benchmark courses · language precision sweep · Now/Next/Later learner focus model · production/review build separation with no unapproved numerics in the learner build · troubleshooting index moved out of the renderer into reviewable data · builder made portable and self-describing · six-stage go-live ladder · pilot feedback loop with a binding build gate · automated QA suite (13 checks) wired into CI.

## Next-builder queue — READ THE GATE FIRST
> **`Pilot_Feedback_Loop.md` §4 blocks bulk authoring of the remaining 44 skill specifications until one pilot cycle has completed and been written up.** The only exception is a safety-critical gap found during the pilot. This gate is enforced by `qa_check.py`. Do not "helpfully" clear the backlog.

1. **Human work, not builder work** — Phase A localization: T2 scope verification, reference-card approval, the R1a review question on each course, equipment survey, placeholder resolution. Nothing below matters until these move.
2. Run the pilot. Collect the ten signals. Write up the findings.
3. *Then* revise existing modules in the order the pilot's "what did you still have to explain" data dictates — and **cut** what the overexplained signal identifies. The next cycle is expected to remove material, not only add it.
4. Then author remaining specs, prioritised by what the pilot showed people needed and could not find, using a template corrected by the findings.
5. Equipment-dependent modules (Lab analyzers, imaging, pumps) unblock when the registry is populated.

## Standing rules for any contributor
Canonical content in the repository, never LMS-only · every clinical change through medical review · no high-risk numerics outside approved Controlled Reference Cards · the renderer renders and never authors · `qa_check.py` must pass before commit · only a human advances the go-live stage · update this file and `BUILD_MANIFEST.json` each session.
