---
document: changelog
version: 1.0.0
last_updated: 2026-06-09
---

## 2026-06-09 — run-081
- Italy: depth_score 2.5 -> 4.0; sections 5.4 cost of living and 5.5 rent moved from pending to completed for first-pass screening.
- Added Italy cost/rent sources `src-396` through `src-400` from Livingcost country and city pages.
- Main finding: Palermo is the best first-pass Italy budget/climate city, Naples is plausible, Rome is tight, and Milan is a poor default fit on one taxed income.
- Verification queue remains 5 pending/open items; next suggested focus: Portugal 5.3 taxes.

## 2026-06-09 — run-080
- Spain: depth_score 2.5 -> 4.0; sections 5.4 cost of living and 5.5 rent moved from pending to completed for first-pass screening.
- Added Spain cost/rent sources `src-391` through `src-395` from Livingcost country and city pages.
- Main finding: Valencia is the best first-pass Spain budget city, Malaga is plausible but tourist-rent-sensitive, and Madrid/Barcelona are poor default fits on one taxed income.
- Verification queue remains 5 pending/open items; next suggested focus: Italy 5.4/5.5.

## 2026-06-09 — run-079
- Greece: depth_score 2.0 -> 4.0; sections 5.4 cost of living and 5.5 rent moved from pending to completed for first-pass screening.
- Added Greece cost/rent sources `src-386` through `src-390` from Livingcost country and city pages.
- Main finding: Thessaloniki and Patras are the best first-pass budget cities; Heraklion is climate-favorable but rent-sensitive, and Athens is service-rich but cost/heat pressured.
- Verification queue remains 5 pending/open items; next suggested focus: Spain 5.4/5.5.

## 2026-06-09 — run-078
- Croatia: depth_score 2.0 -> 4.0; sections 5.4 cost of living and 5.5 rent moved from pending to completed for first-pass screening.
- Added Croatia cost/rent sources `src-381` through `src-385` from Livingcost country and city pages.
- Main finding: Rijeka is the best first-pass cost/coastal compromise; Zagreb is serviceable but colder, Split is a stretch, and Dubrovnik is too rent-heavy by default on one income.
- Verification queue remains 5 pending/open items; next suggested focus: Greece 5.4/5.5.

## 2026-06-08 — run-077
- Malta: depth_score 2.0 -> 4.0; sections 5.4 cost of living and 5.5 rent moved from pending to completed for first-pass screening.
- Added Malta cost/rent sources `src-376` through `src-380` from Livingcost country and city pages.
- Main finding: Malta is tight-to-negative on current income; Marsaskala is the only screened city that looks potentially manageable, while Sliema is too rent-heavy by default.
- Verification queue remains 5 pending/open items; next suggested focus: Croatia 5.4/5.5.

## 2026-06-08 — run-076
- Cyprus: depth_score 2.0 -> 4.0; sections 5.4 cost of living and 5.5 rent moved from pending to completed for first-pass screening.
- Added Cyprus cost/rent sources `src-371` through `src-375` from Livingcost country and city pages.
- Main finding: Larnaca and Nicosia are the only plausible first-pass cities on the current income; Paphos is rent-sensitive and Limassol is too expensive by default.
- Verification queue remains 5 pending/open items; next suggested focus: Malta 5.4/5.5.

## 2026-06-08 — run-075
- Verification batch: resolved `vq-100` through `vq-104` to conservative screening baselines for Slovenia, Montenegro, Serbia, Turkey, and Georgia tax-fit blockers.
- Country tax sections remain partial; accountant / VAT / contribution / immigration-status details were demoted to application-prep checks rather than treated as passed DoD.
- Verification queue: 10 -> 5 pending/open items. Next suggested focus: Cyprus 5.4/5.5 cost and rent.

## 2026-06-08 — run-074
- Georgia: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Georgia tax / FX sources `src-365` through `src-370` and `claim-georgia-008` through `claim-georgia-012`.
- Main finding: if small-business status applies, USD 3,000/month is about GEL 7,986 gross and screens at about GEL 7,906 / USD 2,970 net tax-only, or GEL 7,587 / USD 2,850 with a 4% pension sensitivity; ordinary 20% PIT fallback is about USD 2,400.
- Added `vq-104` for small-business / IT residence / VAT / pension compatibility; queue 9 -> 10, so next mode should be verification.

## 2026-06-08 — run-073
- Turkey: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Turkey tax / FX sources `src-359` through `src-364` and `claim-turkey-010` through `claim-turkey-014`.
- Main finding: USD 3,000/month is about TRY 138,286; ordinary 2026 non-employment PIT leaves about TRY 99,677 / USD 2,162 net, while a 15% employee-style SGK sensitivity leaves about TRY 86,194 / USD 1,870.
- Added `vq-103` for Turkish self-employment / SGK / VAT / foreign-income exemption / immigration-status compatibility; queue 8 -> 9, below the active verification threshold.

## 2026-06-08 — run-072
- Serbia: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Serbia tax / FX sources `src-353` through `src-358` and `claim-serbia-011` through `claim-serbia-015`.
- Main finding: USD 3,000/month is about RSD 302,160; a conservative gross-base PIT + SSC stress test leaves about RSD 166,037 / USD 1,649 net, while a 20% expense-base sensitivity leaves about RSD 193,262 / USD 1,919.
- Added `vq-102` for freelancer / entrepreneur classification, APR, contribution-base, VAT, and single-permit compatibility; queue 7 -> 8, below the active verification threshold.

## 2026-06-08 — run-071
- Montenegro: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Montenegro tax sources `src-349` through `src-352`, reused `src-348` ECB FX, and added `claim-montenegro-012` through `claim-montenegro-016`.
- Main finding: if the entrepreneur PIT model applies, USD 3,000/month leaves about EUR 2,314 / USD 2,693 PIT-only, or about EUR 2,043 / USD 2,378 under a conservative 10.5% employee-rate SSC sensitivity.
- Added `vq-101` for self-employed registration / SSC / VAT / DN-status tax compatibility; queue 6 -> 7, below the active verification threshold.

## 2026-06-07 — run-070
- Slovenia: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Slovenia tax sources `src-344` through `src-348` and `claim-slovenia-009` through `claim-slovenia-013`.
- Main finding: a conservative ordinary self-employed stress test at USD 3,000/month leaves about EUR 1,364 / USD 1,587 net per month after a gross-rate social-contribution stress test and PIT, before accountant/VAT/immigration costs.
- Added `vq-100` for Slovenian s.p. / normirani / VAT / immigration-status confirmation; queue 5 -> 6, still below the active verification threshold.

