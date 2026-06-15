---
run_id: 129
date: 2026-06-15T16:21:04Z
agent: hermes
mode: country-deep-dive
target_country: Spain
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 42
sources_added: ["src-613", "src-614", "src-615"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-spain-012", "claim-spain-013", "claim-spain-014", "claim-spain-015"]
files_modified:
  - countries/spain.md
  - claims/spain.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-129-spain-healthcare-education.md
proposals_created: []
completed_at: 2026-06-15T16:21:04Z
status: completed
schema_version: 2.0.0
---

# Run 129 - Spain healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Spain, focusing only on sections 5.6 and 5.7 to rotate across Tier-1-hint countries and avoid clustering on Portugal.

## What was done

- Added a first-pass Spain section 5.6 healthcare baseline as partial, because live DN-compliant insurance quotes and region-specific health-card registration still need a selected-city check.
- Added a completed first-pass Spain section 5.7 education baseline covering early childhood, public schooling, childcare cost proxies, and international-school cost risk.
- Added three source registry entries: `src-613` through `src-615`.
- Added four atomic claims: `claim-spain-012` through `claim-spain-015`.
- Added `vq-121` for Spain healthcare application-prep details.
- Updated Spain profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 3.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 2 pending/open items.
- Spain section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 4.0 to 5.5.

## Key findings

- Healthcare screens structurally strong for TP/public-system access, but DN filing still needs exact private-insurance quotes and maternity waiting-period checks.
- Private care is usable as a fallback: captured proxies show ordinary doctor visits around USD 47-73 in target cities / nationally, with a secondary EUR 100 doctor-visit and EUR 200 ER-visit baseline.
- Spain education is positive if the couple accepts Spanish-language public schooling: ages 3-5 early childhood is free and primary/ESO are free compulsory schooling.
- Private childcare and international schools are the education budget risk: daycare/preschool proxies are about USD 560-629/month and international primary school is around USD 10.4k-10.9k/year in the target cities.

## What remains

- Spain comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route, and exact DN insurance / regional health-card application details remain for later iterations.

## Open questions added

- `vq-121`: DN-compliant private health-insurance quotes for two young adults, maternity waiting periods / exclusions, and selected-region public health-card registration steps.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending queue remains below threshold, preferably Italy 5.6/5.7 to keep rotating through Tier-1-hint countries.
