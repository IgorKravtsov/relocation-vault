---
run_id: 68
date: 2026-06-07T21:30:00Z
agent: hermes
mode: country-deep-dive
target_country: Slovakia
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-338", "src-339", "src-340", "src-341", "src-342", "src-343"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-slovakia-010", "claim-slovakia-011", "claim-slovakia-012", "claim-slovakia-013", "claim-slovakia-014", "claim-slovakia-015"]
files_modified:
  - countries/slovakia.md
  - claims/slovakia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-068-slovakia-taxes.md
proposals_created: []
completed_at: 2026-06-07T21:30:00Z
status: completed
schema_version: 2.0.0
---

# Run 068 - Slovakia taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue started below the active threshold.
- Follow the previous hint to cover Slovakia section 5.3 taxes.
- Focus on a practical first tax pass: tax residence, PIT, SZCO expense mechanics, social and health contribution minimums, VAT thresholds, filing mechanics, and a USD 3,000/month worked example.

## What was done

- Updated Slovakia section 5.3 from pending to partial.
- Added six Slovakia tax / exchange sources (`src-338` through `src-343`) covering PwC Slovakia tax-residence, PIT, entrepreneur deductions, filing mechanics, official Social Insurance Agency 2026 SZCO social-insurance minimums, health-insurer 2026 SZCO health-insurance advances, VAT thresholds, and ECB EUR/USD exchange rate.
- Added six Slovakia tax claims (`claim-slovakia-010` through `claim-slovakia-015`).
- Calculated a conservative current-income scenario: USD 3,000/month is about EUR 2,577/month. If the non-VAT SZCO 60% lump-sum expense model and 2026 minimum social/health contributions apply, first-pass net is about EUR 2,050-2,147/month, or about USD 2,386-2,499/month, before accountant/VAT/immigration costs.
- Added risk flag `slovakia-szco-tax-and-immigration-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-099` for Slovak SZCO/trade classification, VAT / reverse-charge treatment, first-year contribution timing, and compatibility with the evidence-heavy self-employed/business residence route for a Ukrainian foreign-client IT freelancer.
- Pending/open verification queue is now 10, which reaches the active verification threshold.

## What remains

- Slovakia section 5.3 remains partial because exact IT trade classification, foreign-client VAT/reverse-charge handling, first-year contribution timing, accountant filing details, and immigration-status compatibility are unresolved.
- Slovakia cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-099`: Slovakia SZCO/trade classification / VAT / contribution timing / immigration-status fit for a Ukrainian foreign-client IT freelancer.

## Recommendation for next iteration

- Switch to `verification` mode because the pending/open queue reached 10 after this run. Prioritize recent tax blockers where a conservative operational answer can be closed without changing country scoring prematurely.
