# Mandate answers P5-W3D-r1 - WV ID NM DC (PASS 4, wave 3D, round 1, 2026-10-29)

Hunter: compliance-source-hunter. Parts worked = blocking list in build-manifest.json (WV 1,2,3,4,6; ID 1-6; NM 1-6; DC 1-6); no earlier PASS 4 section covered these states. Register: `00-official-sources/_register-shards/mandate-P5-W3D-r1.csv` (32 rows, ids US-<UF>-P5-1-NNN; the `supersedes` column names the older rows). Budget about 12 reads per state, not exceeded. Own Chrome tab (closed at end), get_page_text/find/read_page only, no javascript_tool. Wayback: one request per 10 s, no 429 seen; copies saved under `00-official-sources/pdfs/<UF>/` and read locally with PyMuPDF/text.

Access findings: otr.cfo.dc.gov and dws.nm.gov return Access denied / 403 in Chrome and WebFetch; labor.idaho.gov, tax.idaho.gov and legislature.idaho.gov refuse connections; code.wvlegislature.gov and www.wvlegislature.gov redirect to fbi.gov (browser and WebFetch) so every WV code section was read from Wayback PDFs. WebFetch is a small-model extract; rows from it carry verification_method `webfetch-extract` and are one confidence step lower.

## DC (US-MQ-27)
1. Wage tax: PARTIAL, confidence MEDIUM. Employer withholding by percentage method or tables similar to IRC 3402, no standard-deduction allowance, optional rounding to the nearest dollar, extra withholding only by agreement, annual statements by Jan 31 [US-DC-P5-1-001]. DC publishes no tables since TCJA: employers use the DC rate schedule and the federal allowance amount [US-DC-P5-1-002, notice dated 2022-10-17]; no FR-230 after 2018 exists on the OTR page [US-DC-P5-1-004]; FR-230 2016 kept as historical structure only [US-DC-P5-1-005]. Filing: FR-900Q electronic on MyTax.DC.gov, FR-900A annual under 200 USD, D-4/D-4A "under review" [US-DC-P5-1-003]. Missing: a 2026-specific OTR notice or schedule for withholding and any supplemental-wage rate (none found on the pages read; the statute has none).
2. Local: ANSWERED (structural), MEDIUM. DC is itself the only taxing jurisdiction; no city/county/school-district wage taxes; Home Rule Act bars taxing nonresident income [US-DC-P5-1-006].
3. SUI: ANSWERED, HIGH. DOES; 2026 wage base 9,000 USD; new employer 2.7% plus 0.2% administrative assessment; employee does not contribute [US-DC-P5-1-008, US-DC-P5-1-009]. Effective 2026-01-01.
4. Levies: ANSWERED, HIGH on rate / MEDIUM on completeness. Paid Family Leave: 0.75% of wages, employer-funded, not deductible from pay, 2026 all quarters [US-DC-P5-1-010, US-DC-P5-1-011]; the older 0.62% figure [US-DC-PFL-001] is superseded. No state SDI/TDI program located.
5. Multistate: ANSWERED, MEDIUM. No reciprocity agreements; nonresidents are not taxed on DC wages (D-4A certificate) [US-DC-P5-1-006]; residents get a credit for tax paid to another state [US-DC-P5-1-007].
6. Pay statement / POA / oracle: PARTIAL. Pay statement D.C. Code 32-1008(b) incl. new item (6A) from 2026-01-01 and language rule in (c) [US-DC-P5-1-012]; payday frequency 32-1302 [US-DC-P5-1-013]; tax POA Form D-2848 [US-DC-P5-1-014]; UI POA: DOES form required in ESSP [US-DC-P5-1-008]. NOT LOCATED after a real read: state prevailing-wage statute (only a search summary pointing to DOES Office of Wage-Hour and D.C. Law 25-274; not read); official withholding calculator (none; OTR publishes no 2026 tables, re-derive from the DC rate schedule).

