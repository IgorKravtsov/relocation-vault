---
country: Bulgaria
tier: null
depth_score: 2.0
last_updated: 2026-06-07T22:15:00Z
sections_completed: ["5.2"]
sections_partial: ["5.1", "5.3"]
sections_pending: ["5.4", "5.5", "5.6", "5.7", "5.8", "5.9", "5.10", "5.11"]
risk_flags: ["self-employment-permit-3-year-cap", "dual-citizenship-restriction-for-non-eu-naturalized", "self-employment-requirements-not-operational", "bulgaria-self-employed-contribution-and-status-fit-gap"]
sources_used: ["src-002", "src-079", "src-080", "src-081", "src-082", "src-083", "src-084", "src-085", "src-086", "src-087", "src-089", "src-090", "src-118", "src-328", "src-329", "src-330", "src-331"]
unverified_count: 1
schema_version: 2.0.0
---

# Bulgaria

> **All content in this file is written in English** per `vault-protocol.md` language rule.

## Block 1 — Summary

- **Tier**: TBD (insufficient data for tier assignment after first pass)
- **depth_score**: 2.0
- **Last updated**: 2026-06-07
- **Tier rationale**: TBD. Bulgaria offers a self-employment residence route with a 3-year cap and a 5-year path to permanent residence, but the 3-year self-employment permit limitation and the absence of a captured TP-to-ordinary-residence bridge create operational constraints. Dual-citizenship restrictions for naturalized non-EU nationals are a further consideration. A tier will be assigned after deeper research.

## Block 2 — Scoring

| Criterion | Score (1–10) | Confidence | Brief rationale | Profile section |
|---|---:|---|---|---|
| Legalization (now + post-03.2027) | — | N/A | [verification required] | §5.1 |
| Climate | — | N/A | [verification required] | §5.2 |
| Taxes | — | medium | First-pass 10% PIT / statutory-expense / social-insurance / VAT baseline; exact immigration-status and contribution package fit still needs verification | §5.3 |
| Cost of living | — | N/A | [verification required] | §5.4 |
| Rent (decent 2BR) | — | N/A | [verification required] | §5.5 |
| Healthcare | — | N/A | [verification required] | §5.6 |
| Education (future child) | — | N/A | [verification required] | §5.7 |
| Comfort of life | — | N/A | [verification required] | §5.8 |
| Fit for couple with single income | — | N/A | [verification required] | §5.9 |

**Weighted score**: — (compute when all criteria are scored)

## Block 3 — Profile by section

### 5.1. Legalization {status: partial, depth: 1, last_updated: 2026-05-28, dod: pending}

> **DoD**: all applicable paths listed with official-primary source links; income thresholds verified as claims; document checklists with apostille/translation notes; post-March-2027 transition pathway documented with law reference; Polish karta pobytu interaction explicitly addressed; personal playbook for our couple included; all facts confidence ≥ medium.

#### Now (until 03.2027)

**Temporary Protection (TP)**

Bulgaria, as an EU Member State, applies the EU-wide temporary protection for displaced persons from Ukraine extended until **04 March 2027** by Council Implementing Decision (EU) 2025/1460 [src-002]. UNHCR Bulgaria confirms the local operational baseline: eligible people fleeing Ukraine can register for temporary protection in Bulgaria without going through the standard asylum procedure, receive a Personal Foreigner's Number (PFN/ЛНЧ) and temporary registration document with photo, and may need to complete an address card at the police station for the place where they settle [src-089].

UNHCR Bulgaria lists TP rights as the right to remain in Bulgaria, access to shelter/social welfare assistance, medical care, education, and the ability to work without a permit [src-089]. UNHCR also published a 25 February 2026 notice that Bulgaria extended TP until **04 March 2027** and that beneficiaries must renew registration cards at State Agency for Refugees registration centres [src-090]. This is enough to close the local TP-procedure blocker at medium-high confidence, though Bulgarian MVR's own Ukraine page remained WAF-protected during capture [src-088].

**Self-employment residence route**

