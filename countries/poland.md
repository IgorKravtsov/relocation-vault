---
country: Poland
tier: null
depth_score: 3.0
last_updated: 2026-06-12T07:13:26Z
sections_completed: ["5.2", "5.4", "5.5"]
sections_partial: ["5.1", "5.3"]
sections_pending: ["5.6", "5.7", "5.8", "5.9", "5.10", "5.11"]
risk_flags: ["poland-zus-social-contribution-gap", "poland-ryczalt-it-rate-fit-gap", "warsaw-rent-pressure"]
sources_used: ["src-002", "src-062", "src-063", "src-064", "src-065", "src-066", "src-067", "src-091", "src-293", "src-320", "src-321", "src-322", "src-323", "src-501", "src-502", "src-503", "src-504"]
unverified_count: 4
schema_version: 2.0.0
---

# Poland

> **All content in this file is written in English** per `vault-protocol.md` language rule.

## Block 1 — Summary

- **Tier**: TBD (set after sufficient evidence; justify with sources)
- **depth_score**: 3.0
- **Last updated**: 2026-06-12
- **Tier rationale**: TBD. Poland is a uniquely relevant case because one partner already holds a Polish `karta pobytu` (residence permit), which creates a family-reunification path that does not exist for most other countries in the set. The new CUKR card (May 2026) also provides a clear post-2027 bridge for Ukrainian temporary-protection holders. If both paths hold, Poland could rate Tier 1 or Tier 2; the first tax pass suggests the self-employed tax answer can be workable, but exact ZUS and IT lump-sum classification require accountant confirmation.

## Block 2 — Scoring

| Criterion | Score (1–10) | Confidence | Brief rationale | Profile section |
|---|---|---:|---|---|
| Legalization (now + post-03.2027) | — | N/A | [verification required] | §5.1 |
| Climate | — | N/A | [verification required] | §5.2 |
| Taxes | — | medium | First-pass self-employed model: 12% IT `ryczalt` may leave about PLN 8,777 / USD 2,412 per month before uncaptured ZUS social contributions; exact classification and ZUS table pending. | §5.3 |
| Cost of living | — | medium | Livingcost first-pass screen: national one-person total with rent is about $1,393/month; Warsaw is expensive at about $2,026/month, while Krakow/Wroclaw screen around $1,662/month before healthcare, immigration, and accountant costs. | §5.4 |
| Rent (decent 2BR) | — | medium | The 40 m2 1BR proxy is workable in Krakow/Wroclaw ($737-$973/month) but Warsaw is rent-pressured ($945 cheap / $1,304 center); 80 m2 3BR is an upper stress test, not the default. | §5.5 |
| Healthcare | — | N/A | [verification required] | §5.6 |
| Education (future child) | — | N/A | [verification required] | §5.7 |
| Comfort of life | — | N/A | [verification required] | §5.8 |
| Fit for couple with single income | — | N/A | [verification required] | §5.9 |

**Weighted score**: — (compute when all criteria are scored)

## Block 3 — Profile by section

### 5.1. Legalization {status: partial, depth: 1, last_updated: 2026-05-27, dod: pending}

> **DoD**: all applicable paths listed with official-primary source links; income thresholds verified as claims; document checklists with apostille/translation notes; post-March-2027 transition pathway documented with law reference; Polish karta pobytu interaction explicitly addressed; personal playbook for our couple included; all facts confidence ≥ medium.

#### Now (until 03.2027)

**Temporary Protection (PESEL UKR)**
- Ukrainian citizens who arrived in Poland after 23 February 2022 can obtain temporary protection (status UKR) evidenced by a PESEL UKR number. [src-002][src-064]
- The EU-level temporary protection is extended until 04 March 2027. [src-002]
- Status UKR gives the right to reside, work (with employer notification to the labour office), access to medical care, education, and social assistance. [src-063]
- Status UKR is cancelled if the holder leaves Poland for more than 30 days. [src-063]

**CUKR card — new post-TP bridge (launched 04 May 2026)**
- The CUKR card (`karta pobytu z adnotacją "Poprzednio posiadacz ochrony czasowej"`) is a 3-year temporary residence permit on special conditions for former Ukrainian TP holders. [src-062][src-063]
- **Eligibility** (must meet all four conditions): [src-062]
  1. Hold a valid PESEL UKR on the day of application.
  2. Held a valid PESEL UKR on 04 June 2025.
  3. Hold a valid PESEL UKR on the day the voivode issues the card.
  4. Held status UKR continuously for at least 365 days.
