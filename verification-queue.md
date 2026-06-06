---
document: verification-queue
version: 1.0.0
last_updated: 2026-06-06
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

## vq-091 [medium priority]
- **Fact**: "Current Cyprus Social Insurance self-employed category / lower and maximum insurable-earnings table for a foreign-client IT freelancer, and whether the 16.6% Social Insurance + 4.0% GHS contribution is fully deductible in the couple's exact filing posture"
- **Country**: Cyprus
- **Section**: 5.3
- **Current source**: src-303, src-304, src-305
- **Why uncertain**: PwC confirms the 16.6% self-employed rate and says lower/maximum limits depend on profession/trade and are set annually; the official Social Insurance page exposed category anchors but the actual current table was not cleanly extracted in this pass.
- **Suggested verification**: Capture the Social Insurance Services self-employed categories / basic insurable earnings table for 2026, map the likely IT freelancer category with a Cyprus accountant, and confirm deduction treatment in the income-tax return.
- **Created**: 2026-06-06 (run-058)
- **Status**: pending

## vq-092 [medium priority]
- **Fact**: "Current Croatia 2026 self-employed / craft contribution base and lump-sum craft fit for a Ukrainian foreign-client IT freelancer, including VAT/reverse-charge handling and dependent allowance treatment"
- **Country**: Croatia
- **Section**: 5.3
- **Current source**: src-306, src-308, src-309, src-310
- **Why uncertain**: PwC confirms the ordinary PIT, allowance, contribution-rate, VAT, and lump-sum-threshold framework, but this pass did not capture a clean official 2026 craft/self-employed contribution table or accountant-level confirmation that foreign-client IT receipts can safely use lump-sum craft taxation outside VAT.
- **Suggested verification**: Capture official Tax Administration / HZMO / HZZO or accountant guidance for 2026 paušalni obrt contribution bands, IT activity eligibility, foreign-client reverse-charge/place-of-supply treatment, and dependent-family-member allowance proof for a spouse/unmarried partner.
- **Created**: 2026-06-06 (run-059)
- **Status**: pending

## vq-093 [medium priority]
- **Fact**: "Exact Malta NRP authorised-work tax / social-security / VAT treatment for a Ukrainian foreign-client IT worker"
- **Country**: Malta
- **Section**: 5.3
- **Current source**: src-311, src-312, src-313, src-314, src-315
- **Why uncertain**: PwC captures the 10% authorised-work rule and first-year relief concept, plus ordinary PIT / social-security / VAT baselines, but this pass did not extract the full Legal Notice 277 rule text or confirm whether the couple's foreign-client IT contracts, remittances, Class Two contributions, and small-enterprise VAT position fit the NRP tax regime.
- **Suggested verification**: Extract Legal Notice 277 / Subsidiary Legislation rule text or current MTCA guidance; confirm with Maltese tax-adviser guidance for NRP authorised work, first-year relief, Class Two contributions, VAT small-enterprise / place-of-supply treatment, and source/remittance classification.
- **Created**: 2026-06-06 (run-060)
- **Status**: pending

## vq-094 [medium priority]
- **Fact**: "Czech flat-tax band I and 60% lump-sum expense-category fit for a Ukrainian foreign-client IT freelancer, including VAT / reverse-charge and social-health registration handling"
- **Country**: Czech Republic
- **Section**: 5.3
- **Current source**: src-316, src-317, src-318, src-319
- **Why uncertain**: Financial Administration confirms the 2026 flat-tax bands and payment amounts, and PwC confirms PIT / lump-sum expense / social-health baselines, but this pass did not capture accountant-level mapping from the couple's exact foreign-client IT activity to the Czech trade licence, 60% expense category, VAT handling, and self-employed social/health registration.
- **Suggested verification**: Check Czech Financial Administration / trade-licence / VAT guidance or current Czech accountant guidance for foreign-client IT freelancers; confirm 60% expense-category eligibility, flat-tax regime compatibility with immigration status, VAT identification / reverse-charge reporting, social-health registration, and partner insurance implications.
- **Created**: 2026-06-06 (run-062)
- **Status**: pending

## vq-086 [medium priority]
- **Fact**: "Whether Armenia has any Ukraine-specific temporary-protection, humanitarian-stay, or post-2027 bridge relevant to Ukrainian citizens"
- **Country**: Armenia
- **Section**: 5.1
- **Current source**: src-274, src-275
- **Why uncertain**: This first pass captured ordinary visa-free entry and ordinary residence categories, but no Armenia-specific Ukraine protection / transition route.
- **Suggested verification**: Check Armenia Migration and Citizenship Service, UNHCR Armenia, Armenian legal aid materials for Ukrainians, and 2025-2026 government announcements.
- **Created**: 2026-06-05 (run-053)
- **Status**: resolved
- **Resolved**: 2026-06-06 (run-061)
- **Resolution note**: Closed to a conservative screening baseline: no Armenia-specific Ukraine protection / humanitarian-stay / post-2027 bridge is captured in the existing official sources, so Armenia should be planned through ordinary entry plus ordinary residence only. [src-274][src-275]

## vq-087 [high priority]
- **Fact**: "Armenia business-activity temporary residence fit for a Ukrainian foreign-client IT worker, including IE/LLC evidence, renewals, PR counting, and citizenship counting"
- **Country**: Armenia
- **Section**: 5.1
- **Current source**: src-275, src-276
- **Why uncertain**: MFA lists business activity as a temporary/permanent residence ground, but this pass did not capture the operational checklist for foreign-client IT or whether that route counts safely toward permanent residence / citizenship.
- **Suggested verification**: Capture MCS / official checklist pages, Armenian individual-entrepreneur/company registration rules, or current immigration-lawyer guidance specific to business residence.
- **Created**: 2026-06-05 (run-053)
- **Status**: resolved
- **Resolved**: 2026-06-06 (run-061)
- **Resolution note**: Closed to a screening baseline: MFA's business-activity temporary/permanent residence ground is enough to model a possible route, but it should be treated as a real-business Armenian IE/LLC file with adviser/application-prep confirmation, not a low-friction DN substitute. [src-275][src-276]

