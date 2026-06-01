---
country: Portugal
tier: null
depth_score: 2.5
last_updated: 2026-06-01T16:05:49Z
sections_completed: ["5.4"]
sections_partial: ["5.1","5.2","5.5"]
sections_pending: ["5.3","5.6","5.7","5.8","5.9","5.10","5.11"]
risk_flags: ["no-clear-post-2027-tp-bridge","climate-sunny-days-gap","d8-income-above-current-budget","lisbon-rent-pressure"]
sources_used: ["src-002","src-017","src-018","src-019","src-020","src-021","src-022","src-023","src-024","src-026","src-077","src-078","src-176","src-177","src-178","src-179"]
unverified_count: 2
schema_version: 2.0.0
---

# Portugal

> First research iteration for Portugal. All content in this file is in English per `vault-protocol.md`.

## Block 1 — Summary

- **Tier**: TBD after taxes, rent, healthcare, partner-path, and bureaucracy research are added.
- **depth_score**: 2.5
- **Last updated**: 2026-06-01T16:05:49Z
- **Tier rationale**: Portugal still looks strategically interesting because it combines a live temporary-protection framework with a known remote-work residence route and a warm Atlantic south, but the first pass surfaced two major constraints for this couple: no documented official post-04 March 2027 TP conversion bridge was captured in this iteration, and the D8 remote-work income threshold appears above the couple's current nominal monthly budget.

## Block 2 — Scoring

| Criterion | Score (1–10) | Confidence | Brief rationale | Profile section |
|---|---:|---|---|---|
| Legalization (now + post-03.2027) | 5 | medium | Portugal offers a real TP shelter path and a known D8 remote-work track, but the D8 threshold looks too high for the current household budget, the official-primary D8 checklist still needs capture, and no clean TP→ordinary-residence bridge for after 04 March 2027 was documented in this pass. | §5.1 |
| Climate | 8 | medium | Lisbon and especially Faro fit the warm-climate preference well, while Porto is cooler and much wetter; direct sunny-day counts still need a dedicated source. | §5.2 |
| Taxes | — | N/A | [verification required] | §5.3 |
| Cost of living | 6 | medium | A $3,000/month household can work in Porto/Faro with disciplined rent and no car-heavy lifestyle, but Lisbon leaves little buffer once rent is included. | §5.4 |
| Rent (decent 2BR) | 4 | medium | Lisbon and parts of the Algarve are rent-pressure markets; Porto is more workable, but exact T2 listing medians still need verification. | §5.5 |
| Healthcare | — | N/A | [verification required] | §5.6 |
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

### 5.3. Taxes {status: pending, depth: 0, last_updated: —, dod: pending}

> **DoD**: effective rate at $3000/mo computed; registration procedure for applicable regime; gross→net example; new-resident reliefs; marriage tax effect.

[verification required]

### 5.4. Cost of Living {status: completed, depth: 1, last_updated: 2026-06-01, dod: passed}

> **DoD status**: passed at medium confidence. Covered: monthly expense ranges for Lisbon, Porto, and Faro/Algarve; utilities, groceries, transport, internet, eating out, and explicit $3,000/month budget conclusion.

| City | Practical monthly budget for the couple, excluding rent | Rent-sensitive all-in read | Budget fit on ~$3,000/month |
|---|---:|---|---|
| Lisbon | ~€1,450–€1,770 excluding rent for a couple; single-person city budget examples show €260–€340 groceries, €90–€135 electricity/water, €35–€50 internet, €40 transport, and €200–€350 moderate eating out. [src-176][src-178] | With a normal apartment, Lisbon commonly pushes a couple toward ~€2,800–€3,500/month all-in. [src-176] | Tight: possible only with careful rent choice, limited car use, and little buffer for visa/legalization costs. |
| Porto | Single-person city budgets are about €1,280–€2,235 including T1 rent; recurring non-rent items are slightly below Lisbon: €240–€320 groceries, €85–€125 electricity/water, €35–€50 internet, €40 Andante pass, and €180–€300 moderate eating out. [src-178] | For a couple, shared rent keeps Porto meaningfully below Lisbon, but central housing still dominates the budget. | Workable: best large-city cost/quality compromise if rent is controlled. |
| Faro / Algarve | Single-person Faro budgets are about €1,330–€2,120 including T1 rent; typical line items are €240–€320 groceries, €70–€120 electricity/water, €35–€50 internet, and €25–€150 transport/car costs. [src-178] | Seasonal/coastal rent and car dependence are the main swing factors. | Workable but variable: attractive climate, but avoid resort-priced coastal leases. |

Portugal-wide baseline: current 2026 guides place a single person's non-rent costs around €650–€750/month or about €666/month, while utilities for an 85 m² apartment are roughly €110–€150/month / €114/month, fibre internet is commonly €31–€50/month, and major-city public-transport passes are around €35–€40/month. [src-176][src-177]

