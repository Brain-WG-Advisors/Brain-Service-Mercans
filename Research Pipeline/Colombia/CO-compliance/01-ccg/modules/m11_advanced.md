# Module 11: Advanced Scenarios & Cross-Cutting Logic

*Purpose: To capture complex, overarching rules that affect multiple aspects of payroll.*

## 11.1 Calculation Logic

### How is the proration and projection logic applied for income tax, social security, exemptions, and deductions?

Colombia prorates on a **30-day commercial month and a 360-day year**, and — because the system is neither
cumulative nor annualised — it **projects nothing**.

| Element | Proration | Projection |
|---|---|---|
| **Basic salary** | `S × days worked ÷ 30` | None |
| **Transport allowance** | `249,095 × days worked ÷ 30` | None |
| **Contribution base** | On the prorated salary; the 1-minimum-wage floor is **also prorated** to the contributory days | None |
| **Contribution-base ceiling** | 25 minimum wages, applied to the **monthly** base — **not** prorated | None |
| **Solidarity-fund trigger** | Tested on the **monthly** base as computed — not prorated, not annualised | None |
| **Exemption test (art. 114-1)** | Tested on the month's **actual earnings** — not prorated to a full-month equivalent, not averaged | None |
| **Payroll-levy base** | On the prorated salary plus paid rest days; **no ceiling** | None |
| **Withholding tax, Procedure 1** | Art. 385 sub-30-day rule: `(payments ÷ days) × 30` → read the table **percentage** → apply to the actual payments | None — this is a *grossing-up for rate determination*, not a projection of future income |
| **Withholding tax, Procedure 2** | The fixed percentage applies to whatever the month's base is | **Backward-looking only** — 12 months' history ÷ 13 |
| **Annual exemption caps** (790 and 1,340 tax units) | Apportioned at **one twelfth per month** — 65.8333 units = COP 3,447,955 and 111.6667 units = COP 5,848,430 | None |
| **Per-dependant deduction** (72 tax units per year, max 4) | Apportioned at 6 tax units per dependant per month = COP 314,244 | None |
| **Monthly-capped deductions** (housing interest 100 units, prepaid health 16 units, dependants 32 units) | Already monthly — no proration | None |
| **Statutory benefit accruals** | `base × days ÷ 360` for the service bonus, severance savings and interest; `base × days ÷ 720` for vacation | None |
| **Vacation entitlement** | 1.25 working days per month of service | None |

**The one genuine "projection-like" mechanic is Procedure 2, and it looks backwards.** The fixed percentage
is derived from the preceding 12 months' taxable payments divided by 13 — never from an estimate of the
year ahead. There is no projected annual salary, no notional bonus and no year-end catch-up anywhere in
Colombian payroll.

**A proration asymmetry worth stating.** The **contribution-base floor is prorated** to the contributory
days; the **contribution-base ceiling is not**. An employee hired on the 20th of a month contributes on 11
days at the prorated floor, but if that employee earns COP 60,000,000 for those 11 days the base is capped
at the **full monthly** 25-minimum-wage ceiling of COP 43,772,625, not at 11/30 of it.

### If tax or contribution rates change mid-pay period, which rates apply?

Colombia's default rule is that a statutory change **applies from its stated effective date, prospectively**,
and a pay period spanning the date must be **split**. Colombian statutes are unusually explicit about
effective dates, and 2026 has three.

| Change | Effective date | Rule |
|---|---|---|
| **Minimum wage** | 1 January | Applies from 1 January. Every derived floor, ceiling and trigger moves at once. There is no transitional or blended rate |
| **Tax unit** | 1 January | Applies to the whole tax year. Every band boundary and cap reprices |
| **Rest-day and holiday premium: 80% → 90%** | **1 July 2026** | **Split the month.** Hours worked on rest days up to 30 June carry 80%; from 1 July, 90%. Circular 101 of 2025 §4 |
| **Hourly divisor: 220 → 210** | **15 July 2026** | **Split the month.** The ordinary hour value to 14 July is `salary ÷ 220`; from 15 July it is `salary ÷ 210` — a rise of about **4.8%** in every premium. Circular 101 of 2025 |
| **Night window: 21:00 → 19:00** | 25 December 2025 | Already fully effective for all of 2026 |
| **Maximum ordinary week: 44 → 42 hours** | **15 July 2026** | Split at 15 July. Maximum ordinary plus overtime hours falls from 56 to **54 per week** |
| **Contribution rates** | No change for 2026 | — |
| **Occupational-risk class or rate** | On reclassification | Applies from the effective date of the reclassification; report a work-centre change event |
| **Employee-requested higher withholding rate** | The **month after** the request (Tax Code art. 383 par. 3) | Never mid-month |
| **Procedure 2 fixed percentage** | 1 July and 1 January | Never mid-semester |

