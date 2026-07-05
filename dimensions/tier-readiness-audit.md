# Dimension: Tier-readiness audit

Last updated: 2026-07-05
Mode: consolidation
Inputs: `state.json`, `countries.yml`, `INDEX.md`, country frontmatter, `verification-queue.md`, `scripts/find-stale.py`

## Scope

This is a non-ranking audit. It checks whether the vault is structurally ready for a later dedicated tier-normalization workflow. It does **not** assign final tiers, reorder countries, or recommend a TOP-N.

## Structural snapshot

- Country set: 33/33 countries are present in `countries.yml`, `state.json`, and `INDEX.md`.
- Screening depth: 33/33 countries have `depth_score: 10.0`.
- Assigned tiers: 31/33. Greece and Poland have `tier: 1`; Spain, Portugal, Italy, Czech Republic, Slovakia, Slovenia, Montenegro, Serbia, Turkey, Georgia, Albania, Uruguay, and Paraguay have `tier: 2`; Moldova, Panama, Argentina, Malaysia, Thailand, and Indonesia have `tier: 3`; Cyprus, Croatia, Malta, Romania, Bulgaria, Hungary, North Macedonia, Bosnia and Herzegovina, Mexico, and UAE have `tier: X` in country frontmatter, `countries.yml`, live state, and `INDEX.md`; the remaining 2 countries still have `tier: null`. Run-251 added the non-ranking worksheet, run-252 started schema-safe tier application, run-253 continued it with Spain, run-254 continued it with Portugal, run-255 continued it with Italy, run-256 continued it with Cyprus, run-257 continued it with Croatia, run-258 continued it with Malta, run-259 continued it with Czech Republic, run-260 continued it with Poland, run-261 continued it with Romania, run-262 continued it with Bulgaria, run-263 continued it with Hungary, run-264 continued it with Slovakia, run-265 continued it with Slovenia, run-266 continued it with Montenegro, run-267 continued it with Serbia, run-268 continued it with Turkey, run-269 continued it with Georgia, run-270 continued it with Albania, run-271 continued it with North Macedonia, run-272 continued it with Bosnia and Herzegovina, run-273 continued it with Moldova, run-274 continued it with Uruguay, run-275 continued it with Paraguay, run-276 continued it with Panama, run-277 continued it with Mexico, run-278 continued it with Argentina, run-279 continued it with UAE, run-280 continued it with Malaysia, run-281 continued it with Thailand, and run-282 continued it with Indonesia.
- Tier hints: Tier-1 hints 7; Tier-2 hints 15; Tier-3 hints 11.
- Verification queue: 0 pending/open items.
- Country-local unverified counters: 0 nonzero values after run-250 reconciliation.
- Staleness check: 0 stale claims from `scripts/find-stale.py` at run-252 pre-flight.
- Partial sections remain deliberate screening caveats: 33 countries partial in §5.1 and §5.6; 30 countries partial in §5.3. These are not active queue blockers, but they matter for final tier confidence.

## Readiness conclusion

The vault is in the **dedicated tier-normalization workflow**: runs 252-282 applied the first thirty-one country tiers, but broad automatic tier assignment is still forbidden. The inputs are complete enough to compare countries for screening, but assigned tiers should be written only in a focused run that explicitly records rationale, confidence, and caveats per country.

## Required guardrails for tier normalization

- Do not convert `tier_hint` into final `tier` mechanically.
- Do not treat all depth-10 countries as equally settlement-ready; depth measures coverage, not desirability.
- Use country Block 1 tier rationale plus §5.1, §5.3, §5.6, §5.10, and §5.11 as the core evidence set.
- Keep bridge-only routes separate from durable residence / PR / citizenship ladders.
- Preserve partial-section caveats in the tier rationale instead of forcing DoD completion.
- If a country remains `tier: null` after review, record why in the run log rather than silently skipping it.

## Data-quality notes found during audit

- `INDEX.md` summary had stale tier-hint totals from before the current country set distribution; live `countries.yml` / `state.json` show 7 Tier-1 hints, 15 Tier-2 hints, and 11 Tier-3 hints. Run-249 corrects the summary.
- Run-250 reconciled the two legacy nonzero country-local `unverified_count` values (Poland 4 and Romania 1) to 0 in country frontmatter and `state.json`, matching the global queue size of 0 pending/open items.

## Next consolidation candidate

Continue using `dimensions/tier-normalization-worksheet.md` as the normalization bridge. The next consolidation candidate is another schema-safe small-batch tier-application pass: write explicit country Block 1 rationale, country frontmatter, `countries.yml`, `state.json`, and `INDEX.md` together, and leave any unsupported country as `tier: null` with a documented blocker. If protocol changes are needed for tier confidence fields, create a proposal before editing schema-critical rules.
