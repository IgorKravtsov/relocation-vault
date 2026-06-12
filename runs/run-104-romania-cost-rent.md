---
run_id: 104
date: 2026-06-12T10:24:03Z
agent: hermes
mode: country-deep-dive
target_country: Romania
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-505", "src-506", "src-507", "src-508"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-romania-017", "claim-romania-018", "claim-romania-019", "claim-romania-020"]
files_modified:
  - countries/romania.md
  - claims/romania.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-104-romania-cost-rent.md
proposals_created: []
completed_at: 2026-06-12T10:24:03Z
status: completed
schema_version: 2.0.0
---

# Run 104 - Romania cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Romania sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Bucharest / Cluj-Napoca / Timisoara city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Romania §5.4 cost-of-living and §5.5 rent sections.
- Added four Livingcost source registry entries: `src-505` through `src-508`.
- Added four atomic cost/rent claims: `claim-romania-017` through `claim-romania-020`.
- Updated Romania profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Romania sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Romania nationally at about $973/month for one person with rent and $2,438/month for a family-of-four proxy.
- Timisoara has the best captured cost/rent fit: about $1,029/month one-person total, with the cheap 40 m2 1BR proxy around $337/month.
- Cluj-Napoca is the rent-pressure warning: the 40 m2 proxy is about $533 cheap / $668 center, so `cluj-rent-pressure` was added.

## What remains

- Romania healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, agency fees, landlord requirements for foreigners, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Bulgaria §5.4/§5.5 cost/rent coverage to avoid clustering Romania and advance the low-depth Tier-2-hint cohort.