## 2026-06-07 — run-069
- Verification batch: resolved vq-095 through vq-099 to conservative screening baselines for Poland, Romania, Bulgaria, Hungary, and Slovakia tax-fit blockers.
- Country tax sections remain partial; exact accountant / VAT / immigration-status checks were demoted to application-prep notes rather than treated as passed DoD.
- Verification queue: 10 → 5 pending/open items.

## 2026-06-07 — run-068
- Slovakia: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Slovakia tax sources `src-338` through `src-343` and `claim-slovakia-010` through `claim-slovakia-015`.
- Main finding: if the non-VAT SZCO 60% lump-sum expense model and 2026 minimum social/health contributions apply, USD 3,000/month leaves about EUR 2,050-2,147 / USD 2,386-2,499 net before accountant/VAT/immigration costs.
- Added `vq-099` for SZCO trade classification / VAT / contribution timing / business-residence compatibility; queue 9 -> 10, so next mode should be verification.

## 2026-06-07 — run-067
- Verification mode: resolved Greece `vq-089` by capturing EFKA's official 2026 self-employed contribution table.
- Added Greece source `src-337` and `claim-greece-012`; Greece section 5.3 remains partial but now has a usable ordinary PIT + minimum EFKA stress test.
- Main finding: EFKA category-1 main pension + health is EUR 250.77/month plus EUR 10 unemployment; Greece's conservative USD 3,000/month tax baseline is about EUR 1,844 / USD 2,131 net before accountant/VAT filing costs.
- Removed `greece-efka-self-employed-contribution-gap`; queue 10 -> 9, so next mode can resume country-deep-dive.

## 2026-06-07 — run-066
- Hungary: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Hungary tax sources `src-332` through `src-336` and `claim-hungary-010` through `claim-hungary-016`.
- Main finding: USD 3,000/month is about HUF 919,157 gross; a conservative actual-base stress test leaves about HUF 534,490 / USD 1,745 net, while an unverified minimum-base sensitivity leaves about HUF 671,448 / USD 2,192.
- Added `vq-098` for individual-entrepreneur regime / contribution-base / VAT / immigration-status confirmation; queue 9 -> 10, so next mode should be verification.

## 2026-06-07 — run-065
- Bulgaria: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Bulgaria tax sources `src-328` through `src-331` and `claim-bulgaria-012` through `claim-bulgaria-017`.
- Main finding: a USD 3,000/month foreign-client freelance stress test is about BGN 5,072 gross and roughly BGN 3,658 / USD 2,164 net after 25% statutory expenses, capped-base 27.8% contributions, and 10% PIT.
- Added `vq-097` for self-insured contribution package / IT classification / VAT / immigration-status confirmation; queue 8 -> 9.

## 2026-06-07 — run-064
- Romania: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Romania tax sources `src-324` through `src-327` and `claim-romania-010` through `claim-romania-016`.
- Main finding: ordinary PFA-style tax stress test at USD 3,000/month leaves about RON 9,156 / USD 2,027 per month after CAS/CASS and PIT, with a lower gross-base-PIT sensitivity around USD 1,952.
- Added `vq-096` for PFA registration / expense / VAT / immigration-status confirmation; queue 7 -> 8.

## 2026-06-07 — run-063
- Poland: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Poland tax sources `src-320` through `src-323`, reused `src-293` USD/PLN, and added `claim-poland-011` through `claim-poland-017`.
- Main finding: if 12% IT `ryczalt` applies, USD 3,000/month is about PLN 10,918 gross and leaves about PLN 8,777 / USD 2,412 after lump-sum tax and health contribution, before uncaptured ZUS social contributions.
- Added `vq-095` for 2026 ZUS / IT classification / VAT / immigration-status confirmation; queue 6 -> 7.

## 2026-06-06 — run-062
- Czech Republic: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Czech tax sources `src-316` through `src-319`, reused `src-293` USD/CZK, and added `claim-czech-006` through `claim-czech-011`.
- Main finding: if flat-tax band I applies, USD 3,000/month nets about CZK 52,691 / USD 2,522 after the CZK 9,984 monthly flat-tax payment.
- Added `vq-094` for Czech IT trade / 60% expense-category / VAT / social-health confirmation; queue 5 -> 6.

## 2026-06-06 — run-061
- Verification mode: resolved 5 legal/route blockers (`vq-072`, `vq-086`, `vq-087`, `vq-088`, `vq-055`).
- Armenia now has conservative screening baselines: no captured Ukraine-specific bridge, business activity is a real-business IE/LLC route rather than DN, and partner planning is marriage/independent-status first.
- Argentina tourist-entry capture is demoted to before-travel / DN-filing check; Albania Unique Permit microdetails are demoted to application-prep / later deep-dive checks.
- Sources added: none.
- Verification queue: 10 -> 5 pending/open; next can resume country-deep-dive, likely Czech Republic 5.3 taxes.

## 2026-06-06 — run-060
- Malta: depth_score 1.5 -> 2.0; section 5.3 taxes moved from pending to partial.
- Added Malta tax sources `src-311` through `src-315` and claims `claim-malta-006` through `claim-malta-011`.
- Added `vq-093` for NRP authorised-work tax / social-security / VAT verification; queue 9 -> 10.

## 2026-06-06 — run-059
- Croatia: depth_score 1.5 -> 2.0; section 5.3 taxes is now partial with tax-residence, ordinary self-employment PIT, social contributions, allowances, VAT, filing, and worked-example baselines.
- Worked example: USD 3,000/month -> about EUR 31,152/year; conservative ordinary self-employment stress test leaves about EUR 1,407-1,491/month after 36.5% contributions and local lower-bracket PIT.
- Main finding: Croatia's tax answer is incomplete rather than negative because lump-sum craft taxation may be much better, but exact 2026 contribution / IT activity / VAT treatment needs verification.
- Sources added: src-306 through src-310; reused src-293 FX.
- Claims added: claim-croatia-006 through claim-croatia-011.
- Verification queue: 8 -> 9 pending/open; next should continue Tier-1-hint practical tax coverage without clustering, likely Malta 5.3.

## 2026-06-06 — run-058
- Cyprus: depth_score 1.5 -> 2.0; section 5.3 taxes is now partial with tax-residence, PIT, self-employed Social Insurance/GHS, filing, marriage, and worked-example baselines.
- Worked example: USD 3,000/month -> about EUR 31,152/year; estimated net about EUR 1,974/month if contributions are deductible, or about EUR 1,854/month in the non-deductible sensitivity.
- Main finding: Cyprus tax burden is moderate, but current income is still far below the DN route's EUR 3,500/month net-after-tax/contribution threshold.
- Sources added: src-301 through src-305; reused src-293 FX.
- Claims added: claim-cyprus-006 through claim-cyprus-011.
- Verification queue: 7 -> 8 pending/open; next should continue Tier-1-hint practical tax coverage, likely Croatia 5.3.

