---
country: Mexico
tier: null
depth_score: 10.0
last_updated: 2026-06-29T22:31:12Z
sections_completed: ["5.2", "5.4", "5.5", "5.7", "5.8", "5.9", "5.10", "5.11"]
sections_partial: ["5.1", "5.3", "5.6"]
sections_pending: []
risk_flags: ["ukrainian-entry-visa-likely-required", "temporary-residence-income-above-current-budget", "no-dedicated-digital-nomad-visa", "coastal-heat-humidity", "mexico-resico-eligibility-gap", "mexico-vat-export-service-gap", "mexico-social-security-category-gap", "mexico-city-rent-pressure", "tourist-coast-cost-pressure", "mexico-health-insurance-quote-gap", "mexico-international-school-cost-risk", "mexico-public-safety-regional-risk", "mexico-spanish-language-integration-needed", "mexico-one-income-margin-risk"]
sources_used: ["src-226", "src-227", "src-228", "src-229", "src-230", "src-231", "src-232", "src-449", "src-450", "src-451", "src-452", "src-453", "src-454", "src-455", "src-570", "src-571", "src-572", "src-573", "src-574", "src-709", "src-710", "src-711", "src-712", "src-791", "src-792", "src-832"]
unverified_count: 0
schema_version: 2.0.0
---

# Mexico

## Block 1 - Summary

- **Tier**: TBD. First pass suggests Mexico is a possible ordinary-residence fallback rather than a clean digital-nomad route: temporary residence can lead to permanent residence after four years, but 2026 economic-solvency thresholds appear above the couple's current ~$3,000/month income if they apply through the standard income route. [src-227][src-229]
- **depth_score**: 10.0
- **Last updated**: 2026-06-29T22:31:12Z
- **Tier rationale**: keep as Tier-3 hint until the exact serving-consulate threshold, entry mechanics for Ukrainian passports, taxes, rent, healthcare, and partner sponsorship are checked.

## Block 2 - Scoring

| Criterion | Score (1-10) | Confidence | Brief rationale | Profile section |
|---|---:|---|---|---|
| Legalization (now + post-03.2027) | — | medium | No EU TP dependency; ordinary temporary-residence ladder exists, but the standard solvency route appears above the couple's income and no dedicated DN visa was captured. | §5.1 |
| Climate | — | medium | Huge regional spread: Mexico City is mild and dry-comfortable, while Caribbean / Pacific coasts are warm but humid and rainy in season. | §5.2 |
| Taxes | — | medium | Progressive PIT is workable but not low-tax at USD 3,000/month: ordinary resident PIT-only net screens near USD 2,447/month before accountant, VAT, and any social-security/IMSS obligations. RESICO or export-service VAT treatment could improve the answer, but eligibility was not proven in this pass. | §5.3 |
| Cost of living | — | medium | Mexico is not a low-cost fallback in the captured cities: Mexico City and tourist/coastal choices are tight on one income after tax, while Guadalajara is the best first-pass services/cost compromise. | §5.4 |
| Rent (decent 2BR) | — | medium | A modest 40 m2 proxy is manageable in Guadalajara/Cancun/Merida but Mexico City is expensive and should require a strict rent cap. | §5.5 |
| Healthcare | — | medium | Screenable but not application-ready: public and private providers exist, IMSS/IMSS-Bienestar are key public anchors, and private hospitals are strongest in major cities; exact insurance, IMSS enrollment, maternity/newborn terms, and city prices remain open. | §5.6 |
| Education (future child) | — | medium | Public school is the Spanish-language baseline, while Mexico City / Guadalajara have international-school anchors; exact current tuition, preschool prices, and non-capital availability remain budget checks. | §5.7 |
| Comfort of life | — | medium | Screenable but uneven: safety is regional, TravelSafe gives Mexico safety index 58 / Medium and WPR gives 2025 GPI 2.636; Guadalajara/Merida-style bases need Spanish for daily life. | §5.8 |
| Fit for couple with single income | — | medium | Weak-to-borderline at current income: the working partner likely must solve a consular solvency gate above USD 3,000/month, while the student partner should use marriage/family unity or an independent file. | §5.9 |

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

### 5.4. Cost of living {status: deep, depth: 1, last_updated: 2026-06-14, dod: passed}

> **DoD status**: passed at medium confidence for first-pass screening. Livingcost provides national and city-level one-person / family-of-four cost totals, rent-and-utilities, food, transport, utilities, and internet for Mexico, Mexico City, Guadalajara, Cancun, and Merida. Healthcare, insurance, accountant, immigration-lawyer, live lease, and tax-registration costs remain separate later checks.

