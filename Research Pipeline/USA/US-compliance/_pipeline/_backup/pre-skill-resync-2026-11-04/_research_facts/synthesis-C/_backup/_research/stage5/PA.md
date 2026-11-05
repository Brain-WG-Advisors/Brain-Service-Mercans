# Stage 5 — PA (Pennsylvania): 13-domain hunt

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Budget declared: 60 fetches / 2 h; used about 45 fetch-equivalents (curl + search) and under 1 h; stopped acquiring at the 75% fetch line.
Shard: `00-official-sources/_register-shards/S5-PA.csv` (22 rows, US-PAS5-001..022). Sources: `00-official-sources/ccg-sources/PA/` (25 files, 6,554,568 bytes, below the 33,554,432 limit).
Reused active rows (not fetched again): US-PA-001 (DSM-12 withholding guide, local file), US-PA-003/US-PA-P5-2-003 (employee UC 0.07%, rounding), US-PA-007 (UC-748 2026 rates), US-PA-009 (2026 UC highlights), US-PA-P5-1-001 (34 Pa. Code 231.36), US-PA-P5-1-002 (WPCL), US-PA-P5-1-003/006 (prevailing wage), US-PA-P5-1-004/US-PA-008/US-FIL-010 (third-party authorisation, REV-415), US-FIL-008 (UC-2010 file layouts), US-MULTI-007 (reciprocity), US-PAP7-001..006 (levies), US-PAL-001/002, US-PAP9L-001.

Tier: T4 (state flat PIT + Act 32 EIT/LST remitted to local collectors + Philadelphia wage tax on a city return) — unchanged from MANDATE US-MQ-58.

---

## 1 — Labour code
- **Minimum wage 7.25/h** (statewide). Statutory mechanism: MWA Sec. 4(a)(8) fixed 7.15 from 2007-07-01; Sec. 4(a.1) raises the state minimum automatically to any higher FLSA rate from the same date, so 7.25 applies since 2009-07-24 [US-PAS5-001, A.1]. Regulation 34 Pa. Code 231.101a(a) states 7.25 [US-PAS5-002, A.1]. DLI page and FAQ state 7.25 [US-PAS5-004 A.2, US-PAS5-003 A.3]. The minimum wage is not indexed. **2027:** nothing enacted. The MWA consolidated text and the Pa. Code (current through 56 Pa.B. 5370, 2026-08-08) carry no new rate. Confidence high.
- **Local minimum wage:** none possible. MWA Sec. 14.1 preempts local ordinances, except ordinances in force on 2006-01-01 [US-PAS5-001].
- **Tipped:** cash wage 2.83/h, with the employer making up any shortfall to 7.25 (231.101a(b)). A tipped employee is one who customarily and regularly receives more than 135/month in tips (231.1). The tip credit must be notified in writing whenever it changes (231.34) [US-PAS5-002]. No deduction of card-processing fees from tips [US-PAS5-004].
- **Overtime:** 1.5x the regular rate over 40 h/workweek. The FLSA 7(j) 8-and-80 system is allowed for hospitals (Act 109 of 2012) [US-PAS5-001, US-PAS5-003]. No daily overtime. **Departure from FLSA:** for salaried non-exempt employees, regular rate = remuneration / 40 hours (231.43(g), 2022 rule). The federal fluctuating-workweek half-time method is therefore not available [US-PAS5-002]. Comp time in lieu of OT is not legal [US-PAS5-003]. The EAP exemption uses the federal duties tests with a salary level of **684 USD/week**: DLI follows the 2019 federal level, and the PA-specific salary sections 231.82-84 are abrogated [US-PAS5-003, US-PAS5-002].
- **Sub-minimum:** learners/students by special certificate, not below 85% (LLC-3/LLC-4). Training wage for under-20s for the first 60 days at the FLSA 6(a) rate. Disability licence LLC-18 [US-PAS5-001, US-PAS5-004].
- **Pay frequency / pay-day timing:** WPCL Sec. 3(a). Regular paydays are designated in advance. Wages are due within the time in the written contract, or within the customary time lapse for the trade, or within 15 days after the end of the pay period. Overtime may be paid in the next period. Fringe benefits and union dues are remitted within 10 days of their due date [US-PAS5-005, A.1]. Sec. 4 requires notice at hire of payday, place and rate, and notice of any change before it takes effect [US-PAS5-005].
- **Method of payment:** WPCL Sec. 3 allows "lawful money of the United States or check" [US-PAS5-005]. No PA statute or regulation read here addresses direct deposit or paycards (open question Q1).
- **Breaks:** only minors 14-17 get a mandatory 30 minutes after 5 consecutive hours. Breaks under 20 minutes that the employer allows are paid [US-PAS5-003].
- **Records:** 3 years (MWA Sec. 8; 231.31 lists 13 items) [US-PAS5-001, US-PAS5-002].