- **Family scope**: spouses, minor children, minor children of the spouse, and closest family members who hold a Karta Polaka. Children born in Poland after 23 February 2022 can obtain the card if their mother holds a CUKR card. [src-062][src-063]
- **Application**: exclusively electronic via the dedicated MOS portal (`mos.cudzoziemcy.gov.pl`). No in-person appointment is required for submission; the applicant visits the voivode office only to collect the finished card. [src-062]
- **Deadline**: applications can be submitted until 04 March 2027. [src-062][src-063]
- **Fees**: 340 PLN stamp duty for the residence permit + 100 PLN for the card production. [src-062]
- **Rights**: full labour-market access (no additional work permit, no employer notification), right to conduct economic activity on the same terms as Polish citizens, Schengen travel up to 90 days in any 180-day period, and all rights of a standard temporary-residence permit holder. [src-062][src-063]
- **Caveats**: upon receiving the CUKR card, the holder loses status UKR and associated benefits (including free accommodation in collective centres). The holder must inform the voivode of any address change within 15 working days. Leaving Poland for more than 6 months causes loss of the permit. [src-063]
- **Next permit**: after the 3-year CUKR period, the next temporary residence permit is granted under general rules (i.e. the applicant must demonstrate a specific purpose such as work, business, or family reunification). [src-063]

**Family reunification via the partner's existing Polish `karta pobytu`**
- One partner in the couple already holds a Polish `karta pobytu` (residence permit). This creates a potential family-reunification path under Article 159 of the Act on Foreigners.
- Verification baseline from a Polish voivodeship information portal: the operational family-reunification file is built around Article 159 conditions, proof of family ties (for example marriage certificate / birth certificate), health insurance, accommodation, and stable regular income. The portal gives income baselines of **PLN 776 net for a single person** or **PLN 600 net per family member**, plus PLN 340 stamp duty and PLN 50 residence-card fee after approval [src-091].
- The captured official-secondary guidance does **not** list an unmarried partner as a family-reunification beneficiary. For this couple, the safe planning baseline is therefore: **marriage is required before relying on family reunification via the existing Polish `karta pobytu`; an unmarried partner should use independent eligibility (CUKR/TP, study, work/business) unless a lawyer obtains a different written interpretation** [src-091].
- The source does not condition sponsorship on a Polish local employer. It asks for stable and regular income sufficient for the household, so foreign-client remote income may be usable if it is documented and accepted by the voivode; verify document practice before filing [src-091].

**Business / self-employed temporary residence**
- [verification required] Poland offers a temporary residence permit for the purpose of conducting business activity. Details on minimum capital, business-plan requirements, and processing times need primary-source capture.
- [verification required] There is no dedicated digital-nomad visa in Poland comparable to Portugal's D8 or Spain's DN visa. Remote workers generally need to qualify under business-activity or work-permit routes.

#### After 4 March 2027

- For Ukrainian citizens who switch to the CUKR card before the TP deadline, the post-2027 path is a 3-year temporary residence permit. After that, they must transition to a general-purpose temporary residence permit (work, business, family, etc.). [src-062][src-063]
- The CUKR period counts toward the required residence period for EU long-term residence (`zezwolenie na pobyt rezydenta długoterminowego UE`). [src-062]
- [verification required] The exact counting rules (whether CUKR time counts in full, and whether prior TP time counts partially) need an official-primary legal source.
- For the partner who already holds a standard Polish `karta pobytu`, the post-2027 horizon is governed by their existing permit's expiry and renewal rules, not by the TP/CUKR framework.

#### Residence without local employer

- The CUKR card explicitly allows conducting economic activity (self-employment / business) on the same terms as Polish citizens. [src-063]
- [verification required] For non-CUKR applicants, the standard business-activity residence permit requires proof of sustainable business activity. Minimum income thresholds and registration procedures need primary-source capture.

#### PR and citizenship

- [verification required] General Polish rules: permanent residence (`zezwolenie na pobyt stały`) is typically available after 5 years of continuous temporary residence; EU long-term residence after 5 years of legal continuous residence.
- [verification required] Citizenship by naturalisation: generally 3 years on permanent residence or 10 years of total legal residence, plus B1 Polish language and stable income/source of livelihood.
- [verification required] Dual citizenship: Poland does not formally recognise dual citizenship, but in practice it is tolerated (Polish citizens who acquire another citizenship retain Polish citizenship, and foreigners naturalising in Poland are not required to renounce their original citizenship).

