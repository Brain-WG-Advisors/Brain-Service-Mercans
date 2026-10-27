# Module 7: Deductions, Exemptions & Benefits

*Purpose: To define rules for all items that adjust income or pay.*

## 7.1 Statutory Tax Reliefs, Deductions, and Exemptions

### Deliverable: For EACH statutory tax relief, deduction, exemption, or other tax advantage, provide Name and Definition, Eligibility Rules, Statutory Limits & Amounts, Calculation Method, Application Point, Employee Declaration Requirements

Colombia's reliefs fall into **three legally distinct classes**, and the class determines where each item
sits in the depuration and which caps it consumes. Getting the class wrong is the most common source of
withholding error.

| Class | Legal name | Where deducted | Consumes the 40% / 1,340-unit cap? |
|---|---|---|---|
| **A** | Non-taxable income (*ingresos no constitutivos de renta ni ganancia ocasional*) | Step (B), **before** the cap reference figure is struck | **No** |
| **B** | Deductions (*deducciones*) and exempt income (*rentas exentas*) | Steps (D) and (E) | **Yes** |
| **C** | Outside the cap | After the cap | **No** |

---

**A1 — Mandatory pension contribution**

| Element | Detail |
|---|---|
| **Definition** | The employee's compulsory 4% pension contribution on the social-security contribution base |
| **Eligibility** | Every employee who contributes to pension. Not available to an employed old-age pensioner, who makes no pension contribution |
| **Limit** | 4% of the contribution base, itself capped at 25 minimum wages = COP 43,772,625 → maximum COP 1,750,905 per month |
| **Calculation** | 4% × contribution base, rounded up to the nearest 100 |
| **Application point** | Step (B), non-taxable income |
| **Declaration** | None — computed by the engine |
| **Source** | Tax Code art. 55 |

**A2 — Solidarity pension fund contribution**

| Element | Detail |
|---|---|
| **Definition** | The employee-only surcharge funding the solidarity and subsistence sub-accounts |
| **Eligibility** | Contribution base ≥ 4 minimum wages (COP 7,003,620) for the 1% solidarity account; ≥ 16 minimum wages for the banded 0.2%–1.0% subsistence account |
| **Limit** | 1.0% to 2.0% of the contribution base |
| **Calculation** | Banded — see Module 5.1.1 |
| **Application point** | Step (B), non-taxable income. **Confirmed** by field 24 of the information return, which groups the pension and solidarity contributions on a single line |
| **Declaration** | None |
| **Source** | Tax Code art. 55; Law 100 of 1993 art. 20 |

**A3 — Mandatory health contribution**

| Element | Detail |
|---|---|
| **Definition** | The employee's compulsory 4% health contribution |
| **Eligibility** | Every employee |
| **Limit** | 4% of the contribution base, maximum COP 1,750,905 per month |
| **Calculation** | 4% × contribution base, rounded up to the nearest 100 |
| **Application point** | Step (B) |
| **Declaration** | None |
| **Source** | Tax Code art. 56 |

**A4 — Voluntary contributions to the individual pension account**

| Element | Detail |
|---|---|
| **Definition** | Voluntary contributions made by the employee, or by the employer on the employee's behalf, to the employee's individual account in the private pension regime |
| **Eligibility** | Employees affiliated to the private individual-account regime |
| **Limit** | The lower of **25% of annual labour income** and **2,500 tax units** = COP 130,935,000 per year |
| **Calculation** | Deducted at the amount contributed, within the cap |
| **Application point** | Step (B) — **more valuable than exempt income**, because it is deducted before the 40% cap reference figure is struck |
| **Declaration** | Amount and period, evidenced by a pension administrator certificate |
| **Clawback** | A withdrawal that does not meet the qualifying conditions is **withheld at 35%** |
| **Source** | Tax Code art. 55 |

**A5 — Third-party meal payments**

| Element | Detail |
|---|---|
| **Definition** | Payments made by the employer **to a third party** for the food of the employee or the employee's family, including the purchase of meal vouchers or tickets. *"Familia"* means the spouse or permanent partner, the children and the parents of the employee |
| **Eligibility** | **Two independent conditions, both must hold:** (i) the employee's salary does **not exceed 310 tax units** = COP 16,235,940; and (ii) the payment is made to a **third party** — cash paid to the employee is salary and gets none of this treatment |
| **Limit** | Where the payments in the month exceed **41 tax units** = COP 2,147,334, **the excess is taxable employment income** subject to withholding |
| **Calculation** | Up to 41 tax units: not income to the employee, income to the third party supplying the food. Above 41 tax units: the excess enters the taxable base |
| **Application point** | Step (B) as a non-income exclusion |
| **Declaration** | Employer records; the information return reports the within-limit amount (field 32) and the excess (field 8) **separately** |
| **Excluded** | Representation expenses are expressly outside this rule and are deductible for the employer |
| **Source** | Tax Code art. 387-1 |

