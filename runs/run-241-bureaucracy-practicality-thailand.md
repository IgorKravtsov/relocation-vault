---
run_id: 241
date: 2026-06-30T10:54:31Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-836]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/thailand.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-241-bureaucracy-practicality-thailand.md
proposals_created: []
completed_at: 2026-06-30T10:54:31Z
status: completed
schema_version: 2.0.0
---

# Run 241 - bureaucracy/practicality criterion slice, Thailand

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Thailand, following run-240's next hint.

## What was done

- Converted Thailand's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the practical route sequence: DTV pre-arrival e-visa planning from Poland/Ukraine, 180-day stay / extension / re-entry calendar, Bangkok-first setup, Thai tax advice before 180-day residence/remittance exposure, marriage-first spouse dependency, and bridge-only settlement caution.
- Added one neutral professional-services contact lead, Fragomen Thailand / Bangkok, with public phone contact and immigration / mobility services context.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Thailand frontmatter, Block 1 date/depth, Block 6 practical notes, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-836`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Thailand 9.0 -> 10.0.

## Key findings

- Thailand is bureaucracy-screenable as a DTV bridge if the couple pre-clears the e-visa file, maintains 500,000 THB savings evidence, uses marriage for dependency, and coordinates insurance, tax, lease/TM30, extension, and re-entry logistics.
- The practical bottleneck is not initial visibility but durability: DTV is a bridge/mobility route, while DTV-to-PR/citizenship counting and a durable foreign-client IT settlement route remain uncaptured.
- Bangkok is the setup base for immigration, advisers, private healthcare, and banking; Chiang Mai is the later budget test; Phuket should remain a lifestyle exception with explicit buffers.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Indonesia unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Thailand application-prep should compare Thai immigration consultants / visa agents and tax advisers, confirm current DTV e-visa channel and fees, quote insurance and adviser costs, test lease / TM30 / banking acceptance, and verify spouse-dependent document sequencing and extension/re-entry costs.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Indonesia unless accepted proposals, verification threshold, or staleness checks take priority.
