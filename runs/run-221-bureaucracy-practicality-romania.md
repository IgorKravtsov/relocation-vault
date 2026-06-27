---
run_id: 221
date: 2026-06-27T16:11:32Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-816]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/romania.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-221-bureaucracy-practicality-romania.md
proposals_created: []
completed_at: 2026-06-27T16:11:32Z
status: completed
schema_version: 2.0.0
---

# Run 221 - bureaucracy/practicality criterion slice, Romania

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Romania, following run-220's next hint.

## What was done

- Converted Romania's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured official workflow practicality: E-VISA online start plus diplomatic-mission presentation, document upload / translation / original-copy caveats, and IGI portal use for local residence-permit / work-authorisation workflows.
- Added one neutral professional-contact lead, Immigration-Romania.com / Milaciu N. Cristina - Cabinet Avocatura, with public phone, email, and address details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Romania frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-816`).
- Claims added: 0; no new machine-readable critical claim was needed because this pass covered workflow/contact practicality rather than new route thresholds.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Romania 9.0 -> 10.0.

## Key findings

- Romania is administratively visible but route-constrained: E-VISA and IGI reduce opacity, but the digital-nomad threshold is above current income and D/AC is a company/investment-heavy route rather than a simple freelancer permit.
- Timisoara remains the first practical base to test, Bucharest second with a rent cap, and Cluj-Napoca only for a specific tech/community reason.
- A Romanian immigration lawyer and accountant should be budgeted before any filing because PFA/company, VAT/reverse-charge, family, CNAS/private insurance, and post-TP sequencing are linked.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Bulgaria unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Romania application-prep should compare independent Bucharest/Timisoara lawyers and accountants; confirm GII appointment availability, exact document legalisation, final route sequencing, PFA/company tax fit, insurance/CNAS onboarding, and live provider quotes.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Bulgaria unless accepted proposals, verification threshold, or staleness checks take priority.
