---
run_id: 142
date: 2026-06-17T09:32:42Z
agent: hermes
mode: country-deep-dive
target_country: Slovenia
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-656", "src-657", "src-658", "src-659", "src-660", "src-661"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-slovenia-018", "claim-slovenia-019", "claim-slovenia-020", "claim-slovenia-021", "claim-slovenia-022"]
files_modified:
  - countries/slovenia.md
  - claims/slovenia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-142-slovenia-healthcare-education.md
proposals_created: []
completed_at: 2026-06-17T09:32:42Z
status: completed
schema_version: 2.0.0
---

# Run 142 - Slovenia healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the anti-clustered state hint for Slovenia, focusing on sections 5.6 and 5.7 to continue practical healthcare/education coverage across Tier-2-hint countries.

## What was done

- Added a first-pass Slovenia section 5.6 healthcare baseline as partial, anchored on GOV.SI temporary-protection healthcare and ZZZS compulsory-health-insurance / public-provider mechanics.
- Added a completed first-pass Slovenia section 5.7 education baseline covering temporary-protection school inclusion, kindergarten access/costs, public basic-school structure, and Ljubljana international-school fee risk.
- Added six source registry entries: `src-656` through `src-661`.
- Added five atomic claims: `claim-slovenia-018` through `claim-slovenia-022`.
- Added `vq-133` for Slovenia healthcare application-prep details.
- Updated Slovenia profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 6.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue now has 4 pending/open items.
- Slovenia section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable but status-sensitive: Ukrainian TP gives emergency/pregnancy/childbirth healthcare access, while ordinary DN/self-employed/family routes need route-compliant insurance and final-status ZZZS onboarding checks.
- Slovenia's education baseline is strong for public schooling: kindergarten from 11 months to school entry, income-based kindergarten fees, and compulsory publicly funded nine-year basic education from age 6.
- Ljubljana international schooling is expensive enough to be a major future-child budget risk on one USD 3,000/month income.

## What remains

- Slovenia comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-insurance / ZZZS / GP onboarding remain for later iterations.
- Continue anti-clustered healthcare/education coverage; Montenegro 5.6/5.7 is the suggested next low-depth Tier-2-hint target.

## Open questions added

- `vq-133`: Slovenia route-compliant private health-insurance quotes, maternity waiting periods/exclusions, exact ZZZS registration / compulsory-insurance basis, GP / pediatrician onboarding, and city-specific private-clinic checks.

## Recommendation for next iteration

- Continue `country-deep-dive` with Montenegro sections 5.6 and 5.7, unless new accepted proposals or verification items bring the queue to the threshold.
