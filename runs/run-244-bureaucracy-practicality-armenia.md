---
run_id: 244
date: 2026-06-30T20:12:08Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-839]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/armenia.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-244-bureaucracy-practicality-armenia.md
proposals_created: []
completed_at: 2026-06-30T20:12:08Z
status: completed
schema_version: 2.0.0
---

# Run 244 - bureaucracy/practicality criterion slice, Armenia

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Armenia, following run-243's next hint.

## What was done

- Converted Armenia's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the practical sequence: Ukrainian visa-free scouting only, MCS Yerevan residence filing, 30-day processing / extension timing, document-localisation burden, and adviser-led business-activity / IE-or-LLC / tax / VAT / lease / spouse sequencing.
- Added one neutral legal/tax professional-services lead, ADWISE Business & Legal Consulting, with public Yerevan contact details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Armenia frontmatter, Block 1 date/depth, Block 6 contacts, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-839`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Armenia 9.0 -> 10.0.

## Key findings

- Armenia is easy to enter but should be treated as an adviser-assisted ordinary business-residence file, not as a DN-style remote-work route.
- Yerevan is the setup base for MCS filing, translators, banks, accountants, clinics, and professional support; Gyumri/Vanadzor are budget fallbacks only after the residence/tax file is stable.
- The decisive practical question is whether a foreign-client IT IE/LLC structure can support residence renewal, tax/VAT compliance, banking, lease/address evidence, and spouse dependency.

## What remains

- Initial 5.11 coverage is now complete for all 33 countries; next normal iteration should choose consolidation unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Armenia application-prep should compare immigration/tax advisers, verify the exact business-activity checklist, quote insurance, test lease/address support, and confirm spouse-dependent mechanics.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Choose `consolidation` unless accepted proposals, verification threshold, or staleness checks take priority.
