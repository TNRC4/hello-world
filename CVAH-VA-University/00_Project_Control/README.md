# 00_Project_Control

Project-level control documents for CVAH Veterinary Assistant University.

| File | Purpose |
|---|---|
| `Executive_Overview.md` | One-page orientation for hospital leadership |
| `BUILD_MANIFEST.json` | Machine-readable manifest of every asset, its status, and review state |
| `CONTINUATION_STATE.md` | Where the build stands; what a future builder should do next |
| `CVAH_Discovery_Questionnaire.md` | Structured Phase-1 discovery instrument for hospital-specific inputs |
| `Version_Control_Policy.md` | How content is versioned, reviewed, and released |

## Ground rules for all contributors

1. Canonical content lives in this repository (Markdown/CSV/JSON), never only in the LMS.
2. No high-risk numeric clinical guidance outside `18_Controlled_References/`.
3. Every clinical module carries references (`25_References/Source_Library.md`).
4. Every change to clinical content flows through the medical review workflow (`01_University_Governance/Medical_Review_Workflow.md`).
5. `[CVAH-SPECIFIC INPUT REQUIRED]` marks the only permitted placeholders.
