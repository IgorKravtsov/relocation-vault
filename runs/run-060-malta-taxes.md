---
run_id: 60
date: 2026-06-06T16:06:18Z
agent: hermes
mode: country-deep-dive
target_country: Malta
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 55
sources_added: ["src-311", "src-312", "src-313", "src-314", "src-315"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-malta-006", "claim-malta-007", "claim-malta-008", "claim-malta-009", "claim-malta-010", "claim-malta-011"]
files_modified:
  - countries/malta.md
  - claims/malta.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-060-malta-taxes.md
proposals_created: []
completed_at: 2026-06-06T16:06:18Z
status: completed
schema_version: 2.0.0
---

# Run 060 - Malta taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue starts below the active threshold.
- Follow the prior hint to cover Malta section 5.3 taxes without clustering on Croatia.
- Focus on a practical first tax pass: tax-residence scope, ordinary PIT, NRP authorised-work taxation, social security, VAT, filing mechanics, marriage effects, and USD 3,000/month examples.

## What was done

- Updated Malta section 5.3 from pending to partial.
- Added five Malta tax sources (`src-311` through `src-315`) covering PwC Malta tax residence, 2026 PIT bands, NRP authorised-work taxation, self-employed social security, VAT, deductions, tax administration, and the Legislation Malta legal-notice metadata anchor.
- Reused `src-293` for the run-date USD/EUR exchange rate.
- Added six Malta tax claims (`claim-malta-006` through `claim-malta-011`).
- Calculated current-income examples: USD 3,000/month is about EUR 31,152/year; ordinary self-employed stress test nets about EUR 1,867/month single or EUR 1,963/month married after PIT and capped 2026 social security; NRP 10% PIT-only net would be about EUR 2,336/month but the NRP threshold is not met.
- Added risk flag `malta-nrp-authorized-work-tax-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-093` for Malta NRP authorised-work tax / social-security / VAT / source-remittance treatment.
- Pending/open verification queue is now 10, so the next iteration should switch to verification mode under the active threshold rule.

## What remains

- Malta section 5.3 remains partial because the exact NRP tax-regime fit, Class Two social security, VAT small-enterprise / place-of-supply treatment, and source/remittance classification need official rule-text extraction or adviser confirmation.
- Malta remains income-blocked for the couple's current budget because NRP requires EUR 42,000/year gross while USD 3,000/month is about EUR 31,152/year.
- Malta cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-093`: exact Malta NRP authorised-work tax / social-security / VAT treatment for a Ukrainian foreign-client IT worker.

## Recommendation for next iteration

- Switch to verification mode because the pending/open verification queue has reached 10. Start with the newest tax blockers (`vq-089` through `vq-093`) or batch them with Armenia / Albania legal blockers if source access is easier.