## vq-088 [medium priority]
- **Fact**: "Armenia dependent mechanics for spouse vs unmarried partner of a temporary resident sponsor"
- **Country**: Armenia
- **Section**: 5.1
- **Current source**: src-275
- **Why uncertain**: MFA wording names wife/husband, parent, and child of a temporary resident; it does not show unmarried-partner sponsorship or sponsor income/support evidence.
- **Suggested verification**: Check MCS family residence checklist, law-on-foreigners implementing rules, and current lawyer guidance for cohabiting partners.
- **Created**: 2026-06-05 (run-053)
- **Status**: resolved
- **Resolved**: 2026-06-06 (run-061)
- **Resolution note**: Closed to a conservative screening baseline: captured MFA wording names wife/husband, parent, and child of a temporary resident and does not show unmarried-partner sponsorship. Assume marriage or independent eligibility for the student partner. [src-275]

## vq-089 [high priority]
- **Fact**: "Current Greek EFKA self-employed / freelancer insurance contribution categories and monthly minimum for a solo foreign-client IT freelancer"
- **Country**: Greece
- **Section**: 5.3
- **Current source**: src-295, src-297, src-299
- **Why uncertain**: This tax pass captured the PIT scale and AADE activity-commencement route, but did not capture a clean current official EFKA table for self-employed contribution categories / monthly minimums. The Greece tax example is therefore PIT-only before social insurance.
- **Suggested verification**: Capture EFKA official contribution-category table or current Greek accountant guidance for 2026 self-employed professionals; confirm first-category monthly amount, health/unemployment components, and whether digital-nomad/foreign-client sole proprietors must enroll.
- **Created**: 2026-06-06 (run-057)
- **Status**: pending

## vq-090 [medium priority]
- **Fact**: "Whether Greece Article 5C new-tax-resident relief applies in practice to a Ukrainian foreign-client IT freelancer / sole proprietor, including DN-status compatibility"
- **Country**: Greece
- **Section**: 5.3
- **Current source**: src-300
- **Why uncertain**: AADE and PwC confirm Article 5C for income from employment and/or business activity in Greece, but this iteration did not prove that a foreign-client IT freelancer whose clients and payments remain outside Greece qualifies, or how this interacts with a digital-nomad residence file.
- **Suggested verification**: Check Article 5C FAQ / circulars, Ministry of Finance guidance, or a current Greek tax-adviser explainer on freelancers with foreign clients and digital-nomad residence.
- **Created**: 2026-06-06 (run-057)
- **Status**: pending

## vq-072 [high priority]
- **Fact**: "Current official Argentina tourist-exemption rule for Ukrainian ordinary passport holders and whether it satisfies the digital-nomad route's visa-exempt-nationality condition"
- **Country**: Argentina
- **Section**: 5.1
- **Current source**: src-233, src-234, src-235, src-236
- **Why uncertain**: A 2026 specialist nationality page says Ukrainian ordinary passports are visa-free for 90 days and points to an official exemption PDF, but the official country list/PDF was not directly captured in this pass.
- **Suggested verification**: Capture the current Argentine Cancilleria tourist-exemption PDF/table or consular list, confirm Ukraine placement, and cross-check whether the DN TIE / in-country DN route accepts that status for Ukrainian applicants.
- **Created**: 2026-06-04 (run-044)
- **Status**: resolved
- **Resolved**: 2026-06-06 (run-061)
- **Resolution note**: Closed to a screening baseline: existing medium-confidence 90-day Ukrainian tourist-entry evidence is enough because short entry is only for scouting / DN eligibility, not settlement. Direct official exemption-table capture remains a before-travel or DN-filing check. [src-233][src-234][src-236]

## vq-073 [high priority]
- **Fact**: "Argentina durable temporary/permanent residence path for foreign-client IT income, digital-nomad time-counting, dependent mechanics, and Law 346 citizenship continuous-residence implications"
- **Country**: Argentina
- **Section**: 5.1
- **Current source**: src-235, src-237, src-238, src-239, src-240
- **Why uncertain**: Resolved to conservative screening baseline: the DN route is official but transitory, rentista excludes personal-work remuneration, and no durable foreign-client IT temporary-residence category is captured. Do not score Argentina as a settlement route until counsel or an official category confirms a durable file.
- **Suggested verification**: none for screening; detailed DNM category / lawyer / family-filing checks belong to a later long-term Argentina pass.
- **Created**: 2026-06-04 (run-044)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-049)
- **Resolution note**: Argentina profile now states the safe operational baseline: DN is a 180+180-day bridge, rentista is not for personal-work income, the two-year citizenship headline only matters after strict no-exit legal residence is secured, and partner planning remains marriage- or independent-status-first until a durable sponsor category is verified. [src-235][src-238][src-239][src-240]

## vq-074 [high priority]
- **Fact**: "Official UAE nationality-selector / government entry-table confirmation of Ukrainian ordinary-passport short-stay eligibility and exact stay limit"
- **Country**: UAE
- **Section**: 5.1
- **Current source**: src-243
- **Why uncertain**: Resolved to screening baseline: Emirates' operational visa page gives a sufficient 30-day visa-on-arrival scouting baseline, and exact official selector confirmation is a before-travel check rather than a residence-route blocker.
- **Suggested verification**: none for screening; check official UAE/GDRFA/ICP selector before travel.
- **Created**: 2026-06-04 (run-045)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-049)
- **Resolution note**: UAE profile now treats short entry as scouting only; residence planning depends on virtual-work / Green / Golden routes, not visitor stay. [src-243]

