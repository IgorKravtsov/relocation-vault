---
run_id: 121
date: 2026-06-14T15:13:27Z
agent: hermes
mode: country-deep-dive
target_country: Argentina
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 41
sources_added: ["src-575", "src-576", "src-577", "src-578", "src-579"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-argentina-012", "claim-argentina-013", "claim-argentina-014", "claim-argentina-015", "claim-argentina-016"]
files_modified:
  - countries/argentina.md
  - claims/argentina.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-121-argentina-cost-rent.md
proposals_created: []
completed_at: 2026-06-14T15:13:27Z
status: completed
schema_version: 2.0.0
---

# Run 121 - Argentina cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Argentina sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Buenos Aires / Cordoba / Mendoza / Rosario city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Argentina section 5.4 cost-of-living and section 5.5 rent sections.
- Added five Livingcost source registry entries: `src-575` through `src-579`.
- Added five atomic cost/rent claims: `claim-argentina-012` through `claim-argentina-016`.
- Updated Argentina profile frontmatter, scoring rows, practical verdict, relocation-budget rent rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Argentina sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Argentina nationally at about USD 878/month for one person with rent and USD 2,136/month for a family-of-four proxy.
- Buenos Aires is the services-rich but margin-tight option: about USD 1,207/month one-person total, USD 2,929 family proxy, and a 40 m2 rent proxy around USD 396-578.
- Cordoba and Mendoza look like the first budget/climate screens, with 40 m2 rent proxies around USD 245-353 and USD 269-344 respectively.
- Rosario is very cheap on paper, but safety/quality-of-life and service-depth checks should precede any recommendation.

## What remains

- Argentina healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, citizenship, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, guarantees/deposits, landlord acceptance of foreign remote-worker income, DNM address evidence, private insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Malaysia sections 5.4 and 5.5 cost/rent coverage to continue advancing the remaining low-depth countries.
