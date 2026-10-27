# Egypt (EG) — Wage Type Catalogue (WTC)

**Tax year 2026 · Currency EGP (E£) — ISO 4217 alpha `EGP`, numeric `818` · Private-sector employers**

---

# 0. How to read this catalogue

Every wage type below carries five treatments:

| Column | Meaning |
|---|---|
| **ETA field** | The **real** field code on the ETA monthly calculation form / integration payload (ETA Taxpayer SDK v5). Where a field code exists, it is authoritative — this is where the amount must physically go, and putting it elsewhere changes the tax |
| **Tax** | Subject to salary tax (ضريبة المرتبات وما فى حكمها) under Law 91/2005 art. 9 — **Yes / No / Exempt** |
| **SI** | Part of the social-insurance **contribution wage** (أجر الاشتراك) under Law 148/2019 art. 1(8) — **Yes / No** |
| **UHI** | Part of the universal-health-insurance contribution base under Law 2/2018 — follows the SI contribution wage |
| **Net pay** | Whether the element flows into cash net pay, or is a tax-base-only adjustment |

**The ISO currency code is `EGP`** (numeric 818), confirmed against the Central Bank of Egypt and used throughout ETA and NOSI filings. There is no second currency and no minor-unit rounding convention in the statute beyond the two rules in `01-ccg.md` §6.6.

**The three-way split that governs everything.** The ETA monthly calculation form divides the payroll into three blocks and the block decides the treatment:

1. **بنود الاستحقاقات — entitlements** (`DTE*`): amounts in the salary-tax base. 24 elements in three classifications (ETA FAQ, technical Q38):
   - **مفردات المرتب** — salary components: **13 taxable** elements + **3 exempt** elements (the exempt three carry straight into the exemptions block);
   - **المزايا النقدية** — cash benefits: **2** elements (employer-borne employee SI share; employer-borne salary tax);
   - **المزايا العينية** — in-kind benefits: **6** elements (cars; mobiles; loans and advances; life policies borne by the employer; shares inside or outside Egypt granted below market value after any ownership restriction lapses; any other benefit paid to the worker that is not compensation for actual expenses).
2. **الإعفاءات — exemptions** (`DAE*` plus system-carried values): **no manual entry is accepted in this block** for the carried fields — it is populated by carry-over from the insurance and entitlement screens (ETA FAQ Q97).
3. **مبالغ غير مؤثرة على حساب الضريبة — amounts not affecting the tax** (`NAD*`): additions and deductions that appear on the payslip but have **no effect whatsoever** on the tax computation.

**The cardinal rule for in-kind benefits.** They belong in their own `DTE` field and **nowhere else**, they enter the tax base at their prescribed value, and they **never** appear in the net-pay formula (ETA FAQ Q55). An engine that nets a car benefit out of take-home pay is wrong; an engine that puts the car benefit into "other allowances" is also wrong, because the value entered must be the **20% benefit**, not the underlying expense.

**The cardinal rule for exempt collective benefits.** Meals, collective transport, health care, work tools and clothing, and employer-provided work housing are **not entered at all** — not as entitlement, not as exemption (ETA FAQ Q4, Q56, Q59, Q95).

---

# 1. Basic pay

| Code | Wage type | ETA field | Tax | SI | UHI | Net pay | Formula / basis |
|---|---|---|---|---|---|---|---|
| `EG-1000` | **المرتب الأساسي** — Basic salary (private sector) | `DTE155` | Yes | **Yes** | Yes | Yes | Contractual monthly basic. ETA FAQ salary-items Q49: *"لا يتضمن الأجر الأساسي بجهات القطاع الخاص علي العلاوات المنضمة"* — the private-sector basic wage **does not** include merged allowances. Labour Law art. 1(4): الأجر الأساسي is the wage stated in the contract plus any increments arising on it |
| `EG-1005` | **الراتب الأساسي المجرد** — Bare basic salary | `DTE145` | Yes | Yes | Yes | Yes | Basic salary **without** the special allowances merged into it. Used as the *الأساس المجرد* base for proportional salary stamp duty in entities not subject to the Civil Service Law (ETA FAQ Q66). For private employers outside stamp-duty scope this is informational |
| `EG-1010` | **الأجر الوظيفي** — Job wage | `DTE105` | Yes | Yes | Yes | Yes | Civil-Service-Law entities only. Listed for completeness; not used by private employers |
| `EG-1011` | **الأجر المكمل** — Complementary wage | `DTE110` | Yes | Yes | Yes | Yes | Civil-Service-Law entities only |
| `EG-1020` | **مقابل الخدمة** — Service charge | `DTE200` | Yes | Yes | Yes | Yes | Hospitality/service sectors |
| `EG-1021` | **البقشيش** — Tips / tronc (الوهبة) | `DTE205` | Yes | **Conditional** | Conditional | Yes | Part of the SI contribution wage **only** where all three tests in Law 148/2019 art. 1(8)(6) are met: (a) custom is to pay it to establishment workers as a **pre-set percentage** of amounts due from customers; (b) there is a **common fund** in the establishment collecting it for distribution; (c) there are **agreed rules** between employer and workers governing distribution. Fail any test → taxable but outside the SI base |
| `EG-1030` | **رواتب ومكافآت رؤساء وأعضاء مجالس الإدارة** — Chairmen / board members' remuneration | `DTE190` | **Yes** | Per status | Per status | Yes | Law 91/2005 art. 9(3) and 9(4): taxable as salary **in return for administrative work** in capital companies. Non-administrative distributions to shareholder directors are **not** salary income — do not route them here |
| `EG-1040` | **الأجر المتغير** — Variable wage (concept) | — | Yes | Yes | Yes | Yes | Labour Law art. 1(4) defines it as the remainder of the wage elements — commission/percentage, allowances, grants, bonuses, allowances for conditions or risks, and the worker's share of profits. A **definitional** container, not a field |

