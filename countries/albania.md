---
country: Albania
tier: null
depth_score: 9.0
last_updated: 2026-06-25T20:50:12Z
sections_completed: ["5.2", "5.4", "5.5", "5.7", "5.8", "5.9", "5.10"]
sections_partial: ["5.1", "5.3", "5.6"]
sections_pending: ["5.11"]
risk_flags: ["official-primary-capture-gaps", "remote-worker-route-application-prep-gap", "albania-tax-regime-2029-sunset", "albania-self-employed-contribution-base-gap", "albania-foreign-client-vat-fit-gap", "tirana-rent-pressure", "albania-private-insurance-quote-gap", "albania-international-school-cost-risk", "albanian-language-integration-needed", "albania-road-and-transport-risk", "albania-one-income-margin-risk"]
sources_used: ["src-164", "src-165", "src-166", "src-167", "src-168", "src-169", "src-170", "src-188", "src-407", "src-408", "src-409", "src-410", "src-411", "src-412", "src-541", "src-542", "src-543", "src-544", "src-680", "src-681", "src-682", "src-683", "src-777", "src-778"]
unverified_count: 0
schema_version: 2.0.0
---

# Albania

## Block 1 — Summary

- **Tier**: TBD. Albania has an attractive remote-worker / Unique Permit narrative and a warm Adriatic/Ionian climate, but this first pass could not capture clean official-primary route pages because several Albanian government sites were blocked or unreachable. Treat the digital-nomad route as promising but medium-confidence until the official e-Albania / State Police / law-text checklist is extracted.
- **depth_score**: 9.0
- **Last updated**: 2026-06-25T20:50:12Z
- **Tier rationale**: Not assigned until taxes, rent, healthcare, and full practical costs are verified. Run-061 closes the remote-worker Unique Permit blocker to a conservative screening baseline: Albania remains a promising ordinary-residence candidate for a foreign-client IT worker, but exact official checklist / fees / PR-counting should be treated as application-prep or deeper-country work, not as a current queue blocker.

## Block 2 — Scoring

| Criterion | Score (1–10) | Confidence | Brief rationale | Profile section |
|---|---:|---|---|---|
| Legalization (now + post-03.2027) | — | N/A | Visa-free entry, Ukraine temporary-protection placeholder, and remote-worker Unique Permit baseline opened; official-primary route pages still need capture. | §5.1 |
| Climate | — | medium | Tirana, Durrës, and Vlorë temperature/rain/sunshine baselines captured; WeatherSpark clearer-sky proxies now close the sunny-day blocker. | §5.2 |
| Taxes | — | medium-high | First-pass self-employed screen: current law/PwC summaries show 0% PIT for self-employed / commercial individuals under ALL 14m gross until 31 Dec 2029, plus minimum self-employed social/health contributions of about ALL 14,900/month; exact activity classification, contribution base, VAT/place-of-supply, and residence-permit fit remain accountant/application-prep checks. | §5.3 |
| Cost of living | — | medium | First-pass Livingcost baseline captured for Albania, Tirana, Durrës, and Vlorë. A $3,000 gross / ~$2,819 favorable tax-screen net can cover modest Albania living costs, with Tirana tighter but still screenable. | §5.4 |
| Rent (decent 2BR) | — | medium | Livingcost 40 m2 1BR proxy is about $449-$703 in Tirana, $322-$449 in Durrës, and $326-$378 in Vlorë; use Tirana with a rent cap and screen coastal cities for seasonality. | §5.5 |
| Healthcare | — | medium | Public system and compulsory insurance fund map captured; Tirana has the main private-hospital market; route-compliant private policy quotes, maternity/newborn cover, foreign-resident public onboarding, and city-specific private-care prices remain application-prep checks. | §5.6 |
| Education (future child) | — | medium-high | Eurydice captures preschool, compulsory basic/lower-secondary structure, and public/private baseline; Tirana International School confirms an English-language international option, but tuition/private-preschool quotes remain application-prep budget checks. | §5.7 |
| Comfort of life | — | medium | Safety screens well by regional standards (GPI 1.812, TravelSafe 75 / Low risk), but road safety, public-transport reliability, petty-crime caution, and Albanian-language friction remain practical constraints. | §5.8 |
| Fit for couple with single income | — | medium | The one-income plan is plausible if the Type D + Unique Permit route and favorable tax screen hold; marriage is the conservative dependent baseline, remote Ukrainian study is practically compatible, and Tirana healthcare/schooling costs can narrow the budget. | §5.9 |

**Weighted score**: — (compute when all criteria are scored)

## Block 3 — Profile by section

### 5.1. Legalization {status: partial, depth: 1, last_updated: 2026-06-06, dod: partial}

> **DoD status**: Partial. First pass opened entry, remote-worker residence, family inclusion, PR/citizenship, and conservative Polish-card interaction baselines. `vq-054` is closed to a safe screening baseline: use ordinary entry/residence planning, not Albania temporary protection or a post-2027 bridge. Run-061 also closes `vq-055` to an operational screening baseline: the secondary-sourced Type D + Unique Permit remote-worker route is enough to keep Albania in the research set as promising for this income profile, while exact official checklist/fees/dependents/PR-counting remain application-prep or later deep-dive items rather than blockers.

#### Now (until 03.2027)

