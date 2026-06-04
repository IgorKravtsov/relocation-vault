---
run_id: 43
date: 2026-06-04T00:00:00Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1"]
target_criterion: null
duration_minutes: 45
sources_added: []
facts_added: 5
facts_verified: 5
claims_added: []
files_modified:
  - countries/bosnia-and-herzegovina.md
  - countries/moldova.md
  - countries/mexico.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-043-verification-operational-baselines.md
proposals_created: []
completed_at: 2026-06-04T00:00:00Z
status: completed
schema_version: 2.0.0
---

# Run 043 - Verification operational baselines

## Plan

- Run `verification` because the pending/open queue was 11, at or above the active threshold.
- Close a focused batch of legal route-fit blockers using existing official sources where they already support a safe country-screening baseline.

## What was done

- Pre-flight passed: repository clean, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Resolved five verification items without adding new sources: `vq-067`, `vq-068`, `vq-069`, `vq-070`, and `vq-071`.
- Bosnia and Herzegovina: closed the company-founder / self-employment blocker to a high-burden local company/work-permit baseline, not a DN-style remote-work route.
- Moldova: closed TP/DN blockers to conservative baselines: ordinary provisional stay before TP expiry, DN budget gate as 3x current-year forecast average salary, and no assumed DN/IT PR counting or foreign-DN dependent sponsorship.
- Mexico: closed entry and temporary-residence blockers to conservative baselines: do not assume temporary Polish residence waives the visa; standard temporary-residence income likely exceeds USD 3,000/month unless savings or a lower serving-consulate threshold works.
- Updated country profiles, `verification-queue.md`, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Pending/open queue decreased from 11 to 6.
- No new source was added; all closures rely on already captured official or reputable sources.

## What remains

- Remaining pending/open items are mostly entry-table or official-protection gaps for Georgia, Albania, Panama, North Macedonia, and Bosnia and Herzegovina.
- Since the queue is now below the active verification threshold, the next normal iteration can return to country-deep-dive unless proposals or staleness checks intervene.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive` with Argentina sections 5.1 and 5.2 as the next fresh depth-0 country, unless the protocol chooser selects another priority.
