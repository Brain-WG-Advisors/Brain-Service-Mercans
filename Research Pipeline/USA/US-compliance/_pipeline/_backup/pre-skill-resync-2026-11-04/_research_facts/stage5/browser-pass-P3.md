# Browser pass P3 - 2026-11-02

Worker P3, per `_prompts/browser-pass-brief.md`. Targets: the state 2026 research blockers in `_qa/CCG-review-r1.json` routed to agent 2 (FED skipped). VPN off (Brazil exit). Own Chrome tab, closed at the end. No CAPTCHA, challenge or login was bypassed.

Shard: `00-official-sources/_register-shards/S5B-P3.csv`, **22 rows, 20 columns**. IDs use the **3xx range** (`US-{JUR}B5-301…`) so they cannot collide with P1/P2/P4 (P2 already holds US-COB5-001..003, P1 US-DCB5-001..002, etc.). Page texts and files are in `00-official-sources/ccg-sources/{JUR}/*_2026-11-02.*`, each with a `.txt` whose first line is `URL: … | read 2026-11-02 in Chrome (…)`.

About 62 page loads used (Chrome and curl together; budget 90). I stopped early: what was left are hosts already known to block a Brazil exit.

**Method notes**
- Chrome let the first page-text download through and then **silently blocked the rest**. So the local copy of each page is (a) the same URL fetched by curl when curl gets 200 (most hosts did), or (b) a verbatim excerpt of the Chrome page text, saved as `*_browser_2026-11-02.txt` (Oakland, DC LIMS, Michigan, mass.gov). Case (b) is stated in each register row.
- URLs were found with web search, not by guessing paths. Numbers come only from the authority page or document.

## Summary: what closed, what stayed open

