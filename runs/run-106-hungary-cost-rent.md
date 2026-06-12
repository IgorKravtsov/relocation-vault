---
run_id: 106
date: 2026-06-12T16:35:49Z
agent: hermes
mode: country-deep-dive
target_country: Hungary
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-513", "src-514", "src-515", "src-516"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-hungary-017", "claim-hungary-018", "claim-hungary-019", "claim-hungary-020"]
files_modified:
  - countries/hungary.md
  - claims/hungary.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-106-hungary-cost-rent.md
proposals_created: []
completed_at: 2026-06-12T16:35:49Z
status: completed
schema_version: 2.0.0
---

# Run 106 - Hungary cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Hungary sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Budapest / Debrecen / Pécs city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Hungary §5.4 cost-of-living and §5.5 rent sections.
- Added four Livingcost source registry entries: `src-513` through `src-516`.
- Added four atomic cost/rent claims: `claim-hungary-017` through `claim-hungary-020`.
- Updated Hungary profile frontmatter, scoring rows, practical verdict, source list, relocation-budget row, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Hungary sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Hungary nationally at about $1,197/month for one person with rent and $2,914/month for a family-of-four proxy.
- Pécs has the best captured cost/rent fit: about $1,124/month one-person total, with the cheap 40 m2 1BR proxy around $405/month.
- Budapest is the rent-pressure warning: the 40 m2 proxy is about $593 cheap / $772 center, and the family proxy exceeds gross income.

## What remains

- Hungary healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, agency fees, landlord requirements for foreigners, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Slovakia §5.4/§5.5 cost/rent coverage to avoid clustering Hungary and advance the low-depth Tier-2-hint cohort.