## 2026-06-06 — run-057
- Greece: depth_score 1.5 -> 2.0; section 5.3 taxes is now partial with PIT baseline, registration route, filing/marriage mechanics, and Article 5C upside caveat.
- Added AADE/PwC tax sources for Greek tax residence, unified business-profit PIT, myAADE TIN/activity commencement, VAT/filing/prepayment, and new-tax-resident Article 5C relief.
- Worked example: USD 3,000/month -> about EUR 31,152/year; ordinary PIT-only net about EUR 2,105/month before EFKA, or about EUR 2,428/month if Article 5C applies.
- New risk flags: greece-efka-self-employed-contribution-gap; greece-article-5c-foreign-client-fit-gap.
- Sources added: src-294 through src-300; reused src-293 FX.
- Claims added: claim-greece-006 through claim-greece-011.
- Verification queue: 5 -> 7 pending/open; next should continue Tier-1-hint practical tax coverage, likely Cyprus 5.3.

## 2026-06-06 — run-056
- Italy: depth_score 1.5 -> 2.5; section 5.3 taxes now passed, while 5.1 remains partial.
- Added forfetario tax baseline: Agenzia forfetario rules + AA9/12 partita IVA route, INPS Gestione Separata 2026 rate, PwC residence/PIT/filing context, and a USD 3,000/month gross -> about EUR 1,950/month net worked example at the 15% forfetario rate.
- New risk flag: italy-worldwide-tax-and-reporting; Italy remains tax-workable under forfetario but rent and ordinary-status planning remain the bigger blockers.
- Sources added: src-287 through src-293.
- Claims added: claim-italy-006 through claim-italy-011.
- Verification queue: unchanged at 5 pending/open; next should continue Tier-1-hint low-depth practical sections, likely Greece 5.3 taxes.

## 2026-06-06 — run-055
- Spain: depth_score 1.5 -> 2.5; section 5.3 taxes now passed, while 5.1 remains partial.
- Added ordinary autonomo tax baseline: AEAT Form 036 + RETA registration, PIT planning scale, tax-residence rule, and a USD 3,000/month gross -> about EUR 1,800/month net worked example.
- New risk flag: autonomo-tax-social-security-burden; Spain remains legally attractive but budget-tight unless income rises or special-regime / employee structure is confirmed.
- Sources added: src-280 through src-286.
- Claims added: claim-spain-006 through claim-spain-011.
- Verification queue: unchanged at 5 pending/open; next should continue Tier-1-hint low-depth practical sections, likely Italy 5.3 taxes.

## 2026-06-05 — run-054
- Malaysia: depth_score 1.0 -> 1.5; section 5.2 climate now passed, while 5.1 remains partial.
- Added WeatherSpark Malaysia clearer-sky proxy source and claim; Kuala Lumpur, George Town, and Kuching are all only about 52-57 clearer-sky day-equivalent days/year.
- Resolved vq-078 for first-pass screening; Malaysia climate is now clearly hot/humid/rainy with low clear-sky reliability rather than just missing sunny-day data.
- Sources added: src-279.
- Claims added: claim-malaysia-007.
- Verification queue: 6 -> 5 pending/open; next can return to Tier-1-hint low-depth practical sections.

## 2026-06-05 — run-053
- Armenia: created profile and claims; depth_score 0 -> 1.5 (5.2 completed; 5.1 partial).
- Legalization first pass captured official Ukrainian visa-free scouting, temporary/permanent residence grounds, business-activity route baseline, fees, documents, and citizenship-lawful-residence baseline.
- Climate pass completed Yerevan, Gyumri, and Sevan with WeatherSpark clearer-sky proxies for Yerevan/Gyumri and flagged hot Yerevan summers plus cold inland winters.
- Sources added: src-274 through src-278.
- Claims added: claim-armenia-001 through claim-armenia-005.
- Verification queue: 3 -> 6 (added vq-086, vq-087, vq-088); next should return to low-depth country rotation or start deeper practical sections.

## 2026-06-05 — run-052
- Verification mode: resolved 7 legal/route blockers across Thailand, Indonesia, and Kazakhstan to safe operational baselines.
- Countries updated: Thailand, Indonesia, Kazakhstan (bridge/base vs settlement baselines clarified; unverified_count reduced).
- Sources added: 0
- Claims added: 0
- Verification queue: 10 -> 3 pending/open

## 2026-06-05 — run-051
- Kazakhstan: created profile and claims; depth_score 0 -> 1.5 (5.2 completed; 5.1 partial).
- Legalization first pass captured official Ukrainian visa-free scouting up to 90 days, arrival-notification rules, and CIS-citizen TRP purposes; durable foreign-client IT residence remains unproven.
- Neo Nomad / remote-work route is only secondary-sourced in this pass and queued for official-primary checklist verification.
- Climate pass completed Astana, Almaty, and Shymkent with WeatherSpark clearer-sky proxies and flagged cold continental winters as the main comfort risk.
- Sources added: src-267 through src-273.
- Claims added: claim-kazakhstan-001 through claim-kazakhstan-005.
- Verification queue: 7 -> 10 (added vq-083, vq-084, vq-085); next mode should be verification because the queue is at the active threshold.

## 2026-06-05 — run-050
- Indonesia: created profile and claims; depth_score 0 -> 1.5 (5.2 completed; 5.1 partial).
- Legalization first pass captured official VoA/e-VoA scouting eligibility for Ukraine/Poland and E33G remote-worker limited-stay route, but E33G requires US$60,000/year, above the couple's current income.
- Climate pass completed Jakarta, Surabaya, Bandung, and Bali/Denpasar with temperature/rainfall/humidity baselines plus WeatherSpark clearer-sky proxies for Jakarta, Surabaya, and Medan.
- Sources added: src-262 through src-266.
- Claims added: claim-indonesia-001 through claim-indonesia-005.
- Verification queue: 5 -> 7 (added vq-081, vq-082); next can continue depth-0 rotation with Kazakhstan.

## 2026-06-05 — run-049
- Verification batch: resolved 5 legal/route blockers (`vq-073`, `vq-074`, `vq-075`, `vq-076`, `vq-077`).
- Argentina now treats DN as bridge-only until a durable foreign-client IT temporary-residence category is confirmed.
- UAE now treats short entry and virtual-work micro-checklist gaps as travel/application-prep items; core route decision remains income-gated at USD 3,500/month.
- Malaysia now treats visitor-entry row capture as pre-travel only and DE Rantau as a 3-24 month bridge, not a proven PR/citizenship ladder.
- Sources added: none.
- Verification queue: 10 -> 5 pending/open; next can return to country-deep-dive rotation with Indonesia unless another priority appears.

