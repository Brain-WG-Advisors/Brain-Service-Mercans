# ACCESS GAPS - consolidated for the browser pass (Stage 5, 2026-11-02)

Source: the `## ACCESS gaps` section of each `_research/stage5/{JUR}.md`, one line per URL, deduped within each jurisdiction; lines with no URL are listed after the URLs. The orchestrator's queue line from `_pipeline/RUN-JOURNAL.md` is quoted where it exists. Most gaps are HTTP 403 / DNS / TLS failures from a Brazilian exit IP with the VPN off; a US IP or a human browser is the expected fix.

**Totals:** 302 URLs and 39 URL-less items across 53 jurisdictions.

## FED (5 URLs)
_Journal queue:_ ssa.gov EFW2 2026 (26efw2.pdf) e cbb.html (base 2027 192.300); ACF new-hire.
- https://www.ssa.gov/employer/efw/26efw2.pdf - returned HTTP 403. The Wayback copy https://web.archive.org/web/2026id_/ returned 404, and the archive.org availability API returned 429. → US-FEDS5-032 (gated)
- https://www.ssa.gov/employer/EFW2&EFW2C.htm - returned 403.
- https://www.ssa.gov/oact/cola/cbb.html - returned 403, and the Wayback copy returned 403 (blocks re-verification of 2027 OASDI 192,300, US-FED-022).
- https://www.acf.hhs.gov/css/employers/employer-responsibilities/new-hire-reporting - returned 202 with an empty body (bot challenge), and its Wayback copy returned 202 with an empty body. The statute 42 U.S.C. 653a is used instead.
- https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title29-section206… - returned 404 for all six sections. Replaced by govinfo USCODE-2024; no gap.

## MULTI (6 URLs)
_Journal queue:_ HHS registro multiestadual e new-hire (HTTP 202 vazio), congress.gov S.1443.
- https://www.acf.hhs.gov/css/form/multistate-employer-registration-form - returned HTTP 202 with an empty body (redirect to acf.gov). The Wayback `https://web.archive.org/web/2026id_/` return
- https://www.acf.hhs.gov/css/employers/employer-responsibilities/new-hire-reporting - returned HTTP 202, empty.
- https://www.congress.gov/bill/119th-congress/senate-bill/1443/all-actions - returned 403. The bill status rests on govinfo (introduced version only).
- https://wdr.doleta.gov/directives/attach/UIPL20-04.pdf - connection failed (curl 000). The Wayback `2026id_` copy returned 404. Used the dol.gov HTML (`/sites/dolgov/files/ETA/advisories/UIPL/2004/UIPL20-04.html`); Attachment I (examples) is not held.
- https://app.leg.wa.gov/RCW/default.aspx?cite=50A.05.010 - connection failed (curl 000). Read from the Wayback 2026-04-23 copy.
- https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title{T}-section{N} - returned 404 for every section (URL format, not a block). Used govinfo USCODE-2024 instead.

## AK (4 URLs, 1 without URL)
_Journal queue:_ akleg.gov (AS 23.20.175/.530, 25.27.062/.075, 36.05.040, 8 AAC 95.030, Administrative Register 2026), planilha do salário médio (base 54.200).
- https://www.akleg.gov/basis/statutes.asp?media=print&secStart=23.10.065&secEnd=23.10.065 - HTTP 000 (no connection). The whole host is affected.
- https://public.courts.alaska.gov/web/forms/docs/civ-530.pdf - HTTP 000. Read from the Wayback copy dated 20260210203536.
- https://childsupport.alaska.gov/child-support-enforcement/employers/new-hire-wage-withholding - HTTP 404. The `child-support-services/...` path redirects (301) to it, and `.../letter-to-alaskan-employers` is also 404. The Wayback `2026id_` copy is also 404.
- https://labor.alaska.gov/estax/2027-experience-rates.html - HTTP 404. This is a timing gap (2027 not yet published), not an access block.
- (no URL) 8 AAC 95.030 (garnishment amounts) and 8 AAC 85 (ES Tax regulations) on `akleg.gov/basis/aac.asp`: not attempted, because the host is unreachable.

## AL (3 URLs, 1 without URL)
_Journal queue:_ Workforce Alabama 2026 shared cost/UC-216; censo de ~26 impostos ocupacionais municipais (Birmingham 1% só C).
- https://www.auburnalabama.org/finance/business-and-licensing-forms/occupational-license - (and the site root): curl timeout (HTTP 000) from a BR exit, VPN off. Wayback was not tried. Needed for the Auburn rate and return frequency.
- https://library.municode.com/al/birmingham/codes/code_of_ordinances?nodeId=PT1THCOGEOR_TIT3ARETA_CH2OCTA - script-rendered (known from US-ALP7-001). The Birmingham rate stays tier C.
- https://birminghamal.hdlgov.com/Home/Home/Taxes - not fetched (portal).
- (no URL) Workforce Alabama 2026 tax-rate schedule and shared cost: no public page found. The FAQ points to the UC-216 notice in eGov (gated per employer).

## AR (6 URLs, 1 without URL)
_Journal queue:_ arkleg.state.ar.us (TLS; Act 1/2026 texto), guia MyWorkers OCSE (403), Código AR (LexisNexis) 16-66-208, 11-4-401, 9-14-218.
- https://arkleg.state.ar.us/ - `...` (all paths): TLS failure, curl exit 35. Acts 853/2019 and 1019/2021 were read from Wayback. Act 1 of 2026 (1st Ex. Sess.) text, `https://www.arkleg.state.ar.us/Acts/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2F&file=1.pdf&ddBie
- https://www.arkleg.state.ar.us/Acts/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2F&file=1.pdf&ddBienniumSession=2025%2F2026S1 - `https://arkleg.state.ar.us/...` (all paths): TLS failure, curl exit 35. Acts 853/2019 and 1019/2021 were read from Wayback. Act 1 of 2026 (1st Ex. Sess.) text, `https://www.arkleg.state.ar.us/Acts/FTPDocument?path=%2FACTS%2F2026S1%2FPublic%2F&file=1.pdf&ddBie
- https://myworkers.ocse.arkansas.gov/MyWorkers/Content/PDF/MyWorkersEmployerResources.pdf - HTTP 403. The `https://www.ark.org/myworkers/...` mirror also returns 403. No Wayback copy.
- https://www.ark.org/myworkers/ - `https://myworkers.ocse.arkansas.gov/MyWorkers/Content/PDF/MyWorkersEmployerResources.pdf`: HTTP 403. The `...` mirror also returns 403. No Wayback copy.
- https://www.dfa.arkansas.gov/child-support/ocse-partners/employers - 404 (the live page is under `/office/child-support-enforcement/ocse-partners/`).
- https://www.dfa.arkansas.gov/wp-content/uploads/AR4EC.pdf - 404 (the current file is `AR4EC2026.pdf`).
- (no URL) Official Arkansas Code (LexisNexis public portal): not attempted, because it is bot-gated. Needed for 16-66-208, 11-4-401 (current) and 9-14-218.

## AZ (9 URLs, 1 without URL)
_Journal queue:_ azica.gov salário mínimo + cartazes 2026/2027 (confirmar 15,15/15,65), Flagstaff, des.az.gov UC-018 e aviso de separação, azdor A-4 2026, Pub 701 atual.
- https://www.azica.gov/labor-minimum-wage-main-page - 403 direct; Wayback `2026id_` also 403.
- https://www.azica.gov/sites/default/files/2025-09/2026%20THE%20FAIR%20WAGES%20AND%20HEALTHY%20FAMILIES%20ACT_1.pdf - 403 direct; Wayback 403.
- https://www.azica.gov/sites/default/files/2026-09/2027%20THE%20FAIR%20WAGES%20AND%20HEALTHY%20FAMILIES%20ACT_1.pdf - (guessed path): 403.
- https://des.az.gov/services/employment/unemployment-employer - 403 (UC-018 quarterly report, separation notice and news not read).
- https://azdor.gov/forms/withholding-forms/arizona-withholding-percentage-election - 403.
- https://azdor.gov/sites/default/files/document/FORMS_WITHHOLDING_2026_A-4.pdf - 404 (the A-4 instructions are already held by US-AZP51-001).
- https://azdor.gov/sites/default/files/2023-03/PUBLICATION_701.pdf - 403 (the Wayback copy was read).
- https://www.flagstaff.az.gov/3685/Minimum-Wage - 404 (guessed URL; the Flagstaff MW page was not found).
- https://www.tucsonaz.gov/Departments/Business-Services/Minimum-Wage - 404 (the correct page was found and read).
- (no URL) BLS API v1 ignores `startyear`, so only 2024–2026 data was returned. The full 2020–2025 chain needs a POST or v2.

