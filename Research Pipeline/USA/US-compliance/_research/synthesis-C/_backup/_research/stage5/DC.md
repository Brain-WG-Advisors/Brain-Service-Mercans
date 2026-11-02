# Stage 5: District of Columbia (DC), findings for all 13 domains

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-27 (DC, T3 verified, answered at the seal). This pass extends that answer to all 13 domains.

**Budget.** I declared 60 fetches and 2 h. I used about 45 fetches (curl plus 8 web searches) and stopped at the 75% fetch mark.

**Network.** No VPN was active at run time (ipinfo showed a Brazil IP). Plain curl worked on code.dccouncil.gov, otr.cfo.dc.gov, does.dc.gov, essp.does.dc.gov, dcpaidfamilyleave.dc.gov and oag.dc.gov. The one exception is the OTR withholding-instructions page, which returned 403.

**Register shard.** `00-official-sources/_register-shards/S5-DC.csv` has 25 rows, US-DCS5-001 to US-DCS5-025.

**Source files.** They are in `00-official-sources/ccg-sources/DC/`: 25 files, about 5.1 MB, none over 1 MB.
- I deleted one off-target download, the DOES claimant UI booklet, from that folder.
- Text extracts are in the scratchpad only.

**Active rows reused, not re-fetched** (each already has a local file under `pdfs/DC/`):
- US-DC-P5-1-002: Notice 2022-08.
- US-DC-P5-1-004: withholding-instructions page, wayback copy.
- US-DC-P5-1-005 and US-DC-P5-2-002: historical FR-230 booklets.
- US-DC-P5-1-014: power of attorney.
- US-DCR3-002: FR-230, 2015 edition.
- US-DC-P5-2-001: rate schedule. Its bracket base amounts were re-derived, see section 2.

**Statute rows re-read with a local file.** `supersedes` points to the older row so the synthesis can close it:
- US-DCS5-002 replaces US-DC-P5-1-013.
- US-DCS5-010 replaces US-DC-P5-1-012.
- US-DCS5-016 replaces US-DC-P5-1-008.
- US-DCS5-017 replaces US-DC-P5-1-009.
- US-DCS5-019 replaces US-DC-P5-1-011.
- US-DCS5-020 replaces US-DC-P5-1-010.
- US-DCS5-013 replaces US-DC-P5-1-003.
- US-DCS5-025 restates US-DC-P5-1-001 / US-DCR3-001. Those rows stay active; the new row only adds the local file.

---

## 1. labour_code
- **Minimum wage**
  - **17.95 USD/h** from 2025-07-01 to 2026-06-30.
  - **18.40 USD/h** from 2026-07-01. It applies to all employers regardless of size [US-DCS5-011].
  - G-DERIVE: the statute indexes the rate each July 1 by the prior-year CPI-U for the Washington MSA, rounded to the nearest 0.05 [US-DCS5-001, 32-1003(a)(6)]. The 2025 CPI rise was 2.4%: 17.95 × 1.024 = 18.3808, which rounds to **18.40**. The arithmetic matches the published figure.
  - 2027: no amount is published yet. DOES must publish it at least 30 days before 2027-07-01 (f-1).
  - DC is a single jurisdiction, so there are no local minimum wages.
- **Coverage (multistate)**
  - The DC minimum applies to an employee who regularly spends more than 50% of working time in DC.
  - It also applies to an employee who is based in DC, spends a substantial part of working time in DC, and spends no more than 50% in any one state [32-1003(b)].
  - Any employee who works at least 2 hours in DC in a workweek gets the DC minimum for each DC hour [32-1003(b-1)].
