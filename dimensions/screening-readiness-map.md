# Dimension: Screening readiness map

Last updated: 2026-07-07
Mode: consolidation
Inputs: `state.json`, `INDEX.md`, `dimensions/risk-dimensions-5.10.md`, `dimensions/bureaucracy-practicality-5.11.md`, `dimensions/tier-field-consistency-check.md`, `dimensions/route-durability-5.1.md`, `dimensions/tax-budget-stress-5.3.md`, `dimensions/cost-rent-affordability-5.4-5.5.md`, `dimensions/healthcare-education-access-5.6-5.7.md`, `dimensions/comfort-partner-fit-5.8-5.9.md`, `dimensions/final-synthesis-readiness-checklist.md`, `dimensions/application-prep-trigger-map.md`, `dimensions/handoff-maintenance-check.md`
Consolidation status (run-294): all 33 profiles remain depth 10.0, the global verification queue has 0 pending/open items, country-local `unverified_count` values are reconciled, stale claims are 0, the tier-field consistency check confirms that country frontmatter, `countries.yml`, `state.json`, and `INDEX.md` agree on all assigned screening tiers, the non-ranking dimension maps cover route durability (5.1), tax / one-income budget stress (5.3), cost / rent affordability pressure (5.4/5.5), healthcare / education practical access (5.6/5.7), comfort / partner fit (5.8/5.9), risk dimensions (5.10), and bureaucracy / practicality (5.11), `dimensions/final-synthesis-readiness-checklist.md` ties those maps together as a downstream handoff checklist, `dimensions/application-prep-trigger-map.md` defines when future finalist-specific application-prep work should begin, and `dimensions/handoff-maintenance-check.md` records the current no-trigger maintenance state without creating a TOP-N ranking.

## Scope

This scaffold records what the downstream synthesis process can safely consume without turning the vault into a final TOP-N recommendation. It does not assign new tiers, scores, or rankings. It only separates completed screening coverage from known partial sections and names the next safe research gates.

## Current coverage snapshot

- Country profiles: 33/33 researched and represented in `INDEX.md`.
- Average depth score: 10.00 from live `state.json` values.
- Full 10.0 depth profiles: 33/33 countries.
- Below-full-depth profile: none; Portugal is now 10.0, with 5.1, 5.3, and 5.6 still partial but sufficient for screening-depth coverage.
- Verification queue: 0 pending/open items at run-250 pre-flight; country-local unverified counters are also 0 after reconciliation.
- Staleness queue: 0 stale claims at run-250 pre-flight.
- Completed cross-country dimensions available for synthesis support: 5.1 route durability, 5.3 tax / budget stress, 5.4/5.5 cost / rent affordability pressure, 5.6/5.7 healthcare / education practical access, 5.8/5.9 comfort / partner fit, 5.10 risk dimensions, 5.11 bureaucracy/practicality, the run-249 tier-readiness audit, the run-250 unverified-count reconciliation note, the run-251 tier-normalization worksheet, the run-285 tier-field consistency check, the run-291 final synthesis-readiness checklist, the run-292 application-prep trigger map, and the run-294 handoff maintenance check.

## Safe synthesis inputs available now

- Use `INDEX.md` for country coverage, depth, and completed/partial section state.
- Use `state.json` as the source of truth for current depth scores, partial sections, risk flags, source count, claim count, and queue size.
- Use `dimensions/route-durability-5.1.md` for legal-route durability buckets and bridge-vs-settlement guardrails.
- Use `dimensions/tax-budget-stress-5.3.md` for tax / one-income budget stress buckets and tax-favorable-but-immigration-gated guardrails.
- Use `dimensions/cost-rent-affordability-5.4-5.5.md` for cost / rent affordability-pressure buckets and city-discipline guardrails.
- Use `dimensions/healthcare-education-access-5.6-5.7.md` for healthcare / education practical-access buckets, public/private care guardrails, and school-cost / language-integration caveats.
- Use `dimensions/comfort-partner-fit-5.8-5.9.md` for comfort / partner-fit buckets, marriage/dependency guardrails, independent-status fallback needs, and adaptation/distance caveats.
- Use `dimensions/risk-dimensions-5.10.md` for cross-country operational risk categories and risk-driver wording.
- Use `dimensions/bureaucracy-practicality-5.11.md` for filing practicality, timing, and professional-support leads.
- Use country profiles for detailed route, tax, healthcare, school, cost, rent, comfort, partner, and bureaucracy caveats.
- Use `dimensions/final-synthesis-readiness-checklist.md` as the downstream handoff order and pre-synthesis checklist; it is still not a final recommendation or TOP-N ranking.
- Use `dimensions/application-prep-trigger-map.md` only after a human names finalists, new evidence appears, a stale-source trigger appears, or downstream synthesis requests country-specific filing-grade checks.
- Use `dimensions/handoff-maintenance-check.md` to confirm the current no-trigger state before doing further scheduled maintenance-only consolidation.
- Use `dimensions/tier-readiness-audit.md` only as a workflow-readiness check; use `dimensions/tier-normalization-worksheet.md` as a non-ranking screening-band worksheet, not as final assigned tiers; use `dimensions/tier-field-consistency-check.md` to confirm cross-file tier/count consistency before downstream synthesis.

## Do-not-use-as-final-ranking guardrails

- Do not infer a final country order from row order in any dimension file.
- Do not treat `tier_hint` as assigned final `tier`; all 33 countries have assigned screening tiers after run-284, each with explicit country-level rationale; do not treat that as a final country order.
- Do not promote partial 5.1, 5.3, or 5.6 sections into passed sections unless a later iteration explicitly completes them.
- Do not treat bridge routes such as DN / DTV / DE Rantau / virtual work as settlement ladders unless the country profile already proves a durable follow-on route.
- Do not collapse application-prep checks into active verification blockers when the queue is already resolved for screening.

## Open gates before any downstream TOP-N process

- Tier application is complete for all 33 countries after runs 252-284, ending with Armenia; run-285 confirmed cross-file tier/count consistency. Any later tier changes should be deliberate country-level revisions, not mechanical conversions from tier hints.
- Non-ranking dimension maps are now available for 5.1 route durability, 5.3 tax / budget stress, 5.4/5.5 cost / rent affordability pressure, 5.6/5.7 healthcare / education practical access, 5.8/5.9 comfort / partner fit, 5.10 risk dimensions, and 5.11 bureaucracy/practicality.
- `dimensions/final-synthesis-readiness-checklist.md` ties the dimension maps together as a safe handoff checklist for a downstream synthesis process, `dimensions/application-prep-trigger-map.md` defines when future finalist-specific application-prep work should start, and `dimensions/handoff-maintenance-check.md` records the no-trigger maintenance gate for scheduled iterations.
- Keep final recommendations, ranking, and visit order out of Hermes iterations unless the downstream synthesis process explicitly owns them.

## Next consolidation candidate

If no proposal, verification, or staleness trigger appears, the vault is ready for downstream synthesis handoff. Normal future iterations should respond to new evidence, staleness, accepted proposals, or human-directed country/application-prep focus rather than creating a TOP-N ranking.
