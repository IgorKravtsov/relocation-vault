---
run_id: 253
date: 2026-07-01T23:58:55Z
agent: hermes
mode: consolidation
target_country: Spain
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 22
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/spain.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-253-tier-application-spain.md
proposals_created: []
completed_at: 2026-07-01T23:58:55Z
status: completed
schema_version: 2.0.0
---

# Run 253 - tier application: Spain

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger found during pre-flight, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Spain `tier: 2` in `countries/spain.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Spain Block 1 tier wording to explain why the assignment is medium-confidence and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect two assigned tiers rather than one.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Spain fits Tier 2 at screening confidence: the official international-telework route is real and partner-aware, but the absence of a captured post-2027 TP bridge, tight two-person DN income math, autonomo tax burden, and PR/citizenship counting gaps keep it below Tier 1.
- This is not a final recommendation or TOP-N ranking. Spain still carries application-prep caveats around serving-consulate proof, gestor/tax structuring, insurance, rent pressure, and Spanish-language bureaucracy.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 31 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
