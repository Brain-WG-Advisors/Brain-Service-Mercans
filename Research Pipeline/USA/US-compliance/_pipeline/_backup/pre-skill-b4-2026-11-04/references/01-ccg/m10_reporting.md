# Module 10: Reporting, Compliance & Finalisation

*Purpose: To define all statutory reporting obligations and final processing rules.*

## 10.1 Statutory Reporting

Field-level content of every return lives in the Report Specifications (04-reports-spec). Channels and authorisations live in the Statutory Integration Research (03-statutory-integrations). This module states the obligations.

### Describe the country's primary digital payroll reporting system.

There is no single national payroll reporting system. Each layer is reported separately:
- **Federal (IRS):** Form 941 quarterly (quarterly; due last day of the month after the quarter; amounts in cents (partial source)) [US-FEDS5-031], Form 940 annual (January 31 (10 more days if all FUTA deposited on time) (partial source)) [US-FEDS5-031], and deposits on the schedule set by the lookback liability (monthly up to 50,000, semiweekly above it, next day from 100,000) [US-FEDS5-004].
- **Federal (SSA):** Forms W-2/W-3 filed electronically in the EFW2 format (EFW2 Publication 42-007 (W-2) / 42-014 (W-2c) via SSA Business Services Online) [US-FIL-002], fixed records of 512 bytes [US-FEDS5-032]. Tax-year 2026 changes: TY2026 changes: RE adds Employer Signature PIN (319-328); RW adds Box 14b Primary/Secondary Treasury Tipped Occupation Code (490-492 / 493-495); RO/RU split Codes A and B into separate money fields (combined A+B field valid through TY2025 only), add money fields for existing Codes J, K, L, P and new Codes TA, TP, TT; SS wage base 184,500; FIRE replaced by IRIS [US-FEDS5-032].
- **State:** income-tax withholding returns to every State where withholding applies, and the UI quarterly wage report to the State of UI coverage only (UI quarterly wage report to the sui_state only (localization); State income-tax withholding returns to every State where withholding applies) [US-MULTIS5-017].
- **Local:** separate local returns where a locality collects its own tax (Module 6 and the PA, OH, MI, KY, MO, AL, CO, DE, OR, WV and NJ annexes).

**Filing channel for this build.** Federal and State filings are submitted through a third-party filing provider; there is no ADP integration (owner decision). The employer authorises the agent on Form 8655 (Form 8655 (Rev. Jan 2024); agent may sign/file 940/941 and deposit; taxpayer stays liable) [US-FED-008]. The employer remains liable for the tax. Third-party payer arrangements are described in Pub. 15 (Pub. 15 (2026) third-party payer arrangements (reporting agents, sec. 3504 agents, CPEOs) - liability allocation per arrangement) [US-FEDP51-002].

### Provide a Data Disaggregation Mapping Guide describing main reporting categories.

| Reporting category | Built from payroll | Federal return / form | State / local | Source |
|---|---|---|---|---|
| Wages subject to federal income tax, and FIT withheld | Taxable earnings less pre-tax exclusions; FIT per period | 941 (quarter), W-2 (year) | State wages and tax on the State W-2 copy | [US-FEDS5-031] |
| Social security (OASDI) wages and tax | Wages up to the annual base 184,500 | 941, W-2 | — | [US-FEDS5-005] |
| Medicare wages and tax, Additional Medicare | All wages; Additional Medicare above 200,000 | 941, W-2 | OH municipal base starts from Medicare wages (Module 6) | [US-FEDS5-005] |
| FUTA wages | First 7,000 per employee per year | 940 (deposit when liability exceeds 500 (partial source)) | SUI taxable wages per State base | [US-FEDS5-031] |
| Tips, qualified overtime, Trump-account contributions | TP (cash tips reported to employer); TT (qualified overtime compensation); TA (employer Trump-account contributions) | W-2 box 12 (new 2026 codes) | — | [US-FEDS5-007] |
| Tipped occupation | Box 14 split into 14a Other and 14b Treasury Tipped Occupation Code(s) | W-2 box 14b | — | [US-FEDS5-007] |
| State and local wages and tax | Per State and locality of withholding | — | W-2 boxes 15-20, up to 2 States and localities per form | [US-MULTIS5-011] |
| State PFML/SDI employee contributions | Employee premium per programme | Box 14 (informational) | Labels e.g. CA CASDI (or VPDI) in Box 14; CA PIT wages Box 16; CA PIT withheld Box 17; ME MEPFML | [US-CAS5-018] |
| UI wages per employee | Gross wages, taxable wages, (some States) hours and occupation | — | UI quarterly wage report to the State of coverage | [US-MULTIS5-017] |

### List all other mandatory reports, stating the frequency, file format, due date, reporting authority.

**Table 10.1.1: Federal reports**

| Report | Authority | Frequency / due | Format / channel | Source |
|---|---|---|---|---|
| Form 941 | IRS | quarterly; due last day of the month after the quarter; amounts in cents (partial source) | Electronic via the filing agent | [US-FEDS5-031] |
| Form 944 (instead of 941) | IRS | Annual, only on written IRS notice (liability up to 1,000 (partial source)) | Electronic via the filing agent | [US-FEDS5-031] |
| Form 940 (FUTA) | IRS | January 31 (10 more days if all FUTA deposited on time) (partial source) | Electronic via the filing agent | [US-FEDS5-031] |
| Forms W-2 / W-3 | SSA | Due 2027-02-01; a W-2 is required even with no withholding from 2,000 of wages | EFW2 Publication 42-007 (W-2) / 42-014 (W-2c) via SSA Business Services Online | [US-FEDS5-007] |
| Form 1042-S | IRS | IRIS (FIRE retired for TY2026); due 2027-03-15 | IRIS | [US-FEDS5-016] |
| Forms 1094-C / 1095-C (ACA) | IRS | Annual, for applicable large employers (50 (partial source) or more full-time incl. equivalent employees) | Electronic filing at 10 or more returns | [US-FEDS5-012] |
| New-hire report | State Directory of New Hires | Within 20 days of hire (shorter in many States, Table 10.1.2) | W-4 copy or an equivalent form; seven federal data elements (employee name, address, SSN, date of hire = first day of services for pay; employer name, address, FEIN) | [US-FEDS5-024] |
| Davis-Bacon certified payroll | Contracting agency | weekly, to the contracting agency; prime responsible for subcontractors; optional form WH-347; records 3 years | Paper or electronic to the agency (optional DOL form named in the rule) | [US-FEDS5-027] |

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

Instructions for the tax-year 2026 Forms 940 and 1094-C/1095-C are not yet issued; the 2025 editions were read. Not configured in this release (open gap RQ-526): The tax-year 2026 instructions for Forms 940 and 1094-C/1095-C are not yet issued; the 2025 editions were read.

**Table 10.1.2: State reporting parameters established from official sources.** The withholding-return and reconciliation forms per State are in the annexes and the Report Specifications.

| State | New-hire report (days) | UI quarterly report due | W-2 e-file threshold (forms) |
|---|---|---|---|
| Alaska (AK) | 20 | — | — |
| Alabama (AL) | 7 | — | 10 |
| Arkansas (AR) | 20 | — | — |
| Arizona (AZ) | 20 | — | — |
| California (CA) | 20 | — | — |
| Connecticut (CT) | 20 | — | — |
| District of Columbia (DC) | 20 | — | 25 |
| Delaware (DE) | 20 | — | — |
| Florida (FL) | 20 | — | — |
| Georgia (GA) | 10 | — | — |
| Hawaii (HI) | 20 | — | — |
| Iowa (IA) | 15 | — | — |
| Idaho (ID) | 20 | — | — |
| Illinois (IL) | 20 | — | — |
| Indiana (IN) | 20 | — | 25 |
| Kentucky (KY) | 20 | — | 26 |
| Louisiana (LA) | 20 | — | 50 |
| Massachusetts (MA) | 14 | — | 50 (from 2026-01-30) |
| Maryland (MD) | 20 | — | 25 |
| Maine (ME) | 7 | — | — |
| Michigan (MI) | 20 | — | — |
| Minnesota (MN) | 20 | — | — |
| Missouri (MO) | 20 | Apr 30; Jul 31; Oct 31; Jan 31 | 250 |
| Mississippi (MS) | 15 | Apr 30; Jul 31; Oct 31; Jan 31 | 10 |
| Montana (MT) | 20 | Apr 30; Jul 31; Oct 31; Jan 31 | — |
| North Carolina (NC) | 20 | Apr 30; Jul 31; Oct 31; Jan 31 | — |
| North Dakota (ND) | 20 | — | — |
| Nebraska (NE) | 20 | Apr 30; Jul 31; Oct 31; Jan 31 | 50 |
| New Hampshire (NH) | 20 | last day of month following quarter | — |
| New Jersey (NJ) | 20 | — | — |
| New Mexico (NM) | 20 | last day of month after quarter, electronic only | — |
| Nevada (NV) | 20 | Apr 30; Jul 31; Oct 31; Jan 31 (received) | — |
| New York (NY) | 20 | — | — |
| Ohio (OH) | 20 | last day of month after quarter | — |
| Oklahoma (OK) | 20 | — | — |
| Oregon (OR) | 20 | — | — |
| Pennsylvania (PA) | 20 | Apr 30; Jul 31; Oct 31; Jan 31 | — |
| Rhode Island (RI) | 14 | — | 25 |
| South Carolina (SC) | 20 | last day of month after quarter | — |
| South Dakota (SD) | 20 | Apr 30; Jul 31; Oct 31; Jan 31 (received) | — |
| Tennessee (TN) | 20 | Apr 30; Jul 31; Oct 31; Jan 31 | — |
| Texas (TX) | 20 | — | — |
| Utah (UT) | 20 | Apr 30; Jul 31; Oct 31; Jan 31 | — |
| Virginia (VA) | 20 | last day of month after quarter | — |
| Vermont (VT) | 10 | Apr 30; Jul 31; Oct 31; Jan 31 | — |
| Washington (WA) | 20 | Apr 30; Jul 31; Oct 31; Jan 31 | — |
| Wisconsin (WI) | 20 (from 2026-03-16) | end of month after quarter (from 2026-03-16) | 10 |
| West Virginia (WV) | 14 | Apr 30; Jul 31; Oct 31; Jan 31 | — |
| Wyoming (WY) | 20 (from 2026-05-08) | Apr 30; Jul 31; Oct 31; Jan 31 | — |

"—" means the parameter is not established from an official source for that State at this level (see the annex). Multistate employers that report electronically may report all new hires to one State (A multistate employer reporting electronically may send all new-hire reports to ONE designated State in which it has employees, after notifying HHS in writing) [US-MULTIS5-006]. Not configured in this release (open gap RQ-527): The HHS channel through which a multistate employer registers its designated new-hire State was not read (the statute, 42 U.S.C. 653a(b)(1)(B), carries the rule).

