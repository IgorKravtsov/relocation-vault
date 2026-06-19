---
run_id: 130
date: 2026-06-15T19:30:09Z
agent: hermes
mode: country-deep-dive
target_country: Italy
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 44
sources_added: ["src-616", "src-617", "src-618"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-italy-012", "claim-italy-013", "claim-italy-014", "claim-italy-015"]
files_modified:
  - countries/italy.md
  - claims/italy.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-130-italy-healthcare-education.md
proposals_created: []
completed_at: 2026-06-15T19:30:09Z
status: completed
schema_version: 2.0.0
---

# Run 130 - Italy healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Italy, focusing only on sections 5.6 and 5.7 to keep rotating across Tier-1-hint countries.

## What was done

- Added a first-pass Italy section 5.6 healthcare baseline as partial, because live DN-compliant insurance quotes and selected-city ASL registration steps still need application-prep checks.
- Added a completed first-pass Italy section 5.7 education baseline covering ECEC, compulsory public schooling, childcare cost proxies, and international-school cost risk.
- Added three source registry entries: `src-616` through `src-618`.
- Added four atomic claims: `claim-italy-012` through `claim-italy-015`.
- Added `vq-122` for Italy healthcare application-prep details.
- Updated Italy profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 3.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 3 pending/open items.
- Italy section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 4.0 to 5.5.

## Key findings

- Healthcare is structurally positive once status is secure: TP beneficiaries can register with SSN, and SSN access for residents covers core public care, but DN filing still needs insurance documentation.
- Private doctor-visit proxies are around USD 79.5-117 in screened cities, so occasional private fallback looks manageable but not free.
- Italy education is positive if the couple accepts Italian-language public schooling: compulsory education runs from ages 6 to 16, and 3-6 pre-primary is free.
- Budget risk sits in 0-3 childcare and international school: daycare/preschool proxies range around USD 403-867/month in screened cities, and international primary school is about USD 7.0k-18.2k/year.

## What remains

- Italy comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route, and exact DN insurance / ASL application-prep details remain for later iterations.

## Open questions added

- `vq-122`: DN-compliant private health-insurance quotes for two young adults, maternity waiting periods / exclusions, and selected-city ASL / SSN registration steps.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending queue remains below threshold, preferably Greece 5.6/5.7 to keep rotating through Tier-1-hint countries.
