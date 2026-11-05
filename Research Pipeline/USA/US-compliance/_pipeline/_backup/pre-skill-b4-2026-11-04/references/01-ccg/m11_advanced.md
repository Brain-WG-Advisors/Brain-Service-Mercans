# Module 11: Advanced Scenarios & Cross-Cutting Logic

*Purpose: To capture complex, overarching rules that affect multiple aspects of payroll.*

## 11.1 Calculation Logic

### How is the proration and projection logic applied for income tax, social security, exemptions, and deductions?

- **Income tax: projection, not proration.** The federal method annualises the period wage by the number of pay periods (2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)) [US-FEDS5-001], applies the annual tables and divides by the periods (IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked)) [US-FEDS5-001]. There is no cumulative true-up. A part-period pay (joiner or leaver) is withheld on the wages actually paid with the normal period frequency. Most State formulas follow the same pattern (Module 12, 12.2.2).
- **Exemptions and allowances:** annual amounts divided by the periods. Example: Michigan's annual exemption 5,900 becomes 226.92 biweekly [US-MIS5-019].
- **Social security:** no proration and no projection. OASDI applies to wages paid up to the annual base (184,500) per employer. FUTA applies to the first 7,000. Each period takes the rate × the lesser of the remaining base and the period wage (Module 12, Scenario C).
- **Deductions:** garnishment limits are per pay period (Module 7). Plan limits (401(k), HSA) are annual caps applied cumulatively.

### If tax or contribution rates change mid-pay period, which rates apply?

The rates and tables in force on the **payment date** apply to the whole payment (calendar year (W-2 on calendar-year basis)) [US-FED-006]. A December-earned wage paid in January takes the new year's federal rates and bases [US-FEDS5-005]. Exception: Massachusetts PFML applies to wages earned on or after 1 January [US-MAS5-012].

**Mid-year 2026 changes to date by payment date (Table 11.1.1)**

| Change | Value | Source |
|---|---|---|
| Georgia income tax | Withholding rate 5.19% for payments to 2026-05-10, 4.99% from 2026-05-11; tax year 2026 assessment rate 4.99% (retroactive to 1 January); law in force (signed 2026-05-11, retroactive 2026-01-01); levels withholding + assessment (rate), assessment + reporting (subtractions). Withholding examples dated from 2026-05-11 (Module 12) | [US-GA-001] [US-GAS5-009] |
| Ohio withholding tables | Effective 2026-08-01 | [US-OHS5-001] |
| Indiana county rates | County rates may change in January and October (DN#1 R47/10-26 from 2026-10-01) | [US-INS5-009] |
| Idaho single zero bracket (biweekly) | 577 (2025-04-28 to 2026-07-22); 619 (from 2026-07-23) | [US-IDS5-011] |
| Philadelphia wage tax (resident / nonresident) | 3.74 (2025-07-01 to 2026-06-30); 3.735 (from 2026-07-01) / 3.43 (2025-07-01 to 2026-06-30); 3.425 (from 2026-07-01) | [US-PAS5-022] |
| District of Columbia minimum wage | 17.95 (2025-07-01 to 2026-06-30); 18.40 (from 2026-07-01) | [US-DCS5-011] |
| Oregon standard minimum wage | 15.05 (2025-07-01 to 2026-06-30); 15.55 (2026-07-01 to 2027-06-30) | [US-ORS5-002] |
| Trump-account employer contribution exclusion | 2,500 (from 2026-07-04) | [US-FEDS5-030] |

### How are tax and social security handled when an employee is paid multiple times in a single pay period?

- **FIT:** a second payment in the period is a supplemental wage. Either withhold the optional flat 22% on it (if identified separately), or aggregate it with the regular wages of the period and withhold on the total [US-FEDS5-003]. Aggregate procedure: Supplemental wages identified separately, income tax withheld from regular wages in the current or preceding year: either flat 22% or aggregate - add the supplemental wages to the concurrently paid regular wages (or, if none, to the regular wages of the current or preceding payroll period), figure the tax as if one regular-period payment, subtract the tax withheld or to be withheld from the regular wages, withhold the remainder; earlier supplemental payments of the same period are aggregated too. No income tax withheld from regular wages in the current or preceding year: aggregate method only. Supplemental wages paid with regular wages without specifying each amount: withhold on the total as one regular payment. [US-FEDQ1-002].
- **FICA and FUTA:** computed payment by payment against the cumulative annual bases. OASDI is the rate × the lesser of the remaining base and the payment. Additional Medicare applies to the part of the cumulative wages above 200,000 [US-FEDS5-005].

### How is payroll calculated if an employee's pay cycle changes mid-year?

Each payment uses the pay-period table of its own frequency (2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily)) [US-FEDS5-001]. Annual wage bases are unaffected because they run on wages paid. Not configured in this release (open gap RQ-532): The IRS rule for a change of payroll period within the year, or for a short transitional period, is not established from an official source.