**July 2026 is the critical month, and it has two cut-overs two weeks apart.** They must not be collapsed:

```
1 - 30 June 2026     rest-day premium 80%,  divisor 220
1 - 14 July 2026     rest-day premium 90%,  divisor 220
15 - 31 July 2026    rest-day premium 90%,  divisor 210
```

A rest-day hour worked on 10 July 2026 by an employee on COP 2,400,000 is therefore
`2,400,000 ÷ 220 × 0.90 = COP 9,818.18` of premium, while the same hour on 20 July is
`2,400,000 ÷ 210 × 0.90 = COP 10,285.71`. Applying one rate to the whole month understates or overstates
every premium hour in it.

**The tax-authority position on reporting the split.** DIAN Concepto 013840 (int. 1568) of 1 October 2025
confirms that *"the possible coexistence of differentiated premium percentages within the same month does not
constitute any obstacle to the generation, transmission and subsequent validation"* of the electronic
payroll document, and that the annex's published percentage *"must be read in accordance with the
rules in force for each specific case"*. The employer consolidates all the month's earnings,
each premium settled at the percentage applicable to its own date.

### How are tax and social security handled when an employee is paid multiple times in a single pay period?

**Both are monthly by construction, so multiple payments are aggregated into one monthly calculation.**

| Aspect | Rule |
|---|---|
| **Social security** | One contribution base per employee per month, built from **all** payments attributed to the month. One set of contributions. One record on the contribution return. Floors, ceilings and triggers all tested on the aggregate |
| **Withholding tax, Procedure 1** | The table is read on the **month's** depurated total. Where the employer withholds on each payment, the second withholding must be computed as `table(month total) − already withheld`, not as a fresh read on the second payment alone. Reading the table twice on two half-month bases **systematically under-withholds**, because the progressive bands are applied twice from zero |
| **Withholding tax, Procedure 2** | The fixed percentage is applied to each payment, or to the month's total; both give the same result, because the percentage is linear |
| **Electronic payroll XML** | **One document per employee per month**, aggregating all payments — Resolution DIAN 000013 of 2021 art. 3 and DIAN Concepto 013840 of 2025 |
| **Form 350** | One monthly aggregate |
| **The statutory service bonus under Procedure 1** | Keeps its **separate** table read even if paid in the same month as salary |
| **Severance savings and interest** | Excluded from the monthly base under both procedures, whenever paid |

**The dominant Colombian case is the semi-monthly payroll.** Market practice pays the 15th as a **fixed
advance of half the basic salary with no withholding**, and settles the whole month on the second payment:
all variable pay, the whole month's contributions and the whole month's withholding. This is
arithmetically correct and is what the engine should default to. The statutorily rigorous alternative —
grossing each half-month to 30 days under art. 385, reading the table percentage and applying it to the
actual half-month payment — produces a smoother net and is available where a client requires it.

**Off-cycle payments in the same month** (a bonus paid on the 20th, a termination settlement paid on the
25th) are aggregated into the same monthly base for both tax and social security. The tax effect of an
additional payment is therefore always `table(new month total) − already withheld`.

### How is payroll calculated if an employee's pay cycle changes mid-year?

A change of pay frequency is an **administrative change, not a statutory event**. Colombian law neither
restricts nor regulates it, beyond the outer limits of Labour Code art. 134 — one week for day wages, one
month for salaries — and the general requirement that salary be paid in **equal periods and in arrears**.

| Aspect | Effect of a frequency change |
|---|---|
| **Contribution rates, floors, ceilings, triggers** | **None** — all are monthly parameters |
| **Contribution return** | **None** — monthly regardless |
| **Electronic payroll XML** | **None** — monthly regardless. Only the pay-frequency code changes |
| **Withholding table** | **None** — the table is monthly |
| **Procedure 1** | The art. 385 sub-30-day rule applies to any transitional period shorter than a month |
| **Procedure 2** | **None** — the fixed percentage is unaffected. The 12-month accumulator simply continues |
| **Statutory benefit accruals** | **None** — they accrue on time, not on payments |
| **Vacation accrual** | **None** |

