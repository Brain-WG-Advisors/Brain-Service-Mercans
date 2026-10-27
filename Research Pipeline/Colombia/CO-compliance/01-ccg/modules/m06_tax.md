# Module 6: Income Tax Withholding System

*Purpose: To define the entire income tax withholding system.*

> **Resident / non-resident treatment matrix (control B1).** Built before the prose because Colombia's
> treatment turns on tax residence in a way that is frequently mis-configured. **All amounts in COP; tax
> unit (UVT) 2026 = 52,374; minimum wage 2026 = 1,750,905.**
>
> | Income type | **RESIDENT** | **NON-RESIDENT** |
> |---|---|---|
> | **Regular salary from a Colombian employer, work performed in Colombia** | Progressive table, Tax Code **art. 383** (0 / 19 / 28 / 33 / 35 / 37 / 39%), applied to the art. 388 depurated monthly base. Method: Procedure 1 or Procedure 2 | **Flat 20%**, Tax Code **art. 408**, applied to the **gross payment**. **No** art. 388 depuration, **no** 25% exempt-income deduction, **no** dependants or other art. 387 deductions, **no** tax-free band. Confirmed by **DIAN Concepto 011108 of 29 June 2026**, which upholds Concepto 1789 (int. 14595) of 2025 |
> | **Regular salary from a Colombian employer, work performed entirely outside Colombia** | Worldwide income — art. 383 progressive table applies | **Not taxable in Colombia** — foreign-source income. **No withholding.** DIAN Oficio 28380 of 2019 |
> | **Annual / 13th-month bonus (statutory service bonus)** | **Procedure 1:** the statutory minimum bonus is withheld **separately** on its own read of the art. 383 table (art. 385). **Procedure 2:** folded into the ordinary monthly base | **Flat 20%** under art. 408, on the gross bonus. No separate treatment and no separate table read |
> | **Severance payments — statutory severance savings and interest** | Exempt in full where the average monthly income of the last 6 months ≤ **350 tax units** (18,330,900); tapered above (Tax Code art. 206 num. 4). **Excluded** from the monthly withholding base under both procedures | **Flat 20%** under art. 408 on the gross amount. The art. 206 num. 4 exemption is an exemption of the **resident** cédula-general regime and does not attach to a non-resident's flat withholding |
> | **Dismissal indemnity** | Fully taxable employment income; enters the ordinary monthly base. Only the statutory-minimum indemnities of art. 206 nums. 1–3 are exempt, and only up to the legal minimum amount (art. 206 par. 1) | **Flat 20%** under art. 408 |
> | **Equity / share incentives (stock options, restricted shares)** | Taxable **employment income at exercise or vesting**, on the spread between market value and exercise price; enters the ordinary monthly base and the art. 383 table. Subsequent disposal is a separate capital transaction, outside payroll | **Flat 20%** under art. 408 where the underlying service was performed in Colombia. Where the service was performed abroad, foreign-source and not taxable |
> | **Labour-service / contractor pay (non-employment work income)** | **Art. 383 table applies**, using *"pagos mensualizados"* — total contract value less mandatory health and pension contributions, divided by the months of the contract (art. 383 par. 2, added by Law 2277 of 2022 art. 8) | **Flat 20%** under art. 408 for services rendered in Colombia. Technical services, technical assistance and consultancy rendered from abroad are **also** subject to withholding under arts. 24 and 408 |
> | **Benefits in kind (salary in kind, employer-paid housing, cars, insurance)** | Valued contractually or by expert appraisal; **fully taxable** as employment income within the ordinary monthly base. No notional valuation scale exists | **Flat 20%** under art. 408 on the valued amount |
> | **Third-party meal payments** | **Not income** up to 41 tax units per month (2,147,334) where salary ≤ 310 tax units (16,235,940); the excess is taxable (art. 387-1) | The art. 387-1 exclusion is drafted as a non-income rule for the worker and applies on its own terms; any excess is withheld at the flat 20% |
> | **Pension income paid by the employer** | Taxable only above **1,000 tax units per month** (52,374,000) — art. 206 num. 5 | **Flat 20%** |
>
> **The residence switch is prospective, never retroactive.** DIAN Concepto 011108 of 2026 rejected the
> argument that a foreign employee on a contract exceeding 183 days may be withheld under art. 383 from
> day one in anticipation of future residence. Withholding is determined **at the moment of each payment**,
> on the status then held. The engine must therefore withhold at 20% until residence is acquired, and
> switch to the art. 383 table **from the payment following** the date the 183-day test is met. There is
> **no true-up of the earlier months through payroll**; the employee reconciles in their own annual return.
>
> **Non-residents are IN SCOPE for Mercans Colombia payroll.** A foreign national employed under a
> Colombian contract before acquiring residence is a real and common case (expatriate assignments,
> regional roles). The engine must carry a residence flag with an effective date and must support the
> mid-year switch.

## 6.1 System Overview and Methodology

### Describe the country's income tax withholding system.

Colombia operates a **monthly, employer-administered advance-collection system** called *retención en la
fuente sobre rentas de trabajo* — withholding at source on work income. Its defining characteristics:

| Characteristic | Colombia |
|---|---|
| Nature | **Advance instalment** of the employee's own annual income tax, not a final tax |
| Frequency | **Monthly** — one aggregated return per employer per month |
| Cumulative? | **No.** Non-cumulative. Each month stands alone under Procedure 1; Procedure 2 uses a fixed percentage recomputed twice a year |
| Employer-borne income tax? | **None.** Colombia has no employer payroll tax on income. The employer's cost is the social-security and levy burden of Module 5 only |
| Basis | A **depurated** monthly figure, neither gross pay nor the social-security contribution base |
| Rate structure | **Progressive, expressed in tax units** — seven bands, 0% to 39% |
| Employee election | The employee may request **a higher** rate in writing; there is no election of a lower rate |
| Employer election | The employer elects **Procedure 1 or Procedure 2 per employee**; once elected for a semester, Procedure 2 binds for six months |
| Reconciliation | The employee's own annual income-tax return, if required to file. The **employer performs no year-end true-up** |
| Return | **Form 350**, monthly, aggregating all withholdings of every type made by the employer |
| Certificate | **Form 220**, annual income and withholding certificate to each employee |

