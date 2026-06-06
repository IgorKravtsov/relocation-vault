---
run_id: 58
date: 2026-06-06T09:48:30Z
agent: hermes
mode: country-deep-dive
target_country: Cyprus
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 50
sources_added: ["src-301", "src-302", "src-303", "src-304", "src-305"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-cyprus-006", "claim-cyprus-007", "claim-cyprus-008", "claim-cyprus-009", "claim-cyprus-010", "claim-cyprus-011"]
files_modified:
  - countries/cyprus.md
  - claims/cyprus.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-058-cyprus-taxes.md
proposals_created: []
completed_at: 2026-06-06T09:48:30Z
status: completed
schema_version: 2.0.0
---

# Run 058 - Cyprus taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue is below the active threshold.
- Follow the prior hint to cover Cyprus section 5.3 taxes without clustering on Greece.
- Focus on a practical first tax pass: tax residence, PIT, self-employed Social Insurance/GHS, filing mechanics, marriage effects, and a USD 3,000/month worked example.

## What was done

- Updated Cyprus section 5.3 from pending to partial.
- Added five Cyprus tax sources (`src-301` through `src-305`) covering official PIT bands, GHS/GESY contribution rates, tax/social registration anchors, PwC tax-residence scope, self-employed Social Insurance, deductions, filing, and individual-taxation mechanics.
- Reused `src-293` for the run-date USD/EUR exchange rate.
- Added six Cyprus tax claims (`claim-cyprus-006` through `claim-cyprus-011`).
- Calculated a first-pass self-employed example: USD 3,000/month equals about EUR 31,152/year; after 16.6% Social Insurance, 4.0% GHS, and PIT with contributions treated as deductible, estimated net is about EUR 1,974/month. Non-deductible sensitivity is about EUR 1,854/month.
- Added risk flag `cyprus-social-insurance-category-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-091` for Cyprus Social Insurance self-employed category / lower and maximum insurable-earnings table and deduction-treatment verification.
- Pending/open verification queue is now 8.

## What remains

- Cyprus section 5.3 remains partial because the exact Social Insurance self-employed category floor/ceiling for an IT freelancer was not cleanly extracted from an official table.
- The DN route remains unrealistic at current income because it requires EUR 3,500/month net after taxes and contributions, while the tax example estimates materially less.
- Cyprus section 5.1 remains partial; cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-091`: current Cyprus Social Insurance self-employed categories / lower and maximum insurable earnings and exact deductibility treatment for the couple's filing posture.

## Recommendation for next iteration

- Continue country-deep-dive mode because the verification queue remains below the active threshold. Prefer another Tier-1-hint low-depth practical section, likely Croatia section 5.3 taxes, rather than clustering on Cyprus.