## CA (7 URLs)
_Journal queue:_ salários mínimos municipais (DIR não mantém lista; 1 worker por cidade), fast-food/saúde, DE 9C formato eletrônico, leginfo 403 (usado Wayback).
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=226 - direct 403 (bot check). The Wayback copies used are dated 2026-08-31 (226, 204), 2026-01-02 (510) and 2025 (201, 202, 203, 227.3, 246, 224, 351). Section 213 is f
- https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=706.050 - 403. Wayback holds only 2022-01-21, which is pre-SB 1477 and was discarded. The current rule is taken from Judicial Council WG-002 (Rev. 2026-01-01).
- https://www.dir.ca.gov/dlse/faq_minimumwage.htm - , `https://dir.ca.gov/DIRNews/2026/2026-66.html` and `https://www.dir.ca.gov/Public-Works/Certified-Payroll-Reporting.html`: direct curl timed out (000). Wayback (2026) used.
- https://dir.ca.gov/DIRNews/2026/2026-66.html - `https://www.dir.ca.gov/dlse/faq_minimumwage.htm`,  and `https://www.dir.ca.gov/Public-Works/Certified-Payroll-Reporting.html`: direct curl timed out (000). Wayback (2026) used.
- https://www.dir.ca.gov/Public-Works/Certified-Payroll-Reporting.html - `https://www.dir.ca.gov/dlse/faq_minimumwage.htm`, `https://dir.ca.gov/DIRNews/2026/2026-66.html` and : direct curl timed out (000). Wayback (2026) used.
- https://childsupport.ca.gov/employers/ - 404 directly and on Wayback. PUB 307 and the IWO fact sheet were used instead.
- https://www.ftb.ca.gov/forms/2025/2025-1001-publication.html - 404 (guessed URL). The 540 CA instructions were used instead.

## CO (13 URLs)
_Journal queue:_ cdle.colorado.gov, famli.colorado.gov, sos.state.co.us (regras COMPS/HFWA), childsupport.colorado.gov, denvergov.org (OPT 2026), mínimos 2027 (15,71 / Denver 19,84 só B).
- https://cdle.colorado.gov/dlss/labor-laws-rules-resources/minimum-wage - — 403; Wayback 404.
- https://cdle.colorado.gov/sites/cdle/files/adopted_2026_pay_calc_order_7_ccr_1103-14_12.8.25.docx - — 403; Wayback 404. This is the official 2026 list of local minimum wages.
- https://cdle.colorado.gov/sites/cdle/files/2026_comps_order_poster_english_%5Baccessible%5D.pdf - — 403 direct; obtained through Wayback (US-COS5-001).
- https://famli.colorado.gov/employers/premiums - — 403; Wayback 404.
- https://famli.colorado.gov/ - — 403.
- https://www.sos.state.co.us/CCR/NumericalCCRDocList.do?deptID=9 - — 403 (CCR: COMPS 7 CCR 1103-1, PAY CALC 1103-14, FAMLI 7 CCR 2702).
- https://childsupport.colorado.gov/new-hire-reporting - — timeout (twice); childsupport.state.co.us — 302 then timeout.
- https://coag.gov/resources/data-protection-laws/ - — 202 empty.
- https://content.leg.colorado.gov/sites/default/files/R24-800_Overview%20of%20Minimum%20Wage%20Laws%20Issue%20Brief-accessible.pdf - — 202 empty.
- https://leg.colorado.gov/laws/colorado-revised-statutes - — the CRS are hosted only on LexisNexis (JS, gated). No official per-section host for C.R.S. 13-54-104, 6-1-716, 8-76-102 or 8-13.3-5xx.
- https://www.denvergov.org/ - ... (Denver Labor, Minimum Wage) — bot rejection; the Wayback copy of the Finance news release was used (US-COS5-010). The 2027 release URL guessed on Wayback: 404.
- https://bouldercolorado.gov/minimum-wage - — 404.
- https://oui.doleta.gov/unemploy/pdf/uilawcompar/2026/coverage.pdf - and /2025/ — 404 (2023 edition used).

## CT (5 URLs)
- https://www.cga.ct.gov/current/pub/chap_558.htm - , `chap_567.htm`, `chap_906.htm`, `chap_743dd.htm`: curl 000 (connection refused, VPN off). All were read from Wayback 2026 captures (`web.archive.org/web/2026id_/…`, captures 20261013–20261024).
- https://prdext2.cga.ct.gov/2026/ACT/PA/PDF/2026PA-00012-R00HB-05003-PA.PDF - and `https://prdext2.cga.ct.gov/2026/rpt/pdf/2026-R-0081.pdf`: curl 000. Read from the Wayback copies of the cga.ct.gov URLs.
- https://prdext2.cga.ct.gov/2026/rpt/pdf/2026-R-0081.pdf - `https://prdext2.cga.ct.gov/2026/ACT/PA/PDF/2026PA-00012-R00HB-05003-PA.PDF` and : curl 000. Read from the Wayback copies of the cga.ct.gov URLs.
- https://portal.ct.gov/dol/divisions/unemployment-insurance-tax/information-on-unemployment-tax-rate-for-calendar-year-2027 - HTTP 404 (not yet published, not a block).
- https://portal.ct.gov/DOLUI/ReEmployCT-for-Employers_File-Formats_Excel-Sheet-Templates_Info-for-Bulk-Filers - redirects to the TPA page (US-CTP52-002). The bulk-filer ICESA/MMREF specification page named in search leads was not reached. The 276-character f

## DC (4 URLs)
_Journal queue:_ OTR instruções de retenção (403), instruções W-2 2026, D-4/D-4A ('under review'), lei permanente do FY2027 BSA.
- https://otr.cfo.dc.gov/page/income-tax-withholding-instructions-and-tables - HTTP 403 to plain curl on 2026-11-02. It was also blocked in earlier rounds; the wayback copy from 2025-07-10 is in US-DCP51-004.
- https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026%20MyTax%20W2_W2C%20Instructions%20v1.0_Final.pdf - 404. The TY2026 W-2 specification is not yet published at that path.
- https://otr.cfo.dc.gov/page/withholding-tax-forms - The D-4 and D-4A fill-in links on  are absent ("currently under review").
- https://does.dc.gov/page/minimum-wage - 404. I used the notice PDFs instead.

## DE (3 URLs)
- https://tax.delaware.gov/ - **Delaware W-2 data-file FAQ document** ("W2/1099 FAQ document located on the Delaware Tax Portal"): it is behind  and is linked only from the portal. I did not try it (no login).
- https://industrialaffairs.delaware.gov/en/knowledgebase-employer/when-are-employers-required-to-pay-overtime-in-delaware - **DOL Industrial Affairs KB overtime answer:** . The answer body is script-rendered, and curl returned only the meta description. The fetche
- https://labor.delaware.gov/divisions/unemployment-insurance/employer-services/ - **UI quarterly electronic wage-file specification:** the DOL FAQ says to call (302) 761-8484. No public spec was found on .

## FL (1 URLs, 1 without URL)
_Journal queue:_ floridajobs.org página do salário mínimo (403).
- https://www.floridajobs.org/business-growth-and-partnerships/for-employers/display-posters-and-required-notices/minimum-wage - HTTP 403 by curl. The Wayback copy `https://web.archive.org/web/2026id_/<same>` returns 404. The FloridaCommerce 2026 minimum-wage n
- (no URL) FloridaCommerce rules (F.A.C. 73B-10) on separation notices and the text of Rule 73B-10.037: not fetched (budget).

## GA (8 URLs, 1 without URL)
- https://dor.georgia.gov/withholding-tax - → 404 (2026-11-02).
- https://dor.georgia.gov/taxes/withholding-tax/withholding-tax-forms-and-information - → 404 (2026-11-02).
- https://www.ga-newhire.com/faq - → 404; the site redirects to `https://newhire-reporting.com/GA-Newhire/` (read there).
- https://newhire-reporting.com/GA-Newhire/ - `https://www.ga-newhire.com/faq` → 404; the site redirects to  (read there).
- https://gov.georgia.gov/document/2016-signed-legislation/sb-255/download - → 404; `https://gov.georgia.gov/document/2017-signed-legislation/sb-201/download` → 404. The enacted garnishment and Family Care Act texts were not located on the Governor's site.
- https://gov.georgia.gov/document/2017-signed-legislation/sb-201/download - `https://gov.georgia.gov/document/2016-signed-legislation/sb-255/download` → 404;  → 404. The enacted garnishment and Family Care Act texts were not located on the Governor's site.
- https://dor.georgia.gov/federal-format-layout - TY2026 G-1003 Federal Format / CSV / template: not posted at  or `https://dor.georgia.gov/documents/withholding-g-1003-tax-template` on 2026-11-02 (Rev 01/18 spec and an undated XLS only).
- https://dor.georgia.gov/documents/withholding-g-1003-tax-template - TY2026 G-1003 Federal Format / CSV / template: not posted at `https://dor.georgia.gov/federal-format-layout` or  on 2026-11-02 (Rev 01/18 spec and an undated XLS only).
- (no URL) The O.C.G.A. text is not available section-by-section on an official host reachable by curl. All statute reads here are from acts or bills on legis.ga.gov.

