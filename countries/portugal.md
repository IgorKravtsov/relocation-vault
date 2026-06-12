---
country: Portugal
tier: null
depth_score: 4.0
last_updated: 2026-06-12T01:00:47Z
sections_completed: ["5.4", "5.5"]
sections_partial: ["5.1","5.2","5.3","5.6"]
sections_pending: ["5.7","5.8","5.9","5.10","5.11"]
risk_flags: ["no-clear-post-2027-tp-bridge","climate-sunny-days-gap","d8-income-above-current-budget","lisbon-rent-pressure","portugal-self-employed-tax-burden","portugal-foreign-client-vat-fit-gap","portugal-health-insurance-quote-gap"]
sources_used: ["src-002","src-017","src-018","src-019","src-020","src-021","src-022","src-023","src-024","src-026","src-077","src-078","src-176","src-177","src-178","src-179","src-189","src-401","src-402","src-403","src-404","src-405","src-406","src-492","src-493","src-494","src-495","src-496"]
unverified_count: 2
schema_version: 2.0.0
---

# Portugal

> First research iteration for Portugal. All content in this file is in English per `vault-protocol.md`.

## Block 1 — Summary

- **Tier**: TBD after taxes, rent, healthcare, partner-path, and bureaucracy research are added.
- **depth_score**: 4.0
- **Last updated**: 2026-06-12T01:00:47Z
- **Tier rationale**: Portugal still looks strategically interesting because it combines a live temporary-protection framework with a known remote-work residence route and a warm Atlantic south, but the first pass surfaced two major constraints for this couple: no documented official post-04 March 2027 TP conversion bridge was captured in this iteration, and the D8 remote-work income threshold appears above the couple's current nominal monthly budget.

## Block 2 — Scoring

| Criterion | Score (1–10) | Confidence | Brief rationale | Profile section |
|---|---:|---|---|---|
| Legalization (now + post-03.2027) | 5 | medium | Portugal offers a real TP shelter path and a known D8 remote-work track, but the D8 threshold looks too high for the current household budget, the official-primary D8 checklist still needs capture, and no clean TP→ordinary-residence bridge for after 04 March 2027 was documented in this pass. | §5.1 |
| Climate | 8 | medium | Lisbon and especially Faro fit the warm-climate preference well, while Porto is cooler and much wetter; direct sunny-day counts still need a dedicated source. | §5.2 |
| Taxes | 4 | medium | Ordinary Portuguese self-employment at the current income is materially heavy: the conservative simplified-regime stress test leaves about EUR 1,862/month (USD 2,148) net if filed singly, or about EUR 1,949/month (USD 2,249) if joint taxation is available with no second income. Exact Article 151 activity mapping, VAT/place-of-supply, and immigration-status compatibility remain accountant/application-prep checks. | §5.3 |
| Cost of living | 6 | medium | A $3,000/month household can work in Porto/Faro with disciplined rent and no car-heavy lifestyle, but Lisbon leaves little buffer once rent is included. | §5.4 |
| Rent (decent 2BR) | 4 | medium | Current 2025-2026 T2 bands confirm Lisbon is rent-stressed, Porto is more workable, and Faro/Algarve is seasonal but possible with a year-round lease. | §5.5 |
| Healthcare | 7 | medium | Legal residents can register for an SNS user number and local health-centre access, TP holders already have NHS access via the Portugal Ukraine mechanism, and private care is available for faster/English-speaking access. Remaining gaps: official D8 visa insurance minimums and live insurer quotes for two young adults. | §5.6 |
| Education (future child) | — | N/A | [verification required] | §5.7 |
| Comfort of life | — | N/A | [verification required] | §5.8 |
| Fit for couple with single income | — | N/A | [verification required] | §5.9 |

**Weighted score**: — (compute when all criteria are scored)

## Block 3 — Profile by section

### 5.1. Legalization {status: partial, depth: 1, last_updated: 2026-05-25, dod: partial}

