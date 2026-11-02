# Annex CT: Connecticut

This annex sets out the Connecticut payroll rules for the 2026 build year. Read with Annex FED (the federal layer every employee carries) and Annex MULTI (which routes an employee to this State by work location, residence or UI localization). Every value is shown with its effective dates and its source (list at the end of the annex). Federal values are not repeated here.

Classification: T3. Separate State withholding, UI and a separate Paid Leave contribution; no local wage tax.

## CT.1 Employment and labour code

State minimum wage USD [[FACT:ct.minwage.hourly=16.94]] for 2026 and USD [[FACT:ct.minwage.hourly=17.48]] for 2027, indexed [[FACT:ct.minwage.indexation=every 1 January by ECI (wages and salaries, all civilian workers) for 12 months to preceding 30 June, nearest cent; announced by 15 October; never below federal MW + 0.5%]].

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Minimum wage hourly | USD [[FACT:ct.minwage.hourly=16.94]] | 2026-01-01 to 2026-12-31 |  | S1 | Derivation: 16.35 x 1.036 (ECI) = 16.9386 -> [[FACT:ct.minwage.hourly=16.94]] (Decimal ROUND_HALF_UP). |
| Minimum wage hourly | USD [[FACT:ct.minwage.hourly=17.48]] | from 2027-01-01 |  | S2 | Announced; [[FACT:ct.minwage.hourly=16.94]] x 1.032 = 17.48208 -> [[FACT:ct.minwage.hourly=17.48]]. |
| Minimum wage indexation | [[FACT:ct.minwage.indexation=every 1 January by ECI (wages and salaries, all civilian workers) for 12 months to preceding 30 June, nearest cent; announced by 15 October; never below federal MW + 0.5%]] | from 2023-06-01 |  | S3 |  |
| Overtime weekly threshold hours | [[FACT:ct.overtime.weekly_threshold_hours=40]] hours | from 2026-01-01 |  | S4 | 1.5x; no daily OT; fluctuating workweek allowed except certain delivery drivers/sales merchandisers. |
| Pay frequency rule | [[FACT:ct.pay_frequency.rule=weekly or biweekly regular payday designated in advance; period ends no more than 8 days before payday; Commissioner waiver never less than monthly]] | from 2026-01-01 |  | S5 |  |
| Payment method | [[FACT:ct.payment.method=cash or check; direct deposit only at employee written/electronic request; payroll card only if DD and check also offered and employee authorises voluntarily (31-71k)]] | from 2026-01-01 |  | S5 |  |
| Tipped employer share hotel restaurant | USD [[FACT:ct.tipped.employer_share.hotel_restaurant=6.38]] | from 2026-01-01 |  | S6 | Fixed employer cash wage; maximum tip credit 2026 [[FACT:ct.tipped.max_tip_credit.hotel_restaurant=10.56]] (minimum wage [[FACT:ct.minwage.hourly=16.94]] less the employer share). Bartenders: employer share [[FACT:ct.tipped.employer_share.bartender=8.23]]. Other industries and meal credits: in the source. No cannabis tip credit from 2026-10-01 (PA 26-12 s.6). |
| Tipped employer share bartender | USD [[FACT:ct.tipped.employer_share.bartender=8.23]] | from 2026-01-01 |  | S6 |  |
| Tipped max tip credit hotel restaurant | USD [[FACT:ct.tipped.max_tip_credit.hotel_restaurant=10.56]] | 2026-01-01 to 2026-12-31 |  | S6 | [[FACT:ct.minwage.hourly=16.94]] - [[FACT:ct.tipped.employer_share.hotel_restaurant=6.38]]. |
| Minimum wage minor hourly | USD [[FACT:ct.minwage.minor.hourly=14.40]] | 2026-01-01 to 2026-12-31 |  | S3 | Under 18 not emancipated: greater of 85% of MW (first 90 days) or 10.10: 0.85 x [[FACT:ct.minwage.hourly=16.94]] = [[FACT:ct.minwage.minor.hourly=14.40]] (2027: 14.86). |

⚠️ RESEARCH-GAP (non-blocking): Payslip consolidated text lag: not established by the research. Source that would close it: a consolidated text of 31-13a that includes PA 26-12 s.38; until then PA 26-12 governs