#### Personal playbook for our couple

- **If the partner with the Polish `karta pobytu` can sponsor the other**: marriage would likely create the strongest family-reunification path. The sponsored partner could obtain a temporary residence permit for family reunification, with work rights.
- **If neither can use family reunification**: the CUKR card is the most straightforward path for a Ukrainian citizen who has been in Poland on TP for at least 365 days and held PESEL UKR on 04 June 2025. Apply electronically before 04 March 2027.
- **For the IT worker**: after obtaining CUKR or family-reunification residence, register as a self-employed / sole proprietor (`jednoosobowa działalność gospodarcza`) to invoice foreign clients legally.
- **For the student partner**: a dependent residence permit via family reunification would allow legal residence without needing a separate student status. Alternatively, enrolling in a Polish university could open a student-residence path.

### 5.2. Climate {status: partial, depth: 1, last_updated: 2026-05-27, dod: pending}

> **DoD**: January/July temperatures in 3+ cities; sunny days; humidity; year-round comfort.

**Warsaw** [src-065]
- January average: -1.4 °C (min -4 °C, max 1 °C)
- July average: 19.8 °C (min 14 °C, max 25 °C)
- Annual sunshine hours: ~2,000
- Precipitation: ~550 mm/year, spread relatively evenly
- Comfort: cold, grey winters with frequent snow; pleasantly warm summers; occasional heat waves above 30 °C

**Kraków** [src-066]
- January average: -1.6 °C (min -4 °C, max 2 °C)
- July average: 19.6 °C (min 14 °C, max 25 °C)
- Annual sunshine hours: ~1,455
- Precipitation: ~675 mm/year
- Comfort: similar to Warsaw but slightly more precipitation and fewer sunshine hours; winter temperature inversions can trap smog

**Wrocław** [src-067]
- January average: -0.1 °C (min -3 °C, max 3 °C)
- July average: 19.7 °C (min 14 °C, max 25 °C)
- Annual sunshine hours: ~1,885
- Precipitation: ~540 mm/year
- Comfort: marginally milder winters than Warsaw/Kraków; warm summers

**Summary**
- Poland has a moderately continental climate. Winters are cold and grey; summers are warm and pleasant. [src-065][src-066][src-067]
- [verification required] Direct annual sunny-day counts are not yet captured; only sunshine-hour totals are available.
- The climate is not ideal for the couple's preference for warm/short winters, but it is manageable with proper housing and clothing.

### 5.3. Taxes {status: partial, depth: 1, last_updated: 2026-06-07, dod: pending}

> **DoD**: effective rate at $3000/mo computed; registration procedure for applicable regime; gross->net example; new-resident reliefs; marriage tax effect.

#### Tax-residence baseline
- Polish tax residents pay PIT on worldwide income; non-residents pay Polish PIT only on Polish-source income. PwC states that an individual is resident if they have a centre of personal or business interests in Poland or spend more than 183 days in a fiscal year in Poland. [src-320][src-322]
- For a couple actually living in Poland after CUKR / family reunification, assume Polish tax residence and worldwide-income reporting unless a tax adviser confirms a non-resident treatment for a short first year. [src-320][src-322]

#### Self-employed tax regimes for a foreign-client IT worker
- Poland lets natural-person entrepreneurs choose between three main business-activity taxation forms: general tax scale (12% / 32%), flat-rate tax (19%), or lump-sum tax on registered revenue; tax scale is the default unless another form is chosen. [src-323]
- PwC similarly states that sole traders can choose the scale, a 19% flat income tax, or lump-sum tax subject to conditions; it specifically notes that income from certain designated IT services is taxed at a 12% lump-sum rate. [src-320]
- For this couple's current profile (foreign clients, low expenses, about USD 36,000/year revenue), the most promising first-pass tax model is **registered sole proprietorship + lump-sum revenue tax (`ryczalt`) at 12% for designated IT services**, but the exact PKD/PKWiU classification and whether the client's activity is 12% rather than another lump-sum rate must be confirmed by a Polish accountant. [src-320][src-323]
- The alternative conservative model is flat 19% PIT on income plus health contribution, but it usually looks worse if the freelancer has low deductible costs. [src-320][src-321][src-323]

