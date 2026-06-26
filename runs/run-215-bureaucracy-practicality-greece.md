---
run_id: 215
date: 2026-06-26T21:40:44Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-810]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/greece.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-215-bureaucracy-practicality-greece.md
proposals_created: []
completed_at: 2026-06-26T21:40:44Z
status: completed
schema_version: 2.0.0
---

# Run 215 - bureaucracy/practicality criterion slice, Greece

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Greece, one of the remaining Tier-1-hint countries.

## What was done

- Converted Greece's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured route timing and filing-location baselines: Greek TP holders can use the electronic Immigration Code switch before 04 March 2027 without an entry visa; the DN route is consular, has a 10-day response baseline, starts with a one-year visa, and can lead to a two-year renewable residence permit.
- Added one neutral professional-contact lead, Immigration Greece / lawyersgreece.eu, for immigration-law triage.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Greece frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-810`).
- Claims added: 0; no new machine-readable critical immigration/tax claim was needed because the core TP/DN timing facts were already sourced in the Greece profile.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Greece 9.0 -> 10.0.

## Key findings

- Greece is procedurally promising for bureaucracy/practicality because the TP-to-Immigration-Code bridge is explicit, electronic, and available before 04 March 2027 for Greek TP holders.
- The fresh DN path remains consular and income-gated; the family threshold is above the couple's current one-income budget.
- Practical friction remains Greek-language administration, translations, private insurance, tax / EFKA / VAT setup, and adviser quality, with Thessaloniki / Patras still the safer budget bases than Athens or tourist-market Crete.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Cyprus / Croatia / Malta unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Greece application-prep should compare independent Athens / Thessaloniki immigration lawyers and accountants, confirm serving-consulate DN appointment/localisation details, and capture exact e-portal / municipality / AADE / EFKA timing for the final route.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Cyprus / Croatia / Malta unless accepted proposals, verification threshold, or staleness checks take priority.
