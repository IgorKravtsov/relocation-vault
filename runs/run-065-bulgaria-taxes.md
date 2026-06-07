---
run_id: 65
date: 2026-06-07T07:49:24Z
agent: hermes
mode: country-deep-dive
target_country: Bulgaria
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-328", "src-329", "src-330", "src-331"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-bulgaria-012", "claim-bulgaria-013", "claim-bulgaria-014", "claim-bulgaria-015", "claim-bulgaria-016", "claim-bulgaria-017"]
files_modified:
  - countries/bulgaria.md
  - claims/bulgaria.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-065-bulgaria-taxes.md
proposals_created: []
completed_at: 2026-06-07T07:49:24Z
status: completed
schema_version: 2.0.0
---

# Run 065 - Bulgaria taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue starts below the active threshold.
- Follow the prior hint to cover Bulgaria section 5.3 taxes.
- Focus on a practical first tax pass: tax residence, PIT, freelance statutory expenses, social/health contribution limits, VAT threshold, filing/spouse mechanics, and a USD 3,000/month worked example.

## What was done

- Updated Bulgaria section 5.3 from pending to partial.
- Added four Bulgaria tax / exchange sources (`src-328` through `src-331`) covering PwC Bulgaria PIT, residence, deductions, social/health contribution limits, VAT threshold, filing mechanics, and USD/BGN exchange rate.
- Added six Bulgaria tax claims (`claim-bulgaria-012` through `claim-bulgaria-017`).
- Calculated a conservative planning scenario: USD 3,000/month is about BGN 5,072/month; after 25% statutory expenses, capped-base 27.8% contributions, and 10% PIT, estimated net is about BGN 3,658/month (~USD 2,164). A 31.3% contribution sensitivity is about BGN 3,528/month (~USD 2,087).
- Added risk flag `bulgaria-self-employed-contribution-and-status-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-097` for Bulgaria self-insured contribution package, health-insurance obligation, foreign-client IT classification, VAT / reverse-charge handling, and immigration-status compatibility.
- Pending/open verification queue is now 9, still below the active verification threshold.

## What remains

- Bulgaria section 5.3 remains partial because the exact NRA self-insured contribution package, non-EU health-insurance obligation by residence type, IT freelancer classification, VAT / reverse-charge treatment, and compatibility with the Employment Agency / Migration Directorate self-employment route need authority or accountant confirmation.
- Bulgaria cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-097`: Bulgaria self-insured contribution package / IT classification / VAT / immigration-status fit for a Ukrainian remote IT freelancer.

## Recommendation for next iteration

- Continue country-deep-dive mode because the queue remains below threshold. Prefer Hungary section 5.3 taxes to continue low-depth Tier-2-hint tax coverage without clustering on Bulgaria.