#### Social and health contributions
- Self-employed people generally pay ZUS social-security contributions as lump sums independent of actual income, with a basis tied to the forecast average monthly wage. PwC also notes startup relief: no social-security contributions for the first six months of self-employment and lower preferential contributions for the next 24 months, subject to conditions. [src-321]
- Entrepreneur health contributions depend on the chosen tax form: 9% of income for scale, 4.9% of income for the 19% flat-rate tax, and a revenue-band-based fixed contribution for lump-sum taxpayers. PwC gives the lump-sum health band for annual revenue between PLN 60,000 and PLN 300,000 as **PLN 830.58/month**. [src-321]
- This pass did **not** capture the official 2026 ZUS monthly social-contribution table for normal / preferential entrepreneurs. Therefore the worked example below is a startup-relief or before-social-contribution baseline, not a complete long-term net figure. [verification required]

#### Registration and filing mechanics
- Registration route is expected to be Polish sole proprietorship / CEIDG (`jednoosobowa dzialalnosc gospodarcza`) after the person has a residence status allowing economic activity (CUKR explicitly allows economic activity on the same terms as Polish citizens). [src-063]
- Annual PIT returns are generally due by 30 April of the following year; PwC says this also applies to taxpayers reconciling lump-sum-tax income for 2022 and following years. [src-322]
- Taxes are paid via an individual tax micro-account using PESEL for most individual taxpayers and NIP for entrepreneurs / tax or social-security remitters. [src-322]

#### Worked example at USD 3,000/month
- Run-date exchange reference: NBP USD/PLN mid-rate on 2026-06-05 was 3.6392, so USD 3,000/month is about **PLN 10,918/month** or **PLN 131,011/year**. [src-293]
- If the IT activity safely qualifies for the 12% lump-sum rate, monthly lump-sum tax is about **PLN 1,310** (12% of revenue). [src-320]
- With the PwC lump-sum health band for PLN 60,000-300,000 revenue, health contribution is **PLN 830.58/month**. [src-321]
- **Startup-relief / before-ZUS-social baseline**: PLN 10,918 gross - PLN 1,310 lump-sum tax - PLN 831 health contribution = about **PLN 8,777/month net**, roughly **USD 2,412/month**, before accounting fees and any ZUS social contributions not captured in this pass. [src-293][src-320][src-321]
- Planning interpretation: Poland is tax-workable at the couple's current income if 12% `ryczalt` applies and startup relief is available, but the full long-term result may be materially lower once normal ZUS social contributions start.

#### Marriage and one-income household effect
- PwC says married Polish tax residents may choose joint or separate filing if conditions are met, and joint filing is often more beneficial when one spouse has no income or a lower tax rate. [src-322]
- Important caveat: PwC also states that joint reconciliation is available only if neither spouse conducts business activity taxed differently than progressive rates up to 32%; using 19% flat tax or lump-sum taxation can therefore block the main joint-filing benefit. [src-322]
- For this couple, marriage mainly matters for immigration / family reunification first. Tax-wise, marriage may help only if they choose the progressive tax scale rather than lump-sum or flat tax, which may not be optimal for IT income.

#### DoD status
- Section 5.3 is **partial**, not passed: core PIT / health / filing / marriage baselines are captured, but the official 2026 ZUS social-contribution table, exact IT classification for 12% `ryczalt`, VAT / reverse-charge handling for foreign B2B clients, and immigration-status compatibility still need verification.

### 5.4. Cost of living {status: deep, depth: 1, last_updated: 2026-06-12, dod: passed}

> **DoD status**: Passed for first-pass screening. Livingcost is a commercial aggregator, so this is a medium-confidence budget screen rather than a replacement for live shopping / utility / insurance quotes. Healthcare, visa insurance, accountant fees, deposits, and legal costs remain outside this section.

Livingcost's Poland country page screens the national average at about **$1,393/month for one person with rent** and **$3,169/month for a family of four**, with one-person spending split roughly into $584 without rent, $809 rent/utilities, $388 food, and $71 transport [src-501]. For this couple, the family-of-four line is only a conservative household proxy; a two-adult couple with one bedroom should land between the one-person and family-of-four lines.

| City | One-person total with rent | Family-of-four total | Food / transport one-person | Screening read |
|---|---:|---:|---:|---|
| Warsaw | $2,026 | $4,583 | $454 / $160 | Strong services and jobs, but too rent-heavy as the default on one income; keep only if the existing Polish status, work network, or Ukrainian community benefits outweigh the housing cost [src-502]. |
| Krakow | $1,662 | $3,756 | $425 / $104 | Better balance than Warsaw with strong services and diaspora; still tourist/student-demand pressure in central districts [src-503]. |
| Wroclaw | $1,662 | $3,671 | $420 / $85 | Similar cost to Krakow, milder climate than Warsaw, and a practical candidate if rent is controlled [src-504]. |

