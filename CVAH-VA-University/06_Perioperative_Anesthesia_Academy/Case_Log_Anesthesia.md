# Anesthesia Case Log — Extended Schema & Variety Requirements

Version 1.0 · Ten identical dog neuters are one case, experienced ten times. Variety is the exposure that builds monitors. Schema (extends `16_Case_Logs/case_log_template.csv`):

`log_id, date, employee_id, tier_role (T2-support|T3-monitor|recorder), species, age_category (pediatric|adult|senior|geriatric), breed_class (brachycephalic|sighthound|toy|standard|giant), procedure, procedure_class (routine-sx|dental|emergency-sx|imaging-sedation|other), asa_class_as_stated_by_DVM, duration_min, circuit_type, monitoring_used (spo2;etco2;ecg;osc-bp;doppler;temp), abnormal_events (none|hypotension-trend|bradycardia|tachycardia|desat-event|etco2-event|artifact-resolved|recovery-event|other:note), troubleshooting_performed, reports_made (count + were any report-now), recovery_involvement (none|observed|sitter), anesthetist_id, countersigned, feedback_note`

## Variety requirements for T3 (within the 15-case log)
≥2 feline · ≥1 pediatric or geriatric · ≥1 brachycephalic (or documented case-mix substitution: sim SIM-ANES-011 + anesthetist attestation) · ≥1 dental ≥60 min · ≥1 case with a real abnormal-event entry (they happen; logging them honestly is the requirement) · ≥3 procedure classes · ≥5 recovery involvements including ≥2 as sitter. The manager's exposure-diagnosis panel reads this table: if case-mix starves a learner of a category, the SCHEDULING fixes it (assign them to Tuesday dentals), not the standard.
