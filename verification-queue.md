---
document: verification-queue
version: 1.0.0
last_updated: 2026-06-01
---

# Verification Queue

Facts marked `[требует верификации]` that need cross-reference or primary-source confirmation. Format per `vault-protocol.md` §3.7.

Items are added during regular iterations. Closed in batches during `mode: verification` iterations.

## High priority

## vq-001 [high priority]
- **Fact**: "How a Polish `karta pobytu` / Polish non-TP residence interacts with a move to Greece and with DN or TP options"
- **Country**: Greece
- **Section**: 5.1
- **Current source**: src-001, src-002, src-005
- **Why uncertain**: Current sources confirm the one-Member-State rule for temporary protection, but do not explicitly explain how a Polish residence permit that is not TP affects long-stay residence planning in Greece.
- **Suggested verification**: Check Greek consular guidance, EU long-stay mobility rules, or a current Greek immigration-lawyer explainer.
- **Created**: 2026-05-24 (run-002)
- **Status**: resolved
- **Resolved**: 2026-05-25 (run-005)
- **Resolution note**: The Greece profile now makes the operational answer explicit: a Polish residence title does not replace the need for a Greek status, and if the Polish status is itself temporary protection, Greece's one-Member-State TP rule blocks a second Greek TP file. [src-001][src-002][src-003]

## vq-002 [high priority]
- **Fact**: "Exact Greek DN document checklist, fees, apostille/translation requirements from an official-primary source"
- **Country**: Greece
- **Section**: 5.1
- **Current source**: src-003, src-004
- **Why uncertain**: Resolved at the operational-core level; the Greece profile now uses the Hellenic MFA digital-nomad page as an official-primary route/checklist anchor. Serving-consulate appointment/payment/localisation details remain application-prep checks rather than a vault blocker.
- **Suggested verification**: none for core route; check serving consulate immediately before filing.
- **Created**: 2026-05-24 (run-002)
- **Status**: resolved
- **Resolved**: 2026-05-31 (run-028)
- **Resolution note**: Official MFA digital-nomad page now anchors the DN route/checklist baseline alongside the earlier Work From Greece threshold/family sources. [src-003][src-004][src-152]

## Medium priority

## vq-003 [medium priority]
- **Fact**: "Exact sunny days per year for Athens, Thessaloniki, and Heraklion"
- **Country**: Greece
- **Section**: 5.2
- **Current source**: src-008, src-009, src-010
- **Why uncertain**: Current climate sources provide temperatures, humidity, and sunshine hours but not direct sunny-day counts in machine-readable form.
- **Suggested verification**: Find a source that exposes explicit day counts (meteoblue chart data, HNMS climate atlas, or another statistical source).
- **Created**: 2026-05-24 (run-002)
- **Status**: resolved
- **Resolved**: 2026-05-26 (run-009)
- **Resolution note**: Current Results gives annual sunshine hours and clear-sky percentages for Athens, Thessaloniki, and Heraklion; the Greece profile now records medium-confidence clear-sky day-equivalent proxies and treats the climate blocker as closed. [src-044]

## vq-004 [medium priority]
- **Fact**: "Spain's official post-04 March 2027 transition path from Ukrainian temporary protection into an ordinary residence permit, if any"
- **Country**: Spain
- **Section**: 5.1
- **Current source**: src-002, src-011, src-012
- **Why uncertain**: Resolved to conservative planning baseline: no captured Spanish bridge equivalent to Greece's Article 194 mechanism.
- **Suggested verification**: none
- **Created**: 2026-05-24 (run-003)
- **Status**: resolved
- **Resolved**: 2026-05-26 (run-012)
- **Resolution note**: The Spain profile now records the safe operational baseline: TP is current protection through the EU horizon, not a documented automatic ordinary-residence off-ramp, so plan a standard Spanish route before TP expiry. [src-002][src-011][src-012][src-013]

## vq-005 [medium priority]
- **Fact**: "How a Polish `karta pobytu` or other existing EU residence interacts with Spain-based TP or digital nomad residence planning"
- **Country**: Spain
- **Section**: 5.1
- **Current source**: src-011, src-012, src-013
- **Why uncertain**: Current Spanish sources document TP and DN separately but do not explicitly explain how an existing Polish residence title affects the move.
- **Suggested verification**: Check Spanish consular guidance, UGE-CE materials, or a current Spanish immigration-lawyer explainer.
- **Created**: 2026-05-24 (run-003)
- **Status**: resolved
- **Resolved**: 2026-05-25 (run-005)
- **Resolution note**: Spain's DN route remains a Spanish status with its own NIE and visa requirements, so a Polish residence title does not substitute for Spanish authorization; if the Polish status is TP, the EU one-Member-State TP rule remains the safe planning baseline. [src-002][src-013]

## vq-006 [medium priority]
- **Fact**: "Exact sunny days per year for Madrid, Valencia, and Málaga"
- **Country**: Spain
- **Section**: 5.2
- **Current source**: src-025
- **Why uncertain**: Resolved. Current Results provides direct annual clear-day counts for all three target cities.
- **Suggested verification**: none
- **Created**: 2026-05-24 (run-003)
- **Status**: resolved
- **Resolved**: 2026-05-25 (run-005)
- **Resolution note**: Current Results reports 97 clear days/year for Madrid, 91 for Valencia, and 107 for Málaga, which is sufficient to pass the climate DoD for Spain's section 5.2. [src-025]

## vq-007 [high priority]
- **Fact**: "Official-primary Portugal D8 / remote-work residence checklist, income-proof mechanics, and filing route"
- **Country**: Portugal
- **Section**: 5.1
- **Current source**: src-026
- **Why uncertain**: Resolved for the post-visa filing stage. AIMA now provides an official-primary filing route and document list for the remote-work residence-authorization stage.
- **Suggested verification**: none
- **Created**: 2026-05-24 (run-004)
- **Status**: resolved
- **Resolved**: 2026-05-25 (run-005)
- **Resolution note**: AIMA confirms that the post-visa route is filed by appointment/in person (with e-platform rollout noted for residence-visa holders) and requires a valid passport, valid remote-work residence visa, foreign employer/client declaration, and residence-address evidence. [src-026]

