---
run_id: 109
date: 2026-06-13T01:58:26Z
agent: hermes
mode: country-deep-dive
target_country: Montenegro
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-525", "src-526", "src-527", "src-528"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-montenegro-017", "claim-montenegro-018", "claim-montenegro-019", "claim-montenegro-020"]
files_modified:
  - countries/montenegro.md
  - claims/montenegro.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-109-montenegro-cost-rent.md
proposals_created: []
completed_at: 2026-06-13T01:58:26Z
status: completed
schema_version: 2.0.0
---

# Run 109 - Montenegro cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Montenegro sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Podgorica / Budva / Kotor city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Montenegro section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-525` through `src-528`.
- Added four atomic cost/rent claims: `claim-montenegro-017` through `claim-montenegro-020`.
- Updated Montenegro profile frontmatter, scoring rows, practical verdict, source list, relocation-budget row, stale Block 8 wording for resolved `vq-101`, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Montenegro sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Montenegro nationally at about $1,090/month for one person with rent and $2,606/month for a family-of-four proxy.
- Podgorica is the best captured budget/admin baseline: about $1,066/month one-person total, with the cheap 40 m2 1BR proxy around $416/month.
- Budva is the warmer coastal compromise but rent-sensitive; Kotor is the coastal rent-pressure warning, with 40 m2 proxies around $620-$634 and 80 m2 proxies above $1,100.

## What remains

- Montenegro healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, seasonal lease restrictions, agency fees, landlord requirements for foreigners, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Serbia sections 5.4 and 5.5 cost/rent coverage to avoid clustering Montenegro and advance the low-depth Tier-2-hint non-EU cohort.
