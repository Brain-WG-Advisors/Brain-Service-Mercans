# Egypt (EG) — Statutory Report Specifications

**Tax year 2026 · Private-sector employers · Currency EGP**

---

# 0. Inventory

| ID | Report | Authority | Frequency | Legal deadline | Trigger | Layout confidence |
|---|---|---|---|---|---|---|
| **EG-RPT-01** | **نموذج الاحتساب الشهري** — Monthly Calculation Form | ETA (payroll system) | **Per disbursement**, or aggregated monthly | Tax remitted **within the first 15 days of the month following** the month of deduction (Law 91/2005 art. 14) | Any disbursement of salary or the like | **92%** — field-level, from SDK v5 |
| **EG-RPT-02** | **نموذج السداد الشهري** — Monthly Payment Form | ETA (Core Taxation) | Monthly | Same 15-day window | **Auto-filed by integration** on submission of EG-RPT-01 | 70% — DERIVED |
| **EG-RPT-03** | **نموذج 2 مرتبات** — Form 2 Salaries | ETA (Core Taxation) | Monthly | Same 15-day window | **Auto-filed by integration** where the form contains tax treatment 2 | 60% — DERIVED |
| **EG-RPT-04** | **نموذج 4 مرتبات** — Form 4 Salaries (quarterly return) | ETA (Core Taxation) | **Quarterly** | **January, April, July and October** of each year (Law 91/2005 art. 15(1)) | Being a person responsible for withholding under art. 14 | 65% — DERIVED |
| **EG-RPT-05** | **نموذج 9 تسويات** — Form 9 Settlements (annual settlement) | ETA (Core Taxation) | **Annual** | Calendar year Jan–Dec, regardless of the company's financial year | Close of the tax year | 70% — DERIVED |
| **EG-RPT-06** | **مساهمة صندوق الشهداء** — Martyrs' Fund contribution claim | ETA (Core Taxation) | Per disbursement | With the salary-tax claim | Basic disbursements at a **subject** entity | 75% |
| **EG-RPT-07** | **نموذج /21خ** — Proportional salary stamp-duty return | ETA | Per the stamp-duty rules | Per the stamp-duty rules | **Government and public-business-sector disbursements only** | 45% — DERIVED, **below floor** |
| **EG-RPT-08** | **بيان مفردات الأجر** — Wage-components statement to the employee | Employer → employee | Each payment | With each wage payment | Labour Law art. 115 | See `06-payslip.md` |
| **EG-RPT-09** | **كشف الضريبة المحجوزة** — Withheld-tax statement to the employee | Employer → employee | **On request** | On request | Law 91/2005 art. 15(2) | **95%** — the statute lists the content |
| **EG-RPT-10** | **نموذج 1 تأمينات** — Form 1, insured-person subscription | NOSI | Per hire | **Within two weeks of joining** | New hire | 80% |
| **EG-RPT-11** | **استمارة 2 تأمينات** — Form 2, wage and contribution data | NOSI | Monthly / on change | Contributions due at the **start of the following month**, additional amount waived if paid **within 15 days** (Law 148/2019 art. 121) | Wage data and changes | 70% — DERIVED |
| **EG-RPT-12** | **نموذج 6 تأمينات** — end-of-service notification | NOSI | Per leaver | On leaving | Termination | 55% — DERIVED, **below floor** |
| **EG-RPT-13** | **سجلات العاملين والأجور** — Worker and wage registers | Ministry of Labour | Continuous | Available at inspection | Labour Law art. 105 | 85% |
| **EG-RPT-14** | **Training and Rehabilitation Fund levy** | Fund (Ministry of Labour) | **Annual** | Not established — see §8 | 30+ workers | 40% — **below floor** |

Reports **not** applicable to a private-sector employer: EG-RPT-06 and EG-RPT-07 (public / public-business-sector scope — see `01-ccg.md` §8).

---

# 1. EG-RPT-01 — Monthly Calculation Form (نموذج الاحتساب الشهري)

**The centre of gravity of Egyptian payroll compliance.** Everything else in the ETA stack is generated from it.

## 1.1 Identity

| Item | Value |
|---|---|
| Authority | ETA — منظومة توحيد أسس ومعايير احتساب ضريبة الأجور والمرتبات |
| Legal basis | Law 206/2020 (Unified Tax Procedures) and its executive regulations; substantive computation under Law 91/2005 arts. 8, 9, 10, 13, 14, 72 bis |
| Frequency | **One form per disbursement (صرفية)**, or one form aggregating the month's disbursements — the employer's choice (FAQ general Q9, Q10, salary-items Q19) |
| Deadline | The **tax** must be remitted within the **first fifteen days of the month following** the month of deduction. Filing after the 15th triggers recomputation, a claim and delay fee (FAQ technical Q23) |
| Amendment | **None exists.** Corrections go into the next month's form, an additional disbursement, or the annual settlement's processing sheet |
| Nil filing | Supported — `PAYROLL_TYPE = 3` (*بدون موظفين*, "no employees") |

## 1.2 Disbursement types (نوع الصرفية)

