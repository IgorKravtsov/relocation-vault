---
country: Mexico
tier: null
depth_score: 2.0
last_updated: 2026-06-11T00:04:17Z
sections_completed: ["5.2"]
sections_partial: ["5.1", "5.3"]
sections_pending: ["5.4","5.5","5.6","5.7","5.8","5.9","5.10","5.11"]
risk_flags: ["ukrainian-entry-visa-likely-required", "temporary-residence-income-above-current-budget", "no-dedicated-digital-nomad-visa", "coastal-heat-humidity", "mexico-resico-eligibility-gap", "mexico-vat-export-service-gap", "mexico-social-security-category-gap"]
sources_used: ["src-226", "src-227", "src-228", "src-229", "src-230", "src-231", "src-232", "src-449", "src-450", "src-451", "src-452", "src-453", "src-454", "src-455"]
unverified_count: 0
schema_version: 2.0.0
---

# Mexico

## Block 1 - Summary

- **Tier**: TBD. First pass suggests Mexico is a possible ordinary-residence fallback rather than a clean digital-nomad route: temporary residence can lead to permanent residence after four years, but 2026 economic-solvency thresholds appear above the couple's current ~$3,000/month income if they apply through the standard income route. [src-227][src-229]
- **depth_score**: 2.0
- **Last updated**: 2026-06-11T00:04:17Z
- **Tier rationale**: keep as Tier-3 hint until the exact serving-consulate threshold, entry mechanics for Ukrainian passports, taxes, rent, healthcare, and partner sponsorship are checked.

## Block 2 - Scoring

| Criterion | Score (1-10) | Confidence | Brief rationale | Profile section |
|---|---:|---|---|---|
| Legalization (now + post-03.2027) | — | medium | No EU TP dependency; ordinary temporary-residence ladder exists, but the standard solvency route appears above the couple's income and no dedicated DN visa was captured. | §5.1 |
| Climate | — | medium | Huge regional spread: Mexico City is mild and dry-comfortable, while Caribbean / Pacific coasts are warm but humid and rainy in season. | §5.2 |
| Taxes | — | medium | Progressive PIT is workable but not low-tax at USD 3,000/month: ordinary resident PIT-only net screens near USD 2,447/month before accountant, VAT, and any social-security/IMSS obligations. RESICO or export-service VAT treatment could improve the answer, but eligibility was not proven in this pass. | §5.3 |
| Cost of living | — | N/A | [verification required] | §5.4 |
| Rent (decent 2BR) | — | N/A | [verification required] | §5.5 |
| Healthcare | — | N/A | [verification required] | §5.6 |
| Education (future child) | — | N/A | [verification required] | §5.7 |
| Comfort of life | — | N/A | [verification required] | §5.8 |
| Fit for couple with single income | — | N/A | [verification required] | §5.9 |

**Weighted score**: — (compute when all criteria are scored)

## Block 3 - Profile by section

### 5.1. Legalization {status: partial, depth: 1, last_updated: 2026-06-04, dod: partial}

> **DoD status**: partial. Entry / visa-alternative mechanics, the ordinary temporary-residence to permanent-residence ladder, and naturalization baseline are opened. `vq-070` and `vq-071` are closed to conservative screening baselines: do not assume a temporary Polish `karta pobytu` waives a Mexican visa; use the serving consulate's economic-solvency test as the controlling gate; treat the rough 2026 income benchmark as above the couple's current income unless savings or a lower post-specific threshold is confirmed.

#### Now (until 03.2027)

