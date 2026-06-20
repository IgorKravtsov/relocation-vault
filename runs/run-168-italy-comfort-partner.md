---
run_id: 168
date: 2026-06-20T19:35:38Z
agent: hermes
mode: country-deep-dive
target_country: Italy
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-747", "src-748"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-italy-016", "claim-italy-017"]
files_modified:
  - countries/italy.md
  - claims/italy.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-168-italy-comfort-partner.md
proposals_created: []
completed_at: 2026-06-20T19:35:38Z
status: completed
schema_version: 2.0.0
---

# Run 168 - Italy comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the state hint and rotate to Italy sections 5.8 and 5.9.

## What was done

- Added Italy comfort-of-life coverage using a country-level safety proxy, existing Ukraine reception evidence, city-comfort synthesis, and EF EPI English-proficiency data.
- Added Italy partner/student-fit coverage using the existing DN family wording, TP work/study baseline, remote-study planning assumption, and one-income city budget screen.
- Added sources `src-747` and `src-748`, plus claims `claim-italy-016` and `claim-italy-017`.
- Updated Italy frontmatter, scoring row, practical verdict, playbook, source list, Block 8, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Italy sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Italy is comfort-positive for safety, Ukrainian reception infrastructure, and southern/central city options, but it is not English-first; Italian-language integration is a practical requirement.
- Marriage remains the conservative DN-dependent path because the captured Italy DN family wording covers spouse/minor children, not an unmarried partner.
- On one USD 3,000/month income, Italy screens mainly through Palermo or Naples; Rome is tight and Milan is a poor default unless income rises.

## What remains

- Italy still needs risk dimensions and bureaucracy/practicality coverage, plus later PR/citizenship, registered-lease, spouse work-right, insurance, and selected-city application-prep checks.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Greece sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