> **DoD status**: partial. Covered: Portugal's current TP shelter mechanism, the 04 March 2027 EU horizon, the existence and broad structure of the D8 remote-work route, the current naturalization rule change, the official post-visa AIMA filing route for remote workers, and the baseline planning answer for an existing Polish residence title. Missing for full DoD: a documented post-04 March 2027 TP conversion bridge into ordinary residence and a direct source for annual sunny-day counts.

#### Now (until 03.2027)

- Portugal's justice portal says Portugal set up a special programme to receive Ukrainian citizens that **does not require a visa**. [src-017]
- The same FAQ says that on arrival a special mechanism authorizes a residence permit called the **Temporary Protection Title**, with automatic assignment of **Social Security (NISS)** and **tax (NIF)** numbers plus access to the National Health System. [src-017]
- The FAQ states that temporary protection has an **initial duration of one year** and may be **extended by two six-month periods** while return-blocking conditions continue. [src-017]
- At EU level, temporary protection for displaced persons from Ukraine has been extended through **04 March 2027**. [src-002]
- Portugal's AIMA also published a country-specific notice confirming that temporary protection for people displaced from Ukraine was **extended until 2027**. [src-019]

#### After 4 March 2027

- Verification pass baseline: current sources confirm the EU/Portugal temporary-protection horizon through **04 March 2027**, but no Portuguese official-primary page captured so far explains a formal **TP-to-ordinary-residence transition mechanism** after that date. Treat this as the operational answer until AIMA/gov.pt publishes a bridge: TP should not be modeled as an automatic ordinary-residence off-ramp. [src-002][src-019]
- That gap matters more in Portugal than in Greece because the couple cannot safely assume TP time will auto-convert into a normal residence track. The prudent working assumption is that Portugal is safer only if the couple moves onto an ordinary status **before** the TP horizon becomes critical. [src-026]

#### Residence without local employer

- Portugal's D8 / digital-nomad-style remote-work route is described in current secondary guidance as a path for **non-EU remote workers earning active income from outside Portugal**. [src-020]
- Portugalist's 2026 deep-dive says the main applicant must show **at least four times the Portuguese minimum wage per month**, which it translates into **€3,680/month** in 2026, plus Portuguese administrative setup such as a **NIF**, Portuguese bank account, accommodation evidence, criminal-record certificate, and proof of remote-work authorization. [src-020]
- The same source says family applications require **higher income and savings**, plus marriage certificate or proof of cohabitation for unmarried partners. [src-020]
- Portugalist also distinguishes two products inside the remote-work framework: a **residence visa** for long-stay relocation and a **temporary-stay visa** for longer non-resident stays. The residence route is the one relevant to a genuine relocation plan. [src-020]
- Portugal's AIMA now provides an official-primary page for the **post-visa residence-authorization stage** for remote workers. It says the application is made **by appointment** (or via an electronic platform for residence-visa holders once implemented), is filed **in person** with AIMA, and must include a **valid passport**, a **valid residence visa for remote work**, a declaration from the foreign employer/client attesting the employment or service relationship, and **residence-address evidence** backed by ownership or landlord-host documentation. The same page says the temporary permit is valid for **two years**, renewable for **successive three-year periods**. [src-026]

#### PR and citizenship

- Portugal's justice ministry announced that, from **19 May 2026**, the minimum period of legal residence for naturalization became **seven years** for nationals of Portuguese-speaking countries or EU member states and **ten years** for nationals of other states. For this couple, Ukraine falls into the **ten-year** bucket. [src-021]
- The same official notice says naturalization now also requires sufficient knowledge of Portuguese culture, history, symbols, and civic duties, plus the ability to support oneself and the absence of serious criminal / terrorism-related bars. [src-021]
- This is a material downgrade versus older Portugal narratives built around a five-year citizenship story. The first-pass conclusion is therefore: **Portugal still has a path, but it is no longer a fast citizenship case for Ukrainians under the currently captured 2026 rule set.** [src-021]
- This iteration did not capture a primary-source page mapping the exact **permanent residence** step, nor whether time spent under temporary protection counts cleanly toward long-term residence calculations in the same way as an ordinary residence permit. [verification required; vq-008]

#### Personal playbook for our couple

