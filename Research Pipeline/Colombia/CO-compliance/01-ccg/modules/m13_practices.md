# Module 13: Common Business Practices & Non-Statutory Rules

*Purpose: To capture prevalent, non-statutory conventions.*

> **Status of this module.** Everything below is **market convention, not statute**, except where a
> statutory constraint is expressly identified. These are the practices a Colombian payroll implementation
> will encounter and must be able to configure.

## 13.1 Non-Statutory Conventions

### Describe the common practice for off-cycle or ad-hoc payments.

**Off-cycle payments are common in Colombia and are constrained by one structural fact: the electronic
payroll document and the social-security contribution return are both monthly.** An off-cycle payment
therefore never creates a separate filing — it is aggregated into the same monthly artefacts.

| Practice | Prevalence | Handling |
|---|---|---|
| **The semi-monthly advance** | **Dominant.** The 15th is paid as a fixed advance of half the basic salary, with **no withholding tax and no social-security deduction**; the month-end payment settles everything | Not truly off-cycle — it is the standard cycle. Both payments are aggregated into one monthly contribution base, one monthly withholding calculation and one monthly XML |
| **Termination settlement paid off-cycle** | Very common — settlements are paid within days of termination rather than waiting for the cycle | Aggregated into the termination month's base for both tax and social security |
| **Off-cycle bonus** | Common — annual and performance bonuses are often paid on their own date | Aggregated into the month. Tax effect = `table(new month total) − already withheld` |
| **Payroll error correction** | Common | Where a payment was short, pay the shortfall off-cycle. **Do not defer it** — Labour Code art. 65 exposes the employer to one day's salary per day of delay at termination |
| **Salary advance** (*anticipo de salario*) | Common, typically 30% to 50% of the month's salary, recovered from the next payment | Requires a **written agreement stating the instalment and the amortisation period** (Labour Code art. 151). Not a loan — an advance on salary already accruing |
| **Emergency or hardship payment** | Occasional | Treated as an advance, or as an occasional gratuity (non-salary under art. 128) |
| **Off-cycle statutory benefit payment** | Occasional — the service bonus and severance-savings settlement are frequently paid on their own dates | Statutory dates: 30 June and 20 December for the service bonus; January for the interest; 14 February for the severance-savings deposit |

**Rules that govern any off-cycle payment.**

1. **Aggregate into the month, do not create a second monthly artefact.** One contribution return record,
   one XML document, one Form 350 line per employee per month. Resolution DIAN 000013 of 2021 art. 3 and
   DIAN Concepto 013840 (int. 1568) of 1 October 2025 are both explicit on monthly accumulation.
2. **Compute the incremental tax, not a fresh table read.** Under Procedure 1 the correct withholding on
   the second payment is `table(month total) − already withheld`. A fresh read on the off-cycle payment
   alone applies the progressive bands twice from zero and **systematically under-withholds**.
3. **Re-test the monthly thresholds on the new total.** The 10-minimum-wage exemption cut-off, the
   4-minimum-wage solidarity trigger, the 16-minimum-wage subsistence bands, the 25-minimum-wage ceiling
   and the 40% non-salary clamp are all monthly tests on the month's aggregate.
4. **Transmit the XML once, by the 10th of the following month**, covering all payments of the month.
5. **Never use an off-cycle payment to defer a statutory date.** The service-bonus and severance-savings
   dates are hard deadlines with day-rate penalties.

**A practical convention worth recording.** Because the 15th advance carries no deductions, an employee
who terminates between the 1st and the 15th will have received an advance against a month that will not be
completed. The settlement must recover it, and the recovery is subject to the minimum-wage floor of
Labour Code art. 149 num. 2 — so a large advance against a short final month can be irrecoverable through
payroll and must be pursued separately.

### How are non-recoverable draws against future commissions typically handled?

Commission arrangements are common in Colombian sales, insurance, real-estate and pharmaceutical roles.
Commissions are **salary by express statutory definition** — Labour Code art. 127 lists *"porcentajes sobre
ventas y comisiones"* — which shapes everything about how draws are handled.