The employer is an *agente de retención* — a withholding agent. Its statutory obligations are to withhold
the correct amount, to declare it on Form 350 by the deadline, to pay it, to issue the annual certificate,
and to report the detail in the third-party information return.

### What types of taxes are withheld by the employer?

For a standard employment relationship the employer withholds **one tax only**.

| Withheld item | Applies to payroll? | Basis |
|---|---|---|
| **Income tax withholding on work income** (*retención en la fuente sobre rentas de trabajo*) | **Yes — the only payroll withholding** | Tax Code arts. 383, 385, 386, 388 (resident); arts. 408–415 (non-resident) |
| Value-added tax withholding | No — supplier payments, not payroll | Tax Code art. 437-2 |
| Industry and commerce tax withholding | No — municipal, on business turnover, not on salary | Municipal statutes |
| Stamp duty | No | Tax Code art. 519 |
| Financial-transactions tax | No — bank-level, on movements of funds | Tax Code art. 870 |
| Solidarity contribution to higher education | **Deducted, not a tax** — a Labour Code art. 150 permitted deduction requiring no individual order, added by Law 1911 of 2018 art. 22 | Labour Code art. 150 |

**There is no local, municipal, departmental, church, solidarity or social surcharge on employment income
in Colombia.** The solidarity pension fund contribution (Module 5) is a social-security contribution, not
a tax, and is itself **non-taxable income** to the employee.

### At what level are tax rates published (central or state)?

**Wholly central.** Income tax and its withholding are national taxes, legislated by Congress in the Tax
Code and administered by DIAN. There is:

- no departmental or municipal income tax on employment income;
- no sub-national rate, band, allowance or surcharge;
- no local variation of the tax unit.

The two administrative acts that set the annual parameters are both national:

| Parameter | Instrument | 2026 |
|---|---|---|
| **Tax unit (UVT)** | Resolution DIAN issued each December under Tax Code art. 868 | **Resolution DIAN 000238 of 15 December 2025 — COP 52,374** |
| Consolidated tax, customs and exchange rules | The Single Tax Resolution | Resolution DIAN 000227 of 23 September 2025 |

The tax unit is uprated annually by the consumer price index for middle-income households over the year
to 1 October. For 2026 that variation was certified at **5.17%**, taking the unit from COP 49,799 to
**COP 52,374**.

*Legal basis: Tax Code (Decree-Law 624 of 1989) arts. 365, 368, 383, 385, 386, 388, 408–415, 437-2, 519,
868, 870; Resolution DIAN 000238 of 15 December 2025 art. 1; Resolution DIAN 000227 of 2025; Substantive
Labour Code art. 150 (as amended by Law 1911 of 2018 art. 22); DIAN Concepto 011108 of 29 June 2026; DIAN
Oficio 28380 of 2019.*

---

## 6.1.1 Taxable Income Definition

### Provide the statutory definition of 'Taxable Income'.

The taxable base for withholding is the **depurated payment** of Tax Code **article 388**, added by
Law 1819 of 2016 art. 18:

> *"For the purposes of withholding at source, the payer must **subtract** from the payments or credits to account
> the following factors:*
> *1. Income that the law exhaustively provides as **not constituting taxable income or occasional
> gain**.*
> *2. The **deductions** referred to in article 387 of the Tax Code and the **income that the law
> exhaustively provides as exempt**. In any event, the total sum of deductions and exempt income **may
> not exceed forty percent (40%)** of the result of subtracting, from the amount of the payment or credit to account,
> the attributable income that does not constitute taxable income or occasional gain. This limitation shall not apply in
> the case of the payment of pensions… pension substitution indemnities and refunds of
> pension savings."*

An **absolute annual cap** is added by regulation — Decree 1625 of 2016 art. 1.2.4.1.6 par. 3, as modified
by **Decree 2231 of 2023 art. 9**: deductions and exempt income may not exceed the particular limit of each
benefit, **nor 40%, nor the absolute value of 1,340 tax units per year** (COP 70,181,160 for 2026).

The scope of art. 383 defines what enters the base in the first place: *"the taxable payments made …
arising from an **employment relationship, or a statutory and regulatory relationship**, and payments received in respect of
retirement, disability, old-age, survivors' and occupational-risk **pensions**."*

### Explain how this base is derived from total gross earnings.

```
(A)  TOTAL TAXABLE PAYMENTS OF THE MONTH
     basic salary + overtime + night and rest-day premiums + commissions
     + habitual bonuses + salary in kind + transport allowance
     + service bonus [Procedure 2 only; Procedure 1 reads it separately]
     EXCLUDING: severance savings and the interest on them (both procedures)

(B)  LESS NON-TAXABLE INCOME  (ingresos no constitutivos de renta ni ganancia ocasional)
     - employee mandatory PENSION contribution 4%                    art. 55
     - employee SOLIDARITY PENSION FUND contribution 1% + 0.2-1.0%   art. 55
     - employee mandatory HEALTH contribution 4%                     art. 56
     - voluntary contributions to the individual pension account,
       <= 25% of annual labour income, cap 2,500 tax units           art. 55
     - qualifying third-party meal payments                          art. 387-1

(C)  = (A) - (B)          <-- the reference figure for the 40% cap

(D)  LESS DEDUCTIONS  (art. 387)
     - housing-loan interest and monetary correction   monthly cap 100 tax units = 5,237,400
     - prepaid health / health insurance               monthly cap  16 tax units =   837,984
     - dependants: 10% of the month's gross labour income,
                                                       monthly cap  32 tax units = 1,675,968

(E)  LESS EXEMPT INCOME  (rentas exentas)
     - voluntary pension funds + long-term savings accounts:
       <= 30% of labour income, annual cap 3,800 tax units = 199,021,200   arts. 126-1, 126-4
     - THEN, AND ONLY THEN, the 25% exemption of art. 206 num. 10,
       computed on [(C) - D - other exempt income], annual cap 790 tax units = 41,375,460

(F)  APPLY THE COMBINED CAP
     (D + E) <= 40% of (C)     AND     (D + E) <= 1,340 tax units annually = 70,181,160
     OUTSIDE the cap: 72 tax units per dependant per year, max 4 dependants
                      = 3,770,928 each   (art. 336 num. 3, second paragraph)

(G)  TAXABLE BASE = (C) - (D + E as capped) - (72-unit dependant deduction)

(H)  CONVERT TO TAX UNITS:  base_UVT = (G) / 52,374

(I)  APPLY THE ART. 383 TABLE  ->  withholding in tax units  ->  x 52,374  ->  COP
```