- **Tipped employees**
  - Base wage 10.00 from 2024-07-01, then **10.30 from 2026-07-01** [US-DCS5-011].
  - The statute now sets the tipped wage as a percentage of the full minimum: **56% from 2026-07-01**, 60% from 2028-07-01, 65% from 2030, 70% from 2032 and 75% from 2034. This schedule comes from D.C. Law 26-55 sec. 2222(a), effective 2025-12-06 and applied as of 2025-07-25 [US-DCS5-001, (f)(6A)-(10)].
  - Check: 0.56 × 18.40 = 10.304, which gives 10.30.
  - The employer pays any weekly-average shortfall up to the full minimum.
  - DC government employees and DC-contract employees are excluded from the tipped schedule (i).
  - Employers paying the tipped wage, other than hotels, must use a **third-party payroll business** [32-1008(a-1), US-DCS5-010].
- **Overtime**
  - 1.5 × the regular rate over 40 hours in a workweek [32-1003(c)].
  - Retail and service commission exemption: regular rate above 1.5 × the minimum wage and more than half of pay from commissions (e).
  - No daily overtime.
- **Pay frequency and timing**
  - Paydays must be designated in advance, at least twice per calendar month.
  - Bona fide administrative, executive and professional employees may be paid monthly, as may employers who already pay monthly by contract or custom.
  - At most 10 working days between the end of the pay period and payday [US-DCS5-002].
- **Method of payment**
  - Lawful US money, or checks payable on demand [32-1302, US-DCS5-002].
  - I found no DC statute that authorizes or regulates private-sector direct deposit or paycards. A tier-B lead (ezel.ai) says the same, but I did not verify it on an A source. Treat direct deposit as voluntary with employee consent; that is an inference. Confidence 70%.
- **Security officers** in office buildings must receive the SCA Guard 1 wage plus fringe [32-1003(h)].
- Confidence: 95%.

## 2. income_tax
- **Method.** The employer withholds by a percentage method or by tables similar in principle to IRC 3402 [US-DCS5-025, 47-1812.08(b)(1)].
  - No standard-deduction allowance is allowed in withholding (b)(1A).
  - Wages may be computed to the nearest dollar (b)(2)(C). The statute states no rule for rounding the tax.
  - OTR has published no FR-230 booklet after 2018. Notice 2022-08 tells employers to apply the current rate schedule with the federal allowance amount [US-DC-P5-1-002, US-DC-P5-1-004]. Applying this to 2026 is an inference.
- **Rate schedule** (tax years after 2021-12-31, still current) [US-DC-P5-2-001]:

  | Taxable income (USD) | Tax |
  |---|---|
  | up to 10,000 | 4% |
  | 10,000 – 40,000 | 400 + 6% |
  | 40,000 – 60,000 | 2,200 + 6.5% |
  | 60,000 – 250,000 | 3,500 + 8.5% |
  | 250,000 – 500,000 | 19,650 + 9.25% |
  | 500,000 – 1,000,000 | 42,775 + 9.75% |
  | over 1,000,000 | 91,525 + 10.75% |

  - G-DERIVE: I re-derived each base amount (2,200 / 3,500 / 19,650 / 42,775 / 91,525) from the band rates in Python. All of them match.
- **Employee certificates**
  - D-4 (residents) and D-4A (certificate of nonresidence).
  - Both are marked **"currently under review"** on the live OTR forms page, with no fill-in link [US-DCS5-013].
  - D.C. Act 26-416 repealed personal exemptions (47-1806.02) and set a DC-specific standard deduction for TY2025-2029 [US-DCS5-021]. Both changes remove the basis of the old D-4 allowance. **No 2026 D-4 or withholding method reflecting this has been published.** See Open questions.
- **Supplemental wages**
  - The statute and the FR-230 editions state no flat supplemental rate. Bonuses are withheld as regular wages [US-DCR3-001, US-DCR3-002]. This is unchanged from the seal.
  - Resident lump-sum retirement distributions are withheld at the highest rate, 10.75% [47-1812.08(m)].
