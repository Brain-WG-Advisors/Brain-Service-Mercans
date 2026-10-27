# Module 1: Foundational Jurisdictional Parameters

*Purpose: To establish the core environmental settings that govern all payroll operations in Colombia for fiscal year 2026.*

## 1.1 Fiscal, Currency, and Language

### What is the statutory tax year?

The statutory tax year in Colombia is the **calendar year: 1 January to 31 December**. There is no
alternative fiscal-year concept for employment income. The annual value of the tax indexation unit is
fixed for the calendar year — Resolution DIAN 000238 of 15 December 2025, article 1, fixes the value
"that will govern **during the year 2026**". All employer payroll obligations that reset annually
(the withholding certificate, the third-party information return, the severance-savings deposit and the
interest payment on severance savings) are keyed to that calendar year.

The payroll year and the tax year are the same period. Employer accruals for the statutory benefit
entitlements are computed on a **360-day commercial year of twelve 30-day months**, which is the
convention the Labour Code uses throughout (Substantive Labour Code, *Código Sustantivo del Trabajo*,
Decree 2663 of 1950, articles 249, 306); this is an accrual convention, not a separate fiscal year.

*Source: Tax Code (Estatuto Tributario, Decree-Law 624 of 1989) art. 868; Resolution DIAN 000238 of
15-12-2025 art. 1.*

### Can employers adopt an alternate tax year? If yes, under what circumstances and what are the implications?

**No.** Colombia does not permit an alternate tax year for payroll or for employment-income withholding.
The calendar year is mandatory for every employer, in every sector, and for every employee category.
There is no election, no approval route and no transitional-year mechanism.

Two consequences follow for configuration:

1. All annual caps expressed in tax units (the 790-unit exempt-income cap, the 1,340-unit combined
   deductions cap, the 72-unit-per-dependant deduction) run 1 January to 31 December and cannot be
   shifted.
2. Where an employer joins the Mercans platform mid-year, year-to-date accumulators must be loaded from
   the previous provider on a calendar-year basis. See Module 2.3.

The only date in the Colombian payroll year that is *not* a calendar-year boundary is the June/December
recalculation of the fixed withholding percentage under Withholding Procedure 2 (Tax Code art. 386),
which runs on a six-month cycle inside the calendar year. That is a withholding-method cycle, not a
fiscal year.

### What is the official currency for payroll processing and reporting? Provide the ISO code.

The official currency is the **Colombian peso**, ISO 4217 code **COP**, numeric code 170, symbol `$`.

Resolution DIAN 000013 of 2021 article 26 requires that the electronic payroll support document — the
instrument that carries the legal itemisation duty in Colombia — be issued in Spanish and in Colombian
pesos: *"The Spanish language and the Colombian peso must be used"*. Another currency may be shown **in
addition**, never instead.

| Item | Rule |
|---|---|
| Statutory filings (withholding return, social-security return, third-party information return) | Whole pesos only |
| Electronic payroll XML | Two decimal places, dot as the decimal separator, no thousands separator, no currency symbol (e.g. `1750905.00`) |
| Payslip / human-readable documents | Colombian print convention: dot for thousands, comma for decimals (e.g. `1.750.905,00`) |
| Foreign-currency salary | The employee may demand payment in Colombian pesos at the official exchange rate of the payment date (Labour Code art. 135). For the payroll-tax base of the family-welfare contributions, foreign-currency payments are converted at the official rate on the **last day of the month** (Law 21 of 1982 art. 17) |

The peso has no circulating sub-unit used in payroll. Decimals exist only inside the electronic XML and
in internal calculation; every statutory monetary declaration is in whole pesos.

### What is the official language for statutory reports and employee payslips?

**Spanish**, exclusively, for statutory purposes.

Resolution DIAN 000013 of 2021 article 26 is the operative rule: Spanish and the Colombian peso must be
used. A second language may be **added** to a payslip for the employee's convenience — an English column
alongside the Spanish one is permitted — but it may never replace the Spanish text, and the Spanish
version governs in any discrepancy.

There is no separate labour-law language rule for payslips, because — as Module 10.3 explains —
Colombia has **no statutory payslip-content article in its labour code at all**. The itemisation and
language duty is imposed by tax law, through the electronic payroll regime.

