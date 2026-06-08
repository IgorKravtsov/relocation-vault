---
run_id: 73
date: 2026-06-08T09:02:54Z
agent: hermes
mode: country-deep-dive
target_country: Turkey
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-359", "src-360", "src-361", "src-362", "src-363", "src-364"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-turkey-010", "claim-turkey-011", "claim-turkey-012", "claim-turkey-013", "claim-turkey-014"]
files_modified:
  - countries/turkey.md
  - claims/turkey.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-073-turkey-taxes.md
proposals_created: []
completed_at: 2026-06-08T09:02:54Z
status: completed
schema_version: 2.0.0
---

# Run 073 - Turkey taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue started below the active threshold.
- Follow the previous hint to cover Turkey section 5.3 taxes.
- Focus on a practical first tax pass: tax residence, PIT brackets, foreign-client professional-income caveats, SGK/VAT context, filing mechanics, and a USD 3,000/month worked example.

## What was done

- Updated Turkey section 5.3 from pending to partial.
- Added six Turkey tax / FX sources (`src-359` through `src-364`) covering PwC Turkey tax residence, PIT, income determination, social-security and filing mechanics, VAT context, and XE USD/TRY exchange rate.
- Added five Turkey tax claims (`claim-turkey-010` through `claim-turkey-014`).
- Calculated a conservative tax stress test: USD 3,000/month is about TRY 138,286/month. Ordinary 2026 non-employment PIT leaves about TRY 99,677/month (~USD 2,162), while a 15% employee-style SGK sensitivity leaves about TRY 86,194/month (~USD 1,870), before accountant/VAT/immigration costs.
- Added risk flag `turkey-self-employment-and-sgk-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-103` for Turkish self-employment permission, SGK / Bag-Kur premium base, VAT / export-of-services treatment, foreign-income exemption eligibility, and DN / ordinary-residence compatibility.
- Pending/open verification queue is now 9, still below the active verification threshold.

## What remains

- Turkey section 5.3 remains partial because the correct Turkish tax structure for a Ukrainian foreign-client IT worker was not proven.
- Turkey cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, citizenship detail, and full relocation budget remain pending.

## Open questions added

- `vq-103`: Turkey DN / ordinary-residence foreign-client IT tax route, including SGK / Bag-Kur, VAT, foreign-income exemption, and immigration-status compatibility.

## Recommendation for next iteration

- Continue `country-deep-dive` mode because the queue is below threshold. Prefer Georgia section 5.3 taxes to continue low-depth Tier-2-hint practical coverage without clustering on Turkey.