Livingcost screens Mexico as mid-cost rather than cheap for the couple's one-income file. The national family-of-four proxy is already about USD 2,555/month, and the practical city choices range from about USD 1,232-1,428/month for one person with rent to about USD 2,969-3,399/month for a family-of-four proxy. Compare these against both gross USD 3,000/month and Mexico's conservative ordinary PIT-only tax screen of about USD 2,447/month before accountant, VAT, IMSS/social-security, health-insurance, and immigration costs. [src-570][src-571][src-572][src-573][src-574][src-449]

| Place | One-person total with rent | Family-of-4 proxy | Food | Transport | Utilities / internet | Budget fit for this couple |
|---|---:|---:|---:|---:|---|---|
| Mexico national average | $1,078 | $2,555 | $395 one person / $1,031 family | $90 / $248 | utilities $45.1 / $69.3; internet $29.3 | Borderline after tax and professional costs: national averages look possible, but the PIT-only tax net leaves limited room for insurance, accountant, immigration, and savings. [src-570] |
| Mexico City | $1,428 | $3,399 | $431 / $1,126 | $103 / $280 | utilities $34.6 / $53.1; internet $33.7 | Best bureaucracy, airport, healthcare, banking, and professional-services base, but the family proxy exceeds gross income and the 40 m2 rent line is high. Use only with a strict housing cap. [src-571] |
| Guadalajara | $1,241 | $2,983 | $416 / $1,090 | $113 / $313 | utilities $27.2 / $42.5; internet $30.7 | Best first-pass balance among captured cities: large-city services, highland climate alternative, and lower rent than Mexico City, but still tight after tax/insurance/accountant costs. [src-572] |
| Cancun | $1,232 | $2,969 | $441 / $1,191 | $149 / $426 | utilities $65 / $97.7; internet $37.3 | Warm coast/tourist-services option; numerically similar to Guadalajara but with higher transport/utilities and climate/tourism-season caveats. [src-573] |
| Merida | $1,258 | $3,028 | $401 / $1,044 | $180 / $524 | utilities $57.2 / $88; internet $35.8 | Warm inland Yucatan option with moderate rent but higher transport in this dataset and heat/humidity follow-up needs. [src-574] |

**One-income interpretation**: Mexico City is weak on the current income unless the couple secures unusually cheap housing and confirms a favorable tax/compliance setup. Guadalajara is the first captured city to screen for services/cost balance. Cancun and Merida are lifestyle/climate alternatives rather than default budget bases; they need live listings, private insurance, safety, and seasonality checks before application planning. [src-571][src-572][src-573][src-574]

**Practical cost caveats**: Livingcost is a medium-confidence commercial/crowdsourced source and does not replace 2026 live rentals, landlord requirements, deposit/commission norms, private health-insurance quotes, accountant/SAT onboarding prices, immigration-lawyer fees, flights, or bilingual service costs. Because Mexico's immigration income gate already appears above the couple's current income, cost affordability does not by itself make Mexico route-ready. [src-229][src-449]

### 5.5. Rent {status: deep, depth: 1, last_updated: 2026-06-14, dod: passed}

> **DoD status**: passed at medium confidence for first-pass screening. Livingcost gives 40 m2 1BR city-center and cheaper 1BR rent lines for the captured cities; this vault uses that 40 m2 1BR line as a modest two-room proxy. The 80 m2 3BR line is included only as an upper-size / future-family stress test, not the default requirement.

| City | 40 m2 1BR city-center proxy | 40 m2 cheaper 1BR proxy | 80 m2 3BR stress-test band | Share of USD 3,000 gross | Share of Mexico PIT-only net (~USD 2,447) | First-pass rent verdict |
|---|---:|---:|---:|---:|---:|---|
| Mexico City | $1,035 | $623 | $1,143-$1,886 | 21%-35% for 40 m2 proxy | 25%-42% | Main rent-pressure warning. Use only if capital services are essential and a cheaper-area modest apartment can be found. The 3BR stress case is incompatible with one income. [src-571] |
| Guadalajara | $776 | $492 | $879-$1,418 | 16%-26% | 20%-32% | Best captured rent/services compromise; still requires a cap because tax, insurance, accountant, and immigration costs will reduce the usable budget. [src-572] |
| Cancun | $626 | $398 | $710-$1,139 | 13%-21% | 16%-26% | Rent is workable on paper, but tourist-market seasonality, humidity/storm exposure, and service-cost markups need later checks. [src-573] |
| Merida | $579 | $461 | $829-$1,041 | 15%-19% | 19%-24% | Workable first-pass rent; useful as a warmer inland alternative if heat, transport, healthcare, and community checks are acceptable. [src-574] |