1. **Portugal is attractive as a climate-and-structure candidate, but not yet as a clean low-income remote-worker solution.** The TP framework is real, and the D8 route exists, but the D8 threshold captured in this pass is materially high for the couple's current one-income budget. [src-017][src-020]
2. **Do not treat Portuguese TP as the long-term plan by itself.** This iteration found the current 2027 extension, but not a documented bridge from TP into ordinary residence after that horizon. [src-002][src-019][vq-008]
3. **If Portugal stays in the shortlist, the rational non-local-employer strategy is to verify whether the man can qualify for the residence-type D8 route with stronger income evidence, higher earnings, or later two-income support.** At the current budget level, that looks weak. [src-020]
4. **Marriage may help documentary clarity, but it does not solve the income problem.** The remote-work route appears family-aware, yet still requires higher financial proof for a spouse/partner. [src-020]
5. **A Polish residence title does not substitute for Portugal's own status.** Portugal's remote-work path is structured as a Portuguese residence visa followed by a Portuguese AIMA residence-authorization filing, so a Polish `karta pobytu` should be treated only as existing residence history, not as a replacement for Portuguese authorization. If the Polish status is temporary protection rather than ordinary residence, the couple should also assume the EU one-Member-State TP rule still governs that part of the plan. [src-002][src-026]
6. **Citizenship should be modeled on a slower horizon than older Portugal marketing suggests.** Under the captured official 2026 rule change, the relevant naturalization period is now ten years for non-EU, non-Lusophone nationals such as Ukrainians. [src-021]

### 5.2. Climate {status: partial, depth: 1, last_updated: 2026-05-27, dod: partial}

> **DoD status**: partial. Covered: January/July temperatures in 3 cities, humidity, sunshine-hours profile, direct annual sunshine-percentage for Lisbon and Porto, and practical comfort. Missing for full DoD: a direct source with annual **sunny-day counts** for Faro.

- **Lisbon** is warm and livable by the couple's standards: average **January mean 11.8°C** and **July mean 23.1°C**, with about **2,810 sunshine hours/year** and an annual **Percentage possible sunshine of 63%** (monthly range 51–81%). [src-022][src-077]
- **Porto** is the climate trade-off city: average **January mean 10.2°C** and **July mean 19.5°C**, with about **2,470 sunshine hours/year** and an annual **Percentage possible sunshine of 54%** (monthly range 40–68%), much more rain than Lisbon, and a cooler Atlantic feel. [src-023][src-078]
- **Faro / Algarve** is the strongest match for the couple's warmth preference: average **January mean 12.3°C** and **July mean 24.4°C**, plus about **3,045 sunshine hours/year**, making it one of the sunniest areas in Europe by this source's characterization. [src-024]
- Humidity is not trivial on the Atlantic side. Lisbon and Faro are humid but still feel workable because winters are mild; Porto combines humidity with substantially more rain, which makes it less aligned with the couple's wish to avoid a long gloomy cold season. [src-022][src-023][src-024]
- Practical comfort read: **Faro / Algarve** looks best for warmth and light; **Lisbon** is the best large-city compromise; **Porto** is the least aligned climate-wise even if it may later score well on other dimensions. [src-022][src-023][src-024]
- The remaining climate gap is a clean source for direct annual **sunny-day counts** in **Faro** (Lisbon and Porto are now covered by percentage-possible-sunshine data). [verification required; vq-010 partial]

### 5.3. Taxes {status: partial, depth: 0.5, last_updated: 2026-06-10, dod: partial}

> **DoD status**: partial. Covered: tax residence, 2026 resident PIT brackets, simplified self-employment mechanics, self-employed social-security rate/base, start-of-activity filing route, VAT headline, filing / joint-return mechanics, new-resident reliefs, and a USD 3,000/month gross->net stress test. Missing for full DoD: Portuguese accountant / AT confirmation of the exact Article 151 activity code for foreign-client IT, VAT/place-of-supply and reverse-charge reporting, first-year social-security timing, deductible-expense evidence, and D8 / ordinary-status compatibility.

#### Tax-residence and baseline regime

