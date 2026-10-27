# Egypt (EG) — QA and Confidence Report

**Build type:** from-scratch primary-source research. **No pre-existing Mercans CCG, WTC, SIR, Data Dictionary or reports spec existed for Egypt** — the only prior Egypt artefact in the pipeline was a payslip-generator workbook (`EG-compliance/06-payslip/`), which was **not** used as an input to this build and which this pack **contradicts in two places** (see §6).
**Target year:** 2026 · **Currency:** EGP · **Scope:** private-sector employees
**Gate applied:** 95% floor. Sections below that floor are marked explicitly and are **not** rounded up.
**Research date:** 27 August 2026.

---

# 1. Verdict

**READY FOR REVIEW — with eight sections honestly below the 95% floor and two live-data dependencies that must never be cached.**

The **calculation core is strong and, in several places, better sourced than any published summary of Egyptian payroll**:

- The **Article 8 rate matrix currently in force** was recovered **verbatim from the Official Gazette** (Law 7/2024, *العدد 7 مكرر (أ)، 21 فبراير 2024*) after the ETA-hosted copy of that gazette proved to be a damaged PDF that standard tooling could not open. Its **six-column withdrawal structure** — which almost every secondary summary flattens into a seven-band ladder — is reproduced here in full, together with a computed **cliff table** at each column boundary.
- The **11% / 18.75%** social-insurance split, which appears nowhere in the statute as such, was **reconciled fund by fund to the articles of Law 148/2019** and closes to the cent, including an explanation of why NOSI's own published total of 28.75% is a different (and also correct) number.
- The **Article 10 annualisation engine** — cumulative net income × 360 ÷ days, matrix, apportion back, subtract prior periods, recompute at every disbursement — is taken from ETA's own **March 2026** FAQ, not reconstructed.
- The **field-level specification of the monthly calculation form** comes from ETA's own **Taxpayer SDK**, including the REST endpoint, the payload shape and the four mappers.

The **gaps cluster in four predictable places**: (a) **form layouts** ETA does not publish as images or schemas; (b) **operational detail** for the two smallest levies; (c) **ministerial issuances** made under Law 14/2025 after 1 September 2025 that I could not enumerate; and (d) **the social-insurance/health-insurance boundary** where the two statutes overlap and the operative rate table is internal to NOSI.

**No section was silently rounded up.** Eight items are stated below floor. That is the intended outcome of the gate.

---

# 2. Confidence by section

