---
run_id: 113
date: 2026-06-13T14:22:00Z
agent: hermes
mode: country-deep-dive
target_country: Albania
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-541", "src-542", "src-543", "src-544"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-albania-013", "claim-albania-014", "claim-albania-015", "claim-albania-016"]
files_modified:
  - countries/albania.md
  - claims/albania.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-113-albania-cost-rent.md
proposals_created: []
completed_at: 2026-06-13T14:22:00Z
status: completed
schema_version: 2.0.0
---

# Run 113 - Albania cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Albania sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Tirana / Durrës / Vlorë city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Albania section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-541` through `src-544`.
- Added four atomic cost/rent claims: `claim-albania-013` through `claim-albania-016`.
- Updated Albania profile frontmatter, scoring rows, practical verdict, relocation-budget rent rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Albania sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Albania nationally at about $1,037/month for one person with rent and $2,429/month for a family-of-four proxy.
- Tirana is the services and bureaucracy first screen but has rent pressure: about $1,256/month one-person total, $2,960 family proxy, and a 40 m2 rent proxy around $449-$703/month.
- Durrës and Vlorë screen better for budget: Durrës is about $940/month one-person total with $322-$449 for the 40 m2 proxy; Vlorë is about $893/month and $326-$378 for the 40 m2 proxy.

## What remains

- Albania healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, agency fees, registered-address support, seasonal coastal leases, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Uruguay sections 5.4 and 5.5 cost/rent coverage to avoid clustering Albania and advance the remaining low-depth Tier-2-hint cohort.
