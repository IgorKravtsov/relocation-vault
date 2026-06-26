---
country: Italy
tier: null
depth_score: 10.0
last_updated: 2026-06-26T18:06:00Z
sections_completed: ["5.2", "5.3", "5.4", "5.5", "5.7", "5.8", "5.9", "5.10", "5.11"]
sections_partial: ["5.1", "5.6"]
sections_pending: []
risk_flags: ["no-clear-post-2027-tp-bridge", "dn-income-source-2024", "unmarried-partner-not-covered-by-dn-family-sponsorship", "italy-worldwide-tax-and-reporting", "rome-milan-rent-pressure", "southern-services-tradeoff", "italy-private-insurance-quote-gap", "italy-international-school-cost-risk", "italian-language-integration-needed"]
sources_used: ["src-002", "src-027", "src-028", "src-029", "src-030", "src-031", "src-032", "src-033", "src-034", "src-287", "src-288", "src-289", "src-290", "src-291", "src-292", "src-293", "src-396", "src-397", "src-398", "src-399", "src-400", "src-616", "src-617", "src-618", "src-747", "src-748", "src-809"]
unverified_count: 0
schema_version: 2.0.0
---

# Italy

## Block 1 — Summary

- **Tier**: TBD. Italy has a usable temporary-protection framework through 4 March 2027 and a formal digital-nomad / remote-worker visa, but the first pass did not find an Italy-specific TP-to-ordinary-residence bridge after March 2027, and the digital-nomad family route clearly covers a spouse and minor children, not an unmarried partner. Tier remains unassigned until taxes, rent, partner status, and post-2027 fallback mechanics are researched.
- **depth_score**: 10.0
- **Last updated**: 2026-06-26T18:06:00Z
- **Tier rationale**: Italy looks operationally plausible for a married couple if the IT worker can prove a highly specialized remote-work profile and stable income, but long-term stay after TP still depends on switching to an ordinary permit rather than relying on TP.

## Block 2 — Scoring

| Criterion | Score (1–10) | Confidence | Brief rationale | Profile section |
|---|---:|---|---|---|
| Legalization (now + post-03.2027) | — | N/A | TP is extended to 04 March 2027 and DN route exists, but the safe post-TP baseline is now explicit: no captured conversion bridge; ordinary status required. | §5.1 |
| Climate | — | medium | Strong climate range: cold/damp Milan, mild Rome, very mild Palermo; clear-day counts captured. | §5.2 |
| Taxes | 7 | medium | For a small IT freelancer, Italy's `regime forfetario` can keep the first-pass burden moderate, but Italian tax residence means worldwide-income reporting and INPS contributions are material. At run-date FX, USD 3,000/month gross is about EUR 31.2k/year; simplified forfetario + Gestione Separata gives about EUR 1,950/month net at the ordinary 15% substitute-tax rate, or about EUR 2,078/month if the 5% startup rate truly applies. | §5.3 |
| Cost of living | 6 | medium | Palermo and Naples look manageable on gross USD 3,000 and tighter but plausible against the conservative forfetario net; Rome is tight and Milan is poor by default. | §5.4 |
| Rent (decent 2BR) | 5 | medium | The modest 40 m2 1BR proxy is acceptable in Palermo/Naples but Rome and especially Milan consume too much of the one taxed income; 80 m2 3BR is a stress test, not the default. | §5.5 |
| Healthcare | — | medium | Partial: SSN access looks strong for TP/legal residents and private care is usable, but DN-compliant private-insurance quotes / waiting periods are not yet captured. | §5.6 |
| Education (future child) | 7 | medium | Public schooling is structurally usable and free through compulsory ages; 0-3 childcare and international schools are the main one-income budget risks. | §5.7 |
| Comfort of life | 7 | medium | Safety proxies are broadly positive and Italy has strong everyday services, but bureaucracy and English access are uneven; Palermo/Naples/Rome require Italian-language integration. | §5.8 |
| Fit for couple with single income | 5 | medium | Marriage likely matters for DN dependency, the student partner can study remotely as private activity once status is secure, and the one-income budget works mainly in Palermo/Naples rather than Rome/Milan. | §5.9 |

**Weighted score**: — (compute when all criteria are scored)

## Block 3 — Profile by section

### 5.1. Legalization {status: partial, depth: 1, last_updated: 2026-05-25, dod: partial}

> **DoD status**: Partial. TP extension and DN core route are sourced, but the full Ukraine-applicant consular route remains incomplete; the no-bridge and unmarried-partner baselines have been made explicit from existing sources.

#### Now (until 03.2027)

**Temporary protection for Ukrainians.** Italy participates in the EU temporary-protection framework, and the EU-level extension now runs to 4 March 2027 [src-002]. Italy's Integration Migrants portal reports that Decree-Law 201/2025 allows renewal, at the interested person's request, of relevant Ukrainian residence permits until 4 March 2027 and confirms the same date for temporary protection for displaced Ukrainians under Council Implementing Decision (EU) 2025/1460 [src-027]. UNHCR Italy states that a temporary-protection applicant should contact the Police Headquarters (`Questura`) directly, that the application receipt contains the Italian tax number (`codice fiscale`), and that beneficiaries can work, study, and register with the National Health Service from the moment of the request [src-034]. Confidence: high for extension date, medium-high for the operational Questura / rights summary.

**Digital nomad / remote worker visa.** Italy has a national digital-nomad / remote-worker visa for non-EU citizens who intend to work remotely while living in Italy [src-028]. The route is restricted to highly specialized workers under Article 27-quater of Legislative Decree 286/1998: a post-secondary degree, at least three years of professional training/experience, or a qualifying specialized profile is needed [src-028]. The consular checklist distinguishes independent digital nomads from remote employees [src-028]. Core checklist captured in this pass:

- passport / travel document valid at least 15 months beyond intended travel and with two blank pages [src-028];
- national visa form and photo [src-028];
- travel medical insurance, with medical-expense coverage of at least €30,000 / USD 50,000, or a plan to buy Italian insurance before Questura registration [src-028];
- proof of qualifying profession [src-028];
- registered Italian lease / rental contract / deed covering the visa period; hotel stay or third-party hospitality is not accepted by the cited consulate [src-028];
- legal income of at least three times the minimum necessary to pay healthcare taxes in Italy; the cited 2024 amount is at least €24,789/year, and income must come from the work to be performed in Italy, not passive income [src-028];
- six or more months of prior work experience in the field; for digital nomads, tax returns, client invoices, or professional-association evidence can be used [src-028];
- visa fee; exact amount varies quarterly by official exchange rate [src-028].

For the current couple, €24,789/year is about €2,066/month before any family uplift or rent-proof requirements. Their stated USD 3,000/month gross income may pass the primary-applicant threshold if documented cleanly, but this needs a 2026 consular cross-check because the captured income amount is explicitly a 2024 consular figure [src-028].

#### After 4 March 2027

Operational baseline: do not rely on Italy temporary protection as the long-term plan. EU and Italian sources confirm the current 4 March 2027 horizon [src-002][src-027], but this pass did not find an Italy-specific bridge equivalent to Greece's Article 194. UNHCR Italy explicitly says there is currently no provision allowing conversion of a temporary-protection permit into a work permit [src-034]. Therefore the working plan is: if Italy remains a candidate, file for an ordinary long-stay route (most likely digital nomad / remote worker) before TP expiry rather than waiting for a TP conversion.

#### Residence without local employer

The digital-nomad category is the main no-local-employer route captured in this pass: it covers freelancers, consultants, or other independent specialists working remotely while living in Italy [src-028]. Remote employees can also apply, but must provide an employment contract and an employer declaration concerning specified criminal convictions; salary cannot be below the relevant collective contract and, in any case, below ISTAT median annual salary [src-028]. Local Italian employment is not the basis of this route; it is for remote work.

#### PR and citizenship

Initial DN / remote-worker residence after arrival requires applying at the local Questura within eight working days of arrival [src-028]. The cited consulate says the DN residence permit is currently issued for one year and can be renewed locally as long as the applicant maintains employment, lodging, and health insurance [src-028]. For citizenship, the Prefecture / Interior Ministry citizenship-by-residence guidance is logged for follow-up; the working baseline for non-EU nationals is 10 years of legal residence, but the exact categories and residence-counting mechanics need verification from the PDF in a later iteration [src-029].

#### Polish karta pobytu interaction

Baseline planning rule: a Polish residence title does not substitute for an Italian long-stay status. For temporary protection, the EU one-Member-State principle remains the safe baseline [src-002]. If the Polish `karta pobytu` is not TP, it still does not create a right to reside long-term in Italy; it only helps with Schengen-area mobility within its limits. The couple should plan an Italy-specific TP or DN / remote-worker file.

#### Personal playbook for our couple

1. **If using Italy only as a pre-03.2027 refuge**: apply for temporary protection through the Questura and use the receipt / permit to work, study, and register with the SSN [src-027][src-034]. This is not yet a post-2027 plan.
2. **If using Italy as a long-term candidate**: prepare the IT worker's DN / remote-worker package before moving: degree or experience evidence, client/employer proof, invoices/tax returns, proof of income, insurance, and a registered Italian lease [src-028].
3. **Marriage matters**: the cited DN family section supports sponsorship for a spouse and minor children after arrival; it does not mention unmarried partners [src-028]. If Italy stays in the shortlist, marriage likely materially improves the dependent route for the student partner.
4. **Fallback**: if the IT worker cannot document the highly specialized profile, income, and registered lease, Italy should be treated as legally risky for long-term stay after TP.

### 5.2. Climate {status: deep, depth: 1, last_updated: 2026-05-25, dod: passed}

Italy is climatically uneven: the north is much less aligned with the couple's preference than central and southern/coastal cities.

| City | January mean | July mean | Sunshine / clear-day signal | Comfort notes |
|---|---:|---:|---|---|
| Milan | 3.5 °C | 25.0 °C | ~1,900 sunshine hours/year; 171 sunny mornings and 194 clear evenings/year | Cold, damp, fog-prone winter; hot, muggy summer in the Po Valley [src-031][src-033]. |
| Rome | 7.7 °C | 25.2 °C | 2,473 sunshine hours/year; 218 sunny mornings and 232 clear evenings/year | Mediterranean, mild/rainy winter and hot sunny summer; better fit than Milan [src-030][src-033]. |
| Palermo | 12.4 °C | 26.0 °C | 2,544 sunshine hours/year; 228 sunny mornings and 227 clear evenings/year | Very mild winter, hot sunny summer; sirocco can push summer temperatures above 40 °C [src-032][src-033]. |

**Climate verdict for the couple**: Rome and Palermo/Sicily fit the warm-climate preference much better than Milan. Milan should be treated as a jobs/services hub rather than a climate-fit city. Palermo has the best winter comfort but also the strongest heat and sirocco risk. Rome is the balanced first city to research further for rent, services, and bureaucracy.

### 5.3. Taxes {status: deep, depth: 1, last_updated: 2026-06-06, dod: passed}

> **DoD status**: Passed for first-pass country screening. The section gives a conservative `partita IVA` / `regime forfetario` baseline for a foreign-client IT freelancer at about USD 3,000/month, plus the ordinary-IRPEF fallback and filing caveats. Exact ATECO classification, invoice/VAT handling for specific clients, and the 5% startup-rate eligibility should be checked with an Italian commercialista before filing.

