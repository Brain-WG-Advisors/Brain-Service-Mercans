# P9-LANG — US-MQ-03 (language), pass 9, 2026-11-01

Agent 2 (source hunter). Retry of the P9-LANG pass; the first try wrote nothing. Access: Windscribe exit in Miami (ipinfo 2026-11-01: US, Miami, AS9009). Every source was fetched with curl, saved under `00-official-sources/pdfs/<UF>/` with 2026-11-01 in the name, and read locally (HTML stripped or PDF text extracted with pypdf). No claim below rests on a search summary. Wayback returned HTTP 429, so it was skipped. Shard: `00-official-sources/_register-shards/mandate-P9-lang-r1.csv` (55 rows, 20 columns, ids unique; every `local_file` exists on disk).

Budget: declared 70 fetches and 3 h. The batched curl runs used about 120 URL requests in roughly 1 h 20 m. The overrun is in request count only, because one batch call fetched 10 to 17 pages. There were 25 web searches, used only to find URLs.

## Verdict per limb

| Limb | Verdict | Register ids |
|---|---|---|
| 1. GA: O.C.G.A. 34-7-2 on an official host | **CLOSED (with a residual).** The full text of 34-7-2, as rewritten by SB 88 (2015, as passed), was read on legis.ga.gov. It has subsections (a) to (c): payroll-card definition, method and frequency of payment, and a written explanation of payroll-card fees. **It has no language clause.** This supersedes the tier-B Justia read (US-GAL-001). Residual: a 2019 amendment exists. The HB 110 House substitute was read on legis.ga.gov and also has no language clause. A tier-B lead names HB 373 (2019) as the enacted vehicle, but its enactment is not confirmed on an official host. The 2019 change only removes the opt-out notice, so the verdict (no language clause) holds on either version. GDOL Employer Handbook DOL-224 (R-11/24) p.33 lists the GDOL-required posters (DOL-810/810SP, DOL-154/154SP, DOL-4107/SP, DOL-4244, WC-P1, WC-BOR) and says they are available "in English and Spanish". It does not say any language is mandatory. | US-GAP9L-001 (A.1, supersedes US-GAL-001), US-GAP9L-002 (A.1, partial), US-GAP9L-003 (A.3) |
| 2. MS: wage-payment / postings | **POSTINGS CLOSED; statute partial.** The MDES required-posters page was read. The UI poster comes in English and Spanish, and the page says "the only other state-required poster is the Mississippi Worker's Compensation poster" (also English and Spanish). It states no language mandate. Miss. Code 71-1-35 (frequency of pay for manufacturers and public-service corporations) was NOT read on an official host: the official code is LexisNexis-hosted and no legislature copy was located. Mississippi has no pay-statement or wage-notice statute (US-MS-P5-2-004), so no payroll-document language clause can exist outside 71-1-35. | US-MSP9L-001 (A.3); US-MSL-001 stays `partial` for the 71-1-35 text |
| 3. MD: Healthy Working Families Act notice | **CLOSED.** All of LE 3-1301 to 3-1311 was read on mgaleg.maryland.gov. 3-1306(a)-(d) requires the employer to notify employees of their entitlement (accrual, purposes, anti-retaliation, complaint right), and the Commissioner makes a poster and model notice available. **There is no language clause in 3-1306 or anywhere in 3-1301 to 3-1311** (zero hits for language, Spanish or English). The MD Labor employee-notice poster is a 2-page PDF: page 1 is English and page 2 is Spanish ("Licencia de enfermedad y salida segura de Maryland"). The agency offers the Spanish version but does not require it. | US-MDP9L-001 (A.1), US-MDP9L-002 (A.3) |
| 4a. Required-postings pages, 51 jurisdictions | **38 READ (37 states plus GA from the handbook), 12 ACCESS gaps, and OH partial (its postings page is an empty JS shell; only the min-wage poster read) = 51.** Postings pages were read for AK AL AR CO CT DE GA HI IA IL IN KY MD ME MI MN MO MS MT NC ND NE NJ NM NV NY OK OR PA RI SC SD UT VA VT WI WV WY. Two new language rules surfaced. **CO**: the COMPS Order (7 CCR 1103-1), Rule 7.4.3, requires the Spanish COMPS Order and poster where employees with limited English speak Spanish, or a Division-provided version in another language; Rule 2.3.2(C)(3) applies a 5% first-language rule to agricultural notices. **NJ**: the Gender Equity Notice AD-290/AD-290S comes in English and Spanish; the statutory language mandate (N.J.S.A. 34:11-56.12) is a tier-B lead only. Three express negatives: **NC** ("The law requires posting in English"), **IN** ("Neither ... nor Indiana law require posting of notices in Spanish or other languages"), and **DE** (wage-hour poster: "Delaware law does not specifically require multilingual posters"; the statutory paid-leave poster rule in 19 Del. C. 3710(c) is separate and stands). Every other page read offers translations and states no mandate. No postings page requires the pay statement itself in a language other than English. | US-<UF>P9L-001 for each state read (A.3) |
| 4b. State official-language designations | **13 READ on official hosts:** AZ, FL, HI, IA, KS, MO, MT, NC, ND, NE, NH, SC, SD. **Every designation read governs government documents, proceedings or records only.** AZ (art. 28) and IA (1.18(5)(c)) expressly exclude commerce. KS 73-2801(c) lets agencies publish in other languages as long as English is also used. SC 1-1-697 forbids the State from *requiring* a language other than English, which binds state requirements, not private employers. HI has two official languages, English and Hawaiian, with Hawaiian required only for public acts as provided by law. SD names English as the common language and Lakota/Dakota/Nakota as the official indigenous language. **None restricts or mandates the language of a private employer's payroll documents.** Not checked this pass: every other jurisdiction. The candidate designations in AK, AL, AR, CA, CO, GA, ID, IL, IN, KY, MS, OK, TN, UT, VA, WV and WY are on hosts that are LexisNexis-only, JS-rendered or unreachable here (ID timed out, UT and VA returned pages without the section text). | US-<UF>P9L-002 for AZ FL HI IA KS MO MT NC ND NE NH SC SD (A.1) |
| 5. Express bilingual permission | **Express permission:** IN (DWD "employers are encouraged to post the posters that are available in other languages"), DE (KB: translated posters are "best practice"), NC ("English on one side and Spanish on the other"; English is the legal minimum), KS (73-2801(c), agencies only), ME ("request specific languages if needed"). Statutes already registered permit or require a second language by "also in" wording (NY 195(1)(a), DC 32-1008(c), CO, DE 3710(c), CT, FL, AZ, MI). **Agency-supplied translations, which permit but do not require:** AL, CT, GA, IL, KY, MD, MI, MN, MO, MS, MT, ND, NE, NJ, NM, NV, OR, PA, RI, SD, UT, VA, VT, WI, WY. **No read source in any jurisdiction prohibits a bilingual payroll document.** | as in the table |

