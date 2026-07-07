# Dimension: Application-prep trigger map

Last updated: 2026-07-07
Mode: consolidation
Inputs: `dimensions/final-synthesis-readiness-checklist.md`, `dimensions/screening-readiness-map.md`, country profiles, and resolved-for-screening verification notes
Consolidation status (run-292): downstream-only trigger map for future country-specific application-prep work. This file does not rank countries, choose finalists, change tiers, update claims, update sources, or reopen resolved verification items.

## Scope

This map defines when a later human-directed application-prep iteration is appropriate after downstream synthesis or finalist selection. It is not a TOP-N list, visit order, recommendation, legal advice, tax advice, school recommendation, insurance recommendation, or instruction to start filings.

## When to open application-prep work

Use a country-specific application-prep iteration only when at least one trigger is present:

1. A human explicitly names a finalist country or route for filing preparation.
2. New official evidence changes a route, income threshold, tax regime, insurance requirement, school access rule, or residence-to-PR/citizenship baseline.
3. A source becomes stale before a real filing or visit decision.
4. Downstream synthesis selects a small finalist set and asks for current, filing-grade checks.
5. A live operational dependency is needed: consulate appointment, lawyer/accountant confirmation, insurance quote, rent listing, school fee schedule, translation/apostille checklist, or bank/address-registration mechanics.

Do not open broad application-prep work simply because a profile contains resolved-for-screening caveats. Those caveats are expected and should stay dormant until a trigger above exists.

## Route / immigration triggers

Open a route-specific update when a finalist needs filing-grade confirmation of:

- serving-consulate checklist, appointment channel, fee, translation/apostille, police-record, health-insurance, and document-validity rules;
- whether the chosen residence type allows remote foreign-client IT work, local sole-proprietor/company registration, family dependency, and later renewal;
- how a Polish residence card or temporary-protection status interacts with the destination status;
- whether DN, remote-worker, DTV, DE Rantau, virtual-work, ordinary self-employment, business, family, or student status counts toward PR/citizenship;
- current post-4-March-2027 Ukraine temporary-protection transition rules if the country profile still uses a conservative no-captured-bridge baseline.

## Tax / work triggers

Open a tax/accountant update when a finalist needs filing-grade confirmation of:

- exact self-employed, sole-proprietor, freelancer, company-manager, or small-business registration route;
- activity-code / trade classification for foreign-client IT;
- PIT, social-security, health-insurance, VAT / reverse-charge / export-service, e-invoicing, invoice-language, and banking mechanics;
- whether any favorable regime used in a screening upside scenario really applies;
- spouse/joint-filing, dependent, or second-earner effects.

Keep first-pass worked examples as screening baselines until an adviser or official source changes them.

## Budget / housing triggers

Open a live budget or housing update when a finalist needs:

- current long-term listings in the chosen city and season;
- deposit, agency-fee, utilities, heating/cooling, internet, address-registration, lease-duration, landlord-document, and foreigner-acceptance terms;
- a city-specific two-room / one-bedroom-plus-workspace affordability check against the relevant tax-net band;
- rent evidence for legally required registered leases, if the route depends on it.

Do not replace country-level Livingcost-style screening baselines with live listings until a finalist city is chosen.

## Healthcare / education triggers

Open a healthcare or education update when a finalist needs:

- route-compliant insurance wording and quotes for two adults, maternity/newborn terms, exclusions, and waiting periods;
- public-system onboarding by exact residence/tax status;
- GP, pediatric, maternity, dental, lab, emergency, and private-clinic price samples in the chosen city;
- international/bilingual/local school fee schedules, admission deposits, transport/meals, language support, waiting lists, and foreign-child enrollment rules;
- childcare / preschool quotes if a future-child scenario becomes near-term.

## Comfort / partner / practical triggers

Open a practical-fit update when a finalist needs:

- partner dependency or marriage documentation, cohabitation evidence, independent-status fallback, or student-status route confirmation;
- city-level safety, language, expat/Ukrainian community, transport, air-quality, climate-comfort, and seasonal-risk checks;
- lawyer/accountant/community contact shortlists and first-email scripts;
- arrival sequence, temporary accommodation, SIM/banking, address registration, medical appointment, and first-30-days plan.

## Guardrails for future iterations

- Keep application-prep work country-specific and route-specific; do not reopen all countries mechanically.
- Keep final ranking, TOP-N, and visit order outside normal Hermes iterations unless an explicit downstream synthesis owner requests them.
- Do not change country tiers from application-prep details unless the detail materially changes route viability or budget feasibility.
- If new evidence changes a screening conclusion, update the country profile, relevant dimension map, `state.json`, `INDEX.md`, `CHANGELOG.md`, and the run log in the same iteration.
- If application-prep checks reveal only expected operational details, log them in the country profile without reopening resolved-for-screening verification blockers.