| Ref | Section | Confidence | Basis |
|---|---|---|---|
| **01** | Fiscal year, currency, official language, scope filter | **97%** | ETA FAQ technical Q120 on the Jan–Dec settlement year, verbatim; Labour Law arts. 89, 176 on Arabic; Law 148/2019 art. 2 First(3) on the private-sector category |
| **01** | **Article 8 rate matrix (Law 7/2024)** | **99%** | **Gazette text, verbatim**, recovered by repairing the damaged PDF. Corroborated by reading the two predecessor matrices (Laws 30/2023 and 175/2023) and confirming the direction of change |
| **01** | The **bracket-withdrawal cliffs** at 600k / 700k / 800k / 900k / 1.2m | **97%** | **Computed** from the verbatim matrix; each cliff reconciles exactly to the value of the withdrawn band (e.g. 40,000 × 10% = 4,000). Arithmetic, not interpretation |
| **01** | Personal exemption EGP 20,000, prorated by work period | **97%** | Law 7/2024 art. 13(1) verbatim; proration from ETA FAQ technical Q93 |
| **01** | Effective date of Law 7/2024 for salary tax = 1 March 2024 | **97%** | The law's second enacting article verbatim: *"من أول الشهر التالى لتاريخ نشره"* |
| **01** | **No 2025/2026 change to Article 8** | **93%** | Laws 5, 6 and 7 of 2025 read **in full** — none touches art. 8 or art. 13. An **absence finding**: a later 2026 amendment could exist that I did not surface. See §4.1 |
| **01** | Article 10 annualisation, 360-day convention, per-disbursement recomputation | **97%** | ETA FAQ general Q15, technical Q5, Q29, Q39, Q40, Q76 — six independent restatements, plus the statute |
| **01** | Rounding: annual pool **down** to nearest EGP 10 | **98%** | Art. 8 final sentence, present in all three gazette versions read |
| **01** | **SI contribution wage — the 16 elements and 4 excluded allowance classes** | **96%** | Law 148/2019 art. 1(8) verbatim from NOSI's own published edition. Slight discount because that PDF's Arabic glyph mapping is degraded (letters, not digits) |
| **01** | **Contribution-wage floor 2,700 / ceiling 16,700 from 1 Jan 2026** | **98%** | NOSI's own announcement of 30 Nov 2025, with the 2025 comparatives and the pension consequences |
| **01** | **Fund-by-fund reconciliation to EE 11% / ER 18.75%** | **95%** | Each line traced to an article (19, 36, 46, 70, 86) and the total closes exactly. The **3.25% sickness** limb depends on private-sector employees being items 3–5 of art. 2 First, which art. 2 confirms |
| **01** | The Reward System (art. 36) is the employee's third percentage point, **not** unemployment | **96%** | Art. 36 verbatim (1% + 1%, individual account); art. 86 verbatim (employer-only 1%) |
| **01** | Why NOSI says 28.75% and the employer still pays 18.75% | **90%** | A **reconciliation argument**: 11 + 17.75 = 28.75 excludes the art. 46(1) 1% remitted to the health authority. Arithmetically exact and consistent with art. 46(1)'s drafting, but NOSI does not state the decomposition itself |
| **01** | Next contribution-rate step falls **1 Jan 2027**, not 2026 | **94%** | Art. 19 final paragraph: +1% every seven years from entry into force (1 Jan 2020) |
| **01** | SI payment due at the start of the following month, **15-day grace** | **96%** | Art. 121 verbatim, including the express waiver |
| **01** | Delay fee: CBE rate + 2%; additional amount: T-bill average + 2% | **96%** | Law 91/2005 art. 110 and Law 148/2019 art. 121, both verbatim |
| **01** | **100% cap on delay fee / additional tax** | **96%** | Art. 45 bis of Law 206/2020, inserted by Law 7/2025, read from the gazette |
| **01** | **Universal health insurance — EE 1% + 3%/spouse + 1%/dependant; ER 4% min EGP 50** | **92%** | Law 2/2018 art. 40 gives the employer 4%; the **employee-side splits and the EGP 50 minimum come from UHIA's own FAQ**, not from Schedule 1, which I did not obtain |
| **01** | **Which SI components UHI displaces** | **72%** ⚠ | **BELOW FLOOR** — see §3.1 |
| **01** | UHI governorate rollout list | **78%** ⚠ | Phase 1 well established; **Phase 2 list and dates are press-sourced.** Mitigated by driving the engine from the per-employee flag. See §3.2 |
| **01** | BIK valuations (car 20%, mobile 20%, loan 7%, life premiums, shares at fair value with restriction deferral) | **97%** | Executive Regs art. 11 verbatim, including the two amending decrees named in the text |
| **01** | Exempt collective benefits list and "enter them nowhere" | **97%** | Law 91/2005 art. 13(5) verbatim **and** Regs art. 12(6) verbatim **and** four separate FAQ answers |
| **01** | The eight tax treatments and their effects | **96%** | ETA FAQ technical Q26–Q34, each treatment described in its own answer; corroborated by the SDK dropdown |
| **01** | Art. 72 bis 10% is **under account, not final** | **97%** | Law 30/2023 gazette text verbatim; FAQ technical Q45 explains the repeal of art. 11 |
| **01** | Training Fund levy — rate, threshold, floor/cap, annual frequency | **93%** | Labour Law art. 21(1) **verbatim**. Discounted only because of the base ambiguity — see §3.3 |
| **01** | Martyrs' Fund — rate and mechanics | **90%** | ETA FAQ additional Q110, verbatim and current |
| **01** | Martyrs' Fund — **private sector not subject** | **80%** ⚠ | See §3.4 |
| **01** | Stamp duty on salaries — **private sector not subject** | **88%** | ETA FAQ additional Q66 (*"الصرفيات الحكومية"*) and technical Q88 (public-business-sector companies, art. 79 + State Council Fatwa 475/2/37 of 16/7/1994) |
| **01** | **Minimum wage EGP 7,000 from 1 March 2025**; part-time EGP 28/hour net; periodic allowance 3% of insurance wage with EGP 250 floor | **95%** | **Ministry of Planning announcement of the 9 Feb 2025 Council meeting** — the chairing ministry's own publication |
| **01** | **Private-sector minimum wage still 7,000 as at 27 Aug 2026** | **85%** ⚠ | An **absence finding** — see §4.2 |
| **01** | **Periodic increase is 3% of the insurance wage, not 7% of basic** | **97%** | Labour Law art. 12 verbatim; art. 102(2) confirms the Council's power to set the floor |
| **01** | Overtime **+35% day / +70% night**; rest-day = equal pay **and** a substitute day | **97%** | Art. 121 verbatim |
| **01** | Annual leave 15 / 21 / 30 / 45 + 7; three-year settlement; waiver forfeits pay in lieu | **97%** | Arts. 124, 125 verbatim |
| **01** | Sick pay 75% / 85%, 180 days, 100% chronic; the Law 15/2017 industrial scale | **96%** | Law 148/2019 art. 76 and Labour Law art. 131, both verbatim |
| **01** | Maternity 4 months, ≥45 days post-natal, 3 times; nursing 2 × 30 min for 2 years | **97%** | Arts. 54, 55, 56 verbatim |
| **01** | **Public-holiday list** | **35%** 🔴 | **BELOW FLOOR** — see §3.5 |
| **01** | Notice **3 months flat**; art. 154 gratuity; art. 165 two-months-per-year floor | **97%** | Arts. 154–165 verbatim |
| **01** | Wage payment, 10% loan cap, **25%/50% attachment cap computed after tax and SI** | **97%** | Arts. 108, 113, 114 verbatim, including the base-definition paragraph |
| **01** | **Foreign employees' social-insurance liability test** | **65%** 🔴 | **BELOW FLOOR** — see §3.6 |
| **02** | Wage-type tax/SI treatments | **93%** | Derived by applying two verbatim statutory lists (art. 9 / art. 1(8)) to each wage type, plus explicit FAQ answers for the contested ones (transport, meal allowance, medicine allowance, hardship allowance) |
| **02** | The `DTE` / `DAE` / `NAD` **field codes** | **75–93%** ⚠ | Label set complete and correct; **code-to-label pairing drifts in places** — see §3.7 |
| **02** | The 24-element / three-classification structure | **97%** | ETA FAQ technical Q38, enumerated in full |
| **02** | Employer-borne tax is a taxable cash benefit; gross-up is iterative | **96%** | FAQ technical Q50, Q51, salary-items Q21 |
| **02** | Leave-balance cash paid **during service** falls wholly in the period | **97%** | Art. 10 carve-out *"عدا مقابل الإجازات"* + FAQ technical Q99(6) |
| **02** | End-of-service gratuity taxable on re-appointment | **95%** | FAQ technical Q96, explicit |
| **02** | **Tax treatment of unlawful-termination compensation / ex gratia** | **50%** 🔴 | **BELOW FLOOR** — see §3.8 |
| **02** | `EG-*` code strings | **n/a — DERIVED** | No Global WTC mapping exists for Egypt; the `EG-*` numbering is this pack's own |
| **03** | ETA payroll system is **genuinely M2M** (REST/JSON) | **97%** | SDK endpoint, method, format, sample payload; FAQ integration Q6, Q15, Q18 |
| **03** | **JSON uploads a draft; calculation and submission happen on the portal** | **93%** | FAQ integration Q22 verbatim, March 2026 edition |
| **03** | **No token / no electronic seal** | **93%** | FAQ additional Q68, expressly time-bound (*"حتي تاريخه"*) |
| **03** | Credentials shared with Core Taxation; delegates managed on Core | **95%** | FAQ general Q24, salary-items Q58 |
| **03** | Mandation waves; final date 15 Dec 2024 | **95%** | FAQ general Q4 naming MoF Decree 386/2023; four decree files ETA-hosted |
| **03** | NOSI is form-based, not M2M | **85%** | An absence finding, corroborated by ETA's statement that the integration is pending |
| **03** | **Production API host** | **60%** 🔴 | **BELOW FLOOR** — the SDK publishes only `api.preprod.uptp.eta.gov.eg` |
| **03** | SDK validation-message catalogue | **70%** ⚠ | Partially transcribed; RTL table extraction is lossy |
| **04** | Authority / frequency / deadline / trigger for all reports | **94%** | Statute for the tax deadlines (arts. 14, 15, 86), ETA FAQ for the system mechanics |
| **04** | **Monthly calculation form field layout** | **92%** | SDK v5 field dictionary, transcribed directly |
| **04** | Monthly payment form layout | **70%** ⚠ | **DERIVED** — asserted by ETA to equal the pre-existing Core form, which I could not obtain |
| **04** | Form 2 Salaries layout | **60%** 🔴 | **DERIVED, BELOW FLOOR** |
| **04** | Form 4 Salaries layout | **65%** 🔴 | **DERIVED, BELOW FLOOR.** The **four content items** are ETA's own statement of what art. 31 of the Law 206/2020 regulations requires |
| **04** | Form 9 Settlements layout | **70%** ⚠ | Mechanics richly documented; **layout not obtainable** |
| **04** | Form 9 replaces Forms 6, 7 and 8 | **95%** | FAQ additional Q75, explicit |
| **04** | **Day-of-month for the quarterly return** | **55%** 🔴 | **BELOW FLOOR** — see §4.3 |
| **04** | Form /21خ stamp-duty return | **45%** 🔴 | **DERIVED, BELOW FLOOR.** Out of private-sector scope |
| **04** | Training Fund collection form and due date | **40%** 🔴 | **BELOW FLOOR** — see §3.3 |
| **04** | NOSI Form 6 (end of service) | **55%** 🔴 | **BELOW FLOOR** — the form number and role are asserted from practice, not verified |
| **05** | The four mappers (tax treatment, insurance status 28 values, UHI status, nationality) | **95%** | SDK dropdowns reproduced in full, corroborated by FAQ narrative |
| **05** | Identifier formats (14-digit national ID, 9-digit TRN, passport rules) | **93%** | SDK field dictionary |
| **05** | National-ID **checksum** | **not asserted** | No official specification obtained |
| **05** | Nationality/contract enum — 4 or 5 values | **85%** ⚠ | SDK lists 4; FAQ describes 5 including daily labour |
| **05** | **Record-retention periods** | **35%** 🔴 | **BELOW FLOOR** — see §3.9 |
| **06** | **Art. 115 is the mandate and there is no statutory content list** | **97%** | Gazette text read in full and **grep-tested** across six candidate terms |
| **06** | Art. 15(2) three-item tax statement, on request | **96%** | Law 91/2005 verbatim |
| **06** | ETA Employee-Portal payslip and its content | **93%** | FAQ additional Q74, general Q10, salary-items Q22, Q50 |
| **06** | **Whether a post-Sept-2025 ministerial decision adds payslip content** | **50%** ⚠ | **BELOW FLOOR** — see §3.10 |

