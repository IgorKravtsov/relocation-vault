---
run_id: 205
date: 2026-06-25T14:38:52Z
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
  - countries/poland.md
  - countries/romania.md
  - countries/bulgaria.md
  - countries/hungary.md
  - dimensions/risk-dimensions-5.10.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-205-risk-dimensions-eu-slice-3.md
proposals_created: []
completed_at: 2026-06-25T14:38:52Z
status: completed
schema_version: 2.0.0
---

# Run 205 - EU risk-dimensions criterion slice, part 3

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and the protocol priority points to continuing 5.10 risk dimensions.
- Continue criterion 5.10 with Poland, Romania, Bulgaria, and Hungary.

## What was done

- Converted the pending 5.10 placeholders for Poland, Romania, Bulgaria, and Hungary into screening-level risk baselines covering currency/banking, political / Ukraine-posture, ties to Ukraine, and diaspora / adaptation.
- Extended `dimensions/risk-dimensions-5.10.md` from eight to twelve covered countries.
- Updated country frontmatter, Block 1 depth/date, Block 4 risk summaries, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 0; this slice reused existing country sources and comfort/legal/tax/cost/healthcare/education evidence.
- Claims added: 0; no new critical numeric immigration/tax claim was introduced.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth changes: Poland 8.0 -> 9.0; Romania 8.0 -> 9.0; Bulgaria 8.0 -> 9.0; Hungary 8.0 -> 9.0.

## Key findings

- Poland is the strongest continuity case in this cohort because CUKR / PESEL UKR / NFZ / education infrastructure and existing Polish residence relevance reduce Ukraine-transition risk.
- Romania and Bulgaria screen well for cost and geography, but both remain gated by ordinary-route and tax/social-insurance fit before the TP horizon.
- Hungary is the highest-risk country in this slice: White Card income and partner limits, guest-self-employment burden, HUF/EUR proof issues, and Hungarian-language bureaucracy all stack on the one-income budget.

## What remains

- Continue the 5.10 risk-dimensions slice with Slovakia, Slovenia, Montenegro, and Serbia unless verification or staleness triggers take priority.
- Later application-prep passes should capture exact bank onboarding, city-level Ukrainian communities, live travel-cost details, and local professional contacts for finalists.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.10 with Slovakia, Slovenia, Montenegro, and Serbia unless accepted proposals, verification threshold, or staleness checks take priority.
