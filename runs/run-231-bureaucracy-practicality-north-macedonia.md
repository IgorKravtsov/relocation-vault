---
run_id: 231
date: 2026-06-29T03:48:37Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-826]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/north-macedonia.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-231-bureaucracy-practicality-north-macedonia.md
proposals_created: []
completed_at: 2026-06-29T03:48:37Z
status: completed
schema_version: 2.0.0
---

# Run 231 - bureaucracy/practicality criterion slice, North Macedonia

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with North Macedonia, following run-230's next hint.

## What was done

- Converted North Macedonia's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: short-entry/scouting only, self-employment or company-backed ordinary residence, current post-2025 checklist review, document localisation, tax/VAT/business setup, Skopje-first service sequencing, and marriage/family evidence.
- Added one neutral professional-services contact lead, Qoku & Partners / Karanovic & Partners in Skopje, with public contact details and relevant practice areas.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, North Macedonia frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-826`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: North Macedonia 9.0 -> 10.0.

## Key findings

- North Macedonia is operationally screenable but not plug-and-play: the legal route must be built as a real self-employment/company-backed file, not a DN substitute.
- Skopje is the first practical base for counsel/accountant support, offices, banks, healthcare, and schools; Ohrid/Bitola remain lower-cost fallbacks only after the legal/tax structure is solved.
- The main practicality risk is route proof and Macedonian-language/document execution, not day-to-day affordability.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Bosnia and Herzegovina unless accepted proposals, verification threshold, or staleness checks take priority.
- Later North Macedonia application-prep should compare immigration lawyers/accountants, confirm Ministry of Interior / Employment Agency forms and fees, translations/legalisation, address/lease support, insurance wording, bank/tax registration, VAT/export-service treatment, and spouse/family-file evidence.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Bosnia and Herzegovina unless accepted proposals, verification threshold, or staleness checks take priority.
