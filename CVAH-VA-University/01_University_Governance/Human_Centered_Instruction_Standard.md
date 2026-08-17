# Human-Centered Instruction Standard

Version 1.0 · 2026-08 · **Standing rule. Binds every future contributor to this University — human or AI.** Precedence: this standard sits directly beneath the University Charter and above every content template, including the Clinical Skill Course standard.

---

## 1. What this University teaches

**Outcomes, safety, judgment, and troubleshooting.** Not choreography.

A veterinary assistant who has finished a module should be able to achieve the *result* safely, know what "going wrong" looks like, and know what to do about it. Whether they hold the syringe exactly the way the author of the module holds it is, in almost every case, none of the module's business.

This matters because a system that teaches choreography produces two failures at once. It fails the capable learner who does the job perfectly by a different route and is told they are wrong. And it fails the struggling learner, who memorises a sequence of movements without ever learning what the movements are *for* — so the moment reality deviates from the script, they have nothing.

> **The test for any instruction:** if a learner does this differently but the patient is equally safe, the sample is equally good, and the team is equally informed — is the difference actually a problem? If not, it is not a rule. Write it as what it is.

## 2. The seven levels of "should"

Every instruction in this University carries one of these weights. Content must make the weight legible — in a tag, a sentence, or a section — so that assessors, trainers, and learners all know what they are looking at. Guessing which level applies is the defect this taxonomy exists to prevent.

| # | Level | What it means | May a learner deviate? | Notation |
|---|---|---|---|---|
| 1 | **Universal safety requirement** | Violating it can injure a patient or a person. Independent of hospital, equipment, or preference. | **No.** Deviation is a critical fail. | `[SAFETY]` |
| 2 | **Legal / regulatory requirement** | Statute, Board rule, DEA, OSHA, state radiation control. | **No.** Not ours to waive. | `[LAW]` |
| 3 | **Manufacturer requirement** | The device or product instructions for use. Deviating can void warranty, invalidate results, or harm. | **No**, unless the DVM directs otherwise and documents it. | `[IFU]` |
| 4 | **Evidence-supported recommendation** | Guideline or literature backing (RECOVER, AAHA, ACVAA, peer-reviewed). Strong default; occasionally superseded by patient specifics. | **Rarely**, and with a reason a DVM would accept. | `[EVIDENCE]` |
| 5 | **CVAH house standard** | CVAH deliberately chose one way — for patient safety, workflow consistency, or because variation was causing errors. The *reason must be stated.* | **No**, while the standard stands. Standards are reviewable, not sacred. | `[HOUSE]` |
| 6 | **Assessor-standardized technique** | Standardized only so a practical assessment can be scored consistently. Real clinical practice may vary more. | **Yes in practice**, no during that assessment — and the rubric must say so. | `[SCORED]` |
| 7 | **Useful approximation / experienced-staff preference** | A number, angle, analogy, or habit offered as scaffolding. Genuinely helpful. Not a rule. | **Yes.** Freely. | `[GUIDE]` |

**Levels 1–3 are non-negotiable. Level 5 must justify itself. Levels 6 and 7 must never be enforced as though they were levels 1–5.**

The most common defect this catches: a level-7 preference written in level-1 language. "Always enter the vein at 20 degrees" is not a safety requirement — it is scaffolding for a beginner who needs somewhere to start. Written as an absolute, it teaches a capable learner that this University does not know the difference between physics and habit.

## 3. Nobody fails for a legitimate variant

**A learner must not fail a practical assessment for using a technique variant that is equally safe and equally effective**, unless CVAH has deliberately standardized that technique under level 5 or level 6, and the rubric says so before the assessment begins.

If an assessor sees a variant they did not expect:
1. **Did the patient stay safe?** If no → that is the finding, and it stands on its own merits.
2. **Did the task achieve its outcome?** Usable sample, patent catheter, clean prep.
3. **Could the learner explain their choice?** Reasoning is competence. "That's how I was shown" is a weaker answer than "her vein rolls, so I anchored lower" — but neither is a failure by itself.
4. **Only then:** is this variant excluded by a stated `[HOUSE]` or `[SCORED]` standard the learner was told about in advance?

If 1–3 are satisfied and 4 does not apply, **the variant passes.** The assessor may still teach their preference — they should say plainly that it is a preference.

Surprise standards are prohibited. A learner cannot fail against a rule nobody published.

## 4. Write like a person

The voice of this University is an experienced colleague explaining something to someone they like and want to see succeed. Not a regulation. Not a textbook. Not an AI summarising veterinary medicine.

**Do:**
- Use plain words. "Push the elbow forward" beats "effect cranial translation of the antebrachium."
- Explain the *why* alongside the *what*. A learner who knows why will improvise correctly under pressure; one who only knows what will freeze.
- Name the thing an experienced person actually notices — the feel, the sound, the tell.
- Say "usually", "most dogs", "about", "roughly" when that is the truth. Hedged language is honest language when the underlying fact is genuinely variable.

**Don't:**
- Manufacture precision. "15–30°" is honest scaffolding; "exactly 22°" is theatre.
- Stack qualifiers until a sentence carries no instruction.
- Use jargon where a plain word exists, or invent terminology this hospital does not use out loud.
- Write absolutes for emphasis. `always` and `never` are load-bearing words in this University; spending them on ordinary advice devalues them exactly where they matter — patient ID, sharps, airway, contamination.

## 5. Human review before flagship material ships

Any flagship material — Clinical Skill Courses, practical rubrics, critical-fail lists, controlled reference cards, and anything tagged `[SAFETY]` or `[HOUSE]` — requires review by an experienced CVAH staff member (CVT or DVM) against one question:

> **"Would we actually teach it this way?"**

The reviewer is asked specifically to flag:
- Anything presenting *one common method* as *the only correct method*.
- Anything a competent technician here would disagree with.
- Anything that reads as generated rather than taught.
- Steps that are real but that nobody in this building actually does in that order.
- Anything missing that they would still have to explain at the table.

Reviewer name and date are recorded in `00_Project_Control/BUILD_MANIFEST.json`. **Unreviewed flagship material may be used for education but may not be used as the basis of a failing assessment.** That gate is enforced in the QA suite.

## 6. Trainers may add, contextualize, and offer alternatives

Trainers are not delivery mechanisms for a script. A trainer may — and should:
- Add context this hospital knows and the document does not.
- Offer legitimate alternatives, naming them as alternatives.
- Say plainly "the course says X; I do Y; here's why both work."
- Skip scaffolding a learner has already outgrown.
- Tell the Program Administrator when a document is wrong. **A trainer's contradiction of the curriculum is data, not insubordination** — route it into the pilot feedback loop (`00_Project_Control/Pilot_Feedback_Loop.md`).

What a trainer may not do: waive levels 1–3, quietly lower a rubric standard, or teach a variant as house standard without it going through review.

## 7. Applying this to existing content

This standard is retroactive in principle and incremental in practice. Content is brought into compliance when it is next touched, and flagship content on a scheduled sweep. The first sweep — absolutes and false precision across the ten benchmark Clinical Skill Courses — is recorded in `00_Project_Control/Language_Precision_Sweep.md`.

**Contributors must not respond to this standard by hedging everything.** The goal is accuracy about which rules are rules, not the removal of rules. A University where nothing is firm is as useless as one where everything is.