## 2 — Income tax
- **State PIT:** flat **3.07%** on compensation. It applies to residents (services in or outside PA) and to nonresidents (services in PA) [US-PAS5-009 = re-read of US-PA-002 with local file; US-PA-001]. Method: compensation for the payroll period x rate. There is no PA W-4, no allowances and no brackets. Supplemental pay is added to the current period and multiplied by 3.07% [US-PA-008, US-PA-P5-2-001]. **Rounding rule for PIT: none published** [US-PA-P5-2-001/002]. 2027: no change located.
- **Reciprocity:** IN, MD, NJ, OH, VA, WV. The employee files REV-419 to stop PA withholding [US-PA-001, US-MULTI-007]. Resident credit for tax paid to another state; since 2014 a foreign country does not count as a state [US-PAS5-012].
- **Not subject to PA withholding** (DSM-12 p. 4, US-PA-001): agricultural/H-2A workers not subject to FICA (they may elect withholding), clergy not subject to federal withholding, domestic servants who are not employees for federal purposes, casual non-trade employees, foreign-government employees, nonresident aliens resident in PA working outside the US, statutory employees/newspaper carriers under 18, interstate transport workers exempt federally.
- **Local income taxes (T4):**
  - Act 32 EIT, under LTEA Sec. 512 [US-PAS5-017, A.1]. Withhold the **greater** of the resident EIT and the work-location nonresident EIT from the DCED official register. Temporary assignments: under 90 consecutive days, use the employer's home office; 90 days or more, use the job location. A certificate of residency is collected at hire and at address change. Quarterly return and payment by the last day of the month after the quarter, to each work location's tax officer. Optional combined monthly e-filing for multi-district employers. Annual return and statement with the PSD code (xxxxxx-xx) by **28 February**.
  - DCED [US-PAS5-018, A.2]: worksites include **residences of home-based employees**. Rates come per address from the DCED Address Search Application (no static table); the Residency Certification Form is kept on file; register with the collector; W2-R by the last day of February.
  - **LST** (LTEA 301.1, 312) [US-PAS5-017]: cap **52 USD per person per year**. A levy above 10 USD is collected pro rata per payroll period (annual rate / number of pay periods, **rounded down to the cent**). A levy above 10 USD must exempt anyone earning under 12,000 USD in the subdivision. Mandatory exemptions apply to 100%-disabled veterans and reservists called to active duty. Situs is the place of employment on the first day of each payroll period. Concurrent employment follows a priority order. LST is remitted 30 days after the quarter.
  - **Philadelphia Wage Tax** (Sterling Act; Act 32 does not apply) [US-PAS5-022, A.2]: resident **3.735%** / non-resident **3.425%** from 2026-07-01, and 3.74%/3.43% from 2025-07-01 to 2026-06-30. Residents pay wherever they work; non-residents pay on work in the city. Register within 30 days. Quarterly returns on the Philadelphia Tax Center; no annual reconciliation; payment frequency set by amount withheld. Matches US-PAP7-006.
  - Pittsburgh payroll expense tax 0.55% (employer) [US-PAP7-005].

## 3 — Social security (SUI / SDI / PFML / levies)
- **SUI:** the employer taxable wage base is **10,000** per employee per year, fixed by statute for 2018 and later (UC Law 4(x)(1)) and not indexed [US-PAS5-019, A.1; US-PA-009 and UC-2INS US-PAS5-013 corroborate]. 2026 new-employer rate is 3.8220% for non-construction and 10.5924% for construction. The 2026 computed range is 1.4190%-10.3734%. Surcharge 9.2%; additional contributions 0.60% [US-PA-009, US-PA-007]. **Employee contribution 0.07% of all gross wages, no cap**, withheld in trust (UC Law 301.4) and rounded to the cent [US-PAS5-019, US-PA-P5-2-003].
- **SDI/TDI/PFML:** none in PA [US-PAL-002; the B-tier US-PA-P5-1-005 is superseded].
- **Levies:** see the P7 rows US-PAP7-001..006 (not redone).

