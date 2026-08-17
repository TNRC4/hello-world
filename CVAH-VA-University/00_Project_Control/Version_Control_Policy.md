# Version Control Policy

## Repository as source of truth
All curriculum, assessment, rubric, and reference content is authored in this Git repository. The LMS is a delivery layer only; LMS content is generated/imported from these files.

## Versioning
- Every learner-facing document carries a version block: `Version | Date | Author role | Medical reviewer | Change summary`.
- Semantic scheme: MAJOR (clinical meaning changed — requires medical re-review), MINOR (new content, same clinical meaning), PATCH (typo/format).
- Controlled Reference Cards additionally carry approval date, reviewing veterinarian, and next review date; an expired card is automatically pulled from circulation (see `18_Controlled_References/Controlled_Reference_System.md`).

## Branching
- `main` = approved, deployable content.
- `review/*` = content awaiting medical review.
- Emergency clinical corrections (patient-safety errors) may go straight to `main` with same-day veterinarian review, logged in the manifest.

## Release cadence
Quarterly content releases; emergency releases any time medicine, equipment, regulation, or hospital policy changes (see `24_Revalidation/Revalidation_Program.md`).
