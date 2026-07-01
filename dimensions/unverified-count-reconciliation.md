# Dimension: Unverified-count reconciliation

Last updated: 2026-07-01
Mode: consolidation
Inputs: `verification-queue.md`, `state.json`, country frontmatter

## Scope

This is a data-hygiene consolidation note. It reconciles legacy country-local `unverified_count` counters with the global verification queue. It does not reopen resolved blockers, complete partial sections, assign tiers, or rank countries.

## Reconciliation performed

| Country | Previous local counter | Global pending/open queue items for country | New local counter | Note |
|---|---:|---:|---:|---|
| Poland | 4 | 0 | 0 | Remaining legal/tax/healthcare caveats are profile-level application-prep or partial-section caveats, not active global queue blockers. |
| Romania | 1 | 0 | 0 | Remaining DN/tax/healthcare caveats are profile-level application-prep or partial-section caveats, not active global queue blockers. |

## Result

- `verification-queue.md`: 0 pending/open items.
- `state.json`: all country `unverified_count` values are now 0.
- Country frontmatter: all country `unverified_count` values are now 0.
- Screening caveats remain preserved in country prose, risk flags, and partial-section status.

## Next safe handoff

Run the dedicated non-ranking tier-normalization pass only if no proposal, verification, or staleness trigger appears. Use the country profiles and `dimensions/tier-readiness-audit.md`; do not infer final rankings from this hygiene note.