## vq-008 [high priority]
- **Fact**: "Portugal's official post-04 March 2027 transition path from Ukrainian temporary protection into an ordinary residence permit, if any"
- **Country**: Portugal
- **Section**: 5.1
- **Current source**: src-002, src-017, src-019
- **Why uncertain**: Resolved to conservative planning baseline: no captured Portuguese bridge equivalent to Greece's Article 194 mechanism.
- **Suggested verification**: none
- **Created**: 2026-05-24 (run-004)
- **Status**: resolved
- **Resolved**: 2026-05-26 (run-012)
- **Resolution note**: No captured Portuguese official bridge from TP into ordinary residence after 04 March 2027; the Portugal profile now records the conservative baseline: use D8/another ordinary status before the TP horizon rather than relying on automatic conversion. [src-002][src-019][src-026]

## vq-009 [medium priority]
- **Fact**: "How a Polish `karta pobytu` or other existing EU residence interacts with Portugal-based TP or D8 planning"
- **Country**: Portugal
- **Section**: 5.1
- **Current source**: src-017, src-020
- **Why uncertain**: Current sources explain Portugal's TP and D8 frameworks separately but do not explicitly address how an existing Polish residence title changes the move.
- **Suggested verification**: Check Portuguese consular guidance, AIMA materials, or a current Portugal immigration-lawyer explainer.
- **Created**: 2026-05-24 (run-004)
- **Status**: resolved
- **Resolved**: 2026-05-25 (run-005)
- **Resolution note**: Portugal's remote-work path is a Portuguese residence visa plus a Portuguese AIMA residence-authorization filing, so an existing Polish residence title does not substitute for Portuguese authorization; if the Polish status is TP, the EU one-Member-State TP rule remains the safe planning baseline. [src-002][src-026]

## vq-010 [medium priority]
- **Fact**: "Exact sunny days per year for Lisbon, Porto, and Faro"
- **Country**: Portugal
- **Section**: 5.2
- **Current source**: src-022, src-023, src-024
- **Why uncertain**: Current climate sources provide temperatures, humidity, and sunshine-hour intensity, but not direct annual sunny-day counts.
- **Suggested verification**: Find a source that exposes explicit day counts (for example meteoblue chart data, IPMA climatology tables, or another statistical source).
- **Created**: 2026-05-24 (run-004)
- **Status**: resolved
- **Resolved**: 2026-05-27 (run-015)
- **Resolution note**: Wikipedia Climate of Lisbon and Climate of Porto provide annual "Percentage possible sunshine" (Lisbon 63%, Porto 54%) from WMO/NOAA-sourced tables. Faro remains pending (no dedicated climate page). [src-077][src-078]

## vq-011 [high priority]
- **Fact**: "Italy's official post-04 March 2027 transition path from Ukrainian temporary protection into an ordinary residence permit, if any"
- **Country**: Italy
- **Section**: 5.1
- **Current source**: src-002, src-027, src-034
- **Why uncertain**: This iteration confirmed the TP horizon through 04 March 2027 and captured UNHCR's no-current-conversion baseline, but did not find an Italian bridge equivalent to Greece's Article 194 mechanism.
- **Suggested verification**: Check Ministry of Interior, Questura / Polizia di Stato, Integration Migrants, and Official Gazette updates for any explicit TP conversion or transitional route.
- **Created**: 2026-05-25 (run-006)
- **Status**: resolved
- **Resolved**: 2026-05-26 (run-009)
- **Resolution note**: Existing EU / Italian sources and UNHCR Italy support the safe operational baseline: no captured Italy-specific TP-to-ordinary-residence bridge; plan an ordinary Italy status before TP expiry unless a future official bridge appears. [src-002][src-027][src-034]

## vq-012 [medium priority]
- **Fact**: "Italy digital nomad / remote-worker visa 2026 income threshold and family-dependent mechanics for a Ukrainian applicant, including unmarried partner eligibility"
- **Country**: Italy
- **Section**: 5.1
- **Current source**: src-028
- **Why uncertain**: The captured consular checklist gives a 2024 income floor and names spouse/minor children for family sponsorship, but the route needs a 2026 consular cross-check and a clearer answer for an unmarried partner.
- **Suggested verification**: Check an Italian consulate serving Ukraine/Poland, Visa for Italy, and Questura guidance or a current Italian immigration-lawyer explainer.
- **Created**: 2026-05-25 (run-006)
- **Status**: resolved
- **Resolved**: 2026-05-26 (run-009)
- **Resolution note**: The captured Italian consular DN checklist supports spouse and minor children for family sponsorship and does not cover an unmarried partner; the operational baseline is marriage or another independently eligible status for the partner. [src-028]

## vq-013 [high priority]
- **Fact**: "Cyprus-specific official post-04 March 2027 transition path from Ukrainian temporary protection into ordinary residence, if any"
- **Country**: Cyprus
- **Section**: 5.1
- **Current source**: src-002, src-036
- **Why uncertain**: Resolved to conservative planning baseline: no captured Cyprus-specific bridge equivalent to Greece's Article 194 mechanism.
- **Suggested verification**: none
- **Created**: 2026-05-25 (run-007)
- **Status**: resolved
- **Resolved**: 2026-05-26 (run-012)
- **Resolution note**: No captured Cyprus-specific TP-to-ordinary-residence bridge; the Cyprus profile now records the baseline: do not rely on TP alone after 04 March 2027 unless Cyprus publishes a later transition rule. [src-002][src-035][src-036]

## vq-014 [medium priority]
- **Fact**: "Direct annual sunny-day counts for Nicosia, Limassol/Larnaca, and Paphos"
- **Country**: Cyprus
- **Section**: 5.2
- **Current source**: src-039
- **Why uncertain**: Current climate source provides temperatures, humidity, precipitation days, and annual sun hours, but not direct annual sunny-day counts for the target cities.
- **Suggested verification**: Check Cyprus Meteorological Service climate normals, WMO city climate pages, meteoblue chart data, or another statistical source with explicit sunny/clear-day counts.
- **Created**: 2026-05-25 (run-007)
- **Status**: resolved
- **Resolved**: 2026-05-30 (run-023)
- **Resolution note**: Cyprus profile now uses WeatherSpark monthly clearer-sky percentages as annual day-equivalent proxies: Nicosia ~295, Limassol ~296, Paphos ~294. These are labelled as medium-confidence clearer-sky proxies rather than official sunny-day counts. [src-119]

## Low priority
_(none)_