- PwC's 2026 Portugal summary says Portuguese tax residents are taxed on worldwide income at progressive PIT rates from **12.50% to 48%**; non-residents are taxed only on Portuguese-source income, with a 25% flat rate on taxable remuneration such as employment, self-employment, and pension income. For a relocation/D8-style plan where the couple lives in Portugal, the conservative screening model should therefore assume Portuguese tax residence and worldwide-income reporting rather than non-resident treatment. [src-401][src-402]
- For sole-trader / business and professional income, PwC says income may be taxed under the **simplified regime** or based on organised accounts. The simplified regime applies when the taxpayer has not opted for organised accounts and previous-year turnover / gross business and professional income is below **EUR 200,000** for 2026. [src-403]
- Under the simplified regime, listed Article 151 business/professional services are generally taxed on **75% of gross service income**; services not expressly listed use a 35% coefficient. The 75%/35% deduction is partly conditioned by evidence of activity expenses, and the computed taxable income can be increased if verified expenses are below the required baseline. For screening, use the 75% service coefficient as a conservative IT-freelancer placeholder until an accountant maps the exact activity. [src-403]

#### Social security, VAT, and registration mechanics

- PwC says the self-employed social-security contribution rate is **21.4%**. For self-employed people under the simplified tax regime, the monthly contribution basis is based on the relevant remuneration from the previous three months; relevant remuneration is **70% of service income** and **20% of production/sales income**, with a monthly base cap of 12 times IAS. This creates a simple service-income screening formula of about 21.4% x 70% = **14.98% of gross service receipts** before timing/exemption nuances. [src-404]
- ePortugal's official service page says self-employed workers must register themselves with the Tax Office by submitting a self-employment registration certificate **before starting activity**. Online filing is through the Finances Portal: search for "beginning of activity", choose "Services > Activity > Beginning of Activity", and deliver the certificate. Online delivery is free; at a desk, electronic filing is free and paper filing costs EUR 0.35. [src-405]
- PwC's corporate VAT summary gives Portugal's VAT standard rate as **23%** on the mainland, with lower regional rates in Madeira and the Azores. This tax pass did not verify whether the couple's foreign-client IT invoices are outside the Portuguese VAT charge, reverse-charged, exempt, or require VAT registration / recapitulative statements; treat VAT as an accountant/application-prep check, not a favorable assumption. [src-404]

#### New-resident reliefs and marriage effect

- PwC reports an IFICI / research-and-innovation incentive for certain new Portuguese tax residents who were not resident in Portugal during the previous five years and carry out eligible activities within eligible entities; in general terms it can give a **20% special rate** on net employment or category-B business/professional income from eligible activities and exemption for many foreign-sourced categories. This is not a default for the couple's freelance foreign-client IT file because eligibility depends on the activity and eligible entity criteria. [src-406]
- PwC also describes a former-tax-residents return regime with 50% relief for some returning Portuguese emigrants, but it requires prior Portuguese tax residence and therefore is not a default assumption for this Ukrainian couple. [src-406]
- Marriage or a de facto marriage can matter for rate mechanics: PwC says that, if married / de facto-married taxpayers opt for joint taxation, taxable income is divided by two for applying the PIT rate. PwC's administration page also says PIT returns are normally filed by **30 June** of the following year, and married couples may opt to file a joint return disclosing the total income of both. [src-401][src-402]

#### Worked USD 3,000/month stress test

Assumptions for this screening calculation: USD 3,000/month gross foreign-client service receipts; ECB snapshot **EUR 1 = USD 1.1540**, so USD 3,000 ~= **EUR 2,600/month**; simplified-regime service coefficient 75%; self-employed social security estimated as 21.4% x 70% of monthly gross service receipts; no IFICI/NHR-style relief, no VAT cash cost, no accountant fee, no first-year social-security exemption, and no deductible-expense uplift beyond the simplified-regime baseline. [src-401][src-403][src-404][src-406]

