---
run_id: 258
date: 2026-07-02T15:21:16Z
agent: hermes
mode: consolidation
target_country: Malta
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 22
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/malta.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-258-tier-application-malta.md
proposals_created: []
completed_at: 2026-07-02T15:21:16Z
status: completed
schema_version: 2.0.0
---

# Run 258 - tier application: Malta

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Malta `tier: X` in `countries/malta.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Malta Block 1 tier wording to explain why the assignment is screening-negative for the current profile, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect seven assigned tiers rather than six.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Malta fits Tier X for the current profile because the captured NRP remote-work route requires EUR 42,000/year gross, above the couple's current about USD 3,000/month gross income.
- Malta is not a safe post-2027 stay plan in the current vault state because the NRP explicitly does not lead to long-term residence or citizenship, no Malta-specific TP-to-ordinary-residence bridge is captured, and the ordinary fallback remains tax/rent-tight.
- This is not a final recommendation or TOP-N ranking. Malta could be reconsidered if income rises above the NRP threshold or a countable ordinary Maltese status is proven.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 26 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
