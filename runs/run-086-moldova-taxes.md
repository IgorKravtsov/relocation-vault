---
run_id: 86
date: 2026-06-10T02:06:06Z
agent: hermes
mode: country-deep-dive
target_country: Moldova
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-424", "src-425", "src-426", "src-427", "src-428", "src-429"]
facts_added: 9
facts_verified: 0
claims_added: ["claim-moldova-007", "claim-moldova-008", "claim-moldova-009", "claim-moldova-010", "claim-moldova-011"]
files_modified:
  - countries/moldova.md
  - claims/moldova.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-086-moldova-taxes.md
proposals_created: []
completed_at: 2026-06-10T02:06:06Z
status: completed
schema_version: 2.0.0
---

# Run 086 - Moldova taxes

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold at pre-flight.
- Follow the run-085 hint to cover Moldova section 5.3 taxes as a fresh low-depth Tier-3-hint profile with taxes still pending.
- Keep the unit focused on a conservative first-pass foreign-client IT model at the couple's USD 3,000/month budget.

## What was done

- Updated Moldova section 5.3 from pending to partial.
- Added a worked Moldova tax screening model: USD 3,000/month is about MDL 51,983/month at the run-086 FX snapshot; PIT-only 12% leaves about MDL 45,745/month / USD 2,640, while a fixed 2026 SSC + health contribution sensitivity leaves about MDL 42,786-43,141/month / USD 2,469-2,490 before accountant/VAT/immigration costs.
- Added six Moldova tax / FX sources (`src-424` through `src-429`) and five Moldova tax claims (`claim-moldova-007` through `claim-moldova-011`).
- Added `moldova-entrepreneur-contribution-category-gap` and `moldova-foreign-client-vat-fit-gap` risk flags.
- Added `vq-109` for registration category, fixed-contribution treatment, VAT/place-of-supply, and DN/provisional-stay compatibility.
- Updated Moldova depth_score from 1.5 to 2.0.

## Verification results

- Facts added: 9 tax screening facts.
- Sources added: 6.
- Claims added: 5.
- Verification queue is 10 pending/open items, meeting the active verification threshold.

## What remains

- Moldova cost of living, rent, healthcare, education, comfort, partner/student-specific mechanics, risk dimensions, bureaucracy, citizenship, and full relocation budget remain pending.
- Moldova §5.3 remains partial until Moldovan State Tax Service / CNAS / CNAM guidance or a Moldova accountant confirms the exact individual-entrepreneur / professional-services category, contribution base, VAT/place-of-supply treatment, and immigration-status compatibility for a Ukrainian foreign-client IT worker.

## Open questions added

- `vq-109`: Moldova foreign-client IT tax registration / fixed-contribution / VAT / DN-provisional-stay fit.

## Recommendation for next iteration

- Switch to `verification` mode because the pending/open verification queue is now 10, meeting the active threshold (>= 10). Suggested next focus: close the oldest actionable tax-fit blockers to conservative screening baselines where possible.