**City screen**: screen Guadalajara first for the services/cost/highland compromise; use Mexico City mainly for consular/legal/accounting/healthcare access or a short setup period with a strict rent cap. Cancun and Merida are second-stage checks if the couple deliberately prioritizes a warm region and can handle heat, humidity, tourist-season pricing, and hurricane/rainy-season planning. [src-571][src-572][src-573][src-574]

**Search and lease follow-up**: this iteration did not capture live property portals or lease practice. Before treating section 5.5 as application-ready, check Inmuebles24, Vivanuncios, Facebook/WhatsApp groups, deposits/aval/fiador requirements, whether landlords accept foreign remote-worker income, whether the lease supports address evidence for INM/banking/SAT, and whether utilities/internet are billed separately. Keep these as practical-budget checks rather than country-screening blockers.

### 5.6. Healthcare {status: partial, depth: 1, last_updated: 2026-06-19, dod: partial}

> **DoD status**: partial. A first-pass healthcare screen is now available, but route-compliant private insurance, exact IMSS / IMSS-Bienestar / private-policy onboarding by residence and tax status, maternity/newborn coverage, and selected-city private-care prices remain application-prep checks; run-159 resolved `vq-150` for screening.

Mexico has a mixed healthcare system with large public institutions and a substantial urban private sector. Trade.gov describes public coverage through IMSS, ISSSTE, and the newer IMSS-Bienestar system, with private care expanding in urban areas because middle- and high-income patients seek higher-quality care. For the couple, this means Mexico City and Guadalajara are the safest first healthcare screens, while smaller or coastal bases need a private-clinic/hospital check before commitment. [src-709]

The official public anchors are the Secretariat of Health and IMSS. The Secretariat of Health site is the federal health-authority reference point, while the IMSS site provides citizen-facing information, procedures, facilities, and online health services. This pass did not capture a clean official answer on whether a temporary resident with foreign-client self-employment can voluntarily enroll, what pre-existing-condition or maternity limits apply, or how IMSS-Bienestar access works in practice for foreign residents. [src-710]

A 2026 expat healthcare guide gives a useful but medium-confidence private-market screen: it says Mexican private insurance is commonly around **USD 150-300/month** for long-term expats, serious uninsured private bills can reach **USD 5,000-50,000**, and top private hospitals in Mexico City include ABC Medical Center, Medica Sur, and Hospital Angeles. Treat those as budgeting proxies only, not visa-compliant quotes. [src-711]

**Household verdict**: healthcare is not a reason to exclude Mexico at country-screening level, especially if the base is Mexico City or Guadalajara and the couple budgets for private insurance. It is still not application-ready: exact accepted policy wording, maternity/newborn coverage, IMSS eligibility/costs by final status, and city-specific GP/pediatric/maternity prices need verification before a move plan. [src-709][src-710][src-711]

### 5.7. Education (future child) {status: deep, depth: 1, last_updated: 2026-06-19, dod: passed}

> **DoD status**: passed at medium confidence for first-pass screening. Public-school authority, Spanish-language public baseline, and international/private-school anchors are captured. Exact school fee schedules, private preschool prices, waiting lists, and non-capital / non-Guadalajara availability remain application-prep checks; run-159 resolved `vq-151` for screening.

The official authority anchor is the Secretariat of Public Education (SEP), whose federal site describes its purpose as guaranteeing equitable, inclusive, intercultural, and comprehensive education for Mexico's population and links to basic-education resources. For a future child, the practical public-school baseline is Spanish-language integration through SEP/state schools, with bilingual/private options if the couple's budget allows. [src-712]

A 2026 expat education guide supports the screening baseline that public school is free for resident children but Spanish-only, while bilingual private schools can be much cheaper than top international schools. It gives broad current proxies: bilingual private schools around **USD 2,000-6,000/year**, Mexico City international schools around **USD 8,000-18,000/year**, and warns that some leading schools can have early applications / waiting lists. [src-711]

For city selection, Mexico City has the strongest international-school ecosystem: the American School Foundation states it was founded in Mexico City in 1888 and offers Early Childhood, Lower, Middle, and Upper School divisions; the same guide names ASF, Peterson, Westhill, The English School, and Edron as CDMX anchors. Guadalajara also has an international-school anchor via the American School Foundation of Guadalajara, but exact tuition and private-preschool costs were not captured. [src-711]

