---
run_id: 166
date: 2026-06-20T13:21:03Z
agent: hermes
mode: country-deep-dive
target_country: Montenegro
target_sections: ["5.7"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-744"]
facts_added: 1
facts_verified: 0
claims_added: ["claim-montenegro-026"]
files_modified:
  - countries/montenegro.md
  - claims/montenegro.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-166-montenegro-education.md
proposals_created: []
completed_at: 2026-06-20T13:21:03Z
status: completed
schema_version: 2.0.0
---

# Run 166 - Montenegro education

## Plan

- Run one normal `country-deep-dive` because there are no accepted proposals and the verification queue is below threshold.
- Follow the state hint and close Montenegro section 5.7 by resolving the international-school fee gap for screening.

## What was done

- Captured QSI Montenegro's public 2025-26 information packet fee schedule.
- Updated Montenegro section 5.7 from partial to passed for screening, preserving private-preschool, admissions, meals/transport, waiting-list, public-enrollment, and coastal school checks as application-prep/final-city work.
- Added source `src-744` and claim `claim-montenegro-026`.
- Updated Montenegro frontmatter, scoring row, practical verdict, source list, Block 8, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1.
- Claims added: 1.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items, below the automatic verification threshold.
- Montenegro section 5.7 moved from partial to completed; depth_score moved from 5.0 to 5.5.

## Key findings

- Montenegro public preschool and compulsory primary schooling remain the realistic one-income baseline.
- QSI provides an English-language fallback in Podgorica, but 2025-26 primary/secondary total annual fees are about USD 28,500/year, a major budget risk on the couple's current USD 3,000/month income.
- QSI's 3-4-year-old class is much cheaper at USD 5,700/year, but still far above public preschool fees.

## What remains

- Montenegro still needs comfort, partner/student fit, risk dimensions, bureaucracy, exact DN income/long-term-counting, tax-registration details, healthcare insurance/onboarding, and final-city school/practical budget checks.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` while the verification queue is below threshold. Several Tier-1-hint countries now share the minimum 5.5 depth score; rotate to Spain comfort/partner coverage unless an accepted proposal or new verification-threshold trigger takes priority.