## CT.2 Income tax withholding

**Method.** [[FACT:ct.wh.method=TPG-211 2026 Withholding Calculation Rules (Rev. 12/25) or DRS tables (IP 2026(1)); no percentage method; 2026 rules/tables unchanged from 2025]]. Certificate: [[FACT:ct.wh.certificate.form=CT-W4 (Rev. 12/25), codes A/B/C/D/E/F; exempt certificates to DRS above 36,000 MFS / 45,000 S / 57,000 HoH / 72,000 MFJ; MSRRA with LES]]. Without a certificate: [[FACT:ct.wh.no_certificate.rate=6.99]] %. Supplemental pay: [[FACT:ct.wh.supplemental.method=aggregate only (no flat supplemental rate)]].

```
annual_wages = period_wages x pay_periods
taxable      = annual_wages - TableA_exemption(code)
annual_tax   = TableB(code)(taxable) + TableC_phaseout_addback + TableD_recapture
annual_tax   = annual_tax x (1 - TableE_credit)
period_tax   = annual_tax / pay_periods + CTW4_line2 - CTW4_line3
```

Table A exemption (maximum) by code: A USD [[FACT:ct.wh.table_a.exemption.a=12,000]], B USD [[FACT:ct.wh.table_a.exemption.b=19,000]], C USD [[FACT:ct.wh.table_a.exemption.c=24,000]], F USD [[FACT:ct.wh.table_a.exemption.f=15,000]]. Table B rates [[FACT:ct.pit.rates=2.0 / 4.5 / 5.5 / 6.0 / 6.5 / 6.9 / 6.99 percent]]; band breaks: codes A, D, F [[FACT:ct.pit.bracket_breaks.a_d_f=10,000 / 50,000 / 100,000 / 200,000 / 250,000 / 500,000]]; code B [[FACT:ct.pit.bracket_breaks.b=16,000 / 80,000 / 160,000 / 320,000 / 400,000 / 800,000]]; code C [[FACT:ct.pit.bracket_breaks.c=20,000 / 100,000 / 200,000 / 400,000 / 500,000 / 1,000,000]]. ⚠️ RESEARCH-GAP (non-blocking): Tables C (phase-out add-back), D (recapture) and E (personal tax credit) of TPG-211 carry no facts key; the rules method cannot be computed until they are keyed (research request raised).

**Method choice (decision record).** The Department of Revenue Services permits either the TPG-211 rules or its tables. Its worked examples are table-based, and the rules give results that differ from the tables by up to some cents per period. The engine method is an owner decision; whichever is chosen, the per-period tables are not in the research (blocking gap below), so the oracle examples cannot be reproduced yet.