*Legal basis: Substantive Labour Code (Decree 2663 of 1950) arts. 134, 135; Tax Code (Decree-Law 624 of
1989) art. 868; Resolution DIAN 000238 of 15-12-2025 art. 1; Resolution DIAN 000013 of 2021 art. 26;
Law 21 of 1982 art. 17.*

---

## 1.2 Pay Cycles and Dates

### What are the permissible payroll payment frequencies in the country?

Labour Code article 134 sets the outer limits:

> *"Salary in money must be paid in equal periods and in arrears, in legal tender. The pay
> period for day wages (jornales) may not exceed one week, and for monthly salaries may not exceed one month."*

In plain terms: salary must be paid **in equal periods, in arrears**, and the maximum interval is

| Remuneration type | Maximum interval |
|---|---|
| Day wages (*jornal* — manual/daily-rated workers) | **One week** |
| Salary (*sueldo* — monthly-rated staff) | **One month** |

Any shorter frequency is permitted. The frequencies the electronic payroll code table recognises
(Technical Annex §5.5.1) and that the engine must therefore support are:

| Code | Frequency | Practical use in Colombia |
|---|---|---|
| 1 | Weekly | Daily-rated and agricultural workers |
| 2 | Every ten days (*decenal*) | Rare |
| 3 | Every fourteen days | Rare |
| 4 | **Semi-monthly (*quincenal*)** | **The dominant private-sector practice** — paid on the 15th and the last day of the month |
| 5 | **Monthly** | Common for management and professional staff |
| 6 | Other | Exception handling |

**Critical configuration point.** Whatever the payment frequency, the **electronic payroll support
document is generated monthly**, one per employee per month, aggregating the whole month's earnings and
deductions. Resolution DIAN 000013 of 2021 article 3 is explicit that the document is monthly
*"irrespective of whether the obliged party makes payments in different or shorter periods"*, and
DIAN Concepto 013840 (int. 1568) of 1 October 2025 restates the same monthly-accumulation principle. A
semi-monthly payroll therefore produces **two payments but one monthly XML**.

Overtime and the night-work premium must be paid with the ordinary salary of the period in which they
were worked, or at the latest with the salary of the **following** period (Labour Code art. 134 num. 2).

### For each frequency, detail the corresponding statutory reporting and payment deadlines for both income tax withholding and social security contributions.

The deadlines are **independent of the payroll frequency**. Both the withholding-tax return and the
social-security contribution are **monthly obligations keyed to the employer's tax identification
number**, regardless of whether the employer pays weekly, semi-monthly or monthly.

**(a) Wage withholding tax — Form 350, monthly.** Deadlines fall on **business days** of the following
month and are keyed to the **last digit** of the employer tax number (excluding the verification digit).

| Last digit of employer tax number | Filing and payment deadline |
|---|---|
| 1 | 7th business day of the following month |
| 2 | 8th business day |
| 3 | 9th business day |
| 4 | 10th business day |
| 5 | 11th business day |
| 6 | 12th business day |
| 7 | 13th business day |
| 8 | 14th business day |
| 9 | 15th business day |
| 0 | 16th business day |

*Source: Single Regulatory Decree 1625 of 2016 art. 1.6.1.13.2.33, as set by Decree 2229 of 2023. Form
350 is prescribed by Resolution DIAN 000031 of 29 February 2024, in force from 1 August 2024.*

**(b) Social security and payroll-tax contributions — the integrated contribution return (*Planilla
Integrada de Liquidación de Aportes*, PILA), monthly.** Deadlines fall on **business days** of the
following month and are keyed to the **last two digits** of the employer tax number.

| Business day of the following month | Last two digits of employer tax number |
|---|---|
| 2nd | 00–07 |
| 3rd | 08–14 |
| 4th | 15–21 |
| 5th | 22–28 |
| 6th | 29–35 |
| 7th | 36–42 |
| 8th | 43–49 |
| 9th | 50–56 |
| 10th | 57–63 |
| 11th | 64–69 |
| 12th | 70–75 |
| 13th | 76–81 |
| 14th | 82–87 |
| 15th | 88–93 |
| 16th | 94–99 |

*Source: Decree 780 of 2016 art. 3.2.2.1, as substituted by Decree 1990 of 2016 art. 2.*

