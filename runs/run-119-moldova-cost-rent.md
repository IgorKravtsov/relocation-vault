---
run_id: 119
date: 2026-06-14T09:08:00Z
agent: hermes
mode: country-deep-dive
target_country: Moldova
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 39
sources_added: ["src-566", "src-567", "src-568", "src-569"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-moldova-012", "claim-moldova-013", "claim-moldova-014", "claim-moldova-015"]
files_modified:
  - countries/moldova.md
  - claims/moldova.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-119-moldova-cost-rent.md
proposals_created: []
completed_at: 2026-06-14T09:08:00Z
status: completed
schema_version: 2.0.0
---

# Run 119 - Moldova cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Moldova sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Chisinau / Balti / Tiraspol city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Moldova section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-566` through `src-569`.
- Added four atomic cost/rent claims: `claim-moldova-012` through `claim-moldova-015`.
- Updated Moldova profile frontmatter, scoring rows, practical budget rows, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Moldova sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Moldova nationally at about $863/month for one person with rent and $2,060/month for a family-of-four proxy.
- Chisinau is the practical first base at about $967/month one-person total, $2,283 family proxy, and a 40 m2 rent proxy around $373-$538/month.
- Balti is the cheaper ordinary fallback at about $806/month one-person total, $1,870 family proxy, and $265-$375 for the 40 m2 rent proxy.
- Tiraspol is numerically very cheap, but it remains non-default because of Transnistria governance/security/practicality risk.

## What remains

- Moldova healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, citizenship, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits/commissions, registered-address support, landlord acceptance of foreign remote-worker income, private insurance, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Mexico sections 5.4 and 5.5 cost/rent coverage to continue advancing the remaining low-depth countries.