| Practice | Description | Payroll treatment |
|---|---|---|
| **Guaranteed minimum plus commission** | **The dominant Colombian structure.** A fixed basic salary at or above the minimum wage, plus commission earned on top. There is no draw and no recovery | Basic salary and commission are both salary. Both enter the contribution base, the payroll-levy base and the statutory-benefit base. Commission **also enters the vacation base** (Labour Code art. 192 excludes only overtime and rest-day work) |
| **Recoverable draw** (*anticipo de comisiones*) | A monthly advance against commissions not yet earned, recovered from later commission | Structured as a **salary advance** under Labour Code art. 151, requiring a **written agreement stating the instalment and the amortisation period**. Recovery is subject to the minimum-wage floor of art. 149 num. 2 |
| **Non-recoverable draw** | A guaranteed monthly amount that is **not** recovered if commissions fall short | **This is simply salary.** It is not a loan, it is not recoverable, and it is fully contributory and fully taxable in the month it is paid. Colombia has no concept of a non-recoverable draw sitting outside salary |
| **Commission-only remuneration** | Legally permitted — Labour Code art. 132 num. 1 allows remuneration by unit of time, work, piece or task | **Constrained by the minimum wage.** Where commissions in a month fall below the minimum wage, the employer must top up to the minimum wage. The top-up is salary |

**Why Colombia rarely uses the classic non-recoverable draw.** Four statutory constraints make it
unattractive:

1. **The minimum-wage guarantee.** The employer must in any event top up to the minimum wage, so a
   guaranteed floor already exists by operation of law.
2. **The contribution-base floor.** Even a nil-commission month contributes on **1 minimum wage**, so
   there is no contribution saving in a low month.
3. **Article 149 num. 2.** Recovery of a draw may not take pay below the minimum wage without a court
   order, even with written authorisation — so recovery is often impossible in exactly the months where it
   is needed.
4. **Variable-pay averaging.** Commissions enter the statutory-benefit bases on averaged figures — the
   service bonus on the semester average, severance savings on the average of the last year where the
   salary varied in the last 3 months (art. 253), vacation on the average of the preceding year (art. 192
   num. 2). A draw structure does not reduce those averages.

**Handling the recovery of a draw where the employee terminates.** The outstanding balance is set off
against the termination settlement, but only within the art. 149 limits and only on the strength of the
written agreement. Any residue is an ordinary civil debt, pursued outside payroll. **Do not** withhold the
statutory benefits to force recovery — Labour Code art. 65's late-payment penalty of one day's salary per
day of delay will exceed the draw within weeks.

**Configuration.** Carry three distinct wage types: **commission earned** (salary, contributory, in the
vacation base), **commission advance** (a recoverable payment governed by art. 151, with a balance), and
**commission guarantee top-up** (salary). Maintain the rolling averages the statutory-benefit bases
require.

### Are there common non-statutory leave types? How are they managed and reported?

**Yes — Colombia has an active market in extra-statutory leave**, driven partly by collective agreements
and partly by employer branding. None of it is regulated, and none of it is reported to any authority.

| Non-statutory leave | Prevalence | Typical terms | Payroll treatment |
|---|---|---|---|
| **Additional vacation days** | Common in professional and multinational employers | 5 to 15 additional days on top of the statutory 15 working days | **Paid at ordinary salary.** If genuinely additional paid rest, it enters the contribution base like statutory vacation. Cash compensation of the additional days is not restricted by the art. 189 half-limit, which applies to the statutory entitlement |
| **Birthday day off** | Very common | One paid day per year | Paid leave by employer decision; salary continues; contributions continue |
| **Christmas–New Year shutdown** | Common in manufacturing | Collective shutdown, often charged against statutory vacation | Where charged against vacation, treated as vacation. Where additional, paid leave |
| **Extended bereavement leave** | Common | Beyond the statutory 5 working days, or extending to relatives outside the statutory degrees | Paid leave; salary continues |
| **Extended paternity leave** | Increasingly common | Beyond the statutory 2 weeks, employer-funded | **Employer-paid**, not recoverable from the health insurer. Fully contributory and taxable |
| **Marriage leave** | Common | 3 to 5 paid days | Paid leave |
| **Moving-house leave** | Occasional | 1 to 2 paid days | Paid leave |
| **Study or examination leave** | Common in employers with education programmes | Paid or unpaid | As agreed |
| **Volunteering day** | Growing | 1 to 2 paid days per year | Paid leave |
| **Sabbatical** | Rare, senior staff | 1 to 6 months, usually unpaid | **Unpaid leave** — suspension mechanics apply: unpaid-leave change event, levies to 0%, accruals suspended (Module 8) |
| **"Flexible Friday" / short summer hours** | Common | Early finish, no pay reduction | A working-time arrangement, not leave. Must stay within the maximum-hours rules |
| **Additional sick days without a certificate** | Common | 2 to 3 days per year at full pay | Employer-paid; **not** recoverable from the health insurer, which pays only on a certified incapacity from day 3 |

**Management and reporting.**