**Budget conclusion for this couple**: at ~$3,000/month (roughly €2,750–€2,800 at recent exchange rates; exact exchange rate not fixed in the vault), Portugal is not a cheap landing by this household's constraints. Porto is the most rational large-city target; Faro/Algarve can work if they secure a year-round lease outside resort pricing and do not need a car-heavy lifestyle; Lisbon is possible but financially fragile because one normal apartment can consume most of the income buffer. [src-176][src-177][src-178]

### 5.5. Rent (decent 2BR) {status: partial, depth: 0.5, last_updated: 2026-06-01, dod: partial}

> **DoD status**: partial. Covered: 2026 market ranges, search platforms, upfront-cash/document expectations, and foreign-tenant risks. Missing for full DoD: clean current T2/2BR listing medians for Lisbon, Porto, and Faro from a directly captured listings/statistics source.

| City / area | Working 2026 rent range for a normal 2-room/T2-style apartment | % of $3,000 income | Practical note |
|---|---:|---:|---|
| Lisbon | Use ~€1,300–€1,900/month as a conservative planning band for a non-luxury 2-room apartment: idealista reports December-2025 area rents around €19.6/m² in Lisbon metro, making an 80 m² flat roughly €1,568/month; central one-bed/T1 examples already run ~€1,200–€1,800. [src-177][src-178] | ~47–69% before utilities if $3,000 ≈ €2,750 | High pressure; avoid central Lisbon if the income remains single-source. |
| Porto | Use ~€1,000–€1,500/month as the working planning band: sources place central T1s around €950–€1,400 and older idealista examples show three-bedroom Porto rents around €1,600 central / €1,350 outside centre. [src-176][src-178] | ~36–55% | More realistic than Lisbon; outer neighbourhoods are the likely target. |
| Faro / Algarve | Use ~€1,100–€1,700/month for a normal year-round T2, with higher risk in resort towns: Faro T1s are quoted around €800–€1,200 and Algarve listings can range from ~€700 to luxury-villa levels around €2,200/month. [src-177][src-178] | ~40–62% | Climate fit is strong, but long-term supply is thinner and seasonality matters. |

**Search platforms and process**: start with idealista for broad listings, then cross-check local agencies, Facebook/community listings, and direct landlord offers; long-term contracts of one year or more are standard for residents in 2026. [src-179]

**Documents and landlord expectations**: expect a NIF, passport or residence card, proof of income or employment/remote-work income, sometimes a Portuguese bank account, and sometimes a guarantor. Landlords often prefer Portuguese income; foreign remote income may require extra bank statements, contracts, or savings evidence. Standard upfront cash is one to two months of security deposit plus often one month of rent in advance, and competitive markets may ask for more, all of which should be written into the contract. [src-179]

**Foreigner pitfalls**: the biggest practical risks are overpaying before verifying the landlord and contract, accepting a lease not registered/usable for address proof, and underestimating how much upfront cash disappears at move-in. On a €1,000/month apartment, two to three months of deposit/advance can require €2,000–€3,000 before groceries or setup costs. [src-178][src-179]

[verification required] Exact 2026 T2 listing medians for Lisbon, Porto, and Faro remain queued because live idealista listing pages were JS/WAF-blocked during this iteration. → `vq-057`

### 5.6. Healthcare {status: pending, depth: 0, last_updated: —, dod: pending}

[verification required]

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

### 7b. Reputable secondary
- [src-020] Portugalist — Portugal Digital Nomad Visa (D8) 2026 Guide (income threshold, family requirements, NIF/bank/accountancy setup).
- [src-077] Wikipedia — Climate of Lisbon (Percentage possible sunshine data, WMO/NOAA sourced).
- [src-078] Wikipedia — Climate of Porto (Percentage possible sunshine data, WMO/NOAA sourced).
- [src-176] Movingto — Cost of Living in Portugal 2026 (national budget, utilities, groceries, transport, and housing orientation).
- [src-177] idealista/news — Cost of living in Portugal in 2026 (monthly non-rent costs, utilities, rent €/m², transport pass baseline).
- [src-178] Live in Portugal — Cost of Living in Portugal by City 2026 (Lisbon, Porto, Faro monthly city budgets and line items).
- [src-179] idealista/news — How to rent an apartment in Portugal: step-by-step guide (documents, deposit, advance rent, guarantor, contract process).

### 7c. Community and forums
_(none yet)_

### 7d. Statistical / commercial
- [src-022] Climate to Travel — Lisbon climate averages (temperatures, sunshine hours, precipitation).
- [src-023] Climate to Travel — Porto climate averages.
- [src-024] Climate to Travel — Faro / Algarve climate averages.

### 7e. Not found
- Official-primary D8 visa checklist (pre-visa document list, health-insurance minimum, processing time) from a Portuguese consulate or AIMA circular.
- Direct annual sunny-day counts for Faro.

## Block 8 — Open questions and verification markers

- [verification required] Portugal TP time-counting toward long-term residence. → `vq-008`
- [verification required] Direct annual sunny-day counts for Faro. → `vq-010 partial`
- [verification required] Exact 2026 T2 rent medians for Lisbon, Porto, and Faro from a directly captured listings/statistics source. → `vq-057`
