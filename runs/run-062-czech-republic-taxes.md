---
run_id: 62
date: 2026-06-06T22:23:33Z
agent: hermes
mode: country-deep-dive
target_country: Czech Republic
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-316", "src-317", "src-318", "src-319"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-czech-006", "claim-czech-007", "claim-czech-008", "claim-czech-009", "claim-czech-010", "claim-czech-011"]
files_modified:
  - countries/czech-republic.md
  - claims/czech-republic.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-062-czech-republic-taxes.md
proposals_created: []
completed_at: 2026-06-06T22:23:33Z
status: completed
schema_version: 2.0.0
---

# Run 062 - Czech Republic taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue starts below the active threshold.
- Follow the prior hint to cover Czech Republic section 5.3 taxes.
- Focus on a practical first tax pass: tax-residence scope, PIT rates, self-employed expense mechanics, flat-tax regime, social/health/VAT/filing baselines, and a USD 3,000/month worked example.

## What was done

- Updated Czech Republic section 5.3 from pending to partial.
- Added four Czech tax sources (`src-316` through `src-319`) covering PwC Czech tax residence / PIT / deductions / filing / social-health / VAT and the Czech Financial Administration 2025/2026 flat-tax regime page.
- Reused `src-293` for the run-date USD/CZK exchange rate.
- Added six Czech tax claims (`claim-czech-006` through `claim-czech-011`).
- Calculated the current-income flat-tax scenario: USD 3,000/month is about CZK 62,675/month or CZK 752,100/year; if flat-tax band I applies, the 2026 monthly payment is CZK 9,984 and net after that payment is about CZK 52,691/month, roughly USD 2,522/month.
- Added risk flag `czech-flat-tax-it-trade-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-094` for Czech flat-tax / 60% expense-category / VAT / social-health fit for a Ukrainian foreign-client IT freelancer.
- Pending/open verification queue is now 6, still below the active verification threshold.

## What remains

- Czech Republic section 5.3 remains partial because the exact foreign-client IT trade classification, 60% expense-category eligibility, flat-tax compatibility with the immigration file, VAT/reverse-charge handling, and self-employed social/health registration need accountant or authority confirmation.
- Czech Republic cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-094`: Czech flat-tax / 60% expense-category / VAT / social-health fit for a Ukrainian foreign-client IT freelancer.

## Recommendation for next iteration

- Continue country-deep-dive mode because the queue remains below threshold. Prefer Poland section 5.3 taxes to continue low-depth Tier-2-hint tax coverage without clustering on Czech Republic.
