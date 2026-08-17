# University Transcript — Specification

Version 1.0 · 2026-08-17

One transcript per employee; exportable to PDF for personnel files (LMS certificate/report export or the `21_Dashboards/` report generator).

## Sections (in order)
1. **Header:** employee name/ID, hire date (if supplied), current VA level, Core status, generation date, and the internal-credential disclaimer (verbatim from `01_University_Governance/Credential_Definitions.md`).
2. **Level history:** VA1/VA2/Core Graduate/VA3 with grant dates and signatories.
3. **Specialty credentials:** credential, grant date, revalidation due date, status (current/expired).
4. **Practical competencies:** every passport row at state ≥8: skill ID, name, state, supervision level, grant date, revalidation date.
5. **Completed modules:** module ID, title, best score, completion date.
6. **Continuing education:** refreshers and revalidations completed.
7. **Remediation history:** included on the HR/manager export only, summarized as episodes with outcomes; excluded from the learner's shareable copy.
8. **Case-log summary:** per loggable skill — attempts, successes, patient-type spread.

Data sources: passport JSON + LMS gradebook + case-log CSVs. All fields exist in those systems; the transcript is a report, never a separate database.