#### Tax residence and scope

Italy is a full tax-residence country, not a simple digital-nomad tax shelter. PwC's 2026 Italy tax summary states that an individual is Italian tax resident if, for most of the fiscal year, they are physically present in Italy, have habitual residence, or have domicile / principal social-interest centre in Italy; registration in the resident-population record also creates a presumption of residence [src-291]. A resident individual is taxed in Italy on worldwide income and must report foreign investments / assets in the Italian return [src-291].

For this couple, the practical baseline is: if the IT worker lives in Italy long enough for DN / ordinary residence planning, treat him as Italian tax resident and plan Italian self-employment registration, not "pay taxes only in Ukraine/Poland". The Polish `karta pobytu` does not by itself change Italian tax residence if the actual centre of life moves to Italy.

#### Best-fit regime: `partita IVA` under `regime forfetario`

The most plausible first-pass setup for a solo foreign-client IT freelancer is opening an Italian individual VAT number (`partita IVA`) and using the simplified `regime forfetario`, if eligibility conditions are met. Agenzia delle Entrate describes the forfetario as a preferential regime for individuals carrying on business, arts, or professions; access requires, among other conditions, prior-year revenues/fees not above EUR 85,000 and employee/collaborator costs not above EUR 20,000 [src-287]. Agenzia also says a new activity can opt into the regime by declaring expected eligibility in the VAT-start declaration [src-287]. For individual VAT-number opening / change / closure, Agenzia uses the AA9/12 process for natural persons [src-289].

How the regime works for the calculation:

- income is not actual profit; it is revenues multiplied by an ATECO profitability coefficient [src-288];
- for IT / communications activity codes, a 2026 coefficient table gives the broad ATECO 58-63 band at 67%, meaning 67% of revenue is deemed taxable income before mandatory social-security deductions [src-292];
- mandatory social-security contributions are deducted from the forfetario income base before the substitute tax [src-288];
- the substitute tax is 15% instead of ordinary IRPEF, regional/municipal surtaxes, and IRAP [src-288];
- a 5% substitute tax can apply for the first five years of a genuinely new activity if the statutory startup conditions are met, including no similar artistic/professional/business activity in the prior three years and no mere continuation of prior work [src-287][src-288].

Confidence: medium-high for the 85k cap and 15% / 5% rules from Agenzia; medium for applying the 67% ATECO band to the couple's exact IT activity until a commercialista maps his precise ATECO code.

#### Social security: INPS `Gestione Separata`

For an unlicensed IT consultant / developer without a professional pension fund, the working assumption is INPS `Gestione Separata`. INPS Circular 8/2026 sets the 2026 separate-management contribution framework and shows a 26.07% annual rate for professionals using that category; it also states that professionals enrolled in `Gestione Separata` bear the contribution themselves and pay it by telematic F24 on the income-tax deadlines [src-290]. PwC's 2026 Italy summary is consistent at a planning level: VAT-number self-employed individuals not covered by a mandatory private pension fund pay their own `Gestione Separata` contributions and may charge a 4% client contribution on invoices, but the payment obligation remains with the individual [src-291].

#### Worked example for USD 3,000/month gross

Run-date FX from `open.er-api.com` was 1 USD = EUR 0.865342, so USD 3,000/month equals about EUR 2,596/month or EUR 31,152/year [src-293]. Simplified forfetario calculation for an IT activity with a 67% coefficient and INPS `Gestione Separata` at 26.07%:

| Step | Amount |
|---|---:|
| Gross revenue | EUR 31,152/year |
| Forfetario deemed income, 67% of revenue | EUR 20,872/year |
| INPS `Gestione Separata`, 26.07% of deemed income | EUR 5,441/year |
| Substitute-tax base after mandatory contributions | EUR 15,431/year |
| Substitute tax at 15% | EUR 2,315/year |
| **Estimated net at ordinary forfetario 15%** | **EUR 23,396/year = EUR 1,950/month** |
| Substitute tax at 5% startup rate, if eligible | EUR 772/year |
| **Estimated net at startup 5%** | **EUR 24,939/year = EUR 2,078/month** |

This is before rent and living costs, and before accounting fees / stamp duties / e-invoicing software. It also assumes the activity can safely use forfetario, the 67% ATECO band, and `Gestione Separata` rather than a different INPS fund. The 15% case is the conservative screen; the 5% case is upside, not a guaranteed plan.

#### Ordinary IRPEF fallback and new-resident relief caveat

If forfetario is unavailable, Italy becomes much heavier. PwC lists 2025 national IRPEF brackets of 23% to EUR 28,000, 33% from EUR 28,001 to EUR 50,000, and 43% above EUR 50,000, plus regional tax of 1.23%-3.33% and municipal tax of 0%-0.9% [src-291]. This ordinary regime may allow actual expense deductions, but for a low-cost remote IT worker it is likely less attractive than forfetario.

Italy also has special new-resident / impatriate-style regimes, but the captured PwC material describes high-net-worth lump-sum foreign-income regimes and other specialized rules rather than a clear default benefit for a pure small foreign-client freelancer at USD 3,000/month [src-291]. Do not assume those regimes rescue the budget without professional advice.

#### Registration and compliance playbook

