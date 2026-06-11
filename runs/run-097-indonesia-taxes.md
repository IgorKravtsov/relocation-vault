---
run_id: 97
date: 2026-06-11T12:33:59Z
agent: hermes
mode: country-deep-dive
target_country: Indonesia
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-477", "src-478", "src-479", "src-480", "src-481"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-indonesia-006", "claim-indonesia-007", "claim-indonesia-008", "claim-indonesia-009", "claim-indonesia-010"]
files_modified:
  - countries/indonesia.md
  - claims/indonesia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-097-indonesia-taxes.md
proposals_created: []
completed_at: 2026-06-11T12:33:59Z
status: completed
schema_version: 2.0.0
---

# Run 097 - Indonesia taxes

## Plan

- Continue `country-deep-dive` because the pending/open verification queue is below the active threshold.
- Focus on Indonesia section 5.3 taxes, rotating from Thailand to a low-depth middle-east-asia profile with taxes still pending.
- Determine whether Indonesia taxes are a blocker if E33G becomes realistic later, while preserving the existing warning that E33G is above the current income.

## What was done

- Added a first-pass Indonesia §5.3 tax section using PwC Indonesia PIT, residence, deductions, tax administration, incentives, VAT/BPJS context, and a current USD/IDR FX snapshot.
- Added five new source registry entries: `src-477` through `src-481`.
- Added five atomic claims: tax residence/scope, 2026 PIT brackets, personal relief/marriage effect, VAT/BPJS context, and the USD 3,000/month worked example.
- Added `vq-117` for exact E33G / foreign-client IT tax structure because the safe screening answer is not enough for filing advice.
- Updated the Indonesia profile, practical playbook tax step, Block 7/8, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue moved from 7 to 8 pending/open items.
- Indonesia section 5.3 moved from pending to partial. Depth score moved from 1.5 to 2.0.

## Key findings

- Indonesia should not be treated as tax-free by default. PwC says residents are generally taxed on worldwide income, though a conditional first-four-years skilled-foreigner territorial concession may apply and needs adviser confirmation.
- At USD 3,000/month and USD 1 = IDR 17,916.976082, gross is about IDR 53.75m/month. Conservative resident PIT-only modelling with only IDR 54m personal relief leaves about IDR 43.64m/month / USD 2,436 before accountant, VAT, BPJS/housing-savings, insurance, visa, and living costs.
- VAT/exported-service and BPJS/housing-savings treatment may be manageable but are not proved for an E33G foreign-client IT worker.

## What remains

- Indonesia cost of living, rent, healthcare, education, comfort, partner/student mechanics, risk dimensions, and bureaucracy remain pending.
- Before filing or staying long enough for tax residence, confirm DGT / Indonesian tax-adviser treatment for source classification, skilled-foreigner concession, registration, VAT/exported-service status, BPJS/housing-savings, and E33G status fit.

## Open questions added

- `vq-117`: exact Indonesia E33G / foreign-client IT source classification, skilled-foreigner territorial concession fit, NPWP/registration category, VAT/exported-service handling, BPJS/housing-savings exposure, and immigration-status compatibility.

## Recommendation for next iteration

- Continue `country-deep-dive` while the verification queue remains below threshold. Suggested focus: Kazakhstan section 5.3 taxes, rotating to the next low-depth post-USSR profile with taxes still pending.
