---
run_id: 64
date: 2026-06-07T04:42:38Z
agent: hermes
mode: country-deep-dive
target_country: Romania
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-324", "src-325", "src-326", "src-327"]
facts_added: 7
facts_verified: 0
claims_added: ["claim-romania-010", "claim-romania-011", "claim-romania-012", "claim-romania-013", "claim-romania-014", "claim-romania-015", "claim-romania-016"]
files_modified:
  - countries/romania.md
  - claims/romania.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-064-romania-taxes.md
proposals_created: []
completed_at: 2026-06-07T04:42:38Z
status: completed
schema_version: 2.0.0
---

# Run 064 - Romania taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue starts below the active threshold.
- Follow the prior hint to cover Romania section 5.3 taxes.
- Focus on a practical first tax pass: tax residence, independent-activity PIT/social/health/VAT baselines, ANAF filing channels, marriage filing mechanics, and a USD 3,000/month worked example.

## What was done

- Updated Romania section 5.3 from pending to partial.
- Added four Romania tax / exchange sources (`src-324` through `src-327`) covering PwC Romania individual taxes, residence, social contributions, VAT, ANAF `declaratie unica` / SPV channels, and USD/RON exchange rate.
- Added seven Romania tax claims (`claim-romania-010` through `claim-romania-016`).
- Calculated a conservative current-income scenario: USD 3,000/month is about RON 13,553/month or RON 162,639/year; a no-expense PFA-style stress test leaves about RON 9,156/month (~USD 2,027) if CAS/CASS are deducted before PIT, with a lower gross-base-PIT sensitivity of about RON 8,818/month (~USD 1,952).
- Added risk flags `romania-dn-income-above-current-budget` and `romania-pfa-registration-vat-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-096` for Romania PFA / independent-activity registration, expense, VAT / reverse-charge, and immigration-status fit for a Ukrainian foreign-client IT freelancer.
- Pending/open verification queue is now 8, still below the active verification threshold.

## What remains

- Romania section 5.3 remains partial because PFA registration / CAEN classification, expense deductions and contribution ordering, VAT / reverse-charge handling, and immigration-status compatibility need Romanian accountant or authority confirmation.
- Romania cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-096`: Romania PFA / independent-activity registration, expense, VAT / reverse-charge, and immigration-status fit for a Ukrainian foreign-client IT freelancer.

## Recommendation for next iteration

- Continue country-deep-dive mode because the queue remains below threshold. Prefer Bulgaria section 5.3 taxes to continue low-depth Tier-2-hint tax coverage without clustering on Romania.
