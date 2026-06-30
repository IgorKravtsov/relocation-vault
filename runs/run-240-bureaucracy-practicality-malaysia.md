---
run_id: 240
date: 2026-06-30T07:49:25Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-835]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/malaysia.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-240-bureaucracy-practicality-malaysia.md
proposals_created: []
completed_at: 2026-06-30T07:49:25Z
status: completed
schema_version: 2.0.0
---

# Run 240 - bureaucracy/practicality criterion slice, Malaysia

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Malaysia, following run-239's next hint.

## What was done

- Converted Malaysia's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the practical route sequence: DE Rantau pre-arrival filing, visitor entry as scouting/logistics only, Kuala Lumpur-first MDEC / tax / insurance / banking / lease setup, marriage-first spouse dependent file, and post-DE Rantau exit/durable-route planning by month 12.
- Added one neutral professional-services contact lead, Fragomen Malaysia / Kuala Lumpur, with public immigration-consultancy and Malaysian work-authorisation context.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Malaysia frontmatter, Block 1 date/depth, Block 6 practical notes, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-835`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Malaysia 9.0 -> 10.0.

## Key findings

- Malaysia is bureaucracy-screenable as an English-service, pre-arrival-filed 12-24 month bridge because DE Rantau can fit the working partner's current IT income on paper.
- The practical bottleneck is durability, not initial paperwork: DE Rantau is capped at 24 months and a post-DE Rantau residence / PR path for foreign-client IT work is not proven.
- Kuala Lumpur is the setup base for MDEC, tax, banking, insurance, and professional support; George Town/Penang or Johor Bahru are later living-base screens after the file is stable.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Thailand unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Malaysia application-prep should compare immigration consultants / lawyers and tax advisers, confirm current DE Rantau filing channel and fees, quote insurance and adviser costs, verify tax/source/SST/e-invoice handling, test spouse work rights, and check lease/banking acceptance for DE Rantau remote income.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Thailand unless accepted proposals, verification threshold, or staleness checks take priority.