## vq-015 [high priority]
- **Fact**: "Croatia-specific official post-04 March 2027 transition path from Ukrainian temporary protection into ordinary residence, if any"
- **Country**: Croatia
- **Section**: 5.1
- **Current source**: src-002, src-040
- **Why uncertain**: EU-level temporary protection is extended to 04 March 2027, and Croatia has an official TP application channel, but this pass did not find a Croatia-specific bridge equivalent to Greece's Article 194 mechanism.
- **Suggested verification**: Check MUP, Croatia4Ukraine, Government of Croatia decisions, Official Gazette / Narodne novine, and current Croatian immigration-law updates for any explicit TP conversion or transitional route.
- **Created**: 2026-05-25 (run-008)
- **Status**: resolved
- **Resolved**: 2026-05-26 (run-009)
- **Resolution note**: Existing EU/Croatia sources support the conservative baseline: Croatia has TP intake and EU TP runs to 04 March 2027, but no Croatia-specific bridge is captured; plan on an ordinary Croatian route before TP expiry. [src-002][src-040][src-041]

## vq-016 [medium priority]
- **Fact**: "Direct annual sunny-day counts for Zagreb, Split, and Dubrovnik"
- **Country**: Croatia
- **Section**: 5.2
- **Current source**: src-043
- **Why uncertain**: Current climate source provides temperatures, humidity, precipitation days, and annual sunshine hours, but not direct annual sunny/clear-day counts for the target cities.
- **Suggested verification**: Check Croatian Meteorological and Hydrological Service climate normals, WMO city climate pages, meteoblue chart data, or another statistical source with explicit sunny/clear-day counts.
- **Created**: 2026-05-25 (run-008)
- **Status**: resolved
- **Resolved**: 2026-05-26 (run-009)
- **Resolution note**: Current Results provides direct annual sunshine-day counts: Zagreb-Maksimir 49, Split-Marjan 108, and Dubrovnik 127. [src-045]

## vq-017 [high priority]
- **Fact**: "Malta-specific official post-04 March 2027 transition path from Ukrainian temporary protection into ordinary residence, if any"
- **Country**: Malta
- **Section**: 5.1
- **Current source**: src-002, src-046
- **Why uncertain**: Resolved to conservative planning baseline: no captured Malta-specific bridge equivalent to Greece's Article 194 mechanism.
- **Suggested verification**: none
- **Created**: 2026-05-26 (run-010)
- **Status**: resolved
- **Resolved**: 2026-05-26 (run-012)
- **Resolution note**: No captured Malta-specific TP-to-ordinary-residence bridge; the Malta profile now records the baseline: plan an ordinary route before TP expiry, with NRP usable only if the income threshold is met and with the caveat that NRP does not lead to PR/citizenship. [src-002][src-046][src-049]

## vq-018 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Valletta, Sliema/St Julian's, and Victoria/Gozo"
- **Country**: Malta
- **Section**: 5.2
- **Current source**: src-052
- **Why uncertain**: Current climate source provides temperatures, humidity, precipitation days, and annual sunshine hours, but not direct annual sunny/clear-day counts for the target localities.
- **Suggested verification**: Check Malta Meteorological Office climate normals, WMO city climate pages, meteoblue chart data, or another statistical source with explicit sunny/clear-day counts.
- **Created**: 2026-05-26 (run-010)
- **Status**: resolved
- **Resolved**: 2026-05-30 (run-023)
- **Resolution note**: Malta profile now uses WeatherSpark monthly clearer-sky percentages as annual day-equivalent proxies: Valletta ~266, Sliema ~266, Victoria/Gozo ~265. These are labelled as medium-confidence clearer-sky proxies rather than official sunny-day counts. [src-120]

## vq-019 [high priority]
- **Fact**: "Czech special long-term residence / post-04 March 2027 bridge details for Ukrainian temporary-protection holders from an official-primary Czech source"
- **Country**: Czech Republic
- **Section**: 5.1
- **Current source**: src-002, src-053, src-061
- **Why uncertain**: Resolved for the official-primary route/status-counting anchor; later-round timing after the first registration cycle remains for ordinary follow-up rather than a blocker.
- **Suggested verification**: none for this queue item; later Czech deep-dive should still check future special-residence rounds and Lex Ukraine updates.
- **Created**: 2026-05-26 (run-011)
- **Status**: resolved
- **Resolved**: 2026-05-26 (run-012)
- **Resolution note**: Czech IPC now anchors the special long-term residence route as an official-primary source and states the PR counting rule: special long-term residence counts in full, previous temporary-protection stay counts one-half. The Czech profile and claim-czech-005 were updated. [src-053][src-056][src-061]

## vq-020 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Prague, Brno, and Ostrava"
- **Country**: Czech Republic
- **Section**: 5.2
- **Current source**: src-058, src-059, src-060
- **Why uncertain**: Current climate sources provide temperatures, humidity, precipitation, and annual sunshine hours, but not direct annual sunny/clear-day counts.
- **Suggested verification**: Check Czech Hydrometeorological Institute climate normals, WMO city climate pages, meteoblue chart data, or another statistical source with explicit sunny/clear-day counts.
- **Created**: 2026-05-26 (run-011)
- **Status**: pending

## vq-021 [medium priority]
- **Fact**: "Poland family-reunification residence permit conditions under Article 159 of the Act on Foreigners, specifically for an unmarried partner of a Polish `karta pobytu` holder, and whether marriage is required"
- **Country**: Poland
- **Section**: 5.1
- **Current source**: src-062, src-063
- **Why uncertain**: The CUKR and TP sources do not cover family-reunification rules for partners of existing Polish residence-permit holders. The couple's existing Polish `karta pobytu` is a potentially unique advantage, but the exact sponsorship rules (unmarried partner eligibility, minimum sponsor income, required documents) need an official-primary source.
- **Suggested verification**: Check UdSC family-reunification guidance, MOS portal checklist for Art. 159 residence, or the Act on Foreigners text.
- **Created**: 2026-05-27 (run-013)
- **Status**: resolved
- **Resolved**: 2026-05-28 (run-017)
- **Resolution note**: Polish voivodeship administrative guidance confirms the operational file: Article 159 condition evidence, marriage/birth certificate proof of family ties, health insurance, accommodation, and stable regular income (PLN 776 net single / PLN 600 net per family member). It does not list unmarried partners, so the safe baseline is marriage or independent eligibility. [src-091]

