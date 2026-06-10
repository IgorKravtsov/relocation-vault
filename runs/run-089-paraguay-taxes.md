---
run_id: 89
date: 2026-06-10T11:33:02Z
agent: hermes
mode: country-deep-dive
target_country: Paraguay
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-437", "src-438", "src-439", "src-440", "src-441", "src-442", "src-443"]
facts_added: 9
facts_verified: 0
claims_added: ["claim-paraguay-007", "claim-paraguay-008", "claim-paraguay-009", "claim-paraguay-010", "claim-paraguay-011"]
files_modified:
  - countries/paraguay.md
  - claims/paraguay.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-089-paraguay-taxes.md
proposals_created: []
completed_at: 2026-06-10T11:33:02Z
status: completed
schema_version: 2.0.0
---

# Run 089 - Paraguay taxes

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold at pre-flight.
- Follow the run-088 hint to cover Paraguay section 5.3 taxes as a low-depth Tier-2-hint profile with taxes still pending.
- Keep the unit focused on a conservative first-pass foreign-client IT model at the couple's USD 3,000/month budget.

## What was done

- Updated Paraguay section 5.3 from pending to partial.
- Added a worked Paraguay tax screening model: USD 3,000/month is about PYG 18,458,662/month at the run-089 FX snapshot; the PIT-only model leaves about PYG 16,779,463/month / USD 2,727 before accountant/VAT/immigration costs.
- Added an employee-style social-security downside sensitivity using PwC's 9% commercial-entity employee contribution context; this lowers the screen to about PYG 15,284,311/month / USD 2,484. It is explicitly labelled as a stress test, not proof that the same IPS rule applies to a self-employed IT contractor.
- Added a VAT-output stress-test caveat because PwC says VAT applies to individuals rendering personal services and gives a 10% general rate, but this pass did not prove foreign-client IT export/place-of-supply treatment.
- Added seven Paraguay tax / FX sources (`src-437` through `src-443`) and five Paraguay tax claims (`claim-paraguay-007` through `claim-paraguay-011`).
- Added `paraguay-foreign-client-vat-fit-gap` and `paraguay-social-security-category-gap` risk flags.
- Added `vq-111` for DNIT/RUC category, IPS/private social-security treatment, VAT/export-service handling, and lawful-activity residence-file compatibility.
- Updated Paraguay depth_score from 1.5 to 2.0.

## Verification results

- Facts added: 9 tax screening facts.
- Sources added: 7.
- Claims added: 5.
- Verification queue is 7 pending/open items, below the active verification threshold.

## What remains

- Paraguay cost of living, rent, healthcare, education, comfort, partner/student-specific mechanics, risk dimensions, bureaucracy, accountant/lawyer contacts, and full relocation budget remain pending.
- Paraguay §5.3 remains partial until DNIT/RUC, IPS/private social-security, VAT/place-of-supply, and lawful-activity residence compatibility are confirmed by authority guidance or a Paraguayan accountant.

## Open questions added

- `vq-111`: Paraguay foreign-client IT DNIT/RUC, IPS/private social-security, VAT/export-service, and lawful-activity residence-file fit.

## Recommendation for next iteration

- Continue `country-deep-dive` because the pending/open verification queue is below threshold. Suggested focus: Panama section 5.3 taxes, as another low-depth Tier-2-hint country with taxes still pending.
