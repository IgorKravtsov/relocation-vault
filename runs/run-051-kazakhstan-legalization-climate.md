---
run_id: 51
date: 2026-06-05T11:37:28Z
agent: hermes
mode: country-deep-dive
target_country: Kazakhstan
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 65
sources_added: ["src-267", "src-268", "src-269", "src-270", "src-271", "src-272", "src-273"]
facts_added: 5
facts_verified: 0
claims_added: ["claim-kazakhstan-001", "claim-kazakhstan-002", "claim-kazakhstan-003", "claim-kazakhstan-004", "claim-kazakhstan-005"]
files_modified:
  - countries/kazakhstan.md
  - claims/kazakhstan.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-051-kazakhstan-legalization-climate.md
proposals_created: []
completed_at: 2026-06-05T11:37:28Z
status: completed
schema_version: 2.0.0
---

# Run 051 - Kazakhstan legalization and climate

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was 7, below the active threshold.
- Open Kazakhstan as the next fresh depth-0 Tier-3-hint country in the anti-clustering rotation.
- Focus on sections 5.1 and 5.2: short entry, TRP / remote-work route fit, long-term settlement blockers, and climate first pass.

## What was done

- Pre-flight passed: repository clean on `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Created `countries/kazakhstan.md` and `claims/kazakhstan.yml`.
- Added seven Kazakhstan sources (`src-267` through `src-273`): Kazakhstan MFA visa-regime table, eGov entry/TRP guidance, a Neo Nomad secondary placeholder, Adilet migration and citizenship laws, Climate to Travel, and WeatherSpark.
- Advanced section 5.1 to partial: Ukrainian ordinary passports are officially visa-free up to 90 days; receiving party arrival notification is due within 3 working days; CIS-citizen TRP is listed for up to 1 year for labor, business-immigrant, family, study, medical, and missionary purposes.
- Treated Neo Nomad as a medium-confidence placeholder only: secondary reporting suggests a US$3,000/month remote-worker route, but official-primary checklist / dependent / renewal / settlement mechanics were not captured.
- Completed section 5.2: Astana, Almaty, and Shymkent now have January/July temperature baselines and WeatherSpark clearer-sky day-equivalent proxies. Climate verdict favors southern Kazakhstan only, with cold continental winters as a major comfort risk.
- Added risk flags `ordinary-trp-not-settlement`, `dn-route-secondary-sourced`, `pr-citizenship-ladder-unclear`, and `cold-continental-winters`.
- Added `vq-083`, `vq-084`, and `vq-085` for Neo Nomad official-primary capture, TRP/business-immigrant IT fit, and PR/citizenship mechanics.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No existing verification item was resolved.
- Pending/open verification queue increased from 7 to 10 due to three Kazakhstan legal settlement blockers.

## What remains

- Kazakhstan taxes, cost of living, rent, healthcare, education, comfort, partner mechanics, risk dimensions, bureaucracy, and practical budget remain pending.
- Core legal blockers: official Neo Nomad checklist and family mechanics; whether a foreign-client IT worker can use a TRP/business-immigrant or sole-proprietor route; whether any of these statuses count toward permanent residence or citizenship; and dual-citizenship consequences for Ukrainians.
- Climate first pass is complete, but later city-selection work should compare Almaty and Shymkent against air quality, rents, healthcare, and summer heat / winter inversion risks.

## Open questions added

- `vq-083` — Kazakhstan official-primary Neo Nomad / remote-work visa checklist and family mechanics.
- `vq-084` — Kazakhstan TRP / business-immigrant / self-employed fit for Ukrainian foreign-client IT.
- `vq-085` — Kazakhstan permanent residence and citizenship ladder for TRP / Neo Nomad / foreign-client IT.

## Recommendation for next iteration

- Run `verification` next because the pending/open queue is exactly 10, at the active threshold. Focus first on legal/route blockers that can be closed to safe operational baselines without requiring new source collection for every microdetail.