## HI (6 URLs, 1 without URL)
_Journal queue:_ capitol.hawaii.gov (403): Act 24/2026 SB3125 CD2, HRS 235-2.3, 392-4/392-5, 390-2; Tabela 2 de alíquotas UI.
- https://www.capitol.hawaii.gov/hrscurrent/ - `...` → HTTP 403 to curl for every HRS section. All were read from Wayback `id_` snapshots dated 2025-02 to 2026-09 (dates in the register rows). Sections in a snapshot older than 2026 may miss 2025/2026 amendments.
- https://www.capitol.hawaii.gov/sessions/session2026/bills/SB3125_CD2_.HTM - → 403. The Wayback copy (`/web/20260512230748id_/`) stored the 403. `https://data.capitol.hawaii.gov/sessions/session2026/bills/SB3125_CD2_.HTM` and `.PDF` → 403. Result: the Act 24 SL
- https://data.capitol.hawaii.gov/sessions/session2026/bills/SB3125_CD2_.HTM - `https://www.capitol.hawaii.gov/sessions/session2026/bills/SB3125_CD2_.HTM` → 403. The Wayback copy (`/web/20260512230748id_/`) stored the 403.  and `.PDF` → 403. Result: the Act 24 SL
- https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0390/HRS_0390-0002.htm - → 403, and the Wayback copy also 403. The child labor rules come from the DLIR page instead.
- https://labor.hawaii.gov/ui/employers/ - → 404, and no Wayback copy.
- https://cse.ehawaii.gov/ - → connection failed (000), and no Wayback copy.
- (no URL) DLIR "Contribution Rates Explained" Table 2 (the A–H rate schedules) is not in the HTML text; it is probably an image or a missing element.

## IA (0 URLs, 3 without URL)
- (no URL) legis.iowa.gov code and IAC PDFs, and the bill history;
- (no URL) revenue.iowa.gov guidance and media;
- (no URL) workforce.iowa.gov handbook pages and releases.

## ID (5 URLs, 2 without URL)
_Journal queue:_ tax/labor/legislature.idaho.gov: formulário ID W-4 2026, texto H0544, 72-1349(1), tabela UI 2027.
- https://tax.idaho.gov/ - Direct access fails from this network without the VPN: , `https://www.labor.idaho.gov/`, `https://legislature.idaho.gov/` (curl timeout, HTTP 000). Wayback was used for every row.
- https://www.labor.idaho.gov/ - Direct access fails from this network without the VPN: `https://tax.idaho.gov/`, , `https://legislature.idaho.gov/` (curl timeout, HTTP 000). Wayback was used for every row.
- https://legislature.idaho.gov/ - Direct access fails from this network without the VPN: `https://tax.idaho.gov/`, `https://www.labor.idaho.gov/`,  (curl timeout, HTTP 000). Wayback was used for every row.
- https://tax.idaho.gov/document-mngr/forms_EFO00307/ - Form ID W-4 2026 edition: . The Wayback CDX for `tax.idaho.gov/wp-content/uploads/forms/EFO00307*` lists editions only up to `EFO00307_04-28-2025.pdf`.
- https://legislature.idaho.gov/wp-content/uploads/sessioninfo/2026/legislation/H0544.pdf - H0544 (2026) text: . Not archived (Wayback 404).
- (no URL) IDOL handbook coverage chart, p.3: an image in `Handbook_Tax-information_Nov.-2025-1.pdf`. Not text-extractable; the thresholds were taken from 72-1315 instead.
- (no URL) 2027 UI rate array: no `labor.idaho.gov/wp-content/uploads/*Class-array_2027*` in the CDX as of 2026-11-02.

## IL (5 URLs, 1 without URL)
_Journal queue:_ Chicago (FAQ licença remunerada e salário mínimo, 403), Cook County Paid Leave Ordinance.
- https://www.chicago.gov/content/dam/city/depts/bacp/OSL/faqpaidandpaidsickleave10022025.pdf - 403 Access Denied (Akamai). Wayback `web.archive.org/web/2026id_/...` returned 404. Holds Chicago Paid Leave caps, carryover and the employer-size payout rule.
- https://www.chicago.gov/content/dam/city/depts/bacp/OSL/faqminimumwage09302025.pdf - 403 (Chicago minimum wage FAQ; tipped phase-out schedule).
- https://www.cookcountyil.gov/content/cook-county-minimum-wage - 404 (the FAQ PDF was obtained instead). The Cook County Paid Leave Ordinance page was not attempted.
- https://ftp.ilga.gov/ILCS/ - `https://web.archive.org/web/2026id_/https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=2402&ChapterID=68` (IWPCA full act): 404. ilga.gov returns 403 to automated clients. **Workaround found: ** (used for US-ILS5-022..025).
- https://labor.illinois.gov/faqs/paid-leave-for-all-workers-faq.html - 404 (the correct URL `/faqs/paidleavefaq.html` was obtained).
- (no URL) archive.org availability API: 429 Too Many Requests (rate-limited during this pass).

## IN (10 URLs)
_Journal queue:_ iga.in.gov Código 2026 (tributos, UI, crédito ao consumidor, imposto local), esquema XML WH-1/WH-3, kb.dol.in.gov, página de taxas DWD 2026.
- https://iga.in.gov/ic/2026/Title_6/Article_3.pdf?download=1 - and `https://iga.in.gov/ic/2026/Title_22/Article_4.pdf?download=1`: HTTP 200 SPA shell of 691 bytes. Wayback `id_` returned 404. These would close IC 6-3-2-1 (2027 rate), 6-3-4-8.1 (frequency), 22-4
- https://iga.in.gov/ic/2026/Title_22/Article_4.pdf?download=1 - `https://iga.in.gov/ic/2026/Title_6/Article_3.pdf?download=1` and : HTTP 200 SPA shell of 691 bytes. Wayback `id_` returned 404. These would close IC 6-3-2-1 (2027 rate), 6-3-4-8.1 (frequency), 22-4
- https://iga.in.gov/ic/2026/Title_24/Article_4.5.pdf?download=1 - and `https://iga.in.gov/ic/2026/Title_6/Article_3.6.pdf?download=1`: same SPA shell. These would close the garnishment fee and LIT detail.
- https://iga.in.gov/ic/2026/Title_6/Article_3.6.pdf?download=1 - `https://iga.in.gov/ic/2026/Title_24/Article_4.5.pdf?download=1` and : same SPA shell. These would close the garnishment fee and LIT detail.
- https://www.in.gov/dor/files/IDORWTH2016V1.0 - not fetched, because the connection timed out after the VPN dropped (BR exit). This is the WH-1/WH-3 XML schema. The business rules `https://www.in.gov/dor/files/business-rules-wh1-xml.pdf` and `business-rules-wh
- https://www.in.gov/dor/files/business-rules-wh1-xml.pdf - `https://www.in.gov/dor/files/IDORWTH2016V1.0`: not fetched, because the connection timed out after the VPN dropped (BR exit). This is the WH-1/WH-3 XML schema. The business rules  and `business-rules-wh
- https://www.in.gov/dlgf/files/2026-memos/Legislation-Affecting-Local-Income-Taxes.pdf - Wayback 404, and the direct fetch timed out.
- https://kb.dol.in.gov/ - Cloudflare 403. This is the IDOL knowledge base for vacation payout and pay-statement scope.
- https://forms.in.gov/download.aspx?id=2702 - Cloudflare 403 directly. A Wayback copy was used instead.
- https://www.in.gov/dwd/indiana-unemployment/employers/employer-guide/rate-computation/state-premium-rate-computation/ - The 2026 rate-year page : the 2026-01-13 snapshot still shows 2025.

## KS (6 URLs)
- https://www.ksrevenue.gov/kw100.html - HTTP 000 (timeout). Wayback copy 2026-10-21 used.
- https://www.ksrevenue.gov/taxnotices/notice25-06.pdf - , `.../notice26-11.pdf`: HTTP 000. Wayback used.
- https://www.ksrevenue.gov/taxnotices.html - Wayback `2026id_` returned 404. The full 2026 notice index was not reviewed.
- https://www.dol.ks.gov/employers/employer-services - HTTP 403. Wayback 2026-10-16 copy (already on disk) used.
- https://admin.ks.gov/.../25-p-004-new-kansas-state-withholding-tables - 404 (lead only; not needed).
- https://www.ksrevisor.gov/statutes/2026CompositeListByKSA.html - 404 (guessed URL).

## KY (2 URLs)
_Journal queue:_ KRS 405.465, 40 KAR 1:410 (Wayback 404; sem VPN apps.legislature.ky.gov expira); lista de impostos ocupacionais locais; specs RS/KUIP.
- https://apps.legislature.ky.gov/* - every direct call timed out (VPN off, Brazil exit). Wayback worked except for
- https://lexingtonky.gov/node/659 - , `/node/660`: 404 (stale URLs). The current pages were read instead.

