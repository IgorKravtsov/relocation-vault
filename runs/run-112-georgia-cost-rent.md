---
run_id: 112
date: 2026-06-13T11:16:37Z
agent: hermes
mode: country-deep-dive
target_country: Georgia
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 38
sources_added: ["src-537", "src-538", "src-539", "src-540"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-georgia-013", "claim-georgia-014", "claim-georgia-015", "claim-georgia-016"]
files_modified:
  - countries/georgia.md
  - claims/georgia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-112-georgia-cost-rent.md
proposals_created: []
completed_at: 2026-06-13T11:16:37Z
status: completed
schema_version: 2.0.0
---

# Run 112 - Georgia cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Georgia sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Tbilisi / Batumi / Kutaisi city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Georgia section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-537` through `src-540`.
- Added four atomic cost/rent claims: `claim-georgia-013` through `claim-georgia-016`.
- Updated Georgia profile frontmatter, scoring rows, practical verdict, relocation-budget row, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Georgia sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Georgia nationally at about $923/month for one person with rent and $2,205/month for a family-of-four proxy.
- Tbilisi is the services/bureaucracy first screen but has rent pressure: about $1,028/month one-person total, $2,453 family proxy, and a 40 m2 rent proxy around $398-$616/month.
- Batumi is the warm-coast compromise at about $840/month one-person total and $310-$420 for the 40 m2 proxy; Kutaisi is the affordability fallback at about $706/month and $235-$301 for the 40 m2 proxy.

## What remains

- Georgia healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, agency fees, landlord address-registration cooperation, seasonal Batumi leases, health insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Albania sections 5.4 and 5.5 cost/rent coverage to avoid clustering Georgia and advance the remaining low-depth Tier-2-hint cohort.
