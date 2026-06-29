---
run_id: 230
date: 2026-06-29T00:43:19Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-825]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/albania.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-230-bureaucracy-practicality-albania.md
proposals_created: []
completed_at: 2026-06-29T00:43:19Z
status: completed
schema_version: 2.0.0
---

# Run 230 - bureaucracy/practicality criterion slice, Albania

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Albania, following run-229's next hint.

## What was done

- Converted Albania's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: short-entry / scouting only, Type D + Unique Permit confirmation, adviser-supported tax/business setup, health insurance, accommodation, apostille/translation checks, and marriage/dependent evidence.
- Added one neutral professional-services contact lead, Kalo & Associates in Tirana, with public practice areas and contact details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Albania frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-825`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Albania 9.0 -> 10.0.

## Key findings

- Albania is operationally screenable but adviser-dependent: the warm/low-cost upside depends on a coordinated Type D / Unique Permit, tax/VAT, insurance, lease/address, and family-evidence file.
- Tirana remains the practical bureaucracy, lawyer/accountant, healthcare, and English-service base; Durres and Vlore remain lifestyle/cost options only after lease/address and service checks.
- The main practicality risk is official-route opacity / capture gaps, not immediate affordability.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with North Macedonia unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Albania application-prep should compare immigration lawyers/accountants, confirm current e-Albania / State Police checklist and fees, exact filing location, apostille/translation rules, insurance wording, lease/address proof, tax/VAT activity setup, public-insurance onboarding, and dependent evidence.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with North Macedonia unless accepted proposals, verification threshold, or staleness checks take priority.
