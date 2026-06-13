---
run_id: 116
date: 2026-06-13T23:39:26Z
agent: hermes
mode: country-deep-dive
target_country: Panama
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 38
sources_added: ["src-553", "src-554", "src-555", "src-556"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-panama-012", "claim-panama-013", "claim-panama-014", "claim-panama-015"]
files_modified:
  - countries/panama.md
  - claims/panama.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-116-panama-cost-rent.md
proposals_created: []
completed_at: 2026-06-13T23:39:26Z
status: completed
schema_version: 2.0.0
---

# Run 116 - Panama cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Panama sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Panama City / David / Santiago city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Panama section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-553` through `src-556`.
- Added four atomic cost/rent claims: `claim-panama-012` through `claim-panama-015`.
- Updated Panama profile frontmatter, scoring rows, practical budget row, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Panama sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Panama nationally at about $1,324/month for one person with rent and $3,050/month for a family-of-four proxy.
- Panama City is the services/bureaucracy base but budget-tight: about $1,583/month one-person total, $3,567 family proxy, and a 40 m2 rent proxy around $794-$1,062/month.
- David is the strongest budget fallback at about $922/month one-person total, $2,086 family proxy, and $302-$332 for the 40 m2 proxy; Santiago sits between them at $1,122/month and $387-$590 rent proxy.

## What remains

- Panama healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining residence/tax application-prep gaps are still pending.
- Live rental listings, deposits/commissions, registered-address support, landlord acceptance of foreign remote-worker income, private insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to North Macedonia sections 5.4 and 5.5 cost/rent coverage to avoid clustering Latin America and advance the remaining low-depth countries.
