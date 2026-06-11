---
run_id: 96
date: 2026-06-11T09:26:52Z
agent: hermes
mode: country-deep-dive
target_country: Thailand
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-471", "src-472", "src-473", "src-474", "src-475", "src-476"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-thailand-007", "claim-thailand-008", "claim-thailand-009", "claim-thailand-010", "claim-thailand-011"]
files_modified:
  - countries/thailand.md
  - claims/thailand.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-096-thailand-taxes.md
proposals_created: []
completed_at: 2026-06-11T09:26:52Z
status: completed
schema_version: 2.0.0
---

# Run 096 - Thailand taxes

## Plan

- Continue `country-deep-dive` because the pending/open verification queue is below the active threshold.
- Focus on Thailand section 5.3 taxes, rotating from Malaysia to the next low-depth middle-east-asia profile with taxes still pending.
- Determine whether Thailand taxes are a blocker for a Ukrainian foreign-client IT worker earning about USD 3,000/month while using DTV as a bridge/base.

## What was done

- Added a first-pass Thailand §5.3 tax section using PwC Thailand PIT, residence, deductions, tax-administration, VAT/social-security context, and a current USD/THB FX snapshot.
- Added six new source registry entries: `src-471` through `src-476`.
- Added five atomic claims: residence/remittance scope, PIT brackets, filing/spouse mechanics, VAT/social-security context, and the USD 3,000/month worked example.
- Added `vq-116` for exact Thai DTV / foreign-client IT tax structure because the safe screening answer is not enough for filing advice.
- Updated the Thailand profile, practical playbook tax step, Block 7/8, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 6.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue moved from 6 to 7 pending/open items.
- Thailand section 5.3 moved from pending to partial. Depth score moved from 1.5 to 2.0.

## Key findings

- Thailand should not be treated as tax-free by default for DTV. PwC says residents and non-residents are taxed on assessable income derived from employment or business carried on in Thailand, and residents' post-2024 foreign-source assessable income is taxable when remitted to Thailand.
- At USD 3,000/month and USD 1 = THB 32.936578, gross is about THB 98,810/month. Conservative PIT-only modelling with only the THB 60,000 personal allowance leaves about THB 86,607/month / USD 2,630 before accountant, VAT, social-security, insurance, visa, and living costs.
- Employee social security is capped in the captured PwC context, and VAT/export-service rules may be manageable, but neither is proved for a DTV freelancer with foreign clients.

## What remains

- Thailand cost of living, rent, healthcare, education, comfort, partner/student mechanics, risk dimensions, and bureaucracy remain pending.
- Before filing or relying on DTV as a long stay, confirm Thai Revenue Department / Thai tax adviser treatment for source/remittance, registration, deductions, VAT/export-service, social-security, and DTV extension/status fit.

## Open questions added

- `vq-116`: exact Thailand DTV / foreign-client IT source-remittance classification, tax registration, deductible-expense class, VAT/export-service treatment, social-security exposure, and immigration-status compatibility.

## Recommendation for next iteration

- Continue `country-deep-dive` while the verification queue remains below threshold. Suggested focus: Indonesia section 5.3 taxes, rotating to the next low-depth middle-east-asia profile with taxes still pending.
