---
document: sources-registry
version: 1.0.0
last_updated: 2026-05-31
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
