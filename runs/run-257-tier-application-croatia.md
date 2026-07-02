---
run_id: 257
date: 2026-07-02T12:17:07Z
agent: hermes
mode: consolidation
target_country: Croatia
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 24
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/croatia.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-257-tier-application-croatia.md
proposals_created: []
completed_at: 2026-07-02T12:17:07Z
status: completed
schema_version: 2.0.0
---

# Run 257 - tier application: Croatia

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Croatia `tier: X` in `countries/croatia.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Croatia Block 1 tier wording to explain why the assignment is screening-negative for the current profile, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect six assigned tiers rather than five.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Croatia fits Tier X for the current profile because the captured DN route requires EUR 3,622.50/month before partner uplift, above the couple's current about USD 3,000/month gross income.
- Croatia is not a safe post-2027 stay plan in the current vault state because the DN route is capped at 18 months with a cooling-off period, no Croatia-specific TP-to-ordinary-residence bridge is captured, and ordinary self-employment / lump-sum craft fit remains accountant-dependent.
- This is not a final recommendation or TOP-N ranking. Croatia could be reconsidered if income rises, a post-TP or ordinary self-employment route is proven, and a Croatian accountant confirms a budget-safe craft/tax setup.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 27 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
