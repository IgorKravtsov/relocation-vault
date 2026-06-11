---
run_id: 100
date: 2026-06-11T21:54:00Z
agent: hermes
mode: verification
target_country: null
target_sections: ["5.3"]
target_criterion: tax-fit-screening
duration_minutes: 35
sources_added: []
facts_added: 0
facts_verified: 10
claims_added: []
files_modified:
  - countries/greece.md
  - countries/cyprus.md
  - countries/croatia.md
  - countries/malta.md
  - countries/czech-republic.md
  - countries/malaysia.md
  - countries/thailand.md
  - countries/indonesia.md
  - countries/kazakhstan.md
  - countries/armenia.md
  - verification-queue.md
  - state.json
  - CHANGELOG.md
  - runs/run-100-tax-fit-verification-baselines.md
proposals_created: []
completed_at: 2026-06-11T21:54:00Z
status: completed
schema_version: 2.0.0
---

# Run 100 - Tax-fit verification baselines

## Plan

- Switch to `verification` because the pending/open queue reached the active threshold of 10 after run-099.
- Close recent and older §5.3 tax-fit blockers where the country profiles already contain conservative worked examples and the remaining uncertainty is filing-level registration, VAT/place-of-supply, contribution, or immigration-status compatibility.
- Do not add favorable assumptions and do not mark §5.3 passed.

## What was done

- Resolved 10 tax-fit verification items for country screening: `vq-090` through `vq-094` and `vq-115` through `vq-119`.
- Updated affected country profiles to state that the exact tax registration / contribution / VAT / immigration-file fit remains application-prep or accountant work, while the existing conservative worked examples are sufficient for screening.
- Updated `verification-queue.md`, `state.json`, `INDEX.md`, and `CHANGELOG.md`.

## Verification results

- Facts verified: 10 queue items.
- Sources added: 0; no new claims.
- Pending/open verification queue moved from 10 to 0.

## Key findings

- The recurring pattern from runs 069, 075, 087, and 093 applies: exact foreign-client IT tax registration, VAT/place-of-supply, contribution base, and immigration-status fit are not required to keep comparing countries when a conservative tax baseline and downside sensitivity already exist.
- No country received a more favorable tax assumption. Greece Article 5C, Croatia lump-sum craft, Czech flat-tax/60% expense, Malta NRP, Malaysia DE Rantau, Thailand DTV, Indonesia E33G, Kazakhstan Neo Nomad/TRP, and Armenia high-tech/turnover-tax remain adviser-confirmation topics before filing.

## What remains

- All affected §5.3 sections remain partial. Passing tax DoD still requires country-specific authority/accountant confirmation for the exact filing structure.
- With the verification queue cleared, the next normal iteration can return to country deep dives.

## Open questions added

- None.

## Recommendation for next iteration

- Resume `country-deep-dive`; suggested focus: Portugal §5.6 healthcare, because Portugal is the lowest-depth Tier-1-hint profile and the verification threshold is no longer active.
