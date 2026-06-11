---
run_id: 98
date: 2026-06-11T15:38:28Z
agent: hermes
mode: country-deep-dive
target_country: Kazakhstan
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-482", "src-483", "src-484", "src-485", "src-486"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-kazakhstan-006", "claim-kazakhstan-007", "claim-kazakhstan-008", "claim-kazakhstan-009", "claim-kazakhstan-010"]
files_modified:
  - countries/kazakhstan.md
  - claims/kazakhstan.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-098-kazakhstan-taxes.md
proposals_created: []
completed_at: 2026-06-11T15:38:28Z
status: completed
schema_version: 2.0.0
---

# Run 098 - Kazakhstan taxes

## Plan

- Continue `country-deep-dive` because the pending/open verification queue is below the active threshold.
- Focus on Kazakhstan section 5.3 taxes, following the previous run's hint and rotating from Indonesia to the remaining low-depth post-USSR profile.
- Determine whether Kazakhstan taxes are a blocker if Neo Nomad / TRP becomes a realistic bridge or residence route.

## What was done

- Added a first-pass Kazakhstan §5.3 tax section using PwC Kazakhstan PIT, residence, deductions, income determination, filing, incentives, social-contribution/VAT context, eGov individual-entrepreneur registration, and a current USD/KZT FX snapshot.
- Added five new source registry entries: `src-482` through `src-486`.
- Added five atomic claims: tax residence/scope, PIT bands, deductions/filing, VAT/contribution context, and the USD 3,000/month worked example.
- Added `vq-118` for exact foreign-client IT registration, contribution, VAT/place-of-supply, e-invoice, and residence-status fit.
- Updated the Kazakhstan profile, practical playbook tax step, Block 7/8, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue moved from 8 to 9 pending/open items.
- Kazakhstan section 5.3 moved from pending to partial. Depth score moved from 1.5 to 2.0.

## Key findings

- Kazakhstan residents are taxed on worldwide income; tax residence generally starts at 183 days in a rolling 12-month period, with a centre-of-vital-interest test also relevant for residence-permit holders with family/real estate ties.
- At USD 3,000/month and USD 1 = KZT 488.182834, gross is about KZT 1,464,549/month. PIT-only modelling after the 30 MCI/month basic deduction leaves about KZT 1,331,069/month / USD 2,727 before accountant, VAT, contributions, residence costs, and banking friction.
- The exact contribution and VAT result is not yet filing-ready: employee-style OPC/OMIC exposure, individual-entrepreneur status, Neo Nomad/TRP compatibility, place-of-supply, and e-invoicing need Kazakhstan adviser or tax-authority confirmation.

## What remains

- Kazakhstan cost of living, rent, healthcare, education, comfort, partner/student mechanics, risk dimensions, and bureaucracy remain pending.
- Before filing, confirm Kazakhstan State Revenue Committee / accountant treatment for foreign-client IT registration, contribution base, VAT/place-of-supply, e-invoice handling, and immigration-status compatibility.

## Open questions added

- `vq-118`: exact Kazakhstan foreign-client IT individual-entrepreneur / Neo Nomad tax-registration fit, social-medical-pension contribution base, VAT/place-of-supply and e-invoice handling, and residence-status compatibility.

## Recommendation for next iteration

- Continue `country-deep-dive` while the verification queue remains below threshold. Suggested focus: Armenia section 5.3 taxes, the remaining depth-1.5 post-USSR profile with taxes still pending.
