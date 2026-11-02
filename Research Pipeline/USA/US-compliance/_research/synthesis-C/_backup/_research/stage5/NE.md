# Stage 5 - NE (Nebraska) - 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Scope: `_prompts/stage5-brief.md`, JUR = NE. The mandate block US-MQ-49 (answered at attempt 3) is reused here, not researched again.

**Budget.** Declared 60 fetches and 2 h, with a working ceiling of 45. Used about 34 fetches (30 Wayback/curl, 4 searches) in roughly 1 h.

**Access.** The VPN was off (exit IP in Brazil). nebraskalegislature.gov, revenue.nebraska.gov and dol.nebraska.gov did not resolve from this machine (curl exit 6). Every new file is therefore a Wayback `id_` copy of the official URL. The snapshot timestamp is in each register row.

**Register shard.** `00-official-sources/_register-shards/S5-NE.csv` holds rows US-NES5-001 to US-NES5-019:
- 17 are `active`.
- 2 are `partial`: US-NES5-008 (pre-LB415 definitions, kept only for the pay rate in 48-3802(7)) and US-NES5-015 (child-support employer sections, with the fee and priority sections not read).

**Files.** New files are in `00-official-sources/ccg-sources/NE/` (statute pages, the LB415 slip law, the DOR W-2 page and guidance, 21EFW2). They total about 0.9 MB, and no file is over 5 MB.

**Reused active rows (not fetched again).**
- US-NE-P5-1-001: Circular EN 2026, W-4N, allowances, supplemental tax.
- US-NE-P5-1-002: nonresident 7-day rule and convenience rule.
- US-NE-P5-1-003: UI 2026 rates.
- US-NE-P5-1-004: 48-1230(2) wage statement and POA.
- US-NE-P5-2-001: no SDI/PFML/levy.
- US-NE-P5-2-002: no prevailing-wage statute.
- US-NE-P5-2-003: no official calculator.
- US-NEL-001, US-NEP9L-001/-002, US-NEP9V-001: language and levies.
- US-NE-002: the 2027 Circular EN exists, but there is still no local file (see ACCESS gaps).

## 1. labour_code
- **Minimum wage 2026**: 15.00/h from 2026-01-01 to 2026-12-31 (Neb. Rev. Stat. 48-1203(1)(e)). [US-NES5-001, A.1]
- **2027 and later: LB258 (Laws 2026, in force 2026-07-18).** LB258 replaced the CPI indexation of Initiative 433 with a **fixed +1.75%** each 1 January from 2027-01-01. NDOL must publish the next rate by 15 October, starting 2026-10-15 (48-1203(2)).
  - Derived 2027 rate: 15.00 x 1.0175 = **15.2625**.
  - The statute gives no rounding rule for the adult rate. Tier-B leads say NDOL published 15.26, but no NDOL publication was read (NDOL press-release list snapshot of 2026-08-14 has no 2027 release). See Open questions. [US-NES5-001, derived arithmetically]
- **Youth minimum wage** (new, LB258): 13.50/h for ages 14-15 who are not emancipated.
  - It rises +1.5% every fifth year from 2030-01-01, rounded to the cent (48-1203(5)). [US-NES5-001]
- **Tipped employees**: cash wage 2.13/h. Wages plus tips must reach the minimum, and the employer bears the burden of proof (48-1203(3)). [US-NES5-001]
- **Student-learners**: at least 75% of the applicable minimum (48-1203(4)). [US-NES5-001]
- **Training wage**: at least 75% of the **federal** minimum.
  - It applies to new employees under 20 (not seasonal or migrant) for 90 days, plus 90 more days during Commissioner-approved OJT.
  - At most one-fourth of the hours paid may be at this rate (48-1203.01).
  - The snapshot is from 2026-01, before LB258; LB258's source line amends 48-1203 only. [US-NES5-002]
- **Coverage of the Wage and Hour Act**: employers with **4 or more employees** at any one time.
  - Excluded: agriculture, baby-sitters in private homes, executive/administrative/professional staff, all government employers, and family employment (48-1202). [US-NES5-003]
  - Outside the Act, the federal FLSA applies.