| Item | Single filing stress test | Joint-rate sensitivity if no second income |
|---|---:|---:|
| Gross receipts | EUR 2,600/mo (EUR 31,196/yr) | same |
| PIT taxable base before any expense-evidence adjustment | EUR 23,397/yr | same household base divided by two for rate application |
| Estimated annual PIT from 2026 bands | ~EUR 4,184/yr | ~EUR 3,139/yr |
| Estimated social security | ~EUR 389/mo | ~EUR 389/mo |
| Approximate net before accountant/VAT/immigration costs | **EUR 1,862/mo (~USD 2,148)** | **EUR 1,949/mo (~USD 2,249)** |

**Screening conclusion (`vq-105` closure)**: Portugal is not tax-light for the current one-income budget under ordinary self-employment. The simplified-regime model may still be livable in Porto/Faro if rent is controlled, but Lisbon becomes fragile. For country screening, the existing §5.3 model is sufficient: use the ordinary simplified-regime stress test as the safe baseline, do not assume IFICI/NHR-style relief or VAT/social-security optimisations, and keep Article 151 activity-code, expense-evidence, VAT/place-of-supply, first-year social-security timing, and D8 / ordinary-status compatibility as accountant/application-prep checks before filing. Do **not** mark §5.3 passed until those details are confirmed, but no additional queue item is needed for screening. [src-401][src-403][src-404][src-405][src-406]

### 5.4. Cost of Living {status: completed, depth: 1, last_updated: 2026-06-01, dod: passed}

> **DoD status**: passed at medium confidence. Covered: monthly expense ranges for Lisbon, Porto, and Faro/Algarve; utilities, groceries, transport, internet, eating out, and explicit $3,000/month budget conclusion.

| City | Practical monthly budget for the couple, excluding rent | Rent-sensitive all-in read | Budget fit on ~$3,000/month |
|---|---:|---|---|
| Lisbon | ~€1,450–€1,770 excluding rent for a couple; single-person city budget examples show €260–€340 groceries, €90–€135 electricity/water, €35–€50 internet, €40 transport, and €200–€350 moderate eating out. [src-176][src-178] | With a normal apartment, Lisbon commonly pushes a couple toward ~€2,800–€3,500/month all-in. [src-176] | Tight: possible only with careful rent choice, limited car use, and little buffer for visa/legalization costs. |
| Porto | Single-person city budgets are about €1,280–€2,235 including T1 rent; recurring non-rent items are slightly below Lisbon: €240–€320 groceries, €85–€125 electricity/water, €35–€50 internet, €40 Andante pass, and €180–€300 moderate eating out. [src-178] | For a couple, shared rent keeps Porto meaningfully below Lisbon, but central housing still dominates the budget. | Workable: best large-city cost/quality compromise if rent is controlled. |
| Faro / Algarve | Single-person Faro budgets are about €1,330–€2,120 including T1 rent; typical line items are €240–€320 groceries, €70–€120 electricity/water, €35–€50 internet, and €25–€150 transport/car costs. [src-178] | Seasonal/coastal rent and car dependence are the main swing factors. | Workable but variable: attractive climate, but avoid resort-priced coastal leases. |

Portugal-wide baseline: current 2026 guides place a single person's non-rent costs around €650–€750/month or about €666/month, while utilities for an 85 m² apartment are roughly €110–€150/month / €114/month, fibre internet is commonly €31–€50/month, and major-city public-transport passes are around €35–€40/month. [src-176][src-177]

**Budget conclusion for this couple**: at ~$3,000/month (roughly €2,750–€2,800 at recent exchange rates; exact exchange rate not fixed in the vault), Portugal is not a cheap landing by this household's constraints. Porto is the most rational large-city target; Faro/Algarve can work if they secure a year-round lease outside resort pricing and do not need a car-heavy lifestyle; Lisbon is possible but financially fragile because one normal apartment can consume most of the income buffer. [src-176][src-177][src-178]

### 5.5. Rent (decent 2BR) {status: completed, depth: 1, last_updated: 2026-06-02, dod: passed}

> **DoD status**: passed at medium confidence. Covered: 2026 T2/two-bedroom market bands for Lisbon, Porto, and Faro/Algarve, rent-to-income pressure, search platforms, upfront-cash/document expectations, and foreign-tenant risks.

