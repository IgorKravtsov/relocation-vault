---
run_id: 210
date: 2026-06-26T06:08:55Z
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
  - countries/malaysia.md
  - countries/thailand.md
  - countries/indonesia.md
  - countries/kazakhstan.md
  - dimensions/risk-dimensions-5.10.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-210-risk-dimensions-asia-kazakhstan-slice.md
proposals_created: []
completed_at: 2026-06-26T06:08:55Z
status: completed
schema_version: 2.0.0
---

# Run 210 - risk-dimensions criterion slice, part 8

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and the protocol priority points to continuing 5.10 risk dimensions.
- Continue criterion 5.10 with Malaysia, Thailand, Indonesia, and Kazakhstan.

## What was done

- Converted the pending 5.10 placeholders for Malaysia, Thailand, Indonesia, and Kazakhstan into screening-level risk baselines covering currency/banking, political / route risk, ties to Ukraine, and diaspora / adaptation.
- Extended `dimensions/risk-dimensions-5.10.md` from twenty-eight to thirty-two covered countries.
- Updated country frontmatter, Block 1 depth/date, Block 4 risk summaries, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 0; this slice reused existing country sources and comfort/legal/tax/cost/healthcare/education evidence.
- Claims added: 0; no new critical numeric immigration/tax claim was introduced.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth changes: Malaysia 8.0 -> 9.0; Thailand 8.0 -> 9.0; Indonesia 8.0 -> 9.0; Kazakhstan 8.0 -> 9.0.

## Key findings

- Malaysia is the strongest English-service bridge in this subgroup, but DE Rantau remains a capped 24-month Professional Visit Pass and not a proven settlement route.
- Thailand has a flexible DTV bridge, but very low English proficiency, stay-management, tax/remittance, road/safety, and distance-from-Ukraine risks keep it bridge-only.
- Indonesia is affordable on paper, but the E33G income gate is above the couple's current income and IDR/tax/VAT/BPJS plus natural-disaster/social-norm risks make it high-friction.
- Kazakhstan is the closest and most regionally practical option in this slice, but official-primary Neo Nomad / IT-TRP proof, PR/citizenship/dual-nationality risk, and weak English keep it unresolved.

## What remains

- Continue the 5.10 risk-dimensions slice with Armenia unless verification or staleness triggers take priority.
- Later application-prep passes should capture bank onboarding, route-specific insurance, official Neo Nomad / DTV / DE Rantau operational details, local counsel/accountants, Ukrainian communities, and final-city safety / lease checks for finalists.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.10 with Armenia unless accepted proposals, verification threshold, or staleness checks take priority.
