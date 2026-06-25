---
run_id: 201
date: 2026-06-25T02:05:47Z
agent: hermes
mode: country-deep-dive
target_country: Armenia
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 41
sources_added: ["src-803", "src-804"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-armenia-019", "claim-armenia-020"]
files_modified:
  - countries/armenia.md
  - claims/armenia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-201-armenia-comfort-partner.md
proposals_created: []
completed_at: 2026-06-25T02:05:47Z
status: completed
schema_version: 2.0.0
---

# Run 201 - Armenia comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Armenia sections 5.8 and 5.9.

## What was done

- Added Armenia comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Yerevan / Gyumri / Vanadzor city tradeoffs.
- Added Armenia partner/student-fit coverage using existing residence, spouse-dependent, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-803` and `src-804`, plus claims `claim-armenia-019` and `claim-armenia-020`.
- Updated Armenia frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Armenia sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 7.5.

## Key findings

- Armenia is comfort-screenable: WPR reports GPI 1.893, GTI 0.720, safety index 60 / Low risk, and TravelSafe labels overall risk Low.
- The main comfort caveats are medium transport/taxi risk, border-region security filtering, Yerevan summer heat, and lower service depth outside Yerevan.
- EF ranks Armenia #56 with score 515 in the low-proficiency band, so Armenian/Russian administrative support is still needed.
- For the student partner, marriage/spouse or independent status remains the conservative baseline; Ukrainian remote university study is not a captured Armenian residence ground.
- One-income fit is tight in Yerevan under the conservative tax net but better in Gyumri/Vanadzor if service, healthcare, and community gaps are solved.

## What remains

- Armenia still needs risk dimensions and bureaucracy/practicality coverage, plus official foreign-client IT business-route details, PR/citizenship counting, exact dependent mechanics, tax/VAT registration fit, live lease checks, and final-city healthcare/community checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to UAE sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
