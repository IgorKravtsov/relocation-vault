---
run_id: 206
date: 2026-06-25T17:44:11Z
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
  - countries/slovakia.md
  - countries/slovenia.md
  - countries/montenegro.md
  - countries/serbia.md
  - dimensions/risk-dimensions-5.10.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-206-risk-dimensions-eu-slice-4.md
proposals_created: []
completed_at: 2026-06-25T17:44:11Z
status: completed
schema_version: 2.0.0
---

# Run 206 - risk-dimensions criterion slice, part 4

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and the protocol priority points to continuing 5.10 risk dimensions.
- Continue criterion 5.10 with Slovakia, Slovenia, Montenegro, and Serbia.

## What was done

- Converted the pending 5.10 placeholders for Slovakia, Slovenia, Montenegro, and Serbia into screening-level risk baselines covering currency/banking, political / Ukraine-posture, ties to Ukraine, and diaspora / adaptation.
- Extended `dimensions/risk-dimensions-5.10.md` from twelve to sixteen covered countries.
- Updated country frontmatter, Block 1 depth/date, Block 4 risk summaries, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 0; this slice reused existing country sources and comfort/legal/tax/cost/healthcare/education evidence.
- Claims added: 0; no new critical numeric immigration/tax claim was introduced.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth changes: Slovakia 8.0 -> 9.0; Slovenia 8.0 -> 9.0; Montenegro 8.0 -> 9.0; Serbia 8.0 -> 9.0.

## Key findings

- Slovakia is a eurozone/EU proximity case whose live risk is the evidence-heavy business/SZCO route, not daily safety or euro banking.
- Slovenia has a useful official post-TP filing window and safe daily-life profile, but the DN income formula, one-year DN duration, and conservative tax downside make the route-switch plan critical.
- Montenegro is the warmest lifestyle option in this subgroup with a real DN route, but income-threshold, tax/SSC/VAT, health-insurance, and DN PR-counting gaps keep it medium risk.
- Serbia is the strongest low-cost regional fallback in this subgroup but carries higher RSD/tax, public-order/Kosovo, Serbian/Cyrillic bureaucracy, and citizenship-release caveats.

## What remains

- Continue the 5.10 risk-dimensions slice with Turkey, Georgia, Albania, and North Macedonia unless verification or staleness triggers take priority.
- Later application-prep passes should capture exact bank onboarding, city-level Ukrainian communities, live travel-cost details, and local professional contacts for finalists.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.10 with Turkey, Georgia, Albania, and North Macedonia unless accepted proposals, verification threshold, or staleness checks take priority.
