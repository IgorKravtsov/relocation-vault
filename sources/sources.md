---
document: sources-registry
version: 1.0.0
last_updated: 2026-06-29
---

# Sources Registry

Central registry of all sources cited across the vault. Country profiles and claims reference sources by ID `[src-NNN]`. URLs and metadata live here once; profiles cite by ID without duplicating.

## Schema (per `vault-protocol.md` §3.4)

Each source entry:

- **Title**: human-readable
- **URL**: original
- **Archive**: Wayback Machine snapshot URL (mandatory except for stable gov domains; `[archive: failed YYYY-MM-DD]` if unavailable)
- **Type**: one of `official-primary` | `official-secondary` | `reputable-secondary` | `community` | `commercial` | `aggregator`
- **Date published**: YYYY-MM-DD or `unknown`
- **Date accessed**: YYYY-MM-DD
- **Used by**: country names (or `global` if applies to many)
- **Facts supporting**: brief topic list with claim IDs
- **Confidence ceiling**: max confidence this source can support
- **Stale at**: YYYY-MM-DD (when this source's data becomes stale per `vault-protocol.md` §16)

## ID convention

`src-NNN` where NNN is a zero-padded 3-digit integer. Allocate sequentially.

---

## src-001
- **Title**: Greece Ministry of Migration and Asylum — Information for Displaced Persons from Ukraine
- **URL**: https://migration.gov.gr/en/ukraine/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2022-06-15
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: TP extension to 2027 (claim-greece-001); Article 194 TP→Immigration Code bridge (claim-greece-002); one-Member-State TP rule; document-translation warning
- **Confidence ceiling**: high
- **Stale at**: 2026-11-24

## src-002
- **Title**: Council Implementing Decision (EU) 2025/1460 extending temporary protection introduced by Decision (EU) 2022/382
- **URL**: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202501460
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2025-07-15
- **Date accessed**: 2026-05-24
- **Used by**: Greece, Spain, Italy, Cyprus, Croatia, Malta, Czech Republic
- **Facts supporting**: EU-level TP extension chain to 04 March 2027; one-Member-State TP principle; Spain, Italy, Cyprus, Croatia, Malta, and Czech Republic TP validity context through 04 March 2027
- **Confidence ceiling**: high
- **Stale at**: 2026-11-24

## src-003
- **Title**: Hellenic Republic Ministry of Foreign Affairs — Digital Nomad Visa
- **URL**: https://www.mfa.gr/en/services/working-in-greece-as-a-digital-nomad/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: official DN route exists; MFA points applicants to practical DN guidance; DN consular application channel
- **Confidence ceiling**: high
- **Stale at**: 2026-11-24

## src-004
- **Title**: Work From Greece FAQ
- **URL**: https://workfromgreece.gr/faq/
- **Archive**: [archive: failed 2026-05-24]
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: DN €3,500/month after-tax threshold (claim-greece-003); spouse/child uplift (claim-greece-004); 1-year visa then 2-year permit; no Greek-employer work; fast-track / 10-day response
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-24

## src-005
- **Title**: Greece Ministry of Migration and Asylum — Residence Permit Categories for Third Country Citizens & Documents to be Submitted
- **URL**: https://migration.gov.gr/en/migration-policy/metanasteusi-stin-ellada/katigories-adeion-diamonis-politon-triton-choron-dikaiologitika%E2%80%8B/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2020-06-25
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: Immigration Code residence-permit categories exist beyond TP and DN
- **Confidence ceiling**: high
- **Stale at**: 2027-05-24

## src-006
- **Title**: Greece Ministry of Migration and Asylum — Exclusive electronic renewal of all categories of residence permits for third country nationals
- **URL**: https://migration.gov.gr/en/ilektroniki-ananeosi-olon-ton-katigorion-titlon-diamonis-ton-politon-triton-choron/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2021-11-12
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: renewals handled electronically through ministry e-services
- **Confidence ceiling**: high
- **Stale at**: 2027-05-24

## src-007
- **Title**: Greece Ministry of Interior — Acquisition of the Greek Citizenship (supporting documents page)
- **URL**: https://www.ypes.gr/en/?post_type=page&p=18427
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: citizenship pathway categories include third-country nationals with long-term resident status and foreigners holding permanent residence permits
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-24

## src-008
- **Title**: Wikipedia — Athens climate table
- **URL**: https://en.wikipedia.org/wiki/Athens
- **Archive**: [archive: failed 2026-05-24]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: Athens January/July temperatures; humidity; sunshine hours
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-009
- **Title**: Wikipedia — Thessaloniki climate table
- **URL**: https://en.wikipedia.org/wiki/Thessaloniki
- **Archive**: [archive: failed 2026-05-24]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: Thessaloniki January/July temperatures; humidity; sunshine hours
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-010
- **Title**: Wikipedia — Heraklion climate table
- **URL**: https://en.wikipedia.org/wiki/Heraklion
- **Archive**: [archive: failed 2026-05-24]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Greece
- **Facts supporting**: Heraklion January/July temperatures; humidity; sunshine hours
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-011
- **Title**: Spain Ministry of Inclusion — What temporary protection for displaced persons from Ukraine is
- **URL**: https://www.inclusion.gob.es/web/ucrania-urgente/w/proteccion-temporal-desplazados-ucrania
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Spain
- **Facts supporting**: Spain TP rights (reside/work/medical/study); duration up to 3 years; eligibility categories for Ukrainians and family members (claim-spain-001)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-24

## src-012
- **Title**: Spain Ministry of Inclusion — Procedures and documents necessary to obtain temporary protection in Spain
- **URL**: https://www.inclusion.gob.es/web/ucrania-urgente/w/tramites-proteccion-temporal-desplazados-ucrania
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Spain
- **Facts supporting**: Spain TP 24-hour processing target (claim-spain-002); filing points; required documents; NIE and TIE follow-up flow
- **Confidence ceiling**: high
- **Stale at**: 2026-11-24

## src-013
- **Title**: Spanish Consulate in London — Digital Nomad Visa
- **URL**: https://www.exteriores.gob.es/Consulados/londres/en/ServiciosConsulares/Paginas/Consular/Digital-Nomad-Visa.aspx
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-secondary
- **Date published**: 2024-05-17
- **Date accessed**: 2026-05-24
- **Used by**: Spain
- **Facts supporting**: DN route scope; spouse/unmarried-partner coverage; apostille/translation checklist; 3-month prior work proof; 200% SMI threshold (claim-spain-003); family uplift formula (claim-spain-004); 10-day decision window (claim-spain-005); 1-year visa validity
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-24

## src-014
- **Title**: Climate to Travel — Madrid climate
- **URL**: https://www.climatestotravel.com/climate/spain/madrid
- **Archive**: [archive: failed 2026-05-24]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Spain
- **Facts supporting**: Madrid January/July temperatures; annual sunshine hours; humidity
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-015
- **Title**: Climate to Travel — Valencia climate
- **URL**: https://www.climatestotravel.com/climate/spain/valencia
- **Archive**: [archive: failed 2026-05-24]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Spain
- **Facts supporting**: Valencia January/July temperatures; sunshine profile; humidity
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-016
- **Title**: Climate to Travel — Málaga climate
- **URL**: https://www.climatestotravel.com/climate/spain/malaga
- **Archive**: [archive: failed 2026-05-24]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Spain
- **Facts supporting**: Málaga January/July temperatures; annual sunshine hours; humidity
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-017
- **Title**: Justiça.gov.pt — Temporary Protection FAQ / Reception and integration of Ukrainian citizens in Portugal
- **URL**: https://justica.gov.pt/en-gb/Servicos/Special-measures-for-Ukraine/-Reception-and-integration-of-Ukrainian-citizens-in-Portugal
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Portugal
- **Facts supporting**: Portugal TP does not require a visa; Temporary Protection Title creates a residence permit; automatic NISS/NIF/NHS access (claim-portugal-002); TP initial one-year duration plus two six-month extensions (claim-portugal-001)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-24

## src-018
- **Title**: gov.pt — Ukraine: Information for refugee citizens living in Portugal
- **URL**: https://www2.gov.pt/en/migrantes-viver-e-trabalhar-em-portugal/ucrania-informacoes-e-apoios-disponiveis-em-portugal/ucrania-cidadaos-refugiados-a-viver-em-portugal
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-secondary
- **Date published**: 2022-06-22
- **Date accessed**: 2026-05-24
- **Used by**: Portugal
- **Facts supporting**: Portugal TP guidance umbrella for work/health/education support [data older than 2024, verify freshness]
- **Confidence ceiling**: medium
- **Stale at**: 2026-11-24

## src-019
- **Title**: AIMA — Temporary protection for people displaced from Ukraine extended until 2027
- **URL**: https://aima.gov.pt/pt/noticias/protecao-temporaria-para-pessoas-deslocados-da-ucrania-prorrogada-ate-2027
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2025-03-17
- **Date accessed**: 2026-05-24
- **Used by**: Portugal
- **Facts supporting**: Portugal-specific confirmation that Ukrainian TP remains extended to 2027
- **Confidence ceiling**: high
- **Stale at**: 2026-11-24

## src-020
- **Title**: Portugalist — Portugal's Digital Nomad Visa Requirements: a deep dive into every aspect of the application
- **URL**: https://www.portugalist.com/digital-nomad-visa-requirements/
- **Archive**: [archive: failed 2026-05-24]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Portugal
- **Facts supporting**: D8 route exists; 2026 primary-applicant threshold €3,680/month (claim-portugal-003); NIF/bank-account/accommodation/document checklist orientation (claim-portugal-004); family-document and higher-income expectations; residence-vs-temporary-stay route distinction
- **Confidence ceiling**: medium
- **Stale at**: 2026-11-24

## src-021
- **Title**: Justiça.gov.pt — Nationality Law: new rules enter into force on 19 May
- **URL**: https://justica.gov.pt/Noticias/Lei-da-Nacionalidade-novas-regras-entram-em-vigor-a-19-de-maio
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-05-19
- **Date accessed**: 2026-05-24
- **Used by**: Portugal
- **Facts supporting**: naturalization residence period becomes 7 years for EU / Lusophone nationals and 10 years for other nationals (claim-portugal-005); stronger citizenship requirements from 19 May 2026
- **Confidence ceiling**: high
- **Stale at**: 2027-05-24

## src-022
- **Title**: Climate to Travel — Lisbon climate
- **URL**: https://www.climatestotravel.com/climate/portugal/lisbon
- **Archive**: [archive: failed 2026-05-24]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Portugal
- **Facts supporting**: Lisbon January/July temperatures; annual sunshine hours; humidity
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-023
- **Title**: Climate to Travel — Porto climate
- **URL**: https://www.climatestotravel.com/climate/portugal/porto
- **Archive**: [archive: failed 2026-05-24]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Portugal
- **Facts supporting**: Porto January/July temperatures; annual sunshine hours; humidity
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-024
- **Title**: Climate to Travel — Faro climate
- **URL**: https://www.climatestotravel.com/climate/portugal/faro
- **Archive**: [archive: failed 2026-05-24]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-24
- **Used by**: Portugal
- **Facts supporting**: Faro January/July temperatures; annual sunshine hours; humidity
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-025
- **Title**: Current Results — Annual Sunshine in Spain
- **URL**: https://www.currentresults.com/Weather/Spain/annual-days-of-sunshine.php
- **Archive**: [archive: failed 2026-05-25]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Spain
- **Facts supporting**: direct clear-day counts for Madrid (97), Valencia (91), and Málaga (107)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-026
- **Title**: AIMA — Residence authorization for remote work with a residence visa (Art. 88(1), Digital Nomads)
- **URL**: https://aima.gov.pt/pt/trabalhar/autorizacao-de-residencia-para-o-exercicio-de-atividade-profissional-prestada-de-forma-remota-com-visto-de-residencia-para-o-exe
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Portugal
- **Facts supporting**: post-visa filing route at AIMA; in-person/appointment process; required passport, valid remote-work residence visa, foreign employer/client declaration, and residence-address evidence; 2-year initial permit renewable for 3-year periods
- **Confidence ceiling**: high
- **Stale at**: 2026-11-25

## src-027
- **Title**: Italy Integration Migrants portal — Temporary protection for Ukrainians, permits renewable until March 2027
- **URL**: https://integrazionemigranti.gov.it/it-it/Ricerca-news/Dettaglio-news/id/4550/Protezione-temporanea-per-gli-ucraini-permessi-rinnovabili-fino-a-marzo-2027
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-01-07
- **Date accessed**: 2026-05-25
- **Used by**: Italy
- **Facts supporting**: Italy TP / Ukrainian permit renewal to 04 March 2027 (claim-italy-001); Decree-Law 201/2025 context; link to Council Implementing Decision (EU) 2025/1460
- **Confidence ceiling**: high
- **Stale at**: 2026-11-25

## src-028
- **Title**: Italian Consulate General in New York — Digital Nomad / Remote Worker Visa
- **URL**: https://consnewyork.esteri.it/en/servizi-consolari-e-visti/servizi-per-il-cittadino-straniero/visti/visas-to-enter-italy/digital-nomad-remote-worker-visa/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Italy
- **Facts supporting**: DN route scope; highly specialized worker requirement; document checklist; insurance coverage; registered lease requirement; 2024 income floor €24,789/year (claim-italy-002); one-year renewable permesso (claim-italy-003); spouse/minor-child family scope (claim-italy-005)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-25

## src-029
- **Title**: Italian Prefecture / Ministry of Interior — Citizenship by residence guidance PDF (Section 2)
- **URL**: https://prefettura.interno.gov.it/sites/default/files/98/2023-12/in-_section_2_citizenship_by_residence.pdf
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2023-12-01
- **Date accessed**: 2026-05-25
- **Used by**: Italy
- **Facts supporting**: citizenship-by-residence official guidance captured for follow-up extraction; baseline naturalization timing needs detailed verification
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-25

## src-030
- **Title**: Climate to Travel — Rome climate
- **URL**: https://www.climatestotravel.com/climate/italy/rome
- **Archive**: [archive: failed 2026-05-25]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Italy
- **Facts supporting**: Rome January / July temperatures; Mediterranean comfort summary; annual sunshine hours
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-031
- **Title**: Climate to Travel — Milan climate
- **URL**: https://www.climatestotravel.com/climate/italy/milan
- **Archive**: [archive: failed 2026-05-25]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Italy
- **Facts supporting**: Milan January / July temperatures; cold damp winter and muggy summer comfort summary; annual sunshine hours
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-032
- **Title**: Climate to Travel — Palermo climate
- **URL**: https://www.climatestotravel.com/climate/italy/palermo
- **Archive**: [archive: failed 2026-05-25]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Italy
- **Facts supporting**: Palermo January / July temperatures; very mild winter; sirocco heat risk; annual sunshine hours
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-033
- **Title**: Current Results — Annual Sunshine in Italy
- **URL**: https://www.currentresults.com/Weather/Italy/annual-days-of-sunshine.php
- **Archive**: [archive: failed 2026-05-25]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Italy
- **Facts supporting**: direct annual sunny-morning / clear-evening counts for Milan, Rome, and Palermo
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-034
- **Title**: UNHCR Italy — Temporary Protection
- **URL**: https://help.unhcr.org/italy/forms-of-protection-in-italy/temporary-protection/
- **Archive**: [archive: failed 2026-05-25]
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Italy
- **Facts supporting**: TP eligibility and Questura filing route; rights to education, work, and SSN; no current TP-to-work-permit conversion provision (claim-italy-004)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-25

## src-035
- **Title**: Cyprus Migration Department — Digital nomads and family members
- **URL**: https://www.gov.cy/mip-md/en/documents/digital-nomads-and-family-members/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Cyprus
- **Facts supporting**: Cyprus Digital Nomad route scope; €3,500/month net income threshold (claim-cyprus-003); one-year permit plus two-year renewal (claim-cyprus-004); spouse / civil-union partner / minor-child family scope; fees and 5–7 week examination time
- **Confidence ceiling**: high
- **Stale at**: 2026-11-25

## src-036
- **Title**: Cyprus Asylum Service — Announcement regarding the extension of temporary protection
- **URL**: https://www.mip.gov.cy/mip/asylum/asylumservice.nsf/All/E9992074C56A3109C2258C5300255BAD
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Cyprus
- **Facts supporting**: Cyprus TP local-extension mechanics to 04 March 2026 and first-time application route (claim-cyprus-002)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-25

## src-037
- **Title**: Cyprus Ministry of Interior — Acquisition of Cypriot Citizenship By Naturalization (Due to years of residence, form M127)
- **URL**: https://www.gov.cy/moi/en/documents/acquisition-of-cypriot-citizenship-by-naturalization-due-to-years-of-residence-form-m127/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Cyprus
- **Facts supporting**: citizenship-by-naturalization residence requirement and Greek B1 / civic-knowledge / financial-resource conditions (claim-cyprus-005)
- **Confidence ceiling**: high
- **Stale at**: 2027-05-25

## src-038
- **Title**: Cyprus Migration Department — Long-term Residents (LT) forms
- **URL**: https://www.gov.cy/mip-md/en/documents/long-term-residents-lt/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2025-12-29
- **Date accessed**: 2026-05-25
- **Used by**: Cyprus
- **Facts supporting**: official long-term-resident application packages exist; detailed eligibility extraction queued for later Cyprus legalization work
- **Confidence ceiling**: high
- **Stale at**: 2027-05-25

## src-039
- **Title**: Climates to Travel — Cyprus climate: temperature, rain, when to go
- **URL**: https://www.climatestotravel.com/climate/cyprus
- **Archive**: [archive: failed 2026-05-25]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Cyprus
- **Facts supporting**: Cyprus Mediterranean climate summary; January/July temperatures, humidity, precipitation days, and sun-hours data for Larnaca, Limassol, Nicosia, and Paphos
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-040
- **Title**: Croatia4Ukraine / Ministry of Interior — Temporary protection application form
- **URL**: https://croatia4ukraine.mup.hr/Pages/Zahtjev
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Croatia
- **Facts supporting**: Croatia temporary-protection application channel and eligibility categories for Ukrainians / family members / stateless and other third-country protection beneficiaries
- **Confidence ceiling**: high
- **Stale at**: 2026-11-25

## src-041
- **Title**: Croatia Ministry of Interior — Temporary stay of digital nomads
- **URL**: https://mup.gov.hr/aliens-281621/stay-and-work/temporary-stay-of-digital-nomads/286833
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Croatia
- **Facts supporting**: Croatia digital-nomad route scope; foreign-employer / foreign-company remote-work condition; up-to-18-month duration; €3,622.50/month means threshold; partner uplift; family reunification including common-law partners; document and application route checklist (claim-croatia-002 through claim-croatia-005)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-25

## src-042
- **Title**: gov.hr — Acquiring Croatian Citizenship
- **URL**: https://gov.hr/en/acquiring-croatian-citizenship/460
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Croatia
- **Facts supporting**: official Croatian citizenship-by-naturalisation page captured as anchor for later detailed extraction
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-25

## src-043
- **Title**: Climates to Travel — Croatia climate: temperature, rain, when to go
- **URL**: https://www.climatestotravel.com/climate/croatia
- **Archive**: [archive: failed 2026-05-25]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-25
- **Used by**: Croatia
- **Facts supporting**: Croatia climate zones; January/July temperatures, humidity, precipitation days, and annual sunshine hours for Zagreb, Split, and Dubrovnik
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-044
- **Title**: Current Results — Annual Sunshine in Greece
- **URL**: https://www.currentresults.com/Weather/Greece/annual-average-sunshine.php
- **Archive**: [archive: failed 2026-05-26]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Greece
- **Facts supporting**: annual sunshine hours and clear-sky percentages for Athens, Thessaloniki, and Heraklion; clear-sky day-equivalent proxy used to close the Greece climate sunny-days blocker
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-045
- **Title**: Current Results — Annual Sunshine in Croatia
- **URL**: https://www.currentresults.com/Weather/Croatia/sunshine-annual-average.php
- **Archive**: [archive: failed 2026-05-26]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Croatia
- **Facts supporting**: direct annual sunshine-day counts for Zagreb-Maksimir (49), Split-Marjan (108), and Dubrovnik (127), plus annual sunshine hours
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-046
- **Title**: Malta S.L. 420.5 — Temporary Protection for Displaced Persons (Minimum Standards) Regulations
- **URL**: https://legislation.mt/eli/sl/420.5/20220621/eng
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2022-06-21
- **Date accessed**: 2026-05-26
- **Used by**: Malta
- **Facts supporting**: Malta domestic temporary-protection legal framework for displaced persons (claim-malta-001 context)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-26

## src-047
- **Title**: Residency Malta Agency — Nomad Residence Permit Eligibility
- **URL**: https://nomad.residencymalta.gov.mt/nomad-eligibility/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Malta
- **Facts supporting**: NRP remote-work eligibility categories; foreign-employer / foreign-client scope; EUR 42,000/year gross income threshold (claim-malta-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-26

## src-048
- **Title**: Residency Malta Agency — Nomad Residence Permit Checklist
- **URL**: https://nomad.residencymalta.gov.mt/checklist/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-03-01
- **Date accessed**: 2026-05-26
- **Used by**: Malta
- **Facts supporting**: NRP online filing route; document checklist; bank-statement, police-certificate, relationship, accommodation, and health-insurance requirements; de facto partner evidence (claim-malta-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-26

## src-049
- **Title**: Residency Malta Agency — Nomad Residence Permit FAQ, version 14.1
- **URL**: https://nomad.residencymalta.gov.mt/new-faqs/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-04-17
- **Date accessed**: 2026-05-26
- **Used by**: Malta
- **Facts supporting**: NRP fees; 30-working-day processing target; 1-year duration and renewals to maximum 4 years; family-member list; NRP does not lead to long-term residency or citizenship (claim-malta-003 through claim-malta-005)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-26

## src-050
- **Title**: Identità — Expatriates Unit Non-Employment Permits: Long-Term Residence
- **URL**: https://identita.gov.mt/expatriates-unit-main-page/noneu-nationals/non-employment-permits/long-term-residence/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Malta
- **Facts supporting**: Malta long-term-residence eligibility after 5 years legal continuous residence; resources, accommodation, integration measures; EUR 500 fee
- **Confidence ceiling**: high
- **Stale at**: 2027-05-26

## src-051
- **Title**: Aġenzija Komunità Malta — Acquisition of Citizenship by Naturalisation
- **URL**: https://komunita.gov.mt/services/acquisition-of-citizenship/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Malta
- **Facts supporting**: ordinary citizenship-by-residence requirements; final 12 months plus 4 aggregate years in prior 6; language and good-character requirements; dual citizenship note
- **Confidence ceiling**: high
- **Stale at**: 2027-05-26

## src-052
- **Title**: Climates to Travel — Malta climate: temperature, rain, when to go
- **URL**: https://www.climatestotravel.com/climate/malta
- **Archive**: [archive: failed 2026-05-26]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Malta
- **Facts supporting**: Malta / Valletta January and July temperatures, humidity, precipitation days, annual sunshine hours, and climate comfort caveats
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-053
- **Title**: UNHCR Czechia — Special Long-Term Residence Permit
- **URL**: https://help.unhcr.org/czech/information-for-people-from-ukraine/special-long-term-residence/
- **Archive**: [archive: failed 2026-05-26]
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Czech Republic
- **Facts supporting**: Czech special long-term residence permit for temporary-protection holders; two-year TP residence condition; 2024 taxable-income thresholds; household application rule; private health-insurance requirement; 2025 expression-of-interest / registration timing (claim-czech-002, claim-czech-003)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-26

## src-054
- **Title**: Czech Information Portal for Foreigners — Long-term Visa for the Purpose of Doing Business
- **URL**: https://ipc.gov.cz/en/visa-and-residence-permit-types/third-country-nationals/long-term-visa/long-term-visa-for-the-purpose-of-doing-business/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Czech Republic
- **Facts supporting**: Czech business-purpose long-term visa application channel; documents including proof of accommodation, funds, registration in a relevant register, criminal-record extract, possible medical report; 5,000 CZK consular fee; 90-day processing time with possible interruption (claim-czech-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-26

## src-055
- **Title**: Czech Ministry of the Interior — A visa for a stay of over 90 days (long-term)
- **URL**: https://mv.gov.cz/mvcren/article/a-visa-for-a-stay-of-over-90-days-long-term.aspx
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Czech Republic
- **Facts supporting**: general Czech long-term visa filing rule; originals or official copies; Czech-language official translations; apostille/superlegalisation for foreign public documents; embassy jurisdiction rule
- **Confidence ceiling**: high
- **Stale at**: 2026-11-26

## src-056
- **Title**: Czech Information Portal for Foreigners — Permanent Residence
- **URL**: https://ipc.gov.cz/en/visa-and-residence-permit-types/third-country-nationals/permanent-residence/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Czech Republic
- **Facts supporting**: permanent residence permit after 5 years of temporary residence in the Czech Republic (claim-czech-005)
- **Confidence ceiling**: high
- **Stale at**: 2027-05-26

## src-057
- **Title**: EU Immigration Portal — Self-employed worker in Czechia
- **URL**: https://home-affairs.ec.europa.eu/policies/migration-and-asylum/eu-immigration-portal/self-employed-worker-czechia_en
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Czech Republic
- **Facts supporting**: self-employed route summary; long-term visa for business must be lodged in person at a Czech embassy abroad; long-term residence for business is filed inside Czechia; business/tax/social-security registration obligations
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-26

## src-058
- **Title**: Climates to Travel — Prague climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/czech-republic/prague
- **Archive**: [archive: failed 2026-05-26]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Czech Republic
- **Facts supporting**: Prague January/July temperatures, humidity, wind, precipitation, annual sunshine hours, and comfort caveats
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-059
- **Title**: Climates to Travel — Brno climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/czech-republic/brno
- **Archive**: [archive: failed 2026-05-26]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Czech Republic
- **Facts supporting**: Brno January/July temperatures, humidity, precipitation, annual sunshine hours, and comfort caveats
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-060
- **Title**: Climates to Travel — Ostrava climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/czech-republic/ostrava
- **Archive**: [archive: failed 2026-05-26]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Czech Republic
- **Facts supporting**: Ostrava January/July temperatures, humidity, precipitation, annual sunshine hours, and comfort caveats
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-061
- **Title**: Czech Information Portal for Foreigners — General information on special long-term residence
- **URL**: https://ipc.gov.cz/zvlastni-dlouhodoby-pobyt/obecne-informace-ke-zvlastnimu-dlouhodobemu-pobytu/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-26
- **Used by**: Czech Republic
- **Facts supporting**: official Czech special long-term residence baseline; special long-term residence is distinct from temporary protection; health-insurance obligations; special long-term residence counts in full toward permanent residence while prior temporary-protection stay counts one-half
- **Confidence ceiling**: high
- **Stale at**: 2026-11-26

## src-062
- **Title**: Poland UdSC — CUKR procedure page (Informacja dotycząca procedury wydania karty pobytu CUKR)
- **URL**: https://www.gov.pl/web/udsc/CUKR-procedura
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-05-04
- **Date accessed**: 2026-05-27
- **Used by**: Poland
- **Facts supporting**: CUKR card is a 3-year temporary residence permit on special conditions; eligibility criteria (365 days continuous UKR status, PESEL UKR on 04 June 2025); family scope; electronic application via MOS; fees 340 PLN + 100 PLN; deadline 04 March 2027; counts toward EU long-term residence (claim-poland-001 through claim-poland-005)
- **Confidence ceiling**: high
- **Stale at**: 2027-05-27

## src-063
- **Title**: Poland UdSC — CUKR Q&A page (Pytania i odpowiedzi - karta pobytu CUKR)
- **URL**: https://www.gov.pl/web/udsc/cukr-QA
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-05-04
- **Date accessed**: 2026-05-27
- **Used by**: Poland
- **Facts supporting**: CUKR rights (full labour market, Schengen travel, business activity); loss of UKR benefits upon CUKR receipt; 6-month absence rule; 60-day collection deadline; next permit under general rules; children born in Poland eligibility
- **Confidence ceiling**: high
- **Stale at**: 2027-05-27

## src-064
- **Title**: Poland Gov.pl — Temporary protection extension until March 4, 2027
- **URL**: https://www.gov.pl/web/ochrona-en/extension-of-validity-of-certificates-of-temporary-protection-until-march-4-2026
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2025-08-13
- **Date accessed**: 2026-05-27
- **Used by**: Poland
- **Facts supporting**: Poland-specific confirmation that temporary protection certificates for Ukrainians are extended until 04 March 2027
- **Confidence ceiling**: high
- **Stale at**: 2026-11-27

## src-065
- **Title**: Climate to Travel — Warsaw climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/poland/warsaw
- **Archive**: [archive: failed 2026-05-27]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Poland
- **Facts supporting**: Warsaw January/July temperatures, annual sunshine hours (~2000), precipitation, and comfort caveats (claim-poland-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-066
- **Title**: Climate to Travel — Krakow climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/poland/krakow
- **Archive**: [archive: failed 2026-05-27]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Poland
- **Facts supporting**: Krakow January/July temperatures, annual sunshine hours (~1455), precipitation, and comfort caveats (claim-poland-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-067
- **Title**: Climate to Travel — Wroclaw climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/poland/wroclaw
- **Archive**: [archive: failed 2026-05-27]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Poland
- **Facts supporting**: Wroclaw January/July temperatures, annual sunshine hours (~1885), precipitation, and comfort caveats (claim-poland-008)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-068
- **Title**: OUG 194/2002 (republished, consolidated April 2026) — Romanian law on the regime of foreigners
- **URL**: https://igi.mai.gov.ro/wp-content/uploads/2026/04/ORDONANTA-DE-URGENTA-nr.-194-din-12-decembrie-2002.pdf
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-04-30
- **Date accessed**: 2026-05-27
- **Used by**: Romania
- **Facts supporting**: definition of "nomad digital" (Art. 2); visa types (D/AM, D/AC, D/SD); family reunification (Art. 62); EU long-term residence conditions (Art. 71); temporary-protection references (Art. 81)
- **Confidence ceiling**: high
- **Stale at**: 2027-05-27

## src-069
- **Title**: IGI Portal — Public Online Applications (Portal IGI)
- **URL**: https://portaligi.mai.gov.ro/portaligi/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Romania
- **Facts supporting**: online application platform for residence permits and work authorisations; document-upload rules and appointment scheduling
- **Confidence ceiling**: high
- **Stale at**: 2027-05-27

## src-070
- **Title**: Nomad Girl — Romania Digital Nomad Visa & The 8 Best Cities To Stay
- **URL**: https://nomadgirl.co/romania-digital-nomad-visa-the-8-best-cities-to-stay/
- **Archive**: https://web.archive.org/web/20260527000000*/https://nomadgirl.co/romania-digital-nomad-visa-the-8-best-cities-to-stay/
- **Type**: aggregator
- **Date published**: 2022-01-11
- **Date accessed**: 2026-05-27
- **Used by**: Romania
- **Facts supporting**: DN visa income threshold €3,300/month; 12+12 months duration; tax treatment; application at embassy or e-visa; IT consultant 3% tax and micro-company 1-3% turnover tax mentioned
- **Confidence ceiling**: medium
- **Stale at**: 2027-05-27

## src-071
- **Title**: MAE — Annex 2: List of countries whose nationals are exempted from the Romanian visa requirement
- **URL**: https://www.mae.ro/sites/default/files/file/anul_2021/2021_pdf/3.4._anexa_2_en.pdf
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2021-01-04
- **Date accessed**: 2026-05-27
- **Used by**: Romania
- **Facts supporting**: Ukraine (biometric passport holders) exempt from Romanian short-stay visa
- **Confidence ceiling**: high
- **Stale at**: 2027-05-27

## src-072
- **Title**: Romania E-VISA portal — terms of use
- **URL**: https://evisa.mae.ro/Home?lang=en-US
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Romania
- **Facts supporting**: online visa application available; applicant must still present at diplomatic mission
- **Confidence ceiling**: high
- **Stale at**: 2027-05-27

## src-073
- **Title**: Climate to Travel — Bucharest climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/romania/bucharest
- **Archive**: [archive: failed 2026-05-27]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Romania
- **Facts supporting**: Bucharest January/July temperatures, annual sunshine hours (~2110), precipitation, comfort caveats (claim-romania-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-074
- **Title**: Climate to Travel — Cluj-Napoca climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/romania/cluj-napoca
- **Archive**: [archive: failed 2026-05-27]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Romania
- **Facts supporting**: Cluj-Napoca January/July temperatures, annual sunshine hours (~2030), precipitation, altitude and comfort caveats (claim-romania-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-075
- **Title**: Climate to Travel — Timișoara climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/romania/timisoara
- **Archive**: [archive: failed 2026-05-27]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Romania
- **Facts supporting**: Timișoara January/August temperatures, annual sunshine hours (~2130), precipitation, comfort caveats (claim-romania-008)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-076
- **Title**: UNHCR Romania — Temporary Protection
- **URL**: https://help.unhcr.org/romania/information-for-people-from-ukraine/temporary-protection/
- **Archive**: [archive: failed 2026-05-27]
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Romania
- **Facts supporting**: Romania TP registration through GII; residence permit and CNP issuance; rights (work, self-employment, education, healthcare, social assistance); validity through 04 March 2027; automatic extension; Schengen travel rules; days in Romania under TP do not count toward 90-day limit in other Member States
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-27

## src-077
- **Title**: Wikipedia — Climate of Lisbon
- **URL**: https://en.wikipedia.org/wiki/Climate_of_Lisbon
- **Archive**: [archive: failed 2026-05-27]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Portugal
- **Facts supporting**: Lisbon monthly and annual "Percentage possible sunshine" (annual 63%, monthly range 51–81%); WMO/NOAA-sourced climate table
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-078
- **Title**: Wikipedia — Climate of Porto
- **URL**: https://en.wikipedia.org/wiki/Climate_of_Porto
- **Archive**: [archive: failed 2026-05-27]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-27
- **Used by**: Portugal
- **Facts supporting**: Porto monthly and annual "Percentage possible sunshine" (annual 54%, monthly range 40–68%); WMO/NOAA-sourced climate table
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-079
- **Title**: EU Immigration Portal — Self-employed worker in Bulgaria
- **URL**: https://home-affairs.ec.europa.eu/policies/migration-and-asylum/eu-immigration-portal/self-employed-worker-bulgaria_en
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Bulgaria self-employment permit procedure; Employment Agency permit; Type D visa; residence permit from Migration Directorate; 1-year permit renewable up to 3 years; 1-month exit requirement; 5-year PR path; 6-month/10-month absence rules (claim-bulgaria-002, claim-bulgaria-003)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-28

## src-080
- **Title**: EU Immigration Portal — Family member in Bulgaria
- **URL**: https://home-affairs.ec.europa.eu/policies/migration-and-asylum/eu-immigration-portal/family-member-bulgaria_en
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Bulgaria family reunification scope for third-country nationals
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-28

## src-081
- **Title**: Wikipedia — Bulgarian nationality law
- **URL**: https://en.wikipedia.org/wiki/Bulgarian_nationality_law
- **Archive**: [archive: failed 2026-05-28]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Bulgarian citizenship naturalization rules (5 years residence, 3 years if married to Bulgarian); language requirement; dual-citizenship restrictions for naturalized non-EU citizens (claim-bulgaria-004, claim-bulgaria-005)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-082
- **Title**: Climate to Travel — Sofia climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/bulgaria/sofia
- **Archive**: [archive: failed 2026-05-28]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Sofia January/July temperatures, annual sunshine hours (~2,260), precipitation, humidity, comfort caveats (claim-bulgaria-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-083
- **Title**: Climate to Travel — Plovdiv climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/bulgaria/plovdiv
- **Archive**: [archive: failed 2026-05-28]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Plovdiv January/July temperatures, annual sunshine hours (~2,340), precipitation, humidity, comfort caveats (claim-bulgaria-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-084
- **Title**: Climate to Travel — Varna climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/bulgaria/varna
- **Archive**: [archive: failed 2026-05-28]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Varna January/July temperatures, annual sunshine hours (~2,300), precipitation, humidity, Black Sea climate summary (claim-bulgaria-008)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-085
- **Title**: Wikipedia — Sofia climate table
- **URL**: https://en.wikipedia.org/wiki/Sofia
- **Archive**: [archive: failed 2026-05-28]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Sofia mean monthly sunshine hours (2,261.2/year), NOAA/WMO-sourced temperature table
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-086
- **Title**: Wikipedia — Plovdiv climate table
- **URL**: https://en.wikipedia.org/wiki/Plovdiv
- **Archive**: [archive: failed 2026-05-28]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Plovdiv mean monthly sunshine hours (2,339/year), temperature extremes
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-087
- **Title**: Wikipedia — Varna, Bulgaria climate table
- **URL**: https://en.wikipedia.org/wiki/Varna,_Bulgaria
- **Archive**: [archive: failed 2026-05-28]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Varna mean monthly sunshine hours (2,345/year), NOAA/WMO-sourced temperature table, sea temperatures
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-088
- **Title**: Bulgarian Ministry of Interior — Ukraine information page (WAF-protected, not directly capturable)
- **URL**: https://www.mvr.bg/en/ukraine
- **Archive**: [archive: failed 2026-05-28]
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Bulgaria TP and Ukraine-specific guidance (not extracted due to WAF)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-28

## src-089
- **Title**: UNHCR Bulgaria — Arrival from Ukraine
- **URL**: https://help.unhcr.org/bulgaria/arrival-from-ukraine/
- **Archive**: [archive: failed 2026-05-28; Wayback returned 429]
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Bulgaria temporary-protection eligibility, registration flow, PFN/registration document issuance, address-card requirement, rights including residence, work without permit, medical care, education, social welfare assistance, and validity through 04 March 2027
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-28

## src-090
- **Title**: UNHCR Bulgaria — Important: TP has been extended until 4 March 2027
- **URL**: https://help.unhcr.org/bulgaria/2026/02/25/%F0%9F%93%A2-important-tp-has-been-extended-until-4-march-2027/
- **Archive**: [archive: failed 2026-05-28; Wayback returned 429]
- **Type**: reputable-secondary
- **Date published**: 2026-02-25
- **Date accessed**: 2026-05-28
- **Used by**: Bulgaria
- **Facts supporting**: Bulgaria announcement that TP has been extended until 04 March 2027 and beneficiaries need to renew registration cards at State Agency for Refugees registration centres
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-28

## src-091
- **Title**: Kujawsko-Pomorskie Voivodeship information portal for foreigners — Family reunification
- **URL**: https://cudzoziemiec.bydgoszcz.pl/en/stay-in-poland/temporary-stay/family-reunification/
- **Archive**: [archive: failed 2026-05-28]
- **Type**: official-secondary
- **Date published**: 2020-07-21
- **Date accessed**: 2026-05-28
- **Used by**: Poland
- **Facts supporting**: Poland family-reunification application route under Article 159 conditions, supporting documents, marriage/birth certificate evidence, health insurance, accommodation, stable regular income (PLN 776 net single / PLN 600 net per family member), PLN 340 stamp duty and PLN 50 residence-card fee
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-28

## src-092
- **Title**: OIF Hungary — Provisions and benefits provided for persons applying for recognition as a beneficiary of temporary protection
- **URL**: https://oif.gov.hu/factsheets/provisions-and-benefits-provided-for-persons-applying-for-recognition-as-a-beneficiary-of-temporary-protection
- **Archive**: [archive: failed 2026-05-28; Wayback returned 429]
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Hungary
- **Facts supporting**: temporary-protection eligibility for Ukrainians and qualifying family members; application submission after identity/data/biometric recording; right to work without a specific permit; listed healthcare benefits; accommodation-change reporting caveat (claim-hungary-001, claim-hungary-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-28

## src-093
- **Title**: OIF Hungary — White Card: residency for digital nomads
- **URL**: https://oif.gov.hu/factsheets/white-card-residency-for-digital-nomads
- **Archive**: [archive: failed 2026-05-28; Wayback returned 429]
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Hungary
- **Facts supporting**: White Card eligibility for foreign employment or foreign-company ownership; exclusion of Hungarian gainful activity and Hungarian company shareholding; EUR 3,000 net/month income threshold; 6-month prior-income evidence; extension mechanics; 21-day procedural administration period (claim-hungary-003, claim-hungary-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-28

## src-094
- **Title**: OIF Hungary — Residence permit for guest self-employment
- **URL**: https://oif.gov.hu/factsheets/residence-permit-for-guest-self-employment
- **Archive**: [archive: failed 2026-05-28; Wayback returned 429]
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Hungary
- **Facts supporting**: guest self-employment evidence for registered self-employed persons and business-organisation chief executives; annual self-employment income above 24 times minimum wage; no-tax/no-contribution-debt certificate; permit validity up to 1 year, extendable up to 3 years total (claim-hungary-005, claim-hungary-006)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-28

## src-095
- **Title**: OIF Hungary — Residence permit for the purpose of family reunification
- **URL**: https://oif.gov.hu/factsheets/residence-permit-for-the-purpose-of-family-reunification
- **Archive**: [archive: failed 2026-05-28; Wayback returned 429]
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Hungary
- **Facts supporting**: family-reunification beneficiary examples; spouse/minor-child/dependent-family baseline; subsistence/accommodation/healthcare evidence; general validity up to 3 years and extension rules
- **Confidence ceiling**: high
- **Stale at**: 2026-11-28

## src-096
- **Title**: OIF Hungary — National Residence Card
- **URL**: https://oif.gov.hu/factsheets/national-residence-card
- **Archive**: [archive: failed 2026-05-28; Wayback returned 429]
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Hungary
- **Facts supporting**: National Residence Card eligibility after at least 3 years legal uninterrupted residence for qualifying third-country nationals; 10-year validity and 10-year extension (claim-hungary-007)
- **Confidence ceiling**: high
- **Stale at**: 2027-05-28

## src-097
- **Title**: Wikipedia — Budapest climate table
- **URL**: https://en.wikipedia.org/wiki/Budapest#Climate
- **Archive**: [archive: failed 2026-05-28; Wayback returned 429]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Hungary
- **Facts supporting**: Budapest 1991–2020 January/July temperatures, relative humidity, precipitation days, sunshine hours (~1,928/year), and comfort caveats
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-098
- **Title**: Wikipedia — Debrecen climate table
- **URL**: https://en.wikipedia.org/wiki/Debrecen#Climate
- **Archive**: [archive: failed 2026-05-28; Wayback returned 429]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Hungary
- **Facts supporting**: Debrecen 1991–2020 January/July temperatures, relative humidity, precipitation days, sunshine hours (~2,043/year), and continental-climate caveats
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-099
- **Title**: Wikipedia — Pécs climate table
- **URL**: https://en.wikipedia.org/wiki/P%C3%A9cs#Climate
- **Archive**: [archive: failed 2026-05-28; Wayback returned 429]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-28
- **Used by**: Hungary
- **Facts supporting**: Pécs 1991–2020 January/July/August temperatures, relative humidity, precipitation days, sunshine hours (~2,058/year), and southwestern-Hungary comfort caveats
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-100
- **Title**: UNHCR Slovakia — Temporary Protection
- **URL**: https://help.unhcr.org/slovakia/information-for-people-coming-from-ukraine/temporary-protection/
- **Archive**: [archive: failed 2026-05-29; not attempted within iteration budget]
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovakia
- **Facts supporting**: Slovakia temporary-protection eligibility, EU extension through 04 March 2027, public healthcare/education/labour-market/social-assistance rights, application at Foreign Police, 90/180-day EU travel baseline, Ukraine travel not cancelling status (claim-slovakia-001)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-29

## src-101
- **Title**: EU Immigration Portal — Self-employed worker in Slovakia
- **URL**: https://home-affairs.ec.europa.eu/policies/migration-and-asylum/eu-immigration-portal/self-employed-worker-slovakia_en
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-secondary
- **Date published**: 2025-04-01
- **Date accessed**: 2026-05-29
- **Used by**: Slovakia
- **Facts supporting**: Slovakia temporary residence for purpose of business/self-employment; trade licence / Commercial Register mechanics; application location; documents, apostille/translation and 90-day freshness rules; business and personal financial evidence; fees; post-approval reporting, health-insurance and medical-report requirements; maximum 3-year validity and renewability (claim-slovakia-002, claim-slovakia-003)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-29

## src-102
- **Title**: EU Immigration Portal — Family member in Slovakia
- **URL**: https://home-affairs.ec.europa.eu/policies/migration-and-asylum/eu-immigration-portal/family-member-slovakia_en
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-secondary
- **Date published**: 2025-04-01
- **Date accessed**: 2026-05-29
- **Used by**: Slovakia
- **Facts supporting**: Slovakia family-reunification scope for spouse aged at least 18, children and dependent relatives; application location; document authentication rules; family-reunification fees; validity up to sponsor residence / maximum five years (claim-slovakia-004)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-29

## src-103
- **Title**: IOM Slovakia Migration Information Centre — Permanent Residence
- **URL**: https://www.mic.iom.sk/en/residence/permanent-residence.html
- **Archive**: [archive: failed 2026-05-29; WAF direct capture required Jina text mirror]
- **Type**: reputable-secondary
- **Date published**: 2025-11-25
- **Date accessed**: 2026-05-29
- **Used by**: Slovakia
- **Facts supporting**: Slovakia permanent/long-term residence overview; long-term residence after at least 5 years uninterrupted legal residence; Blue Card / high-qualified / study / research / family-with-Blue-Card counting variant (claim-slovakia-005)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-29

## src-104
- **Title**: Wikipedia — Slovak nationality law
- **URL**: https://en.wikipedia.org/wiki/Slovak_nationality_law
- **Archive**: [archive: failed 2026-05-29; not attempted within iteration budget]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovakia
- **Facts supporting**: Slovakia citizenship naturalization placeholder: continuous permanent residence for at least 8 years, Slovak language and country-knowledge requirement, security/obligation conditions (claim-slovakia-006)
- **Confidence ceiling**: medium
- **Stale at**: 2027-05-29

## src-105
- **Title**: Climate to Travel — Bratislava climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/slovakia/bratislava
- **Archive**: [archive: failed 2026-05-29; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovakia
- **Facts supporting**: Bratislava January/July temperatures, precipitation, humidity, annual sunshine hours (~2,075), and continental climate comfort caveats (claim-slovakia-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-106
- **Title**: Climate to Travel — Košice climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/slovakia/kosice
- **Archive**: [archive: failed 2026-05-29; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovakia
- **Facts supporting**: Košice January/July/August temperatures, precipitation, humidity, annual sunshine hours (~1,945), and continental climate comfort caveats (claim-slovakia-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-107
- **Title**: Climate to Travel — Poprad climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/slovakia/poprad
- **Archive**: [archive: failed 2026-05-29; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovakia
- **Facts supporting**: Poprad high-altitude climate, January/July temperatures, sunshine hours (~1,890), and comfort caveats for colder mountain living (claim-slovakia-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-108
- **Title**: Slovak Ministry of Economy — Foreigners: Running a business in the Slovak Republic
- **URL**: https://www.economy.gov.sk/podnikatelske-prostredie/cudzinci-foreigners/foreigners-running-a-business-in-the-slovak-republic
- **Archive**: [archive: failed 2026-05-29; Wayback returned 429]
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovakia
- **Facts supporting**: business-purpose temporary-residence applications accepted at Slovak diplomatic missions abroad from 01 July 2025; Ministry of Economy opinion role; mandatory business plan; assessment of feasibility, sustainability, and economic contribution; extension scrutiny of real business activity, tax compliance, employees, and unemployment contribution (claim-slovakia-008)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-29

## src-109
- **Title**: Slovak Ministry of Interior — Temporary refuge for displaced people from Ukraine is automatically extended until 4 March 2027
- **URL**: https://www.minv.sk/?tlacove-spravy-6&sprava=docasne-utocisko-pre-odidencov-z-ukrajiny-na-slovensku-sa-automaticky-predlzuje-do-4-marca-2027
- **Archive**: [archive: failed 2026-05-29; Wayback returned 429]
- **Type**: official-primary
- **Date published**: 2026-02-18
- **Date accessed**: 2026-05-29
- **Used by**: Slovakia
- **Facts supporting**: automatic extension of temporary refuge for displaced people from Ukraine in Slovakia until 04 March 2027 under the EU Council implementing decision and Slovak government resolution; residence-card validity/extension mechanics; no captured ordinary-residence bridge in the announcement (claim-slovakia-009)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-29

## src-110
- **Title**: GOV.SI — Support for Ukrainian Nationals in Slovenia
- **URL**: https://www.gov.si/en/topics/slovenias-assistance-to-the-citizens-of-ukraine/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovenia
- **Facts supporting**: Slovenia temporary-protection eligibility and procedure; police registration and administrative-unit application within three working days; TP card valid as temporary residence permit; fee exemption; temporary-residence registration; post-temporary-protection 10-day filing window and certificate effects (claim-slovenia-001, claim-slovenia-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-29

## src-111
- **Title**: GOV.SI Ministry of the Interior — Temporary residence permit for digital nomads
- **URL**: https://www.gov.si/en/news/2025-11-21-temporary-residence-permit-for-digital-nomads/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2025-11-21
- **Date accessed**: 2026-05-29
- **Used by**: Slovenia
- **Facts supporting**: Slovenia digital-nomad temporary residence; foreign remote-work definition; non-entry into Slovenian labour market; filing abroad or in Slovenia while legally present; up to one year, non-extendable, six-month wait before reapplication; sufficient-means formula of at least twice average monthly net salary; immediate family-reunification feature (claim-slovenia-003, claim-slovenia-005)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-29

## src-112
- **Title**: EU Immigration Portal — Self-employed worker in Slovenia
- **URL**: https://home-affairs.ec.europa.eu/policies/migration-and-asylum/eu-immigration-portal/self-employed-worker-slovenia_en
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-secondary
- **Date published**: 2025-04-01
- **Date accessed**: 2026-05-29
- **Used by**: Slovenia
- **Facts supporting**: Slovenia single permit for self-employed work; one-year prior valid-residence rule and professional-activity exception; filing abroad or at administrative unit; permanent residence after five continuous years of legal residence on temporary residence (claim-slovenia-004, claim-slovenia-006)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-29

## src-113
- **Title**: EU Immigration Portal — Family member in Slovenia
- **URL**: https://home-affairs.ec.europa.eu/policies/migration-and-asylum/eu-immigration-portal/family-member-slovenia_en
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-secondary
- **Date published**: 2025-04-01
- **Date accessed**: 2026-05-29
- **Used by**: Slovenia
- **Facts supporting**: Slovenia family-reunification scope for spouse, civil partner/civil-union partner, long-term relationship partner, children and dependent relatives; timing baseline after permanent residence or one year of temporary residence for general sponsors (claim-slovenia-005)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-29

## src-114
- **Title**: GOV.SI — Citizenship
- **URL**: https://www.gov.si/en/topics/citizenship/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovenia
- **Facts supporting**: ordinary Slovenian naturalisation baseline: at least 10 years living in Slovenia, including five continuous years before application (claim-slovenia-007)
- **Confidence ceiling**: high
- **Stale at**: 2027-05-29

## src-115
- **Title**: Climate to Travel — Ljubljana climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/slovenia/ljubljana
- **Archive**: [archive: failed 2026-05-29; Wayback returned 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovenia
- **Facts supporting**: Ljubljana January/July temperatures, precipitation, humidity, annual sunshine hours (~1,955), and continental/foggy winter comfort caveats (claim-slovenia-008)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-116
- **Title**: Climate to Travel — Maribor climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/slovenia/maribor
- **Archive**: [archive: failed 2026-05-29; Wayback returned 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovenia
- **Facts supporting**: Maribor January/July temperatures, precipitation, humidity, annual sunshine hours (~2,045), and continental climate comfort caveats (claim-slovenia-008)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-117
- **Title**: Climate to Travel — Portorož climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/slovenia/portoroz
- **Archive**: [archive: failed 2026-05-29; Wayback returned 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-29
- **Used by**: Slovenia
- **Facts supporting**: Portorož/coastal Slovenia January/July temperatures, precipitation, humidity, annual sunshine hours (~2,415), sea temperature, and mild coastal climate comfort baseline (claim-slovenia-008)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-118
- **Title**: WeatherSpark — Bulgaria city cloud-cover climate pages (Sofia, Plovdiv, Varna)
- **URL**: https://weatherspark.com/countries/BG
- **Archive**: [archive: failed 2026-05-30; Wayback returned 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Bulgaria
- **Facts supporting**: monthly percentages of time in the clearer cloud-cover categories (clear / mostly clear / partly cloudy) for Sofia, Plovdiv, and Varna; annual clearer-day-equivalent proxies calculated from monthly percentages
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-119
- **Title**: WeatherSpark — Cyprus city cloud-cover climate pages (Nicosia, Limassol, Paphos)
- **URL**: https://weatherspark.com/countries/CY
- **Archive**: [archive: failed 2026-05-30; Wayback returned 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Cyprus
- **Facts supporting**: monthly percentages of time in the clearer cloud-cover categories for Nicosia, Limassol, and Paphos; annual clearer-day-equivalent proxies calculated from monthly percentages
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-120
- **Title**: WeatherSpark — Malta city cloud-cover climate pages (Valletta, Sliema, Victoria)
- **URL**: https://weatherspark.com/countries/MT
- **Archive**: [archive: failed 2026-05-30; Wayback returned 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Malta
- **Facts supporting**: monthly percentages of time in the clearer cloud-cover categories for Valletta, Sliema, and Victoria/Gozo; annual clearer-day-equivalent proxies calculated from monthly percentages
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-121
- **Title**: WeatherSpark — Romania city cloud-cover climate pages (Bucharest, Cluj-Napoca, Timișoara)
- **URL**: https://weatherspark.com/countries/RO
- **Archive**: [archive: failed 2026-05-30; Wayback returned 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Romania
- **Facts supporting**: monthly percentages of time in the clearer cloud-cover categories for Bucharest, Cluj-Napoca, and Timișoara airport; annual clearer-day-equivalent proxies calculated from monthly percentages
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-122
- **Title**: WeatherSpark — Slovenia city cloud-cover climate pages (Ljubljana, Maribor, Portorož)
- **URL**: https://weatherspark.com/countries/SI
- **Archive**: [archive: failed 2026-05-30; Wayback returned 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Slovenia
- **Facts supporting**: monthly percentages of time in the clearer cloud-cover categories for Ljubljana, Maribor, and Portorož; annual clearer-day-equivalent proxies calculated from monthly percentages
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-123
- **Title**: Montenegro Ministry of Interior — Temporary protection for persons from Ukraine extended to 04 March 2027
- **URL**: https://www.gov.me/clanak/produzava-se-privremena-zastita-licima-iz-ukrajine-do-4-marta-2027-godine
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-03-03
- **Date accessed**: 2026-05-30
- **Used by**: Montenegro
- **Facts supporting**: Montenegro temporary protection for persons from Ukraine extended until 04 March 2027; existing-document exchange and first-time application baseline; rights under temporary protection (claim-montenegro-001, claim-montenegro-002, claim-montenegro-006)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-124
- **Title**: Digital Nomads GOV.me — Official Montenegro digital-nomad website
- **URL**: https://digitalnomads.gov.me/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Montenegro
- **Facts supporting**: Montenegro official digital-nomad portal; route exists and is tied to the Law on Foreigners and government digital-nomad programme (claim-montenegro-003)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-125
- **Title**: Government of Montenegro — Law on Foreign Nationals
- **URL**: https://www.gov.me/en/documents/e8ac34ee-953a-457c-944a-f9568b1aab65
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2021-05-13
- **Date accessed**: 2026-05-30
- **Used by**: Montenegro
- **Facts supporting**: official-law anchor for Montenegro foreigner residence framework, including digital-nomad route referenced by the official DN portal; PR/citizenship extraction still pending
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-126
- **Title**: Government of Montenegro — Law on International and Temporary Protection of Foreigners / 2022 Ukraine TP decision context
- **URL**: https://www.gov.me/en/documents/05b28b4b-9bd7-4ea8-a1b4-0b6148d650d5
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2018-03-21
- **Date accessed**: 2026-05-30
- **Used by**: Montenegro
- **Facts supporting**: official legal anchor for temporary protection; paired with the March 2022 Cabinet decision granting temporary protection to persons from Ukraine and humanitarian-entry document flexibility
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-30

## src-127
- **Title**: Visa Free Nomads — Montenegro Digital Nomad Visa: Requirements, Fees & How to Apply (2026)
- **URL**: https://visafreenomads.com/guides/digital-nomad-visa/montenegro
- **Archive**: [archive: failed 2026-05-30; not attempted within iteration budget]
- **Type**: reputable-secondary
- **Date published**: 2026-04-16
- **Date accessed**: 2026-05-30
- **Used by**: Montenegro
- **Facts supporting**: secondary operational placeholder for DN income threshold (~EUR 1,350/month), eligibility, foreign-employer/client remote-work requirement, health insurance, background check, processing time and fee caveats (claim-montenegro-004, claim-montenegro-005)
- **Confidence ceiling**: medium
- **Stale at**: 2026-11-30

## src-128
- **Title**: Climate to Travel — Podgorica climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/montenegro/podgorica
- **Archive**: [archive: failed 2026-05-30; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Montenegro
- **Facts supporting**: Podgorica January/July temperatures, precipitation, humidity, annual sunshine hours (~2,475), and extreme summer-heat comfort caveat (claim-montenegro-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-129
- **Title**: Climate to Travel — Budva climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/montenegro/budva
- **Archive**: [archive: failed 2026-05-30; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Montenegro
- **Facts supporting**: Budva / Bar coastal January/July temperatures, precipitation, sea temperatures, annual sunshine hours (~2,530), and coastal comfort baseline (claim-montenegro-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-130
- **Title**: Climate to Travel — Herceg Novi climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/montenegro/herceg-novi
- **Archive**: [archive: failed 2026-05-30; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Montenegro
- **Facts supporting**: Herceg Novi January/July temperatures, precipitation, sea temperatures, annual sunshine hours (~2,435), and Bay of Kotor comfort caveats (claim-montenegro-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-131
- **Title**: Weather in Montenegro — Podgorica, Budva, and Herceg Novi climate guides
- **URL**: https://www.weather-in-montenegro.com/
- **Archive**: [archive: failed 2026-05-30; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Montenegro
- **Facts supporting**: direct practical sunny-day heuristics for Podgorica (270+), Budva (240+), and Herceg Novi (200+) used as medium-confidence climate-screening counts (claim-montenegro-008)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-132
- **Title**: Serbia MFA — Visa regime for entering Serbia: Ukraine
- **URL**: https://mfa.gov.rs/en/citizens/travel-serbia/visa-regime/ukrajina
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: Ukrainian ordinary-passport holders do not need a visa for Serbia visits up to 90 days within 180 days (claim-serbia-001)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-133
- **Title**: KIRS / Serbian official consolidated decision — Temporary protection in Serbia for displaced persons coming from Ukraine
- **URL**: https://rtcm.kirs.gov.rs/wp-content/uploads/2026/04/RS-Privremena-zastita-za-Ukrajince.pdf
- **Archive**: stable official/public-sector domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-04-18
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: Serbia Ukraine temporary-protection eligibility, registration by MUP, rights reference, and one-year extension mechanics while reasons persist (claim-serbia-002, claim-serbia-003)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-134
- **Title**: KIRS — Law on Asylum and Temporary Protection
- **URL**: https://kirs.gov.rs/media/uploads/Law_on_asylum_and_temporary_prot.pdf
- **Archive**: stable gov/public-sector domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2020-12-28
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: legal framework for asylum and temporary protection; family-member definition and Article 76 rights anchor referenced by the Serbia Ukraine TP decision
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-30

## src-135
- **Title**: Serbia Ministry of Interior — Temporary residence information page
- **URL**: https://mup.gov.rs/wps/portal/en/information/temporary%20residence/temporary%20residence/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: temporary-residence and single-permit application baseline; route-specific document sections for self-employment and family reunification; e-application context
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-136
- **Title**: Serbia Ministry of Interior — Law on Foreigners (consolidated through 2023 amendments)
- **URL**: https://mup.gov.rs/wps/wcm/connect/9e10bf1d-79ad-4a50-a8c1-76b6afb0d6e9/Law+on+Foreigners+2023.pdf?MOD=AJPERES&CVID=pdNziNy
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2023-07-27
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: temporary-residence grounds; general temporary-residence evidence; single-permit self-employment framework; up-to-3-year residence/single-permit duration; PR after 3 years; absence limits; student-time counting limits (claim-serbia-004, claim-serbia-005, claim-serbia-006)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-30

## src-137
- **Title**: Welcome to Serbia GOV — Residence and work permit
- **URL**: https://welcometoserbia.gov.rs/residence-and-work-permit
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: Serbia visa D and single temporary residence/work-permit overview; self-employment, independent professional, and electronic application route for visa-exempt nationals
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-138
- **Title**: Serbia MFA — Citizenship
- **URL**: https://www.mfa.gov.rs/en/citizens/services/citizenship
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: ordinary Serbian naturalization requirements for foreigners with permanent residence, including 3 years registered permanent residence and release/proof of release from foreign citizenship (claim-serbia-007)
- **Confidence ceiling**: high
- **Stale at**: 2027-05-30

## src-139
- **Title**: Visa Free Nomads — Serbia Digital Nomad Visa 2026: Temporary Residence Requirements & Eligibility
- **URL**: https://visafreenomads.com/guides/digital-nomad-visa/serbia
- **Archive**: [archive: failed 2026-05-30; not attempted within iteration budget]
- **Type**: reputable-secondary
- **Date published**: 2026-04-16
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: medium-confidence operational placeholder for Serbia self-employment / entrepreneur route, no fixed official minimum income, EUR 1,000 bank-balance placeholder, RSD 22,700 + RSD 420 fee placeholder, 15-day processing, insurance, APR registration, and independent-professional EUR 3,500/month caveat
- **Confidence ceiling**: medium
- **Stale at**: 2026-11-30

## src-140
- **Title**: Climate to Travel — Belgrade climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/serbia/belgrade
- **Archive**: [archive: failed 2026-05-30; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: Belgrade January/July temperatures, precipitation days, humidity, annual sunshine hours, winter fog/cold and summer heat-wave caveats (claim-serbia-008)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-141
- **Title**: Climate to Travel — Novi Sad climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/serbia/novi-sad
- **Archive**: [archive: failed 2026-05-30; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: Novi Sad January/July temperatures, precipitation days, humidity, annual sunshine hours, winter fog/frost and summer heat-wave caveats (claim-serbia-008)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-142
- **Title**: Climate to Travel — Niš climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/serbia/nis
- **Archive**: [archive: failed 2026-05-30; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: 2026-05-30
- **Date accessed**: 2026-05-30
- **Used by**: Serbia
- **Facts supporting**: Niš January/July temperatures, precipitation days, humidity, annual sunshine hours, snow-cover and summer heat-wave caveats (claim-serbia-008)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-143
- **Title**: Digital Nomads GOV.me — How to get the visa? / Legal status for nomads
- **URL**: https://digitalnomads.gov.me/article/legal-status-for-nomads
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-30
- **Used by**: Montenegro
- **Facts supporting**: official-primary Montenegro digital-nomad filing route, document categories, 40-day decision period, up-to-2-year permit plus up-to-2-year extension and six-month cooling-off period, and spouse/minor-child family-reunification baseline (claim-montenegro-009, claim-montenegro-010)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-144
- **Title**: Republic of Turkey Ministry of Foreign Affairs — Visa Information For Foreigners
- **URL**: https://www.mfa.gov.tr/visa-information-for-foreigners.en.mfa
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: e-Visa scope limited to tourism/commerce and work/study visas handled by embassies or consulates (claim-turkey-001)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-145
- **Title**: Turkey Presidency of Migration Management — Residence Permits
- **URL**: https://en.goc.gov.tr/residence-permits
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: official residence-permit framework and categories; ordinary residence planning baseline; family and long-term residence category anchor (claim-turkey-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-146
- **Title**: Turkey Presidency of Migration Management — Temporary Protection in Turkey
- **URL**: https://en.goc.gov.tr/temporary-protection-in-turkey
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: Turkish temporary-protection framework exists, but no Ukraine-specific EU-style TP bridge captured in this pass
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-147
- **Title**: Turkey e-ikamet — Residence permit application portal
- **URL**: https://e-ikamet.goc.gov.tr/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: official electronic residence-permit application channel / operational filing anchor (claim-turkey-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-148
- **Title**: GoTurkey — Digital Nomads / Digital Nomad Identification Certificate application interface
- **URL**: https://digitalnomads.goturkiye.com/
- **Archive**: [archive: failed 2026-05-31; dynamic site not snapshotted within iteration budget]
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: digital-nomad age 21-55, income proof of at least USD 3,000 monthly or USD 36,000 annually, university-graduate document, passport/photo, employer document or freelancer project contract (claim-turkey-003, claim-turkey-004, claim-turkey-005)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-11-30

## src-149
- **Title**: Climate to Travel — Istanbul climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/turkey/istanbul
- **Archive**: [archive: failed 2026-05-31; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: Istanbul January/July temperatures, rain days, humidity, winter cloud/fog caveat, and annual sunshine hours (claim-turkey-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-150
- **Title**: Climate to Travel — Izmir climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/turkey/izmir
- **Archive**: [archive: failed 2026-05-31; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: Izmir January temperature, hot sunny summer, humidity / Meltemi comfort caveats, and seasonal rainfall pattern (claim-turkey-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-151
- **Title**: Climate to Travel — Antalya climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/turkey/antalya
- **Archive**: [archive: failed 2026-05-31; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: Antalya January/July/August temperatures, heavy winter rainfall, hot-summer caveat, and annual sunshine hours (claim-turkey-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-152
- **Title**: Hellenic Republic Ministry of Foreign Affairs — Visa for work in Greece as a digital nomad
- **URL**: https://www.mfa.gr/services/working-in-greece-as-a-digital-nomad/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Greece
- **Facts supporting**: official-primary Greek digital-nomad visa page used to close the core source gap for the DN route; jurisdiction-specific appointment formatting remains an application-prep detail (claim-greece-005)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-154
- **Title**: Turkey Presidency of Migration Management — Residence Permit Types
- **URL**: https://en.goc.gov.tr/residence-permit-types
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: short-term, family, and long-term residence-permit categories; long-term residence after at least eight years continuous residence; residence-type counting and exclusions for temporary-protection / humanitarian statuses (claim-turkey-007, claim-turkey-008)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-155
- **Title**: Georgian Ministry of Foreign Affairs GeoConsul — Entering Georgia
- **URL**: https://geoconsul.gov.ge/en/entering-georgia
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Georgia
- **Facts supporting**: official entry-information portal anchor; country-specific Ukraine stay table was not cleanly extractable in this pass (claim-georgia-001 as a source-gap anchor)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-156
- **Title**: Georgia Today — GD cuts visa-free stay for Ukrainians from 3 years to 1
- **URL**: https://georgiatoday.ge/gd-cuts-visa-free-stay-for-ukrainians-from-3-years-to-1/
- **Archive**: [archive: failed 2026-05-31; not attempted within iteration budget]
- **Type**: reputable-secondary
- **Date published**: 2025-04-03
- **Date accessed**: 2026-05-31
- **Used by**: Georgia
- **Facts supporting**: medium-confidence operational baseline that Ukrainian citizens may enter Georgia visa-free and stay for one full year; Ukrainians already present before 24 February 2025 extended until 24 February 2026 (claim-georgia-001)
- **Confidence ceiling**: medium
- **Stale at**: 2026-11-30

## src-157
- **Title**: Georgia Public Service Development Agency — Migration / Residence Permits
- **URL**: https://sda.gov.ge/en/products/migration-residence-permits/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Georgia
- **Facts supporting**: residence-permit filing baseline; work / entrepreneurial residence requirements; IT residence permit requirements; family reunification; permanent residence after 10 years on temporary residence (claim-georgia-002 through claim-georgia-006)
- **Confidence ceiling**: high
- **Stale at**: 2026-11-30

## src-158
- **Title**: Georgia Public Service Development Agency — Georgian citizenship
- **URL**: https://sda.gov.ge/en/products/citizenship/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Georgia
- **Facts supporting**: ordinary naturalization after 10 consecutive years lawful residence; Georgian language, history, and basic law tests; economic/property/business tie requirement (claim-georgia-006)
- **Confidence ceiling**: high
- **Stale at**: 2027-05-31

## src-159
- **Title**: Climate to Travel — Tbilisi climate: seasons, monthly averages
- **URL**: https://www.climatestotravel.com/climate/georgia/tbilisi
- **Archive**: [archive: failed 2026-05-31; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Georgia
- **Facts supporting**: Tbilisi January/July/August temperatures, annual rainfall and rain days, sunshine hours, humidity, and cold/hot-spell comfort caveats (claim-georgia-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-160
- **Title**: Climate to Travel — Batumi climate: seasons, monthly averages
- **URL**: https://www.climatestotravel.com/climate/georgia/batumi
- **Archive**: [archive: failed 2026-05-31; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Georgia
- **Facts supporting**: Batumi January/July/August temperatures, annual rainfall and rain days, sunshine hours, sea temperature, and humid subtropical comfort caveats (claim-georgia-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-161
- **Title**: Climate to Travel — Kutaisi climate: seasons, monthly averages
- **URL**: https://www.climatestotravel.com/climate/georgia/kutaisi
- **Archive**: [archive: failed 2026-05-31; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Georgia
- **Facts supporting**: Kutaisi January/July/August temperatures, annual rainfall and rain days, humidity, and hot/wet comfort caveats (claim-georgia-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-162
- **Title**: WeatherSpark — Istanbul climate and cloud-cover categories
- **URL**: https://weatherspark.com/y/95434/Average-Weather-in-%C4%B0stanbul-Turkey-Year-Round
- **Archive**: [archive: failed 2026-05-31; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: Istanbul monthly clearer-sky percentages; derived annual clearer-sky day-equivalent proxy of about 231 days/year for section 5.2 verification
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-163
- **Title**: WeatherSpark — Izmir climate and cloud-cover categories
- **URL**: https://weatherspark.com/y/94320/Average-Weather-in-%C4%B0zmir-Turkey-Year-Round
- **Archive**: [archive: failed 2026-05-31; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-05-31
- **Used by**: Turkey
- **Facts supporting**: Izmir monthly clearer-sky percentages; derived annual clearer-sky day-equivalent proxy of about 266 days/year for section 5.2 verification
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-164
- **Title**: Wikipedia — Visa requirements for Ukrainian citizens (Albania row)
- **URL**: https://en.wikipedia.org/wiki/Visa_requirements_for_Ukrainian_citizens
- **Archive**: [archive: failed 2026-06-01; not attempted within iteration budget]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Albania
- **Facts supporting**: medium-confidence operational baseline that Ukrainian citizens are visa-exempt for Albania for 90 days within any 180-day period (claim-albania-001)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-01

## src-165
- **Title**: Albania MFA / Ministry pages — visa regime and Ukraine temporary-protection pages attempted, content WAF-blocked
- **URL**: https://punetejashtme.gov.al/en/regjimi-i-vizave-per-te-huajt/ ; https://mb.gov.al/en/ministry/news/temporary-protection-for-ukrainian-citizens/
- **Archive**: stable gov domain / WAF shell captured; snapshot not useful
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Albania
- **Facts supporting**: official-primary targets for Albanian visa-regime and Ukrainian temporary-protection verification; direct content was blocked by Incapsula/WAF in this pass (claim-albania-002)
- **Confidence ceiling**: low
- **Stale at**: 2026-12-01

## src-166
- **Title**: Nomads Embassy — Albania Digital Nomad Visa: How to Apply
- **URL**: https://nomadsembassy.com/albania-digital-nomad-visa/
- **Archive**: [archive: failed 2026-06-01; not attempted within iteration budget]
- **Type**: reputable-secondary
- **Date published**: 2025-09-02
- **Date accessed**: 2026-06-01
- **Used by**: Albania
- **Facts supporting**: secondary operational baseline for Albania Unique Permit / remote-worker route, 1-year initial validity, renewability up to 5 years, family inclusion, income threshold, documents, apostille/translation notes, Albanian bank account, and health-insurance requirements (claim-albania-003 through claim-albania-006)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-01

## src-167
- **Title**: Citizen Remote — Albania Digital Nomad Visa 2026: requirements, costs and how to apply
- **URL**: https://citizenremote.com/visas/albania-digital-nomad-visa/
- **Archive**: [archive: failed 2026-06-01; not attempted within iteration budget]
- **Type**: reputable-secondary
- **Date published**: 2026-02-23
- **Date accessed**: 2026-06-01
- **Used by**: Albania
- **Facts supporting**: secondary 2026 baseline for Type D visa + Unique Permit remote-worker structure, foreign-client / foreign-employer income requirement, approximate income floor, annual renewals, no Albanian-market work without separate authorization, and document categories (claim-albania-003 through claim-albania-006)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-01

## src-168
- **Title**: Climate to Travel — Tirana climate: seasons, monthly averages
- **URL**: https://www.climatestotravel.com/climate/albania/tirana
- **Archive**: [archive: failed 2026-06-01; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Albania
- **Facts supporting**: Tirana January/July/August temperatures, annual rainfall and rain days, sunshine hours, humidity, and hot/cold comfort caveats (claim-albania-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-169
- **Title**: Climate to Travel — Durrës climate: seasons, monthly averages
- **URL**: https://www.climatestotravel.com/climate/albania/durres
- **Archive**: [archive: failed 2026-06-01; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Albania
- **Facts supporting**: Durrës January/July/August temperatures, annual rainfall and rain days, sea temperature, sunshine hours, and coastal comfort caveats (claim-albania-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-170
- **Title**: Climate to Travel — Vlorë climate: seasons, monthly averages
- **URL**: https://www.climatestotravel.com/climate/albania/vlore
- **Archive**: [archive: failed 2026-06-01; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Albania
- **Facts supporting**: Vlorë January/July/August temperatures, annual rainfall and rain days, sea temperature, sunshine hours, and southern coastal comfort caveats (claim-albania-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-171
- **Title**: WeatherSpark — Czechia city cloud-cover climate pages (Prague, Brno, Ostrava)
- **URL**: https://weatherspark.com/countries/CZ
- **Archive**: [archive: failed 2026-06-01; WeatherSpark direct fetch returned empty 202 responses]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Czech Republic
- **Facts supporting**: monthly percentages of time in the clearer cloud-cover categories for Prague, Brno, and Ostrava; annual clearer-sky day-equivalent proxies calculated from monthly percentages
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-172
- **Title**: WeatherSpark — Hungary city cloud-cover climate pages (Budapest, Debrecen, Pécs)
- **URL**: https://weatherspark.com/countries/HU
- **Archive**: [archive: failed 2026-06-01; WeatherSpark direct fetch returned empty 202 responses]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Hungary
- **Facts supporting**: monthly percentages of time in the clearer cloud-cover categories for Budapest, Debrecen, and Pécs; annual clearer-sky day-equivalent proxies calculated from monthly percentages
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-173
- **Title**: WeatherSpark — Slovakia city cloud-cover climate pages (Bratislava, Košice, Poprad)
- **URL**: https://weatherspark.com/countries/SK
- **Archive**: [archive: failed 2026-06-01; WeatherSpark direct fetch returned empty 202 responses]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Slovakia
- **Facts supporting**: monthly percentages of time in the clearer cloud-cover categories for Bratislava, Košice, and Poprad; annual clearer-sky day-equivalent proxies calculated from monthly percentages
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-174
- **Title**: WeatherSpark — Serbia city cloud-cover climate pages (Belgrade, Novi Sad, Niš)
- **URL**: https://weatherspark.com/countries/RS
- **Archive**: [archive: failed 2026-06-01; WeatherSpark direct fetch returned empty 202 responses]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Serbia
- **Facts supporting**: monthly percentages of time in the clearer cloud-cover categories for Belgrade, Novi Sad, and Niš; annual clearer-sky day-equivalent proxies calculated from monthly percentages
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-175
- **Title**: WeatherSpark — Georgia city cloud-cover climate pages (Tbilisi, Batumi, Kutaisi)
- **URL**: https://weatherspark.com/countries/GE
- **Archive**: [archive: failed 2026-06-01; WeatherSpark direct fetch returned empty 202 responses]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Georgia
- **Facts supporting**: monthly percentages of time in the clearer cloud-cover categories for Tbilisi, Batumi, and Kutaisi; annual clearer-sky day-equivalent proxies calculated from monthly percentages
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-176
- **Title**: Movingto — Cost of Living in Portugal 2026: Real Prices, Rent, and Monthly Budgets
- **URL**: https://movingto.com/pt/cost-of-living-portugal
- **Archive**: [archive: failed 2026-06-01; Wayback returned HTTP 429]
- **Type**: reputable-secondary
- **Date published**: 2026-05-21
- **Date accessed**: 2026-06-01
- **Used by**: Portugal
- **Facts supporting**: Portugal monthly budget ranges for couples, utilities, internet, transport, groceries, and housing orientation for Lisbon/Porto/interior
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-01

## src-177
- **Title**: idealista/news — Cost of living in Portugal in 2026
- **URL**: https://www.idealista.pt/en/news/financial-advice-in-portugal/2026/01/19/5469-cost-of-living-in-portugal
- **Archive**: [archive: failed 2026-06-01; Wayback returned HTTP 429]
- **Type**: reputable-secondary
- **Date published**: 2026-01-19
- **Date accessed**: 2026-06-01
- **Used by**: Portugal
- **Facts supporting**: non-rent monthly cost baselines, family-of-four cost baseline, utilities, rent per square metre, Lisbon metro rent per square metre, transport-pass cost
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-01

## src-178
- **Title**: Live in Portugal — Cost of Living in Portugal by City 2026: Real Monthly Costs
- **URL**: https://liveinpt.com/guides/cost-of-living-portugal-by-city/
- **Archive**: [archive: failed 2026-06-01; Wayback returned HTTP 429]
- **Type**: reputable-secondary
- **Date published**: 2026-05-04
- **Date accessed**: 2026-06-01
- **Used by**: Portugal
- **Facts supporting**: Lisbon, Porto, and Faro city-level rent, groceries, utilities, internet, transport, eating-out, and monthly total ranges for 2026 planning
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-01

## src-179
- **Title**: idealista/news — How to rent an apartment in Portugal: a step-by-step guide
- **URL**: https://www.idealista.pt/en/news/property-for-rent-in-portugal/2026/06/21/730-a-step-by-step-guide-to-renting-property-in-portugal
- **Archive**: [archive: failed 2026-06-01; Wayback returned HTTP 429]
- **Type**: reputable-secondary
- **Date published**: 2026-05-22
- **Date accessed**: 2026-06-01
- **Used by**: Portugal
- **Facts supporting**: rental process, NIF/ID/income/bank/guarantor expectations, standard deposit and advance-rent practice, written contract points, foreign remote-income caveat
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-01

## src-180
- **Title**: Uruguay Ministry of Interior — Regimen de visas de admision
- **URL**: https://www.gub.uy/ministerio-interior/comunicacion/publicaciones/regimen-visas-admision
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2025-08-19
- **Date accessed**: 2026-06-01
- **Used by**: Uruguay
- **Facts supporting**: Ukrainian ordinary-passport admission visa baseline; Ukraine listed as no visa required (claim-uruguay-001)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-01

## src-181
- **Title**: Uruguay gub.uy / National Migration Directorate — Residencia Legal
- **URL**: https://www.gub.uy/tramites/residencia-legal
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-03-13
- **Date accessed**: 2026-06-01
- **Used by**: Uruguay
- **Facts supporting**: official overview of Uruguay temporary/permanent residence routes, document formalities, apostille/legalization/translation rules, and residence/cedula planning baseline
- **Confidence ceiling**: high
- **Stale at**: 2026-12-01

## src-182
- **Title**: Uruguay gub.uy / National Migration Directorate — Residencia Legal - Permanente
- **URL**: https://www.gub.uy/tramites/residencia-legal-permanente
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-02-19
- **Date accessed**: 2026-06-01
- **Used by**: Uruguay
- **Facts supporting**: permanent legal residence checklist; criminal-record, health, vaccination, marriage/birth-document, apostille/translation requirements; means-of-life categories including foreign legal-entity employee, independent worker, and sole proprietor (claim-uruguay-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-01

## src-183
- **Title**: Uruguay gub.uy — Hoja de identidad provisoria
- **URL**: https://www.gub.uy/tramites/hoja-identidad-provisoria
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Uruguay
- **Facts supporting**: provisional identity sheet and digital-nomad subcategory checklist; online/in-person filing route; first filing and renewal evidence including identity document, sworn declaration, criminal records, and Uruguayan vaccination scheme (claim-uruguay-003)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-01

## src-184
- **Title**: Uruguay gub.uy / Corte Electoral — Carta de ciudadania (ciudadania legal uruguaya)
- **URL**: https://www.gub.uy/tramites/carta-ciudadania-ciudadania-legal-uruguaya
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-05-27
- **Date accessed**: 2026-06-01
- **Used by**: Uruguay
- **Facts supporting**: legal citizenship evidence, 3-year family / 5-year no-family habitual residence baseline, six-month consecutive absence reset rule, and Spanish comprehension/expression requirement (claim-uruguay-004)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-01

## src-185
- **Title**: Climate to Travel — Uruguay climate: temperature, rain, when to go
- **URL**: https://www.climatestotravel.com/climate/uruguay
- **Archive**: [archive: failed 2026-06-01; Wayback returned HTTP 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Uruguay
- **Facts supporting**: Uruguay humid-subtropical climate overview, mild windy winters, hot summer / heat-wave caveats, Montevideo rainfall and comfort notes, warmer northern climate context
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-186
- **Title**: WeatherSpark — Uruguay country climate comparison (Montevideo, Salto, Tacuarembo)
- **URL**: https://weatherspark.com/countries/UY
- **Archive**: [archive: failed 2026-06-01; Wayback returned HTTP 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-01
- **Used by**: Uruguay
- **Facts supporting**: monthly average high/low temperatures and clearer-sky percentages for Montevideo, Salto, and Tacuarembo; annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-uruguay-005, claim-uruguay-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-187
- **Title**: Statistical Office of the Republic of Slovenia — Earnings of persons in paid employment by legal persons, March 2026
- **URL**: https://www.stat.si/StatWeb/en/News/Index/14332
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-05-22
- **Date accessed**: 2026-06-02
- **Used by**: Slovenia
- **Facts supporting**: March 2026 average earnings of EUR 2,678.28 gross and EUR 1,678.81 net; derived digital-nomad funds screen of about EUR 3,357.62/month if applying the GOV.SI twice-average-net-salary formula
- **Confidence ceiling**: high
- **Stale at**: 2026-12-02

## src-188
- **Title**: WeatherSpark — Albania country and Vlore city cloud-cover climate pages
- **URL**: https://weatherspark.com/countries/AL ; https://weatherspark.com/y/84249/Average-Weather-in-Vlor%C3%AB-Albania-Year-Round
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: Albania
- **Facts supporting**: monthly clearer-sky percentages for Tirana, Durres, and Vlore; annual clearer-sky day-equivalent proxies calculated as Tirana ~225, Durres ~233, and Vlore ~237
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-189
- **Title**: The Traveler — Rent in Lisbon vs Porto vs Faro: Cost comparison for expats
- **URL**: https://www.thetraveler.org/rent-in-lisbon-vs-porto-vs-faro-cost-comparison-for-expats/
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: reputable-secondary
- **Date published**: 2026-03-30
- **Date accessed**: 2026-06-02
- **Used by**: Portugal
- **Facts supporting**: 2025-2026 long-term T2/two-bedroom rental bands for Lisbon, Porto, and Faro / Algarve, plus central-vs-peripheral rent caveats
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-02

## src-190
- **Title**: Paraguay National Migration Directorate — Informacion sobre Visas
- **URL**: https://migraciones.gov.py/index.php/tramites/informacion-sobre-visas
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: Paraguay
- **Facts supporting**: Ukraine tourist visa-free entry up to 90 days, but visa required for extension of stay, residence, or lucrative activities (claim-paraguay-001)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-02

## src-191
- **Title**: Paraguay National Migration Directorate — Residencia Temporal establecida por la Ley No. 6984/2022 de Migraciones
- **URL**: https://migraciones.gov.py/residencia-temporal/
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: Paraguay
- **Facts supporting**: temporary residence purpose, up-to-2-year duration plus equal extension, temporary residence as prerequisite to permanent residence, residente precario benefits, general document checklist, translation/apostille notes, and fee baseline (claim-paraguay-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-02

## src-192
- **Title**: Paraguay National Migration Directorate — Residencia Permanente para el cambio de categoria de residencia temporal
- **URL**: https://migraciones.gov.py/residencia-permanente-para-el-cambio-de-categoria-de-residente-temporal/
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: Paraguay
- **Facts supporting**: permanent residence as indefinite residence after temporary residence, category-change timing window, post-expiry grace period/fine, and permanent-residence fee / certificate baseline (claim-paraguay-003)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-02

## src-193
- **Title**: BACN — Constitucion de la Republica del Paraguay, Articles 148-150
- **URL**: https://www.bacn.gov.py/leyes-paraguayas/9580/constitucion-nacional-
- **Archive**: stable official legal database — snapshot not required
- **Type**: official-primary
- **Date published**: 2021-06-09
- **Date accessed**: 2026-06-02
- **Used by**: Paraguay
- **Facts supporting**: naturalization after minimum 3 years of radication plus profession/trade/science/art/industry and good conduct; multiple-nationality and loss-of-naturalized-nationality caveats (claim-paraguay-004)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-02

## src-194
- **Title**: Climate to Travel — Paraguay climate: temperature, rain, when to go
- **URL**: https://www.climatestotravel.com/climate/paraguay
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: Paraguay
- **Facts supporting**: Paraguay subtropical climate overview, very mild winters, hot summers, cold-air outbreaks, rainfall pattern, sunshine / cloudy-day comfort notes, and Asuncion / Encarnacion context
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-195
- **Title**: WeatherSpark — Paraguay country climate comparison (Asuncion, Ciudad del Este, Encarnacion)
- **URL**: https://weatherspark.com/countries/PY
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: Paraguay
- **Facts supporting**: monthly average high/low temperatures and clearer-sky percentages for Asuncion, Ciudad del Este, and Encarnacion; annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-paraguay-005, claim-paraguay-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-196
- **Title**: Paraguay National Migration Directorate — MIC y Migraciones lanzan el Paraguay Investor Pass
- **URL**: https://migraciones.gov.py/mic-y-migraciones-lanzan-el-paraguay-investor-pass-para-promover-la-residencia-permanente-a-inversionistas-extranjeros/
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-04-17
- **Date accessed**: 2026-06-02
- **Used by**: Paraguay
- **Facts supporting**: high-capital direct permanent-residence investor route context; USD 150,000 tourism-project or USD 200,000 stock-market / real-estate examples, not suitable as the couple's baseline
- **Confidence ceiling**: high
- **Stale at**: 2026-12-02

## src-197
- **Title**: VisaGuide.World — Ukrainian passport visa-free countries list
- **URL**: https://visaguide.world/visa-free-countries/ukrainian-passport/
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: Panama
- **Facts supporting**: medium-confidence placeholder that Panama is listed as visa-free for Ukrainian passport holders pending official Panama country-table verification
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-02

## src-198
- **Title**: Panama National Migration Service — Permisos Migratorios catalogue
- **URL**: https://www.migracion.gob.pa/permisos-y-requisitos/permisos-migratorios/
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-05-26
- **Date accessed**: 2026-06-02
- **Used by**: Panama
- **Facts supporting**: official catalogue of non-resident, permanent-residence, temporary-residence, foreign-professional, friendly-countries, remote-worker, and related migration permit checklists
- **Confidence ceiling**: high
- **Stale at**: 2026-12-02

## src-199
- **Title**: Panama National Migration Service — Requisitos para solicitar visa de corta estancia como trabajador remoto
- **URL**: https://www.migracion.gob.pa/wp-content/uploads/18.REQUISITOS-PARA-SOLICITAR-VISA-DE-CORTA-ESTANCIA-COMO-TRABAJADOR-REMOTO.pdf
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2023-09-26
- **Date accessed**: 2026-06-02
- **Used by**: Panama
- **Facts supporting**: remote-worker visa eligibility, foreign-source income threshold B/.36,000/year or B/.3,000/month, 9+9 month duration, right to work remotely without extra permit, no-local-work declaration, document checklist, insurance, fees, and self-employed evidence package (claim-panama-001 through claim-panama-003)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-02

## src-200
- **Title**: Panama National Migration Service — Permiso de residente provisional/permanente en calidad de extranjeros nacionales de paises especificos
- **URL**: https://www.migracion.gob.pa/wp-content/uploads/02-PAISES-ESPECIFICOS.pdf
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2024-01-26
- **Date accessed**: 2026-06-02
- **Used by**: Panama
- **Facts supporting**: friendly/specific-countries provisional residence for 2 years, economic/professional activity hooks, investment/employment/dependent evidence, solvency baseline for dependents, and permanent-residence stage (claim-panama-004)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-02

## src-201
- **Title**: Panama National Migration Service — Turistas / Requisitos para solicitar visa de turista
- **URL**: https://www.migracion.gob.pa/turistas/ and https://www.migracion.gob.pa/wp-content/uploads/Solicitud-y-Requesitos-para-Visa-de-Turista-2.pdf
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2025-08-07
- **Date accessed**: 2026-06-02
- **Used by**: Panama
- **Facts supporting**: general tourist entry requirements, passport/visa where required, solvency and return/onward-ticket requirements, tourist visa maximum 90 days, B/.50 fee, and B/.500 minimum solvency proof
- **Confidence ceiling**: high
- **Stale at**: 2026-12-02

## src-202
- **Title**: WeatherSpark — Panama country climate comparison (Panama City and David)
- **URL**: https://weatherspark.com/countries/PA
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: Panama
- **Facts supporting**: monthly average high/low temperatures, precipitation, humidity, and clearer-sky percentages for Panama City and David; annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-panama-005, claim-panama-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-203
- **Title**: WeatherSpark — Boquete / Guayabal climate, weather by month
- **URL**: https://weatherspark.com/y/16703/Average-Weather-in-Boquete-Panama-Year-Round
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: Panama
- **Facts supporting**: Boquete/Guayabal monthly average high/low temperatures, precipitation, humidity, and clearer-sky percentages; annual clearer-sky day-equivalent proxy calculated from monthly percentages (claim-panama-005, claim-panama-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-204
- **Title**: VisaGuide.World — Ukrainian passport visa-free countries list
- **URL**: https://visaguide.world/visa-free-countries/ukrainian-passport/
- **Archive**: [archive: failed 2026-06-02; text mirror/search result used for extraction]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: North Macedonia; Bosnia and Herzegovina; Moldova
- **Facts supporting**: medium-confidence placeholder that North Macedonia, Bosnia and Herzegovina, and Moldova are listed as visa-free for Ukrainian passport holders pending official country-table verification
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-02

## src-205
- **Title**: North Macedonia MFA — Visa requirements for entering the Republic of North Macedonia
- **URL**: https://mfa.gov.mk/en-GB/konzularni-uslugi/informacii-za-vlez-vo-rsm
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: North Macedonia
- **Facts supporting**: EU/Schengen temporary or permanent residence-card short-entry rule of up to 15 days per entry and 90 days in any 180-day period (claim-north-macedonia-001)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-02

## src-206
- **Title**: Invest North Macedonia — Work Visas and Permits
- **URL**: https://investnorthmacedonia.gov.mk/work-visas-and-permits/
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: North Macedonia
- **Facts supporting**: D visa / temporary residence sequence, work and residence permit categories, and temporary residence purposes including work, study, family reunification, humanitarian reasons, and other legal bases (claim-north-macedonia-002, claim-north-macedonia-021)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-02

## src-207
- **Title**: Invest North Macedonia — Permit / Aftercare work permit support
- **URL**: https://investnorthmacedonia.gov.mk/invest-permit/
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: North Macedonia
- **Facts supporting**: aftercare assistance for temporary residence and work permits for employment, work, or self-employment in North Macedonia; contact-point baseline for company-linked applicants (claim-north-macedonia-003)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-02

## src-208
- **Title**: Karanovic & Partners — Temporary Residence and Employment of Foreigners in North Macedonia: Key Changes Under the 2025 Amendments
- **URL**: https://www.karanovicpartners.com/news/temporary-residence-and-employment-of-foreigners-in-north-macedonia-key-changes-under-the-2025-amendments/
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: reputable-secondary
- **Date published**: 2025-09-26
- **Date accessed**: 2026-06-02
- **Used by**: North Macedonia
- **Facts supporting**: 2025 Law on Foreigners amendment alert affecting temporary residence / employment procedure and application-document baselines
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-02

## src-209
- **Title**: UNHCR North Macedonia Fact Sheet, September 2024
- **URL**: https://www.unhcr.org/europe/sites/europe/files/2024-10/bi-annual-fact-sheet-2024-09-north-macedonia.pdf
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: reputable-secondary
- **Date published**: 2024-10-11
- **Date accessed**: 2026-06-02
- **Used by**: North Macedonia
- **Facts supporting**: historical temporary-protection baseline for Ukrainians extended to 09 August 2025; 45 Ukrainian refugees granted temporary protection and residence on humanitarian grounds by mid-2024 (claim-north-macedonia-004)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-02

## src-210
- **Title**: Climate to Travel — Macedonia climate: temperature, rain, when to go
- **URL**: https://www.climatestotravel.com/climate/macedonia
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: North Macedonia
- **Facts supporting**: North Macedonia continental climate overview, Skopje / Ohrid / Bitola climate normals, winter cold, Skopje summer heat, low-humidity comfort caveats, and sunshine-hour context (claim-north-macedonia-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-211
- **Title**: WeatherSpark — Macedonia country climate comparison (Skopje and Ohrid)
- **URL**: https://weatherspark.com/countries/MK
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: North Macedonia
- **Facts supporting**: monthly average high/low temperatures, muggy-condition notes, and clearer-sky percentages for Skopje and Ohrid; annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-north-macedonia-005, claim-north-macedonia-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-212
- **Title**: WeatherSpark — Bitola climate and average weather year round
- **URL**: https://weatherspark.com/y/86830/Average-Weather-in-Bitola-Macedonia-Year-Round
- **Archive**: [archive: failed 2026-06-02; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-02
- **Used by**: North Macedonia
- **Facts supporting**: Bitola January/July temperature baseline, almost-zero muggy-day burden, monthly clearer-sky percentages, and annual clearer-sky day-equivalent proxy calculated from monthly percentages (claim-north-macedonia-005, claim-north-macedonia-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-213
- **Title**: Bosnia and Herzegovina Service for Foreigners' Affairs — Entry of Aliens to B&H and FAQ
- **URL**: https://sps.gov.ba/?page_id=2548&lang=en and https://sps.gov.ba/?page_id=2518&lang=en
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: entry framework, invitation-letter mechanics, visa-free stay FAQ, private-stay registration within 48 hours, and paid-work / work-permit baseline
- **Confidence ceiling**: high
- **Stale at**: 2026-12-03

## src-214
- **Title**: Bosnia and Herzegovina Service for Foreigners' Affairs — Stay of aliens in Bosnia and Herzegovina
- **URL**: https://sps.gov.ba/?page_id=2491&lang=en
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: visa-free stay up to 90 days in six months, temporary residence filing inside / outside Bosnia and Herzegovina, one-year temporary residence baseline, residence registration, permanent residence after five uninterrupted years, absence tolerance, and permanent-residence conditions (claim-bosnia-herzegovina-002, claim-bosnia-herzegovina-003, claim-bosnia-herzegovina-005)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-03

## src-215
- **Title**: Bosnia and Herzegovina Service for Foreigners' Affairs — Required documents and residence checklist PDFs
- **URL**: https://sps.gov.ba/?page_id=2527&lang=en; https://sps.gov.ba/dokumenti/dokumentacija/en/PB-4.1.pdf; https://sps.gov.ba/dokumenti/dokumentacija/en/PB-5.4.pdf; https://sps.gov.ba/dokumenti/dokumentacija/en/PB-6.pdf; https://sps.gov.ba/dokumenti/dokumentacija/en/PB-7.pdf; https://sps.gov.ba/dokumenti/dokumentacija/en/SB-1.pdf
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2018-09-10 for extracted PDFs; index date unknown
- **Date accessed**: 2026-06-03
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: temporary-residence document checklists for work permit, company founders, other justified reasons, real-estate ownership, and permanent residence; BAM 150 temporary-residence fee; BAM 200 permanent-residence fee; translation requirement; health-insurance / accommodation / criminal-record / medical-certificate evidence; company-founder employee and gross-salary burden (claim-bosnia-herzegovina-004, claim-bosnia-herzegovina-005)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-03

## src-216
- **Title**: Climate to Travel — Bosnia Herzegovina climate: temperature, rain, when to go
- **URL**: https://www.climatestotravel.com/climate/bosnia-herzegovina
- **Archive**: [archive: failed 2026-06-03; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Bosnia and Herzegovina climate zones, Mediterranean / transitional / continental split, cold inland winter waves, hot summer periods, and Sarajevo / Mostar / northern plain comfort context
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-217
- **Title**: WeatherSpark — Bosnia and Herzegovina country climate comparison (Sarajevo, Tuzla, Mostar)
- **URL**: https://weatherspark.com/countries/BA
- **Archive**: [archive: failed 2026-06-03; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Sarajevo / Tuzla / Mostar monthly average high/low temperatures, muggy-day burden, and clearer-sky percentages; annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-bosnia-herzegovina-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-218
- **Title**: UNHCR Help Bosnia and Herzegovina — asylum procedure and international protection overview
- **URL**: https://help.unhcr.org/bosniaandherzegovina/
- **Archive**: [archive: failed 2026-06-03; text mirror used for extraction]
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: ordinary asylum / international-protection baseline and absence of captured Ukraine-specific temporary-protection bridge in this pass
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-03

## src-219
- **Title**: Moldova General Inspectorate for Migration — Provisional stay
- **URL**: https://igm.gov.md/en/imigration/provisional-stay/
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Moldova
- **Facts supporting**: Moldova provisional-stay framework for stays over 90 days; purposes including family reunification, work, investments, studies, humanitarian/religious/volunteer activities, other cases, and digital nomad; GIM filing location, 30-day / 15-day submission and processing baselines; permanent-stay 3-year family / 5-year other-category overview (claim-moldova-003, claim-moldova-005)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-03

## src-220
- **Title**: Moldova General Inspectorate for Migration — Digital nomad residence application and document list
- **URL**: https://igm.gov.md/en/cererea-privind-acordarea-prelungirea-dreptului-de-sedere-in-scop-de-nomad-digital-precum-si-lista-de-acte/
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Moldova
- **Facts supporting**: Moldova digital-nomad granting/extension document list; accommodation, criminal-record, insurance, bank-statement, foreign employment/service contract, sworn remote-work statement, passport/application/photo requirements; income formula of at least 18 times current-year forecast average salary / three salaries per month for last six months (claim-moldova-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-03

## src-221
- **Title**: Moldova General Inspectorate for Migration — Permanent Residence
- **URL**: https://igm.gov.md/en/content/permanent-residence
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Moldova
- **Facts supporting**: Moldova permanent-residence conditions, 3-year and 5-year residence baselines, 90-day review period, language/housing/criminal-record conditions, and category caveats for students, IT specialists, posted workers, investment/free-zone workers, and religious/humanitarian/volunteer categories (claim-moldova-005)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-03

## src-222
- **Title**: UNHCR Moldova — Temporary Protection in Moldova
- **URL**: https://help.unhcr.org/moldova/temporary-protection/
- **Archive**: [archive: failed 2026-06-03; text mirror used for extraction]
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Moldova
- **Facts supporting**: Moldova temporary-protection eligibility for displaced persons from Ukraine, online + GIM appointment registration, TP card, rights to remain until 01 March 2027, work, healthcare, education, social assistance, accommodation, vehicle stay, and beneficiary obligations / cessation triggers (claim-moldova-002)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-03

## src-223
- **Title**: Climate to Travel — Moldova climate and Chisinau climate normals
- **URL**: https://www.climatestotravel.com/climate/moldova and https://www.climatestotravel.com/climate/moldova/chisinau
- **Archive**: [archive: failed 2026-06-03; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Moldova
- **Facts supporting**: Moldova continental climate overview, north/south temperature and sunshine differences, Balti and Chisinau climate tables, annual sunshine-hour context, precipitation, summer/winter comfort caveats (claim-moldova-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-224
- **Title**: WeatherSpark — Moldova climate pages for Chisinau, Balti, and Tiraspol
- **URL**: https://weatherspark.com/y/95676/Average-Weather-in-Chisinau-Moldova-Year-Round; https://weatherspark.com/y/95001/Average-Weather-in-B%C4%83l%C5%A3i-Moldova-Year-Round; https://weatherspark.com/y/96107/Average-Weather-in-Tiraspolul-Moldova-Year-Round
- **Archive**: [archive: failed 2026-06-03; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Moldova
- **Facts supporting**: Chisinau / Balti / Tiraspol monthly average high/low/mean temperatures, cloudier/clearer percentages, muggy-condition notes, and annual clearer-sky day-equivalent proxies calculated from monthly clearer percentages (claim-moldova-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-225
- **Title**: Moldova General Inspectorate for Migration — Provisional stay for family reunification
- **URL**: https://igm.gov.md/en/imigration/provisional-stay/provisional-stay-for-family-reunification/
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Moldova
- **Facts supporting**: family-reunification provisional-stay document list for reunification with a Moldovan citizen, including marriage certificate, housing evidence, criminal record, health insurance, application timing, and in-person presence baseline; used as a caveat that foreign digital-nomad dependent mechanics were not captured
- **Confidence ceiling**: high
- **Stale at**: 2026-12-03

## src-226
- **Title**: Mexico INM — Countries and regions that require a visa to travel to Mexico
- **URL**: https://www.inm.gob.mx/gobmx/word/index.php/paises-requieren-visa-para-mexico/
- **Archive**: stable gov domain via text mirror; country list image not OCR-readable in this pass
- **Type**: official-primary
- **Date published**: unknown; page image path indicates 2024-03
- **Date accessed**: 2026-06-03
- **Used by**: Mexico
- **Facts supporting**: Mexican visa-required framework; 180-day visitor cap; alternatives to Mexican visa via permanent residence in Canada/US/Japan/UK/Schengen/Pacific Alliance or valid visa from Canada/US/Japan/UK/Schengen; Polish residence-card caveat (claim-mexico-001)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-03

## src-227
- **Title**: Mexico gob.mx / INM migration procedures — canje, renewal, and permanent residence after four years of temporary residence
- **URL**: https://www.gob.mx/tramites/ficha/expedicion-de-documento-migratorio-por-canje/INM811; https://www.gob.mx/tramites/ficha/expedicion-de-documento-migratorio-por-renovacion/INM823; https://www.gob.mx/tramites/ficha/cambio-a-residente-permanente-por-contar-con-cuatro-anos-de-residencia-temporal/INM824
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Mexico
- **Facts supporting**: resident-visa exchange into Mexican migration document, renewal route, and change to permanent resident after four years of temporary residence (claim-mexico-003)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-03

## src-228
- **Title**: Mexico SRE — Carta de naturalizacion por residencia procedure
- **URL**: https://www.gob.mx/tramites/ficha/carta-de-naturalizacion-por-residencia/SRE256
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Mexico
- **Facts supporting**: SRE naturalization-by-residence procedure baseline; exact residence period / exams / absence limits queued for legal follow-up (claim-mexico-004)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-03

## src-229
- **Title**: Mexperience — Financial Criteria for Legal Residency in Mexico 2026
- **URL**: https://www.mexperience.com/financial-criteria-for-residency-in-mexico/
- **Archive**: [archive: failed 2026-06-03; text mirror used for extraction]
- **Type**: reputable-secondary
- **Date published**: 2026-05-29
- **Date accessed**: 2026-06-03
- **Used by**: Mexico
- **Facts supporting**: 2026 temporary-residence economic-solvency benchmark of about USD 4,400/month net income for last 6 months, consulate variation, and savings/investment alternative context (claim-mexico-002)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-03

## src-230
- **Title**: Climate to Travel — Mexico City climate: seasons, when to go, monthly averages
- **URL**: https://www.climatestotravel.com/climate/mexico/mexico-city
- **Archive**: [archive: failed 2026-06-03; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Mexico
- **Facts supporting**: Mexico City highland subtropical climate, mild days, cool/cold winter nights, rainy-season comfort caveats, and temperature context
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-231
- **Title**: Climate to Travel — Mexico climate, Cancun climate, and Puerto Vallarta climate
- **URL**: https://www.climatestotravel.com/climate/mexico; https://www.climatestotravel.com/climate/mexico/cancun; https://www.climatestotravel.com/climate/mexico/puerto-vallarta
- **Archive**: [archive: failed 2026-06-03; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Mexico
- **Facts supporting**: Mexico regional climate split, Caribbean / Pacific coastal warmth, rainy-season and hurricane / tropical-storm caveats, and warm-region comfort notes
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-232
- **Title**: WeatherSpark — Mexico country climate comparison (Mexico City, Cancun, Puerto Vallarta)
- **URL**: https://weatherspark.com/countries/MX
- **Archive**: [archive: failed 2026-06-03; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-03
- **Used by**: Mexico
- **Facts supporting**: Mexico City / Cancun / Puerto Vallarta monthly average high/low temperatures, muggy-day burden, precipitation days, clearer-sky percentages, and annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-mexico-005, claim-mexico-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-233
- **Title**: ArgentinaVisaLaw — Argentina Visa Requirements for Ukrainian Citizens
- **URL**: https://argentinavisalaw.com/nationality/ukraine
- **Archive**: [archive: failed 2026-06-04; text mirror used for extraction]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-07
- **Date accessed**: 2026-06-04
- **Used by**: Argentina
- **Facts supporting**: medium-confidence Ukraine ordinary-passport tourist visa-free 90-day baseline and planning caveats; identifies official tourist-exemption PDF for later direct capture (claim-argentina-001)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-04

## src-234
- **Title**: Argentina Ministry of Foreign Affairs — Tourist Visa / Visa para Turismo
- **URL**: https://www.cancilleria.gob.ar/en/services/visa/tourist-visa and https://www.cancilleria.gob.ar/es/servicios/visas/visa-para-turismo
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: Argentina
- **Facts supporting**: generic tourist-visa baseline for applicants who need a visa: up to 90 days, passport, photos, application form, proof of income, return booking, lodging/itinerary, interview, and USD/EUR 150 fee
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-235
- **Title**: Argentina.gob.ar / Migraciones — Obtain a transitory residence as a Digital Nomad
- **URL**: https://www.argentina.gob.ar/servicio/obtener-una-residencia-transitoria-como-nomada-digital
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2023-11-10
- **Date accessed**: 2026-06-04
- **Used by**: Argentina
- **Facts supporting**: official digital-nomad transitory residence basis, visa-exempt nationality condition, foreign-client remote-work scope, in-country semi-presential filing route, document checklist, legalization/apostille/translation rules, and 180-day extendable duration (claim-argentina-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-236
- **Title**: Argentina.gob.ar / Migraciones — Electronic Entry Process for Digital Nomads
- **URL**: https://www.argentina.gob.ar/servicio/tramitacion-de-ingreso-electronica-nomadas-digitales
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2022-05-10
- **Date accessed**: 2026-06-04
- **Used by**: Argentina
- **Facts supporting**: online TIE digital-nomad entry checklist, email entry authorization, border-control use, cost-table pointer, and 180-day transitory stay (claim-argentina-003)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-237
- **Title**: Argentina.gob.ar / Migraciones — Obtain an extension of transitory residence as a Digital Nomad
- **URL**: https://www.argentina.gob.ar/servicio/obtener-una-prorroga-de-residencia-transitoria-como-nomada-digital
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2023-10-27
- **Date accessed**: 2026-06-04
- **Used by**: Argentina
- **Facts supporting**: digital-nomad extension eligibility, income-from-services proof during the residence period, country-of-origin criminal-record requirement, legalization/apostille/translation rules, and 180-day extension baseline (claim-argentina-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-238
- **Title**: Argentina.gob.ar / Migraciones — Residences and temporary-residence categories
- **URL**: https://www.argentina.gob.ar/migraciones/residencias and https://www.argentina.gob.ar/migraciones/radicaciones-residencia-temporaria
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2019-01-31 / 2019-06-04
- **Date accessed**: 2026-06-04
- **Used by**: Argentina
- **Facts supporting**: distinction between transitory, temporary, and permanent residence; transitory maximum one year and no DNI; temporary residence up to three years with temporary DNI; list of ordinary temporary categories for follow-up
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-239
- **Title**: Argentina.gob.ar / Migraciones — Obtain temporary residence as a rentista
- **URL**: https://www.argentina.gob.ar/servicio/obtener-una-residencia-temporaria-como-rentista
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2019-06-04
- **Date accessed**: 2026-06-04
- **Used by**: Argentina
- **Facts supporting**: rentista temporary residence route, passive/external asset-income scope, exclusion of remuneration from personal work, five-minimum-wage income threshold, authorized-bank fund-entry rule, RADEX filing, and 1-year temporary-residence duration (claim-argentina-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-240
- **Title**: Argentina Law 346 / InfoLEG — Citizenship law updated text
- **URL**: https://www.argentina.gob.ar/normativa/nacional/ley-346-48854/texto and https://servicios.infoleg.gob.ar/infolegInternet/anexos/45000-49999/48854/texact.htm
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: Law 346; updated by Decree 366/2025
- **Date accessed**: 2026-06-04
- **Used by**: Argentina
- **Facts supporting**: naturalization after two years of continuous and legal residence for foreigners over 18; 2025 continuous-residence definition requiring no exits during the two years before application (claim-argentina-005)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-04

## src-241
- **Title**: Climate to Travel — Argentina, Buenos Aires, Cordoba, and Mendoza climate pages
- **URL**: https://www.climatestotravel.com/climate/argentina; https://www.climatestotravel.com/climate/argentina/buenos-aires; https://www.climatestotravel.com/climate/argentina/cordoba; https://www.climatestotravel.com/climate/argentina/mendoza
- **Archive**: [archive: failed 2026-06-04; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: Argentina
- **Facts supporting**: Argentina regional climate split; Buenos Aires, Cordoba, and Mendoza January/July temperatures, precipitation days, sunshine-hour context, humidity/heat/cold/wind comfort caveats (claim-argentina-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-242
- **Title**: WeatherSpark — Argentina country climate comparison
- **URL**: https://weatherspark.com/countries/AR
- **Archive**: [archive: failed 2026-06-04; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: Argentina
- **Facts supporting**: Buenos Aires / San Miguel de Tucuman / Mendoza / Ushuaia high-low temperatures, clearer-sky percentages, muggy-day burden, wind speeds, and clearer-sky day-equivalent proxies calculated from monthly percentages (claim-argentina-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-243
- **Title**: Emirates — UAE visa information
- **URL**: https://www.emirates.com/ua/english/before-you-fly/visa-passport-information/uae-visa-information/
- **Archive**: [archive: failed 2026-06-04; text mirror used for extraction]
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: UAE
- **Facts supporting**: Ukraine ordinary-passport 30-day visa-on-arrival operational baseline for short UAE scouting entry; generic UAE visa and sponsorship context (claim-uae-001)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-04

## src-244
- **Title**: GDRFA Dubai — Visa Issuance (Virtual Work)
- **URL**: https://gdrfad.gov.ae/en/services/64154a31-ec6d-11ec-140b-0050569629e8
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: UAE
- **Facts supporting**: virtual-work visa scope for remote employment without UAE employment; passport, foreign-entity remote-work proof, USD 3,500/month income, health-insurance requirements; one-year extendable residence; family sponsorship for same period; visa fee baseline (claim-uae-002, claim-uae-003)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-245
- **Title**: ICP UAE — Green Residency
- **URL**: https://icp.gov.ae/en/green-residency/
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2025-09-04
- **Date accessed**: 2026-06-04
- **Used by**: UAE
- **Facts supporting**: Green Residence 5-year renewable self-sponsored status; family sponsorship; freelancer/self-employed eligibility; MOHRE permit / bachelor's or specialized diploma / AED 360,000 annual freelancing income or financial-solvency baseline; skilled-professional AED 15,000/month baseline (claim-uae-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-246
- **Title**: UAE Government — Residence visa for doing business in the UAE / Green visa
- **URL**: https://u.ae/en/information-and-services/visa-and-emirates-id/residence-visas/residence-visa-for-doing-business-in-the-uae
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: UAE
- **Facts supporting**: Green visa benefits: renewable 5-year residence, no sponsor required, family sponsorship for spouse and children, and eligible categories including freelancers/self-employed and investors/business partners
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-247
- **Title**: UAE Government — Golden visa
- **URL**: https://u.ae/en/information-and-services/visa-and-emirates-id/residence-visas/golden-visa
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: updated 2026-02-26
- **Date accessed**: 2026-06-04
- **Used by**: UAE
- **Facts supporting**: 5- or 10-year Golden Visa categories and benefits, including no sponsor, extended time outside UAE, and family sponsorship for spouse and children
- **Confidence ceiling**: high
- **Stale at**: 2027-02-26

## src-248
- **Title**: UAE Government — Emirati nationality
- **URL**: https://u.ae/en/information-and-services/passports-and-traveling/emirati-nationality
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: UAE
- **Facts supporting**: nomination-based UAE citizenship categories, spouse/children coverage, original-nationality retention, and acquisition only through Rulers' and Crown Princes' Courts / Executive Councils / Cabinet nomination channels (claim-uae-005)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-04

## src-249
- **Title**: Climate to Travel — Dubai climate
- **URL**: https://www.climatestotravel.com/climate/united-arab-emirates/dubai
- **Archive**: [archive: failed 2026-06-04; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: UAE
- **Facts supporting**: Dubai subtropical desert climate, January/July-August average temperature range, monthly temperature table, humidity and oppressive summer comfort caveats (claim-uae-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-250
- **Title**: WeatherSpark — UAE country climate comparison
- **URL**: https://weatherspark.com/countries/AE
- **Archive**: [archive: failed 2026-06-04; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: UAE
- **Facts supporting**: Dubai / Abu Dhabi / Al Fujayrah / Al Ain high-low temperatures, muggy-day burden, clearer-sky percentages, and annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-uae-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-251
- **Title**: Malaysian Immigration Department — Visa Requirement by Country
- **URL**: https://www.imi.gov.my/index.php/en/main-services/visa/visa-requirement-by-country/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: Malaysia
- **Facts supporting**: official visa-requirement list target; this pass did not cleanly extract Ukraine's row/status, so Ukrainian short-stay treatment remains queued as an official-table verification item
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-252
- **Title**: Malaysian Immigration Department — Malaysia Digital Arrival Card (MDAC)
- **URL**: https://imigresen-online.imi.gov.my/mdac/main?registerMain
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: Malaysia
- **Facts supporting**: MDAC filing portal includes Ukraine as a nationality option for arrival-card registration, but it does not by itself establish visa-free duration
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-253
- **Title**: Malaysia Digital Economy Corporation — DE Rantau Foreign Digital Nomad Pass
- **URL**: https://mdec.my/derantau/foreign
- **Archive**: stable official programme domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: Malaysia
- **Facts supporting**: DE Rantau / Professional Visit Pass for foreign digital nomads; 3-12 month stay, renewable up to 24 months total; tech-professional annual-income threshold above USD 24,000; non-tech threshold above USD 60,000; spouse/children and main-holder parents as dependents; application from outside Malaysia; all nationalities except Israel (claim-malaysia-001 through claim-malaysia-003)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-04

## src-254
- **Title**: Malaysian Immigration Department — Entry Permit
- **URL**: https://www.imi.gov.my/index.php/en/main-services/permit/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: Malaysia
- **Facts supporting**: Entry Permit as Malaysia's no-time-limit permanent-residence facility; categories include Malaysian-citizen spouse, Malaysian-citizen child, and fully foreign national (claim-malaysia-004)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-04

## src-255
- **Title**: National Registration Department Malaysia — Citizenship under Article 19 of the Federal Constitution, aged 21 and older
- **URL**: https://www.jpn.gov.my/en/core-business/citizenship/warga-19-21lebih-eng
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: Malaysia
- **Facts supporting**: naturalization conditions: age 21+, 10 years residence in a 12-year period including the immediate 12 months, intention to reside permanently, good character, Malay language knowledge, two citizen referees, and Form C filing (claim-malaysia-005)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-04

## src-256
- **Title**: Climate to Travel — Malaysia and Kuala Lumpur climate baselines
- **URL**: https://www.climatestotravel.com/climate/malaysia ; https://www.climatestotravel.com/climate/malaysia/kuala-lumpur
- **Archive**: [archive: failed 2026-06-04; not attempted within iteration budget]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-04
- **Used by**: Malaysia
- **Facts supporting**: Malaysia equatorial hot/humid/rainy baseline; Kuala Lumpur January/July temperatures, rainfall, rain days and 2,200 annual sunshine hours; west-coast Penang / Johor Bahru qualitative rainfall-season comfort caveats (claim-malaysia-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-257
- **Title**: Royal Thai Embassy Warsaw — Visa Information
- **URL**: https://warsaw.thaiembassy.org/en/page/visa-information?menu=5fa59bd069d5ff051774a732
- **Archive**: stable MFA/embassy domain via text mirror — snapshot not required
- **Type**: official-secondary
- **Date published**: 2024-07-25
- **Date accessed**: 2026-06-05
- **Used by**: Thailand
- **Facts supporting**: Ukrainian/Polish passport visa-exemption up to 60 days for tourism; visa-exemption cash/onward-travel conditions; DTV workcation eligibility for applicants residing in Poland or Ukraine; 5-year multiple-entry validity; 180-day stay plus one 180-day extension; 500,000 THB financial evidence; remote-work evidence; spouse/children-under-20 dependent baseline; Warsaw e-visa fee (claim-thailand-001 through claim-thailand-003)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-05

## src-258
- **Title**: Royal Thai Embassy Washington — Destination Thailand Visa (DTV)
- **URL**: https://washingtondc.thaiembassy.org/en/page/dtv-visa
- **Archive**: stable MFA/embassy domain via text mirror — snapshot not required
- **Type**: official-secondary
- **Date published**: 2026-03-19
- **Date accessed**: 2026-06-05
- **Used by**: Thailand
- **Facts supporting**: DTV checklist cross-check: 5-year validity, workcation purposes, spouse/children dependents, 500,000 THB / roughly USD 16,000 savings evidence, and remote-work / freelancer evidence requirements (claim-thailand-002, claim-thailand-003)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-05

## src-259
- **Title**: Thailand BOI — LTR Visa Thailand, Long-Term Resident Program
- **URL**: https://ltr.boi.go.th/
- **Archive**: stable official programme domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-03-17
- **Date accessed**: 2026-06-05
- **Used by**: Thailand
- **Facts supporting**: LTR programme privileges; Work-from-Thailand Professionals category; 10-year renewable visa concept; spouse/children dependents; USD 80,000/year normal income threshold, reduced USD 40,000-80,000/year band with extra qualifications, qualifying overseas-employer requirement, and USD 50,000 insurance / USD 100,000 deposit alternative (claim-thailand-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-05

## src-260
- **Title**: Climate to Travel — Thailand, Bangkok, Phuket, and Chiang Mai climate baselines
- **URL**: https://www.climatestotravel.com/climate/thailand ; https://www.climatestotravel.com/climate/thailand/bangkok ; https://www.climatestotravel.com/climate/thailand/phuket ; https://www.climatestotravel.com/climate/thailand/chiang-mai
- **Archive**: [archive: failed 2026-06-05; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Thailand
- **Facts supporting**: Thailand monsoon regional baseline; Bangkok / Phuket / Chiang Mai January and July temperatures, annual rainfall, rain-season timing, and practical hot/humid comfort caveats (claim-thailand-005)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-261
- **Title**: WeatherSpark — Thailand country climate comparison
- **URL**: https://weatherspark.com/countries/TH
- **Archive**: [archive: failed 2026-06-05; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Thailand
- **Facts supporting**: monthly clearer-sky percentages for Bangkok, Phuket, and Chiang Mai; annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-thailand-006)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-262
- **Title**: Indonesia Directorate General of Immigration — Daftar Visa Indonesia
- **URL**: https://www.imigrasi.go.id/wna/daftar-visa-indonesia
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Indonesia
- **Facts supporting**: official visa-category index including B1 visit visa on arrival, D12 multiple-entry visit visa, family visas, investor visas, and E33G remote-worker / second-home category
- **Confidence ceiling**: high
- **Stale at**: 2026-12-05

## src-263
- **Title**: Indonesia Directorate General of Immigration — VoA/BVK/calling-visa subject-country list and B1 visit visa on arrival page
- **URL**: https://www.imigrasi.go.id/wna/daftar-negara-voa-bvk-calling-visa ; https://www.imigrasi.go.id/wna/daftar-visa-indonesia/B1
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Indonesia
- **Facts supporting**: Ukraine and Poland listed as VoA/BVK/calling-visa subject countries; B1 VoA 30-day stay, one extension to 60 days total, Rp500,000 fee, e-VoA online extension channel, and visitor work/payment restriction (claim-indonesia-001, claim-indonesia-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-05

## src-264
- **Title**: Indonesia Directorate General of Immigration — E33G Visa Rumah Kedua Pekerja Jarak Jauh
- **URL**: https://www.imigrasi.go.id/wna/daftar-visa-indonesia/E33G
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Indonesia
- **Facts supporting**: E33G remote-worker limited-stay route; 1-year stay; online extension; Rp7,000,000 one-year fee package; US$2,000 living-cost bank statement; CV/itinerary/photo/passport; US$60,000/year salary or income proof; foreign-company employment agreement; five-working-day processing after payment; automatic limited-stay / re-entry permit issue at admission (claim-indonesia-003, claim-indonesia-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-05

## src-265
- **Title**: Climate to Travel — Indonesia, Jakarta, Bali, Bandung, and Surabaya climate baselines
- **URL**: https://www.climatestotravel.com/climate/indonesia ; https://www.climatestotravel.com/climate/indonesia/jakarta ; https://www.climatestotravel.com/climate/indonesia/bali ; https://www.climatestotravel.com/climate/indonesia/bandung ; https://www.climatestotravel.com/climate/indonesia/surabaya
- **Archive**: [archive: failed 2026-06-05; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Indonesia
- **Facts supporting**: Indonesia hot/humid/rainy equatorial baseline; Jakarta, Surabaya, Bandung, and Bali/Denpasar January/July temperatures, rainfall, rain days, humidity notes, sunshine hours, monsoon and flood/comfort caveats (claim-indonesia-005)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-266
- **Title**: WeatherSpark — Indonesia country climate comparison
- **URL**: https://weatherspark.com/countries/ID
- **Archive**: [archive: failed 2026-06-05; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Indonesia
- **Facts supporting**: monthly clearer-sky percentages, precipitation days, muggy-day counts, and annual clearer-sky day-equivalent proxies for Jakarta, Surabaya, and Medan (claim-indonesia-005)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-267
- **Title**: Kazakhstan MFA — Visa regime of the Republic of Kazakhstan for foreign citizens
- **URL**: https://www.gov.kz/memleket/entities/mfa/press/article/details/6764?lang=en
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2022-11-11; updated 2026-04-28
- **Date accessed**: 2026-06-05
- **Used by**: Kazakhstan
- **Facts supporting**: Ukrainian ordinary passport visa-free entry up to 90 days for Kazakhstan scouting / short-stay baseline (claim-kazakhstan-001)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-05

## src-268
- **Title**: eGov Kazakhstan — Rules for entry and exit from Kazakhstan for foreign nationals
- **URL**: https://egov.kz/cms/en/articles/exit-entry_of_foreign_nationals
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown; migration digest prepared as of 2023-02
- **Date accessed**: 2026-06-05
- **Used by**: Kazakhstan
- **Facts supporting**: arrival notification within 3 working days; TRP purposes and up-to-1-year duration for CIS citizens; IIN utility for banking/digital services; work-without-permit administrative risk (claim-kazakhstan-002)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-05

## src-269
- **Title**: Kazakhstan Neo Nomad visa first-pass secondary baseline
- **URL**: https://astanatimes.com/ ; secondary reporting and search snippets reviewed for the 2024 Neo Nomad launch
- **Archive**: [archive: failed 2026-06-05; official-primary page not captured]
- **Type**: reputable-secondary
- **Date published**: 2024-11 (reported launch period)
- **Date accessed**: 2026-06-05
- **Used by**: Kazakhstan
- **Facts supporting**: medium-confidence placeholder for Neo Nomad / remote-work route: US$3,000/month income, health insurance, clean criminal record, foreign remote work, and possible bridge fit for the couple pending official-primary checklist capture (claim-kazakhstan-003)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-05

## src-270
- **Title**: Adilet — Law of the Republic of Kazakhstan On Migration
- **URL**: https://adilet.zan.kz/eng/docs/Z1100000477
- **Archive**: stable official legal database via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: current unofficial English translation; amendments through 2025 visible in source
- **Date accessed**: 2026-06-05
- **Used by**: Kazakhstan
- **Facts supporting**: legal definition of residence permit and migration-law context for unresolved TRP / permanent-residence counting questions (claim-kazakhstan-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-05

## src-271
- **Title**: Adilet — Law of the Republic of Kazakhstan On Citizenship
- **URL**: https://adilet.zan.kz/eng/docs/Z910004800_
- **Archive**: stable official legal database via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: current unofficial English translation; amendments through 2025 visible in source
- **Date accessed**: 2026-06-05
- **Used by**: Kazakhstan
- **Facts supporting**: citizenship-law baseline including non-recognition of another country's citizenship for Kazakh citizens and language / constitution / history screening caveats (claim-kazakhstan-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-05

## src-272
- **Title**: Climate to Travel — Kazakhstan and Almaty climate baselines
- **URL**: https://www.climatestotravel.com/climate/kazakhstan ; https://www.climatestotravel.com/climate/kazakhstan/almaty
- **Archive**: [archive: failed 2026-06-05; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Kazakhstan
- **Facts supporting**: Kazakhstan continental-climate overview, extreme winter/summer comfort caveats, aridity/precipitation pattern, and Almaty January/July temperature and precipitation baseline (claim-kazakhstan-005)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-273
- **Title**: WeatherSpark — Kazakhstan country climate comparison
- **URL**: https://weatherspark.com/countries/KZ
- **Archive**: [archive: failed 2026-06-05; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Kazakhstan
- **Facts supporting**: monthly average high/low temperatures and clearer-sky percentages for Astana, Almaty, and Shymkent; annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-kazakhstan-005)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-274
- **Title**: Armenia MFA — Visa framework and visa-free regime lists
- **URL**: https://www.mfa.am/en/visa/ ; https://www.mfa.am/en/visafreelist ; https://www.mfa.am/en/whoneedvisa
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Armenia
- **Facts supporting**: Armenia visa framework, unilateral visa-free list context, and bilateral/multilateral visa-free regime list including Ukraine for all passport types (claim-armenia-001)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-05

## src-275
- **Title**: Armenia MFA — Temporary and Permanent Residency in Armenia
- **URL**: https://www.mfa.am/en/residency/
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Armenia
- **Facts supporting**: temporary, permanent, and special residency types; temporary-residence eligibility including work permit, family, study, business activity, Armenian nationality, and other legal cases; permanent-residence eligibility including business activity; residence documents, fees, filing office, extension timing, and processing time (claim-armenia-002, claim-armenia-003, claim-armenia-004)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-05

## src-276
- **Title**: Armenia MFA — Citizenship
- **URL**: https://www.mfa.am/en/citizenship/
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2026 guidance update visible for e-system launch
- **Date accessed**: 2026-06-05
- **Used by**: Armenia
- **Facts supporting**: citizenship application e-system from 2026; ordinary eligibility grounds including at least three years of permanent and lawful residence, Armenian descent, marriage to an Armenian citizen with residence conditions, parent/child links, refugee and stateless-person grounds (claim-armenia-004)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-05

## src-277
- **Title**: Climate to Travel — Armenia climate and city climate baselines
- **URL**: https://www.climatestotravel.com/climate/armenia
- **Archive**: [archive: failed 2026-06-05; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown; text mirror timestamp 2026-06-05
- **Date accessed**: 2026-06-05
- **Used by**: Armenia
- **Facts supporting**: Armenia continental / arid continental climate zones, winter and summer comfort caveats, Yerevan / Gyumri / Sevan January and July temperature baselines, rainfall, humidity, and sunshine hours (claim-armenia-005)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-278
- **Title**: WeatherSpark — Armenia country climate comparison
- **URL**: https://weatherspark.com/countries/AM
- **Archive**: [archive: failed 2026-06-05; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Armenia
- **Facts supporting**: Yerevan and Gyumri monthly high/low temperatures, clearer-sky percentages, precipitation days, low muggy-day burden, and annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-armenia-005)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-279
- **Title**: WeatherSpark — Malaysia country climate comparison
- **URL**: https://weatherspark.com/countries/MY
- **Archive**: [archive: failed 2026-06-05; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-05
- **Used by**: Malaysia
- **Facts supporting**: monthly clearer-sky percentages for Kuala Lumpur, George Town, and Kuching; annual clearer-sky day-equivalent proxies calculated from monthly percentages (claim-malaysia-007)
- **Confidence ceiling**: medium
- **Stale at**: 2099-12-31

## src-280
- **Title**: Spain Tax Agency — Form 036 census declaration for entrepreneurs, professionals and withholding agents
- **URL**: https://sede.agenciatributaria.gob.es/Sede/en_gb/procedimientoini/G322.shtml
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-06
- **Used by**: Spain
- **Facts supporting**: Spain self-employed / professional tax-registration route using Form 036 census declaration of registration, modification, and deregistration (claim-spain-006)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-281
- **Title**: PwC Worldwide Tax Summaries — Spain individual taxes on personal income
- **URL**: https://taxsummaries.pwc.com/spain/individual/taxes-on-personal-income
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-31
- **Date accessed**: 2026-06-06
- **Used by**: Spain
- **Facts supporting**: Spain PIT general-income progressive withholding scale used as a planning proxy; non-resident 24% general-rate context; autonomous-community caveat for final resident PIT calculation (claim-spain-007, claim-spain-008)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-31

## src-282
- **Title**: PwC Worldwide Tax Summaries — Spain individual residence
- **URL**: https://taxsummaries.pwc.com/spain/individual/residence
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-31
- **Date accessed**: 2026-06-06
- **Used by**: Spain
- **Facts supporting**: Spain tax-residence baseline: more than 183 days, centre of economic/personal interests, no part-year resident concept (claim-spain-009)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-31

## src-283
- **Title**: PwC Worldwide Tax Summaries — Spain other taxes, deductions, and tax administration
- **URL**: https://taxsummaries.pwc.com/spain/individual/other-taxes ; https://taxsummaries.pwc.com/spain/individual/deductions ; https://taxsummaries.pwc.com/spain/individual/tax-administration
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-31
- **Date accessed**: 2026-06-06
- **Used by**: Spain
- **Facts supporting**: 2026 Spanish social-security contribution-base context, employee/social-security certificate caveat, filing period, and individual vs joint taxation / family-unit baseline (claim-spain-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-31

## src-284
- **Title**: Spain Social Security — Special Regime for Self-Employed Workers (RETA) scope
- **URL**: https://www.seg-social.es/wps/portal/wss/internet/Trabajadores/Afiliacion/10548/32825
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-06
- **Used by**: Spain
- **Facts supporting**: RETA self-employed worker definition: habitual, personal, direct lucrative economic activity without employment contract (claim-spain-006)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-285
- **Title**: Infoautonomos — Cuota de autonomos 2026
- **URL**: https://www.infoautonomos.com/seguridad-social/cuota-de-autonomos-cuanto-se-paga/
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: unknown; 2026 article
- **Date accessed**: 2026-06-06
- **Used by**: Spain
- **Facts supporting**: 2026 RETA real-net-income brackets and monthly quota planning table, including EUR 2,330-2,760/month bracket with EUR 427/month minimum quota and EUR 2,760-3,190/month bracket with EUR 452/month minimum quota (claim-spain-011)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-06

## src-286
- **Title**: open.er-api.com — USD exchange-rate feed
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: failed 2026-06-06; direct JSON extraction used]
- **Type**: commercial
- **Date published**: 2026-06-06
- **Date accessed**: 2026-06-06
- **Used by**: Spain
- **Facts supporting**: run-date USD/EUR conversion of 1 USD = EUR 0.860529 used only for the Spain section 5.3 worked budget/tax example
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-06

## src-287
- **Title**: Agenzia delle Entrate — Regime forfetario: che cos'è / eligibility rules
- **URL**: https://www.agenziaentrate.gov.it/portale/regime-forfetario-le-regole-2020-/infogen-regime-forfetario-le-regole-2020-
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: updated 2026-01-19
- **Date accessed**: 2026-06-06
- **Used by**: Italy
- **Facts supporting**: forfetario eligibility baseline, EUR 85,000 annualized revenue/fees cap, EUR 20,000 employee/collaborator cost cap, new-activity opt-in statement, exclusions, and 5% startup-rate condition summary (claim-italy-007, claim-italy-008)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-288
- **Title**: Agenzia delle Entrate — Regime forfetario: reddito e tassazione
- **URL**: https://www.agenziaentrate.gov.it/portale/schede/agevolazioni/regime-agevolato-forfettario/reddito-e-tassazione-nuovo-regime-forfettario-agevolato ; https://www.agenziaentrate.gov.it/portale/schede/agevolazioni/regime-agevolato-forfettario/agevolazioni-per-soggetti-che-iniziano-nuova-attivita
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-06
- **Used by**: Italy
- **Facts supporting**: forfetario income computation by ATECO profitability coefficient; mandatory social-security contributions deducted from forfetario income; 15% substitute tax replacing ordinary income/regional/municipal taxes and IRAP; 5% substitute tax for first five years of qualifying new activities (claim-italy-008)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-289
- **Title**: Agenzia delle Entrate — Partita IVA persone fisiche, modello AA9/12
- **URL**: https://www.agenziaentrate.gov.it/portale/schede/istanze/aa9_11-apertura-variazione-chiusura-pf/modello-e-istr-pi-pf
- **Archive**: stable gov domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-06
- **Used by**: Italy
- **Facts supporting**: individual VAT-number opening, variation, and closure route using model AA9/12 for natural persons
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-290
- **Title**: INPS Circular No. 8/2026 — Gestione Separata contribution rates for 2026
- **URL**: https://www.inps.it/it/it/inps-comunica/atti/circolari-messaggi-e-normativa/dettaglio.circolari-e-messaggi.2026.02.circolare-numero-8-del-03-02-2026_15153.html
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2026-02-03
- **Date accessed**: 2026-06-06
- **Used by**: Italy
- **Facts supporting**: 2026 INPS `Gestione Separata` rates, including 26.07% professional rate, self-paid professional F24 payment mechanics, and 2026 contribution massimale/minimale context (claim-italy-009)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-291
- **Title**: PwC Worldwide Tax Summaries — Italy individual taxes, residence, other taxes, and tax administration
- **URL**: https://taxsummaries.pwc.com/italy/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/italy/individual/residence ; https://taxsummaries.pwc.com/italy/individual/other-taxes ; https://taxsummaries.pwc.com/italy/individual/tax-administration
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-25
- **Date accessed**: 2026-06-06
- **Used by**: Italy
- **Facts supporting**: Italy tax-residence tests, worldwide-income and foreign-asset reporting, ordinary IRPEF / regional / municipal tax bands, social-security context for VAT-number self-employed professionals, Modello 730 vs Modello Redditi PF filing mechanics, joint-filing caveat, and payment deadlines (claim-italy-006)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-25

## src-292
- **Title**: Forfettari.it — Coefficienti di Redditività ATECO 2026
- **URL**: https://www.forfettari.it/coefficienti-ateco.php
- **Archive**: [archive: failed 2026-06-06; text mirror used for extraction]
- **Type**: commercial
- **Date published**: unknown; 2026 page title
- **Date accessed**: 2026-06-06
- **Used by**: Italy
- **Facts supporting**: commercial coefficient table showing `Informatica e comunicazione` / ATECO 58-63 at 67% profitability and 33% presumed costs for the forfetario calculation (claim-italy-010)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-06

## src-293
- **Title**: open.er-api.com — USD exchange-rate feed
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: failed 2026-06-06; direct JSON extraction used]
- **Type**: commercial
- **Date published**: 2026-06-06
- **Date accessed**: 2026-06-06
- **Used by**: Italy; Greece; Croatia; Malta; Czech Republic
- **Facts supporting**: run-date USD/EUR conversion of 1 USD = EUR 0.865342 used for Italy section 5.3 worked forfetario / INPS budget example (claim-italy-011), Greece section 5.3 PIT-only business-profit example (claim-greece-011), Croatia section 5.3 ordinary self-employment stress test (claim-croatia-011), and Malta section 5.3 ordinary / NRP tax examples (claim-malta-011); run-date USD/CZK conversion of 1 USD = CZK 20.891673 used for Czech Republic flat-tax worked example (claim-czech-011)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-06

## src-294
- **Title**: AADE — Tax residence for natural persons (Income Tax Code)
- **URL**: https://www.aade.gr/en/greeks-abroad-non-residents/income-taxation/tax-residence-natural-persons-itc
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-06
- **Used by**: Greece
- **Facts supporting**: Greek tax-residence tests: permanent/principal residence, habitual abode, centre of vital interests, and more-than-183-days presence in any 12-month period (claim-greece-006)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-06

## src-295
- **Title**: PwC Worldwide Tax Summaries — Greece individual taxes on personal income
- **URL**: https://taxsummaries.pwc.com/greece/individual/taxes-on-personal-income
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-16
- **Date accessed**: 2026-06-06
- **Used by**: Greece
- **Facts supporting**: 2026 Greek unified PIT scale for employment, pensions, and business profits: 9%, 20%, 26%, 34%, and 44% brackets; used for the Greece section 5.3 USD 3,000/month PIT example (claim-greece-007, claim-greece-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-16

## src-296
- **Title**: PwC Worldwide Tax Summaries — Greece individual income determination
- **URL**: https://taxsummaries.pwc.com/greece/individual/income-determination
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-16
- **Date accessed**: 2026-06-06
- **Used by**: Greece
- **Facts supporting**: Greek tax residents taxed on worldwide income; non-residents taxed on Greek work/source income; separate freelancer/sole-proprietor taxation abolished and business profits use the unified scale (claim-greece-006, claim-greece-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-16

## src-297
- **Title**: AADE — Commencement of activities and changes to registry details
- **URL**: https://www.aade.gr/en/greeks-abroad-non-residents/registration-tax-register/commencement-activities-and-changes-registry-details
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-06
- **Used by**: Greece
- **Facts supporting**: myAADE activity-commencement route for foreign residents / natural persons not served through gov.gr, Form D211, and headquarters/use-of-space evidence for self-employed registration (claim-greece-009)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-298
- **Title**: AADE — Issuance of Tax Identification Number and Authentication Key and appointment of tax representative
- **URL**: https://www.aade.gr/en/greeks-abroad-non-residents/registration-tax-register/issuance-tax-identification-number-and-authentication-key-and-appointment
- **Archive**: stable official domain via text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-06
- **Used by**: Greece
- **Facts supporting**: electronic TIN and authentication-key application through myAADE, in-person or myAADElive identification, and representative filing mechanics (claim-greece-009)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-299
- **Title**: PwC Worldwide Tax Summaries — Greece other taxes and tax administration
- **URL**: https://taxsummaries.pwc.com/greece/individual/other-taxes ; https://taxsummaries.pwc.com/greece/individual/tax-administration
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-16
- **Date accessed**: 2026-06-06
- **Used by**: Greece
- **Facts supporting**: VAT baseline, electronic individual return filing, 15 March to 15 July filing window, 55% prepayment for non-withheld freelance/business income, and marriage/civil-partnership joint-return mechanics (claim-greece-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-16

## src-300
- **Title**: AADE and PwC — Greece Article 5C new-tax-resident incentive
- **URL**: https://www.aade.gr/en/greeks-abroad-non-residents/income-taxation/tax-incentives-order-attract-new-tax-residents ; https://taxsummaries.pwc.com/greece/individual/other-tax-credits-and-incentives
- **Archive**: stable AADE official domain via text mirror; PwC archive failed 2026-06-06, direct HTML extraction used
- **Type**: official-primary; reputable-secondary
- **Date published**: AADE unknown; PwC reviewed 2026-02-16
- **Date accessed**: 2026-06-06
- **Used by**: Greece
- **Facts supporting**: Article 5C special taxation for new Greek tax residents earning salaried employment and/or business-activity income in Greece; 50% income-tax exemption described by PwC; application-timing caveats and foreign-client IT fit gap (claim-greece-008, claim-greece-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-16


## src-301
- **Title**: Cyprus Tax Department — Tax rates for income tax from 1991
- **URL**: https://www.mof.gov.cy/mof/TAX/taxdep.nsf/All/9F836EBDE0C59EDDC225825000322C38?OpenDocument
- **Archive**: stable official domain; direct HTML extraction used with SSL verification disabled due local certificate-chain failure
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-06
- **Used by**: Cyprus
- **Facts supporting**: Cyprus individual PIT bands for 2011 onward: 0%, 20%, 25%, 30%, and 35% brackets (claim-cyprus-007, claim-cyprus-011)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-302
- **Title**: PwC Worldwide Tax Summaries — Cyprus individual taxes and residence
- **URL**: https://taxsummaries.pwc.com/cyprus/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/cyprus/individual/residence
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-05-18
- **Date accessed**: 2026-06-06
- **Used by**: Cyprus
- **Facts supporting**: Cyprus resident worldwide-income / non-resident Cyprus-source baseline and 183-day / 60-day tax-residence rules (claim-cyprus-006)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-18

## src-303
- **Title**: PwC Worldwide Tax Summaries — Cyprus other taxes, deductions, and tax administration
- **URL**: https://taxsummaries.pwc.com/cyprus/individual/other-taxes ; https://taxsummaries.pwc.com/cyprus/individual/deductions ; https://taxsummaries.pwc.com/cyprus/individual/tax-administration
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-05-18
- **Date accessed**: 2026-06-06
- **Used by**: Cyprus
- **Facts supporting**: self-employed Social Insurance contribution rate, contribution-limit caveat, GHS/deduction context, calendar tax year, e-filing due dates, and individual-taxation baseline (claim-cyprus-008, claim-cyprus-010, claim-cyprus-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-18

## src-304
- **Title**: Cyprus Tax Department — General Healthcare System (GESY) contributions
- **URL**: https://www.mof.gov.cy/mof/TAX/taxdep.nsf/All/F27BF90AF3990FD6C225857E002C04CF?OpenDocument
- **Archive**: stable official domain; direct HTML extraction used with SSL verification disabled due local certificate-chain failure
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-06
- **Used by**: Cyprus
- **Facts supporting**: self-employed GHS/GESY contribution rate of 4.00% from 1 July 2020 onward (claim-cyprus-008, claim-cyprus-011)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-305
- **Title**: Cyprus Tax Department and Social Insurance Services — tax / self-employed registration anchors
- **URL**: https://www.mof.gov.cy/mof/TAX/taxdep.nsf/All/781EF8626258458AC22584710036A93E?OpenDocument ; https://www.mlsi.gov.cy/mlsi/sid/sidv2.nsf/page33_en/page33_en?OpenDocument
- **Archive**: stable official domains; direct HTML extraction used with SSL verification disabled due local certificate-chain failure
- **Type**: official-primary
- **Date published**: unknown; Social Insurance page modified 2026-06-04
- **Date accessed**: 2026-06-06
- **Used by**: Cyprus
- **Facts supporting**: tax-registration/data-amendment and employee/self-employed registration / online contribution-payment route anchors (claim-cyprus-009)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-306
- **Title**: PwC Worldwide Tax Summaries — Croatia individual taxes on personal income
- **URL**: https://taxsummaries.pwc.com/croatia/individual/taxes-on-personal-income
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-30
- **Date accessed**: 2026-06-06
- **Used by**: Croatia
- **Facts supporting**: Croatian worldwide-income tax-residence baseline, local progressive PIT rates for annual income, self-employment inclusion in annual income, EUR 60,000 lower bracket, and local-rate ranges of 15%-23% / 25%-33% (claim-croatia-006, claim-croatia-008, claim-croatia-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-30

## src-307
- **Title**: PwC Worldwide Tax Summaries — Croatia individual residence
- **URL**: https://taxsummaries.pwc.com/croatia/individual/residence
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-30
- **Date accessed**: 2026-06-06
- **Used by**: Croatia
- **Facts supporting**: Croatian PIT residence rules based on real estate available for at least 183 days or physical presence for at least 183 days in one or two calendar years, plus family/work-location and DTT tie-breaker context (claim-croatia-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-30

## src-308
- **Title**: PwC Worldwide Tax Summaries — Croatia individual income determination
- **URL**: https://taxsummaries.pwc.com/croatia/individual/income-determination
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-30
- **Date accessed**: 2026-06-06
- **Used by**: Croatia
- **Facts supporting**: Croatian self-employment income categories, business-book baseline, receipts-minus-expenses tax base, monthly prepayments, and lump-sum taxation possibility where the taxpayer is outside VAT and annual receipts do not exceed EUR 60,000 (claim-croatia-008, claim-croatia-009)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-30

## src-309
- **Title**: PwC Worldwide Tax Summaries — Croatia individual deductions
- **URL**: https://taxsummaries.pwc.com/croatia/individual/deductions
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-30
- **Date accessed**: 2026-06-06
- **Used by**: Croatia
- **Facts supporting**: EUR 600 monthly personal allowance, EUR 300 monthly dependent-family-member allowance, and mandatory health-insurance contribution deduction context used in the Croatia section 5.3 worked example (claim-croatia-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-30

## src-310
- **Title**: PwC Worldwide Tax Summaries — Croatia individual other taxes and tax administration
- **URL**: https://taxsummaries.pwc.com/croatia/individual/other-taxes ; https://taxsummaries.pwc.com/croatia/individual/tax-administration
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-30
- **Date accessed**: 2026-06-06
- **Used by**: Croatia
- **Facts supporting**: Croatian pension and health social-contribution baseline, contribution-base caveat by status/circumstances, 25% general VAT rate, no joint PIT filing, annual return deadline, and lump-sum assessment/reporting mechanics (claim-croatia-010, claim-croatia-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-30

## src-311
- **Title**: PwC Worldwide Tax Summaries — Malta individual taxes on personal income
- **URL**: https://taxsummaries.pwc.com/malta/individual/taxes-on-personal-income
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-06
- **Used by**: Malta
- **Facts supporting**: Malta tax-residence scope, 2026 PIT bands, NRP authorised-work 10% tax rule and first-year relief concept, and USD 3,000/month Malta tax examples (claim-malta-006, claim-malta-007, claim-malta-008, claim-malta-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-312
- **Title**: PwC Worldwide Tax Summaries — Malta individual residence
- **URL**: https://taxsummaries.pwc.com/malta/individual/residence
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-06
- **Used by**: Malta
- **Facts supporting**: Malta residence / ordinary residence / domicile and remittance-basis factual caveats (claim-malta-006)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-313
- **Title**: PwC Worldwide Tax Summaries — Malta other taxes
- **URL**: https://taxsummaries.pwc.com/malta/individual/other-taxes
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-06
- **Used by**: Malta
- **Facts supporting**: 2026 self-occupied / self-employed social-security rate and weekly cap, 18% standard VAT, and service small-enterprise EUR 35,000 turnover baseline (claim-malta-009, claim-malta-010, claim-malta-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-314
- **Title**: PwC Worldwide Tax Summaries — Malta deductions and tax administration
- **URL**: https://taxsummaries.pwc.com/malta/individual/deductions ; https://taxsummaries.pwc.com/malta/individual/tax-administration
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-06
- **Used by**: Malta
- **Facts supporting**: no general personal allowances, business deductions baseline, calendar-year filing, end-June return due date, responsible-spouse / separate-computation mechanics, and self-employed provisional-tax instalments (claim-malta-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-315
- **Title**: Legislation Malta — Legal Notice 277 of 2023, Nomad Residence Permits (Income Tax) Rules, 2023
- **URL**: https://legislation.mt/eli/ln/2023/277/eng
- **Archive**: stable official domain via direct HTML extraction — snapshot not required
- **Type**: official-primary
- **Date published**: 2023-12-07
- **Date accessed**: 2026-06-06
- **Used by**: Malta
- **Facts supporting**: official legal-notice metadata anchor for Malta NRP income-tax rules; full rule text / article-level extraction remains a verification item (claim-malta-008)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-06

## src-316
- **Title**: PwC Worldwide Tax Summaries — Czech Republic individual taxes on personal income and residence
- **URL**: https://taxsummaries.pwc.com/czech-republic/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/czech-republic/individual/residence
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-07
- **Date accessed**: 2026-06-06
- **Used by**: Czech Republic
- **Facts supporting**: Czech tax-residence scope / worldwide-income baseline, permanent-home and 183-day residence tests, 2026 15% / 23% PIT brackets, and threshold of CZK 1,762,812 (claim-czech-006, claim-czech-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-07

## src-317
- **Title**: PwC Worldwide Tax Summaries — Czech Republic individual deductions and tax administration
- **URL**: https://taxsummaries.pwc.com/czech-republic/individual/deductions ; https://taxsummaries.pwc.com/czech-republic/individual/tax-administration
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-07
- **Date accessed**: 2026-06-06
- **Used by**: Czech Republic
- **Facts supporting**: self-employed actual-expense and percentage-expense deduction baseline, 60% / 40% lump-sum expense categories, CZK 2 million cap mechanics, calendar-year filing, 1 April / 1 May / 1 July filing deadlines, and tax-adviser extension context (claim-czech-008)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-07

## src-318
- **Title**: PwC Worldwide Tax Summaries — Czech Republic individual other taxes
- **URL**: https://taxsummaries.pwc.com/czech-republic/individual/other-taxes
- **Archive**: [archive: failed 2026-06-06; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-07
- **Date accessed**: 2026-06-06
- **Used by**: Czech Republic
- **Facts supporting**: Czech social-security / health-insurance contribution context, 2026 social-security assessment-base cap, sickness-insurance caveat for entrepreneurs, and 21% VAT baseline (claim-czech-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-07

## src-319
- **Title**: Czech Financial Administration — Information on the flat-tax institute for 2025 and 2026
- **URL**: https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/pausalni-dan/informace-k-institutu-pausalni-dane-pro-rok-2025
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-06
- **Used by**: Czech Republic
- **Facts supporting**: 2026 flat-tax bands, monthly payments, income/category eligibility bands, 60% expense-category relevance, and payment due date by the 20th day of each month (claim-czech-009, claim-czech-010, claim-czech-011)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-06

## src-320
- **Title**: PwC Worldwide Tax Summaries — Poland individual taxes on personal income
- **URL**: https://taxsummaries.pwc.com/poland/individual/taxes-on-personal-income
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-26
- **Date accessed**: 2026-06-07
- **Used by**: Poland
- **Facts supporting**: Polish worldwide-income baseline for tax residents, 12% / 32% PIT scale, PLN 30,000 tax-free amount, 19% flat business tax option, lump-sum business taxation option, and 12% lump-sum rate for certain designated IT services (claim-poland-011, claim-poland-012, claim-poland-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-26

## src-321
- **Title**: PwC Worldwide Tax Summaries — Poland individual other taxes
- **URL**: https://taxsummaries.pwc.com/poland/individual/other-taxes
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-26
- **Date accessed**: 2026-06-07
- **Used by**: Poland
- **Facts supporting**: self-employed social-security contribution framework, startup and preferential-contribution relief baseline, entrepreneur health contributions by tax form, PLN 830.58/month lump-sum health contribution band for PLN 60,000-300,000 annual revenue, and health-contribution deduction caveats (claim-poland-014, claim-poland-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-26

## src-322
- **Title**: PwC Worldwide Tax Summaries — Poland individual residence and tax administration
- **URL**: https://taxsummaries.pwc.com/poland/individual/residence ; https://taxsummaries.pwc.com/poland/individual/tax-administration
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-26
- **Date accessed**: 2026-06-07
- **Used by**: Poland
- **Facts supporting**: Polish tax residence tests, annual PIT filing deadline by 30 April, tax micro-account / PESEL / NIP mechanics, joint-spouse filing baseline, and business-tax-form caveat for joint filing (claim-poland-011, claim-poland-016)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-26

## src-323
- **Title**: Biznes.gov.pl — How to choose the best form of business activity taxation
- **URL**: https://www.biznes.gov.pl/en/portal/004172
- **Archive**: stable official domain via direct HTML extraction — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-07
- **Used by**: Poland
- **Facts supporting**: official business-tax-form baseline for natural-person entrepreneurs: tax scale, 19% flat tax, lump-sum registered-revenue tax, tax-scale default rule, lump-sum eligibility caveats, and health-contribution dependency on chosen tax form (claim-poland-012, claim-poland-014)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-07

## src-324
- **Title**: PwC Worldwide Tax Summaries — Romania individual taxes on personal income, residence, and tax administration
- **URL**: https://taxsummaries.pwc.com/romania/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/romania/individual/residence ; https://taxsummaries.pwc.com/romania/individual/tax-administration
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-30
- **Date accessed**: 2026-06-07
- **Used by**: Romania
- **Facts supporting**: Romanian tax-residence tests, worldwide-income scope for residents, 10% flat PIT and no local personal-income tax, annual return / payment deadline of 25 May, separate spouse filing, and foreign-income / independent-activity filing baseline (claim-romania-010, claim-romania-011, claim-romania-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-30

## src-325
- **Title**: PwC Worldwide Tax Summaries — Romania individual other taxes and social contributions
- **URL**: https://taxsummaries.pwc.com/romania/individual/other-taxes
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-30
- **Date accessed**: 2026-06-07
- **Used by**: Romania
- **Facts supporting**: 2026 independent/freelance CAS 25% base thresholds, CASS 10% on annual net income with 72-minimum-salary cap, 2026 minimum-salary base values, and 21% standard VAT baseline from 1 August 2025 (claim-romania-012, claim-romania-013, claim-romania-014, claim-romania-016)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-30

## src-326
- **Title**: ANAF — Declaratie unica / SPV-PF filing and Spatiul Privat Virtual registration pages
- **URL**: https://www.anaf.ro/anaf/internet/ANAF/asistenta_contribuabili/declararea_obligatiilor_fiscale/declaratia_unica ; https://www.anaf.ro/anaf/internet/ANAF/servicii_online/inreg_inrol_pf_pj_spv
- **Archive**: stable official domain via direct HTML extraction — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-07
- **Used by**: Romania
- **Facts supporting**: official ANAF online filing channel for `declaratie unica` / SPV-PF forms and registration / enrolment of individuals and legal entities in Spatiul Privat Virtual (claim-romania-015)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-07

## src-327
- **Title**: open.er-api.com — USD exchange-rate feed, RON rate
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: failed 2026-06-07; direct JSON extraction used]
- **Type**: commercial
- **Date published**: 2026-06-07
- **Date accessed**: 2026-06-07
- **Used by**: Romania
- **Facts supporting**: run-date USD/RON conversion of 1 USD = RON 4.517763 used for Romania section 5.3 PFA / independent-activity tax stress test (claim-romania-016)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-07

## src-328
- **Title**: PwC Worldwide Tax Summaries — Bulgaria individual taxes on personal income and residence
- **URL**: https://taxsummaries.pwc.com/bulgaria/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/bulgaria/individual/residence
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-30
- **Date accessed**: 2026-06-07
- **Used by**: Bulgaria
- **Facts supporting**: Bulgarian tax-residence tests, worldwide-income / Bulgarian-source-income scope, services-rendered-in-Bulgaria source rule, and 10% flat PIT baseline (claim-bulgaria-012, claim-bulgaria-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-30

## src-329
- **Title**: PwC Worldwide Tax Summaries — Bulgaria individual other taxes, deductions, and tax administration
- **URL**: https://taxsummaries.pwc.com/bulgaria/individual/other-taxes ; https://taxsummaries.pwc.com/bulgaria/individual/deductions ; https://taxsummaries.pwc.com/bulgaria/individual/tax-administration
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-30
- **Date accessed**: 2026-06-07
- **Used by**: Bulgaria
- **Facts supporting**: 25% statutory freelance expense deduction, 2026 freelancer minimum/maximum insurance base, non-EU/EEA social/health contribution caveat, 20% standard VAT headline, annual return / quarterly advance-tax mechanics, and separate-spouse taxation (claim-bulgaria-014, claim-bulgaria-015, claim-bulgaria-016, claim-bulgaria-017)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-30

## src-330
- **Title**: PwC Worldwide Tax Summaries — Bulgaria corporate other taxes / VAT registration threshold
- **URL**: https://taxsummaries.pwc.com/bulgaria/corporate/other-taxes
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-30
- **Date accessed**: 2026-06-07
- **Used by**: Bulgaria
- **Facts supporting**: 2026 mandatory VAT registration threshold of EUR 51,130, calendar-year turnover test, and 7-day application deadline after exceeding the threshold (claim-bulgaria-016)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-30

## src-331
- **Title**: open.er-api.com — USD exchange-rate feed, BGN rate
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: failed 2026-06-07; direct JSON extraction used]
- **Type**: commercial
- **Date published**: 2026-06-07
- **Date accessed**: 2026-06-07
- **Used by**: Bulgaria
- **Facts supporting**: run-date USD/BGN conversion of 1 USD = BGN 1.690673 used for Bulgaria section 5.3 freelancer tax stress test (claim-bulgaria-017)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-07

## src-332
- **Title**: PwC Worldwide Tax Summaries — Hungary individual taxes on personal income and residence
- **URL**: https://taxsummaries.pwc.com/hungary/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/hungary/individual/residence
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-31
- **Date accessed**: 2026-06-07
- **Used by**: Hungary
- **Facts supporting**: Hungarian tax-residence tests, 15% PIT rate, independent-activity inclusion in the consolidated tax base, and 90%-of-gross or actual-cost independent-activity tax-base mechanics (claim-hungary-010, claim-hungary-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-31

## src-333
- **Title**: PwC Worldwide Tax Summaries — Hungary individual other taxes and social contributions
- **URL**: https://taxsummaries.pwc.com/hungary/individual/other-taxes
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-31
- **Date accessed**: 2026-06-07
- **Used by**: Hungary
- **Facts supporting**: 18.5% employee social-security contribution, 13% employer-side social tax, 2026 minimum wage / guaranteed minimum wage, non-Hungarian employer compliance caveat, 2026 healthcare service contribution, and individual VAT headline context (claim-hungary-012, claim-hungary-013, claim-hungary-014)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-31

## src-334
- **Title**: PwC Worldwide Tax Summaries — Hungary corporate other taxes / VAT rates
- **URL**: https://taxsummaries.pwc.com/hungary/corporate/other-taxes
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-31
- **Date accessed**: 2026-06-07
- **Used by**: Hungary
- **Facts supporting**: general 27% VAT rate and reduced 18% / 5% VAT-rate context for Hungary (claim-hungary-014)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-31

## src-335
- **Title**: PwC Worldwide Tax Summaries — Hungary individual tax administration
- **URL**: https://taxsummaries.pwc.com/hungary/individual/tax-administration
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-31
- **Date accessed**: 2026-06-07
- **Used by**: Hungary
- **Facts supporting**: calendar-year taxation, annual individual tax return deadline of 20 May following the tax year, self-assessment / NAV draft-return caveat, and separate spouse filing (claim-hungary-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-31

## src-336
- **Title**: open.er-api.com — USD exchange-rate feed, HUF rate
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: failed 2026-06-07; direct JSON extraction used]
- **Type**: commercial
- **Date published**: 2026-06-07
- **Date accessed**: 2026-06-07
- **Used by**: Hungary
- **Facts supporting**: run-date USD/HUF conversion of 1 USD = HUF 306.3855 used for Hungary section 5.3 independent-activity tax stress test (claim-hungary-016)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-07

## src-337
- **Title**: e-EFKA — 2026 insurance-category choice for main insurance, health care, auxiliary insurance and lump-sum benefits
- **URL**: https://www.efka.gov.gr/el/asphalismenoi/me-misthotoi/neo-systhma-asfalistikon-eisforon/eleftheroi-epaggelmaties-aftoapasxoloumenoi
- **Archive**: stable official domain; direct HTML extraction used
- **Type**: official-primary
- **Date published**: 2026-01-01 effective table; page dated 2020-12-21
- **Date accessed**: 2026-06-07
- **Used by**: Greece
- **Facts supporting**: 2026 EFKA freelancer / self-employed contribution categories, including category-1 main pension plus health amount of EUR 250.77/month, EUR 10 unemployment add-on, and separate auxiliary / lump-sum benefit categories (claim-greece-012)
- **Confidence ceiling**: high
- **Stale at**: 2027-01-01

## src-338
- **Title**: PwC Worldwide Tax Summaries — Slovak Republic individual taxes on personal income, residence, and tax administration
- **URL**: https://taxsummaries.pwc.com/slovak-republic/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/slovak-republic/individual/residence ; https://taxsummaries.pwc.com/slovak-republic/individual/tax-administration
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-20
- **Date accessed**: 2026-06-07
- **Used by**: Slovakia
- **Facts supporting**: Slovak tax-residence tests, worldwide-income scope, 2026 PIT-rate baseline, 2026 return threshold and filing deadlines, electronic communication obligation, and separate-spouse filing (claim-slovakia-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-20

## src-339
- **Title**: PwC Worldwide Tax Summaries — Slovak Republic individual deductions and private-entrepreneur lump-sum expenses
- **URL**: https://taxsummaries.pwc.com/slovak-republic/individual/deductions
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-20
- **Date accessed**: 2026-06-07
- **Used by**: Slovakia
- **Facts supporting**: private-entrepreneur ordinary expenses, 60% lump-sum expense option capped at EUR 20,000/year for non-VAT payers, 2026 personal allowance, and dependent-spouse allowance context (claim-slovakia-011, claim-slovakia-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-20

## src-340
- **Title**: Social Insurance Agency Slovakia — Tables for payment of insurance premiums from 1 January 2026
- **URL**: https://www.socpoist.sk/socialne-poistenie/platenie-poistneho/tabulky-platenia-poistneho/tabulky-platenia-poistneho-od-1-6?ref=2435
- **Archive**: stable official domain; direct HTML extraction used
- **Type**: official-primary
- **Date published**: 2026-01-01 effective table
- **Date accessed**: 2026-06-07
- **Used by**: Slovakia
- **Facts supporting**: 2026 SZCO minimum assessment base of EUR 914.40/month, minimum social-insurance contribution of EUR 303.11/month, maximum assessment base of EUR 16,764/month, and prior-year income threshold note (claim-slovakia-012)
- **Confidence ceiling**: high
- **Stale at**: 2027-01-01

## src-341
- **Title**: Vseobecna zdravotna poistovna / Dovera — 2026 SZCO health-insurance advances
- **URL**: https://www.vszp.sk/platitelia/platenie-poistneho/oznamenia-zmeny/zmeny-od-01-01.2026/ ; https://www.dovera.sk/platitel/samoplatitel-szco/tema-platba-poistneho/kolko-platit-v-roku-2026
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2025-11-11 for Dovera; 2026 update page for VZP
- **Date accessed**: 2026-06-07
- **Used by**: Slovakia
- **Facts supporting**: 2026 SZCO public health-insurance minimum advance of EUR 121.92/month for a person without disability, EUR 762.00 minimum health assessment base, and 16% rate (claim-slovakia-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-01

## src-342
- **Title**: PwC Worldwide Tax Summaries — Slovak Republic corporate other taxes / VAT
- **URL**: https://taxsummaries.pwc.com/slovak-republic/corporate/other-taxes
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-20
- **Date accessed**: 2026-06-07
- **Used by**: Slovakia
- **Facts supporting**: Slovak 23% standard VAT rate, EUR 50,000 annual turnover registration threshold, EUR 62,500 immediate-registration threshold, voluntary registration, and reverse-charge context (claim-slovakia-014)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-20

## src-343
- **Title**: European Central Bank — Euro foreign exchange reference rates, USD rate
- **URL**: https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml
- **Archive**: stable official XML feed; direct XML extraction used
- **Type**: official-primary
- **Date published**: 2026-06-05
- **Date accessed**: 2026-06-07
- **Used by**: Slovakia
- **Facts supporting**: EUR/USD reference rate of EUR 1 = USD 1.1640 used for Slovakia USD 3,000/month tax stress test (claim-slovakia-015)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-07

## src-344
- **Title**: PwC Worldwide Tax Summaries — Slovenia individual taxes on personal income and residence
- **URL**: https://taxsummaries.pwc.com/slovenia/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/slovenia/individual/residence
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-06
- **Date accessed**: 2026-06-07
- **Used by**: Slovenia
- **Facts supporting**: Slovenian tax-residence tests, resident worldwide-income scope, non-resident Slovenia-source scope, and 2025/2026 progressive PIT band baseline used for section 5.3 stress test (claim-slovenia-009, claim-slovenia-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-06

## src-345
- **Title**: PwC Worldwide Tax Summaries — Slovenia individual other taxes / social security contributions
- **URL**: https://taxsummaries.pwc.com/slovenia/individual/other-taxes
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-06
- **Date accessed**: 2026-06-07
- **Used by**: Slovenia
- **Facts supporting**: self-employed obligation to pay income tax and social-security contributions themselves; employee-side 22.10%, employer-side 16.10%, and aggregate 38.20% social-contribution rate table used as a conservative stress-test baseline (claim-slovenia-010, claim-slovenia-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-06

## src-346
- **Title**: PwC Worldwide Tax Summaries — Slovenia individual deductions and tax administration
- **URL**: https://taxsummaries.pwc.com/slovenia/individual/deductions ; https://taxsummaries.pwc.com/slovenia/individual/tax-administration
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-06
- **Date accessed**: 2026-06-07
- **Used by**: Slovenia
- **Facts supporting**: EUR 5,000 general allowance where total income is EUR 16,000 or above, calendar-year tax period, annual PIT assessment mechanics, business-activity tax return by 31 March, and monthly prepayment reporting for employment income from a non-Slovenian payer (claim-slovenia-009, claim-slovenia-011, claim-slovenia-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-06

## src-347
- **Title**: PwC Worldwide Tax Summaries — Slovenia corporate other taxes / VAT
- **URL**: https://taxsummaries.pwc.com/slovenia/corporate/other-taxes
- **Archive**: [archive: failed 2026-06-07; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-06
- **Date accessed**: 2026-06-07
- **Used by**: Slovenia
- **Facts supporting**: 22% standard VAT rate, EUR 60,000 VAT registration threshold from 1 January 2025, VAT return timing, and EU B2B reverse-charge / recapitulative-statement context (claim-slovenia-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-06

## src-348
- **Title**: European Central Bank — Euro foreign exchange reference rates, USD rate
- **URL**: https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml
- **Archive**: stable official XML feed; direct XML extraction used
- **Type**: official-primary
- **Date published**: 2026-06-05
- **Date accessed**: 2026-06-07
- **Used by**: Slovenia; Montenegro
- **Facts supporting**: EUR/USD reference rate of EUR 1 = USD 1.1640 used for Slovenia and Montenegro USD 3,000/month tax stress tests (claim-slovenia-012, claim-slovenia-013, claim-montenegro-016)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-07

## src-349
- **Title**: PwC Worldwide Tax Summaries — Montenegro individual taxes on personal income and residence
- **URL**: https://taxsummaries.pwc.com/montenegro/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/montenegro/individual/residence
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-27
- **Date accessed**: 2026-06-08
- **Used by**: Montenegro
- **Facts supporting**: Montenegro tax-residence tests, resident worldwide-income / non-resident source-income baseline, and salary / entrepreneurial-income PIT bands used for the USD 3,000/month tax stress test (claim-montenegro-012, claim-montenegro-013, claim-montenegro-016)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-27

## src-350
- **Title**: PwC Worldwide Tax Summaries — Montenegro individual other taxes / social security contributions
- **URL**: https://taxsummaries.pwc.com/montenegro/individual/other-taxes
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-27
- **Date accessed**: 2026-06-08
- **Used by**: Montenegro
- **Facts supporting**: Montenegro salary social-security contribution baseline of 10% employee pension/disability plus 0.5% employee unemployment and 0.5% employer unemployment, and statement that SSC are also levied on other personal income under the SSC Law (claim-montenegro-014, claim-montenegro-016)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-27

## src-351
- **Title**: PwC Worldwide Tax Summaries — Montenegro individual tax administration
- **URL**: https://taxsummaries.pwc.com/montenegro/individual/tax-administration
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-27
- **Date accessed**: 2026-06-08
- **Used by**: Montenegro
- **Facts supporting**: Montenegro calendar-year tax period, annual tax return by end-April, tax payment on submission where not withheld, and 12 monthly instalments for entrepreneurial-income tax (claim-montenegro-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-27

## src-352
- **Title**: PwC Worldwide Tax Summaries — Montenegro corporate other taxes / VAT
- **URL**: https://taxsummaries.pwc.com/montenegro/corporate/other-taxes
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-27
- **Date accessed**: 2026-06-08
- **Used by**: Montenegro
- **Facts supporting**: Montenegro VAT context, including standard 21% VAT rate and reduced 15%, 7%, and 0% rates; used as VAT background for foreign-client IT tax checks (claim-montenegro-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-27

## src-353
- **Title**: PwC Worldwide Tax Summaries — Serbia individual residence
- **URL**: https://taxsummaries.pwc.com/serbia/individual/residence
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-25
- **Date accessed**: 2026-06-08
- **Used by**: Serbia
- **Facts supporting**: Serbia tax-residence tests and resident worldwide-income / non-resident Serbian-source and Serbia-related worldwide-income baseline (claim-serbia-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-25

## src-354
- **Title**: PwC Worldwide Tax Summaries — Serbia individual taxes on personal income and income determination
- **URL**: https://taxsummaries.pwc.com/serbia/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/serbia/individual/income-determination
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-25
- **Date accessed**: 2026-06-08
- **Used by**: Serbia
- **Facts supporting**: Serbia PIT range, 10% employment PIT after RSD 34,221 salary cap, self-employment / entrepreneurial-income categories, VAT-registered individual as self-employment taxpayer, and lump-sum sole-proprietor caveat (claim-serbia-012, claim-serbia-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-25

## src-355
- **Title**: Serbia freelancer portal — FAQ and home page for foreign-payer self-taxation
- **URL**: https://frilenseri.purs.gov.rs/en/ ; https://frilenseri.purs.gov.rs/en/faq.html
- **Archive**: stable gov domain — snapshot not required; direct HTTPS blocked by legacy TLS, Jina text mirror used for extraction while citing original URLs
- **Type**: official-primary
- **Date published**: no page date captured
- **Date accessed**: 2026-06-08
- **Used by**: Serbia
- **Facts supporting**: official freelancer portal scope for natural persons with foreign-payer income, resident/non-resident adult registration baseline, and warning that portal registration enables tax application/payment but does not create a legal status (claim-serbia-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-08

## src-356
- **Title**: PwC Worldwide Tax Summaries — Serbia individual other taxes and tax administration
- **URL**: https://taxsummaries.pwc.com/serbia/individual/other-taxes ; https://taxsummaries.pwc.com/serbia/individual/tax-administration
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-25
- **Date accessed**: 2026-06-08
- **Used by**: Serbia
- **Facts supporting**: Serbia social-security contribution rates and min/max base baseline, electronic tax returns, offshore-income return timing, supplementary annual PIT filing mechanics, and dependent-family deductions for supplementary annual tax (claim-serbia-014, claim-serbia-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-25

## src-357
- **Title**: PwC Worldwide Tax Summaries — Serbia corporate other taxes / VAT
- **URL**: https://taxsummaries.pwc.com/serbia/corporate/other-taxes
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-25
- **Date accessed**: 2026-06-08
- **Used by**: Serbia
- **Facts supporting**: Serbia VAT context, including 20% standard rate, 10% reduced rate, 0% export-related context, VAT-taxpayer definition for independent business/service/self-employed activities, and foreign-entity VAT-registration caveat (claim-serbia-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-25

## src-358
- **Title**: XE Currency Converter — USD to Serbian dinar snapshot
- **URL**: https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=RSD
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: live rate snapshot, no static publication date
- **Date accessed**: 2026-06-08
- **Used by**: Serbia
- **Facts supporting**: USD/RSD rate snapshot of about 1 USD = RSD 100.72 used only for Serbia section 5.3 worked example (claim-serbia-015)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08


## src-359
- **Title**: PwC Worldwide Tax Summaries — Turkey individual residence
- **URL**: https://taxsummaries.pwc.com/turkey/individual/residence
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-27
- **Date accessed**: 2026-06-08
- **Used by**: Turkey
- **Facts supporting**: Turkey tax-residence tests, more-than-six-month foreigner residence rule, full-taxpayer / limited-taxpayer distinction (claim-turkey-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-27

## src-360
- **Title**: PwC Worldwide Tax Summaries — Turkey individual taxes on personal income
- **URL**: https://taxsummaries.pwc.com/turkey/individual/taxes-on-personal-income
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-27
- **Date accessed**: 2026-06-08
- **Used by**: Turkey
- **Facts supporting**: resident worldwide-income / non-resident Turkish-source baseline, foreign-income exemption caveat, 2026 progressive PIT brackets for non-employment income, and no local personal income tax (claim-turkey-010, claim-turkey-012, claim-turkey-014)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-27

## src-361
- **Title**: PwC Worldwide Tax Summaries — Turkey individual income determination
- **URL**: https://taxsummaries.pwc.com/turkey/individual/income-determination
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-27
- **Date accessed**: 2026-06-08
- **Used by**: Turkey
- **Facts supporting**: foreign-national self-employment restriction warning and business / professional income taxability for activities carried out in Turkey or by Turkish tax residents abroad (claim-turkey-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-27

## src-362
- **Title**: PwC Worldwide Tax Summaries — Turkey individual other taxes and tax administration
- **URL**: https://taxsummaries.pwc.com/turkey/individual/other-taxes ; https://taxsummaries.pwc.com/turkey/individual/tax-administration
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-27
- **Date accessed**: 2026-06-08
- **Used by**: Turkey
- **Facts supporting**: 2026 employee-style social-security and unemployment contribution rates / bases, foreign-coverage exemption caveat, annual return deadline, March/July payment instalments, and 15% quarterly advance tax for commercial or professional income (claim-turkey-013, claim-turkey-014)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-27

## src-363
- **Title**: PwC Worldwide Tax Summaries — Turkey corporate other taxes / VAT
- **URL**: https://taxsummaries.pwc.com/turkey/corporate/other-taxes
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-27
- **Date accessed**: 2026-06-08
- **Used by**: Turkey
- **Facts supporting**: Turkey VAT context, including 1%-20% VAT rate range, 20% general rate, input/output VAT mechanism, and VAT-return context for later foreign-client IT checks (claim-turkey-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-27

## src-364
- **Title**: XE Currency Converter — USD to Turkish lira snapshot
- **URL**: https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=TRY
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: commercial
- **Date published**: live rate snapshot, no static publication date
- **Date accessed**: 2026-06-08
- **Used by**: Turkey
- **Facts supporting**: USD/TRY rate snapshot of 1 USD = TRY 46.0952 used only for Turkey section 5.3 worked example (claim-turkey-014)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-365
- **Title**: PwC Worldwide Tax Summaries — Georgia individual taxes on personal income
- **URL**: https://taxsummaries.pwc.com/georgia/individual/taxes-on-personal-income
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-21
- **Date accessed**: 2026-06-08
- **Used by**: Georgia
- **Facts supporting**: Georgia resident foreign-source exemption baseline, 20% flat PIT, micro-business turnover ceiling, and individual-entrepreneur small-business 1% / 3% turnover-tax regime (claim-georgia-008, claim-georgia-009, claim-georgia-010, claim-georgia-012)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-21

## src-366
- **Title**: PwC Worldwide Tax Summaries — Georgia individual residence
- **URL**: https://taxsummaries.pwc.com/georgia/individual/residence
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-21
- **Date accessed**: 2026-06-08
- **Used by**: Georgia
- **Facts supporting**: Georgia individual tax-residence rule of actual presence for 183 days or more in any continuous 12-month period ending in the current tax year (claim-georgia-008)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-21

## src-367
- **Title**: PwC Worldwide Tax Summaries — Georgia individual other taxes
- **URL**: https://taxsummaries.pwc.com/georgia/individual/other-taxes
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-21
- **Date accessed**: 2026-06-08
- **Used by**: Georgia
- **Facts supporting**: no social-security contributions in Georgia; pension contribution context including 4% self-employed contribution sensitivity and government matching limits (claim-georgia-010, claim-georgia-012)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-21

## src-368
- **Title**: PwC Worldwide Tax Summaries — Georgia individual tax administration
- **URL**: https://taxsummaries.pwc.com/georgia/individual/tax-administration
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-21
- **Date accessed**: 2026-06-08
- **Used by**: Georgia
- **Facts supporting**: Georgia calendar tax year and individual income tax declaration deadline before 1 April for income not taxed at source (claim-georgia-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-21

## src-369
- **Title**: PwC Worldwide Tax Summaries — Georgia corporate other taxes / VAT
- **URL**: https://taxsummaries.pwc.com/georgia/corporate/other-taxes
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-21
- **Date accessed**: 2026-06-08
- **Used by**: Georgia
- **Facts supporting**: Georgia 18% VAT rate, GEL 100,000 VAT-registration threshold, B2B/B2C service place-of-supply context, and foreign-client IT VAT verification caveat (claim-georgia-011, claim-georgia-012)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-21

## src-370
- **Title**: ExchangeRate-API — USD to Georgian lari snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: failed 2026-06-08; Wayback returned HTTP 429, direct JSON extraction used]
- **Type**: commercial
- **Date published**: live rate snapshot, time_last_update_utc 2026-06-08T00:02:31Z
- **Date accessed**: 2026-06-08
- **Used by**: Georgia
- **Facts supporting**: USD/GEL rate snapshot of 1 USD = GEL 2.661955 used only for Georgia section 5.3 worked example (claim-georgia-012)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-371
- **Title**: Livingcost — Cost of living in Cyprus
- **URL**: https://livingcost.org/cost/cyprus
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-08
- **Used by**: Cyprus
- **Facts supporting**: Cyprus national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-372
- **Title**: Livingcost — Cost of living in Nicosia
- **URL**: https://livingcost.org/cost/cyprus/nicosia
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-08
- **Used by**: Cyprus
- **Facts supporting**: Nicosia cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-373
- **Title**: Livingcost — Cost of living in Limassol
- **URL**: https://livingcost.org/cost/cyprus/limassol
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-08
- **Used by**: Cyprus
- **Facts supporting**: Limassol cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-374
- **Title**: Livingcost — Cost of living in Larnaca
- **URL**: https://livingcost.org/cost/cyprus/larnaca
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-08
- **Used by**: Cyprus
- **Facts supporting**: Larnaca cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-375
- **Title**: Livingcost — Cost of living in Paphos
- **URL**: https://livingcost.org/cost/cyprus/paphos
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-08
- **Used by**: Cyprus
- **Facts supporting**: Paphos cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-376
- **Title**: Livingcost — Cost of living in Malta
- **URL**: https://livingcost.org/cost/malta
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-08
- **Used by**: Malta
- **Facts supporting**: Malta national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-377
- **Title**: Livingcost — Cost of living in Valletta
- **URL**: https://livingcost.org/cost/malta/valletta
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-08
- **Used by**: Malta
- **Facts supporting**: Valletta cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-378
- **Title**: Livingcost — Cost of living in Sliema
- **URL**: https://livingcost.org/cost/malta/sliema
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-08
- **Used by**: Malta
- **Facts supporting**: Sliema cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-379
- **Title**: Livingcost — Cost of living in Birkirkara
- **URL**: https://livingcost.org/cost/malta/birkirkara
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-08
- **Used by**: Malta
- **Facts supporting**: Birkirkara cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-380
- **Title**: Livingcost — Cost of living in Marsaskala
- **URL**: https://livingcost.org/cost/malta/marsaskala
- **Archive**: [archive: failed 2026-06-08; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-08
- **Used by**: Malta
- **Facts supporting**: Marsaskala cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-08

## src-381
- **Title**: Livingcost — Cost of living in Croatia
- **URL**: https://livingcost.org/cost/croatia
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Croatia
- **Facts supporting**: Croatia national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-382
- **Title**: Livingcost — Cost of living in Zagreb
- **URL**: https://livingcost.org/cost/croatia/zagreb
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Croatia
- **Facts supporting**: Zagreb cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-383
- **Title**: Livingcost — Cost of living in Split
- **URL**: https://livingcost.org/cost/croatia/split
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Croatia
- **Facts supporting**: Split cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-384
- **Title**: Livingcost — Cost of living in Dubrovnik
- **URL**: https://livingcost.org/cost/croatia/dubrovnik
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Croatia
- **Facts supporting**: Dubrovnik cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-385
- **Title**: Livingcost — Cost of living in Rijeka
- **URL**: https://livingcost.org/cost/croatia/rijeka
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Croatia
- **Facts supporting**: Rijeka cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-386
- **Title**: Livingcost — Cost of living in Greece
- **URL**: https://livingcost.org/cost/greece
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Greece
- **Facts supporting**: Greece national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-387
- **Title**: Livingcost — Cost of living in Athens
- **URL**: https://livingcost.org/cost/greece/athens
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Greece
- **Facts supporting**: Athens cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-388
- **Title**: Livingcost — Cost of living in Thessaloniki
- **URL**: https://livingcost.org/cost/greece/thessaloniki
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Greece
- **Facts supporting**: Thessaloniki cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-389
- **Title**: Livingcost — Cost of living in Heraklion
- **URL**: https://livingcost.org/cost/greece/heraklion
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Greece
- **Facts supporting**: Heraklion cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-390
- **Title**: Livingcost — Cost of living in Patras
- **URL**: https://livingcost.org/cost/greece/patras
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Greece
- **Facts supporting**: Patras cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-391
- **Title**: Livingcost — Cost of living in Spain
- **URL**: https://livingcost.org/cost/spain
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Spain
- **Facts supporting**: Spain national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, national 1BR / 3BR rent bands, doctor-visit proxy, daycare/preschool proxy, and international primary-school proxy
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-392
- **Title**: Livingcost — Cost of living in Madrid
- **URL**: https://livingcost.org/cost/spain/madrid
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Spain
- **Facts supporting**: Madrid cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-393
- **Title**: Livingcost — Cost of living in Valencia, Spain
- **URL**: https://livingcost.org/cost/spain/valencia
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Spain
- **Facts supporting**: Valencia cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, internet, doctor-visit proxy, daycare/preschool proxy, and international primary-school proxy
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-394
- **Title**: Livingcost — Cost of living in Malaga
- **URL**: https://livingcost.org/cost/spain/malaga
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Spain
- **Facts supporting**: Malaga cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, internet, doctor-visit proxy, daycare/preschool proxy, and international primary-school proxy
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-395
- **Title**: Livingcost — Cost of living in Barcelona, Spain
- **URL**: https://livingcost.org/cost/spain/barcelona
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Spain
- **Facts supporting**: Barcelona cost/rent stress test: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-396
- **Title**: Livingcost — Cost of living in Italy
- **URL**: https://livingcost.org/cost/italy
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Italy
- **Facts supporting**: Italy national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, national 1BR / 3BR rent bands, doctor-visit proxy, daycare/preschool proxy, and international-primary-school proxy
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-397
- **Title**: Livingcost — Cost of living in Rome, Italy
- **URL**: https://livingcost.org/cost/italy/lz/rome
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Italy
- **Facts supporting**: Rome cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, internet, doctor-visit proxy, daycare/preschool proxy, and international-primary-school proxy
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-398
- **Title**: Livingcost — Cost of living in Milan, Italy
- **URL**: https://livingcost.org/cost/italy/lo/milan
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Italy
- **Facts supporting**: Milan cost/rent stress test: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, internet, doctor-visit proxy, daycare/preschool proxy, and international-primary-school proxy
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-399
- **Title**: Livingcost — Cost of living in Naples, Italy
- **URL**: https://livingcost.org/cost/italy/cm/naples
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Italy
- **Facts supporting**: Naples cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, internet, doctor-visit proxy, daycare/preschool proxy, and international-primary-school proxy
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-400
- **Title**: Livingcost — Cost of living in Palermo, Italy
- **URL**: https://livingcost.org/cost/italy/si/palermo
- **Archive**: [archive: failed 2026-06-09; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-09
- **Used by**: Italy
- **Facts supporting**: Palermo cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, internet, doctor-visit proxy, daycare/preschool proxy, and international-primary-school proxy
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-09

## src-401
- **Title**: PwC Worldwide Tax Summaries — Portugal, Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/portugal/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-05
- **Date accessed**: 2026-06-09
- **Used by**: Portugal
- **Facts supporting**: 2026 Portuguese resident PIT brackets, worldwide-income baseline, non-resident 25% note, joint-rate mechanics for married / de facto-married taxpayers
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-05

## src-402
- **Title**: PwC Worldwide Tax Summaries — Portugal, Individual: Residence / Tax administration
- **URL**: https://taxsummaries.pwc.com/portugal/individual/residence ; https://taxsummaries.pwc.com/portugal/individual/tax-administration
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-05
- **Date accessed**: 2026-06-09
- **Used by**: Portugal
- **Facts supporting**: Portuguese tax-residence baseline, 30 June PIT filing deadline, joint return option, foreign-account reporting context
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-05

## src-403
- **Title**: PwC Worldwide Tax Summaries — Portugal, Individual: Income determination
- **URL**: https://taxsummaries.pwc.com/portugal/individual/income-determination
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-05
- **Date accessed**: 2026-06-09
- **Used by**: Portugal
- **Facts supporting**: 2026 simplified-regime EUR 200,000 turnover cap, 75% / 35% service coefficients, and expense-evidence adjustment mechanics
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-05

## src-404
- **Title**: PwC Worldwide Tax Summaries — Portugal, Individual other taxes / Corporate other taxes
- **URL**: https://taxsummaries.pwc.com/portugal/individual/other-taxes ; https://taxsummaries.pwc.com/portugal/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-05
- **Date accessed**: 2026-06-09
- **Used by**: Portugal
- **Facts supporting**: 21.4% self-employed social-security rate, 70% service-income relevant remuneration, contribution-base mechanics, 2026 minimum wage, and 23% mainland VAT headline
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-05

## src-405
- **Title**: ePortugal — File the self-employment registration
- **URL**: https://eportugal.gov.pt/en/servicos/abrir-atividade-nas-financas
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: official-primary
- **Date published**: not stated
- **Date accessed**: 2026-06-09
- **Used by**: Portugal
- **Facts supporting**: self-employed workers must register with the Tax Office before starting activity; Finances Portal beginning-of-activity filing path; online filing cost
- **Confidence ceiling**: high
- **Stale at**: 2027-06-09

## src-406
- **Title**: PwC Worldwide Tax Summaries — Portugal, Individual: Significant developments
- **URL**: https://taxsummaries.pwc.com/portugal/individual/significant-developments
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-05
- **Date accessed**: 2026-06-09
- **Used by**: Portugal
- **Facts supporting**: IFICI new-resident incentive outline and former-tax-residents relief caveat
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-05


## src-407
- **Title**: PwC Worldwide Tax Summaries — Albania, Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/albania/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-09
- **Used by**: Albania
- **Facts supporting**: Albanian resident worldwide-income baseline, employment/business income categories, 2025+ employment brackets, self-employed/commercial-individual 0% PIT for gross income up to ALL 14m until 31 Dec 2029, and special expense-deduction regime for turnover up to ALL 10m
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-408
- **Title**: PwC Worldwide Tax Summaries — Albania, Individual: Residence / Tax administration
- **URL**: https://taxsummaries.pwc.com/albania/individual/residence ; https://taxsummaries.pwc.com/albania/individual/tax-administration
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-09
- **Used by**: Albania
- **Facts supporting**: Albanian tax-residence tests, calendar-year tax year, annual PIT / business-income return obligations, 31 March filing deadline, and monthly payment deadline by the 20th day of the following month
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-409
- **Title**: PwC Worldwide Tax Summaries — Albania, Individual: Other taxes / Deductions
- **URL**: https://taxsummaries.pwc.com/albania/individual/other-taxes ; https://taxsummaries.pwc.com/albania/individual/deductions
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-09
- **Used by**: Albania
- **Facts supporting**: self-employed social and health contribution minimums, employee/employer SHC context, electronic monthly reporting timing, deductibility of social/health contributions, personal allowances, and child/education deduction context
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-410
- **Title**: PwC Worldwide Tax Summaries — Albania, Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/albania/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-09
- **Used by**: Albania
- **Facts supporting**: Albania 20% standard VAT, ALL 10m VAT registration threshold, VAT monthly deadlines, and business-entity registration fee ALL 120 / ALL 0 online
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-411
- **Title**: PwC Worldwide Tax Summaries — Albania, Individual: Foreign tax relief and tax treaties / Other tax credits and incentives
- **URL**: https://taxsummaries.pwc.com/albania/individual/foreign-tax-relief-and-tax-treaties ; https://taxsummaries.pwc.com/albania/individual/other-tax-credits-and-incentives
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-09
- **Used by**: Albania
- **Facts supporting**: foreign-tax-credit mechanics, treaty table context, absence of Ukraine in captured Albania DTT list, social-security agreement context, and no other significant individual tax credits/incentives
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-412
- **Title**: ExchangeRate-API open rates — USD to ALL snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-09T00:02:31Z
- **Date accessed**: 2026-06-09
- **Used by**: Albania
- **Facts supporting**: run-083 USD/ALL conversion for the Albania USD 3,000/month tax worked example: USD 1 = ALL 82.543185
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-09

## src-413
- **Title**: PwC Worldwide Tax Summaries — North Macedonia, Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/north-macedonia/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-08
- **Date accessed**: 2026-06-09
- **Used by**: North Macedonia
- **Facts supporting**: North Macedonian resident worldwide-income baseline, non-resident Macedonian-source baseline, 10% flat PIT for work/self-employment/royalties/rent/capital/other income, 15% games-of-chance rate, and 70% unexplained-origin income rate
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-08

## src-414
- **Title**: PwC Worldwide Tax Summaries — North Macedonia, Individual: Residence / Tax administration
- **URL**: https://taxsummaries.pwc.com/north-macedonia/individual/residence ; https://taxsummaries.pwc.com/north-macedonia/individual/tax-administration
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-08
- **Date accessed**: 2026-06-09
- **Used by**: North Macedonia
- **Facts supporting**: tax-residence tests including permanent/temporary residence and 183 days in any 12-month period, calendar-year taxable period, Public Revenue Office draft annual return by 30 April, confirmation/correction by 31 May, business-income annual accounts / return by 15 March, and monthly advance PIT reporting/payment for cases outside domestic withholding
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-08

## src-415
- **Title**: PwC Worldwide Tax Summaries — North Macedonia, Individual: Other taxes
- **URL**: https://taxsummaries.pwc.com/north-macedonia/individual/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-08
- **Date accessed**: 2026-06-09
- **Used by**: North Macedonia
- **Facts supporting**: employee-style mandatory social-contribution base, 50% average-salary minimum base, 16-average-salary maximum base, 18.8% pension/disability, 7.5% health, 1.2% employment, 0.5% additional health, and 28.0% combined contribution-rate screening sensitivity
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-08

## src-416
- **Title**: PwC Worldwide Tax Summaries — North Macedonia, Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/north-macedonia/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-08
- **Date accessed**: 2026-06-09
- **Used by**: North Macedonia
- **Facts supporting**: 18% standard VAT, 5% and 10% reduced rates, MKD 2m VAT registration threshold / projected-turnover rule, optional voluntary registration, monthly or quarterly VAT period, and 25-day return / 30-day payment timing
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-08

## src-417
- **Title**: ExchangeRate-API open rates — USD to MKD snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-09T00:02:31Z
- **Date accessed**: 2026-06-09
- **Used by**: North Macedonia
- **Facts supporting**: run-084 USD/MKD conversion for the North Macedonia USD 3,000/month tax worked example: USD 1 = MKD 52.983164
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-09

## src-418
- **Title**: PwC Worldwide Tax Summaries — Bosnia and Herzegovina, Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-09
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: entity-based personal income tax scope, FBiH resident worldwide-income baseline, FBiH 10% PIT, RS 8% PIT, RS small-entrepreneur 2% revenue note, and Brcko 10% PIT (claim-bosnia-herzegovina-008)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-419
- **Title**: PwC Worldwide Tax Summaries — Bosnia and Herzegovina, Individual: Residence / Tax administration
- **URL**: https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/residence ; https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/tax-administration
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-09
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: FBiH / RS / Brcko tax-residence tests, annual-return deadlines, and entity-specific payroll reporting/payment timing (claim-bosnia-herzegovina-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-420
- **Title**: PwC Worldwide Tax Summaries — Bosnia and Herzegovina, Individual: Other taxes / Deductions
- **URL**: https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/other-taxes ; https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/deductions
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-09
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: FBiH employee/employer social-contribution rates, RS employee contribution rates, Brcko pension-fund choice context, and FBiH / RS personal and dependent allowances for the worked screening sensitivity (claim-bosnia-herzegovina-009)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-421
- **Title**: PwC Worldwide Tax Summaries — Bosnia and Herzegovina, Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/bosnia-and-herzegovina/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-09
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: countrywide 17% VAT, no reduced VAT rate, taxable-person baseline, BAM 100,000 VAT registration threshold, and payroll-tax context (claim-bosnia-herzegovina-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-422
- **Title**: PwC Worldwide Tax Summaries — Bosnia and Herzegovina, Individual: Foreign tax relief and tax treaties
- **URL**: https://taxsummaries.pwc.com/bosnia-and-herzegovina/individual/foreign-tax-relief-and-tax-treaties
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-19
- **Date accessed**: 2026-06-09
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: foreign-tax-credit baseline and DTT applicability for FBiH / RS / Brcko residents
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-19

## src-423
- **Title**: ExchangeRate-API open rates — USD to BAM snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-09T00:02:31Z
- **Date accessed**: 2026-06-09
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: run-085 USD/BAM conversion for the Bosnia and Herzegovina USD 3,000/month tax worked example: USD 1 = BAM 1.69618
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-09

## src-424
- **Title**: PwC Worldwide Tax Summaries — Moldova, Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/moldova/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-14
- **Date accessed**: 2026-06-10
- **Used by**: Moldova
- **Facts supporting**: Moldovan resident / non-resident PIT scope, 12% PIT for employment / professional / entrepreneurial / individual-entrepreneur income, and non-resident income categories
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-14

## src-425
- **Title**: PwC Worldwide Tax Summaries — Moldova, Individual: Residence
- **URL**: https://taxsummaries.pwc.com/moldova/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-14
- **Date accessed**: 2026-06-10
- **Used by**: Moldova
- **Facts supporting**: Moldovan tax-residence tests: permanent domicile or physical presence exceeding / at least 183 days during the fiscal year
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-14

## src-426
- **Title**: PwC Worldwide Tax Summaries — Moldova, Individual: Other taxes / Deductions
- **URL**: https://taxsummaries.pwc.com/moldova/individual/other-taxes ; https://taxsummaries.pwc.com/moldova/individual/deductions
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-14
- **Date accessed**: 2026-06-10
- **Used by**: Moldova
- **Facts supporting**: 2026 employer SSC and employee health-insurance context, fixed annual SSC / health contribution amounts for other taxpayer categories, optional private health insurance caveat for foreigners without local labour agreement, contribution deductibility, and 2026 personal / spouse / dependent allowances
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-14

## src-427
- **Title**: PwC Worldwide Tax Summaries — Moldova, Individual: Tax administration / Foreign tax relief and tax treaties
- **URL**: https://taxsummaries.pwc.com/moldova/individual/tax-administration ; https://taxsummaries.pwc.com/moldova/individual/foreign-tax-relief-and-tax-treaties
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-14
- **Date accessed**: 2026-06-10
- **Used by**: Moldova
- **Facts supporting**: calendar-year PIT period, 30 April annual PIT return/payment deadline, payroll reporting context, foreign-tax-credit baseline, and DTT precedence / fiscal-residence-certificate context
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-14

## src-428
- **Title**: PwC Worldwide Tax Summaries — Moldova, Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/moldova/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-14
- **Date accessed**: 2026-06-10
- **Used by**: Moldova
- **Facts supporting**: 20% standard VAT, reduced VAT context, import-of-services reverse-charge baseline, B2C digital-service VAT context, 2026 MDL 1.5m VAT registration threshold, voluntary registration, and monthly VAT return/payment timing
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-14

## src-429
- **Title**: ExchangeRate-API open rates — USD to MDL snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-10T00:02:31Z
- **Date accessed**: 2026-06-10
- **Used by**: Moldova
- **Facts supporting**: run-086 USD/MDL conversion for the Moldova USD 3,000/month tax worked example: USD 1 = MDL 17.327661
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-10

## src-430
- **Title**: PwC Worldwide Tax Summaries — Uruguay, Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/uruguay/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-09
- **Date accessed**: 2026-06-10
- **Used by**: Uruguay
- **Facts supporting**: Uruguayan-source principle, IRPF work-income progressive rates, 2025 bracket table, family-unit bracket mechanics, and warning not to treat foreign-client services performed from Uruguay as automatically tax-free (claim-uruguay-008)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-09

## src-431
- **Title**: PwC Worldwide Tax Summaries — Uruguay, Individual: Residence
- **URL**: https://taxsummaries.pwc.com/uruguay/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-09
- **Date accessed**: 2026-06-10
- **Used by**: Uruguay
- **Facts supporting**: Uruguay tax-residence tests: more than 183 days, base of activities, economic/vital interests, spouse and dependent-child presumption, and investment-based residence context (claim-uruguay-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-09

## src-432
- **Title**: PwC Worldwide Tax Summaries — Uruguay, Individual: Deductions
- **URL**: https://taxsummaries.pwc.com/uruguay/individual/deductions
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-09
- **Date accessed**: 2026-06-10
- **Used by**: Uruguay
- **Facts supporting**: self-employed 30% notional expense deduction, employee deduction limits, and deduction context for the run-088 tax screening model (claim-uruguay-009, claim-uruguay-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-09

## src-433
- **Title**: PwC Worldwide Tax Summaries — Uruguay, Individual: Other taxes
- **URL**: https://taxsummaries.pwc.com/uruguay/individual/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-09
- **Date accessed**: 2026-06-10
- **Used by**: Uruguay
- **Facts supporting**: Uruguayan social-security contribution context, employee contribution band of 18.1%-23.1%, employer contribution 12.625%, retirement cap, health-insurance family variables, and downside contribution sensitivity (claim-uruguay-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-09

## src-434
- **Title**: PwC Worldwide Tax Summaries — Uruguay, Individual: Tax administration
- **URL**: https://taxsummaries.pwc.com/uruguay/individual/tax-administration
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-09
- **Date accessed**: 2026-06-10
- **Used by**: Uruguay
- **Facts supporting**: resident/non-resident return timing, self-employed tax-registration and advance-payment baseline, 7% withholding note for certain self-employed service income above about UYU 63,000, and payment/withholding mechanics
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-09

## src-435
- **Title**: PwC Worldwide Tax Summaries — Uruguay, Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/uruguay/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-03-09
- **Date accessed**: 2026-06-10
- **Used by**: Uruguay
- **Facts supporting**: Uruguay VAT headline context: 22% general rate and 10% reduced-rate context; used only as VAT-risk baseline pending DGI/accountant confirmation for foreign-client IT services
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-09

## src-436
- **Title**: ExchangeRate-API open rates — USD to UYU snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-10T00:02:31Z
- **Date accessed**: 2026-06-10
- **Used by**: Uruguay
- **Facts supporting**: run-088 USD/UYU conversion for the Uruguay USD 3,000/month tax worked example: USD 1 = UYU 40.474288 (claim-uruguay-010)
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-10

## src-437
- **Title**: PwC Worldwide Tax Summaries — Paraguay, Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/paraguay/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-07
- **Date accessed**: 2026-06-10
- **Used by**: Paraguay
- **Facts supporting**: Paraguay PIT source scope, personal-service income inclusion, progressive 8%/9%/10% personal-service income brackets, PYG 80m gross-income no-tax threshold, and 8% capital-gains baseline (claim-paraguay-008, claim-paraguay-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-07

## src-438
- **Title**: PwC Worldwide Tax Summaries — Paraguay, Individual: Residence
- **URL**: https://taxsummaries.pwc.com/paraguay/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-07
- **Date accessed**: 2026-06-10
- **Used by**: Paraguay
- **Facts supporting**: Paraguay tax-residence rule: more than 120 days in a year in Paraguay (claim-paraguay-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-07

## src-439
- **Title**: PwC Worldwide Tax Summaries — Paraguay, Individual: Deductions
- **URL**: https://taxsummaries.pwc.com/paraguay/individual/deductions
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-07
- **Date accessed**: 2026-06-10
- **Used by**: Paraguay
- **Facts supporting**: Paraguay deductible expense context for personal-service taxpayers, including local personal/family expenses, health/education expenses, and independent personal-service provider private social-security contributions (claim-paraguay-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-07

## src-440
- **Title**: PwC Worldwide Tax Summaries — Paraguay, Individual: Other taxes
- **URL**: https://taxsummaries.pwc.com/paraguay/individual/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-07
- **Date accessed**: 2026-06-10
- **Used by**: Paraguay
- **Facts supporting**: Paraguay social-security context: employer registration framework, commercial-entity employee 9% and employer 16.5% rates, and optional contribution caveat for some independent positions (claim-paraguay-009, claim-paraguay-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-07

## src-441
- **Title**: PwC Worldwide Tax Summaries — Paraguay, Individual: Tax administration
- **URL**: https://taxsummaries.pwc.com/paraguay/individual/tax-administration
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-07
- **Date accessed**: 2026-06-10
- **Used by**: Paraguay
- **Facts supporting**: Paraguay calendar-year taxable period, March PIT return deadline, and payment due with the return according to taxpayer-ID schedule
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-07

## src-442
- **Title**: PwC Worldwide Tax Summaries — Paraguay, Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/paraguay/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-07
- **Date accessed**: 2026-06-10
- **Used by**: Paraguay
- **Facts supporting**: Paraguay VAT context for corporations and individuals/associations rendering personal services, 10% general VAT rate, 5% reduced-rate categories, and duplicate social-security context for employee/employer rates (claim-paraguay-009, claim-paraguay-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-07

## src-443
- **Title**: ExchangeRate-API open rates — USD to PYG snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-10T00:02:31Z
- **Date accessed**: 2026-06-10
- **Used by**: Paraguay
- **Facts supporting**: run-089 USD/PYG conversion for the Paraguay USD 3,000/month tax worked example: USD 1 = PYG 6,152.887361 (claim-paraguay-011)
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-10

## src-444
- **Title**: PwC Worldwide Tax Summaries — Panama, Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/panama/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-18
- **Date accessed**: 2026-06-10
- **Used by**: Panama
- **Facts supporting**: Panama territorial personal-income-tax system, resident/non-resident Panama-source income scope, and PIT brackets of 0% up to USD 11,000, 15% on USD 11,000-50,000, and 25% above USD 50,000 (claim-panama-007, claim-panama-010, claim-panama-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-18

## src-445
- **Title**: PwC Worldwide Tax Summaries — Panama, Individual: Residence
- **URL**: https://taxsummaries.pwc.com/panama/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-18
- **Date accessed**: 2026-06-10
- **Used by**: Panama
- **Facts supporting**: Panama individual residence rule: physically located and generating income in Panama for more than 183 days during the year (claim-panama-008)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-18

## src-446
- **Title**: PwC Worldwide Tax Summaries — Panama, Individual: Other taxes
- **URL**: https://taxsummaries.pwc.com/panama/individual/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-18
- **Date accessed**: 2026-06-10
- **Used by**: Panama
- **Facts supporting**: employee social-security rate of 9.75% from 1 April 2025, employee educational-insurance tax of 1.25%, employer payroll-tax context, and individual ITBMS/VAT headline rate of 7% (claim-panama-009, claim-panama-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-18

## src-447
- **Title**: PwC Worldwide Tax Summaries — Panama, Individual: Tax administration
- **URL**: https://taxsummaries.pwc.com/panama/individual/tax-administration
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-18
- **Date accessed**: 2026-06-10
- **Used by**: Panama
- **Facts supporting**: calendar-year tax period, 15 March return deadline for taxpayers other than single-employer employees with withholding, and estimated-tax instalments on 30 June, 30 September, and 31 December
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-18

## src-448
- **Title**: PwC Worldwide Tax Summaries — Panama, Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/panama/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-18
- **Date accessed**: 2026-06-10
- **Used by**: Panama
- **Facts supporting**: Panama ITBMS/VAT 7% general rate, exports-not-taxed statement, and ITBMS credit/refund context used as a VAT/export-service risk baseline pending DGI/accountant confirmation for foreign-client IT (claim-panama-009)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-18

## src-449
- **Title**: PwC Worldwide Tax Summaries — Mexico, Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/mexico/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-30
- **Date accessed**: 2026-06-10
- **Used by**: Mexico
- **Facts supporting**: Mexico resident worldwide-income scope, non-resident Mexican-source scope, 2026 resident PIT progressive brackets, and non-resident compensation brackets (claim-mexico-007, claim-mexico-008, claim-mexico-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-30

## src-450
- **Title**: PwC Worldwide Tax Summaries — Mexico, Individual: Residence
- **URL**: https://taxsummaries.pwc.com/mexico/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-30
- **Date accessed**: 2026-06-10
- **Used by**: Mexico
- **Facts supporting**: Mexican tax-residence home test and centre-of-vital-interests tie-breaker baseline (claim-mexico-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-30

## src-451
- **Title**: PwC Worldwide Tax Summaries — Mexico, Individual: Deductions
- **URL**: https://taxsummaries.pwc.com/mexico/individual/deductions
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-30
- **Date accessed**: 2026-06-10
- **Used by**: Mexico
- **Facts supporting**: no standard deduction, business/professional expense deduction baseline, and professional/business loss ring-fencing; used to keep the ordinary PIT worked example conservative pending exact regime confirmation
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-30

## src-452
- **Title**: PwC Worldwide Tax Summaries — Mexico, Individual: Other taxes
- **URL**: https://taxsummaries.pwc.com/mexico/individual/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-30
- **Date accessed**: 2026-06-10
- **Used by**: Mexico
- **Facts supporting**: employee IMSS contribution context, employer contribution context, employee maximum contribution, 16% VAT general rate, 8% northern-border-region VAT caveat, and no net wealth tax (claim-mexico-009)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-30

## src-453
- **Title**: PwC Worldwide Tax Summaries — Mexico, Individual: Tax administration
- **URL**: https://taxsummaries.pwc.com/mexico/individual/tax-administration
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-01-30
- **Date accessed**: 2026-06-10
- **Used by**: Mexico
- **Facts supporting**: calendar-year tax period, annual return due by 30 April, electronic filing / advanced electronic signature context, and no joint-return baseline for married couples (claim-mexico-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-30

## src-454
- **Title**: PwC Worldwide Tax Summaries — Mexico, Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/mexico/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-24
- **Date accessed**: 2026-06-10
- **Used by**: Mexico
- **Facts supporting**: corporate VAT context, 16% general VAT rate, VAT-exempt transaction examples, payroll/social-security context, and profit-sharing context used as risk background pending exact foreign-client IT classification (claim-mexico-009)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-24

## src-455
- **Title**: ExchangeRate-API open rates — USD to MXN snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-10T00:02:31Z
- **Date accessed**: 2026-06-10
- **Used by**: Mexico
- **Facts supporting**: run-091 USD/MXN conversion for the Mexico USD 3,000/month tax worked example: USD 1 = MXN 17.430625 (claim-mexico-011)
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-10


## src-456
- **Title**: PwC Worldwide Tax Summaries — Argentina, Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/argentina/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-04-01
- **Date accessed**: 2026-06-10
- **Used by**: Argentina
- **Facts supporting**: Argentina resident worldwide-income baseline, 2026 PIT update mechanics, self-employed PIT rates, provincial gross-income-tax ranges and CABA 2026 services / professional-exemption context, and foreign-beneficiary caveat (claim-argentina-008, claim-argentina-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-04-01

## src-457
- **Title**: PwC Worldwide Tax Summaries — Argentina, Individual: Residence
- **URL**: https://taxsummaries.pwc.com/argentina/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-04-01
- **Date accessed**: 2026-06-10
- **Used by**: Argentina
- **Facts supporting**: Argentina individual tax-residence categories, foreign individuals becoming residents after more than 12 months / from the 13th month for non-work reasons, and non-resident / foreign-beneficiary caveats (claim-argentina-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-04-01

## src-458
- **Title**: PwC Worldwide Tax Summaries — Argentina, Individual: Deductions
- **URL**: https://taxsummaries.pwc.com/argentina/individual/deductions
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-04-01
- **Date accessed**: 2026-06-10
- **Used by**: Argentina
- **Facts supporting**: self-employed pension and social-security contributions deductible from PIT, personal allowances and deduction context, and social-security sensitivity caveat (claim-argentina-009, claim-argentina-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-04-01

## src-459
- **Title**: PwC Worldwide Tax Summaries — Argentina, Individual: Other taxes
- **URL**: https://taxsummaries.pwc.com/argentina/individual/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-04-01
- **Date accessed**: 2026-06-10
- **Used by**: Argentina
- **Facts supporting**: employer and employee social-security rate context, June 2026 employee contribution cap, VAT 21% general rate, VAT on self-employed activity, monthly VAT returns, and digital-services / reverse-charge caveats (claim-argentina-009, claim-argentina-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-04-01

## src-460
- **Title**: PwC Worldwide Tax Summaries — Argentina, Individual tax administration and corporate VAT context
- **URL**: https://taxsummaries.pwc.com/argentina/individual/tax-administration and https://taxsummaries.pwc.com/argentina/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-04-01
- **Date accessed**: 2026-06-10
- **Used by**: Argentina
- **Facts supporting**: separate spouse taxation, self-employed tax registration / annual PIT return / advance-payment mechanics, calendar-year tax period, monthly VAT returns, 21% VAT on services, and foreign-beneficiary reverse-charge caveats (claim-argentina-009, claim-argentina-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-04-01

## src-461
- **Title**: ExchangeRate-API open rates — USD to ARS snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-10T00:02:31Z
- **Date accessed**: 2026-06-10
- **Used by**: Argentina
- **Facts supporting**: run-092 USD/ARS conversion for the Argentina USD 3,000/month tax worked example: USD 1 = ARS 1,446.1668 (claim-argentina-011)
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-10

## src-462
- **Title**: PwC Worldwide Tax Summaries — United Arab Emirates Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/united-arab-emirates/individual/taxes-on-personal-income
- **Archive**: [archive: failed 2026-06-11]
- **Type**: reputable-secondary
- **Date published**: 2026-03-12
- **Date accessed**: 2026-06-11
- **Used by**: UAE
- **Facts supporting**: no UAE PIT / no individual registration or reporting obligations; natural-person corporate-tax turnover trigger above AED 1,000,000 (claim-uae-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-12

## src-463
- **Title**: PwC Worldwide Tax Summaries — United Arab Emirates Individual: Residence
- **URL**: https://taxsummaries.pwc.com/united-arab-emirates/individual/residence
- **Archive**: [archive: failed 2026-06-11]
- **Type**: reputable-secondary
- **Date published**: 2026-03-12
- **Date accessed**: 2026-06-11
- **Used by**: UAE
- **Facts supporting**: UAE individual tax-residence tests: centre of interests, 183-day test, and 90-day residence-permit / permanent-home / employment-business test (claim-uae-008)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-12

## src-464
- **Title**: PwC Worldwide Tax Summaries — United Arab Emirates Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/united-arab-emirates/corporate/other-taxes
- **Archive**: [archive: failed 2026-06-11]
- **Type**: reputable-secondary
- **Date published**: 2026-03-12
- **Date accessed**: 2026-06-11
- **Used by**: UAE
- **Facts supporting**: 5% VAT baseline, export-services zero-rating subject to conditions, AED 375,000 mandatory VAT-registration threshold, AED 187,500 voluntary threshold, and non-GCC nationals outside UAE social security (claim-uae-009)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-12


## src-465
- **Title**: PwC Worldwide Tax Summaries — Malaysia Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/malaysia/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-19
- **Date accessed**: 2026-06-11
- **Used by**: Malaysia
- **Facts supporting**: Malaysian-source / foreign-sourced income baseline, 2026 resident PIT rate table, non-resident 30% rate, no local personal income taxes, and USD 3,000/month PIT stress test (claim-malaysia-008, claim-malaysia-009, claim-malaysia-012)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-19

## src-466
- **Title**: PwC Worldwide Tax Summaries — Malaysia Individual: Residence
- **URL**: https://taxsummaries.pwc.com/malaysia/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-19
- **Date accessed**: 2026-06-11
- **Used by**: Malaysia
- **Facts supporting**: Malaysia individual tax residence threshold of 182+ days in a calendar year and resident/non-resident consequence for reliefs and graduated rates (claim-malaysia-008)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-19

## src-467
- **Title**: PwC Worldwide Tax Summaries — Malaysia Individual: Income determination
- **URL**: https://taxsummaries.pwc.com/malaysia/individual/income-determination
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-19
- **Date accessed**: 2026-06-11
- **Used by**: Malaysia
- **Facts supporting**: employment income taxed when work is performed in Malaysia regardless of payment location; foreign-sourced income received in Malaysia may be taxable with listed exemptions subject to conditions (claim-malaysia-008)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-19

## src-468
- **Title**: PwC Worldwide Tax Summaries — Malaysia Individual: Deductions
- **URL**: https://taxsummaries.pwc.com/malaysia/individual/deductions
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-19
- **Date accessed**: 2026-06-11
- **Used by**: Malaysia
- **Facts supporting**: YA 2026 personal reliefs including MYR 9,000 self relief and MYR 4,000 spouse relief under joint assessment; calculation inputs for the resident PIT worked example (claim-malaysia-011, claim-malaysia-012)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-19

## src-469
- **Title**: PwC Worldwide Tax Summaries — Malaysia Individual: Other taxes and tax administration
- **URL**: https://taxsummaries.pwc.com/malaysia/individual/other-taxes and https://taxsummaries.pwc.com/malaysia/individual/tax-administration
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2025-12-19
- **Date accessed**: 2026-06-11
- **Used by**: Malaysia
- **Facts supporting**: non-Malaysian employee EPF rates, SOCSO case-by-case warning for foreign workers, SST/service-tax context, calendar-year tax period, self-assessment, filing deadlines, e-filing, and separate/joint spouse assessment mechanics (claim-malaysia-010, claim-malaysia-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-19

## src-470
- **Title**: ExchangeRate-API open rates — USD to MYR snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-11T00:02:31Z
- **Date accessed**: 2026-06-11
- **Used by**: Malaysia
- **Facts supporting**: run-095 USD/MYR conversion for the Malaysia USD 3,000/month tax worked example: USD 1 = MYR 4.06831 (claim-malaysia-012)
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-11

## src-471
- **Title**: PwC Worldwide Tax Summaries — Thailand Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/thailand/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-02
- **Date accessed**: 2026-06-11
- **Used by**: Thailand
- **Facts supporting**: Thailand PIT scope for resident/non-resident Thai-source employment or business income, post-2024 foreign-source remittance rule for residents, progressive PIT brackets, and USD 3,000/month PIT worked example (claim-thailand-007, claim-thailand-008, claim-thailand-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-02

## src-472
- **Title**: PwC Worldwide Tax Summaries — Thailand Individual: Residence
- **URL**: https://taxsummaries.pwc.com/thailand/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-02
- **Date accessed**: 2026-06-11
- **Used by**: Thailand
- **Facts supporting**: Thailand individual tax-residence threshold of 180+ aggregate days in a calendar tax year (claim-thailand-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-02

## src-473
- **Title**: PwC Worldwide Tax Summaries — Thailand Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/thailand/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-02
- **Date accessed**: 2026-06-11
- **Used by**: Thailand
- **Facts supporting**: VAT on goods/services, export zero-rating context, electronic-services registration threshold, employee social-security contribution rate and cap, and unresolved DTV freelancer VAT/social-security fit (claim-thailand-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-02

## src-474
- **Title**: PwC Worldwide Tax Summaries — Thailand Individual: Deductions
- **URL**: https://taxsummaries.pwc.com/thailand/individual/deductions
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-02
- **Date accessed**: 2026-06-11
- **Used by**: Thailand
- **Facts supporting**: THB 60,000 personal allowance, spouse allowance if spouse does not file one's own return, and deduction inputs for the Thailand USD 3,000/month worked example (claim-thailand-009, claim-thailand-011)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-02

## src-475
- **Title**: PwC Worldwide Tax Summaries — Thailand Individual: Tax administration
- **URL**: https://taxsummaries.pwc.com/thailand/individual/tax-administration
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-02
- **Date accessed**: 2026-06-11
- **Used by**: Thailand
- **Facts supporting**: calendar-year tax period, annual paper/online filing deadlines, six-month business return, payment timing, and separate/joint spouse filing option (claim-thailand-009)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-02

## src-476
- **Title**: ExchangeRate-API open rates — USD to THB snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-11T00:02:31Z
- **Date accessed**: 2026-06-11
- **Used by**: Thailand
- **Facts supporting**: run-096 USD/THB conversion for the Thailand USD 3,000/month tax worked example: USD 1 = THB 32.936578 (claim-thailand-011)
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-11


## src-477
- **Title**: PwC Worldwide Tax Summaries — Indonesia Individual: Taxes on personal income
- **URL**: https://taxsummaries.pwc.com/indonesia/individual/taxes-on-personal-income
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-06-11
- **Date accessed**: 2026-06-11
- **Used by**: Indonesia
- **Facts supporting**: Indonesian resident worldwide-income baseline, skilled-foreigner territorial concession caveat, non-resident 20% WHT baseline, 2026 PIT brackets, and USD 3,000/month PIT worked example (claim-indonesia-006, claim-indonesia-007, claim-indonesia-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-11

## src-478
- **Title**: PwC Worldwide Tax Summaries — Indonesia Individual: Residence
- **URL**: https://taxsummaries.pwc.com/indonesia/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-06-11
- **Date accessed**: 2026-06-11
- **Used by**: Indonesia
- **Facts supporting**: Indonesian individual tax-residence tests: residence, more than 183 days in any 12-month period, or presence plus intention to reside (claim-indonesia-006)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-11

## src-479
- **Title**: PwC Worldwide Tax Summaries — Indonesia Individual: Deductions / Tax administration / Other tax credits and incentives
- **URL**: https://taxsummaries.pwc.com/indonesia/individual/deductions ; https://taxsummaries.pwc.com/indonesia/individual/tax-administration ; https://taxsummaries.pwc.com/indonesia/individual/other-tax-credits-and-incentives
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-06-11
- **Date accessed**: 2026-06-11
- **Used by**: Indonesia
- **Facts supporting**: IDR 54m personal relief, IDR 4.5m spouse/dependant reliefs, calendar-year tax period, annual and monthly filing/payment deadlines, absence of other significant individual tax incentives, and worked-example inputs (claim-indonesia-008, claim-indonesia-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-11

## src-480
- **Title**: PwC Worldwide Tax Summaries — Indonesia Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/indonesia/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-06-11
- **Date accessed**: 2026-06-11
- **Used by**: Indonesia
- **Facts supporting**: effective 11% VAT / 12% luxury VAT context, exported-service zero-rating limits including IT services, BPJS and housing-savings context for employees / independent workers / expatriates, and unresolved E33G freelancer fit (claim-indonesia-009)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-11

## src-481
- **Title**: ExchangeRate-API open rates — USD to IDR snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-11T00:02:31Z
- **Date accessed**: 2026-06-11
- **Used by**: Indonesia
- **Facts supporting**: run-097 USD/IDR conversion for the Indonesia USD 3,000/month tax worked example: USD 1 = IDR 17,916.976082 (claim-indonesia-010)
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-11


## src-482
- **Title**: PwC Worldwide Tax Summaries — Kazakhstan Individual: Taxes on personal income / Residence
- **URL**: https://taxsummaries.pwc.com/kazakhstan/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/kazakhstan/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-02
- **Date accessed**: 2026-06-11
- **Used by**: Kazakhstan
- **Facts supporting**: Kazakhstan resident worldwide-income scope, 183-day / centre-of-vital-interest tax-residence test, and 2026 PIT bands of 10% up to 8,500 MCI and 15% above (claim-kazakhstan-006, claim-kazakhstan-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-11

## src-483
- **Title**: PwC Worldwide Tax Summaries — Kazakhstan Individual: Deductions / Income determination / Tax administration / Other tax credits and incentives
- **URL**: https://taxsummaries.pwc.com/kazakhstan/individual/deductions ; https://taxsummaries.pwc.com/kazakhstan/individual/income-determination ; https://taxsummaries.pwc.com/kazakhstan/individual/tax-administration ; https://taxsummaries.pwc.com/kazakhstan/individual/other-tax-credits-and-incentives
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-02
- **Date accessed**: 2026-06-11
- **Used by**: Kazakhstan
- **Facts supporting**: 30 MCI/month basic deduction, business deductions only for registered entrepreneurs, individual-entrepreneur income determination, annual filing/payment deadlines, and no captured significant individual incentives (claim-kazakhstan-008, claim-kazakhstan-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-11

## src-484
- **Title**: PwC Worldwide Tax Summaries — Kazakhstan Individual: Other taxes; Corporate: Other taxes
- **URL**: https://taxsummaries.pwc.com/kazakhstan/individual/other-taxes ; https://taxsummaries.pwc.com/kazakhstan/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-02 / 2026-04-03
- **Date accessed**: 2026-06-11
- **Used by**: Kazakhstan
- **Facts supporting**: employee/employer social, medical, and pension contribution context; 2026 VAT rate of 16%; 10,000 MCI VAT threshold; quarterly VAT reporting; 1 MCI = KZT 4,325 for 2026 (claim-kazakhstan-009, claim-kazakhstan-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-11

## src-485
- **Title**: eGov Kazakhstan — Notification on start-up of individual entrepreneur business
- **URL**: https://egov.kz/cms/en/services/reg_ip
- **Archive**: [stable gov portal; direct HTML extraction used]
- **Type**: official-primary
- **Date published**: no page date captured
- **Date accessed**: 2026-06-11
- **Used by**: Kazakhstan
- **Facts supporting**: official online entry point for individual-entrepreneur start-up notification through E-Licensing, free of charge, with EDS signature and personal-account tracking
- **Confidence ceiling**: high
- **Stale at**: 2026-12-11

## src-486
- **Title**: ExchangeRate-API open rates — USD to KZT snapshot
- **URL**: https://open.er-api.com/v6/latest/USD
- **Archive**: [archive: not captured; API snapshot]
- **Type**: commercial
- **Date published**: 2026-06-11T00:02:31Z
- **Date accessed**: 2026-06-11
- **Used by**: Kazakhstan
- **Facts supporting**: run-098 USD/KZT conversion for the Kazakhstan USD 3,000/month tax worked example: USD 1 = KZT 488.182834 (claim-kazakhstan-010)
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-11

## src-487
- **Title**: PwC Worldwide Tax Summaries — Armenia Individual: Taxes on personal income / Residence
- **URL**: https://taxsummaries.pwc.com/armenia/individual/taxes-on-personal-income ; https://taxsummaries.pwc.com/armenia/individual/residence
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-05
- **Date accessed**: 2026-06-11
- **Used by**: Armenia
- **Facts supporting**: Armenian resident worldwide-income baseline, non-resident Armenian-source baseline, 183-day / centre-of-vital-interest tax-residence tests, and conservative 20% income-tax stress-test context (claim-armenia-006, claim-armenia-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-05

## src-488
- **Title**: PwC Worldwide Tax Summaries — Armenia Individual: Income determination
- **URL**: https://taxsummaries.pwc.com/armenia/individual/income-determination
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-05
- **Date accessed**: 2026-06-11
- **Used by**: Armenia
- **Facts supporting**: Armenian resident income scope including income received or credited in Armenia or abroad and business-activity income category (claim-armenia-007)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-05

## src-489
- **Title**: PwC Worldwide Tax Summaries — Armenia Individual: Other taxes / Tax administration / Deductions / Incentives
- **URL**: https://taxsummaries.pwc.com/armenia/individual/other-taxes ; https://taxsummaries.pwc.com/armenia/individual/tax-administration ; https://taxsummaries.pwc.com/armenia/individual/deductions ; https://taxsummaries.pwc.com/armenia/individual/other-tax-credits-and-incentives
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-05
- **Date accessed**: 2026-06-11
- **Used by**: Armenia
- **Facts supporting**: entrepreneur funded-pension formulas, mandatory health-insurance contribution, 20% VAT headline on individual page, personal tax declaration timing, no significant individual incentives, and worked-example contribution inputs (claim-armenia-008, claim-armenia-010)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-05

## src-490
- **Title**: PwC Worldwide Tax Summaries — Armenia Corporate: Other taxes / VAT and turnover tax
- **URL**: https://taxsummaries.pwc.com/armenia/corporate/other-taxes
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: reviewed 2026-02-05
- **Date accessed**: 2026-06-11
- **Used by**: Armenia
- **Facts supporting**: 20% VAT, export-services zero-rating context, reverse-charge VAT context, AMD 115m SME turnover-tax threshold, 1% rate for government-listed high-tech activities, and quarterly turnover-tax filing timing (claim-armenia-009)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-05

## src-491
- **Title**: e-register Armenia digital-services portal / ExchangeRate-API USD to AMD snapshot
- **URL**: https://www.e-register.am/en/ ; https://open.er-api.com/v6/latest/USD
- **Archive**: [stable government portal / API snapshot; direct extraction used]
- **Type**: official-primary / commercial
- **Date published**: e-register page no date captured; FX time_last_update_utc 2026-06-11T00:02:31Z
- **Date accessed**: 2026-06-11
- **Used by**: Armenia
- **Facts supporting**: official digital-services portal entry point for sole-proprietor and LLC registration categories, plus run-099 USD/AMD conversion for the Armenia USD 3,000/month tax worked example: USD 1 = AMD 368.343288 (claim-armenia-010)
- **Confidence ceiling**: medium
- **Stale at**: 2026-07-11


## src-492
- **Title**: ePortugal — Obtain a National Health Service (SNS) user number
- **URL**: https://eportugal.gov.pt/en/servicos/pedir-o-numero-de-utente-do-sns
- **Archive**: [not captured]
- **Type**: official-primary
- **Date published**: [no date, verification required]
- **Date accessed**: 2026-06-12
- **Used by**: Portugal
- **Facts supporting**: SNS user number allocation for non-nationals and access to SNS public facilities (claim-portugal-011)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-12

## src-493
- **Title**: ePortugal — Register at the health centre
- **URL**: https://eportugal.gov.pt/en/servicos/inscrever-se-no-centro-de-saude
- **Archive**: [not captured]
- **Type**: official-primary
- **Date published**: [no date, verification required]
- **Date accessed**: 2026-06-12
- **Used by**: Portugal
- **Facts supporting**: free health-centre registration with SNS user number; user number can be obtained while registering (claim-portugal-012)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-12

## src-494
- **Title**: ePortugal — Book a consultation at the health centre
- **URL**: https://eportugal.gov.pt/en/servicos/marcar-uma-consulta-no-centro-de-saude
- **Archive**: [not captured]
- **Type**: official-primary
- **Date published**: [no date, verification required]
- **Date accessed**: 2026-06-12
- **Used by**: Portugal
- **Facts supporting**: registered users can book general/family-medicine and nursing appointments online, by phone, or in person; booking is free
- **Confidence ceiling**: high
- **Stale at**: 2027-06-12

## src-495
- **Title**: Expatica — The healthcare system in Portugal
- **URL**: https://www.expatica.com/pt/healthcare/healthcare-basics/healthcare-in-portugal-106770/
- **Archive**: [not captured]
- **Type**: reputable-secondary
- **Date published**: 2026-04-28
- **Date accessed**: 2026-06-12
- **Used by**: Portugal
- **Facts supporting**: SNS resident coverage baseline; public/private care split; most care free since 2022 with emergency-use exceptions; private doctor EUR 40-50 baseline (claim-portugal-013); private-insurance provider examples; maternity baseline (claim-portugal-014)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-12

## src-496
- **Title**: Portugalist — Portugal's Healthcare System: What Expats Need to Know About Public and Private
- **URL**: https://www.portugalist.com/healthcare-portugal/
- **Archive**: [not captured]
- **Type**: reputable-secondary
- **Date published**: [no date, verification required]
- **Date accessed**: 2026-06-12
- **Used by**: Portugal
- **Facts supporting**: resident access to the public system; public-system safety-net role; waiting-list and family-doctor-shortage caveats; English-language availability caveats
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-12

## src-497
- **Title**: Livingcost — Cost of living in the Czech Republic
- **URL**: https://livingcost.org/cost/czech-republic
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Czech Republic
- **Facts supporting**: Czech Republic national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-498
- **Title**: Livingcost — Cost of living in Prague
- **URL**: https://livingcost.org/cost/czech-republic/prague
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Czech Republic
- **Facts supporting**: Prague cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-499
- **Title**: Livingcost — Cost of living in Brno
- **URL**: https://livingcost.org/cost/czech-republic/brno
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Czech Republic
- **Facts supporting**: Brno cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-500
- **Title**: Livingcost — Cost of living in Ostrava
- **URL**: https://livingcost.org/cost/czech-republic/ostrava
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Czech Republic
- **Facts supporting**: Ostrava cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-501
- **Title**: Livingcost — Cost of living in Poland
- **URL**: https://livingcost.org/cost/poland
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Poland
- **Facts supporting**: Poland national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-502
- **Title**: Livingcost — Cost of living in Warsaw
- **URL**: https://livingcost.org/cost/poland/warsaw
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Poland
- **Facts supporting**: Warsaw cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-503
- **Title**: Livingcost — Cost of living in Krakow
- **URL**: https://livingcost.org/cost/poland/krakow
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Poland
- **Facts supporting**: Krakow cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-504
- **Title**: Livingcost — Cost of living in Wroclaw
- **URL**: https://livingcost.org/cost/poland/wroclaw
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Poland
- **Facts supporting**: Wroclaw cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-505
- **Title**: Livingcost — Cost of living in Romania
- **URL**: https://livingcost.org/cost/romania
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Romania
- **Facts supporting**: Romania national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-506
- **Title**: Livingcost — Cost of living in Bucharest
- **URL**: https://livingcost.org/cost/romania/bucharest
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Romania
- **Facts supporting**: Bucharest cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-507
- **Title**: Livingcost — Cost of living in Cluj-Napoca
- **URL**: https://livingcost.org/cost/romania/cluj-napoca
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Romania
- **Facts supporting**: Cluj-Napoca cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-508
- **Title**: Livingcost — Cost of living in Timisoara
- **URL**: https://livingcost.org/cost/romania/timisoara
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Romania
- **Facts supporting**: Timisoara cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-509
- **Title**: Livingcost — Cost of living in Bulgaria
- **URL**: https://livingcost.org/cost/bulgaria
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Bulgaria
- **Facts supporting**: Bulgaria national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-510
- **Title**: Livingcost — Cost of living in Sofia
- **URL**: https://livingcost.org/cost/bulgaria/sofia
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Bulgaria
- **Facts supporting**: Sofia cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-511
- **Title**: Livingcost — Cost of living in Plovdiv
- **URL**: https://livingcost.org/cost/bulgaria/plovdiv
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Bulgaria
- **Facts supporting**: Plovdiv cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-512
- **Title**: Livingcost — Cost of living in Varna
- **URL**: https://livingcost.org/cost/bulgaria/varna
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Bulgaria
- **Facts supporting**: Varna cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-513
- **Title**: Livingcost — Cost of living in Hungary
- **URL**: https://livingcost.org/cost/hungary
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Hungary
- **Facts supporting**: Hungary national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-514
- **Title**: Livingcost — Cost of living in Budapest
- **URL**: https://livingcost.org/cost/hungary/budapest
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Hungary
- **Facts supporting**: Budapest cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-515
- **Title**: Livingcost — Cost of living in Debrecen
- **URL**: https://livingcost.org/cost/hungary/debrecen
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Hungary
- **Facts supporting**: Debrecen cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-516
- **Title**: Livingcost — Cost of living in Pécs
- **URL**: https://livingcost.org/cost/hungary/pecs
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Hungary
- **Facts supporting**: Pécs cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-517
- **Title**: Livingcost — Cost of living in Slovakia
- **URL**: https://livingcost.org/cost/slovakia
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Slovakia
- **Facts supporting**: Slovakia national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-518
- **Title**: Livingcost — Cost of living in Bratislava
- **URL**: https://livingcost.org/cost/slovakia/bratislava
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Slovakia
- **Facts supporting**: Bratislava cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-519
- **Title**: Livingcost — Cost of living in Kosice
- **URL**: https://livingcost.org/cost/slovakia/kosice
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Slovakia
- **Facts supporting**: Kosice cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-520
- **Title**: Livingcost — Cost of living in Poprad
- **URL**: https://livingcost.org/cost/slovakia/poprad
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Slovakia
- **Facts supporting**: Poprad cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-521
- **Title**: Livingcost — Cost of living in Slovenia
- **URL**: https://livingcost.org/cost/slovenia
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Slovenia
- **Facts supporting**: Slovenia national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-522
- **Title**: Livingcost — Cost of living in Ljubljana
- **URL**: https://livingcost.org/cost/slovenia/ljubljana
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Slovenia
- **Facts supporting**: Ljubljana cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-523
- **Title**: Livingcost — Cost of living in Maribor
- **URL**: https://livingcost.org/cost/slovenia/maribor
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Slovenia
- **Facts supporting**: Maribor cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12

## src-524
- **Title**: Livingcost — Cost of living in Nova Gorica
- **URL**: https://livingcost.org/cost/slovenia/nova-gorica
- **Archive**: [archive: failed 2026-06-12; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-12
- **Used by**: Slovenia
- **Facts supporting**: Nova Gorica cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-12


## src-525
- **Title**: Livingcost — Cost of living in Montenegro
- **URL**: https://livingcost.org/cost/montenegro
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Montenegro
- **Facts supporting**: Montenegro national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-526
- **Title**: Livingcost — Cost of living in Podgorica
- **URL**: https://livingcost.org/cost/montenegro/podgorica
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Montenegro
- **Facts supporting**: Podgorica cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-527
- **Title**: Livingcost — Cost of living in Budva
- **URL**: https://livingcost.org/cost/montenegro/budva
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Montenegro
- **Facts supporting**: Budva cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-528
- **Title**: Livingcost — Cost of living in Kotor
- **URL**: https://livingcost.org/cost/montenegro/kotor
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Montenegro
- **Facts supporting**: Kotor cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-529
- **Title**: Livingcost — Cost of living in Serbia
- **URL**: https://livingcost.org/cost/serbia
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Serbia
- **Facts supporting**: Serbia national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-530
- **Title**: Livingcost — Cost of living in Belgrade
- **URL**: https://livingcost.org/cost/serbia/belgrade
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Serbia
- **Facts supporting**: Belgrade cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-531
- **Title**: Livingcost — Cost of living in Novi Sad
- **URL**: https://livingcost.org/cost/serbia/novi-sad
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Serbia
- **Facts supporting**: Novi Sad cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-532
- **Title**: Livingcost — Cost of living in Niš
- **URL**: https://livingcost.org/cost/serbia/nis
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Serbia
- **Facts supporting**: Niš cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-533
- **Title**: Livingcost — Cost of living in Turkey
- **URL**: https://livingcost.org/cost/turkey
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Turkey
- **Facts supporting**: Turkey national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-534
- **Title**: Livingcost — Cost of living in Istanbul
- **URL**: https://livingcost.org/cost/turkey/istanbul
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Turkey
- **Facts supporting**: Istanbul cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-535
- **Title**: Livingcost — Cost of living in Izmir
- **URL**: https://livingcost.org/cost/turkey/izmir
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Turkey
- **Facts supporting**: Izmir cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-536
- **Title**: Livingcost — Cost of living in Antalya
- **URL**: https://livingcost.org/cost/turkey/antalya
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Turkey
- **Facts supporting**: Antalya cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-537
- **Title**: Livingcost — Cost of living in Georgia
- **URL**: https://livingcost.org/cost/georgia
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Georgia
- **Facts supporting**: Georgia national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-538
- **Title**: Livingcost — Cost of living in Tbilisi
- **URL**: https://livingcost.org/cost/georgia/tbilisi
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Georgia
- **Facts supporting**: Tbilisi cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-539
- **Title**: Livingcost — Cost of living in Batumi
- **URL**: https://livingcost.org/cost/georgia/batumi
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Georgia
- **Facts supporting**: Batumi cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-540
- **Title**: Livingcost — Cost of living in Kutaisi
- **URL**: https://livingcost.org/cost/georgia/kutaisi
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Georgia
- **Facts supporting**: Kutaisi cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-541
- **Title**: Livingcost — Cost of living in Albania
- **URL**: https://livingcost.org/cost/albania
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Albania
- **Facts supporting**: Albania national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-542
- **Title**: Livingcost — Cost of living in Tirana
- **URL**: https://livingcost.org/cost/albania/tirana
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Albania
- **Facts supporting**: Tirana cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-543
- **Title**: Livingcost — Cost of living in Durrës
- **URL**: https://livingcost.org/cost/albania/durres
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Albania
- **Facts supporting**: Durrës cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-544
- **Title**: Livingcost — Cost of living in Vlorë
- **URL**: https://livingcost.org/cost/albania/vlore
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Albania
- **Facts supporting**: Vlorë cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13


## src-545
- **Title**: Livingcost — Cost of living in Uruguay
- **URL**: https://livingcost.org/cost/uruguay
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Uruguay
- **Facts supporting**: Uruguay national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-546
- **Title**: Livingcost — Cost of living in Montevideo
- **URL**: https://livingcost.org/cost/uruguay/montevideo
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Uruguay
- **Facts supporting**: Montevideo cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-547
- **Title**: Livingcost — Cost of living in Punta del Este
- **URL**: https://livingcost.org/cost/uruguay/punta-del-este
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Uruguay
- **Facts supporting**: Punta del Este cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-548
- **Title**: Livingcost — Cost of living in Salto, Uruguay
- **URL**: https://livingcost.org/cost/uruguay/salto
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Uruguay
- **Facts supporting**: Salto cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-549
- **Title**: Livingcost — Cost of living in Paraguay
- **URL**: https://livingcost.org/cost/paraguay
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Paraguay
- **Facts supporting**: Paraguay national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-550
- **Title**: Livingcost — Cost of living in Asuncion
- **URL**: https://livingcost.org/cost/paraguay/asuncion
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Paraguay
- **Facts supporting**: Asuncion cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-551
- **Title**: Livingcost — Cost of living in Ciudad del Este
- **URL**: https://livingcost.org/cost/paraguay/ciudad-del-este
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Paraguay
- **Facts supporting**: Ciudad del Este cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-552
- **Title**: Livingcost — Cost of living in Encarnacion
- **URL**: https://livingcost.org/cost/paraguay/encarnacion
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Paraguay
- **Facts supporting**: Encarnacion cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13


## src-553
- **Title**: Livingcost — Cost of living in Panama
- **URL**: https://livingcost.org/cost/panama
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Panama
- **Facts supporting**: Panama national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-554
- **Title**: Livingcost — Cost of living in Panama City
- **URL**: https://livingcost.org/cost/panama/panama
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Panama
- **Facts supporting**: Panama City cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-555
- **Title**: Livingcost — Cost of living in David, Panama
- **URL**: https://livingcost.org/cost/panama/david
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Panama
- **Facts supporting**: David cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-556
- **Title**: Livingcost — Cost of living in Santiago de Veraguas
- **URL**: https://livingcost.org/cost/panama/santiago-de-veraguas
- **Archive**: [archive: failed 2026-06-13; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-13
- **Used by**: Panama
- **Facts supporting**: Santiago de Veraguas cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-13

## src-557
- **Title**: Livingcost — Cost of living in North Macedonia
- **URL**: https://livingcost.org/cost/north-macedonia
- **Archive**: [archive: failed 2026-06-14; Wayback returned HTTP 429; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: North Macedonia
- **Facts supporting**: North Macedonia national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-558
- **Title**: Livingcost — Cost of living in Skopje
- **URL**: https://livingcost.org/cost/north-macedonia/skopje
- **Archive**: [archive: failed 2026-06-14; Wayback returned HTTP 429; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: North Macedonia
- **Facts supporting**: Skopje cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-559
- **Title**: Livingcost — Cost of living in Ohrid
- **URL**: https://livingcost.org/cost/north-macedonia/ohrid
- **Archive**: [archive: failed 2026-06-14; Wayback returned HTTP 429; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: North Macedonia
- **Facts supporting**: Ohrid cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-560
- **Title**: Livingcost — Cost of living in Bitola
- **URL**: https://livingcost.org/cost/north-macedonia/bitola
- **Archive**: [archive: failed 2026-06-14; Wayback returned HTTP 429; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: North Macedonia
- **Facts supporting**: Bitola cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-561
- **Title**: Livingcost — Cost of living in Bosnia and Herzegovina
- **URL**: https://livingcost.org/cost/bosnia-and-herzegovina
- **Archive**: [archive: failed 2026-06-14; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Bosnia and Herzegovina national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-562
- **Title**: Livingcost — Cost of living in Sarajevo
- **URL**: https://livingcost.org/cost/bosnia-and-herzegovina/sarajevo
- **Archive**: [archive: failed 2026-06-14; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Sarajevo cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-563
- **Title**: Livingcost — Cost of living in Mostar
- **URL**: https://livingcost.org/cost/bosnia-and-herzegovina/mostar
- **Archive**: [archive: failed 2026-06-14; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Mostar cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-564
- **Title**: Livingcost — Cost of living in Banja Luka
- **URL**: https://livingcost.org/cost/bosnia-and-herzegovina/banja-luka
- **Archive**: [archive: failed 2026-06-14; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Banja Luka cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-565
- **Title**: Livingcost — Cost of living in Tuzla
- **URL**: https://livingcost.org/cost/bosnia-and-herzegovina/tuzla
- **Archive**: [archive: failed 2026-06-14; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Tuzla cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14


## src-566
- **Title**: Livingcost — Cost of living in Moldova
- **URL**: https://livingcost.org/cost/moldova
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-14
- **Used by**: Moldova
- **Facts supporting**: Moldova national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-567
- **Title**: Livingcost — Cost of living in Chisinau
- **URL**: https://livingcost.org/cost/moldova/chisinau
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-14
- **Used by**: Moldova
- **Facts supporting**: Chisinau cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-568
- **Title**: Livingcost — Cost of living in Balti
- **URL**: https://livingcost.org/cost/moldova/balti
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-14
- **Used by**: Moldova
- **Facts supporting**: Balti cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-569
- **Title**: Livingcost — Cost of living in Tiraspol
- **URL**: https://livingcost.org/cost/moldova/tiraspol
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-14
- **Used by**: Moldova
- **Facts supporting**: Tiraspol cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as a non-default city because of Transnistria practical risk
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-570
- **Title**: Livingcost - Cost of living in Mexico
- **URL**: https://livingcost.org/cost/mexico
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Mexico
- **Facts supporting**: Mexico national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-571
- **Title**: Livingcost - Cost of living in Mexico City
- **URL**: https://livingcost.org/cost/mexico/mexico
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Mexico
- **Facts supporting**: Mexico City cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-572
- **Title**: Livingcost - Cost of living in Guadalajara
- **URL**: https://livingcost.org/cost/mexico/guadalajara
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Mexico
- **Facts supporting**: Guadalajara cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-573
- **Title**: Livingcost - Cost of living in Cancun
- **URL**: https://livingcost.org/cost/mexico/cancun
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Mexico
- **Facts supporting**: Cancun cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-574
- **Title**: Livingcost - Cost of living in Merida, Mexico
- **URL**: https://livingcost.org/cost/mexico/merida
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Mexico
- **Facts supporting**: Merida cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-575
- **Title**: Livingcost - Cost of living in Argentina
- **URL**: https://livingcost.org/cost/argentina
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Argentina
- **Facts supporting**: Argentina national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-576
- **Title**: Livingcost - Cost of living in Buenos Aires
- **URL**: https://livingcost.org/cost/argentina/buenos-aires
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Argentina
- **Facts supporting**: Buenos Aires cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-577
- **Title**: Livingcost - Cost of living in Cordoba, Argentina
- **URL**: https://livingcost.org/cost/argentina/cordoba
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Argentina
- **Facts supporting**: Cordoba cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-578
- **Title**: Livingcost - Cost of living in Mendoza
- **URL**: https://livingcost.org/cost/argentina/mendoza
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Argentina
- **Facts supporting**: Mendoza cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-579
- **Title**: Livingcost - Cost of living in Rosario
- **URL**: https://livingcost.org/cost/argentina/rosario
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Argentina
- **Facts supporting**: Rosario cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as a cheap fallback pending safety and service-depth checks
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-580
- **Title**: Livingcost - Cost of living in Malaysia
- **URL**: https://livingcost.org/cost/malaysia
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Malaysia
- **Facts supporting**: Malaysia national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, salary context, utilities, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-581
- **Title**: Livingcost - Cost of living in Kuala Lumpur
- **URL**: https://livingcost.org/cost/malaysia/kuala-lumpur
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Malaysia
- **Facts supporting**: Kuala Lumpur cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-582
- **Title**: Livingcost - Cost of living in George Town, Malaysia
- **URL**: https://livingcost.org/cost/malaysia/george-town
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Malaysia
- **Facts supporting**: George Town / Penang cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as the first captured warm/coastal compromise
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-583
- **Title**: Livingcost - Cost of living in Johor Bahru
- **URL**: https://livingcost.org/cost/malaysia/johor-bahru
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Malaysia
- **Facts supporting**: Johor Bahru cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-584
- **Title**: Livingcost - Cost of living in Ipoh
- **URL**: https://livingcost.org/cost/malaysia/ipoh
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Malaysia
- **Facts supporting**: Ipoh cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as an affordability fallback pending healthcare, connectivity, service-depth, and remote-worker community checks
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-585
- **Title**: Livingcost - Cost of living in Thailand
- **URL**: https://livingcost.org/cost/thailand
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Thailand
- **Facts supporting**: Thailand national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, salary context, utilities, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-586
- **Title**: Livingcost - Cost of living in Bangkok
- **URL**: https://livingcost.org/cost/thailand/bangkok
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Thailand
- **Facts supporting**: Bangkok cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as services-rich but margin-tight on one income
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-587
- **Title**: Livingcost - Cost of living in Chiang Mai
- **URL**: https://livingcost.org/cost/thailand/chiang-mai
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Thailand
- **Facts supporting**: Chiang Mai cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as the first budget screen pending smoke-season and service-depth checks
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-588
- **Title**: Livingcost - Cost of living in Phuket
- **URL**: https://livingcost.org/cost/thailand/phuket
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Thailand
- **Facts supporting**: Phuket cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as coastal/tourist-market lifestyle exception rather than default base
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14

## src-589
- **Title**: Livingcost - Cost of living in Pattaya
- **URL**: https://livingcost.org/cost/thailand/pattaya
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-14
- **Used by**: Thailand
- **Facts supporting**: Pattaya cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as a budget/coastal compromise pending quality-of-life and family-fit checks
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-14
## src-590
- **Title**: Livingcost - Cost of living in Indonesia
- **URL**: https://livingcost.org/cost/indonesia
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Indonesia
- **Facts supporting**: Indonesia national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, salary context, utilities, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-591
- **Title**: Livingcost - Cost of living in Jakarta
- **URL**: https://livingcost.org/cost/indonesia/jakarta
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Indonesia
- **Facts supporting**: Jakarta cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-592
- **Title**: Livingcost - Cost of living in Surabaya
- **URL**: https://livingcost.org/cost/indonesia/surabaya
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Indonesia
- **Facts supporting**: Surabaya cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-593
- **Title**: Livingcost - Cost of living in Bandung
- **URL**: https://livingcost.org/cost/indonesia/bandung
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Indonesia
- **Facts supporting**: Bandung cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-594
- **Title**: Livingcost - Cost of living in Denpasar
- **URL**: https://livingcost.org/cost/indonesia/denpasar
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Indonesia
- **Facts supporting**: Denpasar cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as the Bali warm/coastal proxy pending live listing and tourist-season lease checks
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-595
- **Title**: Livingcost - Cost of living in Kazakhstan
- **URL**: https://livingcost.org/cost/kazakhstan
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Kazakhstan
- **Facts supporting**: Kazakhstan national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, salary context, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-596
- **Title**: Livingcost - Cost of living in Almaty
- **URL**: https://livingcost.org/cost/kazakhstan/almaty
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Kazakhstan
- **Facts supporting**: Almaty cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as services-rich but rent-sensitive
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-597
- **Title**: Livingcost - Cost of living in Nur-Sultan
- **URL**: https://livingcost.org/cost/kazakhstan/nur-sultan
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Kazakhstan
- **Facts supporting**: Nur-Sultan / Astana cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as administratively useful but winter-negative
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-598
- **Title**: Livingcost - Cost of living in Shymkent
- **URL**: https://livingcost.org/cost/kazakhstan/shymkent
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Kazakhstan
- **Facts supporting**: Shymkent cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as first budget-and-climate screen
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-599
- **Title**: Livingcost - Cost of living in Aktau
- **URL**: https://livingcost.org/cost/kazakhstan/aktau
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Kazakhstan
- **Facts supporting**: Aktau cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as an affordable Caspian fallback pending service-depth checks
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-600
- **Title**: Livingcost - Cost of living in Armenia
- **URL**: https://livingcost.org/cost/armenia
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Armenia
- **Facts supporting**: Armenia national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, salary context, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-601
- **Title**: Livingcost - Cost of living in Yerevan
- **URL**: https://livingcost.org/cost/armenia/yerevan
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Armenia
- **Facts supporting**: Yerevan cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as the services-rich but rent-sensitive default screen
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-602
- **Title**: Livingcost - Cost of living in Gyumri
- **URL**: https://livingcost.org/cost/armenia/gyumri
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Armenia
- **Facts supporting**: Gyumri cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as a low-cost but cold-winter fallback
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-603
- **Title**: Livingcost - Cost of living in Vanadzor
- **URL**: https://livingcost.org/cost/armenia/vanadzor
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: Armenia
- **Facts supporting**: Vanadzor cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as an affordability fallback pending service-depth checks
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-604
- **Title**: Livingcost - Cost of living in the United Arab Emirates
- **URL**: https://livingcost.org/cost/united-arab-emirates
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: UAE
- **Facts supporting**: UAE national cost-of-living screen, including one-person and family-of-four totals, rent/utilities, food, transport, salary context, utilities, internet, and national 1BR / 3BR rent bands
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-605
- **Title**: Livingcost - Cost of living in Dubai
- **URL**: https://livingcost.org/cost/united-arab-emirates/dubai
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: UAE
- **Facts supporting**: Dubai cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as services-rich but rent-sensitive
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-606
- **Title**: Livingcost - Cost of living in Abu Dhabi
- **URL**: https://livingcost.org/cost/united-arab-emirates/abu-dhabi
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: UAE
- **Facts supporting**: Abu Dhabi cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as high-service but rent-sensitive
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-607
- **Title**: Livingcost - Cost of living in Sharjah
- **URL**: https://livingcost.org/cost/united-arab-emirates/sharjah
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: updated 2026-03-11
- **Date accessed**: 2026-06-15
- **Used by**: UAE
- **Facts supporting**: Sharjah cost/rent screen: total with rent, rent/utilities, food, transport, 1BR and 3BR rent bands, utilities, and internet; treated as the first lower-cost UAE screen
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-608
- **Title**: Eurydice — Portugal overview of the national education system
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/portugal/overview
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: official-secondary
- **Date published**: updated 2026-03-18
- **Date accessed**: 2026-06-15
- **Used by**: Portugal
- **Facts supporting**: Portugal public education structure, optional pre-primary education from age 3 to 6, compulsory basic-education cycles starting around age 6, and foreign-student diversity / teacher-shortage caveats
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-18

## src-609
- **Title**: Numbeo — Portugal cost of living / Lisbon / Porto childcare and school cost proxies
- **URL**: https://www.numbeo.com/cost-of-living/country_result.jsp?country=Portugal ; https://www.numbeo.com/cost-of-living/in/Lisbon ; https://www.numbeo.com/cost-of-living/in/Porto
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: live crowd-sourced table, no static publication date
- **Date accessed**: 2026-06-15
- **Used by**: Portugal
- **Facts supporting**: Private full-day preschool / kindergarten monthly fee proxies and international primary-school annual tuition proxies for Portugal, Lisbon, and Porto
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-610
- **Title**: International Schools Database — List of international schools in Portugal
- **URL**: https://www.international-schools-database.com/country/portugal
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: live directory, no static publication date captured
- **Date accessed**: 2026-06-15
- **Used by**: Portugal
- **Facts supporting**: Portugal international-school availability baseline, including the directory count of 82 international schools
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-611
- **Title**: Numbeo — Quality of Life and Crime / Safety in Portugal
- **URL**: https://www.numbeo.com/quality-of-life/country_result.jsp?country=Portugal ; https://www.numbeo.com/crime/country_result.jsp?country=Portugal
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: live crowd-sourced table, last update displayed 2026-06
- **Date accessed**: 2026-06-15
- **Used by**: Portugal
- **Facts supporting**: Portugal quality-of-life, safety, healthcare, climate, commute, pollution, and selected city-level safety-index proxies for comfort screening
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-15

## src-612
- **Title**: EF English Proficiency Index — Portugal country page
- **URL**: https://www.ef.com/wwen/epi/regions/europe/portugal/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 index page, no exact publication date captured
- **Date accessed**: 2026-06-15
- **Used by**: Portugal
- **Facts supporting**: Portugal English-proficiency screening baseline, including global rank #6 and EF EPI score 612, plus main city score context
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-15

## src-613
- **Title**: International Insurance — Health Insurance in Spain: Coverage Options for Foreigners
- **URL**: https://www.internationalinsurance.com/health/europe/spain.php
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: live guide, no static publication date captured
- **Date accessed**: 2026-06-15
- **Used by**: Spain
- **Facts supporting**: Spain public/private healthcare screening baseline, no-copay public doctor-visit context, private-care access caveats, uninsured private doctor / emergency-room visit proxies, and specialist-wait caveat (claim-spain-012)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-15

## src-614
- **Title**: Eurydice — Spain organisation of the education system and its structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/spain/organisation-education-system-and-its-structure
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: official-secondary
- **Date published**: updated 2026-01-20
- **Date accessed**: 2026-06-15
- **Used by**: Spain
- **Facts supporting**: Spain education-system structure, free compulsory primary and ESO schooling, age bands for primary / ESO, and public-school planning baseline (claim-spain-014)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-20

## src-615
- **Title**: Eurydice — Spain early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/spain/early-childhood-education-and-care
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: official-secondary
- **Date published**: updated 2026-01-20
- **Date accessed**: 2026-06-15
- **Used by**: Spain
- **Facts supporting**: Spain early-childhood education structure, voluntary 0-2 and 3-5 cycles, legal right to a place from age 3, free second cycle, and near-universal 3-5 attendance (claim-spain-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-20

## src-616
- **Title**: International Insurance — Health Insurance in Italy: Local, Private and Global Options
- **URL**: https://www.internationalinsurance.com/health/europe/italy.php
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: updated 2026-02-02
- **Date accessed**: 2026-06-15
- **Used by**: Italy
- **Facts supporting**: Italy public/private healthcare screening baseline, SSN access for non-citizens with residency status, scope of SSN-covered care, private-insurance need before residence is finalized, and general private-insurance caveats (claim-italy-012)
- **Confidence ceiling**: medium
- **Stale at**: 2027-02-02

## src-617
- **Title**: Eurydice — Italy organisation of the education system and its structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/italy/organisation-education-system-and-its-structure
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: official-secondary
- **Date published**: updated 2026-01-23
- **Date accessed**: 2026-06-15
- **Used by**: Italy
- **Facts supporting**: Italy education-system structure, compulsory education from 6 to 16, primary/lower-secondary/upper-secondary split, state/paritarie schooling baseline, and ECEC overview (claim-italy-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-23

## src-618
- **Title**: Eurydice — Italy early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/italy/early-childhood-education-and-care
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: official-secondary
- **Date published**: contents revised 2023-08
- **Date accessed**: 2026-06-15
- **Used by**: Italy
- **Facts supporting**: Italy ECEC split between 0-3 educational services and 3-6 pre-primary school, fee/free baseline, non-compulsory attendance, and nursery/pre-primary planning caveats (claim-italy-014)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-15


## src-619
- **Title**: UNHCR Greece — Access to Healthcare
- **URL**: https://help.unhcr.org/greece/living-in-greece/access-to-healthcare/
- **Archive**: stable UNHCR Help page via text mirror — snapshot not required
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-15
- **Used by**: Greece
- **Facts supporting**: free public healthcare access baseline for refugees/asylum seekers; PAAYPA and AMKA onboarding mechanics; emergency access number and vaccination-access baseline (claim-greece-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-15

## src-620
- **Title**: Eurydice — Greece organisation of the education system and its structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/greece/organisation-education-system-and-its-structure
- **Archive**: stable EU/EACEA Eurydice page via direct extraction — snapshot not required
- **Type**: official-secondary
- **Date published**: updated 2025-09-24
- **Date accessed**: 2026-06-15
- **Used by**: Greece
- **Facts supporting**: Greece formal education structure, compulsory two-year pre-primary from age 4, six-year primary school, lower/upper secondary structure, and public/private school baseline (claim-greece-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-09-24

## src-621
- **Title**: Eurydice — Greece early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/greece/early-childhood-education-and-care
- **Archive**: stable EU/EACEA Eurydice page via direct extraction — snapshot not required
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-15
- **Used by**: Greece
- **Facts supporting**: Greece ECEC split between under-age-4 municipal/private care and age-4/5 pre-primary school; compulsory two-year preschool from age 4; public nipiagogeia free-of-charge baseline (claim-greece-014)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-15


## src-622
- **Title**: GESY / Health Insurance Organisation — Beneficiary portal
- **URL**: https://www.gesy.org.cy/beneficiary/?lang=en
- **Archive**: [stable official portal; direct HTML shell captured 2026-06-16]
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Cyprus
- **Facts supporting**: Cyprus healthcare baseline; official GESY beneficiary portal anchor for public-healthcare registration / beneficiary checks after status is established
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-16

## src-623
- **Title**: Eurydice — Cyprus: Overview
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/cyprus/overview
- **Archive**: [stable EU education-system page; direct HTML captured 2026-06-16]
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Cyprus
- **Facts supporting**: Cyprus compulsory-education duration, public/free education baseline, and free textbooks for first-pass future-child education screening
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-16

## src-624
- **Title**: Eurydice — Cyprus: Early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/cyprus/early-childhood-education-and-care
- **Archive**: [stable EU education-system page; direct HTML captured 2026-06-16]
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Cyprus
- **Facts supporting**: Cyprus pre-primary / early-childhood public education baseline and compulsory/free education context
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-16

## src-625
- **Title**: Eurydice — Cyprus: Primary education
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/cyprus/primary-education
- **Archive**: [stable EU education-system page; direct HTML captured 2026-06-16]
- **Type**: official-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Cyprus
- **Facts supporting**: Cyprus public primary education: six-year cycle, free and compulsory for children who have reached age 6
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-16


## src-626
- **Title**: HZZO — Tko su osigurane osobe HZZO-a
- **URL**: https://hzzo.hr/obvezno-zdravstveno-osiguranje-0/tko-su-osigurane-osobe-hzzo
- **Archive**: stable official HZZO page via direct HTML extraction — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Croatia
- **Facts supporting**: Croatia compulsory-health-insurance insured-person categories, including permanent/long-term residents, employees/self-employed bases, children, family members, and some EU temporary-stay categories (claim-croatia-012)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-16

## src-627
- **Title**: HZZO — Prijava, promjena i odjava u obveznom zdravstvenom osiguranju
- **URL**: https://hzzo.hr/obvezno-zdravstveno-osiguranje-0/prijava-promjena-i-odjava-u-obveznom-zdravstvenom-osiguranju
- **Archive**: stable official HZZO page via direct HTML extraction — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Croatia
- **Facts supporting**: HZZO application/change/deregistration filing at any regional office or branch within 8 days from status-triggering circumstances (claim-croatia-013)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-16

## src-628
- **Title**: HZZO — Opseg prava na zdravstvenu zastitu iz obveznoga zdravstvenog osiguranja
- **URL**: https://hzzo.hr/obvezno-zdravstveno-osiguranje-0/opseg-prava-na-zdravstvenu-zastitu-iz-obveznoga-zdravstvenog
- **Archive**: stable official HZZO page via direct HTML extraction — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Croatia
- **Facts supporting**: compulsory-insurance healthcare scope including preventive student care and women's healthcare related to pregnancy monitoring and childbirth (claim-croatia-012)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-16

## src-629
- **Title**: Eurydice — Croatia: Overview
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/croatia/overview
- **Archive**: stable EU/EACEA Eurydice page via direct extraction — snapshot not required
- **Type**: official-secondary
- **Date published**: updated 2025-09-24
- **Date accessed**: 2026-06-16
- **Used by**: Croatia
- **Facts supporting**: Croatia education-system overview: compulsory 8-year primary/lower-secondary single structure from age 6-7 to 14-15, public/private primary baseline, and mandatory state-financed/free preschool year before elementary school (claim-croatia-014, claim-croatia-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-09-24

## src-630
- **Title**: Eurydice — Croatia: Early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/croatia/early-childhood-education-and-care
- **Archive**: stable EU/EACEA Eurydice page via direct extraction — snapshot not required
- **Type**: official-secondary
- **Date published**: updated 2025-05-14
- **Date accessed**: 2026-06-16
- **Used by**: Croatia
- **Facts supporting**: Croatia ECEC baseline: kindergarten/other providers for ages 6 months to primary-school age, and mandatory one-year pre-primary programme before starting school (claim-croatia-015)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-14


## src-631
- **Title**: Expat Arrivals — Healthcare and health insurance for expats in Malta
- **URL**: https://www.expatarrivals.com/europe/malta/healthcare-malta
- **Archive**: stable page via Jina text mirror — direct extraction used
- **Type**: reputable-secondary
- **Date published**: 2026-06-16
- **Date accessed**: 2026-06-16
- **Used by**: Malta
- **Facts supporting**: Malta public/private healthcare screening baseline, private-insurance need for non-EU/UK expats, public health-centre / hospital structure, pharmacy access, emergency number 112, and routine-vaccination caveat
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-16

## src-632
- **Title**: Eurydice — Malta: Overview
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/malta/overview
- **Archive**: stable EU/EACEA Eurydice page via direct extraction — snapshot not required
- **Type**: official-secondary
- **Date published**: updated 2025-04-22
- **Date accessed**: 2026-06-16
- **Used by**: Malta
- **Facts supporting**: Malta education-system overview, childcare / kindergarten age bands, compulsory education ages 5-16, primary and secondary cycle structure, and state/church/independent school baseline
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-04-22

## src-633
- **Title**: Eurydice — Malta: Organisation of the education system and of its structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/malta/organisation-education-system-and-its-structure
- **Archive**: stable EU/EACEA Eurydice page via direct extraction — snapshot not required
- **Type**: official-secondary
- **Date published**: updated 2025-02-13
- **Date accessed**: 2026-06-16
- **Used by**: Malta
- **Facts supporting**: Malta formal education structure, primary education as a six-year cycle for ages 5-11, and compulsory-education structure
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-13

## src-634
- **Title**: Eurydice — Malta: Early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/malta/early-childhood-education-and-care
- **Archive**: stable EU/EACEA Eurydice page via direct extraction — snapshot not required
- **Type**: official-secondary
- **Date published**: updated 2024-01-30
- **Date accessed**: 2026-06-16
- **Used by**: Malta
- **Facts supporting**: Malta early-childhood education and care baseline, including the Free Childcare Scheme for parents in employment or furthering education
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-01-30


## src-635
- **Title**: PVZP — Foreigners' Medical Insurance
- **URL**: https://www.pvzp.cz/en/products/foreigners-medical-insurance/
- **Archive**: [archive: failed 2026-06-16; direct extraction used]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Czech Republic
- **Facts supporting**: Czech foreigners' medical-insurance product baseline, including dedicated comprehensive foreigner-insurance product family (claim-czech-016)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-16

## src-636
- **Title**: InfoCizinci.cz — Health insurance calculator for foreigners in CZ
- **URL**: https://infocizinci.cz/en/health-insurance-calculator/
- **Archive**: [archive: failed 2026-06-16; direct extraction used]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Czech Republic
- **Facts supporting**: Czech foreigner health-insurance requirement baseline, emergency vs comprehensive insurance distinction, indicative starting monthly price from CZK 1,000, and pregnancy-coverage caveat (claim-czech-016, claim-czech-017)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-16

## src-637
- **Title**: Eurydice — Czechia: Early childhood education and care / overview
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/czechia/early-childhood-education-and-care and https://eurydice.eacea.ec.europa.eu/national-education-systems/czechia/overview
- **Archive**: stable EU/EACEA Eurydice page via direct extraction — snapshot not required
- **Type**: official-secondary
- **Date published**: updated 2026-06-10 for structure-linked page; ECEC page accessed current
- **Date accessed**: 2026-06-16
- **Used by**: Czech Republic
- **Facts supporting**: Czech ECEC baseline: children's groups from 6 months, nursery schools for ages 2-6/7, compulsory last pre-primary year, municipal nursery-place obligation for children aged 3+, and school-administration roles (claim-czech-018)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-10

## src-638
- **Title**: Eurydice — Czechia: Organisation of the education system and of its structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/czechia/organisation-education-system-and-its-structure
- **Archive**: stable EU/EACEA Eurydice page via direct extraction — snapshot not required
- **Type**: official-secondary
- **Date published**: updated 2026-06-10
- **Date accessed**: 2026-06-16
- **Used by**: Czech Republic
- **Facts supporting**: Czech education-system structure, compulsory/free final pre-primary year in public/state nursery schools, and 9-year basic education / compulsory schooling baseline (claim-czech-018)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-10


## src-639
- **Title**: Pacjent.gov.pl / NFZ — Medical assistance for Ukrainian citizens
- **URL**: https://pacjent.gov.pl/aktualnosc/pomoc-medyczna-dla-obywateli-ukrainy
- **Archive**: stable official patient/NFZ page via Jina text mirror — snapshot not required
- **Type**: official-primary
- **Date published**: 2022-02-28; modified 2022-12-22
- **Date accessed**: 2026-06-16
- **Used by**: Poland
- **Facts supporting**: Ukraine special-framework public medical-care baseline: medical services are settled like for Polish patients, Ukrainian citizens have an additional health-service entitlement, and NFZ pays from the state budget (claim-poland-022)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-16

## src-640
- **Title**: Expat Arrivals — Healthcare and health insurance for expats in Poland
- **URL**: https://www.expatarrivals.com/europe/poland/healthcare-poland
- **Archive**: stable page via Jina text mirror — direct extraction used
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Poland
- **Facts supporting**: Poland public/private healthcare screening baseline, private-insurance usefulness, large-city facility baseline, waiting-list / GP-referral friction, and language-barrier caveat (claim-poland-023)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-16

## src-641
- **Title**: Eurydice — Poland: Overview / Early childhood education and care / Organisation of the education system
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/poland/overview ; https://eurydice.eacea.ec.europa.eu/national-education-systems/poland/early-childhood-education-and-care ; https://eurydice.eacea.ec.europa.eu/national-education-systems/poland/organisation-education-system-and-its-structure
- **Archive**: stable EU/EACEA Eurydice pages via Jina text mirror — snapshot not required
- **Type**: official-secondary
- **Date published**: accessed current 2026-06-16
- **Date accessed**: 2026-06-16
- **Used by**: Poland
- **Facts supporting**: Poland education baseline: optional preschool for ages 3-5, obligatory preschool for 6-year-olds, entitlement to community pre-primary place, 8-year primary school usually ages 7-15, and education/training obligation to age 18 (claim-poland-024)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-16

## src-642
- **Title**: Expat Arrivals — Healthcare and health insurance for expats in Romania
- **URL**: https://www.expatarrivals.com/europe/romania/healthcare-romania
- **Archive**: stable page via Jina text mirror — direct extraction used
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-16
- **Used by**: Romania
- **Facts supporting**: Romania public/private healthcare screening baseline, National Health Insurance House context, private medical-insurance need for expats / visa issuance, public-system waiting-time and facility-quality caveats (claim-romania-022)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-16

## src-643
- **Title**: Eurydice — Romania: Overview / Organisation of the education system / Early childhood education and care / Primary education
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/romania/overview ; https://eurydice.eacea.ec.europa.eu/national-education-systems/romania/organisation-education-system-and-its-structure ; https://eurydice.eacea.ec.europa.eu/national-education-systems/romania/early-childhood-education-and-care ; https://eurydice.eacea.ec.europa.eu/national-education-systems/romania/primary-education
- **Archive**: stable EU/EACEA Eurydice pages via Jina text mirror — snapshot not required
- **Type**: official-secondary
- **Date published**: accessed current 2026-06-16
- **Date accessed**: 2026-06-16
- **Used by**: Romania
- **Facts supporting**: Romania education baseline: Ministry / inspectorate governance, ECEC ages and free/compulsory baseline, primary education start and structure, lower-secondary structure, and free public primary textbooks (claim-romania-023, claim-romania-024)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-16

## src-644
- **Title**: National Health Insurance Fund (NHIF) Bulgaria — Welcome / institutional overview
- **URL**: https://www.nhif.bg/en
- **Archive**: direct HTML extraction used; stable official page
- **Type**: official-primary
- **Date published**: no page date shown
- **Date accessed**: 2026-06-17
- **Used by**: Bulgaria
- **Facts supporting**: NHIF public / compulsory health-insurance institutional baseline and regional fund structure (claim-bulgaria-022)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-645
- **Title**: Eurydice — Bulgaria: Early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/bulgaria/early-childhood-education-and-care
- **Archive**: stable EU/EACEA Eurydice page via Jina text mirror — direct extraction used
- **Type**: official-secondary
- **Date published**: accessed current 2026-06-17
- **Date accessed**: 2026-06-17
- **Used by**: Bulgaria
- **Facts supporting**: Bulgaria ECEC structure, nursery/kindergarten age bands, compulsory pre-primary from age 4, and free compulsory preschool in state/municipal kindergartens (claim-bulgaria-023)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-646
- **Title**: Eurydice — Bulgaria: Overview of the education system
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/bulgaria/overview
- **Archive**: stable EU/EACEA Eurydice page via Jina text mirror — direct extraction used
- **Type**: official-secondary
- **Date published**: 2026-06-16 page timestamp in extracted metadata
- **Date accessed**: 2026-06-17
- **Used by**: Bulgaria
- **Facts supporting**: Bulgaria pre-school and school-system governance, state education standards, and public-school structure (claim-bulgaria-024)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-647
- **Title**: International Schools Database — British School of Sofia fees
- **URL**: https://www.international-schools-database.com/in/sofia/british-school-of-sofia
- **Archive**: stable page via Jina text mirror — direct extraction used
- **Type**: commercial
- **Date published**: 2025/2026 fee data shown on page
- **Date accessed**: 2026-06-17
- **Used by**: Bulgaria
- **Facts supporting**: Sofia international-school fee risk benchmark for the future-child budget (claim-bulgaria-025)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-17

## src-648
- **Title**: NEAK Hungary - Health-care services for insured persons
- **URL**: https://www.neak.gov.hu/felso_menu/lakossagnak/ellatas_magyarorszagon/egeszsegugyi_ellatasok
- **Archive**: stable official page via Jina text mirror - direct extraction used
- **Type**: official-primary
- **Date published**: no page date shown
- **Date accessed**: 2026-06-17
- **Used by**: Hungary
- **Facts supporting**: public health-insurance service baseline for insured persons, including screening, treatment, family-doctor / pediatric / dental basic care, specialist care, and hospital care categories (claim-hungary-022)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-649
- **Title**: Eurydice - Hungary: Early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/hungary/early-childhood-education-and-care
- **Archive**: stable EU/EACEA Eurydice page via Jina text mirror - direct extraction used
- **Type**: official-secondary
- **Date published**: last update 2026-03-29 in extracted page
- **Date accessed**: 2026-06-17
- **Used by**: Hungary
- **Facts supporting**: Hungary ECEC split between nursery birth-to-3 and mandatory free kindergarten from age 3 until compulsory schooling; ministry / municipal governance context (claim-hungary-023)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-29

## src-650
- **Title**: Eurydice - Hungary: Organisation of the education system and of its structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/hungary/organisation-education-system-and-its-structure
- **Archive**: stable EU/EACEA Eurydice page via Jina text mirror - direct extraction used
- **Type**: official-secondary
- **Date published**: 2026-06-16 page timestamp in extracted metadata
- **Date accessed**: 2026-06-17
- **Used by**: Hungary
- **Facts supporting**: kindergarten from age 3, mandatory school age 6-16, and 8-grade basic education structure (claim-hungary-024)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-16

## src-651
- **Title**: International Schools Database - Budapest international schools
- **URL**: https://www.international-schools-database.com/in/budapest
- **Archive**: stable page via Jina text mirror - direct extraction used
- **Type**: commercial
- **Date published**: 2025/2026 fee data shown on page
- **Date accessed**: 2026-06-17
- **Used by**: Hungary
- **Facts supporting**: Budapest international-school market and British International School Budapest 2025/2026 fee benchmark for future-child budget risk (claim-hungary-024)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-17

## src-652
- **Title**: IOM Migration Information Centre Slovakia — Health Care / Public health insurance / Insurance card and payments / Doctors and medical facilities
- **URL**: https://www.mic.iom.sk/en/social-issues/health-care.html ; https://www.mic.iom.sk/en/social-issues/health-care/438-public-health-insurance.html ; https://www.mic.iom.sk/en/social-issues/health-care/440-insurance-card-and-payments-for-health-care.html ; https://www.mic.iom.sk/en/social-issues/health-care/442-doctors-and-medical-facilities-in-slovakia.html
- **Archive**: stable IOM pages via Jina text mirror — direct extraction used
- **Type**: reputable-secondary
- **Date published**: public-health page last updated 2026-02-11; other subpages last updated 2021-03-08
- **Date accessed**: 2026-06-17
- **Used by**: Slovakia
- **Facts supporting**: healthcare screening baseline: public-health-insurance eligibility mechanics, insurance-card proof, doctor/facility lookup, and IOM consultation contact point (claim-slovakia-020, claim-slovakia-021)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-02-11

## src-653
- **Title**: Eurydice — Slovakia: Early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/slovakia/early-childhood-education-and-care
- **Archive**: stable EU/EACEA Eurydice page — direct extraction used
- **Type**: official-secondary
- **Date published**: accessed current 2026-06-17
- **Date accessed**: 2026-06-17
- **Used by**: Slovakia
- **Facts supporting**: Slovakia ECEC baseline: care for ages 6 months to 3 years, kindergarten ages 3-6, compulsory last kindergarten year from age 5, and free compulsory pre-primary education in public kindergartens (claim-slovakia-022)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-654
- **Title**: Eurydice — Slovakia: Organisation of the education system and of its structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/slovakia/organisation-education-system-and-its-structure
- **Archive**: stable EU/EACEA Eurydice page — direct extraction used
- **Type**: official-secondary
- **Date published**: last update 2025-08-20 in extracted page
- **Date accessed**: 2026-06-17
- **Used by**: Slovakia
- **Facts supporting**: Slovakia school-system baseline: compulsory school attendance duration, start age, primary-school stages, and state/private/church school choice (claim-slovakia-023)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-655
- **Title**: International Schools Database — Bratislava international schools
- **URL**: https://www.international-schools-database.com/in/bratislava
- **Archive**: stable page — direct extraction used
- **Type**: commercial
- **Date published**: 2025/2026 fee data shown on page
- **Date accessed**: 2026-06-17
- **Used by**: Slovakia
- **Facts supporting**: Bratislava international-school market and 2025/2026 fee benchmarks for future-child budget risk (claim-slovakia-023)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-17

## src-656
- **Title**: GOV.SI — Healthcare for Ukrainian nationals
- **URL**: https://www.gov.si/en/topics/slovenias-assistance-to-the-citizens-of-ukraine/healthcare-for-ukrainian-nationals/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-17
- **Used by**: Slovenia
- **Facts supporting**: temporary-protection healthcare access for Ukrainian nationals, emergency healthcare rights, proof/card mechanics, pregnancy/childbirth healthcare, medicines procedure, GP request route, and coverage by the Government Office for the Support and Integration of Migrants (claim-slovenia-018)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-17

## src-657
- **Title**: ZZZS — Compulsory health insurance / accessing healthcare in Slovenia / extent and classes of rights
- **URL**: https://www.zzzs.si/en/compulsory-health-insurance/inclusion-in-the-compulsory-health-insurance/ ; https://www.zzzs.si/en/accessing-healthcare-in-slovenia/ ; https://www.zzzs.si/en/compulsory-health-insurance/the-extent-of-rights-deriving-from-compulsory-health-insurance/ ; https://www.zzzs.si/en/compulsory-health-insurance/classes-of-rights-under-compulsory-health-insurance/
- **Archive**: stable public health-insurance institute pages — direct extraction used
- **Type**: official-primary
- **Date published**: current public pages, no single publication date captured
- **Date accessed**: 2026-06-17
- **Used by**: Slovenia
- **Facts supporting**: Slovenia compulsory-health-insurance registration baseline, family-member insurance categories, temporary-residence requirement for immediate family members, public provider network, and statutory healthcare-rights basket including primary, specialist, hospital, pregnancy preventive care, medicines, devices, and transport (claim-slovenia-019)
- **Confidence ceiling**: high
- **Stale at**: 2026-12-17

## src-658
- **Title**: GOV.SI — Providing education to Ukrainian children living in Slovenia
- **URL**: https://www.gov.si/en/topics/slovenias-assistance-to-the-citizens-of-ukraine/izobrazevanje-ukrajinskih-otrok-v-sloveniji/
- **Archive**: stable gov domain — snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-17
- **Used by**: Slovenia
- **Facts supporting**: temporary-protection education card/decision proof, inclusive kindergarten and regular-class baseline, kindergarten entry throughout year if places are available, vaccination certificate requirement, reduced/free kindergarten fee rules for temporary-protection families, and same-conditions primary enrolment for under-18 temporary-protection children
- **Confidence ceiling**: high
- **Stale at**: 2027-06-17

## src-659
- **Title**: Eurydice — Slovenia: Access to early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/slovenia/access
- **Archive**: stable EU/EACEA Eurydice page — direct extraction used
- **Type**: official-secondary
- **Date published**: 2025-09-02 average-price table; 2026-01 payment-bracket table cited on page
- **Date accessed**: 2026-06-17
- **Used by**: Slovenia
- **Facts supporting**: kindergarten place guarantee, age/access baseline, average 2025 programme prices, parent-payment subsidy range from 0% to 77%, social-work-centre reduced-payment application, and foreign-parent / multi-child payment caveats (claim-slovenia-020)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-660
- **Title**: Eurydice — Slovenia: Organisation of the education system and of its structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/slovenia/organisation-education-system-and-its-structure
- **Archive**: stable EU/EACEA Eurydice page — direct extraction used
- **Type**: official-secondary
- **Date published**: current public page, no single publication date captured
- **Date accessed**: 2026-06-17
- **Used by**: Slovenia
- **Facts supporting**: Slovenia compulsory publicly funded nine-year basic education from age 6 to about 15 and local public-school place guarantee (claim-slovenia-021)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-661
- **Title**: International Schools Database — Ljubljana international schools
- **URL**: https://www.international-schools-database.com/in/ljubljana
- **Archive**: stable page — direct extraction used
- **Type**: commercial
- **Date published**: 2025/2026 fee data shown where published
- **Date accessed**: 2026-06-17
- **Used by**: Slovenia
- **Facts supporting**: Ljubljana international-school market and fee benchmarks for future-child budget risk (claim-slovenia-022)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-17


## src-662
- **Title**: FZOCG - Health Insurance Fund of Montenegro (institutional overview)
- **URL**: https://fzocg.me/
- **Archive**: direct HTML extraction used; official public site
- **Type**: official-primary
- **Date published**: no page date shown
- **Date accessed**: 2026-06-17
- **Used by**: Montenegro
- **Facts supporting**: public health-insurance / insurer map, headquarters and regional units, contracted institutions/pharmacies, price lists, insured-person rights, medicines, and e-health links (claim-montenegro-021)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-663
- **Title**: Montenegro Ministry of Health - ministry homepage / contact baseline
- **URL**: https://www.gov.me/en/mzd
- **Archive**: direct HTML extraction used; official government page
- **Type**: official-primary
- **Date published**: no page date shown
- **Date accessed**: 2026-06-17
- **Used by**: Montenegro
- **Facts supporting**: Ministry of Health authority/contact baseline and Podgorica health-system contact point for later healthcare onboarding checks
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-664
- **Title**: Eurydice - Montenegro: Access to early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/montenegro/access
- **Archive**: stable EU/EACEA Eurydice page - direct extraction used
- **Type**: official-secondary
- **Date published**: current public page, no single publication date captured
- **Date accessed**: 2026-06-17
- **Used by**: Montenegro
- **Facts supporting**: ECEC equal-access baseline, public/private preschool network, public-preschool parent fees of about EUR 50 full-day and EUR 25 half-day, reduced/free fee categories, and private-preschool fee caveat (claim-montenegro-023)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-665
- **Title**: Eurydice - Montenegro: Organisation of the education system and of its structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/montenegro/organisation-education-system-and-its-structure
- **Archive**: stable EU/EACEA Eurydice page - direct extraction used
- **Type**: official-secondary
- **Date published**: last update 2026-05-04 in extracted page
- **Date accessed**: 2026-06-17
- **Used by**: Montenegro
- **Facts supporting**: education-system levels, nursery/kindergarten age bands, compulsory 9-year primary education, and free primary education from about age 6 to 15 (claim-montenegro-024)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-04

## src-666
- **Title**: QSI International School of Montenegro - school homepage
- **URL**: https://www.qsi.org/montenegro/
- **Archive**: direct HTML extraction used; tuition page not found
- **Type**: commercial
- **Date published**: no page date shown
- **Date accessed**: 2026-06-17
- **Used by**: Montenegro
- **Facts supporting**: international-school alternative in Donja Gorica, Podgorica, covering preschool, elementary, middle, and secondary levels; tuition remains uncaptured (claim-montenegro-025)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-17


## src-667
- **Title**: RFZO Serbia - insured-person rights / compulsory health-insurance baseline
- **URL**: https://www.rfzo.rs/index.php/osiguranalica
- **Archive**: text mirror extraction used; original RFZO URL cited
- **Type**: official-primary
- **Date published**: public page rendered 2026-06-17 in text mirror; no stable page date shown
- **Date accessed**: 2026-06-17
- **Used by**: Serbia
- **Facts supporting**: Serbian compulsory health-insurance / insured-person rights baseline, contracted healthcare institutions, insurance-document requirement, covered-care categories including pregnancy/childbirth/children (claim-serbia-020, claim-serbia-021)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-668
- **Title**: Eurydice - Serbia: Overview
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/serbia/overview
- **Archive**: stable EU/EACEA Eurydice page - direct extraction used
- **Type**: official-secondary
- **Date published**: last update 2026-05-29 in extracted page
- **Date accessed**: 2026-06-17
- **Used by**: Serbia
- **Facts supporting**: Serbian education-system structure, Ministry role, public/private institution baseline, compulsory preschool preparatory programme plus 8 years basic education, free public basic and secondary education (claim-serbia-022)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-29

## src-669
- **Title**: Eurydice - Serbia: Early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/serbia/early-childhood-education-and-care
- **Archive**: stable EU/EACEA Eurydice page - direct extraction used
- **Type**: official-secondary
- **Date published**: last update 2025-09-21 in extracted page
- **Date accessed**: 2026-06-17
- **Used by**: Serbia
- **Facts supporting**: ECEC age bands from 6 months to 6.5 years, nursery/kindergarten/preschool preparatory split, mandatory/free preschool preparatory programme, and ECEC care/preventive-health/social-protection role (claim-serbia-022)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-09-21

## src-670
- **Title**: International Schools Database - Belgrade international schools
- **URL**: https://www.international-schools-database.com/in/belgrade
- **Archive**: stable commercial directory page - direct extraction used
- **Type**: commercial
- **Date published**: 2026/2027 fee data shown where published
- **Date accessed**: 2026-06-17
- **Used by**: Serbia
- **Facts supporting**: Belgrade international-school market and fee benchmarks, including International School of Belgrade 2026/2027 yearly fees (claim-serbia-023)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-17

## src-671
- **Title**: SGK Turkey Social Security Institution / General Health Insurance public site
- **URL**: https://www.sgk.gov.tr/ ; https://www.sgk.gov.tr/Content/Post/b8664248-0ed2-4d28-ae80-89df691fd21d/Ilave-Ucret-2022-05-14-09-21-06
- **Archive**: stable official public site; text mirror extraction used where direct page text was dynamic
- **Type**: official-primary
- **Date published**: public pages, no single publication date captured
- **Date accessed**: 2026-06-17
- **Used by**: Turkey
- **Facts supporting**: public SGK / General Health Insurance institution map and healthcare-provider extra-fee context used to open Turkey section 5.6 healthcare baseline (claim-turkey-019)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-17

## src-672
- **Title**: Turkey Ministry of Health public site
- **URL**: https://www.saglik.gov.tr/
- **Archive**: stable official public site; text mirror extraction used
- **Type**: official-primary
- **Date published**: current public site; no single publication date captured
- **Date accessed**: 2026-06-17
- **Used by**: Turkey
- **Facts supporting**: public Ministry of Health authority/contact baseline for Turkey healthcare-system orientation (claim-turkey-019)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-12-17

## src-673
- **Title**: Eurydice - Turkey: Overview
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/turkey/overview
- **Archive**: stable EU/EACEA Eurydice page; text mirror extraction used
- **Type**: official-secondary
- **Date published**: last update 2025-12-09 in extracted page
- **Date accessed**: 2026-06-17
- **Used by**: Turkey
- **Facts supporting**: Turkish education-system structure, MoNE role, and 12-year compulsory education split into 4+4+4 stages (claim-turkey-020)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-674
- **Title**: Eurydice - Turkey: Early childhood education and care / organisation of the education system
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/turkey/early-childhood-education-and-care ; https://eurydice.eacea.ec.europa.eu/national-education-systems/turkey/organisation-education-system-and-its-structure
- **Archive**: stable EU/EACEA Eurydice pages; text mirror extraction used
- **Type**: official-secondary
- **Date published**: current public pages; 2026 extraction used
- **Date accessed**: 2026-06-17
- **Used by**: Turkey
- **Facts supporting**: preschool age-band responsibilities, voluntary pre-primary baseline, free public pre-primary services, private nursery/daycare fee caveat, and primary/lower-secondary age rules (claim-turkey-020, claim-turkey-021)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-675
- **Title**: International Schools Database - Istanbul international schools
- **URL**: https://www.international-schools-database.com/in/istanbul
- **Archive**: stable commercial directory page; text mirror extraction used
- **Type**: commercial
- **Date published**: 2026/2027 fee data shown where published
- **Date accessed**: 2026-06-17
- **Used by**: Turkey
- **Facts supporting**: Istanbul international-school market and fee benchmarks for future-child budget risk (claim-turkey-022)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-17

## src-676
- **Title**: U.S. International Trade Administration - Healthcare Resource Guide: Georgia
- **URL**: https://www.trade.gov/healthcare-resource-guide-georgia
- **Archive**: direct HTML extraction used from official .gov page
- **Type**: reputable-secondary
- **Date published**: current public guide, no single page date captured
- **Date accessed**: 2026-06-17
- **Used by**: Georgia
- **Facts supporting**: healthcare system structure, high private-hospital share, citizen-focused Universal Healthcare Coverage, out-of-pocket/co-pay risk, Tbilisi vs rural healthcare capacity, and private-insurance context (claim-georgia-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-17

## src-677
- **Title**: Eurydice - Georgia: Overview / general education structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/georgia/overview ; https://eurydice.eacea.ec.europa.eu/national-education-systems/georgia/organisation-education-system-and-its-structure
- **Archive**: stable EU/EACEA Eurydice pages - direct extraction used
- **Type**: official-secondary
- **Date published**: pages rendered 2026-06-17 in extraction
- **Date accessed**: 2026-06-17
- **Used by**: Georgia
- **Facts supporting**: Georgia 12-year general-education structure, primary/basic/secondary grades, age-6 school-entry rule, compulsory primary and basic education, and national-curriculum baseline (claim-georgia-018)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-678
- **Title**: Eurydice - Georgia: Early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/georgia/early-childhood-education-and-care
- **Archive**: stable EU/EACEA Eurydice page - direct extraction used
- **Type**: official-secondary
- **Date published**: page rendered 2026-06-17 in extraction
- **Date accessed**: 2026-06-17
- **Used by**: Georgia
- **Facts supporting**: early/preschool education age bands, free public preschool education and catering, municipal funding, voluntary participation, and school-readiness component (claim-georgia-019)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-17

## src-679
- **Title**: International Schools Database - Tbilisi international schools
- **URL**: https://www.international-schools-database.com/in/tbilisi
- **Archive**: stable commercial directory page - direct extraction used
- **Type**: commercial
- **Date published**: 2025/2026 fee data shown where published
- **Date accessed**: 2026-06-17
- **Used by**: Georgia
- **Facts supporting**: Tbilisi international-school market, languages/curricula, and a published Deutsche Internationale Schule Tbilissi 2025/2026 fee range for budget-risk screening (claim-georgia-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-17

## src-680
- **Title**: U.S. International Trade Administration - Albania Medical Equipment / healthcare system overview
- **URL**: https://www.trade.gov/country-commercial-guides/albania-medical-equipment
- **Archive**: direct HTML extraction used from official .gov page
- **Type**: reputable-secondary
- **Date published**: 2021-10-09
- **Date accessed**: 2026-06-18
- **Used by**: Albania
- **Facts supporting**: healthcare system structure, Ministry of Health and Social Protection role, compulsory healthcare insurance fund baseline, public hospital capacity, Tirana private-hospital market, and private-sector growth (claim-albania-017, claim-albania-018)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-18

## src-681
- **Title**: Eurydice - Albania: Overview
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/albania/overview
- **Archive**: stable EU/EACEA Eurydice page - direct extraction used
- **Type**: official-secondary
- **Date published**: last update 2025-09-15 in extracted page
- **Date accessed**: 2026-06-18
- **Used by**: Albania
- **Facts supporting**: education governance, public/private institution baseline, obligatory education ages 6-16, basic/lower-secondary structure, optional upper secondary, and ministry contact baseline (claim-albania-019)
- **Confidence ceiling**: medium-high
- **Stale at**: 2026-09-15

## src-682
- **Title**: Eurydice - Albania: Early childhood education and care
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/albania/early-childhood-education-and-care
- **Archive**: stable EU/EACEA Eurydice page - direct extraction used
- **Type**: official-secondary
- **Date published**: last update 2026-03-30 in extracted page
- **Date accessed**: 2026-06-18
- **Used by**: Albania
- **Facts supporting**: preschool age bands, nursery/kindergarten split, non-obligatory ECEC, public/private nursery fees, full-day public kindergarten local fees, and free half-day public kindergarten baseline (claim-albania-019)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-03-30

## src-683
- **Title**: Tirana International School (QSI) - admissions, preschool, and secondary school pages
- **URL**: https://tirana.qsi.org/admissions ; https://tirana.qsi.org/academics/preschool ; https://tirana.qsi.org/academics/secondary-school
- **Archive**: direct HTML extraction used from public school pages
- **Type**: commercial
- **Date published**: current public pages, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Albania
- **Facts supporting**: Tirana English-language international-school option, no-prior-English admissions baseline through age 13 / U.S. grade 8, preschool from age 2, English instruction, secondary college-prep programme, and AP / IB-linked offerings (claim-albania-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-684
- **Title**: U.S. International Trade Administration - Uruguay Healthcare
- **URL**: https://www.trade.gov/country-commercial-guides/uruguay-healthcare
- **Archive**: direct HTML extraction used from official .gov page
- **Type**: reputable-secondary
- **Date published**: 2025-08-28
- **Date accessed**: 2026-06-18
- **Used by**: Uruguay
- **Facts supporting**: Uruguay SNIS/FONASA healthcare-system structure, public/private provider choice, mutualista baseline, and premium private-insurance context (claim-uruguay-016)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-685
- **Title**: gub.uy - Carne de salud procedure
- **URL**: https://www.gub.uy/tramites/carne-salud
- **Archive**: stable government service page - direct extraction used
- **Type**: official-primary
- **Date published**: current public procedure page, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Uruguay
- **Facts supporting**: Uruguayan health-card procedure anchor for healthcare/residence-file planning (claim-uruguay-017)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-18

## src-686
- **Title**: gub.uy - Education in Uruguay
- **URL**: https://www.gub.uy/educacion-en-uruguay
- **Archive**: stable government overview page - direct extraction used
- **Type**: official-primary
- **Date published**: current public overview page, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Uruguay
- **Facts supporting**: Uruguay education structure: initial education ages 3-5, compulsory from age 4, public primary compulsory/free from age 6, secondary cycles from age 12 (claim-uruguay-018)
- **Confidence ceiling**: high
- **Stale at**: 2027-06-18

## src-687
- **Title**: Uruguay Ministry of Education and Culture - Panorama of early childhood and initial education 2023
- **URL**: https://www.gub.uy/ministerio-educacion-cultura/datos-y-estadisticas/estadisticas/panorama-educacion-primera-infancia-inicial-2023 ; https://www.gub.uy/ministerio-desarrollo-social/node/8839
- **Archive**: stable government pages - direct extraction used
- **Type**: official-primary
- **Date published**: 2024-11-15 for MEC panorama page; MIDES page current, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Uruguay
- **Facts supporting**: early-childhood and initial-education statistics/context, compulsory initial education from age 4, and age-3 coverage expansion context (claim-uruguay-018)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-18

## src-688
- **Title**: ExpatLife.AI - Schools in Uruguay 2026: fees guide
- **URL**: https://expatlife.ai/uruguay/education
- **Archive**: [archive: failed 2026-06-18, Wayback HTTP 429]; text mirror/direct HTML extraction used
- **Type**: aggregator
- **Date published**: data verified 2026-05-08 on page
- **Date accessed**: 2026-06-18
- **Used by**: Uruguay
- **Facts supporting**: Montevideo international-school sector and broad annual fee screen of about USD 6,000-18,000/year for English/bilingual/IB options (claim-uruguay-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18


## src-689
- **Title**: Paraguay Ministry of Public Health and Social Welfare - public website / services and hospitals baseline
- **URL**: https://www.mspbs.gov.py/ ; https://www.mspbs.gov.py/portal/portal.html
- **Archive**: stable ministry pages - direct HTML extraction used
- **Type**: official-primary
- **Date published**: current public pages, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Paraguay
- **Facts supporting**: public health authority, regional health services, specialist/general/maternal-child hospital categories, and public-system entry map for the Paraguay healthcare screen (claim-paraguay-016)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-18

## src-690
- **Title**: ExpatLife.AI - Paraguay Healthcare 2026: insurance and hospitals guide
- **URL**: https://expatlife.ai/paraguay/healthcare
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: data verified 2026-06-18 on page
- **Date accessed**: 2026-06-18
- **Used by**: Paraguay
- **Facts supporting**: Paraguay public/IPS/private healthcare structure, private GP cost proxy of USD 15-50, private insurance proxy of USD 50-150/month, and Asuncion private-hospital baseline (claim-paraguay-016, claim-paraguay-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-691
- **Title**: ExpatLife.AI - Schools in Paraguay 2026: fees guide
- **URL**: https://expatlife.ai/paraguay/education
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: data verified 2026-06-18 on page
- **Date accessed**: 2026-06-18
- **Used by**: Paraguay
- **Facts supporting**: public school free / Spanish-Guarani / resource caveat, private bilingual school proxy of USD 200-500/month, international-school proxy of USD 6,000-12,000/year, and American School of Asuncion proxy of USD 8,000-15,000/year (claim-paraguay-018, claim-paraguay-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-692
- **Title**: American School of Asuncion - public website
- **URL**: https://www.asa.edu.py
- **Archive**: direct HTML extraction used from public school page
- **Type**: commercial
- **Date published**: current public page, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Paraguay
- **Facts supporting**: Asuncion bilingual early-childhood through college-preparatory school option, U.S. and Paraguayan academic standards, and elementary/middle/high school programme anchor (claim-paraguay-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-693
- **Title**: Panama Ministry of Health (MINSA) - public website
- **URL**: https://www.minsa.gob.pa/
- **Archive**: stable ministry website - direct HTML extraction used
- **Type**: official-primary
- **Date published**: current public website, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Panama
- **Facts supporting**: official public-health authority baseline and MINSA clinic/public-system context for Panama healthcare screening (claim-panama-016)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-18

## src-694
- **Title**: ExpatLife.AI - Panama Healthcare 2026: insurance and hospitals guide
- **URL**: https://expatlife.ai/panama/healthcare
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: data verified 2026-06-18 on page
- **Date accessed**: 2026-06-18
- **Used by**: Panama
- **Facts supporting**: Panama private healthcare system, Panama City hospital baseline, local/international insurance cost proxies, private GP proxy, CSS/public eligibility caveat, Boquete/David healthcare escalation baseline, and remote-worker insurance reminder (claim-panama-016, claim-panama-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-695
- **Title**: ExpatLife.AI - Schools in Panama 2026: fees guide
- **URL**: https://expatlife.ai/panama/education
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: data verified 2026-06-18 on page
- **Date accessed**: 2026-06-18
- **Used by**: Panama
- **Facts supporting**: Panama public-school language/enrollment baseline, bilingual and international-school cost proxies, Panama City international-school ecosystem, and expat-child enrollment documents (claim-panama-018, claim-panama-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-696
- **Title**: International School of Panama - public website
- **URL**: https://www.isp.edu.pa/
- **Archive**: direct HTML extraction used from public school page
- **Type**: commercial
- **Date published**: current public pages, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Panama
- **Facts supporting**: flagship international K-12 school option, admissions/placement/tuition-fees/legal-requirements page availability, and international-student practical anchor (claim-panama-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18


## src-697
- **Title**: North Macedonia Ministry of Health - public website
- **URL**: https://zdravstvo.gov.mk/
- **Archive**: stable ministry website - direct HTML extraction used
- **Type**: official-primary
- **Date published**: current public website, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: North Macedonia
- **Facts supporting**: official public-health authority anchor and public-system context for North Macedonia healthcare screening (claim-north-macedonia-016)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-18

## src-698
- **Title**: ExpatLife.AI - North Macedonia Healthcare 2026: insurance and hospitals guide
- **URL**: https://expatlife.ai/north-macedonia/healthcare
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: data verified 2026-06-15 on page
- **Date accessed**: 2026-06-18
- **Used by**: North Macedonia
- **Facts supporting**: FZO/public-healthcare baseline, private GP and specialist cost proxies, private/international insurance proxy, Skopje private-hospital examples, and healthcare application-prep gaps (claim-north-macedonia-016, claim-north-macedonia-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-699
- **Title**: ExpatLife.AI - Schools in North Macedonia 2026: fees guide
- **URL**: https://expatlife.ai/north-macedonia/education
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: data verified 2026-06-15 on page
- **Date accessed**: 2026-06-18
- **Used by**: North Macedonia
- **Facts supporting**: public school age/language baseline, Skopje international-school ecosystem, international-school tuition proxy of EUR 4,000-8,000/year, and public-university fee context (claim-north-macedonia-018)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-700
- **Title**: QSI International School of Skopje and NOVA International School Skopje - public websites
- **URL**: https://qsi.org/skopje/ ; https://nova.edu.mk/
- **Archive**: direct HTML extraction used from public school pages
- **Type**: commercial
- **Date published**: current public pages, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: North Macedonia
- **Facts supporting**: Skopje English/international-school anchors, including QSI preschool/elementary/middle/secondary and NOVA early-education/elementary/secondary programme and support-service availability (claim-north-macedonia-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-701
- **Title**: Trade.gov — Bosnia and Herzegovina: Medical Equipment
- **URL**: https://www.trade.gov/country-commercial-guides/bosnia-and-herzegovina-medical-equipment
- **Archive**: direct HTML extraction used from public U.S. government page
- **Type**: reputable-secondary
- **Date published**: 2026-02-04
- **Date accessed**: 2026-06-18
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Bosnia and Herzegovina public/private healthcare-system overview, entity/cantonal health-insurance fund structure, payroll-contribution funding, public clinical-center locations, and private-hospital/private-practice baseline (claim-bosnia-herzegovina-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-02-04

## src-702
- **Title**: Federation of Bosnia and Herzegovina Ministry of Health / Republika Srpska Ministry of Health and Social Welfare public websites
- **URL**: https://fmoh.gov.ba/ ; https://www.vladars.rs/eng/vlada/ministries/MHSW/Pages/default.aspx
- **Archive**: direct HTML extraction used from public ministry websites
- **Type**: official-primary
- **Date published**: current public websites, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: public health-authority anchors for FBiH / Republika Srpska healthcare-system and onboarding follow-up
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-18

## src-703
- **Title**: Eurydice — Bosnia and Herzegovina education system overview / organisation and structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/bosnia-and-herzegovina/overview ; https://eurydice.eacea.ec.europa.eu/national-education-systems/bosnia-and-herzegovina/organisation-education-system-and-its-structure
- **Archive**: direct HTML extraction used from public EU/EACEA pages
- **Type**: official-secondary
- **Date published**: overview updated 2026-05-28; organisation page updated 2023-11-27
- **Date accessed**: 2026-06-18
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: decentralized education governance, preschool/primary/secondary structure, compulsory pre-primary year, nine-year compulsory primary education, free public primary schooling, and secondary-school baseline (claim-bosnia-herzegovina-019)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-05-28

## src-704
- **Title**: QSI International School of Sarajevo and UWC Mostar public websites
- **URL**: https://qsi.org/sarajevo/ ; https://www.uwcmostar.ba/
- **Archive**: direct HTML extraction used from public school websites
- **Type**: commercial
- **Date published**: current public pages, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Sarajevo international-school anchor, QSI preschool/elementary/middle/secondary/AP/support baseline, and UWC Mostar older-student IB/residential international-school anchor (claim-bosnia-herzegovina-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-705
- **Title**: Moldova Ministry of Health public website
- **URL**: https://ms.gov.md/en/
- **Archive**: stable gov domain - snapshot not required
- **Type**: official-primary
- **Date published**: current public website, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Moldova
- **Facts supporting**: official public-health authority anchor for Moldova healthcare screening and CNAM/public-insurance follow-up (claim-moldova-016)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-18

## src-706
- **Title**: ExpatLife.AI - Moldova Healthcare 2026: insurance and hospitals guide
- **URL**: https://expatlife.ai/moldova/healthcare
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: data verified 2026-06-15 on page
- **Date accessed**: 2026-06-18
- **Used by**: Moldova
- **Facts supporting**: public/private healthcare baseline, Chisinau tertiary-care concentration, private-insurance proxy, emergency-care proxy, and healthcare application-prep gaps (claim-moldova-016, claim-moldova-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18

## src-707
- **Title**: Eurydice - Moldova organisation of the education system and its structure
- **URL**: https://eurydice.eacea.ec.europa.eu/national-education-systems/moldova/organisation-education-system-and-its-structure
- **Archive**: direct HTML extraction used from public EU/EACEA page
- **Type**: official-secondary
- **Date published**: current public page, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Moldova
- **Facts supporting**: Moldova education levels, preschool/primary/secondary structure, and compulsory education through age 16 (claim-moldova-018)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-18

## src-708
- **Title**: ExpatLife.AI Moldova education 2026 guide plus QSI / Heritage public school websites
- **URL**: https://expatlife.ai/moldova/education ; https://qsi.org/chisinau/ ; https://heritage.md/
- **Archive**: direct HTML extraction used from public guide and school pages
- **Type**: aggregator
- **Date published**: ExpatLife data verified 2026-06-15; school pages current public pages, no single publication date captured
- **Date accessed**: 2026-06-18
- **Used by**: Moldova
- **Facts supporting**: Chisinau international-school anchors, QSI preschool-through-secondary baseline, Heritage all-through international-school baseline, tuition and private-kindergarten screening proxies, and education application-prep gaps (claim-moldova-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-18


## src-709
- **Title**: Trade.gov - Mexico Healthcare Products & Services
- **URL**: https://www.trade.gov/country-commercial-guides/mexico-healthcare-products-services
- **Archive**: direct HTML extraction used from public U.S. government page
- **Type**: reputable-secondary
- **Date published**: 2026-02-12
- **Date accessed**: 2026-06-19
- **Used by**: Mexico
- **Facts supporting**: Mexico mixed public/private healthcare-system baseline, public institutions including IMSS/ISSSTE/IMSS-Bienestar, urban private-sector expansion, and healthcare provider-screening caveats (claim-mexico-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-02-12

## src-710
- **Title**: Mexico Secretariat of Health and IMSS public websites
- **URL**: https://www.gob.mx/salud ; https://www.imss.gob.mx/
- **Archive**: stable gov domains - snapshot not required
- **Type**: official-primary
- **Date published**: current public websites, no single publication date captured
- **Date accessed**: 2026-06-19
- **Used by**: Mexico
- **Facts supporting**: federal public-health authority anchor, IMSS public-insurance/service anchor, and onboarding follow-up for temporary/permanent/self-employed residents (claim-mexico-017)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-19

## src-711
- **Title**: ExpatLife.AI Mexico healthcare and education 2026 guides plus ASF / ASFG public school websites
- **URL**: https://expatlife.ai/mexico/healthcare ; https://expatlife.ai/mexico/education ; https://www.asf.edu.mx/ ; https://www.asfg.mx/
- **Archive**: direct HTML extraction used from public guide and school pages
- **Type**: aggregator
- **Date published**: 2026 guide pages, exact page update date not captured
- **Date accessed**: 2026-06-19
- **Used by**: Mexico
- **Facts supporting**: private health-insurance and serious-care cost proxies, Mexico City private-hospital examples, public-school / bilingual-private / international-school screening baseline, ASF / ASFG school anchors, and healthcare/education application-prep gaps (claim-mexico-018, claim-mexico-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-19

## src-712
- **Title**: Mexico Secretariat of Public Education (SEP) public website and basic-education links
- **URL**: https://www.gob.mx/sep ; https://www.gob.mx/sep/acciones-y-programas/educacion-basica
- **Archive**: stable gov domains - snapshot not required
- **Type**: official-primary
- **Date published**: current public websites, no single publication date captured
- **Date accessed**: 2026-06-19
- **Used by**: Mexico
- **Facts supporting**: federal public-education authority anchor, SEP purpose statement, basic-education resource link, and public-school follow-up baseline (claim-mexico-019)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-19


## src-713
- **Title**: Argentina Ministry of Health public website
- **URL**: https://www.argentina.gob.ar/salud
- **Archive**: stable gov domain - snapshot not required
- **Type**: official-primary
- **Date published**: current public website, no single publication date captured
- **Date accessed**: 2026-06-19
- **Used by**: Argentina
- **Facts supporting**: official public-health authority anchor, national health programs/procedures, and public-hospital follow-up baseline for Argentina healthcare screening (claim-argentina-017)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-19

## src-714
- **Title**: ExpatLife.AI - Argentina Healthcare 2026: insurance and hospitals guide
- **URL**: https://expatlife.ai/argentina/healthcare
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: 2026 guide page, exact page update date not captured
- **Date accessed**: 2026-06-19
- **Used by**: Argentina
- **Facts supporting**: private prepaga insurance proxy, public-hospital access caveat, Buenos Aires private-hospital anchors, and healthcare application-prep gaps (claim-argentina-017, claim-argentina-018)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-19

## src-715
- **Title**: Argentina national education public website
- **URL**: https://www.argentina.gob.ar/educacion
- **Archive**: stable gov domain - snapshot not required
- **Type**: official-primary
- **Date published**: current public website, no single publication date captured
- **Date accessed**: 2026-06-19
- **Used by**: Argentina
- **Facts supporting**: official education authority anchor, basic-education / school-calendar / statistics resource baseline, and public-school follow-up context (claim-argentina-019)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-19

## src-716
- **Title**: ExpatLife.AI Argentina education 2026 guide plus Lincoln School public website
- **URL**: https://expatlife.ai/argentina/education ; https://www.lincoln.edu.ar/
- **Archive**: direct HTML extraction used from public guide and school page
- **Type**: aggregator
- **Date published**: 2026 guide page, exact page update date not captured; school site current public page
- **Date accessed**: 2026-06-19
- **Used by**: Argentina
- **Facts supporting**: public-school Spanish-language baseline, bilingual/private and top international-school cost proxies, Buenos Aires school anchors, Lincoln admissions/tuition-page anchor, and education application-prep gaps (claim-argentina-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-19


## src-717
- **Title**: Ministry of Health Malaysia public portal
- **URL**: https://www.moh.gov.my/
- **Archive**: stable gov domain - snapshot not required
- **Type**: official-primary
- **Date published**: current public website, no single publication date captured
- **Date accessed**: 2026-06-19
- **Used by**: Malaysia
- **Facts supporting**: official health-authority anchor, public hospital / appointment / health-service starting point, and healthcare follow-up baseline (claim-malaysia-018)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-19

## src-718
- **Title**: ExpatLife.AI - Malaysia Healthcare 2026: hospitals and insurance guide
- **URL**: https://expatlife.ai/malaysia/healthcare
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: 2026 guide page, data verified 2026-06-15 on page; exact page update date not captured
- **Date accessed**: 2026-06-19
- **Used by**: Malaysia
- **Facts supporting**: private-care system baseline, GP / specialist / hospital / dental price proxies, DE Rantau / MM2H insurance coverage proxy, international insurance monthly proxy, hospital anchors, and healthcare application-prep gaps (claim-malaysia-018, claim-malaysia-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-19

## src-719
- **Title**: Ministry of Education Malaysia public portal
- **URL**: https://www.moe.gov.my/en
- **Archive**: stable gov domain - snapshot not required
- **Type**: official-primary
- **Date published**: current public website, no single publication date captured
- **Date accessed**: 2026-06-19
- **Used by**: Malaysia
- **Facts supporting**: official education-authority anchor, preschool / primary / secondary / private-institution portal links, and education follow-up baseline (claim-malaysia-020)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-19

## src-720
- **Title**: ExpatLife.AI - Schools in Malaysia 2026: Expat Guide
- **URL**: https://expatlife.ai/malaysia/education
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: 2026 guide page, data verified 2026-06-15 on page; exact page update date not captured
- **Date accessed**: 2026-06-19
- **Used by**: Malaysia
- **Facts supporting**: public-school Bahasa Malaysia baseline, dependent-child school access proxy, international-school examples and tuition proxies, kindergarten fee proxies, waiting-list timing, and education application-prep gaps (claim-malaysia-020, claim-malaysia-021)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-19

## src-721
- **Title**: Thailand Ministry of Public Health official portal
- **URL**: https://www.moph.go.th/
- **Archive**: stable gov domain -- snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-19
- **Used by**: Thailand
- **Facts supporting**: official health authority anchor for Thailand healthcare section
- **Confidence ceiling**: high
- **Stale at**: 2026-12-19

## src-722
- **Title**: InternationalInsurance.com -- Healthcare in Thailand: How Expats and Visitors Can Access Care
- **URL**: https://www.internationalinsurance.com/countries/thailand/healthcare/
- **Archive**: [archive: failed 2026-06-19: Wayback save returned HTTP 429]
- **Type**: commercial
- **Date published**: 2021-11-15
- **Date accessed**: 2026-06-19
- **Used by**: Thailand
- **Facts supporting**: expat private-insurance baseline; private-hospital quality and Bangkok procedure-cost proxies (claim-thailand-017, claim-thailand-018)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-19

## src-723
- **Title**: Thailand Ministry of Education official portal
- **URL**: https://www.moe.go.th/
- **Archive**: stable gov domain -- snapshot not required
- **Type**: official-primary
- **Date published**: unknown
- **Date accessed**: 2026-06-19
- **Used by**: Thailand
- **Facts supporting**: official education authority anchor for Thailand education section
- **Confidence ceiling**: high
- **Stale at**: 2026-12-19

## src-724
- **Title**: Scholaro -- Education System in Thailand
- **URL**: https://www.scholaro.com/db/Countries/Thailand/Education-System
- **Archive**: [archive: failed 2026-06-19: Wayback save returned HTTP 429]
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-06-19
- **Used by**: Thailand
- **Facts supporting**: kindergarten, primary, middle, secondary/vocational structure and Thai-language public-school baseline (claim-thailand-019)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-19

## src-725
- **Title**: International Schools Database -- International Schools in Bangkok, Thailand
- **URL**: https://www.international-schools-database.com/in/bangkok
- **Archive**: [archive: failed 2026-06-19: Wayback save returned HTTP 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-19
- **Used by**: Thailand
- **Facts supporting**: Bangkok international-school count and 2026/2027 fee examples (claim-thailand-020)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-19

## src-726
- **Title**: International Schools Database -- International Schools in Chiang Mai and Phuket, Thailand
- **URL**: https://www.international-schools-database.com/in/chiang-mai ; https://www.international-schools-database.com/in/phuket
- **Archive**: [archive: failed 2026-06-19: Wayback save returned HTTP 429]
- **Type**: commercial
- **Date published**: unknown
- **Date accessed**: 2026-06-19
- **Used by**: Thailand
- **Facts supporting**: Chiang Mai and Phuket international-school counts and fee examples (claim-thailand-020)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-19

## src-727
- **Title**: Indonesia Ministry of Health official portal
- **URL**: https://kemkes.go.id/
- **Archive**: stable gov domain - direct HTML extraction used
- **Type**: official-primary
- **Date published**: current public website, no single publication date captured
- **Date accessed**: 2026-06-19
- **Used by**: Indonesia
- **Facts supporting**: official health authority anchor, public health-service and Ministry hospital starting point, and healthcare onboarding follow-up baseline (claim-indonesia-016)
- **Confidence ceiling**: medium-high
- **Stale at**: 2027-06-19

## src-728
- **Title**: ExpatLife.AI - Indonesia Healthcare 2026: insurance and hospitals guide
- **URL**: https://expatlife.ai/indonesia/healthcare
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: 2026 guide page, data verified 2026-06-15 on page; exact page update date not captured
- **Date accessed**: 2026-06-19
- **Used by**: Indonesia
- **Facts supporting**: Indonesia public/private healthcare screen, BPJS/Puskesmas baseline, expat insurance monthly proxy, private GP / BIMC / evacuation cost proxies, insurer names, and healthcare application-prep gaps (claim-indonesia-016, claim-indonesia-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-19

## src-729
- **Title**: Indonesia.go.id education category / government information portal
- **URL**: https://indonesia.go.id/kategori/pendidikan
- **Archive**: stable gov domain - direct HTML extraction used
- **Type**: official-primary
- **Date published**: current public portal category, no single publication date captured
- **Date accessed**: 2026-06-19
- **Used by**: Indonesia
- **Facts supporting**: minimal official education-sector portal anchor and Ministry-page capture gap for Indonesia education screening (claim-indonesia-018)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-19

## src-730
- **Title**: ExpatLife.AI - Schools in Indonesia 2026: fees and expat guide
- **URL**: https://expatlife.ai/indonesia/education
- **Archive**: direct HTML extraction used from public guide
- **Type**: aggregator
- **Date published**: 2026 guide page, data verified 2026-06-15 on page; exact page update date not captured
- **Date accessed**: 2026-06-19
- **Used by**: Indonesia
- **Facts supporting**: local/private school baseline, Bahasa Indonesia integration caveat, international-school cost bands, Jakarta/Bali school anchors, homeschooling note, and education application-prep gaps (claim-indonesia-018)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-19

## src-731
- **Title**: International Schools Database - International Schools in Jakarta and Bali, Indonesia
- **URL**: https://www.international-schools-database.com/in/jakarta ; https://www.international-schools-database.com/in/bali
- **Archive**: direct HTML extraction used from public school-list pages
- **Type**: commercial
- **Date published**: current public pages, no single publication date captured; fee rows include 2025/2026 and 2026/2027 labels
- **Date accessed**: 2026-06-19
- **Used by**: Indonesia
- **Facts supporting**: Jakarta and Bali international-school counts, English-language availability, and selected annual-fee examples for education screening (claim-indonesia-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-19


## src-732
- **Title**: eGov Kazakhstan — Mandatory Social Health Insurance (MSHI)
- **URL**: https://egov.kz/cms/en/articles/health_care/osms
- **Archive**: direct HTML extraction used from eGov public page
- **Type**: official-primary
- **Date published**: last update 2025-08-22 on page
- **Date accessed**: 2026-06-20
- **Used by**: Kazakhstan
- **Facts supporting**: MSHI/SFMA eligibility baseline for citizens, candas, refugees, permanent-resident foreigners with residence permits, and temporarily staying foreigners' limited free-care rights for dangerous diseases (claim-kazakhstan-016)
- **Confidence ceiling**: high
- **Stale at**: 2027-08-22

## src-733
- **Title**: Numbeo — Health Care in Kazakhstan
- **URL**: https://www.numbeo.com/health-care/country_result.jsp?country=Kazakhstan
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: aggregator
- **Date published**: current crowd-sourced survey page, no single publication date captured
- **Date accessed**: 2026-06-20
- **Used by**: Kazakhstan
- **Facts supporting**: Kazakhstan private/public health-care quality proxy, overall health-care index, public/private waiting and equipment satisfaction comparison for healthcare screening (claim-kazakhstan-017)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-20

## src-734
- **Title**: Scholaro — Education System in Kazakhstan
- **URL**: https://www.scholaro.com/db/Countries/Kazakhstan/Education-System
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: aggregator
- **Date published**: no page date captured
- **Date accessed**: 2026-06-20
- **Used by**: Kazakhstan
- **Facts supporting**: mandatory-schooling baseline, primary/lower-secondary structure, Ministry-prescribed curriculum, and Kazakh/Russian public-school language baseline (claim-kazakhstan-018)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-20

## src-735
- **Title**: International Schools Database — International Schools in Kazakhstan, Almaty, and Astana
- **URL**: https://www.international-schools-database.com/country/kazakhstan ; https://www.international-schools-database.com/in/almaty ; https://www.international-schools-database.com/in/astana
- **Archive**: direct HTML extraction used from public school-list pages
- **Type**: commercial
- **Date published**: current public pages, no single publication date captured; fee rows include 2024/2025 and 2025/2026 labels
- **Date accessed**: 2026-06-20
- **Used by**: Kazakhstan
- **Facts supporting**: Kazakhstan international-school count, Almaty/Astana school supply, English/IB/British/American/French curriculum examples, ages, and selected annual-fee examples (claim-kazakhstan-019)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-20

## src-736
- **Title**: Numbeo - Health Care in Armenia
- **URL**: https://www.numbeo.com/health-care/country_result.jsp?country=Armenia
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: aggregator
- **Date published**: current crowd-sourced survey page, no single publication date captured
- **Date accessed**: 2026-06-20
- **Used by**: Armenia
- **Facts supporting**: Armenia private/public healthcare quality proxy and healthcare screening baseline; used with Livingcost doctor-visit proxies to frame private-care budgeting (claim-armenia-015, claim-armenia-016)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-20

## src-737
- **Title**: Scholaro - Education System in Armenia
- **URL**: https://www.scholaro.com/db/Countries/Armenia/Education-System
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: aggregator
- **Date published**: no page date captured
- **Date accessed**: 2026-06-20
- **Used by**: Armenia
- **Facts supporting**: Armenia education-system structure: preschool, primary education, grades 4-9 middle education, secondary schooling, and public-school language/integration planning baseline (claim-armenia-017)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-20

## src-738
- **Title**: QSI International School of Yerevan - school profile
- **URL**: https://www.qsi.org/yerevan/
- **Archive**: direct HTML extraction used from public school page
- **Type**: commercial
- **Date published**: current public school page, no single publication date captured
- **Date accessed**: 2026-06-20
- **Used by**: Armenia
- **Facts supporting**: QSI Yerevan as a captured English/international-school anchor with preschool, elementary, middle, secondary, AP, intensive English, and student-support services (claim-armenia-018)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-20

## src-739
- **Title**: UWC Dilijan - Fees
- **URL**: https://www.uwcdilijan.org/admissions/fees
- **Archive**: direct HTML extraction used from public fee page
- **Type**: commercial
- **Date published**: 2026/27 academic-year fee page, no separate publication date captured
- **Date accessed**: 2026-06-20
- **Used by**: Armenia
- **Facts supporting**: UWC Dilijan fee baseline: USD 88,000 for the two-year IBDP from 2026/27, included items, excluded travel/pocket-money/holiday costs, and USD 300 deposit (claim-armenia-018)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-20


## src-740
- **Title**: Numbeo - Health Care in United Arab Emirates
- **URL**: https://www.numbeo.com/health-care/country_result.jsp?country=United+Arab+Emirates
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: aggregator
- **Date published**: current crowd-sourced survey page, no single publication date captured
- **Date accessed**: 2026-06-20
- **Used by**: UAE
- **Facts supporting**: UAE healthcare system index and private/public healthcare quality proxy; used with Livingcost doctor-visit proxies for the screening baseline (claim-uae-014)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-20

## src-741
- **Title**: Policybazaar UAE - Health Insurance in Dubai & UAE
- **URL**: https://www.policybazaar.ae/health-insurance/
- **Archive**: direct HTML extraction used from public commercial page
- **Type**: commercial
- **Date published**: 2026-06-17 page update shown in extracted text
- **Date accessed**: 2026-06-20
- **Used by**: UAE
- **Facts supporting**: UAE resident health-insurance mandatory baseline, broad basic-to-comprehensive premium proxy, and maternity/emergency coverage caveat (claim-uae-015)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-20

## src-742
- **Title**: Scholaro - Education System in the United Arab Emirates
- **URL**: https://www.scholaro.com/db/Countries/United-Arab-Emirates/Education-System
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: aggregator
- **Date published**: no page date captured
- **Date accessed**: 2026-06-20
- **Used by**: UAE
- **Facts supporting**: UAE public-school structure baseline, compulsory primary/preparatory years, and public-school integration planning caveat (claim-uae-016)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-20

## src-743
- **Title**: International Schools Database - Dubai-Sharjah-Ajman and Abu Dhabi
- **URL**: https://www.international-schools-database.com/in/dubai ; https://www.international-schools-database.com/in/abu-dhabi
- **Archive**: direct HTML extraction used from public school-list pages
- **Type**: commercial
- **Date published**: current public pages, no single publication date captured; extracted fee rows include 2025/2026 and 2026/2027 labels
- **Date accessed**: 2026-06-20
- **Used by**: UAE
- **Facts supporting**: international-school supply in Dubai-Sharjah-Ajman and Abu Dhabi, English-language availability, and selected fee-range examples; used with Livingcost childcare/school proxies (claim-uae-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-20


## src-744
- **Title**: QSI International School of Montenegro - School Information Packet 2025-2026
- **URL**: https://resources.finalsite.net/images/v1759316931/qsiorg/qxrtasif0flf67yw3ebj/QSIMontenegroInfoPacket2025-26.pdf
- **Archive**: direct PDF extraction used from public QSI resource
- **Type**: commercial
- **Date published**: 2025-2026 school-year packet, no separate publication date captured
- **Date accessed**: 2026-06-20
- **Used by**: Montenegro
- **Facts supporting**: QSI Montenegro 2025-26 registration fee, capital-fund fee, annual tuition for the 5-year-old through secondary programme, 3-4-year-old class fee, and late-enrollment fee; used for the international-school budget stress test (claim-montenegro-026)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-20

## src-745
- **Title**: World Population Review — Safest Countries in the World 2026
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: unknown
- **Date accessed**: 2026-06-20
- **Used by**: Spain
- **Facts supporting**: Spain comfort / safety screening proxy: 2025 Global Peace Index score, TravelSafe safety index, and US News safest-country rank (claim-spain-016)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-20

## src-746
- **Title**: EF English Proficiency Index — Spain
- **URL**: https://www.ef.com/wwen/epi/regions/europe/spain/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-20
- **Used by**: Spain
- **Facts supporting**: Spain English-proficiency baseline: global rank #36, EF EPI score 540, moderate proficiency band (claim-spain-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-20


## src-747
- **Title**: World Population Review - Safest Countries in the World 2026
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: 2026-06-16T17:05:34.452Z shown in page metadata
- **Date accessed**: 2026-06-20
- **Used by**: Italy
- **Facts supporting**: Italy comfort / safety screening proxy: 2025 Global Peace Index score, TravelSafe safety index / risk label, and US News safest-country rank (claim-italy-016)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-20

## src-748
- **Title**: EF English Proficiency Index - Italy
- **URL**: https://www.ef.com/wwen/epi/regions/europe/italy/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-20
- **Used by**: Italy
- **Facts supporting**: Italy English-proficiency baseline: global rank #59, EF EPI score 513, and language-integration friction for relocation planning (claim-italy-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-20


## src-749
- **Title**: World Population Review - Safest Countries in the World 2026
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: 2026-06-16T17:05:34.452Z shown in page metadata
- **Date accessed**: 2026-06-20
- **Used by**: Greece
- **Facts supporting**: Greece comfort / safety screening proxy: 2025 Global Peace Index score, TravelSafe safety index / risk label, and US News safest-country rank (claim-greece-016)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-20

## src-750
- **Title**: EF English Proficiency Index - Greece
- **URL**: https://www.ef.com/wwen/epi/regions/europe/greece/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-20
- **Used by**: Greece
- **Facts supporting**: Greece English-proficiency baseline: global rank #20, EF EPI score 592, Athens 616, Thessaloniki 611, and language-integration friction for relocation planning (claim-greece-016)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-20

## src-751
- **Title**: World Population Review - Safest Countries in the World 2026
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: 2026-06-16T17:05:34.452Z shown in page metadata
- **Date accessed**: 2026-06-21
- **Used by**: Cyprus
- **Facts supporting**: Cyprus comfort / safety screening proxy: 2025 Global Peace Index score, TravelSafe safety index / risk label, and US News safest-country rank (claim-cyprus-016)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-752
- **Title**: EF English Proficiency Index - Cyprus
- **URL**: https://www.ef.com/wwen/epi/regions/europe/cyprus/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-21
- **Used by**: Cyprus
- **Facts supporting**: Cyprus English-proficiency baseline: global rank #40, EF EPI score 537, Limassol/Paphos/Nicosia city and regional scores, and Greek-language integration caveat (claim-cyprus-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-753
- **Title**: World Population Review - Safest Countries in the World 2026; Numbeo - Crime in Croatia
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.numbeo.com/crime/country_result.jsp?country=Croatia
- **Archive**: [archive: failed 2026-06-21]
- **Type**: aggregator
- **Date published**: WPR page metadata 2026-06-16T17:05:34.452Z; Numbeo last update 2026-06-04
- **Date accessed**: 2026-06-21
- **Used by**: Croatia
- **Facts supporting**: Croatia comfort / safety screening proxy: 2025 Global Peace Index score, TravelSafe safety index / low-risk label, US News safest-country rank, Numbeo crime index, safety index, and walking-alone perception data (claim-croatia-016)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-754
- **Title**: EF English Proficiency Index - Croatia
- **URL**: https://www.ef.com/wwen/epi/regions/europe/croatia/
- **Archive**: [archive: failed 2026-06-21]
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-21
- **Used by**: Croatia
- **Facts supporting**: Croatia English-proficiency baseline: global rank #2, EF EPI score 617, global average score 488, and Croatian-language integration caveat for bureaucracy / public services (claim-croatia-017)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-755
- **Title**: World Population Review / Numbeo safety proxies for Malta
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.numbeo.com/crime/country_result.jsp?country=Malta
- **Archive**: WPR direct extraction used; Numbeo direct extraction used
- **Type**: aggregator
- **Date published**: WPR article 2026-06-16; Numbeo live page
- **Date accessed**: 2026-06-21
- **Used by**: Malta
- **Facts supporting**: Malta safety screening baseline: TravelSafe safety index 78 / Low risk and Numbeo crime index 43.02 / safety index 56.98 (claim-malta-016)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-21

## src-756
- **Title**: World Population Review / TravelSafe safety proxies for Czechia
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: WPR article 2026-06-16
- **Date accessed**: 2026-06-21
- **Used by**: Czech Republic
- **Facts supporting**: Czechia safety screening baseline: 2025 Global Peace Index score 1.435, TravelSafe safety index 88 / Low risk, and US News 2024 safest-country rank #27 (claim-czech-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-757
- **Title**: EF English Proficiency Index - Czechia
- **URL**: https://www.ef.com/wwen/epi/regions/europe/czech-republic/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-21
- **Used by**: Czech Republic
- **Facts supporting**: Czechia English-proficiency baseline: global rank #23, EF EPI score 582, high proficiency band, Brno score 620, and Prague score 576 (claim-czech-021)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21


## src-758
- **Title**: World Population Review / TravelSafe safety proxies for Poland
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: WPR article 2026-06-16
- **Date accessed**: 2026-06-21
- **Used by**: Poland
- **Facts supporting**: Poland comfort / safety screening proxy: 2025 Global Peace Index score 1.713, TravelSafe safety index 84 / Low risk, and US News 2024 safest-country rank #22 (claim-poland-026)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-759
- **Title**: EF English Proficiency Index - Poland
- **URL**: https://www.ef.com/wwen/epi/regions/europe/poland/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-21
- **Used by**: Poland
- **Facts supporting**: Poland section 5.8 English-proficiency baseline: global rank #15, EF EPI score 600, high proficiency band, and city snippets for Krakow 605, Wroclaw 599, and Warsaw 591
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-760
- **Title**: World Population Review / TravelSafe safety proxies for Romania
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: WPR article 2026-06-16
- **Date accessed**: 2026-06-21
- **Used by**: Romania
- **Facts supporting**: Romania comfort / safety screening proxy: 2025 Global Peace Index score 1.721, TravelSafe safety index 80 / Low risk, and US News 2024 safest-country rank #40 (claim-romania-025)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-761
- **Title**: EF English Proficiency Index - Romania
- **URL**: https://www.ef.com/wwen/epi/regions/europe/romania/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-21
- **Used by**: Romania
- **Facts supporting**: Romania section 5.8 English-proficiency baseline: global rank #11, EF EPI score 605, high proficiency band, and city snippets for Bucharest 608, Cluj-Napoca 597, and Timisoara 593 (claim-romania-026)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21


## src-762
- **Title**: World Population Review / TravelSafe safety proxies for Bulgaria
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: WPR article 2026-06-16
- **Date accessed**: 2026-06-21
- **Used by**: Bulgaria
- **Facts supporting**: Bulgaria comfort / safety screening proxy: 2025 Global Peace Index score 1.610, TravelSafe safety index 80 / Low risk, and US News 2024 safest-country rank #37 (claim-bulgaria-026)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-763
- **Title**: EF English Proficiency Index - Bulgaria
- **URL**: https://www.ef.com/wwen/epi/regions/europe/bulgaria/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-21
- **Used by**: Bulgaria
- **Facts supporting**: Bulgaria section 5.8 English-proficiency baseline: global rank #18, EF EPI score 594, high proficiency band implied by score display, and city snippets for Sofia 616 and Varna 553 (claim-bulgaria-027)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21


## src-764
- **Title**: World Population Review / TravelSafe safety proxies for Hungary
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: WPR article 2026-06-16
- **Date accessed**: 2026-06-21
- **Used by**: Hungary
- **Facts supporting**: Hungary comfort / safety screening proxy: 2025 Global Peace Index score 1.500, TravelSafe safety index 83 / Low risk, and US News 2024 safest-country rank #26 (claim-hungary-025)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-765
- **Title**: EF English Proficiency Index - Hungary
- **URL**: https://www.ef.com/wwen/epi/regions/europe/hungary/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-21
- **Used by**: Hungary
- **Facts supporting**: Hungary section 5.8 English-proficiency baseline: global rank #22, EF EPI score 590, and Budapest city score 613 (claim-hungary-026)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-21

## src-766
- **Title**: World Population Review / TravelSafe safety proxies for Slovakia
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: WPR article 2026-06-16
- **Date accessed**: 2026-06-22
- **Used by**: Slovakia
- **Facts supporting**: Slovakia comfort / safety screening proxy: 2025 Global Peace Index score 1.609, TravelSafe safety index 80 / Low risk, and US News 2024 safest-country rank #34 (claim-slovakia-024)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-22

## src-767
- **Title**: EF English Proficiency Index - Slovakia
- **URL**: https://www.ef.com/wwen/epi/regions/europe/slovakia/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-22
- **Used by**: Slovakia
- **Facts supporting**: Slovakia section 5.8 English-proficiency baseline: global rank #10, EF EPI score 606, and regional/city scores for Kosice 605, Trnava 604, Presov 601, Bratislava 600, Nitra 600, Zilina 592, and Banska Bystrica 578 (claim-slovakia-025)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-22


## src-768
- **Title**: World Population Review / TravelSafe safety proxies for Slovenia
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: direct HTML / embedded-data extraction used; archive not captured
- **Type**: aggregator
- **Date published**: WPR article 2026-06-16
- **Date accessed**: 2026-06-22
- **Used by**: Slovenia
- **Facts supporting**: Slovenia comfort / safety screening proxy: 2025 Global Peace Index score 1.409, TravelSafe safety index 87 / Low risk, and US News 2024 safest-country rank #32 (claim-slovenia-023)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-22

## src-769
- **Title**: World Population Review / TravelSafe safety proxies for Montenegro
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/montenegro/
- **Archive**: direct HTML / text-mirror extraction used; archive not captured
- **Type**: aggregator
- **Date published**: WPR article 2026-06-16; TravelSafe page accessed current
- **Date accessed**: 2026-06-22
- **Used by**: Montenegro
- **Facts supporting**: Montenegro comfort / safety screening proxy: 2025 Global Peace Index score 1.685, TravelSafe safety index 70 / Low risk, low overall risk, and medium transport/pickpocket/scam caveats (claim-montenegro-027)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-22

## src-770
- **Title**: Expat Arrivals — Moving to and living in Montenegro
- **URL**: https://www.expatarrivals.com/europe/montenegro/moving-montenegro
- **Archive**: stable page via Jina text mirror — direct extraction used
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-22
- **Used by**: Montenegro
- **Facts supporting**: Montenegro comfort / adaptation baseline: small expat community mostly in Podgorica, younger people often speak foreign languages, basic Serbian/Montenegrin recommended, low cost relative to Western Europe, Podgorica international-school concentration, private healthcare caveat, and low-crime practical baseline (claim-montenegro-027, claim-montenegro-028)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-22

## src-771
- **Title**: World Population Review / TravelSafe Serbia safety proxies
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/serbia/
- **Archive**: stable pages via Jina text mirror — direct extraction used
- **Type**: commercial
- **Date published**: WPR 2026 table current; TravelSafe published 2026-06-11
- **Date accessed**: 2026-06-22
- **Used by**: Serbia
- **Facts supporting**: Serbia comfort / safety screening proxy: 2025 Global Peace Index score 1.914, Global Terrorism Index 0.582, safety index 77, medium risk band, US News safest-country rank 66th, TravelSafe safety index 77 / medium overall risk, and transport / pickpocket / scam caveats (claim-serbia-024)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-22

## src-772
- **Title**: EF English Proficiency Index Serbia / Expat Arrivals moving-to-Serbia adaptation overview
- **URL**: https://www.ef.com/wwen/epi/regions/europe/serbia/ ; https://www.expatarrivals.com/europe/serbia/moving-serbia
- **Archive**: stable pages via Jina text mirror — direct extraction used
- **Type**: reputable-secondary
- **Date published**: EF 2025 index; Expat Arrivals current page, no explicit page date shown
- **Date accessed**: 2026-06-22
- **Used by**: Serbia
- **Facts supporting**: Serbia English-proficiency / language-adaptation baseline: EF EPI score 578, global rank #25, regional and city scores, English as widely spoken second language, and Serbian / Cyrillic usefulness for everyday activities (claim-serbia-024)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-22


## src-773
- **Title**: World Population Review / TravelSafe Turkey safety proxies
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/turkey/
- **Archive**: stable pages via direct HTML / Jina text-mirror extraction; archive not captured
- **Type**: commercial
- **Date published**: WPR 2026 table current; TravelSafe published 2025-08-27
- **Date accessed**: 2026-06-23
- **Used by**: Turkey
- **Facts supporting**: Turkey comfort / safety screening proxy: 2025 Global Peace Index score 2.852, Global Terrorism Index 3.968, TravelSafe safety index 45 / Medium risk, US News safest-country rank #43, 112 emergency number, Istanbul/main tourist corridors safer than Syria/Iraq/Iran border areas, and earthquake / transport / scam caveats (claim-turkey-023)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-23

## src-774
- **Title**: EF English Proficiency Index Turkey / Expat Arrivals moving-to-Turkey adaptation overview
- **URL**: https://www.ef.com/wwen/epi/regions/europe/turkey/ ; https://www.expatarrivals.com/europe/turkey/moving-turkey
- **Archive**: stable pages via Jina text mirror / direct extraction; archive not captured
- **Type**: reputable-secondary
- **Date published**: EF page published 2026-06-16; Expat Arrivals current page, no explicit page date shown
- **Date accessed**: 2026-06-23
- **Used by**: Turkey
- **Facts supporting**: Turkey English-proficiency / adaptation baseline: EF EPI global rank #71, score 488, city scores Izmir 515, Antalya 510, Ankara 508, Istanbul 504; Expat Arrivals notes residence-closed neighborhoods, landlord upfront-rent demands, foreign-currency affordability with dollar inflation, private healthcare / insurance need, Turkish-language school barrier, and remote-worker / DN practicality (claim-turkey-023, claim-turkey-024)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-23

## src-775
- **Title**: World Population Review / TravelSafe Georgia safety proxies
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/georgia/
- **Archive**: stable pages via direct HTML extraction; archive not captured
- **Type**: commercial
- **Date published**: WPR 2026 table current; TravelSafe updated 2025-12-13
- **Date accessed**: 2026-06-23
- **Used by**: Georgia
- **Facts supporting**: Georgia comfort / safety screening proxy: 2025 Global Peace Index score 2.185, TravelSafe safety index 63, low risk labels, Tbilisi/Batumi generally safe, Abkhazia and South Ossetia avoidance, and transport/road/night caution (claim-georgia-021)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-23

## src-776
- **Title**: EF English Proficiency Index Georgia
- **URL**: https://www.ef.com/wwen/epi/regions/europe/georgia/
- **Archive**: direct HTML extraction used; archive not captured
- **Type**: reputable-secondary
- **Date published**: 2025-11-01
- **Date accessed**: 2026-06-23
- **Used by**: Georgia
- **Facts supporting**: Georgia section 5.8 English-proficiency baseline: global rank #35, EF EPI score 541, Tbilisi score 550, and Batumi score 544 (claim-georgia-021)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-23


## src-777
- **Title**: World Population Review / TravelSafe Albania safety proxies
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/albania/
- **Archive**: stable pages via direct HTML extraction; archive not captured
- **Type**: commercial
- **Date published**: WPR 2026 table current; TravelSafe updated 2025-12-25
- **Date accessed**: 2026-06-23
- **Used by**: Albania
- **Facts supporting**: Albania comfort / safety screening proxy: 2025 Global Peace Index score 1.812, TravelSafe safety index 75 / Low risk, low overall / transport / pickpocket / mugging / terrorism / women-traveler risks, medium scam and natural-disaster caveats, and public-transport / road caution (claim-albania-021)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-23

## src-778
- **Title**: EF English Proficiency Index Albania / Expat Arrivals moving-to-Albania adaptation overview
- **URL**: https://www.ef.com/wwen/epi/regions/europe/albania/ ; https://www.expatarrivals.com/europe/albania/moving-albania
- **Archive**: stable pages via direct HTML / Jina text-mirror extraction; archive not captured
- **Type**: reputable-secondary
- **Date published**: EF 2025 index; Expat Arrivals current page, no explicit page date shown
- **Date accessed**: 2026-06-23
- **Used by**: Albania
- **Facts supporting**: Albania English-proficiency / adaptation baseline: EF EPI global rank #42, score 532, Tirana score 557; Expat Arrivals notes Albania is not a major expat hotspot, has lower living costs, cheap housing, unreliable public transport / road caveats, private healthcare / international-school cost pressure, and Albanian-language schooling (claim-albania-021, claim-albania-022)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-23

## src-779
- **Title**: World Population Review / TravelSafe Uruguay safety proxies
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/uruguay/
- **Archive**: stable pages via direct HTML extraction; archive not captured
- **Type**: commercial
- **Date published**: WPR 2026 table current; TravelSafe 2026 safety-rating page current
- **Date accessed**: 2026-06-23
- **Used by**: Uruguay
- **Facts supporting**: Uruguay comfort / safety screening proxy: 2025 Global Peace Index score 1.784, 2025 Global Terrorism Index 0.059, TravelSafe safety index 77 / Low risk, US News safest-country rank #56, overall/transport/terrorism/women-traveler low-risk labels, and pickpocket/scam/natural-disaster/mugging medium-risk caveats (claim-uruguay-020)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-23

## src-780
- **Title**: EF English Proficiency Index Uruguay / Expat Arrivals moving-to-Uruguay adaptation overview
- **URL**: https://www.ef.com/wwen/epi/regions/latin-america/uruguay/ ; https://www.expatarrivals.com/americas/uruguay/moving-uruguay
- **Archive**: stable pages via direct HTML / Jina text-mirror extraction; archive not captured
- **Type**: reputable-secondary
- **Date published**: EF 2025 index; Expat Arrivals current page, no explicit page date shown
- **Date accessed**: 2026-06-23
- **Used by**: Uruguay
- **Facts supporting**: Uruguay English-proficiency / adaptation baseline: EF EPI global rank #34, score 542, Montevideo score 544; Spanish-language integration caveat, English not fluent everywhere, Montevideo street-crime caution, accessible public transport, high-standard healthcare, mutualista route, public Spanish-language education, international-school concentration in Montevideo, and rising cost/accommodation caveats (claim-uruguay-021)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-23

## src-781
- **Title**: World Population Review / TravelSafe Paraguay safety proxies
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/paraguay/
- **Archive**: stable pages via direct HTML extraction; archive not captured
- **Type**: commercial
- **Date published**: WPR 2026 table current; TravelSafe updated 2025-12-10
- **Date accessed**: 2026-06-23
- **Used by**: Paraguay
- **Facts supporting**: Paraguay comfort / safety screening proxy: 2025 Global Peace Index score 1.981, 2025 Global Terrorism Index 0.073, TravelSafe-derived index 45 / Medium, TravelSafe low overall risk, and medium transport / pickpocket / mugging / scam / women-traveler / tap-water caveats (claim-paraguay-020)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-23

## src-782
- **Title**: EF English Proficiency Index Paraguay / Expat Arrivals moving-to-Paraguay adaptation overview
- **URL**: https://www.ef.com/wwen/epi/regions/latin-america/paraguay/ ; https://www.expatarrivals.com/americas/paraguay/moving-paraguay
- **Archive**: stable pages via direct HTML / Jina text-mirror extraction; archive not captured
- **Type**: reputable-secondary
- **Date published**: EF 2025 index; Expat Arrivals current page, no explicit page date shown
- **Date accessed**: 2026-06-23
- **Used by**: Paraguay
- **Facts supporting**: Paraguay English-proficiency / adaptation baseline: EF EPI global rank #43, score 531, city scores Asuncion 563, Lambare 557, San Lorenzo 547; Spanish/Guarani official-language adaptation, bus/taxi and poor-road caveats, Asuncion private-care concentration, and Asuncion school concentration (claim-paraguay-021)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-23
## src-783
- **Title**: World Population Review — Safest Countries in the World 2026 / TravelSafe Abroad — Panama safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/panama/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: WPR 2026-06-16; TravelSafe updated 2026-01-03
- **Date accessed**: 2026-06-23
- **Used by**: Panama
- **Facts supporting**: Panama comfort/safety screen: GPI 2.006, WPR rank #52, TravelSafe-derived safety index 65 / Medium, TravelSafe overall risk Medium, transport/taxis Medium, pickpocket and mugging Low (claim-panama-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-01-03

## src-784
- **Title**: EF English Proficiency Index — Panama
- **URL**: https://www.ef.com/wwen/epi/regions/latin-america/panama/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-23
- **Used by**: Panama
- **Facts supporting**: Panama English-proficiency / language-integration screen: global rank #70, EF EPI score 491, reading 511, listening 476, writing 455, speaking 452 (claim-panama-021)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-23

## src-785
- **Title**: World Population Review — Safest Countries in the World 2026 / TravelSafe-derived North Macedonia safety fields
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026-06-16
- **Date accessed**: 2026-06-23
- **Used by**: North Macedonia
- **Facts supporting**: North Macedonia comfort / safety screening proxy: 2025 Global Peace Index score 1.799, 2024 GPI 1.764, 2023 GPI 1.713, and TravelSafe-derived safety index 55 / Low (claim-north-macedonia-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-16

## src-786
- **Title**: EF English Proficiency Index — North Macedonia
- **URL**: https://www.ef.com/wwen/epi/regions/europe/north-macedonia/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-23
- **Used by**: North Macedonia
- **Facts supporting**: North Macedonia English-proficiency / language-integration screen: EF EPI score 595, global average score 488, and European ranking #17 on the captured country page (claim-north-macedonia-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-23


## src-787
- **Title**: World Population Review — Safest Countries in the World 2026 / TravelSafe Bosnia and Herzegovina safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/bosnia-and-herzegovina/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: WPR 2026 table current; TravelSafe updated 2025-12-20
- **Date accessed**: 2026-06-24
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Bosnia and Herzegovina comfort / safety screen: 2025 Global Peace Index score 1.895, 2025 Global Terrorism Index 1.218, TravelSafe-derived safety index 48 / Low, TravelSafe overall risk Low, and medium transport/taxi, pickpocket, scam, mugging, and natural-disaster caveats (claim-bosnia-herzegovina-021)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-20

## src-788
- **Title**: EF English Proficiency Index — Bosnia and Herzegovina
- **URL**: https://www.ef.com/wwen/epi/regions/europe/bosnia-and-herzegovina/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-24
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Bosnia and Herzegovina English-proficiency / language-integration screen: global rank #21, EF EPI score 591, global average score 488, Federation of Bosnia and Herzegovina score 594, Republika Srpska score 584, and Sarajevo score 587 (claim-bosnia-herzegovina-022)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-24

## src-789
- **Title**: World Population Review — Safest Countries in the World 2026 / TravelSafe Moldova safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/moldova/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: WPR 2026 table current; TravelSafe updated 2025-12-16
- **Date accessed**: 2026-06-24
- **Used by**: Moldova
- **Facts supporting**: Moldova comfort / safety screen: 2025 Global Peace Index score 1.918, 2024 GPI 1.976, 2023 GPI 1.873, TravelSafe-derived safety index 67 / Medium, TravelSafe Safety Index 67, user sentiment 65/100, overall risk Medium, and transport/taxi plus Transnistria/regional-security caveats (claim-moldova-020)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-16

## src-790
- **Title**: EF English Proficiency Index — Moldova
- **URL**: https://www.ef.com/wwen/epi/regions/europe/moldova/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-24
- **Used by**: Moldova
- **Facts supporting**: Moldova English-proficiency / language-integration screen: global rank #43, EF EPI score 531, global average score 488, and Chisinau score 572 (claim-moldova-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-24


## src-791
- **Title**: World Population Review — Safest Countries in the World 2026 / TravelSafe Mexico safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/mexico/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: WPR 2026 table current; TravelSafe updated 2026-03-18
- **Date accessed**: 2026-06-24
- **Used by**: Mexico
- **Facts supporting**: Mexico comfort / safety screen: 2025 Global Peace Index score 2.636, 2025 Global Terrorism Index 0.582, WPR safety index 65 / Medium risk, US News safest-country rank 81st, TravelSafe Safety Index 58, user sentiment 75/100, overall risk Medium, transport/taxi Low, pickpocket risk High, and regional safety caveats (claim-mexico-021)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-24

## src-792
- **Title**: EF English Proficiency Index — Mexico
- **URL**: https://www.ef.com/wwen/epi/regions/latin-america/mexico/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-24
- **Used by**: Mexico
- **Facts supporting**: Mexico English-proficiency / language-integration screen: global rank #103, EF EPI score 440, global average score 488, skill scores, and city scores including Monterrey 532, Guadalajara 511, Merida 470, Mexico City 428, and Cancun 414 (claim-mexico-022)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-24


## src-793
- **Title**: World Population Review — Safest Countries in the World 2026 / TravelSafe Argentina safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/argentina/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: WPR 2026 table current; TravelSafe updated 2025-12-27
- **Date accessed**: 2026-06-24
- **Used by**: Argentina
- **Facts supporting**: Argentina comfort / safety screen: 2025 Global Peace Index score 1.768, 2025 Global Terrorism Index 0.801, safety index 70 / Low risk, US News safest-country rank 53rd, TravelSafe Safety Index 70, user sentiment 80/100, low overall and transport/taxi risk, and medium pickpocket, scam, natural-disaster, and women-traveler caveats (claim-argentina-021)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-27

## src-794
- **Title**: EF English Proficiency Index — Argentina
- **URL**: https://www.ef.com/wwen/epi/regions/latin-america/argentina/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-24
- **Used by**: Argentina
- **Facts supporting**: Argentina English-proficiency / language-integration screen: global rank #26, EF EPI score 575, global average score 488, skill scores, and city scores including Buenos Aires 594, Rosario 589, Mendoza 577, and Cordoba 547 (claim-argentina-022)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-24

## src-795
- **Title**: World Population Review - Safest Countries in the World 2026 / TravelSafe Malaysia safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/malaysia/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: WPR 2026-06-16; TravelSafe updated 2025-12-27
- **Date accessed**: 2026-06-24
- **Used by**: Malaysia
- **Facts supporting**: Malaysia comfort / safety screen: 2025 Global Peace Index score 1.469, 2025 Global Terrorism Index 1.626, WPR safety index 69 / Medium, US News safest-country rank 44th, TravelSafe Safety Index 69, user sentiment 78/100, overall risk Low, public transport / ride-hailing generally safe, and East Malaysia warning caveat (claim-malaysia-022)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-27

## src-796
- **Title**: EF English Proficiency Index - Malaysia
- **URL**: https://www.ef.com/wwen/epi/regions/asia/malaysia/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-24
- **Used by**: Malaysia
- **Facts supporting**: Malaysia English-proficiency / adaptation screen: global rank #24, EF EPI score 581, global average score 488, skill scores, region scores, and city scores including Kuala Lumpur 588, Ipoh 582, and Johor Bahru 577 (claim-malaysia-023)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-24


## src-797
- **Title**: World Population Review - Safest Countries in the World 2026 / TravelSafe Thailand safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/thailand/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: WPR 2026-06-16; TravelSafe page title indicates 2026 safety rating
- **Date accessed**: 2026-06-24
- **Used by**: Thailand
- **Facts supporting**: Thailand comfort / safety screen: 2025 Global Peace Index 2.017, 2025 Global Terrorism Index 4.630, WPR / TravelSafe safety index 48, TravelSafe risk level Medium, US News safest-country rank 46th, TravelSafe Safety Index 48, user sentiment 79/100, overall traveler risk Low in tourist-friendly areas, far-south unrest caveat, and medium transport/taxi, pickpocket, natural-disaster, and tap-water risks (claim-thailand-021)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-24

## src-798
- **Title**: EF English Proficiency Index - Thailand
- **URL**: https://www.ef.com/wwen/epi/regions/asia/thailand/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-24
- **Used by**: Thailand
- **Facts supporting**: Thailand English-proficiency / adaptation screen: global rank #116, EF EPI score 402, global average score 488, and city scores including Pattaya 474, Bangkok 467, Chiang Mai 453, and Phuket 431 (claim-thailand-022)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-24

## src-799
- **Title**: World Population Review - Safest Countries in the World 2026 / TravelSafe Indonesia safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/indonesia/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: WPR 2026-06-16; TravelSafe page title indicates 2026 safety rating and page metadata modified 2025-12-27
- **Date accessed**: 2026-06-24
- **Used by**: Indonesia
- **Facts supporting**: Indonesia comfort / safety screen: 2025 Global Peace Index 1.786, 2025 Global Terrorism Index 4.170, WPR / TravelSafe safety index 58, TravelSafe risk level Medium, US News safest-country rank 51st, TravelSafe user sentiment 85/100, medium overall / transport / pickpocket / mugging / scam / tap-water / women-traveler risks, high natural-disaster and terrorism risk boxes, and 2026 criminal-code / social-norm caveats (claim-indonesia-020; claim-indonesia-021)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-24

## src-800
- **Title**: EF English Proficiency Index - Indonesia
- **URL**: https://www.ef.com/wwen/epi/regions/asia/indonesia/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-24
- **Used by**: Indonesia
- **Facts supporting**: Indonesia English-proficiency / adaptation screen: global rank #80, EF EPI score 471, global average score 488, and city scores including Jakarta 523, Surabaya 519, Bandung 505, Balikpapan / Batam 495, and Denpasar 477 (claim-indonesia-020)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-24


## src-801
- **Title**: World Population Review - Safest Countries in the World 2026 / TravelSafe Kazakhstan safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/kazakhstan/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: WPR 2026-06-16; TravelSafe updated 2025-12-24
- **Date accessed**: 2026-06-24
- **Used by**: Kazakhstan
- **Facts supporting**: Kazakhstan comfort / safety screen: 2025 Global Peace Index 1.875, WPR safety index 72 / Low risk, US News safest-country rank 65th, TravelSafe Safety Index 72, user sentiment 85/100, overall risk Low, and petty-crime / transport-taxi practical caveats (claim-kazakhstan-020)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-24

## src-802
- **Title**: EF English Proficiency Index - Kazakhstan
- **URL**: https://www.ef.com/wwen/epi/regions/asia/kazakhstan/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-24
- **Used by**: Kazakhstan
- **Facts supporting**: Kazakhstan English-proficiency / adaptation screen: global rank #107, EF EPI score 417, global average score 488, and city scores including Astana 460, Almaty 457, Aktau 397, and Shymkent 377 (claim-kazakhstan-021)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-24


## src-803
- **Title**: World Population Review - Safest Countries in the World 2026 / TravelSafe Armenia safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/armenia/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: WPR 2026-06-16; TravelSafe page title indicates 2026 safety rating
- **Date accessed**: 2026-06-25
- **Used by**: Armenia
- **Facts supporting**: Armenia comfort / safety screen: 2025 Global Peace Index 1.893, 2025 Global Terrorism Index 0.720, TravelSafe-derived safety index 60 / Low risk, overall traveler risk Low, low pickpocket / mugging / terrorism / scam / women-traveler / tap-water risk, medium transport/taxi risk, and border-region / mountain-road caveats (claim-armenia-019)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-25

## src-804
- **Title**: EF English Proficiency Index - Armenia
- **URL**: https://www.ef.com/wwen/epi/regions/europe/armenia/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-25
- **Used by**: Armenia
- **Facts supporting**: Armenia English-proficiency / adaptation screen: global rank #56, EF EPI score 515, low-proficiency band, and need for Armenian/Russian administrative support despite better English baseline than many post-USSR fallback countries (claim-armenia-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-25

## src-805
- **Title**: World Population Review - Safest Countries in the World 2026 / TravelSafe UAE safety report
- **URL**: https://worldpopulationreview.com/country-rankings/safest-countries-in-the-world ; https://www.travelsafe-abroad.com/united-arab-emirates/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: WPR 2026-06-16; TravelSafe updated 2025-12-25
- **Date accessed**: 2026-06-25
- **Used by**: UAE
- **Facts supporting**: UAE comfort / safety screen: 2025 Global Peace Index 1.812, 2025 Global Terrorism Index 1.178, TravelSafe-derived safety index 79, risk level Low, US News safest-country rank 25th, TravelSafe Safety Index 79, user sentiment 78/100, overall traveler risk Low, and medium transport/taxi, terrorism, scams, and women-traveler caveats (claim-uae-018)
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-25

## src-806
- **Title**: EF English Proficiency Index - United Arab Emirates
- **URL**: https://www.ef.com/wwen/epi/regions/middle-east/united-arab-emirates/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: reputable-secondary
- **Date published**: 2026 edition page, no separate page date captured
- **Date accessed**: 2026-06-25
- **Used by**: UAE
- **Facts supporting**: UAE English-proficiency / adaptation screen: global rank #72, EF EPI score 487, global average 488, skill scores, job-function scores, and city/region scores including Dubai 509-513, Abu Dhabi 481-484, Sharjah 477-479, Al Ain 452, and Ajman 425 (claim-uae-019)
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-25

## src-807
- **Title**: Balcells Group - Contact
- **URL**: https://balcellsgroup.com/contact/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-26
- **Used by**: Spain
- **Facts supporting**: Spain bureaucracy/practicality contact lead: Barcelona law firm advertising immigration, tax, business, and real-estate services; phone +34 93 631 51 39; address Rambla de Catalunya 124, Barcelona
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-26

## src-808
- **Title**: Global Citizen Solutions - Contact Us
- **URL**: https://www.globalcitizensolutions.com/contact-us/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-26
- **Used by**: Portugal
- **Facts supporting**: Portugal bureaucracy/practicality contact lead: private residence / immigration advisory firm with Portugal office at Av. 24 de Julho 4, 2o Esquerdo, Lisboa 1200-480; phone +351 21 060 5995
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-26

## src-809
- **Title**: Mazzeschi Legal Counsels - Contact us
- **URL**: https://www.mazzeschi.it/contact-us/
- **Archive**: [archive: failed 2026-06-26; HTTP 429 from Wayback save; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-26
- **Used by**: Italy
- **Facts supporting**: Italy bureaucracy/practicality contact lead: firm focused on Italian immigration, citizenship, corporate, and commercial law; headquarters near Siena; Milan representative office; email info@mazzeschi.it; telephone +39 0577 926921
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-26

## src-810
- **Title**: Immigration Greece - Contact our immigration lawyer in Greece
- **URL**: https://www.immigration-greece.com/contact/
- **Archive**: [archive: failed 2026-06-26; HTTP 429 from Wayback save; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-26
- **Used by**: Greece
- **Facts supporting**: Greece bureaucracy/practicality contact lead: Athens immigration-lawyer site advertising residency, citizenship, retirement-visa, nomad-visa, and FIP-visa services; address Ermou 56, Athina 105 63, Greece; email clients(at)lawyersgreece.eu
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-26

## src-811
- **Title**: Michael Kyprianou Law Firm - Contact us
- **URL**: https://www.kyprianou.com/en/contact-us
- **Archive**: [archive: failed 2026-06-27; HTTP 429 from Wayback save; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-27
- **Used by**: Cyprus
- **Facts supporting**: Cyprus bureaucracy/practicality contact lead: Cyprus law-firm contact page with offices in Nicosia, Limassol, and Paphos; Nicosia office at 17 Stasinou Avenue, 1060 Nicosia; telephone +357 22 447 777; email info@kyprianou.com; Limassol and Paphos office contacts also listed
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-27

## src-812
- **Title**: Vukmir & Associates - Services / Contact
- **URL**: https://www.vukmir.net/services/ ; https://www.vukmir.net/contact/
- **Archive**: [archive: failed 2026-06-27; HTTP 429 from Wayback save; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-27
- **Used by**: Croatia
- **Facts supporting**: Croatia bureaucracy/practicality contact lead: Zagreb law firm with Labor and Immigration Law, corporate/commercial, real-estate, ICT, and privacy/data-protection service areas; contact address Gramača 2L, 10000 Zagreb; telephone +385 1 3760 511; email vukmir@vukmir.net
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-27

## src-813
- **Title**: Chetcuti Cauchi Advocates - Contact Us
- **URL**: https://www.ccmalta.com/contact
- **Archive**: [archive: failed 2026-06-27; HTTP 429 from Wayback save; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-27
- **Used by**: Malta
- **Facts supporting**: Malta bureaucracy/practicality contact lead: law-firm contact page and navigation listing Immigration, European Residency, Global Mobility, Tax, Corporate Services, Property, and related practice areas; main entrance 86 Merchants Street, Valletta VLT 1166; email info@ccmalta.com; telephone +356 22056200
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-27

## src-814
- **Title**: Foreigners.cz - services for foreign students and expats in the Czech Republic
- **URL**: https://www.foreigners.cz/relocation-services/
- **Archive**: [archive: failed 2026-06-27; HTTP 429 from Wayback save; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-27
- **Used by**: Czech Republic
- **Facts supporting**: Czech Republic bureaucracy/practicality contact lead: relocation-services page listing visa arrangement, residence permit, employee card, digital nomad program, proof of accommodation, cleaning service, and relocation support for foreign students and expats; public contact info@foreigners.cz and +420 211 221 492; city selector includes Brno, Prague, Pilsen, Hradec Kralove, and Olomouc
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-27


## src-815
- **Title**: Immigration-Poland.com - Contact our Poland immigration specialists
- **URL**: https://www.immigration-poland.com/contact/
- **Archive**: [archive: failed 2026-06-27; HTTP 429 from Wayback save; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-27
- **Used by**: Poland
- **Facts supporting**: Poland bureaucracy/practicality contact lead: Warsaw immigration-specialist contact page listing residency / citizenship / Schengen-visa / temporary-residence services; address ul. Hoza 86, office 210/214, 00-682 Warszawa; email clients(at)lawyerspoland.eu; phone +485****3752
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-27

## src-816
- **Title**: Immigration-Romania.com - Contact Us | Romanian Immigration Lawyer
- **URL**: https://www.immigration-romania.com/contact/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-27
- **Used by**: Romania
- **Facts supporting**: Romania bureaucracy/practicality contact lead: Romanian immigration-lawyer site advertising support for immigration to Romania, foreign-worker hiring, work visa / residence-permit / employer-support contact form, document review, and guidance until completion; phone +40 734 679 007; email Office@immigration-romania.com and Astrid114@yahoo.com; address Alba-Iulia Str., No. 96, Ighiu, Alba County, Romania
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-27

## src-817
- **Title**: New Balkans Law Office — Business Immigration Bulgaria
- **URL**: https://www.newbalkanslawoffice.com/practice-areas/business-immigration/
- **Archive**: [archive: failed 2026-06-27; direct page is dynamic/cookie-protected, text extracted via Jina reader]
- **Type**: reputable-secondary
- **Date published**: unknown
- **Date accessed**: 2026-06-27
- **Used by**: Bulgaria
- **Facts supporting**: Neutral Bulgaria immigration-lawyer contact lead; Sofia office email/phone/address; business-immigration services covering visas, residence permits, work permits, documentation, and administrative procedures
- **Confidence ceiling**: medium
- **Stale at**: 2027-06-27

## src-818
- **Title**: Helpers Hungary - Services and Contact
- **URL**: https://helpers.hu/services/ ; https://helpers.hu/services/immigration/ ; https://helpers.hu/contact/
- **Archive**: [archive: not captured; direct pages extracted through Jina reader]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-27
- **Used by**: Hungary
- **Facts supporting**: Neutral Hungary bureaucracy/practicality contact lead: Budapest business and immigration services provider offering immigration services from residency to citizenship, company formation, back office/accountancy, residence-permit and business-immigration assistance; public phone +36 1 317 8570; email info@helpers.hu; address Budapart Gate, Dombovari ut 27, Budapest 1117
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-27


## src-819
- **Title**: AKMV Law Firm - Immigration law / Contact
- **URL**: https://www.akmv.sk/en/legal-services-category/immigration-law/ ; https://www.akmv.sk/en/contact/
- **Archive**: [archive: not captured; direct gzip HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-28
- **Used by**: Slovakia
- **Facts supporting**: Neutral Slovakia bureaucracy/practicality contact lead: Bratislava law firm listing immigration-law services for residence permits for foreigners, temporary residence for the purpose of doing business, work permits, and family reunification; contact phone +421 915 046 749, phone +421 (2) 4333 3509, email recepcia@akmv.sk, address Pluhova 17, 831 03 Bratislava
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-28

## src-820
- **Title**: Lawyers Slovenia / BridgeWest - Law Firm in Slovenia / Contact
- **URL**: https://www.lawyersslovenia.com/ ; https://www.lawyersslovenia.com/contact/
- **Archive**: [archive: not captured; direct page blocked with HTTP 403, text extracted through Jina reader]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-28
- **Used by**: Slovenia
- **Facts supporting**: Neutral Slovenia bureaucracy/practicality contact lead: Ljubljana legal-services provider advertising immigration representation before the Ministry of the Interior, work permits from the Employment Service of Slovenia, company setup, residence, citizenship, VAT registration, and tax advice; public contact `clients(at)lawyersslovenia.com` and phone `(+35) 699 699 405`
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-28

## src-821
- **Title**: Prelevic Law Firm - Contact / Expertise
- **URL**: https://www.prelevic.com/contact/ ; https://www.prelevic.com/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-28
- **Used by**: Montenegro
- **Facts supporting**: Neutral Montenegro bureaucracy/practicality contact lead: Podgorica law firm describing banking/finance, corporate/commercial, labour, real estate, human rights, energy, and intellectual-property practice areas; address Bulevar Svetog Petra Cetinjskog 130/7, 81000 Podgorica; phone +382 20 228 563 / +382 20 228 564; email office@prelevic.com
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-28


## src-822
- **Title**: Zunic Law - Serbia Immigration Lawyer / Contact
- **URL**: https://zuniclaw.com/en/serbia-immigration-lawyer/ ; https://zuniclaw.com/en/contact/
- **Archive**: [archive: failed 2026-06-28; HTTP 429 from Wayback save; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-28
- **Used by**: Serbia
- **Facts supporting**: Neutral Serbia bureaucracy/practicality contact lead: Serbia immigration-lawyer page advertising immigration services for companies, investors, global entrepreneurs, and families, including temporary residence, permanent residence, work permits, family reunification, and citizenship; contact page listing Belgrade address Tadije Sondermajera 3, 11000 Belgrade, phone +381 63 185 84 58, Novi Sad address Theater Square 7, 21000 Novi Sad, phone +381 62 89 68 090, and email bd@zuniclaw.com
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-28

## src-823
- **Title**: Ata Kurumsal - Turkey work/residence permit consultancy and contact
- **URL**: https://atakurumsal.com/en/homepage ; https://atakurumsal.com/en/contact
- **Archive**: [archive: not captured; text extracted through Jina reader]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-28
- **Used by**: Turkey
- **Facts supporting**: Neutral Turkey bureaucracy/practicality contact lead: public English site advertising work-permit, residence-permit, company-establishment, and Turkish-citizenship consultancy services; contact page listing public email info@atakurumsal.com
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-28

## src-824
- **Title**: BGI Legal - Georgian law firm homepage / services / contact
- **URL**: https://bgi.ge/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-28
- **Used by**: Georgia
- **Facts supporting**: Neutral Georgia bureaucracy/practicality contact lead: Tbilisi full-service law firm describing contracts/corporate structuring, tax and customs advice, corporate registrations and incorporation, and public contact details at Meidan Palace, 44 Kote Abkhazi Str., Tbilisi 0108; bgilegal@bgi.ge; +995 322 470 747
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-28

## src-825
- **Title**: Kalo & Associates - Contact / Practice Areas
- **URL**: https://www.kalo-attorneys.com/contact/ ; https://www.kalo-attorneys.com/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-29
- **Used by**: Albania
- **Facts supporting**: Neutral Albania bureaucracy/practicality contact lead: Tirana law firm contact page listing Kavaja Avenue, Tirana Tower, 5th Floor, Tirana, Albania; phone +355 (4)2233 532 / +355 (4)2224727; email info@kalo-attorneys.com; site practice areas include FDI, banking and finance, corporate/commercial, employment, real estate, tax and taxation, litigation and arbitration, and intellectual property
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-29

## src-826
- **Title**: Karanovic & Partners - Contact / Practice and industry groups
- **URL**: https://www.karanovicpartners.com/contact/ ; https://www.karanovicpartners.com/practice-industry-groups/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-29
- **Used by**: North Macedonia
- **Facts supporting**: Neutral North Macedonia bureaucracy/practicality contact lead: Qoku & Partners in cooperation with Karanovic & Partners listed in Skopje at Maksim Gorki no. 13, 1000 Skopje, North Macedonia; tel. +389 2 3223 870; northmacedonia@karanovicpartners.com; public practice list includes corporate and commercial, employment, real estate, tax, IT/startups, and technology/media/telecoms coverage
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-29

## src-827
- **Title**: MARIC & Co - Law firm homepage / expertise / contact
- **URL**: https://mariclaw.com/
- **Archive**: [archive: not captured; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-29
- **Used by**: Bosnia and Herzegovina
- **Facts supporting**: Neutral Bosnia and Herzegovina bureaucracy/practicality contact lead: Sarajevo law firm describing more than 65 years of legal-services experience and public expertise areas including corporate and commercial law, employment law, immigration and nationality law, regulatory compliance, risk management, and tax law; public contact details include contact@mariclaw.com and +387 33 566 700
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-29

## src-828
- **Title**: Turcan Cazac - Work permits / contacts / Moldova business-law practice pages
- **URL**: https://www.turcanlaw.md/practices/work-permits/ ; https://www.turcanlaw.md/contacts ; https://www.turcanlaw.md/
- **Archive**: [archive: failed 2026-06-29; Wayback returned HTTP 429; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-29
- **Used by**: Moldova
- **Facts supporting**: Neutral Moldova bureaucracy/practicality contact lead: Chisinau law firm with public practice links for corporate and M&A, commercial and employment, regulatory and tax, tax advisory, data protection, and work permits; work-permits page lists Alexander.Tuceac@TurcanLaw.md for a free description of the Moldovan work-permitting process; contact page lists Str. Puskin 47/1-5a, Chisinau, MD-2005, tel. (373) 22 212 031 / 226 113, and Turcan@TurcanLaw.md
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-29

## src-829
- **Title**: FERRERE Uruguay - services and contact pages
- **URL**: https://www.ferrere.com/en/services/ ; https://www.ferrere.com/en/contact/
- **Archive**: [archive: failed 2026-06-29; Wayback returned HTTP 429; direct HTML extraction used]
- **Type**: commercial
- **Date published**: no page date captured
- **Date accessed**: 2026-06-29
- **Used by**: Uruguay
- **Facts supporting**: Neutral Uruguay bureaucracy/practicality contact lead: public services page lists practice areas including immigration, tax, labour, company law and corporate governance, corporate and commercial, real estate, family law, data privacy and information technologies, and technology/media/TMT; contact page lists Uruguay offices and public phone contacts including Montevideo +598 2900 1000, Aguada Park +598 2 927 2360, Punta del Este +598 4244 1287, Colonia +598 4523 1517, and Tacuarembo +598 4633 1111
- **Confidence ceiling**: medium
- **Stale at**: 2026-12-29
