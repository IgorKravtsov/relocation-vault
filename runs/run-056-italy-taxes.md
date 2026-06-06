---
run_id: 56
date: 2026-06-06T03:29:02Z
agent: hermes
mode: country-deep-dive
target_country: Italy
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-287", "src-288", "src-289", "src-290", "src-291", "src-292", "src-293"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-italy-006", "claim-italy-007", "claim-italy-008", "claim-italy-009", "claim-italy-010", "claim-italy-011"]
files_modified:
  - countries/italy.md
  - claims/italy.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-056-italy-taxes.md
proposals_created: []
completed_at: 2026-06-06T03:29:02Z
status: completed
schema_version: 2.0.0
---

# Run 056 - Italy taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue is below the active threshold.
- Follow the prior hint to continue Tier-1-hint low-depth practical tax coverage without clustering on Spain.
- Focus only on Italy section 5.3 taxes: forfetario / partita IVA baseline, INPS social security, registration, tax-residence scope, filing mechanics, and a worked USD 3,000/month example.

## What was done

- Updated Italy section 5.3 from pending to passed for first-pass country screening.
- Added seven Italy tax sources (`src-287` through `src-293`): Agenzia delle Entrate forfetario eligibility and tax mechanics, AA9/12 `partita IVA` route, INPS Circular 8/2026 for `Gestione Separata`, PwC Italy individual tax summaries, a 2026 ATECO coefficient table, and run-date USD/EUR FX.
- Added six Italy tax claims (`claim-italy-006` through `claim-italy-011`).
- Calculated a conservative forfetario example: USD 3,000/month gross equals about EUR 31,152/year at run-date FX; after a 67% IT/communications coefficient, 26.07% INPS `Gestione Separata`, and 15% substitute tax, net is about EUR 1,950/month. If the conditional 5% startup rate applies, the estimate is about EUR 2,078/month.
- Added risk flag `italy-worldwide-tax-and-reporting`.
- Updated `INDEX.md`, `state.json`, and `CHANGELOG.md`.

## Verification results

- No existing verification item was resolved.
- Pending/open verification queue remains 5.

## What remains

- Italy section 5.1 remains partial because a durable post-TP ordinary-status bridge and full PR/citizenship counting mechanics remain incomplete.
- Cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.
- Exact ATECO code, forfetario eligibility, 5% startup-rate eligibility, and invoice/VAT mechanics should be checked with an Italian commercialista before filing; this is application-prep detail, not a country-screening blocker.

## Open questions added

- None.

## Recommendation for next iteration

- Continue country-deep-dive mode because the verification queue remains below the active threshold. Prefer another Tier-1-hint low-depth practical section, likely Greece section 5.3 taxes, rather than clustering on Italy.