| QA finding (RQ) | Key | Result | Register |
|---|---|---|---|
| RQ-478 | `ca.local_minwage.hourly` | **Mostly closed.** LA City 17.87 (2025-07-01) / 18.42 (2026-07-01). LA County unincorporated 17.81 to 18.47 (2026-07-01). SF 19.18 / 19.61 (2026-07-01). San Diego 17.75 (2026-01-01) / 18.35 (2027-01-01). Berkeley 19.18 / 19.61 (2026-07-01). Oakland 17.34 (2026-01-01). **San Jose blocked** (Akamai, Chrome and curl). | US-CAB5-303..308 |
| RQ-479 | `ca.industry_minwage.fast_food_health_care` | **Closed.** Fast food is 20.00 from 2024-04-01, and the DIR page shows no later Council increase. Health care: the full SB 525 schedule for 4 facility tiers (for example large systems 24, then 25 from 2026-07-01; clinics 21, then 22 from 2026-07-01). State minimum 16.90 for 2026. | US-CAB5-301, -302 |
| RQ-490 | `co.famli.split.next_year` | **Closed on the rate.** CDLE bulletin 2026-09-30: **0.86% from 2027-01-01** (0.88% in 2026). The bulletin does not restate the split. The 50% employee cap and the under-10-employee employer exemption stay on US-COB5-003 (P2). Employee maximum 0.43% is derived. | US-COB5-301 |
| RQ-491 | `co.local_minwage.other_cities` | **Partly closed.** Boulder County (unincorporated) 16.82 (2026) / 17.43 (2027). City of Boulder 16.82 (2026) / 18.17 (2027) per Ord. 8664; no later City amendment found. **Edgewater blocked** (Akamai 403, Chrome and curl). **Denver** not retried (P2: WAF). | US-COB5-302, -303 (supersede US-COS5-011 for these localities) |
| RQ-146 | `dc.live.fy2027_bsa_permanent` | **Closed (status).** B26-0661 was enacted without the Mayor's signature as **D.C. Act 26-418** (2026-08-14, 73 DCR 11735). It went to Congress 2026-08-20 and became **D.C. Law 26-189, effective 2026-10-02** (73 DCR 13120). Not checked: whether the permanent text matches Act 26-416 secs. 4051-4053 / 7112 (214 pages not read). | US-DCB5-301 |
| RQ-138 | `dc.wh.method` | Not retried (P1 confirmed it absent; nothing new). | — |
| RQ-147 | `de.wh.w4_2020_mapping` | **Closed. This contradicts a current fact.** DOR FAQ: an employer **may not** accept a 2020-or-later federal W-4 for Delaware withholding; the employee files the **Delaware W-4**. A pre-2020 federal W-4 may still be relied on. The fact `de.wh.certificate` = "federal W-4" (US-DES5-008) needs correcting. | US-DEB5-301 |
| RQ-272 | `ny.pit.supplemental.local_rates` | **Closed.** NYS-50-T-NYC (1/26): 4.25%. NYS-50-T-Y (1/26): Yonkers resident 1.95975%, nonresident 0.50%. Both from tax.ny.gov, effective 2026-01-01 to 2026-12-31. | US-NYB5-301, -302 (supersede US-NY-011) |
| RQ-337 | `tx.report.ui.enhanced_fields_layout` | **Closed as "not yet mandatory".** TWC proposed 40 TAC 815.107 (51 TexReg 5161, 2026-08-07) with 6 fields: wages, industry, occupation field, FT/PT, county of primary employment, remote status. Comments closed 2026-09-07. **No adoption** in the Texas Register adopted-rules issues of 09-25 to 10-30. So no field and no start quarter is binding on 2026-11-02. The TWC layout (twc.texas.gov) is geo-blocked. | US-TXB5-301 |
| RQ-203 | `il.leave.cook.paid_leave` | **Closed (FAQ level).** Accrual is 1 h per 40 h, for any reason. Carry-over cap at least 40 h. Payout at separation only if the leave sits in a PTO/vacation bank (within 15 days). Front-loading is allowed. The County ordinance does not apply in Chicago. Rules approved 2025-04-10 are listed but not read. | US-ILB5-301 |
| RQ-202 | `il.leave.chicago.paid_leave.payout` | **Not tried.** chicago.gov is Akamai-blocked (P2). | — |
| RQ-029 | `mi.local.cities.rates` | **Census closed, rates open.** Treasury lists 24 cities: Detroit (Treasury) plus 23 that administer their own tax (named in the row). Rates and forms sit on each city's own site, which is outside the budget. | US-MIB5-301 |
| RQ-255 | `ma.report.w2.due_date_conflict` | **Narrowed.** The "Feb 28 paper / Mar 31 electronic" dates come from **Directive 07-2 (2007)**. 830 CMR 62B.2.1(d) fixes **Jan 31 for the employee statement** but sets no deadline for filing with DOR. The DOR W-2 page (updated 2026-01-30) says Jan 31. No TIR or Directive formally replacing 07-2 was found. | US-MAB5-301, -302 |
| RQ-250 | `ma.pit.conformity.items` | Not reached (budget went to the due-date conflict). | — |
| RQ-118 | `nm.labour.minwage.local.other` | **Closed for 2026.** Santa Fe County (unincorporated) 15.40, tipped base 4.62, from 2026-03-01 (2025: 15.00 / 4.50). The 2027 rate comes in March 2027. | US-NMB5-301 |
| RQ-388 | `wv.pit.tables.start_date` | **Still open, now sourced.** WV Tax Division: SB 392 signed 2026-03-31; 11-21-4j effective 2026-06-12 with a 5% cut retroactive to 2026-01-01; IT-100.2A dated March 2026. Neither document states when employers must switch or whether a catch-up applies. | US-WVB5-301 (partial) |
| RQ-390 | `wv.pit.local.service_fees` | **Lead only (not registered).** The WVU Shared Services page compiles the ordinances: Charleston 3.00, Chester 2.00 (nonresidents), Fairmont 2.00 (nonresidents), Huntington 5.00, Parkersburg 2.50, Romney 1.00, Wheeling 2.00 per week. WVU is not the levying authority, so these stay tier C. The wheelingwv.gov regulations PDF returns 403. | — |
| RQ-391 | `wv.ui.sb1053_fee` | No WorkForce WV notice found by search. Open. | — |
| RQ-315 | `sc.pit.tables.post_act110` | **Confirmed still open.** dor.sc.gov still serves WH-1603F 2026 **Rev. 11/4/25** (pre-Act 110: 3% / 6.0%). WH1603F_2027.pdf returns 404. File saved for evidence: `SC/SC_DOR_WH-1603F_2026_Rev-11-4-25_2026-11-02.pdf` (md5 1257ffc4dd0c2709ed70b638bfb27d56); no new row. | — |
| RQ-463 | `ar.wh.formula.switch_date` | No change. The DFA formula says only "Effective 01/01/2026" (the file held is unchanged; md5 ed3e83fc…). Open. | — |
| RQ-458 | `al.local.occupational_tax.census` | **Lead only.** The Alabama League of Municipalities survey lists 25 municipal occupational taxes (Attalla 2% … Tuskegee 2%; Opelika 1.5%, Goodwater 0.75%, Red Bay 0.5%). The League is an association and disclaims accuracy, so this is tier C and not registered. Saved as `AL/AL_League-of-Municipalities_tax-rates_LEAD-tierC_2026-11-02.html`. Auburn's site timed out again (curl 000). | — |
| RQ-227 | `ky.local.occupational_tax.census` | **Open.** No state list exists. KACo (an association) publishes a 2026 county data brief, but the download failed and it would be tier C anyway. | — |
| RQ-156 | `fl.sui.wages.401k_deferral` | **Open.** RT-6 instructions (rt6n.pdf) do not mention 401(k), 403(b), deferred compensation or cafeteria plans. The DOR tutorial rtPart4.pdf has no text layer. | — |
| RQ-189 | `id.wh.certificate.current_edition` | **Blocked.** tax.idaho.gov returns a Chrome error page and curl times out (2 attempts). | — |
| RQ-308 | `ri.records.2026_version` | **Blocked.** webserver.rilegislature.gov does not load in Chrome and curl times out (2 attempts). | — |
| RQ-352 | `va.ui.pool_cost_and_new_employer` | **Blocked.** vec.virginia.gov returns F5 "URL rejected" 403 in Chrome and 403 in curl. | — |
| RQ-497 | `ct.wh.tables.per_period` | **Not an access gap.** IP 2026(1) is already held (`pdfs/CT/`, md5 a64b2bbb…). Parsing the pp. 31+ tables is hunter/builder work. | — |
| RQ-021 / RQ-236 / RQ-237 / RQ-165 / RQ-343 / RQ-398 | ME UPAF, LA conformity and day-31, GA RS layout, UT Pub 14, WY rates | **Not retried.** maine.gov is CloudFront geo-blocked and revenue.louisiana.gov is behind Cloudflare (P2). GA is timing, not access (P2). UT and WY were already done by P1 with no result. These need a US exit or later publication. | — |