Two component funds carry their own statutory wording, both absorbed in practice into the integrated
return calendar above: the occupational-risk contribution is due *"within the first ten common days of
the following month"* (Decree 1072 of 2015 art. 2.2.4.3.7), and the family-welfare payroll taxes are due
*"within the first ten days of the month following the one being settled"* (Law 21 of 1982 art. 10).

**(c) Electronic payroll support document — monthly.** Transmitted for validation *"within the first ten
(10) days of the month following"* the payment or credit (Resolution DIAN 000013 of 2021 art. 8).

**Frequency-specific point.** For a **weekly** payroll the four or five weekly payments of a calendar
month are summed into one monthly contribution return and one monthly XML. For a **semi-monthly**
payroll the two half-month payments are likewise summed. Neither the contribution rates nor the
withholding table change with frequency; only Withholding Procedure 1 has an explicit sub-monthly rule —
for a period **shorter than 30 days**, divide the payments by the number of days, multiply by 30, read
the resulting percentage from the table, and then apply that percentage to the actual payments of the
period (Tax Code art. 385).

### Describe the statutory rule for handling pay dates that fall on a weekend or public holiday.

There are two distinct rules, and they must not be conflated.

**For statutory filing and payment deadlines: the business-day rule is built into the deadline itself.**
Both the withholding-tax and the social-security calendars above are expressed in **business days**
(*días hábiles*) of the following month, not calendar days. Saturdays, Sundays and the 18 public holidays
are simply not counted. There is therefore no "roll forward" step to configure — the engine counts
business days from the first business day of the month. Where a component statute is expressed in
**common days** (the occupational-risk contribution, Decree 1072 art. 2.2.4.3.7), the integrated return
calendar in business days prevails in practice because the return cannot be filed on a non-business day.

**For paying the employee: there is no statutory displacement rule.** The Labour Code fixes only that
payment be made in equal periods and in arrears (art. 134) and at the place of work, during work or
immediately after it ends (art. 138). It does not say what happens when the contractual pay date is a
Sunday or a holiday. The universal Colombian business practice, which Mercans applies as the default, is
to **bring the payment forward to the last preceding business day**, never to defer it — deferral would
expose the employer to the late-payment penalty of Labour Code art. 65 if the contract or the internal
work rules fix the date.

The public-holiday calendar that drives the business-day count is in Module 1.4. Note that most Colombian
holidays are **moved to the following Monday** under the "Emiliani" rule, which changes the business-day
count from year to year — the engine must use a maintained holiday calendar, not a fixed table.

### What are the common payroll pay dates and cut-off dates for payroll processing?

These are business conventions, not statutory rules, and they are recorded here because the engine must
be configured to them.

| Pay pattern | Prevalence | Pay dates | Typical processing cut-off |
|---|---|---|---|
| Semi-monthly | Dominant across the private sector | **15th and last calendar day** of the month | Around the 10th and the 25th — 3 to 5 business days before payment |
| Monthly | Common for management, professional and expatriate staff | **Last calendar day** of the month, or the 30th | Around the 20th to 25th |
| Weekly | Daily-rated, construction and agricultural labour | End of the working week (Friday or Saturday) | 1 to 2 business days before payment |

Practical notes for configuration:

- Under the semi-monthly pattern the first payment (the 15th) is customarily a **fixed advance of half
  the basic salary with no withholding tax**, and the second payment (month-end) settles the full month:
  all variable pay, all overtime and premiums, the whole month's social-security deductions and the whole
  month's withholding tax. This is the single most common source of net-pay reconciliation queries.
- Because the electronic payroll XML is monthly, the transmission cut-off is driven by the **10th day of
  the following month**, not by the pay date.
- Employers commonly close variable-pay input (overtime hours, commissions, absence) between the 20th
  and 25th, and treat later items as retrospective adjustments in the next month (Module 9.2).
- December payroll is customarily accelerated so that the second half of the statutory service bonus,
  due by 20 December, and the December salary are paid together in the third week of December.

