---
run_id: 139
date: 2026-06-17T00:00:26Z
agent: hermes
mode: country-deep-dive
target_country: Bulgaria
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-644", "src-645", "src-646", "src-647"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-bulgaria-022", "claim-bulgaria-023", "claim-bulgaria-024", "claim-bulgaria-025"]
files_modified:
  - countries/bulgaria.md
  - claims/bulgaria.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-139-bulgaria-healthcare-education.md
proposals_created: []
completed_at: 2026-06-17T00:00:26Z
status: completed
schema_version: 2.0.0
---

# Run 139 - Bulgaria healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Bulgaria, focusing on sections 5.6 and 5.7 to continue practical-section coverage across Tier-2-hint countries.

## What was done

- Added a first-pass Bulgaria section 5.6 healthcare baseline as partial, anchored on NHIF and TP medical-care evidence.
- Added a completed first-pass Bulgaria section 5.7 education baseline covering early-childhood care, compulsory/free pre-primary education, public-school structure, and international-school budget risk.
- Added four source registry entries: `src-644` through `src-647`.
- Added four atomic claims: `claim-bulgaria-022` through `claim-bulgaria-025`.
- Added `vq-130` for Bulgaria healthcare application-prep details.
- Updated Bulgaria profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 1 pending/open item.
- Bulgaria section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable but status-sensitive: NHIF is the public compulsory-insurance payer and TP holders have medical-care rights, while ordinary self-employment / family status needs exact onboarding and insurance checks.
- Bulgaria's education baseline is structurally clear: nurseries cover 3 months-3 years, kindergartens cover age 3 to first grade, and compulsory preschool is free in state/municipal kindergartens.
- Sofia international schooling is expensive enough to be a future-child budget risk on one income.

## What remains

- Bulgaria comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-insurance / NHIF onboarding remain for later iterations.
- Continue anti-clustered healthcare/education coverage; Hungary 5.6/5.7 is the suggested next low-depth Tier-2-hint target.

## Open questions added

- `vq-130`: Bulgaria self-employment/family-residence-compliant private health-insurance quotes, maternity waiting periods/exclusions, and exact NHIF / GP onboarding workflow by final status and city.

## Recommendation for next iteration

- Continue `country-deep-dive` with Hungary sections 5.6 and 5.7, unless new accepted proposals or verification items bring the queue to the threshold.
