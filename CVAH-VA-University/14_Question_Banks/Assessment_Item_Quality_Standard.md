# Assessment Item Quality Standard (Anti-Giveaway Design)

Binding for every item, existing and future. Enforced by the scripted audit (`00_Project_Control/qb_audit.py`) plus the human checks below. An item failing any check is rewritten before entering a pool.

## Construction rules
1. **Length parity:** options of comparable length; the key is never systematically the longest or the most nuanced. When the correct action genuinely needs words, distractors get equal structural weight.
2. **Position balance:** keys distributed across A–D per bank (no position >35%); LMS shuffling enabled where order isn't meaningful.
3. **Plausible distractors only:** every wrong option is a real novice error, wrong prioritization, right-action-wrong-time, unverified-finding jump, or near-miss concept from the skill's Common Rookie Mistakes / failure modes. No absurd filler. Target: an underprepared learner hesitates; a prepared one can say *why* it's wrong.
4. **No linguistic tells:** no lesson-verbatim phrasing only in the key; no safety-vocabulary monopoly ("verify/assess/escalate") in keys while distractors sound reckless; no grammatical pointers; absolutes (always/never/only) permitted in wrong options only when the taught rule genuinely uses them (e.g., recap = never IS the rule — allowed).
5. **Safest-sounding ≠ shortcut:** for judgment items, ≥2 options must sound safe; case details decide. The "call the DVM" option must sometimes be wrong (right answer = a 5-second physical check first) and sometimes right — unpredictably.
6. **No tricks:** difficulty from clinical discrimination (artifact vs deterioration, flash vs seated catheter, contamination vs acceptable), never from syntax, double negatives, untaught exceptions, or trivia. No default all/none-of-the-above.
7. **Best-answer stems** ("FIRST / BEST next / MOST concerning") whenever multiple options hold some validity; the explanation must say why the tempting options lose *in this case*.
8. **Cognitive levels:** tag L1 recall → L5 integrated reasoning. Core exams ≥50% L3–4; specialty/technician exams ≥40% L4–5. L1 never dominates a bank.
9. **Distractor teaching:** flagship banks (VEN, IVC, MED, ANES) explain the principal distractors, not just the key.
10. **Parallel items:** each important objective gets variants across patients/contexts so retakes test the concept, not question 17's letter.

## Review gates
- **Blind test-taker check** (per bank sample): could a test-wise non-veterinary reader find keys via length/tone/pattern/absurd-elimination? If yes → rewrite.
- **Expert ambiguity check** (advanced banks): could an experienced professional defend two options with the information given? If yes → add case detail, sharpen the asked priority, or accept multiple keys. Difficulty ≠ ambiguity.
- **Post-deployment item analytics** (LMS): flag near-100%-correct "hard" items, negative discriminators, never-chosen distractors; revise quarterly.

## Feedback modes
Practice mode: immediate explanations. Graded quizzes: feedback after submission. Finals: review per assessment policy only. Never leak explanations mid-attempt.
