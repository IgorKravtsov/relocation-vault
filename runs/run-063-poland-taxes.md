---
run_id: 63
date: 2026-06-07T01:33:58Z
agent: hermes
mode: country-deep-dive
target_country: Poland
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-320", "src-321", "src-322", "src-323"]
facts_added: 7
facts_verified: 0
claims_added: ["claim-poland-011", "claim-poland-012", "claim-poland-013", "claim-poland-014", "claim-poland-015", "claim-poland-016", "claim-poland-017"]
files_modified:
  - countries/poland.md
  - claims/poland.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-063-poland-taxes.md
proposals_created: []
completed_at: 2026-06-07T01:33:58Z
status: completed
schema_version: 2.0.0
---

# Run 063 - Poland taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue starts below the active threshold.
- Follow the prior hint to cover Poland section 5.3 taxes.
- Focus on a practical first tax pass: tax residence, self-employed PIT forms, IT lump-sum baseline, social/health contribution framework, filing/marriage mechanics, and a USD 3,000/month worked example.

## What was done

- Updated Poland section 5.3 from pending to partial.
- Added four Poland tax sources (`src-320` through `src-323`) covering PwC Poland PIT / residence / social and health / filing context and Biznes.gov.pl business-tax-form guidance.
- Reused `src-293` for the run-date USD/PLN exchange rate.
- Added seven Poland tax claims (`claim-poland-011` through `claim-poland-017`).
- Calculated a first-pass current-income scenario: USD 3,000/month is about PLN 10,918/month or PLN 131,011/year; if 12% IT `ryczalt` applies and the PLN 60,000-300,000 lump-sum health band applies, net is about PLN 8,777/month or USD 2,412/month before uncaptured ZUS social contributions.
- Added risk flags `poland-zus-social-contribution-gap` and `poland-ryczalt-it-rate-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-095` for Poland 2026 ZUS social-contribution amounts, IT `ryczalt` classification, VAT / reverse-charge handling, and immigration-status compatibility.
- Pending/open verification queue is now 7, still below the active verification threshold.

## What remains

- Poland section 5.3 remains partial because the official 2026 ZUS normal / preferential social-contribution table, PKD/PKWiU classification for the exact foreign-client IT activity, VAT / reverse-charge handling, and self-employment compatibility with the immigration file need accountant or authority confirmation.
- Poland cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-095`: Poland 2026 ZUS / IT `ryczalt` / VAT / immigration-status fit for a Ukrainian foreign-client IT freelancer.

## Recommendation for next iteration

- Continue country-deep-dive mode because the queue remains below threshold. Prefer Romania section 5.3 taxes to continue low-depth Tier-2-hint tax coverage without clustering on Poland.
