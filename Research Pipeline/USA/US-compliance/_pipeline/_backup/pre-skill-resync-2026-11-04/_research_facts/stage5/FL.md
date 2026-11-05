# Stage 5 — FL (Florida) — findings for the 13 domains

Worker: compliance-source-hunter, 2026-11-02, 07:10-07:35. Budget declared: 60 fetches and 2 h. Used: about 44 fetches (curl, plus 3 web searches used only as leads) and about 30 minutes.
Shard: `00-official-sources/_register-shards/S5-FL.csv` (US-FLS5-001..027, 27 rows). Tiers: A.1 x17, A.2 x9, A.3 x1. No MANUAL rows.
Sources: `00-official-sources/ccg-sources/FL/` (about 5.7 MB). It holds 17 statute pages (2026 Florida Statutes, flsenate.gov), the Florida Constitution page, 6 DOR pages/PDFs, the import spec PDF and the RT XML package zip (2.0 MB, kept as an archive, not expanded).

**Edition note.** flsenate.gov already publishes the **2026 Florida Statutes**. Every statute row in this shard cites the 2026 edition. The earlier rows cite the 2025 edition: US-FL-003, US-FL-P5-2-*, US-FLL-*. Read against the 2026 text, their content still holds.

Florida is a T1 jurisdiction. It has no wage tax at any level, so payroll obligations reduce to these:
- minimum wage;
- reemployment tax, which is employer-only;
- new-hire reporting;
- E-Verify certification;
- garnishment and child-support rules.

## 1 — labour_code
- **Minimum wage.** Fla. Const. Art. X s.24(c) sets USD 10.00 from 2021-09-30, plus USD 1.00 each 30 September until USD 15.00 on 2026-09-30.
  - **USD 14.00:** 2025-09-30 to 2026-09-29.
  - **USD 15.00:** from 2026-09-30.
  - **Next change:** the first CPI-W adjustment is calculated on 2027-09-30 and takes effect 2028-01-01. Art. X s.24(c) says each adjusted rate is "published and take effect on the following January 1st". So **there is no change on 2027-09-30 and no 2027 rate**: USD 15.00 runs through 2027-12-31.
  - [US-FLS5-001, A.1, high]
- **Scope trap: Fla. Stat. 448.110 is stale.** The 2026 text still says USD 6.15, with a January CPI-W South indexation. Both are overridden by the 2020 constitutional amendment.
  - 448.110 still controls coverage: only FLSA-covered individuals are entitled to the state minimum wage, and FLSA ss.13-14 exemptions apply.
  - DOR and FloridaCommerce must post the new rate by 15 October each year, and FloridaCommerce mails a notice to employers by 15 November.
  - Before suing for unpaid minimum wage, the employee must give 15 days' written notice.
  - [US-FLS5-002, A.1]
- **Tipped employees.** The credit is capped at the FLSA tip credit allowable in 2003, which is USD 3.02 (5.15 − 2.13; G-DERIVE, computed in Python).
  - **Tipped cash wage:** USD 10.98 (from 2025-09-30), then **USD 11.98 from 2026-09-30**.
  - The 2003 inputs (USD 5.15 minimum wage, USD 2.13 cash wage under 29 U.S.C. 203(m)) are federal facts carried by the FED unit.
  - Tier-B sites (vendors, news) give the same 11.98. They are leads only.
  - [US-FLS5-001, derived arithmetically]
- **Local minimum wages:** none for private employers. Fla. Stat. 218.077(2), as amended by ch. 2024-80, bars political subdivisions from setting a minimum wage other than the state or federal one. It also bars them from mandating employment benefits, including sick leave, vacation and holidays, and from controlling contractor wages through procurement.
  - Exceptions: their own employees, and employers that receive a direct tax abatement or subsidy.
  - Ch. 2024-80 does not impair contracts entered before 2026-09-30.
  - [US-FLS5-009, A.1, high]