### What pay elements are required as intermediates from payroll for reporting?

Per employee and per period, the payroll engine must keep (and accumulate per quarter and per year):
- gross wages; wages subject to FIT; FIT withheld;
- OASDI wages (capped at the annual base) and tax, employee and employer;
- Medicare wages and tax, employee and employer; wages above the Additional Medicare threshold and that tax;
- FUTA taxable wages (first 7,000);
- per State: State wages, State tax withheld, SUI gross and taxable wages, PFML/SDI premium wages and premiums;
- per locality: local wages and local tax;
- the 2026 W-2 box 12 amounts TP (cash tips reported to employer); TT (qualified overtime compensation); TA (employer Trump-account contributions) [US-FEDS5-007], and the tipped-occupation code;
- hours worked and occupation where a State UI or PFML report requires them (e.g. Washington: Combined Paid Leave + WA Cares quarterly report; per employee: SSN or ITIN, last and first name (middle initial optional), hours associated with wages paid (rounded up to a whole number; salaried full-time 40 h/week; no hours for leave cash-outs or severance), wages paid in the quarter excluding tips, WA Cares exemption status, date of birth; employer totals of Paid Leave and WA Cares premiums withheld [US-WAB5-003]).

## 10.2 Integrations

### Is there any mandatory inbound integration?

- **Income withholding orders (child support):** the employer must act on IWOs received from State agencies (paper or e-IWO). For interstate orders the employer applies the law of the employee's principal place of employment (When an employer receives an income withholding order issued by another State, the employer shall apply the income withholding law of the State of the obligor's principal place of employment in determining the employer's fee for processing an income withholding order; the maximum amount permitted to be withheld from the obligor's income; the time periods within which the employer must implement the income withholding order and forward the child support payment; the priorities for withholding and allocating income withheld for multiple child support obligees; and any withholding terms or conditions not specified in the order) [US-MULTIS5-007]. It remits within 7 business days [US-MULTIS5-007]. The current federal IWO form is approved until 2029-08-31 [US-FEDS5-028]. Not configured in this release (open gap RQ-528): The dates on which States go live with the revised IWO / e-IWO (gig-worker fields) within the one-year extension are not known.
- **IRS levies** on wages follow Pub. 1494 exemption amounts (Module 7). Order of priority: Withholding for support has priority over any other legal process under state law against the same income (section 466(b)(7) of the Social Security Act); if a federal tax levy is in effect, notify the sender [US-FEDP6-002].
- No system-to-system inbound feed from a tax authority (such as a tax-code notice) is mandatory. Withholding certificates come from the employee (W-4 and State forms).

### Is there any mandatory outbound integration beyond standard reporting?

- **New-hire reporting** (employee name, address, SSN, date services first performed; employer name, address, FEIN) [US-FEDS5-024]. Electronic filers transmit Electronic/magnetic filers: two monthly transmissions, not less than 12 nor more than 16 days apart [US-FEDB5-001].
- **Certified payroll** on public works: federal Davis-Bacon weekly [US-FEDS5-027]; California electronic upload (electronic to Labor Commissioner via DIR eCPR (XML upload spec available)) [US-CAS5-017]. Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.
- All statutory filings go through the third-party filing provider (owner decision). The SIR documents the handoff.

## 10.3 Payslip Requirements

### List all mandatory components that must be itemized on an employee payslip.

**Federal:** no federal law requires a pay statement (not required) [US-FED-010]. The FLSA requires records only. They are kept 3 years [US-FEDS5-021]. Employment-tax records are kept 4 years [US-FEDS5-003].
**Which State's rule applies:** Default: the pay-statement statute of the work-location State (no other State reach rule researched); payslip in English (US-OWN-006) [US-MULTIS5-018]. The payslip is in English (owner decision US-OWN-006).

**Table 10.3.1: State pay-statement rules established from official sources**