Lump-sum pension withholding: [[FACT:ct.wh.pension_lump_sum.suspension=withholding on lump-sum retirement distributions suspended 2025-07-01 to 2026-12-31 (CT-W4P on request)]].

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Withholding method | [[FACT:ct.wh.method=TPG-211 2026 Withholding Calculation Rules (Rev. 12/25) or DRS tables (IP 2026(1)); no percentage method; 2026 rules/tables unchanged from 2025]] | 2026-01-01 to 2026-12-31 |  | S7 | Steps: annualise; less Table A exemption; Table B rates; + Table C phase-out add-back + Table D recapture; x (1 - Table E credit); / periods; + CT-W4 line 2 - line 3. |
| Withholding table a exemption a | USD [[FACT:ct.wh.table_a.exemption.a=12,000]] | 2026-01-01 to 2026-12-31 |  | S7 | A [[FACT:ct.wh.table_a.exemption.a=12,000]]; B 19,000; C 24,000; F 15,000; D 0; phases out 1,000 per 1,000 of income. |
| Withholding table a exemption b | USD [[FACT:ct.wh.table_a.exemption.b=19,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| Withholding table a exemption c | USD [[FACT:ct.wh.table_a.exemption.c=24,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| Withholding table a exemption f | USD [[FACT:ct.wh.table_a.exemption.f=15,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| PIT rates | [[FACT:ct.pit.rates=2.0 / 4.5 / 5.5 / 6.0 / 6.5 / 6.9 / 6.99 percent]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| PIT bracket breaks a d f | [[FACT:ct.pit.bracket_breaks.a_d_f=10,000 / 50,000 / 100,000 / 200,000 / 250,000 / 500,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| PIT bracket breaks b | [[FACT:ct.pit.bracket_breaks.b=16,000 / 80,000 / 160,000 / 320,000 / 400,000 / 800,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| PIT bracket breaks c | [[FACT:ct.pit.bracket_breaks.c=20,000 / 100,000 / 200,000 / 400,000 / 500,000 / 1,000,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| Withholding no certificate rate | [[FACT:ct.wh.no_certificate.rate=6.99]] % | from 2026-01-01 |  | S8 | No CT-W4: flat [[FACT:ct.wh.no_certificate.rate=6.99]] % without exemption; code E expires 15 Feb, then [[FACT:ct.wh.no_certificate.rate=6.99]] % from 16 Feb. |
| Withholding certificate form | [[FACT:ct.wh.certificate.form=CT-W4 (Rev. 12/25), codes A/B/C/D/E/F; exempt certificates to DRS above 36,000 MFS / 45,000 S / 57,000 HoH / 72,000 MFJ; MSRRA with LES]] | from 2025-12-01 |  | S8 |  |
| Withholding supplemental method | [[FACT:ct.wh.supplemental.method=aggregate only (no flat supplemental rate)]] | from 2026-01-01 |  | S9 |  |
| Withholding pension lump sum suspension | [[FACT:ct.wh.pension_lump_sum.suspension=withholding on lump-sum retirement distributions suspended 2025-07-01 to 2026-12-31 (CT-W4P on request)]] | 2025-07-01 to 2026-12-31 |  | S7 |  |

⚠️ RESEARCH-GAP (blocking): Withholding tables per period: not established by the research. Source that would close it: the DRS withholding tables in IP 2026(1) transcribed as keyed per-period tables, together with the owner's choice of engine method (rules or tables)

## CT.2b Non-resident regime and reciprocity

Rules: [[FACT:ct.nonres.rules=residents: all wages, prorated where another qualifying jurisdiction requires withholding; nonresidents: CT-service wages via CT-W4NA or records, else all wages; 15-day rule; no reciprocity; convenience-of-employer rule from 2019 (reciprocal)]].

**Resident / non-resident matrix (Connecticut income tax)**

| Income type | Resident | Non-resident |
|---|---|---|
| Regular salary | Rules or tables (CT.2) on all wages, prorated where another qualifying jurisdiction requires withholding | Rules or tables on Connecticut-service wages (CT-W4NA or records), otherwise all wages; day threshold and convenience rule in Annex MULTI |
| Annual bonus / supplemental pay | Aggregate only (no flat rate) | Same, on the Connecticut portion |
| Severance | Aggregate (federal wage definition) | Same, on the Connecticut portion |
| Equity | Aggregate; classification of equity income open at federal level (Annex FED, FED.2b) | Same, on the Connecticut portion |
| Benefits in kind | Federal wage definition; Connecticut departures open (CT.8) | Same, on the Connecticut portion |
| Contractor pay | Out of scope | Out of scope |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Non-resident rules | [[FACT:ct.nonres.rules=residents: all wages, prorated where another qualifying jurisdiction requires withholding; nonresidents: CT-service wages via CT-W4NA or records, else all wages; 15-day rule; no reciprocity; convenience-of-employer rule from 2019 (reciprocal)]] | from 2026-01-01 |  | S10 |  |

## CT.3 Social insurance: unemployment, disability, paid leave and payroll levies

Employer UI on wages up to USD [[FACT:ct.sui.wage_base=27,000]] plus the fund-solvency rate ([[FACT:ct.sui.fund_solvency.rate=1]] %); no employee UI ([[FACT:ct.sui.employee.rate=0]] %). Connecticut Paid Leave: employee [[FACT:ct.pfml.employee.rate=0.5]] % on wages up to USD [[FACT:ct.pfml.wage_cap=184,500]]; coverage [[FACT:ct.pfml.multistate=employee for whom employer pays CT UI and CT payroll taxes is working in CT (follows UI localization)]]. No SDI or TDI.

```
ct_pfml = min(period_CTPL_wages, max(0, ct_pfml_wage_cap - ytd_CTPL_wages)) x ct_pfml_employee_rate
```

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI wage base | USD [[FACT:ct.sui.wage_base=27,000]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| SUI new employer rate | [[FACT:ct.sui.new_employer.rate=1.9]] % | 2026-01-01 to 2026-12-31 |  | S11 |  |
| SUI employer rate min | [[FACT:ct.sui.employer.rate.min=0.1]] % | 2026-01-01 to 2026-12-31 |  | S11 | Charged 0.1-8.9% plus 1.0% fund solvency (combined 1.1-9.9%). |
| SUI employer rate max | [[FACT:ct.sui.employer.rate.max=8.9]] % | 2026-01-01 to 2026-12-31 |  | S11 |  |
| SUI fund solvency rate | [[FACT:ct.sui.fund_solvency.rate=1]] % | 2026-01-01 to 2026-12-31 |  | S11 |  |
| SUI employee rate | [[FACT:ct.sui.employee.rate=0]] % | from 2026-01-01 |  | S12 |  |
| SUI wage base other state credit | [[FACT:ct.sui.wage_base.other_state_credit=True]] | from 2026-01-01 |  | S13 | 31-222(b); each concurrent employer reports to the max; predecessor wages only for successor. |
| PFML employee rate | [[FACT:ct.pfml.employee.rate=0.5]] % | 2026-01-01 to 2026-12-31 |  | S14 | Statutory cap [[FACT:ct.pfml.employee.rate=0.5]] %; subject earnings = UI total wages excl. FICA-excluded benefits; each employer withholds to cap separately; no employer share. |
| PFML wage cap | USD [[FACT:ct.pfml.wage_cap=184,500]] | 2026-01-01 to 2026-12-31 |  | S14 | = SS wage base. |
| PFML benefit weekly max | USD [[FACT:ct.pfml.benefit.weekly_max=1,016.40]] | 2026-01-01 to 2026-12-31 |  | S15 | 60 x [[FACT:ct.minwage.hourly=16.94]]; 2027 60 x [[FACT:ct.minwage.hourly=17.48]] = 1,048.80. Paid by the Authority, not payroll. |
| PFML multistate | [[FACT:ct.pfml.multistate=employee for whom employer pays CT UI and CT payroll taxes is working in CT (follows UI localization)]] | from 2026-01-01 |  | S16 |  |
| PFML wages FICA basis | [[FACT:ct.pfml.wages.fica_basis=For FICA-covered employees, CTPL wages exclude any benefit excluded from FICA taxable wages (CTPL base follows FICA wages: s.125 excluded, 401(k) deferrals included); 0.5% up to the Social Security contribution and benefit base]] | from 2026-10-05 |  | S17 |  |

⚠️ RESEARCH-GAP (non-blocking): SUI wage base next year: not established by the research. Source that would close it: CT DOL "Information on Unemployment Tax Rate for Calendar Year 2027" (December).

## CT.4 Pay statement

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Payslip items | [[FACT:ct.payslip.items=hours worked, gross pay with straight time and overtime separately, itemised deductions, net pay (hours/split not for OT-exempt); electronic only with explicit consent and secure access]] | from 2026-01-01 |  | S18 |  |
| Payslip pay code guide url employer threshold | [[FACT:ct.payslip.pay_code_guide_url.employer_threshold=100]] employees | from 2026-10-01 |  | S19 | PA 26-12 s.38 (31-13a(c)): guide (>=10 codes, en/es/other common languages, dispute contact) URL on every pay record and at hire. Consolidated 31-13a text lags (F18): cite PA 26-12. |

## CT.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Report withholding remitter class | [[FACT:ct.report.wh.remitter_class=weekly if lookback > 10,000 (Wednesday after Sat-Fri week); monthly 2,000-10,000 (15th); quarterly <= 2,000 (last day of month after quarter); all via myconneCT EFT]] | from 2026-01-01 |  | S20 |  |
| Report withholding ct941 | [[FACT:ct.report.wh.ct941=quarterly due 4/30, 7/31, 10/31, 1/31 even if zero; annual status on request by 31 March]] | from 2026-01-01 |  | S20 |  |
| Report W-2 ctw3 | [[FACT:ct.report.w2.ctw3=CT-W3 + all W-2s by 31 January via myconneCT (key-and-send, EFW2 upload or DRS CSV); box 15 CT + registration number; 5 per return up to 2,000]] | from 2026-01-01 |  | S20 |  |
| Report SUI quarterly | [[FACT:ct.report.sui.quarterly=ReEmployCT electronic (manual, upload, TPA, FSET); due 4/30, 7/31, 10/31, 1/31; 276-char fixed-length S/T records; zero report required; late file 25, late pay greater of 50 or 10%]] | from 2026-01-01 |  | S21 | Optional occupation/hours/worksite ZIP from Q3 2026 (31-225a(j)(1)(B)) have no positions in the 2022 spec. |
| Report SUI record length | [[FACT:ct.report.sui.record_length=276]] characters | from 2022-01-01 |  | S21 |  |
| Newhire report days | [[FACT:ct.newhire.report_days=20]] days | from 2026-01-01 |  | S22 | Rehire = separated > 60 days; copy of CT-W4, DOL website or fax. |
| Report PFML quarterly | [[FACT:ct.report.pfml.quarterly=My Account portal or batch SFTP XML/CSV; due last day of the quarter, no penalty if paid by last day of following month]] | from 2026-01-01 |  | S23 |  |
| Report PFML file spec | [[FACT:ct.report.pfml.file_spec=CT Paid Leave File Specification Toolkit v2.1.9 (2026-10-05): batch enrollment and quarterly return files in XML (XSD published) or CSV via SFTP; CSV return file under 5 MB and under 5,000 return records; underscore-node file naming; acknowledgement file with E (error, record rejected) / W (warning, accepted) levels]] | from 2026-10-05 |  | S17 |  |

⚠️ RESEARCH-GAP (non-blocking): Report SUI optional fields layout: not established by the research. Source that would close it: CT DOL bulk-filer file-format page or updated ReEmployCT spec (Employer Tax Accounting Unit, dol.etau@ct.gov).

## CT.6 Leave

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Leave sick coverage threshold employees | [[FACT:ct.leave.sick.coverage_threshold_employees=11]] employees | 2026-01-01 to 2026-12-31 |  | S24 | CT headcount for week containing [[FACT:ct.leave.sick.coverage_threshold_employees=1]] Jan; [[FACT:ct.leave.sick.coverage_threshold_employees=1]]+ from 2027-01-01. |
| Leave sick coverage threshold employees | [[FACT:ct.leave.sick.coverage_threshold_employees=1]] employees | from 2027-01-01 |  | S24 |  |
| Leave sick accrual hours worked per hour | [[FACT:ct.leave.sick.accrual.hours_worked_per_hour=30]] hours | from 2026-01-01 |  | S24 | Cap 40 h/yr; carryover 40; use from day 120; pay greater of normal wage or MW; no payout; seasonal <= 120 days excluded. |
| Leave sick cap hours | [[FACT:ct.leave.sick.cap_hours=40]] hours | from 2026-01-01 |  | S24 |  |
| Leave sick use after days | [[FACT:ct.leave.sick.use_after_days=120]] days | from 2026-01-01 |  | S24 |  |

⚠️ RESEARCH-GAP (non-blocking): Leave sick multistate: not established by the research. Source that would close it: CT DOL Wage and Workplace Standards paid-sick-leave FAQ 2025/2026.

## CT.7 Termination and final pay

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Final pay rule | [[FACT:ct.final_pay.rule=discharge: business day after; quit/layoff: next regular payday]] | from 2026-01-01 |  | S25 | Vacation/PTO payout only if policy/CBA provides (31-76k). Double damages for unpaid wages from 2027-01-01 (PA 26-12 s.56). |
| Separation notice | [[FACT:ct.separation_notice=UC-21 Separation Packet with UC-21A to every separating employee]] | from 2026-01-01 |  | S12 |  |

## CT.8 Benefits in kind and taxable wages

Withholding follows the federal wage definition; no Connecticut departure was found for 401(k), cafeteria-plan, HSA, transit or group-term-life amounts (medium confidence; gap below). Paid Leave wages: [[FACT:ct.pfml.wages.fica_basis=For FICA-covered employees, CTPL wages exclude any benefit excluded from FICA taxable wages (CTPL base follows FICA wages: s.125 excluded, 401(k) deferrals included); 0.5% up to the Social Security contribution and benefit base]]. New 2026 subtractions operate at assessment level, not in withholding.

⚠️ RESEARCH-GAP (non-blocking): PIT departures from federal: not established by the research. Source that would close it: Conn. Gen. Stat. 12-701(a)(20) text.

## CT.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Deductions rule | [[FACT:ct.deductions.rule=only if required by law, written authorisation on a Labor Commissioner-approved form, medical/hospital without employer benefit, auto-enrolment retirement/CRSP, or another state withholding requirement]] | from 2026-01-01 |  | S26 |  |
| Garnishment creditor max percent | [[FACT:ct.garn.creditor.max_percent=25]] % | from 2026-01-01 |  | S27 | 52-361a: lesser of [[FACT:ct.garn.creditor.max_percent=25]] % of disposable earnings or excess over 40 x higher of federal/CT MW; 20-day stay; one execution at a time. |
| Garnishment creditor weekly protected | USD [[FACT:ct.garn.creditor.weekly_protected=677.60]] | 2026-01-01 to 2026-12-31 |  | S27 | 40 x [[FACT:ct.minwage.hourly=16.94]]; 2027 699.20. |
| Garnishment child support remit business days | [[FACT:ct.garn.child_support.remit_business_days=7]] business days | from 2026-01-01 |  | S28 | 52-362: exempt greater of 85% of first 145/week disposable or CCPA amount; start first period after 14 days; SDU pro-rates, current support first. |

⚠️ RESEARCH-GAP (non-blocking): Garnishment employer fee: not established by the research. Source that would close it: a full read of 52-362 and 52-361a(j)-(k)

## CT.10 Collective agreements and prevailing wage

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Prevailing wage threshold new construction | USD [[FACT:ct.prevailing_wage.threshold.new_construction=1,000,000]] | from 2026-01-01 |  | S29 | Remodeling/repair 100,000; weekly certified payroll to contracting agency (failure class D felony). |
| Prevailing wage threshold remodel | USD [[FACT:ct.prevailing_wage.threshold.remodel=100,000]] | from 2026-01-01 |  | S29 |  |

## CT.11 Indexation

One index drives both the minimum wage and the UI wage base: the Employment Cost Index (wages and salaries, all civilian workers) for the twelve months to 30 June ([[FACT:ct.minwage.indexation=every 1 January by ECI (wages and salaries, all civilian workers) for 12 months to preceding 30 June, nearest cent; announced by 15 October; never below federal MW + 0.5%]]). The minimum wage is rounded to the cent and the UI base to a round step stated in the source.

## CT.12 Payroll data protection and records

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Records retention years | [[FACT:ct.records.retention_years=3]] years | from 2026-01-01 |  | S18 | 31-66, at place of employment. |

## CT.13 Live legal change

In force in 2026: paid sick leave for employers with [[FACT:ct.leave.sick.coverage_threshold_employees=11]] or more employees; the pay-code guide duty (CT.4); the minor-league baseball exclusion and the end of the cannabis tip credit; optional UI report fields. Enacted for 2027: paid sick leave from [[FACT:ct.leave.sick.coverage_threshold_employees=1]] employee; minimum wage USD [[FACT:ct.minwage.hourly=17.48]]; double damages; UI shared-work non-charging; prevailing-wage records. The lump-sum pension withholding suspension ends with 2026 (CT.2). Public Acts known only from legislative summaries are listed as a gap below.

⚠️ RESEARCH-GAP (non-blocking): Live public act texts: not established by the research. Source that would close it: the Public Act PDFs on cga.ct.gov

## CT.14 Authority worked examples (oracle values)

Oracle values from the Department of Revenue Services informational publication IP 2026(1), examples 8 to 10 (table method). They cannot be reproduced until the per-period tables are keyed (CT.2 gap).

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Oracle ip2026 1 ex8 withholding | USD [[FACT:ct.oracle.ip2026_1.ex8.withholding=17.65]] | 2026-01-01 to 2026-12-31 |  | S8 | IP 2026(1) Ex. 8: code F, 700 weekly (table-based). TPG-211 rules give 17.79 (residual 0.14). |
| Oracle ip2026 1 ex9 withholding | USD [[FACT:ct.oracle.ip2026_1.ex9.withholding=39.97]] | 2026-01-01 to 2026-12-31 |  | S8 | Ex. 9: code A, 1,000 weekly (tables). Rules give 39.86 (residual 0.11). |
| Oracle ip2026 1 ex10 withholding | USD [[FACT:ct.oracle.ip2026_1.ex10.withholding=78.82]] | 2026-01-01 to 2026-12-31 |  | S8 | Ex. 10: code B, 2,300 biweekly (tables). Rules give 79.30 (residual 0.48). |

## CT.15 Special populations

- Domestic workers: minimum wage and overtime exclude private-home domestic service except where FLSA covers it; UI above the quarterly cash-wage threshold; withholding voluntary (CT-941 HHE, CT-W3 HHE).
- Agricultural workers: withhold where federal withholding applies; annual CT-941 option.
- Minors: minor rate USD [[FACT:ct.minwage.minor.hourly=14.40]] in 2026; newspaper carriers under 18 excluded from UI.
- Tipped employees: employer share USD [[FACT:ct.tipped.employer_share.hotel_restaurant=6.38]] (hotel and restaurant) and USD [[FACT:ct.tipped.employer_share.bartender=8.23]] (bartenders); no cannabis tip credit.
- Clergy: UI excludes churches and ministers; withholding follows the federal definition.
- Students: UI exclusions; resident assistants excluded from the minimum wage.
- Non-resident aliens and statutory employees: no Connecticut rule beyond the federal one.
- Government: State and municipal service UI-covered; Paid Leave excludes governments unless they opt in.
- Military: non-resident military pay is not Connecticut wages; military spouses exempt on CT-W4.
- Seasonal employees: excluded from sick leave.

⚠️ RESEARCH-GAP (non-blocking): the coverage thresholds that apply to these populations (quarterly cash-wage and headcount thresholds for UI coverage of domestic, agricultural and non-profit employment) are cited by statute only and carry no facts key; the engine must not hard-code them until they are keyed.

## CT.16 Language

The pay-code guide must be offered in English, Spanish and other common languages; the 31-57w(b) sick-leave notice in English and Spanish. The payslip is in English.

## CT.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | Governor's press release: minimum wage [[FACT:ct.minwage.hourly=16.94]] USD from 2026-01-01 (ECI +3.6%) | Full release | Office of the Governor of Connecticut (announcing the Labor Commissioner's … |
| S2 | Governor's press release: minimum wage [[FACT:ct.minwage.hourly=17.48]] USD from 2027-01-01 (ECI +3.2%) | Full release | Office of the Governor of Connecticut (announcing the Labor Commissioner's … |
| S3 | Conn. Gen. Stat. 31-58(i) Minimum fair wage (chapter 558) | Sec. 31-58(i)(1)-(5) | Connecticut General Assembly |
| S4 | Conn. Gen. Stat. 31-76b to 31-76c overtime | Sec. 31-76b(1); 31-76c; 31-76e | Connecticut General Assembly |
| S5 | Conn. Gen. Stat. 31-71b, 31-71i, 31-71k pay frequency, pay day and method | Sec. 31-71b(a)-(b); 31-71i; 31-71k(b) | Connecticut General Assembly |
| S6 | Conn. Gen. Stat. 31-60(b)-(d) tip credit and board allowances | Sec. 31-60(b) and (d)(3) | Connecticut General Assembly |
| S7 | TPG-211 2026 Withholding Calculation Rules (Rev. 12/25) - local copy | Steps 1-16; Tables A-E | Connecticut Department of Revenue Services |
| S8 | IP 2026(1) Circular CT: CT-W4 codes and default withholding | pp. 10-11; Form CT-W4 (Rev. 12/25) p. 29 | Connecticut Department of Revenue Services |
| S9 | IP 2026(1) Circular CT: supplemental compensation | p. 12 Supplemental Compensation; Examples 11-12 | Connecticut Department of Revenue Services |
| S10 | DRS Informational Publication 2026(1) Connecticut Employer's Tax Guide (Circular CT) | Q5 (gross CT wages); 'Residents working outside CT' (proration among qualifying jurisdictions); '15-Day Rule for Nonresident Employees' p.8; CT-W4NA allocation | Connecticut Department of Revenue Services |
| S11 | CTDOL Information on Unemployment Tax Rate for Calendar Year 2026 | Full page; PA 21-200, PA 22-67 | Connecticut Department of Labor |
| S12 | CT DOL Employer's Guide to Unemployment Compensation (updated 2026-04-23) - local copy | pp. 17, 20-21 (Taxable wage base; Filing of UI Tax and Wage Reports; due dates; penalties); Separation Packet UC-21/UC-21A | Connecticut Department of Labor |
| S13 | Conn. Gen. Stat. 31-222(b) UI taxable wages (indexed wage base; other-state wage credit) | Sec. 31-222(b)(1)(A)(v)-(vi) | Connecticut General Assembly |
| S14 | Connecticut Paid Leave employee contribution | Conn. Gen. Stat. 31-49e | CT official authority |
| S15 | Conn. Gen. Stat. 31-49e, 31-49g, 31-49o, 31-49q Paid Family and Medical Leave (CT Paid Leave) | Sec. 31-49e(4)(7)(8)(17); 31-49g; 31-49o(c); 31-49q | Connecticut General Assembly |
| S16 | CT Paid Leave Authority Guide for Employers (fact sheet updated October 2024) | Eligibility footnote | Connecticut Paid Leave Authority |
| S17 | CT Paid Leave File Specification Toolkit version 2.1.9 (10/5/26) | Latest updates; file naming convention; XML/CSV Enrollment and Return formats; acknowledgement file; versioning | Connecticut Paid Leave Authority |
| S18 | Conn. Gen. Stat. 31-13a(b) and 31-66 electronic statements and record retention | Sec. 31-13a(a)-(b) (ch. 557); 31-66 (ch. 558) | Connecticut General Assembly |
| S19 | Public Act 26-12 (Sub. HB 5003) omnibus workforce act - payroll-relevant sections | Sec. 6 (21a-421d cannabis), 38 (31-13a(c)), 40 (31-58(e)), 54 (31-53), 55-56 (31-72) | Connecticut General Assembly |
| S20 | IP 2026(1) Circular CT: remitter classes, CT-941, CT-W3, W-2 filing, EFT | pp. 4-6 and 12-14 | Connecticut Department of Revenue Services |
| S21 | CT DOL ReEmployCT Tax and Wage Report upload file format (276-character fixed length) | S record and T record layouts (4 pp.) | Connecticut Department of Labor |
| S22 | Conn. Gen. Stat. 31-254(b) state directory of new hires | Sec. 31-254(b) | Connecticut General Assembly |
| S23 | CT Paid Leave Authority: contributions and remittance pages (2026) | Contributions; Remit Contributions; Batch Process; I am an Employer | Connecticut Paid Leave Authority |
| S24 | Conn. Gen. Stat. 31-57r to 31-57s paid sick leave (as amended by P.A. 23-101 and P.A. 24-8) | Sec. 31-57r(2)(3)(11); 31-57s(a)-(f) and termination subsection | Connecticut General Assembly |
| S25 | Conn. Gen. Stat. 31-71c and 31-76k final pay and accrued fringe benefits | Sec. 31-71c(a)-(c); 31-76k | Connecticut General Assembly |
| S26 | Conn. Gen. Stat. 31-71e withholding of part of wages | Sec. 31-71e(1)-(5) | Connecticut General Assembly |
| S27 | Conn. Gen. Stat. 52-361a wage execution (creditor garnishment) | Sec. 52-361a(d)-(f) | Connecticut General Assembly |
| S28 | Conn. Gen. Stat. 52-362 income withholding for support | Sec. 52-362(e)(f) and allocation clause | Connecticut General Assembly |
| S29 | Conn. Gen. Stat. 31-53(f)-(h) prevailing wage certified payroll and thresholds | Sec. 31-53(f)(h) | Connecticut General Assembly |