**Procedure for a mid-year change.**

```
1. Change at a MONTH BOUNDARY. Both statutory artefacts are monthly and
   keyed to the payment month; a mid-month change splits an indivisible filing.

2. Ensure no PERIOD IS SKIPPED OR DOUBLE-PAID at the transition.
   Monthly -> semi-monthly:  pay the full month on the last day, then start
                             the 15th/last-day pattern in the following month.
   Semi-monthly -> monthly:  pay the second half as normal, then move to a
                             single month-end payment.
   Weekly -> semi-monthly:   pay the outstanding weeks to the changeover date,
                             then start the new pattern. A transitional period
                             shorter than 30 days uses the art. 385 rule.

3. Update the PAY-FREQUENCY CODE on the employee record for the XML.

4. Preserve every ACCUMULATOR: 12-month taxable payments, 6-month average
   labour income, year-to-date cap consumption, benefit accruals, vacation
   balance. None of them resets.

5. Where the contract specifies the pay date, obtain the employee's WRITTEN
   AGREEMENT to the change. A unilateral change to a contractual pay date is
   a variation of an essential term and, if adverse, is capable of amounting
   to indirect dismissal under Labour Code art. 62 lit. B).

6. Do NOT extend the interval beyond the art. 134 maxima: one week for
   day wages, one month for salaries.
```

**The one real risk is a gap or an overlap at the transition**, which produces either an unpaid period —
exposing the employer to the Labour Code art. 65 late-payment penalty — or a double payment that must be
recovered under art. 151, requiring a **written** agreement with the instalment and amortisation period
stated.

*Legal basis: Substantive Labour Code arts. 62, 65, 127, 134, 151, 179 (as substituted by Law 2466 of 2025
art. 14), 161 (as substituted by art. 11); Law 2101 of 2021 arts. 3 and 4; Ministry of Labour Circular 101
of 22 September 2025 §§2.1, 4, 5.1; Tax Code arts. 383 par. 3, 385, 386, 388, 114-1; Law 100 of 1993
art. 18; Resolution DIAN 000013 of 2021 art. 3; DIAN Concepto 013840 int. 1568 of 1 October 2025;
Resolution DIAN 000238 of 2025; Decree 1469 of 2025.*

---

## 11.2 Special Employee Groups & Income

### How does taxation and social security differ for part-time employees and Board of Directors?

**Part-time employees.**

Colombia has **no distinct part-time employment regime**, no separate part-time contract type and no
reduced part-time entitlements. A part-time employee is an ordinary employee whose agreed hours are fewer
than the maximum.

| Aspect | Part-time treatment |
|---|---|
| **Minimum wage** | Applies **proportionally** to time worked. There is no separate part-time rate |
| **Contribution rates** | Identical — health 4%/8.5%, pension 4%/12%, occupational risk, levies 4%/2%/3% |
| **Contribution base** | Actual earnings, but **floored at 1 minimum wage** where the employee works a full month on part-time hours. This is the defining part-time cost effect: an employee earning COP 900,000 for a full month of part-time work still contributes on **COP 1,750,905** |
| **Statutory benefits** | Full proportional entitlement — service bonus, severance savings, interest, vacation, work clothing |
| **Paid weekly rest** | Labour Code art. 173 num. 5: where the agreed schedule does not require work on all working days of the week, the rest day is paid **in proportion to time worked** |
| **Withholding tax** | Ordinary. In practice a part-time employee is almost always in the 0% band |
| **Overtime** | Hours beyond the *agreed* ordinary day are supplementary work, even where they are below the statutory maximum (Labour Code art. 159) |
| **Part-time contributions for micro-enterprises and households** | **Law 2466 of 2025 art. 34** permits micro-enterprises and households to pay social security on a part-time basis, computed in weeks and settled monthly, and to contribute proportionally where monthly income is below the minimum wage. Requires commercial registration, accounting books and an internal contract register. Monitored by the contributions authority; may **not** be used where the work is in fact full-time (par. 2). **Outside standard corporate payroll scope** |

**Board of Directors.** The treatment turns on the **substance** of the relationship, not the title.

