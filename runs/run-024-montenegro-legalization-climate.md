---
run_id: 24
date: 2026-05-30T10:05:11Z
agent: hermes
mode: country-deep-dive
target_country: Montenegro
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 52
sources_added: ["src-123", "src-124", "src-125", "src-126", "src-127", "src-128", "src-129", "src-130", "src-131"]
facts_added: 11
facts_verified: 0
claims_added: ["claim-montenegro-001", "claim-montenegro-002", "claim-montenegro-003", "claim-montenegro-004", "claim-montenegro-005", "claim-montenegro-006", "claim-montenegro-007", "claim-montenegro-008"]
files_modified:
  - countries/montenegro.md
  - claims/montenegro.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-30T10:05:11Z
status: completed
schema_version: 2.0.0
---

# Run 024 — Montenegro legalization and climate first pass

## Plan

- Resume normal country-deep-dive rotation because no accepted proposals were present and the pending verification queue was below threshold after run-023.
- Open Montenegro as the next fresh depth-0 Tier-2-hint non-EU Europe country.
- Focus on sections 5.1 and 5.2, using official GOV.me / Ministry of Interior sources where available and queuing ordinary source gaps rather than treating them as recovery issues.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Created `countries/montenegro.md` from the country template.
- Captured Montenegro Ministry of Interior's 2026 temporary-protection extension page (`src-123`): temporary protection for persons from Ukraine is extended to 04 March 2027; existing holders should apply locally with valid ID and the old TP document; first-time applicants are also approved until 04 March 2027.
- Captured the official Montenegro digital-nomad portal (`src-124`) and Law on Foreign Nationals anchor (`src-125`) to confirm the route exists, while noting that this pass did not extract a clean official checklist or numeric threshold.
- Added a 2026 secondary digital-nomad guide (`src-127`) only as a medium-confidence operational placeholder for the EUR 1,350/month income-floor claim, foreign-employer/client fit, health-insurance/background-check baseline, and fee/processing-time caveats.
- Captured official temporary-protection legal anchor / 2022 Ukraine TP context (`src-126`) for the broader Montenegro TP framework.
- Completed a climate first pass for Podgorica, Budva, and Herceg Novi (`src-128` through `src-131`), including January/July temperatures, sunshine hours, direct sunny-day heuristics, and comfort caveats.
- Added 9 sources and 8 atomic claims.
- Added 3 verification items (`vq-041` through `vq-043`) for Montenegro DN official checklist/threshold/dependent mechanics, post-2027 TP bridge, and PR/citizenship/counting rules.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No queue items were resolved in this country-deep-dive run.
- Pending/open verification queue increased from 6 to 9.

## What remains

- Verify Montenegro DN current official numeric income threshold, filing route, document checklist, fees, and spouse/unmarried-partner dependent mechanics.
- Verify whether Montenegro has any explicit post-04 March 2027 TP-to-ordinary-residence bridge or post-TP filing window.
- Extract PR/citizenship rules and whether DN, TP, or ordinary temporary-residence time counts toward permanent residence.
- Research Montenegro taxes, cost of living, rent, healthcare, education, comfort, partner/student status, risk dimensions, and bureaucracy.

## Open questions added

- `vq-041` — Montenegro DN official checklist, numeric income threshold, filing route, fees, and dependent/family mechanics.
- `vq-042` — Montenegro-specific post-04 March 2027 TP-to-ordinary-residence bridge, if any.
- `vq-043` — Montenegro PR/citizenship timeline and residence-counting rules.

## Recommendation for next iteration

- Continue country-deep-dive rotation with Serbia sections 5.1 and 5.2 unless accepted proposals appear or the pending verification queue crosses the verification threshold.
