---
run_id: 226
date: 2026-06-28T07:40:25Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-821]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/montenegro.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-226-bureaucracy-practicality-montenegro.md
proposals_created: []
completed_at: 2026-06-28T07:40:25Z
status: completed
schema_version: 2.0.0
---

# Run 226 - bureaucracy/practicality criterion slice, Montenegro

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Montenegro, following run-225's next hint.

## What was done

- Converted Montenegro's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: TP extension to 04 March 2027, local DN filing after lawful entry, 40-day decision baseline, 2+2-year DN duration plus 6-month cooling-off rule, and evidence sequencing before the short-stay clock expires.
- Added one neutral professional-services contact lead, Prelevic Law Firm in Podgorica, with public email, phone, and address details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Montenegro frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-821`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Montenegro 9.0 -> 10.0.

## Key findings

- Montenegro is locally fileable and practical to screen: the DN application is filed personally at the local MIA branch after lawful entry and carries a 40-day decision baseline.
- It remains adviser-dependent: the exact DN income/fee/localisation requirements, partner sequencing, health insurance, lease proof, accountant mapping, SSC/VAT handling, and PR-clock strategy are the binding application-prep risks.
- Podgorica is the legal/accounting/admin anchor; Budva remains the warm-coast compromise only if rent and seasonal evidence are controlled.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Serbia unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Montenegro application-prep should compare immigration lawyers and accountants; confirm official DN income and fee amounts, document localisation, insurance wording, lease evidence, spouse/family proof, entrepreneur/company tax setup, VAT/reverse-charge handling, and whether DN/ordinary temporary residence counts toward PR.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Serbia unless accepted proposals, verification threshold, or staleness checks take priority.