- **Entry / visitor baseline (`vq-070` closure)**: INM's visa-required-country page says nationals in the visa-required list must obtain a Mexican visa for entry, including visitor and resident categories. The same page lists alternatives to a Mexican visitor visa: proof of **permanent residence** in Canada, the United States, Japan, the United Kingdom, Schengen countries, or Pacific Alliance countries; or a valid visa from Canada, the United States, Japan, the United Kingdom, or Schengen. For screening, assume a Ukrainian ordinary passport needs a Mexican visa unless a readable official list or visa-checker confirms otherwise. [src-226]
- **Polish `karta pobytu` caveat**: the captured INM alternative is **permanent residence** in a Schengen country, not any temporary Polish residence card. A Polish temporary `karta pobytu` should not be assumed to replace a Mexican visa; if the card is permanent, it may be useful for visitor entry only, not for Mexican residence. [src-226]
- **No dedicated digital-nomad visa captured (`vq-071` closure)**: Mexico is best treated as a temporary-resident / economic-solvency route, not a Panama-style explicit remote-worker visa. Current secondary 2026 guidance says consulates apply economic-solvency thresholds that vary by post; for temporary residence by income, the rough 2026 benchmark is about **US$4,400/month net income for the last 6 months** (some consulates request 12 months), or savings/investments instead. For country screening this closes the blocker: the couple's ~$3,000/month income is likely insufficient through income alone unless a serving consulate accepts a lower threshold or savings route. [src-229]
- **Consular visa then in-country card exchange**: Mexico's federal immigration-tramites catalogue includes the exchange (`canje`) of a consular resident visa into a Mexican migration document and renewal of migration documents. Operationally, the route is normally: get the resident visa from a Mexican consulate, enter Mexico, then exchange it for the residence card with INM. [src-227]

#### After 4 March 2027

- Mexico is outside the EU temporary-protection framework, so the post-03.2027 question is whether the couple can obtain and maintain Mexican ordinary residence before relying on Mexico as a fallback. There is no Ukraine-specific TP bridge to capture.
- The long-term ladder is straightforward in concept: Mexico has a federal procedure for changing to permanent resident after **four years of temporary residence**. Naturalization by residence is handled by SRE under the carta de naturalizacion process; exact ordinary five-year / reduced-term applicability needs a later legal check before using citizenship as a planning advantage. [src-227][src-228]

#### Residence without local employer

- For the IT partner, the most realistic captured route is temporary residence based on economic solvency from foreign income or savings. It does not require a Mexican employer in the first-pass baseline, but it likely requires a consular financial threshold higher than current income. [src-229]
- Remote work for foreign clients while resident, tax residency, RFC/SAT registration, and whether local self-employment registration is needed were not captured in this pass. Treat this as a major follow-up item before Mexico can be ranked.

#### Partner / dependent baseline

- `vq-071` partner closure: no official dependent checklist was captured in this pass, so the safe screening baseline is marriage before any family-unity/dependent strategy or two independently eligible files. Unmarried-partner treatment and dependent solvency uplift are application-prep checks; they should not be assumed in scoring. [src-227][src-229]

#### Personal playbook for our couple

1. **Before relying on Mexico**: confirm whether Ukrainian ordinary passports require a Mexican visitor visa and whether the existing Polish card is temporary or permanent. Do not assume a temporary Polish `karta pobytu` waives the Mexican visa. [src-226]
2. **Consular screen**: ask the serving Mexican consulate for its 2026 temporary-resident economic-solvency numbers, accepted currency, required months of statements, remote-work evidence, and dependent uplift. The rough public benchmark (~US$4,400/month net) is above the couple's current income. [src-229]
3. **If income is insufficient**: check whether savings/investment criteria or a second income can qualify; otherwise Mexico is more of a future option than a current primary route.
4. **If approved**: enter on the resident visa and complete INM `canje` into the residence card; maintain temporary residence toward the four-year permanent-residence change. [src-227]
5. **Before March 2027**: if Mexico is chosen as a fallback, file the ordinary route early enough that the EU TP deadline is not the trigger for a rushed consular application.

### 5.2. Climate {status: deep, depth: 2, last_updated: 2026-06-03, dod: passed}

> **DoD status**: passed at medium confidence. Temperature, clearer-sky day-equivalent proxies, humidity / precipitation comfort, and warm-region tradeoffs are covered for three representative areas.

Mexico's climate fit depends heavily on altitude and coast. The best first-pass household candidates are not necessarily the hottest coastal cities: Mexico City gives mild days and almost no muggy days; Guadalajara / Bajio-style highland cities may offer similar dry comfort; Cancun and Puerto Vallarta are warm but much more humid, with rainy / hurricane-season or tropical-storm caveats. [src-230][src-231][src-232]