1. Before filing, ask a commercialista to map the exact work to an ATECO code and confirm forfetario eligibility, 5% startup eligibility, and INPS fund.
2. Open `partita IVA` as a natural person through Agenzia's AA9/12 route; indicate expected forfetario eligibility if starting under that regime [src-287][src-289].
3. Register / pay INPS `Gestione Separata` if this is the correct fund; budget for self-assessed F24 payments aligned with income-tax deadlines [src-290].
4. Use Italian-compliant invoicing / e-invoicing workflows and keep foreign-client contracts, invoices, bank statements, and proof of remote work consistent with the immigration file.
5. File `Modello Redditi PF` rather than the simplified employee-style 730 if he has a VAT number; PwC states `Modello Redditi PF` is used where 730 is not applicable, with electronic filing by 31 October and self-assessed payments / advances [src-291].

#### Couple-specific verdict

At USD 3,000/month, Italy's tax system is workable only if the IT worker can use forfetario and keep rent under control. The tax result is not the main blocker compared with legalization/rent: net around EUR 1,950/month at the ordinary forfetario rate may be enough in cheaper cities but tight for Rome/Milan with a dependent partner. Marriage does not create a major freelancer-tax saving in this baseline; PwC notes joint filing for Modello 730, but VAT-number taxpayers use `Modello Redditi PF`, where married couples cannot file jointly [src-291]. If the partner later works, her income should be modelled separately.

### 5.4. Cost of living {status: deep, depth: 1, last_updated: 2026-06-09, dod: passed}

> **DoD status**: Passed for first-pass screening. Livingcost is commercial data, so confidence is medium and live-listing checks remain application-prep, but it gives a consistent city-level budget baseline for Rome, Milan, Naples, and Palermo.

Italy is not a uniform budget country. The north/service hubs are significantly harder on one remote-IT income than the south.

| City | Total with rent, one person / family of 4 | Food, one person / family of 4 | Transport, one person / family of 4 | Budget verdict for this couple |
|---|---:|---:|---:|---|
| National baseline | $1,656 / $3,941 | $553 / $1,463 | $104 / $290 | Useful only as a broad benchmark; national family-of-four costs exceed the couple's gross, but the couple is two adults rather than a family of four [src-396]. |
| Rome | $2,082 / $4,816 | $543 / $1,432 | $186 / $518 | Service-rich and balanced climatically, but tight on the conservative Italy tax net; workable only with disciplined rent and no large legal/medical surprises [src-397]. |
| Milan | $2,370 / $5,666 | $655 / $1,732 | $193 / $544 | Poor default fit: cold-climate penalty plus high rent/cost pressure; keep only as a services/jobs hub, not a budget base [src-398]. |
| Naples | $1,615 / $3,721 | $507 / $1,323 | $131 / $359 | Better first-pass budget fit than Rome/Milan; warmer south, but quality-of-life / bureaucracy / local-services tradeoffs need later sections [src-399]. |
| Palermo | $1,308 / $3,151 | $479 / $1,260 | $101 / $277 | Best first-pass budget/climate fit among screened cities; rent is meaningfully lower, but island/southern-services tradeoffs must be checked later [src-400]. |

**Budget interpretation.** The tax section's conservative forfetario model leaves roughly EUR 1,950/month net before rent and living costs, about USD 2,250 at the run-056 FX baseline [src-293]. On that net, Milan is not a realistic default and Rome is tight; Palermo and Naples are the practical first screens. Against the gross USD 3,000/month income, Palermo leaves the most buffer for immigration, accountant, insurance, and travel costs.

**Practical monthly baseline for two adults.** Livingcost does not give a two-adult line, so use the one-person line plus a conservative add-on for the non-working partner's food/transport/variable costs rather than the family-of-four line. For screening: Palermo/Naples can plausibly fit if rent is controlled; Rome needs careful apartment selection; Milan should be avoided unless income rises.

### 5.5. Rent {status: deep, depth: 1, last_updated: 2026-06-09, dod: passed}

> **DoD status**: Passed for first-pass screening. The vault uses Livingcost's 40 m2 1BR as the closest proxy for the modest two-room-apartment definition; 80 m2 3BR is recorded only as an upper-size stress test. Exact listings, lease registration, deposits, agency fees, and landlord requirements remain application-prep.

| City | 40 m2 1BR centre / cheap | 80 m2 3BR centre / cheap | 40 m2 proxy as % of $3,000 gross | Screening verdict |
|---|---:|---:|---:|---|
| National baseline | $873 / $627 | $1,607 / $1,114 | 21%-29% | Broad benchmark; not enough to choose a city [src-396]. |
| Rome | $1,430 / $899 | $2,479 / $1,607 | 30%-48% | A cheap 40 m2 unit may be workable; central/default rent is too high for a one-income couple after Italian taxes [src-397]. |
| Milan | $1,522 / $1,068 | $2,800 / $1,958 | 36%-51% | Rent-pressure flag: even the cheap 40 m2 proxy strains the budget, while 80 m2 is incompatible with the current income [src-398]. |
| Naples | $941 / $616 | $1,689 / $1,032 | 21%-31% | Plausible first-pass rent fit if the couple accepts Naples/local-quality tradeoffs; better than Rome/Milan for budget [src-399]. |
| Palermo | $630 / $399 | $1,025 / $678 | 13%-21% | Best screened rent fit; 40 m2 proxy leaves room for tax, insurance, and immigration costs [src-400]. |

**Utilities and internet.** Livingcost's family utility lines are broadly similar across the screened cities: Rome $227/month, Milan $228, Naples $187, Palermo $188; internet is about $27-$32/month [src-397][src-398][src-399][src-400]. This means the main housing variable is rent, not utilities.

**Search platforms and process.** For a later application-prep pass, search on Immobiliare.it, Idealista Italy, Casa.it, local agencies, and city Facebook groups. The DN route makes housing unusually important because the captured consular checklist requires a registered Italian lease / rental contract / deed and does not accept hotel stay or third-party hospitality [src-028]. Therefore, the couple should treat lease formality and landlord willingness to register the contract as a legal-route constraint, not only a comfort preference.