**Household verdict**: Mexico is education-screenable if the family accepts Spanish public schooling or can budget for private/bilingual schooling. On one income after Mexico's conservative tax screen, top CDMX international-school tuition is a major risk; Guadalajara or Spanish public/private bilingual options are more realistic first-pass paths. [src-711][src-712]


### 5.8. Comfort of life {status: deep, depth: 1, last_updated: 2026-06-24, dod: passed}

> **DoD status**: passed at medium confidence for country screening. Public-safety, English/Spanish adaptation, transport, climate-city comfort, healthcare/education service depth, and city-fit tradeoffs are covered. Exact neighborhood crime, live lease friction, local lawyer/accountant quality, and final-city community checks remain application-prep work.

Mexico is livable for a remote-work household, but comfort is strongly city- and neighborhood-dependent. WPR's 2026 safest-countries table gives Mexico a 2025 Global Peace Index score of **2.636**, Global Terrorism Index **0.582**, safety index **65**, Medium risk level, and US News safest-country rank **81st**. TravelSafe's country page gives Safety Index **58**, user sentiment 75/100, and overall risk Medium; it also says major tourist areas are generally safe but flags crime/kidnapping concerns and regional variation. Treat this as a regional-security screen, not a blanket no-go. [src-791]

Transport and daily movement need conservative habits. TravelSafe labels transport/taxi risk Low but recommends approved/licensed taxis, hotel-called taxis, and caution with crowded public transport; it labels pickpocket risk High in tourist areas. For the couple, that points to a stable neighborhood, app-based transport or known taxi stands, and avoiding border/high-crime zones rather than trying to optimize only for climate or rent. [src-791]

English is weaker than in most earlier candidate countries. EF EPI lists Mexico at global rank **#103**, score **440** versus global average 488, with city variation: Monterrey 532, Guadalajara 511, Merida 470, Mexico City 428, and Cancun 414. English may work in expat/tourist/private-service contexts, but Spanish is the operating language for INM, SAT/RFC, landlords, doctors, schools, banking, utilities, and neighborhood life. [src-792]

City comfort screen:

| City / base | Comfort upside | Comfort downside | Screening verdict |
|---|---|---|---|
| Guadalajara | Best captured services/cost compromise, lower rent than Mexico City, large-city amenities, EF city score 511. [src-572][src-792] | Still tight after tax/insurance/accountant costs; Spanish needed for bureaucracy and leases. | First city to screen if Mexico remains viable. |
| Mexico City | Deepest bureaucracy, healthcare, airport, schooling, and professional-services base. [src-571][src-709][src-711] | Rent and family-cost proxies are high; EF city score 428; crime/neighborhood selection matters. [src-571][src-791][src-792] | Use for setup or services only with strict rent and safety filters. |
| Merida | Warm inland option with workable rent proxy and likely calmer lifestyle; EF city score 470. [src-574][src-792] | Heat/humidity, transport, healthcare depth, and community fit need follow-up. | Good second-stage warmer-base check. |
| Cancun / coast | Warm climate, tourist-service ecosystem, low first-pass rent proxy. [src-573] | Tourist pricing, pickpocket/scam exposure, humidity/storms, and weaker EF city score 414. [src-573][src-791][src-792] | Lifestyle exception, not default one-income base. |

**Comfort verdict**: Mexico can pass a screening-level comfort bar if the couple chooses a safer, service-rich neighborhood and commits to Spanish. It is not a low-friction English-first relocation: city selection, transport habits, private healthcare planning, Spanish-language bureaucracy, and neighborhood safety are core practical constraints. [src-791][src-792]

### 5.9. Partner (student) {status: deep, depth: 1, last_updated: 2026-06-24, dod: passed}

> **DoD status**: passed at medium confidence for screening. The section now covers the student partner's likely status logic, remote Ukrainian study, marriage/dependent baseline, work-right constraints, language adaptation, healthcare/education implications, and one-income budget fit. Exact family-unity checklist, apostille/translation requirements, dependent solvency uplift, and student/work authorization details remain serving-consulate / lawyer checks.

For the student partner, the conservative planning baseline is **marriage/family unity or a separate independent file**, not an assumed unmarried-partner dependent route. The Mexico profile already treats dependent mechanics as unresolved and spouse-first for screening; no captured source proves an unmarried partner can ride on the working partner's temporary-residence file. [src-227][src-229]

