---
run_id: 125
date: 2026-06-15T03:45:03Z
agent: hermes
mode: country-deep-dive
target_country: Kazakhstan
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 42
sources_added: ["src-595", "src-596", "src-597", "src-598", "src-599"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-kazakhstan-011", "claim-kazakhstan-012", "claim-kazakhstan-013", "claim-kazakhstan-014", "claim-kazakhstan-015"]
files_modified:
  - countries/kazakhstan.md
  - claims/kazakhstan.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-125-kazakhstan-cost-rent.md
proposals_created: []
completed_at: 2026-06-15T03:45:03Z
status: completed
schema_version: 2.0.0
---

# Run 125 - Kazakhstan cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Kazakhstan sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Almaty / Nur-Sultan / Shymkent / Aktau city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Kazakhstan section 5.4 cost-of-living and section 5.5 rent sections.
- Added five Livingcost source registry entries: `src-595` through `src-599`.
- Added five atomic cost/rent claims: `claim-kazakhstan-011` through `claim-kazakhstan-015`.
- Updated Kazakhstan profile frontmatter, scoring rows, practical verdict, relocation-budget rent rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Kazakhstan sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Kazakhstan nationally at about USD 690/month for one person with rent and USD 1,667/month for a family-of-four proxy.
- Almaty is the services-rich but rent-sensitive option: about USD 974/month one-person total, USD 2,342 family proxy, and a 40 m2 rent proxy around USD 421-649.
- Shymkent is the first budget/climate screen, with about USD 562/month one-person total and a 40 m2 proxy around USD 142-268.
- Nur-Sultan is affordable but winter-negative; Aktau is an affordable Caspian fallback pending service-depth and foreigner lease checks.

## What remains

- Kazakhstan healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, citizenship, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits/agency fees, registered-address support, landlord acceptance of foreign tenants, private insurance, accountant costs, city service depth, and TRP / Neo Nomad lease-evidence fit remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Armenia sections 5.4 and 5.5 cost/rent coverage to finish first-pass cost/rent coverage for the remaining low-depth country.
