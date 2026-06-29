---
run_id: 233
date: 2026-06-29T10:05:11Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-828]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/moldova.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-233-bureaucracy-practicality-moldova.md
proposals_created: []
completed_at: 2026-06-29T10:05:11Z
status: completed
schema_version: 2.0.0
---

# Run 233 - bureaucracy/practicality criterion slice, Moldova

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Moldova, following run-232's next hint.

## What was done

- Converted Moldova's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: TP online registration plus GIM appointment, ordinary provisional-stay / DN filing through GIM with 30-day timing discipline, Chisinau-first execution, local-language document support, and pre-filing legal/accounting coordination.
- Added one neutral professional-services contact lead, Turcan Cazac in Chisinau, with public work-permit, commercial/employment, tax, corporate, and contact information.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Moldova frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-828`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Moldova 9.0 -> 10.0.

## Key findings

- Moldova is bureaucratically screenable as a nearby Chisinau-first bridge/base, with visible GIM, TP, and DN filing anchors.
- The hard problems remain route gates rather than day-to-day administration: DN income formula, partner/dependent mechanics, PR-counting for DN/IT time, tax/contribution category, and insurance / lease evidence.
- Transnistria remains a practical and security caveat; low Tiraspol costs should not be used as the default relocation plan.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Uruguay unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Moldova application-prep should compare immigration lawyers/accountants, confirm the current DN threshold number, dependent mechanics, PR-counting, exact GIM filing practice, translation/legalisation requirements, private insurance wording, CNAM/CNAS/tax setup, VAT/export-service treatment, and registered-address lease support.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Uruguay unless accepted proposals, verification threshold, or staleness checks take priority.
