---
run_id: 263
date: 2026-07-03T06:43:02Z
agent: hermes
mode: consolidation
target_country: Hungary
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 24
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/hungary.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-263-tier-application-hungary.md
proposals_created: []
completed_at: 2026-07-03T06:43:02Z
status: completed
schema_version: 2.0.0
---

# Run 263 - tier application: Hungary

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Hungary `tier: X` in `countries/hungary.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Hungary Block 1 tier wording to explain why the assignment is current-profile screening-negative, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect twelve assigned tiers rather than eleven.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Hungary has real short/medium-term route scaffolding: TP through the EU horizon, OIF White Card and guest-self-employment pages, a National Residence Card framework, acceptable safety/English proxies, and Debrecen/Pecs rent screens.
- The route blockers are material: no captured post-2027 TP bridge, White Card income is above the current budget and cannot sponsor family, guest self-employment is evidence-heavy and capped at three years total, and conservative tax/contribution modelling can erase the rent advantage.
- This is not a final recommendation or TOP-N ranking. Hungary could improve if income rises, the woman has independent status, or professional advice confirms a durable guest-self-employment / tax / healthcare file.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 21 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
