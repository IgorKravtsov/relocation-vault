---
run_id: 70
date: 2026-06-07T23:34:54Z
agent: hermes
mode: country-deep-dive
target_country: Slovenia
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-344", "src-345", "src-346", "src-347", "src-348"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-slovenia-009", "claim-slovenia-010", "claim-slovenia-011", "claim-slovenia-012", "claim-slovenia-013"]
files_modified:
  - countries/slovenia.md
  - claims/slovenia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-070-slovenia-taxes.md
proposals_created: []
completed_at: 2026-06-07T23:34:54Z
status: completed
schema_version: 2.0.0
---

# Run 070 - Slovenia taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue started below the active threshold.
- Follow the previous hint to cover Slovenia section 5.3 taxes.
- Focus on a practical first tax pass: tax residence, PIT, social contributions, filing/VAT context, and a USD 3,000/month worked example.

## What was done

- Updated Slovenia section 5.3 from pending to partial.
- Added five Slovenia tax / exchange sources (`src-344` through `src-348`) covering PwC Slovenia tax-residence and PIT, social-security contribution rates, deductions / filing mechanics, VAT context, and ECB EUR/USD exchange rate.
- Added five Slovenia tax claims (`claim-slovenia-009` through `claim-slovenia-013`).
- Calculated a conservative ordinary self-employed stress test: USD 3,000/month is about EUR 2,577/month. Applying a gross-rate 38.2% social-contribution stress test plus progressive PIT after a EUR 5,000 allowance leaves about EUR 1,364/month, or about USD 1,587/month, before accountant/VAT/immigration costs.
- Added risk flag `slovenia-self-employed-tax-and-immigration-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-100` for Slovenian s.p. / normirani / VAT / contribution-base / immigration-status confirmation for a Ukrainian foreign-client IT freelancer.
- Pending/open verification queue is now 6, still below the active verification threshold.

## What remains

- Slovenia section 5.3 remains partial because normirani s.p. eligibility, exact contribution bases, foreign-client VAT/reverse-charge treatment, and immigration-status compatibility are unresolved.
- Slovenia cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-100`: Slovenia s.p. / normirani / VAT / contribution-base / immigration-status fit for a Ukrainian foreign-client IT freelancer.

## Recommendation for next iteration

- Continue `country-deep-dive` mode because the queue is below threshold. Prefer Montenegro section 5.3 taxes to continue low-depth Tier-2-hint practical coverage without clustering on recent countries.
