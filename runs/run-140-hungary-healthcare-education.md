---
run_id: 140
date: 2026-06-17T03:11:20Z
agent: hermes
mode: country-deep-dive
target_country: Hungary
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-648", "src-649", "src-650", "src-651"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-hungary-021", "claim-hungary-022", "claim-hungary-023", "claim-hungary-024"]
files_modified:
  - countries/hungary.md
  - claims/hungary.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-140-hungary-healthcare-education.md
proposals_created: []
completed_at: 2026-06-17T03:11:20Z
status: completed
schema_version: 2.0.0
---

# Run 140 - Hungary healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Hungary, focusing on sections 5.6 and 5.7 to continue practical-section coverage across Tier-2-hint countries.

## What was done

- Added a first-pass Hungary section 5.6 healthcare baseline as partial, anchored on TP healthcare rights and NEAK public-service evidence.
- Added a completed first-pass Hungary section 5.7 education baseline covering nursery/kindergarten structure, mandatory/free kindergarten from age 3, compulsory school age, basic education structure, and international-school budget risk.
- Added four source registry entries: `src-648` through `src-651`.
- Added four atomic claims: `claim-hungary-021` through `claim-hungary-024`.
- Added `vq-131` for Hungary healthcare application-prep details.
- Updated Hungary profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 2 pending/open items.
- Hungary section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable but status-sensitive: OIF supports the TP healthcare baseline, while NEAK proves public insured-person service categories; exact private-insurance and final-status onboarding remain application-prep checks.
- Hungary's education baseline is structurally clear: nursery before age 3, mandatory/free kindergarten from age 3 to school start, mandatory school age 6-16, and 8-grade basic education.
- Budapest international schooling is expensive enough to be a future-child budget risk on one income.

## What remains

- Hungary comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-insurance / NEAK onboarding remain for later iterations.
- Continue anti-clustered healthcare/education coverage; Slovakia 5.6/5.7 is the suggested next low-depth Tier-2-hint target.

## Open questions added

- `vq-131`: Hungary White Card / guest-self-employment / family-status-compliant private health-insurance quotes, maternity waiting periods/exclusions, and exact NEAK / TAJ / GP onboarding workflow by final status and city.

## Recommendation for next iteration

- Continue `country-deep-dive` with Slovakia sections 5.6 and 5.7, unless new accepted proposals or verification items bring the queue to the threshold.