- **Overtime**: no state overtime provision appears in the Wage and Hour Act sections read (48-1202, 48-1203, 48-1203.01). FLSA overtime applies. Confidence 80%: the full article 12 index was not read.
- **Pay frequency and paydays**:
  - Pay on regular paydays designated by the employer or agreed with the employee.
  - 30 days' written notice before changing paydays.
  - **No statutory minimum frequency** (48-1230(1)). [US-NES5-006]
- **Deductions**: only when required or permitted by state or federal law, by court order, or by **written agreement** with the employee (48-1230(1)). [US-NES5-006]
- **Payment method (paycards)**:
  - The 15 U.S.C. 1693k compulsory-use bar applies.
  - At least one free withdrawal per pay period (no more than once a week) up to net pay.
  - No card fees may be passed to the employee (48-1230(3)). [US-NES5-006]
  - Direct deposit: no state consent text was read beyond 1693k (federal Reg E).
- **Local minimum wages**: none located. The Circular EN and the DOR tax list show no local wage layer, and no Omaha or Lincoln ordinance came up in the sources read. Confidence 70%: preemption was not verified.
- Confidence: high (A.1) for the rates and the 48-1230 rules.

## 2. income_tax
- **Method (2026)**: Circular EN 2026 (Rev. 11-2025), percentage method or wage-bracket tables. [US-NE-P5-1-001, US-NES5-010]
  - Nebraska taxable wages = federal taxable wages.
  - Form **W-4N**. A post-2019 federal W-4 without a W-4N is treated as single with zero allowances.
  - Allowance 2,440/year (weekly 46.92 ... monthly 203.33).
- **Percentage method, annual table** (withholding rates 2.26 / 3.22 / 4.21 / 4.35 / 4.48 / 4.60%): [US-NES5-010]
  - Single: thresholds 3,430 / 6,710 / 21,810 / 31,610 / 40,130 / 75,370.
  - Married: thresholds 8,190 / 13,010 / 32,400 / 50,400 / 62,530 / 82,920.
  - Cumulative amounts re-derived in Python:
    - single 74.13 / 560.35 / 972.93 / 1,343.55 / 2,922.30, all exact;
    - married 108.93 / 733.29 / 1,491.09 / 2,018.74 (published **2,018.75**: DOR rounds the cumulative 2,018.745 half-up) / 2,932.22.
- **Statutory assessment rates** (77-2715.03): 2.46% and 3.51% in the lower brackets. [US-NES5-018]
  - Top two rates: 4.55% for tax year 2026, **3.99% from 2027** (LB754, 2023).
  - Brackets are CPI-indexed.
  - The withholding table rates are DOR-designed and are not the statutory rates. Do not mix the two.
- **Minimum withholding**: employers with **more than 24 employees** must withhold at least **1.5%** of taxable wages unless the employee documents a lower liability. [US-NES5-010, US-NE-P5-2-001]
- **Supplemental wages**: aggregate method, or an optional flat **3.5%**. [US-NE-P5-1-001]
- **Rounding**: the Circular EN tables are in cents. No whole-dollar rounding rule was stated.
- **Exempt status**: a new W-4N is required by 15 February each year. [US-NES5-010]
- **Local income tax**: none. The Circular EN has no local layer, and the DOR list has "Occupation Taxes" only as local **business** taxes. [US-NE-P5-1-001, US-NEP9V-001]
- **Reciprocity**: none. [US-NE-P5-1-002; MULTI line 66]
- **Nonresidents** (LB1023, from tax year 2025): [US-NE-P5-1-002, US-NES5-010]
  - **7 employment-duty-day** threshold.
  - Conference/training rule: 7 days or fewer and 5,000 or less in NE wages.
  - **Convenience rule** (77-2733(8)(c)).
  - Form 9N allocation percentage.
- **Non-employee nonresident personal services**: 4% of the net payment under 28,000, 6% at 28,000 or more (W-4NA/W-4NB). [US-NES5-010]

