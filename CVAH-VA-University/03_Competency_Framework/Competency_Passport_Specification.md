# Digital Competency Passport — Specification

Version 1.0 · 2026-08-17

The Passport is the structural backbone of the University: one living record per employee, one row per skill, moving through controlled states with full audit history.

## Skill states (canonical, in order)
| # | State | Entered when | Set by |
|---|---|---|---|
| 1 | Not Introduced | default | system |
| 2 | Theory Assigned | lesson assigned | system/admin |
| 3 | Theory Complete | knowledge check passed | LMS (auto) |
| 4 | Demonstration Observed | learner watched live demo, logged | Supervising Tech |
| 5 | Practicing With Direct Supervision | first coached attempts (S1) | Supervising Tech |
| 6 | Repetition Requirement In Progress | case log accruing | system (from logs) |
| 7 | Practical Assessment Ready | reps met + trainer flags ready | Supervising Tech |
| 8 | Practical Assessment Passed | rubric passed, no critical fails | Assessor |
| 9 | Competent Under Defined Supervision | post-assessment consolidation period per skill spec | Assessor |
| 10 | Independently Assignable Within Hospital Policy | Assessor + DVM co-sign; supervision level per scope matrix (never legal independence) | Assessor + DVM |
| 11 | Remediation Required | failed assessment / flagged unsafe / decay detected | Assessor/Manager/DVM |
| 12 | Revalidation Due | interval elapsed (per skill spec) | system |
| 13 | Temporarily Restricted | safety concern pending review | any DVM; Assessor pending DVM review ≤48 h |
| 14 | Competency Expired | revalidation window lapsed | system |

Transitions 8→9→10 are promotions; 11/13 can be entered from any state ≥5; 12/14 only from 9–10. Every transition records: timestamp, actor, evidence link (rubric ID, case-log range, quiz attempt), and comment. States 11 and 13 always carry a linked remediation plan (`23_Remediation/`).

## Supervision explicitness rule
A passport row never says just "competent." It always displays: **state + supervision level (S1/S2/S3) + scope class + any CVAH policy condition** — e.g., "TS-VEN-CEPH-001 · State 10 · S2 · P · routine canine/feline draws." The word "independent" appears only inside the fixed phrase "Independently Assignable Within Hospital Policy."

## Data model (JSON)
```json
{
  "employee_id": "E-0042",
  "name": "…",
  "hire_date": "2026-09-01",
  "va_level": "VA2",
  "passport": [
    {
      "skill_id": "TS-VEN-CEPH-001",
      "state": 9,
      "supervision": "S2",
      "scope_class": "P",
      "granted_by": "assessor:E-0007",
      "granted_date": "2026-10-12",
      "reps": {"observed": 4, "assisted": 6, "successful": 12, "unsuccessful": 3},
      "revalidation_due": null,
      "history": [{"ts": "...", "from": 8, "to": 9, "actor": "E-0007", "evidence": "PA-VEN-CEPH-001#a7f2", "note": ""}]
    }
  ]
}
```

## Implementation
Phase 1 (launch): Moodle custom-certificate + Database activity, or the maintained spreadsheet register `16_Case_Logs/passport_register.csv` — one row per employee-skill, mirrored weekly to the repo. Phase 2: Moodle Competency framework import (`20_LMS/moodle_competency_framework.csv` mapping states to Moodle competency scales). The JSON schema above is the portability contract either way.