*Legal basis: Substantive Labour Code arts. 134, 135, 138, 139; Decree 780 of 2016 art. 3.2.2.1
(substituted by Decree 1990 of 2016 art. 2); Decree 1625 of 2016 art. 1.6.1.13.2.33 (as set by Decree
2229 of 2023); Decree 1072 of 2015 art. 2.2.4.3.7; Law 21 of 1982 art. 10; Resolution DIAN 000013 of 2021
arts. 3 and 8; Resolution DIAN 000031 of 2024; DIAN Concepto 013840 int. 1568 of 1 October 2025; Tax Code
art. 385.*

---

## 1.3 Extra Pay Period Handling

### Describe the statutory handling and calculation adjustments required for fiscal years containing extra pay periods (e.g., 53 weekly pays).

**Colombia has no statutory extra-pay-period mechanism, and for the two dominant frequencies the problem
does not arise.**

The reason is structural. Colombian payroll is built on a **360-day commercial year of twelve 30-day
months**. Monthly and semi-monthly payrolls therefore produce exactly 12 and exactly 24 periods every
year, without exception, in every calendar year including leap years. A monthly-paid employee is paid one
monthly salary for a 28-day February and the same monthly salary for a 31-day March; the 30-day
convention absorbs the difference. There is no 13th monthly period and no "extra" semi-monthly period.

The one genuine 13th payment in Colombia — the statutory service bonus (*prima de servicios*), 30 days'
salary per year paid in two halves — is **not** an extra pay period. It is a separate statutory benefit
with its own accrual, its own payment dates (by 30 June and by 20 December) and its own withholding
treatment. It is covered in Module 4.5 and Module 7, not here.

**Weekly payrolls are the only case where the question bites.** A calendar year contains 52 weeks and one
or two extra days, so a weekly payroll can contain **53 pay dates** in some years. Colombian law provides
no adjustment rule. Two points settle the treatment:

1. The weekly wage is a genuine payment for a genuine week worked. It is fully due, fully contributory
   and fully taxable. There is no statutory basis for reducing 53 weekly payments to a 52-week annual
   equivalent.
2. Social security and payroll taxes are **not** calculated per pay period. They are calculated on the
   **monthly** contribution base, which is the sum of the salary payments attributable to the calendar
   month. A month containing five weekly pay dates simply has a larger monthly contribution base than a
   month containing four. There is no distortion to correct.

### Detail the impact on annualized tax calculations and social security contributions.

**Social security: no impact requiring adjustment, but two thresholds must be watched.**

Contributions are computed on the monthly contribution base, so a five-payment month raises that base for
that month only. Two monthly tests can flip as a result:

| Test | Effect of a five-payment month |
|---|---|
| Payroll-tax exemption test (Tax Code art. 114-1): employee earns **less than** 10 minimum wages | A weekly-paid employee near the line can lose the exemption for that month only, adding employer health 8.5% + apprenticeship-training levy 2% + family-welfare levy 3% |
| Solidarity pension fund trigger: contribution base **at or above** 4 minimum wages | A five-payment month can trigger the 1% employee surcharge for that month only |
| Contribution-base ceiling: 25 minimum wages | A five-payment month can reach the ceiling that a four-payment month does not |

All three tests are applied **per employee, per month**, on that month's actual earnings. They are not
averaged over the year and they are not annualised. The engine must therefore evaluate them on the
month's real total, and must **not** normalise a five-payment month to a notional four-payment amount.

**Withholding tax: the effect depends on which of the two withholding procedures is elected.**

- **Withholding Procedure 1** (Tax Code art. 385) reads the tariff table on the actual payments of the
  month. A five-payment month therefore produces a higher monthly base, a higher marginal band and a
  higher withholding — which is arithmetically correct, because the employee did receive more income in
  that month. No adjustment is made and none is required; the annual return reconciles it.
- **Withholding Procedure 2** (Tax Code art. 386) is inherently immune. The fixed withholding percentage
  is computed in June and December by summing the **last 12 months'** taxable payments and **dividing by
  13**. The 13 divisor already smooths a 53-week year, and the percentage is then applied to whatever the
  month's actual base is. A 53rd week raises the base it is applied to but does not distort the rate for
  that period; it is picked up in the next semi-annual recalculation.

For a weekly-paid employee, Withholding Procedure 2 is the technically cleaner election precisely because
of this smoothing. Note, however, that weekly-paid employees in Colombia are overwhelmingly at or near
the minimum wage and therefore fall in the 0% withholding band entirely, so the point is usually
academic in practice.