| Aspect | Treatment |
|---|---|
| **Legal basis** | Contract, internal work rules or collective agreement. Once granted habitually, an extra-statutory benefit may become a binding condition of employment through the principle of acquired rights, so it should be documented as revocable where the employer wants flexibility |
| **Contribution base** | Paid extra-statutory leave is **paid rest** and enters the contribution base and the payroll-levy base, exactly as statutory vacation does |
| **Statutory-benefit base** | Enters the service-bonus, severance-savings and interest bases as ordinary salary |
| **Tax** | Ordinary taxable employment income |
| **Statutory reporting** | **None.** No authority receives extra-statutory leave data. It appears in the electronic payroll XML only as ordinary remunerated leave or as part of the ordinary salary line |
| **Vacation register** | Labour Code art. 187 num. 3 requires a register of **statutory** vacation. Extra-statutory days should be tracked **separately**, so that the statutory 15 working days can be evidenced and the art. 190 accumulation limits applied to the right balance |
| **Termination** | Extra-statutory leave is **not** paid out on termination unless the contract or agreement says so. Only the statutory vacation entitlement must be settled in cash |

**The configuration rule that matters.** Keep **two separate balances** — statutory vacation and
extra-statutory leave. They have different accrual rules, different accumulation limits, different cash
compensation limits and, critically, **different termination payout obligations**. Merging them into one
balance creates an unfunded termination liability on the extra-statutory portion and makes the statutory
15-day entitlement impossible to evidence.

---

### Other prevalent non-statutory practices worth recording

| Practice | Prevalence | Notes |
|---|---|---|
| **Non-salary pacts on a substantial share of remuneration** | **Very widespread.** The standard Colombian remuneration-structuring device | Reduces the contribution base and the statutory-benefit base, **up to the 40% clamp of Law 1393 of 2010 art. 30**. **No tax effect whatsoever.** Employers commonly structure to just under 40% |
| **All-inclusive salary for senior staff** | Standard above 13 minimum wages | Contribution and payroll-levy bases at 70%; three of the four statutory benefits absorbed; **vacation is not** |
| **Employer-paid prepaid health cover** | Very common for professional staff | Structured as non-salary; the employee may deduct up to 16 tax units per month against the withholding base |
| **Meal vouchers and meal cards** | Common | Tax Code art. 387-1: not income up to 41 tax units per month where salary ≤ 310 tax units. Must be paid to a **third party** — cash for food is salary |
| **Employer-funded voluntary pension contributions** | Common for senior staff | Exempt income within the shared 30% / 3,800-unit cap; deductible for the employer up to 3,800 units per employee |
| **Extra-statutory Christmas bonus** (*prima extralegal de navidad*) | Common | Set off against the statutory service bonus under Labour Code art. 308; the employer pays only the difference where the statutory bonus is larger |
| **Extra-statutory vacation bonus** (*prima de vacaciones*) | Common | Usually structured as non-salary under a written art. 128 pact |
| **Payroll lending** (*libranza*) | **Extremely widespread** — a mainstream consumer-credit channel in Colombia | Law 1527 of 2012. The employer must deduct and remit; the aggregate must leave at least 50% of net salary. Employers routinely manage several concurrent lenders per employee |
| **Employee savings funds** (*fondos de empleados*) | Very common in larger employers | Employee contributions deducted under Labour Code art. 150 without an individual order; employer contributions usually structured as non-salary |
| **Monthly advance deposit of severance savings** | **New and growing** | Law 2466 of 2025 art. 64 permits monthly deposit of 8.33% to the fund, and written agreement to pay the 1% interest monthly. Smooths the February and January cash-flow spikes |
| **Advancing health-insurer benefits through payroll** | **Universal practice** | The employer advances sickness, maternity and paternity benefits and recovers from the insurer, because the institution pays in arrears. The engine must model a benefit line that is **paid to the employee but receivable from the institution** |
| **Paying the 100% rest-day premium early** | Occasional | Labour Code art. 179 transitional paragraph expressly permits an employer to adopt the 100% premium ahead of the 2027 date. Where it does, DIAN Concepto 013840 of 2025 confirms the differentiated percentages can coexist within a month without obstructing the electronic payroll filing |
| **Thirteenth and fourteenth salaries** | **Not a Colombian practice** | Colombia's 13th-month equivalent is the statutory service bonus, paid in two halves. There is no 14th salary |
| **Tax equalisation for expatriates** | Common in multinationals | Purely contractual; no statutory recognition. The grossed-up amount is itself taxable, so the calculation is iterative |

*Legal basis: Substantive Labour Code arts. 65, 127, 128, 132, 149, 150, 151, 179, 187 num. 3, 189, 190,
192, 253, 306, 307, 308; Law 1393 of 2010 art. 30; Law 1527 of 2012; Law 2466 of 2025 arts. 14 and 64;
Tax Code arts. 126-1, 206 num. 10, 387, 387-1, 388; Resolution DIAN 000013 of 2021 art. 3; DIAN Concepto
013840 int. 1568 of 1 October 2025.*