---

# 3. Below-floor sections, stated plainly

## 3.1 Which social-insurance components universal health insurance displaces — **72%**

**What is solid.** Law 2/2018 art. 40 obliges employers at **4%** of the contribution wage. UHIA describes that 4% as **3% sickness + 1% work injury**, with a **minimum of EGP 50/month**, and the employee at **1%** plus 3% per non-working spouse and 1% per dependant. Those percentages map one-for-one onto Law 148/2019 art. 70 (sickness treatment and care) and art. 46(1) (injury medical care). Art. 46(1) is drafted to apply only to those **not** subject to the universal-health-insurance law, and art. 70 opens *"مع عدم الإخلال بأحكام قانون نظام التأمين الصحي الشامل"*.

**What is missing.** The **exact residual NOSI employer percentage** for a UHI-covered private-sector employee. Specifically: private-sector employers pay **3.25%** sickness, of which **0.25%** funds *wage compensation and transport costs* rather than treatment. Whether that 0.25% stays at NOSI when the treatment limb moves to UHIA, or falls away with it, determines whether the employer's combined burden for a UHI-covered employee is 18.75%, or something between 18.75% and 19.75%.

**Why I could not close it.** The operative table is internal to NOSI and is loaded into the ETA system behind insurance-status code `06` — ETA FAQ salary-items Q35 says the system *"تم تغذية بيانات النظام بجميع حالات حساب اشتراكات التأمينات الاجتماعية المعدة بواسطة الهيئة القومية للتأمين الاجتماعي"*. NOSI does not publish that table as a document.

