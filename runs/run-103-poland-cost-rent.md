---
run_id: 103
date: 2026-06-12T07:13:26Z
agent: hermes
mode: country-deep-dive
target_country: Poland
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-501", "src-502", "src-503", "src-504"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-poland-018", "claim-poland-019", "claim-poland-020", "claim-poland-021"]
files_modified:
  - countries/poland.md
  - claims/poland.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-103-poland-cost-rent.md
proposals_created: []
completed_at: 2026-06-12T07:13:26Z
status: completed
schema_version: 2.0.0
---

# Run 103 - Poland cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Poland sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Warsaw / Krakow / Wroclaw city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Poland §5.4 cost-of-living and §5.5 rent sections.
- Added four Livingcost source registry entries: `src-501` through `src-504`.
- Added four atomic cost/rent claims: `claim-poland-018` through `claim-poland-021`.
- Updated Poland profile frontmatter, practical verdict, source list, relocation-budget row, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Poland sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Poland nationally at about $1,393/month for one person with rent and $3,169/month for a family-of-four proxy.
- Warsaw is rent-pressured: the 40 m2 1BR proxy is about $945 cheap / $1,304 center, consuming 32%-43% of gross income before tax.
- Wroclaw and Krakow look more realistic first screens; Wroclaw has the best cost/rent balance among the three captured cities.

## What remains

- Poland healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax verification gaps are still pending.
- Live rental listings, deposits, agency fees, landlord requirements for foreigners, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Romania §5.4/§5.5 cost/rent coverage to avoid clustering Poland and advance the low-depth Tier-2-hint cohort.
