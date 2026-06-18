---
run_id: 150
date: 2026-06-18T11:23:04Z
agent: hermes
mode: country-deep-dive
target_country: Paraguay
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-689", "src-690", "src-691", "src-692"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-paraguay-016", "claim-paraguay-017", "claim-paraguay-018", "claim-paraguay-019"]
files_modified:
  - countries/paraguay.md
  - claims/paraguay.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-150-paraguay-healthcare-education.md
proposals_created: []
completed_at: 2026-06-18T11:23:04Z
status: completed
schema_version: 2.0.0
---

# Run 150 - Paraguay healthcare/education

## Plan

- Run a normal `country-deep-dive` because there are no accepted proposals and the verification queue is below the automatic threshold.
- Continue the healthcare/education coverage wave with Paraguay sections 5.6 and 5.7, following the run-149 hint and anti-clustering rule.

## What was done

- Added a first-pass Paraguay section 5.6 healthcare baseline as partial, anchored on the Ministry public-system map plus a 2026 private-care / insurance proxy.
- Added a completed first-pass Paraguay section 5.7 education baseline covering public Spanish/Guarani schooling, private bilingual school cost proxies, ASA, and international-school budget risk.
- Added four source registry entries: `src-689` through `src-692`.
- Added four atomic claims: `claim-paraguay-016` through `claim-paraguay-019`.
- Added `vq-142` for Paraguay healthcare application-prep details.
- Updated Paraguay profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 2 pending/open items, below the automatic verification threshold.
- Paraguay section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Paraguay healthcare screens as routine-care affordable, but route-sensitive: the public Ministry network and private-cost proxies are useful for screening, while exact IPS/public eligibility and insurance acceptance depend on the final residence/tax status.
- Paraguay education is screenable if Spanish/Guarani public schooling or private bilingual schooling is acceptable. Asuncion is the safest future-child base because it has the strongest private/international-school ecosystem.
- International schooling is a material one-income risk: the first-pass guide bands international/ASA options around USD 6,000-15,000/year, which can consume a large part of a single USD 3,000/month income.

## What remains

- Paraguay comfort, partner/student fit, risk dimensions, bureaucracy, residence/tax practice, healthcare quote/onboarding details, and practical lawyer/accountant contacts remain for later iterations.
- Panama 5.6/5.7 is a natural next low-depth Tier-2-hint healthcare/education target.

## Open questions added

- `vq-142`: Paraguay private health-insurance quotes, maternity/newborn coverage, exact IPS / Ministry public-care onboarding by final status, and selected-city private GP/pediatric/maternity prices.

## Recommendation for next iteration

- Continue `country-deep-dive` with Panama sections 5.6 and 5.7 unless accepted proposals or verification-threshold logic take priority.
