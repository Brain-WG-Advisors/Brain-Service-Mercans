# Egypt (EG) — Mandatory Payslip Content

**Tax year 2026 · Private-sector employers · Language: Arabic**

---

# 1. The headline finding — Egypt has a payslip *obligation* but no statutory *content list*

**Labour Law 14/2025, Article 115**, in full:

> **مادة (115):**
> لا تبرأ ذمة صاحب العمل من الأجر إلا إذا وقع العامل بما يفيد استلام الأجر فى السجل المعد لذلك، أو فى كشوف الأجور، أو إتمام تحويل أجره ومستحقاته إلى حسابه بأحد البنوك، **ويلتزم صاحب العمل بإعطاء العامل بيانًا بمفردات أجره.**

> *The employer is not discharged of the wage unless the worker signs to acknowledge receipt of the wage in the register kept for that purpose, or on the wage schedules, or the transfer of the wage and entitlements to the worker's bank account is completed; **and the employer is obliged to give the worker a statement of the components of their wage.***

That final clause is **the whole of the Egyptian payslip mandate**. It requires a statement of the **components** of the wage (مفردات الأجر). **It does not enumerate what those components must be, in what order, with what labels, or in what format.**

**This is a grep-tested finding, not an inference.** Across the full gazette text of Law 14/2025 (*الجريدة الرسمية، العدد 18 (تابع)، 3 مايو 2025*, 110 pages):

| Term searched | Hits |
|---|---|
| **مفردات** (components) | **1** — Article 115 only |
| **قسيمة** (payslip) | **0** |
| **كشف الأجر** (wage statement) | **0** |
| **بيان الأجر** (wage statement) | **0** |
| **إيصال** (receipt, in the wage sense) | **0** |
| **استمارة الأجر** (wage form) | **0** |

There is no second provision, no enumerated list, and no cross-reference to a schedule. Egypt therefore behaves like Denmark and the Philippines in this pipeline: **a real obligation with no prescribed content**.

**Do not fabricate a mandatory-content list.** Anything presented as "the eleven items an Egyptian payslip must show" is somebody's template, not the law.

---

# 2. What *is* prescribed — three separate, narrower obligations

## 2.1 The tax statement — Law 91/2005, Article 15(2)

The person responsible for withholding and remitting the tax under Article 14 must:

> **إعطاء العامل بناءً على طلبه كشفًا يبين فيه اسمه ثلاثيًا ومبلغ ونوع الدخل وقيمة الضريبة المحجوزة.**

> *Give the worker, **upon their request**, a statement showing:*
> 1. **the worker's three-part name** (اسمه ثلاثيًا)
> 2. **the amount and type of the income** (مبلغ ونوع الدخل)
> 3. **the value of the tax withheld** (قيمة الضريبة المحجوزة)

This is the **only** statutory content list attached to a payroll document in Egypt, and note its two limits: it is **on request**, not automatic, and it covers **three items**, not a full payslip. The Executive Regulations set out the rules and procedures for implementing the article.

**Design consequence:** an engine must be able to produce this three-item statement on demand, independently of the monthly payslip, with the name rendered in **three parts**.

## 2.2 The contract, which pre-commits the pay structure — Labour Law Article 89

The employment contract must be **in writing, in Arabic, in four copies** (employer, worker, the competent social-insurance office, the competent administrative authority), and must contain **at least**:

1. the **start date** of the contract;
2. the **employer's name and the address of the workplace**;
3. the **worker's name, qualification, profession or trade, insurance number, place of residence** and what is needed to establish their identity;
4. the **nature and type of the work** that is the subject of the contract;
5. **the agreed wage, the method and date of its payment, and all other agreed cash and in-kind benefits.**

Where the worker is a foreigner who does not know Arabic the contract may be drawn in **Arabic and the worker's language**, and **on a difference of interpretation the Arabic text governs**. Where there is no written contract, **both** worker and employer may prove the employment relationship, its duration and all rights arising from it **by any means of proof**. The employer must give the worker a **receipt** for any papers and certificates deposited with them.

Item 5 is the practical anchor for payslip design: **the contract must already itemise the wage, the payment method and date, and every cash and in-kind benefit** — so the payslip's line structure should mirror the contract's.

## 2.3 The ETA Employee-Portal payslip — an authority-issued document

Since the ETA payroll system became universal (final mandation **15 December 2024**), each employee has a second, **state-issued** payslip, produced from what the employer filed.

