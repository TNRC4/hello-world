# QA Report

**Stage: `LOCALIZATION REQUIRED`** (see `00_Project_Control/Go_Live_Status.md`) · last full audit 2026-08 (go-live maturation pass)

Machine-checked portions of this report are produced by `00_Project_Control/qa_check.py`, which runs in CI on every change. Prose findings are human judgements about the same evidence.

---

## Automated gate — current result

```
13 passed · 1 warning · 0 failures        (release mode: 2 failures, correctly)
```

| Check | Result |
|---|---|
| Assessment answer-leakage | 294 items · key positions A74/B102/C83/D35 · longest-answer giveaway 12% |
| Duplicate IDs | 294 question IDs unique · 75 skill IDs unique · KB IDs unique |
| Broken internal references | all backticked repo paths resolve |
| Regulatory citation integrity | §32-2281 appears only in dispensing context; assistant scope cites §32-2211(5) |
| T2 scope verification | 10 T2 rows · **10 awaiting Board-rule verification** |
| Controlled references | **0/7 approved** · production console carries no unapproved clinical values |
| Knowledge-base provenance | 24 entries, all tracing to real source documents · **24 awaiting review** |
| Console freshness | matches current sources |
| Regulatory verification age | **warning: no scope row has ever been verified** |
| Placeholders | 47 open `[CVAH-SPECIFIC INPUT REQUIRED]` |
| Pilot build gate | 29 specs written · 44 correctly withheld pending pilot |
| Human review gate | 10 skill courses awaiting the R1a question |

Release mode additionally fails on the 47 placeholders and the 10 unreviewed courses. That is the gate working.

---

## Defects found and corrected in the 2026-08 pass

**1. Wrong statute cited for assistant scope — 12 occurrences across 11 files.** The University cited **A.R.S. § 32-2281** as the veterinary-assistant scope statute. Verified against primary text at azleg.gov: § 32-2281 is *"Dispensing of drugs and devices; conditions; definition"* and has nothing to do with assistant scope. The correct authority is **§ 32-2211(5)** ("Exceptions from application of chapter"). The substantive rule the University taught was correct throughout — assistants may perform duties other than diagnosis, prognosis, prescription or surgery under direct or indirect supervision — but it was attached to the wrong section number. In a compliance document that is not a rounding error; it is the kind of defect that discredits the whole matrix in front of a Board inspector. All occurrences corrected; sourcing rule added requiring primary-text verification for statutory citations.

**2. Invented a supervision tier Arizona does not have.** The S1/S2/S3 scheme implied three statutory levels. Arizona defines exactly two: *direct* (§ 32-2201(8), veterinarian **physically present at the location**) and *indirect* (§ 32-2201(11), not present but written or oral instructions given). CVAH's S2 — "on premises, quickly available" — is legally **direct**, not a middle tier. Supervision tables rewritten to map house operating levels onto the two statutory states, with an explicit warning against reading them as a legal ladder. This defect was not in the brief; it surfaced while verifying the first one.

**3. Higher-risk tasks extrapolated from a general exemption.** The scope matrix implied that § 32-2211(5) settled questions it does not settle. Risk tiers T1/T2/T3 added: ten T2 rows (IV catheter placement, IM injection, IV push, induction, intubation, anesthetic monitoring support, dental procedures, prescription filling, controlled-substance records, cystocentesis) now require dated Board-rule verification plus a written CVAH policy decision, and **read NOT PERMITTED until both exist.** Silence is not authorisation. Enforced by the QA gate.

**4. Controlled-reference discipline violated by the University's own course.** `CSC-ASM-01` reprinted the CRC-001 vital-sign bands inline — creating a second, unversioned copy of exactly the numbers the controlled-reference system exists to centralise. Found by the production-build leak test, not by reading. Course now teaches the technique and cites the card. This is the failure mode the leak test was written to catch, and it caught it on the first run.

**5. Renderer was authoring clinical content.** 24 symptom-first troubleshooting entries lived inside `build_console.py` as Python literals — a second clinical source of truth, outside the medical-review workflow and invisible to reviewers. Moved to `28_Knowledge_Base/Troubleshooting_Index.json` with `source_document`, `source_section`, `review_status`, `medical_review_required`, `last_reviewed` and `reviewer` per entry. The QA gate now fails if the builder authors inline again.

**6. Unapproved clinical values were reachable in the learner build.** The console previously exposed draft reference-card values behind an acknowledgment click. Replaced: the **production build contains no unapproved high-risk numerics at all** — not hidden, absent — and a separate `--review` build serves the Medical Reviewer. Verified in-file and at runtime.

**7. Builder was environment-bound and unlabelled.** Absolute `/home/user/...` paths replaced with `Path(__file__)`-derived roots. Console now carries curriculum version, UTC build time, commit SHA, branch, dirty flag, source fingerprint, regulatory verification date, review status, and a stale-build warning after 90 days. All counts are computed programmatically, so prose can no longer drift from the repository.

**8. One broken internal reference and one non-deterministic check.** `passport_register.csv` was referenced but never created — now exists. The console freshness check computed its fingerprint over a call-order-dependent source set, producing a phantom "stale" failure; fingerprinting is now deterministic.

---

## Standing findings (unchanged, still true)

**Clinical accuracy.** Physiology and RECOVER 2024 figures re-checked against the guideline publications. Numeric bands remain DRAFT pending veterinarian approval; the system refuses to present them as clinical truth.

**Instructional quality.** The 2026-08 language sweep classified 47 `never`, 10 `always`, 13 exact angles and 36 exact times across the ten benchmark courses. Most absolutes were correctly spent on genuine critical fails, and most numbers were already honest ranges. One defect ("the only correct order") was fixed. The real gap was not false precision but *unstated weight* — which the seven-level taxonomy and each course's new precision audit now close. Full record: `00_Project_Control/Language_Precision_Sweep.md`.

**Technical education.** 29 full skill specifications; 44 deliberately withheld behind the pilot gate. This is not a backlog — it is a decision recorded in `Pilot_Feedback_Loop.md` §4.

**Operations.** Daily rhythm sized to ≥45 protected minutes; assessor flow designed to a 60-second standard. The learner-facing view is now Now/Next/Later with 1–3 active competencies, without touching the nine graduation gates.

---

## What this report cannot tell you

No learner has used this system. Every judgement here is internal review plus automated checking, and neither substitutes for the pilot. The most likely undiscovered defects are the ones only a real trainer and a real new hire can surface: material that reads well and teaches badly, steps nobody actually performs in that order, and gaps that are invisible from inside the document. That is what the pilot loop is for, and why bulk authoring is blocked until it runs.
