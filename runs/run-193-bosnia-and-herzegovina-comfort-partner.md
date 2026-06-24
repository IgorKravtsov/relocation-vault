---
run_id: 193
date: 2026-06-24T01:16:39Z
agent: hermes
mode: country-deep-dive
target_country: Bosnia and Herzegovina
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-787", "src-788"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-bosnia-herzegovina-021", "claim-bosnia-herzegovina-022"]
files_modified:
  - countries/bosnia-and-herzegovina.md
  - claims/bosnia-and-herzegovina.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-193-bosnia-and-herzegovina-comfort-partner.md
proposals_created: []
completed_at: 2026-06-24T01:16:39Z
status: completed
schema_version: 2.0.0
---

# Run 193 - Bosnia and Herzegovina comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Bosnia and Herzegovina sections 5.8 and 5.9.

## What was done

- Added Bosnia and Herzegovina comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Sarajevo / Mostar / Tuzla / Banja Luka city tradeoffs.
- Added Bosnia and Herzegovina partner/student-fit coverage using existing residence, company/work, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-787` and `src-788`, plus claims `claim-bosnia-herzegovina-021` and `claim-bosnia-herzegovina-022`.
- Updated Bosnia and Herzegovina frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Bosnia and Herzegovina sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Bosnia and Herzegovina is comfort-screenable: WPR gives a 2025 GPI score of 1.895 and TravelSafe-derived safety index 48 / Low, with transport/pickpocket/scam caveats.
- EF EPI gives global rank #21, score 591, and Sarajevo score 587, but Bosnian/Croatian/Serbian remains necessary for bureaucracy, leases, tax, healthcare, public schools, and integration.
- For the student partner, marriage or separate status is the conservative baseline; remote Ukrainian study is practical only after she has lawful residence.
- The one-income plan is helped by low rent, but the high-burden company/work route, entity tax/SSC uncertainty, and professional/insurance costs keep Sarajevo/services on a strict budget watch.

## What remains

- Bosnia and Herzegovina still needs risk dimensions and bureaucracy/practicality coverage, plus later citizenship/dual-citizenship rules, official Ukraine entry/protection confirmation, route-specific spouse/dependent checklist, self-employment/company permit fit, accountant/VAT/contribution confirmation, insurance quotes, and live lease/provider checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Moldova sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