## 3. social_security (SUI / SDI / PFML / levies)
- **SUI 2026**: [US-NE-P5-1-003, US-NES5-011]
  - Wage base **9,000** (categories 1-19) and **24,000** (category 20, 5.40%).
  - New employer **1.25%**, or **5.40%** for construction.
  - Range 0.00%-5.40%; average (category 12) 0.55%.
- **Contributions**: fully employer-paid, no employee contribution (48-648(1)).
- **SUIT** is a 0-20% slice of the combined tax (48-649.01(3)). It is not a separate rate line on payroll.
- **Wages from other States count toward the base**: wages paid for services in another State, or paid by a predecessor, count toward the 9,000 (48-648.02). This answers MULTI-OQ-2 for NE. [US-NES5-011]
- **SDI/TDI/PFML/transit/workforce levy**: none. [US-NE-P5-2-001, US-NEP9V-001]
- **Coverage for domestic and agricultural employers** (48-604(4)): [US-NES5-011]
  - domestic: 1,000 cash wages in a quarter;
  - agricultural: 10 workers in 20 weeks, or 20,000 in a quarter.
- **UI-excluded services** (48-604): ministers and churches, family employment, students employed by their school, and others. [US-NES5-019]
- Confidence: 90%.

## 4. payslip_statute
- **Content**: on each regular payday, a wage statement showing employer identity, hours paid, wages earned and deductions (48-1230(2)). [US-NE-P5-1-004, US-NEL-001]
  - Hours are not required for FLSA-exempt employees unless they are paid overtime or hours-based pay.
- **Delivery**: by mail, electronically, or at the workplace during work hours for all shifts. No consent requirement is stated.
- **Language**: no language rule (US-NEL-001).
- **Retention**: no NE-specific retention period was read. Default to the federal rule (29 CFR 516, FED unit). The NE UI and wage-hour record-keeping periods were not read. See Open questions.
- **SSN on the payslip**: see domain 12.

## 5. reporting_instruments
| Filing | Rule | register_id |
|---|---|---|
| Withholding licence | Required before paying NE wages. Registration form name (Form 20) not read | US-NES5-010 |
| Deposits | Form 501N / EFT by the 15th of the next month when more than 500 is withheld in month 1 or 2 of the quarter. EFT is mandatory if prior-year payments exceeded 5,000 | US-NES5-010 |
| Form 941N | Quarterly, by the last day of the month after the quarter (Apr 30, Jul 31, Oct 31, Jan 31). Licensed annual filers file once by Jan 31. Filed even with zero withholding | US-NES5-010 |
| Form W-3N + state W-2/1099 | By 31 January (next business day if that falls on a weekend or holiday). More than 50 forms must be e-filed via NebFile for Business. Format: **SSA EFW2 with an NE RS record** (state code 31, taxing entity code "31") and an RV total record (21EFW2, Nov 2025). Magnetic media is refused | US-NES5-017, US-NES5-016 |
| W-2 box 15 | "NE" + the 4-8 digit Nebraska ID exactly as shown on the 941N/W-3N | US-NES5-016 |
| UI registration | UI Form 1 via NEworks (48-612) | US-NES5-011 |
| UI Combined Tax Report + Wage Report | Quarterly, due Apr 30 / Jul 31 / Oct 31 / Jan 31. Wage report: SSN, last name + initials, gross wages; optional hours and job title. NEworks online or FTP (spec at dol.nebraska.gov/UITax, not fetched). E-filing expected above 100,000 payroll. Late-report penalty 0.1% of gross wages (min 25, max 200) | US-NES5-011 |
| New hire | DHHS (State Directory of New Hires): within 20 days, or two monthly electronic transmissions 12-16 days apart. Fields: employee name, address, SSN, hire/rehire date; employer name, address, FEIN. A W-4 copy is accepted | US-NES5-014 |
| POA | DOR Form 33; NDOL UI POA | US-NE-P5-1-004 |

