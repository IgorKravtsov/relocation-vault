---
run_id: 274
date: 2026-07-04T16:50:26Z
agent: hermes
mode: consolidation
target_country: Uruguay
target_sections: []
target_criterion: tier-application-small-batch
duration_minutes: 30
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: []
files_modified:
  - countries/uruguay.md
  - countries.yml
  - state.json
  - INDEX.md
  - dimensions/tier-normalization-worksheet.md
  - dimensions/tier-readiness-audit.md
  - dimensions/screening-readiness-map.md
  - decisions/decisions.md
  - CHANGELOG.md
  - runs/run-274-tier-application-uruguay.md
proposals_created: []
completed_at: 2026-07-04T16:50:26Z
status: completed
schema_version: 2.0.0
---

# Run 274 - tier application: Uruguay

## Plan

- Run one focused consolidation unit because there are no accepted proposals, no pending/open verification items, no stale-claim trigger, and all countries are already at depth 10.0.
- Continue schema-safe tier application with a single country rather than bulk-converting tier hints.

## What was done

- Assigned Uruguay `tier: 2` in `countries/uruguay.md`, `countries.yml`, `state.json`, and `INDEX.md`.
- Rewrote Uruguay Block 1 tier wording to explain why the assignment is conditional ordinary-residence / Latin America settlement, not ranking.
- Added a `decisions/decisions.md` entry recording the tier decision, rationale, sources, and counterevidence.
- Updated tier-normalization / readiness handoff notes so they reflect twenty-three assigned tiers rather than twenty-two.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 0 queue items.
- Verification queue remains 0 pending/open items.

## Key findings

- Uruguay has visa-free entry, an official permanent legal residence route that can use foreign-company employment or independent-worker means-of-life evidence, and a legal-citizenship baseline after 3 years with family constituted in Uruguay or 5 years without family.
- Uruguay is Tier 2 for this couple's current profile: stronger than a bridge-only jurisdiction, but still conditional because the durable plan depends on notary/accountant-certified income, DGI/BPS/VAT treatment, insurance/onboarding, habitual presence, Spanish integration, and disciplined one-income city choice.
- This is not a final recommendation or TOP-N ranking. Uruguay could improve if Uruguayan counsel confirms a clean foreign-client IT residence/tax package and stable healthcare/insurance costs; it could weaken if BPS/VAT or Montevideo housing costs compress the budget.

## What remains

- Continue tier application only in small schema-safe batches with explicit Block 1 rationale.
- Leave the remaining 10 countries as `tier: null` until reviewed country by country.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue consolidation with another small-batch tier application pass unless accepted proposals, verification threshold, or staleness checks take priority.