- **Visa-free entry (`vq-054` closure)**: Aggregated visa data records Ukrainian citizens as visa-exempt for Albania for **90 days within any 180-day period**. The Albanian MFA visa-regime page was reachable only behind an Incapsula/WAF shell in this pass, so this remains a medium-confidence travel baseline, but it is sufficient for country screening: Albania can only be treated as short-entry plus ordinary residence, not as a protection-based settlement route. [src-164][src-165] Confidence: medium.
- **Temporary protection / Ukraine-specific protection (`vq-054` closure)**: A Ministry of Interior news URL about temporary protection for Ukrainian citizens exists but was WAF-protected, and no current 2026/2027 Albanian TP extension or ordinary-residence bridge was captured. Conservative operational baseline: do **not** plan Albania as an EU-style post-04 March 2027 TP bridge; before TP expiry, use the ordinary Type D / Unique Permit path if Albania is chosen, or choose another country. [src-165] Confidence: medium for the conservative baseline.
- **Long-stay structure**: Secondary 2025–2026 digital-nomad guides consistently describe Albania's route for remote workers as a Type D long-stay visa followed by a **Unique Permit** / residence authorization for people earning income from employers or clients outside Albania. [src-166][src-167] Confidence: medium.

#### Residence without local employer

- **Remote-worker / digital-nomad route (`vq-055` closure)**: Citizen Remote's 2026 guide says Albania does not use the formal label "Digital Nomad Visa"; remote workers use a Type D visa and Unique Permit for remote-work purposes. It describes the route for foreign nationals working remotely for companies/clients abroad, freelancing for foreign clients, or operating foreign businesses, and says local Albanian employment / serving the Albanian market needs separate authorization. For screening, this is enough to model Albania as a promising ordinary-residence route rather than a pure visitor bridge, but the exact official e-Albania / State Police checklist, fees, and law article should be rechecked before application. [src-167] Confidence: medium.
- **Income threshold**: The captured secondary sources conflict or use unclear conversions: Nomads Embassy says at least about **EUR 450/month** / **USD 9,800/year** and notes that spouse/dependents may increase the required amount; Citizen Remote says approximately **ALL 40,000/month** (~USD 500/month) while noting that higher stable income is preferred. For this couple's ~$3,000/month income, both secondary baselines look passable, so the income screen is not a core blocker; exact official couple/dependent threshold remains an application-prep check before filing. [src-166][src-167] Confidence: medium for budget fit, low-medium for exact threshold.
- **Documents / filing**: Secondary lists converge on passport, photos, proof of remote work or service contracts, proof of financial means / bank statements, Albanian accommodation, Albanian bank account, clean criminal-record certificate, and valid health insurance. Nomads Embassy adds that government-issued documents should be apostilled and that documents may be submitted in English or Albanian. [src-166][src-167] Confidence: medium pending official checklist.
- **Duration and renewals**: Nomads Embassy describes an initial 1-year permit, renewable up to 5 years, followed by possible permanent residence; Citizen Remote describes up to 1 year and annual renewal if requirements remain met. Treat the 1-year renewable baseline as usable; verify the 5-year/PR path in official law before relying on it. [src-166][src-167] Confidence: medium.

#### Family / partner route

- Secondary sources say main applicants can include immediate family members / spouse and dependents, with higher financial support potentially required. They do not establish unmarried-partner recognition. Conservative planning baseline for this couple: marry before relying on dependent status, or have the second partner qualify independently. [src-166][src-167] Confidence: medium.

#### Polish karta pobytu interaction

- Albania is outside the EU/Schengen residence-permit framework. A Polish `karta pobytu` may help travel logistics and lawful-residence history, but it does not substitute for Albanian entry or residence authorization. If the Polish status is EU temporary protection, it does not create an Albanian protection status. Confidence: medium.

#### PR and citizenship

- Secondary sources suggest the remote-worker / Unique Permit can be renewed for several years and may lead to permanent residence, but no official article-level PR clock or citizenship rule was captured. Do not score Albania as a long-term settlement route until the Law on Foreigners / State Police guidance is extracted. [src-166][src-167] Confidence: low-medium.

#### Personal playbook for our couple

1. Treat Albania as easy-entry / exploratory on a 90/180-style baseline until official visa-regime pages are captured; do not rely on any Ukraine-specific TP bridge after 04 March 2027.
2. For the male IT worker, verify the official Type D + Unique Permit remote-worker checklist before committing: foreign-client contracts, income proof, bank statements, Albanian bank account, accommodation, police certificate, insurance, apostilles/translations, and fees.
3. The ~$3,000/month budget appears above secondary income thresholds; re-check exact couple/dependent threshold from official e-Albania / State Police material before filing, but do not treat threshold capture as a screening blocker.
4. For the woman, use marriage as the conservative dependent-status baseline; unmarried-partner treatment remains unconfirmed.
5. Before considering Albania a settlement candidate, verify whether the chosen permit counts toward PR/citizenship and what absences / renewals break the clock.

### 5.2. Climate {status: deep, depth: 1, last_updated: 2026-06-02, dod: passed}

> **DoD status**: passed at medium confidence. Three-city temperature, rain, humidity/comfort, sunshine-hour baselines, and clearer-sky day-equivalent proxies are captured.

| City | January | July/August | Sunshine / rain | Comfort notes |
|---|---:|---:|---|---|
| Tirana | Jan mean 7.1 C | Jul mean 25.3 C; Aug mean 25.5 C; summer heat records above 40 C | ~2,545 sunshine hours/year; ~1,345 mm rain/year over ~98 rain days | Mediterranean but inland: mild/rainy winter, hot sunny summer, occasional winter cold winds and severe summer heat. [src-168] |
| Durrës | Jan mean 8.4 C | Jul mean 26.9 C; Aug mean 27.6 C | ~2,695 sunshine hours/year; ~1,125 mm rain/year over ~117 rain days; sea ~24–25 C in Jul/Aug | Coastal and sunny, but still hot in summer and rainy in winter/autumn. [src-169] |
| Vlorë | Jan mean 8.9 C | Jul mean 26.3 C; Aug mean 26.6 C | ~2,670 sunshine hours/year; ~1,075 mm rain/year over ~120 rain days; sea ~24.5–25 C in Jul/Aug | Southern coast gives warm winters and strong summer beach climate, with autumn/winter rainfall and occasional extreme heat. [src-170] |