**Landlord requirements to verify before filing.** Expect deposit / agency-fee variation, preference for Italian work contracts or local guarantors in stronger markets, and reluctance to register short leases for newcomers. These are not yet sourced enough for DoD beyond first-pass screening, so they remain application-prep checks rather than new vault blockers.

### 5.6. Healthcare {status: partial, depth: 1, last_updated: 2026-06-15, dod: partial}

> **DoD status**: Partial. Covered: TP/SSN access baseline, public/private system split, doctor-visit price proxies, DN insurance-document requirement, and maternity planning caveat. Missing for full DoD: Italy DN-compliant private-insurance quotes for two young adults, maternity waiting-period / exclusion checks, and selected-city ASL registration steps after choosing Palermo / Naples / Rome.

- For a TP-first route, healthcare is a major operational strength: UNHCR Italy says temporary-protection beneficiaries can register with the National Health Service (`SSN`) from the moment of the request, alongside work and study rights. [src-034]
- For a DN / remote-worker route, the captured consular checklist requires travel medical insurance with at least EUR 30,000 / USD 50,000 medical-expense coverage, or a plan to buy Italian insurance before Questura registration. Treat this as a visa-file requirement, not as a full healthcare budget quote. [src-028]
- General public-system baseline: International Insurance describes Italy's SSN as a mixed public/private system that provides free or very low-cost care to citizens and non-citizens with residency status, including hospitalization, family doctors, specialists, discounted medication, laboratory services, and ambulance services. It also notes that non-EU expats generally need finalized residence status / identity documentation for SSN access and private insurance during the waiting period. [src-616]
- Private-care price proxies are manageable for occasional use but higher than Spain/Portugal in the same dataset: Livingcost lists a doctor's visit around USD 99.6 nationally, USD 117 in Rome, USD 84.5 in Naples, USD 79.5 in Palermo, and USD 105 in Milan. [src-396][src-397][src-399][src-400][src-398]
- Maternity / future-child planning baseline: do not rely on a tourist-style travel policy if using DN filing or pregnancy planning. Before filing, obtain an Italy-compliant private medical policy for both adults and verify maternity coverage, pre-existing pregnancy exclusions, waiting periods, and whether SSN registration timing differs between TP, DN, and self-employed tax files. This remains an application-prep check.
- Budget interpretation: Italy healthcare is not the main country blocker if the couple has TP or ordinary residence, but the documentary gap matters for DN filing. Keep `italy-private-insurance-quote-gap` until insurer quotes and selected-city ASL steps are captured.

### 5.7. Education (future child) {status: deep, depth: 2, last_updated: 2026-06-15, dod: passed}

> **DoD status**: Passed for first-pass screening. Covered: early-childhood structure and fee risk, compulsory-school structure, public-school baseline, city/national childcare and international-school cost proxies, and adaptation caveats for a Ukrainian child.

- Italy's education and training system covers early childhood through adult education. Education is compulsory for **10 years**, from ages **6 to 16**, covering five years of primary, three years of lower secondary, and two years of upper secondary or regional vocational education/training. [src-617]
- Early childhood education and care is split into **0-3** educational services and **3-6** pre-primary school. Attendance is not compulsory. Eurydice states that 0-3 services charge fees, while pre-primary school for children over 3 is free. [src-617][src-618]
- The private childcare risk is material before age 3 or when public places are unavailable: Livingcost gives daycare/preschool proxies of about USD 582/month nationally, USD 569/month in Rome, USD 421/month in Naples, USD 403/month in Palermo, and USD 867/month in Milan. [src-396][src-397][src-399][src-400][src-398]
- The default future-child plan should be Italian public schooling, not an international-school budget. State schools and `paritarie` schools cover compulsory education; the State also guarantees the right to complete compulsory education. For a Ukrainian child, municipality/neighbourhood selection and Italian-language integration support should be checked once a city is chosen. [src-617]
- International school is available but not a default one-income plan: Livingcost lists international primary-school proxies of about USD 11,511/year nationally, USD 12,431/year in Rome, USD 7,022/year in Naples, USD 10,956/year in Palermo, and USD 18,202/year in Milan. This is hard to combine with the tax section's conservative forfetario net of about EUR 1,950/month. [src-396][src-397][src-399][src-400][src-398]
- Practical child-plan read: Italy is education-positive if the couple accepts Italian-language public schooling and screens Palermo/Naples/Rome by municipal school access. It becomes budget-negative if they need private nursery before age 3, a bilingual/international school, or Milan-level childcare costs on the current one-income plan.

### 5.8. Comfort of life {status: deep, depth: 1, last_updated: 2026-06-20, dod: passed}

> **DoD status**: Passed for first-pass screening. Covered: safety proxy, Ukrainian reception / institutional access, city comfort synthesis, and English-language friction. Final-neighbourhood safety, landlord experience, and city-specific Ukrainian community contacts remain practical checks.