| Code | Type | Rule |
|---|---|---|
| **1** | **صرفية أساسية** — basic disbursement | **Any number** per company, **provided no employee already has a basic disbursement filed for the period** (FAQ additional Q68). Where the entity is subject to stamp duty, the proportional stamp is computed on basic disbursements |
| **2** | **صرفية إضافية** — additional disbursement | **Any number, without restriction.** Used for bonuses, corrections, catch-ups, and for paying a leaver's December entitlements after year end (FAQ salary-items Q14). **A tax treatment must be selected for an additional disbursement too** (FAQ additional Q63). **الأجر الشامل may not be entered on an additional disbursement** (SDK validation) |
| **3** | **بدون موظفين** — no employees | Nil filing |

Where there is more than one disbursement in the same month, the tax is **recomputed** taking the new disbursement together with those already filed, and the employer is claimed for the difference (FAQ technical Q24).

## 1.3 Screen structure

Two sections (FAQ technical Q97):

**Section 1 — بيانات نموذج الاحتساب الشهري.** Select the disbursement type from the five types; shows a summary of the data entered in the salary-data section. Also carries the **head-office insurance number** (`الرقم التأميني للمركز الرئيسي للمنشأة`) — entered manually the first time and pre-filled thereafter with the ability to amend; **branch insurance numbers are never entered** (FAQ technical Q98).

**Section 2 — بيانات الرواتب**, in six sub-screens:

| # | Sub-screen | Content | Manual entry? |
|---|---|---|---|
| 1 | **البيانات الأساسية** | Employee code, national ID or passport, tax treatment, work period in the month | Yes |
| 2 | **التأمينات** | Insurance status, comprehensive-wage data, universal-health-insurance status, private insurance funds | Yes |
| 3 | **الاستحقاقات** | All taxable entitlement elements | Yes |
| 4 | **الإعفاءات** | Carried automatically from the insurance and entitlement screens | **No — no manual entry accepted in any field** |
| 5 | **ضريبة المرتبات** | The computation results after pressing احتساب | **No** |
| 6 | **إضافات وخصومات** | Additions of non-taxable amounts and deductions of non-exempt amounts | Yes — **neither affects the tax computation** |

## 1.4 Field-level specification

Transcribed from **ETA Taxpayer SDK v5**. Types are the SDK's own (`CHAR n`, `DEC 15.2`, `DATS8`, `INT13`). "R" = إجباري (mandatory), "O" = اختياري (optional), "C" = conditional.

### 1.4.1 Envelope

| Field | Type | Req | Meaning |
|---|---|---|---|
| `USER_NAME` | CHAR 12 | R | أسم المستخدم |
| `PASSWORD` | RAW 8 | R | كلمة السر |
| `FORM_TYPE` | CHAR 4 | R | نوع النموذج (sample `U001`) |
| `PERIOD` | CHAR 4 | R | الفترة (sample `1122`) |
| `PAYROLL_TYPE` | CHAR 1 | R | نوع الصرفية — 1 / 2 / 3 |
| `EMPLOYEES` | TABLE | R | جدول بيانات الموظفين |

### 1.4.2 Employee identification and insurance (`EI*`)

| Field | Type | Req | Label | Rule |
|---|---|---|---|---|
| `EI010` | CHAR 10 | R | كود الموظف | Internal employee number at the employer; **letters and digits accepted** |
| `EI015` | CHAR 100 | R | اسم الموظف | **Four name parts for an Egyptian**, respecting compound names; **two parts for a foreigner**. Arabic and Latin letters accepted; **no symbols**. **Duplicate names are rejected** |
| `EI020` | CHAR 2 | R | الجنسية / الحالة التعاقدية | `01` مصري بعقد · `02` أجنبي بعقد · `03` مصري بدون عقد · `04` أجنبي بدون عقد. (The FAQ also describes a *عمالة يومية* selection; where the value implies Egyptian, **national ID becomes mandatory**, and where it implies foreign, **passport number becomes mandatory** — FAQ technical Q35) |
| `EI025` | CHAR 14 | C | الرقم القومي | **14 digits, numeric only**, for Egyptians. **Duplicate national IDs are rejected** |
| `EI026` | CHAR 14 | C | رقم جواز السفر | For foreigners; **letters and digits in Arabic or Latin script** |
| — | — | — | رقم جواز السفر الجديد | Where the passport changes during the tax period, the **old** number goes in the passport field and the **new** number in this field (FAQ technical Q36) |
| `EI030` | CHAR 20 | R | رقم التليفون | The employee's **personal mobile**, digits only. **Load-bearing:** it is the activation channel for the employee's Employee-Portal account |
| `EI035` | CHAR 2 | R | حالة تصريح العمل لغير المصريين | `01` ساري · `02` قيد الاستخراج / التجديد · `03` لا يوجد. **Must be removed where the employee is Egyptian** (SDK validation message) |
| `EI040` | CHAR 100 | C | رقم تصريح العمل | Valid work-permit number for foreign employees; letters and digits |
| `EI045` | CHAR 100 | R | الوظيفة | Job title; letters and digits |
| `EI050` | CHAR 2 | C | الدرجة الوظيفية | **Government entities only**: `01` third grade and below · `02` first or second grade · `03` senior and excellent grade (above first). **Must be removed for private-sector employees** (SDK validation message) |
| `EI055` | CHAR 100 | R | اسم الجهة / الفرع | Employer or branch name |
| `EI060` | CHAR 2 | R | **المعاملة الضريبية** | `01`–`08`; see `01-ccg.md` §6.5. The SDK notes `06` and `07` are **not available** through the integration channel in that version |
| `EI065` | CHAR 9 | C | رقم التسجيل الضريبي لجهة العمل الأصلية | **Mandatory for tax treatment 2 only.** **9 digits, numeric only.** **May not be replaced by the establishment's insurance number** (FAQ technical Q37, Q47) |
| `EI070` | CHAR 2 | R | **الحالة التأمينية** | 28 values — see §1.5. Selected per NOSI's contribution-calculation bases |
| `EI075` | CHAR 8 | C | الرقم التأميني | Employee's social-insurance number, digits only. **Mandatory for any insured employee, whatever the tax treatment** (FAQ salary-items Q44) |
| `EI080` | DATS8 | C | تاريخ الالتحاق بالتأمينات | **Format `yyyymmdd`** (FAQ insurance Q3). The **social-insurance subscription date per Form 1 or Form 2 – تأمينات** — *not* the employment start date (FAQ additional Q65) |
| `EI085` | DEC 15 | O | قسط مدة سابقة / أنظمة تأمينية بديلة | Instalment for a purchased prior period, secondment or notional period. Where the worker purchases a prior insurance period, enter the instalment **paid during the month** (FAQ insurance Q4) |
| `EI090` | DATS8 | R | تاريخ نهاية الخدمة | Employment end date at the company |
| `EI095` | DATS8 | O | تاريخ انتهاء الاشتراك في التأمينات الاجتماعية | Insurance end date |
| `EI100` | DEC 15.2 | O | **الأجر الشامل** | The comprehensive wage **as recorded on استمارة 2 تأمينات** (FAQ salary-items Q13, insurance Q1). **May not be entered on an additional disbursement** |
| `EI105` | DEC 15.2 | O | **بدلات غير خاضعة تأمينيا** | Allowances exempt from social insurance — i.e. **الأجر الشامل − أجر الاشتراك** (FAQ insurance Q2) |
| `EI115` | CHAR 2 | R | **حالة التأمين الصحي الشامل** | `01` خاضع · `02` غير خاضع |
| `EI120` | INT13 | C | عدد الزوجات غير العاملات | **Mandatory when `EI115` = 01; rejected when 02.** Dropdown 01–04 |
| `EI125` | INT13 | C | عدد المعالين | **Mandatory when `EI115` = 01; rejected when 02.** Digits only |
| `EI130` | INT13 | R | **مدة العمل** | Days worked in the month. **Maximum 30 per month, 360 per year.** A warning is displayed on entering zero. Entering fewer than 30 **prorates the personal exemption** |

