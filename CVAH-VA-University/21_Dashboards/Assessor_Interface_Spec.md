# Assessor Interface — Specification (mobile-first)

**Non-negotiable:** a full skill observation is recordable in under 60 seconds on a phone in the treatment area, or assessors will batch-falsify from memory at shift end.

**Flow 1 — Quick rep log (the 15-second path):** [Employee ▾] → [Skill ▾ recent-first] → outcome chips (Success / Unsuccessful / Aborted-stop ✓-praised) → patient-category chips → optional 1-line note → countersign PIN. Writes case-log row.
**Flow 2 — Practical assessment:** loads the PA rubric as tap-through anchored steps (2/1/0 per step, ★ marked, CF button always visible and requiring confirm + reason); auto-computes pass/fail against the rubric's rules; signature capture both parties; on fail, forces remediation-pathway selection from the catalog before closing.
**Flow 3 — State changes:** promote/restrict with evidence link auto-attached (the rubric or log range just recorded); state-10 promotions route to DVM co-sign queue; Temporarily Restricted triggers the 48 h DVM-review timer.
**Flow 4 — Countersign queue:** pending learner-entered log rows for same-shift countersign.
Implementation: launch = Moodle mobile app with Database activity forms tuned to this flow (test the 60-second standard; if it fails in practice, a simple PWA form writing to the same CSVs/DB is the sanctioned fallback — spec'd so any contractor can build it in days).
