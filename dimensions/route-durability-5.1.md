# Dimension: Route durability map (5.1)

Last updated: 2026-07-06
Mode: consolidation
Inputs: country profiles, `state.json`, `INDEX.md`, `dimensions/tier-normalization-worksheet.md`, `dimensions/tier-field-consistency-check.md`
Consolidation status (run-286): non-ranking synthesis-input map. This file does not change country tiers, scores, sources, claims, or verification status.

## Scope

This map groups the legal-stay durability patterns already captured in country profiles. It is intended as a downstream synthesis input, not a recommendation, visit order, or TOP-N ranking. Row order follows the existing INDEX grouping.

## Route durability buckets

- **Durable settlement file captured**: the profile has a plausible ordinary residence ladder for this couple, with PR/citizenship or long-term residence mechanics screenable, but application-prep gaps may remain.
- **Conditional ordinary-residence file**: a possible self-employed, business, professional, or means-of-life route exists, but adviser confirmation, tax/status fit, income proof, or local-substance requirements are material.
- **Bridge/base route**: the captured route can support scouting or a temporary base, but the profile does not prove a reliable settlement ladder for the current income/profile.
- **High-risk / weak fit**: the captured evidence leaves a major post-2027, income, local-employment, route-counting, or route-availability blocker.

## Non-ranking country map

