---
run_id: 217
date: 2026-06-27T03:48:32Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-812]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/croatia.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-217-bureaucracy-practicality-croatia.md
proposals_created: []
completed_at: 2026-06-27T03:48:32Z
status: completed
schema_version: 2.0.0
---

# Run 217 - bureaucracy/practicality criterion slice, Croatia

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Croatia, one of the remaining Tier-1-hint countries.

## What was done

- Converted Croatia's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured DN filing practicality: online / consular / police-station filing options, up-to-18-month stay, extension no later than 60 days before expiry, 6-month cooling-off period, address / intended-address proof, Croatian/English document and legalisation burdens, and HZZO timing.
- Added one neutral professional-contact lead, Vukmir & Associates in Zagreb, with labor / immigration-law service coverage and public phone/email/address details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Croatia frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-812`).
- Claims added: 0; no new machine-readable critical claim was needed because the DN timing / threshold / family facts were already sourced in the Croatia profile.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Croatia 9.0 -> 10.0.

## Key findings

- Croatia is bureaucratically screenable: MUP's DN route has clear filing channels, document-localisation rules, address proof, and stay-duration mechanics.
- Practical friction remains high because the DN threshold is above current income, DN stay is capped at 18 months, no post-2027 TP bridge is captured, and the Croatian self-employed / lump-sum craft tax setup still needs accountant confirmation.
- Rijeka / Zagreb remain the practical bases to test before Split / Dubrovnik.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Malta unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Croatia application-prep should compare independent immigration lawyers and accountants, confirm appointment load / exact fee receipts / OIB and craft-registration sequencing, and capture city-specific MUP / HZZO / Tax Administration practice.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Malta unless accepted proposals, verification threshold, or staleness checks take priority.