| Situation | Employment? | Social security | Withholding tax |
|---|---|---|---|
| **Executive director holding an employment contract** | **Yes** | Full employee treatment on the **whole** remuneration — salary and any director's fees that are consideration for the service. Employer 12% + 8.5% + occupational risk + levies; employee 4% + 4% + solidarity fund | Art. 383 progressive table |
| **Non-executive director receiving attendance fees only** | **No** — a corporate mandate, not employment | **Not** an employee contribution. The director contributes as an **independent worker** on a base of **40% of the monthly fee**, floored at 1 minimum wage (Law 1955 of 2019 art. 244) | **Art. 383 table still applies** — art. 383 par. 2, added by Law 2277 of 2022 art. 8, extends the employment table to non-employment work income using *"pagos mensualizados"*: total contract value less mandatory health and pension contributions, divided by the months of the contract |
| **Statutory legal representative on an employment contract** | **Yes** | Full employee treatment. Generally excluded from the maximum-hours rules as management staff (Labour Code art. 162 lit. a) | Art. 383 table |

**Two engine consequences.** A person who is **both** an employee and a fee-earning director has **two
different social-security bases** — full salary for the employment, 40% of the fees for the mandate — but
one withholding table, and the two accumulate against the **shared 25-minimum-wage ceiling**. A fee-only
director is outside Mercans payroll scope and is handled as an independent-contractor payment; the client
retains that responsibility.

### How is taxation handled for employees with multiple employers?

**Social security is the constrained side; tax is not.**

| Aspect | Rule |
|---|---|
| **Social security — the shared ceiling** | **Law 100 of 1993 art. 18 par. 1**: where the employee has two or more employers, contributions are made **proportionally to each remuneration** and accumulate up to the legal ceiling of 25 minimum wages. Critically: *"contributions to the health system must be made on the same base"* — the health base must match the pension base |
| **How the proportion works** | Each employer contributes on its own remuneration. Where the **combined** base would exceed 25 minimum wages, the ceiling is allocated **pro rata to each employer's share** of the total remuneration. Each employer therefore needs the **other employer's base**, which only the employee can supply |
| **The employee's duty** | To declare the second employment and the base with the other employer. Without that declaration each employer applies the ceiling to its own base alone, and the employee **over-contributes** |
| **Occupational risk** | Contributed by **each** employer on its own base; there is no shared ceiling logic in practice, because each employer insures its own exposure at its own work centre |
| **Payroll levies** | Each employer on its own payroll-levy base; **no ceiling at all**, so no allocation question arises |
| **Health and pension institutions** | The employee has **one** health insurer and **one** pension administrator. Both employers pay to the same institutions |
| **Withholding tax** | **Each employer withholds independently**, on its own payments, as if it were the only employer. There is **no** aggregation, no cumulative code, no coordination and no employer duty to enquire |
| **The consequence** | Each employer applies the 0% band, the 25% exemption and the art. 387 deductions to its own payments. The employee is therefore **systematically under-withheld** across the two employments, and reconciles — usually with a balance to pay — on the **annual income-tax return** |
| **The employee's remedy** | **Tax Code art. 383 par. 3**: request a **higher** withholding rate in writing from one or both employers, effective from the month after the request. This is the intended mechanism and the engine must support it |
| **Exemption test (art. 114-1)** | Applied by **each employer separately** on the remuneration it pays. An employee earning 6 minimum wages from each of two employers is below 10 minimum wages **at each**, so **both** employers are exonerated, even though the employee earns 12 minimum wages in total |

**Configuration.** Carry a multi-employer flag and, where declared, the other employer's contribution base,
so that the ceiling allocation can be computed. Do **not** attempt to aggregate for tax.

### What is the treatment of foreign-sourced employment income for residents?

**A Colombian tax resident is taxed on worldwide income** (Tax Code art. 9), so foreign-sourced employment
income is taxable in Colombia. What matters for payroll is **who pays it**.