## vq-022 [high priority]
- **Fact**: "Romania digital-nomad visa exact document checklist, health-insurance requirement, and processing time from an official-primary source"
- **Country**: Romania
- **Section**: 5.1
- **Current source**: src-070
- **Why uncertain**: Nomad Girl gives the income threshold and duration, but the exact document list, health-insurance minimum coverage, and processing timeline need an official consulate page or IGI circular.
- **Suggested verification**: Check a Romanian consulate serving Ukraine/Poland, or the IGI digital-nomad guidance page.
- **Created**: 2026-05-27 (run-014)
- **Status**: pending

## vq-023 [medium priority]
- **Fact**: "Romania temporary-protection registration procedure and rights for Ukrainian citizens"
- **Country**: Romania
- **Section**: 5.1
- **Current source**: src-002, src-068
- **Why uncertain**: The EU-level TP decision is known, and OUG 194/2002 references temporary protection, but no Romania-specific TP registration checklist or rights summary for Ukrainians was captured.
- **Suggested verification**: Check IGI / UNHCR Romania pages, or the Romanian Government portal for Ukrainian refugees.
- **Created**: 2026-05-27 (run-014)
- **Status**: resolved
- **Resolved**: 2026-05-27 (run-015)
- **Resolution note**: UNHCR Romania Temporary Protection page confirms GII registration, residence permit, work/self-employment, healthcare, education, social assistance. Valid through 04 March 2027; auto-extended. Days in Romania under TP do not count toward 90-day Schengen limit elsewhere. [src-076]

## vq-024 [high priority]
- **Fact**: "Romania-specific official post-04 March 2027 transition path from Ukrainian temporary protection into ordinary residence, if any"
- **Country**: Romania
- **Section**: 5.1
- **Current source**: src-002, src-068
- **Why uncertain**: No captured Romania-specific bridge equivalent to Greece's Article 194 mechanism.
- **Suggested verification**: Check IGI, Romanian Government decisions, or Official Gazette for any explicit TP conversion or transitional route.
- **Created**: 2026-05-27 (run-014)
- **Status**: resolved
- **Resolved**: 2026-05-27 (run-015)
- **Resolution note**: No captured Romania-specific TP-to-ordinary-residence bridge. Conservative operational baseline: plan an ordinary status before TP expiry unless a future official transition appears. [src-002][src-076]

## vq-025 [medium priority]
- **Fact**: "Direct annual sunny-day counts for Bucharest, Cluj-Napoca, and Timișoara"
- **Country**: Romania
- **Section**: 5.2
- **Current source**: src-073, src-074, src-075
- **Why uncertain**: Current climate sources provide temperatures, humidity, precipitation, and annual sunshine hours, but not direct annual sunny/clear-day counts for the target cities.
- **Suggested verification**: Check Romanian Meteorological Administration climate normals, WMO city climate pages, meteoblue chart data, or another statistical source with explicit sunny/clear-day counts.
- **Created**: 2026-05-27 (run-014)
- **Status**: resolved
- **Resolved**: 2026-05-30 (run-023)
- **Resolution note**: Romania profile now uses WeatherSpark monthly clearer-sky percentages as annual day-equivalent proxies: Bucharest ~209, Cluj-Napoca ~198, Timișoara airport ~191. These are labelled as medium-confidence clearer-sky proxies rather than official sunny-day counts. [src-121]

## vq-026 [medium priority]
- **Fact**: "Whether Romania digital-nomad residence counts toward the 5-year EU long-term residence period"
- **Country**: Romania
- **Section**: 5.1
- **Current source**: src-068, src-070
- **Why uncertain**: OUG 194/2002 Art. 71 requires 5 years of continuous legal temporary residence or international protection, but it is unclear whether the digital-nomad permit is classified as a residence permit that counts.
- **Suggested verification**: Check IGI guidance or a Romanian immigration-law explainer on DN permit classification.
- **Created**: 2026-05-27 (run-014)
- **Status**: resolved
- **Resolved**: 2026-05-27 (run-015)
- **Resolution note**: OUG 194/2002 Art. 71 requires 5 years of continuous legal temporary residence. Digital-nomad permits are typically issued as a distinct temporary-stay category and their counting status toward long-term residence is not guaranteed. Conservative operational baseline: assume DN time does NOT count unless an explicit IGI ruling says otherwise, and plan ordinary residence routes for long-term accumulation. [src-068]

## vq-027 [medium priority]
- **Fact**: "Romania D/AC commercial-activity visa income and capital requirements for a self-employed IT freelancer"
- **Country**: Romania
- **Section**: 5.1
- **Current source**: src-068
- **Why uncertain**: OUG 194/2002 lists the D/AC visa for commercial activity but does not specify the minimum capital or business-plan requirements in the extracted text.
- **Suggested verification**: Check Romanian consulate checklist for D/AC visa, or IGI guidance for self-employed foreigners.
- **Created**: 2026-05-27 (run-014)
- **Status**: resolved
- **Resolved**: 2026-05-28 (run-017)
- **Resolution note**: OUG 194/2002 Art. 43 frames D/AC as a Romanian company/shareholder-or-associate investment route with management/administration role and business-plan requirements, not a lightweight solo IT-freelancer permit. Conservative baseline: do not treat D/AC as the fallback for a remote contractor unless building a real Romanian company/investment file. [src-068]

## vq-028 [medium priority]
- **Fact**: "Romania unmarried partner eligibility for family reunification or derived residence permit"
- **Country**: Romania
- **Section**: 5.1
- **Current source**: src-068
- **Why uncertain**: OUG 194/2002 Art. 62 references family reunification for the spouse and minor children of a sponsor, but does not explicitly address unmarried partners.
- **Suggested verification**: Check IGI family-reunification guidance, or a Romanian immigration-lawyer explainer.
- **Created**: 2026-05-27 (run-014)
- **Status**: resolved
- **Resolved**: 2026-05-27 (run-015)
- **Resolution note**: OUG 194/2002 Art. 62 defines family reunification beneficiaries as spouse and minor children; unmarried partners are not explicitly covered. Conservative operational baseline: marriage or independent eligibility (e.g., DN visa) is required for the partner to obtain derived/family residence in Romania. [src-068]

## Recently resolved (last 10)
- `vq-045` — 2026-05-30 (run-026)
- `vq-044` — 2026-05-30 (run-026)
- `vq-043` — 2026-05-30 (run-026)
- `vq-042` — 2026-05-30 (run-026)
- `vq-041` — 2026-05-30 (run-026)
- `vq-040` — 2026-05-30 (run-023)
- `vq-032` — 2026-05-30 (run-023)
- `vq-025` — 2026-05-30 (run-023)
- `vq-018` — 2026-05-30 (run-023)
- `vq-014` — 2026-05-30 (run-023)

