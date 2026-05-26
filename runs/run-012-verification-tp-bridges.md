---
run_id: 12
date: 2026-05-26T22:04:11Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1"]
target_criterion: null
duration_minutes: 47
sources_added: ["src-061"]
facts_added: 1
facts_verified: 5
claims_added: []
files_modified:
  - countries/spain.md
  - countries/portugal.md
  - countries/cyprus.md
  - countries/malta.md
  - countries/czech-republic.md
  - claims/czech-republic.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
proposals_created: []
completed_at: 2026-05-26T22:04:11Z
status: completed
schema_version: 2.0.0
---

## Plan
- Run `verification` mode because the pending/open verification queue reached 10 items after run-011.
- Close one focused batch of legalization blockers, prioritizing post-04 March 2027 temporary-protection transition baselines and the Czech special long-term residence primary-source gap.
- Avoid overclaiming: where no destination-country bridge was captured, write the conservative operational answer rather than inventing a transition path.

## What was done
- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no half-written runs, and both validators passed before edits.
- Resolved `vq-004` (Spain), `vq-008` (Portugal), `vq-013` (Cyprus), and `vq-017` (Malta) by writing explicit conservative baselines into the country profiles: no captured TP-to-ordinary-residence bridge equivalent to Greece's Article 194; plan an ordinary status before TP expiry unless a later official bridge appears.
- Captured an official-primary Czech Information Portal for Foreigners page on special long-term residence as `src-061`.
- Resolved `vq-019` by updating the Czech profile and `claim-czech-005`: special long-term residence counts in full toward Czech permanent residence, while previous temporary-protection stay counts at one-half.
- Updated `verification-queue.md`, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## What remains
- Pending queue is now 5 items: Greece DN checklist (`vq-002`), Portugal climate sunny days (`vq-010`), Cyprus climate sunny days (`vq-014`), Malta climate sunny days (`vq-018`), and Czech climate sunny days (`vq-020`).
- Later Czech country-deep-dive work should still check future special-long-term-residence rounds, unmarried-partner handling, and Lex Ukraine updates.
- Resume country-deep-dive rotation with Poland sections 5.1 and 5.2 unless accepted proposals appear or the queue crosses the verification threshold again.

## Open questions added
- None.

## Recommendation for next iteration
- Run `country-deep-dive` for Poland, sections 5.1 and 5.2, as the next fresh Tier-2-hint EU country at depth 0.
