# CCG annex_CT research pack — Connecticut

Synthesis B, 2026-11-02. Source: `_research/stage5/CT.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_CT-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Minimum wage 16.94 (2026) / 17.48 (2027), ECI-indexed; weekly overtime only. Withholding by TPG-211 rules or DRS tables (codes A-F on CT-W4; 6.99% with no CT-W4); no supplemental flat rate; no reciprocity; 15-day rule; convenience rule. UI base 27,000 (ECI-indexed), new employer 1.9%, 1.0% fund solvency tax; CT Paid Leave 0.5% employee on wages to 184,500. Pay record with explicit e-consent; pay-code guide URL on every pay record for 100+ employers from 2026-10-01. Oracle: IP 2026(1) Examples 8-10 (table-based).

## 1 — Employment / labour code
- `ct.minwage.hourly` = **16.94** USD (2026-01-01 → 2026-12-31) [A.2, US-CTS5-008, derived arithmetically, conf high] — G-DERIVE: 16.35 x 1.036 (ECI) = 16.9386 -> 16.94 (Decimal ROUND_HALF_UP).
- `ct.minwage.hourly` = **17.48** USD (2027-01-01 → open) [A.2, US-CTS5-009, derived arithmetically, conf high] — Announced; 16.94 x 1.032 = 17.48208 -> 17.48.
- `ct.minwage.indexation` = **every 1 January by ECI (wages and salaries, all civilian workers) for 12 months to preceding 30 June, nearest cent; announced by 15 October; never below federal MW + 0.5%**  (2023-06-01 → open) [A.1, US-CTS5-001, direct artifact inspection, conf high]
- `ct.overtime.weekly_threshold_hours` = **40** hours (2026-01-01 → open) [A.1, US-CTS5-003, direct artifact inspection, conf high] — 1.5x; no daily OT; fluctuating workweek allowed except certain delivery drivers/sales merchandisers.
- `ct.pay_frequency.rule` = **weekly or biweekly regular payday designated in advance; period ends no more than 8 days before payday; Commissioner waiver never less than monthly**  (2026-01-01 → open) [A.1, US-CTS5-004, direct artifact inspection, conf high]
- `ct.payment.method` = **cash or check; direct deposit only at employee written/electronic request; payroll card only if DD and check also offered and employee authorises voluntarily (31-71k)**  (2026-01-01 → open) [A.1, US-CTS5-004, direct artifact inspection, conf high]
- `ct.tipped.employer_share.hotel_restaurant` = **6.38** USD (2026-01-01 → open) [A.1, US-CTS5-002, direct artifact inspection, conf high] — Fixed employer cash wage; max tip credit 2026 10.56 (16.94-6.38), 2027 11.10. Bartenders 8.23 (credit 8.71 / 9.25). Other industries credit max 0.35. Meals 0.85 full / 0.45 light. No cannabis tip credit from 2026-10-01 (PA 26-12 s.6) [US-CTS5-028].
- `ct.tipped.employer_share.bartender` = **8.23** USD (2026-01-01 → open) [A.1, US-CTS5-002, direct artifact inspection, conf high]
- `ct.tipped.max_tip_credit.hotel_restaurant` = **10.56** USD (2026-01-01 → 2026-12-31) [A.1, US-CTS5-002, derived arithmetically, conf high] — 16.94 - 6.38.
- `ct.minwage.minor.hourly` = **14.4** USD (2026-01-01 → 2026-12-31) [A.1, US-CTS5-001, derived arithmetically, conf high] — Under 18 not emancipated: greater of 85% of MW (first 90 days) or 10.10: 0.85 x 16.94 = 14.40 (2027: 14.86).

## 2 — Income tax (state withholding)
Decision record (brief trap "CT tables x rules", CT-OQ-1): DRS permits either the TPG-211 rules or the tables [US-CTS5-010]. The DRS worked examples (oracle) are table-based; an engine implementing the rules is lawful and will show residuals up to 0.48 per period against them, which are method-explained, not defects. The engine method choice is the builder/owner decision; if tables, parse IP 2026(1) pp. 31-39 and reproduce Ex. 8-10 exactly. Rounding: no rule beyond computed per-period amount. Wage definition follows federal.

- `ct.wh.method` = **TPG-211 2026 Withholding Calculation Rules (Rev. 12/25) or DRS tables (IP 2026(1)); no percentage method; 2026 rules/tables unchanged from 2025**  (2026-01-01 → 2026-12-31) [A.2, US-CTS5-010, direct artifact inspection, conf high] — Steps: annualise; less Table A exemption; Table B rates; + Table C phase-out add-back + Table D recapture; x (1 - Table E credit); / periods; + CT-W4 line 2 - line 3. Extract Table E with word-level PyMuPDF, never pdftotext -layout (drops bounds).
- `ct.wh.table_a.exemption.a` = **12000** USD (2026-01-01 → 2026-12-31) [A.2, US-CTS5-010, direct artifact inspection, conf high] — A 12,000; B 19,000; C 24,000; F 15,000; D 0; phases out 1,000 per 1,000 of income.
- `ct.wh.table_a.exemption.b` = **19000** USD (2026-01-01 → 2026-12-31) [A.2, US-CTS5-010, direct artifact inspection, conf high]
- `ct.wh.table_a.exemption.c` = **24000** USD (2026-01-01 → 2026-12-31) [A.2, US-CTS5-010, direct artifact inspection, conf high]
- `ct.wh.table_a.exemption.f` = **15000** USD (2026-01-01 → 2026-12-31) [A.2, US-CTS5-010, direct artifact inspection, conf high]
- `ct.pit.rates` = **2.0 / 4.5 / 5.5 / 6.0 / 6.5 / 6.9 / 6.99 percent**  (2026-01-01 → 2026-12-31) [A.2, US-CTS5-010, direct artifact inspection, conf high]
- `ct.pit.bracket_breaks.a_d_f` = **10,000 / 50,000 / 100,000 / 200,000 / 250,000 / 500,000**  (2026-01-01 → 2026-12-31) [A.2, US-CTS5-010, direct artifact inspection, conf high]
- `ct.pit.bracket_breaks.b` = **16,000 / 80,000 / 160,000 / 320,000 / 400,000 / 800,000**  (2026-01-01 → 2026-12-31) [A.2, US-CTS5-010, direct artifact inspection, conf high]
- `ct.pit.bracket_breaks.c` = **20,000 / 100,000 / 200,000 / 400,000 / 500,000 / 1,000,000**  (2026-01-01 → 2026-12-31) [A.2, US-CTS5-010, direct artifact inspection, conf high]
- `ct.wh.no_certificate.rate` = **6.99** percent (2026-01-01 → open) [A.2, US-CTS5-011, direct artifact inspection, conf high] — No CT-W4: flat 6.99% without exemption; code E expires 15 Feb, then 6.99% from 16 Feb.
- `ct.wh.certificate.form` = **CT-W4 (Rev. 12/25), codes A/B/C/D/E/F; exempt certificates to DRS above 36,000 MFS / 45,000 S / 57,000 HoH / 72,000 MFJ; MSRRA with LES**  (2025-12-01 → open) [A.2, US-CTS5-011, direct artifact inspection, conf high]
- `ct.wh.supplemental.method` = **aggregate only (no flat supplemental rate)**  (2026-01-01 → open) [A.2, US-CTS5-012, direct artifact inspection, conf high]
- `ct.wh.pension_lump_sum.suspension` = **withholding on lump-sum retirement distributions suspended 2025-07-01 to 2026-12-31 (CT-W4P on request)**  (2025-07-01 → 2026-12-31) [A.2, US-CTS5-010, direct artifact inspection, conf high]

## 2b — Non-resident regime and reciprocity
- `ct.nonres.rules` = **residents: all wages, prorated where another qualifying jurisdiction requires withholding; nonresidents: CT-service wages via CT-W4NA or records, else all wages; 15-day rule; no reciprocity; convenience-of-employer rule from 2019 (reciprocal)**  (2026-01-01 → open) [A.2, US-CTP10-001, quoted from authority page, conf high]

## 3 — Social insurance (SUI / SDI / PFML / levies)
Coverage [US-CTS5-017]: domestic at 1,000 cash/quarter; agricultural 20,000/quarter or 10 workers on 20 days in 20 weeks; churches/ministers, family, students and spouses, student nurses/interns, newspaper carriers under 18, co-op students excluded. No SDI/TDI; no other DRS wage levy [US-CTP9W-001/-002].

- `ct.sui.wage_base` = **27000** USD (2026-01-01 → 2026-12-31) [A.2, US-CTP9V-001, quoted from authority page, conf high] — G-DERIVE: 26,100 x 1.036 = 27,039.6 -> 27,000 (nearest 100) [US-CTS5-016]. 2027 derived 27,900 is a projection only (DOL page 404): not a fact.
- `ct.sui.new_employer.rate` = **1.9** percent (2026-01-01 → 2026-12-31) [A.2, US-CTP9V-001, quoted from authority page, conf high]
- `ct.sui.employer.rate.min` = **0.1** percent (2026-01-01 → 2026-12-31) [A.2, US-CTP9V-001, quoted from authority page, conf high] — Charged 0.1-8.9% plus 1.0% fund solvency (combined 1.1-9.9%).
- `ct.sui.employer.rate.max` = **8.9** percent (2026-01-01 → 2026-12-31) [A.2, US-CTP9V-001, quoted from authority page, conf high]
- `ct.sui.fund_solvency.rate` = **1.0** percent (2026-01-01 → 2026-12-31) [A.2, US-CTP9V-001, quoted from authority page, conf high]
- `ct.sui.employee.rate` = **0** percent (2026-01-01 → open) [A.2, US-CTS5-031, direct artifact inspection, conf medium]
- `ct.sui.wage_base.other_state_credit` = **True**  (2026-01-01 → open) [A.1, US-CTS5-016, derived arithmetically, conf high] — 31-222(b); each concurrent employer reports to the max; predecessor wages only for successor.
- `ct.pfml.employee.rate` = **0.5** percent (2026-01-01 → 2026-12-31) [A.2, US-CTP7-001, quoted from authority page, conf high] — Statutory cap 0.5%; subject earnings = UI total wages excl. FICA-excluded benefits; each employer withholds to cap separately; no employer share.
- `ct.pfml.wage_cap` = **184500** USD (2026-01-01 → 2026-12-31) [A.2, US-CTP7-001, quoted from authority page, conf high] — = SS wage base.
- `ct.pfml.benefit.weekly_max` = **1016.4** USD (2026-01-01 → 2026-12-31) [A.1, US-CTS5-020, derived arithmetically, conf high] — 60 x 16.94; 2027 60 x 17.48 = 1,048.80. Paid by the Authority, not payroll.
- `ct.pfml.multistate` = **employee for whom employer pays CT UI and CT payroll taxes is working in CT (follows UI localization)**  (2026-01-01 → open) [A.3, US-CTS5-035, direct artifact inspection, conf medium]

## 4 — Payslip statute
- `ct.payslip.items` = **hours worked, gross pay with straight time and overtime separately, itemised deductions, net pay (hours/split not for OT-exempt); electronic only with explicit consent and secure access**  (2026-01-01 → open) [A.1, US-CTS5-027, direct artifact inspection, conf high]
- `ct.payslip.pay_code_guide_url.employer_threshold` = **100** employees (2026-10-01 → open) [A.1, US-CTS5-028, direct artifact inspection, conf high] — PA 26-12 s.38 (31-13a(c)): guide (>=10 codes, en/es/other common languages, dispute contact) URL on every pay record and at hire. Consolidated 31-13a text lags (F18): cite PA 26-12.

## 5 — Statutory reporting instruments
- `ct.report.wh.remitter_class` = **weekly if lookback > 10,000 (Wednesday after Sat-Fri week); monthly 2,000-10,000 (15th); quarterly <= 2,000 (last day of month after quarter); all via myconneCT EFT**  (2026-01-01 → open) [A.2, US-CTS5-013, direct artifact inspection, conf high]
- `ct.report.wh.ct941` = **quarterly due 4/30, 7/31, 10/31, 1/31 even if zero; annual status on request by 31 March**  (2026-01-01 → open) [A.2, US-CTS5-013, direct artifact inspection, conf high]
- `ct.report.w2.ctw3` = **CT-W3 + all W-2s by 31 January via myconneCT (key-and-send, EFW2 upload or DRS CSV); box 15 CT + registration number; 5 per return up to 2,000**  (2026-01-01 → open) [A.2, US-CTS5-013, direct artifact inspection, conf high]
- `ct.report.sui.quarterly` = **ReEmployCT electronic (manual, upload, TPA, FSET); due 4/30, 7/31, 10/31, 1/31; 276-char fixed-length S/T records; zero report required; late file 25, late pay greater of 50 or 10%**  (2026-01-01 → open) [A.2, US-CTS5-032, direct artifact inspection, conf high] — Optional occupation/hours/worksite ZIP from Q3 2026 (31-225a(j)(1)(B)) [US-CTS5-018] have no positions in the 2022 spec.
- `ct.report.sui.record_length` = **276** characters (2022-01-01 → open) [A.2, US-CTS5-032, direct artifact inspection, conf high]
- `ct.newhire.report_days` = **20** days (2026-01-01 → open) [A.1, US-CTS5-019, direct artifact inspection, conf high] — Rehire = separated > 60 days; copy of CT-W4, DOL website or fax.
- `ct.report.pfml.quarterly` = **My Account portal or batch SFTP XML/CSV; due last day of the quarter, no penalty if paid by last day of following month**  (2026-01-01 → open) [A.2, US-CTS5-022, quoted from authority page, conf high]

## 6 — Leave
- `ct.leave.sick.coverage_threshold_employees` = **11** employees (2026-01-01 → 2026-12-31) [A.1, US-CTS5-021, direct artifact inspection, conf high] — CT headcount for week containing 1 Jan; 1+ from 2027-01-01.
- `ct.leave.sick.coverage_threshold_employees` = **1** employees (2027-01-01 → open) [A.1, US-CTS5-021, direct artifact inspection, conf high]
- `ct.leave.sick.accrual.hours_worked_per_hour` = **30** hours (2026-01-01 → open) [A.1, US-CTS5-021, direct artifact inspection, conf high] — Cap 40 h/yr; carryover 40; use from day 120; pay greater of normal wage or MW; no payout; seasonal <= 120 days excluded.
- `ct.leave.sick.cap_hours` = **40** hours (2026-01-01 → open) [A.1, US-CTS5-021, direct artifact inspection, conf high]
- `ct.leave.sick.use_after_days` = **120** days (2026-01-01 → open) [A.1, US-CTS5-021, direct artifact inspection, conf high]

## 7 — Termination and final pay
- `ct.final_pay.rule` = **discharge: business day after; quit/layoff: next regular payday**  (2026-01-01 → open) [A.1, US-CTS5-005, direct artifact inspection, conf high] — Vacation/PTO payout only if policy/CBA provides (31-76k). Double damages for unpaid wages from 2027-01-01 (PA 26-12 s.56) [US-CTS5-028].
- `ct.separation_notice` = **UC-21 Separation Packet with UC-21A to every separating employee**  (2026-01-01 → open) [A.2, US-CTS5-031, direct artifact inspection, conf high]

## 8 — Benefits in kind / taxable wages
Withholding follows federal wage definition; no CT departure located for 401(k), 125, HSA, transit, GTL (medium; 12-701(a)(20) not read). CTPL base excludes FICA-excluded benefits. 2026 new subtractions operate at assessment [US-CTS5-030].


## 9 — Deductions and garnishments
- `ct.deductions.rule` = **only if required by law, written authorisation on a Labor Commissioner-approved form, medical/hospital without employer benefit, auto-enrolment retirement/CRSP, or another state withholding requirement**  (2026-01-01 → open) [A.1, US-CTS5-006, direct artifact inspection, conf high]
- `ct.garn.creditor.max_percent` = **25** percent (2026-01-01 → open) [A.1, US-CTS5-024, direct artifact inspection, conf high] — 52-361a: lesser of 25% of disposable earnings or excess over 40 x higher of federal/CT MW; 20-day stay; one execution at a time.
- `ct.garn.creditor.weekly_protected` = **677.6** USD (2026-01-01 → 2026-12-31) [A.1, US-CTS5-024, derived arithmetically, conf high] — 40 x 16.94; 2027 699.20.
- `ct.garn.child_support.remit_business_days` = **7** business days (2026-01-01 → open) [A.1, US-CTS5-025, direct artifact inspection, conf high] — 52-362: exempt greater of 85% of first 145/week disposable or CCPA amount; start first period after 14 days; SDU pro-rates, current support first.

## 10 — Collective agreements / prevailing wage
2026 changes (OLR pointers, texts not read) [US-CTS5-029]: PA 26-12 s.54 amends 31-53 (2026-10-01); PA 26-68 ss.371-373 daily attendance records weekly and journeyman benefit rate (2027-01-01); PA 26-17 comptroller withholding (2026-10-01).

- `ct.prevailing_wage.threshold.new_construction` = **1000000** USD (2026-01-01 → open) [A.1, US-CTS5-023, direct artifact inspection, conf high] — Remodeling/repair 100,000; weekly certified payroll to contracting agency (failure class D felony).
- `ct.prevailing_wage.threshold.remodel` = **100000** USD (2026-01-01 → open) [A.1, US-CTS5-023, direct artifact inspection, conf high]

## 11 — Indexation
One caliber, two uses (G-CALIBER): ECI wages and salaries, all civilian workers, 12 months to 30 June, drives both the minimum wage (nearest cent) and the UI wage base (nearest 100). 2025 ECI 4.2% implied: 15.69 x 1.042 = 16.349 -> 16.35 and 25,000 x 1.042 = 26,050 -> 26,100.


## 12 — Payroll data protection / records
42-470/42-471: no public SSN display, secure transmission, privacy protection policy for SSN collectors [US-CTS5-026]. No truncation statute for pay statements; 31-13a does not require the SSN.

- `ct.records.retention_years` = **3** years (2026-01-01 → open) [A.1, US-CTS5-027, direct artifact inspection, conf high] — 31-66, at place of employment.

## 13 — Live legal change
In force: sick leave 11+ (2026-01-01); pay-code guide URL (2026-10-01); minor-league baseball MW/OT exclusion and no cannabis tip credit (2026-10-01); optional UI report fields from Q3 2026. Enacted for 2027: sick leave 1+; MW 17.48; double damages; UI shared-work non-charge; prevailing-wage records. Pension lump-sum suspension ends 2026-12-31. No ruling found. PA 26-15 s.26: AI-related layoff disclosure in WARN notices to DOL (pointer).


## Oracle — worked examples (C37)
- `ct.oracle.ip2026_1.ex8.withholding` = **17.65** USD (2026-01-01 → 2026-12-31) [A.2, US-CTS5-011, direct artifact inspection, conf medium] — IP 2026(1) Ex. 8: code F, 700 weekly (table-based). TPG-211 rules give 17.79 (residual 0.14).
- `ct.oracle.ip2026_1.ex9.withholding` = **39.97** USD (2026-01-01 → 2026-12-31) [A.2, US-CTS5-011, direct artifact inspection, conf medium] — Ex. 9: code A, 1,000 weekly (tables). Rules give 39.86 (residual 0.11).
- `ct.oracle.ip2026_1.ex10.withholding` = **78.82** USD (2026-01-01 → 2026-12-31) [A.2, US-CTS5-011, direct artifact inspection, conf medium] — Ex. 10: code B, 2,300 biweekly (tables). Rules give 79.30 (residual 0.48).

## Special populations (US-OWN-005)
- Domestic: MW/OT excludes private-home domestic service except FLSA domestic service employment; UI at 1,000 cash/quarter; withholding voluntary (CT-941 HHE, CT-W3 HHE); extended hiring notice [US-CTS5-034, US-CTS5-017, US-CTS5-014, US-CTS5-007].
- Agricultural: withhold where federal applies (Pub. 51); annual CT-941 option; UI farm thresholds [US-CTS5-014, US-CTS5-017].
- Minors: 85% MW first 90 days or 10.10, greater (2026 14.40, 2027 14.86); newspaper carriers under 18 UI-excluded [US-CTS5-001, US-CTS5-017].
- Tipped: employer share 6.38 / 8.23; 0.35 elsewhere; no cannabis tip credit from 2026-10-01 [US-CTS5-002, US-CTS5-028].
- Clergy: UI excludes churches and ministers; withholding federal definition [US-CTS5-017, US-CTS5-011].
- Students: UI exclusions; RAs excluded from MW [US-CTS5-017, US-CTS5-034].
- NRAs / statutory employees: no CT rule beyond federal [US-CTS5-011].
- Government: CT state/municipal service UI-covered; CTPL excludes governments unless opted in; sick leave no government exclusion [US-CTS5-017, US-CTS5-020, US-CTS5-021].
- Military/MSRRA: nonresident military pay not CT wages; spouses exempt on CT-W4 [US-CTS5-014].
- Seasonal (<=120 days): excluded from sick leave [US-CTS5-021].

## Language seams (US-OWN-006)
Pay-code guide in English, Spanish and other common languages (PA 26-12 s.38) [US-CTS5-028]; 31-57w(b) notice en + es poster [US-CTL-001]; payslip English (US-OWN-006).

## Synthesis D additions (2026-11-02)

Source: browser-pass rows S5B-P1 / S5B-P2 merged into `legal-basis-register.csv` and SSA EFW2 TY2026 (US-FEDS5-032) read locally. Every claim below carries its register_id; the facts file is authoritative. Full log: `_research/synthesis-D/SYNTHESIS-D.md`.

Facts added:
- `ct.report.pfml.file_spec` = **CT Paid Leave File Specification Toolkit v2.1.9 (2026-10-05): batch enrollment and quarterly return files in XML (XSD published) or CSV via SFTP; CSV return file under 5 MB and under 5,000 return records; underscore-node file naming; acknowledgement file with E (error, record rejected) / W (warning, accepted) levels** (2026-10-05 → open) [A.3, US-CTB5-001, direct artifact inspection, conf high]
- `ct.pfml.wages.fica_basis` = **For FICA-covered employees, CTPL wages exclude any benefit excluded from FICA taxable wages (CTPL base follows FICA wages: s.125 excluded, 401(k) deferrals included); 0.5% up to the Social Security contribution and benefit base** (2026-10-05 → open) [A.3, US-CTB5-001, direct artifact inspection, conf high]

Open questions closed: `ct.report.pfml.file_spec`.

## QA r1b additions (2026-11-02)

Source: the IP 2026(1) PDF already held (`00-official-sources/pdfs/CT/CT_IP-2026-1_2026-11-02.pdf`, md5 a64b2bbb855163fb832396939efc74ef); no new fetch. Facts file is authoritative; every line below is a fact object with the same key.

**2 - Income tax: per-period withholding tables (closes RQ-497).** Register row US-CTQ1B-001 [A.2]. Pages 31-38 have no text layer: every character is a filled vector path, so `pdftotext` and PyMuPDF `get_text("words")` return only the page footer. Decoding (scripts `_research/qa-r1-fix/scripts/ct_tables_parse.py` and `ct_tables_build.py`, `python -I`): each glyph is labelled by its path-command signature and, independently, by bitmap template match on a 600 dpi render; in the table body the two labels never disagree. Result: 139 wage bands per period x codes A/B/C/D/F (weekly to 1,932; bi-weekly to 3,865; semi-monthly to 4,187; monthly to 8,375; above that DRS says "Refer to TPG-211, Withholding Calculation Rules"). Full table: `_research/qa-r1-fix/ct-tables/CT-2026-withholding-tables.csv`; checks: `ct-tables/verify.json`.

**Checks (G-SPOT, direct artifact inspection).** Bands contiguous from 0 to the per-period maximum in all four periods; every code column non-decreasing; three row groups (weekly 673-701, bi-weekly 3,500-3,538, monthly 5,083-5,250) compared by eye with the rendered page. **Oracle:** Example 8 weekly 700 code F: band 692-701 = 17.65, x 60% = 10.59. Example 9 weekly 1,000 code A: band 990-1,000 = 39.97, x 40% = 15.99. Example 10 bi-weekly 2,300 code B: band 2,269-2,307 = 78.82. All three reproduce exactly; the existing oracle facts go from conf medium to high.

**Fact layout.** One fact per band: `ct.wh.table.<period>.row.<nnn>` with value `greater_than|less_than_or_equal_to|A|B|C|D|F` (layout in `ct.wh.tables.columns`); `ct.wh.table.<period>.max_wages` per period. 556 band facts are not listed here; new non-row facts:

- `ct.oracle.ip2026_1.ex8.withholding` = **17.65** USD (2026-01-01 -> 2026-12-31) [A.2, US-CTS5-011, direct artifact inspection, conf high] IP 2026(1) Ex. 8: code F, 700 weekly (table-based). TPG-211 rules give 17.79 (residual 0.14). QA r1b: reproduced from the parsed weekly table, band 692-701, code F = 17.65 (US-CTQ1B-001).
- `ct.oracle.ip2026_1.ex9.withholding` = **39.97** USD (2026-01-01 -> 2026-12-31) [A.2, US-CTS5-011, direct artifact inspection, conf high] Ex. 9: code A, 1,000 weekly (tables). Rules give 39.86 (residual 0.11). QA r1b: reproduced from the parsed weekly table, band 990-1000, code A = 39.97 (US-CTQ1B-001).
- `ct.oracle.ip2026_1.ex10.withholding` = **78.82** USD (2026-01-01 -> 2026-12-31) [A.2, US-CTS5-011, direct artifact inspection, conf high] Ex. 10: code B, 2,300 biweekly (tables). Rules give 79.30 (residual 0.48). QA r1b: reproduced from the parsed biweekly table, band 2269-2307, code B = 78.82 (US-CTQ1B-001).
- `ct.wh.tables.columns` = **wages_greater_than|wages_less_than_or_equal_to|A|B|C|D|F (USD; withholding code from Form CT-W4; amounts per pay period)** (2026-01-01 -> 2026-12-31) [A.2, US-CTQ1B-001, direct artifact inspection, conf high] Layout of every ct.wh.table.<period>.row.<nnn> value. Lookup: the band with greater_than < taxable wages <= less_than_or_equal_to; take the code column.
- `ct.oracle.ip2026_1.ex8.withheld_allocated` = **10.59** USD (2026-01-01 -> 2026-12-31) [A.2, US-CTQ1B-001, direct artifact inspection, conf high] Example 8: table amount 17.65 (weekly band 692-701, code F) x 60% CT-W4NA share = 10.59.
- `ct.oracle.ip2026_1.ex9.week1_allocated` = **15.99** USD (2026-01-01 -> 2026-12-31) [A.2, US-CTQ1B-001, direct artifact inspection, conf high] Example 9: table amount 39.97 (weekly band 990-1000, code A) x 40% of days in CT = 15.99.
- `ct.wh.table.weekly.max_wages` = **1932** USD (2026-01-01 -> 2026-12-31) [A.2, US-CTQ1B-001, direct artifact inspection, conf high] Wages over this amount: "Refer to TPG-211, Withholding Calculation Rules" (no table row).
- `ct.wh.table.biweekly.max_wages` = **3865** USD (2026-01-01 -> 2026-12-31) [A.2, US-CTQ1B-001, direct artifact inspection, conf high] Wages over this amount: "Refer to TPG-211, Withholding Calculation Rules" (no table row).
- `ct.wh.table.semimonthly.max_wages` = **4187** USD (2026-01-01 -> 2026-12-31) [A.2, US-CTQ1B-001, direct artifact inspection, conf high] Wages over this amount: "Refer to TPG-211, Withholding Calculation Rules" (no table row).
- `ct.wh.table.monthly.max_wages` = **8375** USD (2026-01-01 -> 2026-12-31) [A.2, US-CTQ1B-001, direct artifact inspection, conf high] Wages over this amount: "Refer to TPG-211, Withholding Calculation Rules" (no table row).

The engine choice between the tables and the TPG-211 rules (CT-OQ-1) is a design decision and is carried as the non-blocking `ct.wh.engine_method`.


## QA r3b additions (agent 2, 2026-11-02)
- TPG-211 (Rev. 12/25) Tables C, D, E transcribed from IP 2026(1) PDF pp.28-30 [US-CTP10-001]: `ct.wh.table_c.{code_a_d,code_b,code_c,code_f}`, `ct.wh.table_d.{code_a_d_f,code_b,code_c}`, `ct.wh.table_e.{code_a,code_b,code_c,code_f}` (code D personal tax credit 0.00). Closes RQ-509.

## Open questions

Mirrors `unresolved[]` in the facts file (same keys, same wording). Regenerated by QA r1b on 2026-11-02.

- `ct.report.sui.optional_fields_layout` (non-blocking) — The 2022 ReEmployCT 276-char layout has no positions for the optional occupation/hours/ZIP data from Q3 2026; ICESA/MMREF bulk options are leads only. **Would close it:** CT DOL bulk-filer file-format page or updated ReEmployCT spec (Employer Tax Accounting Unit, dol.etau@ct.gov).
- `ct.sui.wage_base.next_year` (non-blocking) — 2027 UI base not published (DOL page 404); 27,900 is a projection only. **Would close it:** CT DOL "Information on Unemployment Tax Rate for Calendar Year 2027" (December).
- `ct.pit.departures_from_federal` (non-blocking) — Only DRS guide-level conformity checked; chapter 229 modification list not read. **Would close it:** Conn. Gen. Stat. 12-701(a)(20) text.
- `ct.leave.sick.multistate` (non-blocking) — 31-57r/s has no apportionment or threshold rule for employees partly in CT. **Would close it:** CT DOL Wage and Workplace Standards paid-sick-leave FAQ 2025/2026.
- `ct.garn.employer_fee` (non-blocking) — No employer administrative fee seen in the 52-361a/52-362 text read. **Would close it:** Full read of 52-362 (held file) and 52-361a(j)-(k).
- `ct.live.public_act_texts` (non-blocking) — PA 26-68 (ss.195, 371-373), PA 26-17, PA 26-15 s.26 known only via OLR summaries (A.3). **Would close it:** Act PDFs on cga.ct.gov via the Wayback route.
- `ct.payslip.consolidated_text_lag` (non-blocking) — Consolidated 31-13a (2026-10-20 capture) predates PA 26-12 s.38. **Would close it:** Re-verify consolidated 31-13a at next synthesis; cite PA 26-12 until then.
- `ct.wh.engine_method` (non-blocking) — DRS allows the tables (IP 2026(1) pp. 31-38, now keyed as ct.wh.table.*) or the TPG-211 calculation rules; results differ by up to 0.48 per period and the DRS oracle examples reproduce only from the tables. Which one the engine uses is a design decision, not a research gap. **Would close it:** Owner/design decision (CT-OQ-1): tables (ct.wh.table.*) up to the per-period maximum and TPG-211 above it, or TPG-211 throughout.