## 4 — Payslip statute
- Statement with every payment: hours worked, rates, gross wages, allowances claimed toward minimum wage, deductions, net wages (34 Pa. Code 231.36) [US-PA-P5-1-001]. The DLI FAQ adds tax and other deductions and the pay-period dates [US-PAS5-003]. Language: English (US-PAL-001). Retention 3 years [US-PAS5-002]. **Electronic delivery/consent:** no PA rule located (Q1).

## 5 — Reporting instruments
- **Withholding (DOR, myPATH):** deposits quarterly, monthly, semi-monthly or semi-weekly depending on the quarterly amount; quarterly W-3 return [US-PAS5-009]. **REV-1667 annual reconciliation plus W-2s by 31 January**, electronic (myPATH) where there are 10 or more statements. Upload formats: PA W-2 **EFW2** or CSV, EFW2C corrections, PA-501 deposits, 1099-R/MISC/NEC [US-PAS5-010]. 1099 withholding goes on a separate Other Income Withholding account [US-PAS5-009].
- **UC quarterly (DLI, UCMS):** UC-2 plus UC-2A due 30 Apr / 31 Jul / 31 Oct / 31 Jan. Zero report required. Online filing is mandatory. E-payment is mandatory from 5,000 per period. A credit week is a week with remuneration of at least 116. Late penalty 15%, minimum 125, maximum 450 [US-PAS5-013]. File layouts: UC-2010 ICESA/CSV [US-FIL-008].
- **New hire:** within **20 days** of hire, or two monthly electronic transmissions 12-16 days apart. Fields: name, address, SSN, hire date, employer name/address/FEIN, employer contact [US-PAS5-008, A.1]. The portal URL (panewhires.com) did not resolve (ACCESS gap).
- **Local:** EIT/LST quarterly returns and W2-R (Feb 28) to the collector [US-PAS5-017/018]. Philadelphia quarterly returns [US-PAS5-022].
- Third-party authorisation: REV-677 for DOR; UCMS TPA handshake for UC [US-PA-P5-1-004, US-FIL-010].

## 6 — Leave
- **State:** no statute requires paid sick leave, vacation, holiday pay or severance; employer policy or contract governs [US-PAS5-003]. Under WPCL these benefits become wages once promised [US-PAS5-005].
- **Philadelphia** (Code ch. 9-4100) [US-PAS5-015, A.2, status partial]: paid sick time where the employer has 10 or more employees for 40 weeks a year; covered employees work at least 40 h/yr in the city; maximum 40 h accrual and use per year; carry-over unless 40 h are front-loaded; a PTO policy complies if it gives 40 h usable for 9-4100 purposes; rehire within 6 months restores the balance. **Accrual rate (1 h per 40 h) is a tier-B lead only**: ordinance text not reached (Q2).
- **Pittsburgh** PSDA [US-PAS5-016, A.3, partial]: the 2025 amendment raises accrual and cap **from 2026-01-01**; the city bulletin mentions 72 h. Exact values (1 h per 30 h; cap 72 h for 15+ employees, 48 h below that) are **tier-B leads** because pittsburghpa.gov returned 403 (Q3).
- PFML benefit interaction: none (no PA programme).

## 7 — Termination
- **Final pay:** due by the next regular payday for any separation (quit, layoff, discharge), by certified mail if requested (WPCL Sec. 5(a)) [US-PAS5-005, US-PAS5-003]. Liquidated damages are 25% or 500 [US-PAS5-005].
- **Accrued vacation payout:** only if the employer's policy or contract promises it [US-PAS5-003, US-PAS5-005].
- **Separation notice:** the employer must notify separating employees of UC availability at separation (UC Law Sec. 206.1, Act 9 of 2020). Form UC-1609 (REV 08-24) is recommended; other formats are allowed; a Spanish version exists [US-PAS5-014].
- State WARN: none located (not searched beyond the federal layer; no payroll impact found).

## 8 — Benefits in kind (departures from federal)
- Employee deferrals to **401(k)/403(b)/457(b)** are **taxable for PA PIT** when made. Employer contributions are not [US-PAS5-011].
- **Section 125:** salary reductions for health, accident, disability and life coverage are excluded as federally. Salary reductions for **dependent care** and 401 plans are **not** excluded. Employer cash dependent-care reimbursement is taxable [US-PAS5-011].
- **Group-term life:** employer premiums are never taxable (no 50,000 imputed income) [US-PAS5-011].
- Personal use of employer property (company car), employer parking, meals and lodging are nontaxable fringes [US-PAS5-011].
- **HSA/MSA:** PA follows the federal rules and limits and allows them as a deduction (Schedule O) [US-PAS5-012]. Whether payroll may exclude HSA salary reductions at withholding is open (Q4).
- Local EIT base: follows PA PIT compensation under the LTEA definition. Not verified separately (Q5).

