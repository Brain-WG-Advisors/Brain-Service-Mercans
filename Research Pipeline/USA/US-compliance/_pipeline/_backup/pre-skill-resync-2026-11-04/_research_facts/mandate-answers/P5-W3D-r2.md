# P5-W3D-r2 - wave 3 (DC, ID, NM, WV), second round (2026-10-29)

Method: different pages from round 1 (agency publications and indexes, enrolled bill text, form files). Sources: WebFetch of unblocked hosts (PDFs saved under 00-official-sources/pdfs/<UF>/ and read with PyMuPDF), Claude in Chrome own tab (HTML only; Chrome returns no text for PDFs), Wayback copies of 2025/2026. Wayback requests from Python returned HTTP 429 from the first call on (shared IP); Chrome Wayback HTML worked. Register: `_register-shards/mandate-P5-W3D-r2.csv` (ids US-<UF>-P5-2-NNN).

## Status after this round
DC  1:partial 2:answered 3:answered 4:answered 5:answered 6:answered
ID  1:answered 2:absence_proven 3:answered 4:answered 5:answered 6:partial
NM  1:answered 2:absence_proven 3:answered 4:partial 5:answered 6:partial
WV  1:answered 2:partial 3:answered 4:partial 5:answered 6:partial

## DC
1. Wage tax: PARTIAL, MEDIUM. Method per D.C. Code 47-1812.08 (round 1). OTR Notice 2022-08 (TCJA, no tables; use the rate schedule and the federal allowance; 10.75% on lump-sum retirement distributions) [US-DCP51-002]; schedule read in Chrome, 4% to 10.75%, effective tax years after 2021-12-31 [US-DCP52-001]; D-4 and D-4A "under review" on the 2026 forms page [US-DCP51-003]. FR-230 2018 read in full: percentage and wage-bracket methods, allowance 4,150 (2018), no flat supplemental rate and no rounding rule [US-DCP52-002, historical]. NOT LOCATED after a real read: a 2026 DC supplemental-wage rate and a rounding rule (the OTR withholding instructions page returns "Access denied" in Chrome and 403 in WebFetch; only the 2025-07 Wayback copy was read).
2-5. Unchanged from round 1 (answered).
6. ANSWERED, MEDIUM-HIGH. Pay statement D.C. Code 32-1008 [US-DCP51-012]. Tax POA D-2848 [US-DCP51-014]. UI POA Form OUCTAX-1 (initials: benefit claims and litigation; tax matters), read in full [US-DCP52-003, US-DCP52-004]. Prevailing wage: no general act seen in Title 32 ch. 13; sector law D.C. Law 25-274, 32-1081.01 to .05, effective 2025-03-07 [US-DCP52-005]; Living Wage Act 2-220.01 et seq. not read. Oracle: none published; re-derive from the rate schedule. Language notice: Spanish POA and TOP letter exist (not required content).

## ID
1. ANSWERED, HIGH. Supplemental: combine with regular wages or flat 5.3% on a separately paid amount; one-day nonresident work is withholdable [US-IDP52-001]. Rounding and method from round 1 [US-ID-001].
2. ABSENCE PROVEN, MEDIUM-HIGH. The Tax Commission's own menu of every tax it administers (Income/Payroll = individual, business, withholding; local items are only city sales taxes and auditorium district taxes) lists no city, county or district wage or payroll tax [US-IDP52-003].
3. ANSWERED (round 1) [US-IDP51-003]: wage base 58,300 USD, standard rate 1.000% for 2026.
4. ANSWERED, MEDIUM-HIGH. Employer-only components: UI 0.97000% + administrative 0.00000% + workforce development 0.03000% = 1.000% (standard class); no employee contribution, no SDI/PFML/LTC levy in the rate array or in the Tax Commission menu [US-IDP52-004, US-IDP52-003].
5. ANSWERED, HIGH on the rule, MEDIUM on completeness. Nonresident earning under 1,000 USD in Idaho in the year need not be withheld; the page lists every no-withholding case and names no reciprocal agreement [US-IDP52-002]. Resident credit for other-state tax (Idaho Code 63-3029) not read.
6. PARTIAL. Pay statement: Idaho Code 45-609 [US-IDP51-002]. Prevailing wage: Title 44 ch. 10 has a 95% resident-hire rule and no prevailing-wage rate [US-IDP52-005]. POA: Form ID-POA (bL375E) and DOL Employer Portal Authorization identified by search listing only; both PDFs unreadable (Chrome no text, Wayback 429) [US-IDP52-006, MANUAL]. Oracle: none; re-derive from the Tax Commission percentage tables.