- **Residents and nonresidents**
  - The Home Rule Act bars DC from taxing nonresidents' income [US-DC-P5-1-006]. A D-4A on file stops DC withholding [US-MULTI-016].
  - A DC resident gets a credit for tax paid to another state. The credit operates at assessment, not withholding [US-DC-P5-1-007].
  - DC therefore has no reciprocity agreements in the usual sense. The MULTI matrix lists MD and VA because those states exempt DC residents.
- **Local income tax.** None: DC is itself the local layer.
- **Federal OBBBA deductions** (tips, overtime, car-loan interest, senior) are disallowed for TY2025 and allowed as DC deductions from TY2026 [US-DCS5-021]. They operate at **assessment** only and do not change withholding.
- Confidence: 80%. The method rests on a 2022 notice, and the D-4 is under review.

## 3. social_security
- **SUI (DOES), 2026**
  - Taxable wage base **9,000 USD** [US-DCS5-017, 51-103(e)(6); US-DCS5-016].
  - New-employer rate **2.7%**.
  - Experience rates come from **Tax Table VI**, range **1.9% to 7.4%** [51-103(c)(8)(A)].
  - Plus a **0.2% administrative funding assessment** on taxable wages [(m)(1); US-DCP7-001].
  - Plus a 0.1% interest surcharge (l)(1), which applies to contributory employers. Whether it is billed in 2026 is not confirmed [US-DCP7-003].
  - **No employee contribution**: contributions may not be deducted from wages (d).
- **SUI coverage.** The standard localization, base-of-operations and residence test applies [US-DCS5-008, 51-101(2)(B)].
- **SUI wage base and other-state wages.** 51-103(e)(6) excludes amounts over 9,000 "actually paid to any person" in the year. The text I read states **no explicit credit for wages reported to another state**, and I found no regulation on it (MULTI hand-off; open).
- **PFL (Universal Paid Leave)**
  - **0.75%** of covered wages, 100% employer-funded, not deductible from pay, with no wage cap in the statute [US-DCS5-020, US-DCS5-019].
  - The rate is 0.75% for all of 2026 (and since 2024-Q3). Historical rates: 0.62% to 2022-Q2, then 0.26% to 2024-Q2.
  - Wage report and tax are due Apr 30, Jul 31, Oct 31 and Jan 31 via ESSP.
- **PFL multistate coverage.** A covered employee spends more than 50% of work time in DC, or is based in DC with substantial DC time and no more than 50% in another jurisdiction [US-DCS5-007, 32-541.01(3)]. This answers the MULTI hand-off: PFL follows this work-time test, not residence.
- **SDI/TDI.** None in DC.
- Confidence: 90%.

## 4. payslip_statute
Itemized statement at each wage payment [US-DCS5-010, 32-1008(b)]:
- Content:
  - date of payment;
  - gross wages;
  - deductions and additions, with a **separate line for gratuities**;
  - net wages;
  - hours worked in the pay period;
  - the employee's **tip-declaration form**, split into cash tips and card tips;
  - **from 2026-01-01**, a list of compensation sources beyond base wages and tips (bonuses, commissions, service-charge percentages, other).
- **Written notice at hire** and on any change (c): in English, and also in the employee's primary language where the Mayor has a template. It covers rate and basis, allowances, overtime, living-wage and prevailing-wage status, tip-sharing policy and payday.
- **Records:** at least 3 years, or the federal standard if longer (a)(1).
- **Electronic delivery:** I found no DC rule. Not researched further.
- **Multistate reach:** 32-1008 attaches to employers subject to the Minimum Wage Act subchapter. Its reach therefore follows the 32-1003(b)/(b-1) coverage test (inference).
- Confidence: 85%.

## 5. reporting_instruments
- **Withholding (OTR)** [US-DCS5-014, US-DCS5-013]
  - FR-900Q, filed electronically on MyTax.DC.gov (mandatory since TY2023). FEIN required. Registration on FR-500.
  - Deposits are weekly, semi-weekly, monthly or quarterly, as OTR assigns, by the 20th of the month after the period.
  - Returns are due Apr 30, Jul 31, Oct 31 and Jan 31. A zero return is still required.
  - Payments over 5,000 per period must be electronic. ACH credit tax type code is 00300.
  - FR-900A: annual filers under 200 USD per year, due 2027-01-31 for 2026.
  - FR-900NP: 1099/W-2G withholding.
  - Household employers report on FR-900Q.