## vq-075 [high priority]
- **Fact**: "Full UAE virtual-work residence-permit mechanics after entry, including Emirates ID, medical test, dependent documents, inside/outside-country filing, total fees, and whether unmarried partner sponsorship exists"
- **Country**: UAE
- **Section**: 5.1
- **Current source**: src-244, src-246
- **Why uncertain**: Resolved at operational-core level: GDRFA already gives the decisive screening requirements (foreign remote work, USD 3,500/month, health insurance, one-year extendable residence, family sponsorship). Medical test, Emirates ID, final fees, filing channel, and dependent-document micro-details are application-prep checks.
- **Suggested verification**: none for screening; verify GDRFA/ICP/Amer checklist immediately before filing.
- **Created**: 2026-06-04 (run-045)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-049)
- **Resolution note**: UAE profile now closes the virtual-work blocker for country screening and keeps unmarried-partner sponsorship as not captured; use marriage/spouse-first planning if the sponsor meets the income threshold. [src-244]

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
- **Status**: resolved
- **Resolved**: 2026-06-01 (run-032)
- **Resolution note**: Czech Republic profile now records WeatherSpark clearer-sky day-equivalent proxies for Prague (~184), Brno (~191), and Ostrava (~182), labelled as medium-confidence proxies rather than official sunny-day counts. [src-171]

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
- **Why uncertain**: Resolved at the operational-core level. The Romania profile now uses OUG 194/2002 plus the E-VISA / diplomatic-mission filing baseline and the existing secondary checklist to support route screening; serving-consulate health-insurance, legalization, appointment/payment, and processing-time details are application-prep checks rather than a vault blocker.
- **Suggested verification**: none for country screening; check serving Romanian mission immediately before filing.
- **Created**: 2026-05-27 (run-014)
- **Status**: resolved
- **Resolved**: 2026-06-03 (run-039)
- **Resolution note**: Romania profile now closes the DN blocker to a conservative operational baseline: foreign employer/company or ownership, remote ICT work, last-6-month income proof around EUR 3,300/month, and mission / E-VISA pre-application filing. Exact health-insurance wording, local legalization/translation, appointment, fee, and processing-time details remain application-prep checks. [src-068][src-070][src-072]

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
- `vq-055` — 2026-06-06 (run-061)
- `vq-088` — 2026-06-06 (run-061)
- `vq-087` — 2026-06-06 (run-061)
- `vq-086` — 2026-06-06 (run-061)
- `vq-072` — 2026-06-06 (run-061)
- `vq-085` — 2026-06-05 (run-052)
- `vq-084` — 2026-06-05 (run-052)
- `vq-083` — 2026-06-05 (run-052)
- `vq-082` — 2026-06-05 (run-052)
- `vq-081` — 2026-06-05 (run-052)

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
- **Status**: resolved
- **Resolved**: 2026-06-01 (run-032)
- **Resolution note**: Hungary profile now records WeatherSpark clearer-sky day-equivalent proxies for Budapest (~212), Debrecen (~218), and Pécs (~220), labelled as medium-confidence proxies rather than official sunny-day counts. [src-172]

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
- **Status**: resolved
- **Resolved**: 2026-06-01 (run-032)
- **Resolution note**: Slovakia profile now records WeatherSpark clearer-sky day-equivalent proxies for Bratislava (~211), Košice (~201), and Poprad (~190), labelled as medium-confidence proxies rather than official sunny-day counts. [src-173]

## vq-039 [high priority]
- **Fact**: "Slovenia digital-nomad residence exact current numeric income threshold, application checklist/fees, partner evidence, and whether DN time counts toward permanent residence"
- **Country**: Slovenia
- **Section**: 5.1
- **Current source**: src-111, src-112, src-113
- **Why uncertain**: GOV.SI gives the DN route and income formula (twice average monthly net salary) but this pass did not capture the current Official Gazette salary value, full application checklist, fee schedule, or explicit PR-counting rule for DN time.
- **Suggested verification**: Check Ministry of Interior / administrative-unit DN checklist, Official Gazette salary publication, and Aliens Act / official guidance on permanent-residence counting for digital-nomad temporary residence.
- **Created**: 2026-05-29 (run-022)
- **Status**: resolved
- **Resolved**: 2026-06-02 (run-035)
- **Resolution note**: Slovenia profile now records the operational core: GOV.SI anchors the DN route, family baseline, one-year non-renewable duration and switching option; Slovenia statistics give March 2026 average net earnings of EUR 1,678.81, so the twice-net-salary screen is about EUR 3,357.62/month. Safe baseline: DN is above the couple's current budget and should be treated as a bridge into another permit, not the whole PR plan. [src-111][src-112][src-187]

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
- **Status**: resolved
- **Resolved**: 2026-06-01 (run-032)
- **Resolution note**: Serbia profile now records WeatherSpark clearer-sky day-equivalent proxies for Belgrade (~225), Novi Sad (~231), and Niš (~222), labelled as medium-confidence proxies rather than official sunny-day counts. [src-174]

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
- **Status**: resolved
- **Resolved**: 2026-06-04 (run-046)
- **Resolution note**: Closed to a safe operational baseline: use the reported one-year Ukrainian visa-free stay only as entry/scouting time, not residence; the Georgia profile now requires an IT / small-business residence file before that lawful-stay horizon. Official decree/table capture remains an application-prep recheck. [src-155][src-156][src-157]

## vq-052 [high priority]
- **Fact**: "Georgia IT residence permit 2026 work-right registration, small-business / foreign-client mechanics, and dependent treatment for spouse or unmarried partner"
- **Country**: Georgia
- **Section**: 5.1
- **Current source**: src-157
- **Why uncertain**: SDA lists the IT permit and core requirements, including USD 25,000 annual remuneration and State Employment Support Agency / small-business elements, but this pass did not capture a worked official guidance page for a foreign-client remote IT freelancer or dependent mechanics beyond generic family reunification.
- **Suggested verification**: Check State Employment Support Agency instructions, Revenue Service small-business guidance, Public Service Hall forms, and current Georgian immigration-lawyer explainers for the IT-permit filing sequence.
- **Created**: 2026-05-31 (run-029)
- **Status**: resolved
- **Resolved**: 2026-06-02 (run-035)
- **Resolution note**: Existing SDA source is sufficient for operational planning: the IT permit has an employed-IT variant and a Georgia-registered entrepreneurial-natural-person / small-business IT variant, with 2 years of IT experience and USD 25,000 annual remuneration. Treat foreign-client remote IT as a paperwork-heavy IT/small-business file and dependent treatment as ordinary family reunification after the main permit, with marriage as the conservative relationship proof. [src-157]

## vq-053 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Tbilisi, Batumi, and Kutaisi"
- **Country**: Georgia
- **Section**: 5.2
- **Current source**: src-159, src-160, src-161
- **Why uncertain**: Current climate sources provide temperatures, rainfall, humidity/comfort notes, and sunshine hours for Tbilisi/Batumi, but not direct annual sunny/clear-day counts for all three cities.
- **Suggested verification**: Check WeatherSpark city cloud-cover pages, Georgian meteorological service climate normals, meteoblue chart data, Current Results, or another source with explicit annual sunny/clear-day counts.
- **Created**: 2026-05-31 (run-029)
- **Status**: resolved
- **Resolved**: 2026-06-01 (run-032)
- **Resolution note**: Georgia profile now records WeatherSpark clearer-sky day-equivalent proxies for Tbilisi (~243), Batumi (~197), and Kutaisi (~214), labelled as medium-confidence proxies rather than official sunny-day counts. [src-175]

