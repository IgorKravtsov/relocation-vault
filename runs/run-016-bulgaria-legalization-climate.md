---
run_id: 16
date: 2026-05-28T06:00:00Z
agent: hermes
mode: country-deep-dive
target_country: Bulgaria
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 55
sources_added: ["src-079", "src-080", "src-081", "src-082", "src-083", "src-084", "src-085", "src-086", "src-087", "src-088"]
facts_added: 12
facts_verified: 0
claims_added: ["claim-bulgaria-001", "claim-bulgaria-002", "claim-bulgaria-003", "claim-bulgaria-004", "claim-bulgaria-005", "claim-bulgaria-006", "claim-bulgaria-007", "claim-bulgaria-008"]
files_modified:
  - countries/bulgaria.md
  - claims/bulgaria.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-28T06:55:00Z
status: completed
schema_version: 2.0.0
---

## Plan

- Run default `country-deep-dive` mode: open Bulgaria sections 5.1 and 5.2 as the next fresh Tier-2-hint EU country at depth 0, following the run-015 recommendation.
- Focus on Bulgaria's self-employment residence route as the most relevant ordinary path for a remote IT worker.
- Capture the official-primary immigration law anchor if available; fall back to EU Immigration Portal summaries if Bulgarian government pages are WAF-protected.
- Queue missing primary-source gaps rather than forcing recovery mode.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, both validators passed before edits.
- Created `countries/bulgaria.md` from the country template.
- Captured the EU Immigration Portal self-employed-worker page (`src-079`) as the best available source for the self-employment route: Employment Agency permit → Type D visa → residence permit; 1-year renewable up to 3 years; 1-month exit before reapplication; 5-year PR path.
- Captured Wikipedia Bulgarian nationality law (`src-081`) for citizenship baseline: 5 years residence (3 if married to Bulgarian); Bulgarian language required; dual-citizenship restrictions for naturalized non-EU citizens.
- Confirmed EU-level TP extends to 04 March 2027 (`src-002` already in vault).
- Added climate first pass for Sofia, Plovdiv, and Varna (`src-082`, `src-083`, `src-084`, `src-085`, `src-086`, `src-087`): continental to humid subtropical; 2,260–2,340 annual sunshine hours; no direct sunny-day counts captured.
- Bulgarian Ministry of Interior Ukraine page (`src-088`) noted as WAF-protected and not directly extractable.
- Added 10 sources to `sources/sources.md`.
- Added 8 atomic claims to `claims/bulgaria.yml`.
- Added 4 verification items (`vq-029` through `vq-032`) for Bulgaria gaps.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## What remains

- Capture official-primary self-employment permit checklist, income threshold, and capital requirements.
- Capture Bulgaria-specific temporary-protection registration procedure and rights for Ukrainians.
- Capture post-04 March 2027 TP transition mechanism, if any.
- Find direct sunny-day counts for Bulgarian cities.
- Verify whether Ukraine has a dual-citizenship reciprocity agreement with Bulgaria.
- Research taxes, cost of living, rent, healthcare, education, partner/student status, risk dimensions, and bureaucracy.

## Open questions added

- `vq-029` — Bulgaria self-employment permit exact document checklist and income threshold.
- `vq-030` — Bulgaria TP registration procedure and rights for Ukrainians.
- `vq-031` — Bulgaria post-04 March 2027 TP-to-ordinary-residence bridge.
- `vq-032` — Direct annual sunny-day counts for Sofia, Plovdiv, and Varna.

## Recommendation for next iteration

- Continue country-deep-dive rotation with Hungary (sections 5.1, 5.2) as the next fresh Tier-2-hint EU country at depth 0, unless the verification queue crosses the threshold or accepted proposals appear.
