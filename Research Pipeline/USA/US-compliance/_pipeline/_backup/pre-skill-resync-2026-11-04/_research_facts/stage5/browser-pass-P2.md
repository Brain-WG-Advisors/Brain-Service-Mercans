# Browser pass P2 — ACCESS gaps (2026-11-02)

Worker P2, Chrome (Claude in Chrome), own tab only (closed at the end). Brief: `_prompts/browser-pass-brief.md`. Roughly 78 page reads. I stopped at the budget.
Shard: `00-official-sources/_register-shards/S5B-P2.csv`, with 18 rows (US-AZB5-001..006, US-COB5-001..003, US-TNB5-001..002, US-VTB5-001..003, US-PAB5-001, US-NMB5-001..002, US-ARB5-001). Page texts and files are in `00-official-sources/ccg-sources/{JUR}/*_2026-11-02.*`.

**Key finding on access.** Chrome clears WAF/bot 403s on many hosts (azica, des.az.gov, cdle, famli, tn.gov, labor/tax.vermont.gov, vermonttreasurer, pittsburghpa, lascruces, bernco, arkleg). It does **not** clear the following:
- country geo-blocks (CloudFront "block access from your country": maine.gov, twc.texas.gov, dew.sc.gov, publications.tnsosfiles.com);
- Cloudflare hard blocks (capitol.hawaii.gov, revenue.louisiana.gov, laworks.net);
- Akamai/Imperva blocks (chicago.gov, labor.mo.gov, denvergov.org);
- network timeouts (in.gov, apps.legislature.ky.gov).

These need a US exit (VPN). I did not try any challenge bypass. Two Cloudflare "verifying" interstitials (azica.gov, lascruces.gov) cleared on their own after a wait, with no interaction.

## Results per target

