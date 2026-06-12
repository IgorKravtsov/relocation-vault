---
run_id: 101
date: 2026-06-12T01:00:47Z
agent: hermes
mode: country-deep-dive
target_country: Portugal
target_sections: ["5.6"]
target_criterion: null
duration_minutes: 40
sources_added: ["src-492", "src-493", "src-494", "src-495", "src-496"]
facts_added: 4
facts_verified: 0
claims_added: ["claim-portugal-011", "claim-portugal-012", "claim-portugal-013", "claim-portugal-014"]
files_modified:
  - countries/portugal.md
  - claims/portugal.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-101-portugal-healthcare.md
proposals_created: []
completed_at: 2026-06-12T01:00:47Z
status: completed
schema_version: 2.0.0
---

# Run 101 - Portugal healthcare

## Plan

- Resume `country-deep-dive` because the verification queue was cleared by run-100 and remains below the active threshold.
- Follow the state hint and open Portugal section 5.6 healthcare with one focused first-pass unit: SNS onboarding, public/private-care split, private-care budget signals, and family-health caveats.

## What was done

- Added a first-pass Portugal §5.6 healthcare section.
- Added five new source registry entries: `src-492` through `src-496`.
- Added four atomic claims: SNS user-number allocation, health-centre registration, private-doctor appointment cost, and SNS maternity baseline.
- Added `vq-120` for exact D8 / residence-visa medical-insurance wording, live private-insurance quotes for two young adults, and private-clinic specialist/lab price checks.
- Updated the Portugal profile, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue moved from 0 to 1 pending/open item.
- Portugal section 5.6 moved from pending to partial. Depth score moved from 3.5 to 4.0.

## Key findings

- Portugal's healthcare baseline is favorable for lawful residents / TP holders: the Ukraine TP mechanism gives NHS access, and ePortugal confirms that non-nationals can obtain an SNS user number through public facilities and register at a local health centre.
- Health-centre registration and appointment booking are free, but the person must be registered with the health centre for routine booking.
- The practical risk for this couple is not the existence of public healthcare; it is waiting lists, family-doctor shortages, English-language uncertainty, and the need for private insurance / private appointments to satisfy visa-file or speed-of-access needs.

## What remains

- Do not mark §5.6 passed until the serving-consulate D8 medical-insurance requirement, live private-insurance quotes for two young adults, and private clinic/specialist/lab costs are captured.
- Portugal education, comfort, single-income fit, risk dimensions, and bureaucracy remain pending.

## Open questions added

- `vq-120`: official D8 / residence-visa medical-insurance minimums, current private-insurance quotes for two young adults, and private-clinic specialist/lab price checks.

## Recommendation for next iteration

- Continue `country-deep-dive` because the queue is still below the verification threshold; rotate to a low-depth Tier-2-hint country such as Czech Republic for cost/rent coverage, unless a manual override chooses another Tier-1 healthcare pass.
