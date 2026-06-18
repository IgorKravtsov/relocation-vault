---
run_id: 152
date: 2026-06-18T17:39:01Z
agent: hermes
mode: country-deep-dive
target_country: North Macedonia
target_sections: ["5.6", "5.7"]
target_criterion: null
duration_minutes: 45
sources_added: ["src-697", "src-698", "src-699", "src-700"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-north-macedonia-016", "claim-north-macedonia-017", "claim-north-macedonia-018", "claim-north-macedonia-019"]
files_modified:
  - countries/north-macedonia.md
  - claims/north-macedonia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-152-north-macedonia-healthcare-education.md
proposals_created: []
completed_at: 2026-06-18T17:39:01Z
status: completed
schema_version: 2.0.0
---

# Run 152 - North Macedonia healthcare/education

## Plan

- Run a normal `country-deep-dive` because there are no accepted proposals and the verification queue is below the automatic threshold.
- Follow the run-151 hint and open North Macedonia sections 5.6 and 5.7, continuing the healthcare/education coverage wave.

## What was done

- Added a first-pass North Macedonia section 5.6 healthcare baseline as partial, anchored on the Ministry of Health website and a 2026 healthcare guide for FZO/private-care screening proxies.
- Added a completed first-pass North Macedonia section 5.7 education baseline covering free public Macedonian/Albanian-medium schooling, Skopje international-school options, and QSI/NOVA anchors.
- Added four source registry entries: `src-697` through `src-700`.
- Added four atomic claims: `claim-north-macedonia-016` through `claim-north-macedonia-019`.
- Added `vq-144` for healthcare insurance/onboarding/provider-price details and `vq-145` for exact school fees/private-preschool/non-Skopje availability.
- Updated North Macedonia profile frontmatter, scoring rows, practical verdict, source list, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Sources added: 4.
- Claims added: 4.
- Facts verified: 0 queue items; verification queue now has 5 pending/open items, below the automatic verification threshold.
- North Macedonia section 5.7 moved from pending to completed; section 5.6 moved from pending to partial. Depth score moved from 3.0 to 5.5.

## Key findings

- North Macedonia healthcare screens affordable for routine private care, with private GP proxies around EUR 15-25, specialist visits around EUR 25-50, and private/international insurance around EUR 50-120/month, but exact route-compliant insurance and FZO onboarding remain unresolved.
- Skopje is the safest healthcare base because major private hospitals and English-speaking private-care navigation are concentrated there; Ohrid/Bitola remain budget/climate fallbacks pending provider checks.
- Education is viable at medium confidence: public schools are free but local-language, while Skopje international-school options screen around EUR 4,000-8,000/year and create a material one-income budget risk.

## What remains

- North Macedonia comfort, partner/student fit, risk dimensions, bureaucracy, PR/citizenship route fit, exact health-insurance quotes, FZO onboarding, school fee schedules, and non-Skopje school/provider checks remain for later iterations.
- Bosnia and Herzegovina 5.6/5.7 is a natural next low-depth healthcare/education target unless accepted proposals or verification-threshold logic take priority.

## Open questions added

- `vq-144`: North Macedonia route-compliant private health-insurance quotes, maternity/newborn terms, FZO onboarding by final residence/tax status, and city-specific private-care price/provider checks.
- `vq-145`: North Macedonia exact QSI/NOVA/international-school fees, private preschool prices, and school availability outside Skopje.

## Recommendation for next iteration

- Continue `country-deep-dive` with Bosnia and Herzegovina sections 5.6 and 5.7 unless accepted proposals or verification-threshold logic take priority.