| JUR | URL | Result | Rows | Closes |
|---|---|---|---|---|
| AZ | azica.gov/labor-minimum-wage-main-page | read | — | page lists 2025/2026 posters only |
| AZ | azica 2026 poster PDF | read (downloaded) | US-AZB5-001 | 2026 = **15.15** confirmed; tip credit $3.00. Supersedes US-AZS5-028 (2026 part) |
| AZ | azica 2027 poster (`/2026-09/2027…ACT_1.pdf`, guessed path, HTTP 200) | read in viewer (screenshot; Chrome blocked the 2nd download) | US-AZB5-002 | 2027 = **15.65** confirmed. Supersedes US-AZS5-028 (2027 part). AZ open item 1 closed |
| AZ | flagstaff.az.gov (via site search) → /3520/Minimum-Wage | read | US-AZB5-003 | Flagstaff **18.35 (2026) / 18.95 (2027)**, no tip credit. AZ open item 2 closed |
| AZ | des.az.gov unemployment-employer + schedule + completing-reports + UIOF | read | US-AZB5-004..006 | UC-018 due dates, penalties, format rules (AZ open item 3, except the separation notice); UIOF 3.15% 2027 agency confirmation (US-AZR3-004); UIOF not FUTA-creditable |
| CO | cdle …/minimum-wage | 404 (page moved) | — | — |
| CO | adopted_2026_pay_calc_order….docx | read (downloaded) | US-COB5-001 | 2026 values. **The PAY CALC does not list local minimum wages** (Rule 2.2 points to coloradolaborlaw.gov), so Edgewater/Boulder stay open |
| CO | cdle Labor Rules page → proposed_2027_pay_calc_order (9.30.2026) | read (downloaded) | US-COB5-002 (status proposed) | state 2027 **15.71** / tipped 12.69 / minors 13.36 / EAP $1,151.23 a week; replaces tier-B US-COS5-011 (state part). Adoption not yet posted (hearing 11/2/2026) |
| CO | famli.colorado.gov/employers/premiums | 404 → read /employers | US-COB5-003 | 2026 0.88% (0.44/0.44), small-employer rule, SS wage cap, 1.2% cap. 2027 not on page |
| CO | denvergov.org Denver Labor minimum wage | blocked (WAF "request was rejected") | — | Denver 2027 stays open |
| CO | sos.state.co.us CCR | not tried (budget) | — | — |
| FL | floridajobs.org minimum-wage | "resource removed or renamed" (moved) | — | no change; FL rests on the constitution (US-FLS5-001/002) |
| GA | dor.georgia.gov/federal-format-layout | read: only Federal_Format_Specs.pdf (unchanged) | — | TY2026 layout still not posted (timing, not access) |
| HI | capitol.hawaii.gov SB3125_CD2 | Cloudflare hard block | — | HRS 235-2.3, 392-4/5 not tried (same host) |
| IL | chicago.gov paid leave FAQ PDF | Akamai Access Denied | — | the minimum wage FAQ (same host) was not tried |
| IL | cookcountyil.gov paid leave | 8 guessed paths 404; site search JS-only | — | open |
| IN | iga.in.gov 2026 code (SPA + PDF) | SPA hangs / 404 | — | open |
| IN | in.gov/dwd rate page | connection error page | — | WH-1 XML schema not reachable (same host) |
| KY | apps.legislature.ky.gov | connection error | — | KRS 405.465, 40 KAR 1:410 open |
| LA | revenue.louisiana.gov FAQ; laworks.net | Cloudflare hard block | — | L-4 open |
| ME | maine.gov minimum wage FAQ | CloudFront geo-block | — | the whole maine.gov host stays a gap |
| MO | labor.mo.gov/DLS/MinimumWage | Imperva "Error 16" | — | dor/dss not tried (same state WAF) |
| TN | publications.tnsosfiles.com pc0617.pdf | CloudFront 403 | — | PC 617 stays MANUAL (US-TNS5-015) |
| TN | tn.gov BWC 2026 legislative changes | read | US-TNB5-001 | TN Q2: no payroll withholding change; WC benefit limits 2026-27 |
| TN | tn.gov DLWD child labor | read | US-TNB5-002 | TN Q8 closed |
| TX | twc.texas.gov your-tax-rates | CloudFront geo-block | — | — |
| TX | 40 TAC 815.106/.107 (new SOS Appian portal) | portal error (needs record id) | — | open |
| VT | labor.vermont.gov UI tax rates | read | US-VTB5-001 | base 15,400; new-employer rate 1% (from 2026-07-01, per page); schedules table. **Schedule in force still not stated** (Q4 open) |
| VT | 2027 minimum wage / 2027 UI base press releases | 404 (not published at the guessed slugs); /newsroom errors | — | 2027 values still open (timing) |
| VT | tax.vermont.gov/business/withholding | read | US-VTB5-002 | deposits, WHT-436/434, e-file triggers, 30-day remote rule |
| VT | vermonttreasurer.gov/node/4603 (VT Saves) | read | US-VTB5-003 | **employers with 2+ W-2 employees** (not 5); penalties $20 → $75 from 2026-10-01. VT Q11 closed except the default rate |
| PA | pittsburghpa.gov (old URLs 404; found via site search) | read; ordinance PDF downloaded, pp.2-4 rendered and transcribed | US-PAB5-001 | Pittsburgh PSDA from 2026-01-01: 1 h per 30 h, cap 72 h (15+) / 48 h (<15), use from day 90, carryover rules |
| PA | Philadelphia Code 9-4100 (amlegal) | host reachable; node id redirects to overview; the search did not render results | — | open (needs a manual click path) |
| NM | lascruces.gov 2026 notice | read (interstitial cleared on its own) | US-NMB5-001 | **13.01 / tipped 5.20 (2026); 13.47 / 5.39 (2027)** |
| NM | bernco.gov workplace postings | read | US-NMB5-002 | county 10.95 overridden by state 12.00; tipped $3 |
| SC | dew.sc.gov tax-rate-information | CloudFront geo-block | — | — |
| AR | myworkers.ocse.arkansas.gov PDF | 403 | — | open |
| AR | arkleg Act 1 of 2026 S1 | read (downloaded) | US-ARB5-001 | statute text for 3.7% top rate (US-ARS5-005/-013); AR-OQ-1 (withholding start date) is not in the Act |

**Not attempted (budget or known-unreachable class):**
- MN uimn (curl 000), MT *.mt.gov (DNS), NE (DNS), RI webserver.rilegislature.gov (curl 000), ID (timeouts), AK akleg (000), WV code (non-US redirect to fbi.gov): all are network/geo classes that Chrome without a VPN would not fix.
- Also not attempted: NJ lis.njleg (JS gateway), NV Labor Commissioner PDFs (captcha, excluded by the brief), MS LexisNexis, KS/OK/NC/ND/SD/WI/IA/DE/MD remaining items, CA city list / DE 9C, HI HRS sections, Chicago minimum wage FAQ.

## Notes for the synthesis
- **AZ:** the 2027 poster is not yet linked from the ICA page. Its PDF metadata title reads "2024 …", but the printed text is 2027 / $15.65.
- **AZ:** the DES UIOF page names the paper report "UIT-0018F", while the completing-reports page names it "UC-018". Keep both names.
- **CO:** ACCESS-GAPS called the PAY CALC Order "the official list of local minimum wages". It is not one, so the local rates need coloradolaborlaw.gov or each city.
- **CO:** US-COB5-002 is a proposed rule. Confirm adoption (expected after the 11/2/2026 hearing) before it is used as final.
- **VT:** the VDOL page dates the 1% new-employer rate to "Beginning July 1, 2026", while Handbook 06/26 says July 1, 2004. The rate is the same either way.
- **Shared scratchpad:** an `r.json` there was reused by another process. For a moment it caused a duplicate append, which I removed: the shard has unique ids, 18 rows.