## Dropped (cannot be verified, last 10)
_(none)_

## vq-029 [high priority]
- **Fact**: "Bulgaria self-employment permit exact income threshold, capital requirement, and document checklist from an official-primary source"
- **Country**: Bulgaria
- **Section**: 5.1
- **Current source**: src-079 (official-secondary, EU Immigration Portal summary)
- **Why uncertain**: The EU Immigration Portal describes the procedure but does not give the exact income floor, capital requirement, or document-by-document checklist for the self-employment permit.
- **Suggested verification**: Check Bulgarian Employment Agency (az.government.bg) or Migration Directorate (mvr.bg) for the detailed checklist; or a Bulgarian consulate serving Ukraine/Poland.
- **Created**: 2026-05-28 (run-016)
- **Status**: resolved
- **Resolved**: 2026-05-28 (run-017)
- **Resolution note**: Existing EU Immigration Portal evidence is enough for an operational baseline: no fixed income/capital threshold was captured; the route turns on an Employment Agency self-employment permit based on a detailed business plan and economic/social-impact assessment. Treat it as non-operational without Employment Agency / lawyer confirmation, not as a fixed-threshold DN substitute. [src-079]

## vq-030 [medium priority]
- **Fact**: "Bulgaria-specific temporary-protection registration procedure and rights for Ukrainian citizens"
- **Country**: Bulgaria
- **Section**: 5.1
- **Current source**: src-002 (EU-level TP decision), src-088 (MVR page, WAF-protected)
- **Why uncertain**: No Bulgaria-specific TP registration checklist or rights summary for Ukrainians was captured.
- **Suggested verification**: Check UNHCR Bulgaria, Bulgarian Migration Directorate, or Bulgarian Government portal for Ukrainian refugees.
- **Created**: 2026-05-28 (run-016)
- **Status**: resolved
- **Resolved**: 2026-05-28 (run-017)
- **Resolution note**: UNHCR Bulgaria confirms local TP registration, PFN/ЛНЧ and temporary registration document issuance, address-card mechanics, and core rights including residence, work without permit, medical care, education, shelter/social welfare support. [src-089]

## vq-031 [high priority]
- **Fact**: "Bulgaria-specific official post-04 March 2027 transition path from Ukrainian temporary protection into ordinary residence, if any"
- **Country**: Bulgaria
- **Section**: 5.1
- **Current source**: src-002 (EU-level TP decision)
- **Why uncertain**: No captured Bulgaria-specific bridge equivalent to Greece's Article 194 mechanism.
- **Suggested verification**: Check Bulgarian Migration Directorate, Council of Ministers decisions, or Official Gazette for any explicit TP conversion or transitional route.
- **Created**: 2026-05-28 (run-016)
- **Status**: resolved
- **Resolved**: 2026-05-28 (run-017)
- **Resolution note**: UNHCR Bulgaria confirms TP validity and card renewal through 04 March 2027 but does not describe an automatic ordinary-residence bridge. Conservative baseline: no captured Bulgaria-specific TP-to-ordinary-residence bridge; plan an ordinary route before TP expiry unless a later official transition appears. [src-002][src-089][src-090]

## vq-032 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Sofia, Plovdiv, and Varna"
- **Country**: Bulgaria
- **Section**: 5.2
- **Current source**: src-082, src-083, src-084 (Climate to Travel sunshine hours only)
- **Why uncertain**: Current climate sources provide temperatures, humidity, precipitation, and annual sunshine hours, but not direct annual sunny/clear-day counts.
- **Suggested verification**: Check Bulgarian Meteorological Service climate normals, WMO city climate pages, meteoblue chart data, Current Results, or another statistical source with explicit sunny/clear-day counts.
- **Created**: 2026-05-28 (run-016)
- **Status**: resolved
- **Resolved**: 2026-05-30 (run-023)
- **Resolution note**: Bulgaria profile now uses WeatherSpark monthly clearer-sky percentages as annual day-equivalent proxies: Sofia ~223, Plovdiv ~230, Varna ~215. These are labelled as medium-confidence clearer-sky proxies rather than official sunny-day counts. [src-118]

## vq-033 [high priority]
- **Fact**: "Hungary-specific official post-04 March 2027 transition path from Ukrainian temporary protection into ordinary residence, if any"
- **Country**: Hungary
- **Section**: 5.1
- **Current source**: src-002, src-092
- **Why uncertain**: Resolved to conservative planning baseline: EU-level temporary protection is known and OIF documents Hungary's TP framework, but no Hungary-specific bridge equivalent to Greece's Article 194 mechanism is captured.
- **Suggested verification**: none
- **Created**: 2026-05-28 (run-018)
- **Status**: resolved
- **Resolved**: 2026-05-29 (run-019)
- **Resolution note**: The Hungary profile now records the safe operational baseline: do not rely on TP alone after 04 March 2027; plan to hold or qualify for ordinary Hungarian status before TP expiry unless Hungary later publishes a transition rule. [src-002][src-092]

## vq-034 [high priority]
- **Fact**: "Hungary White Card exact consular checklist, fees, translation/apostille rules, and family-reunification availability for a Ukrainian applicant / partner"
- **Country**: Hungary
- **Section**: 5.1
- **Current source**: src-093, src-095
- **Why uncertain**: Resolved for operational planning. OIF's White Card page gives mandatory attachments and OIF family-reunification guidance gives a clear partner blocker; jurisdiction-specific consular formatting/fee details can be handled in a later application-prep pass, not as a core route blocker.
- **Suggested verification**: none
- **Created**: 2026-05-28 (run-018)
- **Status**: resolved
- **Resolved**: 2026-05-29 (run-019)
- **Resolution note**: The Hungary profile now lists the White Card document categories (foreign employer/company proof, EUR 3,000 net/month subsistence proof, accommodation, healthcare, exit means, photo) and records the key family rule: a White Card holder cannot sponsor family reunification. [src-093][src-095]