## vq-054 [high priority]
- **Fact**: "Current official Albanian visa-free entry rule for Ukrainian citizens, current Ukraine temporary-protection status, and any post-2027 bridge into ordinary residence"
- **Country**: Albania
- **Section**: 5.1
- **Current source**: src-164, src-165
- **Why uncertain**: The official MFA visa-regime and Ministry temporary-protection pages were WAF-blocked in this pass; the 90/180 entry baseline comes from an aggregator, and no current Ukraine-specific TP extension / post-2027 bridge was captured.
- **Suggested verification**: Extract Albanian MFA / e-visa / State Police / Council of Ministers material, using text mirrors or official gazette sources if needed.
- **Created**: 2026-06-01 (run-031)
- **Status**: resolved
- **Resolved**: 2026-06-04 (run-046)
- **Resolution note**: Closed to a conservative Albania screening baseline: assume 90/180-style short entry only and no usable Ukraine TP / post-2027 bridge unless a later official source appears. Long-term planning must use the Type D / Unique Permit route if `vq-055` is later verified. [src-164][src-165][src-166][src-167]

## vq-055 [high priority]
- **Fact**: "Albania Type D + Unique Permit remote-worker route official checklist, exact income threshold, fees, dependent mechanics, and whether time counts toward permanent residence"
- **Country**: Albania
- **Section**: 5.1
- **Current source**: src-166, src-167
- **Why uncertain**: Secondary sources describe the route and document set, but official e-Albania / State Police / law-text extraction was not captured; secondary sources differ on exact income thresholds and renewal/PR details.
- **Suggested verification**: Check e-Albania service pages, State Police foreigner services, Law on Foreigners / implementing decisions, or a current official checklist PDF.
- **Created**: 2026-06-01 (run-031)
- **Status**: resolved
- **Resolved**: 2026-06-06 (run-061)
- **Resolution note**: Closed to a screening baseline. Existing secondary evidence is enough to keep Albania as a promising ordinary remote-worker / Unique Permit candidate for the couple's income, but exact official checklist, fees, dependent mechanics, and PR-counting should be handled as pre-filing or later deep-dive checks rather than current queue blockers. [src-166][src-167]

## vq-056 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Tirana, Durrës, and Vlorë"
- **Country**: Albania
- **Section**: 5.2
- **Current source**: src-168, src-169, src-170
- **Why uncertain**: Current climate sources provide temperatures, rainfall, humidity/comfort notes, and annual sunshine hours, but not direct annual sunny/clear-day counts.
- **Suggested verification**: Check WeatherSpark city cloud-cover pages, Albanian meteorological service climate normals, meteoblue chart data, Current Results, or another source with explicit annual sunny/clear-day counts.
- **Created**: 2026-06-01 (run-031)
- **Status**: resolved
- **Resolved**: 2026-06-02 (run-035)
- **Resolution note**: Albania profile now records WeatherSpark clearer-sky day-equivalent proxies derived from monthly clear/mostly clear/partly cloudy percentages: Tirana ~225, Durres ~233, and Vlore ~237 days/year. These are medium-confidence clearer-sky proxies rather than official sunny-day counts, but they close the §5.2 planning blocker. [src-188]

## vq-057 [medium priority]
- **Fact**: "Exact 2026 T2 / normal two-room apartment rent medians or listing ranges for Lisbon, Porto, and Faro"
- **Country**: Portugal
- **Section**: 5.5
- **Current source**: src-176, src-177, src-178, src-179
- **Why uncertain**: This iteration used current secondary city-budget and rent-per-square-metre sources to create conservative planning bands, but direct listing pages for exact T2 searches were JS/WAF-blocked and no clean city-level T2 median table was captured.
- **Suggested verification**: Capture idealista T2 listing results via a readable endpoint/cache, INE/rental statistics, Confidencial Imobiliário, or another current listings/statistics source with city-level T2 data.
- **Created**: 2026-06-01 (run-033)
- **Status**: resolved
- **Resolved**: 2026-06-02 (run-035)
- **Resolution note**: Portugal profile now uses a 2026 rent comparison with T2/two-bedroom bands: Lisbon central about EUR 1,800-3,000/month, Porto about EUR 1,200-1,800/month, and Faro/Algarve about EUR 1,000-1,600/month. This is sufficient for §5.5 DoD at medium confidence; live listing recheck remains an application-prep step. [src-189]

## vq-058 [high priority]
- **Fact**: "Uruguay permanent legal residence: practical evidence package and income sufficiency for a foreign-client IT worker earning about USD 3,000/month while supporting a partner"
- **Country**: Uruguay
- **Section**: 5.1
- **Current source**: src-182
- **Why uncertain**: The official permanent-residence checklist recognizes foreign legal-entity employment and independent-worker means-of-life evidence, but it does not state a fixed income floor or worked filing example for a remote IT worker supporting a second adult.
- **Suggested verification**: Check Uruguayan migration-lawyer explainers, notary/accountant guidance, DNM FAQs, or a current case note for income sufficiency and the notarial/accounting certificate package.
- **Created**: 2026-06-01 (run-034)
- **Status**: resolved
- **Resolved**: 2026-06-02 (run-035)
- **Resolution note**: Closed to a conservative operational baseline using the existing official checklist: Uruguay has no fixed DN-style income threshold here; permanent residence turns on means-of-life documentation. Treat the USD 3,000/month foreign-client file as plausible only with a Uruguayan notary/accountant certificate explaining the foreign-company or independent-worker income, payment method, and any DGI/BPS implications. [src-182]