| Item | Position |
|---|---|
| Where | **بوابة الموظف** — the ETA Employee Portal |
| Who registers | **The employee personally**, using **national ID + mobile number** as filed by the employer, with a confirmation code sent to the mobile. The employer's payroll-system administrator has **no** access to it |
| What it shows | ETA FAQ, additional Q74: a payslip for the tax period *"متضمنة جميع استحقاقاته النقدية والعينية وغير المؤثر على الضريبة وكذلك جميع الاستقطاعات التي تمت على أجره"* — **all cash and in-kind entitlements, the amounts that do not affect the tax, and all deductions made from the wage** |
| Guide | `UPTCP-Employee-Portal-Guide-V2.0.pdf` — *دليل الموظف لاستخراج قسيمة الراتب الشهري الخاصة به* |
| If the employee does not register | **No consequence for the employer** (FAQ salary-items Q22) |

**This is the single most important payslip-design fact in Egypt**, and it inverts the usual analysis:

> The employee's official payslip is generated **by the tax authority from the employer's filing**. ETA FAQ salary-items Q50 states it directly: *"لن يكون هناك أخطاء بال Pay Slip والذي تعد بياناته انعكاسًا لما قامت الشركة بإدراجه"* — there will be no errors on the payslip, whose data is **a reflection of what the company entered**.

Two consequences follow:

1. **Anything the employer omits from the monthly calculation form is absent from the employee's official payslip.** The `NAD*` block — loans, alimony, penalties, absence, union subscriptions, other deductions — is *technically optional* on the form and *functionally mandatory* for payslip completeness. ETA FAQ technical Q7 confirms the intent: items that enter the annual settlement but do not appear on the company payslip **will** be visible to the employee, and the payslip *"ستعبر عن جميع بيانات المرتبات بما في ذلك المبالغ الغير مؤثره على الضريبة مثل الجزاءات والغياب والنفقة والسلفة"* — will express all payroll data **including amounts not affecting the tax, such as penalties, absence, alimony and advances**.
2. **The employer payslip and the ETA payslip must reconcile line for line.** Any divergence is visible to the employee and, at examination, to ETA. Build the employer payslip **from the same field set** that populates the monthly calculation form.

---

# 3. Recommended payslip content for Egypt

Because the Labour Law prescribes no list, the defensible design is: **the Article 15(2) statutory minimum, plus every field that feeds the ETA monthly calculation form, plus what Article 89 already obliges the contract to itemise.** That set is reproduced below. Items marked **[STATUTORY]** are required by an identified provision; items marked **[ETA]** are required for reconciliation with the authority-issued payslip; the rest are professional practice.

## 3.1 Header

| Line | Source |
|---|---|
| Employer name and workplace address | **[STATUTORY]** Labour Law art. 89(2) |
| Employer tax registration number (9 digits) | **[ETA]** |
| Employer head-office insurance number | **[ETA]** |
| Pay period, and the **disbursement type** (basic / additional) | **[ETA]** — the type determines the form, the claim and the stamp-duty treatment |
| Payment date and method (cash at the workplace / bank transfer) | **[STATUTORY]** Labour Law arts. 89(5), 108 |
| Currency: **EGP** | |

## 3.2 Employee block

| Line | Source |
|---|---|
| Employee name — **three parts on the tax statement, four parts on the ETA form** for an Egyptian; two parts for a foreigner | **[STATUTORY]** Law 91/2005 art. 15(2); **[ETA]** `EI015` |
| National ID (14 digits) **or** passport number | **[ETA]** `EI025` / `EI026` |
| **Insurance number** | **[STATUTORY]** Labour Law art. 89(3); **[ETA]** `EI075` |
| Employee code | **[ETA]** `EI010` |
| Job title / profession | **[STATUTORY]** art. 89(3)–(4) |
| Start date of the contract | **[STATUTORY]** art. 89(1) |
| **Work period in the month, in days** | **[ETA]** `EI130` — the annualisation divisor and the personal-exemption prorater; showing it lets the employee verify the tax |
| **Tax treatment code (1–8)** | **[ETA]** `EI060` — it determines the whole algorithm; an employee on treatment 2 sees a flat 10% and needs to know why |
| **Insurance status code** | **[ETA]** `EI070` |
| **Universal-health-insurance status**, and the counts of non-working spouses and dependants where subject | **[ETA]** `EI115`, `EI120`, `EI125` — these drive a deduction that can be 7% rather than 1% |

## 3.3 Entitlements — itemised, never bundled

