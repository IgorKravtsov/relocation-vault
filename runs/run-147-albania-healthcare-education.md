---
run_id: 147
date: 2026-06-18T01:20:48Z
agent: hermes
mode: country-deep-dive
target_country: Albania
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-680", "src-681", "src-682", "src-683"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-albania-017", "claim-albania-018", "claim-albania-019", "claim-albania-020"]
files_modified:
  - countries/albania.md
  - claims/albania.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-147-albania-healthcare-education.md
proposals_created: []
completed_at: 2026-06-18T01:20:48Z
status: completed
schema_version: 2.0.0
---

# Run 147 - Albania healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue started below the automatic threshold.
- Follow the anti-clustered state hint for Albania, focusing on sections 5.6 and 5.7 to continue practical healthcare/education coverage across low-depth Tier-2-hint countries.

## What was done

- Added a first-pass Albania section 5.6 healthcare baseline as partial, anchored on the U.S. International Trade Administration healthcare-system overview and preserving private-insurance/public-onboarding gaps.
- Added a completed first-pass Albania section 5.7 education baseline covering preschool, compulsory basic/lower-secondary education, public/private structure, and Tirana International School as an English-language option.
- Added four source registry entries: `src-680` through `src-683`.
- Added four atomic claims: `claim-albania-017` through `claim-albania-020`.
- Added `vq-139` for Albania healthcare application-prep details and `vq-140` for international-school/private-preschool quotes.
- Updated Albania profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 11 pending/open items, which meets the automatic verification threshold.
- Albania section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable but route-sensitive: the public system and compulsory insurance fund exist, yet foreign-resident access and private-policy pricing remain unverified; Tirana is the safest healthcare-practicality base.
- Albania's public education baseline is usable if the family accepts Albanian-language schooling: obligatory education runs from ages 6 to 16, while preschool/ECEC is non-obligatory with half-day public kindergarten free.
- Tirana International School provides a concrete English-language option from preschool, but tuition was not captured, so international schooling remains a budget-risk check.

## What remains

- Albania comfort, partner/student fit, risk dimensions, bureaucracy, permit-renewal practice, health-insurance quotes, foreign-resident public-insurance onboarding, and private-school/preschool fee quotes remain for later iterations.
- Because the pending verification queue is now 11, the next iteration should switch to verification mode.

## Open questions added

- `vq-139`: Albania private health-insurance quotes, maternity/newborn coverage, public-insurance onboarding, and Tirana/Durres/Vlore private-care prices.
- `vq-140`: Albania international-school tuition and private-preschool city quotes.

## Recommendation for next iteration

- Switch to `verification` mode because the pending queue is now at or above the automatic threshold.