### 1.4.3 Entitlements (`DTE*`) — all `DEC 15.2`, all optional individually

| Field | Label | Applies to |
|---|---|---|
| `DTE105` | الأجر الوظيفي | Civil-Service-Law entities |
| `DTE110` | الأجر المكمل | Civil-Service-Law entities |
| `DTE115` | العلاوة الدورية المقررة بقانون الخدمة المدنية | Civil-Service-Law entities |
| `DTE120` | علاوة تشجيعية | Non-Civil-Service entities |
| `DTE125` | علاوة الحافز العلمي | Non-Civil-Service entities |
| `DTE130` | علاوة استثنائية | **Both** Civil-Service and non-Civil-Service entities |
| `DTE135` | حافز تعويضي | Non-Civil-Service entities |
| `DTE140` | علاوة مضمومة | Non-Civil-Service entities |
| `DTE145` | الراتب الأساسي المجرد | Non-Civil-Service entities — the **الأساس المجرد** stamp-duty base |
| `DTE150` | علاوة مضمومة (SDK duplicate row) | Non-Civil-Service entities |
| `DTE155` | **المرتب الأساسي** | **Private-sector companies** |
| `DTE160` | علاوة اجتماعية / إضافية | Non-Civil-Service entities |
| `DTE165` | المكافآت والحوافز / الأجور الإضافية / المنح | All |
| `DTE170` | إعانة غلاء المعيشة | Non-Civil-Service entities |
| `DTE175` | **العلاوات الخاصة معفاة** | Special allowances up to 2013 **approved in tax examinations** |
| `DTE180` | **العلاوات الخاصة الخاضعة** | Special allowances up to 2013 **not approved**, plus all from 2014 |
| `DTE185` | عمولات | All |
| `DTE190` | رواتب ومكافآت رؤساء مجالس الإدارة | All |
| `DTE195` | نصيب العامل من الأرباح | All — exempt limb only |
| `DTE200` | مقابل الخدمة | All |
| `DTE205` | البقشيش | All |
| `DTE210` | **المزايا: القروض والسلفيات** | Valued at 7% or the shortfall from 7%; see `02-wtc.md` §6 |
| `DTE215` | **المزايا: التأمين على الحياة (حصة صاحب العمل)** | Employer-borne premiums paid in the year |
| `DTE220` | **المزايا: أسهم الشركة داخل مصر أو خارجها** | Fair value at acquisition minus the price charged; benefit deferred until transfer restrictions lapse |
| `DTE225` | **مزايا أخرى** / المقابل النقدي لرصيد الأجازات أثناء الخدمة | See note below |
| `DTE230` | **مكافأة نهاية الخدمة الخاضعة** | Taxable end-of-service gratuity |
| `DTE235` | **اضافات و بدلات اخرى — خاضعة** | The allowance catch-all |
| `DTE240` | **ما تحملته المنشأة من التأمينات الاجتماعية** | Employer-borne employee SI share — taxable cash benefit |
| `DTE245` | **ما تحملته المنشأة من ضريبة المرتبات** | Employer-borne salary tax — taxable cash benefit |
| `DTE250` | مبالغ خاضعة منصرفة بصورة سنوية | Annual-frequency taxable amounts |
| `DTE255` | مبالغ خاضعة منصرفة بصورة ربع سنوية | Quarterly-frequency taxable amounts |
| `DTE260` | مبالغ منصرفة بقوانين خاصة (الجزء المعفي منها) | Exempt portion of special-law payments |
| `DTE265` | مبالغ خاضعة منصرفة بصورة نصف سنوية | Half-yearly-frequency taxable amounts |
| `DTE270` | مبالغ خاضعة منصرفة بصورة سنوية | See note below |
| `DTE275` · `DTE280` · `DTE285` · `DTE290` | Further entitlement rows in the SDK sample payload | See note below |

