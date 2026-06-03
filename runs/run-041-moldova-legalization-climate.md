---
run_id: 41
date: 2026-06-03T16:11:26Z
agent: hermes
mode: country-deep-dive
target_country: Moldova
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 59
sources_added: ["src-219", "src-220", "src-221", "src-222", "src-223", "src-224", "src-225"]
facts_added: 8
facts_verified: 0
claims_added: ["claim-moldova-001", "claim-moldova-002", "claim-moldova-003", "claim-moldova-004", "claim-moldova-005", "claim-moldova-006"]
files_modified:
  - countries/moldova.md
  - claims/moldova.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-041-moldova-legalization-climate.md
proposals_created: []
completed_at: 2026-06-03T16:11:26Z
status: completed
schema_version: 2.0.0
---

# Run 041 - Moldova legalization and climate

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was below the active threshold after run-040.
- Open Moldova as the next fresh depth-0 Tier-3-hint country in the anti-clustering rotation.
- Focus on sections 5.1 and 5.2: entry / TP / ordinary residence / digital nomad / long-term ladder / climate DoD.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Created `countries/moldova.md` and `claims/moldova.yml`.
- Reused `src-204` as a medium-confidence Ukrainian-passport entry placeholder and added seven Moldova sources (`src-219` through `src-225`): GIM provisional stay, GIM digital-nomad residence checklist, GIM permanent residence, UNHCR Moldova temporary protection, Climate to Travel, WeatherSpark, and GIM family reunification.
- Advanced section 5.1 to partial: TP eligibility/registration/rights through 01 March 2027, provisional-stay categories for stays over 90 days, an official digital-nomad document list and income formula, PR baselines, Polish residence-card caveat, and conservative no-captured-post-TP-bridge baseline.
- Completed section 5.2 at medium confidence with Chisinau, Balti, and Tiraspol temperature baselines, low muggy-day burden, and WeatherSpark clearer-sky day-equivalent proxies.
- Added risk flags `digital-nomad-threshold-current-year-gap`, `pr-counting-for-digital-nomad-unclear`, `post-2027-tp-bridge-gap`, and `transnistria-practical-risk`.
- Added `vq-068` and `vq-069` for official Ukraine entry / TP bridge / citizenship and DN threshold / dependent / PR-counting mechanics.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No existing verification item was resolved.
- Pending/open verification queue increased from 7 to 9 due to two Moldova legal follow-up items.

## What remains

- Moldova taxes, cost of living, rent, healthcare, education, comfort, partner fit, risk dimensions, bureaucracy, and citizenship remain pending.
- The main legal blockers are the official Ukraine entry table, current numeric digital-nomad income threshold, DN dependent mechanics, DN/IT PR counting, and citizenship / dual-citizenship baseline.

## Open questions added

- `vq-068` — Moldova official Ukraine entry, post-TP bridge, and citizenship baseline.
- `vq-069` — Moldova DN threshold, dependent treatment, and DN/IT PR counting.

## Recommendation for next iteration

- Continue `country-deep-dive` with a fresh depth-0 country, preferably Mexico sections 5.1 and 5.2, while the pending/open verification queue remains below the active threshold.
