---
run_id: 118
date: 2026-06-14T05:50:50Z
agent: hermes
mode: country-deep-dive
target_country: Bosnia and Herzegovina
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 42
sources_added: ["src-561", "src-562", "src-563", "src-564", "src-565"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-bosnia-herzegovina-012", "claim-bosnia-herzegovina-013", "claim-bosnia-herzegovina-014", "claim-bosnia-herzegovina-015", "claim-bosnia-herzegovina-016"]
files_modified:
  - countries/bosnia-and-herzegovina.md
  - claims/bosnia-and-herzegovina.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-118-bosnia-and-herzegovina-cost-rent.md
proposals_created: []
completed_at: 2026-06-14T05:50:50Z
status: completed
schema_version: 2.0.0
---

# Run 118 - Bosnia and Herzegovina cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Bosnia and Herzegovina sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Sarajevo / Mostar / Banja Luka / Tuzla city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Bosnia and Herzegovina section 5.4 cost-of-living and section 5.5 rent sections.
- Added five Livingcost source registry entries: `src-561` through `src-565`.
- Added five atomic cost/rent claims: `claim-bosnia-herzegovina-012` through `claim-bosnia-herzegovina-016`.
- Updated Bosnia and Herzegovina profile frontmatter, scoring rows, practical verdict, relocation-budget rent rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Bosnia and Herzegovina sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Bosnia and Herzegovina nationally at about $819/month for one person with rent and $1,926/month for a family-of-four proxy.
- Sarajevo is the first bureaucracy/services screen at about $956/month one-person total, $2,264 family proxy, and a 40 m2 rent proxy around $276-$391/month.
- Mostar is the best warm-climate cost compromise at about $819/month one-person total and $278-$300 for the 40 m2 proxy; Tuzla is the cheapest fallback at about $721/month and $182-$244 rent proxy.
- Low rent does not solve the core blocker: the visible long-stay path remains a high-burden local company / work-permit / founder file, not a DN-style route.

## What remains

- Bosnia and Herzegovina healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, citizenship, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits/commissions, registered-address support, landlord acceptance of foreign remote-worker income, private insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Moldova sections 5.4 and 5.5 cost/rent coverage to continue advancing the remaining low-depth countries.