For a remote IT worker, the most relevant ordinary route is the **self-employment permit** [src-079]:

- A **self-employment permit** is granted by the central administration of the Bulgarian Employment Agency on the basis of a detailed business plan assessing the economic and social impact of the activity.
- Once the permit is granted, the applicant must apply for a **Type D visa** at a Bulgarian embassy or consulate abroad.
- After entering Bulgaria, a **residence permit** must be obtained from the Migration Directorate of the Ministry of Interior.
- The self-employment permit is valid for a **maximum of 1 year**, renewable for up to **3 years total**.
- After 3 years, the applicant must return to their home country for **1 month** before reapplying via the same procedure.
- The residence permit duration is aligned with the self-employment permit and must be renewed no later than 14 days before expiry.
- **Change of status** requires a new application from outside Bulgaria.

Verification baseline: the captured EU Immigration Portal route does **not** provide a simple published income floor or minimum capital number for the self-employment permit. It frames the decisive test as an Employment Agency permit based on a detailed business plan and economic/social-impact assessment [src-079]. Operationally, this route should be treated as **not yet executable without Bulgarian Employment Agency / Migration Directorate confirmation or counsel**, rather than as a fixed-threshold digital-nomad substitute.

**No captured dedicated digital-nomad visa**

Bulgaria does not appear to offer a dedicated digital-nomad visa comparable to Croatia, Greece, or Portugal. The self-employment route is the closest alternative for a remote worker.

**Family reunification**

Per the EU Immigration Portal, family members (spouse and minor children) of a legally residing third-country national may apply for family reunification [src-080]. Unmarried partners are not explicitly covered in the captured sources.

**Polish karta pobytu interaction**

A Polish residence title does not substitute for Bulgarian authorization. If the Polish status is temporary protection, the EU one-Member-State TP rule applies: the couple cannot hold TP in both Poland and Bulgaria simultaneously. If the Polish status is an ordinary residence permit, it does not automatically confer any right to reside in Bulgaria; a Bulgarian status must be obtained independently.

#### After 4 March 2027

No Bulgaria-specific transition mechanism from temporary protection to an ordinary residence permit has been captured. UNHCR Bulgaria confirms the TP validity horizon and card-renewal mechanics through 04 March 2027, but does not describe any automatic conversion into ordinary residence [src-089][src-090]. Conservative operational baseline: **plan an ordinary Bulgarian route (e.g., self-employment) before TP expiry** unless a future official transition rule appears.

#### Residence without local employer

Remote work for foreign clients is not explicitly recognized as a standalone residence basis in Bulgaria. The self-employment route requires a Bulgarian-registered activity and a detailed business plan. [verification required] Whether pure remote freelancing (without Bulgarian business registration) qualifies for self-employment status.

#### PR and citizenship

- **Permanent residence**: eligible after **5 years of legal residence** in Bulgaria. During the 5-year period, the applicant cannot leave Bulgaria for more than **6 consecutive months** or a total of **10 months** [src-079].
- **Citizenship**: naturalization is possible after **5 years of residence** (or 3 years if married to a Bulgarian citizen) plus a good command of the Bulgarian language [src-081].
- **Dual citizenship**: Bulgaria permits dual citizenship only for native-born citizens, EU/EEA/Swiss citizens, spouses of Bulgarian citizens, and naturalized persons of Bulgarian origin or from countries with reciprocity agreements. Naturalized citizens from non-EU countries (including Ukraine, unless a reciprocity agreement exists) are generally required to renounce their original nationality [src-081]. [verification required] Whether Ukraine has a reciprocity agreement with Bulgaria on dual citizenship.

#### Personal playbook for our couple

TBD pending deeper research on exact self-employment permit requirements, income thresholds, and tax implications.

### 5.2. Climate {status: deep, depth: 1, last_updated: 2026-05-30, dod: passed}

> **DoD**: January/July temperatures in 3+ cities; sunny days; humidity; year-round comfort.

