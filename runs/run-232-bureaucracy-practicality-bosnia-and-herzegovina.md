---
run_id: 232
date: 2026-06-29T06:54:09Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-827]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/bosnia-and-herzegovina.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-232-bureaucracy-practicality-bosnia-and-herzegovina.md
proposals_created: []
completed_at: 2026-06-29T06:54:09Z
status: completed
schema_version: 2.0.0
---

# Run 232 - bureaucracy/practicality criterion slice, Bosnia and Herzegovina

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Bosnia and Herzegovina, following run-231's next hint.

## What was done

- Converted Bosnia and Herzegovina's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: short-entry/scouting only, ordinary temporary residence through the Service for Foreigners' Affairs, work-permit or company/founder evidence, document translation/localisation, health insurance, accommodation/address registration, tax/accountant setup, and marriage/family evidence.
- Added one neutral professional-services contact lead, MARIC & Co in Sarajevo, with public immigration/nationality, corporate/commercial, employment, regulatory, and tax practice areas plus contact details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Bosnia and Herzegovina frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-827`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Bosnia and Herzegovina 9.0 -> 10.0.

## Key findings

- Bosnia and Herzegovina is operationally screenable but high-friction: the visible route is an ordinary work/company/founder file, not a DN-style foreign-client IT route.
- Sarajevo is the first practical bureaucracy and professional-support base; Mostar remains a warm-cost fallback only after the legal/accounting route is confirmed.
- The main practicality risk is the heavy company/work structure and local-language/entity-fragmented execution, not rent or day-to-day affordability.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Moldova unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Bosnia and Herzegovina application-prep should compare immigration lawyers/accountants, confirm field-office practice for D-visa vs in-country filing, family-reunification checklist, employee/company obligations, translations/legalisation, health-insurance wording, tax/VAT/contribution setup, and lease/address-registration support.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Moldova unless accepted proposals, verification threshold, or staleness checks take priority.