- **Overtime:** none beyond the FLSA, except Fla. Stat. 448.01. For manual labor, 10 hours is a legal day's work unless a written contract says otherwise; without such a contract, "extra pay" is due beyond 10 hours a day. No premium rate is fixed. [US-FLS5-027, A.1, high]
- **Pay frequency, payday timing and method of payment:** no Florida statute. The ch. 448 section list has no wage-payment section [US-FLP52-004]. Federal rules apply. The direct-deposit and paycard rules are federal (Reg. E), in the FED unit. Confidence medium-high: this is a negative finding from the chapter list, not a full-text keyword scan of every title.
- **E-Verify.**
  - Every employer verifies each new hire within 3 business days.
  - Private employers with 25+ employees, and all public agencies, must use E-Verify (from 2023-07-01).
  - Each must certify compliance on its **first reemployment tax return of each calendar year**, or on Form RT-E Verify.
  - [US-FLS5-010, A.1; US-FLS5-019, A.2]
- **Minors:** hours limits are in 450.081; they are listed under special populations below [US-FLS5-011]. Florida law has no sub-minimum wage for minors.

## 2 — income_tax
- **No state income tax on natural persons.** Fla. Const. Art. VII s.5(a) [US-FL-001, A.1]. DOR's list of taxes has no personal income or withholding tax [US-FL-002, US-FLL-003, A.2]. The constitution page was re-read on 2026-11-02 (local file `FL_constitution_2026-11-02.html`).
- **Not applicable:** state withholding method, state W-4, supplemental rate, rounding, state W-2, reciprocity, and resident/nonresident rules.
- **Local income taxes:** none. The DOR tax list names no local wage tax [US-FLL-003].
- **Multistate.** A Florida resident working in another state is withheld under that state's rules, and some states penalise non-withholding where the residence state has no tax (e.g. LA RR 08-004, SC RR 22-3). This belongs to the MULTI unit.

## 3 — social_security (reemployment tax; no SDI/PFML)
- **Agencies.** DOR is the tax collection service provider: it registers employers, collects reports, assigns rates and audits. FloridaCommerce runs benefits. [US-FLS5-019, A.2]
- **Wage base: USD 7,000** per employee per employer per calendar year, since 2015-01-01. It is fixed in statute and not indexed.
  - Successor employers may count the predecessor's wages.
  - Out-of-state wages for the same employee are credited through RT-6NF.
  - [US-FLS5-003 A.1; US-FLS5-020 A.3; second independent document: US-FLS5-018]
- **Rates.**
  - **2026 range:** minimum 0.1% (USD 7 per employee), maximum 5.4% (USD 378). [US-FLS5-018, A.2, G-DERIVE: 7000 × 0.001 = 7; 7000 × 0.054 = 378]
  - **New employer:** 2.7%. The statute applies it while the account has been chargeable for fewer than 8 quarters. DOR says "until the employer has reported for 10 quarters", because eligibility for a variation needs 12 consecutive chargeable quarters ending 30 June of the prior year.
  - **Standard rate:** 5.4%.
  - **Floor:** 0.1%.
  - **Ceiling:** 5.4%, plus 1 point for short-time-compensation employers.
  - **Rounding:** a contribution fraction under half a cent is dropped; half a cent or more rounds up to 1 cent.
  - [US-FLS5-004, A.1; US-FLS5-018, A.2]
- **Employee contribution: none.** An employer may not deduct contributions from wages (443.131(1)). The RT-83 poster restates this [US-FLS5-004, US-FLS5-026].
- **Liability threshold:** USD 1,500 in a quarter, or 1 employee in 20 weeks, or FUTA liability; for domestic employers, USD 1,000 in a quarter [US-FLS5-020, US-FLS5-005].
- **Coverage and exemptions (443.1216):** listed in the special-populations table. Corporate officers are covered. Employee-leasing workers are reported under the leasing company's account. [US-FLS5-005, A.1]
- **SDI / TDI / PFML / long-term care / transit levies: none.** Title XXXI has no such chapter [US-FLP52-001]. Workers' compensation is employer-funded, and an employee contribution is void (440.21) [US-FLP52-002]. The P7/P9 levy list is not redone here.

