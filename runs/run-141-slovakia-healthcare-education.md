---
run_id: 141
date: 2026-06-17T06:21:38Z
agent: hermes
mode: country-deep-dive
target_country: Slovakia
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-652", "src-653", "src-654", "src-655"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-slovakia-020", "claim-slovakia-021", "claim-slovakia-022", "claim-slovakia-023"]
files_modified:
  - countries/slovakia.md
  - claims/slovakia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-141-slovakia-healthcare-education.md
proposals_created: []
completed_at: 2026-06-17T06:21:38Z
status: completed
schema_version: 2.0.0
---

# Run 141 - Slovakia healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the anti-clustered state hint for Slovakia, focusing on sections 5.6 and 5.7 to continue practical healthcare/education coverage across Tier-2-hint countries.

## What was done

- Added a first-pass Slovakia section 5.6 healthcare baseline as partial, anchored on TP healthcare access, IOM public-health-insurance mechanics, insurance-card proof, and doctor/facility lookup.
- Added a completed first-pass Slovakia section 5.7 education baseline covering nursery / kindergarten structure, compulsory/free pre-primary baseline, compulsory school structure, and Bratislava international-school fee risk.
- Added four source registry entries: `src-652` through `src-655`.
- Added four atomic claims: `claim-slovakia-020` through `claim-slovakia-023`.
- Added `vq-132` for Slovakia healthcare application-prep details.
- Updated Slovakia profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 3 pending/open items.
- Slovakia section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable but status-sensitive: TP gives near-term healthcare access, while ordinary business/family routes require route-compliant insurance and final-status onboarding checks.
- Slovakia's education baseline is clear: care facilities for ages 6 months to 3 years, kindergarten generally ages 3-6, compulsory last kindergarten year from age 5, and primary school grades 1-4 plus 5-9.
- Bratislava international schools are expensive enough to be a major future-child budget risk on one USD 3,000/month income.

## What remains

- Slovakia comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-insurance / public-insurer / GP onboarding remain for later iterations.
- Continue anti-clustered healthcare/education coverage; Slovenia 5.6/5.7 is the suggested next low-depth Tier-2-hint target.

## Open questions added

- `vq-132`: Slovakia route-compliant private health-insurance quotes, maternity waiting periods/exclusions, exact public-insurer registration / insurance-card workflow, and city-specific GP / specialist / private-clinic checks.

## Recommendation for next iteration

- Continue `country-deep-dive` with Slovenia sections 5.6 and 5.7, unless new accepted proposals or verification items bring the queue to the threshold.
