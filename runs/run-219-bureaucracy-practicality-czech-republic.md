---
run_id: 219
date: 2026-06-27T09:58:20Z
agent: hermes
mode: criterion-slice
target_country: null
target_sections: ["5.11"]
target_criterion: bureaucracy-practicality
duration_minutes: 35
sources_added: [src-814]
facts_added: 5
facts_verified: 0
claims_added: []
files_modified:
  - countries/czech-republic.md
  - dimensions/bureaucracy-practicality-5.11.md
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-219-bureaucracy-practicality-czech-republic.md
proposals_created: []
completed_at: 2026-06-27T09:58:20Z
status: completed
schema_version: 2.0.0
---

# Run 219 - bureaucracy/practicality criterion slice, Czech Republic

## Plan

- Run one normal `criterion-slice` because there are no accepted proposals, no pending verification items, and no stale-claim trigger.
- Continue the 5.11 bureaucracy/practicality slice into Tier-2 countries with Czech Republic.

## What was done

- Converted Czech Republic's pending 5.11 placeholder into a screening-level bureaucracy/practicality baseline.
- Captured business-visa practicality: diplomatic-mission filing, CZK 5,000 consular fee, 90-day processing baseline, required trade/register/funds/accommodation/criminal-record evidence, and Czech translation / apostille or superlegalisation burden.
- Added one neutral professional-contact lead, Foreigners.cz, with visa arrangement, residence permit, digital-nomad-program, proof-of-accommodation, and relocation-service coverage plus public phone/email details.
- Updated `dimensions/bureaucracy-practicality-5.11.md`, Czech Republic frontmatter, Block 1 date/depth, `state.json`, `INDEX.md`, `sources/sources.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 1 (`src-814`).
- Claims added: 0; no new machine-readable critical claim was needed because the Czech route/tax threshold facts were already represented or not critical for this contact/pass.
- Facts verified: 0 queue items.
- Verification queue remains at 0 pending/open items.
- Depth change: Czech Republic 9.0 -> 10.0.

## Key findings

- Czechia is bureaucratically screenable but evidence-heavy: official route mechanics are legible, yet Czech translation/legalisation, business/trade evidence, health-insurance continuity, and future special-residence round timing are practical gates.
- Brno remains the first practical base to test; Prague has the deepest services but the worst rent pressure, while Ostrava is the affordability fallback.
- The special long-term residence concept remains Czechia's strategic upside, but it still needs current-round timing checks before a March-2027 plan.

## What remains

- Continue the 5.11 bureaucracy/practicality slice with Poland unless accepted proposals, verification threshold, or staleness checks take priority.
- Later Czech application-prep should compare independent immigration lawyers, relocation advisers, and accountants; confirm current special-residence rounds, business-visa appointments, trade-licence sequencing, flat-tax/VAT handling, insurer wording, and exact provider fee quotes.

## Commit / push status

- Pending at run-log creation; final status is determined by the git step after validators.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `criterion-slice` for section 5.11 with Poland unless accepted proposals, verification threshold, or staleness checks take priority.