Remote Ukrainian university study is compatible with daily life only after she has lawful status and a stable address. It does not by itself solve Mexican residence, income thresholds, health coverage, school/future-child planning, or Spanish-language bureaucracy. If she later wants to work locally or invoice clients, the couple needs a separate SAT/RFC, immigration-permission, and tax check; do not assume the working partner's file automatically authorizes both partners' economic activity. [src-227][src-449][src-453]

One-income fit remains Mexico's main weakness. Even before partner costs, the standard temporary-residence income benchmark captured from 2026 secondary guidance is about USD 4,400/month net, above the couple's current income; the conservative ordinary-resident PIT-only tax screen leaves about USD 2,447/month before accountant, VAT, IMSS/social-security, health insurance, and immigration costs. Rent can be workable outside Mexico City, but the route gate, private insurance, Spanish support, and professional fees make the margin tight. [src-229][src-449][src-455][src-571][src-572][src-573][src-574]

Practical partner playbook:

1. **Before filing**: decide whether to marry. For Mexico screening, marriage is the safer dependent/family-unity assumption; unmarried-partner treatment is not bankable. [src-227][src-229]
2. **Consular threshold check**: ask the serving consulate whether a spouse/dependent is allowed on the same file, whether income/savings thresholds increase for the spouse, and which apostilled/translated documents are required. [src-229]
3. **Study continuity**: keep Ukrainian university enrollment online, but do not cite it as a residence basis unless a separate Mexican student/residence option is deliberately chosen.
4. **Language plan**: budget time and money for Spanish; EF's low national score means English-only handling of INM/SAT/leases/healthcare is not realistic outside narrow private-service contexts. [src-792]
5. **Budget plan**: use Guadalajara or Merida as first screening bases, keep Mexico City for setup/services if needed, and avoid assuming coastal tourist markets are cheap once transport, insurance, safety, and seasonality are included. [src-571][src-572][src-573][src-574]

**Partner-fit verdict**: Mexico is not impossible for the student partner, but it is fragile on the couple's current facts. It works only if the main applicant clears the consular financial gate or savings route, the partner path is spouse/family-unity or independently eligible, and the household accepts Spanish-first administration plus a tight one-income budget. [src-227][src-229][src-792]

### 5.10. Risk dimensions {status: deep, depth: 1, last_updated: 2026-06-26, dod: passed}

> **DoD status**: passed for country screening at medium confidence. Currency/banking, political/safety, ties-to-Ukraine, and diaspora/adaptation risks are explicit enough for comparison. Serving-consulate solvency, SAT/RFC setup, neighborhood safety, and live community checks remain application-prep work.

- **Currency / banking risk**: Medium-high. MXN exposure is not the only issue: a temporary-residence file likely needs consular financial evidence, then INM/RFC/SAT banking and invoice setup. Ordinary PIT-only net screens near USD 2,447/month before VAT, IMSS, accountant, insurance, and immigration costs, while RESICO/export-service treatment is not yet proven. [src-227][src-229][src-449][src-452][src-455]
- **Political / safety risk**: Medium-high. Mexico is regionally uneven: WPR/TravelSafe proxies give medium overall risk, but crime/kidnapping concerns, tourist-area pickpocketing, transport habits, and neighborhood selection matter. Treat Guadalajara or Merida-style screened neighborhoods as mandatory rather than assuming countrywide comfort. [src-791]
- **Ties to Ukraine**: High risk. Mexico has no EU TP bridge, ordinary entry may require a visa, a temporary Polish residence card should not be assumed to waive Mexican entry, and the standard temporary-residence income benchmark appears above the couple's current USD 3,000/month. [src-226][src-229]
- **Diaspora / adaptation**: Medium-high. Spanish is the operating language for INM, SAT/RFC, leases, public healthcare, schools, and banking; EF places Mexico low nationally, although Guadalajara and Merida are more workable than some alternatives. [src-792]
- **Main route risk**: Mexico's long-term ladder is conceptually attractive because temporary residence can lead to permanent residence after four years, but at this income the solvency gate and tax/compliance file are the blockers. [src-227][src-229][src-449]

### 5.11. Bureaucracy and practicality {status: deep, depth: 1, last_updated: 2026-06-29, dod: passed}

> **DoD status**: passed at medium confidence for country screening. Route timing, filing location, in-country practicality, and one neutral professional-contact lead are now explicit enough for comparison; exact consular appointment timing, local document translations, lawyer engagement terms, INM/SAT sequencing, and final-city lease/address support remain application-prep checks.