## vq-035 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Budapest, Debrecen, and Pécs"
- **Country**: Hungary
- **Section**: 5.2
- **Current source**: src-097, src-098, src-099 (Wikipedia/HungaroMet/NOAA-sourced climate tables with sunshine hours only)
- **Why uncertain**: Current climate sources provide temperatures, humidity, precipitation, and annual sunshine hours, but not direct annual sunny/clear-day counts for the target cities.
- **Suggested verification**: Check HungaroMet climate normals, WMO city climate pages, meteoblue chart data, Current Results, or another statistical source with explicit sunny/clear-day counts.
- **Created**: 2026-05-28 (run-018)
- **Status**: pending

## vq-036 [high priority]
- **Fact**: "Slovakia business/self-employed residence exact official-primary checklist and operational fit for foreign-client IT freelancing"
- **Country**: Slovakia
- **Section**: 5.1
- **Current source**: src-101 (official-secondary EU Immigration Portal), src-108 (official-primary Slovak Ministry of Economy)
- **Why uncertain**: Resolved for operational planning. The Slovak Ministry of Economy confirms the 2025+ business-plan and real-business scrutiny layer; the route is not a fixed-threshold digital-nomad substitute.
- **Suggested verification**: none for this queue item; later Slovakia tax/business deep-dive should still price tax registration, accounting, and lawyer-assisted filing.
- **Created**: 2026-05-29 (run-020)
- **Status**: resolved
- **Resolved**: 2026-05-29 (run-021)
- **Resolution note**: Slovakia profile now records the official-primary baseline: business-purpose temporary residence requires a mandatory business plan assessed for feasibility/sustainability/economic contribution, and extensions scrutinize real business activity, tax compliance, employees, and unemployment contribution. Treat foreign-client IT freelancing as evidence-heavy and adviser-dependent, not as a DN-style remote-work permit. [src-101][src-108]

## vq-037 [high priority]
- **Fact**: "Slovakia-specific official post-04 March 2027 transition path from Ukrainian temporary protection into ordinary residence, if any"
- **Country**: Slovakia
- **Section**: 5.1
- **Current source**: src-002, src-100, src-109
- **Why uncertain**: Resolved to conservative operational baseline: Slovakia officially extended temporary refuge to 04 March 2027, but the captured official update does not establish a TP-to-ordinary-residence bridge.
- **Suggested verification**: none for this queue item; monitor later Ministry of Interior / Foreign Police updates in ordinary staleness checks.
- **Created**: 2026-05-29 (run-020)
- **Status**: resolved
- **Resolved**: 2026-05-29 (run-021)
- **Resolution note**: The Slovakia profile now records the safe baseline: no captured Slovakia-specific bridge equivalent to Greece's Article 194; plan an ordinary Slovak status before TP expiry unless Slovakia later publishes a transition route. [src-002][src-100][src-109]

## vq-038 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Bratislava, Košice, and Poprad"
- **Country**: Slovakia
- **Section**: 5.2
- **Current source**: src-105, src-106, src-107 (Climate to Travel sunshine hours only)
- **Why uncertain**: Current climate sources provide temperatures, humidity, precipitation, and annual sunshine hours, but not direct annual sunny/clear-day counts for the target cities.
- **Suggested verification**: Check Slovak Hydrometeorological Institute climate normals, WMO city climate pages, meteoblue chart data, Current Results, or another statistical source with explicit sunny/clear-day counts.
- **Created**: 2026-05-29 (run-020)
- **Status**: pending

## vq-039 [high priority]
- **Fact**: "Slovenia digital-nomad residence exact current numeric income threshold, application checklist/fees, partner evidence, and whether DN time counts toward permanent residence"
- **Country**: Slovenia
- **Section**: 5.1
- **Current source**: src-111, src-112, src-113
- **Why uncertain**: GOV.SI gives the DN route and income formula (twice average monthly net salary) but this pass did not capture the current Official Gazette salary value, full application checklist, fee schedule, or explicit PR-counting rule for DN time.
- **Suggested verification**: Check Ministry of Interior / administrative-unit DN checklist, Official Gazette salary publication, and Aliens Act / official guidance on permanent-residence counting for digital-nomad temporary residence.
- **Created**: 2026-05-29 (run-022)
- **Status**: pending

## vq-040 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Ljubljana, Maribor, and Portorož/Koper"
- **Country**: Slovenia
- **Section**: 5.2
- **Current source**: src-115, src-116, src-117 (Climate to Travel sunshine hours only)
- **Why uncertain**: Current climate sources provide temperatures, humidity, precipitation, and annual sunshine hours, but not direct annual sunny/clear-day counts for the target cities.
- **Suggested verification**: Check ARSO climate normals, WMO city climate pages, meteoblue chart data, Current Results, or another statistical source with explicit sunny/clear-day counts.
- **Created**: 2026-05-29 (run-022)
- **Status**: resolved
- **Resolved**: 2026-05-30 (run-023)
- **Resolution note**: Slovenia profile now uses WeatherSpark monthly clearer-sky percentages as annual day-equivalent proxies: Ljubljana ~183, Maribor ~185, Portorož ~203. These are labelled as medium-confidence clearer-sky proxies rather than official sunny-day counts. [src-122]

## vq-041 [high priority]
- **Fact**: "Montenegro digital-nomad residence exact official-primary checklist, current numeric income threshold, filing route, fees, and dependent/family mechanics"
- **Country**: Montenegro
- **Section**: 5.1
- **Current source**: src-124 (official portal confirms route), src-127 (secondary 2026 operational placeholder)
- **Why uncertain**: Resolved for the operational core. The official GOV.me DN legal-status page gives filing route, document categories, 40-day decision period, 2+2-year duration, cooling-off period, and spouse/minor-child family baseline; it requires proof of financial means but does not expose a fixed numeric amount.
- **Suggested verification**: none for this queue item; numeric financial-means amount and fees can be handled in a later application-prep pass.
- **Created**: 2026-05-30 (run-024)
- **Status**: resolved
- **Resolved**: 2026-05-30 (run-026)
- **Resolution note**: Official GOV.me DN legal-status page now confirms the filing route, document categories, 40-day decision period, 2+2-year duration, 6-month cooling-off period, and spouse/minor-child family baseline. Numeric financial-means amount remains an application-prep detail; official page requires proof of financial means but does not expose a fixed number. [src-143]

