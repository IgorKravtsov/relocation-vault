---
run_id: 91
date: 2026-06-10T17:48:07Z
agent: hermes
mode: country-deep-dive
target_country: Mexico
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-449", "src-450", "src-451", "src-452", "src-453", "src-454", "src-455"]
facts_added: 9
facts_verified: 0
claims_added: ["claim-mexico-007", "claim-mexico-008", "claim-mexico-009", "claim-mexico-010", "claim-mexico-011"]
files_modified:
  - countries/mexico.md
  - claims/mexico.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-091-mexico-taxes.md
proposals_created: []
completed_at: 2026-06-10T17:48:07Z
status: completed
schema_version: 2.0.0
---

# Run 091 - Mexico taxes

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold at pre-flight.
- Follow the run-090 hint to cover Mexico section 5.3 taxes as a low-depth Tier-3-hint profile with taxes still pending.
- Keep the unit focused on a conservative first-pass foreign-client IT model at the couple's USD 3,000/month budget.

## What was done

- Updated Mexico section 5.3 from pending to partial.
- Added a conservative ordinary resident PIT model: USD 3,000/month is about MXN 52,292/month at the run-091 FX snapshot; resident PIT-only leaves about MXN 42,645/month / USD 2,447 before accountant, VAT, IMSS/social-security, health-insurance, and immigration costs.
- Captured PwC baselines for worldwide-income residence, 2026 PIT rates, business/professional deductions, VAT and employee IMSS context, annual filing, and no joint returns.
- Kept RESICO, VAT/export-service, IMSS/social-security, SAT registration, and immigration-file fit as verification-required rather than assuming a low-tax simplified regime.
- Added seven Mexico tax / FX sources (`src-449` through `src-455`) and five Mexico tax claims (`claim-mexico-007` through `claim-mexico-011`).
- Added `mexico-resico-eligibility-gap`, `mexico-vat-export-service-gap`, and `mexico-social-security-category-gap` risk flags.
- Added `vq-113` for SAT regime / RESICO eligibility, VAT/export-service handling, IMSS/social-security treatment, and temporary-residence compatibility.
- Updated Mexico depth_score from 1.5 to 2.0.

## Verification results

- Facts added: 9 tax screening facts.
- Sources added: 7.
- Claims added: 5.
- Verification queue is 9 pending/open items, below the active verification threshold.

## What remains

- Mexico cost of living, rent, healthcare, education, comfort, partner/student-specific mechanics, risk dimensions, bureaucracy, accountant/lawyer contacts, and full relocation budget remain pending.
- Mexico section 5.3 remains partial until SAT / IMSS guidance or a Mexican accountant confirms the exact individual regime, RESICO eligibility, VAT/export-service treatment, contribution obligations, and compatibility with the temporary-residence file.

## Open questions added

- `vq-113`: Mexico foreign-client IT SAT/RESICO, VAT/export-service, IMSS/social-security, and residence-file fit.

## Recommendation for next iteration

- Continue `country-deep-dive` because the pending/open verification queue is below threshold. Suggested focus: Argentina section 5.3 taxes, as another low-depth country with taxes still pending.
