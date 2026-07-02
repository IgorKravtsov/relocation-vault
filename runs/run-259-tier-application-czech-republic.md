---
run_id: 259
date: 2026-07-02T18:26:15Z
agent: hermes
mode: consolidation
target_country: Czech Republic
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 24
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/czech-republic.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-259-tier-application-czech-republic.md
proposals_created: []
completed_at: 2026-07-02T18:26:15Z
status: completed
schema_version: 2.0.0
---

# Run 259 - tier application: Czech Republic

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Czech Republic `tier: 2` in `countries/czech-republic.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Czech Republic Block 1 tier wording to explain why the assignment is conditional, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect eight assigned tiers rather than seven.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Czech Republic fits Tier 2 because the vault captures a Czech official-primary special long-term residence anchor for economically self-sufficient Ukrainian TP holders, plus status-counting toward PR and an ordinary business/self-employed fallback.
- Czechia is not Tier 1 in the current vault state because future special-residence round timing, unmarried-partner handling, business-file burden, flat-tax/trade-fit mechanics, insurance onboarding, and Prague/Brno one-income budget fit remain application-prep caveats.
- This is not a final recommendation or TOP-N ranking. Czechia could strengthen if Czech TP eligibility, future-round timing, marriage/partner mechanics, and accountant-confirmed flat-tax fit are all clean.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 25 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
