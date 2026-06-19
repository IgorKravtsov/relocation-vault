---
run_id: 135
date: 2026-06-16T11:15:41Z
agent: hermes
mode: country-deep-dive
target_country: Czech Republic
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 42
sources_added: ["src-635", "src-636", "src-637", "src-638"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-czech-016", "claim-czech-017", "claim-czech-018", "claim-czech-019"]
files_modified:
  - countries/czech-republic.md
  - claims/czech-republic.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-135-czech-republic-healthcare-education.md
proposals_created: []
completed_at: 2026-06-16T11:15:41Z
status: completed
schema_version: 2.0.0
---

# Run 135 - Czech Republic healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Czech Republic, focusing on sections 5.6 and 5.7 to continue practical-section coverage across Tier-2-hint countries.

## What was done

- Added a first-pass Czech Republic section 5.6 healthcare baseline as partial, because live comprehensive-insurance quotes, maternity exclusions/waiting periods, and exact final-status health onboarding remain application-prep checks.
- Added a completed first-pass Czech Republic section 5.7 education baseline covering compulsory/free final pre-primary year, 9-year basic schooling, ECEC structure, childcare cost proxies, and international-school budget risk.
- Added four source registry entries: `src-635` through `src-638`.
- Added four atomic claims: `claim-czech-016` through `claim-czech-019`.
- Added `vq-127` for Czech healthcare application-prep details.
- Updated Czech Republic profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 8 pending/open items.
- Czech Republic section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is workable but status-sensitive: insurance continuity already matters for the Ukrainian special-long-term-residence path, and commercial foreigner-insurance sources support using comprehensive coverage as the conservative residence-planning baseline.
- Pregnancy planning should not rely on emergency-only insurance; the captured commercial explainer says pregnancy/birth/newborn care needs comprehensive insurance with a pregnancy package.
- Czech education is structurally strong for local-school integration: the final pre-primary year is compulsory/free in public/state schools and basic education lasts 9 years.
- Budget risk sits in Prague childcare/international schooling: Livingcost proxies show Prague daycare around $1,061/month and international primary about $17,389/year; Brno/Ostrava are cheaper but still meaningful on one income.

## What remains

- Czech Republic comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-insurance / public-health onboarding remain for later iterations.

## Open questions added

- `vq-127`: Czech residence-compliant comprehensive-insurance quotes, maternity exclusions/waiting periods, and exact public/private healthcare onboarding workflow by final status and city.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending queue remains below threshold, preferably Poland 5.6/5.7 to rotate through the next lowest-depth Tier-2-hint country.
