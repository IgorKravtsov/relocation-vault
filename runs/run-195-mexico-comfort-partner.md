---
run_id: 195
date: 2026-06-24T07:29:05Z
agent: hermes
mode: country-deep-dive
target_country: Mexico
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-791", "src-792"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-mexico-021", "claim-mexico-022"]
files_modified:
  - countries/mexico.md
  - claims/mexico.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-195-mexico-comfort-partner.md
proposals_created: []
completed_at: 2026-06-24T07:29:05Z
status: completed
schema_version: 2.0.0
---

# Run 195 - Mexico comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Mexico sections 5.8 and 5.9.

## What was done

- Added Mexico comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Guadalajara / Mexico City / Merida / Cancun city tradeoffs.
- Added Mexico partner/student-fit coverage using existing residence, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-791` and `src-792`, plus claims `claim-mexico-021` and `claim-mexico-022`.
- Updated Mexico frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Mexico sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Mexico is comfort-screenable but uneven: WPR gives 2025 GPI 2.636 and safety index 65 / Medium; TravelSafe gives Safety Index 58 / Medium with regional variation, transport/taxi Low, and pickpocket High.
- EF EPI gives Mexico global rank #103 and score 440; Spanish is necessary for INM, SAT/RFC, leases, healthcare, schools, and daily integration.
- For the student partner, marriage/family unity or an independent file remains the conservative baseline; do not bank on an unmarried-partner dependent route.
- One-income fit remains fragile because the temporary-residence income benchmark appears above USD 3,000/month and the PIT-only tax net leaves limited room for insurance, professional fees, and rent mistakes.

## What remains

- Mexico still needs risk dimensions and bureaucracy/practicality coverage, plus official Ukraine entry confirmation, serving-consulate solvency/dependent checklist, exact family-unity documents, accountant/SAT/IMSS/VAT details, live lease checks, and final-city safety/community/provider checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Argentina sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
