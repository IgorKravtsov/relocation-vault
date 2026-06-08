---
run_id: 74
date: 2026-06-08T12:09:59Z
agent: hermes
mode: country-deep-dive
target_country: Georgia
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 55
sources_added: ["src-365", "src-366", "src-367", "src-368", "src-369", "src-370"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-georgia-008", "claim-georgia-009", "claim-georgia-010", "claim-georgia-011", "claim-georgia-012"]
files_modified:
  - countries/georgia.md
  - claims/georgia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-074-georgia-taxes.md
proposals_created: []
completed_at: 2026-06-08T12:09:59Z
status: completed
schema_version: 2.0.0
---

# Run 074 - Georgia taxes

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue started below the active threshold.
- Follow the previous hint to cover Georgia section 5.3 taxes.
- Focus on a practical first tax pass: tax residence, ordinary PIT, small-business turnover tax, pension/social contribution context, VAT threshold/place-of-supply caveats, and a USD 3,000/month worked example.

## What was done

- Updated Georgia section 5.3 from pending to partial.
- Added six Georgia tax / FX sources (`src-365` through `src-370`) covering PwC Georgia tax residence, PIT and small-business regime, pension/social-security context, filing mechanics, VAT context, and a USD/GEL exchange-rate snapshot.
- Added five Georgia tax claims (`claim-georgia-008` through `claim-georgia-012`).
- Calculated a conservative screening model: USD 3,000/month is about GEL 7,986/month. If small-business status applies, 1% turnover tax leaves about GEL 7,906/month (~USD 2,970); adding a 4% pension sensitivity leaves about GEL 7,587/month (~USD 2,850). If small-business status is unavailable, ordinary 20% PIT leaves about GEL 6,389/month (~USD 2,400), before accountant/VAT/immigration costs.
- Added risk flag `georgia-small-business-tax-and-it-residence-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-104` for Georgia small-business / IT residence compatibility, activity code, VAT / place-of-supply or export-treatment reporting, pension registration, and residence-renewal evidence.
- Pending/open verification queue is now 10, reaching the active verification threshold.

## What remains

- Georgia section 5.3 remains partial because the exact Revenue Service / accountant mapping for a Ukrainian foreign-client IT worker using the IT residence permit is unresolved.
- Georgia cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-104`: Georgia individual-entrepreneur / small-business tax fit, VAT / place-of-supply, pension registration, and IT-residence renewal compatibility.

## Recommendation for next iteration

- Switch to `verification` mode because the pending/open queue reached 10 after this run. Use the tax-fit operational-baseline pattern to close older accountant-level blockers where the country profile already has a conservative screening answer.