| Country | Assigned screening tier | Route durability bucket | Core legal-route reading for synthesis |
|---|---:|---|---|
| Spain | 2 | Conditional ordinary-residence file | DN / self-employment planning remains useful, but no captured post-2027 TP bridge and autonomo/tax/insurance costs keep the legal file conditional. |
| Portugal | 2 | Conditional ordinary-residence file | D8 / ordinary-status planning has a known long-term ladder, but the D8 income gate, self-employed tax/VAT fit, and health-insurance proof keep it conditional. |
| Italy | 2 | Conditional ordinary-residence file | DN / self-employment route is potentially durable if the registered-lease, source-of-income, tax, and family mechanics are made filing-ready. |
| Greece | 1 | Durable settlement file captured | Captured post-TP / ordinary-status planning plus DN/freelance options create a durable legal ladder, with remaining tax, insurance, and application-prep caveats. |
| Cyprus | X | High-risk / weak fit | Current profile is income-gated and bridge-heavy; no clear post-2027 TP bridge or current-budget DN success baseline is captured. |
| Croatia | X | High-risk / weak fit | DN/ordinary options exist, but the captured profile leaves major renewal, tax/craft-fit, and long-term-settlement uncertainty for this couple. |
| Malta | X | High-risk / weak fit | NRP/digital-nomad-style options are income-gated above the current profile and do not create an easy settlement ladder. |
| Czech Republic | 2 | Conditional ordinary-residence file | Business/self-employed and special Ukraine-status baselines make a possible ordinary route, but trade classification, tax, and post-TP timing remain conditional. |
| Poland | 1 | Durable settlement file captured | Existing Poland connection plus ordinary residence/business/tax planning give a captured durable route baseline, while ZUS/tax and partner mechanics stay application-prep issues. |
| Romania | X | High-risk / weak fit | DN is above budget and ordinary PFA/company options remain status/tax-heavy; no captured post-2027 TP bridge solves the current profile. |
| Bulgaria | X | High-risk / weak fit | Ordinary self-employment/company route is not yet a lightweight foreign-client IT file, and post-2027/Employment Agency fit remains weak. |
| Hungary | X | High-risk / weak fit | White Card income/family restrictions and guest self-employment limits make the captured route weak for settlement at current income. |
| Slovakia | 2 | Conditional ordinary-residence file | Evidence-heavy self-employed/business residence can be screenable, but it needs a real-business file, tax fit, and careful post-TP timing. |
| Slovenia | 2 | Conditional ordinary-residence file | DN/self-employed route is plausible but income formula, tax downside, and post-TP ordinary-permit timing keep it conditional. |
| Montenegro | 2 | Conditional ordinary-residence file | TP-to-2027 plus DN/ordinary-residence concepts make a possible base, but official income/tax/status details remain decisive. |
| Serbia | 2 | Conditional ordinary-residence file | Self-employment / independent-professional single-permit mechanics support a possible durable file, with tax, registration, and common-law/family details still important. |
| Turkey | 2 | Conditional ordinary-residence file | DN/ordinary residence can work as a legal base at the income threshold, but tax/SGK, renewals, and long-term counting keep the route conditional. |
| Georgia | 2 | Conditional ordinary-residence file | IT residence / small-business planning is promising, but tax/status fit, dependents, and renewal compatibility remain adviser-level gates. |
| Albania | 2 | Conditional ordinary-residence file | Remote-worker / Unique Permit route looks promising on budget, but official checklist, PR counting, tax, and dependent details remain conditional. |
| North Macedonia | X | High-risk / weak fit | Ordinary self-employment/company route is local-substance-heavy and not proven as a remote foreign-client IT settlement file. |
| Bosnia and Herzegovina | X | High-risk / weak fit | Company-founder/work-permit route is high-burden, with the five-employee founder requirement making it weak for the couple's profile. |
| Moldova | 3 | Bridge/base route | TP/DN/provisional-stay baselines can support a nearby base, but DN threshold, PR counting, dependents, and tax/status fit are not settlement-proof. |
| Uruguay | 2 | Durable settlement file captured | Permanent-residence means-of-life route and 3-/5-year legal-citizenship baseline create a captured settlement path, with adviser-certified income, tax/BPS, and presence discipline still required. |
| Paraguay | 2 | Conditional ordinary-residence file | Lawful-activity residence plus a temporary-to-permanent ladder is plausible, but tax/RUC, IPS, and residence-visa mechanics remain key. |
| Panama | 3 | Bridge/base route | Remote-worker route is a short bridge and territorial-tax upside is useful, but follow-on residence and source/tax classification remain unproven. |
| Mexico | X | High-risk / weak fit | Visa and solvency gates are above or uncertain for the current profile, so the route is not a reliable settlement file without savings or a lower consular threshold. |
| Argentina | 3 | Bridge/base route | DN is a bridge and citizenship has strict continuous-residence/no-exit practice risk; durable foreign-client IT residence remains unproven. |
| UAE | X | High-risk / weak fit | Tax is favorable, but the virtual-work immigration gate is above current income and citizenship/settlement is not predictable. |
| Malaysia | 3 | Bridge/base route | DE Rantau supports a 3-24 month base, but it is not a proven PR/citizenship ladder. |
| Thailand | 3 | Bridge/base route | DTV can be a multi-year bridge if financial evidence is met, but PR/citizenship and tax/status consequences are not a settlement baseline. |
| Indonesia | 3 | Bridge/base route | E33G is income-gated above the current profile, so Indonesia remains scouting/bridge-only unless income rises. |
| Kazakhstan | 3 | Bridge/base route | Neo Nomad/TRP/business mechanics are not yet a proven settlement file for foreign-client IT, and climate/security/tax details keep it as a base. |
| Armenia | 3 | Bridge/base route | Business-activity residence is possible, but it is adviser-led and not a proven lightweight DN/foreign-client IT settlement ladder. |

## Synthesis-use guardrails

- Use this file to identify which legal-route patterns need application-prep work, not to rank countries.
- Do not treat a bridge/base route as a settlement path unless the country profile later captures a durable follow-on route.
- Do not treat `tier_hint` as an assigned tier; use the assigned country `tier` fields confirmed by run-285.
- Keep partial 5.1 statuses partial unless a later country iteration explicitly completes them.

## Next safe consolidation candidates

- A non-ranking tax/budget-stress map for 5.3.
- A non-ranking cost/rent affordability-pressure map for 5.4/5.5.
- A non-ranking healthcare/education practical-access map for 5.6/5.7.
