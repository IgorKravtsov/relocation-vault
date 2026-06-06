---
run_id: 59
date: 2026-06-06T12:56:27Z
agent: hermes
mode: country-deep-dive
target_country: Croatia
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 55
sources_added: ["src-306", "src-307", "src-308", "src-309", "src-310"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-croatia-006", "claim-croatia-007", "claim-croatia-008", "claim-croatia-009", "claim-croatia-010", "claim-croatia-011"]
files_modified:
  - countries/croatia.md
  - claims/croatia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-059-croatia-taxes.md
proposals_created: []
completed_at: 2026-06-06T12:56:27Z
status: completed
schema_version: 2.0.0
---

# Run 059 - Croatia taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue is below the active threshold.
- Follow the prior hint to cover Croatia section 5.3 taxes without clustering on Cyprus.
- Focus on a practical first tax pass: tax residence, ordinary self-employment PIT, social contributions, personal/dependent allowances, VAT/filing mechanics, and a USD 3,000/month worked example.

## What was done

- Updated Croatia section 5.3 from pending to partial.
- Added five Croatia tax sources (`src-306` through `src-310`) covering PwC Croatia tax-residence, PIT bands/local-rate mechanics, self-employment income determination, lump-sum taxation threshold, personal allowances, social contributions, VAT, no-joint-filing baseline, and filing mechanics.
- Reused `src-293` for the run-date USD/EUR exchange rate.
- Added six Croatia tax claims (`claim-croatia-006` through `claim-croatia-011`).
- Calculated a conservative ordinary self-employment stress test: USD 3,000/month equals about EUR 31,152/year; after 36.5% pension/health contributions, EUR 600/month personal allowance, and 15%-23% lower-bracket PIT, estimated net is about EUR 1,407-1,491/month.
- Added risk flags `croatia-self-employed-contribution-base-gap` and `croatia-lump-sum-obrt-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-092` for Croatia 2026 self-employed / craft contribution base, lump-sum craft fit for foreign-client IT, VAT/reverse-charge handling, and dependent allowance treatment.
- Pending/open verification queue is now 9.

## What remains

- Croatia section 5.3 remains partial because the ordinary stress test may be overly conservative if the lump-sum craft route applies.
- A Croatian accountant or official 2026 contribution table is needed before scoring Croatia taxes as workable or unworkable.
- Croatia section 5.1 remains partial; cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-092`: current Croatia 2026 self-employed / craft contribution base and lump-sum craft fit for a Ukrainian foreign-client IT freelancer, including VAT/reverse-charge handling and dependent allowance treatment.

## Recommendation for next iteration

- Continue country-deep-dive mode because the verification queue remains below the active threshold. Prefer another Tier-1-hint practical tax section, likely Malta section 5.3, rather than clustering on Croatia.
