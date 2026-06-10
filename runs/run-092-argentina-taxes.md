---
run_id: 92
date: 2026-06-10T20:58:40Z
agent: hermes
mode: country-deep-dive
target_country: Argentina
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-456", "src-457", "src-458", "src-459", "src-460", "src-461"]
facts_added: 9
facts_verified: 0
claims_added: ["claim-argentina-007", "claim-argentina-008", "claim-argentina-009", "claim-argentina-010", "claim-argentina-011"]
files_modified:
  - countries/argentina.md
  - claims/argentina.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-092-argentina-taxes.md
proposals_created: []
completed_at: 2026-06-10T20:58:40Z
status: completed
schema_version: 2.0.0
---

# Run 092 - Argentina taxes

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold at pre-flight.
- Follow the run-091 hint to cover Argentina section 5.3 taxes as a low-depth Tier-3-hint profile with taxes still pending.
- Keep the unit focused on a conservative first-pass foreign-client IT model at the couple's USD 3,000/month budget.

## What was done

- Updated Argentina section 5.3 from pending to partial.
- Added a conservative PIT-only model: USD 3,000/month is about ARS 4,338,500/month at the run-092 FX snapshot; applying the captured self-employed PIT scale with no optimisation leaves about ARS 3,296,882/month / USD 2,280.
- Added a downside employee-style contribution sensitivity: using 17% of gross and deducting it before PIT leaves about ARS 2,787,975/month / USD 1,928 before accountant, VAT, provincial gross-income tax, banking, and immigration costs.
- Captured PwC baselines for tax residence, resident worldwide income, self-employed PIT, contribution deductibility, VAT, provincial gross-income-tax risk, tax filing, spouse-separate taxation, and corporate VAT/export context.
- Kept monotributo/autonomous-worker classification, VAT/export-service treatment, Ingresos Brutos by city, social-security/health obligations, banking/invoice settlement, and DN/temporary-residence fit as verification-required rather than assuming a favorable simplified regime.
- Added six Argentina tax / FX sources (`src-456` through `src-461`) and five Argentina tax claims (`claim-argentina-007` through `claim-argentina-011`).
- Added `argentina-pit-vat-gross-income-tax-risk`, `argentina-social-security-category-gap`, and `argentina-monotributo-export-fit-gap` risk flags.
- Added `vq-114` for ARCA registration / monotributo-autonomous fit / VAT-export-service / Ingresos Brutos / social-security-health / banking-invoice / residence compatibility.
- Updated Argentina depth_score from 1.5 to 2.0.

## Verification results

- Facts added: 9 tax screening facts.
- Sources added: 6.
- Claims added: 5.
- Verification queue is 10 pending/open items, meeting the active verification threshold.

## What remains

- Argentina cost of living, rent, healthcare, education, comfort, partner/student-specific mechanics, broader risk dimensions, bureaucracy, accountant/lawyer contacts, and full relocation budget remain pending.
- Argentina section 5.3 remains partial until ARCA guidance or an Argentine accountant confirms the exact foreign-client IT structure, monotributo/autonomous-worker eligibility, VAT/export-service handling, Ingresos Brutos exposure, self-employed social-security/health obligations, banking/invoice requirements, and DN/temporary-residence compatibility.

## Open questions added

- `vq-114`: Argentina foreign-client IT ARCA registration, monotributo/autonomous-worker fit, VAT/export-service, Ingresos Brutos, social-security/health, banking/invoice, and residence compatibility.

## Recommendation for next iteration

- Run `verification` next because the pending/open verification queue is now 10, meeting the active threshold. Suggested focus: close a tax-fit batch for recent pending §5.3 items using conservative screening baselines where existing sources already support safe comparison.