## 9 — Deductions and garnishments
- Deductions are limited to the 34 Pa. Code 9.1 list. Each needs a written authorisation; a blanket authorisation at hire is not valid; deductions may not take pay below minimum wage [US-PAS5-006, US-PAS5-003].
- **Wage attachment is narrower than CCPA:** wages are exempt except for support, divorce, board of 4 weeks or less, residential-lease judgments (max 10% of net wages or the poverty-guideline floor, whichever is less; remit to the prothonotary within 15 days; fee of 5 or less), PHEAA loans, and criminal restitution. Support has first priority and restitution second. Ordinary consumer-creditor garnishment is not available (42 Pa.C.S. 8127) [US-PAS5-007, A.1]. Child-support IWO specifics (fees, state disbursement unit) not fetched (Q8).
- State tax levies: no PA-specific rule read (Q6).

## 10 — Collective agreements / prevailing wage
- PA Prevailing Wage Act applies to public works over 25,000 USD (DLI Bureau of Labor Law Compliance) [US-PA-P5-1-003 A.1, US-PA-P5-1-006]. Certified payroll mechanics were not fetched in Stage 5 (Q7).

## 11 — Indexation
- Nothing in PA payroll is indexed automatically. The minimum wage follows the FLSA by statute (Sec. 4(a.1)). The UC employer base is fixed at 10,000. The employee UC rate is set yearly under UC Law 301.7 (0.07% from 2023). Employer UC rates are published yearly on UC-748 and in the Yearly Tax Highlights [US-PA-007, US-PA-009]. The LST cap of 52 is statutory. PIT 3.07% is statutory. Philadelphia sets wage-tax rates every 1 July [US-PAS5-022]. EIT rates are published in the DCED register (twice a year, 1 January and 1 July, per DCED practice; not verified, Q5).
- G-DERIVE: no indexed amount to derive. The 7.25 rate is the FLSA rate carried by Sec. 4(a.1). No arithmetic step exists.

## 12 — Data protection
- SSN Privacy Law (Act 60 of 2006) [US-PAS5-020]: no public display; no SSN on access cards; secure transmission; no SSN on mailed materials unless law requires it. It contains **no pay-stub truncation rule**; mailed pay stubs should therefore omit the SSN.
- Breach Notification Act [US-PAS5-021]: notify without unreasonable delay. Above 500 PA residents, notify the Attorney General and the credit reporting agencies. Where SSN, bank or ID number is breached, offer 12 months of credit monitoring and a credit report (Act 33 of 2024).

## 13 — Live legal change (2026-01-01 to 2026-11-02)
- UC Law amended by **Act 55 of 2025** (P.L.333, 2025-12-22): domestic-violence eligibility (Sec. 402.7) with automatic benefit-charge relief to employers. Benefit side only; no payroll calculation change [US-PAS5-019]. Status: in force; operating level: employer UC account charging.
- Philadelphia Wage Tax drops to 3.735%/3.425% on **2026-07-01** [US-PAS5-022]. Further cuts are announced over five years but not published.
- Pittsburgh PSDA amendment effective **2026-01-01** [US-PAS5-016].
- Minimum wage bill: the House passed an increase bill in 2026 (tier-B news leads); the Senate has not acted. **Not enacted**; the Pa. Code and the MWA text still carry 7.25. Bill number and latest-step date are not pinned (Q9).
- PA Bulletin sweep for 2026: not run (bulletin-sweep.json belongs to the synthesis); Pa. Code is current through 56 Pa.B. 5370 (2026-08-08) for the chapters read.

