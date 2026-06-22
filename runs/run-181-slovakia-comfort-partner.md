---
run_id: 181
date: 2026-06-22T11:40:00Z
agent: hermes
mode: country-deep-dive
target_country: Slovakia
target_sections: ["5.8", "5.9"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-766", "src-767"]
facts_added: 2
facts_verified: 0
claims_added: ["claim-slovakia-024", "claim-slovakia-025"]
files_modified:
  - countries/slovakia.md
  - claims/slovakia.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-181-slovakia-comfort-partner.md
proposals_created: []
completed_at: 2026-06-22T11:40:00Z
status: completed
schema_version: 2.0.0
---

# Run 181 - Slovakia comfort / partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the state hint and rotate to Slovakia sections 5.8 and 5.9.

## What was done

- Added Slovakia comfort-of-life coverage using safety proxies, English-proficiency evidence, and city-comfort synthesis for Bratislava, Kosice, and Poprad.
- Added Slovakia partner/student-fit coverage using the existing TP, family-reunification, Polish residence-card, remote-study, and one-income budget evidence.
- Added sources `src-766` and `src-767`, plus claims `claim-slovakia-024` and `claim-slovakia-025`.
- Updated Slovakia frontmatter, scoring row, practical verdict, playbook/source list context, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Slovakia sections 5.8 and 5.9 moved from pending to completed; depth_score moved from 5.5 to 8.0.

## Key findings

- Slovakia is comfort-acceptable for screening: daily-safety proxies are favorable and EF EPI ranks Slovakia highly, with Kosice and Bratislava around the 600 score band.
- Slovak language remains important for immigration offices, leases, public healthcare, schooling, tax/SZCO administration, and long-term integration despite better English-facing odds in larger cities.
- For the student partner, Slovakia does not solve the unmarried-partner problem automatically: she needs independent TP/status, or marriage before relying on family reunification.

## What remains

- Slovakia still needs risk dimensions and bureaucracy/practicality coverage, plus later citizenship, ordinary-route, accountant/tax, insurance, and selected-city application-prep checks.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to Slovenia sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