## LA (9 URLs)
_Journal queue:_ revenue.louisiana.gov, laworks.net (403), legis.la.gov (DNS), L-4, FAQ cafeteria plan, Acts 2026 pág. 2+.
- https://legis.la.gov/… - and `https://www.legis.la.gov/…`: host does not resolve from this machine; Wayback used for every statute.
- https://www.legis.la.gov/… - `https://legis.la.gov/…` and : host does not resolve from this machine; Wayback used for every statute.
- https://www.legis.la.gov/legis/ActNumbers.aspx?sid=26RS - pages 2-10+ (postback). Wayback holds only page 1.
- https://revenue.louisiana.gov/tax-education-and-faqs/faqs/withholding-tax/are-employees-pre-tax-contributions-to-a-qualified-cafeteria-plan-subject-to-withholding-income-tax/ - live 403, Wayback 404.
- https://dam.ldr.la.gov/taxforms/1300(L4 - `).pdf`: 404. The current L-4 file name is unknown.
- https://revenue.louisiana.gov/ - , `https://www.laworks.net/`, `https://www.doa.la.gov/doa/osr/louisiana-register/`: HTTP 403 to curl.
- https://www.laworks.net/ - `https://revenue.louisiana.gov/`, , `https://www.doa.la.gov/doa/osr/louisiana-register/`: HTTP 403 to curl.
- https://www.doa.la.gov/doa/osr/louisiana-register/ - `https://revenue.louisiana.gov/`, `https://www.laworks.net/`, : HTTP 403 to curl.
- https://dcfs.la.gov/assets/docs/searchable/New-Hire-Registry/Louisiana_New_Hire_Reporting_Form-3.pdf - 404.

## MA (8 URLs)
- https://www.mass.gov/doc/finfer-v-attorney-general-sjc-p13885/download - HTTP 404 (2026-11-02). This is the SJC opinion on Initiative Petition 25-18.
- https://www.sec.state.ma.us/divisions/elections/research-and-statistics/2026-Information-for-voters/2026-ballot-question5.htm - HTTP 302 redirect loop, 0 bytes (2026-11-02). This is the Secretary of the Commonwealth's 2026 ballot questions page.
- https://www.mass.gov/info-details/how-pfml-weekly-benefit-amounts-are-calculated-andor-reduced - , `https://www.mass.gov/info-details/new-hire-reporting`, `https://www.mass.gov/info-details/massachusetts-law-about-wages-and-salary`: HTTP 404 (guessed URLs; the
- https://www.mass.gov/info-details/new-hire-reporting - `https://www.mass.gov/info-details/how-pfml-weekly-benefit-amounts-are-calculated-andor-reduced`, , `https://www.mass.gov/info-details/massachusetts-law-about-wages-and-salary`: HTTP 404 (guessed URLs; the
- https://www.mass.gov/info-details/massachusetts-law-about-wages-and-salary - `https://www.mass.gov/info-details/how-pfml-weekly-benefit-amounts-are-calculated-andor-reduced`, `https://www.mass.gov/info-details/new-hire-reporting`, : HTTP 404 (guessed URLs; the
- https://www.mass.gov/regulations/430-CMR-500-employer-requirement-series - an index page only. The regulation text is a PDF that was not fetched (budget). Needed for Q10.
- https://www.mass.gov/info-details/new-hire-record-layout - Not fetched because of the budget, URLs known:  (new-hire file layout), `https://www.mass.gov/doc/form-m-3-reconciliation-of-massachusetts-income-taxes-withheld-for-employers/download`, and the DUA "Mas
- https://www.mass.gov/doc/form-m-3-reconciliation-of-massachusetts-income-taxes-withheld-for-employers/download - Not fetched because of the budget, URLs known: `https://www.mass.gov/info-details/new-hire-record-layout` (new-hire file layout), , and the DUA "Mas

## MD (7 URLs)
_Journal queue:_ spec W-2 TY2026 (não publicada), MW507 2026, página do mínimo de Montgomery, FAQ new-hire.
- https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/instructions/2026/reporting-w2-instructions.pdf - → 404 (2026-11-02). The TY2026 W-2 spec is not yet at the expected path.
- https://www.marylandcomptroller.gov/content/dam/mdcomp/tax/forms/2026/MW507.pdf - → 404 (guessed path). The 2026 MW507 was not obtained; the existing row US-MDP51-001 covers the certificate via the guide.
- https://www.montgomerycountymd.gov/humanrights/minimumwage.html - → 404 (guessed path). The Montgomery County ordinance or page was not read.
- https://www.labor.maryland.gov/labor/wages/wagehrmw.shtml - → 404 (guessed path). Content was read on `wagehrfacts.shtml` instead.
- https://www.mdnewhire.com/faq.html - → 403. `https://mdnewhire.com/` returns only the "Employer Services Portal" shell (JavaScript). The statute (LE 8-626.1) was read instead.
- https://mdnewhire.com/ - `https://www.mdnewhire.com/faq.html` → 403.  returns only the "Employer Services Portal" shell (JavaScript). The statute (LE 8-626.1) was read instead.
- https://mgaleg.maryland.gov/...section=3-1304.1 - (local file `pdfs/MD/MD_LE-3-1304.1_mgaleg_2026-11-01.html` from the earlier pass) holds only the text "Okay". The section was not captured; the synthesis should not cite that file.

## ME (6 URLs)
_Journal queue:_ maine.gov (403): specs de upload em lote W-2, fonte de alíquota PFML, páginas de mínimo/hora extra, notícias MRS/MDOL 2026.
- https://www.maine.gov/* - All : HTTP 403 (CloudFront geo-block, VPN off). The Wayback copies used are noted per row.
- https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding - Maine Tax Portal Bulk File Upload Specifications (W-2 format). Not fetched (budget).
- https://www.maine.gov/paidleave/ - no A.2 PFML rate notice or rule (12-702 CMR) located; the FAQ (A.3) is the only rate source.
- https://www.maine.gov/labor/labor_laws/minimum_wage_faq.html - and the MDOL / MRS news pages for 2026: not fetched (budget; geo-block).
- https://content.civicplus.com/api/assets/3899b6d8-7441-4566-853b-0491ef6bc426 - Portland ordinance: read from the CivicPlus asset host . The link from `https://www.portlandmaine.gov/` was not re-verified.
- https://www.portlandmaine.gov/ - Portland ordinance: read from the CivicPlus asset host `https://content.civicplus.com/api/assets/3899b6d8-7441-4566-853b-0491ef6bc426`. The link from  was not re-verified.

## MI (2 URLs, 1 without URL)
_Journal queue:_ mi-newhire.com (app JS); 23 cidades com imposto próprio (fora Detroit) — taxas/formulários/prazos.
- https://www.mi-newhire.com/ - HTTP 200, but the body is a JavaScript single-page app with no readable text, so it is unreadable with curl (browser pass needed).
- https://www.michigan.gov/leo/bureaus-agencies/ber/wage-and-hour/minimum-wage - HTTP 404 (guessed URL). The figure rests on A.1 statute text; no second-authority page was obtained.
- (no URL) (Not a gap) legislature.mi.gov was reachable; the earlier ECONNREFUSED did not recur.

## MN (4 URLs)
_Journal queue:_ uimn.org taxas UI 2026 (sem conexão), pl.mn.gov (verificação humana).
- https://www.uimn.org/employers/wages-taxes/tax-rates/index.jsp - HTTP 000 (no connection) today. The 2026 values rest on the Wayback copy (US-MNP52-001).
- https://pl.mn.gov/resources/calculators/premium-rate-and-contributions - the human-verification wall noted in earlier passes; not retried, Wayback row reused.
- https://www.minneapolismn.gov/business-services/labor-standards/minimum-wage/ - HTTP 404. The working route is https://minimumwage.minneapolismn.gov/.
- https://minimumwage.minneapolismn.gov/ - https://www.minneapolismn.gov/business-services/labor-standards/minimum-wage/: HTTP 404. The working route is .

## MO (7 URLs)
_Journal queue:_ labor/dss/dor/sos.mo.gov (403), DSS new-hire, notícias das agências (varredura 2026); renovação dos earnings taxes St. Louis/KC em abril 2026.
- https://revisor.mo.gov/main/OneSection.aspx?section=290.505 - (and every section after the 8th direct read): HTTP 000, timeout. Served through Wayback.
- https://dss.mo.gov/child-support/employers/new-hire-reporting.htm - 403. The Wayback copy redirects to the generic employers page (2025-06-10), which has no deadline text.
- https://labor.mo.gov/DLS/MinimumWage - 403 (Wayback 2026-10-16 used).
- https://dor.mo.gov/forms/MO%20W-4.pdf - 403 (Wayback 2026-08-18 used).
- https://www.sos.mo.gov/elections/petitions/2026BallotMeasures - 403 (Wayback 2026-09-27 used).
- https://labor.mo.gov/dls/faqs - and `https://labor.mo.gov/dls/wages-hours-dismissal-rights`: Wayback 404 (the correct page is `/dls/general`, which was used).
- https://labor.mo.gov/dls/wages-hours-dismissal-rights - `https://labor.mo.gov/dls/faqs` and : Wayback 404 (the correct page is `/dls/general`, which was used).