## vq-042 [high priority]
- **Fact**: "Montenegro-specific post-04 March 2027 transition path from Ukrainian temporary protection into ordinary residence, if any"
- **Country**: Montenegro
- **Section**: 5.1
- **Current source**: src-123, src-126
- **Why uncertain**: Resolved to conservative planning baseline: the Ministry of Interior confirms TP extension to 04 March 2027, but the captured sources do not establish an ordinary-residence conversion or bridge rule.
- **Suggested verification**: none for this queue item; monitor future MUP / Official Gazette updates in staleness checks.
- **Created**: 2026-05-30 (run-024)
- **Status**: resolved
- **Resolved**: 2026-05-30 (run-026)
- **Resolution note**: Existing MUP / TP sources support the conservative operational baseline: no captured Montenegro TP-to-ordinary-residence bridge; use TP only through its published horizon and secure DN or another ordinary status before expiry unless Montenegro later publishes a conversion rule. [src-123][src-126][src-143]

## vq-043 [high priority]
- **Fact**: "Montenegro permanent residence / citizenship timeline and whether digital-nomad, temporary-protection, or ordinary temporary-residence time counts toward permanent residence"
- **Country**: Montenegro
- **Section**: 5.1
- **Current source**: src-125, src-127
- **Why uncertain**: Resolved to a conservative planning baseline: PR should be treated as a 5-year continuous-lawful-residence target, but DN alone should not be assumed to create an uninterrupted PR clock because the official DN route is capped at 2+2 years with a 6-month cooling-off period.
- **Suggested verification**: none for this queue item; later Montenegro PR/citizenship deep dive should still extract article-level law text and nationality details.
- **Created**: 2026-05-30 (run-024)
- **Status**: resolved
- **Resolved**: 2026-05-30 (run-026)
- **Resolution note**: Closed to a conservative planning baseline: treat Montenegro PR as a 5-year continuous-lawful-residence target, but do not assume DN alone creates an uninterrupted PR clock because the official DN route is 2 years + 2-year extension plus a 6-month cooling-off period. Citizenship details remain for a later nationality pass, not a current queue blocker. [src-125][src-143]

## vq-044 [high priority]
- **Fact**: "Serbia digital-nomad / self-employment official checklist, exact financial threshold, fees, processing route, and spouse/unmarried-partner dependent mechanics"
- **Country**: Serbia
- **Section**: 5.1
- **Current source**: src-135, src-136, src-137, src-139
- **Why uncertain**: Resolved for the operational core. Official sources confirm self-employment/independent-professional single-permit electronic filing and family mechanics; a separate fixed-threshold DN special category was not captured and should not be treated as the planning baseline.
- **Suggested verification**: none for this queue item; tax/APR setup, exact fee generation, and route economics belong in the next Serbia business/tax pass.
- **Created**: 2026-05-30 (run-025)
- **Status**: resolved
- **Resolved**: 2026-05-30 (run-026)
- **Resolution note**: Serbia MUP / Welcome to Serbia sources close the operational core: self-employment and independent professional work are official single-permit grounds, single-permit filing is electronic through the Foreign Nationals Portal, fees are paid in the portal, and family mechanics include both marriage and common-law marriage evidence. Treat a separate DN special-category act as later route-specific detail; tax/APR cost moves to the next Serbia business/tax pass. [src-135][src-137]

## vq-045 [high priority]
- **Fact**: "Serbia-specific post-temporary-protection bridge for Ukrainians and whether existing Polish residence/TP affects Serbian TP eligibility or benefits"
- **Country**: Serbia
- **Section**: 5.1
- **Current source**: src-133, src-134, src-136
- **Why uncertain**: Resolved to conservative planning baseline: Serbia can extend Ukraine TP by one-year periods while reasons persist, but no explicit ordinary-residence bridge was captured; Polish residence/TP does not substitute for Serbian status.
- **Suggested verification**: none for this queue item; monitor KIRS/MUP / official-gazette changes in staleness checks.
- **Created**: 2026-05-30 (run-025)
- **Status**: resolved
- **Resolved**: 2026-05-30 (run-026)
- **Resolution note**: Existing Serbian TP and Law on Foreigners sources support the safe baseline: no captured TP-to-ordinary-residence bridge; Serbian TP may be extended by one-year periods while reasons persist, but it should be treated only as a protection layer while ordinary Serbian residence is built. A Polish residence/TP title does not substitute for Serbian long-stay status. [src-133][src-134][src-136]

## vq-046 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Belgrade, Novi Sad, and Niš"
- **Country**: Serbia
- **Section**: 5.2
- **Current source**: src-140, src-141, src-142
- **Why uncertain**: Current climate sources provide temperatures, humidity, precipitation, and annual sunshine hours, but not direct sunny/clear-day counts.
- **Suggested verification**: Check WeatherSpark city cloud-cover pages, Serbia hydrometeorological service climate normals, meteoblue chart data, or another source with explicit annual sunny/clear-day counts.
- **Created**: 2026-05-30 (run-025)
- **Status**: pending

## vq-047 [high priority]
- **Fact**: "Turkey digital-nomad route official applicant-country checklist, consular / in-country workflow, fees, duration, and dependent mechanics"
- **Country**: Turkey
- **Section**: 5.1
- **Current source**: src-148
- **Why uncertain**: Resolved for the operational core. GoTurkey's official interface already confirms the DN certificate's age, income, diploma, passport/photo, and foreign-employment/freelance-contract evidence. Fees, dependent mechanics, and Ukrainian consular workflow remain application-prep checks, not a core route blocker.
- **Suggested verification**: none for the core route; check consular filing details before application.
- **Created**: 2026-05-31 (run-027)
- **Status**: resolved
- **Resolved**: 2026-05-31 (run-028)
- **Resolution note**: Turkey profile now treats GoTurkey as sufficient for the DN operational core while explicitly not overclaiming fees/dependents. [src-148]

## vq-048 [high priority]
- **Fact**: "Whether Turkey has a Ukraine-specific temporary-protection / humanitarian bridge or only ordinary residence planning for Ukrainians, and how a Polish residence/TP title affects the move"
- **Country**: Turkey
- **Section**: 5.1
- **Current source**: src-145, src-146, src-147
- **Why uncertain**: Resolved to a conservative operational baseline. PMM's temporary-protection page is Syria/mass-influx oriented and does not show a Ukraine-specific TP bridge; PMM's residence-permit-types page also says temporary-protection identification does not transfer to long-term residence. Polish residence/TP does not substitute for Turkish residence.
- **Suggested verification**: none for core planning; monitor PMM/UNHCR updates in staleness checks.
- **Created**: 2026-05-31 (run-027)
- **Status**: resolved
- **Resolved**: 2026-05-31 (run-028)
- **Resolution note**: Turkey profile now uses ordinary residence / DN-related residence as the planning baseline, not Ukraine-specific TP conversion. [src-146][src-154]

