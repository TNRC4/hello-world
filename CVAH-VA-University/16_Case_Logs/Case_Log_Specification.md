# Case Logs & Repetition Tracking

## Purpose
One successful performance proves luck; logged consistency across patient variation proves competency. Logs are the evidence layer for passport states 6→10 and revalidation decay rules.

## Log entry schema (per attempt) — `case_log_template.csv`
`log_id, date, employee_id, skill_id, role (observed|assisted|performed), patient_species, patient_category (routine|small<5kg|geriatric|dehydrated|fractious|critical-adjacent), attempts_this_patient, outcome (success|unsuccessful|aborted-stop-criteria), complications (none|hematoma|infiltration|stress-stop|equipment|other:note), supervisor_id, supervision_level (S1|S2), feedback_note, countersigned (Y|N)`

## Rules
1. EVERY attempt is logged, unsuccessful and aborted included — an aborted-at-stop-criteria entry is evidence of competence, not failure.
2. Supervisor countersigns entries at states ≤8 (same shift).
3. The system computes rolling success rate, patient-category spread, and recency; passports auto-flag Revalidation Due on decay rules (per skill spec).
4. Falsified log = integrity violation per governance doc.

## Implementation
Launch: printed pocket cards (template `case_log_card_print.md`) transcribed same-day to the shared register CSV / Moodle Database activity; assessor mobile entry per `21_Dashboards/Assessor_Interface_Spec.md`. The CSV schema above is canonical either way.
