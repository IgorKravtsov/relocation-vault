---
run_id: 265
date: 2026-07-03T12:52:04Z
agent: hermes
mode: consolidation
target_country: Slovenia
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 24
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/slovenia.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-265-tier-application-slovenia.md
proposals_created: []
completed_at: 2026-07-03T12:52:04Z
status: completed
schema_version: 2.0.0
---

# Run 265 - tier application: Slovenia

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Slovenia `tier: 2` in `countries/slovenia.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Slovenia Block 1 tier wording to explain why the assignment is conditional-settlement, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect fourteen assigned tiers rather than thirteen.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Slovenia has a plausible Tier 2 settlement structure: TP through 04 March 2027, an official 10-day post-TP filing window, DN bridge, self-employed / single-permit and family routes, and 5-year PR / 10-year citizenship anchors.
- The route remains conditional: DN is one-year and non-renewable, the current income formula screens above the couple's USD 3,000/month profile, and the durable plan requires ordinary-status transition plus accountant / lawyer confirmation.
- This is not a final recommendation or TOP-N ranking. Slovenia could improve if income rises, accepted savings cover the DN means test, or advisers confirm a clean self-employed/status transition; it could weaken if tax / insurance costs stay near the conservative stress test.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 19 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
