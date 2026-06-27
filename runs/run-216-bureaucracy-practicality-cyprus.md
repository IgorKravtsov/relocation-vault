---
run_id: 216
date: 2026-06-27T00:43:54Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-811]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/cyprus.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-216-bureaucracy-practicality-cyprus.md
proposals_created: []
completed_at: 2026-06-27T00:43:54Z
status: completed
schema_version: 2.0.0
---

# Run 216 - bureaucracy/practicality criterion slice, Cyprus

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Cyprus, one of the remaining Tier-1-hint countries.

## What was done

- Converted Cyprus's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured route timing and filing-location baselines: DN residence-permit filing is within 3 months of arrival at the Migration Department central offices in Nicosia, with an official 5-7 week examination baseline, while TP remains an ordinary bridge only until a Cyprus-specific post-2027 conversion rule appears.
- Added one neutral professional-contact lead, Michael Kyprianou Law Firm, with Nicosia / Limassol / Paphos Cyprus contact offices.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Cyprus frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-811`).
- Claims added: 0; no new machine-readable critical immigration/tax claim was needed because the DN timing, income, fee, and family facts were already sourced in the Cyprus profile.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Cyprus 9.0 -> 10.0.

## Key findings

- Cyprus is administratively screenable: the DN filing office, 3-month arrival window, 5-7 week examination baseline, fee baseline, and certified-translation burden are captured.
- The main blockers are substantive rather than procedural: the EUR 3,500/month net DN threshold is above the couple's current income, dependent coverage likely requires marriage/civil union, family members cannot work locally, and no Cyprus TP-to-ordinary-status bridge is captured.
- Larnaca / Nicosia remain the practical bases if income rises; Limassol remains a poor default on the current one-income budget.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Croatia / Malta unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Cyprus application-prep should compare independent Cyprus immigration lawyers/accountants, confirm current appointment load and exact document checklist, and capture city-specific GESY / tax / Social Insurance sequencing.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Croatia / Malta unless accepted proposals, verification threshold, or staleness checks take priority.