| Line | Source |
|---|---|
| Basic salary | **[STATUTORY]** art. 89(5); **[ETA]** `DTE155` |
| Each allowance, **separately named**, with the insurable ones distinguishable from the non-insurable ones | **[STATUTORY]** art. 89(5) — *"وسائر المزايا النقدية والعينية المتفق عليها"*; **[ETA]** |
| Bonuses, incentives and grants | **[ETA]** `DTE165` |
| **Overtime**, split into **daytime (+35%)** and **night (+70%)**, and **rest-day working** shown separately | **[STATUTORY]** Labour Law art. 121 — the employee cannot verify a premium that is bundled |
| Commissions, service charge, tips | **[ETA]** `DTE185`, `DTE200`, `DTE205` |
| Quarterly / half-yearly / annual taxable amounts, shown as such | **[ETA]** `DTE255`, `DTE265`, `DTE250` |
| Employees' profit share, split into the exempt portion and any excess | **[ETA]** `DTE195` + `DTE235` |
| Cash for leave balance during service | **[ETA]** `DTE225` |
| **Cash benefits**: employer-borne employee SI share; employer-borne salary tax | **[ETA]** `DTE240`, `DTE245` — both are taxable to the employee and must be visible |
| **In-kind benefits at their statutory value**, itemised: car (20%), mobile (20%), loans (7%), life policies, shares, other — each **clearly marked as a tax-base item that does not increase take-home pay** | **[ETA]** — see §4 |
| **Gross cash entitlements** subtotal, and **taxable base** subtotal, shown as **two different numbers** | Practice — they differ by the in-kind benefits and the exempt items |

## 3.4 Exemptions and deductions

| Line | Source |
|---|---|
| **Social insurance — employee share (11%)**, with the **capped contribution wage** shown | **[ETA]** — showing the capped base explains why the deduction is flat at EGP 1,837.00 |
| **Universal health insurance — employee share**, broken into self 1% / spouse 3% each / dependants 1% each where applicable | **[ETA]** |
| Private insurance fund contributions — Law 54/1975 and, separately, Law 155/2024 | **[ETA]** `DAE450` and the Law 155/2024 field — the two have different caps |
| Life / health / pension premiums, and **the amount actually allowed after the 15% or EGP 10,000 cap** | **[ETA]** `DAE455`, `DAE460`, `DAE465` |
| **Personal exemption applied this period** (20,000 ÷ 12, prorated; **+50%** where treatment 4 or 7) | **[ETA]** |
| **Salary tax for the period** | **[STATUTORY]** Law 91/2005 art. 15(2) |
| Loan / advance instalment — **capped at 10% of the wage, interest-free** | **[STATUTORY]** Labour Law art. 113; **[ETA]** `NAD*` |
| Alimony / maintenance | **[ETA]** `NAD*` |
| Disciplinary penalties, absence | **[ETA]** `NAD*` |
| Union / club subscriptions, insurance-policy instalments, other deductions | **[ETA]** `NAD*` |
| **Reversal of total in-kind benefit value**, so the arithmetic to net pay is visible | **[ETA]** |
| **Net pay** | |

## 3.5 Footer — recommended

| Line | Why |
|---|---|
| Year-to-date cumulative net income, annual pool, annual tax, tax already charged | The Egyptian tax is **cumulative and annualised**; without these an employee cannot reconcile a month in which the tax jumps. See `01-ccg.md` §2.2 |
| The **column of the Article 8 matrix** currently applying | Explains a step change that looks like an error |
| **Employer contributions** — SI 18.75%, UHI 4% (min EGP 50) | Transparency; not statutorily required |
| Leave balance, and the **three-year settlement date** | Labour Law art. 125 requires the balance or its cash equivalent to be settled **at least every three years** |
| The **periodic-allowance anniversary date** | Labour Law art. 12: the increase is due one year from appointment or from the previous increase — a **per-employee** date |
| Reference to the ETA Employee Portal | So the employee can obtain the authority-issued payslip |

---

# 4. Formatting and presentation conventions