> **CONFIDENCE NOTE on the `DTE` mapping.** The SDK's field-dictionary tables are laid out as multi-column RTL tables and, in several rows, the code column and the label column drift apart under text extraction — most visibly around `DTE140`/`DTE150`, `DTE175`/`DTE180`, and the block `DTE250`–`DTE290`, where the SDK sample payload carries more populated codes than the dictionary rows I could align with certainty. **The set of labels is complete and correct — it matches ETA FAQ technical Q38's "24 entitlement elements in three classifications" exactly. The code-to-label pairing for the rows flagged above should be re-verified against a live sheet download or a fresh SDK release before it is wired into an integration.** Confidence on the flagged rows: **~75%**; on the unflagged rows: **~93%**. See `07-qa-report.md` §3.

The 24 elements per ETA FAQ technical Q38, which is the authoritative enumeration:

- **مفردات المرتب — taxable (13):** المرتب الأساسي · مكافآت وحوافز · العلاوات غير المعفاة من 2014 · عمولات · مرتبات ومكافآت رؤساء مجالس الإدارة والمديرين في شركات الأموال مقابل عملهم الإداري · مقابل الأجازات الخاضع · مكافآت نهاية الخدمة الخاضعة · مكافآت خاضعة تصرف بصورة ربع سنوية · مكافآت خاضعة تصرف بصورة نصف سنوية · مكافآت خاضعة تصرف بصورة سنوية · بدلات أخرى خاضعة · البقشيش · مقابل الخدمة
- **مفردات معفاة — exempt (3), which carry directly to the exemptions block:** العلاوات المعفاة حتى 2013 والمعتمدة ضريبيًا · حصص العاملين في الأرباح طبقًا للمادة 41 من قانون 159 لسنة 1981 · المبالغ المعفاة بقوانين خاصة — الجزء المعفي
- **المزايا النقدية — cash benefits (2):** ما تحملته المنشأة من حصة العامل في التأمينات الاجتماعية · ما تحملته المنشأة من ضريبة المرتبات
- **المزايا العينية — in-kind benefits (6):** مزايا السيارات · مزايا المحمول · مزايا القروض والسلفيات · مزايا وثائق التأمين على الحياة ما يتحمله صاحب العمل · مزايا الأسهم داخل وخارج مصر التي تمنح بقيمة تقل عن القيمة السوقية بعد زوال أي قيد للملكية · أي مزايا أخرى تُصرف للعامل دون أن تكون عوضًا عن نفقات فعلية

### 1.4.4 Deductions and exemptions (`DAE*`) — all `DEC 15.2`, optional

| Field | Label | Rule |
|---|---|---|
| `DAE425` | العلاوة الاجتماعية / الإضافية لجهات حكومية وقطاع عام وغير خاضع للخدمة المدنية | Mirrors entitlement item code **(36)**; per art. 13(1) note in the SDK |
| `DAE450` | اشتراكات العاملين في صناديق التأمين المنشأة طبقًا لقانون **54 لسنة 1975** | Manual entry; **inside** the capped basket |
| `DAE455` | أقساط التأمين على حياة الممول لمصلحته ولمصلحة زوجته وأولاده القصر | **Inside** the capped basket. The FAQ discusses this field explicitly as *"بند اقساط التأمين على الحياة (dae 455)"* (technical Q41) |
| `DAE460` | أقساط التأمين الصحي | **Inside** the capped basket |
| `DAE465` | أي قسط تأمين لاستحقاق المعاش | **Inside** the capped basket |
| — | أقساط التأمين في صناديق التأمين طبقًا لقانون **155 لسنة 2024** | Dedicated field; **fully exempt, outside the capped basket** (FAQ technical Q43) |

**The cap.** `DAE450` + `DAE455` + `DAE460` + `DAE465` are limited to **the lower of 15% of net income or EGP 10,000 per year**, and in all cases to the amount actually paid; the excess is **taxable** (FAQ technical Q41, Q42).

### 1.4.5 Amounts not affecting the tax (`NAD*`) — all `DEC 15.2`, optional