Bulgaria has a **continental climate** in the north and interior, with cold winters and warm to hot summers; the Black Sea coast is slightly milder. The country is fairly sunny, with **2,200–2,300 annual sunshine hours** in most areas, rising to over 2,600 hours in the southwest (Sandanski) [src-082].

**Sofia** (capital, 550 m altitude) [src-082][src-085]:
- **January**: average 0°C (min -4°C, max +3°C)
- **July**: average 21.5°C (min 16°C, max 27°C)
- Annual sunshine: ~2,260 hours
- January humidity: ~84%
- Winters are cold with frequent snow; summers are warm and sunny with cool nights. Air pollution (PM10/PM2.5) can be severe in winter due to temperature inversions.

**Plovdiv** (southern plain, Thracian Plain) [src-083][src-086]:
- **January**: average 1.5°C (min -3°C, max +6°C)
- **July**: average 24°C (min 17°C, max 31°C)
- Annual sunshine: ~2,340 hours
- January humidity: ~81%
- Hotter summers than Sofia; heat waves can reach 38–40°C. Winters are milder than Sofia but still cold.

**Varna** (Black Sea coast) [src-084][src-087]:
- **January**: average 2°C (min -3°C, max +7°C)
- **July**: average 24°C (min 17°C, max 29°C)
- Annual sunshine: ~2,300 hours
- January humidity: ~81%
- Black Sea influence moderates temperatures; milder winters than inland, warm summers. Sea temperature in summer: 24–27°C.

WeatherSpark provides monthly percentages for the broader clearer-sky categories (clear, mostly clear, or partly cloudy). Converting those monthly percentages to annual day-equivalent proxies gives: **Sofia ~223 clearer-sky day-equivalents/year**, **Plovdiv ~230**, and **Varna ~215** [src-118]. This is not an official meteorological sunny-day count; it is a medium-confidence clearer-sky proxy, but it closes the climate DoD blocker for practical screening.

### 5.3. Taxes {status: partial, depth: 1, last_updated: 2026-06-07, dod: pending}

> **DoD**: effective tax burden for a USD 3,000/month foreign-client IT worker; registration route; PIT, social/health, VAT and filing mechanics; marriage/partner tax effect; concrete gross-to-net example; all critical facts confidence >= medium. This pass opens the section but does not pass DoD because the exact Bulgarian self-employment / immigration-status fit and contribution package for a Ukrainian remote IT worker need accountant or authority confirmation.

#### Tax residence and scope

PwC Bulgaria states that Bulgarian tax residents are taxed on worldwide income, while non-residents are taxed only on Bulgarian-source income. Rendering services in Bulgaria is treated as Bulgarian-source income regardless of where or by whom it is paid [src-328]. Tax residence is triggered by one or more tests: permanent address in Bulgaria plus centre of vital interests, more than 183 days in any 12-month period, assignment abroad by a Bulgarian company/state, or centre of vital interests in Bulgaria; treaty tie-breakers can override domestic tests [src-328].

#### PIT and freelance expense baseline

Bulgaria has a simple headline personal-income-tax regime: a flat **10% PIT** applies to all personal income, with exceptions not relevant to this first pass [src-328]. For freelancers / civil contractors / private practitioners, PwC reports a **25% statutory expense deduction** from gross income before PIT; mandatory social-security contributions borne by the individual are tax-deductible in full when supported by documentation [src-329]. This makes Bulgaria mathematically attractive on PIT, but the immigration route is still the bottleneck: the profile's legal section does not yet prove that a Ukrainian remote IT worker can safely operate as a Bulgarian freelancer under the self-employment residence route without a Bulgarian Employment Agency / Migration Directorate approval file.

#### Social and health contributions

PwC gives the 2026 freelancer insurance-base limits: minimum **EUR 550.66/month** and maximum **EUR 2,111.64/month** from 01 January 2026 [src-329]. It also notes that non-EU/EEA nationals may be subject to social-security contributions under certain conditions, while health-insurance contributions apply if they have a Bulgarian permanent residence permit [src-329]. Because this pass did not capture a clean official NRA table for the exact self-insured foreigner package, the worked example uses a planning stress test rather than a passed-tax conclusion: 27.8% on the capped base for pension + health-like coverage, with a 31.3% sensitivity if the fuller sickness/maternity package applies. This assumption must be confirmed before scoring.

