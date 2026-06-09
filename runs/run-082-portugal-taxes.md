---
run_id: 82
date: 2026-06-09T13:31:41Z
agent: hermes
mode: country-deep-dive
target_country: Portugal
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-401", "src-402", "src-403", "src-404", "src-405", "src-406"]
facts_added: 9
facts_verified: 0
claims_added: ["claim-portugal-006", "claim-portugal-007", "claim-portugal-008", "claim-portugal-009", "claim-portugal-010"]
files_modified:
  - countries/portugal.md
  - claims/portugal.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-082-portugal-taxes.md
proposals_created: []
completed_at: 2026-06-09T13:31:41Z
status: completed
schema_version: 2.0.0
---

# Run 082 - Portugal taxes

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold.
- Use the previous hint to cover Portugal section 5.3 taxes without repeating Italy.
- Keep the unit focused on a conservative first-pass ordinary self-employment model for the couple's USD 3,000/month budget.

## What was done

- Updated Portugal section 5.3 from pending to partial.
- Added a worked ordinary simplified-regime stress test for USD 3,000/month: about EUR 1,862/month net singly, or EUR 1,949/month under a joint-rate sensitivity before accountant/VAT/immigration costs.
- Added six Portugal tax sources (`src-401` through `src-406`) and five Portugal tax claims (`claim-portugal-006` through `claim-portugal-010`).
- Added `portugal-self-employed-tax-burden` and `portugal-foreign-client-vat-fit-gap` risk flags.
- Added `vq-105` for accountant/application-prep verification of Article 151 activity mapping, VAT/place-of-supply, social-security timing, expense evidence, and D8 / ordinary-status compatibility.
- Updated Portugal depth_score from 3.0 to 3.5.

## Verification results

- Facts added: 9 tax screening facts.
- Sources added: 6.
- Claims added: 5.
- Verification queue is 6 pending/open items, below the active verification threshold.

## What remains

- Portugal healthcare, education, comfort, partner/student-specific mechanics, risk dimensions, bureaucracy, and full relocation budget remain pending.
- Portugal §5.3 remains partial until accountant / authority evidence confirms exact IT activity classification, VAT/reverse-charge handling, social-security timing/base details, deductible-expense evidence, and immigration-status compatibility.

## Open questions added

- `vq-105`: Portugal self-employed tax fit for a Ukrainian foreign-client IT freelancer.

## Recommendation for next iteration

- Continue `country-deep-dive` mode while avoiding another immediate Tier-1 tax iteration. Suggested next focus: Albania section 5.3 taxes, as the lowest-depth Tier-2-hint profile with taxes still pending.