| City / area | January average high/low | July average high/low | Clearer-sky day-equivalent proxy | Comfort notes |
|---|---:|---:|---:|---|
| Mexico City | ~21.7 / 6.7 C | ~23.3 / 13.3 C | ~150 days/year | Highland capital; mild days, cold-ish winter nights, pronounced rainy/cloudy summer, virtually 0 muggy days. [src-230][src-232] |
| Cancun | ~27.2 / 19.4 C | ~32.2 / 25.0 C | ~184 days/year | Warm Caribbean option; no cold winter, but many muggy days almost year-round and hurricane/rainy-season exposure. [src-231][src-232] |
| Puerto Vallarta | ~27.2 / 16.7 C | ~32.2 / 24.4 C | ~152 days/year | Pacific coastal warmth; winter is pleasant, but summer is hot, wet, and very muggy. [src-231][src-232] |

**Sunny/clear-day method**: WeatherSpark's Mexico country page reports monthly percentages of time that the sky is clear, mostly clear, or partly cloudy. Converted with month lengths, the medium-confidence clearer-sky day-equivalent proxies are Mexico City ~150, Cancun ~184, and Puerto Vallarta ~152. These are not official sunny-day counts. [src-232]

**Household comfort verdict**: Mexico can satisfy the no-long-cold-winter preference, but the comfortable regions are climate-specific. For daily comfort on one remote IT income, a highland city is likely easier than a humid tourist coast until rent, safety, and healthcare are researched. The coasts are warmer but carry heat, humidity, rainy-season, and storm risk. [src-230][src-231][src-232]

### 5.3. Taxes {status: partial, depth: 1, last_updated: 2026-06-11, dod: partial}

> **DoD status**: partial. A conservative ordinary-resident PIT screen is now available for a foreign-client IT worker at USD 3,000/month. Run-093 resolved `vq-113` for country screening: ordinary PIT plus explicit RESICO/VAT/IMSS caveats are enough for comparison, while exact SAT regime, RESICO eligibility, VAT/export-of-services treatment, IMSS/social-security obligations, and temporary-residence compatibility remain accountant/application-prep checks before DoD-passed filing advice.

#### Tax residence and scope

- **Residence baseline**: PwC says the Federal Tax Code treats a person as Mexican tax-resident when they establish a home in Mexico; if the person also has a home elsewhere, the centre of vital interests test applies. Resident individuals are taxed on worldwide income regardless of nationality, while non-residents are taxed only on Mexican-source income. [src-449][src-450]
- **Planning implication**: if the couple actually settles in Mexico, the working partner should assume Mexican tax-resident filing and worldwide-income reporting rather than a visitor-only or non-resident model. This is especially important because Mexico is not a clean digital-nomad-tax-holiday jurisdiction in the captured sources. [src-449][src-450]

#### Ordinary individual / professional-services screen

- **2026 resident PIT table**: PwC's 2026 resident table is progressive up to 35%. At the run-091 FX snapshot, USD 3,000/month is about **MXN 52,292/month** or **MXN 627,503/year**. That falls in the MXN 424,353.98-668,840.14 annual bracket: MXN 67,981.92 basic tax plus 23.52% on the excess. [src-449][src-455]
- **Worked example (ordinary PIT-only)**: gross MXN 627,503/year -> estimated PIT about **MXN 115,762/year** / **MXN 9,647/month** -> net about **MXN 42,645/month**, roughly **USD 2,447/month**, before accountant fees, e.firma / CFDI administration, VAT, and any IMSS / social-security treatment. [src-449][src-453][src-455]
- **Business deductions**: PwC says business owners and independent professionals may deduct most of the same business expenses as corporations, while there is no standard deduction and professional/business losses are ring-fenced against professional/business income. This could improve the ordinary-regime net if the worker has deductible business costs, but this pass keeps the screening model conservative and does not assume a specific deduction percentage. [src-451]

#### RESICO / simplified trust caveat

- Mexico has a known simplified-trust regime for some individuals, but SAT pages were not captured cleanly in this cron pass and PwC's extracted pages did not provide enough regime mechanics to use it as the baseline. Treat **RESICO eligibility, foreign-client IT fit, and rate/table mechanics as verification-required** rather than assuming a 1%-2.5% low-tax outcome. [src-451]

#### Social security, VAT, filing, and marriage

