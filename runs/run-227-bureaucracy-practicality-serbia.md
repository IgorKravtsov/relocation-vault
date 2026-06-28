---
run_id: 227
date: 2026-06-28T10:49:05Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-822]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/serbia.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-227-bureaucracy-practicality-serbia.md
proposals_created: []
completed_at: 2026-06-28T10:49:05Z
status: completed
schema_version: 2.0.0
---

# Run 227 - bureaucracy/practicality criterion slice, Serbia

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Serbia, following run-226's next hint.

## What was done

- Converted Serbia's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: Ukrainian 90/180 visa-free reconnaissance, electronic temporary-residence / single-permit filing through the Foreign Nationals Portal, up-to-3-year temporary residence / single permits, early ordinary-route planning rather than reliance on TP, and address/insurance/tax/partner-evidence sequencing.
- Added one neutral professional-services contact lead, Zunic Law in Belgrade / Novi Sad, with public email and phone details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Serbia frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-822`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Serbia 9.0 -> 10.0.

## Key findings

- Serbia is operationally attractive for entry and filing: visa-free reconnaissance plus electronic single-permit filing reduce embassy-first friction.
- The binding practicality risk is classification, not access: the couple still needs lawyer/accountant confirmation of self-employment / independent-professional tax status, APR/freelancer fit, VAT/e-invoicing, health-insurance evidence, landlord-supported address registration, and partner documentation.
- Belgrade and Novi Sad are the first professional-support bases; Nis remains a budget fallback but needs stronger local-services checks before a long lease.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Turkey unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Serbia application-prep should compare immigration lawyers and accountants; confirm official fee/current portal checklist, Serbian translation/legalisation rules, APR/freelancer route, VAT/e-invoicing, RFZO/private-insurance onboarding, lease/address registration, and common-law/marriage family evidence.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Turkey unless accepted proposals, verification threshold, or staleness checks take priority.