**US-MQ-03 net position after P9.** Limbs 1 and 3 are closed on A.1. Limb 2 is closed for postings, but the 71-1-35 text is still not read on an official host (low materiality: no MS payroll-document statute exists). Limb 4a is complete for 38 jurisdictions and leaves 12 ACCESS gaps plus OH partial; for each of those, the statute-level census row already exists. Limb 4b is complete only for 13 designations. Limb 5 is now shown in 30+ states, but it is not a universal proof. Agent 2 does not regard the census limbs as fully closed. Two closing routes remain: the owner opens the 13 postings URLs below (12 ACCESS + OH), or one owner decision (`US-OWN-006`) accepts the scope statement with the remaining gaps listed as known limits. The design result does not change: payslip in English everywhere; Spanish (and other languages) only as statutory or agency notice and poster templates. The two new items for CCG/PSL are the CO COMPS Rule 7.4.3 translation duty and the NJ gender-equity notice (the latter pending a statute read).

## 51-jurisdiction table

Key. Statute = language clause in the pay-statement, wage-notice or sick-leave-notice statute (earlier passes). Postings = agency required-postings page, this pass. Official language = designation read this pass. "none" means none in the read source. ACCESS means the page could not be read; the URL is in the gap list.

| UF | Statute (existing rows) | Postings page (P9) | Official language (P9) | Status |
|---|---|---|---|---|
| AK | none [US-AKL-001] | none; only the federal NLRA notice is multilingual [US-AKP9L-001] | not checked | closed (postings) |
| AL | none; no state wage law [US-ALL-001] | none; translations offered [US-ALP9L-001] | not checked | closed (postings) |
| AR | none [US-ARL-001] | none [US-ARP9L-001] | not checked | closed (postings) |
| AZ | yes: 23-375(B) sick-time notice in English + Spanish [US-AZL-001] | ACCESS (azica.gov 403) | gov-only; commerce excluded [US-AZP9L-002] | postings gap |
| CA | yes: 2810.5(a)(1) hire notice in the employer's usual language [US-CAP6-001] | ACCESS (dir.ca.gov timeout) | not checked | postings gap |
| CO | yes: 8-13.3-408(2) English + 5% first language [US-COL-001] | **yes**: COMPS Rule 7.4.3 Spanish (or other) for LEP employees; ag Rule 2.3.2(C)(3) 5% rule [US-COP9L-001] | not checked | closed (postings) |
| CT | yes: 31-57w(b) poster in English + Spanish [US-CTL-001] | none stated; English/Spanish offered [US-CTP9L-001] | not checked | closed (postings) |
| DC | yes: 32-1008(c) English + primary-language template [US-DC-P5-1-012] | ACCESS (does.dc.gov 403) | not checked | postings gap |
| DE | yes: 19 Del. C. 3710(c) English, Spanish, 5% [US-DEL-001] | express none for the wage-hour poster [US-DEP9L-001] | not checked | closed (postings) |
| FL | yes: 448.109(3)(a) min-wage poster in English + Spanish [US-FLL-001] | ACCESS (floridajobs.org path 404) | English official, no employer rule [US-FLP9L-002] | postings gap |
| GA | none [US-GAP9L-001] | none; English/Spanish offered [US-GAP9L-003] | not checked | **closed** |
| HI | none [US-HIL-001] | none [US-HIP9L-001] | English + Hawaiian; public acts only [US-HIP9L-002] | closed |
| IA | none [US-IAL-001] | none [US-IAP9L-001] | gov-only; commerce excluded [US-IAP9L-002] | closed |
| ID | none [US-IDL-001] | ACCESS (labor.idaho.gov timeout) | not checked | postings gap |
| IL | none [US-FEDR3-008] | none stated; 10-language PLAWA notice offered [US-ILP9L-001] | not checked | closed (postings); PLAWA rule text not read |
| IN | none [US-INP6-001] | **express none** [US-INP9L-001] | not checked | closed (postings) |
| KS | none [US-KSL-001] | ACCESS (dol.ks.gov 403) | gov-only [US-KSP9L-002] | postings gap |
| KY | none [US-KYP8-001..003] | none; English/Spanish [US-KYP9L-001] | not checked | closed (postings) |
| LA | none [US-LAL-001] | ACCESS (laworks.net Cloudflare) | not checked | postings gap |
| MA | yes: c.149 s.148C(o) by cross-reference to c.151A s.62A(d)(iii) [US-MAL-002] | ACCESS (mass.gov 403) | not checked | postings gap |
| MD | none [US-MDL-001, US-MDP9L-001] | none; English/Spanish poster [US-MDP9L-002] | not checked | **closed** |
| ME | none [US-MEL-001] | none; 8 languages offered [US-MEP9L-001] | not checked | closed (postings) |
| MI | yes: MCL 408.968 English, Spanish, 10% [US-MIL-001] | none added; English/Spanish/Arabic [US-MIP9L-001] | not checked | closed (postings) |
| MN | yes: 181.032 English, other language on request [US-MNP6-001] | none stated [US-MNP9L-001] | not checked | closed (postings) |
| MO | none [US-MOL-001] | none; En Español versions [US-MOP9L-001] | gov-only [US-MOP9L-002] | closed |
| MS | none located; 71-1-35 not read on an official host [US-MSL-001 partial] | none; English/Spanish [US-MSP9L-001] | not checked | postings closed; statute partial |
| MT | none [US-MTL-001] | none [US-MTP9L-001] | gov-only [US-MTP9L-002] | closed |
| NC | none [US-NCL-001] | **express: English required** [US-NCP9L-001] | bare designation [US-NCP9L-002] | closed |
| ND | none [US-NDL-001] | none [US-NDP9L-001] | bare designation [US-NDP9L-002] | closed |
| NE | none [US-NEL-001] | none stated; Paid Sick Time Act text not read [US-NEP9L-001] | gov records only [US-NEP9L-002] | closed (postings) |
| NH | none [US-NHL-001] | ACCESS (nh.gov 403) | gov-only [US-NHP9L-002] | postings gap |
| NJ | yes: ESL notice in primary language [US-FEDR3-010] | Gender Equity AD-290/AD-290S; statutory mandate is a tier-B lead [US-NJP9L-001 partial] | not checked | partial |
| NM | none [US-NMP8-001] | none; 4 languages offered [US-NMP9L-001] | not checked | closed (postings) |
| NV | none [US-NVL-001] | none; Spanish versions [US-NVP9L-001] | not checked | closed (postings) |
| NY | yes: 195(1)(a) English + primary language [US-NY-P5-1-003] | confirms 195.1 [US-NYP9L-001] | not checked | closed (postings) |
| OH | none [US-OHL-001] | page empty (JS); 2027 min-wage poster English-only [US-OHP9L-001 partial] | not checked | partial |
| OK | none [US-OKL-001] | none [US-OKP9L-001] | not checked | closed (postings) |
| OR | agency duty 652.610(6); 652.110(6) usual language [US-ORL-001] | none stated [US-ORP9L-001] | not checked | closed (postings) |
| PA | none [US-PAL-001] | none stated; Spanish versions [US-PAP9L-001] | not checked | closed (postings) |
| RI | none [US-RIL-001] | none; English/Spanish/Portuguese [US-RIP9L-001] | not checked | closed (postings) |
| SC | none [US-SCL-001] | none [US-SCP9L-001] | 1-1-697 binds the State only [US-SCP9L-002] | closed |
| SD | none [US-SDL-001] | none [US-SDP9L-001] | gov-only; Lakota/Dakota/Nakota indigenous [US-SDP9L-002] | closed |
| TN | none [US-TNL-001] | ACCESS (tn.gov 403) | not checked | postings gap |
| TX | agency duty 61.006; payroll card 61.017 [US-TXL-001] | ACCESS (twc.texas.gov 202 challenge) | not checked | postings gap |
| UT | none [US-UTP6-001] | none; Spanish versions [US-UTP9L-001] | not read (le.utah.gov page lacked text) | closed (postings) |
| VA | none [US-VAL-001] | none; English/Spanish [US-VAP9L-001] | not read (LIS page lacked text) | closed (postings) |
| VT | yes: 342(f) payroll-card disclosures [US-VTL-001] | none stated [US-VTP9L-001] | not checked | closed (postings) |
| WA | none [US-WAL-001] | ACCESS (lni.wa.gov 404 to curl) | not checked | postings gap |
| WI | yes: 103.915(8) migrant workers [US-WIL-001] | none stated [US-WIP9L-001] | not checked | closed (postings) |
| WV | none [US-WVL-001] | none [US-WVP9L-001] | not checked | closed (postings) |
| WY | none [US-WYL-001] | none; Spanish version [US-WYP9L-001] | not checked | closed (postings) |