| Situation | Payroll treatment |
|---|---|
| **Resident employee, paid by the Colombian employer for work performed abroad** | Ordinary Colombian payroll. Fully taxable under the art. 383 table, fully contributory. The place of performance does not change the treatment of a payment made by a Colombian employer to a resident |
| **Resident employee, paid directly by a foreign group company (a "shadow payroll" or split-payroll arrangement)** | The Colombian employer is a withholding agent only in respect of **payments it makes**. A payment made by a foreign entity with no Colombian withholding-agent status is **not** subject to Colombian withholding. The income remains **taxable to the employee**, who declares it in the annual return. **Colombia has no shadow-payroll obligation** requiring the local entity to withhold on foreign-paid amounts, unless the local entity in substance bears the cost, in which case the payment is treated as made by it |
| **Resident employee with pre-arrival foreign employment income in the year of arrival** | Residence attaches to the whole tax year in which the 183rd day falls, so pre-arrival income of that year is within the worldwide base. Not a payroll matter; the employee declares it |
| **Foreign social-security contributions paid by a resident** | Not deductible against the Colombian withholding base. Only **Colombian** mandatory pension, solidarity-fund and health contributions are non-taxable income under arts. 55 and 56 |
| **Double-tax relief** | **Tax Code art. 254** grants a credit for tax paid abroad on foreign-sourced income, limited to the Colombian tax on the same income. Claimed in the employee's **annual return**, not through payroll |
| **Treaty relief** | Colombia's treaty network and Andean Community Decision 578 may assign the taxing right to the other state. **Applied only on written client instruction supported by a residence certificate** |

**The rule of thumb for the engine:** withhold on what the Colombian entity pays; report what it pays;
do not attempt to gross up or shadow-withhold on foreign-paid amounts unless the client instructs it and
the local entity bears the cost.

### How do employer stock option plans work and how are they taxed?

Colombia has **no dedicated statutory regime for employee share schemes** — no approved-plan legislation,
no tax-advantaged option scheme and no specific valuation rule. The treatment is derived from first
principles.

| Aspect | Treatment |
|---|---|
| **Legal nature** | A benefit derived from the employment relationship. Where it is **ordinary and permanent** consideration for the service it is salary in kind (Labour Code art. 129); where it is **occasional or gratuitous**, or subject to a valid written non-salary pact, it is not salary (art. 128) |
| **Taxable event** | **Exercise** (for options) or **vesting** (for restricted shares) — the point at which the employee acquires an unconditional economic benefit |
| **Taxable amount** | The **spread**: market value of the shares at exercise or vesting, less any exercise price paid by the employee |
| **Tax character** | **Employment income**, taxable within the ordinary monthly base under the art. 383 progressive table. There is no preferential rate |
| **Withholding** | The employer withholds. Where the benefit is non-cash and cash pay is insufficient, the minimum-wage protection rules of Module 4.1 apply and the shortfall is carried |
| **Social security** | Contributory **only if the award is salary**. Where a valid written non-salary pact exists, it is out of the contribution base **up to the 40% clamp**; the excess above 40% of total remuneration goes back in |
| **Statutory benefits** | Enter the service-bonus, severance-savings and vacation bases **only if salary** |
| **Subsequent disposal** | A separate transaction for the employee — occasional gain or capital income depending on the holding period. **Outside payroll** |
| **Awards from a foreign parent** | The Colombian entity withholds where **it** makes or bears the cost of the payment. Where the foreign parent grants and settles directly at its own cost, there is no Colombian withholding agent for that payment, but the income remains taxable to a resident employee, who declares it |
| **Non-resident employee** | **Flat 20%** under art. 408 where the underlying service was performed in Colombia; foreign-source and not taxable where it was performed abroad |
| **Valuation** | No statutory scale. Market value at the taxable event, evidenced by the plan administrator's valuation or the quoted price |

**Configuration.** Model an equity award as a **taxable earnings line** carrying the spread, with an
explicit salary/non-salary flag, plus an offsetting deduction line where no cash is delivered. The
salary/non-salary flag decides the contribution and benefit consequences; it has **no** tax effect.

### How is payroll handled for employees who transfer between different legal entities mid-year?

The controlling concept is **substitution of employer** (*sustitución patronal*), Labour Code arts. 67–72,
which distinguishes sharply from a resignation-and-rehire.

**Case A — substitution of employer (business transfer, merger, spin-off).**

