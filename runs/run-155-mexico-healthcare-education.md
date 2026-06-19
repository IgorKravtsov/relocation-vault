---
run_id: 155
date: 2026-06-19T03:01:21Z
agent: hermes
mode: country-deep-dive
target_country: Mexico
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-709", "src-710", "src-711", "src-712"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-mexico-017", "claim-mexico-018", "claim-mexico-019", "claim-mexico-020"]
files_modified:
  - countries/mexico.md
  - claims/mexico.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-155-mexico-healthcare-education.md
proposals_created: []
completed_at: 2026-06-19T03:01:21Z
status: completed
schema_version: 2.0.0
---

# Run 155 - Mexico healthcare/education

## Plan

- Run a normal `country-deep-dive` because there are no accepted proposals and the verification queue was below the automatic threshold at pre-flight.
- Follow the run-154 hint and open Mexico sections 5.6 and 5.7, continuing healthcare/education coverage for low-depth Tier-3-hint countries.

## What was done

- Added a first-pass Mexico section 5.6 healthcare baseline as partial, anchored on Trade.gov, official Secretariat of Health / IMSS public sites, and a 2026 private-insurance / private-care proxy.
- Added a completed first-pass section 5.7 education baseline from SEP plus Mexico City / Guadalajara international-school anchors and broad school-cost proxies.
- Added four source registry entries: `src-709` through `src-712`.
- Added four atomic claims: `claim-mexico-017` through `claim-mexico-020`.
- Added `vq-150` for healthcare insurance/onboarding/provider-price details and `vq-151` for school-fee/private-preschool/non-capital availability details.
- Updated the country profile frontmatter, scoring rows, relocation budget, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 11 pending/open items, reaching the automatic verification threshold of >=10.
- Mexico section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable in major cities but not application-ready: Mexico has public and private providers, with IMSS / IMSS-Bienestar as key public anchors and stronger private hospitals concentrated in large urban markets.
- Private insurance is a likely practical requirement for comfort even if not captured as a residence-file requirement; exact accepted policies, maternity/newborn terms, IMSS enrollment, and city prices remain open.
- Education is viable at medium confidence if the family accepts Spanish public schooling or budgets for private/bilingual options. Top Mexico City international schools are expensive on one income, while Guadalajara or Spanish/bilingual options look more realistic.

## What remains

- Mexico comfort, partner/student fit, risk dimensions, bureaucracy, citizenship/naturalization details, exact health-insurance quotes, IMSS onboarding, school fee schedules, and private preschool prices remain for later iterations.
- Because the verification queue reached the protocol threshold, the next iteration should run `verification` before continuing the remaining low-depth Tier-3 healthcare/education targets.

## Open questions added

- `vq-150`: Mexico route-compliant private health-insurance quotes, maternity/newborn terms, IMSS / IMSS-Bienestar onboarding by final status, and selected-city private-care price checks.
- `vq-151`: Mexico exact international/bilingual school fees, private preschool prices, waiting lists, and English/bilingual availability outside Mexico City / Guadalajara.

## Recommendation for next iteration

- Run `verification` mode because pending/open verification items are now >=10.
