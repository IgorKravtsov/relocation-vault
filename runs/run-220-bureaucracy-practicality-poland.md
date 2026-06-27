---
run_id: 220
date: 2026-06-27T13:05:43Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-815]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/poland.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-220-bureaucracy-practicality-poland.md
proposals_created: []
completed_at: 2026-06-27T13:05:43Z
status: completed
schema_version: 2.0.0
---

# Run 220 - bureaucracy/practicality criterion slice, Poland

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Poland, following run-219's next hint.

## What was done

- Converted Poland's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the CUKR practical core: electronic MOS filing, 04 March 2027 horizon, PLN 340 + PLN 100 core fees, 3-year permit duration, labour-market / business-activity usefulness, and post-CUKR general-permit caveat from existing official sources.
- Added one neutral professional-contact lead, Immigration-Poland.com / BridgeWest-associated Poland immigration specialists in Warsaw, with public email/address/phone details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Poland frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-815`).
- Claims added: 0; no new machine-readable critical claim was needed because CUKR timing/fees/duration facts were already captured in Poland claims.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Poland 9.0 -> 10.0.

## Key findings

- Poland is bureaucratically promising if the Ukraine-special status facts align: CUKR is digital/local and tailored to Ukrainians, unlike many ordinary remote-work routes.
- The practical risk is sequence choice before March 2027: CUKR vs marriage/family vs business/self-employment should be selected with Polish legal/accounting support, not improvised.
- Wroclaw remains the first practical base to test, Krakow second, and Warsaw only with a strict rent cap or compelling legal/support reason.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Romania unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Poland application-prep should compare independent immigration lawyers and accountants; confirm voivode practice, exact CUKR eligibility, family-reunification sequencing, ZUS / VAT / `ryczalt` handling, sworn-translation costs, and live appointment practice.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Romania unless accepted proposals, verification threshold, or staleness checks take priority.
