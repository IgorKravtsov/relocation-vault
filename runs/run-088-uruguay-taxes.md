---
run_id: 88
date: 2026-06-10T08:22:00Z
agent: hermes
mode: country-deep-dive
target_country: Uruguay
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-430", "src-431", "src-432", "src-433", "src-434", "src-435", "src-436"]
facts_added: 9
facts_verified: 0
claims_added: ["claim-uruguay-007", "claim-uruguay-008", "claim-uruguay-009", "claim-uruguay-010", "claim-uruguay-011"]
files_modified:
  - countries/uruguay.md
  - claims/uruguay.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-088-uruguay-taxes.md
proposals_created: []
completed_at: 2026-06-10T08:22:00Z
status: completed
schema_version: 2.0.0
---

# Run 088 - Uruguay taxes

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold at pre-flight.
- Follow the run-087 hint to cover Uruguay section 5.3 taxes as a low-depth Tier-2-hint profile with taxes still pending.
- Keep the unit focused on a conservative first-pass foreign-client IT model at the couple's USD 3,000/month budget.

## What was done

- Updated Uruguay section 5.3 from pending to partial.
- Added a worked Uruguay tax screening model: USD 3,000/month is about UYU 121,423/month at the run-088 FX snapshot; the 30% notional-expense IRPF-only model leaves about UYU 116,565/month / USD 2,880 before BPS/VAT/accountant costs, while a full-gross IRPF sensitivity leaves about USD 2,694.
- Added an employee-style social-security downside sensitivity using PwC's 18.1%-23.1% employee contribution band; this lowers the self-employed IRPF-only screen to about UYU 88,516-94,587/month / USD 2,187-2,337. It is explicitly labelled as a stress test, not a claim that employee rates apply to the self-employed category.
- Added seven Uruguay tax / FX sources (`src-430` through `src-436`) and five Uruguay tax claims (`claim-uruguay-007` through `claim-uruguay-011`).
- Added `uruguay-self-employed-bps-gap` and `uruguay-foreign-client-vat-fit-gap` risk flags.
- Added `vq-110` for DGI registration category, BPS self-employed contribution base, VAT/export-service treatment, and compatibility with the permanent-residence means-of-life file.
- Updated Uruguay depth_score from 1.5 to 2.0.

## Verification results

- Facts added: 9 tax screening facts.
- Sources added: 7.
- Claims added: 5.
- Verification queue is 6 pending/open items, below the active verification threshold.

## What remains

- Uruguay cost of living, rent, healthcare, education, comfort, partner/student-specific mechanics, risk dimensions, bureaucracy, citizenship practice, and full relocation budget remain pending.
- Uruguay §5.3 remains partial until DGI/BPS guidance or a Uruguayan accountant confirms the exact foreign-client IT registration category, BPS contribution base, VAT/export-service treatment, and compatibility with the migration notary/accounting certificate.

## Open questions added

- `vq-110`: Uruguay foreign-client IT DGI/BPS/VAT/residence-file fit.

## Recommendation for next iteration

- Continue `country-deep-dive` because the pending/open verification queue is below threshold. Suggested focus: Paraguay section 5.3 taxes, as another low-depth Tier-2-hint country with taxes still pending.