**What would close it to ~97%.** Either (a) NOSI's published contribution-rate table by insurance-status code, or (b) a screenshot / Excel extract of an ETA monthly calculation form for an employee with `EI070 = 06` and `EI115 = 01`, showing the computed employer and employee amounts against a known contribution wage. Option (b) is trivially obtainable by any employer already on the system and would settle it definitively.

## 3.2 Universal-health-insurance governorate rollout — **78%**

Phase 1 (Port Said, Ismailia, Suez, South Sinai, Luxor, Aswan) is well established. **Phase 2 — announced as Minya, Matrouh, Damietta, Kafr El Sheikh and North Sinai, with Alexandria under study — is press-sourced**, from reporting of government statements in 2026, not from a gazette schedule or a UHIA publication I could read. Law 2/2018 art. 3 applies the system *"تدريجيا على المحافظات استرشادا بالمراحل المبينة بالجدول رقم (5)"* — guided by Schedule 5, which I did not obtain.

**Mitigation, and why this is not fatal.** The engine input is **not** a governorate table. It is the per-employee flag `EI115`, which the employer sets from the establishment's actual UHIA registration. **Drive from the flag.** A wrong governorate table produces a wrong *expectation*; a wrong flag produces a wrong *number*.

**What would close it.** Schedule 5 of Law 2/2018 plus the Prime Ministerial decrees activating each phase.

