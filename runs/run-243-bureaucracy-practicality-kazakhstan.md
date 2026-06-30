---
run_id: 243
date: 2026-06-30T17:05:40Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-838]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/kazakhstan.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-243-bureaucracy-practicality-kazakhstan.md
proposals_created: []
completed_at: 2026-06-30T17:05:40Z
status: completed
schema_version: 2.0.0
---

# Run 243 - bureaucracy/practicality criterion slice, Kazakhstan

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Kazakhstan, following run-242's next hint.

## What was done

- Converted Kazakhstan's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the practical sequence: visa-free scouting only, 3-working-day arrival notification, adviser-led Neo Nomad / TRP / business-immigrant pre-clearance, and coordinated IIN, banking, EDS, tax/IE/VAT, insurance, lease/address, and spouse/student-status sequencing.
- Added one neutral professional-services lead, GRATA International Kazakhstan / Almaty and Astana, with public phone contacts and office email anchors.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Kazakhstan frontmatter, Block 1 date/depth, Block 6 practical notes, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-838`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Kazakhstan 9.0 -> 10.0.

## Key findings

- Kazakhstan is practical for scouting but not self-service for residence: easy entry masks unresolved official Neo Nomad, TRP foreign-client IT, tax/contribution, dependent, and PR-counting mechanics.
- Almaty is the first services/adviser base; Astana is useful for capital/authority access but winter-negative; Shymkent/Aktau remain budget/climate fallbacks only after service-depth and lease/address checks.
- If Kazakhstan is pursued beyond scouting, the couple should coordinate immigration counsel, accountant, private insurance, lease/address, IIN/banking, and marriage/spouse-status decisions before leaving the EU safety layer.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Armenia unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Kazakhstan application-prep should capture official Neo Nomad rules, compare advisers, verify TRP/business-immigrant foreign-client IT fit, quote insurance, and test lease/address support.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Armenia unless accepted proposals, verification threshold, or staleness checks take priority.
