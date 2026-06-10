---
run_id: 87
date: 2026-06-10T05:13:27Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.3"]
target_criterion: null
duration_minutes: 35
sources_added: []
facts_added: 0
facts_verified: 5
claims_added: []
files_modified:
  - countries/portugal.md
  - countries/albania.md
  - countries/north-macedonia.md
  - countries/bosnia-and-herzegovina.md
  - countries/moldova.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-087-tax-fit-verification-baselines.md
proposals_created: []
completed_at: 2026-06-10T05:13:27Z
status: completed
schema_version: 2.0.0
---

# Run 087 - tax-fit verification baselines

## Plan

- Run `verification` mode because run-086 left the pending/open verification queue at 10, meeting the active threshold (>= 10).
- Close one focused batch of recent tax-fit blockers where existing profile evidence already supports a safe country-screening baseline.
- Preserve every affected §5.3 section as partial; do not add favorable assumptions or mark tax DoD passed.

## What was done

- Resolved five recent §5.3 tax-fit queue items to conservative screening baselines: `vq-105` Portugal, `vq-106` Albania, `vq-107` North Macedonia, `vq-108` Bosnia and Herzegovina, and `vq-109` Moldova.
- Updated the five country profiles to state explicitly that exact activity registration, VAT/place-of-supply, contribution base/order, and immigration-status compatibility are application-prep/accountant checks rather than open screening blockers.
- Kept all five tax sections partial. Depth scores and sections completed did not change.
- Updated `state.json`, `INDEX.md`, `CHANGELOG.md`, and aggregate queue counts.

## Verification results

- Facts verified: 5 queue items resolved for screening.
- Sources added: 0.
- Claims added: 0.
- Verification queue is now 5 pending/open items, below the active verification threshold.

## What remains

- Remaining pending/open queue items are older tax-fit details: Greece Article 5C applicability, Cyprus self-employed social-insurance categories, Croatia lump-sum/craft fit, Malta NRP authorised-work tax fit, and Czech flat-tax / 60% expense-category fit.
- Portugal, Albania, North Macedonia, Bosnia and Herzegovina, and Moldova still require accountant/authority confirmation before any §5.3 section can be marked DoD-passed or used as filing advice.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` because the pending/open verification queue is below threshold. Suggested focus: Uruguay section 5.3 taxes, as a low-depth Tier-2-hint country with taxes still pending.
