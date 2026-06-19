---
run_id: 145
date: 2026-06-17T19:02:21Z
agent: hermes
mode: country-deep-dive
target_country: Turkey
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-671", "src-672", "src-673", "src-674", "src-675"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-turkey-019", "claim-turkey-020", "claim-turkey-021", "claim-turkey-022"]
files_modified:
  - countries/turkey.md
  - claims/turkey.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-145-turkey-healthcare-education.md
proposals_created: []
completed_at: 2026-06-17T19:02:21Z
status: completed
schema_version: 2.0.0
---

# Run 145 - Turkey healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the anti-clustered state hint for Turkey, focusing on sections 5.6 and 5.7 to continue practical healthcare/education coverage across low-depth Tier-2-hint countries.

## What was done

- Added a first-pass Turkey section 5.6 healthcare baseline as partial, anchored on residence-file health-insurance requirements plus SGK / Ministry of Health public-system sources.
- Added a completed first-pass Turkey section 5.7 education baseline covering 12-year compulsory education, public preschool cost/access, and Istanbul international-school fee risk.
- Added five source registry entries: `src-671` through `src-675`.
- Added four atomic claims: `claim-turkey-019` through `claim-turkey-022`.
- Added `vq-137` for Turkey healthcare application-prep details.
- Updated Turkey profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 8 pending/open items.
- Turkey section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable but route-sensitive: residence filing needs health-insurance evidence, and SGK / Ministry sources map the public system, but exact DN/self-employed foreign-resident onboarding and private-policy pricing remain open.
- Turkey's education baseline is usable if the family accepts Turkish-language public education: compulsory schooling is 12 years, and public pre-primary services are free where available.
- Istanbul international schooling is not a normal one-income fallback: published 2026/2027 examples run from about TRY 950k/year to above TRY 2.3m/year.

## What remains

- Turkey comfort, partner/student fit, risk dimensions, bureaucracy, citizenship/nationality detail, private-insurance quotes, and exact SGK/GSS onboarding remain for later iterations.
- Continue anti-clustered healthcare/education coverage; Georgia 5.6/5.7 is the suggested next low-depth Tier-2-hint target.

## Open questions added

- `vq-137`: Turkey private health-insurance quotes, maternity/newborn coverage, exact SGK/GSS onboarding by residence route, and Istanbul/Izmir/Antalya private-care checks.

## Recommendation for next iteration

- Continue `country-deep-dive` with Georgia sections 5.6 and 5.7, unless accepted proposals or verification queue growth change the chooser.