## 4 — payslip_statute
- **No general Florida pay-statement statute.** The only one is for labor pools: 448.24(2)(g) requires an itemised statement of deductions at each payment (electronic on request), and (2)(h) an annual earnings summary by 1 February [US-FLL-002, US-FLP52-004, A.1]. For every other employer, federal records rules apply.
- **Electronic delivery and retention:** no Florida rule found.
- **Required postings with payroll content:** RT-83 "To Employees" (R. 10/26, current; Spanish version RT-83SP) under 443.151(1) [US-FLS5-026, US-FLS5-007]; the minimum-wage poster in English and Spanish under 448.109 [US-FLL-001].
- **Language:** English (US-OWN-006).

## 5 — reporting_instruments
- **Withholding return, deposit schedule, annual reconciliation, state W-2:** not applicable, because there is no income tax [US-FL-001]. There is no state W-2 filing.
- **Quarterly UI report: RT-6 (R. 07/23, on Rule 73B-10.037 F.A.C.).**
  - **Due dates:** 30 April, 31 July, 31 October, 31 January, moved to the next business day when the date falls on a weekend or holiday. A report is required even when no tax is due.
  - **Electronic payment** must be initiated by 5 pm ET on the business day before the due date.
  - **Lines:**
    - Line 1: covered employees in the pay period that includes the 12th of each month.
    - Line 2: gross wages.
    - Line 3: excess wages over USD 7,000.
    - Line 4: taxable wages.
    - Line 5: tax.
  - **Wage detail:** name, SSN and gross/taxable wages per employee.
  - **Corrections:** on RT-8A.
  - [US-FLS5-021, US-FLS5-020, A.2/A.3]
- **Electronic mandate.** Employers with 10+ employees in any quarter of the prior state fiscal year (July-June) must e-file and e-pay.
  - Non-electronic report: USD 25 + USD 1 per employee, max USD 300.
  - Non-electronic remittance: USD 25 each.
  - Erroneous or incomplete report, including a bad SSN: the greater of USD 50 or 10% of tax, max USD 300, waivable once in 12 months.
  - An ITIN is not accepted in place of an SSN.
  - [US-FLS5-006 A.1; US-FLS5-024 A.2]
- **Channel: `file_upload` (fixed-length text) or `xml`.** The prior register said the RT-6 layout was not obtained [US-FIL-015]; it is now obtained.
  - **Flat File Web Import, Version 7 (Dec 2023).**
    - Fixed-length text with record types 00 Header (FEIN, RT account), 01 Employer, 02 Employee (optional for RT-6, required for RT-8A), 03 Totals (monthly counts) and 99 Trailer.
    - Currency fields have 2 implied decimals; numeric fields are zero-padded; zip files are refused.
    - Files with 8,000+ records should be sent in the first two weeks of the due month.
    - [US-FLS5-022, A.2, inspected]
  - **XML package `FL_RT_XML_Schemas_v2026 1.0`.**
    - Contents: 9 XSD, a guide, XPath, samples and 4 test cases. It uses the IRS efile Transmission envelope.
    - It is **required above 20,000 employee records**.
    - The header has an optional E-Verify certification block.
    - **G-SPOT:** the archive was extracted and `RT-6 Sample.xml` validates against `RT_FLTransmission.xsd` (lxml: True).
    - [US-FLS5-023, A.2, inspected]
- **Other quarterly forms:** BLS-3020 (Multiple Worksite Report) for multi-location employers; RT-6EW for staff contracted to public or nonprofit educational institutions; RT-6NF for out-of-state taxable wages; RT-7 annual report for domestic-only employers, due 1 January and late after 31 January [US-FLS5-020, US-FLS5-004].
- **New-hire reporting** (State Directory of New Hires, DOR) [US-FLS5-008, A.1]:
  - **Deadline:** within 20 days of the hire date, which is the first day of work for which pay is owed. Electronic filers may instead send two monthly transmissions 12-16 days apart.
  - **Fields:** employee name, address, SSN and date of hire; employer name, address and FEIN; date of birth optional.
  - **Multistate employers** may designate one state.
  - **Florida also requires reporting of non-employees** paid USD 600+ in a year, within 20 days. This is a scope item for the DD and RSPEC.
- **Registration:** online at floridarevenue.com/taxes/registration (DR-1) before the first RT-6 [US-FLS5-021, US-FLS5-020].
- **Third-party filing:** DR-835 power of attorney; Section 4 covers the RT agent; RTS-9 is the agent registration [US-FL-005].