## 11.2 Special Employee Groups & Income

### How does taxation and social security differ for part-time employees and Board of Directors?

- **Part-time employees:** no separate regime. Withholding uses the same method on the wages of the period; FICA applies from the first dollar. Part-time hours count toward the ACA full-time-equivalent test (50 (partial source)) [US-FEDS5-012] (Module 12, Scenario B).
- **Corporate officers** are employees. Their wages take FIT withholding, FICA and FUTA, and State law includes officers for withholding (Oklahoma [US-OKS5-010]) and for UI coverage. **Directors' fees** paid to a non-employee director are not wages and fall outside payroll (self-employment income). **Statutory employees:** FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only [US-FEDR3-005].

### How is taxation handled for employees with multiple employers?

Each employer withholds and applies the wage bases on its own. The OASDI and FUTA bases are per employer. Additional Medicare starts at 200,000 of wages paid by that employer. Excess OASDI from several employers is refunded at assessment. The employee coordinates FIT through W-4 Step 2. When Step 2 is checked, the Step-2-checked schedule applies and the line 1g amount (8,600 / 12,900) is not subtracted [US-FEDS5-001]. Not configured in this release (open gap RQ-533): Common-paymaster relief for related employers (IRC 3121(s)) is not established from an official source.

### What is the treatment of foreign-sourced employment income for residents?

- **Federal:** US citizens and residents are taxed on worldwide wages. For a US citizen working abroad the employer may stop FIT withholding on a Form 673 statement (Employer may stop FIT withholding on Form 673 statement (FEIE/housing); citizens only) [US-FEDR3-007]. The foreign earned income exclusion for 2026 is 132,900 [US-FED-025]. FICA follows its own coverage rules.
- **State:** No general federal rule: each State taxes residents on all wages (credit at assessment for tax paid to the work State) and nonresidents on wages for services performed in the State; federal limits only for transport workers and military spouses. 4 U.S.C. 114 is retirement income only, not wages. [US-MULTIQ1-001].

### How do employer stock option plans work and how are they taxed?

- **Federal, resident employee:** Resident employee, 2026: (1) Nonstatutory option (NSO): the spread at exercise (FMV - price) is wages - a taxable fringe benefit subject to the supplemental-wage rules (22% optional flat or aggregate; 37% on supplemental wages above 1,000,000), FICA and FUTA wages, timed at the actual exercise (transfer) date; W-2 boxes 1, 3 (to the SS base), 5 and box 12 code V. (2) ISO and ESPP options: no FICA or FUTA at grant, exercise or disposition; no FIT withholding required on a disqualifying disposition or on the ESPP discount at a qualifying disposition, but the ordinary income is W-2 box 1 wages. (3) Restricted stock (actual shares subject to forfeiture): FMV minus amount paid is wages when substantially vested (or at transfer with an 83(b) election). (4) RSU (legally binding right to receive shares in a future year): FICA and FUTA wages at the later of service performance and vesting (special timing rule, 26 CFR 31.3121(v)(2)-1 / 31.3306(r)(2)-1); FIT withholding when the shares are delivered (settlement) as supplemental wages. (5) 83(i) election (private company): FIT deferred up to 5 years and withheld at 37% when included; FICA/FUTA not deferred; W-2 codes GG/HH. [US-FEDQ1-001].
- **Nonstatutory option spread:** reported with W-2 box 12 code V [US-FEDQ1-001].
- **ISO and ESPP:** FICA and FUTA do not apply at grant, exercise or disposition, and income-tax withholding is not required on a disqualifying disposition [US-FEDQ1-001].
- **RSU timing for FICA and FUTA:** Later of the performance of the services and the date the right is no longer subject to a substantial risk of forfeiture (vesting); FUTA follows the same rule [US-FEDQ1-004].
- **Federal, nonresident alien employee:** Nonresident alien employee, 2026: equity income is wages subject to graduated withholding as for residents, with the Pub. 15-T NRA add-on, except that no add-on applies when the payment is withheld at the 22% optional or 37% mandatory flat supplemental rate. Only the U.S.-source part is wages for U.S. withholding: compensation attributable to several years is sourced on a time basis (U.S. workdays / total workdays over the period to which it is attributable, facts and circumstances). FICA/FUTA follow the resident rules (NSO spread and RSU at vesting are FICA wages) unless the employee is exempt as an F-1/J-1/M-1/Q nonimmigrant. Reporting on Form W-2; Form 1042-S only for wages exempt under a treaty claimed on Form 8233. [US-FEDQ1-006].
- **State example:** California withholds bonuses and stock-option income at 10.23% [US-CAS5-004].