| Field | Label |
|---|---|
| `NAD615` | اضافات: قيمة السلفة / قروض |
| `NAD620` | اضافات: قيمة مكافأة نهاية الخدمة **غير الخاضعة** |
| `NAD625` | اضافات: قيمة رصيد الأجازات **غير الخاضعة** |
| `NAD630` | إضافات أخرى |
| `NAD635` | استقطاعات: نفقة |
| `NAD640` | استقطاعات: قيمة قسط السلفة / القرض |
| `NAD645` | استقطاعات: اشتراكات نقابات / أندية |
| `NAD650` | استقطاعات: جزاءات |
| `NAD655` | استقطاعات: قيمة قسط بوليصة التأمين على الحياة |
| `NAD660` | استقطاعات أخرى |
| `NAD665` | خصم اجمالي قيمة المزايا العينية / المبالغ المحولة بالفعل |

> **CONFIDENCE NOTE on the `NAD` mapping.** As with the `DTE` block, the code-to-label alignment in the SDK's RTL table drifts by one row in places (the *نفقة* / *قسط السلفة* pair in particular). **The label set is complete; verify the pairing against a live sheet.** Confidence: **~78%**.

These fields are **individually optional but functionally mandatory**, because the Employee-Portal payslip is built from them: FAQ technical Q7 — the payslip *"ستعبر عن جميع بيانات المرتبات بما في ذلك المبالغ الغير مؤثره على الضريبة مثل الجزاءات والغياب والنفقة والسلفة"*.

## 1.5 The insurance-status mapper (`EI070`) — 28 values

Reproduced in full in `05-data-dictionary.md` §3.2. Summary of the arithmetic-relevant values in `01-ccg.md` §4.6.

## 1.6 Validation rules extracted from the SDK

| Rule | Message (Arabic, as extracted) |
|---|---|
| Insurance data may not be entered where the employee is not insured | لا يمكن ادخال بيانات التأمينات في حالة غير مؤمن عليه للمسلسل رقم … |
| Tax computed for prior periods must be entered for tax treatment 3 | برجاء ادخال الضريبة المحتسبة عن الفترات السابقة للمعاملة 3 للمسلسل رقم … |
| Universal-health-insurance status must be checked against the insurance status | برجاء التأكد من حالة التأمين الصحي الشامل مع الحالة التأمينية للمسلسل رقم … |
| Comprehensive wage and non-insurable allowances must be checked | برجاء التأكد من الأجر الشامل والبدلات غير خاضعة تأمينيًا للمسلسل رقم … |
| The insurance status is not permitted for this tax registration number | لا يمكن اختيار الحالة التأمينية لرقم التسجيل المستخدم للمسلسل رقم … |
| A current-period form cannot be filed while a prior period is unfiled | لا يمكن تقديم نموذج الاحتساب لفترة حالية دون تقديم الفترة السابقة |
| Disbursement type must be entered on the form-data screen | برجاء ادخال نوع الصرفية في صفحة بيانات نموذج الأحتساب |
| **The comprehensive wage may not be entered with an additional disbursement** | لا يمكن ادخال الاجر الشامل مع الصرفية الإضافية للمسلسل رقم … |
| **A basic disbursement already exists for this employee for the period** | تم ادخال صرفية اساسية من قبل للموظف عن الفترة للمسلسل رقم … |
| The tax treatment is not permitted for your tax registration number | لا يمكن اختيار المعاملة الضريبية للرقم التسجيل الخاص بك للمسلسل رقم … |
| The insurance number may not be entered for an uninsured status | لا يمكن ادخال الرقم التأميني … حالة غير مؤمن عليه مع المعاملة الضريبية المختارة |
| **Remove the work permit — the employee is Egyptian** | برجاء ازالة تصريح العمل لان الموظف مصري للمسلسل رقم … |
| **Spouse/dependant counts may not be entered for a non-UHI status** | لا يمكن ادخال عدد الزوجات او عدد المعالين لحالة ت.ص.شامل للمسلسل رقم … |
| **The employee number may not repeat** | رقم الموظف لايجب ان يتكرر للمسلسل رقم … |
| **Remove the job grade** (private-sector employee) | برجاء حذف الدرجة الوظيفية للمسلسل رقم … |
| A general warning shows the payment due date | يرجي العلم ان تاريخ استحقاق السداد هو … |

**Two structural rules with consequences.** (a) *"لا يمكن تقديم نموذج الاحتساب لفترة حالية دون تقديم الفترة السابقة"* — **periods must be filed in order**; a missed month blocks the current one. (b) A **duplicate national ID or duplicate name is rejected outright** (FAQ additional Q70) — so employee master data must be de-duplicated *before* the file is built, not after rejection.

## 1.7 Outputs

| Output | Where |
|---|---|
| Computed tax for the period | On screen, instantly on pressing احتساب (FAQ additional Q72: *"تتم عملية احتساب الضريبة لحظي"*) |
| Excel extract of the form **plus computed tax and insurance** | Download from the top-left of the calculation screen (FAQ technical Q48) |
| **نموذج السداد الشهري** and **نموذج 2 مرتبات** filed on Core Taxation | Automatic on submission |
| **Claims (مطالبات)** — one for salary tax, one for the martyrs'-fund contribution | Issued on Core Taxation |
| **قسيمة الراتب** for each employee | Employee Portal |
| Dashboards for senior management | Total Egyptian and foreign headcount, total tax due, tax paid, and **tax paid on time versus late** (FAQ general Q2) |

---

# 2. EG-RPT-02 — Monthly Payment Form (نموذج السداد الشهري)

