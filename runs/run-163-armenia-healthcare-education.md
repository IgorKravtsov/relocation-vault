---
run_id: 163
date: 2026-06-20T03:56:53Z
agent: hermes
mode: country-deep-dive
target_country: Armenia
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-736", "src-737", "src-738", "src-739"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-armenia-015", "claim-armenia-016", "claim-armenia-017", "claim-armenia-018"]
files_modified:
  - countries/armenia.md
  - claims/armenia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-163-armenia-healthcare-education.md
proposals_created: []
completed_at: 2026-06-20T03:56:53Z
status: completed
schema_version: 2.0.0
---

# Run 163 - Armenia healthcare/education

## Plan

- Run one normal `country-deep-dive` because no accepted proposals exist and the verification queue is below the automatic threshold.
- Follow the state hint and cover Armenia sections 5.6 healthcare and 5.7 education as one focused unit.

## What was done

- Added first-pass Armenia section 5.6 healthcare baseline as partial, anchored on Numbeo healthcare proxies plus Livingcost doctor-visit cost proxies and the existing residence-file context.
- Added first-pass Armenia section 5.7 education baseline as completed, covering public-school structure, childcare cost proxies, QSI Yerevan, and UWC Dilijan.
- Added four source registry entries: `src-736` through `src-739`.
- Added four atomic claims: `claim-armenia-015` through `claim-armenia-018`.
- Added `vq-162` for exact insurance/onboarding/provider-price details and `vq-163` for exact school-fee/private-preschool/non-Yerevan availability details.
- Updated Armenia frontmatter, scoring rows, practical verdict, relocation budget, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items.
- Verification queue moved from 6 to 8 pending/open items, still below the automatic verification threshold.
- Armenia section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Armenia healthcare is screenable only with private/international insurance and Yerevan-first provider checks; doctor-visit proxies are low, but residence-file policy wording, public onboarding, and maternity/newborn terms remain uncaptured.
- Education is viable but Yerevan-centric for English-first schooling: public/local schooling implies Armenian/Russian integration, QSI Yerevan is the main captured English-school anchor, and UWC Dilijan is an expensive older-student IB option.

## What remains

- Armenia comfort, partner/student fit, risk dimensions, bureaucracy, business-residence mechanics, exact insurance policy wording, maternity/newborn terms, QSI/current school fee schedules, private preschool, and non-Yerevan bilingual availability remain for later iterations.
- Continue low-depth Tier-3 healthcare/education coverage; UAE sections 5.6 and 5.7 are the next suggested target unless proposals or the verification threshold take priority.

## Open questions added

- `vq-162`: Armenia accepted insurance wording, quotes, maternity/newborn terms, public-system onboarding, and city provider prices.
- `vq-163`: Armenia exact international-school/private-preschool fees, deposits, meals/transport, waiting lists, public enrollment documents, and non-Yerevan bilingual availability.

## Recommendation for next iteration

- Resume `country-deep-dive` with UAE sections 5.6 and 5.7 unless accepted proposals or a verification-threshold trigger takes priority.
