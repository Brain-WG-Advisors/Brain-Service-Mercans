# Egypt (EG) — Statutory Integration Requirements (SIR)

**Tax year 2026 · Private-sector employers**

---

# 0. Headline finding — Egypt inverts the regional default

The pattern established for the CEMAC and GCC packs in this pipeline is that most authorities are **portal round-trip**: a human logs into a web portal, keys or uploads, and downloads a receipt; there is no machine-to-machine contract.

**Egypt's tax authority breaks that pattern.** The Egyptian Tax Authority operates a **genuine machine-to-machine channel** for payroll: a documented **REST endpoint accepting JSON**, with a published field dictionary, a pre-production environment, credential provisioning, and an SDK. ETA states it flatly (Payroll-System FAQ v4, integration Q6): *"التكامل كامل من خلال integration API"* — the integration is complete, through an integration API. And Q18: *"هل API سيكون Web Services و نعمل لها Calling? — نعم REST Web Service"*.

**The two social funds do not.** NOSI and the Universal Health Insurance Authority are, for payroll purposes in 2026, **portal / form-based** channels, and the ETA payroll system's own FAQ confirms that the integration between the payroll system and those two systems **is not yet live** (technical Q22: universal-health-insurance data is keyed manually *"لحين إتمام التكامل الكامل مع منظومة التأمينات الاجتماعية ومنظومة التأمين الصحي الشامل"*).

So Egypt is a **split-channel** country: M2M for tax, round-trip for social insurance and health.

---

# 1. Channel inventory

| # | Authority | Channel | Direction | M2M capable? | Authentication |
|---|---|---|---|---|---|
| **EG-SIR-01** | **ETA** — منظومة توحيد أسس ومعايير احتساب ضريبة الأجور والمرتبات (the Unified Payroll Tax Calculation Standards System, "the payroll system") | REST/JSON **API**, **or** CSV upload, **or** manual keying | **Outbound** (employer → ETA), with a computed result returned | **YES** | Username + password **in the request body**; same credentials as the Core Taxation system |
| **EG-SIR-02** | **ETA** — منظومة الأعمال الضريبية الرئيسية (**Core Taxation** / الميكنة الشاملة) | Portal; **fed automatically by EG-SIR-01 through internal integration** | Outbound | Indirect | ETA taxpayer-portal credentials; delegate (مفوض) permissions |
| **EG-SIR-03** | **ETA** — بوابة الموظف (**Employee Portal**) | Portal, **employee-facing** | **Inbound to the employee** | No | Employee self-registers with **national ID + mobile number** as recorded on the employer's monthly calculation forms |
| **EG-SIR-04** | **NOSI** — الهيئة القومية للتأمين الاجتماعي | Forms (paper or electronic) at the competent insurance office; electronic media accepted for large employers | Outbound | **No** | Office-based; identity by establishment insurance number |
| **EG-SIR-05** | **UHIA** — هيئة التأمين الصحي الشامل | Contribution data currently keyed by the employer **into the ETA payroll form**; remittance to UHIA | Outbound | **No** | — |
| **EG-SIR-06** | **Ministry of Labour** — inspection and records | On-premises inspection of paper or electronic registers | Inbound (inspection) | No | — |

---

# 2. EG-SIR-01 — the ETA payroll system in detail

## 2.1 Legal basis and mandation

The system was built *"طبقًا لأحكام قانون الإجراءات الضريبية الموحد الصادر بالقانون رقم 206 لسنة 2020 وتعديلاته ولائحته التنفيذية"* — under the **Unified Tax Procedures Law 206/2020**, its amendments and its executive regulations (ETA SDK v5, project overview).

Mandation ran in waves by **Ministerial Decree**, each naming the obliged entities in an annex:

| Decree | Wave | ETA-hosted file |
|---|---|---|
| **MoF Decree 137/2023** | Phase 1 | `payroll-law-137-2023.pdf` |
| **MoF Decree 175/2023** | Phase 2, sub-waves 1 and 2 | `payroll-law-175-2023.pdf` |
| **MoF Decree 251/2023** | Phase 3 | `payroll-law-251-2023.pdf` |
| **MoF Decree 386/2023** | Phase 4 **and the dates of the following phases** | `karar-386-2023-payroll.pdf` |

