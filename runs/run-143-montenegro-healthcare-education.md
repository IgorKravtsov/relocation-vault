---
run_id: 143
date: 2026-06-17T12:44:12Z
agent: hermes
mode: country-deep-dive
target_country: Montenegro
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-662", "src-663", "src-664", "src-665", "src-666"]
facts_added: 7
facts_verified: 0
claims_added: ["claim-montenegro-021", "claim-montenegro-022", "claim-montenegro-023", "claim-montenegro-024", "claim-montenegro-025"]
files_modified:
  - countries/montenegro.md
  - claims/montenegro.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-143-montenegro-healthcare-education.md
proposals_created: []
completed_at: 2026-06-17T12:44:12Z
status: completed
schema_version: 2.0.0
---

# Run 143 - Montenegro healthcare/education

## Plan

- Continue `country-deep-dive` because there are no accepted proposals and the pending verification queue is below the automatic threshold.
- Follow the anti-clustered state hint for Montenegro, focusing on sections 5.6 and 5.7 to continue practical healthcare/education coverage across Tier-2-hint countries.

## What was done

- Added a first-pass Montenegro section 5.6 healthcare baseline as partial, anchored on the Health Insurance Fund, Ministry of Health, and DN health-insurance requirement.
- Added a first-pass Montenegro section 5.7 education baseline as partial, covering public preschool fees, nursery/kindergarten age bands, compulsory/free 9-year primary education, and a Podgorica international-school presence anchor.
- Added five source registry entries: `src-662` through `src-666`.
- Added five atomic claims: `claim-montenegro-021` through `claim-montenegro-025`.
- Added `vq-134` for Montenegro healthcare application-prep details and `vq-135` for international-school/private-preschool fee details.
- Updated Montenegro profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 5.
- Claims added: 5.
- Facts verified: 0 queue items; verification queue now has 6 pending/open items.
- Montenegro sections 5.6 and 5.7 moved from pending to partial. Depth score moved from 3.0 to 5.0.

## Key findings

- Healthcare is screenable but status-sensitive: the public Health Insurance Fund / Ministry map is captured, and DN filing requires health insurance, but private quotes and public-insurance onboarding by residence status remain open.
- Public education looks usable for a future child: public preschool fees are about EUR 50/month full-day or EUR 25/month half-day, and primary education is compulsory/free for about ages 6-15.
- QSI confirms an international-school option in Podgorica, but exact tuition was not captured, so Montenegro education remains partial rather than passed.

## What remains

- Montenegro comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route detail, and exact private-health-insurance / international-school fee quotes remain for later iterations.
- Continue anti-clustered healthcare/education coverage; Serbia 5.6/5.7 is the suggested next low-depth Tier-2-hint target.

## Open questions added

- `vq-134`: Montenegro private health-insurance quotes, maternity/newborn coverage, FZOCG/public-insurance onboarding, and city-specific private-care checks.
- `vq-135`: Montenegro international-school tuition and private-preschool city quotes.

## Recommendation for next iteration

- Continue `country-deep-dive` with Serbia sections 5.6 and 5.7, unless accepted proposals or verification queue growth change the chooser.
