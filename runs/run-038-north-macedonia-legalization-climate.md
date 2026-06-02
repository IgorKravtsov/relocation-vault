---
run_id: 38
date: 2026-06-02T22:01:56Z
agent: hermes
mode: country-deep-dive
target_country: North Macedonia
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 54
sources_added: ["src-204", "src-205", "src-206", "src-207", "src-208", "src-209", "src-210", "src-211", "src-212"]
facts_added: 8
facts_verified: 0
claims_added: ["claim-north-macedonia-001", "claim-north-macedonia-002", "claim-north-macedonia-003", "claim-north-macedonia-004", "claim-north-macedonia-005", "claim-north-macedonia-006"]
files_modified:
  - countries/north-macedonia.md
  - claims/north-macedonia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-038-north-macedonia-legalization-climate.md
proposals_created: []
completed_at: 2026-06-02T22:01:56Z
status: completed
schema_version: 2.0.0
---

# Run 038 - North Macedonia legalization and climate

## Plan

- Run a normal country-deep-dive because there were no accepted proposals and the pending/open verification queue was below the active threshold at the start of the iteration.
- Open North Macedonia as the next fresh depth-0 Tier-3-hint country per `state.json.next_iteration_hint` and anti-clustering.
- Focus on sections 5.1 and 5.2: entry / temporary residence / ordinary self-employment baseline and climate DoD.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Created `countries/north-macedonia.md` and `claims/north-macedonia.yml`.
- Added nine North Macedonia sources (`src-204` through `src-212`): Ukrainian passport visa-free placeholder, MFA entry rules, Invest North Macedonia work/residence permit pages, a 2025 Law on Foreigners amendments explainer, UNHCR North Macedonia fact sheet, Climate to Travel, WeatherSpark country comparison, and WeatherSpark Bitola.
- Advanced North Macedonia section 5.1 to partial at medium confidence: short-entry placeholder, Polish/EU residence-card 15-day entry rule, D visa / temporary residence category baseline, self-employment as a candidate route, stale Ukraine temporary-protection evidence, and conservative no-captured-post-2027-bridge baseline.
- Completed North Macedonia section 5.2 at medium confidence with Skopje, Ohrid, and Bitola temperature baselines, low-humidity / low-muggy-day comfort notes, and WeatherSpark clearer-sky day-equivalent proxies.
- Added risk flags `official-ukraine-entry-table-gap`, `no-dedicated-digital-nomad-visa`, and `ordinary-residence-route-needs-fit-check`.
- Added `vq-064` and `vq-065` for North Macedonia entry / protection and self-employment / partner / PR mechanics.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No existing verification item was resolved.
- Pending/open verification queue increased from 8 to 10 due to two North Macedonia legal follow-up items.

## What remains

- North Macedonia taxes (5.3), cost of living, rent, healthcare, education, comfort, partner fit, risk dimensions, and bureaucracy remain pending.
- The main legal blockers are whether Ukrainian citizens have a current official visa-free / protection route and whether a foreign-client IT worker can use self-employment / company-backed ordinary residence without local employment or significant investment.
- PR/citizenship timing and countable-residence rules still need official law-text extraction.

## Open questions added

- `vq-064` — North Macedonia Ukrainian entry / temporary-protection current status and any post-2027 bridge.
- `vq-065` — North Macedonia self-employment / foreign-client IT route, income sufficiency, partner mechanics, and PR counting.

## Recommendation for next iteration

- Switch to `mode: verification` because the pending/open verification queue reached the active threshold of 10 after this run.
