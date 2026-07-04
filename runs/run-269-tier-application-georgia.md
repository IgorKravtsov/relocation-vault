---
run_id: 269
date: 2026-07-04T01:14:50Z
agent: hermes
mode: consolidation
target_country: Georgia
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 29
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/georgia.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-269-tier-application-georgia.md
proposals_created: []
completed_at: 2026-07-04T01:14:50Z
status: completed
schema_version: 2.0.0
---

# Run 269 - tier application: Georgia

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Georgia `tier: 2` in `countries/georgia.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Georgia Block 1 tier wording to explain why the assignment is conditional-settlement, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect eighteen assigned tiers rather than seventeen.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Georgia has a plausible Tier 2 structure: easy entry / scouting, an official SDA IT residence-permit route with a USD 25,000/year remuneration anchor, family residence after the main permit, a favorable small-business tax screen if confirmed, and workable Tbilisi / Batumi / Kutaisi cost and rent baselines.
- The route remains conditional: visa-free stay is not residence, Georgia is outside the EU temporary-protection bridge framework, IT / small-business / VAT / pension mechanics need Georgian adviser confirmation, healthcare onboarding remains partial, and PR / ordinary citizenship are long 10-year clocks.
- This is not a final recommendation or TOP-N ranking. Georgia could improve if counsel and an accountant confirm a clean IT / small-business permit and renewal file; it could weaken if the tax route falls back to 20% PIT or if insurance, rent, or family sequencing compresses the one-income margin.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 15 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
