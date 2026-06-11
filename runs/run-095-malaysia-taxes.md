---
run_id: 95
date: 2026-06-11T06:20:51Z
agent: hermes
mode: country-deep-dive
target_country: Malaysia
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-465", "src-466", "src-467", "src-468", "src-469", "src-470"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-malaysia-008", "claim-malaysia-009", "claim-malaysia-010", "claim-malaysia-011", "claim-malaysia-012"]
files_modified:
  - countries/malaysia.md
  - claims/malaysia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-095-malaysia-taxes.md
proposals_created: []
completed_at: 2026-06-11T06:20:51Z
status: completed
schema_version: 2.0.0
---

# Run 095 - Malaysia taxes

## Plan

- Continue `country-deep-dive` because the pending/open verification queue is below the active threshold.
- Focus on Malaysia section 5.3 taxes, rotating from UAE to another low-depth middle-east-asia profile with taxes still pending.
- Determine whether Malaysia taxes are a blocker for a Ukrainian foreign-client IT worker earning about USD 3,000/month on a DE Rantau bridge.

## What was done

- Added a first-pass Malaysia §5.3 tax section using PwC Malaysia PIT, residence, income-determination, deductions, other-taxes, and tax-administration pages plus a current USD/MYR FX snapshot.
- Added six new source registry entries: `src-465` through `src-470`.
- Added five atomic claims: tax-residence/source scope, resident/non-resident PIT rates, EPF/SOCSO/SST context, filing/marriage mechanics, and the USD 3,000/month worked example.
- Added `vq-115` for the exact DE Rantau foreign-client tax structure because the safe screening answer is not enough for filing advice.
- Updated the Malaysia profile, practical verdict, playbook tax step, Block 7/8, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 6.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue moved from 5 to 6 pending/open items.
- Malaysia section 5.3 moved from pending to partial. Depth score moved from 1.5 to 2.0.

## Key findings

- Malaysia is not a tax-free default for the couple. PwC says individuals are taxed on Malaysian-source income, resident individuals can be taxed on foreign-sourced income received in Malaysia, and employment income is taxable when work is performed in Malaysia.
- At USD 3,000/month and USD 1 = MYR 4.06831, gross is about MYR 12,205/month. A resident PIT stress test after MYR 9,000 self relief leaves about MYR 10,641/month / USD 2,616 before non-tax costs.
- If taxable while non-resident, the flat 30% downside leaves about MYR 8,544/month / USD 2,100.
- Non-Malaysian employee EPF is listed at 2% employee / 2% employer, but exact freelancer / DE Rantau EPF, SOCSO, SST, e-invoice, and source classification remain adviser checks.

## What remains

- Malaysia cost of living, rent, healthcare, education, comfort, partner/student mechanics, risk dimensions, and bureaucracy remain pending.
- Before filing, confirm the exact Inland Revenue Board / Customs / EPF / SOCSO posture for DE Rantau foreign-client IT income.

## Open questions added

- `vq-115`: exact Malaysia DE Rantau / foreign-client IT source classification, foreign-sourced-income exemption fit, tax registration, SST/e-invoice, EPF/SOCSO exposure, and immigration-status compatibility.

## Recommendation for next iteration

- Continue `country-deep-dive` while the verification queue is below threshold. Suggested focus: Thailand section 5.3 taxes, rotating to the next low-depth middle-east-asia profile with taxes still pending.
