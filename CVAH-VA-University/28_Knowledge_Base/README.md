# 28_Knowledge_Base

Learner- and staff-facing quick-answer content, authored here and **rendered** by the console builder.

| File | Purpose |
|---|---|
| `Troubleshooting_Index.json` | Symptom-first index: "no flash", "won't thread", "pump alarming". 24 entries, each tracing to a source document section and carrying its own review state. |

## The rule this directory exists to enforce

**The renderer renders. It does not author.**

Until 2026-08 the troubleshooting entries lived inside `build_console.py` as Python string literals. That made a build script a second source of clinical truth — invisible to reviewers, outside the medical-review workflow, and impossible to audit alongside the curriculum. Any clinically meaningful statement now lives in a reviewable data file with:

- `source_document` and `source_section` — where the statement comes from, so it can be checked against the curriculum and cannot silently drift from it
- `review_status` — `pending_human_review` or `approved`
- `medical_review_required` — true for anything giving clinical technique direction
- `last_reviewed` and `reviewer` — filled by a person, never by a script

Entries that are not `approved` render with a visible pending-review marker. `qa_check.py` fails the build if any entry's `source_document` does not exist, and reports the count of unreviewed entries.

**Current state: 24 entries, all `pending_human_review`, 22 requiring medical review.** They are accurate to the source courses and safe to teach from, but no CVAH clinician has yet signed them.