- **Social security / IMSS**: PwC's individual page describes employee IMSS contributions withheld at source and employer contributions with annual employee maximums, but it does not answer whether a foreign-client independent IT contractor on a temporary-residence route must or may register with IMSS. The screening model therefore excludes IMSS and flags this as an accountant/SAT/IMSS check. [src-452]
- **VAT / IVA**: PwC reports Mexico's VAT at **16%** on sales of goods and services, leases, and imports, with an 8% effective rate possible in the northern border region. Corporate VAT context confirms the same 16% general rate and lists exempt categories, but this pass did not verify whether foreign-client software/IT services can be zero-rated/exported or how invoices must be worded. [src-452][src-454]
- **Filing**: the tax year is 1 January-31 December; residents receiving income generally file an annual return by **30 April** of the following year, usually electronically with an advanced electronic signature. [src-453]
- **Marriage**: joint returns are not allowed. PwC notes a limited investment-income reporting rule for married couples, but personal service income should be declared by the spouse who earns it. Marriage helps immigration/dependency more than the captured tax model. [src-453]

#### Conservative verdict for the couple

At the current USD 3,000/month income, Mexico is not tax-prohibitive in the ordinary PIT-only model, but it is also not a low-tax answer: a conservative resident-professional screen leaves about **USD 2,447/month** before accountant, VAT, social-security/IMSS, health insurance, and immigration costs. Because the immigration solvency gate already appears above the couple's income, tax attractiveness alone does not fix Mexico's main route problem. Run-093 closed `vq-113` for screening only; do not mark section 5.3 passed until a Mexican accountant or official SAT/IMSS guidance confirms RESICO/ordinary-regime registration, VAT/export-service handling, contribution duties, and compatibility with temporary residence. [src-449][src-451][src-452][src-453][src-454][src-455]

### 5.4. Cost of living {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

### 5.5. Rent {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

### 5.6. Healthcare {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

### 5.7. Education (future child) {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

### 5.8. Comfort of life {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

### 5.9. Partner (student) {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

### 5.10. Risk dimensions {status: pending, depth: 0, last_updated: —, dod: pending}

- **Currency/banking risk**: [verification required]
- **Political risk**: [verification required]
- **Ties to Ukraine**: [verification required]
- **Diaspora and adaptation**: [verification required]

### 5.11. Bureaucracy and practicality {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

## Block 4 - Risk dimensions (summary)

| Category | Level | Rationale |
|---|---|---|
| Currency / banking | — | [verification required] |
| Political | — | [verification required] |
| Ties to Ukraine | — | [verification required] |
| Diaspora / adaptation | — | [verification required] |

## Block 5 - Practical verdict

- **Can relocate now**: possible only after entry / consular requirements are confirmed. Conservative baseline: Ukrainian citizens need a Mexican visa unless a qualifying alternative document applies, and a temporary Polish residence card is not enough. [src-226]
- **Best legalization path for the man**: temporary resident visa based on economic solvency if income/savings meet the serving-consulate threshold; no dedicated DN route captured. [src-227][src-229]
- **Best legalization path for the woman**: spouse/family-unity route if married and eligible, or independent file; do not assume an unmarried-partner or one-income dependent route until the serving consulate confirms it. [src-227][src-229]
- **Does marriage change the picture**: probably yes for dependent/family-unity clarity, but the exact Mexican dependent evidence and solvency uplift were not captured.
- **Realism of staying after 03.2027**: medium-low at current income until the solvency threshold is solved; ordinary temporary residence can lead to permanent residence after four years if obtained and maintained. Tax screening is workable under ordinary PIT but not enough to overcome the immigration income gate by itself. [src-227][src-449]

**Pros**:
- Ordinary non-EU residence ladder avoids EU temporary-protection uncertainty. [src-227]
- Permanent-residence change after four years of temporary residence is a clear long-term concept. [src-227]
- Highland climates can be mild year-round with very low muggy-day burden. [src-230][src-232]

**Cons / risks**:
- Standard 2026 temporary-residence income benchmark appears above the couple's current ~$3,000/month. [src-229]
- Ukrainian entry / visa-waiver alternatives need a readable official country-list confirmation. [src-226]
- Partner/dependent mechanics should be handled spouse-first for screening; remote-work tax compliance remains accountant-level, especially RESICO, VAT/export-service, and IMSS treatment. [src-451][src-452][src-454]
- Coastal warmth comes with high humidity, rainy-season, and storm exposure. [src-231][src-232]

## Block 6 - Practical playbook (working relocation guide)