## vq-049 [high priority]
- **Fact**: "Turkey long-term residence and citizenship timeline/counting rules for digital-nomad, short-term, family, and any Ukraine-related statuses"
- **Country**: Turkey
- **Section**: 5.1
- **Current source**: src-145
- **Why uncertain**: Resolved for long-term residence counting; citizenship remains a later nationality-law pass rather than a current core blocker. PMM confirms long-term residence after at least eight years continuous residence, with half student time and full ordinary-permit time counted; temporary-protection / humanitarian residence does not transfer to long-term residence.
- **Suggested verification**: none for LTR counting; later Turkey citizenship pass should check NVI/nationality guidance.
- **Created**: 2026-05-31 (run-027)
- **Status**: resolved
- **Resolved**: 2026-05-31 (run-028)
- **Resolution note**: Turkey profile and claims now record the eight-year long-term-residence clock and residence-type counting / exclusion rules. [src-154]

## vq-050 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Istanbul, Izmir, and Antalya"
- **Country**: Turkey
- **Section**: 5.2
- **Current source**: src-149, src-150, src-151, src-162, src-163
- **Why uncertain**: Resolved at medium confidence for planning: WeatherSpark provides city cloud-cover percentages for Istanbul and Izmir; Antalya still uses a strong sunshine-hour proxy rather than an official sunny-day count.
- **Suggested verification**: none for current climate DoD; if Turkey reaches application-prep depth, check Turkish State Meteorological Service normals for an Antalya-specific official sunny/clear-day count.
- **Created**: 2026-05-31 (run-027)
- **Status**: resolved
- **Resolved**: 2026-05-31 (run-030)
- **Resolution note**: Turkey profile now records WeatherSpark clearer-sky day-equivalent proxies for Istanbul (~231 days/year) and Izmir (~266 days/year), derived from monthly clear/mostly clear/partly cloudy percentages by month length. Antalya remains represented by Climate to Travel's high sunshine-hour baseline (~2,865 h/year). [src-151][src-162][src-163]

## vq-051 [high priority]
- **Fact**: "Current official Georgian visa-free stay duration for Ukrainian citizens and transitional treatment for Ukrainians already present in Georgia"
- **Country**: Georgia
- **Section**: 5.1
- **Current source**: src-155, src-156
- **Why uncertain**: GeoConsul is the official entry portal but the country-specific Ukraine table was not cleanly extracted in this pass; the one-year stay baseline comes from a 2025 reputable-secondary report quoting a Prime Ministerial decree.
- **Suggested verification**: Capture the official decree text or GeoConsul / MFA country-specific Ukraine entry table and verify whether one-year visa-free stay remains current in 2026.
- **Created**: 2026-05-31 (run-029)
- **Status**: pending

## vq-052 [high priority]
- **Fact**: "Georgia IT residence permit 2026 work-right registration, small-business / foreign-client mechanics, and dependent treatment for spouse or unmarried partner"
- **Country**: Georgia
- **Section**: 5.1
- **Current source**: src-157
- **Why uncertain**: SDA lists the IT permit and core requirements, including USD 25,000 annual remuneration and State Employment Support Agency / small-business elements, but this pass did not capture a worked official guidance page for a foreign-client remote IT freelancer or dependent mechanics beyond generic family reunification.
- **Suggested verification**: Check State Employment Support Agency instructions, Revenue Service small-business guidance, Public Service Hall forms, and current Georgian immigration-lawyer explainers for the IT-permit filing sequence.
- **Created**: 2026-05-31 (run-029)
- **Status**: pending

## vq-053 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Tbilisi, Batumi, and Kutaisi"
- **Country**: Georgia
- **Section**: 5.2
- **Current source**: src-159, src-160, src-161
- **Why uncertain**: Current climate sources provide temperatures, rainfall, humidity/comfort notes, and sunshine hours for Tbilisi/Batumi, but not direct annual sunny/clear-day counts for all three cities.
- **Suggested verification**: Check WeatherSpark city cloud-cover pages, Georgian meteorological service climate normals, meteoblue chart data, Current Results, or another source with explicit annual sunny/clear-day counts.
- **Created**: 2026-05-31 (run-029)
- **Status**: pending

## vq-054 [high priority]
- **Fact**: "Current official Albanian visa-free entry rule for Ukrainian citizens, current Ukraine temporary-protection status, and any post-2027 bridge into ordinary residence"
- **Country**: Albania
- **Section**: 5.1
- **Current source**: src-164, src-165
- **Why uncertain**: The official MFA visa-regime and Ministry temporary-protection pages were WAF-blocked in this pass; the 90/180 entry baseline comes from an aggregator, and no current Ukraine-specific TP extension / post-2027 bridge was captured.
- **Suggested verification**: Extract Albanian MFA / e-visa / State Police / Council of Ministers material, using text mirrors or official gazette sources if needed.
- **Created**: 2026-06-01 (run-031)
- **Status**: pending

## vq-055 [high priority]
- **Fact**: "Albania Type D + Unique Permit remote-worker route official checklist, exact income threshold, fees, dependent mechanics, and whether time counts toward permanent residence"
- **Country**: Albania
- **Section**: 5.1
- **Current source**: src-166, src-167
- **Why uncertain**: Secondary sources describe the route and document set, but official e-Albania / State Police / law-text extraction was not captured; secondary sources differ on exact income thresholds and renewal/PR details.
- **Suggested verification**: Check e-Albania service pages, State Police foreigner services, Law on Foreigners / implementing decisions, or a current official checklist PDF.
- **Created**: 2026-06-01 (run-031)
- **Status**: pending

## vq-056 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Tirana, Durrës, and Vlorë"
- **Country**: Albania
- **Section**: 5.2
- **Current source**: src-168, src-169, src-170
- **Why uncertain**: Current climate sources provide temperatures, rainfall, humidity/comfort notes, and annual sunshine hours, but not direct annual sunny/clear-day counts.
- **Suggested verification**: Check WeatherSpark city cloud-cover pages, Albanian meteorological service climate normals, meteoblue chart data, Current Results, or another source with explicit annual sunny/clear-day counts.
- **Created**: 2026-06-01 (run-031)
- **Status**: pending
