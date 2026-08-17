# Arizona Scope Matrix (Living Document)

Version 1.0 · 2026-08-17 · **Status: DRAFT — requires Medical Reviewer + regulatory verification before first use, and annual re-verification.**

## Legal foundation (verify at deployment against current law)
- **A.R.S. Title 32, Chapter 21** — Arizona veterinary practice act. § 32-2281: a veterinary assistant employed by a licensed veterinarian may perform duties **other than diagnosis, prognosis, prescription, or surgery** under the **direct or indirect supervision** of the veterinarian, who is responsible for the assistant's performance.
- **A.A.C. Title 3, Chapter 11** — Veterinary Medical Examining Board rules; **R3-11-605** governs Certified Veterinary Technician services (tasks delegated by, and under the direction/supervision/control of, a licensed veterinarian).
- Authoritative access: Arizona State Veterinary Medical Examining Board — vetboard.az.gov (Statutes & Rules page); Arizona Secretary of State Administrative Code Title 3 Ch. 11.
- Federal overlays: DEA (controlled substances — assistants may handle only within hospital's DEA-registrant procedures; logging tasks per policy), OSHA (hazard communication, sharps, anesthetic gas exposure), state radiation control for X-ray operation `[CVAH-SPECIFIC INPUT REQUIRED: confirm Arizona Bureau of Radiation Control registration requirements for operators at CVAH]`.

## Reading the matrix
Scope class and supervision codes per `Scope_Classification_System.md`. The **CVAH policy** column is the hospital's tightening of the legal ceiling — policy may restrict, never expand, legal scope. Machine-readable version: `Arizona_Scope_Matrix.csv`.

## Matrix (core tasks)
| Task | AZ legal ceiling for assistant | Class | Supervision | CVAH policy |
|---|---|---|---|---|
| Patient restraint & handling | Permitted | P | S2 | Per restraint policy |
| TPR / vitals acquisition | Permitted | P | S2 | — |
| Venipuncture (sample collection) | Permitted (not surgery) | P | S2 | First 10 sticks S1 |
| IV catheter placement (peripheral) | Permitted under supervision | P | S1→S2 | `[CVAH-SPECIFIC INPUT REQUIRED: confirm CVAH permits assistants; many AZ practices reserve to CVT]` |
| SQ injection (non-controlled, DVM-ordered) | Permitted | P | S2 | Dose verified by CVT/DVM |
| IM injection (DVM-ordered) | Permitted | P | S1→S2 | Dose verified by CVT/DVM |
| IV push medication | Legal ceiling debated; treat as restricted | HP/CT | S1 | Reserved to CVT/DVM unless Medical Director authorizes specific drugs |
| Anesthesia induction (drug administration) | Delegation-sensitive | CT | S1 | Reserved to CVT/DVM |
| Anesthetic monitoring & recording | Permitted as assigned support | P | S1 | Under CVT/DVM running anesthesia; assistant never solely responsible |
| Adjusting vaporizer/anesthetic depth | Treatment alteration | DVM/CT | — | Assistant reports; never adjusts unless directly instructed in the moment by DVM/CVT present |
| Intubation | Delegation-sensitive | CT/HP | S1 | Reserved to CVT/DVM at CVAH |
| Surgical prep (clip/scrub) | Permitted | P | S2 | — |
| Sterile assistance (instrument passing) | Permitted | A/P | S1 | — |
| Suturing / surgery of any kind | Prohibited (surgery) | DVM | — | Never |
| Dental cleaning/polishing (supra-gingival, anesthetized, delegated) | Delegation-sensitive; AZ rules place dental procedures under DVM/CVT control | HP/CT | S1 | `[CVAH-SPECIFIC INPUT REQUIRED: Medical Director determination]` |
| Dental radiographs | Permitted | P | S2 | Radiation safety training first |
| Diagnostic radiographs (positioning/exposure) | Permitted | P | S2 | Dosimetry + safety module first |
| Interpreting radiographs | Diagnosis | DVM | — | Assistants flag technical quality only |
| In-house lab test performance | Permitted | P | S2 | QC per Lab Academy |
| Reporting/interpreting results to clients | Diagnosis/prognosis territory | DVM/CT | — | Assistants relay only DVM-approved statements |
| Filling prescriptions per DVM order (counting/labeling) | Permitted with verification | P | S2 | CVT/DVM verifies before dispensing |
| Prescribing, dose selection, plan changes | Prohibited | DVM | — | Never |
| Controlled-substance log entries | Permitted per DEA registrant procedure | HP | S2 | Witness signature per policy |
| Euthanasia solution administration | Prohibited for assistants | DVM (CVT only under specific conditions, per rule) | — | Never |
| CPR compressions/BLS support | Permitted | P | S1 | Per RECOVER roles |
| Cystocentesis | Needle into body cavity — treat as CVT/DVM | CT | — | Assist only |
| Client education (approved scripts) | Permitted, non-diagnostic | P | S3 | Approved topics list only |

## Maintenance
Annual verification against vetboard.az.gov Statutes & Rules; immediate row review on any Board rule change; every row change is a MAJOR revision requiring medical review. Research log: `Regulatory_Research_Log.md`.