| State | Verified rule (parameter: value) | Register |
|---|---|---|
| Alaska (AK) | sick leave, on statement: Sick leave used in the accrual year and sick leave balance on every statement (since 2025-09-25); a combined PTO plan satisfies it by showing PTO used and balance; statement, content: Written or electronic, each pay period: rate; gross and net; pay-period dates; federal income tax and Federal Insurance Contribution Act deductions; Alaska Employment Security Act contributions; board/lodging deductions; advances; straight-time and overtime hours; other authorised deductions; sick leave used in accrual year; sick leave balance; statement, electronic delivery: Written or electronic; no separate consent rule; payslip, required: yes; payslip, sick leave balance, required: yes | US-AKS5-001 |
| Alabama (AL) | statement, scope: none: no state pay-statement content statute; federal records rules apply; payslip, state statute, exists: no | US-ALP52-001 US-ALS5-007 |
| Arkansas (AR) | statement, scope: none: no itemised pay-statement statute; tipped employees get the tip-credit amount per hour in writing each time it changes (11 CAR 11) (from 2026-07-21); payslip, state statute, exists: no | US-ARP52-006 |
| Arizona (AZ) | sick leave, on statement: Every regular paycheck or attachment: earned paid sick time available, used to date in the year, and pay received as sick time (A.R.S. 23-375(C)); statement, scope: Statement (no content list) required only when paying by direct deposit or payroll card (A.R.S. 23-351(E),(F)); payslip, required when: only for direct deposit or payroll card: written or electronic statement of earnings and withholdings, no content list (23-351(E),(F)); payslip, sick time fields: sick time available; sick time used year to date; pay received as sick time (on paycheck or attachment, every regular paycheck) | US-AZS5-001 US-AZS5-011 |
| California (CA) | sick leave, on statement: Available paid sick leave on the wage statement or a separate writing each payday; statement, content: Lab. Code 226(a), semimonthly or each payment: gross; total hours (not for salaried exempt); piece units and rates; deductions; net; pay-period dates; name + last 4 SSN or employee ID; employer legal name and address; each hourly rate with hours; statement, household exclusion: Section 226 does not apply to any employer of a person employed by the owner or occupant of a residential dwelling whose duties are incidental to the ownership, maintenance, or use of the dwelling, including the care and supervision of children, or whose duties are personal and not in the course of the trade, business, profession, or occupation of the owner or occupant; payslip, inspection response days: 21; payslip, items: gross wages; total hours (not salaried exempt); piece-rate units and rates; deductions; net wages; pay-period dates; employee name + last 4 SSN or employee ID; employer legal name and address; every hourly rate with hours; payslip, penalty, max: 4,000; payslip, sick leave balance, required: yes | US-CAS5-005 US-CAS5-011 |
| Colorado (CO) | statement, comps rule7: Statement shows total pay, rate, tips, credits and time worked; kept 3 years; statement, content: C.R.S. 8-4-103(4), at least monthly or each payment: gross; all withholdings and deductions; net; pay-period dates; employee name or SSN; employer name and address. COMPS Rule 7 adds rate, tips, credits and time worked; payslip, comps rule7 items: total pay, rate, tips, credits and time worked (in addition to Wage Act items); kept 3 years; payslip, items: gross wages, withholdings/deductions, net wages, pay-period dates, employee name or SSN, employer name and address; at least monthly or each payment; records 3 years; fine up to 250 per employee per month max 7,500 (8-4-103(4)) | US-COP51-005 US-COS5-001 |
| Connecticut (CT) | pay code guide, url on pay record: From 2026-10-01 (PA 26-12 sec. 38, 31-13a(c)): employers with 100+ employees publish a pay-code guide (overtime and common differentials, min 10 codes where applicable) in English, Spanish and other common languages; its Internet web site address appears on each record of hours and is given at hire; a payroll provider guide satisfies it (from 2026-10-01); statement, content: Each payment: hours worked; gross pay with straight time and overtime separate; itemised deductions; net (hours and split not for OT-exempt); statement, electronic delivery: Electronic only with the employee explicit consent, a secure private way to access and print, and confidentiality safeguards (31-13a(b)); payslip, items: hours worked, gross pay with straight time and overtime separately, itemised deductions, net pay (hours/split not for OT-exempt); electronic only with explicit consent and secure access; payslip, pay code guide url, employer threshold: 100 (from 2026-10-01) | US-CTP51-005 US-CTS5-027 US-CTS5-028 |
| District of Columbia (DC) | statement, content: Each payment (32-1008(b)): date of payment; gross; deductions and additions with gratuities on a separate line; net; hours worked; tip declaration split cash/card; from 2026-01-01 a list of compensation sources beyond base wages and tips; payslip, items: date of payment; gross wages; deductions and additions with separate gratuities line; net wages; hours worked; tip-declaration form split cash/card; from 2026-01-01 list of compensation sources beyond base wages and tips | US-DCS5-010 |
| Delaware (DE) | statement, content: Employers with more than 3 employees, each payment: wages due; pay period; total deductions each separately specified; total hours for hourly employees (19 Del. C. 1108); statement, electronic delivery: On the check, a separate slip, or electronically if the employee can retain it; employee may ask for paper; statement, employer threshold: more than 3 employees; payslip, employer threshold: 3; payslip, items: wages due; pay period; total deductions each separately specified; total hours for hourly employees | US-DES5-002 |
| Florida (FL) | statement, scope: none for general employers; labor pools only (448.24(2)(g),(h)): itemised deductions each payment and annual earnings summary by 1 February; payslip, general statute, exists: no | US-FLL-002 |
| Georgia (GA) | statement, scope: none: O.C.G.A. 34-7-2 has no statement duty; GDOL handbook has no pay-stub rule | US-GAP9L-001 |
| Hawaii (HI) | statement, content: HRS 387-6(c), 14 items: employee name; employer name; employer address and phone; total hours; regular and OT hours; straight-time pay; OT pay; other compensation incl. allowances toward minimum wage; gross; amount and purpose of each deduction; net; pay date; pay period; rates and basis incl. OT and piece rates with counts; statement, electronic delivery: Electronic with the employee written authorization; direct deposit still requires a statement; payslip, items: employee name; employer name, address, phone; total hours; regular and OT hours; straight-time pay; OT pay; other compensation incl. MW allowances; gross; amount and purpose of each deduction; net; pay date; pay period; rates and basis incl. OT and piece rates/counts | US-HIP52-001 US-HIS5-007 |
| Iowa (IA) | statement, content: Each regular payday: hours worked, wages earned, deductions (91A.6(4)); itemised computation within 10 working days on request; statement, electronic delivery: Mail, secure electronic means, at the workplace, or access to view; no separate consent; statement, reach: Employees employed in Iowa (work location, not residence) (91A.2(3),(4)); payslip, items: hours worked, wages earned, deductions made, each regular payday (91A.6(4)); mail, secure electronic, workplace or view access, no separate consent; itemised computation within 10 working days on request | US-IAP51-002 US-IAS5-027 |
| Idaho (ID) | statement, scope: deductions_only: written statement of deductions for each pay period with deductions (45-609(2)); payslip, required content: written statement of deductions for each pay period in which deductions are made (45-609(2)); no full itemised statute | US-IDP51-002 US-IDS5-025 |
| Illinois (IL) | statement, content: Pay stub each pay period with itemized deductions (820 ILCS 115/10 as amended by P.A. 103-953); payroll-card payees also get hours, rate and deductions; statement, electronic access: Stubs kept 3 years; copies within 21 days on request (max twice per 12 months; former employees for one year); if electronic stubs become inaccessible after separation, offer prior-year stubs by the final pay period and record the offer; payslip, copy response days: 21; payslip, rules: pay stub each pay period; itemized deductions; payroll-card payees also hours, rate, deductions; stubs kept >= 3 years; copies within 21 days on request (max twice/12 months; former employees 1 year after separation); offer prior-year stubs if electronic access ends (115/10, P.A. 103-953) | US-ILS5-024 |
| Indiana (IN) | statement, content: Each pay period at least hours worked, wages paid, deductions (IC 22-2-2-8(a)); statement, scope: Duty binds employers subject to IC 22-2-2 = 2+ employees NOT subject to the FLSA minimum wage (IC 22-2-2-3); literal reading excludes FLSA-covered employers; payslip, items: hours worked, wages paid, deductions made, each pay period (IC 22-2-2-8(a)) | US-INP6-001 US-INS5-001 |
| Kansas (KS) | statement, scope: on_request: itemized statement of deductions on request for each pay period with deductions (K.S.A. 44-320(d)); payslip, required: itemized statement of deductions on request for each pay period with deductions (44-320(d)); no routine pay statement; payroll card net shown on earnings statement (44-314(d)) | US-KSP52-001 US-KSS5-013 |
| Kentucky (KY) | statement, content: Employers with 10+ employees that make deductions: each payment, paper or electronic statement of each deduction and its purpose; electronic requires access to a computer and printer (section 337.070); statement, employer threshold: 10; payslip, deduction statement, employer threshold: 10 | US-KYP8-001 |
| Louisiana (LA) | statement, scope: The text of R.S. 23:631 (payment after discharge or resignation) carries no pay-statement duty | US-LAR3-002 |
| Massachusetts (MA) | statement, content: Each payment (c.149 s.148): employer name; employee name; date; hours worked; hourly rate; deductions or increases for the period; payslip, items: employer name, employee name, date (day/month/year), hours worked, hourly rate, deductions or increases for the period (c.149 s.148) | US-MAP51-008 US-MAS5-005 |
| Maryland (MD) | sick leave, on statement: Available earned sick and safe leave balance each time wages are paid; an online balance system satisfies it (LE 3-1305(f)); statement, content: LE 3-504: employer name, address, phone; pay date and period; hours (unless exempt); rates; gross and net; each deduction by name and amount; other bases of pay; written or online; statement, tip credit: Tip Credit Wage Statement for restaurants; payslip, essl balance, required: yes; payslip, items: employer name, address, phone; pay date and period; hours (unless exempt); rates; gross and net; each deduction by name and amount; other bases of pay; written or online (LE 3-504); notice at hire and change one pay period ahead; payslip, ssn, prohibited: yes | US-MDP51-005 US-MDS5-007 US-MDS5-008 US-MDS5-013 |
| Maine (ME) | statement, content: Each payment: date of the pay period, hours, total earnings, itemized deductions (Title 26 section 665, subsection 1); statement, electronic delivery: Electronic allowed only with ready access and printing at no cost; same record due when a direct deposit is made; payslip, items: date of the pay period, hours, total earnings, itemized deductions; payslip, required: yes | US-MES5-006 |
| Michigan (MI) | statement, content: At payment (MCL 408.479(2)): hours worked, gross, pay-period identification, separate itemisation of deductions; comp time earned or paid; payslip, items: hours worked, gross wages, pay-period identification, separate itemisation of deductions (piece-rate hand harvesters: units); hours may be omitted for EAP-exempt, elected officials, political appointees (MCL 408.479(2)); comp time earned/paid; payslip, ssn, max digits: 4 | US-MIS5-009 US-MIS5-013 |
| Minnesota (MN) | sick leave, on statement: ESST hours available and used each pay period, on or attached to the statement or via an electronic system; statement, content: Earnings statement at the end of each pay period, in writing or by electronic means. Under 181.032(b) it must include: (1) the name of the employee; (2) the rate or rates of pay and basis thereof, including whether the employee is paid by hour, shift, day, week, salary, piece, commission, or other method; (3) allowances, if any, claimed pursuant to permitted meals and lodging; (4) the total number of hours worked by the employee unless exempt from chapter 177; (5) the total amount of gross pay earned by the employee during that period; (6) a list of deductions made from the employee's pay; (7) any amount deducted by the employer under section 268B.14, subdivision 3, and the amount paid by the employer based on the employee's wages under section 268B.14, subdivision 1; (8) the net amount of pay after all deductions are made; (9) the date on which the pay period ends; (10) the legal name of the employer and the operating name of the employer if different from the legal name; (11) the physical address of the employer's main office or principal place of business, and a mailing address if different; and (12) the telephone number of the employer; statement, electronic delivery: Electronic requires access to an employer computer during work hours and statements kept available 3 years; payslip, esst balance, required: yes; payslip, frequency: each pay period, written or electronic | US-MNP6-001 US-MNS5-011 |
| Missouri (MO) | statement, scope: deductions_only: statement of total deductions at least monthly (290.080); payslip, deduction statement: statement of total deductions at least monthly | US-MOP52-002 |
| Mississippi (MS) | statement, scope: The Mississippi Department of Employment Security required-posters page lists no pay-statement notice | US-MSP9L-001 |
| Montana (MT) | statement, content: Every payment: itemized statement of state and federal income tax, social security and other deductions with amounts; statement saying none if nothing deducted (MCA 39-3-101); payslip, items: itemized statement of state and federal income tax, social security and other deductions each payment | US-MTP51-006 |
| North Carolina (NC) | statement, electronic delivery: In writing, printable e-mail or any means the employee can keep; no separate consent; statement, scope: deductions_only: itemized statement of deductions each pay period with deductions (G.S. 95-25.13), plus hire wage notice; payslip, items: itemized statement of deductions each pay period with deductions; wage notice at hire | US-NCS5-024 US-NCW1B-003 |
| North Dakota (ND) | statement, content: Each pay period a check stub or pay voucher: hours worked, rate, required state and federal deductions, authorized deductions (46-02-07-02, recordkeeping item 10); payslip, items: check stub or pay voucher each pay period: hours worked, rate, required state/federal deductions, authorized deductions | US-NDS5-007 |
| Nebraska (NE) | statement, content: Each regular payday: employer identity, hours paid, wages earned, deductions (48-1230(2)); hours not required for FLSA-exempt unless OT/hours-based; payslip, items: employer identity, hours paid, wages earned, deductions each regular payday | US-NEP51-004 |
| New Hampshire (NH) | statement, scope: deductions_only: statement of deductions each pay period with a deduction (RSA 275:49 IV); written monthly accounting for 275:48 I(d) deductions; payslip, hire notice: written notice at hire and before change of rate, basis, payday/place, computation method; fringe-benefit policy; payslip, items: statement of deductions each pay period a deduction is made; monthly itemized accounting for 275:48 I(d) deductions | US-NHP51-001 US-NHS5-004 |
| New Jersey (NJ) | statement, content: Statement of deductions each pay period with deductions; employers with 10+ employees add gross, net, rate and hours where relevant (34:11-4.6(c)); statement, electronic delivery: Electronic allowed unless the employee asks for paper; payslip, full content, employer threshold: 10; payslip, items: deductions statement; employers 10+ add gross, net, rate and hours | US-NJP8-001 |
| New Mexico (NM) | sick leave, on statement: Year-to-date earned sick leave accrued and used, at least quarterly, on the earnings statement or electronically; statement, content: Written receipt each payday: employer identity; gross; hours worked; total wages and benefits earned; itemized deductions (50-4-2(B)); payslip, items: employer identity, gross pay, hours worked, total wages and benefits, itemized deductions; payslip, sick leave summary: YTD earned sick leave accrued and used at least quarterly | US-NMP8-001 US-NMS5-002 |
| Nevada (NV) | statement, content: Itemized list of deductions at each payment (NRS 608.110(2)); payslip, items: itemized deductions each payment; available paid-leave hours each payday (50+ NV employees) | US-NVR3-001 US-NVS5-001 |
| New York (NY) | statement, content: Labor Law 195(3), every payment: dates of work; names; employer address and phone; rates and basis; gross; deductions; allowances toward minimum wage; net; non-exempt: regular and OT rates and hours; piece rates and counts; payslip, items: dates of work; names; employer address/phone; rates and basis; gross; deductions; allowances; net; regular and OT rates and hours (non-exempt); piece rates | US-NYS5-006 |
| Ohio (OH) | statement, content: ORC 4113.14 (from 2025-04-09), each pay period written or electronic: employee name and address; employer name; gross and net; amount and purpose of each addition and deduction; pay date and period; hourly employees hours and rate; payslip, items: name and address; employer name; gross and net; each addition and deduction; pay date and period; hours and rate (hourly) | US-OHP51-001 |
| Oklahoma (OK) | statement, scope: deductions_only: brief itemized statement of all deductions with each payment (40 O.S. 165.2); payslip, items: brief itemized statement of all deductions with each payment | US-OKS5-003 |
| Oregon (OR) | statement, content: ORS 652.610(1)(b): payment date; dates of work; employee name; employer name and registry/ID number; employer address and phone; rates; basis; gross; net; each deduction with amount and purpose; allowances toward minimum wage; non-exempt regular and OT rates, hours and pay; piece rates and counts; statement, electronic delivery: Electronic only with the employee express agreement and ability to print or store on receipt (652.610(1)(c)); payslip, items: payment date; work dates; employee name; employer name, registry no., address, phone; rates; basis; gross; net; each deduction; allowances; regular/OT rates and hours; piece rates; payslip, new hire explanation: written explanation of earnings, deductions and all payroll codes; updated each January 1 | US-ORS5-022 US-ORS5-026 |
| Pennsylvania (PA) | statement, content: Every payment: hours worked, rates, gross, allowances toward minimum wage, deductions, net (34 Pa. Code 231.36); payslip, items: hours worked, rates, gross, allowances toward minimum wage, deductions, net | US-PAP51-001 |
| Rhode Island (RI) | statement, content: Every regular payday: hours worked (except 28-12-4.3 exempt), every deduction with explanation; commercial construction also regular hourly rate (28-14-2.1); electronic allowed, free printed copy on written request; payslip, items: hours worked (non-exempt), every deduction with explanation; regular hourly rate in commercial construction | US-RIP51-002 |
| South Carolina (SC) | statement, content: Itemized statement of gross pay and deductions each pay period (41-10-30(C)); direct deposit: statement of earnings and withholdings (41-10-40(B)); statement, exemptions: Section 41-10-30 (notification to employees) does not apply to domestic labour in private homes or to employers with fewer than five employees at all times in the preceding twelve months (41-10-20); payslip, items: itemized gross pay and deductions each pay period | US-SCP52-006 |
| South Dakota (SD) | statement, scope: none: no SD statute requires a pay statement (Title 60 full-text scan); payslip, statute, exists: no | US-SDS5-001 |
| Tennessee (TN) | statement, scope: none: no TN itemised pay-statement statute located; federal records rules; payslip, statute, exists: no | US-TNS5-001 |
| Texas (TX) | statement, scope: non_flsa_only: Labor Code 62.003 earnings statement (name, rate, gross, each deduction and purpose, net, hours or units; signed by employer or agent) applies only to employees not covered by the FLSA (62.151); best practice for everyone else; payslip, content, non flsa: signed statement: name, rate, gross, each deduction and purpose, net, hours or units | US-TXS5-003 |
| Utah (UT) | statement, format: All lawful offsets itemized on a statement or detachable check stub (R610-3-20); statement, scope: deductions_only: statement of each deduction on each regular payday (34-28-3(4)); construction-trade licensees full statement (34-28-3(5)); payslip, items: statement of total amount of each deduction each regular payday; construction licensees full statement | US-UTP6-001 US-UTS5-012 |
| Virginia (VA) | statement, content: Each regular pay date, paystub or online accounting: employer name and address; hours (hourly and salaried below the FLSA level); rate; gross; amount and purpose of each deduction; enough detail to work out gross and net (from 2026-07-01); payslip, items: employer name/address; hours (hourly and below-FLSA-salary); rate; gross; each deduction amount and purpose (from 2026-07-01) | US-VAS5-003 |
| Vermont (VT) | statement, content: Detailed written statement with each weekly pay: gross, hours, hourly rate, itemised deductions incl. meals; payslip, items: gross pay, hours worked, hourly rate, all deductions itemised | US-VTP9-001 |
| Washington (WA) | sick leave, on statement: At least monthly: paid sick leave accrued, used and available; may be on the regular pay statement (WAC 296-128-755(2)); statement, content: Every payday, separate from the paycheck: hours or days worked, rates, gross, all deductions, pay period, payment date (WAC 296-126-040); statement, electronic delivery: Electronic if the employee can receive and copy it on payday; otherwise paper; payslip, items: pay basis (hours/days), rates, gross, all deductions, pay period dates, payment date; separate from paycheck; payslip, sick leave balance, monthly: yes | US-WAS5-004 US-WAS5-005 |
| Wisconsin (WI) | statement, content: Hours worked, rate, amount and reason for each deduction, on the check, envelope or accompanying paper; coding system allowed (103.457; DWD 272.10) (from 2026-10-01); payslip, items: hours worked, rate, amount and reason for each deduction | US-WIP52-001 |
| West Virginia (WV) | statement, content: Scheduled payday itemized statement: hourly rate or salary; hours paid; OT rate; bonus or incentive pay; itemized deductions (42 CSR 5 s.7.3, sunset 2029-07-01); payslip, items: hourly rate or salary, hours paid, overtime rate, bonus/incentive, itemized deductions | US-WVS5-008 |
| Wyoming (WY) | statement, scope: deductions_only: detachable part of the check or attached slip with an itemized statement of all deductions (27-4-101(b)); agricultural operations exempt; payslip, items: itemized written statement of all deductions on detachable part of check/voucher or attached slip | US-WYP51-005 |

