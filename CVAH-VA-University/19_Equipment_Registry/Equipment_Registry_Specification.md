# CVAH Equipment Registry — Specification

Version 1.0 · 2026-08-17 · Data: `equipment_registry.csv` · Survey instrument: `Equipment_Discovery_Survey.md`

Each important clinical device gets a row and, for training-relevant devices, a one-page job aid derived from (never copying) the manufacturer's current manual, which is linked as source of truth. Fields: `eq_id, category, manufacturer, model, sw_version, serial_asset, location, purpose, manual_url_or_location, startup, shutdown, cleaning, maintenance_schedule, qc_schedule, consumables, common_errors_top5, troubleshooting_jobaid, safety_notes, competency_required (skill_id), training_module, responsible_dept, last_curriculum_review`.

Registry-driven curriculum rule: Lab Academy analyzer modules, pump job aids, imaging system workflow, dental unit care, and anesthesia machine checklists are all GENERATED against registry rows — when equipment changes, the registry row updates and flags its training module for revision (manifest linkage). The registry is reviewed quarterly by the Program Administrator.
