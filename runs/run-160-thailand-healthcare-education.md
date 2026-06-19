---
run_id: 160
date: 2026-06-19T18:42:00Z
agent: hermes
mode: country-deep-dive
target_country: Thailand
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-721", "src-722", "src-723", "src-724", "src-725", "src-726"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-thailand-017", "claim-thailand-018", "claim-thailand-019", "claim-thailand-020"]
files_modified:
  - countries/thailand.md
  - claims/thailand.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-160-thailand-healthcare-education.md
proposals_created: []
completed_at: 2026-06-19T18:42:00Z
status: completed
schema_version: 2.0.0
---

# Run 160 - Thailand healthcare/education

## Plan

- Run one normal `country-deep-dive` because no accepted proposals exist and the verification queue is below the automatic threshold.
- Follow the state hint and cover Thailand sections 5.6 healthcare and 5.7 education as one focused unit.

## What was done

- Added first-pass Thailand section 5.6 healthcare baseline as partial, anchored on Thai health-authority context and expat/private-care evidence.
- Added first-pass Thailand section 5.7 education baseline as completed, covering public Thai-language schooling and international-school alternatives in Bangkok, Chiang Mai, and Phuket.
- Added six source registry entries: `src-721` through `src-726`.
- Added four atomic claims: `claim-thailand-017` through `claim-thailand-020`.
- Added `vq-156` for exact insurance/onboarding/provider-price details and `vq-157` for exact school-fee/private-preschool/non-core-city availability details.
- Updated Thailand frontmatter, scoring rows, practical verdict, relocation budget, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 6.
- Claims added: 4.
- Facts verified: 0 queue items.
- Verification queue moved from 0 to 2 pending/open items, still below the automatic verification threshold.
- Thailand section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Thailand healthcare is screenable if the couple budgets for private/international insurance and private care; Bangkok is the safest services-first base, while Chiang Mai and Phuket need city-specific provider checks.
- Education is viable but budget-sensitive: public schooling means Thai-language integration, while international-school examples range from about THB 248,200/year in Chiang Mai to more than THB 1,000,000/year for premium Bangkok schools.

## What remains

- Thailand comfort, partner/student fit, risk dimensions, bureaucracy, DTV long-term conversion, exact insurance policy wording, maternity/newborn terms, school fee schedules, private preschool, and non-core-city bilingual availability remain for later iterations.
- Continue low-depth Tier-3 healthcare/education coverage; Indonesia sections 5.6 and 5.7 are the next suggested target unless proposals or the verification threshold take priority.

## Open questions added

- `vq-156`: Thailand DTV-accepted insurance wording, quotes, maternity/newborn terms, public/private onboarding, and city provider prices.
- `vq-157`: Thailand exact international-school/private-preschool fees, deposits, meals/transport, waiting lists, and non-core-city bilingual availability.

## Recommendation for next iteration

- Resume `country-deep-dive` with Indonesia sections 5.6 and 5.7 unless accepted proposals or a verification-threshold trigger takes priority.
