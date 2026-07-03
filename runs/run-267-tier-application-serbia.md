---
run_id: 267
date: 2026-07-03T19:06:54Z
agent: hermes
mode: consolidation
target_country: Serbia
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 26
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/serbia.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-267-tier-application-serbia.md
proposals_created: []
completed_at: 2026-07-03T19:06:54Z
status: completed
schema_version: 2.0.0
---

# Run 267 - tier application: Serbia

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Serbia `tier: 2` in `countries/serbia.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Serbia Block 1 tier wording to explain why the assignment is conditional-settlement, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect sixteen assigned tiers rather than fifteen.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Serbia has a plausible Tier 2 structure: visa-free Ukrainian entry, a Serbian TP layer, official electronic self-employment / independent-professional single-permit filing, up-to-3-year permits, family recognition through marriage or common-law evidence, and a 3-year PR anchor.
- The route remains conditional: no post-TP bridge is captured, APR/tax/single-permit fit and RFZO/private-insurance onboarding need adviser confirmation, conservative tax stress tests can compress the budget, and ordinary citizenship may require release from Ukrainian citizenship.
- This is not a final recommendation or TOP-N ranking. Serbia could improve if counsel confirms a clean entrepreneur / independent-professional permit and tax model; it could weaken if the household lands near the gross-base tax stress test or cannot solve address / insurance evidence cleanly.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 17 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
