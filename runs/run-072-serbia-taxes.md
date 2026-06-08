---
run_id: 72
date: 2026-06-08T05:48:14Z
agent: hermes
mode: country-deep-dive
target_country: Serbia
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 50
sources_added: ["src-353", "src-354", "src-355", "src-356", "src-357", "src-358"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-serbia-011", "claim-serbia-012", "claim-serbia-013", "claim-serbia-014", "claim-serbia-015"]
files_modified:
  - countries/serbia.md
  - claims/serbia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-072-serbia-taxes.md
proposals_created: []
completed_at: 2026-06-08T05:48:14Z
status: completed
schema_version: 2.0.0
---

# Run 072 - Serbia taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue started below the active threshold.
- Follow the previous hint to cover Serbia section 5.3 taxes.
- Focus on a practical first tax pass: tax residence, PIT / self-employment framework, official freelancer portal baseline for foreign-payer income, SSC/VAT context, and a USD 3,000/month worked example.

## What was done

- Updated Serbia section 5.3 from pending to partial.
- Added six Serbia tax / FX sources (`src-353` through `src-358`) covering PwC Serbia tax residence, PIT / self-employment income determination, the official freelancer portal, SSC / filing mechanics, VAT context, and XE USD/RSD exchange rate.
- Added five Serbia tax claims (`claim-serbia-011` through `claim-serbia-015`).
- Calculated a conservative tax stress test: USD 3,000/month is about RSD 302,160/month. A gross-base 10% PIT + 35.05% combined-SSC sensitivity leaves about RSD 166,037/month (~USD 1,649), while a 20% expense-base sensitivity leaves about RSD 193,262/month (~USD 1,919), before accountant/VAT/immigration costs.
- Added risk flag `serbia-freelancer-tax-and-single-permit-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-102` for Serbia freelancer / entrepreneur classification, APR activity, lump-sum or expense treatment, social-contribution base, VAT / reverse-charge / e-invoicing, and single-permit compatibility.
- Pending/open verification queue is now 8, still below the active verification threshold.

## What remains

- Serbia section 5.3 remains partial because the exact foreign-client IT tax route and its fit with the MUP single-permit file are unresolved.
- Serbia cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-102`: Serbia foreign-client IT tax / APR registration / VAT / contribution-base / single-permit compatibility.

## Recommendation for next iteration

- Continue `country-deep-dive` mode because the queue is below threshold. Prefer Turkey section 5.3 taxes to continue low-depth Tier-2-hint practical coverage without clustering on Serbia.