## 3.3 Training and Rehabilitation Fund levy — operational detail — **40%**

**Verbatim and high-confidence:** Labour Law art. 21(1) — **0.25% of the minimum insurance wage**, establishments with **30+ workers**, **floor EGP 10 / cap EGP 30 per worker**, **paid annually**, with a full exemption available where the establishment trains its own workers per ministerial rules.

**Ambiguous:** whether "0.25% of the minimum insurance wage" means the **monthly** minimum (2,700 → 6.75, floored to **EGP 10**) or the **annualised** minimum (32,400 → 81.00, capped at **EGP 30**). The statute does not say.

**Missing entirely:** the collection form, the payment channel, the due date within the year, and the ministerial decree fixing the exemption rules.

**Materiality is low and bounded.** Under either reading the levy is **between EGP 10 and EGP 30 per worker per year** — for a 500-employee establishment, between EGP 5,000 and EGP 15,000 annually. Model **EGP 10 per worker per year** for 2026 (the more conservative reading), disclose the assumption, and confirm with the Fund.

**What would close it.** The Prime Ministerial decree constituting the Fund's board and **its resource-collection system**, which art. 20 requires to be issued, plus the competent Minister's exemption decree.

## 3.4 Martyrs' Fund — the private-sector exclusion — **80%**

The **rate and mechanics** (EGP 5 per EGP 10,000 of basic disbursements, all labour except Egyptian daily labour, its own Core claim) are from ETA's March 2026 FAQ and are solid at ~90%.

**The scope restriction to public agencies, the public sector and the public business sector rests on reporting of the 2021 amending law's text**, not on the gazette article itself. I retrieved Law 16/2018's existence and purpose but not the article listing the Fund's resources.

**Why it matters.** If the restriction is wrong, every private employer in Egypt owes 0.05% of basic pay that this pack says they do not. **In a mixed group containing public-business-sector entities, verify per entity.**

**What would close it.** The gazette text of the 2021 amendment to Law 16/2018, or **ETA circular 119/2021** on the Fund.

## 3.5 Public holidays — **35%**

Labour Law art. 129 grants the worker **paid leave on the holidays, feasts and occasions determined by decision of the competent Minister**, and applies the rule to the religious feasts of non-Muslims. **The entitlement is statutory; the list is not.** I did not retrieve the ministerial decision.

**Do not populate a holiday calendar from this pack.** Note also that Egypt's ministerial holiday decisions routinely **move** observances to the nearest Thursday, which is a payroll-scheduling fact, not just a calendar fact — and I have no primary source for the current rule.

**What would close it.** The competent Minister's decision determining holidays, feasts and occasions, and any decision on their observance dates.

## 3.6 Foreign employees' social-insurance liability — **65%**

Law 148/2019 art. 2 First(3) covers *"العاملين بالقطاع الخاص الخاضعين لأحكام قانون العمل"* and requires a **regular** employment relationship, with the Executive Regulations setting the rules for what counts as regular. Egyptian law equalises the foreign worker's rights with the Egyptian worker's **subject to reciprocity**, and a foreigner may not work without a Ministry of Labour permit.