## 2026-06-05 — run-048
- Thailand: created profile and claims; depth_score 0 -> 1.5 (5.2 completed; 5.1 partial).
- Legalization first pass captured 60-day Ukrainian visa-exempt scouting, DTV workcation as a 5-year multiple-entry bridge with 500,000 THB savings requirement, spouse/children dependent baseline, and BOI LTR Work-from-Thailand threshold caveats.
- Climate pass completed Bangkok, Phuket, and Chiang Mai with temperature/rainfall baselines and WeatherSpark clearer-sky day-equivalent proxies.
- Sources added: src-257 through src-261.
- Claims added: claim-thailand-001 through claim-thailand-006.
- Verification queue: 8 -> 10 (added vq-079, vq-080); next mode should be verification because the queue is at the active threshold.

## 2026-06-04 — run-047
- Malaysia: created profile and claims; depth_score 0 -> 1.0 (5.1 and 5.2 partial).
- Legalization first pass captured DE Rantau as an official remote-work bridge with USD 24,000/year tech-income threshold, spouse/children dependent baseline, 24-month cap, Entry Permit PR anchor, and Article 19 citizenship baseline.
- Climate first pass captured Malaysia / Kuala Lumpur hot-humid-rainy baselines and Penang / Johor Bahru comfort caveats; direct sunny-day counts remain queued.
- Sources added: src-251 through src-256.
- Claims added: claim-malaysia-001 through claim-malaysia-006.
- Verification queue: 5 -> 8 (added vq-076, vq-077, vq-078); next can continue depth-0 rotation with Thailand.

## 2026-06-04 — run-046
- Verification batch: resolved 5 legal/entry-protection blockers (`vq-051`, `vq-054`, `vq-062`, `vq-064`, `vq-066`).
- Georgia, Albania, Panama, North Macedonia, and Bosnia and Herzegovina now state conservative screening baselines: short entry is for scouting only, no uncaptured Ukraine protection bridge should be relied on, and ordinary residence must carry the plan.
- Sources added: none.
- Verification queue: 10 -> 5 pending/open; next can return to country-deep-dive rotation with Malaysia unless another priority appears.

## 2026-06-04 — run-045
- UAE: created profile and claims; depth_score 0 -> 1.5 (5.2 completed; 5.1 partial).
- Legalization first pass captured Ukrainian short-stay entry from Emirates, GDRFA virtual-work visa threshold/duration/family baseline, ICP Green Residence freelancer threshold, Golden Visa route-fit caveat, and nomination-only citizenship baseline.
- Climate pass completed Dubai, Abu Dhabi, Al Fujayrah, and Al Ain with winter/summer temperature baselines, humid heat caveats, and WeatherSpark clearer-sky day-equivalent proxies.
- Sources added: src-243 through src-250.
- Claims added: claim-uae-001 through claim-uae-006.
- Verification queue: 8 -> 10 (added vq-074, vq-075); next mode should be verification because the queue is at the active threshold.

## 2026-06-04 — run-044
- Argentina: created profile and claims; depth_score 0 -> 1.5 (5.2 completed; 5.1 partial).
- Legalization first pass captured the official DN transitory residence / TIE / extension route, Argentina residence-category baselines, rentista route-fit caveat, and updated Law 346 citizenship baseline.
- Climate pass completed Buenos Aires, Cordoba, and Mendoza with temperature/rain/humidity comfort notes and WeatherSpark clearer-sky day-equivalent proxies.
- Sources added: src-233 through src-242.
- Claims added: claim-argentina-001 through claim-argentina-006.
- Verification queue: 6 -> 8 (added vq-072, vq-073); next can continue depth-0 rotation with UAE.

## 2026-06-04 — run-043
- Verification batch: resolved 5 legal blockers (`vq-067`, `vq-068`, `vq-069`, `vq-070`, `vq-071`).
- Bosnia and Herzegovina: closed company/founder route fit to a high-burden local work/company baseline.
- Moldova: closed TP/DN blockers to ordinary-status-before-TP-expiry and DN-formula/PR-counting conservative baselines.
- Mexico: closed entry/temporary-residence blockers to visa-required and consular-solvency conservative baselines.
- Verification queue: 11 -> 6 pending/open.


# CHANGELOG

## 2026-06-03 — run-042
- Mexico: created profile and claims; depth_score 0 → 1.5 (5.2 completed; 5.1 partial).
- Legalization first pass captured Mexico's visa-required / visa-alternative framework, ordinary temporary-residence route, residence-card exchange, permanent-residence change after four years, and naturalization-by-residence procedure baseline.
- Climate pass completed Mexico City, Cancun, and Puerto Vallarta with temperature baselines, highland-vs-coast comfort split, muggy-day caveats, and WeatherSpark clearer-sky day-equivalent proxies.
- Sources added: src-226, src-227, src-228, src-229, src-230, src-231, src-232.
- Claims added: claim-mexico-001 through claim-mexico-006.
- Verification queue: 9 → 11 (added vq-070, vq-071); next mode should be verification because the queue is at or above the active threshold.

## 2026-06-03 — run-041
- Moldova: created profile and claims; depth_score 0 → 1.5 (5.2 completed; 5.1 partial).
- Legalization first pass captured temporary protection through 01 March 2027, provisional-stay categories, the official digital-nomad document list / income formula, and permanent-stay baselines with PR-counting caveats.
- Climate pass completed Chisinau, Balti, and Tiraspol with continental winter/summer baselines and WeatherSpark clearer-sky day-equivalent proxies.
- Sources added: src-219, src-220, src-221, src-222, src-223, src-224, src-225 (reused src-204).
- Claims added: claim-moldova-001 through claim-moldova-006.
- Verification queue: 7 → 9 (added vq-068, vq-069); next can continue depth-0 rotation with Mexico.

## 2026-06-03 — run-040
- Bosnia and Herzegovina: created profile and claims; depth_score 0 → 1.5 (5.2 completed; 5.1 partial).
- Legalization first pass captured 90/180 visa-free mechanics, temporary residence filing, work-permit / company-founder checklists, and permanent residence after five uninterrupted years; no DN route or Ukraine-specific bridge captured.
- Climate pass completed Sarajevo, Tuzla, and Mostar with temperature baselines, low muggy-day burden, and WeatherSpark clearer-sky day-equivalent proxies.
- Sources added: src-213, src-214, src-215, src-216, src-217, src-218 (reused src-204).
- Claims added: claim-bosnia-herzegovina-001 through claim-bosnia-herzegovina-006.
- Verification queue: 5 → 7 (added vq-066, vq-067); next can continue depth-0 rotation with Moldova.

