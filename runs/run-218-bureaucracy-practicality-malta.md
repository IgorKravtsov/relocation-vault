---
run_id: 218
date: 2026-06-27T07:42:00Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-813]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/malta.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-218-bureaucracy-practicality-malta.md
proposals_created: []
completed_at: 2026-06-27T07:42:00Z
status: completed
schema_version: 2.0.0
---

# Run 218 - bureaucracy/practicality criterion slice, Malta

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Malta, the remaining Tier-1-hint country.

## What was done

- Converted Malta's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured NRP route practicality: 30-working-day processing after funds are received, online portal filing, post-Approval-in-Principle accommodation / insurance submission, English-translation burden, and NRP cap / non-settlement caveat.
- Added one neutral professional-contact lead, Chetcuti Cauchi Advocates in Valletta, with immigration / residency / global-mobility / tax practice coverage and public phone/email/address details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Malta frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-813`).
- Claims added: 0; no new machine-readable critical claim was needed because the NRP threshold, route limits, and timing facts were already represented or non-critical for this contact/pass.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Malta 9.0 -> 10.0.

## Key findings

- Malta is bureaucratically screenable: the online NRP path, 30-working-day processing baseline, English-language documentation, and professional-contact lead are clear.
- Strategic/practical fit remains weak at current income because NRP requires EUR 42,000/year gross, does not lead to long-term residence/citizenship, requires private insurance and accommodation proof, and no Malta TP-to-ordinary-status bridge is captured.
- Marsaskala / Birkirkara remain the only first-pass housing bases worth testing if income rises; Sliema / Valletta remain rent-stress markets.

## What remains

- Continue the 5.11 bureaucracy/practicality slice into Tier-2 countries unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Malta application-prep should compare independent immigration lawyers and tax advisers, confirm current NRP portal/appointment practice, exact insurer wording, TP office workflow, and any ordinary route that could count toward long-term residence.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Tier-2 countries unless accepted proposals, verification threshold, or staleness checks take priority.
