---
run_id: 225
date: 2026-06-28T04:33:04Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-820]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/slovenia.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-225-bureaucracy-practicality-slovenia.md
proposals_created: []
completed_at: 2026-06-28T04:33:04Z
status: completed
schema_version: 2.0.0
---

# Run 225 - bureaucracy/practicality criterion slice, Slovenia

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Slovenia, following run-224's next hint.

## What was done

- Converted Slovenia's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: TP police / administrative-unit filing, 10-day post-TP ordinary-permit window, DN filing abroad or in Slovenia while legally present, one-year non-renewable DN duration, and self-employed/single-permit tax-immigration sequencing.
- Added one neutral professional-services contact lead, Lawyers Slovenia / BridgeWest in Ljubljana, with public email and phone details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Slovenia frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-820`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Slovenia 9.0 -> 10.0.

## Key findings

- Slovenia is safe and administratively legible but sequence-sensitive: TP and DN are bridges, not a complete settlement plan.
- The DN route is conceptually clean for foreign remote work but currently budget-gated and non-renewable, so an ordinary permit strategy must be prepared early.
- Ljubljana is the services hub; Maribor remains the best services/cost compromise; Nova Gorica is the warmer affordability fallback only if professional and healthcare support can be confirmed.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Montenegro unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Slovenia application-prep should compare independent immigration lawyers and accountants; confirm serving-office forms/fees, translations/apostilles, DN threshold at filing, self-employed/s.p. setup, VAT/reverse-charge reporting, ZZZS/private-insurance onboarding, lease evidence, and partner/family sequencing.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Montenegro unless accepted proposals, verification threshold, or staleness checks take priority.
