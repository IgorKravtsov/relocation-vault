---
run_id: 49
date: 2026-06-05T05:16:25Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1"]
target_criterion: null
duration_minutes: 40
sources_added: []
facts_added: 0
facts_verified: 5
claims_added: []
files_modified:
  - countries/argentina.md
  - countries/uae.md
  - countries/malaysia.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-049-verification-operational-baselines.md
proposals_created: []
completed_at: 2026-06-05T05:16:25Z
status: completed
schema_version: 2.0.0
---

# Run 049 - verification operational baselines

## Plan

- Run `verification` because the pending/open queue was exactly 10, at the active threshold.
- Resolve a focused batch of legal/route blockers using existing captured sources where they already support safe country-screening baselines.
- Avoid new source collection unless needed; this batch targets operational-core closure, not application-prep microdetails.

## What was done

- Pre-flight passed: repository clean on `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Resolved `vq-073` for Argentina: DN remains a transitory 180+180-day bridge, rentista excludes personal-work income, and no durable foreign-client IT residence category is captured. Argentina should not be scored as a settlement route until a specific temporary category or counsel confirms a durable file.
- Resolved `vq-074` for UAE: Emirates' 30-day visa-on-arrival baseline is sufficient for scouting-screening; official selector confirmation is a before-travel check, not a residence-route blocker.
- Resolved `vq-075` for UAE: GDRFA already provides the decisive virtual-work screening requirements (foreign remote work, USD 3,500/month, health insurance, one-year extendable residence, family sponsorship). Emirates ID, medical test, exact fees, and dependent-document details remain application-prep checks.
- Resolved `vq-076` for Malaysia: exact Ukrainian visitor-entry duration is a before-travel check; Malaysia relocation planning depends on DE Rantau or another pass, not visitor stay.
- Resolved `vq-077` for Malaysia: DE Rantau is a 3-24 month bridge and spouse/children route, not a proven PR/citizenship ladder; do not count Professional Visit Pass time toward Entry Permit / PR or citizenship without later confirmation.
- Updated Argentina, UAE, and Malaysia profiles, `verification-queue.md`, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Resolved 5 pending items: `vq-073`, `vq-074`, `vq-075`, `vq-076`, and `vq-077`.
- Pending/open verification queue decreased from 10 to 5.
- No new sources or claims were added.

## What remains

- Pending queue now focuses on `vq-055`, `vq-072`, `vq-078`, `vq-079`, and `vq-080`.
- Argentina still needs direct official tourist-exemption capture for Ukrainian ordinary passports before relying on DN visa-exempt eligibility.
- Malaysia climate still needs direct sunny/clear-day counts for Kuala Lumpur, Penang/George Town, and Johor Bahru.
- Thailand DTV/PR/citizenship blockers remain for a later verification batch.

## Open questions added

- None.

## Recommendation for next iteration

- Return to `country-deep-dive` because the pending queue is below threshold. The next fresh depth-0 Tier-3-hint country in the anti-clustering rotation is Indonesia, sections 5.1 and 5.2, unless accepted proposals or a new threshold-trigger appears.