| Aspect | Rule |
|---|---|
| **Definition — art. 67** | A change of employer *"by virtue of an act between living persons (inter vivos)"*, with continuity of the business and of the employee in their post |
| **Effect on the contract — art. 68** | The employment contract **is not terminated, suspended or modified**. Seniority, entitlements and accruals continue unbroken |
| **Liability — arts. 69–70** | The **outgoing and incoming employers are jointly and severally liable** for obligations accrued before the substitution; the incoming employer alone is liable for those accruing after. They may agree between themselves on the internal allocation, without prejudice to the employee |
| **Statutory benefits** | **Not settled** at the transfer. Seniority runs continuously; the incoming employer inherits the accrued liability. The parties may agree to settle severance savings at the transfer date, with the employee's agreement |
| **Social security** | The incoming employer reports a **hire change event** and the outgoing employer a **termination change event** in the transfer month, under their **different tax numbers**. Contributions are split by days |
| **Withholding tax** | **Each entity withholds independently on its own payments.** There is **no** carry-over of year-to-date figures. Under Procedure 2 the incoming entity has no 12-month history of its own, so art. 386 directs it to read the table on the month's own payments until its first semi-annual calculation. **Each entity issues its own Form 220** for the part-year it paid |
| **Annual caps** | Because each entity withholds independently, **each applies the annual caps from zero**. The employee may therefore over-consume the 790-unit and 1,340-unit caps across the two entities and reconcile in the annual return |
| **Electronic payroll XML** | Each entity issues its own document under its own tax number and enablement, for the part-month it paid |
| **Occupational risk** | Re-affiliation to the incoming employer's insurer; the risk class follows the incoming employer's work centre |
| **Health insurer, pension administrator, severance-savings fund** | **Unchanged** — these are employee elections and survive the transfer |

**Case B — resignation and rehire within a group (no business continuity).** This is a genuine termination
and a genuine new hire:

1. Full termination settlement by the outgoing entity — salary, severance savings, interest, service bonus,
   unused vacation. No dismissal indemnity where the employee resigns.
2. **Social-security payment evidence for the last three months, within 60 days**, failing which the
   termination does not take effect (art. 65 par. 1).
3. Seniority **restarts** at the incoming entity, with all the consequences for the indemnity tier, the
   work-clothing qualification and the vacation accumulation limits.
4. Where the arrangement is in substance a device to break seniority, it is exposed to challenge —
   Labour Code art. 59A, added by **Law 2466 of 2025 art. 48**, prohibits employer manoeuvres of evasion
   (*maniobras de elusión*).

**The engine must carry a "continuity of service" flag** distinguishing the two cases, because it drives
seniority, the indemnity tier and whether benefits are settled at the transfer.

### What is the process for an employee who changes citizenship or residency status during the fiscal year?

**Tax residence change — the operationally significant case.**

| Direction | Trigger | Payroll effect |
|---|---|---|
| **Non-resident → resident** | The employee reaches **183 days of presence** in any 365-day period | Switch from the **flat 20%** of art. 408 to the **art. 383 progressive table**, **from the payment following** the date the test is met. Confirmed by **DIAN Concepto 011108 of 29 June 2026**, which rejected withholding under art. 383 from day one in anticipation of residence: status is determined *"at the time of each payment"*. **No retroactive adjustment through payroll**; the employee reconciles in the annual return |
| **Resident → non-resident** | Departure such that the 183-day test is no longer met for the relevant period | Switch to the flat 20% for Colombian-source payments; **no withholding** on payments for services performed entirely outside Colombia (DIAN Oficio 28380 of 2019) |

**Configuration requirements.**

1. A **residence flag with an effective date** on the employee record.
2. **Re-evaluation every payroll period**, not annually.
3. A **presence-day accumulator** rolling over any 365-day window — the test is not calendar-year based.
4. A **prospective-only** switch. The engine must never restate prior months.
5. Where the year straddles the threshold, residence attaches to the **year in which the 183rd day falls**.

**Citizenship change — far less consequential.** Colombian nationality does **not** by itself determine tax
residence for the presence test, and it does not change any contribution rate. What it changes:

| Aspect | Effect |
|---|---|
| **Identity document** | From a foreigner identity card (code 22) or permit to a **citizen identity card (code 13)**, with a **new document number**. This is a master-data change that must be reported as a change event on the contribution return and must be reflected in the electronic payroll XML and the annual certificate |
| **Foreign pension-system waiver** | A foreign national who had waived Colombian pension affiliation under Decree 1072 of 2015 art. 2.2.1.2.1.4 on proof of foreign coverage should be reviewed on naturalisation |
| **Tax residence** | Article 10's nationality-plus-connection tests become available. A **Colombian national** is resident where the spouse, dependants, 50%+ of assets, 50%+ of income or the place of asset administration is in Colombia — tests that do not apply to a foreign national |
| **Contribution rates** | **None** |

