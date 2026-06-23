---
run_id: 192
date: 2026-06-23T22:09:00Z
agent: hermes
mode: country-deep-dive
target_country: North Macedonia
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-785", "src-786"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-north-macedonia-020", "claim-north-macedonia-021"]
files_modified:
  - countries/north-macedonia.md
  - claims/north-macedonia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-192-north-macedonia-comfort-partner.md
proposals_created: []
completed_at: 2026-06-23T22:09:00Z
status: completed
schema_version: 2.0.0
---

# Run 192 - North Macedonia comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to North Macedonia sections 5.8 and 5.9.

## What was done

- Added North Macedonia comfort-of-life coverage using WPR / TravelSafe-derived safety proxies, EF English-proficiency data, and Skopje / Ohrid / Bitola city tradeoffs.
- Added North Macedonia partner/student-fit coverage using existing residence, self-employment/company, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-785` and `src-786`, plus claims `claim-north-macedonia-020` and `claim-north-macedonia-021`.
- Updated North Macedonia frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- North Macedonia sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- North Macedonia is comfort-screenable: WPR gives a 2025 GPI score of 1.799 and TravelSafe-derived safety index 55 / Low.
- EF EPI gives an English score of 595 versus global average 488 and European rank #17, but Macedonian remains necessary for bureaucracy, leases, taxes, public schools, and integration.
- For the student partner, marriage or separate status is the conservative baseline; remote Ukrainian study is practical only after she has lawful residence.
- The one-income plan is helped by low rent, but the self-employment/company route and conservative contribution stress-test net keep Skopje, private insurance, and future international school on a strict budget watch.

## What remains

- North Macedonia still needs risk dimensions and bureaucracy/practicality coverage, plus later PR/citizenship rules, current Ukraine entry/protection confirmation, route-specific spouse/dependent checklist, self-employment/company permit fit, accountant/VAT/contribution confirmation, insurance quotes, and live lease/provider checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Bosnia and Herzegovina sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
