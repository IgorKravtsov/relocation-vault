---
run_id: 144
date: 2026-06-17T15:51:27Z
agent: hermes
mode: country-deep-dive
target_country: Serbia
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-667", "src-668", "src-669", "src-670"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-serbia-020", "claim-serbia-021", "claim-serbia-022", "claim-serbia-023"]
files_modified:
  - countries/serbia.md
  - claims/serbia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-144-serbia-healthcare-education.md
proposals_created: []
completed_at: 2026-06-17T15:51:27Z
status: completed
schema_version: 2.0.0
---

# Run 144 - Serbia healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the anti-clustered state hint for Serbia, focusing on sections 5.6 and 5.7 to continue practical healthcare/education coverage across Tier-2-hint countries.

## What was done

- Added a first-pass Serbia section 5.6 healthcare baseline as partial, anchored on RFZO insured-person rights and the existing temporary-residence health-insurance requirement.
- Added a completed first-pass Serbia section 5.7 education baseline covering ECEC, compulsory/free preparatory and basic education, language/inclusion caveats, and Belgrade international-school fee risk.
- Added four source registry entries: `src-667` through `src-670`.
- Added four atomic claims: `claim-serbia-020` through `claim-serbia-023`.
- Added `vq-136` for Serbia healthcare application-prep details.
- Updated Serbia profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 7 pending/open items.
- Serbia section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable but status-sensitive: RFZO maps compulsory-insurance rights and pregnancy/child/childbirth coverage once insured status exists, while residence filing still needs route-compliant health-insurance evidence.
- Serbia's education baseline is usable for a future child if the family accepts Serbian-language public education: mandatory/free preschool preparatory plus 8 years of free public basic education are captured.
- Belgrade international schooling is available but expensive relative to one USD 3,000/month income; International Schools Database shows ISB yearly fees from about RSD 1.41m to RSD 3.26m for 2026/2027.

## What remains

- Serbia comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, exact private-insurance / RFZO onboarding, and city-specific private-care costs remain for later iterations.
- Continue anti-clustered healthcare/education coverage; Turkey 5.6/5.7 is the suggested next low-depth Tier-2-hint target.

## Open questions added

- `vq-136`: Serbia private health-insurance quotes, maternity/newborn coverage, RFZO/public-insurance onboarding by self-employed / independent-professional / family status, and city-specific private-care checks.

## Recommendation for next iteration

- Continue `country-deep-dive` with Turkey sections 5.6 and 5.7, unless accepted proposals or verification queue growth change the chooser.
