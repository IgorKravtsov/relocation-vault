---
run_id: 157
date: 2026-06-19T09:10:43Z
agent: hermes
mode: country-deep-dive
target_country: Argentina
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-713", "src-714", "src-715", "src-716"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-argentina-017", "claim-argentina-018", "claim-argentina-019", "claim-argentina-020"]
files_modified:
  - countries/argentina.md
  - claims/argentina.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-157-argentina-healthcare-education.md
proposals_created: []
completed_at: 2026-06-19T09:10:43Z
status: completed
schema_version: 2.0.0
---

# Run 157 - Argentina healthcare/education

## Plan

- Run a normal `country-deep-dive` because there are no accepted proposals and the verification queue is below the automatic threshold.
- Follow the run-156 hint and open Argentina sections 5.6 and 5.7, continuing healthcare/education coverage for low-depth Tier-3-hint countries.

## What was done

- Added a first-pass Argentina section 5.6 healthcare baseline as partial, anchored on the national Ministry of Health and a 2026 private prepaga / hospital guide.
- Added a completed first-pass section 5.7 education baseline from the national education site plus Argentina private/international-school screening evidence and Lincoln School as a public school-site anchor.
- Added four source registry entries: `src-713` through `src-716`.
- Added four atomic claims: `claim-argentina-017` through `claim-argentina-020`.
- Added `vq-152` for healthcare insurance/onboarding/provider-price details and `vq-153` for school-fee/private-preschool/non-capital availability details.
- Updated the country profile frontmatter, scoring rows, relocation budget, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 8 pending/open items, below the automatic verification threshold of >=10.
- Argentina section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable if the couple budgets for private prepaga coverage and treats Buenos Aires as the service-depth benchmark; exact accepted policy wording, maternity/newborn terms, and city prices remain application-prep work.
- Education is viable at medium confidence through Spanish public schooling or lower-cost bilingual private options. Top Buenos Aires international schools are expensive and should not be the default on one income.

## What remains

- Argentina comfort, partner/student fit, risk dimensions, bureaucracy, durable residence route, tax-registration details, exact health-insurance quotes, prepaga onboarding, school fee schedules, and non-Buenos-Aires bilingual availability remain for later iterations.
- Because the verification queue remains below threshold, continue country-deep-dive with the next low-depth Tier-3 healthcare/education target.

## Open questions added

- `vq-152`: Argentina route-compliant private health-insurance quotes, maternity/newborn terms, public/prepaga onboarding by final status, and selected-city private-care price checks.
- `vq-153`: Argentina exact international/bilingual school fees, private preschool prices, waiting lists, and bilingual/international availability outside Buenos Aires.

## Recommendation for next iteration

- Continue `country-deep-dive` with UAE sections 5.6 and 5.7 unless accepted proposals or a verification-threshold trigger takes priority.
