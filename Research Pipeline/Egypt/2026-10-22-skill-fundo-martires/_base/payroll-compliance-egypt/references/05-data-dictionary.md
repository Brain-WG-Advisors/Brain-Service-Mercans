# Egypt (EG) — Master Data Dictionary

**Tax year 2026 · Private-sector employees only** — civil servants, the public and public-business sectors, military and police, domestic-service workers, employers, the self-employed and self-insured/freelance categories are **out of scope** per the standard Mercans scope filter.

---

# 0. What drives what

Egypt is unusually explicit about which master-data field switches which calculation, because the ETA payroll system's field list *is* the specification. Five fields carry almost all of the risk:

| Field | Switches |
|---|---|
| **المعاملة الضريبية** (`EI060`) | The **entire tax algorithm** — annualisation vs flat 10% vs flat 5% vs frozen manual |
| **الحالة التأمينية** (`EI070`) | The **entire social-insurance rate set** |
| **حالة التأمين الصحي الشامل** (`EI115`) | Whether Law 2/2018 applies **and** whether two other fields become mandatory or forbidden |
| **مدة العمل** (`EI130`) | The **annualisation divisor** and the **proration of the personal exemption** |
| **الجنسية / الحالة التعاقدية** (`EI020`) | Which **identifier** is mandatory, and whether the work-permit fields are required or forbidden |

Get any one of them wrong and the number is wrong — and there is **no amended return** in Egyptian payroll (see `04-reports-spec.md`).

---

# 1. Identification fields

| Field | Arabic | ETA code | Type | Req | Format and validation |
|---|---|---|---|---|---|
| Employee code | كود الموظف | `EI010` | CHAR 10 | **M** | Internal employer number. **Letters and digits.** **Must not repeat within a form** |
| Employee name | اسم الموظف | `EI015` | CHAR 100 | **M** | **Four name parts for an Egyptian**, respecting compound names; **two parts for a foreigner**. Arabic **and** Latin letters accepted — ETA requires names *"بالحروف العربية والإنجليزية"*. **No symbols.** The system **validates the name against nationality**. **Duplicate names are rejected** |
| **National ID** | الرقم القومي | `EI025` | CHAR 14 | **C** | **Exactly 14 digits, numeric only.** Mandatory where nationality/contract status is Egyptian (`01`, `03`) or daily labour. **Duplicates rejected** |
| **Passport number** | رقم جواز السفر | `EI026` | CHAR 14 | **C** | **Letters and digits, Arabic or Latin script.** Mandatory where the status is foreign (`02`, `04`) |
| New passport number | رقم جواز السفر الجديد | — | CHAR | **C** | Where the passport changes **during the tax period**: the **old** number stays in `EI026` and the **new** number goes here |
| Mobile number | رقم التليفون | `EI030` | CHAR 20 | **M** | **The employee's personal mobile, digits only.** Used to activate the employee's ETA **Employee-Portal** account via a confirmation code. Treat as operationally mandatory even where a placeholder would pass validation |
| **Employer tax registration number** | رقم التسجيل الضريبي | — | CHAR 9 | **M** (employer level) | **Exactly 9 digits, numeric only** |
| Original employer's TRN | رقم التسجيل الضريبي لجهة العمل الأصلية | `EI065` | CHAR 9 | **C** | **Mandatory for tax treatment 2 only.** 9 digits. **May not be substituted by the establishment's insurance number** |
| Establishment insurance number | الرقم التأميني للمركز الرئيسي للمنشأة | — | numeric | **M** (employer level) | **Head-office number only** — never a branch number, even where branches have their own. Keyed once, pre-filled thereafter, amendable |
| **Employee insurance number** | الرقم التأميني | `EI075` | CHAR 8 | **C** | Digits only. **Mandatory for any insured employee whatever the tax treatment**; **must not be present** where the insurance status is `21` (uninsured) |
| Bank account / IBAN | — | — | — | **O** for ETA, **operationally M** | Labour Law art. 108 permits payment into the worker's bank account; art. 115 makes completed transfer to that account one of the three ways the employer is discharged of the wage. Egyptian IBAN: **`EG` + 27 characters (29 total)** |

