---
run_id: 196
date: 2026-06-24T10:34:43Z
agent: hermes
mode: country-deep-dive
target_country: Argentina
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-793", "src-794"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-argentina-021", "claim-argentina-022"]
files_modified:
  - countries/argentina.md
  - claims/argentina.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-196-argentina-comfort-partner.md
proposals_created: []
completed_at: 2026-06-24T10:34:43Z
status: completed
schema_version: 2.0.0
---

# Run 196 - Argentina comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Argentina sections 5.8 and 5.9.

## What was done

- Added Argentina comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Buenos Aires / Cordoba / Mendoza / Rosario city tradeoffs.
- Added Argentina partner/student-fit coverage using existing DN bridge, residence, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-793` and `src-794`, plus claims `claim-argentina-021` and `claim-argentina-022`.
- Updated Argentina frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Argentina sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Argentina is comfort-screenable: WPR gives 2025 GPI 1.768, GTI 0.801, safety index 70 / Low risk, and US News safest-country rank 53rd; TravelSafe also gives Safety Index 70 and low overall / transport risk.
- Street-crime and practical-safety caveats matter: TravelSafe marks pickpockets, scams, natural disasters, and women-traveler risk as medium, including counterfeit-currency, informal taxi/exchange, and dating-app robbery risks.
- EF EPI gives Argentina global rank #26 and score 575; English fallback is comparatively good, especially Buenos Aires, but Spanish remains needed for DNM, ARCA/CUIT, leases, healthcare, schools, and daily integration.
- For the student partner, marriage may simplify a future family file, but DN is bridge-only and durable dependent mechanics are unproven; model her as needing independent lawful status until a durable sponsor category is confirmed.

## What remains

- Argentina still needs risk dimensions and bureaucracy/practicality coverage, plus official Ukraine entry confirmation, durable foreign-client IT residence route, DN/family dependent mechanics, accountant/ARCA/VAT/banking details, and final-city safety/community/provider checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Malaysia sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
