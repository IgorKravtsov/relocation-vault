---
run_id: 39
date: 2026-06-03T04:07:07Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1"]
target_criterion: null
duration_minutes: 52
sources_added: []
facts_added: 0
facts_verified: 5
claims_added: []
files_modified:
  - countries/romania.md
  - countries/paraguay.md
  - countries/panama.md
  - countries/north-macedonia.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-039-verification-operational-baselines.md
proposals_created: []
completed_at: 2026-06-03T04:07:07Z
status: completed
schema_version: 2.0.0
---

# Run 039 - verification operational baselines

## Plan

- Run `mode: verification` because the pending/open verification queue reached the active threshold of 10 after run-038.
- Close one focused batch of legal blockers at the operational-core level using existing official/source evidence where a safe planning baseline is already possible.
- Avoid adding new sources unless needed; do not over-hunt application-prep micro-details.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Resolved `vq-022` for Romania: the digital-nomad route is usable for country screening from OUG 194/2002, E-VISA / diplomatic-mission filing, and the existing secondary checklist. Consular health-insurance wording, legalization, appointment/payment, and processing time remain application-prep checks.
- Resolved `vq-060` for Paraguay: official DNM evidence supports the safe split baseline that Ukrainian tourist entry is visa-free up to 90 days, while residence / lucrative activity should be assumed visa-required unless DNM/consulate or counsel confirms an exception.
- Resolved `vq-061` for Paraguay: foreign-client IT should be treated as a generic lawful-activity temporary-residence file with professional evidence and tax/accountant review, not a fixed-threshold DN route; marriage or separate eligibility is the conservative partner baseline.
- Resolved `vq-063` for Panama: the official remote-worker visa is a 9+9 month non-resident bridge; friendly-countries / foreign-professional follow-on residence is unproven for a Ukrainian foreign-client IT worker until a country-list / lawyer check confirms it.
- Resolved `vq-065` for North Macedonia: no DN-style foreign-client route is captured; the operational baseline is a real local self-employment/company/work-permit file, with marriage or separate eligibility for the partner.
- Updated affected country files, `verification-queue.md`, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Resolved 5 queue items: `vq-022`, `vq-060`, `vq-061`, `vq-063`, `vq-065`.
- Pending/open verification queue decreased from 10 to 5.
- No new sources or claims were added.

## What remains

- Still pending: `vq-051`, `vq-054`, `vq-055`, `vq-062`, and `vq-064`.
- These are mostly official entry / Ukraine-protection / official-primary route-capture blockers for Georgia, Albania, Panama, and North Macedonia.
- Since the queue is below the active threshold, the next normal iteration can resume country-deep-dive rotation.

## Open questions added

- None.

## Recommendation for next iteration

- Continue `country-deep-dive` with a fresh depth-0 country, preferably Bosnia and Herzegovina sections 5.1 and 5.2, unless accepted proposals appear.
