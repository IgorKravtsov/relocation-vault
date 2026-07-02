---
run_id: 260
date: 2026-07-02T21:30:04Z
agent: hermes
mode: consolidation
target_country: Poland
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 24
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/poland.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-260-tier-application-poland.md
proposals_created: []
completed_at: 2026-07-02T21:30:04Z
status: completed
schema_version: 2.0.0
---

# Run 260 - tier application: Poland

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Poland `tier: 1` in `countries/poland.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Poland Block 1 tier wording to explain why the assignment is user-specific, medium-confidence, and non-ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect nine assigned tiers rather than eight.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Poland fits Tier 1 for this couple because one partner already has a Polish `karta pobytu`, the captured family-reunification baseline becomes practical if the couple marries, and the CUKR card gives eligible Ukrainian TP holders a 3-year post-TP residence bridge with work / business rights.
- The assignment remains medium-confidence because ordinary post-CUKR renewal, exact PR/citizenship counting, ZUS and IT `ryczalt` classification, VAT/reverse-charge handling, Polish-language integration, and one-income city budget fit remain application-prep caveats.
- This is not a final recommendation or TOP-N ranking. Poland could weaken if CUKR eligibility does not apply to the couple or if ZUS/tax and family-reunification practice materially compress the budget.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 24 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
