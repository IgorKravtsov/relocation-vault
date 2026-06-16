---
run_id: 137
date: 2026-06-16T17:50:29Z
agent: hermes
mode: country-deep-dive
target_country: Romania
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-642", "src-643"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-romania-021", "claim-romania-022", "claim-romania-023", "claim-romania-024"]
files_modified:
  - countries/romania.md
  - claims/romania.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-137-romania-healthcare-education.md
proposals_created: []
completed_at: 2026-06-16T17:50:29Z
status: completed
schema_version: 2.0.0
---

# Run 137 - Romania healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue was below the automatic threshold at pre-flight.
- Follow the advisory state hint for Romania, focusing on sections 5.6 and 5.7 to continue practical-section coverage across Tier-2-hint countries.

## What was done

- Added a first-pass Romania section 5.6 healthcare baseline as partial, because live residence-compliant insurance quotes, maternity exclusions/waiting periods, and exact final-status CNAS / family-doctor onboarding remain application-prep checks.
- Added a completed first-pass Romania section 5.7 education baseline covering ECEC, compulsory/free early childhood baseline from age 4, primary/lower-secondary structure, and childcare/international-school budget risk.
- Added two source registry entries: `src-642` and `src-643`.
- Added four atomic claims: `claim-romania-021` through `claim-romania-024`.
- Added `vq-129` for Romania healthcare application-prep details.
- Updated Romania profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 2.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 10 pending/open items.
- Romania section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is workable but status-sensitive: TP gives a public-health baseline, while ordinary DN/family/self-employed status needs exact insurance and CNAS onboarding checks.
- Private insurance should be budgeted as a conservative default; public facility quality and waits vary, with deeper care supply in larger cities.
- Romania's education baseline is structurally clear: ECEC covers 3 months-6 years, is free even full-time, compulsory from age 4, and primary education starts at age 6.
- International school and private childcare are the main future-child budget risks on one income.

## What remains

- Romania comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-insurance / CNAS onboarding remain for later iterations.
- Because the pending verification queue is now at the >=10 threshold, the next normal mode should be verification.

## Open questions added

- `vq-129`: Romania DN/family/self-employed-residence-compliant private health-insurance quotes, maternity waiting periods/exclusions, and exact CNAS/public-health onboarding workflow by final status and city.

## Recommendation for next iteration

- Switch to `verification` mode because the pending queue is now 10, meeting the protocol threshold.
