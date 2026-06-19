---
run_id: 123
date: 2026-06-14T21:29:15Z
agent: hermes
mode: country-deep-dive
target_country: Thailand
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 41
sources_added: ["src-585", "src-586", "src-587", "src-588", "src-589"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-thailand-012", "claim-thailand-013", "claim-thailand-014", "claim-thailand-015", "claim-thailand-016"]
files_modified:
  - countries/thailand.md
  - claims/thailand.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-123-thailand-cost-rent.md
proposals_created: []
completed_at: 2026-06-14T21:29:15Z
status: completed
schema_version: 2.0.0
---

# Run 123 - Thailand cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Thailand sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Bangkok / Chiang Mai / Phuket / Pattaya city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Thailand section 5.4 cost-of-living and section 5.5 rent sections.
- Added five Livingcost source registry entries: `src-585` through `src-589`.
- Added five atomic cost/rent claims: `claim-thailand-012` through `claim-thailand-016`.
- Updated Thailand profile frontmatter, scoring rows, practical verdict, relocation-budget rent rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Thailand sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Thailand nationally at about USD 914/month for one person with rent and USD 2,348/month for a family-of-four proxy.
- Bangkok is the services-rich but margin-tight option: about USD 1,027/month one-person total, USD 2,622 family proxy, and a 40 m2 rent proxy around USD 319-632.
- Chiang Mai is the first budget screen, with about USD 780/month one-person total and a 40 m2 rent proxy around USD 253-444, but smoke-season and service-depth checks remain.
- Phuket is the expensive/tourist-coast exception; Pattaya may be cheaper but needs quality-of-life and family-fit checks.

## What remains

- Thailand healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, citizenship, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits/agency fees, TM30/address-registration handling, landlord support for DTV address evidence, private insurance, accountant costs, and visa-trip/extension costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Indonesia sections 5.4 and 5.5 cost/rent coverage to continue advancing the remaining low-depth countries.
