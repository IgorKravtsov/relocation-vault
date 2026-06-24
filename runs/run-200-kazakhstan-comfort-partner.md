---
run_id: 200
date: 2026-06-24T22:58:04Z
agent: hermes
mode: country-deep-dive
target_country: Kazakhstan
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 39
sources_added: ["src-801", "src-802"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-kazakhstan-020", "claim-kazakhstan-021"]
files_modified:
  - countries/kazakhstan.md
  - claims/kazakhstan.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-200-kazakhstan-comfort-partner.md
proposals_created: []
completed_at: 2026-06-24T22:58:04Z
status: completed
schema_version: 2.0.0
---

# Run 200 - Kazakhstan comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Kazakhstan sections 5.8 and 5.9.

## What was done

- Added Kazakhstan comfort-of-life coverage using WPR / TravelSafe safety proxies, EF English-proficiency data, and Almaty / Astana / Shymkent / Aktau city tradeoffs.
- Added Kazakhstan partner/student-fit coverage using existing TRP, Neo Nomad, tax, cost, rent, healthcare, and education evidence.
- Added sources `src-801` and `src-802`, plus claims `claim-kazakhstan-020` and `claim-kazakhstan-021`.
- Updated Kazakhstan frontmatter, scoring rows, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Kazakhstan sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Kazakhstan is comfort-screenable: WPR reports GPI 1.875, safety index 72 / Low risk, and US News safety rank 65th; TravelSafe also gives Safety Index 72, user sentiment 85/100, and overall risk Low.
- The main comfort downside is language/service depth: EF ranks Kazakhstan #107 with score 417; Astana and Almaty are stronger than Shymkent/Aktau but still require Russian/Kazakh support.
- For the student partner, marriage/spouse or independent status is the conservative baseline; unmarried-partner treatment and Neo Nomad dependent thresholds are not captured.
- One-income fit is best in Shymkent/Aktau and tighter in Almaty once insurance, legal/accountant, lease, and future school costs are included.

## What remains

- Kazakhstan still needs risk dimensions and bureaucracy/practicality coverage, plus official Neo Nomad/dependent mechanics, TRP/business-immigrant fit, PR/citizenship counting, tax/source classification, live lease checks, and final-city healthcare/community checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Armenia sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
