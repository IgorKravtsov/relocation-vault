---
run_id: 115
date: 2026-06-13T20:34:24Z
agent: hermes
mode: country-deep-dive
target_country: Paraguay
target_sections: ["5.4", "5.5"]
target_criterion: null
duration_minutes: 39
sources_added: ["src-549", "src-550", "src-551", "src-552"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-paraguay-012", "claim-paraguay-013", "claim-paraguay-014", "claim-paraguay-015"]
files_modified:
  - countries/paraguay.md
  - claims/paraguay.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-115-paraguay-cost-rent.md
proposals_created: []
completed_at: 2026-06-13T20:34:24Z
status: completed
schema_version: 2.0.0
---

# Run 115 - Paraguay cost/rent

## Plan

- Continue `country-deep-dive` because the verification queue remains below the active threshold.
- Follow the rotation hint and open Paraguay sections 5.4 and 5.5 with one focused first-pass unit: national cost baseline, Asuncion / Ciudad del Este / Encarnacion city screens, rent proxy, and one-income fit.

## What was done

- Added first-pass Paraguay section 5.4 cost-of-living and section 5.5 rent sections.
- Added four Livingcost source registry entries: `src-549` through `src-552`.
- Added four atomic cost/rent claims: `claim-paraguay-012` through `claim-paraguay-015`.
- Updated Paraguay profile frontmatter, scoring rows, practical verdict, relocation-budget rent row, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue remains 1 pending/open item.
- Paraguay sections 5.4 and 5.5 moved from pending to completed for first-pass screening. Depth score moved from 2.0 to 3.0.

## Key findings

- Livingcost screens Paraguay nationally at about $682/month for one person with rent and $1,633/month for a family-of-four proxy.
- Asuncion is the services/bureaucracy first screen: about $752/month one-person total, $1,837 family proxy, and a 40 m2 rent proxy around $268-$448/month.
- Ciudad del Este and Encarnacion screen cheaper: Ciudad del Este is about $649/month one-person total with $227-$347 for the 40 m2 proxy; Encarnacion is about $619/month and $219-$355 for the 40 m2 proxy.

## What remains

- Paraguay healthcare, education, comfort, partner/student fit, risk dimensions, bureaucracy, and remaining legal/tax application-prep gaps are still pending.
- Live rental listings, deposits, agency fees, registered-address support, foreigner lease acceptance, private healthcare, accountant costs, and immigration-lawyer costs remain for later practical-budget work.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` while the queue is below threshold; rotate to Panama sections 5.4 and 5.5 cost/rent coverage to avoid clustering and advance the remaining low-depth Tier-2-hint Latin America cohort.
