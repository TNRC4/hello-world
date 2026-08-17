# Manager Readiness Dashboard — Specification

Answers the staffing questions directly; every view exportable.

**View 1 — Capability matrix (the core view):** rows = staff, columns = key workload rows from the Ownership Matrix (blood draws, IV catheters, surgical prep, imaging, anesthesia support, emergency roles, inpatient tier); cells = passport-state color (green ≥10, teal 9, blue 5–8 "in training", amber 11/13, red 12/14, gray untrained) with supervision level letter. One glance = "who can draw blood today and under what supervision."
**View 2 — Individual drill-down:** full passport, case-log trends, time-in-training vs cohort bands, current gates outstanding, remediation history (manager-only), exposure diagnosis panel: reps-needed vs case-opportunities-offered (answers "is lack of case exposure the limiting factor?" — if offered-cases < needed, the constraint is scheduling, not the learner).
**View 3 — Team gaps & risk:** coverage counts per capability per shift template ("Tuesday PM: 0 signed IV-catheter assistants scheduled"); expiring competencies 60-day horizon; skill-decay flags (no logged reps in threshold window); Contribution Index per staff member and team aggregate (22_Analytics spec).
**View 4 — Program health:** time-to-VA1/VA2/graduation distributions; first-time practical pass rates; remediation effectiveness (pass-after-remediation rate); operational transfer metrics (% draws/catheters/preps by assistants; technician minutes returned; retake/sample-error/setup-error rates).
Alert rules: expired safety-critical competency → manager + employee notification + auto state-14; learner >2 weeks with no state progression → exposure-diagnosis prompt; failed practical → remediation-assigned confirmation required within 48 h.