### How is payroll handled for employees who transfer between different legal entities mid-year?

Each legal entity (EIN) is a separate employer. Wage bases restart at the new entity, and each entity files its own 941 and W-2. A successor employer that acquires the business may count the predecessor's wages toward the FUTA base [US-FED-007]. Not configured in this release (open gap RQ-533): Common-paymaster relief and the OASDI successor rule for related entities are not established from an official source.

### What is the process for an employee who changes citizenship or residency status during the fiscal year?

- **State residency change:** from the move date, the new residence State's rules apply to wages paid. Withholding follows the new State routing (residence/work State, reciprocity certificates such as REV-419 in Pennsylvania [US-MULTI-007]). The employee files new State certificates. The resident credit for tax paid to another State is generally taken at assessment (e.g. Arizona: assessment) [US-AZWH-003].
- **Nonresident alien becoming a resident alien:** Not configured in this release (open gap RQ-535): The withholding change when an employee's federal status changes from nonresident alien to resident alien during the year is not established from an official source.

### Are there specific rules for expatriates or inpatriates?

**Inpatriates (nonresident aliens working in the US):**

| Rule | Value | Source |
|---|---|---|
| Form W-4 | Check Single or MFS regardless of marital status; write NRA below Step 4(c); exempt not allowed; Step 3 only for residents of Canada, Mexico, South Korea or India (students/apprentices) | [US-FEDS5-015] |
| Add-on to wages for the FIT computation (2020+ W-4, annual) | 16,100 | [US-FEDS5-002] |
| Add-on (pre-2020 W-4, annual) | 11,800 | [US-FEDS5-002] |
| Treaty-exempt wages | Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS | [US-FEDS5-016] |
| Commercial traveler exception | Present at most 90 days and paid at most 3,000 | [US-FEDS5-016] |

**Expatriates (US citizens abroad):** Form 673 and the FEIE, as above [US-FEDR3-007].

### Special treatments by worker category

| Category | Treatment | Source |
|---|---|---|
| Statutory employees | FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only | [US-FEDR3-005] |
| Ministers | No FIT, social security or Medicare withholding (SE tax; voluntary FIT withholding agreement allowed); parsonage allowance excluded from W-2 box 1 | [US-FED-030] |
| Household employees | FICA from 3,000 cash wages in the year; FUTA from 1,000 in a quarter | [US-FEDS5-029] |
| Agricultural workers | FICA where a worker is paid 150 or more, or total pay reaches 2,500; FUTA from 20,000 in a quarter | [US-FEDR3-006] |
| Family employees | Child under 18 of a sole proprietor/parents-only partnership: FICA exempt, FUTA exempt under 21; spouse: FUTA exempt; parent employed by child: FUTA exempt | [US-FEDS5-029] |
| Students | Private school/college students: FIT withheld, FICA and FUTA exempt; public school: FICA exempt unless sec. 218 agreement; work-experience full-time student: FICA taxable | [US-FEDS5-029] |
| Government employees | FIT withheld; no FUTA; FICA with sec. 218 / Medicare-only exceptions | [US-FEDS5-029] |
| Election workers | FICA from 2,500 in the year | [US-FEDS5-003] |
| Military spouses (State tax) | A military spouse present in a State solely to be with the servicemember under military orders neither loses nor acquires residence or domicile; the spouse's income for services performed in that State is not income for services performed or from sources within that State if the spouse is not a resident of it; for any taxable year the spouse may elect the residence of the servicemember, the spouse's own residence or the permanent duty station (50 U.S.C. 4001(a)(2), (c)). Payroll effect: on the employee's State certificate of nonresidence, stop work-State withholding. | [US-MULTIS5-005] |

