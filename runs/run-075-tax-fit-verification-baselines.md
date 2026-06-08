---
run_id: 75
date: 2026-06-08T15:18:10Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.3 tax-fit operational baselines"]
target_criterion: null
duration_minutes: 40
sources_added: []
facts_added: 0
facts_verified: 5
claims_added: []
files_modified:
  - countries/slovenia.md
  - countries/montenegro.md
  - countries/serbia.md
  - countries/turkey.md
  - countries/georgia.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-075-tax-fit-verification-baselines.md
proposals_created: []
completed_at: 2026-06-08T15:18:10Z
status: completed
schema_version: 2.0.0
---

# Run 075 - tax-fit verification baselines

## Plan

- Run `verification` mode because the pending/open verification queue reached the active threshold after run-074.
- Apply the run-069 tax-fit verification pattern to recent section 5.3 accountant-level blockers where the country profile already has a conservative worked example.
- Close only the country-screening blocker; keep each tax section partial and preserve accountant / authority checks as application-prep items.

## What was done

- Resolved `vq-100` through `vq-104` for Slovenia, Montenegro, Serbia, Turkey, and Georgia.
- Updated each affected country profile to state an explicit screening baseline:
  - Slovenia: use the conservative ordinary self-employed gross-rate stress test; do not assume normirani s.p. availability.
  - Montenegro: use the entrepreneur PIT baseline plus SSC sensitivity; do not assume a DN tax exemption.
  - Serbia: use the gross-base and 20% expense-base stress tests; do not assume the freelancer portal creates immigration status.
  - Turkey: use the ordinary PIT-only baseline plus SGK sensitivity; do not assume a foreign-income exemption or DN tax shelter.
  - Georgia: use the small-business tax-only / pension-sensitivity model as the optimistic conservative baseline and keep the 20% PIT fallback.
- Updated `verification-queue.md`, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Facts verified / resolved for screening: 5.
- Sources added: 0.
- Claims added: 0.
- Pending/open verification queue is now 5, below the active verification threshold.

## What remains

- All five country tax sections remain partial.
- Exact activity classification, VAT/reverse-charge or export-treatment, contribution bases, tax-registration route, accountant costs, and immigration-status compatibility remain application-prep checks before filing or before marking §5.3 passed.

## Open questions added

- None.

## Recommendation for next iteration

- Return to `country-deep-dive` mode. Prefer Cyprus sections 5.4 and 5.5 (cost of living and rent) among low-depth Tier-1-hint countries, because the verification queue is back below threshold and this avoids clustering on the recent tax countries.