### If optional adjustment methods are permitted, provide a step-by-step guide.

**No optional adjustment method is permitted, because none exists in Colombian law.** There is no
statutory election, no tax-authority-approved smoothing method, and no administrative doctrine
authorising an employer to re-spread a 53rd weekly payment across the year. Any such adjustment would
under-declare the contribution base of the month in which the payment falls and would expose the employer
to a contribution-audit assessment by the contributions authority (*Unidad de Gestión Pensional y
Parafiscales*, UGPP).

The correct handling is a three-step **procedure**, not an adjustment:

**Step 1 — attribute each weekly payment to a calendar month.** Use the payment date. A pay period
straddling a month end is attributed to the month in which the payment falls, because both the
contribution return and the electronic payroll XML are keyed to the payment or credit month.

**Step 2 — build the monthly contribution base from the attributed payments.** Sum all salary-constituting
payments attributed to the month, then apply, in this order: the 40% non-salary clamp, the 70% rule for
all-inclusive salary, the 1-minimum-wage floor, the 25-minimum-wage ceiling, and the round-up to the
nearest whole peso. The result is the contribution base for that month, whether it was built from four
payments or five.

**Step 3 — evaluate every monthly test on that base, without normalisation.** Exemption test, solidarity
fund trigger, subsistence sub-account band, floor and ceiling — all on the actual base.

*Worked illustration.* A weekly-paid employee on COP 500,000 per week. In a four-payment month the
contribution base is COP 2,000,000; in a five-payment month it is COP 2,500,000. Both are above the
1-minimum-wage floor of COP 1,750,905 and below the 4-minimum-wage solidarity trigger of COP 7,003,620,
so the contribution outcome differs only in amount, not in structure:

| Item | Four-payment month | Five-payment month |
|---|---|---|
| Contribution base | 2,000,000 | 2,500,000 |
| Employee health 4% | 80,000 | 100,000 |
| Employee pension 4% | 80,000 | 100,000 |
| Solidarity pension fund | 0 (base < 4 minimum wages) | 0 (base < 4 minimum wages) |
| Employer pension 12% | 240,000 | 300,000 |
| Employer health 8.5% | 0 — exempt (< 10 minimum wages) | 0 — exempt (< 10 minimum wages) |

No re-spreading, no annualisation, no correcting entry.

*Legal basis: Substantive Labour Code arts. 134, 249, 306; Law 100 of 1993 arts. 18 and 20 (as
substituted by Law 797 of 2003 arts. 5 and 7); Tax Code arts. 114-1, 385, 386; Decree 780 of 2016
art. 3.2.1.5 (substituted by Decree 1990 of 2016 art. 1).*

---

## 1.4 Holiday Calendar

### What are the official public holidays?

Colombia has **18 paid public holidays**, fixed by Labour Code article 177 as substituted by Law 51 of
1983 articles 1 and 2, and restated by Ministry of Labour Circular 101 of 22 September 2025 §4.

Nine of them are subject to the "Emiliani" transfer rule (Labour Code art. 177 num. 2): where the
festivity does not fall on a Monday, the paid holiday **moves to the following Monday**. The nine
transferable dates are 6 January, 19 March, 29 June, 15 August, 12 October, 1 November, Ascension, Corpus
Christi and the Sacred Heart. The remaining nine are fixed to their calendar date.

**Colombia 2026 public-holiday calendar**