**The single most important ordering rule.** Tax Code art. 206 num. 10 requires the 25% exemption to be
computed *"once there are subtracted from the total value of the labour payments received by the employee the
income that does not constitute taxable income, the deductions and the other exempt income items other than the one established
in the present numeral"*. Computing 25% of **gross** rather than 25% of the post-deduction figure
overstates the exemption and under-withholds. It is computed **last**.

**Which tax-unit vintage applies to the annual caps.** DIAN Concepto 015007 (int. 973) of 13 September 2023
confirms that the **current year's** tax unit is used — COP 52,374 for 2026 — *"a clarification that is
applicable for the purposes of procedure two … and the calculation of the fixed withholding percentage that must
be carried out in the month of June"*.

**Open item — monthly apportionment of annual caps.** The 790-tax-unit and 1,340-tax-unit caps are stated
**annually**, yet withholding is monthly. Market practice, which Mercans follows, is to apportion them at
one twelfth per month — 65.8333 tax units (COP 3,447,955) and 111.6667 tax units (COP 5,848,430)
respectively — and to test each month against the apportioned figure. No regulation prescribes the
apportionment expressly. Carried in the QA report.

### Deliverable: Step-by-step decision guide to determine the correct tax schedule for an employee

```
START
 |
 +-- Q1. Is the payment employment income (relación laboral, o legal y reglamentaria)?
 |        NO  -> not payroll scope. Non-employment work income uses art. 383 par. 2
 |               "pagos mensualizados" for residents; art. 408 for non-residents
 |        YES -> continue
 |
 +-- Q2. Is the employee a COLOMBIAN TAX RESIDENT at the date of this payment?
 |        Test (art. 10): >183 days present in any 365-day period, OR diplomatic
 |        status, OR the nationality-plus-connection tests
 |
 |        NO  -> Q2a. Is the service performed IN Colombia?
 |               |      NO  -> FOREIGN-SOURCE INCOME. NOT TAXABLE. NO WITHHOLDING.
 |               |             (DIAN Oficio 28380 of 2019)
 |               |      YES -> SCHEDULE N: FLAT 20% ON GROSS, art. 408.
 |               |             No depuration, no deductions, no exemptions.
 |               |             (DIAN Concepto 011108 of 2026)
 |               |             Re-test residence EVERY month; switch prospectively
 |               |             on the payment following the 183rd day.
 |        YES -> continue
 |
 +-- Q3. Is the payment SEVERANCE SAVINGS or the INTEREST on them?
 |        YES -> SCHEDULE C: art. 206 num. 4 exemption and taper.
 |               EXCLUDED from the monthly base under BOTH procedures.
 |        NO  -> continue
 |
 +-- Q4. Which withholding procedure has the employer elected for this employee?
 |
 |     PROCEDURE 1 (art. 385)
 |     |
 |     +-- Q4a. Is the payment the STATUTORY MINIMUM SERVICE BONUS?
 |     |        YES -> SCHEDULE B: separate read of the art. 383 table on the
 |     |               bonus alone, depurated in its own right.
 |     |        NO  -> SCHEDULE A: art. 383 table on the month's depurated base.
 |     |               If the period is shorter than 30 days: divide by days,
 |     |               multiply by 30, read the table PERCENTAGE, then apply that
 |     |               percentage to the actual payments of the period.
 |     |
 |     PROCEDURE 2 (art. 386)
 |     |
 |     +-- SCHEDULE D: apply the FIXED PERCENTAGE set in the preceding June or
 |            December to the month's depurated base. The service bonus is
 |            INCLUDED in that base; no separate read.
 |            New hire with no calculation yet -> read the table on the month's
 |            own taxable payments until the first semi-annual calculation.
 |
 +-- Q5. Has the employee requested a HIGHER rate in writing (art. 383 par. 3)?
          YES -> apply the higher requested rate, effective from the month AFTER
                 the request. It overrides upward only, never downward.
```

### Deliverable: Explain the official tax calculation method with formulas and examples

**The tariff table — Tax Code art. 383**, first paragraph and table replaced by **Law 2010 of 2019 art. 42**:

| Band in tax units | Marginal rate | Withholding formula (in tax units) | 2026 band boundary (COP) |
|---|---|---|---|
| 0 – 95 | **0%** | 0 | 0 – 4,975,530 |
| > 95 – 150 | **19%** | (base − 95) × 19% | > 4,975,530 – 7,856,100 |
| > 150 – 360 | **28%** | (base − 150) × 28% + 10 | > 7,856,100 – 18,854,640 |
| > 360 – 640 | **33%** | (base − 360) × 33% + 69 | > 18,854,640 – 33,519,360 |
| > 640 – 945 | **35%** | (base − 640) × 35% + 162 | > 33,519,360 – 49,493,430 |
| > 945 – 2,300 | **37%** | (base − 945) × 37% + 268 | > 49,493,430 – 120,460,200 |
| > 2,300 and above | **39%** | (base − 2,300) × 39% + 770 | > 120,460,200 |

