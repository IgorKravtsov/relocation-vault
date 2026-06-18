---
run_id: 151
date: 2026-06-18T14:30:50Z
agent: hermes
mode: country-deep-dive
target_country: Panama
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-693", "src-694", "src-695", "src-696"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-panama-016", "claim-panama-017", "claim-panama-018", "claim-panama-019"]
files_modified:
  - countries/panama.md
  - claims/panama.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-151-panama-healthcare-education.md
proposals_created: []
completed_at: 2026-06-18T14:30:50Z
status: completed
schema_version: 2.0.0
---

# Run 151 - Panama healthcare/education

## Plan

- Run a normal `country-deep-dive` because there are no accepted proposals and the verification queue is below the automatic threshold.
- Follow the run-150 hint and open Panama sections 5.6 and 5.7, with one focused healthcare/education pass.

## What was done

- Added a first-pass Panama section 5.6 healthcare baseline as partial, anchored on MINSA, the remote-worker insurance requirement, and private healthcare / insurance cost proxies.
- Added a completed first-pass Panama section 5.7 education baseline covering public Spanish-medium schooling, bilingual/international school cost proxies, Panama City school ecosystem, and International School of Panama as a flagship option.
- Added four source registry entries: `src-693` through `src-696`.
- Added four atomic claims: `claim-panama-016` through `claim-panama-019`.
- Added `vq-143` for Panama healthcare application-prep details.
- Updated Panama profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 3 pending/open items, below the automatic verification threshold.
- Panama section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- Panama healthcare screens positively if the couple can budget private insurance and use Panama City for serious care; David and Boquete need escalation planning to David/Panama City for specialist, maternity, or complex care.
- Panama education is viable but budget-sensitive: public schooling is Spanish-medium, bilingual schools screen around USD 3,000-8,000/year, and international schools around USD 8,000-20,000/year.
- Panama City is the strongest healthcare/education base, but it compounds the existing rent and one-income margin pressure.

## What remains

- Panama comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route fit, tax-source practice, live insurance quotes, maternity/newborn policy wording, CSS/MINSA onboarding, and final-city health/school checks remain for later iterations.
- North Macedonia 5.6/5.7 is a natural next low-depth healthcare/education target unless accepted proposals or verification-threshold logic take priority.

## Open questions added

- `vq-143`: Panama route-compliant private health-insurance quotes, maternity/newborn coverage, exact CSS/MINSA onboarding by final residence/tax status, and selected-city private-care prices.

## Recommendation for next iteration

- Continue `country-deep-dive` with North Macedonia sections 5.6 and 5.7 unless accepted proposals or verification-threshold logic take priority.
