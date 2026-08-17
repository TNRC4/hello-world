# LMS Platform Analysis & Recommendation

Version 1.0 · 2026-08-17 · **Verify current pricing at deployment — SaaS tiers move.**

## Requirements recap
≤~30 learners; quizzes with randomized banks + safety-critical flag handling; prerequisites/conditional release; H5P interactives; competency tracking; mobile-usable assessor entry; reporting; certificates; export/portability; low monthly cost; maintainable by a practice manager + occasional IT help.

## Options
| Option | Fit | Cost posture (verify) | Notes |
|---|---|---|---|
| **MoodleCloud** (hosted Moodle) | Strong: quizzes/GIFT import, conditional activities, H5P built-in, Competencies module, custom certificates, mobile app | Low monthly tier for ≤50 users | Zero server maintenance; some plugin limits; branding limited on lowest tiers |
| **Self-hosted Moodle** (small VPS ~2 vCPU/4 GB) | Same features + full plugin freedom (custom certificate, Configurable Reports) | ~US$10–30/mo VPS + admin time | Needs updates/backups discipline; most portable; recommended if any staff/contractor can own patching |
| Open-source alternates (Canvas self-host, Chamilo, Opigno) | Feature-capable | Similar hosting | Smaller vet-adjacent community; Canvas self-host is heavy for this scale |
| Lightweight SaaS course tools (TalentLMS-class) | Easy authoring | Per-user fees scale poorly; weakest competency/practical tracking; export lock-in risk | Not recommended as system of record |
| Custom web app | Perfect fit theoretically | Highest build+maintain cost | Rejected: maintainability over elegance |

## Recommendation
**Moodle** (MoodleCloud to start; migrate to self-hosted later if plugin needs grow — Moodle-to-Moodle migration is routine). Rationale: only mainstream option combining question-bank randomization, conditional release, H5P, a native Competency framework (maps to passport states), free mobile app, GIFT/XML import from this repo, and full-course backup export (portability). Practical-assessment and case-log data live in Moodle Database activities at launch (or the maintained CSV registers), NOT in a proprietary add-on — keeping the passport portable per `Competency_Passport_Specification.md`.

## Vendor lock-in guardrails
Canonical content stays in this Git repo (Markdown/CSV); LMS import is generated; quarterly full-course backups (.mbz) archived; passport JSON/CSV exports monthly. The LMS is replaceable in a weekend; the content is not — so the content never lives only there.