---

**B1 — Housing-loan interest and monetary correction**

| Element | Detail |
|---|---|
| **Definition** | Interest and monetary correction paid on a loan for the acquisition of the employee's dwelling, or on a housing leasing contract |
| **Eligibility** | Employees paying qualifying housing-loan interest |
| **Limit** | Monthly cap **100 tax units** = COP 5,237,400 (the monthly figure is derived from the annual 1,200-unit limit of Tax Code art. 119; the monthly apportionment is market practice — see the QA report) |
| **Calculation** | The lower of the amount paid and the cap |
| **Application point** | Step (D), inside the 40% and 1,340-unit caps |
| **Declaration** | Amount paid, evidenced by a lender certificate |
| **Source** | Tax Code arts. 119 and 387 first paragraph |

**B2 — Prepaid medicine and health-insurance premiums**

| Element | Detail |
|---|---|
| **Definition** | Payments for prepaid medicine or health insurance covering the employee, the spouse, the children and the dependants |
| **Eligibility** | The provider must be supervised by the **National Health Superintendence** (prepaid medicine) or the **Financial Superintendence** (health insurance) |
| **Limit** | **16 tax units per month** = COP 837,984 |
| **Calculation** | The lower of the amount paid and the cap |
| **Application point** | Step (D) |
| **Declaration** | Amount paid, evidenced by a provider certificate |
| **Source** | Tax Code art. 387 literals a) and b) |

**B3 — Dependants deduction**

| Element | Detail |
|---|---|
| **Definition** | A deduction of **10% of the month's gross labour income** where the employee has one or more qualifying dependants |
| **Eligibility** | At least one dependant as defined in Tax Code art. 387 par. 2 |
| **Limit** | **32 tax units per month** = COP 1,675,968. Note: the deduction is **10% of gross regardless of the number of dependants** — it does not multiply |
| **Calculation** | min(10% × gross labour income of the month, 1,675,968) |
| **Application point** | Step (D) |
| **Declaration** | The dependants and the basis of dependency |
| **Source** | Tax Code art. 387 |

**Who is a dependant — Tax Code art. 387 par. 2**, numerals 2 and 3 as amended by **Law 2411 of 2024
art. 2**:

| # | Dependant |
|---|---|
| 1 | Children up to 18 |
| 2 | Children aged 18 to 25 whose higher or technical education the taxpayer finances |
| 3 | Children over 18 in a certified state of physical or psychological dependence |
| 4 | Spouse or permanent partner dependent by absence of income, or with annual income **below 260 tax units** (COP 13,617,240) certified by a public accountant, or by certified physical or psychological dependence |
| 5 | Parents and siblings on the same conditions as numeral 4 |

**B4 — Voluntary pension fund and long-term savings account contributions**

| Element | Detail |
|---|---|
| **Definition** | Contributions to voluntary pension funds (art. 126-1) and to construction-savings or long-term-savings accounts (art. 126-4) |
| **Eligibility** | Any employee; employer contributions on the employee's behalf count toward the same cap |
| **Limit** | The lower of **30% of labour income** and **3,800 tax units per year** = COP 199,021,200, **shared** between the two vehicles |
| **Calculation** | Amount contributed within the shared cap |
| **Application point** | Step (E), exempt income, inside the 40% and 1,340-unit caps |
| **Declaration** | Amount and period, evidenced by fund certificates |
| **Employer deduction** | Employer contributions are deductible for the employer up to 3,800 tax units per employee (art. 126-1 first paragraph) |
| **Source** | Tax Code arts. 126-1 and 126-4 |

**B5 — The 25% exempt-income deduction**

| Element | Detail |
|---|---|
| **Definition** | The general labour-income exemption of twenty-five per cent of total labour payments — *"Twenty-five percent (25%) of the total value of the labour payments"* |
| **Eligibility** | Every resident employee. **Not available to a non-resident** withheld under art. 408 |
| **Limit** | **790 tax units per year** = COP 41,375,460; apportioned monthly at 65.8333 units = COP 3,447,955 |
| **Calculation** | **CRITICAL ORDERING — it is computed after every other item has been deducted:** *"The calculation of this exempt income shall be made **once there are subtracted** from the total value of the labour payments received by the employee the income that does not constitute taxable income, the deductions and the other exempt income items other than the one established in the present numeral."* It is computed **LAST**, on the figure net of A, B1–B4 |
| **Application point** | Step (E), last item, then subject to the caps |
| **Declaration** | None — automatic |
| **Excluded** | Does not apply to severance savings, to income already excluded by other rules, or to the taxable part of a pension (art. 206 par. 2) |
| **Source** | Tax Code art. 206 num. 10, as amended by Law 2277 of 2022 art. 2 |

**B6 — Severance savings exemption**