**The final mandation date for all entities in Egypt was 15 December 2024**, under MoF Decree 386/2023 — ETA FAQ, general Q4: *"وتعتبر اخر مراحل الالزام لجميع الجهات في مصر في 2024/12/15 وفقا لقرار وزير الماليه 386 لسنة 2023"*. As at 2026 the system is therefore **universal for obliged employers**, and once an employer's payroll-system account is activated, **manual filing of the monthly payment form and Form 2 – Salaries on Core Taxation is blocked**: ETA FAQ Q13 — *"لن يُسمح لأصحاب الأعمال تقديم هذا النموذج يدويًا علي منظومة الأعمال الضريبية الرئيسية فور تفعيل حساباتهم علي منظومة المرتبات الجديدة"*.

## 2.2 The three submission modes

ETA FAQ, general Q17, lists exactly three, and all three end at the same computation:

1. **Integration with the employer's payroll system** where one exists — the API.
2. **Download the Excel template, populate it, re-upload** to the system.
3. **Manual entry** of employee data directly on the system.

Mode 2 has a precise procedure (ETA FAQ, salary-items Q23) that is easy to fail:
```
1. Download the monthly calculation form from the Authority's portal
2. Populate all employee data — basic, insurance, financial entitlements,
   and the amounts that do not affect the tax
3. DELETE THE FIRST ROW OF THE SHEET
4. Save the file as  CSV UTF-8 (Comma delimited)
5. Log in to the payroll system and upload the monthly calculation form
6. Press "احتساب" (Calculate) to compute the tax for the period
7. Save as draft, then submit — or submit directly
```
Notes on mode 2: **there is no row limit** on the Excel sheet (FAQ salary-items Q37); **more than one sheet may be uploaded** for the same monthly calculation form (Q23); the sheet **cannot be split** into separate files because it holds basic, insurance, entitlement, deduction and non-tax-affecting sections together, though only the mandatory fields must be filled (Q67); and on error the system **displays the errors after "احتساب"** and refuses to send the file until every error is corrected (Q25).

## 2.3 The API contract

From **ETA Taxpayer SDK v5**:

```
Endpoint : https://api.preprod.uptp.eta.gov.eg/RESTAdapter/Post_Payroll_Employees
Type     : REST
Method   : POST
Format   : JSON
```

Envelope and header fields:

| Field | Type | Required | Meaning |
|---|---|---|---|
| `USER_NAME` | CHAR 12 | Yes | Integration username |
| `PASSWORD` | RAW 8 | Yes | Integration password |
| `FORM_TYPE` | CHAR 4 | Yes | Form type — sample value `U001` |
| `PERIOD` | CHAR 4 | Yes | Period — sample value `1122` (MMYY) |
| `PAYROLL_TYPE` | CHAR 1 | Yes | Disbursement type: `1` basic disbursement / `2` additional disbursement / `3` no employees |
| `EMPLOYEES` | TABLE | Yes | Array of employee items; each item carries the `EI*`, `DTE*`, `DAE*` and `NAD*` fields (see `05-data-dictionary.md`) |