Federal layer, unchanged: English official language by presidential action, with no obligation on private employers [US-FED-020]; 29 CFR 516.2 has no pay statement and no language rule [US-FED-010].

## ACCESS gaps (exact URLs; owner can open in a normal browser and save into `pdfs/<UF>/`)

| UF | URL | Result 2026-11-01 |
|---|---|---|
| AZ | https://www.azica.gov/posters | 403 |
| CA | https://www.dir.ca.gov/wpnodb.html | connection timeout |
| DC | https://does.dc.gov/page/workplace-business-posters | 403 |
| FL | https://floridajobs.org/business-growth-and-partnerships/for-employers/display-posters-and-required-notices | 404 to curl |
| ID | https://www.labor.idaho.gov/businesses/labor-laws/Required-Posters/ | connection timeout |
| KS | https://www.dol.ks.gov/employers/posters | 403 |
| LA | https://www.laworks.net/ (Labor Law posters section) | 404 / Cloudflare |
| MA | https://www.mass.gov/info-details/massachusetts-workplace-poster-requirements | 403 |
| NH | https://www.nh.gov/labor/inspection/posters.htm | 403 |
| OH | https://com.ohio.gov/divisions-and-programs/industrial-compliance/wage-and-hour-administration/posters | 200, but the content is rendered by JS ("No content found") |
| TN | https://www.tn.gov/workforce/general-resources/major-publications0/major-publications-redirect/posters-redirect/required-posters.html | 403 |
| TX | https://www.twc.texas.gov/businesses/posters-workplace | 202 bot challenge |
| WA | https://lni.wa.gov/workers-rights/workplace-policies/workplace-posters | 404 to curl |
| MS (statute) | Miss. Code 71-1-35 official text (LexisNexis-hosted Mississippi Code) | no legislature copy located |
| GA (enactment) | HB 373 / HB 110 (2019) enacted text and Act number on legis.ga.gov | status page not reached |
| NJ (statute) | N.J.S.A. 34:11-56.12 (gender equity notice language) on njleg.state.nj.us | not attempted this pass |
| Wayback | https://web.archive.org/web/2026id_/... | 429 rate limit |

