---
run_id: 238
date: 2026-06-30T01:39:54Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-833]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/argentina.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-238-bureaucracy-practicality-argentina.md
proposals_created: []
completed_at: 2026-06-30T01:39:54Z
status: completed
schema_version: 2.0.0
---

# Run 238 - bureaucracy/practicality criterion slice, Argentina

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Argentina, following run-237's next hint.

## What was done

- Converted Argentina's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the practical route sequence: DN transitory status as a 180+180 day bridge, Buenos Aires-first DNM / legal / tax / banking / lease setup, and urgent durable-residence testing during the first 3-6 months.
- Added one neutral professional-services contact lead, Fragomen Argentina / Buenos Aires, with public immigration-services context and Buenos Aires phone contact.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Argentina frontmatter, Block 1 date/depth, Block 6 practical notes, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-833`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Argentina 9.0 -> 10.0.

## Key findings

- Argentina is bureaucracy-screenable because the DN bridge and document-localisation mechanics are visible and Buenos Aires has professional-service depth.
- The practical file is strategically fragile: DN is transitory, so a durable foreign-client IT temporary-residence category and tax/banking/VAT/Ingresos Brutos execution must be confirmed quickly.
- Buenos Aires is the setup base; Cordoba/Mendoza are later one-income living bases only after the legal/tax file is stable.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with UAE unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Argentina application-prep should compare immigration/tax advisers, confirm Ukrainian entry and DN filing sequence, quote lawyer/translation/insurance costs, verify ARCA/CUIT/VAT/Ingresos Brutos/banking setup, and test lease/address and partner-family documentation.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with UAE unless accepted proposals, verification threshold, or staleness checks take priority.