**Sunny/clear-day proxy verification**: WeatherSpark country and city cloud-cover pages provide monthly percentages in the broader clearer-sky categories (clear, mostly clear, or partly cloudy). Converted by month length, the medium-confidence clearer-sky day-equivalent proxies are: Tirana ~225 days/year, Durrës ~233 days/year, and Vlorë ~237 days/year. These are not official meteorological sunny-day counts, but they are enough to close the §5.2 sunny-day blocker for planning. [src-188]

**Climate verdict for first pass**: Albania is a strong warm-climate candidate for the couple: coastal Durrës/Vlorë are mild in winter and sunny in summer, while Tirana is practical but hotter inland. The main comfort caveats are hot summer peaks and wet autumn/winter periods rather than a long cold winter. [src-168][src-169][src-170][src-188]

### 5.3. Taxes {status: partial, depth: 1, last_updated: 2026-06-10, dod: partial}

> **DoD status**: Partial. This is a conservative first-pass screening model for a Ukrainian foreign-client IT worker at about USD 3,000/month. It captures tax residence, the self-employed PIT screen, minimum self-employed social/health contributions, filing deadlines, VAT threshold, marriage/dependent-child notes, and a worked gross-to-net example. It is **not** DoD-passed until an Albanian accountant / General Directorate of Taxes / National Business Center check confirms the exact IT activity code, contribution base, VAT / place-of-supply treatment for foreign clients, and compatibility with the Type D + Unique Permit remote-worker file.

#### Tax residence and scope
- Albania taxes residents on worldwide income and non-residents only on Albanian-source income. An individual is Albanian tax resident if they have a permanent home in Albania or stay in Albania for more than 183 days in a calendar year; the tax year is the calendar year. [src-407][src-408] Confidence: medium-high.
- For a couple relocating under an ordinary residence strategy, assume the working partner can become Albanian tax resident once living there full-time. Do not assume foreign-client income is outside the Albanian tax base after tax residence begins. [src-407][src-408] Confidence: medium-high.

#### Applicable self-employed / small-business model
- PwC's 2026 Albania summary says net taxable business income of commercial individuals and the self-employed is generally taxed at 15% up to ALL 14 million and 23% above ALL 14 million, but also notes that for commercial individuals and self-employed persons with annual gross income up to ALL 14 million, the PIT rate is **0% until 31 December 2029**. The couple's USD 3,000/month at the run-083 FX snapshot is about ALL 247,630/month or ALL 2.97m/year, well below ALL 14m. [src-407][src-412] Confidence: medium-high.
- Natural persons / individual traders / self-employed individuals with annual turnover up to ALL 10m may choose a special regime with automatic business-expense deductions depending on activity, locked for three years once chosen. This is likely relevant only if the 0% small-business PIT sunset ends or if an accountant recommends a specific expense model; do not rely on the exact deduction percentage until the IT activity category is mapped. [src-407] Confidence: medium-high.
- Social/health contributions are still material: PwC reports that self-employed persons (excluding agriculture) must pay for themselves mandatory social insurance of no less than 23% of the monthly minimum salary of ALL 50,000, plus health insurance of 3.4% on no less than double the minimum salary (ALL 100,000). Minimum modeled contribution: ALL 11,500 social + ALL 3,400 health = ALL 14,900/month. The wording is a minimum, so accountant confirmation is needed before treating this as the final contribution base for a high-earning IT freelancer. [src-409] Confidence: medium-high.

#### VAT, registration, and filing mechanics
- VAT: PwC's corporate VAT summary gives a 20% standard VAT rate and says a taxable person is not required to register when annual turnover does not exceed ALL 10m, although voluntary registration is possible. At about ALL 2.97m/year, the current income is below that threshold. However, foreign-client B2B place-of-supply / export-service treatment was not verified for the Albanian individual entrepreneur model, so VAT / reverse-charge handling remains an application-prep check. [src-410] Confidence: medium-high for threshold, medium for foreign-client fit.
- Registration cost: PwC records a business-entity registration fee of ALL 120, reduced to ALL 0 if registration is made online. This supports a low state-fee baseline, but the exact National Business Center / e-Albania flow for a foreign self-employed IT worker still needs official extraction because those sites were WAF-blocked in this pass. [src-410] Confidence: medium.
- Filing: tax resident individuals with worldwide income and every natural person carrying out self-employed or trader economic activity must submit the annual return by 31 March following the tax year. Monthly tax payment / declaration mechanics use the 20th day of the month after income is received; payroll/social-health reporting is electronic by the 20th day of the following month. [src-408][src-409] Confidence: medium-high.

