---
run_id: 149
date: 2026-06-18T07:54:44Z
agent: hermes
mode: country-deep-dive
target_country: Uruguay
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 50
sources_added: ["src-684", "src-685", "src-686", "src-687", "src-688"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-uruguay-016", "claim-uruguay-017", "claim-uruguay-018", "claim-uruguay-019"]
files_modified:
  - countries/uruguay.md
  - claims/uruguay.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-149-uruguay-healthcare-education.md
proposals_created: []
completed_at: 2026-06-18T07:54:44Z
status: completed
schema_version: 2.0.0
---

# Run 149 - Uruguay healthcare/education

## Plan

- Run a normal `country-deep-dive` because there are no accepted proposals and the verification queue is below the automatic threshold.
- Use the target-selection rule to prioritize a lowest-depth Tier-2-hint country over the advisory North Macedonia hint; focus on Uruguay sections 5.6 and 5.7.

## What was done

- Added a first-pass Uruguay section 5.6 healthcare baseline as partial, anchored on the SNIS/FONASA/mutualista structure and the health-card procedure already relevant to residence files.
- Added a completed first-pass Uruguay section 5.7 education baseline covering public initial/primary/secondary structure, compulsory/free public education baselines, and Montevideo international-school fee risk.
- Added five source registry entries: `src-684` through `src-688`.
- Added four atomic claims: `claim-uruguay-016` through `claim-uruguay-019`.
- Added `vq-141` for Uruguay healthcare application-prep details.
- Updated Uruguay profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 1 pending/open item, below the automatic verification threshold.
- Uruguay section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Uruguay healthcare screens as practical but route-sensitive: SNIS/FONASA/mutualista coverage is a strong structural baseline, yet exact onboarding and private-policy costs depend on residence and BPS/DGI status.
- Uruguay education is screenable if Spanish-language public schooling is acceptable: compulsory initial education starts at age 4, public primary from age 6 is compulsory/free, and secondary follows from around age 12.
- Montevideo international schools are a major budget risk: a 2026 guide screens English/bilingual/IB options around USD 6,000-18,000/year, so private schooling can consume a large share of a single USD 3,000/month income.

## What remains

- Uruguay comfort, partner/student fit, risk dimensions, bureaucracy, exact residence/tax practice, private health-insurance quotes, FONASA/ASSE/mutualista onboarding, maternity/newborn terms, and private-care price checks remain for later iterations.
- Paraguay 5.6/5.7 is a natural next low-depth Tier-2-hint healthcare/education target.

## Open questions added

- `vq-141`: Uruguay private health-insurance quotes, maternity/newborn terms, exact FONASA/ASSE/mutualista onboarding by residence/self-employed status, and selected-city private GP/pediatric/maternity prices.

## Recommendation for next iteration

- Continue `country-deep-dive` with Paraguay sections 5.6 and 5.7 unless accepted proposals or staleness checks take priority.