## 2026-06-03 — run-039
- Mode: verification; resolved 5 pending items (`vq-022`, `vq-060`, `vq-061`, `vq-063`, `vq-065`) to conservative operational baselines.
- Romania DN core route, Paraguay residence/lawful-activity file, Panama remote-worker follow-on baseline, and North Macedonia self-employment baseline updated.
- Sources added: none.
- Verification queue: 10 → 5 pending/open items.
- Next: country-deep-dive rotation can resume; prioritize fresh depth-0 Bosnia and Herzegovina sections 5.1/5.2 unless accepted proposals appear.

## 2026-06-02 — run-038
- North Macedonia: created profile and claims; depth_score 0 → 1.5 (5.2 completed; 5.1 partial)
- Sources added: src-204, src-205, src-206, src-207, src-208, src-209, src-210, src-211, src-212
- Claims added: claim-north-macedonia-001 through claim-north-macedonia-006
- Verification queue: 8 → 10 (added vq-064, vq-065); next mode should be verification

## 2026-06-02 — run-037
- Panama: created profile and claims; depth_score 0 → 1.5 (5.2 completed; 5.1 partial)
- Sources added: src-197, src-198, src-199, src-200, src-201, src-202, src-203
- Claims added: claim-panama-001 through claim-panama-006
- Verification queue: 6 → 8 (added vq-062, vq-063)

## 2026-06-02 — run-036 — paraguay-legalization-climate

- Paraguay profile created from template.
- Paraguay: depth_score 0 → 1.5 (section 5.2 completed; section 5.1 advanced to partial).
- Legalization first pass captured Ukrainian tourist visa-free entry up to 90 days, the residence / lucrative-activity visa caveat, temporary residence up to 2+2 years, temporary-to-permanent category change, official fees, and constitutional naturalization after 3 years of radication.
- Climate pass completed Asuncion, Ciudad del Este, and Encarnacion temperature / comfort baselines and WeatherSpark clearer-sky day-equivalent proxies.
- Sources added: `src-190` … `src-196`.
- Claims added: `claim-paraguay-001` … `claim-paraguay-006`.
- Verification queue: 4 → 6 pending/open items (`vq-060`, `vq-061` added).
- Next: continue country-deep-dive rotation with Panama sections 5.1/5.2 while the queue remains below threshold.

## 2026-06-02 — run-035 — verification-batch

- Mode: verification; resolved 6 pending items (`vq-039`, `vq-052`, `vq-056`, `vq-057`, `vq-058`, `vq-059`).
- Portugal: depth_score 2.5 → 3.0 (section 5.5 rent completed with current T2/two-bedroom bands).
- Albania: depth_score 1.0 → 1.5 (section 5.2 climate completed with WeatherSpark clearer-sky proxies for Tirana, Durres, and Vlore).
- Slovenia: DN route operational core updated; current twice-net-salary screen is about EUR 3,357.62/month, above the couple's current budget.
- Georgia and Uruguay legal blockers closed to conservative operational baselines using existing official sources.
- Sources added: `src-187` … `src-189`.
- Verification queue: 10 → 4 pending/open items.
- Next: country-deep-dive rotation can resume; prioritize a fresh depth-0 Tier-2-hint country such as Paraguay, unless new accepted proposals appear.

## 2026-06-01 — run-034 — uruguay-legalization-climate

- Uruguay profile created from template.
- Uruguay: depth_score 0 → 1.5 (section 5.2 completed; section 5.1 advanced to partial).
- Legalization first pass captured Ukrainian visa-free entry, ordinary permanent residence, foreign-company / independent-worker means-of-life evidence, 6+6 month digital-nomad provisional identity bridge, and legal citizenship after 3 years with family or 5 years without family.
- Climate pass completed Montevideo, Salto, and Tacuarembo temperature / comfort baselines and WeatherSpark clearer-sky day-equivalent proxies.
- Sources added: `src-180` … `src-186`.
- Claims added: `claim-uruguay-001` … `claim-uruguay-006`.
- Verification queue: 8 → 10 pending/open items (`vq-058`, `vq-059` added).
- Next: continue country-deep-dive rotation with Paraguay sections 5.1/5.2 unless the queue rises above threshold.

## 2026-06-01 — run-033 — portugal-cost-rent

- Portugal: depth_score 1.0 → 2.5 (section 5.4 completed; section 5.5 advanced to partial).
- Cost-of-living pass added Lisbon, Porto, and Faro/Algarve monthly budget ranges, utilities, internet, transport, groceries, and a $3,000/month budget conclusion.
- Rent pass added working T2 planning bands, search-process notes, foreign-tenant document expectations, deposit/advance-rent rules, and a new `lisbon-rent-pressure` flag.
- Sources added: `src-176` … `src-179`.
- Verification queue: 7 → 8 pending/open items (`vq-057` added for exact Portugal T2 listing medians).
- Next: continue country-deep-dive rotation with Italy sections 5.3/5.4 unless the queue rises above threshold.

## 2026-06-01 — run-031 — albania-legalization-climate

- Albania profile created from template.
- Albania: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Legalization first pass opened the visa-free entry baseline, WAF-blocked official Ukraine/visa source gap, Type D + Unique Permit remote-worker route from 2025–2026 secondary sources, family/dependent baseline, and conservative no-TP-bridge caution.
- Climate first pass captured Tirana, Durrës, and Vlorë temperature / rainfall / sunshine-hour / comfort baselines; direct sunny/clear-day counts remain queued.
- Sources added: `src-164` … `src-170`.
- Claims added: `claim-albania-001` … `claim-albania-007`.
- Verification queue: 9 → 12 pending/open items (`vq-054` through `vq-056` added).
- Next: verification batch because the queue is above threshold.

## 2026-05-31 — run-030 — verification-turkey-climate-clearer-days

- Mode: verification; resolved Turkey climate blocker `vq-050` at medium confidence.
- Turkey: depth_score 1.0 → 1.5 (section 5.2 passed; section 5.1 remains partial).
- Added WeatherSpark clearer-sky day-equivalent proxies: Istanbul ~231 days/year and Izmir ~266 days/year; Antalya remains represented by ~2,865 annual sunshine hours.
- Sources added: `src-162`, `src-163`.
- Verification queue: 10 → 9 pending/open items.
- Next: continue verification, prioritizing Georgia legal blockers and older climate sunny-day gaps.

## 2026-05-31 — run-029 — georgia-legalization-climate