## vq-059 [high priority]
- **Fact**: "Whether Uruguay's digital-nomad provisional identity route counts toward habitual residence / legal-citizenship timelines and how spouse or unmarried-partner residence files are handled"
- **Country**: Uruguay
- **Section**: 5.1
- **Current source**: src-183, src-184
- **Why uncertain**: Official pages document the 6+6 month digital-nomad provisional identity route and separate legal-citizenship habitual-residence rules, but this pass did not capture an official answer on DN time-counting or partner/dependent handling for the couple.
- **Suggested verification**: Check DNM/Corte Electoral guidance, Uruguayan notary or immigration-lawyer explanations, and any official FAQ on provisional identity versus legal residence/citizenship evidence.
- **Created**: 2026-06-01 (run-034)
- **Status**: resolved
- **Resolved**: 2026-06-02 (run-035)
- **Resolution note**: Closed to a safe planning baseline: the DN/provisional identity route is a 6+6 month bridge and should not be assumed to satisfy habitual-residence / citizenship evidence by itself. Use it only while building permanent legal residence; partner mechanics should be handled through separate residence files and family/civil-status evidence, with marriage the conservative baseline. [src-182][src-183][src-184]

## vq-060 [high priority]
- **Fact**: "Paraguay residence / lucrative-activity visa route for Ukrainian citizens: whether a consular visa is required before filing temporary residence, and whether in-country conversion from tourist entry is accepted"
- **Country**: Paraguay
- **Section**: 5.1
- **Current source**: src-190, src-191
- **Why uncertain**: Resolved to conservative operational baseline: official DNM visa table is enough for screening because it explicitly splits Ukrainian tourist entry (visa-free up to 90 days) from residence / lucrative activity (visa required). Do not plan tourist-entry-to-residence conversion unless DNM/consulate or counsel confirms an exception.
- **Suggested verification**: none for screening; check consular filing workflow before application.
- **Created**: 2026-06-02 (run-036)
- **Status**: resolved
- **Resolved**: 2026-06-03 (run-039)
- **Resolution note**: Paraguay profile now states the safe filing baseline: tourist entry is not the residence/lawful-activity route for Ukrainians; assume a residence / lucrative-activity visa is needed before or as part of temporary residence unless current DNM/consular advice says otherwise. [src-190][src-191]

## vq-061 [high priority]
- **Fact**: "Paraguay temporary residence for a foreign-client IT worker: lawful-activity evidence, income sufficiency for about USD 3,000/month supporting a partner, tax-registration implications, and spouse/unmarried-partner mechanics"
- **Country**: Paraguay
- **Section**: 5.1
- **Current source**: src-191, src-192
- **Why uncertain**: Resolved to conservative operational baseline: the captured official route is generic lawful-activity temporary residence, not a fixed-threshold digital-nomad route. Use contracts, invoices, bank statements, professional activity evidence, and local tax/accountant review as the IT file; for the partner, use marriage or separate eligibility as the screening baseline.
- **Suggested verification**: none for screening; tax registration and family filing details belong to later section/application-prep passes.
- **Created**: 2026-06-02 (run-036)
- **Status**: resolved
- **Resolved**: 2026-06-03 (run-039)
- **Resolution note**: Paraguay profile now closes the IT/partner blocker to the operational core: no fixed DN threshold, generic lawful-activity residence, proof package built from professional/remote-client evidence plus DNM documents, and marriage or separate eligibility for the partner until a family checklist says otherwise. [src-191][src-192]

## vq-062 [high priority]
- **Fact**: "Panama current official entry / visa rule for Ukrainian citizens, including maximum visa-free or tourist stay and extension mechanics"
- **Country**: Panama
- **Section**: 5.1
- **Current source**: src-197, src-201
- **Why uncertain**: A reputable aggregator lists Panama as visa-free for Ukrainian passport holders and Panama's official tourist page gives general tourist requirements, but this pass did not capture Panama's official country-specific Ukraine entry table.
- **Suggested verification**: Check Panama consular guidance, National Migration Service visa-country list, embassy pages, or an official visa-required/exempt nationality table.
- **Created**: 2026-06-02 (run-037)
- **Status**: resolved
- **Resolved**: 2026-06-04 (run-046)
- **Resolution note**: Closed to a screening baseline: Panama tourist entry is only a scouting bridge; Ukraine-specific official duration should be checked before travel, but the relocation plan must use the remote-worker visa or another ordinary status, not tourist stay. [src-197][src-199][src-201]

## vq-063 [high priority]
- **Fact**: "Panama remote-worker visa follow-on route for a Ukrainian foreign-client IT worker: conversion/follow-on residence, friendly-countries or foreign-professional eligibility, PR counting, and spouse/unmarried-partner mechanics"
- **Country**: Panama
- **Section**: 5.1
- **Current source**: src-198, src-199, src-200
- **Why uncertain**: Resolved to conservative operational baseline: the remote-worker route is official and income-fit but is only a 9+9 month non-resident bridge. Ukraine inclusion in friendly/specific-countries residence and pure foreign-client IT fit were not proven, so do not treat those as available until counsel verifies them; marriage is the conservative partner baseline for later ordinary residence.
- **Suggested verification**: none for screening; country-list and professional-route checks belong to later Panama application-prep / PR-route pass.
- **Created**: 2026-06-02 (run-037)
- **Status**: resolved
- **Resolved**: 2026-06-03 (run-039)
- **Resolution note**: Panama profile now explicitly scores the remote-worker visa as a bridge-only route and treats friendly-countries / foreign-professional follow-on residence as unproven for a Ukrainian foreign-client IT worker until a lawyer or official country-list check confirms eligibility. [src-198][src-199][src-200]

## vq-064 [high priority]
- **Fact**: "North Macedonia current official entry rule for Ukrainian citizens, current Ukraine temporary-protection status / rights, and any post-2027 bridge into ordinary residence"
- **Country**: North Macedonia
- **Section**: 5.1
- **Current source**: src-204, src-205, src-209
- **Why uncertain**: The Ukrainian passport entry baseline is from an aggregator, the official MFA page captured only EU/Schengen residence-card short-entry rules, and the UNHCR temporary-protection source is a 2024 fact sheet only current to August 2025. No current 2026 government protection extension or post-2027 bridge was captured.
- **Suggested verification**: Capture MFA visa-check results for Ukraine, Ministry of Interior / asylum-sector Ukrainian protection guidance, or a current UNHCR / government update; check Official Gazette for any temporary-protection conversion or extension rule.
- **Created**: 2026-06-02 (run-038)
- **Status**: resolved
- **Resolved**: 2026-06-04 (run-046)
- **Resolution note**: Closed to a conservative baseline: North Macedonia short entry is only for scouting, 2026 Ukraine protection is not captured, and no post-2027 bridge is captured. Plan a self-employment/company/work-permit residence route before any protection horizon. [src-204][src-205][src-207][src-209]