> **Note on the national ID.** The 14-digit Egyptian national ID encodes century, date of birth, governorate of birth and sex, and carries a check digit. **This pack does not specify the checksum algorithm** — I did not obtain an official specification for it. Validate length and numeric composition; do **not** implement a checksum from folklore. Confidence on the structure claim: ~80%; on any specific checksum: not asserted.

---

# 2. Demographic and personal fields

| Field | Arabic | ETA code | Req | Notes |
|---|---|---|---|---|
| Nationality / contract status | الجنسية / الحالة التعاقدية | `EI020` | **M** | See §3.1 |
| Date of birth | تاريخ الميلاد | — | **M** (NOSI) | Not on the ETA form; **required by NOSI** on Form 1 with a digitised birth certificate. **Minimum age 18** for the private-sector, domestic-service and employer's-family categories under Law 148/2019 art. 2 |
| Sex | النوع | — | **M** (NOSI) | Drives maternity, nursing-break and pregnancy-hours entitlements |
| Disability status | من ذوي الاحتياجات الخاصة | via `EI060` = 04 / 07 | **C** | Evidenced by the **بطاقة الخدمات المتكاملة** issued by the Ministry of Social Solidarity. **Also applies where the employee *cares for* a person with a disability** — FAQ salary-items Q47 confirms code 4 covers a carer. Effect: **personal exemption +50%** (Law 10/2018 art. 23(1)). Annual-leave effect: **45 days** (Labour Law art. 124(4)), also for persons of short stature (الأقزام) |
| Chronic-disease status | من أصحاب الأمراض المزمنة | via `EI060` = 05 | **C** | Diseases listed in **Health Minister Decree 259/1995**; **conditional on the employee not being present at the workplace**. Effect: the **insurance wage is exempted from net income** (MoF Decree 285/2023) |
| **Non-working spouses count** | عدد الزوجات غير العاملات | `EI120` | **C** | **Mandatory when `EI115` = 01; rejected when `EI115` = 02.** Dropdown **01–04**. Each adds **3%** to the employee's UHI deduction |
| **Dependants count** | عدد المعالين | `EI125` | **C** | **Mandatory when `EI115` = 01; rejected when `EI115` = 02.** Digits only. Each adds **1%** to the employee's UHI deduction |

**Data-ownership rule.** ETA FAQ, laws Q1: the spouse and dependant data is supplied **by the employee**; the employer makes it available to the system; **responsibility for its accuracy rests on the employee**. And laws Q3: entering it does not conflict with data-confidentiality law, because all of it is provided for in the tax, social-insurance or universal-health-insurance laws, so **employee consent is not required**.

---

# 3. Employment fields and their mappers

## 3.1 Nationality / contract status (`EI020`)

| Code | Value | Consequence |
|---|---|---|
| `01` | **مصري – بعقد** — Egyptian, under contract | National ID mandatory; work-permit fields **must be removed** |
| `02` | **أجنبي – بعقد** — Foreign, under contract | Passport mandatory; work-permit status mandatory |
| `03` | **مصري – بدون عقد** — Egyptian, without contract | National ID mandatory |
| `04` | **أجنبي – بدون عقد** — Foreign, without contract | Passport mandatory; work-permit status mandatory |
| — | **عمالة يومية** — daily labour | Described by ETA FAQ technical Q35 as a fifth nationality/contract-status selection requiring a national ID. **Work period = actual days worked.** Excluded from the martyrs'-fund contribution where Egyptian |

> The SDK dropdown lists four values; ETA FAQ technical Q35 describes **five** *"أنواع من الجنسيات والحالة التعاقدية"* including daily labour. Treat the SDK list as the integration enum and the FAQ as the functional description; verify against a current sheet. Confidence: ~85%.

Note also FAQ integration Q26: for a non-Egyptian employee the nationality entry is a dropdown of **مصري / غير مصري** — so there are two distinct concepts in the system, a nationality flag and a nationality/contract-status code. Model both.

## 3.2 Insurance status (`EI070`) — the 28-value mapper