- Georgia profile created from template.
- Georgia: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Legalization first pass captured MFA entry portal anchor, 2025 Ukraine one-year visa-free baseline from secondary reporting, SDA residence-permit framework, work/entrepreneur permit, IT residence permit, family reunification, PR after 10 years, and ordinary citizenship after 10 consecutive years.
- Climate first pass captured Tbilisi, Batumi, and Kutaisi temperature / rainfall / humidity comfort baselines; direct sunny/clear-day counts remain queued.
- Sources added: `src-155` … `src-161`.
- Claims added: `claim-georgia-001` … `claim-georgia-007`.
- Verification queue: 7 → 10 pending/open items (`vq-051` through `vq-053` added).
- Next: verification batch because the queue reached threshold.

## 2026-05-31 — run-028 — verification-greece-turkey-legal-baselines

- Mode: verification; resolved 4 legal blockers (`vq-002`, `vq-047`, `vq-048`, `vq-049`).
- Greece: official MFA digital-nomad page now closes the core DN official-primary route/checklist anchor; consular micro-details remain application-prep checks.
- Turkey: DN operational core, no-Ukraine-TP-bridge baseline, and eight-year long-term-residence counting rules updated from PMM/GoTurkey sources.
- Sources added: `src-152`, `src-154`.
- Claims added: `claim-greece-005`, `claim-turkey-007` … `claim-turkey-009`.
- Verification queue: 11 → 7 pending/open items.
- Next: resume country-deep-dive rotation with Georgia sections 5.1 and 5.2.

## 2026-05-31 — run-027 — turkey-legalization-climate

- Turkey profile created from template.
- Turkey: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Legalization first pass captured MFA visa-scope baseline, official residence/e-ikamet filing anchors, Turkey temporary-protection framework caveat, and GoTurkey digital-nomad requirements: age 21-55, diploma, foreign employment/freelance evidence, and USD 3,000/month or USD 36,000/year income proof.
- Climate first pass captured Istanbul, Izmir, and Antalya temperature / sunshine-hours / humidity comfort baselines; direct sunny/clear-day counts remain queued.
- Sources added: `src-144` … `src-151`.
- Claims added: `claim-turkey-001` … `claim-turkey-006`.
- Verification queue: 7 → 11 pending/open items (`vq-047` through `vq-050` added).
- Next: verification batch because the queue is above threshold.

## 2026-05-30 — run-026 — verification-montenegro-serbia-legal-baselines

- Mode: verification; resolved 5 legal blockers (`vq-041` through `vq-045`).
- Montenegro: official GOV.me DN checklist/filing route captured; DN duration is 2+2 years with 6-month cooling-off, and family baseline covers spouses/minor children.
- Montenegro: TP bridge and PR-counting blockers closed to conservative operational baselines.
- Serbia: official MUP/Welcome to Serbia sources now confirm self-employment / independent-professional single-permit electronic filing and marriage/common-law family mechanics.
- Serbia: TP bridge / Polish-status blocker closed to conservative baseline: TP is protection only; ordinary Serbian residence is still needed.
- Sources added: `src-143`; claims added: `claim-montenegro-009` … `claim-montenegro-011`, `claim-serbia-009` … `claim-serbia-010`.
- Verification queue: 12 → 7 pending/open items.
- Next: resume country-deep-dive rotation with Turkey sections 5.1 and 5.2.

## 2026-05-30 — run-025 — serbia-legalization-climate

- Serbia profile created from template.
- Serbia: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Legalization first pass captured visa-free entry for Ukrainians, Serbian temporary-protection framework, Law on Foreigners temporary residence / single permits, PR after 3 years, and MFA citizenship baseline.
- Self-employment / digital-nomad route opened as a medium-confidence placeholder; official implementing checklist, threshold, and dependent mechanics queued for verification.
- Climate first pass captured Belgrade, Novi Sad, and Niš temperatures, humidity, precipitation, sunshine hours, and comfort caveats; direct sunny/clear-day counts remain queued.
- Sources added: `src-132` … `src-142`.
- Claims added: `claim-serbia-001` … `claim-serbia-008`.
- Verification queue: 9 → 12 pending/open items (`vq-044` through `vq-046` added).
- Next: verification batch because the queue is above threshold.

## 2026-05-30 — run-024 — montenegro-legalization-climate

- Montenegro profile created from template.
- Montenegro: depth_score 0 → 1.5 (section 5.2 passed; section 5.1 advanced to partial).
- Temporary protection captured from Montenegro MUP: protection for persons from Ukraine extended to 04 March 2027, with existing-document exchange / first-time application baseline.
- Digital-nomad route opened from official GOV.me portal plus a secondary 2026 checklist placeholder; official numeric threshold and dependent mechanics queued for verification.
- Climate first pass completed for Podgorica, Budva, and Herceg Novi, including January/July temperatures, sunshine hours, and sunny-day heuristics.
- Sources added: `src-123` … `src-131`.
- Claims added: `claim-montenegro-001` … `claim-montenegro-008`.
- Verification queue: 6 → 9 pending/open items (`vq-041` through `vq-043` added).
- Next: country-deep-dive rotation with Serbia sections 5.1 and 5.2 unless accepted proposals appear.

## 2026-05-30 — run-023 — verification-climate-clearer-days

- Mode: verification; resolved 5 climate sunny/clear-day blockers (`vq-014`, `vq-018`, `vq-025`, `vq-032`, `vq-040`).
- Cyprus, Malta, Romania, Bulgaria, and Slovenia: §5.2 advanced from partial to passed using WeatherSpark monthly clearer-sky percentages converted into annual day-equivalent proxies.
- Depth changes: Cyprus, Malta, Romania, Bulgaria, and Slovenia each +0.5 → 1.5.
- Sources added: `src-118` … `src-122`.
- Claims added: none.
- Verification queue: 11 → 6 pending/open items.
- Next: resume country-deep-dive rotation with Montenegro sections 5.1 and 5.2 unless accepted proposals appear.

## 2026-05-29 — run-022 — slovenia-legalization-climate

- Slovenia profile created from template.
- Slovenia: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Temporary protection captured from GOV.SI, including police registration, administrative-unit application, TP card as temporary residence, and post-TP 10-day ordinary-permit filing window.
- Digital-nomad residence captured from GOV.SI: foreign remote work, no Slovenian labour-market entry, up to 1 year, non-extendable, twice-average-net-salary formula, immediate family-reunification feature.
- Climate first pass for Ljubljana, Maribor, and Portorož/coast completed; direct sunny-day counts still missing.
- Sources added: `src-110` … `src-117`.
- Claims added: `claim-slovenia-001` … `claim-slovenia-008`.
- Verification queue: 9 → 11 pending/open items (`vq-039`, `vq-040` added).
- Next: verification batch because the queue reached threshold again.

## 2026-05-29 — run-021 — verification-slovakia-legal-baselines