States not listed carry their pay-statement rule (or its absence) in the annex and in the Payslip Generator research. The Payslip Generator implements the union of these items.

## 10.4 Other Compliance

### Is payroll software certification mandatory?

No general federal certification of payroll software is established from an official source. A filing agent is authorised per employer on Form 8655 [US-FED-028]. That is an authorisation, not a software certification. Agent-list changes go through the IRS channel described in Pub. 1474 (Pub. 1474 (Rev. 4-2026): reporting agent = accounting service, franchiser, bank, service bureau or other payroll-services entity; agent list additions/deletions electronic above 100 submissions a week via SLFT B2B; deposits via EFTPS or FTA) [US-FIL-001]. State example: Wisconsin (Payroll service providers must register and test their software with DOR) [US-WIS5-016]. Not configured in this release (open gap RQ-529): A census of State software-certification or provider-testing duties (beyond Wisconsin) is not established from an official source.

## 10.5 Year-End Processing and Finalisation

### Describe the mandatory year-end finalisation process.

There is no employer-side income-tax regularisation. The employee settles at assessment (Form 1040 and State returns). The employer's year end is a reconciliation:
1. Reconcile the four quarterly Forms 941 to the W-2/W-3 totals [US-FEDS5-031].
2. File Form W-2/W-3 with SSA by 2027-02-01 [US-FEDS5-007].
3. File Form 940 (January 31 (10 more days if all FUTA deposited on time) (partial source)) [US-FEDS5-031].
4. File each State's annual withholding reconciliation and State W-2 copies (Report Specifications; e.g. Michigan Form 5081 annual reconciliation for 2026 due 2027-02-28 (every filer) [US-MIS5-021]).
5. Collect new W-4 exemption claims for the next year (2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027) [US-FEDS5-006].
6. Reset the annual accumulators (OASDI, FUTA, SUI and PFML bases, Additional Medicare threshold) at the first payment date of the new year. The 2027 OASDI base is 192,300 [US-FEDB5-401].

Changes during 2026 that the year-end process must apply from their date:

| Item | Rule or value | In force from | Source |
|---|---|---|---|
| Form 940 due date, return for 2025 | TY2025 rule: Form 940 for 2025 due February 2, 2026 (February 10, 2026 if all FUTA tax was deposited when due) (TY2025 rule, re-verify on the 2026 instructions) | 2026-01-01 to 2026-02-10 | [US-FEDS5-031] |
| Form 940 due date, from the 2026 instructions | TY2025 rule applies until the 2026 Form 940 instructions are published: Form 940 due the last day of the month after the year ends (February 1, 2027 for TY2026; February 10, 2027 if all FUTA tax was deposited when due, per the 2025 instructions' rule). Requirement: re-verify against the Instructions for Form 940 (2026) when the IRS publishes them; the live i940.pdf was still the 2025 edition on 2026-11-04. | 2026-02-11 | [US-FEDS5-031] |
| FUTA credit-reduction States, wages of 2025 (reported on the 2025 Form 940) | 2025 (final): CA 0.012 (1.2%); VI 0.045 (4.5%); no other state | 2025-01-01 to 2026-02-10 | [US-FEDS6-009] |
| FUTA credit-reduction States, wages of 2026 | The 2026 list: Not configured in this release (open gap RQ-402): The 2026 list of FUTA credit-reduction States is published by the Department of Labor after November 10, 2026. | 2026-02-11 |  |
| Maine withholding return form | 941ME quarterly, last day of month after quarter, electronic mandatory even when nothing to report | 2026-04-14 | [US-MEP52-002] |
| New Jersey withholding representative appointment form | M-5008-R Appointment of Taxpayer Representative (6/26) | 2026-06-09 | [US-NJR3-004] |
| District of Columbia withholding representative form | OTR D-2848 | 2026-09-16 | [US-DCP51-014] |
| Texas UI representation form | Form C-42 Written Authorization to Represent Employing Unit | 2026-03-13 | [US-TXP52-008] |

TY2027 federal indexation is not yet published: Not configured in this release (open gap RQ-530): The tax-year 2027 IRS inflation adjustments, 2027 retirement-plan limits and 2027 Pub. 15-T are not yet published.

### What documentation or annual statements must be provided to employees?

- **Form W-2** by 2027-02-01 [US-FEDS5-007]. For a terminated employee: Terminated employee: W-2 no later than January 31 of following year (earlier on request) [US-FED-016]. State examples: Delaware within 30 days of termination on request [US-DES5-005]; Mississippi within 30 days [US-MSS5-004].
- The SSN may be truncated to its last four digits on the employee copies of Form W-2 only, never on Copy A; the EIN is never truncated [US-FEDS5-022].
- **Form 1042-S** for treaty-exempt wages of nonresident aliens [US-FEDS5-016].
- **Form 1095-C** for employees of an applicable large employer [US-FEDS5-012].

### Is there a formal process for correcting errors discovered after the fiscal year has been closed?

Yes. Wage statements are corrected on Form W-2c, filed electronically in the EFW2C format (EFW2 Publication 42-007 (W-2) / 42-014 (W-2c) via SSA Business Services Online) [US-FIL-002]. Quarterly returns are corrected on Form 941-X [US-FEDS5-031]. Excess OASDI withheld because of multiple employers is refunded to the employee at assessment, not by the employer. States have their own amendment routes; for example Alabama UI (Quarterly Contribution and Wage Report via eGov only (online_form or file_upload); due last day of month after quarter; corrections UC-10C) [US-ALS5-007] and Massachusetts W-2 (due Jan 31; 50+ W-2s electronic via MassTaxConnect/Bulk File Portal; <= 49 paper with M-3; corrections paper W-2c; EFW2 RA/RE/RS/RT, RS MA wages 276-286, MA tax 287-297, RT = sum RS) [US-MAS5-015].


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `ak.newhire.report_days` | 20 | from 2026-01-01 | US-AKS5-007 |
| `al.newhire.report_days` | 7 | from 2026-01-01 | US-ALS5-008 |
| `al.report.sui.quarterly` | Quarterly Contribution and Wage Report via eGov only (online_form or file_upload); due last day of month after quarter; corrections UC-10C | from 2026-01-01 | US-ALS5-007 |
| `al.report.w2.efile_threshold` | 10 | from 2026-01-01 | US-ALS5-006 |
| `ar.newhire.report_days` | 20 | from 2026-01-01 | US-ARP9V-001 |
| `az.newhire.report_days` | 20 | from 2026-01-01 | US-AZS5-012 |
| `az.payslip.required_when` | only for direct deposit or payroll card: written or electronic statement of earnings and withholdings, no content list (23-351(E),(F)) | from 2026-01-01 | US-AZS5-001 |
| `az.payslip.sick_time_fields` | sick time available; sick time used year to date; pay received as sick time (on paycheck or attachment, every regular paycheck) | from 2017-07-01 | US-AZS5-011 |
| `ca.newhire.report_days` | 20 | from 2026-01-01 | US-CAS5-018 |
| `ca.payslip.inspection_response_days` | 21 | from 2026-01-01 | US-CAS5-005 |
| `ca.payslip.items` | gross wages; total hours (not salaried exempt); piece-rate units and rates; deductions; net wages; pay-period dates; employee name + last 4 SSN or employee ID; employer legal name and address; every hourly rate with hours | from 2026-01-01 | US-CAS5-005 |
| `ca.payslip.penalty.max` | 4,000 | from 2026-01-01 | US-CAS5-005 |
| `ca.prevailing_wage.certified_payroll` | electronic to Labor Commissioner via DIR eCPR (XML upload spec available) | from 2026-01-01 | US-CAS5-017 |
| `co.payslip.comps_rule7_items` | total pay, rate, tips, credits and time worked (in addition to Wage Act items); kept 3 years | from 2026-01-01 | US-COS5-001 |
| `co.payslip.items` | gross wages, withholdings/deductions, net wages, pay-period dates, employee name or SSN, employer name and address; at least monthly or each payment; records 3 years; fine up to 250 per employee per month max 7,500 (8-4-103(4)) | from 2025-08-06 | US-COP51-005 |
| `ct.newhire.report_days` | 20 | from 2026-01-01 | US-CTS5-019 |
| `ct.payslip.items` | hours worked, gross pay with straight time and overtime separately, itemised deductions, net pay (hours/split not for OT-exempt); electronic only with explicit consent and secure access | from 2026-01-01 | US-CTS5-027 |
| `ct.payslip.pay_code_guide_url.employer_threshold` | 100 | from 2026-10-01 | US-CTS5-028 |
| `dc.newhire.report_days` | 20 | from 2026-01-01 | US-DCS5-022 |
| `dc.payslip.items` | date of payment; gross wages; deductions and additions with separate gratuities line; net wages; hours worked; tip-declaration form split cash/card; from 2026-01-01 list of compensation sources beyond base wages and tips | from 2026-01-01 | US-DCS5-010 |
| `dc.report.w2.efile_threshold` | 25 | from 2025-01-01 | US-DCS5-015 |
| `de.newhire.report_days` | 20 | from 2026-01-01 | US-DES5-005 |
| `de.payslip.employer_threshold` | 3 | from 2026-01-01 | US-DES5-002 |
| `de.payslip.items` | wages due; pay period; total deductions each separately specified; total hours for hourly employees | from 2026-01-01 | US-DES5-002 |
| `de.report.w2.employee_on_termination_days` | 30 | from 2026-01-01 | US-DES5-005 |
| `fed.aca.ale.fte_threshold` | 50 | from 2025-01-01 | US-FEDS5-012 |
| `fed.aca.efile_threshold` | 10 | from 2025-01-01 | US-FEDS5-012 |
| `fed.davis_bacon.certified_payroll.frequency` | weekly, to the contracting agency; prime responsible for subcontractors; optional form WH-347; records 3 years | from 2023-10-23 | US-FEDS5-027 |
| `fed.deposit.monthly_max_lookback_liability` | 50,000 | from 2026-01-01 | US-FEDS5-004 |
| `fed.deposit.next_day_threshold` | 100,000 | from 2026-01-01 | US-FEDS5-004 |
| `fed.efw2.record_length` | 512 | from 2026-01-01 | US-FEDS5-032 |
| `fed.efw2.ty2026_changes` | TY2026 changes: RE adds Employer Signature PIN (319-328); RW adds Box 14b Primary/Secondary Treasury Tipped Occupation Code (490-492 / 493-495); RO/RU split Codes A and B into separate money fields (combined A+B field valid through TY2025 only), add money fields for existing Codes J, K, L, P and new Codes TA, TP, TT; SS wage base 184,500; FIRE replaced by IRIS | from 2026-01-01 | US-FEDS5-032 |
| `fed.fica.addl_medicare.withholding_threshold` | 200,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 184,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 192,300 | from 2027-01-01 to 2027-12-31 | US-FEDB5-401 |
| `fed.form1042s.channel` | IRIS (FIRE retired for TY2026); due 2027-03-15 | from 2026-01-01 | US-FEDS5-016 |
| `fed.form940.due` | January 31 (10 more days if all FUTA deposited on time) | from 2026-01-01 | US-FEDS5-031 |
| `fed.form941.frequency` | quarterly; due last day of the month after the quarter; amounts in cents | from 2026-01-01 | US-FEDS5-031 |
| `fed.form944.max_liability` | 1,000 | from 2026-01-01 | US-FEDS5-031 |
| `fed.futa.deposit_threshold` | 500 | from 2026-01-01 | US-FEDS5-031 |
| `fed.futa.wage_base` | 7,000 | from 2025-01-01 | US-FED-007 |
| `fed.iwo.omb_expiry` | 2029-08-31 | from 2026-08-25 to 2029-08-31 | US-FEDS5-028 |
| `fed.iwo.priority` | Withholding for support has priority over any other legal process under state law against the same income (section 466(b)(7) of the Social Security Act); if a federal tax levy is in effect, notify the sender | from 2026-01-01 to 2026-12-31 | US-FEDP6-002 |
| `fed.newhire.deadline_days` | 20 | from 1997-10-01 | US-FEDS5-024 |
| `fed.newhire.electronic_interval` | Electronic/magnetic filers: two monthly transmissions, not less than 12 nor more than 16 days apart | from 1997-10-01 | US-FEDB5-001 |
| `fed.newhire.fields` | employee name, address, SSN, date services first performed; employer name, address, FEIN | from 1997-10-01 | US-FEDS5-024 |
| `fed.newhire.form` | W-4 copy or an equivalent form; seven federal data elements (employee name, address, SSN, date of hire = first day of services for pay; employer name, address, FEIN) | from 1997-10-01 | US-FEDB5-001 |
| `fed.records.flsa.retention_years` | 3 | from 2026-11-02 | US-FEDS5-021 |
| `fed.records.irs.retention_years` | 4 | from 2026-01-01 | US-FEDS5-003 |
| `fed.reporting_agent.authorization` | Form 8655 (Rev. Jan 2024); agent may sign/file 940/941 and deposit; taxpayer stays liable | from 2012-11-19 | US-FED-008 |
| `fed.w2.box12.new_codes` | TP (cash tips reported to employer); TT (qualified overtime compensation); TA (employer Trump-account contributions) | from 2026-01-01 | US-FEDS5-007 |
| `fed.w2.box14b` | Box 14 split into 14a Other and 14b Treasury Tipped Occupation Code(s) | from 2026-01-01 | US-FEDS5-007 |
| `fed.w2.due_date` | 2027-02-01 | from 2026-01-01 | US-FEDS5-007 |
| `fed.w2.no_withholding_threshold` | 2,000 | from 2026-01-01 | US-FEDS5-007 |
| `fed.w2.terminated_employee.furnishing` | Terminated employee: W-2 no later than January 31 of following year (earlier on request) | from 2026-01-01 | US-FED-016 |
| `fed.w4.exempt.validity` | 2026 only: the exemption checkbox certification lapses; a new W-4 is required for 2027 | from 2026-01-01 to 2026-12-31 | US-FEDS5-006 |
| `fl.newhire.report_days` | 20 | from 2026-01-01 | US-FLS5-008 |
| `ga.newhire.report_days` | 10 | from 2026-01-01 | US-GAS5-012 |
| `hi.newhire.report_days` | 20 | from 2026-01-01 | US-HIS5-021 |
| `hi.payslip.items` | employee name; employer name, address, phone; total hours; regular and OT hours; straight-time pay; OT pay; other compensation incl. MW allowances; gross; amount and purpose of each deduction; net; pay date; pay period; rates and basis incl. OT and piece rates/counts | from 2026-01-01 | US-HIS5-007 |
| `ia.newhire.report_days` | 15 | from 2026-01-01 | US-IAS5-012 |
| `ia.payslip.items` | hours worked, wages earned, deductions made, each regular payday (91A.6(4)); mail, secure electronic, workplace or view access, no separate consent; itemised computation within 10 working days on request | from 2026-01-01 | US-IAS5-027 |
| `id.newhire.report_days` | 20 | from 2026-01-01 | US-IDS5-015 |
| `id.payslip.required_content` | written statement of deductions for each pay period in which deductions are made (45-609(2)); no full itemised statute | from 2026-01-01 | US-IDS5-025 |
| `il.newhire.report_days` | 20 | from 2026-01-01 | US-ILS5-018 |
| `il.payslip.copy_response_days` | 21 | from 2025-01-01 | US-ILS5-024 |
| `il.payslip.rules` | pay stub each pay period; itemized deductions; payroll-card payees also hours, rate, deductions; stubs kept >= 3 years; copies within 21 days on request (max twice/12 months; former employees 1 year after separation); offer prior-year stubs if electronic access ends (115/10, P.A. 103-953) | from 2025-01-01 | US-ILS5-024 |
| `in.newhire.report_days` | 20 | from 2024-07-01 | US-INS5-016 |
| `in.payslip.items` | hours worked, wages paid, deductions made, each pay period (IC 22-2-2-8(a)) | from 2026-01-01 | US-INS5-001 |
| `in.report.w2.efile_threshold` | 25 | from 2026-01-01 | US-INS5-011 |
| `ks.payslip.required` | itemized statement of deductions on request for each pay period with deductions (44-320(d)); no routine pay statement; payroll card net shown on earnings statement (44-314(d)) | from 2026-01-01 | US-KSS5-013 |
| `ky.newhire.report_days` | 20 | from 2025-07-01 | US-KYS5-020 |
| `ky.payslip.deduction_statement.employer_threshold` | 10 | from 2026-01-01 | US-KYP8-001 |
| `ky.report.w2.efile_threshold` | 26 | from 2026-01-01 | US-KYS5-013 |
| `la.newhire.report_days` | 20 | from 2026-01-01 | US-LAS5-010 |
| `la.report.w2.efile_threshold` | 50 | from 2026-01-01 | US-LAS5-009 |
| `ma.newhire.report_days` | 14 | from 2026-01-01 | US-MAS5-016 |
| `ma.payslip.items` | employer name, employee name, date (day/month/year), hours worked, hourly rate, deductions or increases for the period (c.149 s.148) | from 2026-01-01 | US-MAS5-005 |
| `ma.report.w2` | due Jan 31; 50+ W-2s electronic via MassTaxConnect/Bulk File Portal; <= 49 paper with M-3; corrections paper W-2c; EFW2 RA/RE/RS/RT, RS MA wages 276-286, MA tax 287-297, RT = sum RS | from 2026-01-30 | US-MAS5-015 |
| `ma.report.w2.efile_threshold` | 50 | from 2026-01-30 | US-MAS5-015 |
| `md.newhire.report_days` | 20 | from 2026-01-01 | US-MDS5-018 |
| `md.payslip.items` | employer name, address, phone; pay date and period; hours (unless exempt); rates; gross and net; each deduction by name and amount; other bases of pay; written or online (LE 3-504); notice at hire and change one pay period ahead | from 2026-01-01 | US-MDP51-005 |
| `md.report.w2.efile_threshold` | 25 | from 2025-01-01 | US-MDS5-016 |
| `me.newhire.report_days` | 7 | from 2026-01-01 | US-MES5-016 |
| `me.payslip.items` | date of the pay period, hours, total earnings, itemized deductions | from 2026-01-01 | US-MES5-006 |
| `me.pfml.w2_box14_label` | MEPFML | from 2025-01-01 | US-MES5-025 |
| `mi.newhire.report_days` | 20 | from 2026-01-01 | US-MIB5-001 |
| `mi.payslip.items` | hours worked, gross wages, pay-period identification, separate itemisation of deductions (piece-rate hand harvesters: units); hours may be omitted for EAP-exempt, elected officials, political appointees (MCL 408.479(2)); comp time earned/paid | from 2026-01-01 | US-MIS5-009 |
| `mi.payslip.ssn.max_digits` | 4 | from 2005-01-01 | US-MIS5-013 |
| `mi.report.annual.5081` | Form 5081 annual reconciliation for 2026 due 2027-02-28 (every filer) | from 2026-01-01 | US-MIS5-021 |
| `mn.newhire.report_days` | 20 | from 2026-01-01 | US-MNS5-016 |
| `mn.payslip.frequency` | each pay period, written or electronic | from 2026-01-01 | US-MNP6-001 |
| `mo.newhire.report_days` | 20 | from 2026-01-01 to 2026-12-31 | US-MOS5-001 |
| `mo.payslip.deduction_statement` | statement of total deductions at least monthly | from 1955-08-28 | US-MOP52-002 |
| `mo.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2026-01-01 | US-MOS5-013 |
| `mo.report.w2.efile_threshold` | 250 | from 2026-01-01 to 2026-12-31 | US-MOS5-001 |
| `ms.newhire.report_days` | 15 | from 1998-10-01 | US-MSS5-006 |
| `ms.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2026-01-01 | US-MSS5-012 |
| `ms.report.w2.efile_threshold` | 10 | from 2026-01-01 | US-MSS5-005 |
| `ms.term.w2_after_termination.days` | 30 | from 2026-01-01 | US-MSS5-004 |
| `mt.newhire.report_days` | 20 | from 2026-01-01 | US-MTS5-012 |
| `mt.payslip.items` | itemized statement of state and federal income tax, social security and other deductions each payment | from 2026-01-01 | US-MTP51-006 |
| `mt.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2025-07-01 | US-MTS5-025 |
| `multi.iwo.governing_law` | When an employer receives an income withholding order issued by another State, the employer shall apply the income withholding law of the State of the obligor's principal place of employment in determining the employer's fee for processing an income withholding order; the maximum amount permitted to be withheld from the obligor's income; the time periods within which the employer must implement the income withholding order and forward the child support payment; the priorities for withholding and allocating income withheld for multiple child support obligees; and any withholding terms or conditions not specified in the order | from 2026-01-01 | US-MULTIS5-007 |
| `multi.iwo.remittance_business_days` | 7 | from 2026-01-01 | US-MULTIS5-007 |
| `multi.newhire.designated_state` | A multistate employer reporting electronically may send all new-hire reports to ONE designated State in which it has employees, after notifying HHS in writing | from 2026-01-01 | US-MULTIS5-006 |
| `multi.payslip.reach.default` | Default: the pay-statement statute of the work-location State (no other State reach rule researched); payslip in English (US-OWN-006) | from 2020-06-29 | US-MULTIS5-018 |
| `multi.ui_wage_report.routing` | UI quarterly wage report to the sui_state only (localization); State income-tax withholding returns to every State where withholding applies | from 2026-01-01 | US-MULTIS5-017 |
| `multi.w2.states_per_form` | 2 | from 2026-01-01 | US-MULTIS5-011 |
| `nc.newhire.report_days` | 20 | from 2026-01-01 | US-NCS5-020 |
| `nc.payslip.items` | itemized statement of deductions each pay period with deductions; wage notice at hire | from 2026-01-01 | US-NCW1B-003 |
| `nc.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2026-01-01 | US-NCS5-025 |
| `nd.newhire.report_days` | 20 | from 2026-01-01 | US-NDS5-013 |
| `nd.payslip.items` | check stub or pay voucher each pay period: hours worked, rate, required state/federal deductions, authorized deductions | from 2012-10-01 | US-NDS5-007 |
| `ne.newhire.report_days` | 20 | from 2004-01-01 | US-NES5-014 |
| `ne.payslip.items` | employer identity, hours paid, wages earned, deductions each regular payday | from 2026-01-01 | US-NEP51-004 |
| `ne.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2025-09-11 | US-NES5-011 |
| `ne.report.w2.efile_threshold` | 50 | from 2025-11-01 | US-NES5-017 |
| `nh.newhire.report_days` | 20 | from 2026-01-01 | US-NHS5-006 |
| `nh.payslip.hire_notice` | written notice at hire and before change of rate, basis, payday/place, computation method; fringe-benefit policy | from 2020-03-05 | US-NHS5-004 |
| `nh.payslip.items` | statement of deductions each pay period a deduction is made; monthly itemized accounting for 275:48 I(d) deductions | from 2026-01-01 | US-NHP51-001 |
| `nh.report.ui.quarterly_due` | last day of month following quarter | from 2026-01-01 | US-NHS5-013 |
| `nj.newhire.report_days` | 20 | from 2026-01-01 | US-NJS5-018 |
| `nj.payslip.full_content.employer_threshold` | 10 | from 2026-01-01 | US-NJP8-001 |
| `nj.payslip.items` | deductions statement; employers 10+ add gross, net, rate and hours | from 2026-01-01 | US-NJP8-001 |
| `nm.newhire.report_days` | 20 | from 1997-10-01 | US-NMS5-010 |
| `nm.payslip.items` | employer identity, gross pay, hours worked, total wages and benefits, itemized deductions | from 2026-01-01 | US-NMP8-001 |
| `nm.payslip.sick_leave_summary` | YTD earned sick leave accrued and used at least quarterly | from 2022-07-01 | US-NMS5-002 |
| `nm.report.ui.quarterly_due` | last day of month after quarter, electronic only | from 2026-01-01 | US-NMS5-016 |
| `nv.newhire.report_days` | 20 | from 2026-01-01 | US-NVS5-007 |
| `nv.payslip.items` | itemized deductions each payment; available paid-leave hours each payday (50+ NV employees) | from 2025-10-01 | US-NVS5-001 |
| `nv.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 (received) | from 2026-01-01 | US-NVS5-008 |
| `ny.newhire.report_days` | 20 | from 2026-01-01 | US-NYS5-010 |
| `ny.payslip.items` | dates of work; names; employer address/phone; rates and basis; gross; deductions; allowances; net; regular and OT rates and hours (non-exempt); piece rates | from 2026-01-01 | US-NYS5-006 |
| `oh.newhire.report_days` | 20 | from 2013-09-29 | US-OHS5-014 |
| `oh.payslip.items` | name and address; employer name; gross and net; each addition and deduction; pay date and period; hours and rate (hourly) | from 2025-04-09 | US-OHP51-001 |
| `oh.report.ui.quarterly_due` | last day of month after quarter | from 2014-09-15 | US-OHS5-020 |
| `ok.newhire.report_days` | 20 | from 2015-11-01 | US-OKS5-007 |
| `ok.payslip.items` | brief itemized statement of all deductions with each payment | from 2022-11-01 | US-OKS5-003 |
| `or.newhire.report_days` | 20 | from 2024-01-01 | US-ORS5-016 |
| `or.payslip.items` | payment date; work dates; employee name; employer name, registry no., address, phone; rates; basis; gross; net; each deduction; allowances; regular/OT rates and hours; piece rates | from 2026-01-01 | US-ORS5-026 |
| `or.payslip.new_hire_explanation` | written explanation of earnings, deductions and all payroll codes; updated each January 1 | from 2026-01-01 | US-ORS5-022 |
| `pa.newhire.report_days` | 20 | from 2026-01-01 | US-PAS5-008 |
| `pa.payslip.items` | hours worked, rates, gross, allowances toward minimum wage, deductions, net | from 2026-01-01 | US-PAP51-001 |
| `pa.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2023-09-01 | US-PAS5-013 |
| `psl.ak.sick_leave.on_statement` | Sick leave used in the accrual year and sick leave balance on every statement (since 2025-09-25); a combined PTO plan satisfies it by showing PTO used and balance | from 2025-09-25 | US-AKS5-001 |
| `psl.ak.statement.content` | Written or electronic, each pay period: rate; gross and net; pay-period dates; federal income tax and Federal Insurance Contribution Act deductions; Alaska Employment Security Act contributions; board/lodging deductions; advances; straight-time and overtime hours; other authorised deductions; sick leave used in accrual year; sick leave balance | from 2025-09-25 | US-AKS5-001 |
| `psl.ak.statement.electronic_delivery` | Written or electronic; no separate consent rule | from 2025-09-25 | US-AKS5-001 |
| `psl.al.statement.scope` | none: no state pay-statement content statute; federal records rules apply | from 2025-10-02 | US-ALP52-001 |
| `psl.ar.statement.scope` | none: no itemised pay-statement statute; tipped employees get the tip-credit amount per hour in writing each time it changes (11 CAR 11) | from 2026-07-21 | US-ARP52-006 |
| `psl.az.sick_leave.on_statement` | Every regular paycheck or attachment: earned paid sick time available, used to date in the year, and pay received as sick time (A.R.S. 23-375(C)) | from 2017-07-01 | US-AZS5-011 |
| `psl.az.statement.scope` | Statement (no content list) required only when paying by direct deposit or payroll card (A.R.S. 23-351(E),(F)) | from 2026-01-01 | US-AZS5-001 |
| `psl.ca.sick_leave.on_statement` | Available paid sick leave on the wage statement or a separate writing each payday | from 2024-01-01 | US-CAS5-011 |
| `psl.ca.statement.content` | Lab. Code 226(a), semimonthly or each payment: gross; total hours (not for salaried exempt); piece units and rates; deductions; net; pay-period dates; name + last 4 SSN or employee ID; employer legal name and address; each hourly rate with hours | from 2023-10-13 | US-CAS5-005 |
| `psl.ca.statement.household_exclusion` | Section 226 does not apply to any employer of a person employed by the owner or occupant of a residential dwelling whose duties are incidental to the ownership, maintenance, or use of the dwelling, including the care and supervision of children, or whose duties are personal and not in the course of the trade, business, profession, or occupation of the owner or occupant | from 2023-10-13 | US-CAS5-005 |
| `psl.co.statement.comps_rule7` | Statement shows total pay, rate, tips, credits and time worked; kept 3 years | from 2026-01-01 to 2026-12-31 | US-COS5-001 |
| `psl.co.statement.content` | C.R.S. 8-4-103(4), at least monthly or each payment: gross; all withholdings and deductions; net; pay-period dates; employee name or SSN; employer name and address. COMPS Rule 7 adds rate, tips, credits and time worked | from 2025-08-06 | US-COP51-005 |
| `psl.ct.pay_code_guide.url_on_pay_record` | From 2026-10-01 (PA 26-12 sec. 38, 31-13a(c)): employers with 100+ employees publish a pay-code guide (overtime and common differentials, min 10 codes where applicable) in English, Spanish and other common languages; its Internet web site address appears on each record of hours and is given at hire; a payroll provider guide satisfies it | from 2026-10-01 | US-CTS5-028 |
| `psl.ct.statement.content` | Each payment: hours worked; gross pay with straight time and overtime separate; itemised deductions; net (hours and split not for OT-exempt) | from 2026-01-01 | US-CTP51-005 |
| `psl.ct.statement.electronic_delivery` | Electronic only with the employee explicit consent, a secure private way to access and print, and confidentiality safeguards (31-13a(b)) | from 2026-01-01 | US-CTS5-027 |
| `psl.dc.statement.content` | Each payment (32-1008(b)): date of payment; gross; deductions and additions with gratuities on a separate line; net; hours worked; tip declaration split cash/card; from 2026-01-01 a list of compensation sources beyond base wages and tips | from 2026-01-01 | US-DCS5-010 |
| `psl.de.statement.content` | Employers with more than 3 employees, each payment: wages due; pay period; total deductions each separately specified; total hours for hourly employees (19 Del. C. 1108) | from 2026-01-01 | US-DES5-002 |
| `psl.de.statement.electronic_delivery` | On the check, a separate slip, or electronically if the employee can retain it; employee may ask for paper | from 2026-01-01 | US-DES5-002 |
| `psl.de.statement.employer_threshold` | more than 3 employees | from 2026-01-01 | US-DES5-002 |
| `psl.fl.statement.scope` | none for general employers; labor pools only (448.24(2)(g),(h)): itemised deductions each payment and annual earnings summary by 1 February | from 2026-01-01 | US-FLL-002 |
| `psl.ga.statement.scope` | none: O.C.G.A. 34-7-2 has no statement duty; GDOL handbook has no pay-stub rule | from 2015-05-05 | US-GAP9L-001 |
| `psl.hi.statement.content` | HRS 387-6(c), 14 items: employee name; employer name; employer address and phone; total hours; regular and OT hours; straight-time pay; OT pay; other compensation incl. allowances toward minimum wage; gross; amount and purpose of each deduction; net; pay date; pay period; rates and basis incl. OT and piece rates with counts | from 2026-01-01 | US-HIP52-001 |
| `psl.hi.statement.electronic_delivery` | Electronic with the employee written authorization; direct deposit still requires a statement | from 2026-01-01 | US-HIS5-007 |
| `psl.ia.statement.content` | Each regular payday: hours worked, wages earned, deductions (91A.6(4)); itemised computation within 10 working days on request | from 2026-01-01 | US-IAP51-002 |
| `psl.ia.statement.electronic_delivery` | Mail, secure electronic means, at the workplace, or access to view; no separate consent | from 2026-01-01 | US-IAP51-002 |
| `psl.ia.statement.reach` | Employees employed in Iowa (work location, not residence) (91A.2(3),(4)) | from 2023-07-01 | US-IAS5-027 |
| `psl.id.statement.scope` | deductions_only: written statement of deductions for each pay period with deductions (45-609(2)) | from 2026-01-01 | US-IDP51-002 |
| `psl.il.statement.content` | Pay stub each pay period with itemized deductions (820 ILCS 115/10 as amended by P.A. 103-953); payroll-card payees also get hours, rate and deductions | from 2025-01-01 | US-ILS5-024 |
| `psl.il.statement.electronic_access` | Stubs kept 3 years; copies within 21 days on request (max twice per 12 months; former employees for one year); if electronic stubs become inaccessible after separation, offer prior-year stubs by the final pay period and record the offer | from 2025-01-01 | US-ILS5-024 |
| `psl.in.statement.content` | Each pay period at least hours worked, wages paid, deductions (IC 22-2-2-8(a)) | from 2026-01-01 | US-INP6-001 |
| `psl.in.statement.scope` | Duty binds employers subject to IC 22-2-2 = 2+ employees NOT subject to the FLSA minimum wage (IC 22-2-2-3); literal reading excludes FLSA-covered employers | from 2007-06-30 | US-INS5-001 |
| `psl.ks.statement.scope` | on_request: itemized statement of deductions on request for each pay period with deductions (K.S.A. 44-320(d)) | from 1973-07-01 | US-KSP52-001 |
| `psl.ky.statement.content` | Employers with 10+ employees that make deductions: each payment, paper or electronic statement of each deduction and its purpose; electronic requires access to a computer and printer (section 337.070) | from 2017-06-29 | US-KYP8-001 |
| `psl.ky.statement.employer_threshold` | 10 | from 2017-06-29 | US-KYP8-001 |
| `psl.la.statement.scope` | The text of R.S. 23:631 (payment after discharge or resignation) carries no pay-statement duty | from 2026-01-01 | US-LAR3-002 |
| `psl.ma.statement.content` | Each payment (c.149 s.148): employer name; employee name; date; hours worked; hourly rate; deductions or increases for the period | from 2026-01-01 | US-MAP51-008 |
| `psl.md.sick_leave.on_statement` | Available earned sick and safe leave balance each time wages are paid; an online balance system satisfies it (LE 3-1305(f)) | from 2018-02-11 | US-MDS5-013 |
| `psl.md.statement.content` | LE 3-504: employer name, address, phone; pay date and period; hours (unless exempt); rates; gross and net; each deduction by name and amount; other bases of pay; written or online | from 2026-01-01 | US-MDP51-005 |
| `psl.md.statement.tip_credit` | Tip Credit Wage Statement for restaurants | from 2026-01-01 | US-MDS5-007 |
| `psl.me.statement.content` | Each payment: date of the pay period, hours, total earnings, itemized deductions (Title 26 section 665, subsection 1) | from 2026-01-01 | US-MES5-006 |
| `psl.me.statement.electronic_delivery` | Electronic allowed only with ready access and printing at no cost; same record due when a direct deposit is made | from 2026-01-01 | US-MES5-006 |
| `psl.mi.statement.content` | At payment (MCL 408.479(2)): hours worked, gross, pay-period identification, separate itemisation of deductions; comp time earned or paid | from 1979-01-04 | US-MIS5-009 |
| `psl.mn.sick_leave.on_statement` | ESST hours available and used each pay period, on or attached to the statement or via an electronic system | from 2024-01-01 | US-MNS5-011 |
| `psl.mn.statement.content` | Earnings statement at the end of each pay period, in writing or by electronic means. Under 181.032(b) it must include: (1) the name of the employee; (2) the rate or rates of pay and basis thereof, including whether the employee is paid by hour, shift, day, week, salary, piece, commission, or other method; (3) allowances, if any, claimed pursuant to permitted meals and lodging; (4) the total number of hours worked by the employee unless exempt from chapter 177; (5) the total amount of gross pay earned by the employee during that period; (6) a list of deductions made from the employee's pay; (7) any amount deducted by the employer under section 268B.14, subdivision 3, and the amount paid by the employer based on the employee's wages under section 268B.14, subdivision 1; (8) the net amount of pay after all deductions are made; (9) the date on which the pay period ends; (10) the legal name of the employer and the operating name of the employer if different from the legal name; (11) the physical address of the employer's main office or principal place of business, and a mailing address if different; and (12) the telephone number of the employer | from 2026-01-01 | US-MNP6-001 |
| `psl.mn.statement.electronic_delivery` | Electronic requires access to an employer computer during work hours and statements kept available 3 years | from 2026-01-01 | US-MNP6-001 |
| `psl.mo.statement.scope` | deductions_only: statement of total deductions at least monthly (290.080) | from 1955-08-28 | US-MOP52-002 |
| `psl.ms.statement.scope` | The Mississippi Department of Employment Security required-posters page lists no pay-statement notice | from 2026-01-01 | US-MSP9L-001 |
| `psl.mt.statement.content` | Every payment: itemized statement of state and federal income tax, social security and other deductions with amounts; statement saying none if nothing deducted (MCA 39-3-101) | from 2026-01-01 | US-MTP51-006 |
| `psl.nc.statement.electronic_delivery` | In writing, printable e-mail or any means the employee can keep; no separate consent | from 1999-04-01 | US-NCS5-024 |
| `psl.nc.statement.scope` | deductions_only: itemized statement of deductions each pay period with deductions (G.S. 95-25.13), plus hire wage notice | from 2026-01-01 | US-NCW1B-003 |
| `psl.nd.statement.content` | Each pay period a check stub or pay voucher: hours worked, rate, required state and federal deductions, authorized deductions (46-02-07-02, recordkeeping item 10) | from 2012-10-01 | US-NDS5-007 |
| `psl.ne.statement.content` | Each regular payday: employer identity, hours paid, wages earned, deductions (48-1230(2)); hours not required for FLSA-exempt unless OT/hours-based | from 2026-01-01 | US-NEP51-004 |
| `psl.nh.statement.scope` | deductions_only: statement of deductions each pay period with a deduction (RSA 275:49 IV); written monthly accounting for 275:48 I(d) deductions | from 2026-01-01 | US-NHP51-001 |
| `psl.nj.statement.content` | Statement of deductions each pay period with deductions; employers with 10+ employees add gross, net, rate and hours where relevant (34:11-4.6(c)) | from 2026-01-01 | US-NJP8-001 |
| `psl.nj.statement.electronic_delivery` | Electronic allowed unless the employee asks for paper | from 2026-01-01 | US-NJP8-001 |
| `psl.nm.sick_leave.on_statement` | Year-to-date earned sick leave accrued and used, at least quarterly, on the earnings statement or electronically | from 2022-07-01 | US-NMS5-002 |
| `psl.nm.statement.content` | Written receipt each payday: employer identity; gross; hours worked; total wages and benefits earned; itemized deductions (50-4-2(B)) | from 2026-01-01 | US-NMP8-001 |
| `psl.nv.statement.content` | Itemized list of deductions at each payment (NRS 608.110(2)) | from 2026-01-01 | US-NVR3-001 |
| `psl.ny.statement.content` | Labor Law 195(3), every payment: dates of work; names; employer address and phone; rates and basis; gross; deductions; allowances toward minimum wage; net; non-exempt: regular and OT rates and hours; piece rates and counts | from 2020-10-02 | US-NYS5-006 |
| `psl.oh.statement.content` | ORC 4113.14 (from 2025-04-09), each pay period written or electronic: employee name and address; employer name; gross and net; amount and purpose of each addition and deduction; pay date and period; hourly employees hours and rate | from 2025-04-09 | US-OHP51-001 |
| `psl.ok.statement.scope` | deductions_only: brief itemized statement of all deductions with each payment (40 O.S. 165.2) | from 2022-11-01 | US-OKS5-003 |
| `psl.or.statement.content` | ORS 652.610(1)(b): payment date; dates of work; employee name; employer name and registry/ID number; employer address and phone; rates; basis; gross; net; each deduction with amount and purpose; allowances toward minimum wage; non-exempt regular and OT rates, hours and pay; piece rates and counts | from 2026-01-01 | US-ORS5-026 |
| `psl.or.statement.electronic_delivery` | Electronic only with the employee express agreement and ability to print or store on receipt (652.610(1)(c)) | from 2026-01-01 | US-ORS5-026 |
| `psl.pa.statement.content` | Every payment: hours worked, rates, gross, allowances toward minimum wage, deductions, net (34 Pa. Code 231.36) | from 2026-01-01 | US-PAP51-001 |
| `psl.ri.statement.content` | Every regular payday: hours worked (except 28-12-4.3 exempt), every deduction with explanation; commercial construction also regular hourly rate (28-14-2.1); electronic allowed, free printed copy on written request | from 2026-01-01 | US-RIP51-002 |
| `psl.sc.statement.content` | Itemized statement of gross pay and deductions each pay period (41-10-30(C)); direct deposit: statement of earnings and withholdings (41-10-40(B)) | from 2026-01-01 | US-SCP52-006 |
| `psl.sc.statement.exemptions` | Section 41-10-30 (notification to employees) does not apply to domestic labour in private homes or to employers with fewer than five employees at all times in the preceding twelve months (41-10-20) | from 2026-01-01 | US-SCP52-006 |
| `psl.sd.statement.scope` | none: no SD statute requires a pay statement (Title 60 full-text scan) | from 2026-01-01 | US-SDS5-001 |
| `psl.tn.statement.scope` | none: no TN itemised pay-statement statute located; federal records rules | from 2026-01-01 | US-TNS5-001 |
| `psl.tx.statement.scope` | non_flsa_only: Labor Code 62.003 earnings statement (name, rate, gross, each deduction and purpose, net, hours or units; signed by employer or agent) applies only to employees not covered by the FLSA (62.151); best practice for everyone else | from 1993-09-01 | US-TXS5-003 |
| `psl.ut.statement.format` | All lawful offsets itemized on a statement or detachable check stub (R610-3-20) | from 2012-04-16 | US-UTS5-012 |
| `psl.ut.statement.scope` | deductions_only: statement of each deduction on each regular payday (34-28-3(4)); construction-trade licensees full statement (34-28-3(5)) | from 2014-05-13 | US-UTP6-001 |
| `psl.va.statement.content` | Each regular pay date, paystub or online accounting: employer name and address; hours (hourly and salaried below the FLSA level); rate; gross; amount and purpose of each deduction; enough detail to work out gross and net | from 2026-07-01 | US-VAS5-003 |
| `psl.vt.statement.content` | Detailed written statement with each weekly pay: gross, hours, hourly rate, itemised deductions incl. meals | from 2009-01-01 | US-VTP9-001 |
| `psl.w2.box14.ca_sdi` | CASDI (or VPDI) in Box 14; CA PIT wages Box 16; CA PIT withheld Box 17 | from 2026-01-01 to 2026-12-31 | US-CAS5-018 |
| `psl.wa.sick_leave.on_statement` | At least monthly: paid sick leave accrued, used and available; may be on the regular pay statement (WAC 296-128-755(2)) | from 2026-01-01 | US-WAS5-005 |
| `psl.wa.statement.content` | Every payday, separate from the paycheck: hours or days worked, rates, gross, all deductions, pay period, payment date (WAC 296-126-040) | from 2026-01-01 | US-WAS5-004 |
| `psl.wa.statement.electronic_delivery` | Electronic if the employee can receive and copy it on payday; otherwise paper | from 2026-01-01 | US-WAS5-004 |
| `psl.wi.statement.content` | Hours worked, rate, amount and reason for each deduction, on the check, envelope or accompanying paper; coding system allowed (103.457; DWD 272.10) | from 2026-10-01 | US-WIP52-001 |
| `psl.wv.statement.content` | Scheduled payday itemized statement: hourly rate or salary; hours paid; OT rate; bonus or incentive pay; itemized deductions (42 CSR 5 s.7.3, sunset 2029-07-01) | from 2019-07-01 to 2029-07-01 | US-WVS5-008 |
| `psl.wy.statement.scope` | deductions_only: detachable part of the check or attached slip with an itemized statement of all deductions (27-4-101(b)); agricultural operations exempt | from 2026-01-01 | US-WYP51-005 |
| `ri.newhire.report_days` | 14 | from 1997-10-01 | US-RIS5-010 |
| `ri.payslip.items` | hours worked (non-exempt), every deduction with explanation; regular hourly rate in commercial construction | from 2026-01-01 | US-RIP51-002 |
| `ri.report.w2.efile_threshold` | 25 | from 2026-01-01 to 2026-12-31 | US-RIS5-018 |
| `rspec.fed.form940.due` | TY2025 rule applies until the 2026 Form 940 instructions are published: Form 940 due the last day of the month after the year ends (February 1, 2027 for TY2026; February 10, 2027 if all FUTA tax was deposited when due, per the 2025 instructions' rule). Requirement: re-verify against the Instructions for Form 940 (2026) when the IRS publishes them; the live i940.pdf was still the 2025 edition on 2026-11-04. | from 2026-02-11 | US-FEDS5-031 |
| `rspec.fed.form940.due` | TY2025 rule: Form 940 for 2025 due February 2, 2026 (February 10, 2026 if all FUTA tax was deposited when due) (TY2025 rule, re-verify on the 2026 instructions) | from 2026-01-01 to 2026-02-10 | US-FEDS5-031 |
| `rspec.fed.futa.credit_reduction.states` | 2025 (final): CA 0.012 (1.2%); VI 0.045 (4.5%); no other state | from 2025-01-01 to 2026-02-10 | US-FEDS6-009 |
| `rspec.me.wh_return.form` | 941ME quarterly, last day of month after quarter, electronic mandatory even when nothing to report | from 2026-04-14 | US-MEP52-002 |
| `sc.newhire.report_days` | 20 | from 1998-10-01 | US-SCS5-011 |
| `sc.payslip.items` | itemized gross pay and deductions each pay period | from 2026-01-01 | US-SCP52-006 |
| `sc.report.ui.quarterly_due` | last day of month after quarter | from 2023-10-25 | US-SCS5-006 |
| `sd.newhire.report_days` | 20 | from 2026-01-01 | US-SDS5-007 |
| `sd.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 (received) | from 2026-01-01 | US-SDS5-013 |
| `sir.dc.withholding.agent_authorization` | OTR D-2848 | from 2026-09-16 | US-DCP51-014 |
| `sir.fed.reporting_agent.tech_spec` | Pub. 1474 (Rev. 4-2026): reporting agent = accounting service, franchiser, bank, service bureau or other payroll-services entity; agent list additions/deletions electronic above 100 submissions a week via SLFT B2B; deposits via EFTPS or FTA | from 2026-04-01 | US-FIL-001 |
| `sir.fed.third_party_payer.rules` | Pub. 15 (2026) third-party payer arrangements (reporting agents, sec. 3504 agents, CPEOs) - liability allocation per arrangement | from 2026-01-01 | US-FEDP51-002 |
| `sir.fed.w2.format` | EFW2 Publication 42-007 (W-2) / 42-014 (W-2c) via SSA Business Services Online | from 2026-01-01 | US-FIL-002 |
| `sir.nj.withholding.agent_authorization` | M-5008-R Appointment of Taxpayer Representative (6/26) | from 2026-06-09 | US-NJR3-004 |
| `sir.tx.ui.agent_authorization` | Form C-42 Written Authorization to Represent Employing Unit | from 2026-03-13 | US-TXP52-008 |
| `sir.wi.provider_registration` | Payroll service providers must register and test their software with DOR | from 2026-01-01 | US-WIS5-016 |
| `tn.newhire.report_days` | 20 | from 2026-01-01 | US-TNS5-008 |
| `tn.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2025-05-27 | US-TNS5-005 |
| `tx.newhire.report_days` | 20 | from 2026-01-01 | US-TXS5-017 |
| `tx.payslip.content.non_flsa` | signed statement: name, rate, gross, each deduction and purpose, net, hours or units | from 1993-09-01 | US-TXS5-003 |
| `ut.newhire.report_days` | 20 | from 2026-01-01 | US-UTS5-003 |
| `ut.payslip.items` | statement of total amount of each deduction each regular payday; construction licensees full statement | from 2014-05-13 | US-UTP6-001 |
| `ut.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2026-01-01 | US-UTS5-004 |
| `va.newhire.report_days` | 20 | from 2020-07-01 | US-VAS5-006 |
| `va.payslip.items` | employer name/address; hours (hourly and below-FLSA-salary); rate; gross; each deduction amount and purpose | from 2026-07-01 | US-VAS5-003 |
| `va.report.ui.quarterly_due` | last day of month after quarter | from 2026-01-01 | US-VAS5-014 |
| `vt.newhire.report_days` | 10 | from 2025-09-01 | US-VTS5-014 |
| `vt.payslip.items` | gross pay, hours worked, hourly rate, all deductions itemised | from 2009-01-01 | US-VTP9-001 |
| `vt.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2026-01-01 | US-VTS5-007 |
| `wa.newhire.report_days` | 20 | from 2026-01-01 | US-WAS5-018 |
| `wa.payslip.items` | pay basis (hours/days), rates, gross, all deductions, pay period dates, payment date; separate from paycheck | from 2026-01-01 | US-WAS5-004 |
| `wa.report.pfml_ltc.fields` | Combined Paid Leave + WA Cares quarterly report; per employee: SSN or ITIN, last and first name (middle initial optional), hours associated with wages paid (rounded up to a whole number; salaried full-time 40 h/week; no hours for leave cash-outs or severance), wages paid in the quarter excluding tips, WA Cares exemption status, date of birth; employer totals of Paid Leave and WA Cares premiums withheld | from 2026-06-26 | US-WAB5-003 |
| `wa.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2026-01-01 | US-WAS5-013 |
| `wi.newhire.report_days` | 20 | from 2026-03-16 | US-WIS5-013 |
| `wi.payslip.items` | hours worked, rate, amount and reason for each deduction | from 2026-01-01 | US-WIP52-001 |
| `wi.report.ui.quarterly_due` | end of month after quarter | from 2026-03-16 | US-WIS5-013 |
| `wi.report.w2.efile_threshold` | 10 | from 2026-01-01 | US-WIS5-012 |
| `wv.newhire.report_days` | 14 | from 2024-06-01 | US-WVS5-016 |
| `wv.payslip.items` | hourly rate or salary, hours paid, overtime rate, bonus/incentive, itemized deductions | from 2019-07-01 to 2029-07-01 | US-WVS5-008 |
| `wv.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2026-01-01 | US-WVUI-001 |
| `wy.newhire.report_days` | 20 | from 2026-05-08 | US-WYS5-006 |
| `wy.payslip.items` | itemized written statement of all deductions on detachable part of check/voucher or attached slip | from 2026-01-01 | US-WYP51-005 |
| `wy.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | from 2026-01-01 | US-WYS5-009 |
