# Dimension: Handoff maintenance check

Last updated: 2026-07-16
Mode: consolidation
Inputs: `state.json`, `INDEX.md`, `verification-queue.md`, `sources/sources.md`, `claims/*.yml`, `dimensions/final-synthesis-readiness-checklist.md`, `dimensions/application-prep-trigger-map.md`
Consolidation status (run-365): scheduled no-trigger recheck confirming that the vault remains in downstream handoff mode. This file does not rank countries, choose finalists, change tiers, update claims, update sources, or reopen resolved verification items.

## Scope

This check records the safe condition for future scheduled normal iterations after screening completion. It is a maintenance artifact for the vault, not a final synthesis, recommendation, TOP-N list, visit order, or application-prep instruction.

## Current maintenance gates

| Gate | Current status | Action for normal iterations |
|---|---|---|
| Accepted proposals | none in `proposals/queue.md` | No `proposal-apply` work. |
| Verification queue | 0 pending/open items | Do not reopen resolved-for-screening items without new evidence or explicit direction. |
| Stale claims | 0 stale claims in the run-365 no-trigger recheck | No staleness-check work until `scripts/find-stale.py` reports stale items. |
| Country depth | 33/33 at depth_score 10.0 | No broad country-deep-dive work unless a profile changes or a human names a focus. |
| Assigned screening tiers | 33/33 assigned and cross-file consistent | Tier changes must be deliberate country-level revisions, not mechanical ranking work. |
| Source / claim registry | 839 source headings and 716 claim entries | Recompute counts before any future state update. |
| Downstream handoff artifacts | screening-readiness, all non-ranking dimension maps, final-synthesis checklist, and application-prep trigger map exist | Use these as inputs only; do not create TOP-N output in normal iterations. |

## Safe next-action rules

A future scheduled normal iteration should do one of the following, in priority order:

1. Apply accepted proposals if any appear.
2. Run verification only if pending/open queue items exist.
3. Run staleness-check only if `scripts/find-stale.py` reports stale claims.
4. Run country or application-prep work only if a human names a country/route, new evidence changes a baseline, or downstream synthesis requests filing-grade checks.
5. Otherwise keep the vault in handoff mode and limit work to lightweight maintenance checks, with no ranking or recommendation.

## Guardrails preserved

- Do not infer final country order from tier values, dimension buckets, or table row order.
- Do not promote partial sections 5.1, 5.3, or 5.6 to passed without a later country-specific evidence update.
- Do not reopen application-prep caveats that were deliberately resolved for screening.
- Do not change country profiles, claims, sources, or verification statuses in maintenance-only runs.
- Do not create a final TOP-N, visit order, recommendation narrative, or filing instruction in a normal Hermes iteration.

## Result

The vault is still screening-complete and handoff-ready as of run-365. The next substantive work should be downstream synthesis, accepted proposals, stale-claim refresh, new-evidence handling, or explicit human-directed finalist/application-prep work.
