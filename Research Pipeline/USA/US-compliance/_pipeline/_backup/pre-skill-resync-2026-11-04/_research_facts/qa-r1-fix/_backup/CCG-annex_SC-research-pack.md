# CCG research pack - annex_SC (South Carolina)

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_SC` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_SC-facts.json` (42 facts, 8 pending on the register_id pattern defect, 8 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/SC.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- ACT 110 TRAP: 1.99% / 5.21% are ASSESSMENT-level for TY2026. 2026 WITHHOLDING stays on WH-1603F (0/3/6%) until SCDOR reissues tables - do NOT put 1.99/5.21 in the 2026 withholding engine.
- No supplemental flat rate in SC; no consumer garnishment.
- Oracle: WH-1603F weekly 750 / 3 allowances = 10.58.
- SC W-2 must be filed separately with SCDOR (RS record with full SSN); SSA filing does not satisfy SC.

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-SC-004: superseded
- US-SCP51-004: superseded
- US-SCP52-004: superseded

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `sc.labour.minwage.state.exists` | False | 2014-06-09 |  | US-SCS5-012 | high |
| `sc.local_mandates.preempted` | True | 2014-06-09 |  | US-SCS5-012 | high |
| `sc.labour.overtime.state_rule` | none (FLSA only) | 2026-01-01 |  | US-SCR3-006 | medium |
| `sc.wh.method` | WH-1603F: annualize; minus 5,000 per allowance; minus std deduction 10% of gross capped 7,500 (only with 1+ allowances); bands | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.pit.allowance.annual` | 5000 USD | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.pit.wh.std_deduction.rate` | 10 % | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.pit.wh.std_deduction.cap` | 7500 USD | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.pit.wh.band.1.ceiling` | 3640 USD | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.pit.wh.band.2.rate` | 3 % | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.pit.wh.band.2.subtract` | 109.2 USD | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.pit.wh.band.3.floor` | 18230 USD | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.pit.wh.band.3.rate` | 6 % | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.pit.wh.band.3.subtract` | 656.1 USD | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.pit.oracle.example_1.withholding` | 10.58 USD | 2026-01-01 | 2026-12-31 | US-SCS5-004 | high |
| `sc.wh.certificate` | SC W-4 (2026); none = zero allowances; no flat amount on regular wages | 2026-01-01 |  | US-SCS5-003 | high |
| `sc.pit.withholding_threshold.annual` | 1000 USD | 2026-01-01 |  | US-SCS5-018 | high |
| `sc.pit.supplemental.flat_rate.exists` | False | 2026-01-01 |  | US-SCS5-002 | high |
| `sc.pit.statutory.rate.1` | 1.99 % | 2026-01-01 |  | US-SCS5-001 | high |
| `sc.pit.statutory.rate.2` | 5.21 % | 2026-01-01 |  | US-SCS5-001 | high |
| `sc.pit.statutory.bracket.1.ceiling` | 30000 USD | 2026-01-01 |  | US-SCS5-001 | high |
| `sc.pit.sciad.single` | 15000 USD | 2026-01-01 |  | US-SCS5-001 | high |
| `sc.reciprocity.states` | none | 2026-01-01 |  | US-SCS5-018 | high |
| `sc.pit.conformity.irc_date` | 2024-12-31 | 2026-01-01 |  | US-SCS5-001 | high |
| `sc.sui.wage_base` | 14000 USD | 2015-01-01 |  | US-SCS5-014 | high |
| `sc.sui.wage_base.other_state_credit` | True | 2015-01-01 |  | US-SCS5-014 | high |
| `sc.ui.rate.min_total` | 0.06 % | 2026-01-01 | 2026-12-31 | US-SC-003 | high |
| `sc.ui.rate.max_total` | 5.46 % | 2026-01-01 | 2026-12-31 | US-SC-003 | high |
| `sc.sui.new_employer.rate` | 1.06 % | 2026-01-01 | 2026-12-31 | US-SC-003 | high |
| `sc.ui.daca.rate` | 0.06 % | 2015-01-01 |  | US-SCS5-014 | high |
| `sc.ui.benefit_ratio.lookback_quarters` | 16 | 2027-01-01 | 2027-12-31 | US-SCS5-015 | high |
| `sc.sdi_pfml.exists` | False | 2026-01-01 |  | US-SCR3-006 | high |
| `sc.report.wh.deposit_threshold.monthly` | 500 USD | 2026-01-01 |  | US-SCS5-002 | high |
| `sc.report.wh1605.due` | Apr 30; Jul 31; Oct 31 | 2026-01-01 |  | US-SCS5-002 | high |
| `sc.report.w2.due` | Jan 31; EFW2 with SC RS record (state code 45, full SSN); electronic at 10+ forms | 2026-01-01 |  | US-SCS5-016 | high |
| `sc.report.ui.quarterly_due` | last day of month after quarter | 2023-10-25 |  | US-SCS5-006 | high |
| `sc.newhire.report_days` | 20 days | 1998-10-01 |  | US-SCS5-011 | high |
| `sc.leave.sick.state_statute.exists` | False | 2017-04-05 |  | US-SCS5-013 | high |
| `sc.garn.consumer.available` | False | 2026-01-01 |  | US-SCS5-008 | high |
| `sc.garn.iwo.employer_fee.per_withholding` | 3 USD | 2026-01-01 |  | US-SCS5-010 | high |
| `sc.garn.iwo.remit_working_days` | 7 days | 2026-01-01 |  | US-SCS5-010 | high |
| `sc.prevailing_wage.exists` | False | 2026-01-01 |  | US-SCR3-009 | high |
| `sc.data.ssn.max_digits_mailed` | 5 | 2026-01-01 |  | US-SCS5-009 | high |
| `sc.labour.pay_change_notice.days` | 7 days | 2026-01-01 |  | US-SCP52-006 (promoted, Synthesis C) | low |
| `sc.labour.direct_deposit.free_withdrawal` | True | 2026-01-01 |  | US-SCP52-006 (promoted, Synthesis C) | low |
| `sc.local_wage_tax.exists` | False | 2026-01-01 |  | US-SCP52-003 (promoted, Synthesis C) | low |
| `sc.sui.employee.rate` | 0 % | 2026-01-01 |  | US-SCP52-005 (promoted, Synthesis C) | low |
| `sc.payslip.items` | itemized gross pay and deductions each pay period | 2026-01-01 |  | US-SCP52-006 (promoted, Synthesis C) | low |
| `sc.records.wage.retention_years` | 3 years | 2026-01-01 |  | US-SCP52-006 (promoted, Synthesis C) | low |
| `sc.final_pay.rule` | within 48 hours or next regular payday (max 30 days) | 2026-01-01 |  | US-SCP52-006 (promoted, Synthesis C) | low |
| `sc.term.vacation.payout` | only if due under policy or contract | 2026-01-01 |  | US-SCP52-006 (promoted, Synthesis C) | low |

# Findings by domain (stage 5)

## 1. labour_code
- **Minimum wage:** SC has no state minimum-wage statute, so the federal FLSA rate of 7.25 USD/h applies. The research ruled out a state section from two things: the Title 41 chapter index [US-SCR3-006] and 6-1-130, which takes the FLSA section 6 rate as its reference. Local minimum wages are **preempted**: 6-1-130 bars any political subdivision from setting a minimum wage above the federal rate, except in its own contracts. No 2027 change is enacted [US-SCS5-012]. Confidence: 95%.
- **Overtime:** no state overtime statute in Title 41; FLSA only [US-SCR3-006]. Confidence: 85%. This is an absence proven only at the chapter-index level.
- **Pay frequency and timing:** no statutory frequency. The employer must pay at the time and place set in the hire notice under 41-10-30(A), and give 7 calendar days' written notice before changing it (wage increases excepted) [US-SCP52-006; local file `ccg-sources/SC/SC-Code_41-10_wage-payment.html`, 41-10-40(D)].
- **Method of payment:** lawful US money, or a negotiable warrant or check dated the payday. Wages may go to an insured financial institution doing business in SC. With direct deposit, the employee gets a statement of earnings and withholdings and at least one free withdrawal per deposit (41-10-40(A)-(B)). The statute does not mention paycards [US-SC-004, US-SCP52-006].
- **Deductions:** none without state or federal authority or the written notice under 41-10-30(A) (41-10-40(C)). Penalty for unpaid wages: treble damages, 3-year limitation (41-10-80(C)).
- **Lactation:** reasonable unpaid break time, or use of paid break or meal time (41-1-130) [US-SCS5-013].

## 2. income_tax
- **Withholding method 2026 (operative):** the WH-1603 tables (0-10 allowances) or the WH-1603F formula. Steps: annualize; subtract 5,000 USD per allowance; subtract a standard deduction of 10% of gross, capped at 7,500 USD, only with one or more allowances. Annual tax is 0% below 3,640 USD; 3% minus 109.20 USD from 3,640 to 18,230 USD; 6% minus 656.10 USD from 18,230 USD [US-SC-007, US-SCP51-002, US-SCS5-004].
  - **G-DERIVE, done in Python:** 750 × 52 = 39,000; minus 3 × 5,000 and minus 3,900 gives 20,100; 20,100 × 0.06 − 656.10 = 549.90; ÷ 52 = **10.58**, matching the WH-1603F worked example.
  - Bracket continuity: 3,640 × 3% − 109.20 = 0. At 18,230, both 3% − 109.20 and 6% − 656.10 give 437.70, which matches the "max tax 1st bracket" constant.
- **Certificate:** SC W-4 (2026), Rev. 12/5/25.
  - Allowances, an additional amount, and exempt status (expires 2026-12-31); military-spouse domicile election (RR #24-5).
  - Regular wages may not be withheld as a flat amount or percentage.
  - An employee without an SC W-4 is withheld at zero allowances.
  - [US-SCS5-003, US-SCP51-003]
- **Threshold and rounding:** withhold if wages are expected to reach 1,000 USD in the year. The employer may compute wages to the nearest dollar (12-8-520(A)-(B)) [US-SCS5-018, US-SCR3-001].
- **Supplemental rate:** none. No flat supplemental rate exists in the statute, in Reg. ch. 117, in the DOR withholding page or in the FAQ (re-read 2026-11-02, keyword search for bonus, supplemental and flat). Bonuses are wages run through the tables [US-SCR3-002, US-SCS5-002].
- **2026 liability (assessment level, Act 110):** the two-rate schedule above.
  - SC taxable income starts from federal AGI.
  - SCIAD is 15,000 / 22,500 / 30,000 USD (single or MFS / head of household / MFJ). It phases out over AGI 40,000–95,000, 60,000–142,500 and 80,000–190,000 USD respectively; the reduction is rounded down to 10 USD.
  - SC EITC is 125% of the federal credit, capped at 200 USD.
  - Continuity check: 30,000 × 1.99% = 597 = 30,000 × 5.21% − 966.
  - [US-SCS5-001, US-SCS5-005]
- **Resident / nonresident:**
  - Wages are taxed where earned. A nonresident is withheld on SC-earned wages.
  - A resident working in a state with no income tax is withheld for SC.
  - A resident's wages earned in another state are not SC-withheld if that state's withholding applies (12-8-520(C)(1)). The resident gets a credit for tax paid to other states (12-6-3400).
  - SC has no reciprocity agreement.
  - A nonresident's SCIAD is prorated by SC AGI / federal AGI.
  - [US-SCS5-002, US-SCS5-018, US-SCR3-003, US-SCR3-004, US-SCS5-001]
- **Local income taxes:** none. The SCDOR tax index lists only local sales taxes [US-SCP52-003].
- **Conformity:** the IRC as of 2024-12-31 (12-6-40(A)(1)(a), last amended by 2025 Act No. 63). No 2026 conformity act appears in the section history [local `pdfs/SC/t12c006_scstatehouse-20261030.html`; cited via US-SCR3-004's file].
- Confidence: 95% on the 2026 withholding mechanics and the Act 110 text. The date of the post-Act-110 table revision is unknown.

## 3. social_security (SUI / SDI / PFML / levies)
- **SUI agency:** SC Department of Employment and Workforce (DEW). Contributions are employer-only and may not be deducted from wages (41-31-310) [US-SCP52-005].
- **Taxable wage base:** **14,000 USD** per employee per calendar year, fixed by statute since 2015-01-01 and not indexed. Wages reported under other states' UI laws count toward it (41-27-380(B)) [US-SCS5-014]. This is A.1, confirming US-SC-003 (A.2).
- **2026 rates (DEW page, wayback copy of 2026-06-07):** class 1 total 0.060% up to class 20 total 5.460%; no solvency surcharge in 2026. A new employer pays the higher of the class 12 rate or 1%, plus DACA = **1.060%** [US-SC-003].
  - G-DERIVE: 14,000 × 0.0006 = 8.40; 14,000 × 0.0106 = 148.40; 14,000 × 0.0546 = 764.40. All three equal the page's "maximum cost per employee" figures.
- **DACA:** 0.06% of wages for all contributory employers, except reimbursing and governmental employers. The statute (41-27-410) [US-SCS5-014] and the DEW page [US-SCR3-007] are two independent authorities for the same number.
- **2026 Act No. 243 (S.688), in force 2026-07-01:**
  - Benefit-ratio look-back: 12 quarters through tax year 2026, **16 quarters for 2027**, 20 quarters from 2028 (employers in rate class 1 in 2026 keep 12 quarters while they stay in class 1).
  - Solvency surcharge (41-31-45) rewritten.
  - Unpaid tax execution issued on or after 2027-01-01: employer rate plus 2 percentage points.
  - Late-report penalty: 10%, minimum 25 USD; the 1,000 USD caps on penalties are removed.
  - [US-SCS5-015]
- **SDI / TDI / PFML / LTC:** none in SC (Title 41 chapter index) [US-SCR3-006].
- **Corporate officers:** covered unless the corporation files a written election out for at least 2 years and notifies the officers (41-27-265) [US-SCS5-014].
- Confidence: 90%. The 2026 rate-class table rests on the wayback copy, because dew.sc.gov returns 403 to a direct GET.

## 4. payslip_statute
- **Content:** an itemized statement of gross pay and deductions for each pay period (41-10-30(C)). With direct deposit, a statement of earnings and withholdings (41-10-40(B)). The statute requires no other field, such as hours, rates or employer address [US-SCP52-006, US-SC-004].
- **Exemptions from 41-10-30:** employers of domestic labour in private homes, and employers with fewer than 5 employees at all times during the preceding 12 months (41-10-20).
- **Hire notice:** written notice of normal hours, wages, time and place of payment, and deductions, or conspicuous posting. Changes take effect only after 7 days' written notice [US-SCP52-006].
- **Electronic delivery:** no SC statute addresses it. 41-10-30(C) says only "furnish".
- **Retention:** wage-payment records 3 years (41-10-30(B)); UI payroll records 5 years (Reg. 47-14) [US-SCS5-007].
- **SSN:** see domain 12.
- Confidence: 90%. Electronic consent rests only on the silence of the statute.

## 5. reporting_instruments
| Filing | Authority | Frequency / deadline | Format / channel | register_id |
|---|---|---|---|---|
| Withholding deposits | SCDOR | Resident agents: same dates as federal deposits. Nonresident agents (and agents not depositing federally): by the 15th of the next month if 500 USD or more, else quarterly. Payments allocated by paycheck date | MyDORWAY / EFT. Electronic required at 15,000 USD or more per quarter or 24+ payments a year; paper coupon WH-1601 | US-SCS5-002, US-SCS5-018 |
| WH-1605 (Q1–Q3) | SCDOR | Apr 30, Jul 31, Oct 31. Zero returns are required while the account is open | MyDORWAY, batch program (10+ returns), or paper | US-SCS5-002 |
| WH-1606 (Q4 + annual reconciliation) | SCDOR | Jan 31. Required if the account was open in any part of the year | same | US-SCS5-002 |
| W-2 to SCDOR | SCDOR | Jan 31 (employees, SSA and SCDOR) | `file_upload`: EFW2 .txt with the required SC **RS** state record (state code 45, full SSN), or Excel template (up to 30 employees), or manual entry. Electronic is mandatory at 10+ forms. Paper filers send WH-1612. Filing with SSA does **not** satisfy SC | US-SCS5-016, US-SCS5-017, US-SCS5-003 |
| Quarterly UI contribution and wage report | DEW | Last day of the month after the quarter (Reg. 47-15(C), 47-16) | `file_upload` / online in SUITS: ICESA, EFW2, XML or CSV (SUITS spec v1.6, 2023-10-25). Agents for 10+ employees must file electronically (41-31-160) | US-SCS5-006, US-SCS5-007, US-SCP52-005 |
| New hire | DSS State Directory of New Hires | 20 calendar days after hire. Electronic transmitters: semi-monthly, 12–16 days apart. Rehire after 60+ days counts as a new hire | newhire.sc.gov, or a copy of the SC W-4 with boxes 8–10. Fields: employer name, address and FEIN; employee name, address and SSN | US-SCS5-011, US-SCS5-003 |
| Mass separation | DEW | UCB-113 per worker within 10 days (excluding Sundays and holidays); 10+ workers in one establishment | form | US-SCS5-007 |
| Registration | SCDOR (9-digit withholding file number, MyDORWAY) / DEW (SUITS) | at start | online | US-SCS5-002 |

- **Scope trap:** the TY2026 RS-1 edition is not yet published. The file at the same URL is the TY2025 edition (October 2025) [US-SCS5-017].
- Confidence: 90%.

## 6. leave
- **Paid sick leave:** no state statute. **Local mandates are preempted:** 41-1-25 (2017 Act No. 3) bars every political subdivision from requiring any employee benefit, including paid sick leave, paid vacation, paid holidays and retirement benefits [US-SCS5-013].
- **PFML:** none [US-SCR3-006].
- **Jury duty / subpoena:** protected against dismissal or demotion (41-1-70); no paid-leave mandate [US-SCS5-013].
- **Vacation and sick pay:** paid only under the employer's policy. Once due under the policy, they are "wages" for the wage-payment chapter (41-10-10(2)).
- Confidence: 90%.

## 7. termination
- **Final pay:** all wages due within 48 hours of separation, or by the next regular payday, which may not exceed 30 days. The rule applies to any separation, discharge or resignation alike (41-10-50). Remedy: treble damages (41-10-80(C)).
- **Accrued vacation:** payable only if due under the employer's policy or contract (41-10-10(2)). There is no statutory payout mandate.
- **Wages in dispute:** pay the conceded amount unconditionally (41-10-60).
- **Separation notice:** no employer-issued UI separation notice at termination. The employer answers DEW's claim notice (Reg. 47-19, 41-31-160). For mass separations, UCB-113 [US-SCS5-007].
- **Child support:** within 20 days after employment ends, notify the clerk of the termination date and the final paycheck (63-17-1460(G)) [US-SCS5-010].
- **State WARN law:** none found in the Title 41 index (absence at index level) [US-SCR3-006].
- Confidence: 90%.

## 8. benefits_in_kind
- **Conformity:** SC adopts the IRC as amended through 2024-12-31 (12-6-40). Act 110 decouples only the federal standard and itemized deductions (12-6-50(21)) [US-SCS5-001].
  - Federal exclusions (401(k), section 125, HSA, transit, group-term life) follow the 2024 IRC, and no SC departure was found.
  - Federal changes enacted after 2024-12-31 (OBBBA 2025) are not adopted for SC unless a later conformity act passes.
  - These are return-level effects; wages for withholding follow 12-8-520(D) and IRC 3401.
- **UI:** in-kind pay is valued at DEW rates (Reg. 47-1). In-kind pay to agricultural and domestic workers is excluded from UI wages, and so are employer plan payments for retirement, sickness, medical care and death (41-27-380(A)) [US-SCS5-007, US-SCS5-014].
- Confidence: 80%. No item-by-item SC addition/subtraction list (12-6-1130/1140) was read for each benefit.

## 9. deductions_garnishments
- **Consumer debt:** **no wage garnishment** for consumer credit sales, leases, loans or rental-purchase agreements (37-5-104). An employer may not discharge an employee over such a garnishment (37-5-106) [US-SCS5-008].
- **Child support:**
  - Start by the next regular pay period after service.
  - Cap: CCPA 15 USC 1673(b).
  - Employer fee: up to **3 USD per withholding**, deducted from the obligor.
  - Priority: current support first, and every order partly implemented.
  - Remit to the State Disbursement Unit within **7 working days**, stating the withholding date.
  - Out-of-state orders: the fee, cap and timing follow the law of the principal place of employment.
  - [US-SCS5-010]
- **Wage deductions:** require legal authority or written notice (41-10-40(C)).
- **State tax levy on wages:** not read (open question).
- Confidence: 85%.

## 10. collective_agreements / prevailing wage
- SC has **no state prevailing-wage law**: it is among the 24 states listed in the DOL footnote, and chapter 41-10 has no such section. Federal Davis-Bacon certified payroll applies on federal projects only [US-SCR3-009, US-SCP51-004]. Confidence: 90%.

## 11. indexation
- **Income tax brackets:** cumulatively indexed each 15 December by chained CPI, capped at 4% a year, rounded to 10 USD, for the next tax year (12-6-520). The Act 110 30,000 USD bracket is indexed the same way.
- **Top rate (from TY2027):** cut if the Board of Economic Advisors (BEA) projects individual income tax revenue up by at least 5%. The reduction is the greater of 200 million USD or 25% of the surplus, until the rate reaches 1.99%. The forecast in effect on 15 February is final [US-SCS5-001, US-SCS5-005].
- **Withholding constants** (5,000 USD per allowance, 10% / 7,500 USD cap): set by DOR each year in WH-1603F; not statutory.
- **Not indexed:** the UI wage base (14,000 USD, statutory) and the minimum wage (federal).
- **Publication:** SCDOR's annual withholding tables in early November, via the news page and the Withholding Tax News email [US-SCS5-002]. The 2027 files (WH1603_2027, WH1603F_2027, SCW4_2027) returned **404 on 2026-11-02**, so they are not yet published.
- **DEW:** annual rate notice and tax-rate table (2027 not read).

## 12. data_protection
- **SSN (37-20-180):**
  - No public display of 6 or more digits.
  - No SSN, or a portion of 6 or more digits, on materials mailed to the individual unless law requires it, and never visible on a postcard or through the envelope.
  - Internet transmission only over a secure connection or encrypted.
  - No disclosure to third parties without consent, except for a legitimate business or government purpose.
- **Payroll consequences:**
  - Mailed pay statements show 5 digits at most.
  - The W-2 (federal requirement) and the DOR RS record (full SSN required) are exempt as legally required.
- [US-SCS5-009, US-SCS5-017]
- Confidence: 90%. The breach-notice statute 39-1-90 was not read.

## 13. live_legal_change (2026-01-01 → 2026-11-02)
| Change | Status | Level | register_id |
|---|---|---|---|
| 2026 Act No. 110 (H.4216): 1.99% / 5.21% schedule, SCIAD, EITC cap, decoupling from the federal standard deduction | **In force**: signed 2026-03-30, applies to TY2026 | Assessment (annual return). Withholding unchanged until SCDOR reissues WH-1603/1603F; no revised edition as of 2026-11-02 | US-SCS5-001, -002, -005 |
| Act 110 Section 6: DOR to adjust withholding tables | Ordered; **not yet implemented** (IL #26-20, 2026-08-31: "will consult RFA") | Withholding | US-SCS5-005 |
| 2026 Act No. 243 (S.688): UI benefit ratio 16 quarters (2027) / 20 quarters (2028); +2% rate on post-2027 executions; penalty caps removed | **In force** 2026-07-01 (benefit-ratio change effective for tax year 2027) | Employer UI rate | US-SCS5-015 |
| Other 2026 acts in the downloaded chapters: Act 146 (H.4189), Act 183 (H.3551, 12-6-1120(12)), Act 162 (S.32), Act 225 (S.556) | In force; they touch hospital definitions and return-level adjustments and credits, not payroll withholding (section titles only) | Assessment | — (sweep note) |
| Rate cut for TY2027 under 12-6-510(C)(2) | Contingent on the BEA forecast; not determined | Assessment, then tables | US-SCS5-001 |

Sweep method: a mechanical grep for "2026 Act No." in the history notes of every code chapter downloaded this pass and in t12c006. No 2026 amendments were found in chapters 41-10, 41-1, 12-8, 37-5, 37-20 or 63-17 (beyond Act 146 conforming edits in 63-17 and 43-5). This is limited to the chapters read; it is not a full SC session sweep.

## Special populations (state-level, US-OWN-005)
| Population | SC rule | register_id |
|---|---|---|
| Domestic / household workers | Exempt from the 41-10-30 notice and pay-statement duties. Employer-paid FICA and in-kind pay are excluded from UI wages. Coverage threshold (41-27-230) not read | US-SCS5-014; 41-10-20 in the US-SC-004 file |
| Agricultural | UI defines agricultural labour (41-27-120). Agricultural labour by students or qualifying part-timers is excluded (41-27-260(16)). In-kind pay excluded from UI wages. Minimum wage: federal | US-SCS5-014 |
| Minors | Child labour: 41-13-20 delegates the rules to LLR regulations (not read). Newspaper delivery by under-18s and a child under 18 employed by a parent are excluded from UI | US-SCS5-014 |
| Tipped employees | No state minimum wage, so the federal tipped rules apply. Reported tips are UI wages (41-27-380(A)) | US-SCS5-014, US-SCS5-012 |
| Clergy / religious | Churches and ministers excluded from UI (41-27-260(10)). Withholding: follows the federal wage definition | US-SCS5-014 |
| Students | A student employed by own school, and student nurses and interns, are excluded from UI (41-27-260(9), (12)) | US-SCS5-014 |
| Nonresident aliens | No SC rule beyond the general rule: SC wages withheld wherever the employee resides. 12-8-550: 2% on nonresidents performing temporary personal services (non-wage) | US-SCS5-018, US-SCP52-004 |
| Statutory employees | No state rule beyond federal (chapter 12-8 read; wages follow IRC 3401) | US-SCS5-018 |
| Government employees | Elected and policymaking posts excluded from UI (41-27-260(5)). Governmental employers exempt from DACA (41-27-410). 12-8-10 includes governments as "person" | US-SCS5-014, US-SCS5-018 |
| Corporate officers | UI-covered unless the corporation elects out (2-year election plus notice) | US-SCS5-014 |
| Military spouses | Exemption election on the SC W-4 (RR #24-5) | US-SCS5-003 |
| Commission-only insurance and real-estate agents, direct sellers, owner-operator drivers | Excluded from UI | US-SCS5-014 |

## ACCESS gaps (exact URLs)
- `https://dew.sc.gov/employers/tax-rate-information`: HTTP 403 (direct curl, US exit IP). The wayback 2026-06-07 copy is already held (US-SC-003).
- `https://dew.sc.gov/employers/ui-tax-forms`: no response (curl code 000). The wayback 2026-10-09 copy is held.
- `https://dew.sc.gov/sites/dew/files/Documents/SUITS-%20Wage%20Report%20and%20Payment%20File%20Specification%20version%201.6%2010.25.2023.pdf`: HTTP 403. Retrieved via the wayback 2025-08-04 capture.
- `https://dew.sc.gov/employers/file-and-pay-taxes`: no wayback capture (404).
- `https://newhire.sc.gov/`: no response directly. The wayback 2026-10-16 copy is a JavaScript shell with no content.

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **sc.pit.tables.post_act110** (blocking): SCDOR has not reissued WH-1603/1603F after Act 110 (IL #26-20 "will consult RFA"); 2027 files 404. What would close it: SCDOR 2027 (or revised 2026) WH-1603F on dor.sc.gov/withholding (~Nov 2026).
- **sc.ui.rates.next_year** (non-blocking): DEW 2027 rate table and solvency surcharge under Act 243 not read (403). What would close it: DEW 2027 tax-rate page or employer rate notice (browser pass).
- **sc.report.rs1.next_year** (non-blocking): TY2026 RS-1 not yet published. What would close it: SCDOR October-2026 RS-1.
- **sc.ui.coverage_thresholds** (non-blocking): Domestic/agricultural UI thresholds (41-27-230/210) not extracted. What would close it: t41c027 file already held.
- **sc.labour.child_labour** (non-blocking): LLR child-labour regulations not read. What would close it: SC Code of Regulations ch. 71 child-labour article.
- **sc.garn.state_tax_levy** (non-blocking): SCDOR wage levy not read. What would close it: S.C. Code 12-54.
- **sc.bik.addition_subtraction** (non-blocking): 12-6-1130/1140 item-by-item fringe treatment after Act 110 not read. What would close it: Those sections in t12c006 file held.
