---
run_id: 214
date: 2026-06-26T18:06:00Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-809]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/italy.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-214-bureaucracy-practicality-italy.md
proposals_created: []
completed_at: 2026-06-26T18:06:00Z
status: completed
schema_version: 2.0.0
---

# Run 214 - bureaucracy/practicality criterion slice, Italy

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Italy, one of the remaining Tier-1-hint countries.

## What was done

- Converted Italy's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured route timing and filing-location baselines: TP applicants contact the Questura directly; DN is visa-first, then residence-permit filing at the local Questura within eight working days after arrival; the captured DN permit baseline is one year and locally renewable.
- Added one neutral professional-contact lead, Mazzeschi Legal Counsels, for immigration / citizenship / corporate-law triage.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Italy frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-809`).
- Claims added: 0; no new machine-readable critical immigration/tax claim was needed because the timing and permit-validity facts were already sourced in the Italy profile.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Italy 9.0 -> 10.0.

## Key findings

- Italy is screenable for bureaucracy/practicality but high-friction: the file hinges on a registered lease, highly specialized DN evidence, post-arrival Questura permit filing, ASL/SSN handling, tax / `partita IVA` alignment, and Italian-speaking professional support.
- TP is operationally useful for shelter/onboarding through the Questura, but it remains a poor long-term plan without a captured post-2027 conversion bridge.
- Palermo/Naples remain the practical budget-first cities; Rome is service-rich but tight; Milan is a poor default on current income.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Greece / Cyprus / Croatia / Malta unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Italy application-prep should compare Palermo/Naples/Rome local immigration lawyers and commercialisti, confirm serving-consulate DN appointment/localisation details, and capture selected-city Questura / ASL timing.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Greece / Cyprus / Croatia / Malta unless accepted proposals, verification threshold, or staleness checks take priority.