### 6a. Before the move (what to prepare in Ukraine / Poland)
- Passports for both partners; proof of any valid visas or permanent residence documents that could waive a Mexican visitor visa. [src-226]
- Bank statements and employment/client contracts showing foreign remote IT income; ask the consulate whether it accepts the couple's currency and how many months are required. [src-229]
- Marriage certificate if they marry; apostille/translation requirements need official confirmation. [verification required]
- Police certificates, birth certificates, tax records, and savings evidence to be checked against the serving-consulate list. [verification required]

### 6b. First month after arrival
- If a resident visa is granted, complete the INM exchange (`canje`) into a residence card rather than staying only as a visitor. [src-227]
- Start RFC/SAT and tax-residency checks before invoicing foreign clients from Mexico. [verification required]

### 6c. First 3-6 months
- Keep proof of residence, income, and address for renewal.
- Decide whether a highland city or coast is the realistic climate/cost fit; climate alone does not justify a tourist coast.

### 6d. Before March 2027 (critical deadline)
- Mexico should only be treated as a post-EU-TP fallback if the resident-visa threshold and partner file are solved well before March 2027.

### 6e. Long-term (4-6 years)
- Maintain temporary residence and check eligibility for permanent-residence change after four years. [src-227]
- Verify naturalization residence period, Spanish/culture exam, absence limits, and dual-citizenship consequences before treating citizenship as a strategic advantage. [src-228]

### 6f. Relocation budget (one-time costs)

| Item | USD / EUR | Notes |
|---|---:|---|
| Visa / residence permit fees | — | [verification required] |
| Apostilles and translations | — | [verification required] |
| Flights for two | — | [verification required] |
| Rental deposit | — | [verification required] |
| First month rent | — | [verification required] |
| Health insurance / healthcare entry costs | — | [verification required] |
| Immigration lawyer / facilitator | — | Useful for consular threshold and dependent file. |
| Buffer / contingencies | — | [verification required] |
| **Total** | — | |

### 6g. Contact points and communities
- Immigration lawyers / facilitators: [verification required]
- Ukrainian / Russian-speaking diaspora: [verification required]
- Expat communities in Mexico City / Guadalajara / Cancun / Puerto Vallarta: [verification required]
- Official immigration points: INM / Mexican consulate serving current residence. [src-226][src-227]

## Block 7 - Sources

### 7a. Official primary
- [src-226] INM visa-required country / alternatives page.
- [src-227] Gob.mx / INM migration-document exchange, renewal, and permanent-residence-after-four-years procedures.
- [src-228] SRE carta de naturalizacion by residence procedure.

### 7b. Reliable secondary
- [src-229] Mexperience 2026 financial-criteria guide for Mexican residency.
- [src-449] PwC Mexico individual taxes on personal income.
- [src-450] PwC Mexico individual residence.
- [src-451] PwC Mexico individual deductions.
- [src-452] PwC Mexico individual other taxes.
- [src-453] PwC Mexico individual tax administration.
- [src-454] PwC Mexico corporate other taxes.

### 7c. Community and forums
- None used in this pass.

### 7d. Statistical / commercial
- [src-230] Climate to Travel Mexico City.
- [src-231] Climate to Travel Cancun / Puerto Vallarta / Mexico overview.
- [src-232] WeatherSpark Mexico country climate comparison.
- [src-455] ExchangeRate-API USD/MXN snapshot.

### 7e. Not found / not captured cleanly
- Readable official OCR/text for Ukraine's exact placement in Mexico's visa-required / visa-free list.
- Serving-consulate 2026 temporary-resident economic-solvency checklist and exact USD/EUR/UAH thresholds.
- Dependent / family-unity mechanics for a spouse or unmarried partner of a temporary resident.
- Remote-work tax / local registration treatment for foreign-client IT income: ordinary PIT is screened and `vq-113` was resolved for screening in run-093, but exact SAT regime, RESICO eligibility, VAT/export-service handling, IMSS/social-security duty, and residence-file compatibility remain application-prep/accountant checks.

## Block 8 - Open questions and verification notes

- `vq-070` — Mexico Ukrainian entry / visa-waiver alternatives and Polish residence-card treatment from a readable official source.
- `vq-071` — Mexico temporary-resident economic-solvency threshold, remote-work fit, dependent mechanics, PR counting, and naturalization details.
- `vq-113` resolved for screening in run-093 — Mexico has a conservative ordinary-PIT tax baseline; exact tax registration, RESICO eligibility, VAT/export-service treatment, IMSS/social-security position, and immigration-file fit remain application-prep/accountant checks.
