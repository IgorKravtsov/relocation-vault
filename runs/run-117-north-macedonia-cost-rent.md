---
run_id: 117
date: 2026-06-14T02:45:41Z
agent: hermes
mode: country-deep-dive
target_country: North Macedonia
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 39
sources_added: ["src-557", "src-558", "src-559", "src-560"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-north-macedonia-012", "claim-north-macedonia-013", "claim-north-macedonia-014", "claim-north-macedonia-015"]
files_modified:
  - countries/north-macedonia.md
  - claims/north-macedonia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-117-north-macedonia-cost-rent.md
proposals_created: []
completed_at: 2026-06-14T02:45:41Z
status: completed
schema_version: 2.0.0
---

# Run 117 - North Macedonia cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open North Macedonia sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Skopje / Ohrid / Bitola city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass North Macedonia section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-557` through `src-560`.
- Added four atomic cost/rent claims: `claim-north-macedonia-012` through `claim-north-macedonia-015`.
- Updated North Macedonia profile frontmatter, scoring rows, practical verdict, relocation-budget rent rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- North Macedonia sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens North Macedonia nationally at about $775/month for one person with rent and $1,829/month for a family-of-four proxy.
- Skopje is the practical first base at about $887/month one-person total, $2,082 family proxy, and a 40 m2 rent proxy around $294-$378/month.
- Ohrid and Bitola are stronger budget fallbacks: Ohrid is about $735/month with $161-$242 for the 40 m2 proxy; Bitola is about $678/month with $180-$251 for the 40 m2 proxy.

## What remains

- North Macedonia healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits/commissions, registered-address support, landlord acceptance of foreign remote-worker income, private insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Bosnia and Herzegovina sections 5.4 and 5.5 cost/rent coverage to continue advancing the remaining low-depth countries.
