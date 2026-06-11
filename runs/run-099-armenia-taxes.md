---
run_id: 99
date: 2026-06-11T18:48:17Z
agent: hermes
mode: country-deep-dive
target_country: Armenia
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-487", "src-488", "src-489", "src-490", "src-491"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-armenia-006", "claim-armenia-007", "claim-armenia-008", "claim-armenia-009", "claim-armenia-010"]
files_modified:
  - countries/armenia.md
  - claims/armenia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-099-armenia-taxes.md
proposals_created: []
completed_at: 2026-06-11T18:48:17Z
status: completed
schema_version: 2.0.0
---

# Run 099 - Armenia taxes

## Plan

- Continue `country-deep-dive` because the pending/open verification queue was below the active threshold at pre-flight.
- Focus on Armenia section 5.3 taxes, following the previous run hint and finishing the remaining depth-1.5 post-USSR profile tax baseline.
- Determine whether Armenian taxes are a blocker if the business-activity residence route becomes operational for foreign-client IT.

## What was done

- Added a first-pass Armenia §5.3 tax section using PwC Armenia individual tax, residence, business-income, contribution, filing, VAT / turnover-tax context, e-register portal evidence, and a current USD/AMD FX snapshot.
- Added five new source registry entries: `src-487` through `src-491`.
- Added five atomic claims: tax residence/scope, business-income scope, entrepreneur contribution formulas, VAT/turnover-tax context, and the USD 3,000/month worked example.
- Added `vq-119` for exact foreign-client IT tax category, high-tech / turnover-tax eligibility, VAT export treatment, contribution base, and business-residence compatibility.
- Updated the Armenia profile, practical playbook tax checkpoint, Block 7/8, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue moved from 9 to 10 pending/open items.
- Armenia section 5.3 moved from pending to partial. Depth score moved from 1.5 to 2.0.

## Key findings

- Armenia residents are taxed on worldwide income; tax residence generally starts at 183 days in the calendar year, centre of vital interests, or Armenian civil service.
- At USD 3,000/month and USD 1 = AMD 368.343288, gross is about AMD 1,105,030/month. Conservative ordinary modelling with 20% income tax, entrepreneur pension formula, and mandatory health contribution leaves about AMD 787,721/month / USD 2,139 before accountant, VAT, immigration, healthcare, rent, and banking friction.
- A favorable high-tech / turnover-tax and exported-service VAT outcome may exist, but it is not assumed until Armenian accountant or State Revenue Committee evidence confirms the activity-code and residence-file fit.

## What remains

- Armenia cost of living, rent, healthcare, education, comfort, partner/student mechanics, risk dimensions, and bureaucracy remain pending.
- Before filing, confirm State Revenue Committee / accountant treatment for IE vs LLC setup, high-tech / turnover-tax eligibility, VAT zero-rating or place-of-supply, pension/health contribution base, and business-activity residence renewal compatibility.

## Open questions added

- `vq-119`: exact Armenia foreign-client IT individual-entrepreneur vs LLC category, high-tech / turnover-tax eligibility, VAT export-service treatment, entrepreneur contribution base, and business-residence compatibility.

## Recommendation for next iteration

- Switch to `verification` because the pending/open verification queue has reached the active threshold of 10. Suggested focus: recent §5.3 tax-fit items that can be closed to conservative screening baselines where appropriate.