## Special populations (state level)
| Population | PA rule | register_id |
|---|---|---|
| Domestic/household | Exempt from MWA min wage and OT (Sec. 5(a)(2)). UC covered only where cash pay is 1,000 or more in a quarter. PA withholding not required when not an employee federally. Household pay is PA-taxable to the worker | US-PAS5-001; US-PAS5-019; US-PA-001; US-PAS5-011 |
| Agricultural | Farm labour exempt from MWA (Sec. 5(a)(1)). UC excludes agricultural labour except farms covered under 4(l)(3)(G). PA withholding not required where FICA does not apply (H-2A may elect) | US-PAS5-001; US-PAS5-019; US-PA-001 |
| Minors | 30-min break for ages 14-17 after 5 h. Training wage under 20 for 60 days. UC excludes a child under 18 working for a parent. Child Labor Act 2012 hours/permit rules not read (Q10) | US-PAS5-003; US-PAS5-001; US-PAS5-019 |
| Tipped | 2.83 cash wage; more than 135/month threshold; tip records; no card-fee deduction. Tips paid through the employer are subject to PA withholding; tips received directly are not withheld but are reported | US-PAS5-002; US-PAS5-004; US-PA-001 |
| Clergy/religious | No PA withholding where federal withholding does not apply. Cash housing allowance taxable; parsonage value exempt. Church service excluded from UC (Arts. X-XII) | US-PA-001; US-PAS5-011; US-PAS5-019 |
| Students | Special certificates (85%, 20 h/week). Seasonal students may be excluded from OT. UC excludes students employed by their school and some camp students | US-PAS5-001; US-PAS5-002; US-PAS5-019 |
| Nonresident aliens | Same 3.07% flat rate; exempt only when a PA resident NRA works outside the US | US-PA-001 |
| Statutory employees | No PA withholding; amounts reported on the W-2 | US-PA-001 |
| Government employees | Government bodies are employers for PA withholding. MWA excludes elected officials and their policy staff (Sec. 5(a)(12)). Federal service is excluded from PA UC | US-PA-001; US-PAS5-001; US-PAS5-019 |

## ACCESS gaps
- https://www.pittsburghpa.gov/mayor/paidsickleave — 403 (direct and `web.archive.org/web/2026id_/`).
- https://www.pittsburghpa.gov/City-Government/Mayor/Equity-Commissions/Office-of-Equity/Paid-Sick-Days-Act — 403.
- https://codelibrary.amlegal.com/codes/philadelphia/latest/philadelphia_pa/0-0-0-201085 (Phila. Code 9-4100) — 403.
- https://www.phila.gov/services/working-in-philadelphia/workers-rights/paid-sick-leave/ — 404.
- https://www.panewhires.com/ — connection failed (curl exit 6, DNS).
- https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/uc-tax/quarterly-reports — 404 (covered by UC-2INS instead).
- https://www.uc.pa.gov/documents/uc_law.pdf — redirects to pa.gov search (covered by the legis.state.pa.us PDF instead).

## Open questions
- **Q1** Direct deposit, paycards and electronic pay statements: no PA rule located in WPCL, 34 Pa. Code 9.1 or the DLI FAQ. Would close it: a DLI Bureau of Labor Law Compliance interpretation, or a statute search on palegis.us for "payroll card".
- **Q2** Philadelphia accrual rate (1 h per 40 h, tier B). Would close it: Phila. Code 9-4104 text (amlegal; Chrome pass) or the phila.gov Office of Worker Protections page.
- **Q3** Pittsburgh 2026 accrual (1 per 30) and caps (72/48), tier B. Would close it: the enacted ordinance (Pittsburgh Legistar) or pittsburghpa.gov/mayor/paidsickleave (Chrome pass).
- **Q4** HSA salary reductions at PA withholding (exclude, or include and let the employee deduct on Schedule O). Would close it: REV-634 or PA PIT Bulletin 2006-05.
- **Q5** Local EIT compensation base (LTEA "compensation" definition vs PA PIT) and the DCED register publication cadence. Would close it: LTEA Sec. 501 definitions (in the local PDF, not extracted) and the DCED Tax Register page.
- **Q6** PA DOR administrative wage levy on employees' wages: not researched. Would close it: 72 P.S. 7345 / DOR collections guidance.
- **Q7** Certified payroll under the PA Prevailing Wage Act (form and frequency). Would close it: 34 Pa. Code ch. 9 prevailing-wage regulations (r-5) / DLI LLC forms.
- **Q8** Child-support IWO state specifics (employer fee, PA SCDU remittance, timing). Would close it: 23 Pa.C.S. 4348 and the PA Child Support Program employer page.
- **Q9** Minimum-wage increase bill (2025-26 session): bill number, House passage date, Senate status. Would close it: palegis.us bill history.
- **Q10** Child Labor Act 2012 (Act 64) hours and permits: slip-law PDF has no text layer. Would close it: DLI child labour page or the consolidated 43 P.S. 40.1 ff.

Confidence by domain: labour 95%, income tax (state) 95%, local tax 85% (rates are per address by design), SUI 95%, payslip 85%, reporting 90%, leave 60% (city ordinances tier B on numbers), termination 90%, BIK 85%, garnishment 90%, prevailing wage 75%, indexation 90%, data protection 90%, live change 75%.
