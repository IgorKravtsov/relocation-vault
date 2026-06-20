---
run_id: 164
date: 2026-06-20T07:07:51Z
agent: hermes
mode: country-deep-dive
target_country: UAE
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-740", "src-741", "src-742", "src-743"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-uae-014", "claim-uae-015", "claim-uae-016", "claim-uae-017"]
files_modified:
  - countries/uae.md
  - claims/uae.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-164-uae-healthcare-education.md
proposals_created: []
completed_at: 2026-06-20T07:07:51Z
status: completed
schema_version: 2.0.0
---

# Run 164 - UAE healthcare/education

## Plan

- Run one normal `country-deep-dive` because no accepted proposals exist and the verification queue is below the automatic threshold at pre-flight.
- Follow the state hint and cover UAE sections 5.6 healthcare and 5.7 education as one focused unit.

## What was done

- Added first-pass UAE section 5.6 healthcare baseline as partial, anchored on the existing GDRFA health-insurance requirement, Numbeo healthcare proxy, Policybazaar premium-range proxy, and Livingcost doctor-visit proxies.
- Added first-pass UAE section 5.7 education baseline as completed, covering public-school structure, daycare/preschool cost proxies, and international-school alternatives in Dubai-Sharjah-Ajman and Abu Dhabi.
- Added four source registry entries: `src-740` through `src-743`.
- Added four atomic claims: `claim-uae-014` through `claim-uae-017`.
- Added `vq-164` for exact insurance/onboarding/provider-price details and `vq-165` for exact school-fee/private-preschool/admissions details.
- Updated UAE frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items.
- Verification queue moved from 8 to 10 pending/open items, reaching the automatic verification threshold for the next iteration.
- UAE section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 4.5 to 6.0.

## Key findings

- UAE healthcare is strong enough for screening but private-insurance-dependent: GDRFA already requires valid insurance for virtual work, Policybazaar gives broad basic-to-comprehensive premium proxies, and doctor-visit proxies are moderate, but accepted wording and maternity/newborn terms remain uncaptured.
- Education is available but expensive: Dubai/Abu Dhabi have deep international-school supply, while Sharjah is the affordability screen; international primary-school proxies can consume roughly USD 660-1,406/month before deposits, transport, and meals.

## What remains

- UAE comfort, partner/student fit, risk dimensions, bureaucracy, full virtual-work/family-sponsorship filing mechanics, exact health-insurance policy wording, maternity/newborn terms, school fee schedules, private nursery quotes, and cross-emirate admissions constraints remain for later iterations.
- Because the pending/open verification queue is now 10, the next suggested mode is `verification` rather than another normal country-deep-dive.

## Open questions added

- `vq-164`: UAE accepted insurance wording, quotes, maternity/newborn terms, public/private onboarding, and city provider prices.
- `vq-165`: UAE exact international-school/nursery fees, deposits, meals/transport, waiting lists, public enrollment documents, and cross-emirate access rules.

## Recommendation for next iteration

- Run `verification` mode next unless an accepted proposal takes priority, because the queue has reached the automatic threshold.