**Formulae**

```
base_UVT       = taxable base in COP / 52,374
withholding_UVT = per the band formula above
withholding_COP = withholding_UVT x 52,374

Effective rate (art. 383 par. 1):
  rate = withholding_UVT / total gravable labour income in tax units
  -- used to convert a table result into the percentage applied to the monthly income

Procedure 2 fixed percentage (art. 386):
  average = (sum of taxable payments over the preceding 12 months) / 13
            [divide by the actual months of service if fewer than 12]
  fixed % = table(average) expressed as a percentage of the average
  -- recomputed each JUNE and DECEMBER; binds for the following six months
```

**Worked example — resident, Procedure 1, August 2026.**

Facts: legal-person employer, income-tax filer. Employee on an ordinary salary of **COP 8,000,000**,
indefinite-term contract, full 30-day month, no overtime, no non-salary payments, no salary in kind,
occupational risk class I. No declared art. 387 deductions, no voluntary pension or savings contributions.
Tax unit 52,374; minimum wage 1,750,905.

| Line | Computation | COP |
|---|---|---|
| (A) Total taxable payments of the month | Salary 8,000,000 > 2 minimum wages, so no transport allowance | 8,000,000.00 |
| (B) Non-taxable — pension 4% (art. 55) | 4% × 8,000,000 | (320,000.00) |
| (B) Non-taxable — solidarity fund 1% (art. 55) | Base 8,000,000 ≥ 4 minimum wages (7,003,620) | (80,000.00) |
| (B) Non-taxable — health 4% (art. 56) | 4% × 8,000,000 | (320,000.00) |
| **(C) Subtotal** | 8,000,000 − 720,000 | **7,280,000.00** |
| (D) Art. 387 deductions | None declared | 0.00 |
| (E) Exempt income — 25% of art. 206 num. 10 | 25% × 7,280,000 | (1,820,000.00) |
| — 790-tax-unit annual cap check | 790 ÷ 12 = 65.8333 units = 3,447,955 → 1,820,000 is below | ok |
| (F) Combined 40% cap check | 40% × 7,280,000 = 2,912,000 → 1,820,000 ≤ 2,912,000 | ok |
| — 1,340-tax-unit annual cap check | 1,340 ÷ 12 = 111.6667 units = 5,848,430 → 1,820,000 is below | ok |
| **(G) Taxable base** | 7,280,000 − 1,820,000 | **5,460,000.00** |
| (H) In tax units | 5,460,000 ÷ 52,374 | **104.2502** |
| (I) Band | > 95 and ≤ 150 → marginal **19%** | |
| (I) Withholding | (5,460,000 − 95 × 52,374) × 19% = (5,460,000 − 4,975,530) × 19% = 484,470 × 19% | **92,049.30** |

Cross-check in tax units: (104.2502 − 95) × 19% = 1.757538 units × 52,374 = **COP 92,049.30**. Effective
rate on the gross: 1.15%.

**Worked example — non-resident, same facts.** Foreign national on a Colombian contract, working in
Colombia, day 40 of the assignment, therefore **not yet a tax resident**:

| Line | Computation | COP |
|---|---|---|
| Gross payment | | 8,000,000.00 |
| Depuration | **None** — art. 408 applies to the gross | — |
| Withholding at 20% | 20% × 8,000,000 | **1,600,000.00** |

The same salary produces **COP 92,049 of withholding for a resident and COP 1,600,000 for a non-resident**
— a 17-fold difference. This is the single largest configuration risk in Colombian expatriate payroll.

*Legal basis: Tax Code (Decree-Law 624 of 1989) arts. 10, 55, 56, 126-1, 126-4, 206, 336, 383 (table as
replaced by Law 2010 of 2019 art. 42), 385, 386, 387, 387-1, 388, 408–415; Decree 1625 of 2016
art. 1.2.4.1.6 par. 3 (as modified by Decree 2231 of 2023 art. 9); DIAN Concepto 015007 int. 973 of
13 September 2023; DIAN Concepto 011108 of 29 June 2026; DIAN Oficio 28380 of 2019; Resolution DIAN 000238
of 2025.*

---

## 6.2 Tax Rates and Logic

### What are the latest tax rates by tax type, residential status, and payment frequency?

| Tax type | Resident | Non-resident | Frequency sensitivity |
|---|---|---|---|
| Withholding on employment income | Progressive **0 / 19 / 28 / 33 / 35 / 37 / 39%**, art. 383 | **Flat 20%** on gross, art. 408 | **None** — the table is monthly; a sub-30-day period is grossed to 30 days under Procedure 1 |
| Withholding on non-employment work income | Progressive art. 383 table on *"pagos mensualizados"* (art. 383 par. 2) | Flat 20%, art. 408 | Contract value ÷ months of contract |
| Withholding on employer-paid pension income | Progressive art. 383 table, taxable only above 1,000 tax units per month | Flat 20% | Monthly |
| Employee-requested higher rate | Any rate above the computed one, on written request | Not applicable | From the month after the request |
| Employer income tax on payroll | **None** | **None** | — |

**Note on the tax-unit denominated bands.** Because the bands are in tax units, they reprice automatically
each year. The 2026 boundaries in pesos are set out in the table in Module 6.1.1.

### How are rates applied for different frequencies?

**The withholding table is a monthly table, and the rates do not change with frequency.** What changes is
how a non-monthly period is mapped onto it.

