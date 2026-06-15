---
run_id: 126
date: 2026-06-15T06:52:06Z
agent: hermes
mode: country-deep-dive
target_country: Armenia
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 44
sources_added: ["src-600", "src-601", "src-602", "src-603"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-armenia-011", "claim-armenia-012", "claim-armenia-013", "claim-armenia-014"]
files_modified:
  - countries/armenia.md
  - claims/armenia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-126-armenia-cost-rent.md
proposals_created: []
completed_at: 2026-06-15T06:52:06Z
status: completed
schema_version: 2.0.0
---

# Run 126 - Armenia cost/rent

## Plan

- Continue `country-deep-dive` because the pending verification queue is below the active automatic threshold.
- Follow the rotation hint and open Armenia sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Yerevan / Gyumri / Vanadzor city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Armenia section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-600` through `src-603`.
- Added four atomic cost/rent claims: `claim-armenia-011` through `claim-armenia-014`.
- Updated Armenia profile frontmatter, scoring rows, practical verdict, relocation-budget rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Armenia sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Armenia nationally at about USD 1,070/month for one person with rent and USD 2,543/month for a family-of-four proxy.
- Yerevan is the services-rich but rent-sensitive default: about USD 1,148/month one-person total, USD 2,725 family proxy, and a 40 m2 rent proxy around USD 461-657.
- Gyumri is the first affordability fallback, with about USD 746/month one-person total and a 40 m2 proxy around USD 253-406, but the winter and service-depth tradeoff is substantial.
- Vanadzor is the cheapest captured rent screen, but it should remain a fallback until live listings, heating, healthcare, community, and landlord residence-address support are checked.

## What remains

- Armenia healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, citizenship, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits/agency fees, residence-address support, winter heating costs, private insurance, accountant costs, city service depth, and business-residence lease-evidence fit remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- All 33 countries now have first-pass legalization/climate/tax/cost/rent baselines. Even though the pending queue remains below the automatic threshold, the next useful pass is verification or consolidation rather than another cost/rent country rotation.
