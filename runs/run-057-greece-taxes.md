---
run_id: 57
date: 2026-06-06T06:39:40Z
agent: hermes
mode: country-deep-dive
target_country: Greece
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 55
sources_added: ["src-294", "src-295", "src-296", "src-297", "src-298", "src-299", "src-300"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-greece-006", "claim-greece-007", "claim-greece-008", "claim-greece-009", "claim-greece-010", "claim-greece-011"]
files_modified:
  - countries/greece.md
  - claims/greece.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-057-greece-taxes.md
proposals_created: []
completed_at: 2026-06-06T06:39:40Z
status: completed
schema_version: 2.0.0
---

# Run 057 - Greece taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue is below the active threshold.
- Follow the prior hint to cover Greece section 5.3 taxes without clustering on Italy.
- Focus on a practical first tax pass: tax-residence scope, freelancer/business-profit PIT, registration route, filing and marriage mechanics, Article 5C upside, and a USD 3,000/month worked example.

## What was done

- Updated Greece section 5.3 from pending to partial.
- Added seven Greece tax sources (`src-294` through `src-300`) covering AADE tax residence, AADE TIN/authentication and activity-commencement procedures, PwC PIT / income-determination / VAT and filing context, and AADE/PwC Article 5C new-tax-resident relief.
- Reused `src-293` for the run-date USD/EUR exchange rate.
- Added six Greece tax claims (`claim-greece-006` through `claim-greece-011`).
- Calculated a PIT-only example: USD 3,000/month equals about EUR 31,152/year at run-date FX; ordinary Greek business-profit PIT is about EUR 5,892/year, leaving about EUR 2,105/month before EFKA, VAT/accounting costs, rent, and living costs.
- Added a clearly labelled Article 5C upside scenario: if the 50% income-tax exemption applies, PIT-only net is about EUR 2,428/month before EFKA and accountant/VAT mechanics.
- Added two risk flags: `greece-efka-self-employed-contribution-gap` and `greece-article-5c-foreign-client-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added two new verification items: `vq-089` for current official EFKA self-employed/freelancer contribution categories and monthly minimums, and `vq-090` for Article 5C applicability to a foreign-client IT freelancer / digital-nomad file.
- Pending/open verification queue is now 7.

## What remains

- Greece section 5.3 remains partial because the EFKA self-employed contribution amount is material to actual take-home pay and was not cleanly captured from an official source.
- Article 5C should not be used as the default tax score until a Greek tax adviser or official-practice source confirms that the couple's likely foreign-client IT structure qualifies.
- Greece section 5.1 remains partial; cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-089`: current Greek EFKA self-employed / freelancer insurance contribution categories and monthly minimum for a solo foreign-client IT freelancer.
- `vq-090`: Article 5C applicability to a Ukrainian foreign-client IT freelancer / sole proprietor, including DN-status compatibility.

## Recommendation for next iteration

- Continue country-deep-dive mode because the verification queue remains below the active threshold. Prefer another Tier-1-hint low-depth practical tax section, likely Cyprus section 5.3, rather than clustering on Greece.