- **Safety / public-order baseline**: World Population Review's safest-country table gives Italy a 2025 Global Peace Index score of **1.662**, TravelSafe country safety index **77** with a **medium** risk label, and US News safest-country rank **23rd**. This is not a neighbourhood-level crime audit, but it is enough to treat Italy as broadly safe for screening, with normal big-city caution in Rome/Milan/Naples and city-choice diligence for Palermo/Naples. [src-747]
- **Ukrainian reception and services**: Italy's TP / Ukraine support baseline is operationally real rather than improvised: the Integration Migrants portal confirms the 04 March 2027 horizon for Ukraine permits, and UNHCR Italy gives a practical Questura / tax-code / work-study-SSN rights summary. That helps comfort-of-life because the couple would not be relying only on private lawyers for first contact with institutions. [src-027][src-034]
- **City comfort split**: Rome is the best service-depth / climate balance but expensive; Palermo is the strongest rent-climate screen with island/southern-services tradeoffs; Naples is a cheaper mainland south option with local-quality and bureaucracy diligence; Milan has services but fails the couple's climate/rent default. Use Palermo first for budget/climate, Naples second, Rome only with strict rent control, and Milan only if income rises. [src-030][src-031][src-032][src-397][src-398][src-399][src-400]
- **Language and daily bureaucracy**: EF EPI's Italy page gives global rank **#59** and score **513**, i.e. a moderate/low-mid English environment rather than an English-first relocation base. Plan Italian-language learning early for landlords, ASL/SSN, Questura, municipality/school paperwork, tax/accounting, and daily life. [src-748]
- **Comfort verdict**: Italy is comfort-positive if the couple chooses a southern/central city and accepts Italian-language integration. It is not a low-friction bureaucracy country; the comfort plan needs an Italian-speaking accountant/immigration adviser, registered lease support, and a realistic buffer for appointments and document loops.

### 5.9. Partner (student) {status: deep, depth: 1, last_updated: 2026-06-20, dod: passed}

> **DoD status**: Passed for first-pass screening. Covered: dependent status with and without marriage, Ukrainian remote-study baseline, work/study rights by route, and one-income budget fit. Exact family-permit filing wording, dependent work rights under DN, and relationship-document standards remain application-prep checks.

- **Dependent / partner with marriage**: The captured DN / remote-worker checklist names family members as a spouse who is not separated or separating and children under 18. For this couple, marriage is the conservative low-friction dependent strategy if Italy becomes a serious DN filing target. [src-028]
- **Dependent / partner without marriage**: No captured Italy DN source safely covers an unmarried partner. Keep the working baseline as "not covered unless a serving consulate or Italian immigration lawyer confirms otherwise." This is materially worse than Spain's unmarried-partner wording and should remain a route-risk flag. [src-028]
- **Remote Ukrainian-university study**: Remote study at a Ukrainian university is best treated as compatible private activity once the partner has Italian status, not as an independent Italian student-residence route. Under TP, UNHCR Italy says beneficiaries can study and work from the moment of request; under DN, the partner should rely on spouse/dependent status rather than a Ukrainian remote-study basis. [src-034][src-028]
- **Possibility of work**: TP is clear for work/study access. For the DN family route, this pass does not capture a clean official sentence on the spouse's independent work rights, so plan conservatively: the woman's immediate baseline is dependent residence / remote study, with separate work authorization or adviser confirmation before relying on local employment. [src-034][src-028]
- **Single-income fit**: The current USD 3,000/month household can screen only if the man qualifies for the DN / remote-worker route, forfetario-style tax treatment, and controlled rent. Palermo and Naples are the realistic city budget screens; Rome is tight and Milan is poor. A child before income rises would make private nursery or international school hard to absorb. [src-293][src-396][src-397][src-398][src-399][src-400][src-617][src-618]
- **Partner verdict**: Italy is viable for the student partner mainly as a married-spouse file or separate TP file. If they do not marry and cannot both keep independent Ukrainian TP/ordinary status, Italy's partner fit is weak until official unmarried-partner evidence is captured.

### 5.10. Risk dimensions {status: deep, depth: 1, last_updated: 2026-06-25, dod: passed}

> **DoD status**: passed for screening. Covered: currency/banking, political/Ukraine-posture, ties to Ukraine, and diaspora/language adaptation. Exact bank onboarding, active Ukrainian community contacts, and city travel-cost checks remain application-prep.

- **Currency / banking risk**: Low-medium. Italy is a euro-area jurisdiction, so the main financial risk is not local-currency collapse but USD-to-EUR income conversion, bank/KYC friction, and Italian tax/social-security/reporting complexity. Registered-lease and tax-file formality are already practical route constraints in this profile. [src-028][src-287][src-288][src-293]
- **Political / Ukraine-posture risk**: Low-medium for screening. Italy has an operational Ukraine TP / permit framework through 04 March 2027 and UNHCR confirms work, study, and SSN access from the request stage; safety proxies are acceptable, though TravelSafe labels overall risk medium. [src-027][src-034][src-747]
- **Ties to Ukraine**: Medium. Italy is closer than Iberia and keeps the couple inside the EU/Schengen travel ecosystem, but southern budget cities such as Palermo/Naples may require extra connections for Ukraine-related trips. [src-027][src-034][src-397][src-399][src-400]
- **Diaspora / adaptation**: Medium-high. Institutional TP support helps, but EF places Italy below Spain/Portugal/Greece and the profile already requires Italian-speaking support for Questura, ASL/SSN, leases, tax/accounting, and schools. Keep `italian-language-integration-needed`. [src-034][src-748]

### 5.11. Bureaucracy and practicality {status: deep, depth: 1, last_updated: 2026-06-26, dod: passed}

> **DoD status**: Passed for first-pass screening. Covered: timing / filing-location baselines for TP and DN, document-localisation friction, and one neutral immigration-law contact lead. Exact serving-consulate appointment availability, lease-registration execution, ASL / Questura appointment timing, and a signed commercialista / lawyer engagement remain application-prep checks.