| Convention | Position |
|---|---|
| **Language** | **Arabic.** The Labour Law itself is Arabic; the employment contract must be in Arabic (art. 89) and the Arabic text prevails on any interpretive conflict; collective agreements must be in Arabic with the Arabic text prevailing (art. 176). **A bilingual Arabic/English payslip is normal practice and is not prohibited** — ETA accepts employee data in either language (FAQ integration Q9, Q10) and requires names in **both** Arabic and Latin letters (FAQ salary-items Q38). **But the Arabic is the operative version.** A monolingual English payslip is defensible only where the employee is a foreigner who does not know Arabic, and even then Article 89's logic points to Arabic-plus-worker's-language |
| **Direction** | **Right-to-left.** Arabic script; amount columns conventionally on the left of an RTL layout |
| **Currency** | **EGP (جنيه مصري)**, ISO 4217 `EGP` / 818 |
| **Decimals** | **Two.** ETA's own payload returns monetary results as strings with two decimals (`"58600.00"`), and the annual-settlement distribution screen requires values *"أرقام – خليتين عشريتين"* — numeric, two decimal cells |
| **Rounding** | **Do not round payslip lines.** The two statutory rounding rules operate elsewhere: the **annual net-income pool is rounded DOWN to the nearest EGP 10** before applying the Article 8 matrix (Law 91/2005 art. 8), and **fractions of a month and of a pound are disregarded** in the delay-fee computation (art. 110). Neither is a payslip-presentation rule |
| **Numerals** | Both Arabic-Indic (٠١٢٣٤٥٦٧٨٩) and Western digits are in official use — Egyptian gazette text uses Arabic-Indic; ETA systems use Western. Either is acceptable on a payslip; **be consistent** |
| **In-kind benefits** | Must be shown **at their statutory value** (20% / 20% / 7% / premiums / share spread), and must be **visibly excluded from the net-pay arithmetic**. ETA FAQ technical Q55: the 20% *"ليست استحقاقا فعليا وعليه لاتظهر في معادلة صافي الأجر النهائي"* — it is not an actual entitlement and does not appear in the final net-wage formula |
| **Exempt collective benefits** | Do **not** appear — they are not entered on the ETA form at all, and showing them on the payslip creates an unreconcilable difference |
| **Bundling** | Avoid. Article 89(5) obliges the contract to itemise the wage and **all** cash and in-kind benefits, and Article 115 speaks of the **مفردات** — the *components* — of the wage. A single "allowances" line defeats the word |

---

# 5. Discharge of the wage — what the payslip does and does not do

**A payslip is not a discharge.** Article 115 makes the employer discharged of the wage **only** by one of three things:

1. the worker's **signature acknowledging receipt** in the register kept for the purpose; **or**
2. the worker's signature **on the wage schedules**; **or**
3. **completion of the transfer** of the wage and entitlements to the worker's bank account.

The wage statement is a **separate, additional** obligation in the same article. An employer who issues perfect payslips but holds no signed register and no completed transfer has **not** discharged the wage, and **bears the burden** on that point.

Related rules that a payslip design should respect:

- **Article 116**: wages, bonuses and other legal entitlements of **child workers** are delivered to them **directly**, and that delivery discharges the employer.
- **Article 108**: payment is on a **working day, at the workplace, in legal tender or into the worker's bank account**; monthly-paid workers **at least once a month**; on termination, **within not more than seven days** of the worker's claim.
- **Article 114**: any assignment of wage within the permitted 25% / 50% band is valid **only with the worker's written consent** — so a deduction line that reflects an assignment must be backed by that consent.
- **Article 108 final paragraph**: **withholding the wage or part of it without legal basis is prohibited**, and the worker must not receive less than the minimum wage.

---

# 6. Confidence

| Item | Confidence | Basis |
|---|---|---|
| **Article 115 is the payslip mandate, and there is no statutory content list** | **97%** | Gazette text read in full and **grep-tested**: *مفردات* appears once; *قسيمة*, *كشف الأجر*, *بيان الأجر*, *إيصال* appear zero times in the wage sense |
| Article 15(2) three-item tax statement, on request | **96%** | Law 91/2005 text verbatim |
| Article 89 contract-content list | **96%** | Gazette text verbatim |
| Arabic is the operative language; Arabic prevails on conflict | **95%** | Arts. 89 and 176 |
| Discharge mechanics (register / schedules / completed transfer) | **96%** | Art. 115 verbatim |
| ETA Employee-Portal payslip content and mechanics | **93%** | ETA FAQ additional Q74, general Q10, salary-items Q22, Q50, technical Q7; Employee-Portal guide exists but I read its title and role rather than its screens |
| **Whether the Labour Law's implementing regulations add a content list** | **50%** ⚠ | **BELOW FLOOR.** Law 14/2025 delegates a great deal to ministerial decisions. I did **not** obtain the implementing decisions issued after 1 September 2025, and one of them **could** prescribe payslip content. The statute itself does not, and the statute is what I verified. **Re-check the Ministry of Labour's issuances before treating "no content list" as final.** See `07-qa-report.md` §3 |
| Two-decimal convention | **85%** | Inferred from ETA's own payload format and the settlement screen's stated format, not from a presentation rule in any statute |
