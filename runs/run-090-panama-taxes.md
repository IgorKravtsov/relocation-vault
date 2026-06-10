---
run_id: 90
date: 2026-06-10T14:40:09Z
agent: hermes
mode: country-deep-dive
target_country: Panama
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-444", "src-445", "src-446", "src-447", "src-448"]
facts_added: 9
facts_verified: 0
claims_added: ["claim-panama-007", "claim-panama-008", "claim-panama-009", "claim-panama-010", "claim-panama-011"]
files_modified:
  - countries/panama.md
  - claims/panama.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-090-panama-taxes.md
proposals_created: []
completed_at: 2026-06-10T14:40:09Z
status: completed
schema_version: 2.0.0
---

# Run 090 - Panama taxes

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold at pre-flight.
- Follow the run-089 hint to cover Panama section 5.3 taxes as a low-depth Tier-2-hint profile with taxes still pending.
- Keep the unit focused on a conservative first-pass foreign-client IT model at the couple's USD 3,000/month budget.

## What was done

- Updated Panama section 5.3 from pending to partial.
- Added a worked Panama tax screening model: if foreign-client remote-work income is confirmed as non-Panama-source under the territorial system, USD 3,000/month can screen near USD 3,000 before accountant, banking, insurance, registration, or ITBMS costs.
- Added two downside models: if the income is treated as Panama-source personal-service income, PIT is about USD 312.50/month and net is about USD 2,688/month; with an employee-style 9.75% CSS plus 1.25% education-tax stress test, net is about USD 2,358/month.
- Added five Panama tax sources (`src-444` through `src-448`) and five Panama tax claims (`claim-panama-007` through `claim-panama-011`).
- Added `panama-territorial-tax-source-risk` and `panama-itbms-export-service-gap` risk flags.
- Added `vq-112` for DGI/RUC registration, source classification, CSS/education-tax, ITBMS/export-service handling, and remote-worker / follow-on residence-file compatibility.
- Updated Panama depth_score from 1.5 to 2.0.

## Verification results

- Facts added: 9 tax screening facts.
- Sources added: 5.
- Claims added: 5.
- Verification queue is 8 pending/open items, below the active verification threshold.

## What remains

- Panama cost of living, rent, healthcare, education, comfort, partner/student-specific mechanics, broader risk dimensions, bureaucracy, accountant/lawyer contacts, and full relocation budget remain pending.
- Panama §5.3 remains partial until DGI guidance or a Panamanian accountant confirms source classification for foreign-client IT performed from Panama, DGI/RUC registration duties, CSS/education-tax treatment, ITBMS/export-service handling, invoice wording, and compatibility with the remote-worker visa or later ordinary residence route.

## Open questions added

- `vq-112`: Panama foreign-client IT source classification, DGI/RUC registration, CSS/education-tax, ITBMS/export-service, and immigration-file fit.

## Recommendation for next iteration

- Continue `country-deep-dive` because the pending/open verification queue is below threshold. Suggested focus: Mexico section 5.3 taxes, as another low-depth country with taxes still pending.
