---
run_id: 222
date: 2026-06-27T19:17:06Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-817]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/bulgaria.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-222-bureaucracy-practicality-bulgaria.md
proposals_created: []
completed_at: 2026-06-27T19:17:06Z
status: completed
schema_version: 2.0.0
---

# Run 222 - bureaucracy/practicality criterion slice, Bulgaria

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Bulgaria, following run-221's next hint.

## What was done

- Converted Bulgaria's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: Employment Agency self-employment permit and business plan, Type D visa abroad, post-entry Migration Directorate residence permit, 1-year permit / 3-year cap, and no captured TP-to-ordinary-status bridge.
- Added one neutral professional-contact lead, New Balkans Law Office in Sofia, with public email, phone, and address details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Bulgaria frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-817`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Bulgaria 9.0 -> 10.0.

## Key findings

- Bulgaria is cost-attractive but bureaucratically fragile: the self-employment route is a formal authority-backed business-plan file, not a simple freelancer or digital-nomad route.
- The 3-year self-employment cap plus no captured post-2027 TP bridge makes March 2027 sequencing important.
- Plovdiv remains the first practical base, Varna the coastal option, and Sofia the professional-services/bureaucracy hub with rent pressure.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Hungary unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Bulgaria application-prep should compare independent immigration lawyers and accountants; confirm Employment Agency business-plan practice, Migration Directorate appointments, exact translations/apostilles, state fees, self-employed tax/VAT/NHIF fit, and spouse/family sequencing.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Hungary unless accepted proposals, verification threshold, or staleness checks take priority.