**What I could not verify from primary text** is the operative test most practitioners state: a contract of **at least one year** **plus** a **reciprocity agreement** with the worker's state. The Executive Regulations of Law 148/2019 (issued by Prime Ministerial decree) would settle it; I did not obtain them.

**Mitigation.** Drive the engine from the explicit per-employee **insurance-status** field (`EI070`, value `21` = *غير مؤمن عليه*), not from nationality. And note that **salary tax applies to foreigners identically to Egyptians** — ETA FAQ technical Q52 and Q77 are categorical — so the open question is **social insurance only**.

**What would close it.** The Executive Regulations of Law 148/2019, and Egypt's list of bilateral social-security agreements.

## 3.7 `DTE` / `DAE` / `NAD` code-to-label pairing — **75% on the flagged rows, 93% elsewhere**

The SDK's field dictionary is laid out as multi-column right-to-left tables. Under text extraction the **code column and the label column drift apart** in several rows — most visibly around `DTE140` / `DTE150` (both extracting as *علاوة مضمومة*), `DTE175` / `DTE180` (the exempt / taxable special-allowance pair), and the block `DTE250`–`DTE290`, where the SDK's **sample payload carries more populated codes than the dictionary rows I could align with certainty**.

**The label set is complete and correct** — it matches ETA FAQ technical Q38's enumeration of 24 elements in three classifications **exactly**, and that enumeration is reproduced in `04-reports-spec.md` §1.4.3 as the authoritative list.

**What would close it.** A downloaded copy of the live Excel monthly calculation form, whose column headers pair codes to labels unambiguously, or a fresh SDK release. **Do not wire an integration to the flagged rows without that check.**

## 3.8 Tax treatment of unlawful-termination compensation — **50%**