Selected *"طبقا لأسس حساب الأشتراكات التأمينية لجميع القطاعات بالملف الوارد التأمينات الأجتماعية"* — per NOSI's contribution-calculation bases for all sectors. **This single field carries the whole social-insurance rate set** (ETA FAQ salary-items Q35: the system has been loaded with **all** NOSI contribution-calculation cases).

| Code | Value |
|---|---|
| `01` | مؤمن عليه مع عدم تطبيق نظام التأمين الصحي الشامل — insured, universal health insurance **not** applied |
| `02` | مؤمن عليه مع وجود قرار من الهيئة المعنية بالتأمين الصحي للجهة بالعلاج والرعاية للعاملين — insured, with a health-authority decision for the establishment to provide treatment and care |
| `03` | مؤمن عليه مع وجود قرار من الهيئة القومية للتأمين الاجتماعي بتحمل تعويض الأجر ومصاريف الانتقال — insured, with a NOSI decision that the employer bears wage compensation and transport costs |
| `04` | مؤمن عليه مع وجود قرار بتحمل العلاج والرعاية الطبية وتعويض الأجر ومصاريف الانتقال — insured, both decisions |
| `05` | مؤمن عليه مع عدم خضوع التأمين الصحي — insured, not subject to health insurance |
| `06` | **مؤمن عليه مع تطبيق نظام التأمين الصحي الشامل** — insured, **with universal health insurance applied** |
| `07` | مؤمن عليه في جهة ذات حالة وظيفية خاصة (أعمال صعبة) — special occupational status, **arduous work** |
| `08` | مؤمن عليه في جهة ذات حالة وظيفية خاصة (أعمال خطرة) — special occupational status, **hazardous work** |
| `09` | مؤمن عليه إصابة عمل بأجر — insured, work injury, with pay |
| `10` | مؤمن عليه إصابة عمل بدون أجر — insured, work injury, without pay |
| `11` | مؤمن عليه إصابات عمل وتأمين مرض — insured, work injury and sickness insurance |
| `12` | المؤمن عليها الحاصلة على أجازة رعاية طفل — insured woman on childcare leave |
| `13` | مدة التجنيد — conscription period |
| `14` | مؤمن عليه مدد الاستدعاء والاستبقاء للقوات المسلحة — call-up and retention periods for the armed forces |
| `15` | صاحب عمل — employer |
| `16` | منتدب إلى الجهة كلي — seconded **to** the entity, full |
| `17` | منتدب من الجهة جزئي — seconded **from** the entity, partial |
| `18` | منتدب إلى الجهة جزئي — seconded **to** the entity, partial |
| `19` | حالات العمل جزء من الوقت — part-time working |
| `20` | بعثات علمية — scientific missions |
| `21` | **غير مؤمن عليه** — **not insured** |
| `22` | مؤمن عليه لإجازة خاصة لغير العمل بالداخل — special leave, not for work, inside the country |
| `23` | مؤمن عليه لإجازة خاصة للعمل بالخارج — special leave for work abroad |
| `24` | مؤمن عليه طبقًا لبند 1 مادة 63 للائحة التنفيذية لقانون التأمينات الاجتماعية 148 لسنة 2019 |
| `25` | مؤمن عليه طبقًا لبند 2 مادة 63 للائحة التنفيذية لقانون التأمينات الاجتماعية 148 لسنة 2019 |
| `26` | الإجازة الخاصة لغير العمل لمرافقة الزوج (بالخارج) — special leave to accompany a spouse abroad |
| `27` | مبعوثي الأزهر الشريف بالخارج — Al-Azhar envoys abroad |
| `28` | **الأنظمة التأمينية البديلة** — **alternative insurance systems** |

**Value `28` is a scope switch, not a rate switch.** ETA FAQ, insurance Q5: alternative insurance systems are established under **Law 64/1980**, and *"لا يتم سداد تأمينات اجتماعية للعاملين التابعين للجهات التي تعمل بهذا النظام، حيث أن كل نظام له الحصة المستقلة الخاصة به"* — **no social insurance is paid to NOSI** for workers of entities operating such a system; each system has its **own independent share**. The corresponding tax exemption survives, because Law 91/2005 art. 13(2) exempts contributions deducted under the social-insurance laws *"أو أية نظم بديلة عنها"*.

