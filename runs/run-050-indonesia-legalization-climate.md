---
run_id: 50
date: 2026-06-05T08:28:47Z
agent: hermes
mode: country-deep-dive
target_country: Indonesia
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 55
sources_added: ["src-262", "src-263", "src-264", "src-265", "src-266"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-indonesia-001", "claim-indonesia-002", "claim-indonesia-003", "claim-indonesia-004", "claim-indonesia-005"]
files_modified:
  - countries/indonesia.md
  - claims/indonesia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-050-indonesia-legalization-climate.md
proposals_created: []
completed_at: 2026-06-05T08:28:47Z
status: completed
schema_version: 2.0.0
---

# Run 050 - Indonesia legalization and climate

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was 5, below the active threshold.
- Open Indonesia as the next fresh depth-0 Tier-3-hint country in the anti-clustering rotation.
- Focus on sections 5.1 and 5.2: short entry, remote-worker route fit, post-2027 ordinary-status baseline, and climate first pass.

## What was done

- Pre-flight passed: repository clean on `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Created `countries/indonesia.md` and `claims/indonesia.yml`.
- Added five Indonesia sources (`src-262` through `src-266`): Indonesia Immigration visa index, VoA/B1 materials, E33G remote-worker visa page, Climate to Travel Indonesia/city pages, and WeatherSpark Indonesia country climate comparison.
- Advanced section 5.1 to partial: Ukrainian and Polish nationals are captured on the official VoA/e-VoA subject list for short scouting; B1 visitor stay is 30 days plus one extension to 60 days and forbids local paid work. E33G is an official 1-year remote-worker limited-stay route for work for a foreign company, but requires at least US$60,000/year income, above the couple's current ~US$36,000/year.
- Completed section 5.2: Jakarta, Surabaya, Bandung, and Bali/Denpasar now have January/July temperature baselines, rainfall/humidity/monsoon comfort notes, and WeatherSpark clearer-sky day-equivalent proxies for Jakarta, Surabaya, and Medan.
- Added risk flags `remote-worker-income-above-current-budget`, `bridge-route-not-settlement`, `pr-ladder-unclear`, and `hot-humid-rainy-climate`.
- Added `vq-081` and `vq-082` for E33G dependent/tax/conversion mechanics and official ITAP/PR/citizenship mechanics.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No existing verification item was resolved.
- Pending/open verification queue increased from 5 to 7 due to two Indonesia legal settlement blockers.

## What remains

- Indonesia taxes, cost of living, rent, healthcare, education, comfort, partner mechanics, risk dimensions, bureaucracy, and practical budget remain pending.
- Core legal blockers: E33G family/dependent treatment, tax residency for foreign-client IT income, whether repeated E33G years can convert/count toward ITAP/PR, and official citizenship/dual-citizenship consequences.
- Climate blocker is closed for first-pass DoD, but later city-selection work should verify flood exposure, air quality, and whether Bali/Bandung comfort offsets route weakness.

## Open questions added

- `vq-081` — Indonesia E33G dependent/spouse/unmarried-partner mechanics, tax residence, and durable-residence conversion/counting.
- `vq-082` — Indonesia official ITAP/PR and citizenship mechanics for a foreign-client remote IT worker without a local employer.

## Recommendation for next iteration

- Continue `country-deep-dive` because the pending/open verification queue remains below threshold. The next fresh depth-0 Tier-3-hint country in the anti-clustering rotation is Kazakhstan, sections 5.1 and 5.2, unless accepted proposals or a new threshold trigger appears.