The payload is wrapped in an SAP-style root — `"ns0:ZPYC_POST_EMP_PAYROLL"` with `"@xmlns:ns0": "urn:sap-com:document:sap:rfc:functions"` — and the response mirrors it as `"ZPYC_POST_EMP_PAYROLL.Response"`, returning the same employee rows with the **system-computed** values populated (in the SDK's own sample, monetary results come back as strings with two decimals, e.g. `"58600.00"`).

**Observed constraints and behaviours** (SDK; ETA FAQ, integration section):

| Item | Position |
|---|---|
| Authentication style | **Username and password carried in the request body.** There is no OAuth, no client certificate, and no mutual-TLS requirement documented |
| **Electronic seal / token** | **Not required.** ETA FAQ Q68 is explicit: *"لا تحتاج منظومة توحيد أسس ومعايير احتساب ضريبة المرتبات لوجود Token حاليًا حيث لم تتضمن متطلبات تشغيل المنظومة وجود ختم الكتروني حتي تاريخه"* — no token and no electronic seal to date. **This distinguishes payroll from ETA's e-invoicing system, which does require a seal.** Do not carry an e-invoice signing design into payroll |
| File size | JSON file size scales with employee count; **a file under 4 MB has been tested successfully** (FAQ integration Q21) |
| **JSON submits a draft, not a filing** | FAQ integration Q22: *"المتاح حاليًا هو عمل Upload للبيانات الخاصة بالمسودة و لكن الاحتساب والتقديم يتم من خلال البوابة نفسها"* — the API uploads **draft** data; **calculation and submission are performed through the portal itself.** This is the single most important integration caveat: the channel is M2M for *data transport*, but the **act of filing remains a portal action** |
| Test environment | ETA issues a **username and password for the test environment valid for 15 days, renewable once for a like period**; on moving to production the employer's account is activated there (FAQ general Q23) |
| Credentials | **The same username and password as the Core Taxation system** — no separate identity (FAQ general Q24) |
| Delegates | **No independent delegate may be added** for the payroll system separately from the Core Taxation delegate; a new delegate is added by assigning permissions **on Core Taxation** (FAQ salary-items Q58) |
| Linkage codes (أكواد الربط) | **Not issued** for taxpayers already on Core Taxation — the payroll system is simply activated. Linkage codes **are** issued to employers **not** on Core Taxation (FAQ, additional Q76) |
| ERP compatibility | *"متوافقة مع نظام SAP بالإضافة إلي الأنظمة الأخرى"* — SAP plus other systems (FAQ general Q22). Integration is with whatever payroll system the taxpayer has; the employer's ERP vendor IT staff are expected to do the work (FAQ integration Q13) |
| Live coupling | FAQ integration Q19: the integration **can** be developed so that it is directly linked to the payroll disbursement system, so that any change to a disbursement appears on the new system directly |
| Data language | **Either Arabic or English is accepted** for employee data (FAQ integration Q9, Q10). Names must be entered **in Arabic and Latin letters** (FAQ salary-items Q38), the system **validates names against nationality** (integration Q11), accepts a **four-part name** per the user guide and SDK rules (salary-items Q52), and **rejects duplicate names or duplicate national-ID cards** with an error (additional Q70) |
| Output | An Excel extract of the monthly calculation form is downloadable **after** calculation, containing the uploaded payroll data **plus the tax and insurance figures the system computed** (FAQ general Q16, technical Q48) |
| Feedback | Submitting the monthly calculation form causes the **monthly payment form to be filed on Core Taxation** with the tax computed by the payroll system (FAQ, additional Q64) |

## 2.4 Documentation set published by ETA

All at `eta.gov.eg/ar/content/payroll-services`:

| Document | File |
|---|---|
| دليل الأسئلة الشائعة — **FAQ, 4th edition, March 2026** | `2026-05/faqs-payroll-system-v4.pdf` |
| **دليل الـ SDK** — Taxpayer SDK v5 | `2023-05/UPTCP-Taxpayer-SDK-V.5.pdf` |
| دليل الممول التعريفي — taxpayer introductory guide | `2022-12/payroll-guide.pdf` |
| دليل المستخدم النهائي لتقديم نموذج الاحتساب الشهري v1.7 | `2023-09/UPTCP-Submitting-Payroll-Claculation-Form-Guide-V1.7.pdf` |
| الدليل الإرشادي لتقديم نموذج الاحتساب الشهري — v1.7 highlights, **Jan 2026** | `2026-01/uptcp_submitting_payroll_claculation_form_guide_v_1.7_highlights.pdf` |
| دليل تنسيق رفع ملف نموذج الإحتساب الشهري — upload format guide | `2023-09/uploading-monthly-calculation-form-format-guide_0.pdf` |
| دليل تقديم نموذج الربع سنوي — **Form 4 Salaries**, v1.2, **Nov 2025** | `2025-11/UPTCP_Quarterly_Payroll_Form_Submission_Guide_v.1.2.pdf` |
| الدليل الإرشادي لنموذج التسوية السنوية لسنة **2025**, v2.2, **Jan 2026** | `2026-01/uptcp_annual_payroll_claculation_form_guide_v_2.2_1.pdf` |
| الدليل الإرشادي لنموذج التسوية السنوية لسنة **2024**, v2.2 | `2025-11/UPTCP_annual_Payroll_Claculation_Form_Guide_v.2.2.pdf` |
| دليل الموظف لاستخراج قسيمة الراتب — **employee portal guide** v2.0 | `2023-02/UPTCP-Employee-Portal-Guide-V2.0.pdf` |
| دليل إدراج حسابات الممولين — enrolment guide v2.0 | `2023-02/Taxpayer-enrollement-ETA-portal-user-Guide-V2.0.pdf` |
| خطوات الإدراج على البيئة الفعلية — production enrolment steps | `2023-05/payroll-listing-steps.pdf` |
| خطوات إنشاء حساب لغير المنضمين لمنظومة الأعمال الضريبية | `2024-07/uptcp-non_core_taxpayer_enroll_guide-2024-07-14.pdf` |

## 2.5 What flows where — the integration map

```
Employer payroll / ERP
        │
        │  REST POST (JSON)  ──►  UPTP payroll system  ──►  DRAFT
        │  or CSV upload                    │
        │  or manual keying                 │  press "احتساب": tax computed
        │                                   │  press "تقديم": submitted
        ▼                                   │
                                            ├──► internal integration with CORE TAXATION:
                                            │      • نموذج السداد الشهري (monthly payment form)
                                            │      • نموذج 2 مرتبات (Form 2 Salaries)
                                            │      • نموذج 4 مرتبات (Form 4 Salaries, quarterly)
                                            │      • نموذج 9 تسويات (Form 9 Settlements, annual)
                                            │      → CLAIMS (مطالبات) issued on Core:
                                            │          – salary tax
                                            │          – martyrs'-fund contribution
                                            │      → employer pays the claim on Core
                                            │
                                            └──► EMPLOYEE PORTAL: payslip (قسيمة الراتب)

NOSI (social insurance)   ── separate, form-based, not integrated (as at Mar 2026)
UHIA (health insurance)   ── data keyed into the ETA form by the employer;
                             remittance separate; integration pending
```

Two consequences a design must respect:

1. **The payroll system does not issue claims itself.** FAQ, additional Q62: *"لا تصدر منظومة توحيد أسس ومعايير احتساب ضريبة الاجور والمرتبات مطالبات بالسداد بل هي مسئولة عن حساب ضريبة المرتبات … وتقديم نموذج السداد الشهري لجهات الأعمال علي منظومة الأعمال الضريبية الرئيسية."* Claims live on **Core Taxation**; payment is made there.
2. **A claim is only issued if the form is actually SENT.** FAQ Q9: a claim issues per disbursement *"بشرط القيام بإرسال نموذج الاحتساب وليس الاكتفاء فقط بالتحقق او حفظ مسوده"* — verifying or saving a draft is not enough.

---

# 3. EG-SIR-03 — the Employee Portal

| Item | Position |
|---|---|
| Who creates the account | **The employee, personally.** FAQ general Q10: *"يقوم الموظف نفسه بإنشاء الحساب الخاص به من خلال بوابة الموظف، ولا علاقة للمسئول عن التسجيل علي منظومة المرتبات بهذه البوابة"* — the employer's payroll-system administrator has **no** relationship with this portal, for privacy and account-confidentiality reasons |
| Credentials | **National ID + the employee's mobile number**, as recorded on the employer's monthly calculation forms. The mobile number receives a **confirmation code** to complete registration (FAQ, additional Q61) |
| What it delivers | **قسيمة الراتب** — a payslip for the tax period, containing **all** the employee's cash and in-kind entitlements, the amounts that do not affect the tax, **and all deductions made from their wage** (FAQ, additional Q74) |
| Consequence of non-registration | **None for the employer.** FAQ salary-items Q22: the portal is a benefit to the employee; if the employee does not register there is no effect on the company |
| Employer data obligation | The **mobile-number column is therefore load-bearing**: it is the activation channel for the employee's portal account and one of the confidentiality controls |

---

# 4. EG-SIR-04 — NOSI

| Item | Position |
|---|---|
| Channel | **Forms lodged with the competent insurance office**, manually or electronically. Establishments with **more than 100 insured workers** may submit wage-adjustment forms **electronically on USB or CD** to their insurance office (NOSI announcement, 30 November 2025) |
| Enrolment | **Form 1 – نموذج 1 تأمينات** (*طلب اشتراك مؤمن عليه*), in triplicate — original plus two copies — **within two weeks of the worker joining** |
| Supporting documents for enrolment | Digitised birth certificate; qualifications and professional-union membership; national ID copy; appointment decision or employment contract; statement of work receipt where applicable; **Form 3** basic-data sheet for prior subscription periods; **Form 4** worker's declaration on prior periods; **Form 111** medical-fitness report; **Form 5** insurance-coverage data |
| Wage / contribution data | **Form 2 – استمارة 2 تأمينات** carries the **الأجر الشامل** (comprehensive wage) and the insurance-wage data, and is the source of truth the ETA payroll form points at (ETA FAQ, insurance section, Q1–Q2) |
| Subscription date | **Form 1 or Form 2** determines *تاريخ الاشتراك في التأمينات الاجتماعية* — the insurance subscription date, which is a distinct field from the employment start date (FAQ, additional Q65) |
| Statutory data obligation | **Law 148/2019 art. 120**: the private-sector employer must submit workers' data, wages and contributions on NOSI's forms. Failure → contributions computed on the last statement submitted or on NOSI's own investigations, with notification, a **30-day** objection window, an **EGP 100** objection fee, a 30-day answer, then the dispute-examination committee (art. 148) and the court |
| Payment | **Beginning of the month following the month of accrual** (art. 121), with the additional amount **waived if paid within 15 days** |
| M2M | **No.** No documented API, no schema, no certificate model. ETA's own FAQ describes the ETA↔NOSI integration as **pending** |

---

# 5. EG-SIR-05 — UHIA

| Item | Position |
|---|---|
| Data capture | Currently **keyed by the employer into the ETA monthly calculation form** — flag `EI115` plus the two count fields `EI120` (non-working spouses) and `EI125` (dependants) — *"بمعرفة صاحب الأعمال لحين إتمام التكامل الكامل"* (ETA FAQ technical Q22) |
| Data ownership | The **employee** supplies spouse and dependant data; the employer makes it available; **responsibility for its accuracy rests on the employee** (FAQ, laws Q1) |
| Data-privacy position | FAQ, laws Q3: entering this data on the system does **not** conflict with data-confidentiality law, because all of it is provided for in the tax law, the social-insurance law or the universal-health-insurance law, and **employers therefore do not need employee consent** to make it available to the system |
| Remittance | Employer deducts the employee share and remits both shares to the Authority **monthly** (UHIA FAQ) |
| M2M | **No** |

---

# 6. EG-SIR-06 — Ministry of Labour

| Item | Position |
|---|---|
| Register obligation | **Labour Law art. 105**: employers or their representatives must keep **paper or electronic registers** containing workers' data and the wage due to each worker |
| Inspection | The competent Ministry's inspection bodies conduct **periodic inspection** of establishments subject to the law to verify implementation of **National Wages Council decisions** |
| Contract deposit | **Art. 89**: the employment contract is written in Arabic in **four copies** — employer keeps one, worker receives one, **the third is deposited with the competent social-insurance office**, and the fourth with the competent administrative authority |
| Channel | On-premises / office lodgement. **No M2M** |

---

# 7. Design consequences for a payroll engine

1. **Build the API integration, but do not model it as "file and forget".** The JSON channel delivers a **draft**; calculation and submission are portal actions. A fully unattended month-end is **not** achievable with the documented 2026 contract. Design for API transport + a human submit step, and instrument the gap.
2. **Do not build an electronic-seal / certificate layer for payroll.** ETA states no token and no e-seal is required. Reuse of the e-invoicing signing stack is over-engineering and will not authenticate anything.
3. **Credentials are shared with Core Taxation, and delegates are managed on Core.** Provisioning is not a payroll-system concern; it is an ETA-portal identity concern.
4. **Two authorities, two calendars, two remittance rails.** Salary tax and the martyrs'-fund contribution settle through Core claims; social insurance settles at NOSI; health insurance settles at UHIA. Only the first is automated.
5. **The employee payslip is delivered by the authority, not only by the employer.** The ETA Employee Portal issues a payslip built from what the employer filed. Anything the employer omits from the form is **absent from the employee's official payslip** — which makes the "amounts not affecting the tax" block (`NAD*`) functionally mandatory even though each field is technically optional. ETA FAQ Q7 says as much: the payslip *"ستعبر عن جميع بيانات المرتبات بما في ذلك المبالغ الغير مؤثره على الضريبة مثل الجزاءات والغياب والنفقة والسلفة"*.
6. **There is no amended filing anywhere in this stack.** No amended monthly calculation form, no amended quarterly return, no amended annual settlement (FAQ Q102, Q103, salary-items Q31). Correction happens in the **next month's form**, in an **additional disbursement**, or in the annual settlement's **processing sheet** — and, once the annual settlement is submitted, **no disbursement may be filed for that period at all** (FAQ Q104). Validation must therefore be pre-submission, not post-hoc.
7. **Pre-file before you pay.** ETA recommends uploading and calculating the monthly form **before** the disbursement — FAQ technical Q61 and current-phase Q3: *"يُفضل رفع بيانات نموذج الاحتساب الشهري قبل الصرفية واحتسابها من قبل المنظومة"* — so that the employer knows the tax before paying the net, and has evidence.

---

# 8. Confidence

| Item | Confidence | Basis |
|---|---|---|
| ETA payroll system is M2M-capable (REST/JSON, documented endpoint) | **97%** | SDK v5 endpoint, method, format and sample payload read directly; FAQ integration Q6, Q15, Q18 corroborate |
| **JSON = draft only; submission via portal** | **93%** | FAQ integration Q22 verbatim, from the **March 2026** edition. The one risk is that the contract has since been extended without the FAQ being updated |
| No token / no electronic seal required | **93%** | FAQ additional Q68 verbatim, qualified by *"حتي تاريخه"* — "to date" — so it is time-bound by construction |
| Credentials shared with Core Taxation; delegates on Core | **95%** | FAQ general Q24, salary-items Q58 |
| Mandation waves and the 15 Dec 2024 final date | **95%** | FAQ general Q4 names MoF Decree 386/2023; the four decree files are ETA-hosted |
| Three submission modes and the CSV procedure | **96%** | FAQ general Q17, salary-items Q23, step by step |
| Employee portal mechanics (self-registration, ID + mobile) | **95%** | FAQ general Q10, additional Q61, Q74 |
| NOSI is form-based, not M2M | **85%** | An **absence finding**: NOSI publishes forms and office procedures and no API; ETA describes the NOSI integration as pending. Absence of evidence, corroborated by ETA's own statement, but not a positive statement by NOSI that no API exists |
| UHIA is not integrated | **90%** | ETA FAQ technical Q22, explicit and dated |
| **Production endpoint host** | **60%** ⚠ | The SDK publishes only the **pre-production** host (`api.preprod.uptp.eta.gov.eg`). The production host is **not** in any document I read. **BELOW FLOOR** — obtain it from ETA with the production credentials |
| Field-level error catalogue | **70%** ⚠ | The SDK contains a validation-message table, but it extracts poorly from the PDF's RTL layout and I transcribed it only in part. Re-derive from a live test run rather than from this pack |