## MS (1 URLs, 2 without URL)
_Journal queue:_ Código MS (LexisNexis) 71-1-35, 85-3-4, 71-1-45, 71-1-17..29, 27-7-16, 43-19-46; layout UI-2.
- https://mdes.ms.gov/media/231725/filelayout_bulkfilingtable102920.pdf - (UI-2 bulk layout): not fetched; low priority.
- (no URL) **Mississippi Code of 1972 (official text):** published only through LexisNexis public access (JS application, not fetched). Sections not read in an official copy:
- (no URL) The DOR Form 21-002 POA text was not read (US-MSP51-006 stays MANUAL).

## MT (8 URLs, 4 without URL)
_Journal queue:_ *.mt.gov (DNS fora dos EUA): carta do mínimo 2027 (confirmar 11,20), rules.mt.gov, manual de envio eletrônico UI.
- https://revenue.mt.gov/
- https://revenuefiles.mt.gov/files/Forms/Montana_Employer_and_Information_Agent_Guide_with_Tax_Tables.pdf
- https://erd.dli.mt.gov/
- https://uid.dli.mt.gov/
- https://dli.mt.gov/
- https://rules.mt.gov/
- https://dphhs.mt.gov/csed
- https://erd.dli.mt.gov/_docs/labor-standards/2027-MW-Determination-Letter.pdf - the Wayback capture 20261007064405 returned 404, and no other capture exists.
- (no URL) Local DNS failure from the BR network for all of these (not retried with a DNS override; the classifier refused that route):
- (no URL) ARM rules not read because rules.mt.gov is unreachable: 24.16.7511 (final pay "immediately"), 24.16.7566 (penalty), 24.40.1609 (UI e-filing), 24.11.* (UI reports/separation), 42.17.105 (tables), 42.17.203 (records).
- (no URL) Montana UI Contributions E-Filing Handbook (uid.dli.mt.gov): not located in the Wayback index search, not fetched.
- (no URL) 2027 DOR withholding tables and Employer Guide: not yet indexed in Wayback (revenue.mt.gov/news/recent-news, 2026 captures).

## NC (4 URLs, 1 without URL)
- https://des.nc.gov/documents/files/employers-quarterly-tax-and-wage-report-english/open - HTTP 404 (NCUI 101 form PDF).
- https://des.nc.gov/documents/downloads/ncdes-524e/download - HTTP 404.
- https://des.nc.gov/employers/workplace-posters - HTTP 404.
- http://reports.oah.state.nc.us/ncac/title%2013%20-%20labor/chapter%2012%20-%20wage%20and%20hour/subchapter%2008/subchapter%2008%20rules.pdf - HTTP 404 (single rules .0802/.0805/.0807 fetched instead; .0801/.0806 not fetched).
- (no URL) These are 404s, not bot blocks, so Wayback was not tried.

## ND (3 URLs)
- https://www.jobsnd.com/sites/www/files/documents/jsnd-documents/uitaxrateschedules2027.pdf - HTTP 403 on 2026-11-02 (probably not published yet; the rates are set after September).
- https://www.tax.nd.gov/sites/www/files/documents/forms/individual/2027-iit/2027-income-tax-withholding-rates-booklet.pdf - 404 on 2026-11-02 (guessed URL; not yet published).
- https://www.tax.nd.gov/sites/www/files/documents/forms/business/form-ndw-r.pdf - HTTP 403 (guessed URL; the form itself was not needed, since the rule is in US-NDS5-002).

## NE (6 URLs, 2 without URL)
_Journal queue:_ guia de retenção 2027 PDF, FAQ licença médica e página do mínimo (DOL NE), aviso do mínimo 2027 (arredondamento de 15,2625).
- https://revenue.nebraska.gov/sites/default/files/doc/business/Cir_En_2026/2027cir_en_whole.pdf - Wayback 404 (also tried under `/sites/revenue.nebraska.gov/files/...`; the `2027_percent.pdf` variant also 404). Direct host: DNS failure.
- https://dol.nebraska.gov/LaborStandards/WorkerRights/PSTFAQs - Wayback timeout (000).
- https://dol.nebraska.gov/LaborStandards/Wage/MinimumWage - Wayback 404.
- https://dol.nebraska.gov/PressRelease - NDOL 2027 minimum-wage publication: not located. Press-release list snapshot of 2026-08-14 () predates it.
- https://nebraskalegislature.gov/FloorDocs/109/PDF/Slip/LB258.pdf - Wayback 404. Covered by the 48-1203 text, which carries "Laws 2026, LB258, s.1; Effective Date July 18, 2026".
- https://nebraskalegislature.gov/laws/statutes.php?statute=48-3802 - only the pre-LB415 snapshot (2025-03-11) exists. The LB415 slip law was read instead.
- (no URL) `https://web.archive.org/cdx/search/cdx?...dol.nebraska.gov/PressRelease/Details/*`: the Internet Archive CDX was "Temporarily Offline".
- (no URL) All three NE hosts: DNS failure from this machine (VPN off). A US-exit retry would allow direct reads.

## NH (9 URLs, 1 without URL)
_Journal queue:_ nh.gov (403 sem IP EUA): regras Emp 300 (gc.nh.gov), RSA 275:37-f, NHES new-hire, NHES 0047, status HB 1484/SB 416, confirmação 1,7% novo empregador.
- https://gc.nh.gov/ - All nh.gov hosts returned HTTP 403 to curl from a non-US IP (VPN off), so the work went through Wayback. Hosts: , https://www.gencourt.state.nh.us/, https://www.nhes.nh.gov/, https://www.dol.nh.gov/, https://www.revenue.nh.gov/, https://www.p
- https://www.gencourt.state.nh.us/ - All nh.gov hosts returned HTTP 403 to curl from a non-US IP (VPN off), so the work went through Wayback. Hosts: https://gc.nh.gov/, , https://www.nhes.nh.gov/, https://www.dol.nh.gov/, https://www.revenue.nh.gov/, https://www.p
- https://www.nhes.nh.gov/ - All nh.gov hosts returned HTTP 403 to curl from a non-US IP (VPN off), so the work went through Wayback. Hosts: https://gc.nh.gov/, https://www.gencourt.state.nh.us/, , https://www.dol.nh.gov/, https://www.revenue.nh.gov/, https://www.p
- https://www.dol.nh.gov/ - All nh.gov hosts returned HTTP 403 to curl from a non-US IP (VPN off), so the work went through Wayback. Hosts: https://gc.nh.gov/, https://www.gencourt.state.nh.us/, https://www.nhes.nh.gov/, , https://www.revenue.nh.gov/, https://www.p
- https://www.revenue.nh.gov/ - All nh.gov hosts returned HTTP 403 to curl from a non-US IP (VPN off), so the work went through Wayback. Hosts: https://gc.nh.gov/, https://www.gencourt.state.nh.us/, https://www.nhes.nh.gov/, https://www.dol.nh.gov/, , https://www.p
- https://www.paidfamilymedicalleave.nh.gov/ - All nh.gov hosts returned HTTP 403 to curl from a non-US IP (VPN off), so the work went through Wayback. Hosts: https://gc.nh.gov/, https://www.gencourt.state.nh.us/, https://www.nhes.nh.gov/, https://www.dol.nh.gov/, https://www.revenue.nh.gov/, https://www.p
- https://gc.nh.gov/rules/state_agencies/emp300.html - (NHES Emp 300 rules, incl. Emp 303.02 due dates): not in Wayback for 2024, 2025 or 2026, on either host.
- https://www.gc.nh.gov/rsa/html/XXIII/275/275-37-f.htm - (parental medical leave): direct 403, and the Wayback copy of 2026-06-17 is the 403 page.
- https://www.nhes.nh.gov/employers/new-hire-reporting - 403. The statute was read instead.
- (no URL) NHES 0047 Electronic Wage Reporting instructions (file format for the quarterly wage file): not fetched. Wayback was rate-limiting (HTTP 429) during the run.

