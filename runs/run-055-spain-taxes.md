---
run_id: 55
date: 2026-06-06T00:17:44Z
agent: hermes
mode: country-deep-dive
target_country: Spain
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 55
sources_added: ["src-280", "src-281", "src-282", "src-283", "src-284", "src-285", "src-286"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-spain-006", "claim-spain-007", "claim-spain-008", "claim-spain-009", "claim-spain-010", "claim-spain-011"]
files_modified:
  - countries/spain.md
  - claims/spain.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-055-spain-taxes.md
proposals_created: []
completed_at: 2026-06-06T00:17:44Z
status: completed
schema_version: 2.0.0
---

# Run 055 - Spain taxes

## Plan

- Run `country-deep-dive` because there are no accepted proposals and the pending/open verification queue is below the active threshold.
- Follow the prior hint to return to a Tier-1-hint low-depth practical section rather than clustering on Malaysia.
- Focus only on Spain section 5.3 taxes: ordinary freelancer/autonomo baseline, social security, registration, new-resident relief caveat, marriage effect, and a worked USD 3,000/month example.

## What was done

- Updated Spain section 5.3 from pending to passed for first-pass country screening.
- Added seven Spain tax sources (`src-280` through `src-286`): AEAT Form 036, PwC Spain PIT / residence / administration pages, Spain Social Security RETA scope, Infoautonomos 2026 autonomo quota table, and a run-date USD/EUR FX source.
- Added six Spain tax claims (`claim-spain-006` through `claim-spain-011`).
- Calculated a conservative ordinary-autonomo budget example: USD 3,000/month gross equals about EUR 2,582/month at run-date FX; after about EUR 427/month RETA and about EUR 355/month simplified IRPF, net is about EUR 1,800/month before rent and living costs.
- Added risk flag `autonomo-tax-social-security-burden`.
- Updated `INDEX.md`, `state.json`, and `CHANGELOG.md`.

## Verification results

- No existing verification item was resolved.
- Pending/open verification queue remains 5.

## What remains

- Spain section 5.1 remains partial because a primary-source PR/citizenship/counting pass and any post-2027 TP bridge remain uncaptured.
- Spain cost of living, rent, healthcare, education, comfort, partner section, risk dimensions, bureaucracy, and full relocation budget remain pending.
- VAT / invoice reporting and exact autonomous-community IRPF should be checked with a Spanish gestor before application; this is filing-prep detail, not a country-screening blocker.

## Open questions added

- None.

## Recommendation for next iteration

- Continue country-deep-dive mode because the verification queue remains below the active threshold. Prefer another Tier-1-hint low-depth practical section, likely Italy section 5.3 taxes, rather than clustering on Spain.