## Points for the orchestrator / builder (data, not edits)
1. **DE contradiction.** `de.wh.certificate` and US-DES5-008 say "federal W-4". DOR says a 2020+ federal W-4 is not acceptable and the DE W-4 is required. The fact needs correcting before the CCG re-assembles.
2. **CO FAMLI 2027.** The rate is 0.86% (A.3 bulletin). Keep the 50/50 cap and the small-employer rule on US-COB5-003. Read 7 CCR 2702 if an A.1 split is wanted.
3. **TX.** The 815.107 fields are proposed only. Configure nothing as mandatory. Recheck the Texas Register adopted-rules issues from November 2026 on.
4. **DC.** The permanent BSA is Law 26-189 (in force 2026-10-02). A text comparison with Act 26-416 (tax secs. 7111-7113, PFL 4051-4053) is still needed before the "survives 2026-11-11" question can be marked fully closed.
5. **City of Boulder 2027 (18.17)** comes from the City's Ord. 8664 page; the County is lower (17.43). Search found no City amendment.

## Files written
- Shard: `00-official-sources/_register-shards/S5B-P3.csv` (22 rows).
- Sources: CA (11 files), CO (4), DE (1), DC (1), IL (2), MA (2), MI (1), NM (2), NY (2), SC (1), TX (1), WV (2), AL (1 tier-C lead), each with a `.txt`.
- Not touched: legal-basis-register.csv, facts files, MANDATE.md, manifest.