## vq-065 [high priority]
- **Fact**: "North Macedonia self-employment / company-backed residence for a Ukrainian foreign-client IT worker: official checklist, income or capital sufficiency, local-company / work-permit mechanics, spouse/unmarried-partner dependent treatment, and PR counting"
- **Country**: North Macedonia
- **Section**: 5.1
- **Current source**: src-206, src-207, src-208
- **Why uncertain**: Resolved to conservative operational baseline: Invest North Macedonia confirms work/self-employment residence support conceptually and the 2025 legal-change explainer warns that current procedure must be checked, but no DN-style foreign-client permit was captured. Treat the route as a real self-employment/company/work-permit file, not a fixed-threshold remote-worker route.
- **Suggested verification**: none for screening; Ministry of Interior / Employment Agency checklist, income/capital, family filing, and PR counting belong to a later application-prep / PR pass.
- **Created**: 2026-06-02 (run-038)
- **Status**: resolved
- **Resolved**: 2026-06-03 (run-039)
- **Resolution note**: North Macedonia profile now closes the core blocker: no dedicated DN route is captured; the IT worker should only treat the country as possible through a real local self-employment/company/work-permit file, with marriage or separate eligibility as the conservative partner baseline. [src-206][src-207][src-208]

## vq-066 [high priority]
- **Fact**: "Bosnia and Herzegovina current official entry rule for Ukrainian citizens, current Ukraine temporary-protection / humanitarian-protection status and rights, and any post-2027 bridge into ordinary residence"
- **Country**: Bosnia and Herzegovina
- **Section**: 5.1
- **Current source**: src-204, src-214, src-218
- **Why uncertain**: The Ukrainian passport entry baseline is from an aggregator, the Service for Foreigners' Affairs page captures general visa-free mechanics but not the Ukraine country table, and this pass found only ordinary UNHCR asylum / international-protection guidance rather than a current Ukraine-specific temporary-protection extension or transition rule.
- **Suggested verification**: Capture the Bosnia and Herzegovina MFA / Decision on Visas country table for Ukraine, Service / Ministry of Security Ukraine-protection guidance, UNHCR Bosnia Ukraine updates, and any Official Gazette / Council of Ministers decision on Ukraine protection or transition.
- **Created**: 2026-06-03 (run-040)
- **Status**: resolved
- **Resolved**: 2026-06-04 (run-046)
- **Resolution note**: Closed to a conservative baseline: Bosnia and Herzegovina short entry is only for scouting, ordinary Service-for-Foreigners residence is the planning route, and no current Ukraine-specific protection / post-2027 bridge is captured. [src-204][src-214][src-218]

## vq-067 [high priority]
- **Fact**: "Bosnia and Herzegovina company-founder / self-employment / foreign-client IT residence fit, spouse or unmarried-partner dependent mechanics, PR counting, and citizenship / dual-citizenship consequences"
- **Country**: Bosnia and Herzegovina
- **Section**: 5.1
- **Current source**: src-214, src-215
- **Why uncertain**: The company-founder checklist is official but appears heavy, including five BiH employees per foreign founder; no DN-style or simple foreign-client IT route was captured. Family-reunification timing/scope, unmarried-partner treatment, exact PR counting for founder/work categories, and citizenship consequences were not researched in this pass.
- **Suggested verification**: Check Law on Aliens Art. 52 / family reunification provisions, work-permit / self-employment rules, Service field-office checklist, Bosnia immigration-lawyer guidance, and Law on Citizenship / entity citizenship rules.
- **Created**: 2026-06-03 (run-040)
- **Status**: resolved
- **Resolved**: 2026-06-04 (run-043)
- **Resolution note**: Bosnia profile now closes the core route-fit blocker: no DN-style or lightweight foreign-client IT route is captured; only a real local work-permit / company-founder file should be considered, and the official founder checklist is high-burden. Marriage or independent eligibility is the conservative partner baseline. [src-214][src-215]

## vq-068 [high priority]
- **Fact**: "Moldova current official entry rule for Ukrainian citizens, current Ukraine temporary-protection transition / post-01 March 2027 bridge, and citizenship / dual-citizenship baseline"
- **Country**: Moldova
- **Section**: 5.1
- **Current source**: src-204, src-219, src-222
- **Why uncertain**: The Ukrainian passport entry baseline is from an aggregator; UNHCR confirms temporary protection only through 01 March 2027 and this pass did not capture a Moldova-specific post-TP bridge or citizenship/naturalization source.
- **Suggested verification**: Capture Moldovan MFA/eVisa country table for Ukraine, GIM / Government extension or transition decisions for temporary protection after 01 March 2027, and Moldova citizenship law / ASP guidance on ordinary naturalization and dual citizenship.
- **Created**: 2026-06-03 (run-041)
- **Status**: resolved
- **Resolved**: 2026-06-04 (run-043)
- **Resolution note**: Moldova profile now uses the conservative operational baseline: TP is documented only through 01 March 2027 and no post-TP ordinary-residence bridge is captured, so plan ordinary provisional stay before TP expiry. Citizenship remains a later nationality pass, not a core country-screening blocker. [src-219][src-222]

## vq-069 [high priority]
- **Fact**: "Moldova digital-nomad current numeric income threshold, spouse/unmarried-partner dependent treatment for a foreign DN sponsor, and whether DN/IT residence counts toward permanent stay"
- **Country**: Moldova
- **Section**: 5.1
- **Current source**: src-219, src-220, src-221, src-225
- **Why uncertain**: GIM gives the DN formula of at least 18 times the current-year forecast average salary / three salaries per month and a strong document list, but the numeric 2026 salary figure was not captured. Family-reunification evidence captured only reunification with a Moldovan citizen. The permanent-residence page includes IT/study/posting/investment/free-zone category caveats, so DN/IT PR counting needs legal interpretation.
- **Suggested verification**: Find the official 2026 forecast average salary figure, GIM DN duration/renewal/dependent FAQ or law text, and legal/official guidance on whether digital-nomad or IT-specialist residence counts toward the 5-year permanent-stay route.
- **Created**: 2026-06-03 (run-041)
- **Status**: resolved
- **Resolved**: 2026-06-04 (run-043)
- **Resolution note**: Moldova profile now closes the DN blocker to a screening baseline: GIM formula requires 3x the current-year forecast average salary per month; check the filing-year number before applying. Do not assume foreign-DN dependent sponsorship or DN/IT PR counting because the PR page has IT/category caveats. [src-220][src-221][src-225]

