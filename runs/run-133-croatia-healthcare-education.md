---
run_id: 133
date: 2026-06-16T04:53:48Z
agent: hermes
mode: country-deep-dive
target_country: Croatia
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 42
sources_added: ["src-626", "src-627", "src-628", "src-629", "src-630"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-croatia-012", "claim-croatia-013", "claim-croatia-014", "claim-croatia-015"]
files_modified:
  - countries/croatia.md
  - claims/croatia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-133-croatia-healthcare-education.md
proposals_created: []
completed_at: 2026-06-16T04:53:48Z
status: completed
schema_version: 2.0.0
---

# Run 133 - Croatia healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Croatia, focusing only on sections 5.6 and 5.7 to keep rotating across Tier-1-hint countries.

## What was done

- Added a first-pass Croatia section 5.6 healthcare baseline as partial, because live Croatia-compliant insurance quotes and exact HZZO onboarding steps still need application-prep checks.
- Added a completed first-pass Croatia section 5.7 education baseline covering compulsory public schooling, the mandatory/free pre-primary year, childcare cost proxies, and international-school cost risk.
- Added five source registry entries: `src-626` through `src-630`.
- Added four atomic claims: `claim-croatia-012` through `claim-croatia-015`.
- Added `vq-125` for Croatia healthcare application-prep details.
- Updated Croatia profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 6 pending/open items.
- Croatia section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 4.0 to 5.5.

## Key findings

- Healthcare is workable only after status-specific mapping: HZZO covers compulsory-insurance categories and pregnancy/childbirth care for insured persons, while DN filing still needs private insurance covering Croatia.
- HZZO application/change/deregistration is an 8-day office/branch workflow once the status-triggering circumstance exists.
- Croatia education is positive if the couple accepts Croatian public schooling: compulsory single-structure primary/lower-secondary lasts 8 years and the pre-primary year is mandatory, state-financed, and free for parents.
- Budget risk sits in younger childcare and international school: Livingcost proxies range about $93.9-$488/month for daycare/preschool and $7.3k-$15.0k/year for international primary.

## What remains

- Croatia comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-insurance / HZZO application-prep details remain for later iterations.

## Open questions added

- `vq-125`: DN/residence-compliant private health-insurance quotes, maternity waiting periods/exclusions, and exact HZZO onboarding workflow by status/city.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending queue remains below threshold, preferably Malta 5.6/5.7 to keep rotating through Tier-1-hint countries.
