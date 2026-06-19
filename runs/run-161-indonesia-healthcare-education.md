---
run_id: 161
date: 2026-06-19T21:41:23Z
agent: hermes
mode: country-deep-dive
target_country: Indonesia
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-727", "src-728", "src-729", "src-730", "src-731"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-indonesia-016", "claim-indonesia-017", "claim-indonesia-018", "claim-indonesia-019"]
files_modified:
  - countries/indonesia.md
  - claims/indonesia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-161-indonesia-healthcare-education.md
proposals_created: []
completed_at: 2026-06-19T21:41:23Z
status: completed
schema_version: 2.0.0
---

# Run 161 - Indonesia healthcare/education

## Plan

- Run one normal `country-deep-dive` because no accepted proposals exist and the verification queue is below the automatic threshold.
- Follow the state hint and cover Indonesia sections 5.6 healthcare and 5.7 education as one focused unit.

## What was done

- Added first-pass Indonesia section 5.6 healthcare baseline as partial, anchored on the Ministry of Health portal and current expat/private-care evidence.
- Added first-pass Indonesia section 5.7 education baseline as completed, covering public/local Indonesian-language schooling, local private-school costs, and international-school alternatives in Jakarta and Bali.
- Added five source registry entries: `src-727` through `src-731`.
- Added four atomic claims: `claim-indonesia-016` through `claim-indonesia-019`.
- Added `vq-158` for exact insurance/onboarding/provider-price details and `vq-159` for exact school-fee/private-preschool/non-core-city availability details.
- Updated Indonesia frontmatter, scoring rows, practical verdict, relocation budget, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 4.
- Facts verified: 0 queue items.
- Verification queue moved from 2 to 4 pending/open items, still below the automatic verification threshold.
- Indonesia section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Indonesia healthcare is screenable only with private/international insurance and evacuation cover; public BPJS/Puskesmas access should not be assumed for E33G/KITAS planning until final-status onboarding is verified.
- Education is viable but budget-sensitive: local/private Indonesian schools are cheap but language-heavy, while Jakarta/Bali international schools can range from affordable-ish Bali options to premium Jakarta fees that exceed the couple's one-income budget.

## What remains

- Indonesia comfort, partner/student fit, risk dimensions, bureaucracy, E33G long-term conversion, exact insurance policy wording, maternity/newborn terms, school fee schedules, private preschool, and non-Jakarta/Bali bilingual availability remain for later iterations.
- Continue low-depth Tier-3 healthcare/education coverage; Kazakhstan sections 5.6 and 5.7 are the next suggested target unless proposals or the verification threshold take priority.

## Open questions added

- `vq-158`: Indonesia E33G/KITAS-accepted insurance wording, quotes, maternity/newborn terms, BPJS/public onboarding, and city provider prices.
- `vq-159`: Indonesia exact international-school/private-preschool fees, deposits, meals/transport, waiting lists, and non-Jakarta/Bali bilingual availability.

## Recommendation for next iteration

- Resume `country-deep-dive` with Kazakhstan sections 5.6 and 5.7 unless accepted proposals or a verification-threshold trigger takes priority.