| Element | Detail |
|---|---|
| **Definition** | Exemption of statutory severance savings and the interest on them |
| **Eligibility** | Exempt **in full** where the employee's **average monthly income over the last 6 months of employment** does not exceed **350 tax units** = COP 18,330,900 |
| **Limit** | Above that, the untaxed portion tapers: |

| Average monthly salary | Untaxed portion |
|---|---|
| 350 – 410 tax units | 90% |
| 410 – 470 tax units | 80% |
| 470 – 530 tax units | 60% |
| 530 – 590 tax units | 40% |
| 590 – 650 tax units | 20% |
| From 650 tax units | **0%** |

| Element | Detail |
|---|---|
| **Application point** | Severance savings and their interest are **excluded from the monthly withholding base entirely**, under both procedures (Tax Code arts. 385 and 386). The exemption and taper are applied when the payment is made |
| **Declaration** | None; the engine must maintain the rolling 6-month average |
| **Source** | Tax Code art. 206 num. 4 |

**B7 — Pension income exemption**

| Element | Detail |
|---|---|
| **Definition** | Retirement, invalidity, old-age, survivor and occupational-risk pensions |
| **Limit** | Taxable only on the monthly amount exceeding **1,000 tax units** = COP 52,374,000 |
| **Eligibility** | The taxpayer must meet the Law 100 pension-entitlement conditions; the treatment extends to foreign and multilateral-organisation pensions |
| **Source** | Tax Code art. 206 num. 5 and par. 3 |

**B8 — Statutory indemnity exemptions**

| Element | Detail |
|---|---|
| **Definition** | Accident and illness indemnities (num. 1), maternity-protection indemnities (num. 2), and the burial expenses of the employee (num. 3) |
| **Limit** | **Art. 206 par. 1** limits numerals 1, 2, 3, 4 and 6 to the statutory minimum amounts: *"operates only on the amounts corresponding to the statutory minimum … the excess is not exempt"* |
| **Source** | Tax Code art. 206 nums. 1–3 and par. 1 |

---

**C1 — The additional dependants deduction**

| Element | Detail |
|---|---|
| **Definition** | A deduction of **72 tax units per dependant per year**, maximum **4 dependants** |
| **Eligibility** | Dependants as defined in art. 387 par. 2 |
| **Limit** | 72 tax units = COP 3,770,928 per dependant per year; maximum 4 dependants = COP 15,083,712 per year; monthly 6 tax units = COP 314,244 per dependant |
| **Calculation** | Deducted **after and outside** the 40% and 1,340-unit caps — *"in addition to the limit established in the preceding paragraph"* |
| **Application point** | Step (G), outside the caps |
| **Declaration** | Number of dependants and **each dependant's identity document**, relationship and basis of dependency. The information return (field 34) requires the document, not merely a count |
| **Stacking** | **May be taken together with B3 for the same dependant.** Decree 2231 of 2023 art. 3: *"the same dependant shall give rise to only one of these two deductions, **except where the taxpayer has income from an employment or statutory and regulatory relationship, in which case both deductions may be applied for the same dependant**"* |
| **Source** | Tax Code art. 336 num. 3, second paragraph; Decree 2231 of 2023 art. 3 |

---

**Not available against withholding.** The 1% / 240-tax-unit invoice-based deduction of Tax Code
art. 336 num. 5 is expressly excluded — *"shall not be taken into account for the calculation of withholding at
source"* — confirmed by **DIAN Concepto 015007 (int. 973) of 13 September 2023**: *"this deduction is
confined to the determination of the net income of the general basket and does not apply for the purposes of withholding
at source."* It is available only in the employee's own annual return.

**Outside the caps by statute, but outside Mercans scope.** Tax Code art. 206 par. 4 and Decree 1625 of
2016 art. 1.2.4.1.6 par. 3 place numerals 6 to 9 of art. 206, the *prima especial* and the *prima de costo
de vida* outside the 40% and 1,340-unit limits. These attach to military, judicial, diplomatic and public
university staff — out of Mercans private-sector scope — but the engine must carry the flag so that it does
not silently clamp them if such an employee is loaded.

### Are salary sacrifice arrangements allowed?

**There is no salary-sacrifice regime in Colombian law**, and the nearest Colombian equivalents work in a
materially different way.

