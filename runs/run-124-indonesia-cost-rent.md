---
run_id: 124
date: 2026-06-15T00:35:50Z
agent: hermes
mode: country-deep-dive
target_country: Indonesia
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 43
sources_added: ["src-590", "src-591", "src-592", "src-593", "src-594"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-indonesia-011", "claim-indonesia-012", "claim-indonesia-013", "claim-indonesia-014", "claim-indonesia-015"]
files_modified:
  - countries/indonesia.md
  - claims/indonesia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-124-indonesia-cost-rent.md
proposals_created: []
completed_at: 2026-06-15T00:35:50Z
status: completed
schema_version: 2.0.0
---

# Run 124 - Indonesia cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Indonesia sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Jakarta / Surabaya / Bandung / Denpasar city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Indonesia section 5.4 cost-of-living and section 5.5 rent sections.
- Added five Livingcost source registry entries: `src-590` through `src-594`.
- Added five atomic cost/rent claims: `claim-indonesia-011` through `claim-indonesia-015`.
- Updated Indonesia profile frontmatter, scoring rows, practical verdict, relocation-budget rent rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Indonesia sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Indonesia nationally at about USD 575/month for one person with rent and USD 1,369/month for a family-of-four proxy.
- Jakarta is the services-rich option: about USD 684/month one-person total, USD 1,643 family proxy, and a 40 m2 rent proxy around USD 205-355, but capital-quality housing and address-evidence leases need checks.
- Surabaya and Bandung are the first budget screens: Surabaya combines larger-city depth with a 40 m2 proxy around USD 135-264; Bandung is cooler and cheap but needs healthcare/connectivity/flood checks.
- Denpasar/Bali looks cheap in Livingcost's median table, but tourist-season leases, foreigner-market pricing, and landlord address support make it a lifestyle exception rather than the default one-income base.

## What remains

- Indonesia healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, citizenship, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits/agency fees, registered-address support, district flood/traffic/air-quality, Bali lease seasonality, private insurance, accountant costs, BPJS/VAT, and visa extension costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Kazakhstan sections 5.4 and 5.5 cost/rent coverage to continue advancing the remaining low-depth countries.
