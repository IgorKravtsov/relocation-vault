---
run_id: 114
date: 2026-06-13T17:28:57Z
agent: hermes
mode: country-deep-dive
target_country: Uruguay
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 42
sources_added: ["src-545", "src-546", "src-547", "src-548"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-uruguay-012", "claim-uruguay-013", "claim-uruguay-014", "claim-uruguay-015"]
files_modified:
  - countries/uruguay.md
  - claims/uruguay.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-114-uruguay-cost-rent.md
proposals_created: []
completed_at: 2026-06-13T17:28:57Z
status: completed
schema_version: 2.0.0
---

# Run 114 - Uruguay cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Uruguay sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Montevideo / Punta del Este / Salto city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Uruguay section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-545` through `src-548`.
- Added four atomic cost/rent claims: `claim-uruguay-012` through `claim-uruguay-015`.
- Updated Uruguay profile frontmatter, scoring rows, practical verdict, relocation-budget rent rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Uruguay sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Uruguay nationally at about $1,389/month for one person with rent and $3,346/month for a family-of-four proxy.
- Montevideo is the services/bureaucracy first screen but needs rent discipline: about $1,572/month one-person total, $3,766 family proxy, and a 40 m2 rent proxy around $499-$632/month.
- Punta del Este is rent-pressured at about $795-$1,013 for the 40 m2 proxy, while Salto is the affordability fallback at about $1,055/month one-person total and $262-$412 for the 40 m2 proxy.

## What remains

- Uruguay healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining residence/tax application-prep gaps are still pending.
- Live rental listings, deposits/guarantee products, agency fees, registered-address support, seasonal coastal leases, health insurance, accountant/notary costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Paraguay sections 5.4 and 5.5 cost/rent coverage to avoid clustering Uruguay and advance the remaining low-depth Tier-2-hint Latin America cohort.