### Fringe benefit exclusions (2026)

| Benefit | Federal exclusion | Source |
|---|---|---|
| Qualified parking | 340 per month | [US-FEDS5-008] |
| Transit pass / commuter vehicle | 340 per month | [US-FEDS5-008] |
| Dependent care assistance | 7,500 per year | [US-FEDS5-008] |
| Educational assistance | 5,250 per year | [US-FEDS5-008] |
| Group-term life insurance | Coverage up to 50,000; the cost of coverage above it is FICA wages | [US-FEDS5-008] |
| Trump-account employer contribution | Up to 2,500 (from 2026-07-04) | [US-FEDS5-030] |
| Moving expenses and bicycle commuting | Not excluded (taxable wages) | [US-FEDS5-008] |
| Business mileage reimbursement | Not configured in this release (open gap RQ-536): The 2026 IRS business standard mileage rate is not established from an official source (it is not printed in Pub. 15-B). | — |

ACA affordability percentage for 2026: 9.96% [US-FEDS5-011].

The population coverage matrix (federal and multistate cut of every special population) follows as §11.3.


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `ca.wh.supplemental.rate.bonus_stock_options` | 10.23 | from 2026-01-01 | US-CAS5-004 |
| `dc.minwage.hourly` | 17.95 | from 2025-07-01 to 2026-06-30 | US-DCS5-011 |
| `dc.minwage.hourly` | 18.40 | from 2026-07-01 | US-DCS5-011 |
| `fed.aca.affordability.rate` | 9.96 | from 2026-01-01 to 2026-12-31 | US-FEDS5-011 |
| `fed.aca.ale.fte_threshold` | 50 | from 2025-01-01 | US-FEDS5-012 |
| `fed.agricultural.futa_quarter_threshold` | 20,000 | from 2026-01-01 | US-FEDR3-006 |
| `fed.agricultural.per_worker_threshold` | 150 | from 2026-01-01 | US-FEDR3-006 |
| `fed.agricultural.total_threshold` | 2,500 | from 2026-01-01 | US-FEDR3-006 |
| `fed.bik.dependent_care.exclusion` | 7,500 | from 2026-01-01 | US-FEDS5-008 |
| `fed.bik.educational_assistance.exclusion` | 5,250 | from 2026-01-01 | US-FEDS5-008 |
| `fed.bik.group_term_life.excluded_coverage` | 50,000 | from 2026-01-01 | US-FEDS5-008 |
| `fed.bik.parking.monthly_exclusion` | 340 | from 2026-01-01 | US-FEDS5-008 |
| `fed.bik.transit.monthly_exclusion` | 340 | from 2026-01-01 | US-FEDS5-008 |
| `fed.bik.trump_account.employer_contribution_max` | 2,500 | from 2026-07-04 | US-FEDS5-030 |
| `fed.citizen_abroad.form673` | Employer may stop FIT withholding on Form 673 statement (FEIE/housing); citizens only | from 2026-01-01 | US-FEDR3-007 |
| `fed.election_worker.fica_threshold` | 2,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-003 |
| `fed.equity.nso.w2_code` | V | from 2026-01-01 | US-FEDQ1-001 |
| `fed.equity.rsu.fica_timing` | Later of the performance of the services and the date the right is no longer subject to a substantial risk of forfeiture (vesting); FUTA follows the same rule | from 2026-01-01 | US-FEDQ1-004 |
| `fed.equity.withholding_treatment.nonresident` | Nonresident alien employee, 2026: equity income is wages subject to graduated withholding as for residents, with the Pub. 15-T NRA add-on, except that no add-on applies when the payment is withheld at the 22% optional or 37% mandatory flat supplemental rate. Only the U.S.-source part is wages for U.S. withholding: compensation attributable to several years is sourced on a time basis (U.S. workdays / total workdays over the period to which it is attributable, facts and circumstances). FICA/FUTA follow the resident rules (NSO spread and RSU at vesting are FICA wages) unless the employee is exempt as an F-1/J-1/M-1/Q nonimmigrant. Reporting on Form W-2; Form 1042-S only for wages exempt under a treaty claimed on Form 8233. | from 2026-01-01 | US-FEDQ1-006 |
| `fed.equity.withholding_treatment.resident` | Resident employee, 2026: (1) Nonstatutory option (NSO): the spread at exercise (FMV - price) is wages - a taxable fringe benefit subject to the supplemental-wage rules (22% optional flat or aggregate; 37% on supplemental wages above 1,000,000), FICA and FUTA wages, timed at the actual exercise (transfer) date; W-2 boxes 1, 3 (to the SS base), 5 and box 12 code V. (2) ISO and ESPP options: no FICA or FUTA at grant, exercise or disposition; no FIT withholding required on a disqualifying disposition or on the ESPP discount at a qualifying disposition, but the ordinary income is W-2 box 1 wages. (3) Restricted stock (actual shares subject to forfeiture): FMV minus amount paid is wages when substantially vested (or at transfer with an 83(b) election). (4) RSU (legally binding right to receive shares in a future year): FICA and FUTA wages at the later of service performance and vesting (special timing rule, 26 CFR 31.3121(v)(2)-1 / 31.3306(r)(2)-1); FIT withholding when the shares are delivered (settlement) as supplemental wages. (5) 83(i) election (private company): FIT deferred up to 5 years and withheld at 37% when included; FICA/FUTA not deferred; W-2 codes GG/HH. | from 2026-01-01 | US-FEDQ1-001 |
| `fed.family_employment.treatment` | Child under 18 of a sole proprietor/parents-only partnership: FICA exempt, FUTA exempt under 21; spouse: FUTA exempt; parent employed by child: FUTA exempt | from 2026-01-01 | US-FEDS5-029 |
| `fed.feie.amount` | 132,900 | from 2026-01-01 to 2026-12-31 | US-FED-025 |
| `fed.fica.addl_medicare.withholding_threshold` | 200,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 184,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fit.method` | IRS Pub. 15-T (2026) Worksheet 1A with the Annual Percentage Method tables (STANDARD schedule; Step-2-checked schedule when W-4 Step 2 box checked) | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.nra.addon.table1.annual` | 11,800 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.addon.table2.annual` | 16,100 | from 2026-01-01 to 2026-12-31 | US-FEDS5-002 |
| `fed.fit.nra.commercial_traveler.max_days` | 90 | from 2026-01-01 | US-FEDS5-016 |
| `fed.fit.nra.commercial_traveler.max_pay` | 3,000 | from 2026-01-01 | US-FEDS5-016 |
| `fed.fit.nra.treaty_exempt.reporting` | Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS | from 2026-01-01 | US-FEDS5-016 |
| `fed.fit.nra.w4.rule` | Check Single or MFS regardless of marital status; write NRA below Step 4(c); exempt not allowed; Step 3 only for residents of Canada, Mexico, South Korea or India (students/apprentices) | from 2020-01-01 | US-FEDS5-015 |
| `fed.fit.pay_periods_per_year` | 2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, monthly, semimonthly, biweekly, weekly, daily) | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.supplemental.aggregate_method` | Supplemental wages identified separately, income tax withheld from regular wages in the current or preceding year: either flat 22% or aggregate - add the supplemental wages to the concurrently paid regular wages (or, if none, to the regular wages of the current or preceding payroll period), figure the tax as if one regular-period payment, subtract the tax withheld or to be withheld from the regular wages, withhold the remainder; earlier supplemental payments of the same period are aggregated too. No income tax withheld from regular wages in the current or preceding year: aggregate method only. Supplemental wages paid with regular wages without specifying each amount: withhold on the total as one regular payment. | from 2026-01-01 to 2026-12-31 | US-FEDQ1-002 |
| `fed.fit.supplemental.flat_rate` | 22 | from 2026-01-01 | US-FEDS5-003 |
| `fed.fit.worksheet1a.line1g.mfj` | 12,900 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.fit.worksheet1a.line1g.other` | 8,600 | from 2026-01-01 to 2026-12-31 | US-FEDS5-001 |
| `fed.futa.wage_base` | 7,000 | from 2025-01-01 | US-FED-007 |
| `fed.government_employee.treatment` | FIT withheld; no FUTA; FICA with sec. 218 / Medicare-only exceptions | from 2026-01-01 | US-FEDS5-029 |
| `fed.household.fica_cash_threshold` | 3,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-029 |
| `fed.household.futa_quarter_threshold` | 1,000 | from 2026-01-01 | US-FEDS5-029 |
| `fed.minister.withholding` | No FIT, social security or Medicare withholding (SE tax; voluntary FIT withholding agreement allowed); parsonage allowance excluded from W-2 box 1 | from 2026-01-01 | US-FED-030 |
| `fed.statutory_employee.treatment` | FICA withheld, no FIT withholding; W-2 box 13 checked; FUTA for drivers and traveling salespersons only | from 2026-01-01 | US-FEDR3-005 |
| `fed.students.treatment` | Private school/college students: FIT withheld, FICA and FUTA exempt; public school: FICA exempt unless sec. 218 agreement; work-experience full-time student: FICA taxable | from 2026-01-01 | US-FEDS5-029 |
| `fed.tax_year.basis` | calendar year (W-2 on calendar-year basis) | from 2026-01-01 | US-FED-006 |
| `ga.live.hb463.status` | in force (signed 2026-05-11, retroactive 2026-01-01); levels withholding + assessment (rate), assessment + reporting (subtractions) | from 2026-01-01 | US-GAS5-009 |
| `ga.pit.rate.flat` | 4.99 | from 2026-01-01 | US-GAS5-009 |
| `ga.wh.rate` | 4.99 | from 2026-05-11 | US-GAS5-009 |
| `ga.wh.rate` | 5.19 | from 2026-01-01 to 2026-05-10 | US-GA-001 |
| `id.wh.zero_bracket.single.biweekly` | 577 | from 2025-04-28 to 2026-07-22 | US-IDS5-012 |
| `id.wh.zero_bracket.single.biweekly` | 619 | from 2026-07-23 | US-IDS5-011 |
| `in.county.change_dates` | County rates may change in January and October (DN#1 R47/10-26 from 2026-10-01) | from 2026-01-01 | US-INS5-009 |
| `mi.wh.exemption.annual` | 5,900 | from 2026-01-01 to 2026-12-31 | US-MIS5-015 |
| `mi.wh.exemption.biweekly` | 226.92 | from 2026-01-01 to 2026-12-31 | US-MIS5-019 |
| `multi.military_spouse.rule` | A military spouse present in a State solely to be with the servicemember under military orders neither loses nor acquires residence or domicile; the spouse's income for services performed in that State is not income for services performed or from sources within that State if the spouse is not a resident of it; for any taxable year the spouse may elect the residence of the servicemember, the spouse's own residence or the permanent duty station (50 U.S.C. 4001(a)(2), (c)). Payroll effect: on the employee's State certificate of nonresidence, stop work-State withholding. | from 2018-12-31 | US-MULTIS5-005 |
| `multi.pit.sourcing.general` | No general federal rule: each State taxes residents on all wages (credit at assessment for tax paid to the work State) and nonresidents on wages for services performed in the State; federal limits only for transport workers and military spouses. 4 U.S.C. 114 is retirement income only, not wages. | from 2026-01-01 | US-MULTIQ1-001 |
| `multi.reciprocity.pa.certificate` | REV-419 | from 2026-01-01 | US-MULTI-007 |
| `multi.resident_credit.az.level` | assessment | from 2026-01-01 | US-AZWH-003 |
| `oh.wh.tables.effective_from` | 2026-08-01 | from 2026-08-01 | US-OHS5-001 |
| `or.labour.minwage.standard.hourly` | 15.05 | from 2025-07-01 to 2026-06-30 | US-ORS5-002 |
| `or.labour.minwage.standard.hourly` | 15.55 | from 2026-07-01 to 2027-06-30 | US-ORS5-002 |
| `pa.local.philadelphia.nonresident.rate` | 3.425 | from 2026-07-01 | US-PAS5-022 |
| `pa.local.philadelphia.nonresident.rate` | 3.43 | from 2025-07-01 to 2026-06-30 | US-PAS5-022 |
| `pa.local.philadelphia.resident.rate` | 3.735 | from 2026-07-01 | US-PAS5-022 |
| `pa.local.philadelphia.resident.rate` | 3.74 | from 2025-07-01 to 2026-06-30 | US-PAS5-022 |