#### VAT, filing, and spouse mechanics

The standard VAT rate is **20%** [src-329]. PwC's corporate VAT summary says mandatory VAT registration from 01 January 2026 applies when taxable turnover exceeds **EUR 51,130** in the current or previous calendar year, with a new 7-day registration deadline after the threshold is exceeded [src-330]. At USD 36,000/year, the couple's current income is below this headline threshold, but foreign-client B2B place-of-supply / reverse-charge handling remains an accountant-level check.

Annual PIT returns are generally due by **30 April** of the following year, with a 5% discount on outstanding PIT if filed electronically and paid by 31 March, capped at EUR 255.65; freelancers must pay quarterly advance taxes regardless of whether the payer is Bulgarian or foreign [src-329]. Spouses are treated as separate taxpayers and no income splitting is allowed [src-329].

#### Worked example at USD 3,000/month

Run-date FX from open.er-api is **1 USD = BGN 1.690673**, so USD 3,000/month is about **BGN 5,072/month** or **BGN 60,864/year** [src-331]. Using the 2026 maximum freelancer insurance base of about BGN 4,130/month (EUR 2,111.64 at the fixed EUR/BGN peg), a planning calculation is:

1. Gross: **BGN 5,072/month**.
2. 25% statutory freelance expense deduction: **BGN 1,268/month**.
3. Social/health stress test at 27.8% of capped base: **BGN 1,148/month**.
4. PIT base after statutory expense and contributions: about **BGN 2,656/month**.
5. 10% PIT: about **BGN 266/month**.
6. Estimated net: about **BGN 3,658/month**, or **USD 2,164/month**.

If the fuller 31.3% contribution package applies, the sensitivity falls to about **BGN 3,528/month** or **USD 2,087/month**. Conservative conclusion: Bulgaria's first-pass tax math is potentially favorable relative to many EU routes, but section 5.3 remains partial until Bulgarian NRA / accountant evidence confirms exact self-insured status, foreign-client IT classification, health-insurance obligation for the couple's residence posture, VAT / reverse-charge handling, and whether this tax registration is compatible with the immigration route.

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

- **Can relocate now**: TBD
- **Best legalization path for the man**: TBD (self-employment route appears most relevant, but exact requirements unclear)
- **Best legalization path for the woman**: TBD
- **Does marriage change the picture**: TBD (marriage to a Bulgarian citizen reduces citizenship timeline from 5 to 3 years; marriage to the working partner may enable family reunification)
- **Realism of staying after 03.2027**: TBD

**Pros**:
- TBD

**Cons / risks**:
- TBD

## Block 6 — Practical playbook (working relocation guide)

### 6a. Before the move (what to prepare in Ukraine / Poland)
- Documents (with apostille / notarized translation markers): TBD
- Steps in Ukrainian government agencies: TBD
- What to do with the Polish karta pobytu: TBD
- Financial preparation (USD cushion): TBD
- For the student partner (academic certificates, translations): TBD
- Submitting visa/permit application from abroad: TBD

### 6b. First month after arrival
- Address registration: TBD
- Submitting residence application (if not done from abroad): TBD
- Bank account opening: TBD
- Tax ID / social security number: TBD
- Long-term housing: TBD
- Health insurance / public health registration: TBD
- SIM card, internet, utilities: TBD

### 6c. First 3–6 months
- Tax registration as self-employed / freelancer: TBD
- Transferring partner to dependent / partner / student status: TBD
- Marriage (if applicable to scenario): TBD
- Integration (language courses, communities): TBD

### 6d. Before March 2027 (critical deadline)
- What must be in hand by this date: TBD
- Fallback path if TP→VNZh transition fails: TBD

