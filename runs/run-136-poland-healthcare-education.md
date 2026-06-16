---
run_id: 136
date: 2026-06-16T14:41:19Z
agent: hermes
mode: country-deep-dive
target_country: Poland
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 38
sources_added: ["src-639", "src-640", "src-641"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-poland-022", "claim-poland-023", "claim-poland-024", "claim-poland-025"]
files_modified:
  - countries/poland.md
  - claims/poland.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-136-poland-healthcare-education.md
proposals_created: []
completed_at: 2026-06-16T14:41:19Z
status: completed
schema_version: 2.0.0
---

# Run 136 - Poland healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Poland, focusing on sections 5.6 and 5.7 to continue practical-section coverage across Tier-2-hint countries.

## What was done

- Added a first-pass Poland section 5.6 healthcare baseline as partial, because live residence-compliant insurance quotes, maternity exclusions/waiting periods, and exact final-status NFZ onboarding remain application-prep checks.
- Added a completed first-pass Poland section 5.7 education baseline covering compulsory preschool preparation, 8-year primary school, education/training obligation to 18, childcare structure, and childcare/international-school budget risk.
- Added three source registry entries: `src-639` through `src-641`.
- Added four atomic claims: `claim-poland-022` through `claim-poland-025`.
- Added `vq-128` for Poland healthcare application-prep details.
- Updated Poland profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 3.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 9 pending/open items.
- Poland section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is workable but status-sensitive: PESEL UKR / special Ukraine-framework access is publicly funded through NFZ, while CUKR/family/self-employed status requires an exact insured-title check.
- Private care is useful as a budget fallback in Warsaw, Krakow, and Wroclaw; Livingcost doctor-visit proxies are about $70-$89, but insurance and maternity terms remain unquoted.
- Poland's education baseline is strong for local integration: obligatory preschool preparation at age 6, entitlement to community pre-primary places for ages 3-5, and 8-year primary school from about age 7.
- Budget risk sits in private childcare and international schooling, especially Warsaw; Wroclaw screens better for a future-child budget.

## What remains

- Poland comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-insurance / NFZ onboarding remain for later iterations.

## Open questions added

- `vq-128`: CUKR/family/self-employed-residence-compliant private health-insurance quotes, maternity waiting periods/exclusions, and exact NFZ/public-health onboarding workflow by final status and city.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending queue remains below threshold, preferably Romania 5.6/5.7 to rotate through the next lowest-depth Tier-2-hint country.
