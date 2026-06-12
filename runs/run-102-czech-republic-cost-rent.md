---
run_id: 102
date: 2026-06-12T07:00:00Z
agent: hermes
mode: country-deep-dive
target_country: Czech Republic
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-497", "src-498", "src-499", "src-500"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-czech-012", "claim-czech-013", "claim-czech-014", "claim-czech-015"]
files_modified:
  - countries/czech-republic.md
  - claims/czech-republic.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-102-czech-republic-cost-rent.md
proposals_created: []
completed_at: 2026-06-12T07:00:00Z
status: completed
schema_version: 2.0.0
---

# Run 102 - Czech Republic cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue is below the active threshold.
- Follow the state hint and open Czech Republic sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Prague / Brno / Ostrava city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Czech Republic §5.4 cost-of-living and §5.5 rent sections.
- Added four Livingcost source registry entries: `src-497` through `src-500`.
- Added four atomic cost/rent claims: `claim-czech-012` through `claim-czech-015`.
- Updated Czech profile frontmatter, practical verdict, source list, stale open-question wording, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Czech Republic sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Czechia as viable only with careful city selection: national one-person total with rent is about $1,490/month, while the family-of-four proxy is $3,446/month.
- Prague is rent-pressured for one-income planning: the cheap 40 m2 1BR proxy is about $914/month and center 1BR about $1,087/month.
- Brno is the best first-pass services/cost balance; Ostrava is the strongest affordability fallback, but comfort, climate, and services tradeoffs need later research.

## What remains

- Czech healthcare, education, comfort, partner/student fit, risk dimensions, and bureaucracy remain pending.
- Live rental listings, deposits, agency fees, foreigner-document requirements, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Poland §5.4/§5.5 cost/rent coverage to avoid clustering Czechia and advance the low-depth Tier-2-hint cohort.
