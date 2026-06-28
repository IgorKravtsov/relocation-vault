---
run_id: 229
date: 2026-06-28T21:36:27Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-824]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/georgia.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-229-bureaucracy-practicality-georgia.md
proposals_created: []
completed_at: 2026-06-28T21:36:27Z
status: completed
schema_version: 2.0.0
---

# Run 229 - bureaucracy/practicality criterion slice, Georgia

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice with Georgia, following run-228's next hint.

## What was done

- Converted Georgia's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured the operational sequence: use visa-free stay only for entry/scouting, build the SDA IT residence / small-business file while lawfully staying, file before the lawful-stay horizon, and coordinate address, tax/VAT, insurance, translations, and marriage/family evidence.
- Added one neutral professional-services contact lead, BGI Legal in Tbilisi, with public law/tax/corporate-registration service areas and contact details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Georgia frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-824`).
- Claims added: 0; no new machine-readable critical claim was needed because the source adds workflow/contact practicality rather than a new statutory threshold.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Georgia 9.0 -> 10.0.

## Key findings

- Georgia is operationally screenable because SDA has a visible IT residence / ordinary residence anchor and the current profile already supports a tax/cost/rent screen.
- The binding practicality risk is treating easy entry as settlement: the couple must make the IT / small-business residence file credible with Georgian legal/accounting support before the visa-free horizon expires.
- Tbilisi remains the first administrative base; Batumi is a warm/coastal option only after lease/address seasonality checks; Kutaisi is the affordability fallback.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Albania unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Georgia application-prep should compare immigration lawyers/accountants, confirm the current SDA filing channel and fees, Public Service Hall workflow, address/lease proof, translations/legalisation, Revenue Service small-business/VAT handling, insurance/public-health onboarding, and family-residence evidence.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Albania unless accepted proposals, verification threshold, or staleness checks take priority.
