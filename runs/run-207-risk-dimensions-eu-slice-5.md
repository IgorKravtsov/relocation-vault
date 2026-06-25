---
run_id: 207
date: 2026-06-25T20:50:12Z
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
  - countries/turkey.md
  - countries/georgia.md
  - countries/albania.md
  - countries/north-macedonia.md
  - dimensions/risk-dimensions-5.10.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-207-risk-dimensions-eu-slice-5.md
proposals_created: []
completed_at: 2026-06-25T20:50:12Z
status: completed
schema_version: 2.0.0
---

# Run 207 - risk-dimensions criterion slice, part 5

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and the protocol priority points to continuing 5.10 risk dimensions.
- Continue criterion 5.10 with Turkey, Georgia, Albania, and North Macedonia.

## What was done

- Converted the pending 5.10 placeholders for Turkey, Georgia, Albania, and North Macedonia into screening-level risk baselines covering currency/banking, political / Ukraine-posture, ties to Ukraine, and diaspora / adaptation.
- Extended `dimensions/risk-dimensions-5.10.md` from sixteen to twenty covered countries.
- Updated country frontmatter, Block 1 depth/date, Block 4 risk summaries, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 0; this slice reused existing country sources and comfort/legal/tax/cost/healthcare/education evidence.
- Claims added: 0; no new critical numeric immigration/tax claim was introduced.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth changes: Turkey 8.0 -> 9.0; Georgia 8.0 -> 9.0; Albania 8.0 -> 9.0; North Macedonia 8.0 -> 9.0.

## Key findings

- Turkey has the clearest DN route in this subgroup but is fragile because the USD 3,000/month threshold, TRY/inflation exposure, tax/SGK uncertainty, and earthquake/security checks all stack on one income.
- Georgia's IT residence / small-business path is attractive on budget, but the route depends on exact IT/small-business fit and carries GEL, occupied-territory, and ordinary-renewal risks.
- Albania is one of the warmest and cheapest screens, but official route-page capture gaps, the 2029 tax-regime sunset, road/transport friction, and Albanian-language administration keep it medium risk.
- North Macedonia is the low-cost fallback, but no DN route is captured; the self-employment/company file and conservative contribution downside are the key risks.

## What remains

- Continue the 5.10 risk-dimensions slice with Bosnia and Herzegovina, Moldova, Uruguay, and Paraguay unless verification or staleness triggers take priority.
- Later application-prep passes should capture exact bank onboarding, active Ukrainian communities, live travel costs, final-city professional contacts, and route-specific local counsel for finalists.

## Commit / push status

- Initial commit completed as `75c9d0a`; `git log -1 --pretty=fuller` showed canonical author/committer identity (`Hermes <hermes@example.local>`).
- Identity-gate note: the first commit command string should have been stopped before execution because the typed environment prefix contained placeholder-looking fragments; no amend or history rewrite was performed. This follow-up log note was committed with a read-back checked canonical helper.
- Push status is determined by the final git push step.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.10 with Bosnia and Herzegovina, Moldova, Uruguay, and Paraguay unless accepted proposals, verification threshold, or staleness checks take priority.
