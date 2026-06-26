---
run_id: 208
date: 2026-06-25T23:57:07Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.10"]
target_criterion: risk-dimensions
duration_minutes: 35
sources_added: []
facts_added: 16
facts_verified: 0
claims_added: []
files_modified:
  - countries/bosnia-and-herzegovina.md
  - countries/moldova.md
  - countries/uruguay.md
  - countries/paraguay.md
  - dimensions/risk-dimensions-5.10.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-208-risk-dimensions-latam-balkans-slice.md
proposals_created: []
completed_at: 2026-06-25T23:57:07Z
status: completed
schema_version: 2.0.0
---

# Run 208 - risk-dimensions criterion slice, part 6

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and the protocol priority points to continuing 5.10 risk dimensions.
- Continue criterion 5.10 with Bosnia and Herzegovina, Moldova, Uruguay, and Paraguay.

## What was done

- Converted the pending 5.10 placeholders for Bosnia and Herzegovina, Moldova, Uruguay, and Paraguay into screening-level risk baselines covering currency/banking, political / route risk, ties to Ukraine, and diaspora / adaptation.
- Extended `dimensions/risk-dimensions-5.10.md` from twenty to twenty-four covered countries.
- Updated country frontmatter, Block 1 depth/date, Block 4 risk summaries, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 0; this slice reused existing country sources and comfort/legal/tax/cost/healthcare/education evidence.
- Claims added: 0; no new critical numeric immigration/tax claim was introduced.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth changes: Bosnia and Herzegovina 8.0 -> 9.0; Moldova 8.0 -> 9.0; Uruguay 8.0 -> 9.0; Paraguay 8.0 -> 9.0.

## Key findings

- Bosnia and Herzegovina is affordable and comfort-screenable, but its visible company/work route is too heavy to treat as a DN-style fallback.
- Moldova is the strongest proximity bridge in this subgroup, but DN threshold, PR-counting, dependent mechanics, and Transnistria/regional-security exposure keep it route-sensitive.
- Uruguay has the cleanest ordinary-residence logic of the four, but distance from Ukraine, Spanish/habitual-residence requirements, BPS/VAT uncertainty, and Montevideo costs make it budget-sensitive.
- Paraguay is the most budget-forgiving, but residence / lucrative-activity visa sequencing, PYG/VAT/IPS treatment, Spanish/Guarani, roads/transport, and distance make it operationally high-friction.

## What remains

- Continue the 5.10 risk-dimensions slice with Panama, Mexico, Argentina, and UAE unless verification or staleness triggers take priority.
- Later application-prep passes should capture exact bank onboarding, active Ukrainian communities, travel costs, local counsel/accountant contacts, route-specific insurance, and final-city safety/neighborhood checks for finalists.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.10 with Panama, Mexico, Argentina, and UAE unless accepted proposals, verification threshold, or staleness checks take priority.