## 6. leave
- **Paid sick time: Healthy Families and Workplaces Act** (Initiative 436, 2024, as amended by **LB415**, in force 2025-09-03; obligations from 2025-10-01).
  - **Coverage**: employers with **11 or more employees**. "Small business" means 11-19 employees.
  - **Excluded employees**: [US-NES5-009]
    - owner-operators and independent contractors;
    - anyone working **fewer than 80 hours in NE in the calendar year**;
    - seasonal or temporary agricultural workers;
    - RUIA railroad workers;
    - workers **under 16**;
    - State and political-subdivision employers.
  - **Accrual**: begins after 80 consecutive hours, at **1 h per 30 h worked**. [US-NES5-007]
    - Cap on earning and using: **40 h** a year (small business) or **56 h** (others).
    - Exempt employees are deemed to work 40 h a week.
    - Front-loading is allowed.
    - Carryover is required, or the employer pays out the balance and front-loads.
    - A rehire within 12 months has the balance reinstated.
    - **No payout at separation** (48-3803(10)).
  - **Pay rate**: the same hourly rate and benefits as hours worked, never below the 48-1203 minimum (48-3802(7)). LB415 did not amend this paragraph in the slip text read. [US-NES5-008]
  - Use in hourly increments or the payroll's smallest increment. Documentation may be required after 3 consecutive days. [US-NES5-007]
  - **Multistate (MULTI-OQ-4)**: the employee must work at least 80 hours in NE in the calendar year to be covered. [US-NES5-009]
- **PFML**: none. No benefit-side interaction. [US-NE-P5-2-001]
- **Other paid leave with pay impact**: none read. Jury-duty and voting-leave statutes were not fetched (Open questions).
- Confidence: 90% for paid sick time (A.1 statute plus slip law).

## 7. termination
- **Final pay** (private employers): unpaid wages are due on the **next regular payday or within two weeks** of termination, **whichever is sooner**. The same rule applies to discharge and resignation (48-1230(4)(a)). [US-NES5-006]
  - Political subdivisions: within two weeks of the next governing-body meeting.
- **Commissions**: due on the next regular payday after the customer pays, with periodic accounting (48-1230.01). [US-NES5-005]
- **Vacation**: **earned but unused vacation is wages due at separation**. Other paid leave (including sick time) is due only by agreement (48-1229(6)). [US-NES5-004] Sick-time balance: no payout (48-3803(10)). [US-NES5-007]
- **UI separation**: NDOL requests separation information through SIDES, with a reply due within 10 days. No mandatory separation notice to the employee was found in the guide; the UI benefit-rights poster is required (US-NEP9L-001). [US-NES5-011]
- No state WARN act was located (not searched in depth).

## 8. benefits_in_kind
- Nebraska withholding wages = **federal taxable wages**, so the federal exclusions (401(k), section 125, HSA, transit, group-term life) carry over at withholding. [US-NE-P5-1-001] No departure was found in the Circular EN.
- UI wages include 401(k) deferrals and board/lodging at Commissioner values (NAC 220 ch. 2). [US-NES5-019]

## 9. deductions_garnishments
- **Wage deductions**: written agreement, law or court order (48-1230(1)). [US-NES5-006]
- **Ordinary garnishment**: the lesser of 25% of disposable earnings or the amount above 30 x the federal minimum wage. If the debtor is **head of a family**, the limit is **15%**. [US-NES5-012]
  - The limits do not apply to support orders, Chapter 13 orders or tax debts.
  - No discharge for one garnishment (25-1558).
  - This is stricter than the CCPA for heads of family.
- **Child-support income withholding**: [US-NES5-015 partial]
  - Anti-retaliation fine of up to 500 per violation (43-1725).
  - The notice stops binding the employer 30 days after separation; the employer returns it with forwarding information (43-1726).
  - The employer processing fee and priority rules (43-1720 to 43-1724) were not read.
- **State tax levies**: not read.