Mexico is bureaucratically visible but not route-easy for this couple. The main durable path remains a **consular temporary-resident visa based on economic solvency or savings**, followed by in-country exchange (`canje`) into a Mexican residence card with INM. That means the real clock starts before travel: the couple should confirm the serving consulate's threshold, required bank-statement period, dependent uplift, interview/appointment timing, and accepted proof of foreign remote IT income before treating Mexico as a March-2027 fallback. [src-227][src-229]

Route timing is less deterministic than the Panama-style remote-worker route captured in the previous slice. The public INM procedure catalogue confirms the post-entry exchange and later renewal / permanent-residence-after-four-years procedures, while the financial gate is consulate-specific in current secondary guidance. Fragomen's Mexico page also warns at a general level that requirements, processing times, and employment eligibility vary by visa classification. For planning, treat Mexico as a **pre-clearance country**: do not move first and hope to solve residence locally unless the visa / alternative-entry and `canje` sequence is already approved. [src-227][src-229][src-832]

Filing practicality is therefore two-stage:

1. **Before travel / outside Mexico**: confirm Ukrainian entry, whether any permanent-residence or valid-visa alternative applies, and file the resident-visa route at the competent Mexican consulate if eligible. A temporary Polish residence card should not be assumed to waive the Mexican visa. [src-226][src-229]
2. **After arrival with a resident visa**: complete INM `canje`, then coordinate RFC/SAT, banking, lease/address evidence, private insurance or IMSS advice, and renewal evidence. Guadalajara is still the best first screening city for services/cost balance; Mexico City is useful for lawyers, consular follow-up, healthcare, banking, and schools but needs a strict rent/safety cap. [src-227][src-571][src-572][src-709][src-792]

**Professional-contact lead (neutral, not a recommendation)**: Fragomen has a Mexico country page and a related Mexico City office / regional coordination-center listing with phone **+52 55 9420 0200**. Its public materials describe immigration support for companies sending employees to Mexico or expanding there, Mexican visa-classification variability, business/work visitor constraints, and services that go beyond preparing and filing visa/work-permit applications. This is useful as a screening lead for consular route fit, employer/foreign-client evidence, and processing variability, but the couple should compare it with Mexico-focused local immigration/tax counsel before filing. [src-832]

**Practicality verdict**: Mexico is screenable but fragile. It has a long-term residence concept after four years of temporary residence, large-city services, and professional support, but the couple's current USD 3,000/month income is below the captured rough income benchmark. Mexico should be treated as a future ordinary-residence option or savings-supported fallback unless a serving consulate confirms eligibility; Spanish-language administration, SAT/RFC/VAT/IMSS advice, private insurance, lease/address proof, and spouse/family documentation all need coordinated support. [src-227][src-229][src-449][src-452][src-571][src-572][src-792]

## Block 4 - Risk dimensions (summary)

| Category | Level | Rationale |
|---|---|---|
| Currency / banking | Medium-high | MXN/SAT/RFC and tax-registration mechanics combine with a conservative PIT-only net around USD 2,447/month and unresolved VAT/IMSS/RESICO fit. [src-449][src-452][src-455] |
| Political / safety | Medium-high | Safety is city/neighborhood-specific; WPR/TravelSafe support a medium-risk screen with crime, transport, and tourist-area caution. [src-791] |
| Ties to Ukraine | High | No TP bridge; Ukrainian entry / visa-alternative mechanics and the consular solvency gate are still controlling, and Mexico is distant from the Poland/Ukraine support base. [src-226][src-229] |
| Diaspora / adaptation | Medium-high | Spanish-first administration is unavoidable and EF scores are low nationally; Guadalajara/Merida are more plausible than English-default planning. [src-792] |

## Block 5 - Practical verdict

- **Can relocate now**: possible only after entry / consular requirements are confirmed. Conservative baseline: Ukrainian citizens need a Mexican visa unless a qualifying alternative document applies, and a temporary Polish residence card is not enough. [src-226]
- **Best legalization path for the man**: temporary resident visa based on economic solvency if income/savings meet the serving-consulate threshold; no dedicated DN route captured. [src-227][src-229]
- **Best legalization path for the woman**: spouse/family-unity route if married and eligible, or independent file; do not assume an unmarried-partner or one-income dependent route until the serving consulate confirms it. [src-227][src-229]
- **Does marriage change the picture**: probably yes for dependent/family-unity clarity, but the exact Mexican dependent evidence and solvency uplift were not captured. For screening, marriage is the safer partner assumption; an unmarried-partner route is not bankable. [src-227][src-229]
- **Best first city screen**: Guadalajara first, then Merida as a warmer lower-rent check; Mexico City mainly for setup/services with a strict rent and neighborhood-safety cap; Cancun/coasts only as lifestyle exceptions. [src-571][src-572][src-573][src-574][src-791][src-792]
- **Realism of staying after 03.2027**: medium-low at current income until the solvency threshold is solved; ordinary temporary residence can lead to permanent residence after four years if obtained and maintained. Tax screening plus cost/rent/comfort screening is workable only with Spanish-first administration, private insurance/professional-fee buffers, and a strict city/housing choice. [src-227][src-449][src-571][src-572][src-573][src-574][src-791][src-792]