- **TP / Ukraine-permit filing practicality**: The practical first contact is the local `Questura`; UNHCR Italy says temporary-protection applicants should contact the Police Headquarters directly, and that the application receipt already contains the `codice fiscale` and unlocks work, study, and SSN registration from the request stage. That makes TP useful for shelter/onboarding before March 2027, but it is not a captured post-2027 settlement bridge. [src-034][src-027]
- **Digital-nomad / remote-worker timing and sequence**: The captured consular checklist is visa-first: obtain the national visa abroad, then apply for the Italian residence permit at the local Questura within eight working days after arrival. The cited consulate states the resulting DN residence permit is currently issued for one year and can be renewed locally if employment, lodging, and health-insurance conditions remain satisfied. [src-028]
- **Document burden**: Italy is practical only with a paper-heavy file. The DN checklist requires proof of highly specialized status, prior work experience, income evidence, health insurance, and a registered Italian lease / rental contract / deed; hotel stay or third-party hospitality is not accepted by the cited consulate. Treat lease registration and landlord cooperation as a legal-route constraint, not just a rent detail. [src-028]
- **Professional-contact lead**: Mazzeschi Legal Counsels is a neutral contact lead, not a recommendation. Its public contact page describes the firm as focused on Italian immigration, citizenship, corporate, and commercial law, with headquarters near Siena, a Milan representative office, email `info@mazzeschi.it`, and telephone +39 0577 926921. Use it as one candidate for screening DN / family / `partita IVA` coordination, then compare with Palermo / Naples / Rome local lawyers and commercialisti before paying. [src-809]
- **Practicality verdict**: Italy is screenable but high-friction. The most realistic path is not a walk-in DN process; it is a coordinated package: marry or otherwise solve the partner file, secure a registered lease in a budget city, align immigration evidence with the tax / `partita IVA` story, and use Italian-speaking professional help for Questura, ASL, and commercialista steps. Palermo and Naples remain the budget-first bases; Rome is service-rich but tighter; Milan is a poor default on current income.

## Block 4 — Risk dimensions (summary)

| Category | Level | Rationale |
|---|---|---|
| Currency / banking | low-medium | Euro-area currency risk is manageable; Italian KYC, registered-lease, tax and reporting formality are the bigger practical risks. [src-028][src-287][src-293] |
| Political | low-medium | Ukraine TP/permit framework and SSN/work/study rights are positive; broad safety proxy is acceptable but not friction-free. [src-027][src-034][src-747] |
| Ties to Ukraine | medium | EU location helps, but cheaper southern bases may add travel complexity for Ukraine-related trips. [src-027][src-399][src-400] |
| Diaspora / adaptation | medium-high | Italian-language bureaucracy, leases, healthcare, schools, and tax/accounting support are material adaptation needs. [src-034][src-748] |

## Block 5 — Practical verdict

- **Can relocate now**: Yes for temporary protection through 04 March 2027; long-term stay requires switching to an Italy-specific ordinary status.
- **Best legalization path for the man**: Digital nomad / remote-worker visa if he can document highly specialized IT work, income, insurance, and registered lodging.
- **Best legalization path for the woman**: Temporary protection separately if eligible; for DN-dependent planning, marriage likely matters because the captured consular guidance names spouse and minor children, not an unmarried partner.
- **Does marriage change the picture**: Yes. It likely improves DN family sponsorship options and reduces partner-status uncertainty.
- **Realism of staying after 03.2027**: Medium but not yet proven; ordinary-status switch needed, and the budget only works cleanly in lower-rent cities.
- **Healthcare/education/comfort read**: Positive for public-system access once status is secure, Italian-language public schooling, and warm southern/central city options; DN private-insurance quotes, 0-3 childcare, international-school costs, bureaucracy, and Italian-language integration can erode the one-income budget.

**Pros**:
- TP horizon currently matches the EU 04 March 2027 deadline.
- Formal DN / remote-worker route exists for highly specialized remote workers.
- Rome and southern/coastal Italy are strong climate fits.
- Palermo and Naples are materially cheaper than Rome/Milan for first-pass rent and living-cost screening.
- Public education is structurally usable if the couple accepts Italian-language schooling.
- Comfort screening is positive for safety and services if they choose Palermo/Naples/Rome deliberately and start Italian-language integration early.

**Cons / risks**:
- No captured Italy-specific post-TP bridge to ordinary residence.
- DN route requires a registered lease before/for the visa package, which can be hard before relocation.
- Unmarried partner is not clearly covered in the captured DN family sponsorship guidance.
- Rome and Milan are rent-pressure cities on one taxed Italy income.
- Northern Italy is much less attractive on winter climate.
- DN private-insurance quotes / maternity exclusions and ASL registration steps still need city-specific application-prep checks.
- Private nursery and international school are not safe default assumptions on the current one-income budget, especially in Milan/Rome.
- English is not enough for low-friction daily life; Italian-language support is needed for Questura, ASL, landlords, schools, and accountants.

## Block 6 — Practical playbook (working relocation guide)

### 6a. Before the move (what to prepare in Ukraine / Poland)
- Documents for DN: passport, qualification evidence, income proof, invoices/contracts, insurance, and Italian registered lease evidence [src-028].
- For TP: prepare Ukrainian identity and family documents; file with the Questura after arrival [src-034].
- What to do with the Polish karta pobytu: keep it valid if possible, but do not rely on it as Italian residence authorization.
- For the student partner: collect student-status documents and civil-status documents; marriage may be worth evaluating if DN family sponsorship is used because the captured family wording covers spouse/minor children, not an unmarried partner.
- For healthcare: collect DN-compliant private-insurance quotes for both adults and check maternity waiting periods / exclusions before filing.