## 10. collective_agreements / prevailing wage
- No state prevailing-wage rate statute exists. Chapter 73 only requires a fair-labour-standards statement in public-works contracts, and Davis-Bacon applies by contract. [US-NE-P5-2-002]
- Public agencies withhold final settlement from contractors until NDOL certifies their UI status (48-657(4)). [US-NES5-011]

## 11. indexation
| Item | Mechanism | Publication | register_id |
|---|---|---|---|
| Minimum wage | Fixed +1.75% each 1 Jan from 2027 (LB258) | NDOL by 15 Oct | US-NES5-001 |
| Youth minimum wage | +1.5% every 5 years from 2030 | NDOL | US-NES5-001 |
| PIT brackets | CPI-U (12 months to 31 Aug), rounded to 10 | DOR rate schedules / Circular EN | US-NES5-018 |
| Withholding allowance and tables | Annual | Circular EN (2027 edition Rev. 8-2026 exists) | US-NE-002 |
| UI wage base | Fixed 9,000 / 24,000, not indexed | NDOL rate guide | US-NE-P5-1-003 |

## 12. data_protection
- Employers may not display more than the **last 4 SSN digits** publicly or to coworkers (48-237). [US-NES5-013]
  - They may not require more than 4 digits to be sent over the Internet without security, to access a website without a password, or as an employee number.
  - Full SSN use is allowed for legal compliance and internal administration.
  - Payslip implication: no full SSN on a statement that coworkers can see. The statute does not expressly mandate truncation on the pay statement itself.

## 13. live_legal_change (2026-01-01 to 2026-11-02)
- **LB258 (2026)**, in force 2026-07-18: minimum-wage indexation is now a fixed 1.75%, and a youth minimum wage was created. Status: enacted. Level: wage floor. [US-NES5-001]
- **LB754 (2023)**: top PIT rates fall to 3.99% from tax year 2027. Status: enacted. Level: assessment, plus the 2027 Circular EN tables at withholding. [US-NES5-018]
- **LB415 (2025)**: paid-sick-time coverage narrowed (11+ employees). Status: enacted, in force 2025-09-03. Level: leave accrual. [US-NES5-009]
- **LB1023 (2024)**: nonresident 7-day and convenience rules from tax year 2025. Status: in force. Level: withholding/sourcing. [US-NE-P5-1-002]
- No bulletin sweep was possible on the agency hosts (DNS); this is a partial sweep from the statute source notes.

## Special populations
| Population | NE rule | register_id |
|---|---|---|
| Domestic/household | UI coverage at 1,000 cash wages in a quarter. Baby-sitters in private homes are outside the Wage and Hour Act (FLSA governs). Paid sick time only with an employer of 11+ | US-NES5-011, US-NES5-003, US-NES5-009 |
| Agricultural | Outside the Wage and Hour Act (federal FLSA only). UI at 10 workers in 20 weeks or 20,000 in a quarter. Seasonal/temporary agricultural workers are excluded from paid sick time | US-NES5-003, US-NES5-011, US-NES5-009 |
| Minors | Youth minimum wage 13.50 (ages 14-15). Training wage 75% of the federal minimum (under 20, 90 days). Under 16 excluded from paid sick time. Newspaper delivery under 18 is UI-exempt. Child-labour hours statutes not read | US-NES5-001, US-NES5-002, US-NES5-009, US-NES5-019 |
| Tipped | Cash wage 2.13, with a tip make-up to the minimum | US-NES5-001 |
| Clergy/religious | UI-exempt (ministers, church service). Withholding follows federal taxable wages | US-NES5-019, US-NE-P5-1-001 |
| Students | Student-learners 75% of the minimum. Students working for their school, and academic-credit work, are UI-exempt | US-NES5-001, US-NES5-019 |
| Nonresident aliens | Wages follow federal taxable wages. Treaty-exempt NRA personal-services payments: no NE withholding with a statement | US-NES5-010 |
| Statutory employees | No state rule beyond federal (Circular EN read) | US-NE-P5-1-001 |
| Government employees | Outside the Wage and Hour Act and the paid-sick-time Act. Separate final-pay timing for political subdivisions. UI reimbursable option | US-NES5-003, US-NES5-009, US-NES5-006, US-NES5-011 |
| Commission-only real-estate/insurance agents | UI-exempt | US-NES5-019 |

