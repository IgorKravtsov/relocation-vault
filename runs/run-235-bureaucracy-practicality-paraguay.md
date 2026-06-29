---
run_id: 235
date: 2026-06-29T16:17:45Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-830]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/paraguay.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-235-bureaucracy-practicality-paraguay.md
proposals_created: []
completed_at: 2026-06-29T16:17:45Z
status: completed
schema_version: 2.0.0
---

# Run 235 - bureaucracy/practicality criterion slice, Paraguay

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Paraguay, following run-234's next hint.

## What was done

- Converted Paraguay's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the practical route sequence: visa-free entry only as scouting, residence / lucrative-activity visa confirmation before travel, temporary residence for lawful activity, Asuncion-first DNM / lawyer / accountant / healthcare / school setup, and later permanent-residence category change.
- Added one neutral professional-services contact lead, Vouga Abogados in Asuncion, with public corporate-immigration, labour/social-security, and contact information.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Paraguay frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-830`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Paraguay 9.0 -> 10.0.

## Key findings

- Paraguay is budget-forgiving but bureaucratically sequence-sensitive: the useful ordinary temporary-to-permanent residence ladder is not the same as a clean digital-nomad route.
- The gating practical issue is confirming the Ukrainian residence / lucrative-activity visa sequence and making the foreign-client IT lawful-activity file credible before travel or early after arrival.
- Asuncion should be the setup base for DNM, lawyers/accountants, healthcare, schools, and Spanish support; Encarnacion remains a later affordability/climate fallback only after the file is stable.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Panama unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Paraguay application-prep should compare immigration lawyers/accountants, confirm consular vs inside-country filing, quote translations/apostilles/health/INTERPOL steps, verify DNIT/RUC/VAT/IPS treatment, confirm private-insurance wording, and test lease/address support.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Panama unless accepted proposals, verification threshold, or staleness checks take priority.