## 6 — leave
- **Paid sick leave: none at state level, and local mandates are preempted** (218.077(1)(d), (2)(a)) [US-FLS5-009].
- **PFML:** none [US-FLP52-001].
- **Domestic or sexual violence leave:**
  - Applies to employers with 50+ employees, for employees with 3+ months of service.
  - Up to 3 working days in any 12 months, paid or unpaid at the employer's choice.
  - The employee must first use annual/vacation, personal and sick leave unless the employer waives this.
  - [US-FLS5-014, A.1]
- **Jury service:** protected from dismissal; no statutory pay duty [US-FLS5-015, A.1].
- **Vacation:** no statute. Policy or contract governs.

## 7 — termination
- **Final-pay timing:** no Florida statute. The ch. 448 section list has none. FLSA payday rules apply.
- **Accrued vacation payout:** no statute. The employer's policy or contract governs.
- **Recovery:** in a wage action the prevailing party may get attorney's fees (448.08) [US-FLS5-016, US-FLP52-004, A.1, medium-high: negative finding].
- **Separation notice:** 443.151(1) makes the employer post the benefit-rights statements and supply claim materials "as directed by the rules". Whether a FloridaCommerce rule requires a separation form was **not read** (open question) [US-FLS5-007].
- **State WARN law:** none in Title XXXI [US-FLP52-001].