| Arrangement | Available? | Effect |
|---|---|---|
| **Classic salary sacrifice** — the employee gives up contractual salary in exchange for a non-cash benefit, reducing both the tax and the contribution base | **No.** There is no statutory mechanism, no tax-authority-approved structure and no doctrine supporting it. Labour Code art. 13 makes the minimum labour rights irrenounceable, and art. 143 presumes any differential remuneration unjustified | — |
| **Non-salary pact** (Labour Code art. 128) — the parties agree in writing that a *benefit or allowance* is not salary | **Yes**, and this is the Colombian workhorse. But it is **not** a sacrifice: the employee gives up nothing, and the payment must genuinely be a benefit or allowance, not consideration for the service | Removes the payment from the statutory-benefit base, the overtime base and the contribution base — **but only up to the 40% clamp of Law 1393 of 2010 art. 30**. **No tax effect whatsoever**: the payment remains fully taxable employment income |
| **Employer contributions to voluntary pension funds** | **Yes** | Exempt income to the employee within the shared 30% / 3,800-unit cap; deductible for the employer up to 3,800 units per employee |
| **Employer contributions to the individual pension account** | **Yes** | Non-taxable income to the employee within the 25% / 2,500-unit cap |
| **Third-party meal payments and vouchers** | **Yes** | Not income to the employee within the art. 387-1 thresholds |
| **Salary in kind** (Labour Code art. 129) | **Yes**, but it is the **opposite** of a sacrifice — it is salary, fully contributory and fully taxable, capped at 50% of total salary and 30% at the minimum wage |
| **All-inclusive salary** (Labour Code art. 132 num. 2) | **Yes** | Reduces the contribution and payroll-levy bases to **70%** — the closest Colombia comes to a structural contribution reduction, available only above 13 minimum wages |

**The key configuration point.** Colombian benefit structuring is a **social-security** optimisation, never
a tax optimisation. A non-salary pact reduces contributions (within 40%) and statutory benefits; it does
**not** reduce taxable income by one peso. Any engine that treats a non-salary flag as a tax exclusion will
systematically under-withhold.

### List common types of post-tax deductions and any specific ordering rules or limitations.

**Common post-tax deductions**

| Deduction | Written order required? | Notes |
|---|---|---|
| Union dues | **No** — art. 150 | Deducted at the union's request for members |
| Cooperative and employee savings-fund dues | **No** — art. 150, where legally authorised |
| Disciplinary sanctions | **No** — art. 150, but **only** under a duly approved set of work rules |
| **Higher-education solidarity contribution** | **No** — art. 150, added by Law 1911 of 2018 art. 22 |
| Employer loans and salary advances | **Yes** — art. 151, in writing, stating the instalment and the amortisation period |
| Payroll lending (*libranza*) — third-party lender repayments | **Yes** — written authorisation; governed by Law 1527 of 2012 |
| Voluntary insurance premiums | **Yes** |
| Prepaid health and supplementary health plans | **Yes** |
| Voluntary pension and long-term savings contributions | **Yes** |
| Employee-purchased goods and services from the employer | **Yes** |
| **Court-ordered garnishments** | **Court order**, no employee authorisation needed |

**Ordering rules and limits**

Colombia has **no single statutory priority table**, but the rules combine into a clear order:

| Priority | Item | Authority | May breach the minimum wage? |
|---|---|---|---|
| 1 | Mandatory social security (health, pension, solidarity fund) | Statutory — art. 150 | Yes |
| 2 | Withholding tax | Statutory | Yes |
| 3 | Maintenance obligations (*alimentos*) and cooperative debts | Court order / art. 156 | **Yes — up to 50% of the whole salary** |
| 4 | Other court-ordered garnishments | Court order / art. 155 | Only the excess over the minimum wage, up to 20% of that excess |
| 5 | Art. 150 permitted deductions (union dues, cooperative dues, disciplinary sanctions, higher-education contribution) | Statutory | **No** |
| 6 | Payroll lending, in date order of the authorisations | Written authorisation; Law 1527 of 2012 | **No** |
| 7 | Employer loans and advances | Written agreement — art. 151 | **No** |
| 8 | Other voluntary deductions | Written authorisation | **No** |

**The attachability limits — Labour Code arts. 154–156:**

| Rule | Effect |
|---|---|
| Art. 154 | Salary is **not attachable** as a general rule |
| Art. 155 | The **excess over the minimum wage** is attachable up to **one fifth (20%)** of that excess |
| **Art. 156** | **Exception:** for **maintenance obligations** and debts owed to cooperatives, up to **50% of the whole salary**, including the minimum-wage portion, is attachable |

**The overriding limitation — Labour Code art. 149 num. 2.** No deduction or set-off may reduce pay below
the minimum wage or into the non-attachable portion **without a court order, even where the employee has
authorised it in writing**. This governs every voluntary deduction in the table, and is the reason
priorities 5 to 8 carry "No" in the last column.

**Payroll lending specifically.** Law 1527 of 2012 governs *libranza* deductions. The employer must
deduct and remit the instalment to the lender once the authorisation is in place; the aggregate of
libranza deductions must leave the employee with at least **50% of net salary** after all statutory
deductions. Labour Code art. 149 num. 3 makes the employer **liable in damages** for failing to make an
authorised, lawful deduction.

### List any income types that are statutorily exempt from income tax.