Budget verdict: against the couple's **$3,000 gross** income, Poland can work only with tax and rent discipline. The tax section's first-pass `ryczalt` model leaves about **$2,412/month before uncaptured ZUS social contributions** [src-293][src-320][src-321]. That makes Warsaw fragile after rent, health insurance, accountant costs, and visa/residence costs; Krakow or Wroclaw look more realistic first screens.

### 5.5. Rent {status: deep, depth: 1, last_updated: 2026-06-12, dod: passed}

> **DoD status**: Passed for first-pass screening. The vault's "normal two-room apartment" definition is closest to Livingcost's 40 m2 1BR line (separate bedroom + living room), while 80 m2 3BR is included only as an upper-size / future-family stress test. Exact live listings, lease terms, deposit, agency-fee practice, and landlord requirements for foreigners remain application-prep.

| City | 40 m2 1BR centre | 40 m2 cheap 1BR | 80 m2 3BR centre | 80 m2 cheap 3BR | Rent pressure vs $3,000 gross |
|---|---:|---:|---:|---:|---|
| Warsaw | $1,304 | $945 | $2,244 | $1,574 | 32%-43% for the 40 m2 proxy; high pressure after tax, so add `warsaw-rent-pressure` and use a strict housing cap [src-502]. |
| Krakow | $973 | $741 | $1,660 | $1,306 | 25%-32% for the 40 m2 proxy; manageable if outside the most central / tourist districts [src-503]. |
| Wroclaw | $910 | $737 | $1,581 | $1,195 | 25%-30% for the 40 m2 proxy; best first-pass balance among the three target cities [src-504]. |

Search/platform baseline for later housing work: start with OTODOM and OLX Nieruchomosci for broad listing supply, then cross-check city Facebook groups / Ukrainian community groups for landlord practice and scam warnings. This iteration did not capture platform-specific listing samples, so the rent section should be treated as a city-selection screen, not a ready lease budget.

Practical interpretation: for the current one-income couple, **Wroclaw first, Krakow second, Warsaw only with a strict cap or compelling legal/community reason**. Budget planning should assume at least first month + deposit cash needs; exact deposit and agency-fee rules still belong in a later application-prep pass.

### 5.6. Healthcare {status: pending, depth: 0, last_updated: —, dod: pending}

> **DoD**: how to register after the move; private insurance cost for the couple; maternity / birth coverage.

[verification required]

### 5.7. Education (future child) {status: pending, depth: 0, last_updated: —, dod: pending}

> **DoD**: kindergarten cost; public school quality for foreign kids; international school alternative with cost.

[verification required]

### 5.8. Comfort of life {status: pending, depth: 0, last_updated: —, dod: pending}

> **DoD**: safety data; attitude toward Ukrainians with sources; English level among locals.

[verification required]

### 5.9. Partner (student) {status: pending, depth: 0, last_updated: —, dod: pending}

> **DoD**: dependent/partner status with and without marriage; possibility of remote Ukrainian-university study; possibility of work; sponsor minimum income.

[verification required]

### 5.10. Risk dimensions {status: pending, depth: 0, last_updated: —, dod: pending}

> **DoD**: all 4 risk categories assessed (currency/banking, political, ties-to-Ukraine, diaspora).

- **Currency/banking risk**: [verification required]
- **Political risk**: [verification required]
- **Ties to Ukraine**: [verification required]
- **Diaspora and adaptation**: [verification required]

### 5.11. Bureaucracy and practicality {status: pending, depth: 0, last_updated: —, dod: pending}

> **DoD**: timelines for main paths; can-apply-from-inside or from-Ukraine; lawyer contacts (≥1).

[verification required]

## Block 4 — Risk dimensions (summary)

| Category | Level | Rationale |
|---|---|---|
| Currency / banking | — | [verification required] |
| Political | — | [verification required] |
| Ties to Ukraine | — | [verification required] |
| Diaspora / adaptation | — | [verification required] |

## Block 5 — Practical verdict

