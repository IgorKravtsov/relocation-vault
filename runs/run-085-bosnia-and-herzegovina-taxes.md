---
run_id: 85
date: 2026-06-09T22:57:50Z
agent: hermes
mode: country-deep-dive
target_country: Bosnia and Herzegovina
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-418", "src-419", "src-420", "src-421", "src-422", "src-423"]
facts_added: 9
facts_verified: 0
claims_added: ["claim-bosnia-herzegovina-007", "claim-bosnia-herzegovina-008", "claim-bosnia-herzegovina-009", "claim-bosnia-herzegovina-010", "claim-bosnia-herzegovina-011"]
files_modified:
  - countries/bosnia-and-herzegovina.md
  - claims/bosnia-and-herzegovina.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-085-bosnia-and-herzegovina-taxes.md
proposals_created: []
completed_at: 2026-06-09T22:57:50Z
status: completed
schema_version: 2.0.0
---

# Run 085 - Bosnia and Herzegovina taxes

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold.
- Follow the run-084 hint to cover Bosnia and Herzegovina section 5.3 taxes as a fresh low-depth Tier-3-hint profile with taxes still pending.
- Keep the unit focused on a conservative first-pass foreign-client IT model at the couple's USD 3,000/month budget.

## What was done

- Updated Bosnia and Herzegovina section 5.3 from pending to partial.
- Added an entity-based worked tax screening model: USD 3,000/month is about BAM 5,088.54/month at the run-085 FX snapshot; PIT-only leaves about BAM 4,579.69-4,681.46/month / USD 2,700-2,760, while FBiH / RS employee-style contribution stress tests leave about BAM 3,185.94-3,189.98/month / USD 1,878-1,881 before accountant/VAT/immigration costs.
- Added six Bosnia and Herzegovina tax / FX sources (`src-418` through `src-423`) and five Bosnia and Herzegovina tax claims (`claim-bosnia-herzegovina-007` through `claim-bosnia-herzegovina-011`).
- Added `bosnia-entity-tax-and-ssc-fit-gap` and `bosnia-foreign-client-vat-fit-gap` risk flags.
- Added `vq-108` for legal form, contribution base, VAT/place-of-supply, and residence-route compatibility.
- Updated Bosnia and Herzegovina depth_score from 1.5 to 2.0.

## Verification results

- Facts added: 9 tax screening facts.
- Sources added: 6.
- Claims added: 5.
- Verification queue is 9 pending/open items, below the active verification threshold of 10.

## What remains

- Bosnia and Herzegovina cost of living, rent, healthcare, education, comfort, partner/student-specific mechanics, risk dimensions, bureaucracy, citizenship, and full relocation budget remain pending.
- Bosnia and Herzegovina §5.3 remains partial until FBiH/RS/Brcko tax authority guidance or a Bosnia accountant confirms the exact legal form, contribution base, VAT/place-of-supply treatment, and immigration-status compatibility for a Ukrainian foreign-client IT worker.

## Open questions added

- `vq-108`: Bosnia and Herzegovina foreign-client IT tax legal-form / SSC / VAT / residence-route fit.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending/open verification queue remains below the active threshold. Suggested next focus: Moldova section 5.3 taxes, as another fresh low-depth Tier-3-hint profile with taxes still pending.
