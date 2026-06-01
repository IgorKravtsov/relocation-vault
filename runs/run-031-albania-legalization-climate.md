---
run_id: 31
date: 2026-06-01T04:01:26Z
agent: hermes
mode: country-deep-dive
target_country: Albania
target_sections: ["5.1", "5.2"]
target_criterion: null
duration_minutes: 73
sources_added: ["src-164", "src-165", "src-166", "src-167", "src-168", "src-169", "src-170"]
facts_added: 10
facts_verified: 0
claims_added: ["claim-albania-001", "claim-albania-002", "claim-albania-003", "claim-albania-004", "claim-albania-005", "claim-albania-006", "claim-albania-007"]
files_modified:
  - countries/albania.md
  - claims/albania.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-031-albania-legalization-climate.md
proposals_created: []
completed_at: 2026-06-01T04:01:26Z
status: completed
schema_version: 2.0.0
---

# Run 031 — Albania legalization and climate first pass

## Plan

- Run a normal country-deep-dive because there were no accepted proposals and the pending verification queue was below threshold after run-030.
- Open Albania as the next fresh depth-0 Tier-2-hint country, respecting anti-clustering rather than following the prior Georgia verification hint while queue size was still 9.
- Focus on sections 5.1 and 5.2, using strong secondary sources where Albanian official pages were WAF-blocked or unreachable, and queue ordinary source gaps rather than treating them as recovery issues.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Created `countries/albania.md` from the country template.
- Captured a medium-confidence Ukraine visa-free entry baseline of 90 days within any 180-day period from an aggregator, while recording that the Albanian MFA visa-regime page was WAF-blocked (`src-164`, `src-165`).
- Recorded the official-target gap for Albanian Ukraine temporary-protection material: a Ministry URL exists but was WAF-blocked, and no current post-2027 bridge was captured (`src-165`).
- Captured 2025–2026 secondary operational baselines for the Type D + Unique Permit remote-worker route: foreign-client / foreign-employer remote work, low secondary income thresholds, document package, Albanian bank account / health insurance / criminal-record requirements, family inclusion caveat, and renewal / PR claims (`src-166`, `src-167`).
- Captured climate first-pass sources for Tirana, Durrës, and Vlorë (`src-168` through `src-170`), including January and summer temperatures, rainfall, rain days, sunshine hours, sea temperatures for coastal cities, and comfort caveats.
- Added 7 sources and 7 atomic claims.
- Added 3 verification items (`vq-054` through `vq-056`) for the official Albania visa/TP baseline, Unique Permit official checklist / thresholds / dependents / PR counting, and direct sunny/clear-day counts.
- Updated `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- No queue items were resolved in this country-deep-dive run.
- Pending/open verification queue increased from 9 to 12.

## What remains

- Verify Albania's current official visa-free entry rule for Ukrainians and whether any Ukraine temporary-protection extension or post-2027 ordinary-residence bridge exists.
- Verify the official Type D + Unique Permit remote-worker checklist, exact income threshold, fees, dependent mechanics, filing route, and PR-counting rules.
- Verify direct sunny/clear-day counts for Tirana, Durrës, and Vlorë.
- Research Albania taxes, cost of living, rent, healthcare, education, comfort, partner/student status, risk dimensions, and bureaucracy.

## Open questions added

- `vq-054` — Albania official Ukraine entry / TP / post-2027 bridge baseline.
- `vq-055` — Albania official Unique Permit remote-worker checklist, threshold, dependents, fees, and PR counting.
- `vq-056` — Albania direct sunny/clear-day counts for Tirana, Durrës, and Vlorë.

## Recommendation for next iteration

- Enter verification mode because the pending/open queue is above threshold. Prioritize Albania legal blockers and the new climate sunny-day gap before opening another fresh country.
