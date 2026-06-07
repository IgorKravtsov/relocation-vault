---
run_id: 66
date: 2026-06-07T10:58:38Z
agent: hermes
mode: country-deep-dive
target_country: Hungary
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-332", "src-333", "src-334", "src-335", "src-336"]
facts_added: 7
facts_verified: 0
claims_added: ["claim-hungary-010", "claim-hungary-011", "claim-hungary-012", "claim-hungary-013", "claim-hungary-014", "claim-hungary-015", "claim-hungary-016"]
files_modified:
  - countries/hungary.md
  - claims/hungary.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-066-hungary-taxes.md
proposals_created: []
completed_at: 2026-06-07T10:58:38Z
status: completed
schema_version: 2.0.0
---

# Run 066 - Hungary taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue starts below the active threshold.
- Follow the prior hint to cover Hungary section 5.3 taxes.
- Focus on a practical first tax pass: tax residence, PIT, social/security contribution baselines, VAT headline, filing/spouse mechanics, and a USD 3,000/month worked example.

## What was done

- Updated Hungary section 5.3 from pending to partial.
- Added five Hungary tax / exchange sources (`src-332` through `src-336`) covering PwC Hungary tax-residence, PIT, independent-activity tax-base mechanics, social-security / social-tax rates, 2026 minimum wage figures, VAT headline, filing / separate-spouse mechanics, and USD/HUF exchange rate.
- Added seven Hungary tax claims (`claim-hungary-010` through `claim-hungary-016`).
- Calculated a conservative current-income scenario: USD 3,000/month is about HUF 919,157/month. A 90%-of-gross independent-activity base plus 15% PIT, 18.5% social-security contribution, and 13% social-tax sensitivity leaves about HUF 534,490/month (~USD 1,745). A not-yet-verified minimum-base sensitivity leaves about HUF 671,448/month (~USD 2,192).
- Added risk flag `hungary-self-employed-tax-and-immigration-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-098` for Hungary individual-entrepreneur regime, contribution-base, KATA / flat-rate eligibility, VAT / reverse-charge treatment, and immigration-status fit for a Ukrainian foreign-client IT freelancer.
- Pending/open verification queue is now 10, which reaches the active verification threshold.

## What remains

- Hungary section 5.3 remains partial because the exact individual-entrepreneur registration route, 2026 self-employed contribution base, KATA / flat-rate availability for foreign-client IT, VAT / reverse-charge reporting, and White Card versus guest self-employment immigration-status compatibility need NAV/accountant and immigration confirmation.
- Hungary cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-098`: Hungary individual-entrepreneur tax regime / contribution-base / VAT / immigration-status fit for a Ukrainian foreign-client IT freelancer.

## Recommendation for next iteration

- Switch to `verification` mode because the pending/open queue reached 10 after this run. Prioritize recent tax blockers where a conservative operational answer can be closed without changing country scoring prematurely.
