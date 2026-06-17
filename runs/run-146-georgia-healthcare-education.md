---
run_id: 146
date: 2026-06-17T22:13:03Z
agent: hermes
mode: country-deep-dive
target_country: Georgia
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-676", "src-677", "src-678", "src-679"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-georgia-017", "claim-georgia-018", "claim-georgia-019", "claim-georgia-020"]
files_modified:
  - countries/georgia.md
  - claims/georgia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-146-georgia-healthcare-education.md
proposals_created: []
completed_at: 2026-06-17T22:13:03Z
status: completed
schema_version: 2.0.0
---

# Run 146 - Georgia healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the anti-clustered state hint for Georgia, focusing on sections 5.6 and 5.7 to continue practical healthcare/education coverage across low-depth Tier-2-hint countries.

## What was done

- Added a first-pass Georgia section 5.6 healthcare baseline as partial, anchored on Trade.gov's healthcare-system overview and preserving foreign-resident insurance/public-program gaps.
- Added a completed first-pass Georgia section 5.7 education baseline covering public preschool, compulsory primary/basic education, 12-year general education, and Tbilisi international-school budget risk.
- Added four source registry entries: `src-676` through `src-679`.
- Added four atomic claims: `claim-georgia-017` through `claim-georgia-020`.
- Added `vq-138` for Georgia healthcare application-prep details.
- Updated Georgia profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 9 pending/open items.
- Georgia section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable but not yet application-ready: Georgia's provider market is highly privatized, Universal Healthcare is citizen-focused and still involves out-of-pocket costs, and Tbilisi is the safest healthcare-practicality base.
- Georgia's education baseline is usable for a future child if the family accepts Georgian-language public education: public preschool is free with catering, and primary/basic education are compulsory.
- Tbilisi has an international-school market, but fee transparency is limited; one published German-school range is GEL 10,290-19,670/year for 2025/2026, so international schooling remains a budget-risk check.

## What remains

- Georgia comfort, partner/student fit, risk dimensions, bureaucracy, permit-renewal practice, private-insurance quotes, public-health onboarding, maternity/newborn coverage, and city-specific private-care costs remain for later iterations.
- Continue anti-clustered healthcare/education coverage; Albania 5.6/5.7 is the suggested next low-depth Tier-2-hint target.

## Open questions added

- `vq-138`: Georgia private health-insurance quotes, public-health onboarding, maternity/newborn coverage, and Tbilisi/Batumi/Kutaisi private-care prices.

## Recommendation for next iteration

- Continue `country-deep-dive` with Albania sections 5.6 and 5.7, unless accepted proposals or verification queue growth change the chooser.
