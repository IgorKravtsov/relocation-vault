---
run_id: 211
date: 2026-06-26T09:18:00Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.10"]
target_criterion: risk-dimensions
duration_minutes: 35
sources_added: []
facts_added: 4
facts_verified: 0
claims_added: []
files_modified:
  - countries/armenia.md
  - dimensions/risk-dimensions-5.10.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-211-risk-dimensions-armenia-slice.md
proposals_created: []
completed_at: 2026-06-26T09:18:00Z
status: completed
schema_version: 2.0.0
---

# Run 211 - risk-dimensions criterion slice, Armenia closure

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale claims.
- Complete the remaining 5.10 risk-dimensions placeholder for Armenia.

## What was done

- Converted Armenia's pending 5.10 placeholders into screening-level risk baselines covering currency/banking, political / route risk, ties to Ukraine, and diaspora / adaptation.
- Extended `dimensions/risk-dimensions-5.10.md` to cover all 33 countries.
- Updated Armenia frontmatter, Block 1 depth/date, Block 4 risk summary, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 0; this slice reused existing Armenia legal, tax, cost/rent, healthcare, education, comfort, and partner-fit evidence.
- Claims added: 0; no new critical numeric immigration/tax claim was introduced.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Armenia 7.5 -> 9.0.

## Key findings

- Armenia is screenable as a nearby ordinary-business-residence candidate, not as a proven DN-style route.
- Currency/banking risk is medium: AMD exposure, foreign-client bank onboarding, IE/LLC invoicing, VAT/export-service treatment, and tax-residence fit all need adviser checks.
- Political/route risk is medium: daily safety is acceptable for screening, but no Ukraine-specific bridge or DN route is captured and border-region filtering remains necessary.
- Adaptation risk is medium: Yerevan is the default service base, while low English proficiency, Armenian/Russian administration, marriage-first dependency, private healthcare, and international-school costs create friction.

## What remains

- The 5.10 risk-dimensions slice now covers all 33 countries. Continue with 5.11 bureaucracy and practicality unless accepted proposals, verification, or staleness triggers take priority.
- Later application-prep should capture Armenian bank onboarding, IE/LLC/accountant route proof, VAT/export-service handling, current border advisories, Ukrainian/Russian-speaking lawyer/accountant contacts, and final-city lease / healthcare / school checks.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 bureaucracy/practicality unless accepted proposals, verification threshold, or staleness checks take priority.
