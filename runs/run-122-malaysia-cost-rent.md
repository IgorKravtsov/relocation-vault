---
run_id: 122
date: 2026-06-14T18:20:53Z
agent: hermes
mode: country-deep-dive
target_country: Malaysia
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 43
sources_added: ["src-580", "src-581", "src-582", "src-583", "src-584"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-malaysia-013", "claim-malaysia-014", "claim-malaysia-015", "claim-malaysia-016", "claim-malaysia-017"]
files_modified:
  - countries/malaysia.md
  - claims/malaysia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-122-malaysia-cost-rent.md
proposals_created: []
completed_at: 2026-06-14T18:20:53Z
status: completed
schema_version: 2.0.0
---

# Run 122 - Malaysia cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Malaysia sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Kuala Lumpur / George Town / Johor Bahru / Ipoh city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Malaysia section 5.4 cost-of-living and section 5.5 rent sections.
- Added five Livingcost source registry entries: `src-580` through `src-584`.
- Added five atomic cost/rent claims: `claim-malaysia-013` through `claim-malaysia-017`.
- Updated Malaysia profile frontmatter, scoring rows, practical verdict, relocation-budget rent rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Malaysia sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Malaysia nationally at about USD 824/month for one person with rent and USD 1,956/month for a family-of-four proxy.
- Kuala Lumpur is the services-rich but buffer-tight option: about USD 981/month one-person total, USD 2,371 family proxy, and a 40 m2 rent proxy around USD 350-602.
- George Town/Penang and Johor Bahru look like the first practical screens, with 40 m2 rent proxies around USD 333-488 and USD 350-451 respectively.
- Ipoh is very cheap on paper, but healthcare, connectivity, English-language services, and remote-worker community checks should precede any recommendation.

## What remains

- Malaysia healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, citizenship, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits/tenancy-stamping practice, landlord acceptance of DE Rantau / foreign remote-worker income, private insurance, accountant costs, and immigration-agent costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Thailand sections 5.4 and 5.5 cost/rent coverage to continue advancing the remaining low-depth countries.
