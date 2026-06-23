---
run_id: 191
date: 2026-06-23T19:03:25Z
agent: hermes
mode: country-deep-dive
target_country: Portugal
target_sections: ["5.9"]
target_criterion: null
duration_minutes: 35
sources_added: []
facts_added: 2
facts_verified: 0
claims_added: ["claim-portugal-019", "claim-portugal-020"]
files_modified:
  - countries/portugal.md
  - claims/portugal.yml
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-191-portugal-partner-fit.md
proposals_created: []
completed_at: 2026-06-23T19:03:25Z
status: completed
schema_version: 2.0.0
---

# Run 191 - Portugal partner fit

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the rotation hint to Portugal section 5.9 so the remaining Tier-1-hint low-depth profile reaches the baseline depth threshold.

## What was done

- Added Portugal partner / single-income coverage using existing temporary-protection, D8, AIMA remote-work, tax, cost, healthcare, and education evidence.
- Added claims `claim-portugal-019` and `claim-portugal-020` without adding new sources.
- Updated Portugal frontmatter, scoring row, practical verdict, source list, open application-prep notes, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 0.
- Claims added: 2.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Portugal section 5.9 moved from pending to completed; depth_score moved from 6.0 to 7.0.

## Key findings

- The safest near-term partner baseline is separate Ukrainian TP if eligible, because it gives a Temporary Protection Title plus NISS / NIF / SNS access.
- The D8 residence version can include a spouse or long-term partner, but the main applicant threshold is already about EUR 3,680/month and each extra person raises income/savings evidence.
- Marriage or strong cohabitation evidence improves the family file and may help joint tax-rate mechanics, but it does not solve the current one-income D8 gap.
- Ukrainian remote study is practical only if she has another lawful status; it is not a captured Portuguese residence basis by itself.

## What remains

- Portugal still needs risk dimensions and bureaucracy/practicality coverage, plus later exact D8 family dependent-income / savings wording, dependent work-right confirmation, official D8 medical-insurance wording, accountant fit, and live housing/insurance checks.

## Commit / push status

- Pending at run-log creation; completed after validation and git commit/push.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Rotate to North Macedonia sections 5.8 and 5.9 unless an accepted proposal or verification-threshold trigger takes priority.
