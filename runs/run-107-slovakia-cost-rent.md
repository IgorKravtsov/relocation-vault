---
run_id: 107
date: 2026-06-12T19:43:03Z
agent: hermes
mode: country-deep-dive
target_country: Slovakia
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-517", "src-518", "src-519", "src-520"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-slovakia-016", "claim-slovakia-017", "claim-slovakia-018", "claim-slovakia-019"]
files_modified:
  - countries/slovakia.md
  - claims/slovakia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-107-slovakia-cost-rent.md
proposals_created: []
completed_at: 2026-06-12T19:43:03Z
status: completed
schema_version: 2.0.0
---

# Run 107 - Slovakia cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Slovakia sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Bratislava / Kosice / Poprad city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Slovakia §5.4 cost-of-living and §5.5 rent sections.
- Added four Livingcost source registry entries: `src-517` through `src-520`.
- Added four atomic cost/rent claims: `claim-slovakia-016` through `claim-slovakia-019`.
- Updated Slovakia profile frontmatter, scoring rows, practical verdict, source list, relocation-budget row, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Slovakia sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Slovakia nationally at about $1,365/month for one person with rent and $3,140/month for a family-of-four proxy.
- Poprad has the best captured affordability fit: about $1,309/month one-person total, with the cheap 40 m2 1BR proxy around $481/month.
- Bratislava is the rent-pressure warning: the 40 m2 proxy is about $664 cheap / $921 center, and the family proxy exceeds gross income.

## What remains

- Slovakia healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, agency fees, landlord requirements for foreigners, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Slovenia §5.4/§5.5 cost/rent coverage to avoid clustering Slovakia and advance the low-depth Tier-2-hint EU cohort.