A retry of the blocked hosts with browser-imitating headers was refused by the permission classifier as bot-check circumvention. It was not pursued. These hosts need a human browser read.

## What would close US-MQ-03

Two routes. (a) The owner saves the 13 postings pages above plus the NJ 34:11-56.12 text. Agent 2 then grades them in one short pass; each state is one independent lookup and can be fanned out. (b) The owner signs `US-OWN-006`, accepting the following scope statement: "Payslip and authority-facing filings in English; no read source in 51 jurisdictions requires a non-English pay statement; second-language duties are notice/poster templates (AZ, CO, CT, DC, DE, FL, MA, MI, MN, NJ, NY, CA usual-language), carried as PSL/CCG seams; official-language designations read (13) bind government only." The 12 postings ACCESS gaps, OH and the unchecked designations would be recorded as known limits.

## Proof block

- **Request → answer:** limb 1 GA closed on A.1 (residual: 2019 enactment); limb 2 MS postings closed (71-1-35 text open); limb 3 MD closed on A.1; limb 4a 38/51 read plus 12 ACCESS and OH partial; limb 4b 13 designations read, all government-only; limb 5 express permission in IN, DE, NC, KS, ME and offered translations in 25+ states.
- **Sources:** each row's `url` and `local_file` in `mandate-P9-lang-r1.csv`; quoted passages are on the saved files (MD 3-1306 text; GA SB 88/AP Section 1; GDOL DOL-224 p.33; IN DWD, NC DOL, DE KB pages; CO CDLE posters page quoting COMPS 7.4.3).
- **Test:** shard parsed with Python csv: 55 rows, 20 columns, 55 unique ids, every `local_file` exists; every pre-existing id cited in the table resolves in the register or shards (checked by grep, tier and status as cited; US-GAL-001 B/MANUAL now superseded by US-GAP9L-001).
- **Confidence:** MD 98%; GA 90% (enactment of the 2019 amendment not confirmed, verdict unaffected); MS postings 95%, statute 70%; postings census 38/51 read (75%); official-language census 13/51 read; "no source requires a non-English payslip" 90% across the jurisdictions read.