| City / area | Working 2026 rent range for a normal 2-room/T2-style apartment | % of $3,000 income | Practical note |
|---|---:|---:|---|
| Lisbon | Central two-bedrooms often run about €1,800–€3,000/month, with higher-end units at or above €3,500; non-central planning can sometimes be lower but still rent-stressed. [src-177][src-178][src-189] | ~60–100% of $3,000 before utilities at the central-band level | High pressure; avoid central Lisbon if the income remains single-source. |
| Porto | Popular central / near-central two-bedrooms typically fall around €1,200–€1,800/month. [src-178][src-189] | ~40–60% | More realistic than Lisbon; outer neighbourhoods are the likely target. |
| Faro / Algarve | Faro and wider Algarve long-term two-bedrooms usually price around €1,000–€1,600/month, with seasonal/tourism effects pushing summer or short contracts higher. [src-178][src-189] | ~33–53% | Climate fit is strong, but long-term supply is thinner and seasonality matters. |

**Search platforms and process**: start with idealista for broad listings, then cross-check local agencies, Facebook/community listings, and direct landlord offers; long-term contracts of one year or more are standard for residents in 2026. [src-179]

**Documents and landlord expectations**: expect a NIF, passport or residence card, proof of income or employment/remote-work income, sometimes a Portuguese bank account, and sometimes a guarantor. Landlords often prefer Portuguese income; foreign remote income may require extra bank statements, contracts, or savings evidence. Standard upfront cash is one to two months of security deposit plus often one month of rent in advance, and competitive markets may ask for more, all of which should be written into the contract. [src-179]

**Foreigner pitfalls**: the biggest practical risks are overpaying before verifying the landlord and contract, accepting a lease not registered/usable for address proof, and underestimating how much upfront cash disappears at move-in. On a €1,000/month apartment, two to three months of deposit/advance can require €2,000–€3,000 before groceries or setup costs. [src-178][src-179]

Verification note: `vq-057` is resolved at the operational-planning level. The captured source gives current 2025-2026 T2/two-bedroom bands rather than official medians, but that is sufficient to pass §5.5 DoD at medium confidence; application-prep should still recheck live listings before signing a lease. [src-189]

### 5.6. Healthcare {status: partial, depth: 0.5, last_updated: 2026-06-12, dod: partial}

> **DoD status**: partial. Covered: SNS access mechanics for residents / TP holders, how to get an SNS user number and register with a local health centre, primary-care booking route, public/private care split, indicative private GP cost, maternity baseline, English-language caveat, and a budget read. Missing for full DoD: official D8 / residence-visa medical-insurance minimums from the serving consulate, current private-insurance quotes for two young adults, and live private-clinic price checks for common specialist/lab services.

#### Public healthcare / SNS access

- Portugal's Ukraine reception FAQ says the Temporary Protection Title automatically assigns a Social Security number and tax number and gives access to the National Health System, so TP is the cleanest healthcare-onboarding route if the couple uses Portugal as a pre-2027 shelter. [src-017]
- ePortugal states that a National Health Service (SNS) user number is allocated to anyone who needs healthcare at SNS public facilities. Portuguese citizens receive it automatically with the Citizen Card; non-nationals are allocated a number the first time they go to a public health facility such as a health centre or hospital. [src-492]
- ePortugal's health-centre registration service says a person can register at a healthcare centre by presenting the SNS user number, preferably at the centre for the area of residence; if the person does not yet have a user number, it can be obtained during health-centre registration. The service is free. [src-493]
- After registration, ePortugal says general/family-medicine and nursing consultations can be booked online, by phone through the local health centre or SNS 24 (808 24 24 24), or in person. Booking itself is free, but the person must be registered at the target health centre. [src-494]

#### Coverage, quality, and practical caveats