- Mode: verification; resolved 2 Slovakia legal blockers (`vq-036`, `vq-037`).
- Slovakia: business/self-employed route now has an official-primary Ministry of Economy anchor for mandatory business-plan and real-business scrutiny.
- Slovakia: post-2027 TP bridge closed to conservative operational baseline: TP is automatically extended to 04 March 2027, but no captured ordinary-residence bridge.
- Sources added: `src-108`, `src-109`.
- Claims added: `claim-slovakia-008`, `claim-slovakia-009`.
- Verification queue: 11 → 9 pending/open items.
- Next: resume country-deep-dive rotation with Slovenia sections 5.1 and 5.2 unless accepted proposals appear.

## 2026-05-29 — run-020 — slovakia-legalization-climate

- Slovakia profile created from template.
- Slovakia: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Temporary protection captured from UNHCR Slovakia: eligibility, rights, work/self-employment access, and EU horizon through 04 March 2027.
- Business/self-employed residence captured from EU Immigration Portal: trade licence / Commercial Register mechanics, documents, fees, health-insurance and medical-report steps, up to 3-year validity.
- No captured dedicated digital-nomad visa; no captured Slovakia-specific TP-to-ordinary-residence bridge.
- Climate first pass for Bratislava, Košice, and Poprad completed (continental; 1,890–2,075 sunshine hours/year; direct sunny-day counts still missing).
- Sources added: src-100 … src-107.
- Claims added: claim-slovakia-001 … claim-slovakia-007.
- Verification queue: 8 → 11 pending/open items (`vq-036` through `vq-038` added).
- Next: verification batch because the queue reached threshold again.

## 2026-05-29 — run-019 — verification-closure

- Mode: verification; resolved 2 Hungary legal blockers (`vq-033`, `vq-034`).
- Hungary: post-2027 TP bridge closed to conservative operational baseline: no captured Hungary-specific bridge; plan ordinary status before TP expiry unless a later official transition appears.
- Hungary: White Card partner dependency clarified from OIF family-reunification guidance; White Card holders cannot sponsor family reunification.
- Claims added: `claim-hungary-008`, `claim-hungary-009`.
- Sources added: none (existing OIF/EU sources were sufficient for safe operational closure).
- Verification queue: 10 → 8 pending/open items.
- Next: country-deep-dive on Slovakia (sections 5.1, 5.2), unless accepted proposals appear or queue again reaches threshold.

## 2026-05-28 — run-018 — hungary-legalization-climate

- Hungary profile created from template.
- Hungary: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- White Card captured from OIF official-primary source: foreign remote work/company management only, no Hungarian gainful activity, EUR 3,000 net/month for 6 months and throughout stay.
- Guest self-employment captured as a heavier fallback: self-employment income above 24× minimum wage annually or business-organisation evidence; up to 3 years total validity.
- No captured Hungary-specific TP-to-ordinary-residence bridge after 04 March 2027; conservative baseline added.
- Climate first pass for Budapest, Debrecen, and Pécs completed (continental; 1,928–2,058 sunshine hours/year; direct sunny-day counts still missing).
- Sources added: src-092 … src-099.
- Claims added: claim-hungary-001 … claim-hungary-007.
- Verification queue: 7 → 10 pending/open items (`vq-033` through `vq-035` added).
- Next: country-deep-dive on Slovakia (sections 5.1, 5.2), unless verification queue crosses threshold.

## 2026-05-28 — run-017 — verification-closure

- Mode: verification; resolved 5 queue items (`vq-021`, `vq-027`, `vq-029`, `vq-030`, `vq-031`).
- Bulgaria: UNHCR Bulgaria TP pages captured (`src-089`, `src-090`); TP registration/rights and conservative no-bridge baseline added.
- Poland: family-reunification via existing `karta pobytu` resolved to spouse/marriage baseline with income/document guidance (`src-091`).
- Romania: D/AC commercial-activity route resolved as company/investment route, not a simple solo IT-freelancer fallback.
- Sources added: `src-089`, `src-090`, `src-091`.
- Claims added: `claim-bulgaria-009` … `claim-bulgaria-011`, `claim-poland-009` … `claim-poland-010`, `claim-romania-009`.
- Verification queue: 12 → 7 pending/open items.
- Next: country-deep-dive on Hungary (sections 5.1, 5.2), unless accepted proposals appear.

## 2026-05-28 — run-016 — bulgaria-legalization-climate

- Bulgaria profile created from template.
- Bulgaria: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Self-employment route captured as the most relevant ordinary path for a remote IT worker: Employment Agency permit → Type D visa → residence permit; 1-year renewable up to 3 years; then 1-month exit required.
- No captured dedicated digital-nomad visa; no captured Bulgaria-specific TP-to-ordinary-residence bridge.
- Citizenship: 5 years residence + Bulgarian language; dual citizenship restricted for naturalized non-EU citizens unless reciprocity agreement or Bulgarian origin.
- Climate first pass for Sofia, Plovdiv, and Varna completed (continental to humid subtropical; 2,260–2,340 sunshine hours/year).
- Sources added: src-079 … src-088.
- Claims added: claim-bulgaria-001 … claim-bulgaria-008.
- Verification queue: 8 → 12 pending/open items (`vq-029` through `vq-032` added).
- Next: country-deep-dive on Hungary (sections 5.1, 5.2) or verification if queue crosses threshold.

## 2026-05-27 — run-015 — verification-closure

- Mode: verification; resolved 5 queue items (`vq-010`, `vq-023`, `vq-024`, `vq-026`, `vq-028`).
- Romania: UNHCR Temporary Protection page captured (src-076); TP rights, registration procedure, permit validity, and travel rules added to profile.
- Romania: 4 verification blockers closed to conservative operational baselines (TP bridge, DN counting, unmarried partner eligibility).
- Portugal: Lisbon and Porto sunshine percentages captured from Wikipedia climate tables (src-077, src-078); vq-010 partially closed (Faro remains open).
- Sources added: src-076, src-077, src-078.
- Verification queue: 13 → 8 pending/open items.
- Next: country-deep-dive on Bulgaria (sections 5.1, 5.2) or Romania deep-dive on remaining blockers (vq-022, vq-025, vq-027).

## 2026-05-27 — run-014 — romania-legalization-climate

- Romania profile created from template.
- Romania: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Digital-nomad visa captured: Law 22/2022, €3,300/month income, 12+12 months, no Romanian tax (aggregator source; official-primary confirmation queued).
- OUG 194/2002 (consolidated April 2026) captured as official-primary anchor: defines "nomad digital", visa types, family reunification (Art. 62), EU long-term residence conditions (Art. 71).
- Ukrainians exempt from short-stay visa (MAE Annex 2) confirmed.
- Climate first pass for Bucharest, Cluj-Napoca, and Timișoara completed (continental; cold winters; ~2,030–2,130 sunshine hours/year).
- Sources added: src-068 … src-075.
- Claims added: claim-romania-001 … claim-romania-008.
- Verification queue: 6 → 13 pending/open items (7 new Romania items: `vq-022` through `vq-028`).
- Next: country-deep-dive on Bulgaria (sections 5.1, 5.2) or verification if queue crosses threshold.