## NM
1. ANSWERED, HIGH. FYI-104 Rev. 11/2025, effective 2026-01-01, read in full from the official PDF: federal W-4 marked NM-only, percentage tables 1.5% to 5.9%, supplemental flat 5.9% if federal uses a flat rate (Table 8 for separate bonus/overtime), no withholding if under 1 USD in a month, quarterly report TRD-41431 due the 25th from Q1 2026, annual statements by end of January [US-NMP52-001]. This replaces the MANUAL row US-NMP51-005.
2. ABSENCE PROVEN, MEDIUM-HIGH. The TRD list of all taxes it administers shows no local income, wage or payroll tax (local option taxes are gross-receipts type) [US-NMP52-003]. The Local Option Taxes child page was not opened.
3. ANSWERED (round 1): wage base 34,800 USD for 2026; new employers greater of industry average or 1% [US-NMP51-001, US-NMP51-002].
4. PARTIAL, MEDIUM. Workers' compensation administration fee per employee: employer 2.55 and employee 2.25 USD from 2025-07-01 to 2028-06-30, stepping up in 2028 and 2033 [US-NMP52-004; live-page fetch extract, re-read in a browser before use]. State paid family and medical leave: only bill-stage text found, enactment not confirmed (nmlegis returns 403) [US-NM-004].
5. ANSWERED, HIGH. Nonresidents working 15 or fewer days in NM: no withholding; residents withheld on all wages; credit for other-state tax; no reciprocity agreement mentioned in FYI-104 [US-NMP52-002].
6. PARTIAL. Tax POA ACD-31102 [US-NMP51-004]. UI: TPA by nine-digit ID plus notarized POA/Authorization of Agent (listing only; DWS returns 403, Wayback 429) [US-NMP52-006, MANUAL]. Pay statement NMSA 50-4-2 still only from a secondary page [US-NMP52-007, MANUAL]. Prevailing wage: Public Works Minimum Wage Act, 13-4-10 to 13-4-17, DWS Labor Relations; manual returned 403, threshold not usable [US-NMP52-008, MANUAL]. Oracle: none; FYI-104 includes a worked example and tables.

## WV
1. ANSWERED (round 1). Supplemental: tax.wv.gov help page points to the annual percentage table; wording is a fetch extract, re-read in a browser [US-WVP52-007].
2. PARTIAL, MEDIUM. W. Va. Code 8-13-13, text read through HB 2524: municipalities may impose service fees by ordinance, collected as the ordinance specifies; this is a service-fee authority, not an income tax [US-WVP52-005]. Individual city ordinances (for example Charleston, weekly employee fee) not read; absence of a local income tax is not proven by an official list.
3. ANSWERED, MEDIUM-HIGH. Wage base 9,500 USD (21A-1A-28(b)(1), 2024 amendments effective 2024-07-01) [US-WVP52-002]; new employers 2.7% for 36 months [US-WVP52-003]; contribution rate cut by 7% and annual 7% automation fee from 2026-07-01 [US-WVP52-001]. Agency: WorkForce West Virginia. No employee contribution appears in statute extracts or the handbook. CONFLICTS to resolve: handbook 2024 base 9,521 USD vs statute 9,500; construction rate 8.5% (handbook) vs 7.5% (statute copy) [US-WVP52-004].
4. PARTIAL. The automation and administration fee is now read from the enrolled bill (7% of taxable wages, 18 million USD annual cap, to 60 million USD or 2031-07-01) [US-WVP52-001]. No PFML/SDI program located, but no official list of programs proves absence.
5. ANSWERED (round 1) [US-WVP51-001, US-WVP51-002].
6. PARTIAL. UI POA Rev. 3.23 read in full (all UI tax matters) [US-WVP52-006]. Tax POA WV-2848 [US-WVP51-006]. Prevailing wage 21-5A-3 repealed 2016 [US-WVP51-009]. Pay statement: 21-5-3 read in full contains none [US-WVP51-008]; where WV sets one is NOT LOCATED. Oracle: none mentioned on the tax.wv.gov help page; re-derive from IT-100.2A.

## Gated or unreadable (for the owner)
- NM DWS (403 in WebFetch and Chrome): power_of_attorney.pdf, TPA guide, Public Works manual, UI tax pages. nmlegis.gov (403).
- ID: tax.idaho.gov and labor.idaho.gov refuse connections; ID-POA and Employer Portal Authorization PDFs have no text in Chrome.
- DC OTR withholding instructions page: Access denied (Chrome), 403 (WebFetch).
- WV: code.wvlegislature.gov redirects to fbi.gov; wvlegislature.gov denied in Chrome (permission).
- Wayback from Python: HTTP 429 on every request from the first call.
- No CAPTCHA seen. Own Chrome tab closed at the end.