Law 91/2005 art. 12(2) puts *"مكافآت نهاية الخدمة"* outside the charge. Whether **Article 165 damages** (not less than two months' wage per year of service) and negotiated ex-gratia settlements fall inside that phrase, or are caught by Article 9's catch-all — *"أيًا كانت مسميات أو صور أو أسباب هذه المستحقات"* — is **not settled** by any source I read, and the ETA payroll system provides **no dedicated field** for it.

The conservative position stated in `02-wtc.md` §4 is: treat court-ordered or settlement **damages** as outside Article 9 (they compensate harm, not work), treat anything structured as additional **remuneration** as taxable, and obtain a ruling for material amounts.

**What would close it.** An ETA circular (كتاب دوري) or a published appeal-committee principle (مبادئ لجان الطعن) on the point — ETA publishes both categories on its website.

## 3.9 Record-retention periods — **35%**

Labour Law art. 105 requires paper or electronic worker-and-wage registers **and states no retention period**. Law 91/2005 art. 86 requires withholding records to be kept available for examination **and states no period**. The general periods will sit in the **Unified Tax Procedures Law 206/2020** and in Labour Law implementing decisions, neither of which I read in full.

**Do not state a retention period from this pack.**

**What would close it.** Law 206/2020's record-keeping and limitation articles, plus the Labour Law's implementing decisions.

## 3.10 Whether a post-September-2025 ministerial decision prescribes payslip content — **50%**

`06-payslip.md` establishes, by reading the full gazette text and grep-testing six candidate terms, that **Law 14/2025 itself prescribes no payslip content list**. That finding is at 97%.

**What is at 50% is the delegated layer.** Law 14/2025 delegates extensively to ministerial decisions — on reduced hours for categories of workers (art. 117), on intermittent and special-nature work (art. 119), on hazardous and remote-area work (art. 124), on holidays (art. 129), on contagious diseases (art. 132), on training-levy exemption (art. 21), among many others. **One of those issuances could prescribe payslip content**, and I did not enumerate the decisions issued after the law came into force on 1 September 2025.

**What would close it.** An index of ministerial decisions issued under Law 14/2025 since 1 September 2025.

## 3.11 Production API host — **60%**

The SDK publishes only the **pre-production** endpoint: `https://api.preprod.uptp.eta.gov.eg/RESTAdapter/Post_Payroll_Employees`. The **production** host appears in no document I read. Do **not** guess it by dropping "preprod" from the hostname — obtain it from ETA with the production credentials.

---

# 4. Genuine ambiguities and absence findings (not research gaps)

## 4.1 "No 2025 or 2026 change to Article 8" is an absence finding

I read Laws **5, 6 and 7 of 2025** in full and confirmed none touches Article 8, Article 13 or the salary-tax mechanism. I also searched for a 2026 amendment and found that Egypt's 2026 tax-amendment activity concerned **value added tax**. That is **evidence of absence** rather than a positive statement that Article 8 is unamended, and it is stated at 93% rather than 97% for that reason. **Re-verify at each tax year rollover** against ETA's *قوانين ضرائب الدخل* and *كتب دورية وتعليمات* pages.

## 4.2 The private-sector minimum wage for the second half of 2026

The **state administrative apparatus** minimum rises to **EGP 8,000 from July 2026**. Reporting through **mid-June 2026** states the private-sector application date is **not officially fixed**, and I found **no National Wages Council decision** extending EGP 8,000 to the private sector as at **27 August 2026**.

**The position stated in `01-ccg.md` §9.1 is therefore EGP 7,000** — the last positively-decided figure. This is an absence finding at 85%, and it is **exactly the kind of value that must be re-verified at every payroll run**. The Council has changed the minimum **six times in four years**; caching it is a defect, not an optimisation.

Watch: `mped.gov.eg` (the chairing ministry publishes each Council decision) and Ministry of Labour circulars to the directorates on implementation mechanics.

## 4.3 The day of the month for the quarterly return

Law 91/2005 art. 15(1) names the **months** — January, April, July, October — but **not a day**. Art. 86 gives an **end-of-month** date for payment of withheld amounts in the same four months. I found no executive-regulation provision fixing the day for Form 4 Salaries.

Confidence on "the month": 96%. On "the day": **55%**. **The safe operational rule is end of the filing month**, aligning with art. 86. Since the payroll system auto-populates and files Form 4 from the monthly forms, the practical risk is low — but a manual filer should not assume the 15th.

## 4.4 Two readings of the Training Fund base

Covered at §3.3. Genuinely ambiguous on the face of the statute; bounded in effect by the floor and cap.

---

# 5. Live-data items — never hard-code

| # | Item | Why | Source |
|---|---|---|---|
| 1 | **CBE credit-and-discount rate announced on 1 January** | Drives the delay fee (Law 91/2005 art. 110, rate + 2%) **and** the refund interest (art. 112, rate − 2%) | Central Bank of Egypt |
| 2 | **Average Treasury bill/bond issuance rate for the preceding month** | Drives the NOSI additional amount (Law 148/2019 art. 121, rate + 2%) | Ministry of Finance / CBE auctions |
| 3 | **Private-sector minimum wage and the periodic-allowance floor** | Changed six times in four years; a 2026 change is pending | National Wages Council via `mped.gov.eg` |
| 4 | **Minimum and maximum contribution wage** | Steps every **1 January** | NOSI announcements |
| 5 | **Per-employee universal-health-insurance flag** | Rollout is phased and expanding | Establishment's UHIA registration |
| 6 | **Public-holiday list** | Ministerial decision, annual | Ministry of Labour |

---

# 6. Contradictions with the pre-existing Egypt payslip artefact

The pipeline contained a prior Egypt payslip-generator workbook (`EG-compliance/06-payslip/build_eg_payslip.py`) built before this research. It was **not** used as an input here. Two of its recorded characteristics **conflict** with what this build established from primary sources, and this pack governs:

1. **"Single-fund NOSI (EE 11% / ER 18.75%, cap 16,700)."** The **totals and the cap are right**, but modelling social insurance as a *single fund* is wrong in a way that will eventually produce a wrong number. Six branches sit behind those totals (§01 CCG §4.3): one of them (**work injury, art. 46(2)**) is **risk-rated from 0.5% up to 1%**, so the employer rate is **not universally 18.75%**; one of them (**the Reward System, art. 36**) is a **savings account, not an insurance premium**; and one of them (**art. 46(1), 1%**) is remitted to the **health-insurance authority, not NOSI**, and **falls away entirely for employees covered by universal health insurance**. A single-fund model cannot express any of that.
2. **"7-bracket income tax."** Article 8 is **not a seven-bracket ladder**. It is a **six-column × seven-rate matrix** with progressive band withdrawal and hard cliffs at 600k / 700k / 800k / 900k / 1.2m (§01 CCG §6.3). A seven-bracket implementation is correct **only** for employees whose annualised net income stays at or below EGP 600,000, and **understates the tax for everyone above it** — by EGP 4,002.50 at the first boundary and by EGP 10,002.75 at the last.

Recommend re-basing that workbook on this pack before it is used again.

---

# 7. What was resolved during the build

Recorded because each cost real effort and each is a trap for the next builder:

1. **The Law 7/2024 gazette PDF is damaged on ETA's own server** (`eta.gov.eg/sites/default/files/2024-03/law_no.7-2024.pdf`) and on `manshurat.org`, which hosts the same file. `pdftotext` fails with *"Couldn't read xref table / Couldn't find trailer dictionary"*. **PyMuPDF opens it by reconstructing the xref** and the text extracts cleanly. Without that recovery, the operative rate table would have had to be reconstructed from the predecessor law plus press summaries — i.e. below floor.
2. **The ETA URL pattern `sites/default/files/YYYY-MM/law_no.N-YYYY.pdf` returns an HTTP-200 HTML 404 page for names that do not exist**, so a naive existence probe reports success. Check the magic bytes, not the status code.
3. **Egyptian gazette PDFs use Arabic Presentation Forms-B ligatures.** `grep` for ordinary Arabic finds nothing until the text is run through `unicodedata.normalize('NFKC', …)` with tatweel and harakat stripped. Every "term not found" result before normalisation is a false negative.
4. **The employee's 11% did not reconcile** against Articles 19, 70 and 86 (which give only 9% + 1%) until **Article 36, the Reward System**, was found in NOSI's own edition of the law — a 1% + 1% mandatory individual savings account in a chapter that is not obviously about contributions. That single article also resolves the employer's 18.75%.
5. **The Article 8 column structure was initially misread** from the Law 175/2023 layout as leaving a gap between EGP 1,000,000 and EGP 1,200,000. Coordinate-clustering the words by x-position, and then reading the Law 7/2024 text where the columns extract cleanly, established that the fifth column is **">900,000 and ≤1,200,000"** and there is no gap. **Never read an RTL matrix from linearised `pdftotext -layout` output alone.**
6. **The 10% under-account withholding is routinely described as a "final tax"** — including in the ETA system's own dropdown label for tax treatment 2, which still reads *"تُحاسب بضريبة قطعية"*. Law 30/2023 **repealed Article 11** (the final-tax provision) and inserted **Article 72 bis** (under account), effective January 2024. The label is a historical artefact; the treatment is not.
7. **Egypt inverts the CEMAC/GCC portal-round-trip default for the tax authority** — ETA publishes a REST endpoint, a JSON payload and an SDK — **but only halfway**: the API uploads a **draft**, and calculation and submission remain portal actions. Both halves matter to a design.

---

# 8. Recommended next actions, in priority order

| # | Action | Closes | Effort |
|---|---|---|---|
| 1 | Obtain an ETA monthly calculation form Excel extract for an employee with `EI070 = 06` and `EI115 = 01` | §3.1, UHI/SI boundary — the highest-value single artefact in this list | Low — any client already on the system has one |
| 2 | Download the live Excel monthly calculation form template | §3.7, the `DTE`/`NAD` pairing | Low |
| 3 | Obtain the **Executive Regulations of Law 148/2019** | §3.6 foreign-worker liability; the art. 46(2) risk-rating table; art. 63 items 1 and 2 behind insurance statuses 24 and 25 | Medium |
| 4 | Obtain the Ministry of Labour's decision on holidays, feasts and occasions | §3.5 | Low |
| 5 | Obtain ETA circular **119/2021** or the 2021 amendment to Law 16/2018 | §3.4 martyrs'-fund scope | Medium |
| 6 | Index the ministerial decisions issued under Law 14/2025 since 1 Sept 2025 | §3.10 payslip content, plus arts. 117, 119, 124, 132 delegations | Medium |
| 7 | Obtain the production API host and credentials from ETA | §3.11 | Low |
| 8 | Obtain Schedule 5 of Law 2/2018 and the phase-activation decrees | §3.2 | Medium |
| 9 | Obtain the gazette text of the amendment introducing the EGP 10,000 insurance-premium cap | The art. 13(3)–(4) cap's instrument | Medium |
| 10 | Set a watch on `mped.gov.eg` for the 2026 private-sector minimum-wage decision | §4.2 | Ongoing |
