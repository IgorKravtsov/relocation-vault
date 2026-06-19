---
run_id: 158
date: 2026-06-19T12:18:25Z
agent: hermes
mode: country-deep-dive
target_country: Malaysia
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-717", "src-718", "src-719", "src-720"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-malaysia-018", "claim-malaysia-019", "claim-malaysia-020", "claim-malaysia-021"]
files_modified:
  - countries/malaysia.md
  - claims/malaysia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-158-malaysia-healthcare-education.md
proposals_created: []
completed_at: 2026-06-19T12:18:25Z
status: completed
schema_version: 2.0.0
---

# Run 158 - Malaysia healthcare/education

## Plan

- Run a normal `country-deep-dive`: no accepted proposals and the verification queue was below the automatic threshold at pre-flight.
- Select Malaysia rather than the advisory UAE hint because Malaysia is in the minimum-depth Tier-3 cohort at depth 3.0 and has pending healthcare/education sections.

## What was done

- Added a first-pass Malaysia section 5.6 healthcare baseline as partial, anchored on the Ministry of Health and a 2026 private healthcare / insurance guide.
- Added a completed first-pass section 5.7 education baseline from the Ministry of Education and a 2026 schools guide.
- Added four source registry entries: `src-717` through `src-720`.
- Added four atomic claims: `claim-malaysia-018` through `claim-malaysia-021`.
- Added `vq-154` for healthcare insurance/onboarding/provider-price details and `vq-155` for school-fee/private-preschool/non-KL availability details.
- Updated the country profile frontmatter, scoring rows, relocation budget, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 10 pending/open items, meeting the automatic verification threshold.
- Malaysia section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is usable for screening if the couple budgets for private care and DE Rantau-compliant insurance; KL has the deepest hospital/service base, while Penang/Johor/Ipoh need city-specific provider checks.
- Education is viable but not automatically cheap: public schools mean Bahasa Malaysia integration, while KL/Penang international schooling can cost MYR 50,000-120,000/year and is a one-income risk.

## What remains

- Malaysia comfort, partner/student fit, risk dimensions, bureaucracy, durable residence route, DE Rantau long-term conversion, exact insurance policy wording, maternity/newborn terms, school fee schedules, and non-KL bilingual availability remain for later iterations.
- Because the verification queue reached 10 pending/open items, the next iteration should run verification mode unless accepted proposals take priority.

## Open questions added

- `vq-154`: Malaysia route-compliant health-insurance wording, quotes, maternity/newborn terms, onboarding by final status, and city-specific private-care price checks.
- `vq-155`: Malaysia exact international-school fees, private preschool prices, waiting lists, and English/bilingual availability outside Kuala Lumpur/Penang.

## Recommendation for next iteration

- Run `verification` mode and close a focused batch of healthcare/education application-prep blockers now that the queue is at the >=10 threshold.
