---
run_id: 134
date: 2026-06-16T08:03:20Z
agent: hermes
mode: country-deep-dive
target_country: Malta
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 39
sources_added: ["src-631", "src-632", "src-633", "src-634"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-malta-012", "claim-malta-013", "claim-malta-014", "claim-malta-015"]
files_modified:
  - countries/malta.md
  - claims/malta.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-134-malta-healthcare-education.md
proposals_created: []
completed_at: 2026-06-16T08:03:20Z
status: completed
schema_version: 2.0.0
---

# Run 134 - Malta healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the advisory state hint for Malta, focusing only on sections 5.6 and 5.7 to keep rotating across Tier-1-hint countries.

## What was done

- Added a first-pass Malta section 5.6 healthcare baseline as partial, because live Malta-compliant insurance quotes and exact public-health onboarding steps still need application-prep checks.
- Added a completed first-pass Malta section 5.7 education baseline covering compulsory schooling, public/church/independent school structure, childcare eligibility caveats, and international-school cost risk.
- Added four source registry entries: `src-631` through `src-634`.
- Added four atomic claims: `claim-malta-012` through `claim-malta-015`.
- Added `vq-126` for Malta healthcare application-prep details.
- Updated Malta profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 7 pending/open items.
- Malta section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 4.0 to 5.5.

## Key findings

- Healthcare is workable only with insurance/status planning: NRP filing requires Malta/international health insurance, while public-health access depends on the final status and should not be assumed before onboarding is verified.
- Public health centres / hospitals provide the basic care structure; the emergency number is 112, and basic private doctor-visit proxies are around USD 20, but insurance, maternity, specialist, and lab costs remain unquoted.
- Malta education is workable if the couple accepts local public / state or church schooling: compulsory education runs ages 5-16, with primary from 5-11.
- Budget risk sits in childcare and international schooling: free childcare may apply when parents work or study, but private daycare proxies are about USD 267-654/month and international primary about USD 7.2k-13.0k/year.

## What remains

- Malta comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-insurance / public-health application-prep details remain for later iterations.

## Open questions added

- `vq-126`: NRP/residence-compliant private health-insurance quotes, maternity waiting periods/exclusions, and exact public-health onboarding workflow by status.

## Recommendation for next iteration

- Continue `country-deep-dive` while the pending queue remains below threshold, preferably Czech Republic 5.6/5.7 to rotate to the next lowest-depth Tier-2-hint country.