| Frequency | Procedure 1 | Procedure 2 |
|---|---|---|
| **Monthly** | Read the table directly on the month's depurated base | Apply the fixed percentage to the month's depurated base |
| **Semi-monthly** | Common Colombian practice pays the first half as an untaxed advance and computes the full month's withholding on the second payment. The statutorily rigorous alternative — grossing each half-month to 30 days and applying the resulting percentage to the actual half-month payments — is available under art. 385 and produces a smoother net | Apply the fixed percentage to each payment, or to the month's total at month end |
| **Weekly / ten-day / fourteen-day** | Art. 385, sub-30-day rule: **divide the payments by the number of days, multiply by 30, read the table percentage, then apply that percentage to the actual payments of the period** | Apply the fixed percentage to each payment |
| **A period longer than a month** (arrears covering several months) | See Module 9.2 | See Module 9.2 |

The art. 385 sub-30-day rule is worth restating because it is a **percentage** rule, not an amount rule.
The table is read to obtain a rate on the grossed-up notional monthly figure, and that rate is then applied
to the real, smaller payment. Reading the table for an *amount* on the grossed-up figure would grossly
over-withhold.

### How does tax applicability and calculation logic differ by residential status?

| Dimension | Resident | Non-resident |
|---|---|---|
| **Scope of taxation** | **Worldwide** income and wealth | **Colombian-source** income only |
| **Employment income from a Colombian employer, work in Colombia** | Art. 383 progressive | **Art. 408, flat 20% on gross** |
| **Employment income, work performed entirely abroad** | Taxable — worldwide basis | **Not taxable; no withholding** |
| **Depuration** | Full art. 388 depuration | **None** |
| **Non-taxable income** (mandatory contributions) | Deducted | **Not deducted** |
| **Art. 387 deductions** (housing interest, prepaid health, dependants) | Available | **Not available** |
| **25% exempt-income deduction** | Available, capped at 790 tax units per year | **Not available** |
| **Tax-free band** | First 95 tax units per month | **None** — 20% applies from the first peso |
| **Annual return** | Required where the art. 592 thresholds are exceeded | Generally not required where withholding at source has been fully applied (art. 592 num. 2) |
| **Procedure election** | Procedure 1 or 2 | Neither — a flat rate, not a procedure |
| **Treaty relief** | Applies | Applies — Colombia's treaty network (Spain, Chile, Switzerland, Canada, Mexico, South Korea, Portugal, India, Czech Republic, United Kingdom, France, Italy, Japan, and the Andean Community Decision 578) can reduce or eliminate the 20% where the employment article assigns taxing rights to the residence state. **Treaty relief is a client decision requiring a residence certificate; Mercans applies it only on written client instruction** |

**The residence test — Tax Code art. 10.** Presence exceeding **183 calendar days**, continuous or not, in
any **365-day period**; where the period straddles two years, residence attaches to the year in which the
183rd day falls. Plus the diplomatic and nationality-plus-connection tests set out in Module 2.2.

**Operational rule.** Carry a **residence flag with an effective date** on the employee record; re-evaluate
it **every payroll period**; switch the schedule prospectively from the payment following the date the test
is met. Never apply the change retroactively through payroll.

### Provide the tax calculation logic covering eligibility, joining month, termination month, mid-month joining, mid-month terminations, and mid-month salary revisions.

**Eligibility.** Every employee is within the withholding system from the first payment. There is no
registration threshold, no minimum-earnings exclusion and no employee opt-out. An employee whose depurated
base falls in the 0% band is still *within* the system — the withholding is simply nil, and the payment is
still reported on Form 350, in the electronic payroll XML, in the annual certificate and in the information
return.

**Joining month and mid-month joining.**

| Procedure | Rule |
|---|---|
| **Procedure 1** | Apply the art. 385 sub-30-day rule: `(payments ÷ days) × 30` → read the table **percentage** → apply that percentage to the actual payments of the period |
| **Procedure 2** | A new hire has no 12-month history, so **no fixed percentage exists**. Art. 386 directs that until the first semi-annual calculation the employer reads the table on the month's own taxable payments — i.e. Procedure 1 behaviour. At the next June or December calculation, the average uses the **actual months of service** as the divisor, not 13 |

**Termination month and mid-month termination.**

1. Compute the withholding on the salary and other ordinary payments for the days worked, using the same
   sub-30-day rule under Procedure 1 or the fixed percentage under Procedure 2.
2. **Exclude severance savings and the interest on them** from the monthly base under both procedures; they
   carry the art. 206 num. 4 exemption and taper, driven by the **average monthly income of the last six
   months of employment**.
3. Under Procedure 1, the accrued **statutory minimum service bonus** paid on termination retains its
   separate table read.
4. A **dismissal indemnity** is fully taxable ordinary employment income and enters the monthly base.
5. There is **no** termination-year true-up and **no** final tax reconciliation by the employer. The annual
   certificate (Form 220) records what was paid and what was withheld; the employee reconciles.

**Mid-month salary revision.**

| Procedure | Rule |
|---|---|
| **Procedure 1** | The month's payments are simply summed, whatever the segments, and the table is read once on the combined depurated base. No splitting is required for tax — unlike for social security, where a salary-variation change event is reported |
| **Procedure 2** | The fixed percentage is unchanged until the next June or December recalculation. A large mid-year increase therefore produces **under-withholding for the remainder of the semester**. The employee's remedy is a written request for a **higher** rate under art. 383 par. 3; the employer may not unilaterally increase the fixed percentage mid-semester |

**A change of procedure.** The procedure is elected by the **employer**, per employee. Procedure 2, once
elected, applies for the whole six-month period following the June or December calculation. Market practice
is to change procedure only at a semester boundary.

### Do tax rates vary by gender or age?

**No.** There is no gender-differentiated or age-differentiated rate, band, allowance, deduction or
exemption anywhere in the Colombian income-tax withholding system. The art. 383 table, the art. 387
deductions, the art. 206 exemptions and the art. 336 caps are identical for every employee.

Two adjacent points that are sometimes mistaken for age variation:

1. **Pension income** is taxable only on the monthly amount exceeding **1,000 tax units** (COP 52,374,000)
   — Tax Code art. 206 num. 5. That is a rule about the *type of income*, not about the recipient's age,
   and it applies only where the taxpayer meets the Law 100 pension-entitlement conditions.
2. **Dependants** aged 18 to 25 in higher or technical education generate a deduction for the *taxpayer*
   (Tax Code art. 387 par. 2 num. 2). That is a characteristic of the dependant, not of the employee.

### What is the minimum tax rate applicable?

**Zero per cent — for residents.** The first band of the art. 383 table is 0% up to **95 tax units per
month**, which for 2026 is **COP 4,975,530** of *depurated* base. There is no minimum withholding, no
floor amount and no minimum-tax rule in the withholding system.

Two important qualifications:

1. **95 tax units of depurated base is a considerably higher gross salary.** Working the arithmetic
   backwards for an employee with only the mandatory contributions and the 25% exemption: a depurated base
   of 4,975,530 corresponds to a pre-exemption figure of 4,975,530 ÷ 0.75 = 6,634,040, which grossed up for
   the 9% employee contributions (4% + 4% + 1%) is approximately **COP 7,290,000 of monthly gross salary**.
   In practice, therefore, an employee earning up to roughly 7.3 million pesos a month — about **4.2
   minimum wages** — suffers **no withholding at all**.
2. **For non-residents the minimum is 20%, from the first peso.** There is no exempt band, no allowance and
   no minimum threshold under art. 408.

**Is there a maximum?** The top marginal rate is **39%** above 2,300 tax units per month
(COP 120,460,200). Since the base is depurated and progressive, the *effective* rate never reaches 39%.

**Employee-elected uplift.** Tax Code art. 383 par. 3 permits the employee to request a **higher**
withholding rate in writing, effective from the month after the request. This is used by employees who
expect a balance due on their annual return. The engine must support an employee-elected rate that
**overrides upward only**.

*Legal basis: Tax Code (Decree-Law 624 of 1989) arts. 10, 206 nums. 4 and 5, 383 (and pars. 1, 2, 3), 385,
386, 387, 388, 408–415, 592; Law 2010 of 2019 art. 42; Law 2277 of 2022 art. 8; DIAN Concepto 011108 of
29 June 2026; DIAN Oficio 28380 of 2019; Andean Community Decision 578 and Colombia's bilateral double-tax
treaties.*

---

## 6.3 Adjustments and Special Cases

### For annualized tax systems, which salary components must be projected?

**Colombia is not an annualised or cumulative withholding system, so there is no projection of future
income.** Procedure 1 looks only at the current month. Procedure 2 looks only **backwards**, at the
preceding 12 months.

This is a genuine structural difference from cumulative jurisdictions and must be configured deliberately:
there is no annual estimate, no notional annual salary, no projected bonus and no year-end catch-up.

**What Procedure 2 requires — a backward-looking accumulator, not a projection:**

```
In JUNE and in DECEMBER of each year:

  numerator = the sum of ALL taxable payments made to the employee over the
              preceding 12 months, EXCLUDING severance savings and the
              interest on severance savings

  divisor   = 13          (or the actual number of months of service, if < 12)

  average   = numerator / divisor

  fixed %   = the art. 383 table result for `average`, expressed as a
              percentage of `average`   (art. 383 par. 1)

  The fixed % is then applied to each of the FOLLOWING SIX MONTHS' depurated bases.
```

**The divisor is 13, not 12.** Tax Code art. 386 says *"dividir por 13"*. The 13 divisor prorates the
13th-month effect of the statutory service bonus — which, unlike under Procedure 1, is **not** given a
separate table read under Procedure 2 and instead sits inside the ordinary base. Using 12 over-withholds
by roughly 8%.

**Components that must therefore be accumulated for 12 rolling months:**

| Component | In the accumulator? |
|---|---|
| Basic salary | **Yes** |
| Overtime, night and rest-day premiums | **Yes** |
| Commissions and habitual bonuses | **Yes** |
| Statutory service bonus | **Yes** |
| Salary in kind | **Yes** |
| Transport allowance | **Yes** |
| Vacation pay and cash-compensated vacation | **Yes** |
| **Severance savings** | **No** — expressly excluded by art. 386 |
| **Interest on severance savings** | **No** — expressly excluded |
| Non-taxable income and exempt income | Deducted in the depuration, per art. 387 par. 1, which requires the art. 387 deductions to be used **both** in computing the fixed percentage **and** in computing the monthly base it is applied to |

### Are year-end tax adjustments required?

**No — not by the employer.** Colombia imposes **no employer year-end tax reconciliation**. The employer
does not compute an annual liability, does not compare it with withholdings, and does not settle a
difference through payroll. There is no equivalent of a P60 reconciliation or a year-end true-up run.

What the employer must do at year end is **certify and report**, not reconcile:

| Obligation | Deadline | Content |
|---|---|---|
| **Form 220 — annual income and withholding certificate** to each employee | **Last business day of March** | Tax Code arts. 378–379: the employer's and employee's identification, the total payments by concept, the total withheld, and the employee's own declarations where the employee is a non-filer (art. 380). Form prescribed by Resolution DIAN 000022 of 20 February 2024 |
| **Information return, Format 2276 version 4** — income and withholdings on work income | May–June, by tax number | Resolution DIAN 000227 of 2025 arts. 1.3.7.1.1 and 1.3.9.1 |
| **December recalculation of the fixed percentage** (Procedure 2 only) | December | Sets the rate for January–June of the following year |
| **Reparameterisation for the new tax unit** | 1 January | Every band boundary and cap reprices |

**The employee reconciles, not the employer.** An employee whose income exceeds the Tax Code art. 592
filing thresholds files an annual income-tax return, in which the withholdings are credited against the
computed liability and any excess is refunded or any shortfall paid.

### Are there minimum or higher tax requirements if employees fail to submit a tax ID or social security number?

