# CVAH Veterinary Assistant University — Executive Overview

**Learn it. Practice it. Prove it. Use it.**

Version 1.0 · Build date 2026-08-17 · Status: Initial complete build, pending CVAH medical review

---

## What this is

CVAH Veterinary Assistant University (CVAH-VAU) is a complete internal education, competency-management, and workforce-readiness system for Chino Valley Animal Hospital. It takes a new hire with little or no clinical veterinary experience and produces — in approximately 6–8 weeks — a safe, technically useful, general-practice veterinary assistant, then continues developing that person through seven stackable specialty academies.

It is **not** an onboarding packet. It is simultaneously:

1. **A university** — one Core Academy plus seven specialty academies, each with structured lessons, cases, and examinations.
2. **A skills lab** — a Technical Skills Library where every hands-on skill is a first-class object with its own instruction, checklist, rubric, repetition requirement, and sign-off process.
3. **A competency-management system** — a Digital Competency Passport tracking every skill through 14 controlled states from *Not Introduced* to *Independently Assignable Within Hospital Policy*.
4. **A clinical reference library** — a searchable knowledge base plus version-controlled, veterinarian-approved Controlled Reference Cards for all high-risk numeric guidance.
5. **A specialty-training platform** — Perioperative & Anesthesia, Laboratory & IDEXX, Dentistry Support, Diagnostic Imaging, Emergency & Critical Care Support, Inpatient Care, and Pharmacy & Medication Handling.
6. **A workforce-readiness system** — manager dashboards, a Clinical Workload Ownership Matrix, and a Contribution Index that answer, at a glance, "who can safely do what for us today?"

## The organizing principle

Every element answers one question:

> **What appropriate clinical workload can this employee safely and reliably take off another team member's plate after mastering this competency?**

Graduation is competency-based, never calendar-based. Every significant skill requires the learner to pass the Three Questions of Competence:

1. **Can you explain it?** (knowledge assessment)
2. **Can you do it?** (observed practical assessment with defined critical-fail behaviors)
3. **Can you recognize when it is not going correctly?** (failure-recognition, complication, and escalation assessment)

## Structure at a glance

| Component | Content |
|---|---|
| Core VA Academy | 9-week shell (Week 0–8) targeting 6–8 week completion; ~30 lessons; high-practice weeks 3–4 |
| VA1 / VA2 / VA3 | Competency milestones, not courses — defined in `03_Competency_Framework/VA_Levels.md` |
| Technical Skills Library | 100+ inventoried skills; full structured specifications for all safety-critical core skills |
| Assessment system | Diagnostic pretest, per-lesson checks, module quizzes, ~300-item question banks, cumulative final, 13-station graduation practical |
| Specialty academies | 7 post-core credentials with own syllabi, exams, practical assessments, case requirements |
| Governance | Arizona scope matrix (A.R.S. § 32-2281; A.A.C. R3-11), medical review workflow, controlled references, revalidation program |
| Delivery | Moodle-based LMS deployment package; all canonical content kept portable in Markdown/CSV/JSON in this repository |

## What CVAH must supply before go-live

The build is generalizable and deployable now, but the following require local confirmation (flagged `[CVAH-SPECIFIC INPUT REQUIRED]` throughout): installed analyzer/imaging equipment models, hospital-specific protocols and numeric thresholds (all Controlled Reference Cards require reviewing-veterinarian sign-off before use), staffing/assessor assignments, and the completed Discovery Questionnaire in `00_Project_Control/CVAH_Discovery_Questionnaire.md`.

## Cost posture

Recommended stack: MoodleCloud Starter/Mini tier or self-hosted Moodle on a small VPS (~US$10–30/month), H5P for interactives, this Git repository as the canonical content source. No enterprise software. See `20_LMS/LMS_Platform_Analysis.md`.
