---
run_id: 264
date: 2026-07-03T09:47:51Z
agent: hermes
mode: consolidation
target_country: Slovakia
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 23
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/slovakia.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-264-tier-application-slovakia.md
proposals_created: []
completed_at: 2026-07-03T09:47:51Z
status: completed
schema_version: 2.0.0
---

# Run 264 - tier application: Slovakia

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Slovakia `tier: 2` in `countries/slovakia.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Slovakia Block 1 tier wording to explain why the assignment is conditional-settlement, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect thirteen assigned tiers rather than twelve.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Slovakia has a plausible Tier 2 settlement structure: TP through 04 March 2027, ordinary business/self-employed residence, spouse-based family reunification, and a captured 5-year long-term-residence anchor.
- The route remains conditional: no captured post-TP bridge or DN route, business-plan / real-business scrutiny, adviser-confirmed SZCO / tax / VAT / insurance fit, and disciplined non-Bratislava budgeting are all material.
- This is not a final recommendation or TOP-N ranking. Slovakia could improve if counsel confirms the foreign-client IT business file and accountant guidance confirms the favorable SZCO model; it could weaken if the route is treated as insufficiently real for a remote contractor.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 20 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
