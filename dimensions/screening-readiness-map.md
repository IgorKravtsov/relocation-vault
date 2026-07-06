# Dimension: Screening readiness map

Last updated: 2026-07-06
Mode: consolidation
Inputs: `state.json`, `INDEX.md`, `dimensions/risk-dimensions-5.10.md`, `dimensions/bureaucracy-practicality-5.11.md`, `dimensions/tier-field-consistency-check.md`, `dimensions/route-durability-5.1.md`
Consolidation status (run-286): all 33 profiles remain depth 10.0, the global verification queue has 0 pending/open items, country-local `unverified_count` values are reconciled, stale claims are 0, the tier-field consistency check confirms that country frontmatter, `countries.yml`, `state.json`, and `INDEX.md` agree on all assigned screening tiers, and `dimensions/route-durability-5.1.md` now provides a non-ranking legal-route durability map.

## Scope

This scaffold records what the downstream synthesis process can safely consume without turning the vault into a final TOP-N recommendation. It does not assign new tiers, scores, or rankings. It only separates completed screening coverage from known partial sections and names the next safe research gates.

## Current coverage snapshot

- Country profiles: 33/33 researched and represented in `INDEX.md`.
- Average depth score: 10.00 from live `state.json` values.
- Full 10.0 depth profiles: 33/33 countries.
- Below-full-depth profile: none; Portugal is now 10.0, with 5.1, 5.3, and 5.6 still partial but sufficient for screening-depth coverage.
- Verification queue: 0 pending/open items at run-250 pre-flight; country-local unverified counters are also 0 after reconciliation.
- Staleness queue: 0 stale claims at run-250 pre-flight.
- Completed cross-country dimensions available for synthesis support: 5.1 route durability, 5.10 risk dimensions, 5.11 bureaucracy/practicality, the run-249 tier-readiness audit, the run-250 unverified-count reconciliation note, the run-251 tier-normalization worksheet, and the run-285 tier-field consistency check.

## Safe synthesis inputs available now

- Use `INDEX.md` for country coverage, depth, and completed/partial section state.
- Use `state.json` as the source of truth for current depth scores, partial sections, risk flags, source count, claim count, and queue size.
- Use `dimensions/route-durability-5.1.md` for legal-route durability buckets and bridge-vs-settlement guardrails.
- Use `dimensions/risk-dimensions-5.10.md` for cross-country operational risk categories and risk-driver wording.
- Use `dimensions/bureaucracy-practicality-5.11.md` for filing practicality, timing, and professional-support leads.
- Use country profiles for detailed route, tax, healthcare, school, cost, rent, comfort, partner, and bureaucracy caveats.
- Use `dimensions/tier-readiness-audit.md` only as a workflow-readiness check; use `dimensions/tier-normalization-worksheet.md` as a non-ranking screening-band worksheet, not as final assigned tiers; use `dimensions/tier-field-consistency-check.md` to confirm cross-file tier/count consistency before downstream synthesis.

## Do-not-use-as-final-ranking guardrails

- Do not infer a final country order from row order in any dimension file.
- Do not treat `tier_hint` as assigned final `tier`; all 33 countries have assigned screening tiers after run-284, each with explicit country-level rationale; do not treat that as a final country order.
- Do not promote partial 5.1, 5.3, or 5.6 sections into passed sections unless a later iteration explicitly completes them.
- Do not treat bridge routes such as DN / DTV / DE Rantau / virtual work as settlement ladders unless the country profile already proves a durable follow-on route.
- Do not collapse application-prep checks into active verification blockers when the queue is already resolved for screening.

## Open gates before any downstream TOP-N process

- Tier application is complete for all 33 countries after runs 252-284, ending with Armenia; run-285 confirmed cross-file tier/count consistency. Any later tier changes should be deliberate country-level revisions, not mechanical conversions from tier hints.
- Decide whether cross-country dimensions are needed for 5.3, 5.4/5.5, 5.6/5.7, and 5.8/5.9 before synthesis; 5.1 now has a non-ranking route-durability map.
- Keep final recommendations, ranking, and visit order out of Hermes iterations unless the downstream synthesis process explicitly owns them.

## Next consolidation candidate

If no proposal, verification, or staleness trigger appears, the next safe consolidation unit is a non-ranking synthesis-readiness pass for another uncovered cross-country dimension, such as tax/budget stress (5.3), cost/rent pressure (5.4/5.5), healthcare/education access (5.6/5.7), or comfort/partner fit (5.8/5.9), while avoiding TOP-N recommendations.
