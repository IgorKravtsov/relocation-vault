---
run_id: 138
date: 2026-06-16T20:56:27Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.6"]
target_criterion: healthcare-application-prep
duration_minutes: 25
sources_added: []
facts_added: 0
facts_verified: 10
claims_added: []
files_modified:
  - verification-queue.md
  - countries/portugal.md
  - countries/spain.md
  - countries/italy.md
  - countries/greece.md
  - countries/cyprus.md
  - countries/croatia.md
  - countries/malta.md
  - countries/czech-republic.md
  - countries/poland.md
  - countries/romania.md
  - state.json
  - CHANGELOG.md
  - runs/run-138-healthcare-verification-baselines.md
proposals_created: []
completed_at: 2026-06-16T20:56:27Z
status: completed
schema_version: 2.0.0
---

# Run 138 - Healthcare verification baselines

## Plan

- Enter `verification` mode because the pending queue reached the >=10 threshold after run-137.
- Resolve one focused batch: healthcare application-prep quote/onboarding blockers (`vq-120` through `vq-129`) where existing profiles already contain enough evidence for country screening.

## What was done

- Resolved ten healthcare application-prep queue items for screening: `vq-120` through `vq-129`.
- Updated affected country profiles so Block 8 / application-prep language no longer describes those items as active screening blockers.
- Preserved all healthcare sections as partial where exact route-compliant private-insurance quotes, maternity exclusions/waiting periods, or final-status public-health onboarding still need before-filing checks.
- Updated `state.json` aggregate queue size and per-country `unverified_count` fields.

## Verification results

- Facts verified: 10 queue items resolved for screening.
- Sources added: 0.
- Claims added: 0.
- Verification queue pending/open size: 10 -> 0.

## Key findings

- The open healthcare items were not country-screening blockers: existing profiles already establish public/private healthcare baselines good enough for comparison.
- Exact private-insurance quotes, maternity waiting periods/exclusions, and city/status-specific onboarding remain application-prep tasks before filing or committing to a city.

## What remains

- Healthcare sections stay partial until live quotes and final-status onboarding details are captured.
- Resume country-deep-dive mode while the pending queue remains below threshold; Bulgaria 5.6/5.7 is the suggested next anti-clustered target.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` with Bulgaria sections 5.6 and 5.7, unless new accepted proposals or verification items appear.