- Expatica's 2026 healthcare overview describes Portugal's SNS as free and available to residents, including expats, with coverage across primary and secondary care such as doctor visits, maternity care and birth, some dental care, community healthcare, hospitals/specialists, and emergency services. It also notes that most medical treatment became free in 2022, with remaining non-free situations mainly tied to emergency use without SNS referral and no subsequent hospitalization. [src-495]
- The same source characterizes healthcare quality as high, but warns about long wait times in the public system. For this couple, that means SNS is a real safety net, while routine specialist access may still require private appointments or insurance if speed matters. [src-495]
- Portugalist gives a practical expat-oriented caveat: the public system is the main safety net and can treat serious conditions without showing private insurance once resident/onboarded, but waiting lists and family-doctor shortages are common; English is more likely in Lisbon and the Algarve but is not guaranteed in public settings. [src-496]

#### Private care, insurance, and pregnancy

- Expatica reports that a private-doctor appointment in Portugal is commonly around **EUR 40-50**, with shorter private waiting lists and a higher chance of English-speaking staff. Private insurance is therefore a budget-smoothing and access-speed tool rather than a substitute for SNS registration. [src-495]
- Expatica names international/private insurance providers such as Allianz Care and Cigna Global, and a Portugal broker source listing Medis, Allianz Portugal, Fidelidade, Victoria, April, and DKV. This iteration did **not** capture live quotes for two young Ukrainian adults; keep the household budget model conservative until quotes are obtained. [src-495]
- For pregnancy and future childbirth, Expatica says public maternity care is part of SNS coverage, prenatal care takes place at the hospital, and the mother-to-be receives a Pregnancy Booklet during the first appointment. This supports Portugal as a plausible family-healthcare environment, but private maternity package prices and English-speaking OB/GYN access remain later application-prep checks. [src-495]

#### Budget conclusion for this couple

- Healthcare is a **positive but not zero-friction** Portugal factor. Once legally resident / protected and registered with SNS, the couple has a credible public safety net and free health-centre onboarding. The practical monthly-budget risk is not routine public primary care; it is private insurance or out-of-pocket private appointments used to bypass waiting lists, secure English-speaking access, or satisfy visa-file insurance evidence before SNS registration is settled. [src-492][src-493][src-494][src-495]
- Screening baseline: Portugal can remain workable for healthcare on a single USD 3,000/month income if rent is controlled in Porto/Faro and the couple budgets separately for private insurance / occasional private appointments. Do **not** mark healthcare DoD passed until current insurance quotes and the exact residence-visa medical-insurance requirement are captured. [src-495][src-496][vq-120]

### 5.7. Education (future child) {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

### 5.8. Comfort of life {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

### 5.9. Fit for couple with single income {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

### 5.10. Risk dimensions {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

### 5.11. Bureaucracy and practicality {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

## Block 4 — Risk dimensions (summary)

| Category | Level | Rationale |
|---|---|---|
| Currency / banking | — | [verification required] |
| Political | — | [verification required] |
| Ties to Ukraine | — | [verification required] |
| Diaspora / adaptation | — | [verification required] |

## Block 5 — Practical verdict

- **Can relocate now**: Partially — TP is available immediately for eligible Ukrainians; D8 requires income verification.
- **Best legalization path for the man**: D8 remote-work residence visa if the ~€3,680/month threshold can be met with evidence; otherwise, employment or entrepreneurship routes need exploration.
- **Best legalization path for the woman**: TP if eligible, or derived residence through marriage / partnership documentation.
- **Does marriage change the picture**: Some — documentary clarity improves, but income requirements for family D8 remain higher.
- **Realism of staying after 03.2027**: Medium — depends on obtaining ordinary residence (D8 or other) before TP expires; no captured automatic bridge.

**Pros**:
- TBD

**Cons / risks**:
- TBD

## Block 6 — Practical playbook (working relocation guide)

TBD — will be developed as sections 5.3–5.11 are completed.

## Block 7 — Sources