**Wage definition note.** Labour Law 14/2025 art. 1(4) defines *الأجر* as **everything the worker obtains in return for their work, in cash or in kind**, comprising the basic wage plus the variable wage, and expressly enumerating: commission or percentage; allowances (a sum or a percentage of basic pay granted to meet economic, social or technical circumstances, unless merged into basic pay); grants (منح — given over and above the wage where established in individual or collective contracts or the establishment's basic rules, or by custom); bonuses (مكافأة — for excellence, distinction or efficiency); allowances for particular conditions or risks (بدلات); and the worker's share of profits. This is the **labour-law** definition and it is broader than the SI contribution wage — do not use it as the SI base.

---

# 2. Allowances

The decisive Egyptian rule: **a cash allowance is almost always taxable, and its social-insurance treatment depends on which of the four excluded categories in Law 148/2019 art. 1(8)(7) it falls into.**

| Code | Wage type | ETA field | Tax | SI | UHI | Net pay | Basis |
|---|---|---|---|---|---|---|---|
| `EG-2000` | **بدلات أخرى خاضعة** — Other taxable allowances (catch-all) | `DTE235` | Yes | See below | See below | Yes | ETA FAQ salary-items Q43: *"اي نوع من انواع البدلات المنصرفة للعاملين يتم إدراجه ضمن حقل البدلات"* — any kind of allowance disbursed to workers goes in the allowances field |
| `EG-2010` | **بدل الانتقال** — Transport allowance (flat cash) | `DTE235` | **Yes** | **No** | No | Yes | ETA FAQ Q17: the system admits transport allowances disbursed to workers **as taxable allowances**; only *"ما يخص المصروفات لمواجهة تكلفة فعلية"* — amounts meeting an **actual cost** — are excluded and are not entered on the form at all. SI: excluded by art. 1(8)(7)(a) |
| `EG-2011` | **بدل سكن** — Housing allowance (cash) | `DTE235` | Yes | **No** | No | Yes | SI: excluded by art. 1(8)(7)(b) — allowance in lieu of an in-kind benefit. Distinguish sharply from **employer-provided housing on the occasion of the work**, which is an exempt collective in-kind benefit (`EG-7900`) |
| `EG-2012` | **بدل ملبس** — Clothing allowance (cash) | `DTE235` | Yes | **No** | No | Yes | SI: art. 1(8)(7)(b). Distinguish from **work clothing and tools actually provided**, exempt (`EG-7903`) |
| `EG-2013` | **بدل سيارة** — Car allowance (cash) | `DTE235` | Yes | **No** | No | Yes | SI: art. 1(8)(7)(b). Distinguish from the **company car benefit** (`EG-6000`) |
| `EG-2014` | **بدل سفر / بدل حضور جلسات** — Travel / meeting-attendance allowance | `DTE235` | Yes if not a reimbursement | **No** | No | Yes | SI: art. 1(8)(7)(a) |
| `EG-2015` | **بدل التمثيل** — Representation allowance | `DTE235` | Yes | **YES** | Yes | Yes | **The carve-back.** Art. 1(8)(7)(a) excludes job-burden allowances *"ويستثنى من ذلك بدل التمثيل"* — the representation allowance is expressly excluded from the exclusion and **is** part of the contribution wage |
| `EG-2016` | Allowance for time spent outside the original workplace | `DTE235` | Yes | **No** | No | Yes | Art. 1(8)(7)(c) |
| `EG-2017` | Cost-of-living-abroad allowance | `DTE235` | Yes | **No** | No | Yes | Art. 1(8)(7)(d) |
| `EG-2018` | **بدل مشقة** — Hardship / risk allowance | `DTE235` | Yes | **Yes** | Yes | Yes | A بدلات element for conditions/risks. ETA FAQ salary-items Q43 confirms it goes in the allowances field. Not within any of the four SI exclusions → in the contribution wage (art. 1(8)(7) opening words) |
| `EG-2019` | **بدل وجبة** — Meal allowance (cash) | `DTE235` | **Yes** | Yes | Yes | Yes | ETA FAQ salary-items Q89 answers this directly: cash allowances are **subject** to salary tax; only the **meal actually provided** is the exempt collective benefit. A cash meal allowance is taxable |
| `EG-2020` | **بدل أدوية / فواتير علاج** — Medicine / medical-invoice allowance (cash) | `DTE235` | **Yes** | Yes | Yes | Yes | ETA FAQ salary-items Q84: the form admits all cash allowances and in-kind benefits and processes them per the correct income-tax law — **cash allowances are subject** to salary tax. Only **health care actually provided** is exempt (`EG-7902`) |
| `EG-2030` | **إعانة غلاء المعيشة** — Cost-of-living aid | `DTE170` | Yes | **Yes** | Yes | Yes | Art. 1(8)(10) |
| `EG-2031` | **علاوة اجتماعية / إضافية** — Social / additional allowance | `DTE160`; also `DAE425` for the exempt limb | Yes / Exempt limb | **Yes** | Yes | Yes | Art. 1(8)(11)–(12). ETA FAQ Q15: the system **accepts exemption** of social allowances for workers **not addressed by the Civil Service Law**. `DAE425` mirrors entitlement item code (36) into the exemptions block |
| `EG-2032` | **علاوة مضمومة** — Merged allowance | `DTE150` | Yes | Yes | Yes | Yes | Non-Civil-Service entities |
| `EG-2033` | **علاوة استثنائية** — Exceptional allowance | `DTE130` | Yes | Yes | Yes | Yes | Both Civil-Service and non-Civil-Service entities |
| `EG-2034` | **علاوة تشجيعية** — Incentive allowance | `DTE120` | Yes | Yes | Yes | Yes | Non-Civil-Service entities |
| `EG-2035` | **علاوة الحافز العلمي** — Academic-incentive allowance | `DTE125` | Yes | Yes | Yes | Yes | Non-Civil-Service entities |
| `EG-2036` | **العلاوة الدورية المقررة بقانون الخدمة المدنية** | `DTE115` | Yes | Yes | Yes | Yes | Civil-Service entities only |
| `EG-2040` | **العلاوات الخاصة معفاة** — Special allowances, exempt | `DTE175` | **Exempt** | Yes | Yes | Yes | Special allowances **up to 2013** that were **approved in tax examinations**; also presidential-decree special allowances up to 2013, accepted for **both** civil-service and private-sector workers (ETA FAQ Q15). Carries automatically into the exemptions block; appears twice on the Excel sheet by design (FAQ salary-items Q6) |
| `EG-2041` | **العلاوات الخاصة الخاضعة** — Special allowances, taxable | `DTE180` | **Yes** | Yes | Yes | Yes | Special allowances up to 2013 **not** approved in examinations, **plus every special allowance from 2014 onward** |
| `EG-2050` | **العلاوة السنوية الدورية** — Statutory annual periodic increase | Flows into the pay element it increases | Yes | Yes | Yes | Yes | **Labour Law art. 12**: not less than **3% of the insurance wage (الأجر التأميني)**, due one year from appointment or from the previous increase; National Wages Council floor **EGP 250/month**. Compute as `max(3% × insurance wage, 250)`. **Not** 3% of basic pay and **not** the repealed 7% |

---

# 3. Overtime, bonuses and irregular payments

| Code | Wage type | ETA field | Tax | SI | UHI | Net pay | Formula |
|---|---|---|---|---|---|---|---|
| `EG-3000` | **الأجر الإضافي — نهاري** — Overtime, daytime | `DTE165` (المكافآت والحوافز / الأجور الإضافية / المنح) | Yes | **Yes** | Yes | Yes | **hourly rate of the original wage × 1.35** minimum (Labour Law art. 121). SI: art. 1(8)(8) *الأجور الإضافية* |
| `EG-3001` | **الأجر الإضافي — ليلي** — Overtime, night | `DTE165` | Yes | Yes | Yes | Yes | **hourly rate × 1.70** minimum |
| `EG-3002` | **العمل في يوم الراحة** — Rest-day working | `DTE165` | Yes | Yes | Yes | Yes | **An amount equal to the day's pay as compensation**, *and* a substitute rest day in the following week. Both limbs are mandatory |
| `EG-3010` | **المكافآت والحوافز / المنح** — Bonuses, incentives, grants | `DTE165` | Yes | Yes | Yes | Yes | Art. 1(8)(4) incentives; art. 1(8)(13)–(14) collective grants and bonuses |
| `EG-3011` | **التعويض عن الجهود غير العادية** | `DTE165` | Yes | **Yes** | Yes | Yes | Art. 1(8)(9), expressly in the contribution wage |
| `EG-3020` | **عمولات** — Commissions | `DTE185` | Yes | **Yes** | Yes | Yes | Art. 1(8)(5) |
| `EG-3030` | **مبالغ خاضعة منصرفة بصورة ربع سنوية** — Taxable amounts paid quarterly | `DTE255` | Yes | Yes | Yes | Yes | A **dedicated field** exists so the cumulative engine can see the periodicity (ETA FAQ Q49) |
| `EG-3031` | **مبالغ خاضعة منصرفة بصورة نصف سنوية** — paid half-yearly | `DTE265` | Yes | Yes | Yes | Yes | Same |
| `EG-3032` | **مبالغ خاضعة منصرفة بصورة سنوية** — paid annually | `DTE270` | Yes | Yes | Yes | Yes | Same. **Engine note:** these do **not** get special averaging. They enter the period's net income, are annualised at 360/days with everything else, and the cumulative recomputation absorbs the spike over the remaining months. See `01-ccg.md` §2.2 for the worked consequence |
| `EG-3040` | **متجمد الأجور** — Deferred wage arrears | Handled under **tax treatment 8**, entered manually | Yes | Yes | Yes | Yes | Law 91/2005 art. 10 final paragraph: **distributed over the years of accrual**; the revenue base for each year is recomputed and the tax re-settled. The system **freezes** its computation rules for treatment 8 and the employer enters the annual pool and tax **manually**; correctness is verified at examination (ETA FAQ Q34, Q62, Q72) |
| `EG-3050` | **زيادة بأثر رجعي** — Retroactive increase | The field of the element increased | Yes | Yes | Yes | Yes | Entered **in the month of payment** — the taxable event is the disbursement (ETA FAQ Q91). This principle does **not** apply to deferred wage arrears |
| `EG-3060` | **نصيب العامل من الأرباح** — Employee profit share | `DTE195` (exempt limb); excess → `DTE235` | **Exempt within the limit** | Yes | Yes | Yes | Law 91/2005 art. 13(6): exempt **after general-assembly approval**, *"في حدود 100% من مرتبات العاملين"* per the Companies Law (ETA FAQ Q25, Q79). Only the **exempt portion** goes in the profit-share field, which auto-carries to the exemptions block; **the excess must be entered among the other entitlement elements**. ETA exempts the whole amount during the year and tests the 100% limit at the annual settlement. The profit share is also `DTE195`'s label *حصص العاملين في الأرباح طبقا للمادة 41 من قانون 159 لسنة 1981* in the exempt-elements list |
| `EG-3070` | **المقابل النقدي لرصيد الأجازات أثناء الخدمة** — Cash for leave balance during service | `DTE225` | **Yes — wholly in the period** | Yes | Yes | Yes | **The express carve-out.** Law 91/2005 art. 10 spreads lump sums over accrual years *"عدا مقابل الإجازات"*. ETA FAQ Q99(6): *"يدخل المقابل النقدي لرصيد الأجازات المنصرف أثناء الخدمة في وعاء الفترة كاملا بغض النظر عن سنوات هذا الرصيد"* — **the whole amount lands in the period's base regardless of how many years the balance accrued.** Do not spread it |

---

# 4. Termination payments

| Code | Wage type | ETA field | Tax | SI | UHI | Net pay | Basis |
|---|---|---|---|---|---|---|---|
| `EG-4000` | **مكافأة نهاية الخدمة — غير خاضعة** — End-of-service gratuity, not subject | `NAD620` (*إضافات* block — no tax effect) | **Not subject** | No | No | Yes | Law 91/2005 **art. 12(2)**: end-of-service gratuities are **not subject** to the tax. **Condition (ETA FAQ Q96):** the worker's relationship with the employer must have **ended definitively**. Disclosed on the *إضافات وخصومات* screen, which does not affect the computation |
| `EG-4001` | **مكافأة نهاية الخدمة — خاضعة** — End-of-service gratuity, taxable | `DTE230` | **Yes** | Yes | Yes | Yes | **The trap.** If the worker is **re-appointed at the same entity**, the gratuity is taxable and belongs among the entitlement elements (ETA FAQ Q96) |
| `EG-4010` | **مكافأة المادة 154** — Article 154 gratuity | `DTE230` unless art. 12(2) applies | Assess against art. 12(2) | Assess | Assess | Yes | Labour Law art. 154: where the **employer** terminates a fixed-term contract that ran beyond five years, the worker is entitled to a gratuity of **one month's wage per year of service**. Whether it qualifies as an art. 12(2) "end-of-service gratuity" turns on the definitive-end test |
| `EG-4020` | **مقابل مهلة الإخطار** — Pay in lieu of notice | `DTE235` | **Yes** | **Yes** | Yes | Yes | Labour Law art. 164: amount equal to the wage for the notice period or its remainder, **and that period counts as service with the employer continuing to bear the associated burdens** — so social insurance continues to run over it. Treat as wage, not as a termination capital sum |
| `EG-4030` | **تعويض الإنهاء غير المشروع** — Unlawful-termination compensation | Not an art. 9 entitlement | **Assess — see flag** | No | No | Yes | Labour Law art. 165: **not less than two months' wage per year of service**, as compensation for harm |
| `EG-4040` | **المقابل النقدي لرصيد الأجازات عند نهاية الخدمة** | `NAD625` if not subject; `DTE225` if subject | Assess | Assess | Assess | Yes | Labour Law art. 125: on termination before the balance is exhausted the worker is entitled to pay for it. `NAD625` exists precisely for the **non-taxable** leave-balance case |

> **BELOW-FLOOR ITEM — tax treatment of compensation for unlawful termination.** Article 12(2) exempts *"مكافآت نهاية الخدمة"*. Whether **Article 165 damages** (and an ex-gratia settlement) fall inside that phrase or are taxable under Article 9's catch-all — *"أيًا كانت مسميات أو صور أو أسباب هذه المستحقات"* — is **not settled** by any primary source I read in this build, and the ETA payroll system offers no dedicated field for it. Confidence: **~50%**. The conservative position is to treat court-ordered/settlement damages as outside Article 9 (they compensate harm, not work) while treating anything structured as additional remuneration as taxable — and to obtain a ruling for material amounts. See `07-qa-report.md` §3.

---

# 5. Cash benefits (المزايا النقدية)

Two elements, both employer-funded, both **taxable to the employee**:

| Code | Wage type | ETA field | Tax | SI | UHI | Net pay | Basis |
|---|---|---|---|---|---|---|---|
| `EG-5000` | **ما تحملته المنشأة من التأمينات الاجتماعية** — Employer-borne employee SI share | `DTE240` | **Yes** | No | No | **No** | ETA FAQ Q51: where the employer bears the employee's social-insurance share it is added to entitlements **as a benefit** in this field and net income is recomputed |
| `EG-5001` | **ما تحملته المنشأة من ضريبة المرتبات** — Employer-borne salary tax | `DTE245` | **Yes** | No | No | **No** | ETA FAQ Q50, Q51: *"ضريبة المرتبات هي ضريبة شخصيه لا يجوز الاتفاق علي نقل عبئها"* — the salary tax is personal and its burden cannot be transferred by agreement; where the employer bears it the amount is a **taxable cash benefit** |

**Gross-up circularity.** `EG-5001` is inside the base that determines its own amount. A net-of-tax contract therefore requires an **iterative** gross-up, and ETA's own instruction is the iterative one (FAQ salary-items Q21): compute the employee's tax, re-enter that value among the entitlements, recompute. Because Article 8 selects a **column** by the size of the annualised pool (`01-ccg.md` §6.3), a single-pass gross-up can land in the wrong column and understate the liability. **Iterate to convergence.**

Applies equally to seconded foreigners on net packages: ETA FAQ salary-items Q45 — record the wages the worker receives among entitlements **and** record the value of the tax-bearing benefit in its dedicated field.

---

# 6. Benefits in kind (المزايا العينية)

**Valuation is prescribed by Executive Regulations art. 11** (MoF Decree 991/2005, as amended by MoF Decrees 779/2007 and 74/2008). The default for anything not listed is **market value**, or the difference between market value and what the employee was charged (ETA FAQ Q54).

| Code | Wage type | ETA field | Tax | SI | UHI | Net pay | Valuation |
|---|---|---|---|---|---|---|---|
| `EG-6000` | **مزايا السيارات** — Company car at the employee's personal disposal | `DTE175`→ SDK label *المزايا: السيارات* | **Yes** | No | No | **No** | **20% of the cost of fuel, insurance and periodic maintenance** for those cars, whether owned or leased (Regs art. 11(1)). ETA FAQ Q55: the base is *"قيمة المنصرف المثبت بحسابات الشركة"* — the expense actually recorded in the company's accounts; the 20% is added for tax purposes only and **does not appear in the net-pay formula** |
| `EG-6001` | **مزايا المحمول** — Mobile phone | SDK label *المزايا: الهواتف المحمولة* | Yes | No | No | **No** | **20% of the phone-related expenses over the year** (Regs art. 11(2)) |
| `EG-6002` | **مزايا القروض والسلفيات** — Employer loans and advances | `DTE210` | Yes | No | No | **No** | Where the employer grants a loan **exceeding the total the employee received in the preceding six months**, interest-free or at **under 7%**: benefit = **7%**, or the **difference** between the loan rate and 7%. "Loan" includes any form, including amounts paid in advance or appearing in the employer's books charged to the employee's account. **Administrative expenses of obtaining the loan are not deducted from the rate** (Regs art. 11(3); SDK note). Foreign-currency loans: the balance per the company's accounts, converted at the rate announced **on the loan's due date** (FAQ Q21) |
| `EG-6003` | **مزايا وثائق التأمين على الحياة (حصة صاحب العمل)** — Employer-borne life-policy premiums | `DTE215` | Yes | No | No | **No** | **What the employer bears of premiums paid during the year** on the life of the employee, their family or their property (Regs art. 11(4)) |
| `EG-6004` | **مزايا الأسهم داخل وخارج مصر** — Shares granted below fair value | `DTE220` | Yes | No | No | **No** | **Fair value at the date of acquisition minus the value charged to the employee.** **Where restrictions on transfer of ownership exist the benefit does not arise until they lapse** (Regs art. 11(5) as amended by MoF Decree 74/2008). Entered in the **month of release**; tax recomputed with each disbursement entry (FAQ Q107) |
| `EG-6005` | **أي مزايا أخرى** — Any other in-kind benefit | `DTE225` (SDK label *مزايا أخرى*) | Yes | No | No | **No** | Any in-kind benefit disbursed to workers other than those in the law, valued at market value. The gating test remains Regs art. 11: **not** compensation for expenses borne in performing the work, **and** representing a personal benefit |
| `EG-6006` | **بونات وقود / قسائم** — Fuel vouchers and similar, partly recharged | `DTE175`-family car benefit | Yes | No | No | Partly | ETA FAQ Q58 works the arithmetic: where a EGP 100 fuel voucher is issued and 20% is recovered from the employee, *"ال 80% التي تم اثباتها هي وعاء الميزة الذي يستحق عنه نسبة 20% المقررة قانونا"* — **the 80% charged to the company's accounts is the benefit base, and the statutory 20% applies to that**. So the taxable benefit is 20% × 80 = **16**, not 20 and not 100 |
| `EG-6007` | **سلف مقدمة عن الأرباح** — Advances against profits | `DTE210` | Yes | No | No | No | Treated exactly as employer loans and advances — Regs art. 11(3) final paragraph (FAQ salary-items Q40) |

---

# 7. Exempt and non-taxable elements

## 7.1 The exemptions block — carried, not entered

ETA FAQ Q92 enumerates the exemption block as the **sum** of the following fields, and FAQ Q97 confirms the block *"لا يقبل الادخال اليدوي بأي حقل بها"* — accepts no manual entry, being carried from the insurance and entitlement screens:

| Code | Element | ETA field | Basis |
|---|---|---|---|
| `EG-7000` | **أقساط مدد سابقة** — Instalments for prior insurance periods | `EI095` | Law 148/2019 art. 20 purchase of prior periods; the instalment paid in the month |
| `EG-7001` | **حصة العامل في أقساط التأمين الاجتماعي** — Employee SI share | carried from the insurance screen | Law 91/2005 **art. 13(2)** — social-insurance contributions and other amounts deducted under the social-insurance laws **or any alternative systems** substituting for them (Law 64/1980 systems) |
| `EG-7002` | **حصة العامل في أقساط التأمين الصحي الشامل** — Employee UHI share | carried from the insurance screen | Law 2/2018; deducted within the *استقطاعات* items (FAQ salary-items Q20) |
| `EG-7003` | **حصص العاملين في الأرباح** — Employees' profit share, within the statutory limit | `DTE195` | Art. 13(6); 100%-of-salaries limit |
| `EG-7004` | **أقساط التأمين في صناديق التأمين طبقا للقانون 155 لسنة 2024** | dedicated field | **Fully exempt** — final paragraph of **art. 75 of Law 155/2024**; **outside** the 15% / EGP 10,000 basket (FAQ Q43) |
| `EG-7005` | **أقساط التأمين في صناديق التأمين الخاصة طبقا للقانون 54 لسنة 1975** | `DAE450` | Art. 13(3); **inside** the capped basket |
| `EG-7006` | **أقساط التأمين الصحي** — Health-insurance premiums | `DAE460` | Art. 13(4); inside the capped basket |
| `EG-7007` | **أقساط التأمين على حياة الممول لمصلحته ولمصلحة زوجته وأولاده القصر** | `DAE455` | Art. 13(4); inside the capped basket |
| `EG-7008` | **أي قسط تأمين لاستحقاق المعاش** — Any pension-entitlement premium | `DAE465` | Art. 13(4); inside the capped basket |
| `EG-7009` | **الإعفاء الشخصي** — Personal exemption | system-computed | **EGP 20,000 per year** (Law 7/2024, art. 13(1)), applied at **1/12 per month** and **prorated where the work period in the month is under 30 days** (FAQ Q93). **+50%** under tax treatments 4 and 7 (Law 10/2018 art. 23(1)) |
| `EG-7010` | **العلاوات المعفاة حتى 2013** | `DTE175` carried | Special allowances up to 2013 approved in tax examinations |
| `EG-7011` | **المبالغ المعفاة بقوانين خاصة** | dedicated field | Art. 13's opening words preserve exemptions granted by special laws |
| `EG-7012` | **الدمغة المقررة بالمادة 79 من القانون 111 لسنة 1980** | system-computed | Executive Regs art. 12(8): stamp tax legally due is excluded from the tax base |
| `EG-7013` | **مبالغ منصرفة بقوانين خاصة (الجزء المعفي منها)** | `DTE260` | The exempt portion of amounts disbursed under special laws |

**The capped basket.** `EG-7005` + `EG-7006` + `EG-7007` + `EG-7008` together are limited to **the lower of 15% of net income or EGP 10,000 per year, and in all cases to the amount actually paid**; the excess is **taxable** (ETA FAQ Q41, Q42). `EG-7004` (Law 155/2024) is **outside** the cap. See the confidence flag in `01-ccg.md` §6.2 on the amending instrument for the EGP 10,000 figure.

## 7.2 The insurance-wage exemption under tax treatment 5

| Code | Element | Tax | Basis |
|---|---|---|---|
| `EG-7100` | **إعفاء الأجر التأميني — الأمراض المزمنة** | Exempt | Tax treatment **5**: where the worker has a chronic disease under **Health Minister Decree 259/1995** **and is not present at the workplace**, the system **exempts the value of the insurance wage from net income**, per **MoF Decree 285/2023** |

## 7.3 Exempt collective in-kind benefits — enter nowhere

| Code | Element | ETA field | Basis |
|---|---|---|---|
| `EG-7900` | **السكن الذي يتيحه رب العمل للعاملين بمناسبة أدائهم العمل** | **none — do not enter** | Art. 13(5)(e); Regs art. 12(6)(e) |
| `EG-7901` | **النقل الجماعي للعاملين أو ما يقابله من تكلفة** | **none** | Art. 13(5)(b) |
| `EG-7902` | **الرعاية الصحية** | **none** | Art. 13(5)(c) |
| `EG-7903` | **الأدوات والملابس اللازمة لأداء العمل** | **none** | Art. 13(5)(d) |
| `EG-7904` | **الوجبة الغذائية التي تصرف للعاملين** | **none** | Art. 13(5)(a) |

ETA FAQ Q4, Q56, Q59, Q95 all say the same thing from different angles: exempt collective in-kind benefits *"لا تدرج ضمن نموذج الاحتساب الشهري"* — they are **not** included in the monthly calculation form. Also excluded from entry: employer-paid invoices the employee never takes possession of, such as staff meals provided and maintenance of employees' cars (FAQ Q59).

## 7.4 Not subject at all

| Code | Element | Basis |
|---|---|---|
| `EG-7910` | **المعاشات** — Pensions | Law 91/2005 art. 12(1) |
| `EG-7911` | **مكافآت نهاية الخدمة** — End-of-service gratuities (definitive end) | Art. 12(2); see `EG-4000` |
| `EG-7912` | Diplomatic and consular emoluments within official duties | Art. 13(7) — **on a reciprocity basis and within its limits** |

---

# 8. Employee deductions

| Code | Deduction | ETA field | Reduces tax base? | Basis / cap |
|---|---|---|---|---|
| `EG-8000` | **التأمينات الاجتماعية — حصة العامل** | carried | **Yes** — art. 13(2) | **11.00%** of the capped contribution wage. 2026: floor 2,700, cap **16,700** → maximum **EGP 1,837.00/month** |
| `EG-8001` | **التأمين الصحي الشامل — حصة العامل** | carried | **Yes** | **1%** self **+ 3%** per non-working spouse **+ 1%** per dependant, on the contribution wage. Only where flag `EI115` = 01 |
| `EG-8002` | **ضريبة المرتبات** | system-computed | n/a | Article 8 matrix via the Article 10 annualisation engine |
| `EG-8003` | **مساهمة صندوق الشهداء** | system-computed | No | **EGP 5 per EGP 10,000 (0.05%)** of **basic disbursements only**, all labour **except Egyptian daily labour** (ETA FAQ Q110). **Public-sector / public-business-sector payrolls only** — not private employers. Generates its own separate Core claim |
| `EG-8004` | **ضريبة الدمغة النسبية على المرتبات** | system-computed | **Yes** (Regs art. 12(8)) | Art. 79 of Law 111/1980; **government and public-business-sector disbursements only**; filed on **Form 21-خ**. Base = *الأساس المجرد* (`DTE145`) |
| `EG-8010` | **قسط السلفة / القرض** — Loan / advance instalment | `NAD645` | **No** | **Labour Law art. 113: maximum 10% of the wage**, and the employer **may not charge any interest** on such loans. Applies equally to wages paid in advance |
| `EG-8011` | **النفقة** — Alimony / maintenance | `NAD640` | **No** | Labour Law art. 114: attachment cap raised to **50%** for maintenance; maintenance **ranks first** on competition |
| `EG-8012` | **الجزاءات** — Disciplinary penalties | `NAD655` | **No** | Ranks after maintenance and after employer claims for damaged tools or wrongly-paid amounts |
| `EG-8013` | **اشتراكات نقابات / أندية** — Union / club subscriptions | `NAD650` | **No** | |
| `EG-8014` | **قسط بوليصة التأمين على الحياة** — Life-policy instalment | `NAD660` | **No** here | The *deduction* is a non-tax-affecting item; the *exemption* for premiums runs through `DAE455` within the capped basket |
| `EG-8015` | **استقطاعات أخرى** — Other deductions | `NAD665` | **No** | |
| `EG-8016` | **خصم إجمالي قيمة المزايا العينية** — Reversal of total in-kind benefit value | SDK: *خصم اجمالي قيمة المزايا العينية* | **No** | The mechanical counterpart that keeps in-kind benefits out of net pay while leaving them in the tax base |

**The attachment cascade — get the base right.** Labour Law art. 114: deduction, attachment or assignment for **any debt** is limited to **25%** of the wage due, **50%** for maintenance; assignment within the permitted percentage is valid only with the worker's **written** consent; and the percentage is computed **after** deducting income tax on the wage, social-insurance contributions and amounts due under Law 148/2019, and the employer loan within the art. 113 10% limit. Order of priority on competition: (1) maintenance, (2) amounts owed to the employer for tools/equipment the worker damaged or recovery of amounts wrongly paid, (3) penalties imposed on the worker.

---

# 9. Employer-only costs

| Code | Cost | Tax-deductible to employer | Rate / basis |
|---|---|---|---|
| `EG-9000` | **التأمينات الاجتماعية — حصة صاحب العمل** | Yes | **18.75%** of the capped contribution wage. 2026 maximum **EGP 3,131.25/month**. Composed of 12% pension + 3.25% sickness + 1% injury-medical (to the health authority) + 0.5% injury-cash (**risk-rated up to 1%**) + 1% unemployment + 1% Reward System |
| `EG-9001` | **التأمين الصحي الشامل — حصة صاحب العمل** | Yes | **4%** of the contribution wage, **minimum EGP 50 per month**. Only where flag `EI115` = 01 |
| `EG-9002` | **صندوق تمويل التدريب والتأهيل** — Training and Rehabilitation Fund levy | Yes | Labour Law art. 21: **0.25% of the minimum insurance wage**, establishments with **30+ workers**, **floor EGP 10 / cap EGP 30 per worker**, **paid annually**. Full exemption available where the establishment trains its own workers per ministerial rules. Model **EGP 10 per worker per year** for 2026 |
| `EG-9003` | **مقابل التأخير — ضريبة** | No | Law 91/2005 art. 110: **CBE credit-and-discount rate at 1 January preceding + 2%**, fractions of a month and of a pound disregarded; **capped at 100% of the tax principal** by art. 45 bis of Law 206/2020 (inserted by Law 7/2025) |
| `EG-9004` | **المبلغ الإضافي — تأمينات** | No | Law 148/2019 art. 121: **average Treasury bill/bond issuance rate for the preceding month + 2%**, monthly; **waived if paid within 15 days** of the due date. Plus a collection fee of **1‰**, min EGP 10, max EGP 100 |

---

# 10. Sixteen traps, stated as rules

1. **The SI base is a closed list, not "gross minus exemptions".** Build it from Law 148/2019 art. 1(8)'s 16 elements, then subtract nothing else. A cash housing, transport, clothing or car allowance is **out**; a **representation** allowance is **in**.
2. **The tax base and the SI base diverge on exactly those allowances.** They are taxable and non-insurable. Two bases, computed separately.
3. **The SI cap is monthly, not cumulative.** EGP 16,700 tested each month; no year-to-date remaining-room logic.
4. **In-kind benefits never touch net pay.** They enter the tax base at their prescribed value only.
5. **The car and mobile benefit is 20% of the company's expense, not the expense.** And where part is recharged to the employee, 20% applies to the part **charged to the company's accounts** (the EGP 100 voucher / 20% recharge case gives a benefit of **16**).
6. **Exempt collective benefits are entered nowhere at all** — not as entitlement, not as exemption.
7. **A cash allowance in lieu of an exempt collective benefit is taxable.** Meal allowance ≠ meal provided; medicine allowance ≠ health care provided; housing allowance ≠ employer-provided work housing.
8. **Employer-borne tax and employer-borne employee SI are taxable cash benefits**, and the gross-up is **iterative** because Article 8 selects a column by pool size.
9. **Cash for accrued leave paid during service goes wholly into the period's base** — the one express exception to the spreading rule for lump sums.
10. **Deferred wage arrears are spread over accrual years** and require **tax treatment 8** with manual entry of the pool and tax.
11. **End-of-service gratuity is only non-taxable if the relationship ended definitively.** Re-appointment at the same entity makes it taxable.
12. **The periodic annual increase is 3% of the insurance wage with an EGP 250 floor** — not 7%, not 3% of basic pay, and per-employee anniversary.
13. **Overtime is +35% day / +70% night on the hourly rate of the original wage**, and is **inside** the SI contribution wage.
14. **Rest-day work is equal extra pay AND a substitute day** — both limbs.
15. **Employer loans: 0% interest by labour law, 7% imputed benefit by tax law.** Both apply.
16. **The 25%/50% attachment cap is computed after tax, after social insurance and after the 10% employer-loan slice** — not on gross.

---

# 11. Code-set status

The `EG-*` codes in this catalogue are **DERIVED**. No Mercans Global WTC mapping existed for Egypt at the time of this build; the numbering follows the pack's own block structure (1000 basic, 2000 allowances, 3000 variable, 4000 termination, 5000 cash benefits, 6000 in-kind, 7000 exempt, 8000 employee deductions, 9000 employer costs).

**The `ETA field` column is not derived.** Every `DTE*`, `DAE*`, `NAD*` and `EI*` code is transcribed from **ETA Taxpayer SDK v5**, and it is the code that actually matters for filing: the field an amount is placed in determines its tax treatment inside the ETA system, and a misplaced amount cannot be corrected by an amended return, because **no amended return exists** (ETA FAQ salary-items Q31). Where this catalogue shows a `DTE` code against a label the SDK expresses differently, the SDK label is reproduced in the row so the mapping can be re-verified against a current SDK release.