## NJ (10 URLs)
_Journal queue:_ lis.njleg (2A:17-56, 34:21-2, 34:11-56a4, 34:11D-2/-3, 43:21-6/-7, nº do capítulo S.B. 4219), pub.njleg P.L.2005 c.226, notícias Tesouro/DOL 2026.
- https://pub.njleg.gov/Bills/2004/PL05/226_.HTM - and `https://pub.njleg.gov/bills/2004/PL05/226_.HTM`: curl returned status 000 (connection failed), twice. Needed for the SSN rule, C.56:8-164.
- https://pub.njleg.gov/bills/2004/PL05/226_.HTM - `https://pub.njleg.gov/Bills/2004/PL05/226_.HTM` and : curl returned status 000 (connection failed), twice. Needed for the SSN rule, C.56:8-164.
- https://lis.njleg.state.nj.us/nxt/gateway.dll?f=templates&fn=default.htm&vid=Publish:10.1048/Enu - the NJ statutes database renders only in a browser (see US-NJP9M-001). Not tried with curl. Sections needed: 2A:17-56, 34:21-2, 34:11-56a4, 34:11D-2/-3, 43:21-6
- https://www.njleg.state.nj.us/bill-search/2024/S4219 - a JS application. Needed for the chapter number and approval date of S.B. 4219.
- https://www.njcourts.gov/sites/default/files/forms/11471_wage_exec_appndx_xi_j.pdf - 403. The Wayback `2026id_` copy was used instead (row US-NJS5-021).
- https://www.nj.gov/treasury/taxation/news.shtml - 404. `https://www.nj.gov/labor/lwdhome/press/2026/`: 404. Bulletin sweep incomplete.
- https://www.nj.gov/labor/lwdhome/press/2026/ - `https://www.nj.gov/treasury/taxation/news.shtml`: 404. : 404. Bulletin sweep incomplete.
- https://www.nj.gov/labor/employer-services/warn/ - returns an Incapsula meta-refresh to `https://www.nj.gov/labor/business-services/layoffs-and-closing/file-warn-notice/` (not followed; the WARN form was used instead).
- https://www.nj.gov/labor/business-services/layoffs-and-closing/file-warn-notice/ - `https://www.nj.gov/labor/employer-services/warn/`: returns an Incapsula meta-refresh to  (not followed; the WARN form was used instead).
- https://www.nj.gov/labor/wageandhour/tools-resources/laws/minimumwage.shtml - 404 (the press releases and FAQ were used instead).

## NM (8 URLs, 2 without URL)
_Journal queue:_ nmlegis.gov/nmonesource (texto atual de leis; pagamento final 50-4-4 só reimpressão 2017), Las Cruces/Bernalillo/Santa Fe County mínimos, FAQ DWS, esquema de envio em lote, specs UI.
- https://lascruces.gov/minimum-wage-notice-for-2026/ - (403 direct; Wayback 403): Las Cruces 2026 rate.
- https://www.bernco.gov/planning/required-workplace-postings.aspx - (403): Bernalillo County rate.
- https://www.santafecountynm.gov/living-wage - (404; the correct URL is unknown): Santa Fe County living wage.
- https://www.dws.nm.gov/Businesses/Rules-and-Regulations/Labor-Relations-FAQs - (Wayback 403).
- https://www.dws.nm.gov/Portals/0/DM/LaborRelations/New_Mexico_Minimum_Wage_Act.pdf - (Wayback 404).
- https://www.nmlegis.gov/ - and https://nmonesource.com/ (403; current compiled NMSA unreadable): 50-4-4/-5 current text, 51-1-11, 51-1-42, 57-12B, 50-6, 7-2-2.
- https://nmonesource.com/ - https://www.nmlegis.gov/ and  (403; current compiled NMSA unreadable): 50-4-4/-5 current text, 51-1-11, 51-1-42, 57-12B, 50-6, 7-2-2.
- https://www.hca.nm.gov/ - (403): child-support IWO employer fee.
- (no URL) realfile.tax.newmexico.gov TRD-41431 instructions (`trd-41431ins.pdf` 404); the TAP bulk-filing schema (inside TAP).
- (no URL) DWS wage file format specifications (Delimited/ICESA/XML/EFW2), linked from the UI pages on www.dws.nm.gov (403).

## NV (9 URLs)
_Journal queue:_ PDFs do Labor Commissioner (captcha — só leitura humana: AB 307 2026-10-01, boletim 2026-04-24), nome do formulário trimestral UI.
- https://www.leg.state.nv.us/NRS/NRS-608.html - HTTP 403. Same for every leg.state.nv.us page. All read via web.archive.org.
- https://detr.nv.gov/Page/UI_Information_for_Employers - and `https://detr.nv.gov/Page/New_Hire_Reporting_Info`: HTTP 403 (archive copies used).
- https://detr.nv.gov/Page/New_Hire_Reporting_Info - `https://detr.nv.gov/Page/UI_Information_for_Employers` and : HTTP 403 (archive copies used).
- https://ui.nv.gov/ - HTTP 403.
- https://cms.detr.nv.gov/Content/Media/Unemployment_Insurance_Tax.pdf - HTTP 403, with no archive copy.
- https://nevadaworkforce.com/_docs/EDS_Wage-Benefit/MWB-Statewide-2026.pdf - HTTP 000 (archive copy used).
- https://labor.nv.gov/uploadedFiles/labornvgov/content/Employer/*.pdf - bot-check (captcha) page.
- https://labor.nv.gov/uploadedFiles/labornvgov/content/Employer/AB%20307%20Q1%20Required%20Posting%2010.01.2026%20(EN - `).pdf`: bot check, and the archive has no copy (404). **For the browser pass.**
- https://labor.nv.gov/uploadedFiles/labornvgov/content/Employer/Domestic%20Violence%20and%20Sexual%20Assault%20Victim - `'s%20Leave%20Bulletin%2004.24.2026.pdf`: not fetched (budget). **For the browser pass.**

## NY (6 URLs)
_Journal queue:_ DFS decisão PFL 2027 (403), paidfamilyleave.ny.gov/2026 (403), nyc.gov Protected Time Off + FAQ DCWP 02/2026.
- https://www.dfs.ny.gov/apps-and-licensing/health-insurers/pfl-rate-decision-2027-page - HTTP 403 (curl). `https://web.archive.org/web/2026id_/…pfl-rate-decision-2027-page`: 404. Needed for PFL 2027 rate and cap (US-NYS5-022).
- https://paidfamilyleave.ny.gov/2026 - 403. Wayback 2026id_: 403. Needed for the PFL 2026 maximum weekly benefit as an authority figure.
- https://www.nyc.gov/site/dca/about/paid-sick-leave-law.page - 403 (wayback copy used). The DCWP FAQ (02/2026) PDF and NYC Admin. Code 20-911 ff. were not reached (US-NYS5-023).
- https://dol.ny.gov/overtime-0 - and `https://dol.ny.gov/overtime-frequently-asked-questions`: 404 (overtime covered instead by CR 142).
- https://dol.ny.gov/overtime-frequently-asked-questions - `https://dol.ny.gov/overtime-0` and : 404 (overtime covered instead by CR 142).
- https://www.tax.ny.gov/pdf/publications/withholding/nys50.pdf - 404. The guide now exists only as HTML (`/forms/publications/wt/nys50.htm`, used).

## OH (7 URLs)
_Journal queue:_ tax.ohio.gov municipal rate table / The Finder (taxas municipais 2026); lista completa de school districts 2026.
- https://tax.ohio.gov/business/employer-withholding - 404/403 shell to scripts. The Wayback copy https://web.archive.org/web/2026id_/ resolves to 20260923233444 and also gives 404. Tried once.
- https://tax.ohio.gov/employer - and https://tax.ohio.gov/business/ohio-business-taxes/employer-withholding: 404 shell. The municipal rate table on tax.ohio.gov could therefore not be read.
- https://tax.ohio.gov/business/ohio-business-taxes/employer-withholding - https://tax.ohio.gov/employer and : 404 shell. The municipal rate table on tax.ohio.gov could therefore not be read.
- https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/ohio_individual/2026_All_School_Districts.pdf - 404 (no 2026 full list at that path).
- https://jfs.ohio.gov/unemployment-services/for-employers/file-unemployment-taxes/tax-resources/contribution-rates - 404 to curl. The contents are held by US-OH-005 (earlier read) and US-OHS5-002.
- https://thefinder.tax.ohio.gov/ - application shell only (lookup per address, no table).
- https://www.ritaohio.com/Businesses/Faqs - RITA : HTTP 200 at the root this pass, but the employer FAQ was not re-read (US-OH-014 stays gated).

## OK (5 URLs)
_Journal queue:_ regras OESC OAC 240:10 (prazo OES-3).
- https://www.oscn.net/applications/oscn/DeliverDocument.asp?CiteID=77475 - HTTP 000 (timeout). Replaced by the Legislature's complete-title RTFs.
- https://oklahoma.gov/oesc/employers/tax/oklahoma-employers-quarterly-contribution-report.html - 404.
- https://oklahoma.gov/oesc/employers/employer-resources-and-forms/oklahoma-employers-quarterly-contribution-report.html - 404. The Wayback `2026id_` copy (20250222) is also 404. This page should hold the OES-3 due date.
- https://oksenate.gov/press-releases/sen-corn-rep-smithson-announce-tax-cut-working-oklahomans - JavaScript bot wall. The Wayback copy (20260710) showed it is a 2008 release.
- https://eztaxexpress.oesc.ok.gov/Help/UserGuides/UserGuide_Full.pdf - (7 MB): read, not kept. It has no due date.

