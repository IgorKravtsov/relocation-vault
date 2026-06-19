---
run_id: 132
date: 2026-06-16T01:44:44Z
agent: hermes
mode: country-deep-dive
target_country: Cyprus
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 41
sources_added: ["src-622", "src-623", "src-624", "src-625"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-cyprus-012", "claim-cyprus-013", "claim-cyprus-014", "claim-cyprus-015"]
files_modified:
  - countries/cyprus.md
  - claims/cyprus.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-132-cyprus-healthcare-education.md
proposals_created: []
completed_at: 2026-06-16T01:44:44Z
status: completed
schema_version: 2.0.0
---

# Run 132 - Cyprus healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Cyprus, focusing only on sections 5.6 and 5.7 to keep rotating across Tier-1-hint countries.

## What was done

- Added a first-pass Cyprus section 5.6 healthcare baseline as partial, because live Cyprus-compliant insurance quotes and exact GESY onboarding steps still need application-prep checks.
- Added a completed first-pass Cyprus section 5.7 education baseline covering compulsory/free public education, primary-school age, childcare cost proxies, and international-school cost risk.
- Added four source registry entries: `src-622` through `src-625`.
- Added four atomic claims: `claim-cyprus-012` through `claim-cyprus-015`.
- Added `vq-124` for Cyprus healthcare application-prep details.
- Updated Cyprus profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 5 pending/open items.
- Cyprus section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 4.0 to 5.5.

## Key findings

- Healthcare is workable only with a private-insurance-first plan: DN filing requires medical insurance, and GESY registration should be checked after the exact status/city is selected.
- Private doctor-visit proxies are moderate, around USD 50.9-64.2 in screened cities, but insurance, maternity, specialist, and lab costs remain unquoted.
- Cyprus education is positive if the couple accepts public schooling: compulsory/free education starts at pre-primary age and public primary is a free six-year cycle.
- Budget risk sits in early childcare and international schooling: daycare/preschool proxies are about USD 386-644/month and international primary about USD 6.7k-10.6k/year.

## What remains

- Cyprus comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-insurance / GESY application-prep details remain for later iterations.

## Open questions added

- `vq-124`: DN/residence-compliant private health-insurance quotes, maternity waiting periods/exclusions, and selected-city GESY beneficiary / personal-doctor registration workflow.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending queue remains below threshold, preferably Croatia 5.6/5.7 to keep rotating through Tier-1-hint countries.
