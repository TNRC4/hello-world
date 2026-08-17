# Pilot Feedback Loop

Version 1.0 · 2026-08 · **This document contains a hard build gate. Read §4 before authoring new content.**

## 1. Why this exists

The University currently has 47 skill specifications unwritten. The instinct — human or AI — is to finish them. That instinct is wrong, and acting on it would be the single most expensive mistake available to this project right now.

Nothing here has met a real learner. Every unwritten specification would be authored from the same assumptions as the written ones, so if those assumptions are off, the pilot doesn't reveal *one* bad module — it reveals fifty-seven at once, all needing rework. Writing the remaining specs before the pilot converts a cheap lesson into an expensive one.

**Build less, learn, then build the rest against evidence.**

## 2. What the pilot collects

Ten signals. The first three matter most, because they are the ones a curriculum cannot see about itself.

| # | Signal | Captured by | Instrument |
|---|---|---|---|
| 1 | **What the trainer still had to explain** after the learner completed the module | Trainer, end of shift | One line per occurrence. This is the single highest-value datum in the whole loop — it is the direct measure of whether a module taught what it claimed. |
| 2 | **What the learner found confusing** | Learner, in their own words | Weekly, unfiltered, no format requirement. |
| 3 | **What seemed overexplained** or wasted their time | Learner | Same form. Length is a cost, and the curriculum currently has no data on where it is spending it. |
| 4 | **Legitimate technique variants encountered** | Trainer / assessor | Feeds the "what may vary" boxes and the Human-Centered Instruction Standard. |
| 5 | **Attempts to competency** per skill | Case logs (already collected) | Validates or corrects the repetition requirements, which are currently reasoned estimates. |
| 6 | **Critical-fail frequency** by type | Assessors | A critical fail firing often means either a real hazard or a badly drawn line. Both need to be known. |
| 7 | **Assessor disagreement** | Calibration exercises + paired scoring | Where two assessors score the same performance differently, the rubric is ambiguous. |
| 8 | **Skills starved by case exposure** | Manager dashboard | Distinguishes "learner is behind" from "the schedule never gave them the case." |
| 9 | **Failed console searches** | Console search log (manual note at first) | Every failed search is a knowledge-base card that should exist. |
| 10 | **Administrative steps people routinely skip** | Honest observation | If everyone skips it, the step is wrong, not the people. |

## 3. The instruments

**Trainer end-of-shift card** (30 seconds, paper or phone):
> Learner · Module they'd completed · *What did you still have to explain?* · *Did they do anything differently that was fine?* · *Anything in the module that's just wrong?*

**Learner weekly note** (5 minutes, unstructured):
> What confused you this week? · What felt like a waste of your time? · What do you still not feel ready to do alone? · What did someone teach you that wasn't in the course?

**Assessor calibration log:** two assessors independently score the same performance; both scores recorded; any gap >2 points triggers a rubric-wording review, not a conversation about who was right.

**Fortnightly review** (30 minutes, Program Administrator + a trainer + a CVT): read everything collected, and produce a written decision on each item — fix now / fix at next release / accept as-is with reason / needs DVM. Decisions get logged; items that keep recurring without a decision are escalated.

## 4. The build gate — binding on all contributors

> **No contributor — human or AI — may author the remaining 47 skill specifications, or launch a comparable bulk content-generation pass, until at least one pilot cycle has completed and its findings have been written up.**
>
> **The single exception:** a safety-critical gap discovered during the pilot, where the absence of a specification is itself a hazard. Such a specification may be written immediately, must state on its face why it was exempted, and is logged as an exception in the build manifest.

A "pilot cycle" means: at least two learners have worked through Weeks 0–4, at least one fortnightly review has happened, and the findings exist as a document rather than as impressions.

This gate exists because content volume is the easiest thing to add and the hardest thing to unwind. The QA suite checks it.

## 5. How findings become content

The next authoring cycle is *driven* by the pilot, not merely informed by it:
- Signal 1 (what trainers still explained) sets the priority order for revising existing modules — highest-frequency gap first.
- Signal 3 (overexplained) authorises **cutting**. The next cycle is expected to remove material, not only add it. A curriculum that only ever grows is not being maintained.
- Signal 5 replaces the estimated repetition counts with observed ones.
- Signals 6 and 7 rewrite rubric language where it proved ambiguous.
- Signal 9 populates the knowledge base with the questions people actually asked.
- The remaining 47 specifications are then written to a template corrected by all of the above — and prioritised by which skills the pilot showed people actually needed and couldn't find.