## OR (4 URLs)
- https://www.oregonlegislature.gov/bills_laws/ors/ors653.html - (and every `/bills_laws/ors/` page): the connection failed (curl HTTP 000) from a BR exit with the VPN off. Bypassed via web.archive.org snapshots; not a content gap.
- https://www.doj.state.or.us/child-support/for-employers/new-hire-reporting/ - 404 (wrong path). The working page is `/report-new-hires/`.
- https://www.oregon.gov/boli/workers/pages/final-paycheck.aspx - 404. The vacation and final-pay content came from `holiday-and-vacation-pay.aspx` and ORS 652.140.
- https://www.oregon.gov/employ/businesses/tax/pages/default.aspx - 404. The UI rates came from the OED release and ORS 657.

## PA (7 URLs)
_Journal queue:_ pittsburghpa.gov licença remunerada (403), Philadelphia Code 9-4100 amlegal (403), phila.gov licença (404), panewhires.com (DNS).
- https://www.pittsburghpa.gov/mayor/paidsickleave - — 403 (direct and `web.archive.org/web/2026id_/`).
- https://www.pittsburghpa.gov/City-Government/Mayor/Equity-Commissions/Office-of-Equity/Paid-Sick-Days-Act - — 403.
- https://codelibrary.amlegal.com/codes/philadelphia/latest/philadelphia_pa/0-0-0-201085 - (Phila. Code 9-4100) — 403.
- https://www.phila.gov/services/working-in-philadelphia/workers-rights/paid-sick-leave/ - — 404.
- https://www.panewhires.com/ - — connection failed (curl exit 6, DNS).
- https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/uc-tax/quarterly-reports - — 404 (covered by UC-2INS instead).
- https://www.uc.pa.gov/documents/uc_law.pdf - — redirects to pa.gov search (covered by the legis.state.pa.us PDF instead).

## RI (6 URLs, 1 without URL)
_Journal queue:_ RIGL 28-14-12 (versão 2026-01-01), H 5679/2025, RIGL 44-30-71, 280-RICR-20-55-10, notícias DLT, semanas TCI (6/7/8).
- https://webserver.rilegislature.gov/Statutes/TITLE28/28-14/28-14-12_28-14-12.htm - 28-14-12 [Effective January 1, 2026]. Live host curl 000; Wayback `2026id_` 404 (not archived).
- https://webserver.rilegislature.gov/BillText25/HouseText25/H5679A.htm - 2025 H 5679 text. Live curl 000; Wayback 404. The exact bill-text file name is a guess.
- https://webserver.rilegislature.gov/Statutes/TITLE44/44-30/44-30-71.htm - withholding duty (keeps US-RI-002 gated). Live curl 000; Wayback 404.
- https://rules.sos.ri.gov/regulations/part/280-20-55-10 - regulation text (US-RI-006). Not re-tried this run; known to show only the table of contents.
- https://dlt.ri.gov/ - and `https://tax.ri.gov/tax-sections/withholding-tax`: 403 to plain curl (VPN off). All DLT/Taxation reads used Wayback.
- https://tax.ri.gov/tax-sections/withholding-tax - `https://dlt.ri.gov/` and : 403 to plain curl (VPN off). All DLT/Taxation reads used Wayback.
- (no URL) `https://web.archive.org/cdx/search/cdx?url=webserver.rilegislature.gov/Statutes/TITLE28/28-14/28-14-12*` and `...BillText25/HouseText25/H5679*`: "Internet Archive temporarily offline" at 08:39 BRT.

## SC (5 URLs)
_Journal queue:_ dew.sc.gov (taxas UI 2026/2027, sobretaxa, SUITS PDF atual), newhire.sc.gov.
- https://dew.sc.gov/employers/tax-rate-information - HTTP 403 (direct curl, US exit IP). The wayback 2026-06-07 copy is already held (US-SC-003).
- https://dew.sc.gov/employers/ui-tax-forms - no response (curl code 000). The wayback 2026-10-09 copy is held.
- https://dew.sc.gov/sites/dew/files/Documents/SUITS-%20Wage%20Report%20and%20Payment%20File%20Specification%20version%201.6%2010.25.2023.pdf - HTTP 403. Retrieved via the wayback 2025-08-04 capture.
- https://dew.sc.gov/employers/file-and-pay-taxes - no wayback capture (404).
- https://newhire.sc.gov/ - no response directly. The wayback 2026-10-16 copy is a JavaScript shell with no content.

## SD (1 URLs, 1 without URL)
- https://www.yahoo.com/news/articles/2026-reemployment-rate-schedule-won-184909006.html - HTTP 429. Tier-B lead only; superseded by the RAAC minutes (A.2).
- (no URL) The DLR comma-delimited online upload layout sits behind the Internet Quarterly Wage Reporting System login (`gated`). The public CD/DVD layout was obtained.

## TN (8 URLs, 1 without URL)
_Journal queue:_ capitol.tn.gov HB1958, PC 617/2026 (tnsosfiles 403), HRC licença-maternidade, DLWD trabalho infantil, mudanças 2026 workers' comp.
- https://wapp.capitol.tn.gov/apps/BillInfo/Default.aspx?BillNumber=HB1958&GA=114 - curl timeout (000), WebFetch ECONNREFUSED 170.142.7.21:443.
- https://www.capitol.tn.gov/Bills/114/Bill/HB1958.pdf - curl timeout (000).
- https://publications.tnsosfiles.com/acts/114/pub/pc0617.pdf - HTTP 403.
- https://www.tn.gov/humanrights/laws-and-regu1/maternity-leave1.html - HTTP 404 (page moved). The Wayback attempt was blocked by the session permission classifier and was not retried.
- https://sos.tn.gov/elections/voter-information - HTTP 403. Wayback not attempted (same classifier block).
- https://www.tn.gov/workforce/injuries-at-work/bwc-newsroom/2026/7/10/2026-workers-compensation-legislative-changes-tennessee.html - HTTP 403 (tn.gov began rate-limiting curl at about 08:10).
- https://www.tn.gov/workforce/employees/labor-laws/labor-laws-redirect/child-labor.html - HTTP 403 (same).
- https://www.tn.gov/content/dam/tn/workforce/documents/employers/HandbookforEmployers6-13-19.pdf - HTTP 404 (retired).
- (no URL) T.C.A. (Lexis Advance public site): not readable by curl, so no A.1 statute row.

## TX (4 URLs, 1 without URL)
_Journal queue:_ twc.texas.gov (HTTP 202 vazio; notícias 2026 para live_legal_change), 40 TAC 815.106/815.107, OAG employer portal. Ver _research/stage5/TX.md.
- https://www.twc.texas.gov/programs/unemployment-tax/your-tax-rates - HTTP 202, empty body. Wayback `https://web.archive.org/web/2026id_/` returns 302, then a blocked capture. The 2026 figures a
- https://texreg.sos.state.tx.us/public/readtac$ext.TacPage?...ti=40&pt=20&ch=815&rl=107 - (40 TAC 815.107, wage report due date) and the analogous rule 815.106 (records): "Site Has Moved" page. The new SOS TAC host was not resolved.
- https://www.texasattorneygeneral.gov/sites/default/files/files/child-support/Publications/new-hire.pdf - and `.../Publications/csquickrefemp.pdf`: HTTP 404 (the form PDF was read instead).
- https://employer.oag.texas.gov/ - Salesforce app shell with no readable content (lump-sum notification and independent-contractor reporting pages not read).
- (no URL) `https://web.archive.org/web/2026id_/https://www.twc.texas.gov/programs/unemployment-tax/employers-quarterly-wage-report-filing-options`: HTTP 403. Needed for the quarterly due date.