### 6e. Long-term (3–7 years)
- PR: when to apply, what's required: TBD
- Citizenship: conditions and timeline: TBD

### 6f. Relocation budget (one-time costs)

| Item | USD / EUR | Notes |
|---|---|---|
| Visa / residence permit fees | — | TBD |
| Apostilles and translations | — | TBD |
| Flights for two | — | TBD |
| Rental deposit | — | TBD |
| First month rent | — | TBD |
| Health insurance (one year) | — | TBD |
| Immigration lawyer fees | — | TBD |
| Buffer / contingencies | — | TBD |
| **Total** | — | |

### 6g. Contact points and communities
- Immigration lawyers (2–3 with contacts): TBD
- Ukrainian / Russian-speaking diaspora (Telegram channels, FB groups): TBD
- Expat blogs: TBD
- NGOs / Caritas / refugee help: TBD

## Block 7 — Sources

### 7a. Official primary
_(none yet — Bulgarian Ministry of Interior and Employment Agency pages were WAF-protected or not directly capturable)_

### 7b. Reputable secondary
- [src-079] EU Immigration Portal — Self-employed worker in Bulgaria (official-secondary)
- [src-080] EU Immigration Portal — Family member in Bulgaria (official-secondary)
- [src-081] Wikipedia — Bulgarian nationality law (aggregator)
- [src-089] UNHCR Bulgaria — Arrival from Ukraine (reputable-secondary)
- [src-090] UNHCR Bulgaria — TP extended until 04 March 2027 (reputable-secondary)
- [src-328] PwC Worldwide Tax Summaries — Bulgaria individual taxes and residence (reputable-secondary)
- [src-329] PwC Worldwide Tax Summaries — Bulgaria other taxes, deductions, and tax administration (reputable-secondary)
- [src-330] PwC Worldwide Tax Summaries — Bulgaria corporate VAT context (reputable-secondary)

### 7c. Community and forums (mandatory date of original post)
_(none yet)_

### 7d. Statistical / commercial
- [src-082] Climate to Travel — Bulgaria / Sofia climate (commercial)
- [src-083] Climate to Travel — Plovdiv climate (commercial)
- [src-084] Climate to Travel — Varna climate (commercial)
- [src-085] Wikipedia — Sofia climate table (aggregator)
- [src-086] Wikipedia — Plovdiv climate table (aggregator)
- [src-087] Wikipedia — Varna, Bulgaria climate table (aggregator)
- [src-118] WeatherSpark — Bulgaria city cloud-cover climate pages (commercial)
- [src-331] open.er-api.com — USD exchange-rate feed (commercial)

### 7e. Not found
> Explicit list of resources searched for but not found. Signal for future iterations.

- Bulgarian Ministry of Interior Ukraine/TP page (WAF-protected, not capturable via Jina AI)
- Bulgarian Employment Agency self-employment permit exact document checklist / business-plan practice. No fixed income or capital threshold was captured; do not assume one exists without primary confirmation.
- Bulgaria dedicated digital-nomad visa
- Official meteorological annual sunny/clear-day counts for Sofia, Plovdiv, and Varna. WeatherSpark clearer-sky day-equivalent proxies are now captured for §5.2 screening.
- Bulgaria-Ukraine dual-citizenship reciprocity agreement status
- Bulgarian NRA official 2026 self-insured contribution table / exact foreigner health-insurance obligation and self-employed IT classification. Direct NRA capture failed during run-065, so the tax worked example uses a PwC-backed planning stress test and remains partial.
- Accountant-level VAT / reverse-charge and immigration-status compatibility for a Ukrainian foreign-client IT freelancer.

## Block 8 — Open questions and verification markers

> All `[verification required]` items for this country. Links to the corresponding entries in `verification-queue.md` via item ID.

- `vq-097` — resolved to a conservative screening baseline: keep the statutory-expense / contribution stress test as partial only; exact contribution package, foreigner health-insurance obligation, IT classification, VAT / reverse-charge handling, and migration-route fit remain accountant/application-prep checks before filing.