## Round 2 (browser reads, 2026-11-01)

Agent 2, ACCESS-gap pass via Claude in Chrome (own tab, `get_page_text`; no javascript_tool, no downloads, no challenge bypassed). Each page's text is saved under `00-official-sources/pdfs/<UF>/` with the URL and read date on the first line. Shard: `00-official-sources/_register-shards/mandate-P9-lang-r2.csv` (12 rows, 20 columns, ids unique, every `local_file` exists; checked with Python csv).

### Per target

| Target | Result | Register id |
|---|---|---|
| AZ postings | Read (old `/posters` redirects to home; current page found via the home menu). MW 2027 and Earned Paid Sick Time posters listed in English **and** Spanish, both ticked "Required Posting". No rule cited on the page; consistent with A.R.S. 23-375(B) (US-AZL-001). | US-AZP9M-001 (A.2) |
| CA postings | **Gap.** dir.ca.gov does not load in the browser either (Chrome error page, twice). | none |
| DC postings | **Gap.** The Chrome extension refused to read does.dc.gov ("Permission denied for reading page content on this domain"). | none |
| FL postings | **Gap.** Same extension refusal on floridajobs.org; floridacommerce.gov showed an error page. | none |
| ID postings | Read (slow host, about 8 s). English and Spanish packets offered; no mandate. | US-IDP9M-001 (A.2) |
| KS postings | Read. The old URL is "Page Not Found"; the current page was found through the site menu. Spanish versions of the human-trafficking and child-labor posters are offered; no mandate. | US-KSP9M-001 (A.2) |
| LA postings | Read (found through the laworks.net site search). Every state-mandated group is marked "tambien en Español", including Timely Payment of Wages; no mandate. | US-LAP9M-001 (A.2) |
| MA postings | Read. Table of required posters with statutes; no language rule on the page. The statutory UI/ESL language duty stays as registered (US-MAL-002). | US-MAP9M-001 (A.2) |
| NH postings | Read at dol.nh.gov (the old nh.gov URL is 404). The listing includes "2240 - Spanish Employment Poster"; no rule makes it mandatory. Page 2 of the listing was not read. | US-NHP9M-001 (A.2) |
| OH postings | Read. The old URL is 404; the current page is under Wage & Hour > Minimum Wage Posters. It reads "Employers must display the most recent minimum wage poster"; no language versions and no language rule. | US-OHP9M-001 (A.2), supersedes US-OHP9L-001 |
| TN postings | Read. Spanish set listed under "If You Have Spanish-Speaking Employees"; WC notice also in Korean. No rule cited, so this is a conditional recommendation, not a proven mandate. | US-TNP9M-001 (A.2) |
| TX postings | Read. The browser redirected to /programs/unemployment-tax/posters-workplace with no challenge. **New mandate (not payroll):** since 2024-01-08, every employer with 1 or more employees must post the Reporting Workplace Violence notice **in English and Spanish** (HB 915, 2023; 40 TAC 800.600). The Payday Law poster is offered in Spanish only as an option. The HB 915 and 40 TAC 800.600 text itself is still a lead. | US-TXP9M-001 (A.2) |
| WA postings | Read at /forms-publications/required-workplace-posters (found with the L&I site search; the old URL is 404). **Express negative:** "There is no requirement to post the Spanish portion of the posters." | US-WAP9M-001 (A.3) |
| NJ N.J.S.A. 34:11-56.12 | **CLOSED on A.1** (lis.njleg.state.nj.us, updated through P.L.2026 c.50; section text sits in a frame and was transcribed from screenshots). Under (c), the employer "shall post and provide the notification in English, Spanish, and any other language" that the Commissioner has made available and that the employer reasonably believes is the first language of a significant number of its workforce. Applies to employers with 50+ employees. The written copy can be a pay check insert, with a signed acknowledgement within 30 days. | US-NJP9M-001 (A.1), supersedes US-NJP9L-001 |
| GA 34-7-2, 2019 amendment | **Partial.** HB 110 was withdrawn and recommitted on 2019-04-02, so it was **not enacted**. HB 373 was enacted as **Act 185**, effective 2019-05-06, and amends Title 34 (DOL / employment security). The Act 185 text was not opened (the version link is a PDF document), so it is not confirmed whether Act 185 touches 34-7-2. The verdict (no language clause) is unchanged. | US-GAP9M-001 (A.1, partial), supersedes US-GAP9L-002 |
| MS Miss. Code 71-1-35 | **Gap, not attempted.** The only official host is the LexisNexis-licensed code, which is bot-protected. Materiality is low (US-MSL-001 stays partial). | none |
| CO COMPS Rule 7.4.3 | **Gap.** sos.state.co.us returned the Cloudflare "Sorry, you have been blocked" page and was not retried. cdle.colorado.gov/comps is 404, and the site search found no COMPS page. The quote stays as in US-COP9L-001. | none |

