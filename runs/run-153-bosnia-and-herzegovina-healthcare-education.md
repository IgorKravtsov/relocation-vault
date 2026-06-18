---
run_id: 153
date: 2026-06-18T20:47:07Z
agent: hermes
mode: country-deep-dive
target_country: Bosnia and Herzegovina
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-701", "src-702", "src-703", "src-704"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-bosnia-herzegovina-017", "claim-bosnia-herzegovina-018", "claim-bosnia-herzegovina-019", "claim-bosnia-herzegovina-020"]
files_modified:
  - countries/bosnia-and-herzegovina.md
  - claims/bosnia-and-herzegovina.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-153-bosnia-and-herzegovina-healthcare-education.md
proposals_created: []
completed_at: 2026-06-18T20:47:07Z
status: completed
schema_version: 2.0.0
---

# Run 153 - Bosnia and Herzegovina healthcare/education

## Plan

- Run a normal `country-deep-dive` because there are no accepted proposals and the verification queue is below the automatic threshold.
- Follow the run-152 hint and open Bosnia and Herzegovina sections 5.6 and 5.7, continuing the healthcare/education coverage wave.

## What was done

- Added a first-pass Bosnia and Herzegovina section 5.6 healthcare baseline as partial, anchored on Trade.gov, FBiH/RS ministry websites, and the existing residence-insurance checklist.
- Added a completed first-pass section 5.7 education baseline from Eurydice plus QSI Sarajevo / UWC Mostar school anchors.
- Added four source registry entries: `src-701` through `src-704`.
- Added four atomic claims: `claim-bosnia-herzegovina-017` through `claim-bosnia-herzegovina-020`.
- Added `vq-146` for healthcare insurance/onboarding/provider-price details and `vq-147` for school-fee/private-preschool/non-Sarajevo availability details.
- Updated the country profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 7 pending/open items, below the automatic verification threshold.
- Bosnia and Herzegovina section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Healthcare is screenable but fragmented: entity/cantonal insurance funds administer a predominantly public system, public clinical centers exist in Sarajevo/Tuzla/Banja Luka/Mostar, and Sarajevo has the strongest private-care fallback.
- Exact route-compliant health insurance, maternity/newborn terms, public-fund onboarding by final status/entity, and private-care city prices remain application-prep gaps.
- Education is viable at medium confidence: public primary school is free and compulsory, but local-language and decentralized; Sarajevo has QSI as the main future-child international-school anchor, while UWC Mostar is an older-student option rather than a full primary-school substitute.

## What remains

- Bosnia and Herzegovina comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route fit, exact health-insurance quotes, school fee schedules, and city-specific services remain for later iterations.
- Moldova 5.6/5.7 is a natural next low-depth healthcare/education target unless accepted proposals or verification-threshold logic take priority.

## Open questions added

- `vq-146`: Bosnia and Herzegovina route-compliant private health-insurance quotes, maternity/newborn terms, FBiH/RS/canton/Brcko public-fund onboarding, and private-care price checks.
- `vq-147`: Bosnia and Herzegovina exact QSI/UWC/international-school fees, private preschool prices, and English/bilingual availability outside Sarajevo/Mostar.

## Recommendation for next iteration

- Continue `country-deep-dive` with Moldova sections 5.6 and 5.7 unless accepted proposals or verification-threshold logic take priority.
