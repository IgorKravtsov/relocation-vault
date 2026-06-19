---
run_id: 131
date: 2026-06-15T22:39:01Z
agent: hermes
mode: country-deep-dive
target_country: Greece
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 39
sources_added: ["src-619", "src-620", "src-621"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-greece-013", "claim-greece-014", "claim-greece-015"]
files_modified:
  - countries/greece.md
  - claims/greece.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-131-greece-healthcare-education.md
proposals_created: []
completed_at: 2026-06-15T22:39:01Z
status: completed
schema_version: 2.0.0
---

# Run 131 - Greece healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Greece, focusing only on sections 5.6 and 5.7 to keep rotating across Tier-1-hint countries.

## What was done

- Added a first-pass Greece section 5.6 healthcare baseline as partial, because route-compliant insurance quotes and city-level AMKA / health-unit onboarding still need application-prep checks.
- Added a completed first-pass Greece section 5.7 education baseline covering compulsory public pre-primary/schooling, under-age-4 childcare risk, and international-school cost risk.
- Added three source registry entries: `src-619` through `src-621`.
- Added three atomic claims: `claim-greece-013` through `claim-greece-015`.
- Added `vq-123` for Greece healthcare application-prep details.
- Updated Greece profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 3.
- Claims added: 3.
- Facts verified: 0 queue items; verification queue now has 4 pending/open items.
- Greece section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 4.0 to 5.5.

## Key findings

- Healthcare is structurally workable for protected/resident statuses: UNHCR Greece documents free public healthcare access for refugees/asylum seekers and PAAYPA/AMKA mechanics.
- Private care appears usable for occasional fallback: Livingcost doctor-visit proxies are about USD 37-55 in screened cities, but insurance and maternity details remain unquoted.
- Greece education is positive if the couple accepts Greek-language public schooling: compulsory pre-primary begins at age 4 and public nipiagogeia is free.
- Budget risk sits in under-age-4 childcare and international school: city proxies range around USD 436-641/month for daycare/preschool and USD 4.3k-13.3k/year for international primary school.

## What remains

- Greece comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route, and exact DN/private-insurance / AMKA application-prep details remain for later iterations.

## Open questions added

- `vq-123`: DN/residence-compliant private health-insurance quotes for two young adults, maternity waiting periods / exclusions, and selected-city AMKA / health-unit onboarding workflow.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending queue remains below threshold, preferably Cyprus 5.6/5.7 to keep rotating through Tier-1-hint countries.
