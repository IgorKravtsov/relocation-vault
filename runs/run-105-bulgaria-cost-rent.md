---
run_id: 105
date: 2026-06-12T13:29:09Z
agent: hermes
mode: country-deep-dive
target_country: Bulgaria
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-509", "src-510", "src-511", "src-512"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-bulgaria-018", "claim-bulgaria-019", "claim-bulgaria-020", "claim-bulgaria-021"]
files_modified:
  - countries/bulgaria.md
  - claims/bulgaria.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-105-bulgaria-cost-rent.md
proposals_created: []
completed_at: 2026-06-12T13:29:09Z
status: completed
schema_version: 2.0.0
---

# Run 105 - Bulgaria cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Bulgaria sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Sofia / Plovdiv / Varna city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Bulgaria §5.4 cost-of-living and §5.5 rent sections.
- Added four Livingcost source registry entries: `src-509` through `src-512`.
- Added four atomic cost/rent claims: `claim-bulgaria-018` through `claim-bulgaria-021`.
- Updated Bulgaria profile frontmatter, scoring rows, practical verdict, source list, relocation-budget row, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Bulgaria sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Bulgaria nationally at about $1,018/month for one person with rent and $2,517/month for a family-of-four proxy.
- Plovdiv has the best captured cost/rent fit: about $878/month one-person total, with the cheap 40 m2 1BR proxy around $297/month.
- Sofia is the rent-pressure warning: the 40 m2 proxy is about $541 cheap / $702 center, and the family proxy exceeds gross income.

## What remains

- Bulgaria healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, agency fees, landlord requirements for foreigners, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Hungary §5.4/§5.5 cost/rent coverage to avoid clustering Bulgaria and advance the low-depth Tier-2-hint cohort.