| Exempt income | Limit | Source |
|---|---|---|
| **Severance savings and the interest on them** | Full exemption where the average monthly income of the last 6 months ≤ 350 tax units; tapered to nil above 650 units | Tax Code art. 206 num. 4 |
| **Pensions** — retirement, invalidity, old-age, survivor, occupational risk | Taxable only above **1,000 tax units per month** = COP 52,374,000 | Art. 206 num. 5 |
| **Accident and illness indemnities** | Only up to the statutory minimum amount (par. 1) | Art. 206 num. 1 |
| **Maternity-protection indemnities** | Only up to the statutory minimum amount | Art. 206 num. 2 |
| **Burial expenses of the employee** | Only up to the statutory minimum amount | Art. 206 num. 3 |
| **The 25% general labour-income exemption** | 790 tax units per year = COP 41,375,460 | Art. 206 num. 10 |
| **Voluntary pension fund and long-term savings contributions** | 30% of labour income, 3,800 tax units per year | Arts. 126-1, 126-4 |
| **Sickness, maternity and paternity benefits paid by the health insurer** | Within the statutory minimum, under art. 206 nums. 1–2 and par. 1 | Art. 206 |
| **Occupational accident and disease benefits paid by the risk insurer** | Within the statutory minimum | Art. 206 |
| **Third-party meal payments** | Not income up to 41 tax units per month, salary ≤ 310 tax units | Art. 387-1 |
| **Work clothing and footwear** (*dotación*) | In kind, no monetary limit; not consideration for the service | Labour Code arts. 128, 230 |
| **Representation expenses, work tools, protective equipment, means of transport** | Amounts given to enable the work, not to enrich the employee | Labour Code art. 128 |
| **Documented business-expense reimbursement** | Genuine reimbursement of employer expenditure | General principle |

**Not exempt, contrary to a common misconception:** the transport allowance, the connectivity allowance,
the statutory service bonus, vacation pay, overtime and premiums, dismissal indemnities beyond the
statutory-minimum indemnities of art. 206 nums. 1–3, and any bonus however labelled. **A non-salary pact
under Labour Code art. 128 confers no tax exemption of any kind.**

*Legal basis: Tax Code (Decree-Law 624 of 1989) arts. 55, 56, 119, 126-1, 126-4, 206 (nums. 1–5, 10 and
pars. 1, 2, 4), 336 (nums. 3 and 5), 383, 385, 386, 387, 387-1, 388; Law 2277 of 2022 art. 2; Law 2411 of
2024 art. 2; Decree 1625 of 2016 art. 1.2.4.1.6 par. 3 (as modified by Decree 2231 of 2023 art. 9); Decree
2231 of 2023 art. 3; DIAN Concepto 015007 int. 973 of 13 September 2023; Substantive Labour Code arts. 13,
128, 129, 132, 143, 149, 150, 151, 154, 155, 156, 230 (art. 150 as amended by Law 1911 of 2018 art. 22);
Law 1393 of 2010 art. 30; Law 1527 of 2012.*

---

## 7.2 Benefits in Kind (BIK)

### Are non-cash benefits taxed via the standard payroll system, or a separate employer-paid regime?

**Through the standard payroll system.** Colombia has **no fringe-benefits tax**, no separate employer-paid
benefits regime and no parallel filing for non-cash benefits.

A benefit in kind is taxed by being classified. If it is *salary in kind* under Labour Code art. 129, it is
ordinary taxable employment income and ordinary contributory salary, and it flows through the normal
gross-to-net calculation. If it falls within Labour Code art. 128 or a specific tax exclusion, it is
neither.

| Question | Colombia |
|---|---|
| Separate fringe-benefits tax? | **No** |
| Separate employer-paid regime? | **No** |
| Separate return? | **No** — reported in the ordinary electronic payroll XML and information return |
| Notional or administrative valuation scales (company car tables, accommodation scales)? | **None exist** |
| Employer-borne or employee-borne? | **Employee-borne** — the employee is taxed on the value, and the employer withholds |

### What is the definition of fringe benefits and how is the taxable amount evaluated?

**Labour Code art. 129** (Law 50 of 1990 art. 16), verbatim:

> *"1. **Salary in kind** consists of any part of the **ordinary and permanent** remuneration that
> the employee receives as direct consideration for the service, such as food, accommodation or
> clothing that the employer supplies to the employee or to their family, save for the stipulation provided in
> article [128] of this law.*
> *2. Salary in kind **must be expressly valued in every employment contract**. In the absence of a
> stipulation or of agreement on its real value it shall be assessed **by expert appraisal**, without it being able to
> constitute **more than fifty percent (50%)** of the total salary.*
> *3. However, where an employee earns the legal **minimum wage**, the value attributed to
> salary in kind **may not exceed thirty percent (30%)**."*

**Valuation method.** Three rules, in order:

1. **Contractual valuation.** The value must be **expressly stated in the employment contract**. This is
   the primary rule and the one the engine relies on.
2. **Expert appraisal** (*estimación pericial*) where the parties have not agreed a value or disagree on
   the real value.
3. **Statutory ceilings.** Salary in kind may not exceed **50%** of total salary, or **30%** where the
   employee earns the legal minimum wage.

**There is no published valuation schedule for benefits in kind in Colombia.** No company-car table, no
accommodation scale, no notional-value list. This was searched for and none exists — and the absence is
principled rather than accidental: art. 129 num. 2 routes an unvalued benefit to expert appraisal, not to a
published scale. The engine therefore requires a **contractual value on every in-kind wage type**.

### If a separate FBT regime exists, describe it in detail.

**Not Applicable — no fringe-benefits tax regime exists in Colombia.** Non-cash benefits are taxed to the
employee through ordinary payroll withholding, or are excluded from income by a specific statutory rule.
There is no employer-level benefits tax, no separate rate, no separate base and no separate return.

### What is the calculation logic for fringe benefit tax?

**Not Applicable — there is no fringe benefit tax.** The calculation logic for a benefit in kind is
therefore the ordinary classification decision tree:

```
For each benefit provided:

Q1. Is it ordinary and permanent consideration for the service?
    YES -> SALARY IN KIND (Labour Code art. 129)
           * value it in the contract, or by expert appraisal
           * cap: <= 50% of total salary;  <= 30% at the legal minimum wage
           * enters the CONTRIBUTION base, the PAYROLL-LEVY base,
             the STATUTORY-BENEFIT base
           * FULLY TAXABLE within the ordinary monthly base
    NO  -> Q2

Q2. Is it a habitual or occasional benefit that the parties have EXPRESSLY
    agreed IN WRITING is not salary?  (art. 128 - food, housing, clothing,
    extra-statutory bonuses)
    YES -> NOT SALARY for labour-law purposes
           * out of the statutory-benefit base and the overtime base permanently
           * out of the contribution base ONLY UP TO the 40% clamp;
             the excess goes back in (Law 1393 of 2010 art. 30)
           * STILL FULLY TAXABLE - a non-salary pact has NO tax effect
    NO  -> Q3

Q3. Is it given not to enrich the employee but to let them do the job -
    representation expenses, means of transport, work tools, protective
    equipment, statutory work clothing (art. 230)?
    YES -> NOT SALARY and NOT TAXABLE. Outside every base.
    NO  -> Q4

Q4. Is it a MEAL benefit provided through a THIRD PARTY (restaurant,
    voucher, meal card)?
    YES -> Tax Code art. 387-1 regime:
           * salary <= 310 tax units (16,235,940)  AND
           * monthly amount <= 41 tax units (2,147,334)
           -> not income to the employee; income to the third party
           * excess over 41 tax units -> taxable employment income
           * CASH paid to the employee for food is SALARY - none of this applies
    NO  -> Q5

Q5. Is it employer-paid PREPAID HEALTH or HEALTH INSURANCE?
    YES -> not a statutory exclusion. It is a taxable benefit, but the
           EMPLOYEE may deduct up to 16 tax units per month (837,984)
           against the withholding base (art. 387 lits. a and b)
    NO  -> Q6

Q6. Is it an employer contribution to a VOLUNTARY PENSION FUND?
    YES -> exempt income to the employee within the shared 30% /
           3,800-tax-unit annual cap; deductible for the employer up to
           3,800 tax units per employee (art. 126-1)
    NO  -> default: taxable employment income, and salary unless a valid
           written non-salary pact applies
```

### Are benefits-in-kind also subject to withholding tax?

**Yes — every taxable benefit in kind is subject to withholding**, at the same progressive rates and
through the same monthly calculation as cash pay. There is no separate rate and no separate mechanism.

| Benefit | Withheld? |
|---|---|
| Salary in kind (food, housing, clothing as ordinary and permanent consideration) | **Yes**, on the contractual or appraised value |
| Company car for personal use | **Yes**, on the value attributable to the private benefit — valued contractually, since no scale exists |
| Employer-paid housing | **Yes**, on the contractual value |
| Employer-paid prepaid health / health insurance | **Yes**, on the premium — but the employee may deduct up to 16 tax units per month |
| Employer-paid group life or personal accident insurance | **Yes**, where the cover is personal to the employee |
| Non-salary-pacted benefits under art. 128 | **Yes** — the pact has no tax effect |
| Third-party meal payments within the art. 387-1 thresholds | **No** |
| Third-party meal payments above 41 tax units | **Yes**, on the excess |
| Representation expenses, work tools, protective equipment, statutory work clothing | **No** |
| Employer contributions to voluntary pension funds | **No**, within the cap |