**Pros**:
- Ordinary non-EU residence ladder avoids EU temporary-protection uncertainty. [src-227]
- Permanent-residence change after four years of temporary residence is a clear long-term concept. [src-227]
- Highland climates can be mild year-round with very low muggy-day burden. [src-230][src-232]
- Guadalajara, Cancun, and Merida show workable first-pass 40 m2 rent proxies under about $800/month, although non-rent costs still matter. [src-572][src-573][src-574]
- Large-city and tourist-service depth can support remote work, private healthcare, and future-child education if the couple budgets carefully and chooses neighborhoods conservatively. [src-709][src-711][src-791]

**Cons / risks**:
- Standard 2026 temporary-residence income benchmark appears above the couple's current ~$3,000/month. [src-229]
- Ukrainian entry / visa-waiver alternatives need a readable official country-list confirmation. [src-226]
- Partner/dependent mechanics should be handled spouse-first for screening; remote-work tax compliance remains accountant-level, especially RESICO, VAT/export-service, and IMSS treatment. [src-451][src-452][src-454]
- Coastal warmth comes with high humidity, rainy-season, storm exposure, tourist-market pricing, and seasonal lease risk. [src-231][src-232][src-573]
- Mexico City rent is a budget-pressure flag: the captured 40 m2 city-center proxy is about $1,035/month, roughly 42% of the conservative PIT-only net. [src-571]
- Public-safety and language comfort are real constraints: TravelSafe gives Mexico Safety Index 58 / Medium with regional variation and pickpocket risk, while EF ranks Mexico #103 with score 440, so Spanish is necessary for practical settlement. [src-791][src-792]

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
- Decide whether a highland city or coast is the realistic climate/cost/safety fit; climate alone does not justify a tourist coast. Guadalajara is the first screening city, with Merida as a warmer second-stage check. [src-572][src-574][src-791]

### 6d. Before March 2027 (critical deadline)
- Mexico should only be treated as a post-EU-TP fallback if the resident-visa threshold, partner file, private insurance/IMSS plan, and school-language budget are solved well before March 2027.

### 6e. Long-term (4-6 years)
- Maintain temporary residence and check eligibility for permanent-residence change after four years. [src-227]
- Verify naturalization residence period, Spanish/culture exam, absence limits, and dual-citizenship consequences before treating citizenship as a strategic advantage. [src-228]

### 6f. Relocation budget (one-time costs)

| Item | USD / EUR | Notes |
|---|---:|---|
| Visa / residence permit fees | — | [verification required] |
| Apostilles and translations | — | [verification required] |
| Flights for two | — | [verification required] |
| Rental deposit | — | [verification required]; first-pass rent proxy is $492-$776 in Guadalajara, $398-$626 in Cancun, $461-$579 in Merida, and $623-$1,035 in Mexico City before deposits/fees. [src-571][src-572][src-573][src-574] |
| First month rent | $398-$1,035 | First-pass 40 m2 cheaper-to-city-center proxy across the captured cities; Mexico City should be capped strictly. [src-571][src-572][src-573][src-574] |
| Health insurance / healthcare entry costs | ~$150-$300/month private-insurance proxy | Medium-confidence expat guide proxy only; exact policy, maternity/newborn coverage, IMSS eligibility/costs, and city provider prices remain application-prep checks after run-159 resolved `vq-150` for screening. [src-711] |
| Immigration lawyer / facilitator | — | Fragomen Mexico City is captured as one neutral immigration-services contact lead; compare with local immigration/tax counsel before filing. [src-832] |
| Buffer / contingencies | — | [verification required] |
| **Total** | — | |

### 6g. Contact points and communities
- Immigration lawyers / facilitators: Fragomen Mexico City / Mexico country page is captured as one neutral lead for immigration support and processing-variability screening; phone +52 55 9420 0200. [src-832]
- Ukrainian / Russian-speaking diaspora: [verification required]
- Expat communities in Mexico City / Guadalajara / Cancun / Merida / Puerto Vallarta: [verification required]
- Spanish-language tutor / translator support for INM, SAT/RFC, leases, and healthcare should be budgeted because EF ranks Mexico low for English proficiency. [src-792]
- Official immigration points: INM / Mexican consulate serving current residence. [src-226][src-227]

