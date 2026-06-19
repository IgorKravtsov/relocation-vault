---
run_id: 154
date: 2026-06-18T23:54:50Z
agent: hermes
mode: country-deep-dive
target_country: Moldova
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-705", "src-706", "src-707", "src-708"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-moldova-016", "claim-moldova-017", "claim-moldova-018", "claim-moldova-019"]
files_modified:
  - countries/moldova.md
  - claims/moldova.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-154-moldova-healthcare-education.md
proposals_created: []
completed_at: 2026-06-18T23:54:50Z
status: completed
schema_version: 2.0.0
---

# Run 154 - Moldova healthcare/education

## Plan

- Run a normal `country-deep-dive` because there are no accepted proposals and the verification queue is below the automatic threshold.
- Follow the run-153 hint and open Moldova sections 5.6 and 5.7, continuing the healthcare/education coverage wave for low-depth Tier-3-hint countries.

## What was done

- Added a first-pass Moldova section 5.6 healthcare baseline as partial, anchored on the Ministry of Health, existing TP healthcare rights, and a 2026 healthcare guide for insurance/private-care screening proxies.
- Added a completed first-pass section 5.7 education baseline from Eurydice plus QSI Chisinau / Heritage International School anchors.
- Added four source registry entries: `src-705` through `src-708`.
- Added four atomic claims: `claim-moldova-016` through `claim-moldova-019`.
- Added `vq-148` for healthcare insurance/onboarding/provider-price details and `vq-149` for school-fee/private-preschool/non-Chisinau availability details.
- Updated the country profile frontmatter, scoring rows, practical budget, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 9 pending/open items, still below the automatic verification threshold of >=10.
- Moldova section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Moldova healthcare is screenable but not application-ready: TP gives primary/emergency healthcare rights, legal-resident public coverage is the baseline, and Chisinau concentrates tertiary/private care.
- Exact residence-accepted insurance wording, maternity/newborn terms, CNAM onboarding by final status, and private-care prices remain application-prep gaps.
- Education is viable at medium confidence: public compulsory education runs through age 16, but local-language integration is the baseline; Chisinau has QSI and Heritage as international/private anchors, with broad tuition proxies around USD 3,000-8,000/year.

## What remains

- Moldova comfort, partner/student fit, risk dimensions, bureaucracy, citizenship, PR-counting for DN/IT residence, exact health-insurance quotes, and school fee schedules remain for later iterations.
- Mexico 5.6/5.7 is a natural next low-depth healthcare/education target unless accepted proposals or verification-threshold logic take priority.

## Open questions added

- `vq-148`: Moldova route-compliant health-insurance quotes, maternity/newborn terms, CNAM onboarding by status, and city-specific private-care price checks.
- `vq-149`: Moldova exact QSI/Heritage/international-school fees, private preschool prices, and English/bilingual availability outside Chisinau.

## Recommendation for next iteration

- Continue `country-deep-dive` with Mexico sections 5.6 and 5.7 unless accepted proposals or verification-threshold logic take priority.