## ID (US-MQ-33)
1. Wage tax: ANSWERED, HIGH. Statute Idaho Code 63-3035 (Commission tables) [US-ID-P5-1-001]; method, rounding and 5.3% supplemental already read in [US-ID-001] (copy 2026-10-10).
2. Local: PARTIAL. No local layer appears on the Tax Commission withholding pages read [US-ID-001, withholding employers page copy 2026-10-12]; absence by silence only, no statute read.
3. SUI: ANSWERED, HIGH. Idaho DOL Rate Class Array effective 2026-01-01: wage base 58,300 USD; standard rate 1.000% (0.97 UI + 0.03 workforce development); admin rate 0.000% [US-ID-P5-1-003]. Closes the earlier unconfirmed 58,300 [US-ID-002]. Employee contribution: none shown.
4. Levies: PARTIAL. Workforce development component is inside the 1.000% [US-ID-P5-1-003]; no SDI/PFML program located (absence not proven).
5. Multistate: OPEN. No Idaho reciprocity or nonresident source read (tax.idaho.gov unreachable; the nonresident page has no Wayback copy).
6. Pay statement / POA / oracle: PARTIAL. Idaho Code 45-609(2): statement of deductions each pay period, misdemeanor if willful [US-ID-P5-1-002]. NOT LOCATED: tax POA form (page without snapshot), UI agent authorization, prevailing-wage statute, language notice, official calculator.

## NM (US-MQ-52)
1. Wage tax: PARTIAL, MEDIUM. TRD page: tables in FYI-104, federal W-4 allowances, FYI-330 information returns due end of February [US-NM-P5-1-003]. FYI-104 2026 is listed but its PDF opens through a javascript link and could not be read [US-NM-P5-1-005, status MANUAL]; the 5.9% supplemental rate is secondary only.
2. Local: OPEN. No source read.
3. SUI: ANSWERED, HIGH. 2026 taxable wage base 34,800 USD [US-NM-P5-1-001]; new employers: greater of industry average or 1% (2026 industry table 1.00-1.28) [US-NM-P5-1-002]; no employee contribution mentioned on those pages.
4. Levies: PARTIAL. No paid-leave program page found on DWS; bill-stage text only [US-NM-004]; enactment not confirmed by a primary source.
5. Multistate: OPEN. No source read.
6. Pay statement / POA / oracle: PARTIAL. Tax POA ACD-31102 (Rev. 03/27/2023) [US-NM-P5-1-004]; UI: TPA registration via Agent Login [US-NM-P5-1-001]. Pay statement NMSA 50-4-2 remains a search-excerpt citation [US-NM-003]; the nmonesource copy returned no usable text. NOT LOCATED: prevailing-wage statute, language notice, calculator.

## WV (US-MQ-69)
1. Wage tax: ANSWERED, HIGH on method / MEDIUM on supplemental. W. Va. Code 11-21-71 [US-WV-PIT-001], IT-100.2A March 2026 tables re-read (exemption 2,000 USD, brackets 2.11% to 4.58%) [US-WV-P5-1-005], filing rules [US-WV-P5-1-003, US-WV-P5-1-004]. Supplemental/bonus rate NOT in the tables file.
2. Local: PARTIAL. Municipal payroll service fees exist under W. Va. Code 8-13-13 per search summaries only; statute body unreadable [US-WV-P5-1-010, gated].
3. SUI: PARTIAL, MEDIUM. New employer 2.7% (36 months) per 21A-5-5 copy of 2025-11-10 [US-WV-P5-1-007]; the 2026 amendments (rate reduction and 7% automation fee from 2026-07-01) and wage base 9,500 USD are secondary only; 2026 text unreadable.
4. Levies: PARTIAL. 2026-07-01 automation/administration fee reported but unread; no PFML/SDI program located.
5. Multistate: ANSWERED, HIGH. Exception by regulation under 11-21-71(c) [US-WV-P5-1-001]; nonresident credit only under written agreement, 11-21-40 [US-WV-P5-1-002]; WV/IT-104 certificate (states listed in US-WV-PIT-002).
6. Pay statement / POA / oracle: PARTIAL. CORRECTION: W. Va. Code 21-5-3 (copy 2025-04-21) contains no itemized-statement rule, so the older snippet [US-WV-LAB-001] is unsupported [US-WV-P5-1-008]. Prevailing wage: 21-5A-3 repealed 2016 [US-WV-P5-1-009]. Tax POA WV-2848 [US-WV-P5-1-006]. NOT LOCATED: where (if anywhere) WV requires a pay statement, UI agent form, language notice, calculator.

## PASS 4 (wave 3D) - status after this pass
DC 1:partial 2:answered 3:answered 4:answered 5:answered 6:partial
ID 1:answered 2:partial 3:answered 4:partial 5:open 6:partial
NM 1:partial 2:open 3:answered 4:partial 5:open 6:partial
WV 1:answered 2:partial 3:partial 4:partial 5:answered 6:partial
Gated/unreadable: DC OTR (Access denied), NM DWS (403), ID hosts (connection refused), WV legislature (redirect to fbi.gov), NM FYI-104 PDF (javascript link), DC PFL toolkit PDF (no text in Chrome), WV 8-13-13 (script-rendered). No CAPTCHA seen. All Wayback copies are 2025/2026.