## Block 7 - Sources

### 7a. Official primary
- [src-226] INM visa-required country / alternatives page.
- [src-227] Gob.mx / INM migration-document exchange, renewal, and permanent-residence-after-four-years procedures.
- [src-228] SRE carta de naturalizacion by residence procedure.
- [src-710] Mexico Secretariat of Health / IMSS public websites.
- [src-712] Mexico Secretariat of Public Education (SEP) public website and basic-education links.

### 7b. Reliable secondary
- [src-229] Mexperience 2026 financial-criteria guide for Mexican residency.
- [src-449] PwC Mexico individual taxes on personal income.
- [src-450] PwC Mexico individual residence.
- [src-451] PwC Mexico individual deductions.
- [src-452] PwC Mexico individual other taxes.
- [src-453] PwC Mexico individual tax administration.
- [src-454] PwC Mexico corporate other taxes.
- [src-709] Trade.gov Mexico healthcare products/services market overview.

### 7c. Community and forums
- None used in this pass.

### 7d. Statistical / commercial
- [src-230] Climate to Travel Mexico City.
- [src-231] Climate to Travel Cancun / Puerto Vallarta / Mexico overview.
- [src-232] WeatherSpark Mexico country climate comparison.
- [src-455] ExchangeRate-API USD/MXN snapshot.
- [src-570] Livingcost Mexico national cost/rent page.
- [src-571] Livingcost Mexico City cost/rent page.
- [src-572] Livingcost Guadalajara cost/rent page.
- [src-573] Livingcost Cancun cost/rent page.
- [src-574] Livingcost Merida cost/rent page.
- [src-711] ExpatLife.AI Mexico healthcare and education 2026 guides plus ASF/ASFG public school websites.
- [src-791] World Population Review / TravelSafe Mexico safety proxies.
- [src-792] EF English Proficiency Index Mexico.
- [src-832] Fragomen Mexico country and services / Mexico City office listing.

### 7e. Not found / not captured cleanly
- Readable official OCR/text for Ukraine's exact placement in Mexico's visa-required / visa-free list.
- Serving-consulate 2026 temporary-resident economic-solvency checklist and exact USD/EUR/UAH thresholds.
- Dependent / family-unity mechanics for a spouse or unmarried partner of a temporary resident.
- Remote-work tax / local registration treatment for foreign-client IT income: ordinary PIT is screened and `vq-113` was resolved for screening in run-093, but exact SAT regime, RESICO eligibility, VAT/export-service handling, IMSS/social-security duty, and residence-file compatibility remain application-prep/accountant checks.
- Route-compliant private health-insurance quotes, maternity/newborn terms, IMSS / IMSS-Bienestar onboarding by final status, and selected-city private-care prices remain application-prep checks after run-159 resolved `vq-150` for screening.
- Exact international/bilingual school tuition, private-preschool prices, waiting lists, and non-CDMX/non-Guadalajara options remain application-prep / final-city checks after run-159 resolved `vq-151` for screening.
- Exact safe neighborhoods, live local lease friction, Spanish-language service providers, final-city Ukrainian/Russian-speaking community depth, serving-consulate appointment timing, lawyer engagement terms, and INM/SAT sequencing remain application-prep checks after sections 5.8, 5.9, and 5.11 were completed for screening.

## Block 8 - Open questions and verification notes

- `vq-070` — Mexico Ukrainian entry / visa-waiver alternatives and Polish residence-card treatment from a readable official source.
- `vq-071` — Mexico temporary-resident economic-solvency threshold, remote-work fit, dependent mechanics, PR counting, and naturalization details.
- `vq-113` resolved for screening in run-093 — Mexico has a conservative ordinary-PIT tax baseline; exact tax registration, RESICO eligibility, VAT/export-service treatment, IMSS/social-security position, and immigration-file fit remain application-prep/accountant checks.
- `vq-150` resolved for screening in run-159: Mexico healthcare insurance, public-system onboarding, maternity/newborn terms, and city-specific private-care prices remain application-prep checks.
- `vq-151` resolved for screening in run-159: Mexico international/bilingual school fees, private-preschool prices, waiting lists, and non-capital options remain application-prep checks.
- Run-195 completed comfort/partner screening: Mexico requires Spanish-first adaptation, neighborhood/security filtering, and a spouse/independent-file partner baseline; exact final-city support networks, lease practice, and family-unity documents remain application-prep checks.
