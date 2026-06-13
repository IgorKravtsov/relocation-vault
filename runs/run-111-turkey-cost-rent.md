---
run_id: 111
date: 2026-06-13T08:11:06Z
agent: hermes
mode: country-deep-dive
target_country: Turkey
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 39
sources_added: ["src-533", "src-534", "src-535", "src-536"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-turkey-015", "claim-turkey-016", "claim-turkey-017", "claim-turkey-018"]
files_modified:
  - countries/turkey.md
  - claims/turkey.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-111-turkey-cost-rent.md
proposals_created: []
completed_at: 2026-06-13T08:11:06Z
status: completed
schema_version: 2.0.0
---

# Run 111 - Turkey cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Turkey sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Istanbul / Izmir / Antalya city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Turkey section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-533` through `src-536`.
- Added four atomic cost/rent claims: `claim-turkey-015` through `claim-turkey-018`.
- Updated Turkey profile frontmatter, scoring rows, practical verdict, relocation-budget row, source list, stale Block 8 wording for resolved `vq-103`, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Turkey sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Turkey nationally at about $889/month for one person with rent and $2,252/month for a family-of-four proxy.
- Izmir is the best captured services/cost/climate balance: about $1,040/month one-person total, with the cheap 40 m2 1BR proxy around $422/month.
- Istanbul is the rent-pressure warning: one-person total is about $1,305/month and the 40 m2 proxy is about $561-$896; Antalya is the warm-coast option at about $966/month one-person total and $388-$489 for the 40 m2 proxy.

## What remains

- Turkey healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, agency fees, landlord address-registration cooperation, inflation exposure, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Georgia sections 5.4 and 5.5 cost/rent coverage to avoid clustering Turkey and advance the low-depth Tier-2-hint non-EU cohort.
