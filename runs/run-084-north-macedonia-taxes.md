---
run_id: 84
date: 2026-06-09T19:49:41Z
agent: hermes
mode: country-deep-dive
target_country: North Macedonia
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-413", "src-414", "src-415", "src-416", "src-417"]
facts_added: 8
facts_verified: 0
claims_added: ["claim-north-macedonia-007", "claim-north-macedonia-008", "claim-north-macedonia-009", "claim-north-macedonia-010", "claim-north-macedonia-011"]
files_modified:
  - countries/north-macedonia.md
  - claims/north-macedonia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-084-north-macedonia-taxes.md
proposals_created: []
completed_at: 2026-06-09T19:49:41Z
status: completed
schema_version: 2.0.0
---

# Run 084 - North Macedonia taxes

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold.
- Follow the run-083 hint to cover North Macedonia section 5.3 taxes as a fresh low-depth Tier-3-hint profile with taxes still pending.
- Keep the unit focused on a conservative first-pass foreign-client IT model at the couple's USD 3,000/month budget.

## What was done

- Updated North Macedonia section 5.3 from pending to partial.
- Added a worked tax screening model: USD 3,000/month is about MKD 158,949/month at the run-084 FX snapshot; PIT-only 10% leaves about MKD 143,055/month / USD 2,700, while a conservative gross-base 10% PIT plus 28% employee-style contribution stress test leaves about MKD 98,549/month / USD 1,860 before accountant/VAT/immigration costs.
- Added five North Macedonia tax / FX sources (`src-413` through `src-417`) and five North Macedonia tax claims (`claim-north-macedonia-007` through `claim-north-macedonia-011`).
- Added `north-macedonia-self-employed-contribution-base-gap` and `north-macedonia-foreign-client-vat-fit-gap` risk flags.
- Added `vq-107` for registration category, contribution base/order, VAT/place-of-supply, and residence-route compatibility.
- Updated North Macedonia depth_score from 1.5 to 2.0.

## Verification results

- Facts added: 8 tax screening facts.
- Sources added: 5.
- Claims added: 5.
- Verification queue is 8 pending/open items, below the active verification threshold.

## What remains

- North Macedonia cost of living, rent, healthcare, education, comfort, partner/student-specific mechanics, risk dimensions, bureaucracy, and full relocation budget remain pending.
- North Macedonia §5.3 remains partial until Public Revenue Office / Central Register / accountant evidence confirms the exact self-employed or company-manager structure, contribution base and ordering, VAT/place-of-supply treatment, and immigration-status compatibility.

## Open questions added

- `vq-107`: North Macedonia self-employed / company-manager tax fit for a Ukrainian foreign-client IT worker.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending/open verification queue remains below the active threshold. Suggested next focus: Bosnia and Herzegovina section 5.3 taxes, as another fresh low-depth Tier-3-hint profile with taxes still pending.
