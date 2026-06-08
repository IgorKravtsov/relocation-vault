---
run_id: 71
date: 2026-06-08T02:42:16Z
agent: hermes
mode: country-deep-dive
target_country: Montenegro
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-349", "src-350", "src-351", "src-352"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-montenegro-012", "claim-montenegro-013", "claim-montenegro-014", "claim-montenegro-015", "claim-montenegro-016"]
files_modified:
  - countries/montenegro.md
  - claims/montenegro.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-071-montenegro-taxes.md
proposals_created: []
completed_at: 2026-06-08T02:42:16Z
status: completed
schema_version: 2.0.0
---

# Run 071 - Montenegro taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue started below the active threshold.
- Follow the previous hint to cover Montenegro section 5.3 taxes.
- Focus on a practical first tax pass: tax residence, entrepreneur PIT bands, broad SSC/VAT/filing mechanics, and a USD 3,000/month worked example.

## What was done

- Updated Montenegro section 5.3 from pending to partial.
- Added four Montenegro tax sources (`src-349` through `src-352`) covering PwC Montenegro tax residence, PIT / entrepreneur income bands, social-security baseline, tax administration, and VAT context; reused ECB `src-348` for EUR/USD.
- Added five Montenegro tax claims (`claim-montenegro-012` through `claim-montenegro-016`).
- Calculated a first-pass tax stress test: USD 3,000/month is about EUR 2,577/month. If the entrepreneur PIT model applies, PIT-only net is about EUR 2,314/month (~USD 2,693); with a conservative 10.5% employee-rate SSC sensitivity, net is about EUR 2,043/month (~USD 2,378), before accountant/VAT/immigration costs.
- Added risk flag `montenegro-tax-registration-and-ssc-fit-gap`.

## Verification results

- No existing verification item was resolved.
- Added `vq-101` for Montenegro entrepreneur/self-employed registration, exact SSC base/rates, VAT / reverse-charge handling, and DN/ordinary-residence tax compatibility.
- Pending/open verification queue is now 7, still below the active verification threshold.

## What remains

- Montenegro section 5.3 remains partial because the exact registration category, self-employed SSC base/rates, VAT threshold / place-of-supply mechanics, and DN-status tax treatment are unresolved.
- Montenegro cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.

## Open questions added

- `vq-101`: Montenegro entrepreneur/self-employed registration, exact SSC base/rates, VAT / reverse-charge handling, and DN/ordinary-residence tax compatibility for a Ukrainian foreign-client IT freelancer.

## Recommendation for next iteration

- Continue `country-deep-dive` mode because the queue is below threshold. Prefer Serbia section 5.3 taxes to continue low-depth Tier-2-hint practical coverage without clustering on Montenegro.
