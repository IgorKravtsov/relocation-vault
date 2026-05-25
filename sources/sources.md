---
document: sources-registry
version: 1.0.0
last_updated: 2026-05-25
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
- **Used by**: Greece, Spain, Italy, Cyprus
- **Facts supporting**: EU-level TP extension chain to 04 March 2027; one-Member-State TP principle; Spain, Italy, and Cyprus TP validity context through 04 March 2027
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
- **Title**: Portugalist — Portugal’s Digital Nomad Visa Requirements: a deep dive into every aspect of the application
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