- **Annual W-2 to DC** [US-DCS5-015]
  - SSA **EFW2/EFW2C** with a **required RS record**, uploaded via MyTax.DC.gov.
  - Electronic filing is mandatory at 25 or more forms. Fewer than 25 may file on paper with Form WT, or by online manual entry.
  - Due **January 31**.
  - The edition read is TY2025; a TY2026 edition was not yet at the analogous URL (404).
  - 47-1812.08(n) requires electronic statements from employers with 25 or more [US-DC-P5-1-001].
- **UI quarterly (DOES ESSP)** [US-DCS5-018, US-DCS5-016]
  - Wage report and payment due by the last day of the month after the quarter.
  - Household employers may file annually on April 15.
  - Employers with 250 or more employees must file machine-readable reports.
  - Penalty: 10% (minimum 100 USD). Interest: 1.5% per month.
  - Forms are UC-30 and UC-30-H [US-DC-P5-2-004].
- **PFL quarterly:** same ESSP channel and due dates [US-DCS5-019].
- **New hire** [US-DCS5-022, US-DCS5-023]
  - Report within **20 days** of hire or rehire.
  - Required fields: employee name, address and SSN; employer name, address and FEIN; date of hire.
  - Optional fields: contact person, medical insurance, date of birth, wages.
  - Channel: DC Directory of New Hires (dc-newhire.com), online, by mail or by fax.
  - Electronic reporters may send 2 monthly transmissions 12 to 16 days apart. A multistate employer may designate one state.
  - Penalty: 25 USD per employee.
- **Agents.** OTR uses D-2848; DOES uses OUCTAX-1 [US-DC-P5-1-014, US-DC-P5-2-003].
- Confidence: 90%. The channels are confirmed. Field-level UC-30 specs were not read.

## 6. leave
- **Paid sick and safe leave (ASSLA)** [US-DCS5-004]
  - Accrual by employer size:
    - 100 or more employees: 1 h per 37 h worked, up to 7 days per year.
    - 25 to 99: 1 h per 43 h, up to 5 days.
    - 24 or fewer: 1 h per 87 h, up to 3 days.
    - Tipped restaurant and bar staff: 1 h per 43 h, up to 5 days, paid at the full minimum wage.
  - Size is the average monthly FTE of the prior year.
  - FLSA-exempt employees accrue on no more than 40 h a week.
  - Accrual starts at hire; leave can be used after 90 days. Leave is reinstated on rehire within 1 year.
- **ASSLA, from the DOES fact sheet** [US-DCS5-024]
  - Covers workers spending at least 50% of their time in DC (MULTI hand-off). The threshold is set in 7 DCMR 3200-3299, which I did not read.
  - Unused leave carries over, and **no payout** is required at separation.
- **ASSLA exclusions:** students, independent contractors, casual babysitters, health-care premium-pay workers, short-term DCPS substitutes [US-DCS5-005], and construction workers under a CBA [US-DCS5-024].
- **PFL benefit side**
  - The program is state-administered: no employer benefit payments run through payroll.
  - Under D.C. Act 26-416: maximum weekly benefit **1,100 USD from 2026-10-01**, CPI-indexed from then on.
  - Maximum durations for claims filed 2026-10-01 to 2030-09-30: parental 12 weeks, family 6, medical 10, pre-natal 2 [US-DCS5-021].
- Confidence: 85%.

## 7. termination
- **Final pay** [US-DCS5-003, 32-1303]
  - **Discharge:** by the working day after discharge. The employer has 4 days if the employee handled the employer's money.
  - **Resignation:** next regular payday or 7 days, whichever comes first.
  - Liquidated damages: 10% per working day or treble wages, whichever is less.
  - A CBA can override these rules.