## UT (11 URLs, 4 without URL)
_Journal queue:_ le.utah.gov 34-40-104, 59-10-402, 35A-4-303, 35A-4-205, 70C-7-103; tax/jobs/laborcommission.utah.gov (403); vigência Pub 14 (2026-06-01?).
- https://tax.utah.gov/withholding
- https://tax.utah.gov/forms/pubs/pub-14.pdf - (the Pub 14 HTML is held via Wayback)
- https://jobs.utah.gov/ui/employer/Public/Questions/TaxRates.aspx - (held via Wayback 2026-06-11)
- https://laborcommission.utah.gov/divisions/antidiscrimination-and-labor-ald/wage-claims/
- https://tap.utah.gov/
- https://le.utah.gov/xcode/Title34/Chapter40/C34-40-S104_2023050320230503.html - (minimum-wage exemptions)
- https://le.utah.gov/xcode/Title59/Chapter10/C59-10-S402_2022050420230101.html - and `.pdf` (withholding duty; R865-9I-14 used instead)
- https://le.utah.gov/xcode/Title35A/Chapter4/C35A-4-S303_2021111020211116.html - (SUI wage base and other-state wages)
- https://le.utah.gov/xcode/Title35A/Chapter4/C35A-4-S205_1800010118000101.html - (exempt employment)
- https://le.utah.gov/xcode/Title70C/Chapter7/C70C-7-S103_2014040320140327.html - (garnishment limit)
- https://acf.gov/css/contact-information/state-income-withholding-contacts-and-program-requirements - **202 bot challenge:**  (UT IWO fee and remittance timing).
- (no URL) **403 direct; Wayback version not archived or not tried:**
- (no URL) **Timeout direct; Wayback 404 for the current version file:**
- (no URL) **Wayback CDX:** `laborcommission.utah.gov/*` returned empty or "Temporarily Offline" (2026-11-02).
- (no URL) **Route for the orchestrator's pass:** with a US exit IP, `le.utah.gov` will likely serve these sections directly. The versions named above are the current files.

## VA (5 URLs, 1 without URL)
_Journal queue:_ VEC pool-cost % 2026 (Q2), VEC notícias PFML.
- https://www.vec.virginia.gov/sites/default/files/2026-04/PFML%20FAQ%204.22.26.pdf - F5 403 to curl on 2026-11-02 (support ID 3c5d96ef…). Obtained through `web.archive.org/web/2026id_/…` instead.
- https://www.vec.virginia.gov/pfml-news - F5 403 on 2026-11-02. Not retried.
- https://legacylis.virginia.gov/cgi-bin/legp604.exe?261+ful+CHAP0981 - connection returned 000 (no response). The chapter text was replaced by the codified 60.2-806.
- https://www.tax.virginia.gov/legislative-summaries - 404.
- https://www.doli.virginia.gov/labor-law/minimum-wage/ - redirects to a 2021 article (file deleted). The current figures were read on `doli.virginia.gov/programs/labor-law/payment-of-wage/`.
- (no URL) 2026 VEC pool-cost charge: no VEC page carrying the 2026 percentage was reached. The VEC host is intermittently blocked by F5; the FAQ page was readable at 07:31 and blocked by 07:33.

## VT (6 URLs, 1 without URL)
_Journal queue:_ tax.vermont.gov e labor.vermont.gov (403): mínimo 2027, base UI 2027, cronograma de taxas UI desde 2026-07-01, VT Saves, Acts 91/177 de 2026, 21 V.S.A. 471 atual.
- https://tax.vermont.gov/business/withholding - — 403 (VPN off). Live editions of GB-1210, W-4VT and WHT-436 not confirmed.
- https://labor.vermont.gov/unemployment-insurance/ui-employers/unemployment-tax-rates - — 403. The latest Wayback 200 capture is 2025-07-15; the 2025-12 and 2026-02 captures are 403.
- https://labor.vermont.gov/press-release/vermont-department-labor-announces-minimum-wage-increase-starting-january-2027 - — no capture (and direct 403).
- https://labor.vermont.gov/press-release/vermont-department-labor-announces-unemployment-insurance-taxable-wage-base-2027 - — no capture.
- https://www.vermonttreasurer.gov/node/4603 - (VT Saves) — 403, no Wayback 200.
- https://legislature.vermont.gov/Documents/2026/Docs/ACTS/ACT091/ - , …/ACT177/ — Wayback CDX "Temporarily Offline" during the run.
- (no URL) legislature.vermont.gov direct — timeout (code 000). All statutes were read via Wayback.

## WA (5 URLs)
_Journal queue:_ paidleave.wa.gov responsabilidades do empregador (403), seattle.gov (TLS), RCW 26.23 versão viva; WAC 192-310-030 e cap. 192-510 (125/401k/HSA nas bases UI/PFML/WA Cares — prioridade).
- https://paidleave.wa.gov/employer-roles-responsibilities/ - HTTP 403 directly. The Wayback copy `https://web.archive.org/web/2026id_/` also returns 403 (snapshot 20260916). This blocks the PFML/WA Cares
- https://www.seattle.gov/ - (all paths): TLS failure (`SEC_E_INVALID_TOKEN`). The Wayback copy `https://web.archive.org/web/2026id_/laborstandards/ordinances/minimum-wage` returns 403. This blocks Seattle's 2027 minimum wage, Paid Sick a
- https://app.leg.wa.gov/ - and `https://lawfilesext.leg.wa.gov/`: TLS failure. Handled through Wayback `id_` snapshots (see Access findings). Before stage 1 consumes them, the synthesis should re-verify the RCW 26.23 snapshot (2025-09) against the live site thr
- https://lawfilesext.leg.wa.gov/ - `https://app.leg.wa.gov/` and : TLS failure. Handled through Wayback `id_` snapshots (see Access findings). Before stage 1 consumes them, the synthesis should re-verify the RCW 26.23 snapshot (2025-09) against the live site thr
- https://lni.wa.gov/insurance/premiums/report-pay-premiums/ - 404. This was a guessed URL; the L&I quarterly report page was not located.

## WI (7 URLs)
_Journal queue:_ formulário WT-4 (edição), página de penhora por dívida tributária.
- https://docs.legis.wisconsin.gov/statutes/statutes/134/98 - and `https://docs.legis.wisconsin.gov/statutes/statutes/134.pdf`: timed out (curl exit 28). The host stopped answering after about 8 requests. Ch. 134 was taken from `https://web.archive.org/web/2026i
- https://docs.legis.wisconsin.gov/statutes/statutes/134.pdf - `https://docs.legis.wisconsin.gov/statutes/statutes/134/98` and : timed out (curl exit 28). The host stopped answering after about 8 requests. Ch. 134 was taken from `https://web.archive.org/web/2026i
- https://docs.legis.wisconsin.gov/statutes/statutes/109.pdf - the 10-1-26 edition was not fetched; the 6-25-25 edition is on disk.
- https://www.revenue.wi.gov/DORForms/wt-4.pdf - and `https://www.revenue.wi.gov/TaxForms2026/wt-4.pdf`: 404 (guessed paths). The WT-4 URL is not linked from W-166 or Update 2026-1.
- https://www.revenue.wi.gov/TaxForms2026/wt-4.pdf - `https://www.revenue.wi.gov/DORForms/wt-4.pdf` and : 404 (guessed paths). The WT-4 URL is not linked from W-166 or Update 2026-1.
- https://www.revenue.wi.gov/Pages/Businesses/New-Development/home.aspx - 404 (guessed DOR news path).
- https://dwd.wisconsin.gov/uitax/rates.htm - 404 (the right pages are under `/ui/employers/taxrates/`).

## WV (4 URLs, 1 without URL)
_Journal queue:_ code.wvlegislature.gov (só IP EUA): 21-5C-2, 21-5-1, 21A-5-5 (2026), 11-21-74, 11-21-12, 48-14; aviso WorkForce WV sobre taxa SB 1053 (7% de salários ou de contribuições?); taxas de serviço de 8 cidades.
- https://code.wvlegislature.gov/* - returns a 302 to `https://www.fbi.gov/investigate/cyber` from a non-US IP (VPN off). Retry with the US exit for
- https://www.fbi.gov/investigate/cyber - `https://code.wvlegislature.gov/*` returns a 302 to  from a non-US IP (VPN off). Retry with the US exit for
- https://bills.wvlegislature.gov/bill/history/2026/RS/HB5485 - 403, Cloudflare bot check. I used the classic Bill_Status page instead.
- https://tax.wv.gov/Documents/Withholding/it100.1a.pdf - 404. The document has been withdrawn; IT-100.2A and IT-100.2B replace it.
- (no URL) `https://web.archive.org/web/2026id_/https://code.wvlegislature.gov/pdf/21-5C-2/` and `.../pdf/21-5-1/`: timeout (HTTP 000) twice.

## WY (2 URLs, 2 without URL)
_Journal queue:_ dws.wyo.gov (403 sem IP EUA): comunicado de taxas UI jan/2026 (mín/máx, novos empregadores, fator de ajuste), formatos do relatório trimestral e new hire.
- https://dws.wyo.gov/* - HTTP 403 to plain curl (no US VPN). Read through wayback `id_` copies dated 2026-02-13 to 2026-10-20.
- https://newhire-reporting.com/wy-newhire/ - the direct connection failed (HTTP 000), and the wayback copy returned 403. New-hire portal formats and fields beyond the statute were not read.
- (no URL) `https://web.archive.org/web/2026id_/https://dws.wyo.gov/dws-division/labor-standards/employers/faq/`: 404 (not archived).
- (no URL) The wayback availability API returned 429 (rate-limited, shared by parallel workers).