| # | Holiday | Statutory date | Observed 2026 | Day | Transferred? |
|---|---|---|---|---|---|
| 1 | New Year's Day | 1 January | **1 January 2026** | Thursday | Fixed |
| 2 | Epiphany | 6 January | **12 January 2026** | Monday | Yes |
| 3 | Saint Joseph's Day | 19 March | **23 March 2026** | Monday | Yes |
| 4 | Maundy Thursday | Movable | **2 April 2026** | Thursday | Fixed |
| 5 | Good Friday | Movable | **3 April 2026** | Friday | Fixed |
| 6 | Labour Day | 1 May | **1 May 2026** | Friday | Fixed |
| 7 | Ascension of the Lord | Easter + 39 days | **18 May 2026** | Monday | Yes |
| 8 | Corpus Christi | Easter + 60 days | **8 June 2026** | Monday | Yes |
| 9 | Sacred Heart of Jesus | Easter + 68 days | **15 June 2026** | Monday | Yes |
| 10 | Saints Peter and Paul | 29 June | **29 June 2026** | Monday | Already Monday |
| 11 | Independence Day | 20 July | **20 July 2026** | Monday | Fixed (already Monday) |
| 12 | Battle of Boyacá | 7 August | **7 August 2026** | Friday | Fixed |
| 13 | Assumption of the Virgin | 15 August | **17 August 2026** | Monday | Yes |
| 14 | Columbus Day (*Día de la Raza*) | 12 October | **12 October 2026** | Monday | Already Monday |
| 15 | All Saints' Day | 1 November | **2 November 2026** | Monday | Yes |
| 16 | Independence of Cartagena | 11 November | **16 November 2026** | Monday | Yes |
| 17 | Immaculate Conception | 8 December | **8 December 2026** | Tuesday | Fixed |
| 18 | Christmas Day | 25 December | **25 December 2026** | Friday | Fixed |

Easter Sunday 2026 falls on **5 April 2026**, from which the four movable religious dates are derived.

**Payroll effect.** A public holiday is paid at one day's ordinary salary with no deduction for
non-attendance (Labour Code arts. 174, 177). Work performed on a public holiday is remunerated under the
obligatory-rest-day rules — see Module 4.4, and note the **1 July 2026** step in the premium from 80% to
90%.

### Are there any regional, state-specific, or company-specific holidays?

**No regional or departmental public holidays exist in Colombia.** The 18 days above apply uniformly
across all 32 departments and the Capital District. Colombia's holiday statute is national and there is
no departmental or municipal power to create an additional paid public holiday binding on private
employers.

Three qualifications, each of which the engine must be able to represent:

| Category | Status | Payroll treatment |
|---|---|---|
| **Municipal or departmental civic days** (local fairs, patron-saint days, sporting events) | Not statutory public holidays. Local authorities may declare a civic day, but it binds only public offices in that jurisdiction | **No** obligatory-rest-day premium. If a private employer chooses to close, it is paid leave by employer decision, configured as a non-statutory paid absence |
| **Company or collective-agreement holidays** | Permitted and common — a collective agreement or company policy may grant additional paid days off (an employee's birthday, the company anniversary, additional days between Christmas and New Year) | Contractual, not statutory. Paid at ordinary salary. Work performed on such a day attracts **no** statutory holiday premium, because the day is not a Labour Code art. 177 holiday |
| **Agreed alternative rest day** | Statutory, but employee-specific | Labour Code art. 179 par. 3 (as substituted by Law 2466 of 2025 art. 14) allows the parties to agree **in writing** that the obligatory weekly rest day is a day other than Sunday. Absent an express written agreement, **Sunday is presumed**. Circular 101 of 2025 §5 stresses that the substitution is not a discretionary employer choice: it is limited to objective, demonstrable causes such as a continuous production process, imperative public interest, humanitarian or seasonal conditions, or shift patterns that make a collective rest day unworkable |

The last row is a genuine per-employee master-data field, not a company setting — see Module 2.2.

*Legal basis: Substantive Labour Code arts. 172, 173, 174, 177 (as substituted by Law 51 of 1983 arts. 1
and 2) and art. 179 (as substituted by Law 2466 of 2025 art. 14); Ministry of Labour Circular 101 of
22 September 2025 §§4 and 5.*

---

## 1.5 Rounding and Precision Rules

### What are the statutory or common business practice rules for rounding final net pay and individual calculation components?

**Colombia runs three different, legally mandated rounding regimes inside the same payroll month.** This
is the most frequently mis-implemented mechanical rule in Colombian payroll, and the three regimes must
never be unified.

**Regime 1 — Social security and payroll taxes: round UP.**

Decree 780 of 2016 article 3.2.1.5, as substituted by **Decree 1990 of 2016 article 1**:

> *"1. The amount of the contribution base corresponding to each contributor must be rounded to the
> **nearest higher peso**.
> 2. The value of the **assessed contributions** for each contributor and the value of the **interest** must
> be rounded to the **nearest higher multiple of 100**."*

| Item | Rule | Example |
|---|---|---|
| Contribution base | Round **up** to the next whole peso | 8,000,000.40 → 8,000,001 |
| Each contribution amount | Round **up** to the next multiple of **100** | Occupational risk 41,760 → **41,800** |
| Late-payment interest | Round **up** to the next multiple of 100 | — |

Always upward. Never to nearest. Applied **per contributor and per fund**, not to the employer total.

**Regime 2 — Electronic payroll XML: round half to even, with a ±2.00 tolerance.**

The Technical Annex to the electronic payroll support document, §1.1.1.1:

> *"Monetary values shall allow an **error tolerance of + - 2.00**. … The rounding formula
> used … is **round-half-to-even** … and corresponds to Colombian technical standard NTC 3711 (international
> technical standard JIS Z 8401)."*

Two decimal places are carried. The XML additionally provides an explicit `Redondeo` element in which the
residual difference between the sum of the detail lines and the declared total is reported. The engine
must isolate the residual there rather than distorting a detail line.

**Regime 3 — Tax return forms: round to the nearest 1,000.**

Tax Code article 577: *"Amounts entered on tax return forms
must be rounded to the **nearest multiple of one thousand (1000)**."* Fractions below 500 round down; 500 and
above round up. This governs **Form 350** (the monthly withholding return) at the aggregate level only.
It does **not** apply to the individual employee's withholding amount, to the payslip, or to the XML.

**Net pay itself.** There is no statutory rounding rule for net pay. Net pay is the arithmetic residue of
gross less deductions, each deduction having been rounded under its own regime. Mercans presents net pay
to **two decimals** on the payslip and in the XML, and pays the whole-peso amount to the bank where the
paying bank does not accept centavos. Any residual centavo difference is carried in the next period, never
absorbed into a statutory deduction.

**Worked illustration — one employee, one month, three regimes.** Employee on COP 8,000,000, occupational
risk class I at 0.522%:

| Concept | Raw | Contribution return | XML | Form 350 |
|---|---|---|---|---|
| Contribution base | 8,000,000.00 | 8,000,000 (up to peso) | 8000000.00 | — |
| Employee health 4% | 320,000.00 | 320,000 (up to 100) | 320000.00 | — |
| Employer occupational risk 0.522% | 41,760.00 | **41,800** (up to 100) | 41760.00 | — |
| Withholding tax | 92,049.30 | — | 92049.30 | aggregated, then to nearest 1,000 |

The same underlying figure legitimately appears as three different numbers in three different artefacts.
That is correct, and an engine that "harmonises" them is wrong.

### What level of decimal precision is required for statutory reporting?

| Artefact | Precision | Basis |
|---|---|---|
| Integrated social-security contribution return | **Whole pesos**; contribution amounts additionally in multiples of 100 | Decree 780 of 2016 art. 3.2.1.5 (Decree 1990 of 2016 art. 1) |
| Electronic payroll XML | **Two decimal places**, dot decimal separator, no thousands separator, no currency symbol; ±2.00 tolerance; round half to even | Technical Annex §1.1.1.1 |
| Form 350 monthly withholding return | **Whole thousands** | Tax Code art. 577 |
| Form 220 annual income and withholding certificate | **Whole pesos** | Tax Code arts. 378–379 |
| Third-party information return, Format 2276 | **Whole pesos** | Resolution DIAN 000227 of 2025 art. 1.3.7.1.1 |
| Payslip / human-readable document | Two decimals, Colombian convention `1.750.905,00` | Convention; no statutory rule (see Module 10.3) |
| Percentage rates in the XML | As published — e.g. `0.522`, `35.00`, `90.00` | Technical Annex code tables |
| Internal calculation | Mercans carries **full precision** internally and rounds only at the artefact boundary | Design rule |

**Design rule.** Round once, at the point of output, under that output's own regime. Never round an
intermediate result and then feed it into the next step, and never re-round an already-rounded figure
into a different regime.

*Legal basis: Decree 780 of 2016 art. 3.2.1.5 as substituted by Decree 1990 of 2016 art. 1; Tax Code
(Decree-Law 624 of 1989) art. 577; Resolution DIAN 000013 of 2021 and its Technical Annex §1.1.1.1;
Resolution DIAN 000227 of 2025 art. 1.3.7.1.1.*
