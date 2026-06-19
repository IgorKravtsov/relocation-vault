---
run_id: 159
date: 2026-06-19T15:26:02Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 35
sources_added: []
facts_added: 0
facts_verified: 10
claims_added: []
files_modified:
  - countries/bosnia-and-herzegovina.md
  - countries/moldova.md
  - countries/mexico.md
  - countries/argentina.md
  - countries/malaysia.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-159-healthcare-education-verification.md
proposals_created: []
completed_at: 2026-06-19T15:26:02Z
status: completed
schema_version: 2.0.0
---

# Run 159 - healthcare/education verification baselines

## Plan

- Run `verification` mode because the queue reached the automatic threshold after run-158.
- Close one focused batch of healthcare/education application-prep blockers where existing profile evidence already supports safe country-screening baselines.

## What was done

- Resolved `vq-146` through `vq-155` for screening.
- Updated Bosnia and Herzegovina, Moldova, Mexico, Argentina, and Malaysia profiles so exact insurance quotes, maternity/newborn wording, public-system onboarding, provider prices, school fee schedules, private-preschool prices, waiting lists, and non-core-city availability are labelled as application-prep or final-city checks rather than open screening blockers.
- Updated affected country `unverified_count` fields, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 0.
- Claims added: 0.
- Facts verified: 10 queue items.
- Verification queue moved from 10 to 0 pending/open items, below the automatic verification threshold.

## Key findings

- Existing healthcare and education evidence is sufficient for country screening across the five-country batch; none of the missing exact quotes, public-system workflows, school fee schedules, or final-city provider/school checks changes the safe screening baseline.
- The remaining gaps are practical filing, budget, or city-selection checks, not blockers for maintaining the country profiles' current screening scores.

## What remains

- No pending verification-queue items remain after this batch.
- Resume country-deep-dive coverage for low-depth Tier-3 countries; Thailand sections 5.6 and 5.7 are the next suggested target.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` with Thailand sections 5.6 and 5.7 unless accepted proposals or a new verification-threshold trigger takes priority.
