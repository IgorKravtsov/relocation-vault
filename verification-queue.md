---
document: verification-queue
version: 1.0.0
last_updated: 2026-05-27
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
- **Why uncertain**: MFA confirms the route exists, but this iteration did not capture a full primary-source checklist.
- **Suggested verification**: Find a Greek consulate page or ministry circular with document-by-document requirements.
- **Created**: 2026-05-24 (run-002)
- **Status**: pending

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
- **Status**: pending

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
- **Status**: pending

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
- **Status**: pending

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
- **Status**: pending

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
- **Status**: pending

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
- `vq-010` — 2026-05-27 (run-015)
- `vq-023` — 2026-05-27 (run-015)
- `vq-024` — 2026-05-27 (run-015)
- `vq-026` — 2026-05-27 (run-015)
- `vq-028` — 2026-05-27 (run-015)
- `vq-004` — 2026-05-26 (run-012)
- `vq-008` — 2026-05-26 (run-012)
- `vq-013` — 2026-05-26 (run-012)
- `vq-017` — 2026-05-26 (run-012)
- `vq-019` — 2026-05-26 (run-012)

## Dropped (cannot be verified, last 10)
_(none)_
