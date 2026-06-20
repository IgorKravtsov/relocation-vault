---
run_id: 162
date: 2026-06-20T00:49:39Z
agent: hermes
mode: country-deep-dive
target_country: Kazakhstan
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-732", "src-733", "src-734", "src-735"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-kazakhstan-016", "claim-kazakhstan-017", "claim-kazakhstan-018", "claim-kazakhstan-019"]
files_modified:
  - countries/kazakhstan.md
  - claims/kazakhstan.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-162-kazakhstan-healthcare-education.md
proposals_created: []
completed_at: 2026-06-20T00:49:39Z
status: completed
schema_version: 2.0.0
---

# Run 162 - Kazakhstan healthcare/education

## Plan

- Run one normal `country-deep-dive` because no accepted proposals exist and the verification queue is below the automatic threshold.
- Follow the state hint and cover Kazakhstan sections 5.6 healthcare and 5.7 education as one focused unit.

## What was done

- Added first-pass Kazakhstan section 5.6 healthcare baseline as partial, anchored on eGov MSHI/SFMA eligibility, Numbeo private/public healthcare proxies, and Livingcost doctor-cost proxies.
- Added first-pass Kazakhstan section 5.7 education baseline as completed, covering public Kazakh/Russian-language schooling, daycare/preschool cost proxies, and international-school alternatives in Almaty and Astana.
- Added four source registry entries: `src-732` through `src-735`.
- Added four atomic claims: `claim-kazakhstan-016` through `claim-kazakhstan-019`.
- Added `vq-160` for exact insurance/onboarding/provider-price details and `vq-161` for exact school-fee/private-preschool/non-core-city availability details.
- Updated Kazakhstan frontmatter, scoring rows, practical verdict, relocation budget, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items.
- Verification queue moved from 4 to 6 pending/open items, still below the automatic verification threshold.
- Kazakhstan section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Kazakhstan healthcare is screenable only with private-insurance budgeting and final-status MSHI checks: eGov limits full state/free-care access to covered resident categories, while temporary stayers have a narrower emergency/dangerous-disease baseline.
- Education is viable but city-dependent: Almaty and Astana have real international-school ecosystems, but premium annual fees can reach roughly KZT 17-18m/year; Shymkent/Aktau keep better budget/climate margins but lack proven English-school supply.

## What remains

- Kazakhstan comfort, partner/student fit, risk dimensions, bureaucracy, Neo Nomad/TRP official mechanics, exact insurance policy wording, maternity/newborn terms, school fee schedules, private preschool, and non-Almaty/Astana bilingual availability remain for later iterations.
- Continue low-depth Tier-3 healthcare/education coverage; Armenia sections 5.6 and 5.7 are the next suggested target unless proposals or the verification threshold take priority.

## Open questions added

- `vq-160`: Kazakhstan accepted insurance wording, quotes, maternity/newborn terms, MSHI/public onboarding, and city provider prices.
- `vq-161`: Kazakhstan exact international-school/private-preschool fees, deposits, meals/transport, waiting lists, public enrollment documents, and non-core-city bilingual availability.

## Recommendation for next iteration

- Resume `country-deep-dive` with Armenia sections 5.6 and 5.7 unless accepted proposals or a verification-threshold trigger takes priority.