### 6b. First month after arrival
- TP path: contact the local Questura, get the application receipt with tax number, then register for SSN via ASL [src-034].
- If planning a child later: prioritize municipalities/neighbourhoods where Italian public schools and 3-6 pre-primary places are practical, and avoid assuming an international-school budget.
- DN path: apply for `permesso di soggiorno` at the local Questura within eight working days after entry [src-028].
- Choose city carefully: Palermo first for budget/climate, Naples as a cheaper mainland south option, Rome only with strict rent control, and avoid Milan unless income rises.
- Start Italian-language setup immediately: codice fiscale / Questura / ASL / lease / school interactions should not assume English-first service. [src-748]

### 6c. First 3–6 months
- Keep income, accommodation, and insurance evidence continuously updated for DN renewal [src-028].
- Decide whether marriage is needed before attempting a family-dependent path; unmarried-partner eligibility remains unsupported by the captured DN checklist. [src-028]

### 6d. Before March 2027 (critical deadline)
- Do not wait for TP conversion unless Italy publishes a clear official mechanism.
- If Italy remains attractive, start DN / remote-worker filing while TP is still valid.

### 6e. Long-term (3–7 years)
- Confirm whether DN residence counts toward EU long-term residence and citizenship residence periods.
- Verify citizenship-by-residence timing and language/civic requirements from official Interior Ministry material.

### 6f. Relocation budget (one-time costs)

| Item | USD / EUR | Notes |
|---|---:|---|
| Visa / residence permit fees | — | National visa fee varies quarterly [src-028]. |
| Apostilles and translations | — | TBD |
| Flights for two | — | TBD |
| Rental deposit | — | Registered Italian lease is key for DN [src-028]; exact deposit / agency practice still needs live-listing checks. |
| First month rent | $399-$630 Palermo cheap/central 40 m2 proxy; $616-$941 Naples; $899-$1,430 Rome; $1,068-$1,522 Milan | Livingcost 40 m2 proxy, not a guaranteed listing [src-397][src-398][src-399][src-400]. |
| Health insurance (one year) | ≥€30,000 coverage requirement | Coverage amount, not premium [src-028]. |
| Immigration lawyer fees | — | TBD |
| Buffer / contingencies | — | TBD |
| **Total** | — | |

### 6g. Contact points and communities
- Questura: local police headquarters for TP request and DN `permesso di soggiorno` [src-028][src-034].
- ASL: local health authority for SSN doctor registration after TP request [src-034].
- Immigration lawyers / Ukrainian communities: TBD.
- ASL / SSN registration and family-doctor assignment: selected-city procedure still needs an application-prep check.
- Schools / childcare: municipal nursery and pre-primary offices in the chosen city; exact waitlists and fees still need a city/neighbourhood check.

## Block 7 — Sources

### 7a. Official primary
- EU TP extension and one-Member-State baseline: [src-002]
- Italy Integration Migrants portal on Ukraine permit renewal to March 2027: [src-027]
- Italian Consulate New York DN / remote-worker checklist: [src-028]
- Prefecture / Interior Ministry citizenship-by-residence guidance PDF: [src-029]
- Agenzia delle Entrate forfetario eligibility / tax mechanics and AA9/12 `partita IVA` route: [src-287][src-288][src-289]
- INPS `Gestione Separata` 2026 contribution circular: [src-290]

### 7b. Reputable secondary
- UNHCR Italy temporary-protection guide: [src-034]
- Italy SSN / public-private healthcare guide for foreigners: [src-616]
- Eurydice Italy education-system and early-childhood profiles: [src-617][src-618]
- PwC Italy individual tax summaries for PIT, residence, social security, and filing: [src-291]

### 7c. Community and forums (mandatory date of original post)
_(none yet)_

### 7d. Statistical / commercial
- Climate to Travel: Rome, Milan, Palermo [src-030][src-031][src-032]
- Current Results: annual sunshine in Italy [src-033]
- Forfetario IT/communications profitability-coefficient table and run-date USD/EUR FX feed: [src-292][src-293]
- Livingcost Italy cost/rent, doctor-visit, childcare, and international-school price proxies: national, Rome, Milan, Naples, Palermo [src-396][src-397][src-398][src-399][src-400]
- World Population Review safest-country table and EF EPI Italy English-proficiency page: [src-747][src-748]

### 7e. Not found
- Official-primary DN checklist from an Italy-in-Ukraine consular page.
- More favorable evidence, if any, that unmarried partners can be sponsored under Italy's DN family route; current operational baseline is spouse/minor children only.
- Commercialista confirmation of the exact ATECO code, forfetario eligibility, 5% startup-rate eligibility, and invoice/VAT treatment for the IT worker's actual client setup.
- Live-listing confirmation for Rome/Milan/Naples/Palermo rents, registered-lease availability for DN filing, deposits, agency fees, and landlord requirements for foreign remote workers.
- DN-compliant private-insurance premiums for two young adults, maternity waiting periods / exclusions, and selected-city ASL registration steps.
- Municipal nursery waitlists/fees and school-language support in Palermo / Naples / Rome after city selection.
- Final-neighbourhood safety, Ukrainian community contacts, Italian-language course options, and exact DN spouse-permit work-right wording.

## Block 8 — Open questions and verification markers

- `vq-011`: resolved in run-009 as a conservative no-bridge baseline using EU / Italy / UNHCR sources: ordinary status required before TP expiry unless Italy later publishes a bridge.
- `vq-012`: resolved in run-009 for operational planning: the captured consular checklist supports spouse/minor-child sponsorship only; unmarried partner remains not safely covered unless later evidence changes this.
- `vq-122` resolved for screening in run-138: DN-compliant insurance quotes, maternity exclusions/waiting periods, and city-specific ASL registration steps remain application-prep checks.
- Italy comfort and partner/student fit are now screenable; final filing still needs dependent-spouse work-right wording, unmarried-partner confirmation if not marrying, and city-level integration/community checks.
