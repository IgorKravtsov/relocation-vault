---
run_id: 213
date: 2026-06-26T15:29:02Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-808]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/portugal.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-213-bureaucracy-practicality-portugal.md
proposals_created: []
completed_at: 2026-06-26T15:29:02Z
status: completed
schema_version: 2.0.0
---

# Run 213 - bureaucracy/practicality criterion slice, Portugal

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale claims.
- Continue the 5.11 bureaucracy/practicality slice with Portugal, the lowest-depth remaining Tier-1-hint country.

## What was done

- Converted Portugal's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured route timing and filing-location baselines: Ukraine TP is a shelter/onboarding route without a captured SLA; the remote-worker path is D8 visa first, then AIMA residence authorization with a two-year initial permit and three-year renewals.
- Added one neutral professional-contact lead, Global Citizen Solutions in Lisbon, for D8 / residence-file triage.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Portugal frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-808`).
- Claims added: 0; no new machine-readable critical immigration/tax claim was needed because the core permit validity was already sourced in the country profile.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Portugal 8.0 -> 9.0.

## Key findings

- Portugal is screenable for bureaucracy/practicality but less deterministic than Spain: the post-visa AIMA route is official, while exact appointment capacity and consular microdetails remain application-prep.
- The practical blockers are not just paperwork: D8 income above the current budget, NIF / bank / lease setup, address proof, Portuguese tax/social-security registration, and lawyer/accountant execution quality.
- TP remains useful as near-term shelter/onboarding but should not be modeled as a proven post-2027 ordinary-status bridge.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Italy / Greece / Cyprus / Croatia / Malta unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Portugal application-prep should compare independent immigration lawyers and accountants, confirm serving-consulate D8 appointment/localisation details, and capture live NIF / bank / AIMA / lease timing.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with the remaining Tier-1 countries unless accepted proposals, verification threshold, or staleness checks take priority.
