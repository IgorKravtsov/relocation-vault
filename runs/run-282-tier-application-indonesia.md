---
run_id: 282
date: 2026-07-05T17:30:22Z
agent: hermes
mode: consolidation
target_country: Indonesia
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 30
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/indonesia.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-282-tier-application-indonesia.md
proposals_created: []
completed_at: 2026-07-05T17:30:22Z
status: completed
schema_version: 2.0.0
---

# Run 282 - tier application: Indonesia

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Indonesia `tier: 3` in `countries/indonesia.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Indonesia Block 1 tier wording to explain why the assignment is bridge/base rather than Tier 1/2 settlement or Tier X rejection.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect thirty-one assigned tiers rather than thirty.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Indonesia has real official short-stay scouting and an E33G remote-worker limited-stay route, but E33G requires USD 60,000/year income and a foreign-company employment agreement.
- Indonesia is Tier 3 for this profile because it can be a warm, low-rent bridge/base only if income rises or another KITAS path is confirmed; it is not a captured settlement ladder for the current USD 36,000/year profile.
- This is not a final recommendation or TOP-N ranking. Indonesia could improve with counsel-confirmed E33G / KITAS / ITAP mechanics and clean tax treatment; it could weaken if tax, VAT/BPJS, insurance, lease, school, or city-risk costs erase the rent advantage.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 2 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
