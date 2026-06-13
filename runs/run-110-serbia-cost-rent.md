---
run_id: 110
date: 2026-06-13T05:03:41Z
agent: hermes
mode: country-deep-dive
target_country: Serbia
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 42
sources_added: ["src-529", "src-530", "src-531", "src-532"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-serbia-016", "claim-serbia-017", "claim-serbia-018", "claim-serbia-019"]
files_modified:
  - countries/serbia.md
  - claims/serbia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-110-serbia-cost-rent.md
proposals_created: []
completed_at: 2026-06-13T05:03:41Z
status: completed
schema_version: 2.0.0
---

# Run 110 - Serbia cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Serbia sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Belgrade / Novi Sad / Niš city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Serbia section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-529` through `src-532`.
- Added four atomic cost/rent claims: `claim-serbia-016` through `claim-serbia-019`.
- Updated Serbia profile frontmatter, scoring rows, practical verdict, source list, relocation-budget row, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Serbia sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Serbia nationally at about $1,136/month for one person with rent and $2,681/month for a family-of-four proxy.
- Novi Sad is the best captured services/cost balance: about $1,173/month one-person total, with the cheap 40 m2 1BR proxy around $418/month.
- Belgrade is the rent-pressure warning: one-person total is about $1,378/month and the 40 m2 proxy is about $522 cheap / $780 center; Niš is the affordability fallback at about $857/month one-person total and $272-$380 for the 40 m2 proxy.

## What remains

- Serbia healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, agency fees, landlord address-registration cooperation, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Turkey sections 5.4 and 5.5 cost/rent coverage to avoid clustering Serbia and advance the low-depth Tier-2-hint non-EU cohort.
