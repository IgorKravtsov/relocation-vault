---
run_id: 94
date: 2026-06-11T03:12:09Z
agent: hermes
mode: country-deep-dive
target_country: UAE
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 35
sources_added: ["src-462", "src-463", "src-464"]
facts_added: 3
facts_verified: 0
claims_added: ["claim-uae-007", "claim-uae-008", "claim-uae-009"]
files_modified:
  - countries/uae.md
  - claims/uae.yml
  - sources/sources.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-094-uae-taxes.md
proposals_created: []
completed_at: 2026-06-11T03:12:09Z
status: completed
schema_version: 2.0.0
---

# Run 094 - UAE taxes

## Plan

- Resume `country-deep-dive` mode because the pending/open verification queue is below the active threshold.
- Focus on UAE section 5.3 taxes, the next low-depth Tier-3-hint country suggested by state.
- Determine whether taxes are a blocker for a Ukrainian foreign-client remote IT worker earning about USD 3,000/month.

## What was done

- Added a first-pass UAE §5.3 tax section using PwC UAE individual tax-residence / PIT / corporate-tax and VAT/social-security summaries.
- Added three new source registry entries: `src-462` PwC UAE individual PIT, `src-463` PwC UAE individual residence, and `src-464` PwC UAE VAT / social-security context.
- Added three atomic claims: no PIT and natural-person CT threshold, UAE tax-residence tests, and VAT/social-security thresholds.
- Updated the UAE profile, practical verdict, playbook tax steps, Block 7 source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 3.
- Claims added: 3.
- Facts verified: 0 queue items; verification queue remains 5 pending/open items.
- UAE section 5.3 is completed for country screening. Depth score moved from 1.5 to 2.5.

## Key findings

- UAE has no personal income tax and no individual tax registration/reporting obligations in the captured PwC baseline.
- Natural persons conducting UAE business are subject to UAE corporate tax only where business turnover exceeds AED 1,000,000; USD 3,000/month is about AED 132,210/year, far below that trigger.
- UAE resident-business VAT registration is mandatory at AED 375,000 and voluntary at AED 187,500; the current income is below both.
- Non-GCC nationals are not subject to UAE social security, so the screening net is about USD 3,000/month before non-tax costs.
- Tax is favorable, but immigration remains the bottleneck because the virtual-work route requires USD 3,500/month and Green Residence freelancer thresholds are much higher.

## What remains

- UAE cost of living, rent, healthcare, education, comfort, partner/student mechanics, risk dimensions, and bureaucracy remain pending.
- If UAE becomes a serious filing target or income rises materially, confirm business/free-zone structure, VAT export-of-services treatment, corporate-tax registration, bank/accounting costs, and residence-file compatibility with a UAE accountant.

## Open questions added

- None. The remaining tax threshold/accounting issues are application-prep checks, not a new screening blocker at the current income level.

## Recommendation for next iteration

- Continue `country-deep-dive` while the verification queue is below threshold. Suggested focus: Malaysia section 5.3 taxes, rotating to another low-depth middle-east-asia profile with taxes still pending.
