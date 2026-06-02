---
run_id: 36
date: 2026-06-02T10:15:06Z
agent: hermes
mode: country-deep-dive
target_country: Paraguay
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 58
sources_added: ["src-190", "src-191", "src-192", "src-193", "src-194", "src-195", "src-196"]
facts_added: 8
facts_verified: 0
claims_added: ["claim-paraguay-001", "claim-paraguay-002", "claim-paraguay-003", "claim-paraguay-004", "claim-paraguay-005", "claim-paraguay-006"]
files_modified:
  - countries/paraguay.md
  - claims/paraguay.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-036-paraguay-legalization-climate.md
proposals_created: []
completed_at: 2026-06-02T10:15:06Z
status: completed
schema_version: 2.0.0
---

# Run 036 — Paraguay legalization and climate

## Plan

- Run a normal country-deep-dive because there were no accepted proposals and the pending/open verification queue was below the verification threshold after run-035.
- Open a fresh depth-0 Tier-2-hint country per anti-clustering / target-selection rules.
- Focus on Paraguay sections 5.1 and 5.2: entry/residence/citizenship baseline plus climate DoD.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Created `countries/paraguay.md` and `claims/paraguay.yml`.
- Added seven Paraguay sources (`src-190` through `src-196`): DNM visa information, temporary residence, permanent residence category change, BACN Constitution, Climate to Travel country climate, WeatherSpark country climate comparison, and the Investor Pass announcement for high-capital context.
- Advanced Paraguay section 5.1 to partial at medium confidence: Ukrainian tourist visa-free entry up to 90 days, the residence / lucrative-activity visa caveat, temporary residence up to 2+2 years, temporary-to-permanent category change, official fee baselines, and constitutional naturalization after 3 years of radication.
- Completed Paraguay section 5.2 at medium confidence with Asuncion, Ciudad del Este, and Encarnacion temperature baselines, humidity/rain/comfort notes, and WeatherSpark clearer-sky day-equivalent proxies.
- Added risk flags `residence-visa-for-lucrative-activity-gap`, `no-fixed-remote-income-threshold`, and `hot-humid-summers`.
- Added `vq-060` and `vq-061` for Paraguay residence-visa mechanics and foreign-client IT / partner file mechanics.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No existing verification item was resolved.
- Pending/open verification queue increased from 4 to 6 due to two Paraguay legal follow-up items.

## What remains

- Paraguay taxes (5.3), cost of living, rent, healthcare, education, comfort, partner fit, risk dimensions, and bureaucracy remain pending.
- The main operational blockers are the Ukrainian residence / lucrative-activity visa route and whether foreign-client IT income is accepted as a lawful-activity temporary-residence file for a couple on about USD 3,000/month.
- Spouse vs unmarried-partner residence mechanics were not captured and should be checked before scoring partner fit.

## Open questions added

- `vq-060` — Paraguay residence / lucrative-activity visa route for Ukrainian citizens and whether in-country conversion from tourist entry is accepted.
- `vq-061` — Paraguay lawful-activity temporary residence for a foreign-client IT worker, income sufficiency, tax-registration implications, and spouse/unmarried-partner mechanics.

## Recommendation for next iteration

- Continue country-deep-dive rotation with Panama sections 5.1/5.2 while the verification queue remains below threshold.