**No.** Colombia has **no penalty withholding rate** for a missing tax identifier — no equivalent of an
emergency code, a flat penalty rate or a default maximum rate.

The reasons are structural:

1. **Employees are generally not required to be registered in the tax registry.** The employer's withholding
   obligation arises from the payment, not from the employee's registration status. The employee's
   **identity-document number** is the identifier used throughout.
2. **The identity document is a precondition of employment itself**, not of payroll. An employment contract
   requires an identified person; social-security affiliation requires an identity document; the electronic
   payroll XML will not validate without a document type and number from the closed code list.

**What actually happens where identifiers are missing or wrong:**

| Missing item | Consequence |
|---|---|
| Identity document type or number | The electronic payroll XML **fails validation** (rule ZB01 and the global rules). The document cannot be transmitted, so the employer loses the tax deductibility of that payroll cost. Contribution-return filing also fails |
| Employer tax number or verification digit | Validation rules NIE038 / NIE041 reject the document |
| Institution codes (health insurer, pension administrator, occupational-risk insurer, fund) | The contribution return fails or misdirects contributions |
| Employee declarations for deductions (dependants, housing interest, prepaid health) | **No penalty** — the employee simply loses the deduction and is **over-withheld**. The remedy is the employee's own annual return |
| Dependant's identity document | The deduction is not sustainable on audit, and the information return is rejected |

**The one direction in which the rate can move upward is voluntary**: the employee may request a **higher**
rate in writing under art. 383 par. 3.

### What is the income tax and social security refund procedure?

Colombia has **two distinct refund routes**, one for tax and one for contributions, and neither is a
payroll operation in the ordinary case.

**(a) Over-withheld income tax.**

| Route | Who initiates | Mechanism |
|---|---|---|
| **Within the same fiscal year, before the Form 350 is filed** | Employer | The employer corrects the withholding in a subsequent period of the **same year** and adjusts the aggregated Form 350 figure. This is the normal, and preferred, route |
| **After the Form 350 has been filed** | Employer | File a **correction return** for the affected period. Where the correction reduces the declared value, Tax Code art. 589 applies and the correction must be filed within **one year** of the original filing deadline |
| **Reimbursement of amounts withheld in excess or wrongly withheld** (*retenciones practicadas en exceso o indebidamente*) | Employee requests, employer executes | **Decree 1625 of 2016 art. 1.2.4.16**: on the employee's written request with evidence, the employer reimburses the excess and **deducts the reimbursed amount from the withholdings of the following period**, carrying any surplus forward until absorbed. The employer must keep the employee's written request |
| **After the year has closed and the employee has filed** | Employee | The excess is credited on the employee's own annual return and refunded by the tax authority under the general refund procedure (Tax Code arts. 850 et seq.) |

**(b) Over-paid social-security contributions.**

| Route | Mechanism |
|---|---|
| **Correction planilla** (type N) | The employer files paired records — an `A` group with the originally settled values and a `C` group with the corrected values. Note the structural constraint: the sum of the contribution bases and of the day counts in the `C` records must be **greater than or equal to** those in the `A` records, so the correction planilla is designed for **under-declaration**, not over-declaration |
| **Refund claim to the administering entity** | For a genuine overpayment, the claim is made directly to the health insurer, pension administrator, occupational-risk insurer, family compensation fund, apprenticeship service or family welfare institute that received the money. Each has its own procedure and evidentiary requirements |
| **Reimbursement to the employee** | Where the employee's share was over-deducted, the employer reimburses the employee through payroll and pursues the recovery from the receiving entity itself. **The employer carries the cash-flow and the process risk** |
| **UGPP** | Where the overpayment arises from an audit adjustment, the UGPP process governs |

**Timing.** Contribution refunds are materially slower than tax corrections — commonly several months —
because each receiving entity processes independently. Mercans practice is therefore to reimburse the
employee promptly through payroll on the employer's authority and to pursue recovery separately.

### Deliverable: Detailed worked examples for a standard resident employee, a non-resident employee, and an irregular payment

**Example 1 — standard resident employee, Procedure 1, August 2026.**

Employee on COP 8,000,000, no deductions declared. Fully worked in Module 6.1.1 above:
depurated base **COP 5,460,000** = 104.2502 tax units → 19% band → **withholding COP 92,049.30**;
effective rate on gross **1.15%**.

**Example 2 — resident employee with declared deductions, Procedure 1, August 2026.**

Same employee, but now declaring: housing-loan interest COP 1,200,000 per month; prepaid health premium
COP 700,000 per month; **two** dependants (children aged 8 and 12).

| Line | Computation | COP |
|---|---|---|
| (A) Total taxable payments | | 8,000,000.00 |
| (B) Non-taxable — pension 4% + solidarity 1% + health 4% | | (720,000.00) |
| **(C) Subtotal** | | **7,280,000.00** |
| (D1) Housing-loan interest | Declared 1,200,000; monthly cap 100 tax units = 5,237,400 | (1,200,000.00) |
| (D2) Prepaid health | Declared 700,000; monthly cap **16 tax units = 837,984** → within cap | (700,000.00) |
| (D3) Dependants, art. 387 | 10% × 8,000,000 = 800,000; monthly cap **32 tax units = 1,675,968** → within cap | (800,000.00) |
| **Subtotal deductions (D)** | | **(2,700,000.00)** |
| (E) Exempt income — 25% | 25% × (7,280,000 − 2,700,000) = 25% × 4,580,000 | (1,145,000.00) |
| — 790-unit monthly cap | 3,447,955 → within | ok |
| **(D + E) before cap** | 2,700,000 + 1,145,000 | 3,845,000.00 |
| (F) 40% cap | 40% × 7,280,000 = **2,912,000** → **the cap bites**; (D + E) is limited to 2,912,000 | (2,912,000.00) |
| — 1,340-unit monthly cap | 5,848,430 → not reached | ok |
| Subtotal after the capped deductions | 7,280,000 − 2,912,000 | 4,368,000.00 |
| **Outside the cap:** additional dependants deduction, art. 336 num. 3 | 72 tax units × 2 dependants ÷ 12 = 12 units per month = 12 × 52,374 | (628,488.00) |
| **(G) Taxable base** | 4,368,000 − 628,488 | **3,739,512.00** |
| (H) In tax units | 3,739,512 ÷ 52,374 | **71.4002** |
| (I) Band | ≤ 95 tax units → **0%** | |
| **Withholding** | | **COP 0.00** |