## 8 — benefits_in_kind
- **Income tax:** no state tax, so federal exclusions are not modified for state purposes.
- **UI wage definition (443.1217(2)(b)-(g)):**
  - **Excluded:** employer plan payments for sickness or accident disability (workers' comp only), medical/hospital and death benefits; sick pay more than 6 months after separation; employee FICA paid by the employer; convenience-of-employer meals and lodging; payments to or from 401(a) trusts, 403(a) and SEP plans, 403(b) other than salary-reduction contributions, and 3121(v)(3) plans; cafeteria plan payments where s.125 applies; IRC 127 educational assistance.
  - **Taxable:** personal-use cars, non-convenience meals and lodging, group legal, golden parachutes, excess discounts, below-market loan interest, and reported tips.
  - [US-FLS5-003, US-FLS5-020]
- **Open question:** treatment of 401(k) elective deferrals for UI. FUTA adds them back to wages under 3306(r). The Florida text excludes "payments to a trust described in s.401(a)" and carves out salary reduction only for 403(b). The DOR guide does not mention 401(k).

## 9 — deductions_garnishments
- **Wage-deduction authorisation:** no general Florida statute. Reemployment contributions may never be deducted (443.131(1)), and workers' comp premiums may not be charged to the employee (440.21) [US-FLS5-004, US-FLP52-002].
- **Creditor garnishment (222.11).**
  - **Head of family** (provides more than half the support of a child or dependent): disposable earnings up to USD 750 a week are fully exempt. Above USD 750 a week, nothing may be garnished unless the employee signed a separate written waiver, and then only up to the CCPA limit.
  - **Others:** the CCPA limit (15 U.S.C. 1673).
  - The USD 750 is not indexed.
  - [US-FLS5-012, A.1]
- **Child support income deduction (61.1301).**
  - Employer fee: up to USD 5 for the first deduction and USD 2 for each one after, inside the CCPA 1673(b) limit.
  - Start no later than the first pay date more than 14 days after service.
  - Remit within 2 days after each pay date.
  - Arrears: an additional 20% or more.
  - Priority over all other state legal processes; multiple orders are prorated with priority to current support.
  - The employer must notify termination; penalty USD 250 / 500.
  - Discharge because of the deduction is prohibited.
  - [US-FLS5-013, A.1]
- **State tax levies:** not applicable to wages, because there is no income tax. A DOR levy for reemployment-tax debt is not covered here.

## 10 — collective_agreements (prevailing wage)
- **No statewide prevailing wage.** Ch. 255 was scanned in full [US-FLP52-003]. Since ch. 2024-80, local governments may not control contractor wages through procurement (218.077(2)(b)-(c)) [US-FLS5-009]. Federal Davis-Bacon certified payroll applies on federal jobs (FED unit). Confidence high.

## 11 — indexation
- **Minimum wage:** fixed steps to USD 15.00 (2026-09-30). The first CPI-W indexation is calculated 2027-09-30 and effective 2028-01-01; it is published on the FloridaCommerce and DOR home pages [US-FLS5-001, US-FLS5-002].
  - **Derivation line:** 10.00 (2021) → 11 → 12 → 13 → 14.00 (2025-09-30) → 15.00 (2026-09-30).
  - **Tipped wage:** minimum wage − 3.02 = 11.98.
- **UI wage base:** USD 7,000, statutory and not indexed.
- **UI rates:** recomputed every year on experience; DOR mails Form RT-20 each year.
- **Garnishment USD 750 a week:** not indexed.

## 12 — data_protection
- **501.171.** Personal information includes name + SSN and financial account numbers.
  - Covered entities must take reasonable measures to protect it.
  - A breach affecting 500+ Floridians is notified to the Department of Legal Affairs within 30 days (+15 days for good cause).
  - Records are disposed of securely.
  - [US-FLS5-017, A.1]
- **SSN truncation on pay statements:** no Florida statute located.
- **SSNs held by DOR** are confidential (ss. 213.053, 119.071, cited in RT-800002) [US-FLS5-020].

## 13 — live_legal_change (2026-01-01 to 2026-11-02)
- **2026-09-30:** the minimum wage rose to USD 15.00, tipped to USD 11.98 [US-FLS5-001].
- **2026 Statutes check.** The history lines of all 17 sections fetched were read. Only **501.171** was amended in the 2026 session (s. 9, **ch. 2026-52**). Its substance was not read; it may be conforming only (open question).
  - **443.131** history ends with a ch. 2025 amendment, already in the 2026 text read.
  - No 2026 change was found to 443.1216, 443.1217, 443.163, 409.2576, 448.110, 448.095, 450.081, 222.11 or 61.1301.
- **2026-01-01:** UI rates published (min 0.1%, max 5.4%) [US-FLS5-018].
- **RT XML schema v2026 1.0 is current**; `RT_changes.xlsx` in the package lists the changes and was not read [US-FLS5-023].
- **RT-83 poster revised R. 10/26** [US-FLS5-026].
- **2027:** no minimum-wage change in 2027. No 2027 UI rates are published yet; they come with the RT-20 notices in December/January.
- **Not done:** a full bulletin sweep of Laws of Florida 2026 and DOR Tax Information Publications was not run within this budget.

## Special populations (US-OWN-005, state round)
| Population | Florida rule | register_id |
|---|---|---|
| Domestic / household | UI covered if USD 1,000 cash in a quarter (443.1216(6)); otherwise exempt (13)(a). Domestic-only employers may report and pay annually (RT-7, due 1 Jan, late after 31 Jan; apply by 1 Dec). Minor hours limits do not apply to minors in domestic service in private homes. E-Verify: casual labor in a private residence is not "employee" for 448.095 | US-FLS5-005, US-FLS5-004, US-FLS5-020, US-FLS5-011, US-FLS5-010 |
| Agricultural | UI covered if USD 10,000 cash in a quarter or 5+ workers in 20 weeks (443.1216(5)); crew-leader rules in (5)(b) | US-FLS5-005 |
| Minors | Hours limits in 450.081 (15 and under: 3 h on school days, 15 h/week; 16-17: 8 h, 30 h/week in session, waivable); exemptions for graduates, home or virtual education, children of the employer; no sub-minimum wage. Newspaper delivery under 18 is exempt from UI | US-FLS5-011, US-FLS5-005 |
| Tipped employees | Credit capped at USD 3.02; cash wage USD 11.98 from 2026-09-30. UI: tips reported under IRC 6053(a), or used to meet minimum wage, are wages | US-FLS5-001, US-FLS5-020, US-FLS5-021 |
| Clergy / religious | Churches, church-controlled organisations, ministers and members of religious orders are exempt from UI (443.1216(13)). Other 501(c)(3) nonprofits are covered with 4+ workers in 20 weeks | US-FLS5-005, US-FLS5-020 |
| Students | Students employed by their own school are exempt from UI; co-op students working for credit, student nurses and interns are exempt; F/J nonimmigrants doing purpose-related work are exempt | US-FLS5-005, US-FLS5-020, US-FLS5-025 |
| Nonresident aliens | No state income tax. UI: wages of non-citizens are taxable like citizens' wages, except F/J under 443.1216(13)(v); an ITIN is not valid on the RT-6 | US-FLS5-025, US-FLS5-024 |
| Statutory employees | Agent-drivers and commission-drivers, and full-time traveling or city salespersons, are UI-covered under the 443.1216(1)(a)3-4 conditions. Solely-commissioned insurance agents, real-estate salespersons (and barbers, per DOR) are exempt | US-FLS5-005, US-FLS5-020 |
| Government employees | UI covers public employers, except elected officials, legislators, judiciary, temporary emergency staff and major policymaking posts (443.1216(2), (13)). Public agencies must use E-Verify. Political subdivisions may set their own employees' minimum wage and benefits (218.077(3)) | US-FLS5-005, US-FLS5-010, US-FLS5-009 |
| Corporate officers / family | Corporate officers are UI-covered. Family employment (spouse, son/daughter; a child under 21 working for a parent) is exempt, but not in corporations | US-FLS5-005, US-FLS5-020 |
| Labor pools (day labor) | Itemised statement of deductions at each payment; annual earnings summary by 1 Feb (448.24) | US-FLL-002 |

## Oracle
- **Florida has no withholding calculator, because there is no wage tax.** The UI computation is Line 4 × rate with half-cent rounding.
- **Worked examples:**
  - RT-800002 p.9: successor wages; New York to Florida transfer.
  - The 4 RT XML test cases (Test 1-3 RT-6, Test 4 RT-8A).
  - [US-FLS5-020, US-FLS5-023]

## Extraction note (corpus)
- **`FL_DOR_flRtXmlPkg_2026-11-02.zip`** (2,020,533 bytes) holds 20 files: 9 XSD, a guide PDF, an XPath xlsx, 4 samples, 4 test PDFs and RT_changes.xlsx.
  - It was extracted to scratch only, to verify the schema and validate the RT-6 sample.
  - Nothing extracted was kept in the corpus, and the archive stays whole.
- **Total FL folder:** about 5.7 MB. No single file is over 5 MB.

## ACCESS gaps
- `https://www.floridajobs.org/business-growth-and-partnerships/for-employers/display-posters-and-required-notices/minimum-wage`: HTTP 403 by curl. The Wayback copy `https://web.archive.org/web/2026id_/<same>` returns 404. The FloridaCommerce 2026 minimum-wage notice/poster (USD 15.00 / USD 11.98) is therefore not read on an official host.
  - The figures rest on the Constitution (A.1) plus derivation. One browser read would close the second-authority check.
- FloridaCommerce rules (F.A.C. 73B-10) on separation notices and the text of Rule 73B-10.037: not fetched (budget).

## Open questions
1. **ui.wage.exclusion.401k_deferral:** are 401(k) elective deferrals reemployment-taxable in Florida? The 443.1217(2)(f) text is ambiguous against FUTA 3306(r). This would close it: a DOR TIP, or an answer from DOR e-vendor or the Reemployment Tax FAQ.
2. **termination.separation_notice:** does a FloridaCommerce rule require a separation notice or form at termination? This would close it: Rule chapter 73B-10/73B-11 F.A.C. (flrules.org).
3. **live.501_171.ch2026_52:** what did ch. 2026-52 change in 501.171? This would close it: Laws of Florida ch. 2026-52 (laws.flrules.org).
4. **minwage.tipped.cash:** confirm USD 11.98 on the FloridaCommerce 2026 poster (ACCESS gap above). The figure is derived from A.1, so the risk is low.
5. **rt.xml.changes_2026:** read `RT_changes.xlsx` inside the XML package for the 2026 schema changes (stage 3 / RSPEC).
6. **live.bulletin_sweep:** a full sweep of Laws of Florida 2026 and DOR TIPs 2026 for reemployment, new hire and garnishment items is still open for the synthesis or the browser pass.