**Value `21` is a hard gate.** Where the employee is not insured, **insurance data may not be entered at all** and the form is rejected if it is.

**Values `07` and `08` matter for the employer rate.** Arduous and hazardous work engage the risk-rating of the Article 46(2) injury contribution (0.5% rising up to 1%).

**Changing status mid-year is permitted.** FAQ technical Q44: an employee can move from temporary to permanent and back from one month to another, by adding the insurance data — insurance status, insurance start date, insurance end date.

## 3.3 Tax treatment (`EI060`) — the eight-value mapper

| Code | Value | Algorithm |
|---|---|---|
| `01` | للعمالة الدائمة — permanent (and temporary) staff, **this entity is the original employer** | Art. 10 annualisation |
| `02` | للعمالة التي تُحاسب بضريبة قطعية *(legacy label)* — **non-original employer** | **Flat 10% under account** on total entitlements (art. 72 bis). Original employer's 9-digit TRN mandatory |
| `03` | للعمالة التي تتقاضى أكثر من 50% — worker draws **>50% of income** or spends **>50% of time** here | Art. 10 annualisation |
| `04` | لذوي الاحتياجات الخاصة — person with a disability, **or carer of one** | Art. 10 annualisation, **personal exemption +50%** |
| `05` | عمالة أمراض مزمنة (قرار وزير الصحة رقم 259) | Art. 10 annualisation, **insurance wage exempted from net income** |
| `06` | الهيئة العامة للمنطقة الاقتصادية برقم تسجيل ضريبي 100693342 — SCZone entity established **before 24 June 2015** | **Flat 5%** on the annual pool, then apportioned |
| `07` | As `06` **and** the worker is a person with a disability or a carer | **Flat 5%** **and** personal exemption **+50%** |
| `08` | متجمد الأجور — deferred wage arrears for earlier periods | **Rules frozen**; the employer enters the annual pool and the tax **manually**; verified at examination |

**The `02` label is a historical artefact.** It reads *"تُحاسب بضريبة قطعية"* ("assessed at a final tax") because that is what Article 11 of Law 91/2005 provided before **Law 30/2023 repealed Article 11 and inserted Article 72 bis**. Since **January 2024** the 10% is **under account (تحت الحساب), not final** — ETA FAQ technical Q45 explains exactly this. Any engine, template or advice that still treats the 10% as a final tax is running the repealed law.

**Multiple treatments per employee per year are supported**, and the annual settlement computes each as a separate row (FAQ technical Q105).

## 3.4 Universal-health-insurance status (`EI115`)

| Code | Value | Consequence |
|---|---|---|
| `01` | خاضع تأمين صحي شامل — subject | Law 2/2018 applies. `EI120` and `EI125` become **mandatory** |
| `02` | غير خاضع لتأمين صحي شامل — not subject | `EI120` and `EI125` are **rejected** |

Drive this from the **establishment's actual UHIA registration**, not from a governorate lookup table — see `01-ccg.md` §5.3.

## 3.5 Work-permit status (`EI035`)

| Code | Value |
|---|---|
| `01` | ساري — valid |
| `02` | قيد الاستخراج / التجديد — under issue or renewal |
| `03` | لا يوجد — none |

The field **must be removed where the employee is Egyptian** (SDK validation). Foreigners may not work in Egypt without a work permit from the labour ministry.

## 3.6 Job grade (`EI050`)

| Code | Value |
|---|---|
| `01` | درجة ثالثة وما دونها — third grade and below |
| `02` | درجة أولى أو ثانية — first or second grade |
| `03` | درجة عليا وممتازة (ما فوق الأولى) — senior and excellent grade |

**Government entities only.** The field **must be deleted for private-sector employees** (SDK validation message: *"برجاء حذف الدرجة الوظيفية للمسلسل رقم …"*).

## 3.7 Disbursement type (`PAYROLL_TYPE`)

| Code | Value | Rule |
|---|---|---|
| `1` | صرفية أساسية — basic | Any number per company, **provided no employee already has a basic disbursement for the period** |
| `2` | صرفية إضافية — additional | Any number, no restriction. **الأجر الشامل may not be entered on it.** A tax treatment must still be chosen |
| `3` | بدون موظفين — no employees | Nil filing |