**The migration-status case, which is more common in practice.** A change from a Special Permanence Permit
(code 47) or a Temporary Protection Permit to a foreigner identity card (code 22) is also a
document-number change requiring the same reporting. Note the open item recorded in Module 2.2: the
electronic-payroll annex has **no code for the Temporary Protection Permit**, and code 47 is the only
available proxy.

### Are there specific rules for expatriates or inpatriates?

**Colombia has no expatriate tax regime, no inpatriate concession and no impatriate relief.** There is no
reduced rate, no exempt allowance, no tax-free housing or schooling benefit, and no time-limited
concession for inbound assignees. Expatriates are taxed under the ordinary rules, with residence as the
only switch.

| Aspect | Rule for an inbound assignee |
|---|---|
| **Labour law** | **Fully applicable.** Labour Code art. 2 applies the Code to all work performed in Colombian territory, whatever the employee's nationality. **Law 2466 of 2025 art. 37**: *"Immigration status shall not be an impediment to claiming labour guarantees"* — migration status is no bar to labour rights |
| **Withholding tax** | Flat 20% under art. 408 until residence is acquired; the art. 383 table thereafter. See Module 6 |
| **Health and occupational risk** | **Compulsory**, with no waiver |
| **Pension** | Compulsory, **unless** the employee proves affiliation to a pension system abroad and elects in writing not to affiliate — Decree 1072 of 2015 art. 2.2.1.2.1.4 |
| **Totalisation agreements** | Colombia has bilateral social-security agreements with **Spain, Chile, Uruguay, Argentina, Ecuador and Peru**, and is party to the **Ibero-American Multilateral Social Security Convention**. A posted worker with a certificate of coverage may remain covered at home for the certified period. **Colombian occupational-risk cover is nonetheless required for work performed in Colombia** |
| **Double-tax treaties** | Applied only on written client instruction with a residence certificate |
| **Expatriate allowances** — housing, schooling, cost-of-living, hardship, home leave | **Fully taxable.** No exemption exists. They are **salary** unless a valid written non-salary pact under Labour Code art. 128 applies, in which case they are out of the contribution base **up to the 40% clamp** |
| **Tax equalisation and gross-up** | Permitted contractually. The grossed-up amount is itself taxable income, so the calculation is iterative. **No statutory recognition** — a purely commercial arrangement |
| **Split payroll** | The Colombian entity withholds only on what it pays or bears. See the foreign-sourced income question above |
| **Work permit and visa** | A precondition of lawful employment, not a payroll parameter, but the visa type drives the available identity-document code |
| **Vacation accumulation** | Labour Code art. 190 allows **4 years'** accumulation for *"foreign nationals who render their services in places other than those of their family members' residence"* — one of the few express expatriate provisions in Colombian law |
| **Termination** | Identical to a Colombian national. All statutory benefits and indemnities apply in full |
| **Transnational teleworkers** | **Law 2466 of 2025 art. 54**: a contract concluded in Colombia is governed by Colombian law, and the occupational-risk insurer must guarantee occupational cover in the country where the service is performed, with additional foreign insurance at the employer's cost where needed |

**The single largest expatriate configuration risk** remains the residence switch. A COP 15,000,000 salary
produces **COP 3,000,000** of withholding as a non-resident and **COP 1,190,532** as a resident — a
2.5-fold difference that turns on one date. See the worked example in Module 6.3.

*Legal basis: Substantive Labour Code arts. 2, 59A, 62, 67, 68, 69, 70, 71, 72, 128, 129, 159, 162, 173
num. 5, 190 (art. 59A added by Law 2466 of 2025 art. 48); Law 100 of 1993 art. 18 par. 1; Law 1955 of 2019
art. 244; Law 2466 of 2025 arts. 34, 37, 45, 48, 54; Tax Code (Decree-Law 624 of 1989) arts. 9, 10, 55, 56,
114-1, 254, 383 (pars. 2 and 3), 386, 388, 408; Law 2277 of 2022 art. 8; Decree 1072 of 2015
art. 2.2.1.2.1.4; DIAN Concepto 011108 of 29 June 2026; DIAN Oficio 28380 of 2019; Andean Community
Decision 578; the Ibero-American Multilateral Social Security Convention.*