### Remaining gaps (exact URLs)

| UF | URL | Result 2026-11-01 (browser) |
|---|---|---|
| CA | https://www.dir.ca.gov/wpnodb.html (and https://www.dir.ca.gov/) | Chrome error page (host unreachable from this exit) |
| DC | https://does.dc.gov/page/workplace-business-posters | extension: permission denied for the domain |
| FL | https://floridajobs.org/business-growth-and-partnerships/for-employers/display-posters-and-required-notices | extension: permission denied for the domain |
| GA | Act 185 (HB 373, 2019) enacted text: version PDF from https://www.legis.ga.gov/legislation/55136 ("Current Version") | not opened (PDF document) |
| MS | Miss. Code 71-1-35 on the LexisNexis-hosted official code | not attempted |
| CO | 7 CCR 1103-1 (COMPS) on https://www.sos.state.co.us/CCR/ | Cloudflare block |
| TX | 40 TAC 800.600 (https://texreg.sos.state.tx.us/) / HB 915 (88R) enrolled text | not attempted (new lead) |

### Updated census

**Postings read: 48/51** (r1: 38, plus r2: AZ, ID, KS, LA, MA, NH, OH, TN, TX, WA; OH moves from partial to read). The gaps are now CA, DC and FL. Mandates found by agency or statute: CO (COMPS 7.4.3), NJ (34:11-56.12(c), now A.1) and TX (workplace-violence notice, not a payroll document). Express negatives: IN, NC, DE, WA. Every other page offers a second language without requiring it. **No source read in 48 jurisdictions requires the pay statement itself in a language other than English.** Design impact: add the NJ gender-equity notice (English + Spanish + available first languages, for employers with 50+ employees, possibly delivered as a pay check insert) and the TX workplace-violence notice (English + Spanish) to the notice/poster seams. The payslip stays English.

**Proof block.** Request → answer: 13 postings targets (10 read, 3 gaps); NJ statute closed A.1; GA enactment status resolved for HB 110/HB 373, text partial; MS not attempted; CO blocked. Sources: each r2 row's `url` and `local_file`. Test: r2 shard parsed (12 rows × 20 columns, unique ids, local files exist). Confidence: NJ 97% (transcribed from screenshot, verbatim check on the screen); postings rows 95%; TX mandate 90% (agency page, rule text not read); GA 85% on "Act 185 does not add a language clause" (text unread).