**The practical mechanic.** A benefit in kind produces a **positive earnings line** with the benefit's
value, which enters the taxable base, and — where the benefit is not paid in cash — an offsetting deduction
line, so that net cash pay is unchanged while the withholding and, where applicable, the contributions are
correctly computed. Where withholding on benefits would exceed available cash pay, see the minimum-wage
protection rules in Module 4.1.

### Which benefits-in-kind must be processed via payroll, and which require declarations?

| Benefit | Processed via payroll | Requires an employee declaration |
|---|---|---|
| Salary in kind — food, housing, clothing | **Yes**, at the contractual value | No — the value is in the contract |
| Company car with private use | **Yes**, at the attributed value | No |
| Employer-paid housing | **Yes** | No |
| Non-salary-pacted benefits | **Yes**, as a taxable earnings line | The **written pact** must exist |
| Third-party meal payments and vouchers | **Yes**, as an informational earnings line; taxable only on the excess | No — employer records |
| Employer-paid prepaid health | **Yes**, as a taxable earnings line | **Yes**, to claim the 16-unit deduction: provider certificate |
| Employer contributions to voluntary pension funds | **Yes**, as exempt income | **Yes**, fund certificate |
| Employer contributions to the individual pension account | **Yes**, as non-taxable income | **Yes**, administrator certificate |
| Statutory work clothing | **Yes**, as a non-taxable, non-contributory informational line — the electronic payroll XML has a dedicated element | No |
| Representation expenses, work tools | **No** — expense reimbursement, outside payroll | Expense documentation |
| Group life insurance | **Yes**, where personal cover | No |
| Employee-declared reliefs (housing interest, dependants) | **Yes**, as withholding-base adjustments | **Yes** — see Module 7.1 |

**Reporting.** The electronic payroll XML separates salary from non-salary **at element level**, with paired
element names carrying an explicit `S` (salary) or `NS` (non-salary) suffix — salary and non-salary bonus,
salary and non-salary allowance, salary and non-salary concept, salary and non-salary payment, salary and
non-salary meal payment, salary and non-salary travel/accommodation allowance. The engine must therefore
carry a **hard salary/non-salary flag on every wage type**, set at configuration, and must not attempt to
derive it at reporting time.

*Legal basis: Substantive Labour Code arts. 128, 129 (as amended by Law 50 of 1990 arts. 15 and 16), 230;
Tax Code arts. 126-1, 206, 387 lits. a) and b), 387-1, 388; Law 1393 of 2010 art. 30; Resolution DIAN
000013 of 2021 and its Technical Annex.*

---

## 7.3 Garnishments and Court Orders

### What are the rules for processing statutory deductions like child support, court-ordered fines, or tax levies?

The controlling principle is **Labour Code art. 149 num. 1**: the employer *"may not deduct, withhold or
set off any sum from salary **without an authorisation signed by the employee for each case, or without a
court order**."* A garnishment therefore requires either a court order or, in the narrow case
below, an administrative order with statutory force.

| Type | Instrument | Processing |
|---|---|---|
| **Maintenance / child support** (*alimentos*) | Judicial order from a family judge, or a conciliation agreement approved by a family commissioner or the family welfare institute | Served on the employer, who becomes a **retaining agent**. Deduct from each payroll and remit to the beneficiary or to the court's deposit account. **Up to 50% of the whole salary** including the minimum-wage portion (art. 156) |
| **Judicial attachment for a civil or commercial debt** (*embargo*) | Court order in enforcement proceedings | Deduct up to **20% of the excess over the minimum wage** (art. 155). Remit to the court's deposit account |
| **Attachment for a cooperative debt** | Court order | **Up to 50% of the whole salary** (art. 156) |
| **Tax levy by the tax authority** | Administrative enforcement (*proceso de cobro coactivo*) — the tax authority holds jurisdictional powers under Tax Code arts. 823 et seq. and may issue an attachment order without going to court | Treated as a court order for art. 149 purposes. The attachability limits of arts. 154–156 apply |
| **Social-security enforcement by the contributions authority** | Administrative enforcement by the UGPP | Same treatment |
| **Court-ordered fines** | Court order | Same treatment; art. 155 limits |
| **Disciplinary sanctions** | Not a garnishment — an employer deduction permitted by art. 150 **only** where imposed under a duly approved set of work rules | Subject to the minimum-wage floor |

**Employer duties on receipt of an order.**

1. **Acknowledge** the order within the time it specifies and confirm the employment relationship and the
   salary.
2. **Apply the deduction from the next payroll** falling due after service.
3. **Remit** to the account the order specifies, within the period it specifies.
4. **Report** any termination, unpaid leave or salary change that affects the order.
5. **Keep the order and the remittance evidence** for the retention period (Module 2.3).
6. **Do not** apply an order beyond its stated limit or duration, and **do not** apply an order served on
   the employee rather than the employer.

