# Controlled Clinical Reference System

Version 1.0 · 2026-08-17

## The rule
General education teaches concepts and reasoning. **All high-risk numeric clinical guidance** — vital-sign bands, alert thresholds, CPR numbers, equipment settings, emergency workflows, medication references — lives ONLY on versioned Controlled Reference Cards (CRCs), each approved by the reviewing veterinarian. Lessons cite card IDs, never re-state their numbers. This prevents unversioned numbers from fossilizing across hundreds of pages.

## Card anatomy (mandatory header on every card)
`CRC-ID · Title · Version · Approval date · Reviewing veterinarian (signature) · Sources · Next review date · Revision history`. A card past its next-review date auto-flags EXPIRED: dashboards show it, laminated copies are pulled by the Program Administrator, and the LMS displays the expiry banner.

## Card register (`crc_register.csv`)
| ID | Title | Status |
|---|---|---|
| CRC-001 | TPR & vital-sign normal bands (canine/feline, by life stage) | DRAFT — PENDING DVM APPROVAL |
| CRC-002 | CPR quick reference (RECOVER 2024-aligned) | DRAFT — PENDING DVM APPROVAL |
| CRC-003 | Anesthesia monitoring alert thresholds (per-case defaults) | DRAFT — PENDING DVM APPROVAL |
| CRC-004 | Fluid-rate references | NOT DRAFTED — `[CVAH-SPECIFIC INPUT REQUIRED: house protocol]` |
| CRC-005 | Crash-cart contents & audit checklist | DRAFT — PENDING DVM APPROVAL |
| CRC-006 | Disinfectant products, dilutions, contact times | NOT DRAFTED — from house products |
| CRC-007 | Emergency workflow cards (GDV/block/seizure/heat) | DRAFT set in ECC-M4 — PENDING |

**No card is used clinically before approval.** Draft cards carry a diagonal DRAFT watermark. Printed copies are numbered; superseded prints destroyed on release of a new version.
