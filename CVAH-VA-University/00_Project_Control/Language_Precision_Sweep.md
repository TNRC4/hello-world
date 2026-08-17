# Language Precision Sweep — 2026-08

Scope: the ten benchmark Clinical Skill Courses, swept against the Human-Centered Instruction Standard. Method: automated extraction of absolutes and exact values, then manual classification of every instance. **Nothing was deleted automatically.** The point of the sweep was to find out which rules are rules.

## What the scan found

| Pattern | Instances | Verdict |
|---|---|---|
| `never` | 47 | **Overwhelmingly appropriate — kept.** Nearly all attach to genuine critical fails: hand-recapping, stylet left on a table, re-advancing a catheter over its stylet, tracheal pressure, forcing a flush, flicking air toward a patient, fabricating a value, proceeding past a stop. These are exactly the places the word should be spent. |
| `always` | 10 | 6 kept as genuine safety or house standards; 3 were rhetorical prose rather than instruction ("the incident always happens 'suddenly'") and are harmless; 1 sat inside a PEARLS block already labelled as preference. |
| `only correct` | 1 | **Defect — fixed.** "Step 8 — Exit in the only correct order" (CSC-VEN-01) rewritten to "Exit in the order that prevents hematoma," with the reason stated. The order is well-founded; the phrasing claimed more than the physiology does. |
| `must` | 9 | All in safety or legal context. Kept. |
| Exact angles | 13 | **Already honest.** Every one is a *range* (15–30°, 10–20°, 25–30°) rather than a false point value, and the one bare figure — "maybe 45°" for jugular nose elevation — is explicitly hedged. Reclassified as `[GUIDE]` in each course's precision audit rather than reworded. |
| Exact distances | 8 | Mostly the 1–2 mm catheter advance, which reflects real catheter geometry (the plastic tip trails the steel). Reclassified `[EVIDENCE/mechanical]`, not scaffolding. |
| Exact times | 36 | Mixed: pressure holds, fill waits, escalation thresholds. All reclassified `[GUIDE]` except the two-minute alarm-escalation rule, which is a `[HOUSE]` standard with a stated reason. |
| Repetition counts | 0 matched in CSCs | Counts live in `16_Case_Logs/Repetition_Requirements.md`, which already labels them "educational requirements, not legal rules" and states the rationale for each. No change needed. |

## The honest summary

The corpus was in better shape than the sweep expected. The dominant failure mode was **not** false precision — most numbers were already written as ranges — but the *absence of a stated weight*. A reader could not tell which numbers were load-bearing and which were a place to start. That is what §16 (Precision audit) in each course now fixes.

One real defect was found and corrected. One structural gap was closed: every course now carries a "What may vary without being wrong" box, so assessors have an explicit, concrete list of variants they must not fail — rather than inferring permission from silence.

## Tactile analogies — deliberately kept

The sweep flagged the vivid analogies (cooked-versus-uncooked spaghetti for a vein; straw / bread dough / wall for the three flush sensations; "lift a coin" for aspiration force). These are `[GUIDE]` and they stay. They are how experienced people actually transmit tactile knowledge in speech, and removing them in the name of precision would make the courses *less* useful and less human, which is the opposite of the standard's intent.

## Standing rule

New content is written to the seven-level taxonomy from the start. This sweep is repeated whenever a course reaches MAJOR revision, and the QA suite counts absolutes per file so a regression is visible.

## Still outstanding — requires a person

Every course's R1a review question ("would an experienced CVAH technician disagree that any one method is presented as the only correct method?") is **unanswered**, because answering it requires a CVAH technician. Until it is answered per course, that course may teach but may not be the basis of a failing assessment. This is enforced in `qa_check.py` and tracked in the build manifest.