- **Accrued vacation payout:** no statutory rule was found (policy-driven, not researched further). Unused **sick** leave need not be paid out [US-DCS5-024].
- **UI separation notice to the employee:** no DC statutory form found. One search; the DOES UI booklet found is a claimant guide. Open.
- Confidence: 80%.

## 8. benefits_in_kind
- DC income tax starts from federal gross income, so federal exclusions flow through: 401(k), 125, HSA, transit, group-term life. The new decoupling in D.C. Act 26-416 concerns deductions and assessment items, not wage exclusions [US-DCS5-021].
- UI wages include non-cash remuneration and customary tips. They exclude employer retirement, sickness, medical and death-plan payments [US-DCS5-008, 51-101(3)].
- I did not read 47-1803.02 itself (conformity), and I found no DC departure for HSA. Confidence 70%.

## 9. deductions_garnishments
- **Creditor garnishment** [US-DCS5-006, 16-572]
  - At most 25% of the amount by which weekly disposable wages exceed **40 × the DC minimum wage**. That threshold is 40 × 18.40 = 736 USD/week from 2026-07-01. This is more protective than the CCPA's 30 × the federal minimum.
  - Only one attachment is satisfied at a time; the first delivered to the marshal has priority.
- **Child support IWO:** the IV-D agency (OAG CSSD) sends the order within 2 business days of the new-hire entry [46-226.06(f), US-DCS5-022]. DC fees and priority rules were not read.
- **Wage-deduction authorization:** no DC rule read. Open.
- Confidence: 70%.

## 10. collective_agreements (prevailing / living wage)
- **Living Wage Act**
  - Applies to DC contractors and assistance recipients at **100,000 USD or more**, and to subcontractors at 15,000 (contracts) or 50,000 (assistance) [US-DCS5-009].
  - Rate: **17.95 USD/h** from 2026-01-01 to 2026-06-30, then **18.40 from 2026-07-01**, because the living wage may not fall below the minimum [US-DCS5-012].
  - Indexed each January 1 by CPI-U, capped at 3%.
- **Sector prevailing wage:** underground electrical and gas utility work, at Davis-Bacon rates [US-DC-P5-2-005]. Federal Davis-Bacon applies to federal projects.
- CBAs can override final-pay timing [32-1303].
- Confidence: 85%.

## 11. indexation
| Item | Mechanism | Publication | register_id |
|---|---|---|---|
| Minimum wage | July 1, prior-year CPI-U Washington MSA, rounded to 0.05 | DOES OWH public notice, at least 30 days ahead | US-DCS5-001, -011 |
| Tipped wage | % of the minimum (56% from 2026-07-01, rising) | same notice | US-DCS5-001 |
| Living wage | January 1, CPI-U capped at 3%; floor = minimum wage | DOES notice by March 1 | US-DCS5-009, -012 |
| SUI wage base | Fixed at 9,000 (not indexed); rate table set by Fund balance | ESSP notice | US-DCS5-017, -016 |
| PFL rate | Statutory 0.75% (has moved: 0.62 / 0.26 / 0.75) | PFL tax page | US-DCS5-019, -020 |
| PFL max weekly benefit | 1,100 from 2026-10-01, then CPI | statute | US-DCS5-021 |
| DC standard deduction | 15,000 / 22,500 / 30,000 for 2025, COLA from 2026 rounded down to 50 | OTR (2026 amount not read) | US-DCS5-021 |
| Income-tax brackets | Not indexed | OTR rates page | US-DC-P5-2-001 |

## 12. data_protection
- New-hire reports carry the SSN [46-226.06(b)(3)].
- I found no DC rule on SSN truncation on pay statements. I did not read the DC data-breach law (D.C. Code 28-3851 et seq.). Open.
- Payroll records: at least 3 years [32-1008(a)(1)].
- Confidence: 40%.