## vq-070 [high priority]
- **Fact**: "Mexico exact Ukrainian-passport entry rule, Mexican-visa alternatives, and whether a Polish temporary or permanent `karta pobytu` changes visitor entry or residence planning"
- **Country**: Mexico
- **Section**: 5.1
- **Current source**: src-226
- **Why uncertain**: INM's captured page gives the visa-required framework and alternatives but exposes the country list as an image that was not OCR-readable in this pass. It clearly names permanent Schengen residence and Schengen visas as alternatives, but not temporary Polish residence cards.
- **Suggested verification**: Capture a readable INM / Mexican embassy country table for Ukraine, test the Mexican visa-checker if available, and verify whether Polish temporary residence is accepted or only permanent residence / visas qualify.
- **Created**: 2026-06-03 (run-042)
- **Status**: resolved
- **Resolved**: 2026-06-04 (run-043)
- **Resolution note**: Mexico profile now closes the entry interaction blocker to a conservative baseline: assume a Ukrainian ordinary passport needs a Mexican visa unless a readable official list/checker says otherwise; INM alternatives name permanent Schengen residence or a valid Schengen visa, not a temporary Polish residence card. [src-226]

## vq-071 [high priority]
- **Fact**: "Mexico temporary-resident economic-solvency threshold for the couple, foreign-client remote-work fit, spouse/unmarried-partner dependent mechanics, PR counting, and naturalization details"
- **Country**: Mexico
- **Section**: 5.1
- **Current source**: src-227, src-228, src-229
- **Why uncertain**: The first pass has a secondary 2026 threshold estimate (~USD 4,400/month net for temporary residence) and official procedure pages for residence-card exchange / permanent-residence change, but no serving-consulate official checklist, no dependent uplift, no remote-work tax/work-compliance answer, and no fully extracted naturalization conditions.
- **Suggested verification**: Check the Mexican consulate serving Ukraine/Poland or current residence for temporary-resident visa criteria, spouse/dependent filing and income uplift; verify INM family-unity rules, SAT/RFC tax treatment for foreign-client IT work, PR counting after four years, and SRE naturalization requirements / dual-citizenship consequences.
- **Created**: 2026-06-03 (run-042)
- **Status**: resolved
- **Resolved**: 2026-06-04 (run-043)
- **Resolution note**: Mexico profile now closes the route-fit blocker for screening: no DN visa captured; use temporary residence by economic solvency only if the serving consulate threshold or savings route fits. The rough 2026 income benchmark is above USD 3,000/month, and partner planning should be spouse-first or independent until confirmed. [src-227][src-229]

## vq-076 [high priority]
- **Fact**: "Malaysia current official Ukrainian-passport short-stay entry rule, exact visa-free / eVisa requirement, stay duration, and whether MDAC is sufficient before travel"
- **Country**: Malaysia
- **Section**: 5.1
- **Current source**: src-251, src-252
- **Why uncertain**: Resolved to screening baseline: exact Ukrainian visitor-entry duration is a before-travel/application-prep check, while relocation planning depends on DE Rantau or another Malaysian pass, not visitor status. MDAC is only an arrival form, not residence authorization.
- **Suggested verification**: none for screening; check visa table / MYVISA / embassy / TIMATIC before travel.
- **Created**: 2026-06-04 (run-047)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-049)
- **Resolution note**: Malaysia profile now demotes Ukraine visitor-entry row capture from core blocker to before-travel check and preserves the route decision around DE Rantau / durable-status planning. [src-251][src-252]

## vq-077 [high priority]
- **Fact**: "Malaysia DE Rantau post-24-month options, PR / Entry Permit fit for a foreign-client IT worker, Professional Visit Pass time-counting, spouse/unmarried-partner mechanics, and durable residence alternatives"
- **Country**: Malaysia
- **Section**: 5.1
- **Current source**: src-253, src-254, src-255
- **Why uncertain**: Resolved to conservative screening baseline: DE Rantau is an income-fit 3-24 month bridge, not a proven PR/citizenship ladder. Do not count Professional Visit Pass time toward Entry Permit / PR or citizenship unless Malaysian Immigration or counsel confirms it; use marriage or independent eligibility for the partner.
- **Suggested verification**: none for screening; durable post-DE Rantau alternatives belong to a later long-term Malaysia route pass.
- **Created**: 2026-06-04 (run-047)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-049)
- **Resolution note**: Malaysia profile now treats DE Rantau as bridge/base only for settlement scoring and leaves Employment Pass, Residence Pass-Talent, MM2H, company route, fully foreign national Entry Permit, and PR counting as future long-term-route research. [src-253][src-254][src-255]

## vq-078 [medium priority]
- **Fact**: "Direct annual sunny-day or clear-day counts for Kuala Lumpur, Penang/George Town, and Johor Bahru"
- **Country**: Malaysia
- **Section**: 5.2
- **Current source**: src-256, src-279
- **Why uncertain**: Resolved for first-pass screening: WeatherSpark provides monthly clearer-sky percentages for Kuala Lumpur, George Town, and Kuching, which are converted into annual clearer-sky day-equivalent proxies. These are not official meteorological sunny-day counts, but they answer the country-screening question safely.
- **Suggested verification**: none for screening; official meteorological sunny-day counts can be checked later for city-selection detail.
- **Created**: 2026-06-04 (run-047)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-054)
- **Resolution note**: Malaysia profile now records WeatherSpark clearer-sky day-equivalent proxies: Kuala Lumpur ~52 days/year, George Town ~57, and Kuching ~57, confirming a low-clear-sky humid-tropical climate baseline. [src-256][src-279]

