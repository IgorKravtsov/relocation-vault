---
run_id: 47
date: 2026-06-04T22:59:08Z
agent: hermes
mode: country-deep-dive
target_country: Malaysia
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 55
sources_added: ["src-251", "src-252", "src-253", "src-254", "src-255", "src-256"]
facts_added: 6
facts_verified: 0
claims_added: ["claim-malaysia-001", "claim-malaysia-002", "claim-malaysia-003", "claim-malaysia-004", "claim-malaysia-005", "claim-malaysia-006"]
files_modified:
  - countries/malaysia.md
  - claims/malaysia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-047-malaysia-legalization-climate.md
proposals_created: []
completed_at: 2026-06-04T22:59:08Z
status: completed
schema_version: 2.0.0
---

# Run 047 - Malaysia legalization and climate

## Plan

- Run `country-deep-dive` because there were no accepted proposals and the pending/open verification queue was 5, below the active threshold.
- Open Malaysia as the next fresh depth-0 Tier-3-hint country in the anti-clustering rotation.
- Focus on sections 5.1 and 5.2: short entry, DE Rantau digital-nomad fit, PR/citizenship baseline, and climate first pass.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Created `countries/malaysia.md` and `claims/malaysia.yml`.
- Added six Malaysia sources (`src-251` through `src-256`): Malaysian Immigration visa table and MDAC, MDEC DE Rantau, Malaysian Immigration Entry Permit, National Registration Department Article 19 citizenship, and Climate to Travel Malaysia / Kuala Lumpur climate baselines.
- Advanced section 5.1 to partial: DE Rantau is an official Professional Visit Pass for remote workers, with the tech-professional income threshold above USD 24,000/year, 3-12 month validity, renewal up to 24 months total, application possible outside Malaysia, and spouse/children dependent baseline. The long-term ladder remains unclear because no DE Rantau-to-PR route was captured.
- Advanced section 5.2 to partial: Malaysia / Kuala Lumpur climate baseline is hot, humid, and rainy year-round, with Kuala Lumpur January/July temperatures and 2,200 annual sunshine hours captured; direct sunny/clear-day counts remain queued.
- Added risk flags `derantau-bridge-only`, `pr-ladder-unclear`, `official-ukraine-entry-table-gap`, and `hot-humid-rainy-year-round`.
- Added `vq-076`, `vq-077`, and `vq-078` for official Ukrainian entry duration, DE Rantau long-term mechanics, and climate sunny-day counts.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No existing verification item was resolved.
- Pending/open verification queue increased from 5 to 8 due to three Malaysia follow-up items.

## What remains

- Malaysia taxes, cost of living, rent, healthcare, education, comfort, partner fit beyond spouse baseline, risk dimensions, bureaucracy, and full practical budget remain pending.
- Core legal blockers: exact official Ukraine short-stay duration, DE Rantau post-24-month options, Entry Permit / PR fit for a foreign-client IT worker, Professional Visit Pass time-counting, and unmarried-partner treatment.
- Climate blocker: direct sunny/clear-day counts for Kuala Lumpur, Penang/George Town, and Johor Bahru.

## Open questions added

- `vq-076` — Malaysia official Ukrainian-passport short-stay status and duration.
- `vq-077` — DE Rantau long-term route, PR counting, dependent mechanics, and durable alternatives.
- `vq-078` — Malaysia sunny/clear-day counts for target cities.

## Recommendation for next iteration

- Continue `country-deep-dive` with Thailand sections 5.1 and 5.2 unless accepted proposals or a threshold-triggered mode appears.