## 13. live_legal_change (2026-01-01 to today)
- **D.C. Act 26-416**, Fiscal Year 2027 Budget Support Emergency Act of 2026, 73 DCR 11509 [US-DCS5-021]
  - Status: **emergency act, in force from 2026-08-13 for no more than 90 days** (to about 2026-11-11). General applicability is 2026-10-01; the tax subtitle applies as of 2025-01-01.
  - The permanent FY2027 BSA passed its second Council vote on 2026-07-07 (secondary lead only). Its D.C. Law number and the end of congressional review were **not confirmed**.
  - Level, tax part: **assessment**. It sets the DC standard deduction, repeals personal exemptions, and covers the OBBBA deductions and the EITC.
  - Level, PFL part: **benefit side**. Maximum benefit and durations. The 0.75% rate is unchanged.
  - Withholding: no change to 47-1812.08.
- **D.C. Law 26-55** (FY2026 BSA, effective 2025-12-06) [US-DCS5-001]
  - In force.
  - Sets the tipped minimum as a percentage of the minimum wage from 2026-07-01.
  - The pay-statement compensation-sources line (32-1008(b)(6A)) applies from 2026-01-01. US-DC-P5-1-012 records 26-55 as the last amendment of 32-1008; I did not confirm which act inserted (6A).
  - Level: wage and payslip.
- **Minimum wage 18.40 and tipped wage 10.30 from 2026-07-01** [US-DCS5-011].
- **D.C. Law 26-89** (temporary, 2026-02-12) and **D.C. Act 26-214** (emergency, 2025-12-03) amend 47-1812.08(m) only (lump-sum retirement withholding) [US-DCR3-001, US-DCS5-025]. Level: withholding on retirement payouts, not wages.
- For 2027 so far: only the PFL benefit indexation. The 2027 minimum wage is due by about June 2027.

---

## Special populations (DC rules beyond federal)
| Population | DC rule | register_id |
|---|---|---|
| Domestic / household workers | Covered by the minimum wage. Household employers report withholding on FR-900Q with an FEIN, and may file UI annually on April 15. Casual babysitters are excluded from ASSLA | US-DCS5-013, US-DCS5-018, US-DCS5-005 |
| Agricultural | No DC-specific rule read (no material agriculture in DC); federal rules apply | — |
| Minors | No DC youth subminimum in 32-1003 as read. Records must show date of birth for employees under 19 [32-1008(a)(1)(B)] | US-DCS5-001, US-DCS5-010 |
| Tipped employees | Tipped wage 10.30 (56%) from 2026-07-01; employer tops up. A third-party payroll business is mandatory (non-hotel). Tip line and tip-declaration on the payslip. ASSLA at 1/43 h, paid at the full minimum | US-DCS5-001, -010, -011, -004 |
| Clergy / religious | Lay religious officers excluded from ASSLA; no other DC rule read | US-DCS5-005 |
| Students | Excluded from ASSLA; no other DC rule read | US-DCS5-005 |
| Nonresidents (incl. nonresident aliens) | No DC withholding for nonresidents with a D-4A (Home Rule Act). Nonresident aliens resident in DC follow residence; no DC-specific NRA rule read | US-DC-P5-1-006, US-MULTI-016 |
| Statutory employees | No DC rule beyond federal found | — |
| Government employees | DC government employees are excluded from the tipped schedule but covered by ASSLA; the District reimburses UI benefits instead of paying contributions [51-103(f)]; federal employees fall under federal rules | US-DCS5-001, US-DCS5-005, US-DCS5-017 |
| Security officers (office buildings) | SCA Guard 1 wage plus fringe | US-DCS5-001 |
| Workers with disabilities | Minimum wage unless the US DOL has issued a 14(c) certificate | US-DCS5-001 |