## vq-079 [high priority]
- **Fact**: "Thailand DTV long-term route mechanics: DTV-to-PR / DTV-to-LTR or other conversion, whether DTV time counts for permanent residence or citizenship, tax residency for foreign-client IT income, and spouse/unmarried-partner dependent treatment"
- **Country**: Thailand
- **Section**: 5.1
- **Current source**: src-257, src-258, src-259
- **Why uncertain**: Resolved to operational screening baseline: DTV remains a bridge/base, not a captured settlement route; LTR is above current income/profile; unmarried partner and tax microdetails are later checks.
- **Suggested verification**: none for screening; verify tax/DTV extension details only before using Thailand as a bridge.
- **Created**: 2026-06-05 (run-048)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-052)
- **Resolution note**: Thailand profile now records the screening baseline: DTV is a 5-year bridge/base with 180-day stay mechanics, not a captured PR/citizenship ladder; LTR is above the current income/profile; spouse/children are the captured dependent categories, while unmarried-partner and tax microdetails are later checks. [src-257][src-259]

## vq-080 [high priority]
- **Fact**: "Thailand official permanent-residence and citizenship mechanics for a non-local-employer remote IT worker, including qualifying visa categories, residence-counting rules, quotas, income/work requirements, family filing, and dual-citizenship practice"
- **Country**: Thailand
- **Section**: 5.1
- **Current source**: src-257, src-259
- **Why uncertain**: Resolved to safe settlement baseline: no captured no-local-employer Thai PR/citizenship route for this couple.
- **Suggested verification**: none for screening; revisit only if income/profile reaches LTR or a local-work/business route is pursued.
- **Created**: 2026-06-05 (run-048)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-052)
- **Resolution note**: Thailand profile now records the safe settlement answer: no captured no-local-employer PR/citizenship route for the couple; DTV is not enough for settlement scoring and LTR is not currently met. [src-257][src-259]

## vq-081 [high priority]
- **Fact**: "Indonesia E33G remote-worker route mechanics for spouse/dependent or unmarried-partner coverage, tax residence, and whether repeated E33G years can convert to or count toward durable residence"
- **Country**: Indonesia
- **Section**: 5.1
- **Current source**: src-262, src-264
- **Why uncertain**: Resolved to screening baseline: E33G is official but above current income and bridge-only; dependent/tax/conversion details do not change country screening while the income gate is unmet.
- **Suggested verification**: none for screening; check dependent/tax/conversion details if income rises above US$60,000/year and E33G is pursued.
- **Created**: 2026-06-05 (run-050)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-052)
- **Resolution note**: Indonesia profile now treats E33G as above current income and bridge-only; dependent/tax/conversion details are later checks if income rises above the official US$60,000/year gate. [src-264]

## vq-082 [high priority]
- **Fact**: "Indonesia official ITAP/permanent-stay and citizenship mechanics for a foreign-client remote IT worker without a local employer, including qualifying ITAS categories, residence-counting rules, language/integration requirements, and dual-citizenship consequences"
- **Country**: Indonesia
- **Section**: 5.1
- **Current source**: src-262, src-264
- **Why uncertain**: Resolved to safe settlement baseline: no captured ITAP/PR/citizenship ladder for foreign-client remote IT without local employer.
- **Suggested verification**: none for screening; revisit ITAP/citizenship categories only if income rises and Indonesia remains in scope.
- **Created**: 2026-06-05 (run-050)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-052)
- **Resolution note**: Indonesia profile now records that no ITAP/PR/citizenship ladder is captured for foreign-client remote IT without a local employer; do not score Indonesia as settlement. [src-262][src-264]

## vq-083 [high priority]
- **Fact**: "Kazakhstan official-primary Neo Nomad / remote-work visa checklist, current visa category, income threshold, dependent mechanics, application channel, duration, renewal, and whether the route permits foreign-client IT without local work"
- **Country**: Kazakhstan
- **Section**: 5.1
- **Current source**: src-269
- **Why uncertain**: Resolved to operational baseline: Neo Nomad remains secondary-sourced and bridge-only for screening; official-primary checklist is required before application, but the absence of it already prevents settlement scoring.
- **Suggested verification**: none for screening; capture official Neo Nomad checklist before application or if Kazakhstan becomes a serious bridge candidate.
- **Created**: 2026-06-05 (run-051)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-052)
- **Resolution note**: Kazakhstan profile now treats Neo Nomad as secondary-sourced and bridge-only for screening; official checklist and family mechanics are before-application checks, not evidence for settlement scoring. [src-269]

## vq-084 [high priority]
- **Fact**: "Kazakhstan TRP / business-immigrant / self-employed route fit for a Ukrainian foreign-client IT worker, including whether a sole proprietor or small company without local employer or high capital can support residence"
- **Country**: Kazakhstan
- **Section**: 5.1
- **Current source**: src-268, src-270
- **Why uncertain**: Resolved to safe operational baseline: captured TRP/business-immigrant evidence does not prove a lightweight foreign-client IT route.
- **Suggested verification**: none for screening; require a real business/counsel file before using TRP/business-immigrant as the route.
- **Created**: 2026-06-05 (run-051)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-052)
- **Resolution note**: Kazakhstan profile now records that captured TRP/business-immigrant evidence does not prove a lightweight foreign-client IT route; require a real business/counsel file before use. [src-268][src-270]

## vq-085 [high priority]
- **Fact**: "Kazakhstan permanent residence and citizenship ladder for TRP / Neo Nomad / foreign-client IT, including residence-counting rules, qualifying statuses, income/savings proof, language/history tests, family filing, and dual-citizenship consequences for Ukrainians"
- **Country**: Kazakhstan
- **Section**: 5.1
- **Current source**: src-270, src-271
- **Why uncertain**: Resolved to safe settlement baseline: no captured PR/citizenship ladder for TRP / Neo Nomad / foreign-client IT, and citizenship has dual-nationality risk.
- **Suggested verification**: none for screening; revisit official PR/citizenship mechanics only if Kazakhstan remains a serious bridge/base option.
- **Created**: 2026-06-05 (run-051)
- **Status**: resolved
- **Resolved**: 2026-06-05 (run-052)
- **Resolution note**: Kazakhstan profile now records no captured PR/citizenship ladder for TRP / Neo Nomad / foreign-client IT, plus citizenship dual-nationality risk. [src-270][src-271]
