---
run_id: 26
date: 2026-05-30T22:01:43Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.1"]
target_criterion: null
duration_minutes: 48
sources_added: ["src-143"]
facts_added: 5
facts_verified: 5
claims_added: ["claim-montenegro-009", "claim-montenegro-010", "claim-montenegro-011", "claim-serbia-009", "claim-serbia-010"]
files_modified:
  - countries/montenegro.md
  - countries/serbia.md
  - claims/montenegro.yml
  - claims/serbia.yml
  - sources/sources.md
  - verification-queue.md
  - state.json
  - INDEX.md
  - CHANGELOG.md
  - runs/run-026-verification-montenegro-serbia-legal-baselines.md
proposals_created: []
completed_at: 2026-05-30T22:01:43Z
status: completed
schema_version: 2.0.0
---

# Run 026 — Verification: Montenegro and Serbia legal baselines

## Plan

- Enter verification mode because the pending/open verification queue was above threshold after run-025.
- Close a focused legal batch rather than continuing country rotation.
- Prefer existing official sources when they already support a safe operational answer, and add only the minimum new source needed for Montenegro's official DN checklist.

## What was done

- Pre-flight passed: repository clean, branch `main`, `state.json` v2 valid, no accepted proposals, no half-written runs, and both validators passed before edits.
- Added `src-143`, the official GOV.me digital-nomad legal-status / application checklist page for Montenegro.
- Updated Montenegro §5.1 with the official DN filing route: personal filing at the Ministry/MIA branch, photo/fingerprints/signature capture, document categories, 40-day decision period, 2+2-year duration, 6-month cooling-off period, and spouse/minor-child family-reunification baseline.
- Closed Montenegro `vq-041` through `vq-043`: DN official checklist/family mechanics, no captured TP-to-ordinary-residence bridge, and conservative PR-counting baseline.
- Updated Serbia §5.1 using existing MUP / Welcome to Serbia sources: self-employment and independent-professional single-permit filing is electronic through the Foreign Nationals Portal, and family reunification includes both marriage and common-law marriage evidence.
- Closed Serbia `vq-044` and `vq-045`: self-employment / dependent mechanics and TP-bridge / Polish-status interaction baselines.
- Added 5 atomic claims across Montenegro and Serbia.
- Updated `state.json`, `INDEX.md`, `CHANGELOG.md`, and `verification-queue.md`.

## Verification results

- `vq-041` resolved: Montenegro official DN operational checklist captured; exact numeric financial-means amount remains a later application-prep detail.
- `vq-042` resolved: no captured Montenegro TP-to-ordinary-residence bridge; plan an ordinary status before TP expiry.
- `vq-043` resolved: treat Montenegro PR as a 5-year continuous-lawful-residence target, but do not assume DN alone creates an uninterrupted PR clock because of the 2+2-year cap and 6-month cooling-off period.
- `vq-044` resolved: Serbia self-employment / independent-professional single-permit electronic filing and marriage/common-law family mechanics confirmed from official sources.
- `vq-045` resolved: Serbian TP is a protection layer with one-year extension mechanics, not a captured ordinary-residence bridge; Polish residence/TP does not substitute for Serbian status.

## What remains

- Montenegro: verify current numeric DN financial-means amount / fee schedule in an application-prep or later legal pass; research taxes, cost of living, rent, healthcare, education, comfort, partner/student status, risk dimensions, and bureaucracy.
- Serbia: research APR/tax setup, real self-employment costs, rent/cost/healthcare, and direct sunny/clear-day counts (`vq-046`).
- Queue still contains older climate and legal items: Greece DN checklist, Czech/Hungary/Slovakia sunny-day counts, Romania DN official checklist, Slovenia DN numeric threshold/counting, and Serbia sunny-day counts.

## Open questions added

- None.

## Recommendation for next iteration

- Resume normal country-deep-dive rotation because pending/open verification queue is back below threshold. Open Turkey sections 5.1 and 5.2 as the next fresh depth-0 Tier-2-hint non-EU Europe country.