**Liability.** Labour Code art. 149 num. 3 makes the employer *"responsable de los perjuicios"* for
failing to make authorised, lawful deductions in good time. An employer that ignores a garnishment order
can be held liable to the creditor for the amounts that should have been withheld.

### Is there a statutory priority order if an employee has multiple garnishments?

Colombia has **no single statutory garnishment-priority article**, but a clear order emerges from the
combination of the attachability rules, the general privilege of maintenance claims and the ordinary rules
of civil enforcement. Mercans applies:

| Priority | Claim | Limit |
|---|---|---|
| **1** | Mandatory social security and withholding tax | Statutory; applied before any garnishment |
| **2** | **Maintenance obligations** (*alimentos*) | Up to **50% of the whole salary** (art. 156). Maintenance ranks first among garnishments — the obligation is of constitutional rank (Political Constitution art. 44, the prevailing rights of the child) and art. 156 gives it the widest reach |
| **3** | Debts owed to **cooperatives** | Also within the art. 156 50% reach, but ranking behind maintenance where both compete |
| **4** | **Tax and social-security enforcement** | Within the art. 155 limit — 20% of the excess over the minimum wage |
| **5** | **Ordinary civil and commercial attachments**, in **date order of service** on the employer | Within the art. 155 limit, shared among competing orders in date order |
| **6** | **Payroll lending** (*libranza*) and employee-authorised voluntary deductions | Never above the protected floor; the aggregate must leave at least 50% of net salary (Law 1527 of 2012) |

**Where competing orders exceed the ceiling.** The employer applies orders in the priority above until the
applicable ceiling is reached, then **notifies the court or authority whose order cannot be satisfied**,
stating the competing orders and the amounts applied. The employer must **not** apportion pro rata on its
own initiative, and must **not** exceed the ceiling to satisfy all orders.

**Interaction between the two ceilings.** Art. 156 (50% of the whole salary) and art. 155 (20% of the
excess over the minimum wage) are **different ceilings for different claim types**, not cumulative
allowances. A maintenance order may reach into the minimum-wage portion; a commercial attachment may not.
Where both are in play, the maintenance order is applied first within its own 50% ceiling, and the
commercial attachment is then applied only to the extent that the art. 155 headroom on the excess over the
minimum wage remains unused.

### Are there protected earnings limits?

**Yes — Colombia protects salary robustly, with one broad exception.**

| Rule | Protection |
|---|---|
| **Labour Code art. 154** | *"Salary is exempt from attachment"* — salary is **not attachable** as the general rule |
| **Labour Code art. 155** | The **excess over the minimum wage** is attachable only up to **one fifth (20%)** of that excess. So an employee on COP 3,000,000: the excess over 1,750,905 is 1,249,095, and the maximum attachable is 20% of that = **COP 249,819** |
| **Labour Code art. 156** | **Exception:** for **maintenance obligations and cooperative debts**, up to **50% of the whole salary**, minimum wage included, is attachable. The same employee: up to **COP 1,500,000** |
| **Labour Code art. 149 num. 2** | No deduction may reduce pay below the minimum wage or into the non-attachable portion **without a court order, even with written employee authorisation** |
| **Law 1527 of 2012** | Payroll-lending deductions must leave the employee at least **50% of net salary** after all statutory deductions |

**Worked illustration.** Employee on COP 3,000,000 with two orders: a maintenance order for COP 1,000,000
per month and a commercial attachment for COP 400,000 per month.

| Step | Computation | COP |
|---|---|---|
| Gross salary | | 3,000,000 |
| Mandatory social security (4% + 4%; base below 4 minimum wages so no solidarity fund) | 8% × 3,000,000 | (240,000) |
| Withholding tax | Depurated base well below 95 tax units | 0 |
| Salary available for garnishment | | 3,000,000 |
| **Maintenance order, art. 156 ceiling** | 50% × 3,000,000 = 1,500,000 → the order of 1,000,000 fits | **(1,000,000)** |
| **Commercial attachment, art. 155 ceiling** | 20% × (3,000,000 − 1,750,905) = 20% × 1,249,095 = **249,819** → the order of 400,000 is **capped** | **(249,819)** |
| **Net pay** | 3,000,000 − 240,000 − 1,000,000 − 249,819 | **1,510,181** |
| Shortfall on the commercial attachment | 400,000 − 249,819 = 150,181 | Notified to the issuing court |

Note that the two ceilings are tested independently against their own bases, and that the resulting net pay
of COP 1,510,181 is **below the minimum wage** — which is lawful here **only** because the maintenance
order is a court order within the art. 156 exception. A voluntary deduction could not have produced that
result.

*Legal basis: Substantive Labour Code arts. 149, 150, 151, 154, 155, 156; Political Constitution art. 44;
Tax Code arts. 823 et seq.; Law 1527 of 2012; Law 1098 of 2006 (Childhood and Adolescence Code).*
