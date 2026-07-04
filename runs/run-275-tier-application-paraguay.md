---
run_id: 275
date: 2026-07-04T19:54:43Z
agent: hermes
mode: consolidation
target_country: Paraguay
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 30
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/paraguay.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-275-tier-application-paraguay.md
proposals_created: []
completed_at: 2026-07-04T19:54:43Z
status: completed
schema_version: 2.0.0
---

# Run 275 - tier application: Paraguay

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Paraguay `tier: 2` in `countries/paraguay.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Paraguay Block 1 tier wording to explain why the assignment is conditional ordinary-residence / Latin America settlement, not ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect twenty-four assigned tiers rather than twenty-three.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Paraguay has visa-free Ukrainian tourist entry for scouting, an ordinary temporary-residence route for lawful activity, a temporary-to-permanent ladder, and a constitutional naturalization baseline after 3 years of radication plus local professional/economic activity.
- Paraguay is Tier 2 for this couple's current profile: stronger than bridge-only because the ordinary residence ladder and affordability screens are useful, but still conditional because the first file is adviser-led lawful activity, not a clean DN visa.
- This is not a final recommendation or TOP-N ranking. Paraguay could improve if DNM/counsel confirms the residence / lucrative-activity visa sequence, foreign-client IT evidence package, DNIT/RUC/VAT/IPS treatment, spouse mechanics, and insurance; it could weaken if those checks make the lawful-activity route too burdensome or budget-tight.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 9 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
