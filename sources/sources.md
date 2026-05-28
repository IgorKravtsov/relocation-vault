---
document: sources-registry
version: 1.0.0
last_updated: 2026-05-28
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
