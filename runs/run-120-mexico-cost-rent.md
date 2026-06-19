---
run_id: 120
date: 2026-06-14T12:04:50Z
agent: hermes
mode: country-deep-dive
target_country: Mexico
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 42
sources_added: ["src-570", "src-571", "src-572", "src-573", "src-574"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-mexico-012", "claim-mexico-013", "claim-mexico-014", "claim-mexico-015", "claim-mexico-016"]
files_modified:
  - countries/mexico.md
  - claims/mexico.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-120-mexico-cost-rent.md
proposals_created: []
completed_at: 2026-06-14T12:04:50Z
status: completed
schema_version: 2.0.0
---

# Run 120 - Mexico cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Mexico sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Mexico City / Guadalajara / Cancun / Merida city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Mexico section 5.4 cost-of-living and section 5.5 rent sections.
- Added five Livingcost source registry entries: `src-570` through `src-574`.
- Added five atomic cost/rent claims: `claim-mexico-012` through `claim-mexico-016`.
- Updated Mexico profile frontmatter, scoring rows, practical verdict, relocation-budget rent rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Mexico sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Mexico nationally at about $1,078/month for one person with rent and $2,555/month for a family-of-four proxy.
- Mexico City is the main rent-pressure case: about $1,428/month one-person total, $3,399 family proxy, and a 40 m2 rent proxy around $623-$1,035/month.
- Guadalajara is the best captured services/cost compromise at about $1,241/month one-person total, $2,983 family proxy, and $492-$776 for the 40 m2 rent proxy.
- Cancun and Merida rent is workable on paper, but tourist-market pricing, heat/humidity, storm/rainy-season exposure, and service-cost checks remain important.

## What remains

- Mexico healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, citizenship, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits/aval/fiador requirements, landlord acceptance of foreign remote-worker income, address evidence for INM/banking/SAT, private insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Argentina sections 5.4 and 5.5 cost/rent coverage to continue advancing the remaining low-depth countries.
