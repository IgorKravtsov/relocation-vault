---
run_id: 108
date: 2026-06-12T22:51:32Z
agent: hermes
mode: country-deep-dive
target_country: Slovenia
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-521", "src-522", "src-523", "src-524"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-slovenia-014", "claim-slovenia-015", "claim-slovenia-016", "claim-slovenia-017"]
files_modified:
  - countries/slovenia.md
  - claims/slovenia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-108-slovenia-cost-rent.md
proposals_created: []
completed_at: 2026-06-12T22:51:32Z
status: completed
schema_version: 2.0.0
---

# Run 108 - Slovenia cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Slovenia sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Ljubljana / Maribor / Nova Gorica city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Slovenia section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-521` through `src-524`.
- Added four atomic cost/rent claims: `claim-slovenia-014` through `claim-slovenia-017`.
- Updated Slovenia profile frontmatter, scoring rows, practical verdict, source list, relocation-budget row, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Slovenia sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Slovenia nationally at about $1,515/month for one person with rent and $3,570/month for a family-of-four proxy.
- Maribor is the best captured larger-city balance: about $1,317/month one-person total, with the cheap 40 m2 1BR proxy around $414/month.
- Ljubljana is the rent-pressure warning: the 40 m2 proxy is about $735 cheap / $923 center, and the family proxy exceeds gross income.

## What remains

- Slovenia healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, agency fees, landlord requirements for foreigners, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Montenegro sections 5.4 and 5.5 cost/rent coverage to avoid clustering Slovenia and advance the low-depth Tier-2-hint cohort.