### 7a. Official primary
- [src-002] Council Implementing Decision (EU) 2022/382 — Temporary Protection for displaced persons from Ukraine (extended through 04 March 2027).
- [src-017] gov.pt / Justiça — FAQ sobre acolhimento de cidadãos ucranianos (visa exemption, TP title, NISS/NIF, NHS access).
- [src-019] AIMA — Aviso n.º 7035/2024 — Extensão da proteção temporária até 2027.
- [src-021] Diário da República — Decreto-Lei n.º 63/2026 (19 May 2026) — Alteração do regime de aquisição da nacionalidade portuguesa (7/10-year residence periods).
- [src-026] AIMA — Autorização de residência para trabalho remoto (post-visa filing route, documents, validity).
- [src-405] ePortugal — File the self-employment registration (official start-of-activity filing route and cost).
- [src-492] ePortugal — Obtain a National Health Service (SNS) user number.
- [src-493] ePortugal — Register at the health centre.
- [src-494] ePortugal — Book a consultation at the health centre.

### 7b. Reputable secondary
- [src-020] Portugalist — Portugal Digital Nomad Visa (D8) 2026 Guide (income threshold, family requirements, NIF/bank/accountancy setup).
- [src-401] PwC Portugal — Individual taxes on personal income (2026 PIT brackets, worldwide-income baseline, joint-rate mechanics).
- [src-402] PwC Portugal — Individual residence / tax administration (tax-residence baseline, annual PIT filing and joint-return mechanics).
- [src-403] PwC Portugal — Individual income determination (simplified-regime turnover cap, 75% / 35% service coefficients, expense-evidence mechanics).
- [src-404] PwC Portugal — Individual other taxes / corporate VAT summary (self-employed social security and VAT headline context).
- [src-406] PwC Portugal — Individual significant developments (IFICI and former-tax-residents reliefs).
- [src-495] Expatica — The healthcare system in Portugal.
- [src-496] Portugalist — Portugal's Healthcare System: What Expats Need to Know About Public and Private.
- [src-077] Wikipedia — Climate of Lisbon (Percentage possible sunshine data, WMO/NOAA sourced).
- [src-078] Wikipedia — Climate of Porto (Percentage possible sunshine data, WMO/NOAA sourced).
- [src-176] Movingto — Cost of Living in Portugal 2026 (national budget, utilities, groceries, transport, and housing orientation).
- [src-177] idealista/news — Cost of living in Portugal in 2026 (monthly non-rent costs, utilities, rent €/m², transport pass baseline).
- [src-178] Live in Portugal — Cost of Living in Portugal by City 2026 (Lisbon, Porto, Faro monthly city budgets and line items).
- [src-179] idealista/news — How to rent an apartment in Portugal: step-by-step guide (documents, deposit, advance rent, guarantor, contract process).
- [src-189] The Traveler — Rent in Lisbon vs Porto vs Faro (2025-2026 T2/two-bedroom bands and location caveats).

### 7c. Community and forums
_(none yet)_

### 7d. Statistical / commercial
- [src-022] Climate to Travel — Lisbon climate averages (temperatures, sunshine hours, precipitation).
- [src-023] Climate to Travel — Porto climate averages.
- [src-024] Climate to Travel — Faro / Algarve climate averages.

### 7e. Not found
- Official-primary D8 visa checklist (pre-visa document list, health-insurance minimum, processing time) from a Portuguese consulate or AIMA circular.
- Direct annual sunny-day counts for Faro.
- Portugal self-employed tax fit: exact Article 151 activity code / coefficient, VAT place-of-supply or reverse-charge reporting, first-year social-security timing, expense-evidence treatment, and D8 / ordinary-status compatibility for a Ukrainian foreign-client IT freelancer remain accountant/application-prep checks; `vq-105` is closed for screening.
- Portugal healthcare: official D8 / residence-visa medical-insurance minimums, live private-insurance quotes for two young adults, and private-clinic specialist/lab price checks remain open. → `vq-120`

## Block 8 — Open questions and verification markers

- [verification required] Portugal TP time-counting toward long-term residence. → `vq-008`
- [verification required] Direct annual sunny-day counts for Faro. → `vq-010 partial`
- Application-prep check (screening blocker closed): Portugal self-employed tax fit for foreign-client IT — Article 151 code, VAT/place-of-supply, social-security timing, deductible-expense evidence, and immigration-status compatibility. → `vq-105 resolved for screening`
- [verification required] Portugal D8 / residence-visa medical-insurance minimums and current private-insurance quotes for two young adults. → `vq-120`
