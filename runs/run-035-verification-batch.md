---
run_id: 35
date: 2026-06-02T04:01:45Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1", "5.2", "5.5"]
target_criterion: null
duration_minutes: 62
sources_added: ["src-187", "src-188", "src-189"]
facts_added: 4
facts_verified: 6
claims_added: []
files_modified:
  - countries/albania.md
  - countries/georgia.md
  - countries/portugal.md
  - countries/slovenia.md
  - countries/uruguay.md
  - claims/albania.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-035-verification-batch.md
proposals_created: []
completed_at: 2026-06-02T04:01:45Z
status: completed
schema_version: 2.0.0
---

# Run 035 — Verification batch

## Plan

- Run verification mode because the pending/open verification queue was at the active threshold (10 items) after run-034.
- Close a focused batch of operational blockers using existing official sources where sufficient, plus a small number of new sources for Slovenia salary, Albania clearer-sky proxies, and Portugal T2 rent bands.
- Avoid final ranking; only update country profiles, source registry, queue state, state.json, INDEX, CHANGELOG, and this run log.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Added three sources:
  - `src-187` — Slovenia official statistics release for March 2026 average gross/net earnings.
  - `src-188` — WeatherSpark Albania country / Vlore cloud-cover pages.
  - `src-189` — 2026 Portugal Lisbon/Porto/Faro rent comparison with T2/two-bedroom bands.
- Resolved six queue items:
  - `vq-039` Slovenia DN route: current salary screen is about EUR 3,357.62/month using the twice-net-salary formula; DN is above the couple's current budget and should be treated as a bridge.
  - `vq-052` Georgia IT route: official SDA evidence is sufficient for operational planning; treat foreign-client IT as an IT/small-business file with ordinary family reunification.
  - `vq-056` Albania climate: WeatherSpark clearer-sky proxies close the §5.2 sunny-day blocker at medium confidence.
  - `vq-057` Portugal rent: current T2/two-bedroom bands close §5.5 at medium confidence.
  - `vq-058` Uruguay permanent residence income: closed to a conservative notarial/accounting means-of-life baseline.
  - `vq-059` Uruguay DN/provisional identity: closed to a conservative bridge-only baseline; do not rely on DN time alone for habitual-residence/citizenship evidence.
- Advanced Albania section 5.2 to completed and Portugal section 5.5 to completed.
- Updated Slovenia, Georgia, and Uruguay legal notes without changing depth score because their 5.1 sections remain partial.

## Verification results

- Pending/open verification queue decreased from 10 to 4.
- Portugal depth_score increased from 2.5 to 3.0.
- Albania depth_score increased from 1.0 to 1.5.

## What remains

- Still pending/open: Romania DN official checklist (`vq-022`), Georgia current official Ukraine entry/decree (`vq-051`), Albania official Ukraine entry/TP bridge (`vq-054`), and Albania official Unique Permit remote-worker checklist/threshold/dependents/PR counting (`vq-055`).
- Many country profiles still need taxes, cost, rent, healthcare, education, comfort, partner fit, risk, and bureaucracy passes.

## Open questions added

- None.

## Recommendation for next iteration

- Verification queue is now below threshold, so resume country-deep-dive rotation. A fresh depth-0 Tier-2-hint country such as Paraguay is the next reasonable target unless accepted proposals appear.