#### Deductions, incentives, and family effects
- PwC lists no significant individual tax credits or incentives beyond foreign-tax relief / treaty mechanics. Albania has DTTs with many countries, but Ukraine is not listed in the captured treaty table. [src-411] Confidence: medium-high.
- Social and health contributions and voluntary pension contributions are deductible for taxable-income calculation. From 2025, personal yearly allowances for employment/business income are ALL 600,000 up to ALL 600,000 annual income, ALL 420,000 above ALL 600,000 to ALL 720,000, and ALL 360,000 above ALL 720,000. These allowances are not material to the 0% small-business PIT screen but may matter after the 2029 sunset or in an employment-style fallback. [src-409] Confidence: medium-high.
- Marriage / partner effect: captured sources do not show joint filing as a major tax advantage. Child-related deductions exist later (ALL 48,000 per dependent child under 18 and ALL 100,000/year for children's education under income conditions), but there is no current child in the scenario. [src-409] Confidence: medium-high.

#### Worked USD 3,000/month example (run-083 FX)
- FX snapshot: ExchangeRate-API reported USD 1 = ALL 82.543185 on 2026-06-09. USD 3,000/month = about **ALL 247,630/month** and **ALL 2,971,555/year**. [src-412]
- Screening model if the self-employed small-business 0% PIT regime applies and only minimum self-employed contributions are due:
  - Gross receipts: ALL 247,630/month.
  - PIT: ALL 0/month while annual gross stays below ALL 14m and the 0% regime remains in force through 31 Dec 2029.
  - Minimum modeled self-employed contributions: ALL 14,900/month.
  - Net before accountant, banking, VAT administration, insurance, and immigration costs: **about ALL 232,730/month**, or **about USD 2,819/month** at the run-083 FX snapshot.
- Downside / sensitivity (`vq-106` closure): if an accountant or authority requires contributions on a higher base, if the route is treated differently for foreign-client IT, or after the 0% PIT sunset, net can be lower. For country screening, the existing §5.3 model is sufficient: use the 0% PIT plus minimum-contribution scenario only as a favorable partial baseline, preserve the contribution-base / VAT / immigration-compatibility caveats, and do not score it as a final low-tax answer until accountant / General Directorate of Taxes / National Business Center confirmation. The exact activity-code, contribution-base, VAT/place-of-supply, and Unique Permit fit are application-prep checks, not an open screening blocker. [src-407][src-409][src-410][src-412]

#### Practical tax playbook for the couple
1. Before relocating, get accountant confirmation that foreign-client software / IT services can be registered as a self-employed / individual-trader activity compatible with the Type D + Unique Permit file.
2. Confirm whether the 0% PIT small-business regime applies to the exact activity and foreign-client contract structure, and calendar the 31 Dec 2029 sunset as a medium-term risk.
3. Confirm the mandatory contribution base: minimum ALL 14,900/month is the screening model, not a final filing instruction.
4. Confirm VAT / place-of-supply treatment for foreign B2B clients and whether voluntary VAT registration is useful or harmful below the ALL 10m threshold.
5. Budget for accountant support even though state registration fees look low, because the main risk is classification / reporting rather than the headline PIT rate.

### 5.4. Cost of living {status: deep, depth: 1, last_updated: 2026-06-13, dod: passed}

> **DoD status**: passed at medium confidence for first-pass screening. Livingcost gives comparable 2026 national and city baselines for total costs, rent/utilities, food, transport, utilities, and internet. It is still a commercial/statistical screen, not a live lease or grocery basket quote.

| Location | Livingcost monthly baseline | What it implies for the couple |
|---|---:|---|
| Albania national | $1,037/month for one person with rent; $2,429/month for a family-of-four proxy; rent/utilities $467 one person / $738 family; food $390 / $1,034; transport $83 / $241. [src-541] | A two-adult couple should be below the family-of-four proxy if housing is controlled, so Albania screens as workable against both $3,000 gross income and the favorable §5.3 tax-screen net of about $2,819/month. |
| Tirana | $1,256/month one-person total; $2,960 family-of-four proxy; rent/utilities $600 one person / $991 family; food $434 / $1,148; transport $112 / $325. [src-542] | Best administrative/services base, but the family proxy nearly equals gross income and exceeds the §5.3 favorable net, so Tirana needs a strict apartment budget and no assumption of family-of-four spending. |
| Durrës | $940/month one-person total; $2,189 family-of-four proxy; rent/utilities $415 one person / $673 family; food $390 / $1,009; transport $53 / $154. [src-543] | Strong coastal cost screen: materially cheaper than Tirana while still close to the capital. Seasonal and lease-quality checks remain later work. |
| Vlorë | $893/month one-person total; $1,983 family-of-four proxy; rent/utilities $394 one person / $525 family; food $354 / $939; transport $62 / $180. [src-544] | Warm southern-coast affordability screen; lower total costs make it attractive if legal/accountant and healthcare/service access checks are acceptable. |

**Budget verdict**: Albania is one of the more comfortable budget screens at this stage. On the favorable current tax model (about USD 2,819/month before accountant, VAT administration, insurance, and immigration costs), Durrës and Vlorë leave meaningful monthly room, while Tirana is still possible but should be treated as the services-first / rent-controlled option. [src-541][src-542][src-543][src-544]

### 5.5. Rent {status: deep, depth: 1, last_updated: 2026-06-13, dod: passed}

> **DoD status**: passed at medium confidence for first-pass screening. Livingcost's 40 m2 1BR line is used as the modest two-room proxy, and the 80 m2 3BR line is only an upper-size / future-family stress test. Live listings, deposits, agency fees, registered-lease support, and seasonal coastal lease conditions remain later practical checks.

| Location | 40 m2 1BR proxy | 80 m2 3BR stress test | Rent share and notes |
|---|---:|---:|---|
| Albania national | $351 cheap / $536 city-center | $580 cheap / $838 city-center | 40 m2 proxy is about 12%-18% of $3,000 gross, or about 12%-19% of the favorable §5.3 net. [src-541] |
| Tirana | $449 cheap / $703 city-center | $757 cheap / $1,205 city-center | 40 m2 proxy is about 15%-23% of gross and about 16%-25% of favorable net; the 3BR stress test can consume 27%-43% of favorable net. Flag Tirana as the rent-pressure city. [src-542] |
| Durrës | $322 cheap / $449 city-center | $584 cheap / $561 city-center | 40 m2 proxy is about 11%-15% of gross and favorable net; the coastal city screens as affordable but needs seasonality and landlord-registration checks. [src-543] |
| Vlorë | $326 cheap / $378 city-center | $416 cheap / $582 city-center | 40 m2 proxy is about 11%-13% of gross and 12%-13% of favorable net; strongest warm-coast rent screen, pending live listing quality and services checks. [src-544] |

**How to search later**: For a filing-ready pass, check MerrJep / local real-estate agencies, Facebook groups, and Albanian property portals for 12-month leases, registered address support, deposit norms, agency commission, utilities, and whether landlords accept foreign remote-worker documentation. This run deliberately uses Livingcost only for first-pass comparability.

**Rent verdict**: Screen Durrës first for the balance of affordability, capital proximity, and coast; Vlorë second for the warm-coast / lower-rent case; Tirana only with a strict housing cap or if bureaucracy, healthcare, and community access outweigh the rent premium. Add `tirana-rent-pressure` as a risk flag.

### 5.6. Healthcare {status: partial, depth: 1, last_updated: 2026-06-18, dod: partial}

> **DoD status**: Partial. This pass gives a screenable healthcare baseline from public-system and private-sector sources. Run-148 resolves `vq-139` for screening; route-compliant private insurance, maternity/newborn exclusions, foreign-resident public-insurance onboarding, and city-specific private-care prices remain application-prep checks.

- **System structure**: U.S. ITA's Albania medical-equipment guide says Albania's healthcare system still focuses predominantly on public hospitals and public health services, while private healthcare has become increasingly popular. The Ministry of Health and Social Protection leads the public sector, develops policy and budget proposals, and monitors state-owned health institutions. [src-680] Confidence: medium.
- **Insurance/public-fund baseline**: The same source describes the Compulsory Healthcare Insurance Fund as based on payroll contributions and government subsidy, with patients relying on it for reimbursement of prescription pharmaceuticals and approved services by private secondary/tertiary providers. This is enough to know that public coverage is contribution/status-dependent, not an automatic expat benefit; the exact onboarding path for a remote-worker / Unique Permit resident remains unverified. [src-680] Confidence: medium.
- **Capacity and city choice**: ITA lists 22 district hospitals, 11 regional hospitals, four university hospitals, one trauma university center, two psychiatric hospitals, and a National Centre on Child Development and Rehabilitation; it also notes four major private hospitals in Tirana (American, Hygeia, German, and Salus) plus smaller hospitals/clinics. For the couple, Tirana is the safest healthcare-practicality base; Durres/Vlore are cheaper coastal screens but should be checked against emergency access, maternity, pediatrics, and specialist availability. [src-680] Confidence: medium.
- **Budget implication**: Do not assume the captured favorable Albania tax/cost screen is enough until private health-insurance premiums and exclusions are quoted. Secondary immigration-route lists already require health insurance for the residence file, so model a private policy as a mandatory relocation cost until an adviser confirms public-fund access by status. [src-166][src-680] Confidence: medium.

**Healthcare verdict**: Albania is screenable but not yet application-ready. Use Tirana for any healthcare-dependent scenario, and keep coastal Durres/Vlore as budget/lifestyle options only after private insurance, maternity/newborn coverage, pediatric access, and emergency-care logistics are checked. [src-680]

### 5.7. Education (future child) {status: deep, depth: 1, last_updated: 2026-06-18, dod: passed}

> **DoD status**: passed at medium-high confidence for first-pass family screening. Public/private school structure, preschool age bands, compulsory education, and one English-language international-school option are captured. Run-148 resolves `vq-140` for screening; exact international tuition and private-preschool quotes remain application-prep budget checks, not a blocker for section completion.

- **Governance and public/private baseline**: Eurydice's Albania overview says education is provided by both public and private institutions at all levels. The Ministry of Education is responsible for pre-university and higher education, while the Ministry of Finance shares vocational-education responsibilities. [src-681] Confidence: medium-high.
- **Compulsory school structure**: Eurydice records obligatory education from ages 6 to 16, including basic education and lower secondary education. Basic education starts at age 6, lower secondary covers classes VI-IX, and upper secondary education is optional from about age 16. For a future child, the default low-cost plan is Albanian-language public schooling unless the family budgets for private/international education. [src-681] Confidence: medium-high.
- **Preschool / childcare**: Eurydice's ECEC page says preschool education is attended by children aged 3-6; nurseries cover ages 0-3 and kindergartens ages 3-5. ECEC is not obligatory. Public and private nurseries charge fees; full-day public kindergarten fees are set locally, while half-day public kindergartens are free of charge. [src-682] Confidence: medium-high.
- **International-school option**: Tirana International School (QSI) is a concrete English-language option in Tirana. Its admissions page says it accepts students with no previous English from preschool through age 13 / U.S. grade 8, while secondary students must show increasing English proficiency; its preschool page says it accepts children from age 2 and teaches subjects in English. Its secondary page says the program prepares students for colleges/universities in the United States or globally and includes AP / IB-linked course offerings. [src-683] Confidence: medium.
- **Budget caveat**: This pass did not capture current TIS tuition or comparable private-preschool quotes. Because Albania's ordinary budget advantage depends on one income, international schooling should be treated as a major optional cost until a fee schedule or admissions quote is obtained. [src-683] Confidence: medium.

**Education verdict**: Albania is usable for a future child if the family accepts Albanian-language public education and local preschool logistics. If English-language schooling is required, the practical base is Tirana and the budget remains unresolved until TIS / private-preschool tuition quotes are captured. [src-681][src-682][src-683]

### 5.8. Comfort of life {status: deep, depth: 1, last_updated: 2026-06-23, dod: passed}

> **DoD status**: passed at medium confidence for screening. Safety, English/language friction, transport, city-comfort tradeoffs, and everyday adaptation baselines are captured; this is not a final neighborhood-by-neighborhood relocation guide.

- **Safety baseline**: WPR's safety table places Albania at a 2025 Global Peace Index score of **1.812** and TravelSafe gives Albania a **75 / Low risk** safety index. TravelSafe describes Albania as generally safe with friendly locals and low overall, transport/taxi, pickpocket, mugging, terrorism, and women-traveler risks; it keeps scams and natural disasters at medium risk. For screening, Albania is comfort-usable, but normal urban caution still applies in Tirana and tourist/coastal areas. [src-777] Confidence: medium.
- **Transport and road risk**: Both TravelSafe and Expat Arrivals warn that transport is a real friction point: public transport can be unreliable, drivers can be aggressive, road maintenance/signage can be weak, and defensive driving is advised. For the couple, this pushes the practical base toward Tirana or well-connected coastal areas rather than remote towns unless they are comfortable driving locally. [src-777][src-778] Confidence: medium.
- **English / language adaptation**: EF EPI ranks Albania **#42** with score **532**, and lists Tirana at **557**. This is usable for private services and some expat-facing businesses, but the main language remains Albanian; leases, public offices, healthcare administration, tax/accountant work, school interactions, and local transport will still need Albanian-speaking help or paid professionals. [src-778] Confidence: medium.
- **Expat / daily-life baseline**: Expat Arrivals describes Albania as not yet a major expat hotspot but attractive for lower costs, beaches, sunny weather, and foreign-currency income. It also says private healthcare and international schooling are likely the largest expat-specific costs, and that Tirana is the most expensive but strongest services base. [src-778] Confidence: medium.
- **City comfort screen**: Tirana is the default administration, healthcare, accountant, private-school, and English-service base but has the highest rent/cost pressure. Durres is the first coast-plus-capital-access compromise. Vlore is the warm-coast / lower-rent option, but it needs healthcare, school, lease seasonality, and bureaucratic-access checks before becoming the default base. [src-542][src-543][src-544][src-680][src-683] Confidence: medium.

**Comfort verdict**: Albania is a good warm-climate, moderate-safety, lower-cost comfort screen, especially for a couple earning in USD/EUR. The practical downsides are not climate or headline crime; they are language friction, road/transport quality, official-page capture gaps, private healthcare/insurance dependence, and the need to keep Tirana access even if living on the coast. [src-777][src-778]

### 5.9. Partner (student) {status: deep, depth: 1, last_updated: 2026-06-23, dod: passed}

> **DoD status**: passed at medium confidence for screening. The section now gives a conservative dependent/independent-status baseline, remote-study fit, work-right caution, income/budget screen, and one-income playbook. Exact official dependent checklist and PR-counting remain application-prep / later legal-route work.

- **Dependent / family status**: Existing Albania route evidence says spouse / immediate family can be included, but it does not establish unmarried-partner recognition. Conservative baseline for this couple: marry before relying on the woman being included as a dependent, or have her qualify independently under another Albanian status. [src-166][src-167] Confidence: medium.
- **Remote Ukrainian study**: Nothing captured suggests that continuing a Ukrainian university remotely conflicts with Albania's ordinary residence planning. However, remote Ukrainian study is not itself a captured Albanian residence basis. Treat it as compatible life logistics, not as a legal-status anchor. Confidence: medium.
- **Work rights for the partner**: The remote-worker / Unique Permit material was captured around the principal foreign-client worker, not a spouse's local employment rights. Until the official dependent permit terms are extracted, assume the partner should not rely on Albanian local work rights without separate authorization; future remote foreign-client work may require her own tax/residence advice. [src-166][src-167] Confidence: medium.
- **Income / one-income fit**: The USD 3,000/month gross income appears comfortably above the secondary remote-worker thresholds captured earlier, and the favorable tax screen leaves about USD 2,819/month before accountant, VAT administration, insurance, and immigration costs. Durrës and Vlorë fit this one-income screen better than Tirana; Tirana remains the services-first option but can become tight once private insurance, accountant support, international schooling, and route/legal costs are added. [src-166][src-167][src-412][src-541][src-542][src-543][src-544] Confidence: medium.
- **Family/future child fit**: Albania can work if the family accepts Albanian-language public education and budgets for private healthcare. If English-language schooling or complex healthcare is required, Tirana becomes the practical base and the budget advantage narrows sharply. [src-680][src-681][src-682][src-683][src-778] Confidence: medium.
- **Practical sequence**: First, verify official Type D + Unique Permit dependent mechanics and whether marriage is required. Second, keep the partner's Ukrainian study documentation but do not use it as the residence anchor. Third, model the working partner as the sponsor and preserve a monthly buffer for insurance/accounting/immigration costs. Fourth, if the partner later works, run a separate Albania tax/residence check before invoicing or accepting local work.

**Partner verdict**: Albania is plausible for the student partner if the couple is willing to marry for dependent status and keep the male IT worker as the sponsor. It is not yet proven for an unmarried partner, and the one-income plan depends on preserving the favorable remote-worker/tax assumptions through official checklist and accountant checks. [src-166][src-167][src-778]

### 5.10. Risk dimensions {status: deep, depth: 1, last_updated: 2026-06-25, dod: passed}

> **DoD status**: passed for screening. Covered: currency/banking, political/Ukraine-posture, ties to Ukraine, and diaspora/language adaptation. Exact bank onboarding, official route-page capture, active Ukrainian community contacts, and final-city travel-cost checks remain application-prep.

- **Currency / banking risk**: Medium. Albania uses ALL while the couple earns in USD/EUR, and the current favorable tax screen relies on the self-employed / commercial-individual regime and its 31 Dec 2029 sunset. Headline costs and coastal rents are attractive, but banking, VAT/place-of-supply, contribution-base, and residence-permit fit should be confirmed before relying on the high net estimate. [src-407][src-412][src-542][src-543][src-544]
- **Political / Ukraine-posture risk**: Medium. Albania is outside the EU TP system; no current Ukraine protection bridge was captured, and several official-primary route pages were WAF-blocked or unreachable. The operational answer is ordinary Type D / Unique Permit planning, not protection continuity. [src-164][src-166][src-167]
- **Ties to Ukraine**: Medium. Albania is regionally closer than Iberia/Latin America/Asia and has Adriatic/Balkan travel logic, but it is not EU/Schengen continuity and coastal cities may require extra airport/route planning for repeated family or university travel. [src-542][src-543][src-544]
- **Diaspora / adaptation**: Medium. Safety and warm-climate comfort screen positively, and EF places Albania in a usable English band, but Albanian remains necessary for public offices, leases, healthcare, tax/accountants, schools, and transport. Tirana is the practical service hub; Durres/Vlore need stronger support checks before becoming the default base. [src-777][src-778]

### 5.11. Bureaucracy and practicality {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

## Block 4 — Risk dimensions (summary)

| Category | Level | Rationale |
|---|---|---|
| Currency / banking | medium | ALL exposure is manageable on USD/EUR income, but the favorable tax screen depends on regime fit, contribution/VAT details, banking, and the 2029 PIT sunset. [src-407][src-412][src-542][src-543][src-544] |
| Political | medium | No EU-TP continuity or captured Ukraine bridge; route-page capture gaps mean the ordinary Type D / Unique Permit file needs official confirmation before filing. [src-164][src-166][src-167] |
| Ties to Ukraine | medium | Balkan proximity helps, but Albania is not EU/Schengen continuity and coastal bases need airport/travel-cost checks. [src-542][src-543][src-544] |
| Diaspora / adaptation | medium | Tirana has the strongest service layer and English is usable, but Albanian-language, road/transport, healthcare, school, and tax support are still needed. [src-777][src-778] |

## Block 5 — Practical verdict

- **Can relocate now**: likely yes for short entry if the 90/180 visa-free rule is confirmed from the official MFA / e-visa page; not yet a full residence plan.
- **Best legalization path for the man**: Type D + Unique Permit remote-worker route as a promising ordinary-residence path; exact official checklist/fees remain pre-filing checks.
- **Best legalization path for the woman**: likely dependent after marriage if family inclusion is confirmed; unmarried partner route not confirmed.
- **Does marriage change the picture**: likely yes; use marriage as the conservative baseline.
- **Realism of staying after 03.2027**: medium/uncertain; Albania may offer renewable ordinary residence, but no Ukraine-specific TP bridge was captured and PR-counting needs a later deep-dive.
- **Budget/rent first pass**: workable. Durrës and Vlorë screen as the better one-income cost/rent fits; Tirana is still possible for services/bureaucracy but needs a strict rent cap. [src-542][src-543][src-544]
- **Healthcare/education first pass**: healthcare and English-language education both pull the practical default back toward Tirana. Use Tirana first for medical access and international-school optionality; use Durrës/Vlorë only if private insurance, emergency logistics, and school/preschool plans are confirmed. [src-680][src-683]
- **Comfort/partner first pass**: Albania is screenable for everyday life: low/medium safety proxies, warm climate, moderate English in Tirana, and lower coastal costs help. Marriage remains the conservative dependent baseline, while the main stressors are Albanian-language administration, road/transport quality, private healthcare/insurance, and Tirana service-cost pressure. [src-777][src-778]

**Pros**:
- Warm Mediterranean climate with mild coastal winters.
- Secondary evidence suggests a remote-worker residence path fitting foreign-client IT work.
- Current income appears comfortably above secondary income thresholds.
- Durrës and Vlorë rent/cost baselines leave more budget room than Tirana in the first-pass screen.
- Safety and English-proficiency proxies are usable for screening, especially around Tirana and major coastal cities. [src-777][src-778]

**Cons / risks**:
- Key official Albanian government pages were WAF-blocked or unreachable in this pass.
- Exact route category, checklist, fees, and dependent mechanics need primary-source verification.
- No captured Ukraine-specific post-2027 protection bridge.
- Direct sunny/clear-day counts were replaced by WeatherSpark clearer-sky proxies for screening in run-061; official meteorological sunny-day counts remain optional later evidence.
- Route-compliant private health-insurance quotes and exact foreign-resident public-insurance onboarding are not captured.
- English-language/international schooling exists in Tirana, but current tuition and private-preschool city prices were not captured.
- Albanian-language help is still needed for public offices, leases, healthcare administration, taxes, and school interactions.
- Road safety, unreliable public transport, and scam/natural-disaster caveats require city/neighborhood due diligence. [src-777][src-778]

## Block 6 — Practical playbook (working relocation guide)

### 6a. Before the move (what to prepare in Ukraine / Poland)
- Documents: passports, passport photos, foreign employment/service contracts, proof of remote income, 6–12 months of bank statements, criminal-record certificates, health-insurance certificate valid in Albania, accommodation booking/lease, and civil-status documents if using marriage.
- Apostille / translation: secondary sources say government-issued documents should be apostilled and may be submitted in English or Albanian; verify official translation rules before filing. [src-166]
- What to do with the Polish karta pobytu: keep it as a separate Polish/EU status; do not treat it as Albanian residence.

### 6b. First month after arrival
- Confirm lawful-stay deadline and whether Type D filing must be initiated abroad or can be handled after entry.
- Open/prepare an Albanian bank account only after checking the current official filing sequence.
- Avoid local Albanian employment or Albanian-market services until permit/tax authorization is clear.
- If using dependent status, treat marriage as the conservative baseline until the official family/dependent checklist confirms otherwise.
- Choose an initial base near Tirana or a well-connected coastal city; do not optimize only for rent before checking healthcare, transport, and filing logistics.

### 6c. First 3–6 months
- Build the Unique Permit file with foreign-client income evidence and health insurance.
- Decide whether marriage is needed for the partner's dependent status.
- Start a tax pass before invoicing through Albania; tax residency may arise after relocation.

### 6d. Before March 2027 (critical deadline)
- Albania is not an EU TP continuation plan. If moving from an EU TP status, have an Albanian ordinary residence strategy active before relying on Albania long-term.

### 6e. Long-term (3–7 years)
- Verify the permanent-residence clock and whether remote-worker Unique Permit time counts before treating Albania as a settlement destination.

### 6f. Relocation budget (one-time costs)

| Item | USD / EUR | Notes |
|---|---:|---|
| Visa / residence permit fees | — | Official fee schedule required. |
| Apostilles and translations | — | Checklist verification required. |
| Flights for two | — | TBD |
| Rental deposit | $326-$703+ | Use at least 1 month of the captured 40 m2 proxy as a first-pass reserve; exact deposit/agency norms need live-listing checks. [src-542][src-543][src-544] |
| First month rent | $326-$703 | Durrës/Vlorë lower end, Tirana higher end for the 40 m2 proxy. [src-542][src-543][src-544] |
| Health insurance (one year) | — | Required in secondary route lists; quote two-adult private policies and maternity/newborn exclusions before filing. [src-166][src-680] |
| International/private school reserve | — | Public school can be low-cost, but English-language TIS/private preschool tuition is not captured and should be quoted before assuming family affordability. [src-681][src-682][src-683] |
| Immigration lawyer fees | — | Bureaucracy pass required. |
| Buffer / contingencies | — | Important because official route capture is incomplete. |
| **Total** | — | |

### 6g. Contact points and communities
- Official visa-regime / Ministry pages: attempted but WAF-protected in this pass. [src-165]
- e-Albania / e-visa / State Police Unique Permit sources: need future extraction.
- Immigration lawyers and Ukrainian/Russian-speaking communities: TBD.

## Block 7 — Sources

### 7a. Official primary
- [src-165] Albanian MFA / Ministry pages attempted for visa regime and Ukraine temporary-protection anchor, but content capture was blocked.

### 7b. Reputable secondary
- [src-166] Nomads Embassy — Albania Digital Nomad Visa / Unique Permit guide.
- [src-167] Citizen Remote — Albania Digital Nomad Visa 2026 guide.
- [src-680] U.S. International Trade Administration — Albania Medical Equipment / healthcare-system guide.

### 7c. Community and forums (mandatory date of original post)
_(none yet)_

### 7d. Statistical / commercial
- [src-681] Eurydice — Albania education-system overview.
- [src-682] Eurydice — Albania early childhood education and care.
- [src-683] Tirana International School (QSI) — admissions / preschool / secondary-school pages.
- [src-778] EF English Proficiency Index Albania / Expat Arrivals moving-to-Albania adaptation overview.
- [src-164] Wikipedia visa-requirements table for Ukrainian citizens (aggregator entry baseline).
- [src-168] Climate to Travel — Tirana.
- [src-169] Climate to Travel — Durrës.
- [src-170] Climate to Travel — Vlorë.
- [src-188] WeatherSpark — Albania country and Vlorë city cloud-cover pages.
- [src-541] Livingcost — Albania national cost-of-living baseline.
- [src-542] Livingcost — Tirana cost/rent baseline.
- [src-543] Livingcost — Durrës cost/rent baseline.
- [src-544] Livingcost — Vlorë cost/rent baseline.
- [src-777] World Population Review / TravelSafe Albania safety proxies.

### 7e. Not found
- Albanian accountant / General Directorate of Taxes / National Business Center confirmation of the exact foreign-client IT self-employed activity code, mandatory contribution base, VAT/place-of-supply handling, and immigration-status compatibility for the Type D + Unique Permit route remains an application-prep check; `vq-106` is closed for screening.
- Clean official-primary extraction of Albania's current visa regime for Ukrainian citizens remains useful before travel, but `vq-054` is closed for screening.
- Current official Ukraine temporary-protection extension / post-2027 bridge page remains uncaptured; safe baseline is no reliance on a TP bridge.
- Official e-Albania / State Police / law-text page for the Type D + Unique Permit remote-worker checklist, fees, exact income threshold, dependent mechanics, and PR-counting rules remains a pre-filing / later deep-dive item; `vq-055` is closed for screening because the route is promising but not yet fully application-ready.
- Official meteorological sunny-day counts for Tirana, Durrës, and Vlorë; WeatherSpark clearer-sky proxies are now sufficient for planning but not official statistics.
- `vq-139`: resolved in run-148 for screening; private health-insurance quotes, maternity/newborn coverage, public-insurance onboarding by residence route, and Tirana/Durres/Vlore private-care prices remain application-prep checks.
- `vq-140`: resolved in run-148 for screening; Tirana International School tuition and private-preschool city quotes remain application-prep budget checks.
- Official dependent/partner checklist, dependent work-rights wording, and final city/neighborhood comfort checks remain application-prep items after the section 5.9 screening baseline.

## Block 8 — Open questions and verification markers

- `vq-055` resolved in run-061: Type D + Unique Permit remote-worker route remains a promising medium-confidence screening baseline; exact official checklist/fees/dependent/PR-counting mechanics are application-prep or later deep-dive checks, not current queue blockers. [src-166][src-167]
- `vq-106` resolved in run-087: Albania self-employed / individual-trader tax fit is closed for screening using the favorable 0% PIT plus minimum-contribution partial baseline; exact activity code, contribution base, VAT/place-of-supply, and Type D + Unique Permit compatibility remain application-prep checks.
- `vq-139` resolved in run-148 for screening: Albania healthcare is screenable, but route-compliant private insurance, maternity/newborn cover, exact foreign-resident public-fund onboarding, and city-specific private-care prices remain application-prep checks.
- `vq-140` resolved in run-148 for screening: Albania education is screenable through the public system plus Tirana International School as an English-language option, but exact international tuition/private-preschool quotes remain application-prep budget checks.
- Run-187 added comfort and partner screening baselines: Albania is usable for everyday life with language/transport caveats; marriage remains the conservative dependent route for the student partner. [src-777][src-778]
