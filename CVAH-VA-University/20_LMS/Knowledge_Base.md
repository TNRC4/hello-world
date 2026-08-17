# Searchable University Knowledge Base — Structure

**Goal:** any staff member reaches approved how-to content in under 30 seconds, phone in hand. Nobody searches a 200-page manual.

## Architecture
Every knowledge unit is a SHORT card (≤1 screen) generated from the canonical skill specs/lessons, tagged for search. Moodle implementation: Reference Library category with the site search + tag index; each card links "full spec" for depth (layered learning). Cards carry version footers.

## Index spines (browsable without search)
1. **Skills A–Z** (from `05_*/Skills_Inventory.csv`)
2. **Equipment index** (from Equipment Registry — every device → its job aid, errors, cleaning)
3. **Troubleshooting index** — symptom-first entries: "IV catheter won't thread" · "No flash" · "Pump keeps alarming occlusion" · "Smear has no feathered edge" · "Analyzer error code ___" · "SpO2 reading but waveform ragged" · "Capnogram baseline won't zero" · "Autoclave tape turned but strip didn't"
4. **Quick-reference cards** — approved CRCs only
5. **Emergency links** — one tap: CPR card (CRC-002), emergency workflow cards (CRC-007), crash-cart checklist, activation phrasing
6. **"How do I…" seeds (launch set, grown from real staff searches):** set up a Doppler `[card after equipment survey]` · pick the right tube (TS-SAM-001 card) · position lateral abdomen (TS-IMG-001 card) · open a sterile pack (TS-SUR-STER-001 card) · read this capnogram pattern (INT-A3 index) · clean the [analyzer] (registry job aid) · handle a controlled-substance discrepancy (PHA-M4 card) · what does this ECG artifact mean (ANE-M3 card)

## Tagging standard
Every card: `skill:<ID>` `equipment:<EQ-ID>` `domain:<VEN|IVC|...>` `type:<howto|troubleshoot|reference|emergency>` `audience:<all|specialty>`. Search-log review monthly: failed searches become new cards (the KB grows toward real questions).