- **Can relocate now**: Plausibly yes if the couple can rely on existing Polish status / CUKR / family reunification, but the exact residence-file strategy remains unfinished.
- **Best legalization path for the man**: TBD (likely family reunification via partner's `karta pobytu` if married, or CUKR if eligible, or business-activity residence)
- **Best legalization path for the woman**: TBD (likely family reunification via partner's `karta pobytu` if married, or CUKR if eligible, or student residence)
- **Does marriage change the picture**: Yes — marriage would likely unlock family reunification under the partner's existing Polish `karta pobytu`, which is the strongest path.
- **Realism of staying after 03.2027**: Medium pending full legal-route verification; CUKR is a real post-TP bridge, but the next ordinary permit still needs a specific purpose.

**Pros**:
- Existing Polish `karta pobytu` / CUKR relevance makes Poland unusually practical compared with many countries in the set.
- Krakow and Wroclaw screen as workable on the current income if rent is controlled.
- Self-employed `ryczalt` tax may be workable if the 12% IT classification and ZUS assumptions are confirmed.

**Cons / risks**:
- Warsaw rent is too high as a default on one income.
- Climate is colder/greyer than the couple's preference.
- Full ZUS / VAT / business-residence fit is not yet verified.

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
|---|---|---:|
| Visa / residence permit fees | — | TBD |
| Apostilles and translations | — | TBD |
| Flights for two | — | TBD |
| Rental deposit | — | TBD; plan at least one month as a cash placeholder until Polish lease practice is captured. |
| First month rent | $737-$973 Wroclaw/Krakow cheap-to-centre 40 m2 proxy; $945-$1,304 Warsaw | Livingcost first-pass proxy, not guaranteed live listings [src-502][src-503][src-504]. |
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
- [src-062] Poland UdSC — CUKR procedure page (2026-05-04)
- [src-063] Poland UdSC — CUKR Q&A page (2026-05-04)
- [src-064] Poland Gov.pl — Temporary protection extension until March 4, 2027 (2025-08-13)
- [src-091] Kujawsko-Pomorskie Voivodeship information portal — family reunification (2020-07-21, accessed 2026-05-28)
- [src-323] Biznes.gov.pl — How to choose the best form of business activity taxation (accessed 2026-06-07)

### 7b. Reputable secondary
- [src-002] Council Implementing Decision (EU) 2025/1460 extending temporary protection
- [src-320] PwC Worldwide Tax Summaries — Poland individual taxes on personal income (accessed 2026-06-07)
- [src-321] PwC Worldwide Tax Summaries — Poland individual other taxes / social and health contributions (accessed 2026-06-07)
- [src-322] PwC Worldwide Tax Summaries — Poland individual residence and tax administration (accessed 2026-06-07)
- [src-293] NBP USD/PLN exchange-rate API reference reused for 2026-06-05 USD/PLN calculation

### 7c. Community and forums
_(none yet)_

### 7d. Statistical / commercial
- [src-065] Climate to Travel — Warsaw climate (accessed 2026-05-27)
- [src-066] Climate to Travel — Krakow climate (accessed 2026-05-27)
- [src-067] Climate to Travel — Wroclaw climate (accessed 2026-05-27)
- [src-501] Livingcost — Poland cost of living (accessed 2026-06-12)
- [src-502] Livingcost — Warsaw cost of living (accessed 2026-06-12)
- [src-503] Livingcost — Krakow cost of living (accessed 2026-06-12)
- [src-504] Livingcost — Wroclaw cost of living (accessed 2026-06-12)

### 7e. Not found
- A safe Article 159 family-reunification basis for an unmarried partner of a Polish residence-permit holder.
- Official-primary income threshold and business-plan requirements for business-activity temporary residence.
- Official-primary rules on whether remote work for a foreign employer qualifies for a Polish work or business residence permit.
- Direct annual sunny-day counts for Warsaw, Krakow, and Wroclaw (only sunshine-hour totals captured).
- Exact 2026 ZUS normal / preferential self-employed contribution table and accountant-level classification of foreign-client IT services for 12% `ryczalt`, VAT / reverse-charge, and immigration-status compatibility remain application-prep checks; the screening baseline should not assume these are verified.

## Block 8 — Open questions and verification markers

- `[verification required]` Exact counting rules for CUKR and prior TP time toward permanent residence / EU long-term residence.
- `[verification required]` Poland permanent residence and citizenship rules (years required, language level, dual citizenship policy).
- `[verification required]` Business-activity residence permit minimum requirements.
- `[verification required]` Direct sunny-day counts for Polish cities.
- Application-prep check: official/current 2026 ZUS normal / preferential self-employed contribution amounts for a foreign-client IT sole proprietor.
- Application-prep check: exact PKD/PKWiU classification, 12% `ryczalt` eligibility, VAT / reverse-charge handling, and immigration-status compatibility for a Ukrainian foreign-client IT freelancer in Poland.