---

# 4. Employment and date fields

| Field | Arabic | ETA code | Req | Notes |
|---|---|---|---|---|
| Job title | الوظيفة | `EI045` | **M** | Letters and digits |
| Entity / branch name | اسم الجهة / الفرع | `EI055` | **M** | |
| Employment start date | تاريخ التعيين | — | **M** (contract/NOSI) | Not an ETA form field. Drives the **periodic-allowance anniversary** (Labour Law art. 12) and the leave scale |
| **Insurance subscription date** | تاريخ الالتحاق بالتأمينات | `EI080` | **C** | **`yyyymmdd`.** The **social-insurance** subscription date per **Form 1 or Form 2 – تأمينات** — expressly **not** the employment start date, and **not** "from the start of the year" (FAQ additional Q65) |
| Insurance end date | تاريخ انتهاء الاشتراك في التأمينات الاجتماعية | `EI095` | **O** | |
| Service end date | تاريخ نهاية الخدمة | `EI090` | **M** | End date at the company |
| **Work period in the month** | مدة العمل | `EI130` | **M** | **In days. Maximum 30 per month, 360 per year.** `30` for every month January–December while the worker is on strength. Leaver → to the leaving date. Joiner → from the joining date. Daily labour → actual period. **Zero produces a warning.** **Under 30 prorates the personal exemption.** **Cannot be reduced after a full month's pay was disbursed before month end** — that correction belongs in the annual settlement |
| Contract type | نوع العقد | — | **M** (labour) | Indefinite / fixed-term / task. Drives notice (3 months for indefinite, art. 156), the Article 154 five-year gratuity, and termination routes |
| Employment category | العمالة الدائمة / المؤقتة | via `EI060` = 01 | — | **Both permanent and temporary staff take tax treatment 1** (FAQ salary-items Q33). Note the distinct term *العمالة الدائمة المؤقتة* — FAQ salary-items Q30 defines it as **labour working permanently at the company as original employer but not insured there** |
| Governorate of work | المحافظة | — | **M** (operational) | Not an ETA field, but needed to determine universal-health-insurance applicability at establishment level and any regional wage orders |

---

# 5. Tax and social-security profile flags

| Flag | Values | Drives |
|---|---|---|
| `tax_treatment` | 01–08 | The entire tax algorithm |
| `is_original_employer` | Y / N | Treatment 1 vs 2 vs 3; the duty to aggregate other-employer income |
| `pct_income_at_this_employer` | % | The **>50%** test that moves a non-original employer to treatment 3 |
| `pct_time_at_this_employer` | % | The alternative **>50%** test |
| `insurance_status` | 01–28 | The whole social-insurance rate set |
| `uhi_subject` | 01 / 02 | Law 2/2018 applicability; makes two count fields mandatory or forbidden |
| `non_working_spouses` | 0–4 | +3% each on the employee UHI deduction |
| `dependants` | integer | +1% each on the employee UHI deduction |
| `disability_or_carer` | Y / N | Personal exemption **+50%**; annual leave **45 days** |
| `chronic_disease_offsite` | Y / N | Insurance wage exempt from net income |
| `sczone_pre_20150624` | Y / N | Flat **5%** |
| `alternative_insurance_scheme` | Y / N | No NOSI contributions; Law 64/1980 |
| `establishment_headcount_ge_30` | Y / N | Training and Rehabilitation Fund levy |
| `hazardous_or_arduous` | Y / N | Injury-contribution risk rating; **+7 days annual leave** |
| `industrial_estab_law_15_2017` | Y / N | The enhanced employer sick-pay scale (3 months full / 6 months 85% / 3 months 75%) |
| `stamp_duty_subject` | Y / N | Public / public-business-sector only |
| `martyrs_fund_subject` | Y / N | Public / public-business-sector only |

---

# 6. Amount fields the engine must carry per period