## MULTI hand-offs (answers for DC)
- **SUI credit for wages reported to another state:** NOT stated in 51-103(e)(6) as read. Open; see below.
- **PFL coverage of multistate workers:** more than 50% of work time in DC, or DC-based with substantial DC time and no more than 50% elsewhere [US-DCS5-007]. The test is not by residence.
- **Paid sick leave for partial-DC workers:** at least 50% of time in DC, per the DOES fact sheet [US-DCS5-024]. The regulation itself was not read.
- **Pay-statement reach:** follows Minimum Wage Act coverage, 32-1003(b)/(b-1) (inference) [US-DCS5-001, -010].

## ACCESS gaps
- `https://otr.cfo.dc.gov/page/income-tax-withholding-instructions-and-tables`: HTTP 403 to plain curl on 2026-11-02. It was also blocked in earlier rounds; the wayback copy from 2025-07-10 is in US-DC-P5-1-004.
- `https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2026%20MyTax%20W2_W2C%20Instructions%20v1.0_Final.pdf`: 404. The TY2026 W-2 specification is not yet published at that path.
- The D-4 and D-4A fill-in links on `https://otr.cfo.dc.gov/page/withholding-tax-forms` are absent ("currently under review").
- `https://does.dc.gov/page/minimum-wage`: 404. I used the notice PDFs instead.

## Open questions
1. `dc.wh.method.2026`: the 2026 DC withholding method after personal exemptions were repealed (D.C. Act 26-416 sec. 7112(h)) and with the D-4 under review. **Closes with:** an OTR tax notice or 2026/2027 FR-230 or D-4 revision (OTR Individual Income Tax Division), or the live withholding-instructions page through the orchestrator's browser pass.
2. `dc.wh.supplemental.rate`: no flat supplemental rate found (unchanged from the seal). **Closes with:** an OTR statement in a future FR-230 or notice. Until then, model bonuses as regular wages [US-DCR3-002].
3. `dc.law.fy2027bsa.permanent`: the D.C. Law number and congressional-review end date of the permanent FY2027 Budget Support Act, which decides whether the 26-416 tax and PFL changes survive past about 2026-11-11. **Closes with:** the code.dccouncil.gov laws page for the permanent act, or LIMS B26 bill history.
4. `dc.sui.wagebase.otherstate_credit`: whether wages already subject to another state's UI count toward DC's 9,000. **Closes with:** 7 DCMR chapter 3 (UI tax regulations) or the DOES UI Employer Handbook (listed on the UI Tax Division forms page, US-DC-P5-2-004; not fetched).
5. `dc.stddeduction.2026`: the 2026 COLA amount of the DC basic standard deduction (assessment level). **Closes with:** OTR 2026 D-40 instructions.
6. `dc.payslip.electronic`, `dc.pay.direct_deposit`, `dc.deduction.authorization`, `dc.payslip.ssn_truncation`: no DC rule found. **Closes with:** 7 DCMR chapter 9 (wage payment regulations) and D.C. Code 28-3851 et seq. (not read).
7. `dc.termination.ui_separation_notice` and `dc.termination.vacation_payout`: no DC statutory rule found. **Closes with:** 7 DCMR chapter 3 (UI) and the DOES OWH FAQ.
8. `dc.assla.coverage_threshold`: the fact sheet says "at least 50%", while 32-1003(b) and 32-541.01 use "more than 50%". **Closes with:** 7 DCMR 3299 (ASSLA definitions).
9. `dc.ui.uc30.fields`: field-level layout of the UC-30 and ESSP bulk upload. **Closes with:** the DOES ESSP file-upload specification (behind the employer login; status gated).

**Shape of remaining work:** items 4, 6, 7 and 8 are all DCMR reads (Title 7, chapters 3, 9 and 32). One worker could close them in a single DCMR pass at dcregs.dc.gov. Items 1 and 3 depend on OTR or the Council publishing something.

**Overall confidence for DC:** 85%. Labour, SUI, PFL and reporting channels are at 90–95%. Withholding method is at 80%. Data protection and deductions are at 40–70%.