Note the two ordering effects this example demonstrates: the 25% exemption is computed on the
**post-deduction** figure (4,580,000, not 7,280,000), and the 72-unit-per-dependant deduction is applied
**after and outside** the 40% cap. Both children generate **both** the art. 387 deduction and the art. 336
deduction, per Decree 2231 of 2023 art. 3.

**Example 3 — non-resident employee, August 2026.**

Facts: Spanish national, hired on a Colombian indefinite-term contract on **1 July 2026**, working in
Bogotá, salary **COP 15,000,000** per month. As at the August payroll the employee has been present
approximately 45 days and is **not yet a Colombian tax resident**.

| Line | Computation | COP |
|---|---|---|
| Gross payment | | 15,000,000.00 |
| Article 388 depuration | **Not applicable** to a non-resident | — |
| Non-taxable income (contributions) | **Not deducted** | — |
| 25% exempt income | **Not available** | — |
| Tax-free band | **None** | — |
| **Withholding — art. 408, flat 20%** | 20% × 15,000,000 | **3,000,000.00** |
| Employee social security — health 4% | Contribution base 15,000,000 | (600,000.00) |
| Employee social security — pension 4% | Unless the foreign-pension waiver of Decree 1072 art. 2.2.1.2.1.4 is claimed with evidence | (600,000.00) |
| Solidarity fund 1% | 15,000,000 ≥ 4 minimum wages (7,003,620) | (150,000.00) |
| **Net pay** | 15,000,000 − 3,000,000 − 1,350,000 | **10,650,000.00** |

**The switch.** The employee reaches 183 days of presence on or about **30 December 2026**. From the
**first payment after** that date the engine switches to the art. 383 progressive table. Had the same
employee been a resident in August, the withholding would have been **COP 1,190,532** rather
than COP 3,000,000 — depurated base COP 10,237,500 = 195.4691 tax units, in the 28% band. **No retroactive adjustment is made through payroll**; the employee reconciles in their
own annual return. Where the Colombia–Spain double-tax treaty assigns the taxing right differently, relief
is applied only on written client instruction supported by a residence certificate.

**Example 4 — irregular payment: a retention bonus paid to a resident, Procedure 1, September 2026.**

Employee on COP 8,000,000 receiving a one-off retention bonus of **COP 20,000,000**. The bonus is
contractual, is not the statutory service bonus, and is subject to a valid written non-salary pact.

| Line | Computation | COP |
|---|---|---|
| Salary | | 8,000,000.00 |
| Retention bonus (non-salary pact) | | 20,000,000.00 |
| **Total remuneration for the month** | | **28,000,000.00** |
| *Social security:* non-salary payments as a share of total | 20,000,000 ÷ 28,000,000 = **71.4%** | |
| 40% clamp — permitted non-salary | 40% × 28,000,000 | 11,200,000.00 |
| **Excess forced back into the contribution base** | 20,000,000 − 11,200,000 | **8,800,000.00** |
| **Contribution base** | 8,000,000 salary + 8,800,000 clamp excess | **16,800,000** |
| Employee health 4% + pension 4% + solidarity 1% | 9% × 16,800,000 | 1,512,000.00 |
| *Tax:* (A) total taxable payments | The non-salary pact has **no** tax effect — the bonus is fully taxable | 28,000,000.00 |
| (B) Non-taxable — the mandatory contributions actually deducted | | (1,512,000.00) |
| **(C) Subtotal** | | **26,488,000.00** |
| (D) Deductions | None declared | 0.00 |
| (E) 25% exempt income | 25% × 26,488,000 = 6,622,000; monthly 790-unit cap = **3,447,955** → **capped** | (3,447,955.00) |
| (F) 40% cap check | 40% × 26,488,000 = 10,595,200 → 3,447,955 is within | ok |
| **(G) Taxable base** | 26,488,000 − 3,447,955 | **23,040,045.00** |
| (H) In tax units | 23,040,045 ÷ 52,374 | **439.9138** |
| (I) Band | > 360 and ≤ 640 → marginal **33%** | |
| (I) Withholding, in tax units | (439.9138 − 360) × 33% + 69 = 26.3716 + 69 = **95.3716** | |
| **Withholding in COP** | 95.3716 × 52,374 | **4,994,989.65** |

Two lessons this example makes concrete: the **40% clamp** forced COP 8,800,000 of a "non-salary" bonus
back into the contribution base, and the **790-tax-unit monthly cap on the 25% exemption bit** for the
first time, limiting the exemption to COP 3,447,955 rather than the arithmetic 25% of COP 6,622,000.

*Legal basis: Tax Code (Decree-Law 624 of 1989) arts. 206, 336, 378, 379, 380, 383, 385, 386, 387, 388,
408, 589, 592, 850; Decree 1625 of 2016 arts. 1.2.4.16 and 1.6.1.13.2.40; Decree 2231 of 2023 arts. 3 and
9; Law 1393 of 2010 art. 30; Resolution DIAN 000022 of 20 February 2024; Resolution DIAN 000227 of 2025
arts. 1.3.7.1.1 and 1.3.9.1; DIAN Concepto 011108 of 29 June 2026; Decree 1072 of 2015
art. 2.2.1.2.1.4; Resolution MSPS 2388 of 2016.*
