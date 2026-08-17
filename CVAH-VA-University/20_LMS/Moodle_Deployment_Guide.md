# Moodle Deployment Guide

Version 1.0 · 2026-08-17

## 1. Provision
MoodleCloud: create site (smallest tier ≥ user count), enable H5P (built-in), mobile app on. Self-host: Ubuntu LTS VPS, standard Moodle install per moodle.org docs, HTTPS via Let's Encrypt, nightly backup cron (site + DB) to offsite storage.

## 2. Structure (mirrors `Course_Structure_Map.md`)
Course categories: `Core VA Academy` (one course per week, W0–W8) · `Specialty Academies` (one course each ×7) · `Reference Library` (knowledge base + CRC display) · `Assessor Tools`. Site-wide roles: Learner, Trainer (Supervising Tech), Assessor (grading + database entry rights), Manager (report viewing), Admin.

## 3. Content import pipeline
Lessons: Markdown → Moodle Pages/Books (pandoc `md → html`, paste or web-service upload; keep the repo file as canonical — the page carries a footer "source: <repo path> vX.Y"). Question banks: convert `14_Question_Banks/QB-*.md` to GIFT with the conversion script pattern (each `### ID |` block → one GIFT item; category per file; safety-critical items tagged `SC`). Quizzes: build per blueprint, random-draw from categories, SC items force-included; "100% on SC" implemented as a separate mini-quiz section requiring 100% (Moodle-native way to enforce the two-bar standard). Interactives: build per `Interactive_Content_Specs.md` in H5P (drag-drop, hotspot, branching scenario types). Certificates: Custom Certificate plugin (self-host) or tier feature, with the internal-credential disclaimer text block mandatory.

## 4. Conditional release wiring
Week N course visible on Week N-1 completion OR challenge-out flag; floor-practice "lessons" are checklist activities marked complete by Trainers only; PA results entered by Assessors in the Competency framework (scale: the 14 passport states) — activity completion never auto-grants practical states.

## 5. Passport & logs
Import `20_LMS/moodle_competency_framework.csv` (one competency per skill ID, scale = passport states). Case logs: Database activity per loggable skill with the `case_log_template.csv` fields; weekly CSV export to repo `16_Case_Logs/exports/`.

## 6. Go-live checklist
[ ] CRC drafts approved by DVM before Reference Library opens · [ ] scope matrix verified + policy column completed · [ ] two pilot learners run Week 0–1 end-to-end · [ ] assessor mobile entry tested in treatment area wifi dead-zones `[CVAH-SPECIFIC INPUT REQUIRED: wifi coverage]` · [ ] backup restore TESTED once · [ ] analytics baseline captured (pre-launch technician task-time snapshot for the transfer metrics).