## MULTI hand-offs (NE answers)
- **SUI wage-base credit**: yes. Wages paid for services in another State count toward the 9,000 (48-648.02). [US-NES5-011]
- **PFML/SDI coverage**: not applicable (NE has none).
- **Paid-sick-time coverage of part-time-in-State workers**: the employee must work at least 80 h in NE in the calendar year. [US-NES5-009]
- **Pay-statement reach**:
  - The Wage Payment and Collection Act applies to employers "employing any person within the state" (48-1229(2)). The default is employees working in NE. [US-NES5-004]
  - No ruling on remote workers was read.

## ACCESS gaps
- `https://revenue.nebraska.gov/sites/default/files/doc/business/Cir_En_2026/2027cir_en_whole.pdf`: Wayback 404 (also tried under `/sites/revenue.nebraska.gov/files/...`; the `2027_percent.pdf` variant also 404). Direct host: DNS failure.
- `https://dol.nebraska.gov/LaborStandards/WorkerRights/PSTFAQs`: Wayback timeout (000).
- `https://dol.nebraska.gov/LaborStandards/Wage/MinimumWage`: Wayback 404.
- NDOL 2027 minimum-wage publication: not located. Press-release list snapshot of 2026-08-14 (`https://dol.nebraska.gov/PressRelease`) predates it.
- `https://web.archive.org/cdx/search/cdx?...dol.nebraska.gov/PressRelease/Details/*`: the Internet Archive CDX was "Temporarily Offline".
- `https://nebraskalegislature.gov/FloorDocs/109/PDF/Slip/LB258.pdf`: Wayback 404. Covered by the 48-1203 text, which carries "Laws 2026, LB258, s.1; Effective Date July 18, 2026".
- `https://nebraskalegislature.gov/laws/statutes.php?statute=48-3802`: only the pre-LB415 snapshot (2025-03-11) exists. The LB415 slip law was read instead.
- All three NE hosts: DNS failure from this machine (VPN off). A US-exit retry would allow direct reads.

## Open questions
- **NE-OQ-1. 2027 adult minimum wage, rounding.** The derived value is 15.2625. The statute gives no rounding rule; leads say 15.26.
  - What would close it: the NDOL publication due by 2026-10-15 (NDOL Labor Standards or press release), read directly.
- **NE-OQ-2. 2027 Circular EN (Rev. 8-2026).** It carries the 2027 allowance value and tables (3.99% top statutory rate).
  - What would close it: the DOR PDF `Cir_En_2026/2027cir_en_whole.pdf`, read with a US-exit connection or in the orchestrator's Chrome pass.
- **NE-OQ-3. Child-support employer fee, priority and maximum (43-1720 to 43-1724).**
  - What would close it: those statute sections on nebraskalegislature.gov.
- **NE-OQ-4. Payroll-record retention period under NE law.** Including NDOL UI record-keeping (48-612/NAC 220) and 48-1209 wage-hour records.
  - What would close it: the NAC 220 ch. 2 records rule and Neb. Rev. Stat. 48-1209.
- **NE-OQ-5. Absence of a state overtime rule, and of local minimum wages and preemption.**
  - What would close it: the chapter 48 article 12 section list (nebraskalegislature.gov browse) read in full.
- **NE-OQ-6. Withholding registration form name (Form 20 Nebraska Tax Application) and the NEworks FTP wage-file specification.**
  - What would close it: the DOR "Register a Business" page and the dol.nebraska.gov/UITax FTP spec.
- **NE-OQ-7. Jury-duty and voting-leave pay rules, and the child-labour hours statute.**
  - What would close it: Neb. Rev. Stat. 25-1640, 32-922, 48-302 to 48-310.

Confidence overall: 85%. It is high on withholding, UI, paid sick time, final pay, garnishment and W-2 format (A.1/A.2). The 2027 values, the IWO fees and retention remain open.