| Field | Arabic | ETA code | Purpose |
|---|---|---|---|
| Comprehensive wage | الأجر الشامل | `EI100` | The **Form 2 – تأمينات** figure; the starting point of the SI base |
| Non-insurable allowances | بدلات غير خاضعة تأمينيا | `EI105` | **الأجر الشامل − أجر الاشتراك** |
| Prior-period instalment | قسط مدة سابقة / أنظمة تأمينية بديلة | `EI085` | The instalment **paid during the month** for a purchased prior period, secondment or notional period |
| Amounts received from non-original employers | المبالغ الواردة من جهات عمل غير أصلية | — | Entered by the **original** employer from the other employers' notifications; added to entitlements and the pool is recomputed |
| Tax withheld by non-original employers | الضريبة المخصومة من جهات عمل غير أصلية | — | **Must** be entered by the original employer *"حتي لايكون هناك ازدواج ضريبي"* — to prevent double taxation |
| Tax computed for prior periods | الضريبة المحتسبة عن الفترات السابقة | — | Mandatory for **tax treatment 3** (SDK validation) |
| Salary tax paid outside the system | ضريبة المرتبات المسددة خارج المنظومة | — | Recalled at annual settlement and **distributed by the company across employees**; the settlement cannot be filed until totals match, formatted numeric with **two decimal places** |

---

# 7. Employer-level master data

| Field | Notes |
|---|---|
| Tax registration number (9 digits) | The unit of account: **all administrative units under one TRN are one employer**, so an inter-unit bonus is **not** a non-original-employer event unless the unit has its **own** TRN (FAQ technical Q73). Every entity, **including government entities, has an independent TRN** (FAQ salary-items Q32) |
| Head-office insurance number | **Only the head office's**, never a branch's |
| Establishment headcount | Drives the Training Fund threshold (30+) and NOSI's electronic-media concession (100+ insured) |
| UHIA registration | Drives `EI115` at establishment level |
| Core Taxation credentials and delegate | **Shared** with the payroll system; delegates are managed on Core |
| Legal form / sector | Determines stamp-duty and martyrs'-fund scope, and Civil-Service-Law field applicability |
| Law 6/2025 simplified-regime status | Suspends monthly payment and the quarterly return; monthly calculation forms **still required** |
| Establishment sick-pay regime | Whether Law 15/2017 industrial-licensing applies |

---

# 8. Retention

| Requirement | Basis |
|---|---|
| **Worker and wage registers**, paper or electronic, containing workers' data and the wage due to each | Labour Law 14/2025 **art. 105** — no retention period is stated in the article |
| Wage-receipt evidence: the signed register, the wage schedules, or completed bank transfer | Labour Law **art. 115** — the **employer bears the burden** of showing discharge |
| Withholding records: for each tax period, **the amounts paid and the person receiving them**, and **the tax withheld** — available for ETA examination, with a copy sent to ETA | Law 91/2005 **art. 86** |
| Employment contract, **four copies** — employer, worker, social-insurance office, administrative authority | Labour Law **art. 89** |

> **BELOW-FLOOR ITEM — retention periods.** Neither Labour Law art. 105 nor Law 91/2005 art. 86 states a **number of years**. The general limitation and record-keeping periods will sit in the **Unified Tax Procedures Law 206/2020** and in the Labour Law's implementing decisions, neither of which I read in full for this build. Confidence on a specific retention period: **~35%**. **Do not state a retention period from this pack.** See `07-qa-report.md` §3.

---

# 9. Field-status summary

| Group | Confidence | Basis |
|---|---|---|
| Identification fields and their formats | **93%** | ETA SDK v5 field dictionary, read directly |
| **The four mappers** (tax treatment, insurance status, UHI status, nationality/contract) | **95%** | SDK dropdown lists reproduced in full; corroborated by the FAQ's narrative descriptions of each |
| Work-period rules | **96%** | ETA FAQ technical Q39, Q40, Q93, Q13 — four independent statements |
| Mandatory/conditional/forbidden matrix | **90%** | Derived from the SDK's own validation-message table; some messages extract imperfectly from the RTL layout |
| Nationality/contract-status enum: 4 vs 5 values | **85%** ⚠ | SDK lists 4; FAQ describes 5 including daily labour |
| National-ID checksum | **not asserted** | No official specification obtained |
| Retention periods | **35%** 🔴 | **BELOW FLOOR** |
| Employer-level fields | **88%** | Assembled from FAQ answers rather than from a single employer-registration specification |
