# CCG research pack - annex_VT (Vermont)

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_VT` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_VT-facts.json` (40 facts, 5 pending on the register_id pattern defect, 14 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/VT.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- Child Care Contribution 0.44% (employee max 0.11%) on ALL IRC 3401 wages, no cap - WTC/DD must carry both shares.
- 3% minimum tax on AGI over 150,000 is ASSESSMENT-level only.
- Oracle: GB-1210-2026 p.6 weekly 1,800 married 2 allowances = 45.77.
- New hire within 10 days; final pay on discharge within 72 hours; UI report needs gender and hourly wage for hourly workers.

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-VTP51-007: superseded
- US-VTS5-027: partial

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `vt.minwage.hourly` | 14.42 USD | 2026-01-01 | 2026-12-31 | US-VTS5-003 | high |
| `vt.minwage.indexation` | smaller of 5% or CPI-U, each 1 January, nearest 0.01; never decreased | 2025-07-01 |  | US-VTS5-001 | high |
| `vt.minwage.tipped.cash_wage` | 7.21 USD | 2026-01-01 | 2026-12-31 | US-VTS5-003 | high |
| `vt.overtime.weekly_threshold_hours` | 40 hours | 2025-07-01 |  | US-VTS5-001 | high |
| `vt.overtime.premium.multiplier` | 1.5 ratio | 2025-07-01 |  | US-VTS5-001 | high |
| `vt.pay_frequency.rule` | weekly by default (wages to max 6 days before payday); biweekly/semimonthly after notice | 2024-07-01 |  | US-VTS5-002 | high |
| `vt.labour.direct_deposit.consent_required` | True | 2024-07-01 |  | US-VTS5-002 | high |
| `vt.wh.method` | GB-1210-2026 percentage tables after W-4VT allowances | 2026-01-01 | 2026-12-31 | US-VTS5-016 | high |
| `vt.pit.allowance.annual` | 5400 USD | 2026-01-01 | 2026-12-31 | US-VTS5-016 | high |
| `vt.pit.wh.single.thresholds` | 3925;54675;126775;260225 | 2026-01-01 | 2026-12-31 | US-VTS5-016 | high |
| `vt.pit.wh.married.thresholds` | 11775;96475;216525;323825 | 2026-01-01 | 2026-12-31 | US-VTS5-016 | high |
| `vt.pit.wh.rates` | 3.35;6.60;7.60;8.75 | 2026-01-01 | 2026-12-31 | US-VTS5-016 | high |
| `vt.pit.wh.rate.top` | 8.75 % | 2026-01-01 | 2026-12-31 | US-VTS5-016 | high |
| `vt.pit.oracle.example_1.withholding` | 45.77 USD | 2026-01-01 | 2026-12-31 | US-VTS5-016 | high |
| `vt.wh.certificate` | W-4VT (Rev. 12/18); federal W-4 fallback | 2026-01-01 |  | US-VTS5-029 | medium |
| `vt.pit.supplemental.ratio_of_federal` | 30 % | 2026-01-01 | 2026-12-31 | US-VTS5-016 | high |
| `vt.pit.statutory.min_tax.rate` | 3 % | 2026-01-01 |  | US-VTS5-018 | high |
| `vt.reciprocity.states` | none | 2026-01-01 | 2026-12-31 | US-VTS5-016 | high |
| `vt.sui.wage_base` | 15400 USD | 2026-01-01 | 2026-12-31 | US-VTS5-004 | high |
| `vt.sui.wage_base` | 14800 USD | 2025-01-01 | 2025-12-31 | US-VTS5-004 | high |
| `vt.sui.new_employer.rate` | 1.0 % | 2004-07-01 |  | US-VTS5-009 | high |
| `vt.ui.rate.schedule_i.min` | 0.4 % | 2024-07-01 |  | US-VTS5-006 | high |
| `vt.ui.rate.schedule_v.max` | 8.4 % | 2024-07-01 |  | US-VTS5-006 | high |
| `vt.sui.wage_base.other_state_credit` | True | 2012-01-01 |  | US-VTS5-010 | high |
| `vt.ccc.total.rate` | 0.44 % | 2024-07-01 |  | US-VTS5-030 | high |
| `vt.ccc.employee.max_rate` | 0.11 % | 2024-07-01 |  | US-VTS5-030 | high |
| `vt.payslip.items` | gross pay, hours worked, hourly rate, all deductions itemised | 2009-01-01 |  | US-VTP9-001 | high |
| `vt.records.ui.retention_years` | 4 years | 2026-01-01 |  | US-VTS5-009 | high |
| `vt.report.wht434.due` | January 31 | 2026-01-01 | 2026-12-31 | US-VTS5-017 | high |
| `vt.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | 2026-01-01 |  | US-VTS5-007 | high |
| `vt.newhire.report_days` | 10 days | 2025-09-01 |  | US-VTS5-014 | high |
| `vt.leave.est.accrual_ratio_hours_worked` | 52 hours | 2025-05-13 |  | US-VTS5-008 | high |
| `vt.leave.est.annual_cap_hours` | 40 hours | 2025-05-13 |  | US-VTS5-008 | high |
| `vt.leave.est.payout_at_separation` | False | 2024-07-01 |  | US-VTS5-011 | high |
| `vt.term.final_pay.discharge.hours` | 72 hours | 2024-07-01 |  | US-VTS5-002 | high |
| `vt.term.vacation.payout` | only if written policy/agreement provides | 2026-01-01 |  | US-VTS5-025 | high |
| `vt.garn.creditor.max_percent` | 25 % | 2010-07-01 |  | US-VTS5-021 | high |
| `vt.garn.consumer_credit.max_rate` | 15 % | 2010-07-01 |  | US-VTS5-021 | high |
| `vt.garn.iwo.employer_fee.monthly` | 5.0 USD | 2004-09-01 |  | US-VTS5-023 | high |
| `vt.data.ssn.mailed_prohibited` | True | 2007-01-01 |  | US-VTS5-015 | high |
| `vt.pit.nonresident.out_of_state_employer_days` | 30 days | 2026-01-01 |  | US-VTP51-003 (promoted, Synthesis C) | high |
| `vt.local_wage_tax.exists` | False | 2026-01-01 |  | US-VTP51-005 (promoted, Synthesis C) | high |
| `vt.sdi_pfml.exists` | False | 2024-07-01 |  | US-VTP51-006 (promoted, Synthesis C) | high |
| `vt.report.wht436.due` | 25th after quarter end | 2026-01-01 |  | US-VTP51-002 (promoted, Synthesis C) | high |
| `vt.prevailing_wage.threshold` | 100000 USD | 2026-01-01 |  | US-VTP51-011 (promoted, Synthesis C) | high |

# Findings by domain (stage 5)

## 1. labour_code
- **State minimum wage:**
  - **14.42 USD/h** from 2026-01-01 (was 14.01) [US-VTS5-003; statute US-VTS5-001].
  - Indexation (384(a)(1)): each 1 January by the **smaller of 5% or CPI-U US city average** for the 12 months before the previous 1 September, rounded to one decimal. Never decreased; rounded to the nearest 0.01. The federal rate applies if it is higher.
  - G-DERIVE: 14.01 × 1.029 = 14.4163 → **14.42**. The implied CPI step is 2.9%, under the 5% cap. The BLS CPI value itself was not fetched.
  - **2027 rate:** not located. VDOL published the 2026 release on 2025-10-06. No 2027 release was found in the Wayback index, and the web leads (tier B) say it is not yet published (Q1).
- **Tipped (service) employees** (384(a)(2)):
  - Covers hotel, motel, tourist place and restaurant staff who get more than 120 USD/month in tips.
  - Basic wage is at least half the minimum: **7.21 USD/h** from 2026-01-01 (derived 14.42 × 0.5; stated in US-VTS5-003).
  - The employer makes up any shortfall over the workweek.
- **Local minimum wages:** none. VT municipalities have only local option taxes on sales, meals, alcohol and rooms [US-VTP51-005]. No local wage ordinance was located (absence not proven beyond that page).
- **Overtime** (384(b)) [US-VTS5-001]:
  - 1.5× the regular rate above 40 h per workweek. There is no daily overtime.
  - Broad exemptions beyond FLSA: retail or service establishments; seasonal amusement; hotel, motel and restaurant; transport not under FLSA overtime; political subdivisions; FLSA-covered State employees; General Assembly staff.
  - Hospitals and care homes may elect an 8/80 biweekly system.
  - The 383(2) employee exclusions also apply (see Special populations).
  - Allowed deductions from the minimum: board, lodging, apparel, rent, utilities (384(c)).
- **Coverage:** 383(3) employer = 2 or more employees for min wage/OT [US-VTS5-013]. 341 uses an ABC test and an employer of 1 or more for wage payment [US-VTS5-019].
- **Pay frequency** (342(a)) [US-VTS5-002]:
  - Weekly by default, with wages to a day no more than 6 days before payday.
  - Biweekly or semimonthly is allowed after notice to employees. A CBA may set a 13-day lag.
- **Method of payment** (342(c), 343) [US-VTS5-002, US-VTS5-022]:
  - Lawful money or check. No scrip.
  - Direct deposit needs the employee's **written authorisation**.
  - Payroll card needs written voluntary consent (not a condition of hire), plain-language disclosures in 10-point type and 3 free withdrawals per period. No costs may be passed on. Changes need 21 days' notice. One free replacement card per year. A nonbranded card is valid 60 days at most. No credit link.
  - Language rule for card disclosures: 342(f) [US-VTL-001].
- Confidence: 92% (2026); 2027 rate open.

## 2. income_tax
- **Mandate:** withhold as the Commissioner prescribes, by tables or formulae [US-VTP51-001].
- **Method (GB-1210-2026)** [US-VTS5-016]:
  - Effective 2026-01-01, expires 2026-12-31.
  - Wages subject to VT withholding = wages subject to federal withholding, paid to a VT resident or to a nonresident for services in VT.
  - Steps: subtract W-4VT allowances, then apply the percentage table (or the wage-bracket charts).
  - **One allowance:** annual 5,400.00; weekly 103.85; biweekly 207.69; semimonthly 225.00; monthly 450.00; quarterly 1,350.00; daily 20.77. Derived: 5,400/52 = 103.846 → 103.85.
  - **Annual Single:** 0–3,925 nil; to 54,675 3.35%; to 126,775 1,700.13 + 6.60%; to 260,225 6,458.73 + 7.60%; above 16,600.93 + 8.75%.
  - **Annual Married:** 0–11,775 nil; to 96,475 3.35%; to 216,525 2,837.45 + 6.60%; to 323,825 10,760.75 + 7.60%; above 18,915.55 + 8.75%.
  - Civil-union partners use the Married table.
- **Rounding:** no rule is stated. Bracket constants use round-half-up to the cent: (54,675−3,925) × 0.0335 = 1,700.125 → 1,700.13.
- **Oracle (C37):** the worked example in GB-1210-2026 p.6. Weekly 1,800, Married, 2 allowances: 1,800 − 207.70 = 1,592.30; (1,592.30 − 226) × 0.0335 = **45.77**. Reproduced in Python (45.7711). No official calculator was located. Return this to the scaffolder for `build-manifest.oracle`: URL https://tax.vermont.gov/sites/tax/files/documents/GB-1210-2026.pdf, edition 2026, page 6.
- **Certificate:** W-4VT (Rev. 12/18) [US-VTS5-029]:
  - Statuses: Single; MFJ/Civil Union; MFS/Civil Union; Married-withhold-at-single-rate.
  - Allowances worksheet; line 6 extra amount; Exempt.
  - The employer may fall back on the federal W-4. Extra federal withholding on W-4 line 6 → add 30% of it to VT withholding.
  - The current edition on the live site was not confirmed (403).
- **Supplemental / non-periodic payments:** VT withholding may be estimated at **30% of federal withholding**. NQDC distributions: **6%** (5841; GB-1210) [US-VTS5-016, US-VTP51-001]. There is no flat supplemental percentage of wages.
- **Statutory rates** (5822) [US-VTS5-018]:
  - 3.35 / 6.6 / 7.6 / 8.75%, with brackets indexed yearly by CPI-U (5822(b)(2)).
  - **3% minimum tax on federal AGI over 150,000** (5822(a)(6)). Level: **assessment only**, not in the withholding tables.
- **Residents / nonresidents** [US-VTS5-016, US-VTP51-003, US-VTP52-003]:
  - Nonresident working in VT and elsewhere: tax on the full pay × VT hours / total hours.
  - Resident: tax on the full pay, minus tax withheld for the work state. A mover into VT is a resident for withholding.
  - Out-of-state employers start VT withholding after an employee has worked from a VT location for 30 days.
  - The resident credit (5825) is at **assessment** [US-VTP52-001].
  - **No reciprocity agreements** (absence on 3 authority pages + GB-1210 full text).
- **Local income taxes:** none [US-VTP51-005].
- Confidence: 95%.

## 3. social_security
- **SUI** (Vermont DOL):
  - **Wage base:** **15,400** for 2026, up from 14,800 [US-VTS5-004, US-VTSUI-002].
  - **Base indexation:** each 1 January by the % increase in the State annual average wage, when the fund is positive and Title XII advances are repaid. The base drops by 2,000 when the rate schedule falls to III or to I [US-VTS5-005]. G-DERIVE not possible: the 1338(g) average wage was not fetched.
  - **Rates (1326):** rate classes 0–20 × schedules I–V. Schedule I runs 0.4–5.4%; schedule V runs 1.3–8.4%. The **rate year starts 1 July** [US-VTS5-006, US-VTSUI-001].
  - **New-employer rate:** **1.0%** (since 2004-07-01). Foreign construction NAICS 236/237/238 pay the industry average. A new employer stays on this rate for at least 2 years [US-VTS5-009].
  - **Employee contribution:** none, and the tax cannot be withheld [US-VTP51-007].
  - The schedule in force for the 2026-07 rate year was not confirmed (Q4).
- **SDI/TDI/PFML:** no mandatory program. VT-FMLI is voluntary (The Hartford) [US-VTP51-006].
- **Employer levies:** **Child Care Contribution** [US-VTS5-030, US-VTP51-004, US-VTP7-001]:
  - 0.44% of all IRC 3401 wages subject to VT withholding, with no cap.
  - The employer may withhold up to 0.11% from the employee; the share can be less or none and need not be uniform.
  - The employee share goes in W-2 Box 14.
  - Reported on WHT-436 and paid on the withholding schedule. Example split: 0.11 employee + 0.33 employer.
  - No other wage levy (P7/P9 list, US-VTL-003).
- **MULTI hand-off, SUI credit:** **yes.** 1321(b)(2): "employment" includes service covered under another state's UI law. So wages the same employer already paid for other-state covered employment in the same year count toward the VT base. A predecessor's wages also count in the acquisition year [US-VTS5-010].
- **UI localization:** four tests in order — localization, base of operations, … [US-VTS5-009].
- Confidence: 90%.

## 4. payslip_statute
- **Content:** a detailed written statement with each weekly pay: gross pay, hours worked, hourly rate, all deductions itemised (including meals). Service employees: weekly tip report kept 3 years (CVR 24-090-003 §VI) [US-VTP9-001, US-VTP52-004].
- **Delivery:** no electronic-consent rule was found in 342 or the CVR text read (Q6).
- **Retention:** 4 years for UI records [US-VTS5-009]; 3 years for tip reports [US-VTP9-001].
- **Language:** English. Only the payroll-card disclosures carry a primary-language rule [US-VTL-001, US-OWN-006].
- **MULTI hand-off, pay-statement reach:** no reach rule in the CVR text. Default is the work-location state (MULTI §4).
- Confidence: 85%.

## 5. reporting_instruments
- **Withholding** (Department of Taxes, myVTax):
  - Registration through myVTax or BR-400 [US-VTS5-017].
  - The Department sets the deposit frequency from annual totals:
    - semiweekly: Wed–Fri pay dates due the next Wednesday, Sat–Tue due the next Friday;
    - monthly: by the 25th (23rd for the February payment);
    - quarterly: with WHT-436 by the 25th after quarter end [US-VTP51-002, US-VTPIT-003].
  - **WHT-436** quarterly reconciliation also carries the CCC [US-VTS5-030].
  - **WHT-434** annual reconciliation is due **January 31** and is the transmittal for W-2/1099. E-filing is required at **10 or more** forms, and always for payroll services.
  - VT left the Combined Fed/State program, so W-2s must be filed directly with VT [US-VTS5-017].
  - The W-2 file format (EFW2 vs state spec) is not stated in GB-1210 (Q5).
- **UI quarterly wage and contribution report** [US-VTS5-007, US-VTS5-009]:
  - Filed every quarter even with no wages, electronically via Employer e-Services.
  - Due Apr 30 / Jul 31 / Oct 31 / Jan 31, or the next business day.
  - Per worker: name, SSN, gross wages; for **hourly workers also gender and hourly wage** (1314a(a)(2)).
  - Penalty 100 USD per late report. Misclassification: up to 5,000 USD per employee plus State-contract debarment.
  - Separation information within 10 days of a request.
- **New hire** [US-VTS5-014, US-VTS5-009]:
  - Report to VDOL within **10 calendar days** of the first day worked for pay, via Employer e-Services.
  - Fields: employee name, address, SSN, first date of employment; employer name, address, FEIN.
  - A rehire after 60 or more consecutive days apart counts as a new hire.
- POA forms: PA-1 (tax), C-50 (UI) [US-VTP51-012/-013].
- Confidence: 88%.

## 6. leave
- **Earned sick time** (21 V.S.A. 481–483) [US-VTS5-008, -011, -012]:
  - Accrual: 1 h per 52 h worked. The employer may cap accrual at **40 h per 12 months** and cap use at 40 h per 12 months.
  - Waiting period of up to 1 year: time accrues but cannot be used.
  - Paid at the greater of the normal rate or the minimum wage. Group insurance continues.
  - Unused time carries over. **No payout at separation** unless the employer agrees.
  - Rehire within 12 months after a discharge: no new waiting period.
  - **Covered employee:** averages 18 or more h/week over the year. Excluded: federal employees; jobs of 20 weeks or less; under 18s; per-diem/intermittent workers; certain substitutes; excluded State service; WC-excluded owners/officers.
- **Parental and family leave** (21 V.S.A. 471–472) [US-VTS5-026, US-VTS5-027 partial]:
  - Up to 12 weeks unpaid per 12 months for parental, family, safe leave or a qualifying exigency.
  - Up to 2 of those weeks may be bereavement leave (Act 32 of 2025, eff. 2025-07-01).
  - The employee may use accrued paid leave or STD. Benefits continue at the existing employee contribution.
  - Employer thresholds as read (2025-03 copy, pre-Act 32): 10 employees for parental leave, 15 for family leave, counting staff averaging 30 or more h/week; employee needs 1 year of service. **This may be outdated** (Q7).
- **Short-term family leave** (472a): 4 h per 30 days and 24 h per year, unpaid [US-VTS5-028].
- **PFML benefits:** none (voluntary VT-FMLI only).
- **MULTI hand-off, paid sick leave for partly-in-state workers:** 481 has no in-state hours threshold. The employer is any employer "doing business in or operating within this State". Reach to a worker who is only partly in VT is not stated (Q8).
- Confidence: 85%.

## 7. termination
- **Final pay** (342(b)) [US-VTS5-002]: voluntary quit → the last regular payday, or the following Friday if there is none; **discharge → within 72 hours**.
- **Penalties** (345): fine up to 5,000 USD; liability of corporate officers who control payroll [US-VTS5-024].
- **Accrued vacation:** no statute. It is payable only if a written policy or agreement (including a handbook) provides it (VDOL WH-13) [US-VTS5-025]. Earned sick time: no payout (483(e)).
- **UI separation information:** within 10 days of a VDOL request (1314a(e)) [US-VTS5-007].
- **State WARN law** (21 V.S.A. 411 ff.): not read (Q9).
- Confidence: 80%.

## 8. benefits_in_kind
- VT taxable income starts from **federal AGI**. Withholding wages = federal withholding wages [US-VTS5-020, US-VTS5-016].
- No wage-level departure from the federal 401(k), §125, HSA, transit or group-term-life exclusions was found. **HSA follows federal.**
- One departure: civil-union partners are treated as spouses for §125 pretax treatment and imputed-income purposes (GB-1210 p.4).
- CCC base = IRC 3401 wages [US-VTS5-030].
- Confidence: 85%. The statutory add-back list in 5811(21)(A) holds no wage items.

## 9. deductions_garnishments
- **Wage deductions** (VDOL WH-13, Minimum Wage Rules) [US-VTS5-025]:
  - Goods or services: allowed only if pay stays at or above the minimum wage, with written authorisation or documented intent to repay, and not above the agreed amount.
  - Taxes and child support: as authorised by law.
  - Health and retirement contributions: with written authorisation.
  - Meals and lodging actually furnished and accepted.
- **Creditor garnishment (trustee process)** (12 V.S.A. 3170) [US-VTS5-021]:
  - Exempt: the greater of 75% of weekly disposable earnings or 30 × the federal minimum wage.
  - **Consumer-credit debts:** the greater of **85%** or 40 × the federal minimum wage is exempt, so at most 15% is attachable. This is stricter than CCPA.
  - No order against recent DCF/DVHA assistance recipients. Waiver is void. No discharge for trustee process (3172).
- **Child-support IWO** (15 V.S.A. 787) [US-VTS5-023]:
  - Forward to the registry within **7 working days**.
  - The employer may retain **5.00 USD/month** as a fee.
  - Start within 10 working days of notice or at the next payday, whichever is later.
  - Notify termination within 10 days.
  - CCPA 303(b) limit. Combined remittance allowed.
- **Medical support** (33 V.S.A. 4110(a)): enrol the child, withhold the premium share, notify the insurer within 10 days [US-VTS5-014].
- **State tax levies:** not researched (Q10).
- Confidence: 85%.

## 10. collective_agreements (prevailing wage)
- 29 V.S.A. 161(b) [US-VTP51-011, re-read in full]:
  - Applies to State construction projects over **100,000 USD**, or over 200,000 USD when at least 50% funded by a capital construction act or the Cash Fund.
  - Workers get at least the **mean prevailing wage** from the VDOL occupational employment and wage survey, **plus a 42.5% fringe benefit**.
  - Agency of Transportation and Forests/Parks projects are excluded.
- No certified-payroll filing duty appears in 161.
- Confidence: 80%.

## 11. indexation
| Item | Mechanism | Publication | register_id |
|---|---|---|---|
| Minimum wage | min(5%, CPI-U), 1 Jan, round 0.01; tipped = 50% | VDOL press release (Oct) | US-VTS5-001, -003 |
| UI wage base | % change in State annual average wage, 1 Jan (conditional; −2,000 at schedule III/I) | VDOL press release (Oct) | US-VTS5-005, -004 |
| UI rate schedule | fund ratio / highest benefit cost rate, rate year from 1 Jul | VDOL rate notice | US-VTS5-006 |
| PIT brackets | CPI-U, federal method, yearly | GB-1210-{year} (expires 31 Dec) | US-VTS5-018, -016 |
| Withholding allowance | annual table (5,400 in 2026) | GB-1210-{year} | US-VTS5-016 |

## 12. data_protection
- 9 V.S.A. 2440 (SSN Protection Act) [US-VTS5-015]:
  - No SSN on materials mailed to the individual unless law requires it there.
  - Never visible on a postcard or an unopened envelope.
  - No Internet transmission unless secure or encrypted.
  - A redacted SSN is outside the prohibition.
- **For the pay statement:** a full SSN on a mailed payslip is not allowed. A truncated or redacted SSN is permitted.
- Confidence: 85%. The breach-notice statute (9 V.S.A. 2435) was not read.

## 13. live_legal_change (2026-01-01 → 2026-11-02)
- 21 V.S.A. 384 last amended by 2025 No. 91 (Adj. Sess.) §109, eff. **2026-04-30**. The text read is current; the substance of the amendment was not isolated [US-VTS5-001].
- 21 V.S.A. 383 amended by 2025 No. 177 (Adj. Sess.) §8d, eff. **2026-06-18**. Current text read [US-VTS5-013].
- Act 32 of 2025 (eff. 2025-07-01) broadened 472 leave reasons: bereavement, safe leave, exigency [US-VTS5-026].
- **Not located:**
  - 2027 minimum wage;
  - 2027 UI wage base;
  - GB-1210-2027 (expected December 2026).
- **VT Saves** (state auto-IRA, payroll deduction 5% default) is reported by tier-B leads to reach employers with 5 or more employees by 2026-07-01. **Unverified.** The Treasurer page and the statute were unreachable (ACCESS, Q11). Registered as no row.
- A full bulletin sweep (C41) was not possible: tax.vermont.gov and labor.vermont.gov news pages return 403, and Wayback has no 2026 captures of the VDOL release index.
- Confidence: 60%.

## Special populations (US-OWN-005, state round)
| Population | Vermont rule | register_id |
|---|---|---|
| Domestic / household | Excluded from min wage/OT (383(2)(B)). UI covered at 1,000+ cash wages per quarter. Withholding follows federal | US-VTS5-013, US-VTS5-009, US-VTS5-016 |
| Agricultural | Excluded from min wage/OT (383(2)(A)). UI covered at 20,000+ wages per quarter or 10+ workers | US-VTS5-013, US-VTS5-009 |
| Minors | Not covered by earned sick time if under 18 (481(5)(F)). Child-labour hours/permits (21 V.S.A. 430 ff.) not read | US-VTS5-011 |
| Tipped | Basic wage 50% of minimum (7.21 in 2026) for hotel/motel/tourist/restaurant staff with more than 120 USD/month in tips. Employer tops up. Tip reports kept 3 years | US-VTS5-001, -003, US-VTP9-001 |
| Clergy / religious | No state rule beyond federal (withholding follows federal-withholding wages). Some religious-organisation services exempt from UI | US-VTS5-016, US-VTS5-009 |
| Students | Excluded from min wage/OT while working in the school year or regular vacations (383(2)(I)). UI exempt: students at their own school, work-experience programs, some summer camps | US-VTS5-013, US-VTS5-009 |
| Nonresident aliens | No state rule beyond federal. State residency rules apply (hours ratio) | US-VTS5-016 |
| Statutory employees | No state rule beyond federal located (GB-1210 ties to federal withholding) | US-VTS5-016 |
| Government employees | Min wage excludes US employees and municipal officers. OT excludes political subdivisions and FLSA-covered State staff. Earned sick time excludes federal and exempt State service. UI: State reimburses benefits, political subdivisions contribute or elect reimbursement (1321(d)-(e)) | US-VTS5-013, -001, -011, -005 |
| Owners / officers / LLC members | Earned sick time excludes WC-excluded owners/officers. UI excludes multi-member LLC members unless an IRS election is filed | US-VTS5-011, US-VTS5-009 |
| J-1 visa holders | Exempt from UI with documentation | US-VTS5-009 |
| Commission salespeople | Min wage excludes outside salespersons (383(2)(H)). UI excludes commission-only insurance agents and licensed salesmen | US-VTS5-013, US-VTS5-009 |

## ACCESS gaps (exact URLs)
- https://tax.vermont.gov/business/withholding — 403 (VPN off). Live editions of GB-1210, W-4VT and WHT-436 not confirmed.
- https://labor.vermont.gov/unemployment-insurance/ui-employers/unemployment-tax-rates — 403. The latest Wayback 200 capture is 2025-07-15; the 2025-12 and 2026-02 captures are 403.
- https://labor.vermont.gov/press-release/vermont-department-labor-announces-minimum-wage-increase-starting-january-2027 — no capture (and direct 403).
- https://labor.vermont.gov/press-release/vermont-department-labor-announces-unemployment-insurance-taxable-wage-base-2027 — no capture.
- https://www.vermonttreasurer.gov/node/4603 (VT Saves) — 403, no Wayback 200.
- https://legislature.vermont.gov/Documents/2026/Docs/ACTS/ACT091/ , …/ACT177/ — Wayback CDX "Temporarily Offline" during the run.
- legislature.vermont.gov direct — timeout (code 000). All statutes were read via Wayback.

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **vt.minwage.hourly.next_year** (blocking): 2027 VT minimum wage not located. What would close it: VDOL October press release or BLS CPI-U Aug-Aug % for derivation.
- **vt.sui.wage_base.next_year** (non-blocking): 2027 UI wage base not located. What would close it: VDOL wage-base release for 2027.
- **vt.ui.wage_base.derivation** (non-blocking): G-DERIVE of 14,800 -> 15,400 not possible (1338(g) average wage not fetched). What would close it: VDOL state annual average wage figures.
- **vt.ui.schedule.rate_year_2026_07** (non-blocking): Schedule I-V for the rate year from 2026-07-01 not confirmed. What would close it: Live VDOL tax-rates page or employer rate notice.
- **vt.report.w2.format** (non-blocking): VT W-2 electronic file format not stated. What would close it: myVTax W-2 upload specification.
- **vt.payslip.electronic** (non-blocking): Electronic pay statement consent rule not found. What would close it: VDOL Wage and Hour statement or rule text.
- **vt.leave.pfla.thresholds** (non-blocking): 471 thresholds post-Act 32 may be outdated (US-VTS5-027 partial). What would close it: Current 21 V.S.A. 471 or Act 32 As Enacted PDF.
- **vt.leave.est.multistate** (non-blocking): ESTA reach for partly-in-VT workers not stated. What would close it: VDOL ESTA FAQ.
- **vt.term.warn** (non-blocking): 21 V.S.A. 411-419 not read. What would close it: Statute text.
- **vt.garn.state_levy** (non-blocking): Department of Taxes wage levy not read. What would close it: 32 V.S.A. levy provisions.
- **vt.bik.vt_saves** (non-blocking): VT Saves auto-IRA employer mandate is tier-B only; nothing registered. What would close it: Treasurer page and enabling statute.
- **vt.live.bulletin_sweep** (non-blocking): VDOL/Tax news 403; GB-1210-2027 expected Dec 2026. What would close it: VPN-on or browser pass.
- **vt.sui.employee.rate** (non-blocking): No-employee-contribution statement sat on US-VTP51-007, superseded by US-VTS5-009, which does not restate it. What would close it: Re-register the VDOL employer page statement (or 21 V.S.A. 1321 ff.) as an active row.
