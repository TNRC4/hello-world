# Arizona Scope Matrix (Living Document)

Version 1.0 · 2026-08-17 · **Status: DRAFT — requires Medical Reviewer + regulatory verification before first use, and annual re-verification.**

## Legal foundation (verify at deployment against current law)
- **A.R.S. § 32-2211(5)** — "Exceptions from application of chapter." The veterinary-assistant exemption: a veterinary assistant **employed by a licensed veterinarian** who performs duties **other than diagnosis, prognosis, prescription or surgery** under the **direct supervision or indirect supervision** of the licensed veterinarian **who is responsible for the veterinary assistant's performance**. *Verified against azleg.gov, 2026-08-17.*
- **A.R.S. § 32-2201** — definitions that give the exemption its meaning: **direct supervision** (8) = veterinarian physically present at the location; **indirect supervision** (11) = not physically present but written or oral instructions given; **supervising veterinarian** (21); **veterinary assistant** (26). *Verified against azleg.gov, 2026-08-17.*
- **A.R.S. § 32-2281** — "Dispensing of drugs and devices; conditions; definition." Governs dispensing workflow only. **It is not an assistant-scope statute and must never be cited as one.** Earlier versions of this matrix cited it in error; see the Regulatory Research Log correction entry.

> **The exemption is a boundary, not a permission slip.** § 32-2211(5) says what an assistant may *not* do (diagnose, prognose, prescribe, perform surgery) and under whose supervision they operate. It does not authorise any particular procedure. Every RISK-TIER-2 row below must be settled by current Board rule and written CVAH policy — never by inference from this one sentence.
- **A.A.C. Title 3, Chapter 11** — Veterinary Medical Examining Board rules; **R3-11-605** governs Certified Veterinary Technician services (tasks delegated by, and under the direction/supervision/control of, a licensed veterinarian).
- Authoritative access: Arizona State Veterinary Medical Examining Board — vetboard.az.gov (Statutes & Rules page); Arizona Secretary of State Administrative Code Title 3 Ch. 11.
- Federal overlays: DEA (controlled substances — assistants may handle only within hospital's DEA-registrant procedures; logging tasks per policy), OSHA (hazard communication, sharps, anesthetic gas exposure), state radiation control for X-ray operation `[CVAH-SPECIFIC INPUT REQUIRED: confirm Arizona Bureau of Radiation Control registration requirements for operators at CVAH]`.

## Reading the matrix
Scope class and supervision codes per `Scope_Classification_System.md`. The **CVAH policy** column is the hospital's tightening of the legal ceiling — policy may restrict, never expand, legal scope. Machine-readable version: `Arizona_Scope_Matrix.csv`.

### Risk tiers — how each row was decided
| Tier | Meaning | What settles it |
|---|---|---|
| **T1** | Routine assistant work. The § 32-2211(5) exemption plus the supervision definitions genuinely answer the question. | Exemption + CVAH policy |
| **T2** | **Higher-risk. The exemption does NOT settle it.** Patient risk, delegation sensitivity, or Board-rule specificity means this row requires verification against current A.A.C. Title 3 Ch. 11 text and an explicit written CVAH policy decision before any assistant performs it. | Board rule + written policy + Medical Director sign-off |
| **T3** | Reserved by law or by CVAH to veterinarians (or CVTs where rule permits). Not an assistant task under any policy. | Statute / Board rule |

**Until a T2 row carries a dated Board-rule verification and a written CVAH policy entry, it is treated as NOT PERMITTED for assistants.** Silence is not authorisation. This is the single most important rule on the page.

## Matrix (core tasks)
| Task | Risk tier · AZ ceiling for assistant | Class | Supervision | CVAH policy |
|---|---|---|---|---|
| Patient restraint & handling | T1 · Permitted | P | S2 | Per restraint policy |
| TPR / vitals acquisition | T1 · Permitted | P | S2 | — |
| Venipuncture (sample collection) | T1 · Permitted (not surgery) | P | S2 | First 10 sticks S1 |
| IV catheter placement (peripheral) | **T2 · verify Board rule + policy** | P | S1→S2 | `[CVAH-SPECIFIC INPUT REQUIRED: confirm CVAH permits assistants; many AZ practices reserve to CVT]` |
| SQ injection (non-controlled, DVM-ordered) | T1 · Permitted | P | S2 | Dose verified by CVT/DVM |
| IM injection (DVM-ordered) | **T2 · verify Board rule + policy** | P | S1→S2 | Dose verified by CVT/DVM |
| IV push medication | **T2 · verify; treat as restricted until settled** | HP/CT | S1 | Reserved to CVT/DVM unless Medical Director authorizes specific drugs |
| Anesthesia induction (drug administration) | **T2 · verify; delegation-sensitive** | CT | S1 | Reserved to CVT/DVM |
| Anesthetic monitoring & recording | **T2 · verify supporting role scope** | P | S1 | Under CVT/DVM running anesthesia; assistant never solely responsible |
| Adjusting vaporizer/anesthetic depth | T3 · treatment alteration | DVM/CT | — | Assistant reports; never adjusts unless directly instructed in the moment by DVM/CVT present |
| Intubation | **T2 · verify; delegation-sensitive** | CT/HP | S1 | Reserved to CVT/DVM at CVAH |
| Surgical prep (clip/scrub) | T1 · Permitted | P | S2 | — |
| Sterile assistance (instrument passing) | T1 · Permitted | A/P | S1 | — |
| Suturing / surgery of any kind | T3 · Prohibited (surgery) | DVM | — | Never |
| Dental cleaning/polishing (supra-gingival, anesthetized, delegated) | **T2 · verify; Board rule governs dental procedures** | HP/CT | S1 | `[CVAH-SPECIFIC INPUT REQUIRED: Medical Director determination]` |
| Dental radiographs | T1 · Permitted | P | S2 | Radiation safety training first |
| Diagnostic radiographs (positioning/exposure) | T1 · Permitted (state radiation rules apply) | P | S2 | Dosimetry + safety module first |
| Interpreting radiographs | T3 · Diagnosis | DVM | — | Assistants flag technical quality only |
| In-house lab test performance | T1 · Permitted | P | S2 | QC per Lab Academy |
| Reporting/interpreting results to clients | T3 · Diagnosis/prognosis | DVM/CT | — | Assistants relay only DVM-approved statements |
| Filling prescriptions per DVM order (counting/labeling) | **T2 · § 32-2281 dispensing conditions apply** | P | S2 | CVT/DVM verifies before dispensing |
| Prescribing, dose selection, plan changes | T3 · Prohibited | DVM | — | Never |
| Controlled-substance log entries | **T2 · verify DEA + Board + policy** | HP | S2 | Witness signature per policy |
| Euthanasia solution administration | T3 · Prohibited for assistants | DVM (CVT only under specific conditions, per rule) | — | Never |
| CPR compressions/BLS support | T1 · Permitted | P | S1 | Per RECOVER roles |
| Cystocentesis | **T2 · verify; treat as CVT/DVM until settled** | CT | — | Assist only |
| Client education (approved scripts) | T1 · Permitted, non-diagnostic | P | S3 | Approved topics list only |

## Maintenance
**T2 rows carry a hard blocker:** none may be marked permitted for assistants until `verified_date`, `verifier`, and a written CVAH policy entry all exist in `Arizona_Scope_Matrix.csv`. The QA suite (`00_Project_Control/qa_check.py`) fails the build while any T2 row lacks them.

Annual verification against vetboard.az.gov Statutes & Rules; immediate row review on any Board rule change; every row change is a MAJOR revision requiring medical review. Research log: `Regulatory_Research_Log.md`.
