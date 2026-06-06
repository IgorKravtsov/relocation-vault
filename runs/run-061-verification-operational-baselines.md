---
run_id: 61
date: 2026-06-06T19:13:35Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1"]
target_criterion: null
duration_minutes: 45
sources_added: []
facts_added: 0
facts_verified: 5
claims_added: []
files_modified:
  - countries/albania.md
  - countries/argentina.md
  - countries/armenia.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-061-verification-operational-baselines.md
proposals_created: []
completed_at: 2026-06-06T19:13:35Z
status: completed
schema_version: 2.0.0
---

# Run 061 - verification operational baselines

## Plan

- Run `verification` because the pending/open queue started at the active threshold of 10.
- Close at least five blockers using existing captured evidence where a safe screening answer is already clear.
- Avoid new source hunting unless required; this batch focused on operational baselines for route-screening decisions.

## What was done

- Resolved five verification items: `vq-072`, `vq-086`, `vq-087`, `vq-088`, and `vq-055`.
- Updated Armenia section 5.1 to state three conservative baselines:
  - no captured Armenia-specific Ukraine protection / humanitarian / post-2027 bridge, so use ordinary Armenian status only;
  - business activity is the possible route, but should be treated as a real-business Armenian IE/LLC file, not a DN substitute;
  - partner planning is marriage or independent eligibility, because captured MFA wording names spouse/parent/child and does not show unmarried-partner sponsorship.
- Updated Argentina section 5.1 to close the tourist-entry item for screening: the 90-day Ukrainian tourist-entry baseline is sufficient for scouting / DN eligibility planning, while direct official table capture remains a before-travel or DN-filing check.
- Updated Albania section 5.1 to close the Type D + Unique Permit blocker for screening: secondary evidence supports a promising remote-worker route and current income fit, while exact official checklist, fees, dependent mechanics, and PR-counting stay as application-prep or later deep-dive checks.

## Verification results

- `vq-086`: resolved to no captured Armenia Ukraine-specific bridge; ordinary-status planning only.
- `vq-087`: resolved to Armenia business-activity / real-business IE/LLC screening baseline.
- `vq-088`: resolved to Armenia spouse/marriage-first dependent baseline.
- `vq-072`: resolved to Argentina tourist-entry before-travel check, not a settlement-route blocker.
- `vq-055`: resolved to Albania Unique Permit route screening baseline, with microdetails demoted.
- Pending/open verification queue is now 5.

## What remains

- The still-open queue items are mainly tax/application-specific blockers: Cyprus, Croatia, Malta, Greece EFKA / Article 5C.
- Armenia, Albania, and Argentina all remain partial in section 5.1; they are clarified for screening but not application-ready.
- Next normal iteration can resume country-deep-dive because the verification queue is below threshold; Czech Republic section 5.3 taxes is a reasonable next low-depth target.

## Open questions added

- None.

## Recommendation for next iteration

- Resume country-deep-dive mode. Prefer Czech Republic section 5.3 taxes to continue low-depth practical coverage without clustering on the recent Tier-1-hint tax sequence.