| Item | Value |
|---|---|
| Authority | ETA — Core Taxation |
| Legal basis | Law 91/2005 art. 14 |
| Frequency | Monthly |
| Deadline | Remittance **within the first fifteen days of the month following** the month of deduction |
| Trigger | Submission of EG-RPT-01 |
| Filing route | **Automatic by integration.** Manual filing on Core Taxation is **blocked** once the payroll-system account is activated (FAQ general Q13) |
| Content | The salary tax computed by the payroll system for the period, presented *"بذات الحقول المتاحة بنموذج السداد الموجود علي منظومة الكور سيستم"* — the same fields as the existing Core monthly payment form (FAQ salary-items Q42) |
| Partial payment | Activates the delay-fee computation under Law 91/2005 art. 110, per Core's rules (FAQ technical Q19) |
| Payment application order | Administrative and judicial costs → **delay fee** → taxes withheld at source → taxes due (Law 91/2005 arts. 111 and following) |

> **Layout: DERIVED, 70%.** No official form image was retrievable. The field set is asserted by ETA to equal the pre-existing Core monthly payment form; I could not obtain that form.

---

# 3. EG-RPT-03 — Form 2 Salaries (نموذج 2 مرتبات)

| Item | Value |
|---|---|
| Authority | ETA — Core Taxation |
| Frequency | Monthly |
| Deadline | Same 15-day window |
| Trigger | Presence of **tax treatment 2** rows (non-original-employer payments) on the monthly calculation form. FAQ salary-items Q85: choosing treatment 2 plus the original employer's tax registration number causes the form to *"يقوم النموذج بأعداد نموذج (2) مرتبات وتقديمة علي منظومة الأعمال الضريبية الرئيسية"* |
| Filing route | Automatic on submission of EG-RPT-01 |
| Interaction | Where one monthly calculation form mixes treatments 1 and 2, the monthly payment form and Form 2 Salaries are filed **separately**, and **separate claims** issue — which is why a period can show a claim amount that does not match the form total (FAQ technical Q101) |
| Notification duty | The non-original employer must **notify the original employer** of the workers, their total entitlements for the period, and the tax withheld (Law 30/2023, art. 72 bis) |

> **Layout: DERIVED, 60%.**

---

# 4. EG-RPT-04 — Form 4 Salaries, the quarterly return (نموذج 4 مرتبات)

| Item | Value |
|---|---|
| Authority | ETA — Core Taxation |
| Legal basis | **Law 91/2005 art. 15(1)**: the person responsible for withholding and remitting under art. 14 must *"تقديم إقرار ربع سنوي إلى مأمورية الضرائب المختصة في يناير وابريل ويوليو وأكتوبر من كل عام على النموذج المعد لذلك"* |
| Frequency | **Quarterly** |
| Deadline | **January, April, July and October** of each year |
| Related deadline | **Law 91/2005 art. 86**: entities obliged to apply the withholding rules must pay the withheld amounts **by the end of April, July, October and January** each year, and must keep records available for ETA examination containing, for each tax period, **(a) the amounts paid and the person receiving them, and (b) the tax withheld from those amounts**, with a copy of the registers sent to ETA |
| Content | **Law 206/2020 executive regulations art. 31**, as ETA construes it (FAQ, laws Q2): an obligation to enter, within Form 4 Salaries, **the number of workers, the value of monthly salaries, the value of tax paid, and any changes to headcount (increases or decreases), for the preceding three months** |
| Filing route | The system **auto-populates** Form 4 Salaries from the monthly calculation forms filed for the quarter, and the taxpayer submits it from the payroll system (FAQ, laws Q2; salary-items Q16) |
| Amendment | **None.** FAQ technical Q102: *"لا يمكن تقديم اقرار ربع سنوي معدل"* |
| Interaction with the monthly obligation | The quarterly obligation **does not displace** the monthly one. FAQ, laws Q2 is explicit: *"فهذا الإلتزام لا يؤثر علي الإلتزام الشهري بتقديم نموذج الاحتساب وسداد الضريبة"*. And FAQ additional Q73: monthly returns are **mandatory** — the monthly tax can only be paid through the monthly calculation form, and **the quarterly form cannot be produced except from the submitted monthly forms** |
| Simplified-regime relief | Entities under Law 6/2025 are **exempt from filing Form 4 Salaries** from the quarter following entry into the regime (FAQ technical Q117) |
| Guide | `UPTCP_Quarterly_Payroll_Form_Submission_Guide_v.1.2.pdf`, **November 2025** |

> **Layout: DERIVED, 65%.** The four content items are ETA's own statement of what art. 31 of the Law 206/2020 regulations requires; I could not obtain an image or schema of the form itself.

---

# 5. EG-RPT-05 — Form 9 Settlements, the annual settlement (نموذج 9 تسويات)

