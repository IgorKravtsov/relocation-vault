---
run_id: 237
date: 2026-06-29T22:31:12Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-832]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/mexico.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-237-bureaucracy-practicality-mexico.md
proposals_created: []
completed_at: 2026-06-29T22:31:12Z
status: completed
schema_version: 2.0.0
---

# Run 237 - bureaucracy/practicality criterion slice, Mexico

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Mexico, following run-236's next hint.

## What was done

- Converted Mexico's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the practical route sequence: consular temporary-resident visa / solvency pre-clearance, post-entry INM `canje`, RFC/SAT / banking / insurance / lease sequencing, and four-year temporary-to-permanent-residence planning.
- Added one neutral professional-services contact lead, Fragomen Mexico City / Mexico country page, with public immigration-services context and Mexico City phone contact.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Mexico frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-832`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Mexico 9.0 -> 10.0.

## Key findings

- Mexico is screenable but not route-easy: the long-term ladder is conceptually useful, but the practical file must be pre-cleared at a Mexican consulate before relying on it as a post-EU-TP fallback.
- The captured rough temporary-residence income benchmark remains above the couple's current USD 3,000/month, so savings, a higher income, or a lower serving-consulate threshold is decisive.
- Guadalajara remains the first city screen for services/cost balance; Mexico City is mainly a setup / professional-services base with strict rent and safety filters.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Argentina unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Mexico application-prep should compare immigration/tax advisers, confirm Ukrainian entry and serving-consulate thresholds, quote lawyer/translation/insurance costs, verify INM/SAT/RFC/VAT/IMSS sequencing, and test lease/address support.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Argentina unless accepted proposals, verification threshold, or staleness checks take priority.