## 2026-05-27 — run-013 — poland-legalization-climate

- Poland profile created from template.
- Poland: depth_score 0 → 1.5 (section 5.2 completed; section 5.1 advanced to partial).
- CUKR card (3-year temporary residence for former Ukrainian TP holders) captured from official-primary UdSC sources.
- Family-reunification potential via partner's existing Polish `karta pobytu` flagged for verification.
- Climate first pass for Warsaw, Krakow, and Wroclaw completed.
- Sources added: src-062 … src-067; src-002 usage extended to Poland.
- Claims added: claim-poland-001 … claim-poland-008.
- Verification queue: 5 → 6 pending/open items (`vq-021` added: Poland family-reunification rules for unmarried partners).
- Next: country-deep-dive on Romania (sections 5.1, 5.2) or verification if queue crosses threshold.

## 2026-05-26 — run-012
- Mode: verification; resolved 5 queue items (`vq-004`, `vq-008`, `vq-013`, `vq-017`, `vq-019`).
- Spain, Portugal, Cyprus, and Malta: post-2027 TP bridge blockers closed to conservative "no captured bridge; plan ordinary route before TP expiry" baselines.
- Czech Republic: official-primary special long-term residence anchor added; PR counting rule updated (special residence counts full, prior TP counts one-half).
- Sources added: src-061.
- Verification queue: 10 → 5 pending/open items.

## 2026-05-26 — run-011
- Czech Republic profile created from template.
- Czech Republic: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Sources added: src-053 … src-060; src-002 usage extended to Czech Republic.
- Claims added: claim-czech-001 … claim-czech-005.
- Verification queue: 8 → 10 pending/open items (`vq-019`, `vq-020` added).
- Next: verification pass because the queue has reached the scheduled-run threshold.

## 2026-05-26 — run-010
- Malta profile created from template.
- Malta: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial).
- Sources added: src-046 … src-052; src-002 usage extended to Malta.
- Claims added: claim-malta-001 … claim-malta-005.
- Verification queue: 6 → 8 pending/open items (`vq-017`, `vq-018` added).
- Next: country-deep-dive on Czech Republic (sections 5.1, 5.2) unless queue crosses verification threshold.

## 2026-05-26 — run-009
- Mode: verification; resolved 5 queue items (`vq-003`, `vq-011`, `vq-012`, `vq-015`, `vq-016`).
- Greece: depth_score 1.0 → 1.5; §5.2 climate passed using Current Results clear-sky statistics.
- Croatia: depth_score 1.0 → 1.5; §5.2 climate passed using direct sunshine-day counts.
- Sources added: src-044, src-045.
- Verification queue: 11 → 6 pending/open items.

## 2026-05-24 — run-001 — bootstrap-v2

- Vault structure created from scratch
- Foundational docs in place: `criteria.md` v2.0.0, `vault-protocol.md` v1.0.0, `CONTEXT.md` v1.0.0
- 33 countries indexed with tier hints in `countries.yml` and `state.json`
- All boilerplate files and 4 validator scripts created
- Validators passed
- No research performed yet
- Next: country-deep-dive on Greece (sections 5.1, 5.2)

## 2026-05-24 — run-002 — greece-legalization-climate

- Greece profile created from template
- Greece: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial)
- Sources added: src-001 … src-010
- Claims added: claim-greece-001 … claim-greece-004
- Verification queue: 0 → 3
- Next: verification pass on DN primary checklist, Polish karta pobytu interaction, and sunny-day counts

## 2026-05-24 — run-003 — spain-legalization-climate

- Spain profile created from template
- Spain: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial)
- Sources added: src-011 … src-016
- Claims added: claim-spain-001 … claim-spain-005
- Verification queue: 3 → 6
- Next: country-deep-dive on Portugal (sections 5.1, 5.2)

## 2026-05-24 — run-004 — portugal-legalization-climate

- Portugal profile created from template
- Portugal: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial)
- Sources added: src-017 … src-024
- Claims added: claim-portugal-001 … claim-portugal-005
- Verification queue: 6 → 10
- Next: verification pass across Greece / Spain / Portugal blockers because queue threshold reached 10

## 2026-05-25 — run-005 — verification-pass-legalization-climate

- Verification queue: 10 → 5
- Spain: depth_score 1.0 → 1.5 (section 5.2 climate closed to DoD with direct clear-day counts)
- Portugal: official-primary AIMA remote-work residence filing route captured
- Poland-residence interaction clarified for Greece, Spain, and Portugal baseline planning
- Sources added: src-025, src-026
- Facts verified: 5

## 2026-05-25 — run-006 — italy-legalization-climate

- Italy profile created from template
- Italy: depth_score 0 → 1.5 (section 5.2 completed; section 5.1 advanced to partial)
- Sources added: src-027 … src-034
- Claims added: claim-italy-001 … claim-italy-005
- Verification queue: 5 → 7
- Next: country-deep-dive on Cyprus (sections 5.1, 5.2)

## 2026-05-25 — run-007 — cyprus-legalization-climate

- Cyprus profile created from template
- Cyprus: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial)
- Sources added: src-035 … src-039
- Claims added: claim-cyprus-001 … claim-cyprus-005
- Verification queue: 7 → 9
- Next: country-deep-dive on Croatia (sections 5.1, 5.2)

## 2026-05-25 — run-008 — croatia-legalization-climate

- Croatia profile created from template
- Croatia: depth_score 0 → 1.0 (sections 5.1 and 5.2 advanced to partial)
- Sources added: src-040 … src-043
- Claims added: claim-croatia-001 … claim-croatia-005
- Verification queue: 9 → 11
- Next: verification mode because queue threshold is now reached
## 2026-06-01 — run-032
- Verification: closed climate sunny/clear-day blockers for Czech Republic, Hungary, Slovakia, Serbia, and Georgia using WeatherSpark clearer-sky day-equivalent proxies.
- Depth_score: Czech Republic 1.0 → 1.5; Hungary 1.0 → 1.5; Slovakia 1.0 → 1.5; Serbia 1.0 → 1.5; Georgia 1.0 → 1.5.
- Sources added: src-171, src-172, src-173, src-174, src-175.
- Verification queue: 12 → 7 (resolved vq-020, vq-035, vq-038, vq-046, vq-053).