| Item | Value |
|---|---|
| Authority | ETA — Core Taxation |
| Frequency | **Annual** |
| Period | **1 January to 31 December**, *"بغض النظر عن السنة المالية للشركة"* — regardless of the company's own financial year (FAQ technical Q120) |
| **Replaces** | **Forms 6, 7 and 8 Settlements.** FAQ additional Q75: Form 9 is filed *"كنموذج بديل للنماذج أرقام (6، 7، 8) تسويات"*. There is **one** settlement form for companies on the payroll system (FAQ salary-items Q9) |
| Filing route | Prepared **automatically** by integration from the monthly calculation forms; the system auto-fills, the taxpayer verifies and submits; filing onto Core is automatic (FAQ general Q18) |
| Prerequisite | **All monthly calculation forms for the period must have been submitted** — the settlement integrates with them, so it cannot be filed until they are all in (FAQ technical Q118) |
| Content vs monthly form | FAQ salary-items Q10: the monthly form declares **the monthly wages disbursed and the monthly tax withheld**; the annual settlement declares **the actual annual wages disbursed and the actual annual salary tax** for each worker |
| Shape | Same shape as the monthly calculation form, **plus** total annual wages and total annual tax due for the actual period (FAQ general Q8) |
| **Correction mechanism** | **شيت المعالجة** — the processing sheet. All values entered there affect the settlement figures **negatively only** — *"تؤثر بالسالب علي الرقم المتواجد ببيانات التسوية"* — **except** Law 155/2024 insurance premiums, which affect positively, **and only for the 2025 tax period** (FAQ technical Q115). The sheet can reduce work period, entitlement or exemption data entered in error during the year (FAQ technical Q20) |
| Wrong-company correction | Where a disbursement was filed against the wrong company, file it correctly on the right company and, in the wrong company's annual settlement, enter the disbursement's data in the processing sheet — basic data plus all entitlement and exemption elements — and on pressing احتساب **that employee's settlement data becomes zero** (FAQ technical Q94) |
| Multiple tax treatments | Where an employee had more than one tax treatment during the year, **each treatment is called into the settlement as a separate row**, and cumulative net income, the annual pool and the tax are computed **per treatment** (FAQ technical Q105) |
| Tax paid outside the system | The system **recalls** salary tax paid outside the system for periods before the mandation decision, on a dedicated screen, and the company **distributes it across employees**. **The settlement cannot be filed until that distribution is done and totals match the recalled figure**, formatted as *"أرقام – خليتين عشريتين"* — numeric, two decimal places (FAQ technical Q74, Q113) |
| Amendment | **None.** FAQ technical Q103: *"لا يمكن تقديم اقرار معدل للتسوية الضريبيه السنويه"*. And Q104: **no disbursement of any kind may be filed after the annual settlement has been submitted for that period** |
| Resigned-employee differences | Where a resigned employee has tax differences, they appear in the annual settlement **as a credit balance due to the employee**; the system computes the actual tax on the employee's actual salary; **but the employee-level tax difference is settled internally in the company's accounts** (FAQ technical Q11) |
| Guides | `uptcp_annual_payroll_claculation_form_guide_v_2.2_1.pdf` (**2025 settlement**, Jan 2026); `UPTCP_annual_Payroll_Claculation_Form_Guide_v.2.2.pdf` (2024 settlement) |

> **Layout: DERIVED, 70%.** The mechanics are richly documented in ETA's guides and FAQ; the **field layout of Form 9** itself was not obtainable as an image or schema.

---

# 6. EG-RPT-06 — Martyrs' Fund contribution

| Item | Value |
|---|---|
| Computation | **EGP 5 per each EGP 10,000** (0.05%), on **basic disbursements only** (*الصرفيات الأساسية فقط*), for **all labour except Egyptian daily labour** (FAQ additional Q110) |
| Claim | A **separate claim** on Core Taxation, alongside the salary-tax claim (FAQ salary-items Q12) |
| **Scope** | **Government agencies, public-sector entities and their companies, and public-business-sector companies and their affiliates.** **Not private-sector employers** |
| Legal basis | Law 16/2018 establishing the Fund, as amended in 2021 to widen its resources; ETA circular **119/2021** addresses the Fund |

> **Confidence 75%.** Rate and mechanics from ETA's March 2026 FAQ (solid). The **public-sector restriction** rests on reporting of the amending law rather than the gazette article, which I could not retrieve. Verify per entity in a mixed group. See `07-qa-report.md` §3.

---

# 7. EG-RPT-07 — Proportional salary stamp duty (نموذج /21خ)

| Item | Value |
|---|---|
| Legal basis | **Article 79 of the Stamp Duty Law, Law 111/1980** and its amendments, as construed by **State Council Fatwa 475/2/37 of 16 July 1994** |
| **Scope** | **Government disbursements** and **public-business-sector companies**. FAQ additional Q66: *"الدمغة النسبية هي الدمغة المستحقة علي الصرفيات الحكومية"*. FAQ technical Q88 extends it to *"شركات قطاع الأعمال العام"* and notes the system provides a basic disbursement **without** proportional stamp and an additional disbursement **without** proportional stamp for entities outside scope |
| Base | **الأساس المجرد** — *"المرتب الأساسي بدون العلاوات الخاصة المضمومة عليه"*, the bare basic salary without merged special allowances; concerns entities **not** subject to the Civil Service Law. Field `DTE145` |
| Computation | Performed by the ETA payroll system where a basic or additional disbursement is selected for entities whose disbursements are subject to stamp duty |
| **Filing** | The company remains obliged to **file and pay the proportional salary stamp-duty return on Form /21خ** separately (FAQ additional Q66) |
| Interaction that survives for everyone | **Stamp tax legally due is a deduction from the salary-tax base** — Executive Regs art. 12(8); listed in the exemption block as *"الدمغة المقررة بالمادة 79 من القانون 111 لسنة 1980"* (FAQ technical Q92) |

> **Layout and rate schedule: DERIVED, 45% — BELOW FLOOR.** I did **not** obtain the text of Article 79, the proportional-stamp rate schedule, the Form /21خ layout, or its filing deadline. For a private-sector-only engagement this is out of scope. **Do not** attempt to compute salary stamp duty from this pack. See `07-qa-report.md` §3.

---

# 8. EG-RPT-14 — Training and Rehabilitation Fund levy

| Item | Value |
|---|---|
| Legal basis | **Labour Law 14/2025 art. 21(1)** |
| Who | Public-sector, public-business-sector and **private-sector** establishments with **30 or more workers** |
| Amount | **0.25% of the minimum insurance wage**, **floor EGP 10 and cap EGP 30 per worker** |
| Frequency | **Annual** — *"تتحملها وتلتزم المنشأة بسدادها سنويا"* |
| Exemption | Full exemption where the establishment trains its own workers per its requirements or approved internal regulations; the competent Minister issues the rules and conditions |
| Governance | The Prime Minister issues the decree constituting the Fund's board, its governorate branches, its statute, **its resource-collection system** and the accounting system to be followed |

> **BELOW FLOOR — 40%.** The **rate, base, floor, cap, threshold, annual frequency and exemption route are verbatim statute (high confidence)**. What is **missing** is everything operational: the **collection form, the payment channel, the due date within the year, and which of the two readings of "0.25% of the minimum insurance wage" the Fund applies**. Because the floor/cap binds under both readings, the amount is safely within **EGP 10–30 per worker per year**; model **EGP 10** for 2026 and disclose. See `01-ccg.md` §8.1.

---

# 9. Deadline calendar

| Date | Obligation |
|---|---|
| **With / before each disbursement** | File the monthly calculation form (EG-RPT-01). ETA recommends filing **before** paying |
| **By the 15th of each month** | Remit the salary tax withheld from the **previous** month's payments (Law 91/2005 art. 14). Filing after the 15th → recomputation, claim, and **delay fee** |
| **By the 15th of each month (in practice)** | Pay social insurance. Due at the **start** of the following month (Law 148/2019 art. 121); the **additional amount is waived if paid within 15 days** of the due date |
| **Monthly** | Remit universal-health-insurance contributions to UHIA where applicable |
| **January, April, July, October** | File Form 4 Salaries, the quarterly return (Law 91/2005 art. 15(1)) |
| **End of January, April, July, October** | Pay amounts withheld, under the withholding rules (Law 91/2005 art. 86) |
| **After the close of the calendar year** | File Form 9 Settlements, the annual settlement — **after** all monthly calculation forms for the year are in |
| **Annually** | Pay the Training and Rehabilitation Fund levy (date not established — see §8) |
| **Within 2 weeks of a hire** | File NOSI Form 1 (subscription request) |
| **Within 7 days of the worker's claim** | Pay all final entitlements on termination (Labour Law art. 108(4)) |
| **Within 7 days of the event** | Notify the competent administrative authority of the reasons for overtime working in extraordinary or exceptional circumstances (Labour Law art. 121) |
| **1 January each year** | New minimum and maximum social-insurance contribution wage takes effect |

> **BELOW-FLOOR ITEM — the exact statutory due date within the filing month.** Law 91/2005 art. 15(1) names the **months** (January, April, July, October) for the quarterly return but not a day of the month; art. 86 gives an **end-of-month** date for payment by withholding entities. I could **not** find an executive-regulation provision fixing the day for Form 4 Salaries. Confidence on "the month": 96%. Confidence on "the day": **~55%**. The safe operational rule is **end of the filing month**, aligning with art. 86. See `07-qa-report.md` §4.

---

# 10. Penalties

| Charge | Rate | Basis |
|---|---|---|
| **Delay fee — tax** (مقابل التأخير) | **CBE credit-and-discount rate announced on the 1 January preceding the due date, plus 2%**; fractions of a month and of a pound disregarded; objection or appeal does **not** suspend it | Law 91/2005 art. 110 |
| **Cap on the delay fee / additional tax** | **May not exceed 100% of the tax principal** | Art. 45 bis of Law 206/2020, inserted by **Law 7/2025** |
| Interest on late ETA refunds | The same rate **minus 2%**, running from 45 days after the refund request | Law 91/2005 art. 112 |
| **Additional amount — social insurance** | **Average Treasury bill/bond issuance rate for the month preceding the month in which payment fell due, plus 2%**, monthly. **Waived if paid within 15 days of the due date** | Law 148/2019 art. 121 |
| NOSI collection fee | **1‰** of amounts collected, **minimum EGP 10, maximum EGP 100** | Law 148/2019 art. 121 |
| NOSI objection fee | **EGP 100**, and the objection is inadmissible without it | Law 148/2019 art. 120 |
| Settlement of tax offences | The Minister or their delegate may settle offences that do not concern tax dues, against compensation of **not less than half the minimum fine and not more than twice it** | Art. 75 bis of Law 206/2020, inserted by Law 7/2025 |
| Minimum-wage non-compliance | Penalties under the Labour Law for failing to pay the prescribed minimum wage; Ministry inspection verifies implementation of National Wages Council decisions | Labour Law arts. 104, 105 |

**Examination is not abolished by the system.** FAQ technical Q21 and salary-items Q17, Q18: the payroll system will not prevent examination of employers' files, but examination becomes simpler and faster, reduces examination differences, and shortens the gap between filing and examination. Examination is conducted **on the annual settlement** (FAQ technical Q108). And treatment-8 manual computations are **verified at examination** (FAQ technical Q62).
