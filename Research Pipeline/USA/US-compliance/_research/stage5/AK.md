# Stage 5: AK (Alaska), findings across the 13 domains

Worker: compliance-source-hunter, 2026-11-02 (08:21-08:45 local). Budget declared: 60 fetches / 2 h. Used about 40 fetches, including 3 web searches and 4 Wayback CDX lookups, and about 25 minutes.

- **Shard:** `00-official-sources/_register-shards/S5-AK.csv`, rows US-AKS5-001..018.
  - All 18 rows are `active`.
  - By tier: A.1 x 6, A.2 x 5, A.3 x 7.
  - No tier-B row and no MANUAL row.
- **Sources:** `00-official-sources/ccg-sources/AK/`, 18 files, about 3.86 MB. The largest file is 1.04 MB (TQ01C-26). Pamphlet 100 is reused from `00-official-sources/pdfs/AK/` and is not duplicated (F23).
- **Reused active rows (not re-fetched):**
  - US-AKWT-001/-002 and US-AKP9W-001: no individual income tax and no state withholding.
  - US-AKR3-001..003: no local wage tax.
  - US-AKP51-003, US-AKP52-001, US-AKP7-001/-002: STEP 0.10% and TVEP 0.25% carved out of the employee UI rate.
  - US-AKP51-005: prevailing wage threshold.
  - US-AKP51-006: UI power of attorney.
  - US-AKL-001 and US-AKP9L-001: language and posters.
- **Access finding (2026-11-02).** The VPN was off: `ipinfo.io` showed a Brazilian IP (AS27699).
  - `www.akleg.gov` does not connect (HTTP 000).
  - `public.courts.alaska.gov` does not connect (HTTP 000).
  - The employer pages on `childsupport.alaska.gov` return 404 after the 2025-10 site change.
  - `labor.alaska.gov`, `live.laborstats.alaska.gov` and the `childsupport.alaska.gov` document library work with plain curl.
  - Statutes, bill status and the court form were read from `web.archive.org/web/{ts}id_/` snapshots (2026-02 to 2026-10).

## 1. labour_code
- **Minimum wage** (AS 23.10.065(a) as amended by 2024 Ballot Measure 1, from Pamphlet 100, Oct 2025 [US-AKS5-001, A.1]). Confidence: high.
  - 13.00 USD/h from 2025-07-01.
  - **14.00 from 2026-07-01.** DOLWD Wage and Hour page, updated 2026-05-01, confirms it [US-AKS5-002, A.2].
  - **15.00 from 2027-07-01** (already enacted).
  - After that, the rate is indexed annually to 100% of CPI-U Anchorage. The adjustment is calculated each 30 September for the preceding calendar year, rounded **up** to the next 0.10, and applies 1 Jan-31 Dec. By the text, the first indexed rate takes effect 2028-01-01.
  - Floor: the federal minimum + 2.00. The 2.00 is itself indexed (65(d)). Today that floor is 9.25, so it does not bind.
  - **No tip credit** (65(a)).
  - Public school bus drivers get 2x the minimum: 28.00 from 2026-07-01 (65(b)).
  - No local minimum wage was located. Municipal powers are property and sales tax only [US-AKR3-002]. This is an absence by index, not an express pre-emption.
- **Overtime** (AS 23.10.060) [US-AKS5-001]:
  - 1.5x the regular rate for hours over **8 in a day** and over 40 in a week. Hours already paid as daily overtime are not counted again toward the 40.
  - Exempt from overtime:
    - employers with fewer than 4 employees;
    - agriculture; seamen;
    - hospital medical staff;
    - flight crews;
    - flat-rate mechanics paid at least 2x the minimum;
    - CBA flex plans;
    - a voluntary flex plan (10 h/day, 40 h/week) that is certified and filed with DOLWD;
    - line-haul drivers on a comparable pay system.
- **EAP (white-collar) exemption** (AS 23.10.055(b)) [US-AKS5-001]:
  - The salary must be at least 2x the state minimum wage x 40 h, excluding board and lodging. In Python:
    - 1,040/week until 2026-06-30;
    - **1,120/week from 2026-07-01**;
    - 1,200/week from 2027-07-01.
  - A daily-rate option exists at 300 USD/day or more (8 AAC 15.908).
- **Pay frequency** (AS 23.05.140(a)): monthly or semi-monthly, at the **employee's** election. Monthly pay is allowed by an annual initial contract. Confidence: high.
- **Hire notice** (AS 23.05.160): written notice at hire of the payday, place and rate of pay, and notice of any change by the payday before it takes effect. A posted statement is allowed.
- **Method of payment:**
  - Wages are paid in US money or by a negotiable check payable without discount at an in-state bank (AS 23.10.040).
  - **Direct deposit only if the employee voluntarily authorises it, to the bank of the employee's choice** (AS 23.10.043).
  - No Alaska paycard statute was located (open question AK-OQ-3).
- **Deductions and uniforms:** 8 AAC 15.160(a)-(g) and 15.165 (see domain 9).
- **Records:** keep 3 years at the place of employment (AS 23.10.100). The central in-state office counts as that place (8 AAC 15.900).

## 2. income_tax
- **No individual income tax and no state income-tax withholding** [US-AKWT-001, US-AKWT-002, US-AKP9W-001, A.2]. Confidence: high.
- There is no state W-4 equivalent, no supplemental rate, no withholding return and no state W-2 filing.
- There is no reciprocity agreement. Resident and nonresident rules do not apply.
- **Local:** no local wage, payroll or income tax [US-AKR3-001..003] (MANDATE US-MQ-20 part 2).
- **Oracle:** none for income tax, because there is no wage tax. For UI rates, the DOLWD UI Tax Calculation Cookbook 2026 is the agency's worked example [US-AKS5-006].

## 3. social_security
- **State UI (Employment Security Tax, DOLWD), 2026** [US-AKS5-003, A.2, page re-read with a local file]:
  - **Taxable wage base: 54,200.00** (TQ01C-26 prints the same figure [US-AKS5-013]).
  - **Employee contribution: 0.50%**, deducted by the employer.
  - **Employer rate:** 1.00% for experience classes 01-20 and 5.40% for class 21. Effective 2026-01-01..12-31.
  - **New employer:** 1.00% in every industry (total 1.50%) [US-AKS5-004, A.2].
  - Statutory employer range 1.0%-6.5%, class 21 at least 5.4%. Employee range 0.5%-1.0%.
- **G-DERIVE (done in Python)** [US-AKS5-006, A.2, cookbook last updated 2025-12-04, superseding the 2024-12 edition US-AKP9V-001]:
  - ABCR = (131,477,612 / 45,628,865,425) / (10,852,857,547 / 17,381,530,724) = **0.004615**.
  - Employee rate: 0.27 x ABCR = 0.12%, so the 0.50% floor applies.
  - Reserve rate: 811,365,166 / 17,381,530,724 = 4.668%. That is above 3.3%, so the solvency credit applies, capped at 0.40%.
  - Employer rate: 0.73 x ABCR x factor - 0.004 is at most 0.16%. Classes 1-20 therefore go to the 1.00% floor and class 21 to the 5.40% floor.
  - Every published 2026 rate reproduces.
- **Wage base mechanism:** 75% of the Alaska average annual wage, recalculated each year [US-AKS5-005, A.3].
  - The 54,200 itself is **not** re-derived: the "Tax Base Calculation worksheet" that holds the average annual wage was not obtained (open question AK-OQ-1).
  - The 2027 base is not yet published: `2027-experience-rates.html` returned HTTP 404 on 2026-11-02.
- **STEP 0.10% and TVEP 0.25%** are collected inside the employee 0.50% and credited back, so their net cost is nil [US-AKP52-001, US-AKP51-003, US-AKP7-001/-002].
  - There is no employer STEP tax in 2026. SB 217, which would have added one, was not enacted [US-AKS5-012].
- **SDI/TDI/PFML/LTC/transit:** none. The ES Tax forms index lists no such programme [US-AKP52-002], and the US-OWN-007 levy list has no AK employer levy beyond UI.
- The Alaska Family Leave Act (AS 39.20.500-.550) covers **public** employers only and is unpaid, so it has no payroll levy [US-AKS5-001].
- **Workers' compensation** is an insurer premium outside payroll (DOR Tax Division page [US-AKWT-002]).
- **UI-covered wages differ from FUTA** [US-AKS5-005] (see domain 8).

## 4. payslip_statute
- **8 AAC 15.160(h)**, as amended 2025-09-25 [US-AKS5-001, A.1]. Confidence: high.
- The employer gives a **written or electronic** statement of earnings and deductions **each pay period**, showing:
  - rate of pay;
  - gross wages and net wages;
  - pay-period begin and end dates;
  - federal income tax and FICA deductions;
  - Alaska Employment Security Act contributions;
  - board or lodging deductions; advances;
  - straight-time and overtime hours actually worked;
  - other authorised deductions;
  - **sick leave used in the accrual year**;
  - **sick leave balance**.
- The two sick-leave items are new since 2025-09-25. They correct US-AKP51-004, which read the list only to item 12.
- With a combined PTO plan, showing PTO used and the PTO balance satisfies the two sick-leave items (FAQ Q13 [US-AKS5-010]).
- There is no electronic-consent rule beyond "written or electronic".
- **Retention:** wage and hour records 3 years (AS 23.10.100); UI payroll records 5 years [US-AKS5-005].
- **Language:** no language clause [US-AKL-001].

## 5. reporting_instruments
- **No state withholding return, deposit schedule, annual reconciliation or state W-2 filing**, because there is no wage tax [US-AKWT-001].
- **Quarterly UI report: TQ01C (2/26)** with wage schedule [US-AKS5-013, US-AKS5-005]:
  - Due by the last day of the month after the quarter (Apr 30, Jul 31, Oct 31, Jan 31), and within 10 days of ceasing business.
  - A zero report is required. The minimum late penalty is 10 USD.
  - Wages are reported in the quarter **paid**.
  - Per employee: SSN, name, reportable wages, **occupational code (6- or 8-digit) and 2-digit geographic code**. These are Alaska-specific DD fields.
  - Employer level: monthly counts of workers in the pay period that includes the 12th; excess wages; a "wages reported to other states" Y/N flag.
  - Corrections go on Form TADJ.
- **Channel:** `file_upload`, a CSV with no headings [US-AKS5-014, A.2], or online keying through the ES Tax portal, or paper.
  - Online filing is **mandatory** with 50+ employees in a quarter, 1M+ taxable wages in the current or prior year, or when a payroll agent files [US-AKS5-005].
  - The CSV layout (rev. 2016-05-17): a header record of 11 columns and a wage detail record of 12 columns (see the row).
- **Registration:** online, by mail or in person with UI Tax. Form TREG; the new-employer rate depends on the declared industry. The blue "Notice to Employees" placard must be posted (Form 07-1012) [US-AKS5-015]. Agent access: POA [US-AKP51-006].
- **New-hire reporting** (AS 25.27.075) [US-AKS5-007, A.3]:
  - Report within **20 days** of hire, rehire or return to work.
  - Fields: employee name, address and SSN; employer name, address and FEIN.
  - Channel: online through myAlaska. Fax is no longer accepted.
  - Multistate election goes through HHS.
  - Penalty: 10 USD per employee, 100 USD if conspiracy.
  - The child-support agency is now named **CSED**. Its ACSESS system with a Business Portal went live 2025-10-06 [US-AKS5-008, A.2].
  - The statute text itself was not read (ACCESS gap).

## 6. leave
- **Paid sick leave** (AS 23.10.066-.069, Ballot Measure 1, from 2025-07-01; 8 AAC 15.106-.119, effective 2025-09-25) [US-AKS5-001, A.1; FAQ US-AKS5-010, A.3]. Confidence: high.
  - **Accrual:** 1 h per 30 h worked, overtime included; holidays and vacation not counted.
  - **Cap on accrual and use:** 40 h/yr with fewer than 15 FTE, **56 h/yr with 15+ FTE**. FTE is counted on the prior calendar year (8 AAC 15.106).
  - Exempt (overtime-exempt) employees are assumed to work 40 h/week.
  - **Carry-over** is required, but use stays capped. Front-loading removes carry-over (15.108).
  - **Accrual year:** a 52-week period set by the employer, otherwise the calendar year (15.107).
  - **Pay:** the regular rate (29 CFR 778) or the minimum wage, whichever is greater (15.111).
  - Use is in hourly or payroll-system increments. Foreseeable leave needs at most 10 days' notice. Documentation can be asked only after more than 3 consecutive scheduled workdays.
  - **No payout on separation** (068(a)(1)). A voluntary written cash-out is allowed (15.110).
  - Balances are **reinstated on rehire within 6 months** and carry over to a successor employer.
  - Written notice at hire (068(c), 15.114).
  - Exemptions: see Special populations. A CBA may waive the right in clear terms. Employees under the Railroad Unemployment Insurance Act are exempt.
- **Live change:** HB 161, which would have amended sick leave, is not enacted [US-AKS5-011].
- **PFML benefit side:** no state programme exists.
- **AFLA** (AS 39.20.500): public employers only, unpaid leave [US-AKS5-001].

## 7. termination
- **Final pay** (AS 23.05.140(b)) [US-AKS5-001]. Confidence: high.
  - Discharge by the employer, whatever the cause: within **3 working days**.
  - Resignation: on the next regular payday that is at least 3 days after the employer received notice.
  - Payment is made where the employee is usually paid or at an agreed place.
  - **Penalty:** the regular wage from demand to payment, up to 90 working days. In a department action it is computed on an 8-hour straight-time day (140(d),(e)).
- **Accrued vacation:**
  - No statute requires vacation payout. It follows the employer's policy.
  - Sick leave payout is not required.
  - Accrued vacation pay is a "liquid asset" for garnishment purposes (AS 09.38.030(b)) [US-AKS5-017].
  - Confidence: medium. The DOLWD position on earned vacation as wages was not read (AK-OQ-2).
- **Separation notice:** none to the employee. The only UI duty is the posted Notice to Employees [US-AKS5-015]. DOLWD may require a separation statement on demand (AS 23.20.105, as cited in the handbook [US-AKS5-005]).
- **Return transportation:** AS 23.10.375-.400 and 8 AAC 20.010 require return transport for employees whose transport to the work site was furnished by the employer (in Pamphlet 100, not modelled in detail).
- No state WARN act was located in Pamphlet 100.

## 8. benefits_in_kind
- **Income tax:** not applicable, because there is no state tax.
- **UI wage base: Alaska departs from federal FUTA** (AS 23.20.530; ES Tax Handbook pp. 18-21) [US-AKS5-005, A.3]:
  - **Excluded from UI wages:** employee and employer deferrals to 401(k), 403(b), 457, SEP, SIMPLE, PERS/TRS, an employer-established IRA and Roth 401(k). FUTA, by contrast, taxes 401(k) elective deferrals.
  - **Cafeteria plan:** only group-term life, accident/health, 401(k), disability, FSA and HSA are excluded. **Dependent care, adoption assistance, group legal and cash elections ARE UI wages.**
  - **Other exclusions:** non-required severance, moving reimbursements, accountable per diem, room and board for the employer's convenience, employer payments for retirement, sickness, medical or death plans.
  - **Included:** reported tips, sick pay (unless paid by a third-party fund), vacation pay, bonuses and cash in lieu of benefits.
  - Confidence: medium-high. The guide is A.3; AS 23.20.530 itself could not be read on akleg.
- **Board and lodging credit:** allowed only with prior written notice and the employee's signed acceptance, at reasonable cost without profit. 20 USD/day or less needs no director determination (8 AAC 15.160(d)-(f)).

## 9. deductions_garnishments
- **Wage deductions** (8 AAC 15.160(a)-(g)) [US-AKS5-001]:
  - Allowed only by **written agreement**, and never below the minimum wage or overtime.
  - Never for bad checks or customer theft/default.
  - Never for shortages, lost property or breakage unless the employee admits it in writing or the damage was wilful.
  - Third-party deductions need written direction from the employee, and the employer may take no profit.
  - Uniform deposits are allowed up to the item's cost.
  - Required uniforms or equipment may not be sold to the employee (15.165).
- **Creditor garnishment** (AS 09.38.030) [US-AKS5-017, A.1; CIV-530 (8/24) US-AKS5-009, A.3]:
  - **Exempt:** the greater of **473 USD/week** or 75% of disposable earnings. Monthly pay is divided by 4.3 and semi-monthly pay by 2.17.
  - **743 USD/week** on an affidavit that the debtor's earnings alone support the household.
  - **Nonresident:** the federal 30x minimum wage / 75% rule.
  - **Liquid assets:** 1,890 USD/month.
  - The statute's base amounts (350 / 1,400) are CPI-adjusted by regulation (AS 09.38.115; 8 AAC 95.030 not read).
  - Child support, wage claims, state/local taxes and felony restitution get a reduced exemption.
- **Child support IWO:** 42 U.S.C. 666(b)(6) / CCPA from the FED unit. Remittance goes through the CSED ACSESS Business Portal [US-AKS5-008]. Alaska employer fee and priority rules were not read (AK-OQ-4).
- **State tax levies:** UI contribution collection and the Notice and Order to Withhold and Deliver (ES Tax Handbook p. 35, index only) [US-AKS5-005].

## 10. collective_agreements (prevailing wage)
- **Title 36 public construction over 25,000 USD** [US-AKP51-005]. Rates come from the DOLWD determination (Pamphlet 600).
- **Certified payroll**, Notice of Work and Notice of Completion go to DOLWD LSS. The online system and bulk upload are optional; paper remains allowed [US-AKS5-018, A.3].
- The filing frequency statute was not read (AK-OQ-5).
- The paid sick leave statute lets multiemployer CBA funds satisfy the duty (068(e)).

## 11. indexation
- **Minimum wage:** fixed at 14.00 (2026-07-01) and 15.00 (2027-07-01). From 2028-01-01, CPI-U Anchorage, calculated each 30 September and rounded up to 0.10 [US-AKS5-001]. Derivation: none possible yet; no indexed value has been published.
- **EAP salary threshold and school bus driver rate:** follow the minimum wage (2x) [US-AKS5-001].
- **UI wage base:** 75% of the average annual wage, yearly [US-AKS5-005]. 2026 = 54,200; 2027 not published.
- **UI rates:** ABCR formula, re-derived [US-AKS5-006].
- **Garnishment exemptions:** CPI under AS 09.38.115, set in 8 AAC 95.030 [US-AKS5-017].
- No brackets exist (no income tax).

## 12. data_protection
- **AS 45.48.400-.480** [US-AKS5-016, A.1]:
  - The SSN may not be made available to the public.
  - It may not be printed on mailed material unless law authorises it or the document is an application/enrolment form.
  - Collection and disclosure are allowed for the individual's **employment, including employment benefits**, and where required by law.
- **Pay statement:** 8 AAC 15.160(h) does not require the SSN. A **mailed** statement must not show it. **Recommendation:** omit the SSN or truncate it on every statement.
- **Breach notice:** AS 45.48.010. A no-harm determination needs written notice to the attorney general and 5 years of documentation.
- **Personnel file access:** AS 23.10.430 (in Pamphlet 100).

## 13. live_legal_change (2026-01-01 → 2026-11-02, plus 2027)
- **2026-07-01:** minimum wage 13.00 → 14.00, in force [US-AKS5-002].
- **2027-07-01:** 15.00, enacted [US-AKS5-001].
- **2025-09-25:** 8 AAC 15.106-.119 and 15.160(h) sick-leave regulations, in force [US-AKS5-001].
- **HB 161** (sick leave exemption): referred to (H) L&C on 2025-03-28 and never moved. **Not enacted**; operates at no level [US-AKS5-011].
- **SB 217** (employer contribution for STEP): in (S) FIN since 2026-04-15. **Not enacted**; would have operated at UI employer contribution level [US-AKS5-012].
- **CSED ACSESS** (2025-10-06): a new employer portal for IWO and child-support case actions. Operational/administrative, at employer reporting level [US-AKS5-008].
- 2027 UI wage base and rates: not yet published (404).
- Not swept: the Alaska Administrative Register for 2026 issues, and special sessions of 2026 (see Open questions).

## MULTI hand-offs (answers for AK)
- **SUI wage-base credit:**
  - For an employee transferred to Alaska within the same company, the employer **gets credit for taxable wages paid to another state** in the same calendar year.
  - A successor may combine the predecessor's wages.
  - The TQ01C carries a "wages reported to other states" flag [US-AKS5-005, US-AKS5-013].
  - Localization follows the USDOL guidelines.
- **PFML/SDI coverage of multistate workers:** not applicable (no programme).
- **Paid sick leave for employees working partly in Alaska:** the statute covers "employers in Alaska" and their employees, with no hours-in-state threshold. The FAQ is silent. **Open** (AK-OQ-6).
- **Pay-statement reach:** 8 AAC 15.160(h) applies to employers subject to the Wage and Hour Act. AS 23.10.040 covers "an employer of labor performing services in this state". Inference: the duty attaches to work performed in Alaska. No express out-of-state rule was found.

## Special populations (state rules)
| Population | Alaska rule | register_id |
|---|---|---|
| Domestic/household workers | Exempt from Wage and Hour Act minimum wage, overtime and sick leave (23.10.055(a)(4)). UI-excluded if wages are under 1,000 per quarter | US-AKS5-001, US-AKS5-005 |
| Agricultural | Exempt from minimum wage, overtime and sick leave (055(a)(1), 060(d)(4)). UI-excluded if under 20,000 per quarter or fewer than 10 workers | US-AKS5-001, US-AKS5-005 |
| Commercial fishing / seafood | Fishing crews exempt from the Wage and Hour Act (055(a)(2)) and from sick leave. UI-excluded if fewer than 10 crew paid on shares; processing and tender wages are reportable. Seamen exempt from overtime | US-AKS5-001, US-AKS5-005 |
| Minors | Under 18 part-time (30 h/week or less): exempt from the Wage and Hour Act and sick leave, except in a week over 30 h (8 AAC 15.135). Work permit rules (AS 23.10.332 ff.) not read | US-AKS5-001, US-AKS5-010 |
| Tipped employees | **No tip credit.** The full 14.00 is due in cash. The employer may not keep tips except to pass on card tips or run tip pools (8 AAC 15.907) | US-AKS5-001 |
| Clergy / religious | Ministers and members of religious orders and church service are UI-excluded. Volunteers of nonprofit religious organisations are exempt from the Wage and Hour Act | US-AKS5-005, US-AKS5-001 |
| Students | Enrolled students working at their school are UI-excluded. Work-study students under 22 are UI-excluded. Student learners: minimum wage exemption by DOLWD certificate (8 AAC 15.125). University of Alaska practicum is exempt | US-AKS5-005, US-AKS5-001 |
| Nonresident aliens | No state rule beyond federal (no state income tax) | US-AKWT-001 |
| Statutory employees / officers | Corporate executive officers are UI-excluded unless the employer elects coverage (all officers as a group). Commission insurance, real estate and stock agents are UI-excluded when also excluded from FUTA | US-AKS5-005 |
| Government employees | Exempt from the Wage and Hour Act minimum wage and overtime and from sick leave (055(a)(5)). State and political subdivisions are UI employers (contributory or reimbursable). AFLA unpaid family leave applies to public employers | US-AKS5-001, US-AKS5-005 |
| Nonprofit | UI applies at 250 USD per quarter or 4+ employees in 20 weeks. Reimbursable method available. Summer camp: reduced wage of up to 12 weeks, and exempt from sick leave | US-AKS5-005, US-AKS5-001 |
| Line-haul truck drivers / mechanics / auto sales | Alternative overtime systems; motor vehicle dealer sales and service staff exempt from the Wage and Hour Act (055(a)(18)) | US-AKS5-001 |

## ACCESS gaps (exact URLs, 2026-11-02, BR IP, VPN off)
- `https://www.akleg.gov/basis/statutes.asp?media=print&secStart=23.10.065&secEnd=23.10.065`: HTTP 000 (no connection). The whole host is affected.
  - The Wayback `2026id_` copy of `...secStart=23.20.175&secEnd=23.20.175` returned 404.
  - CDX holds no snapshot of AS 23.20, AS 25.27 or AS 36.05.
  - Effect: these statutes are unread: AS 23.20.175 (wage base), AS 23.20.530 (wages), AS 25.27.075 (new hire), AS 36.05.040 (certified payroll).
- `https://public.courts.alaska.gov/web/forms/docs/civ-530.pdf`: HTTP 000. Read from the Wayback copy dated 20260210203536.
- `https://childsupport.alaska.gov/child-support-enforcement/employers/new-hire-wage-withholding`: HTTP 404. The `child-support-services/...` path redirects (301) to it, and `.../letter-to-alaskan-employers` is also 404. The Wayback `2026id_` copy is also 404.
- 8 AAC 95.030 (garnishment amounts) and 8 AAC 85 (ES Tax regulations) on `akleg.gov/basis/aac.asp`: not attempted, because the host is unreachable.
- `https://labor.alaska.gov/estax/2027-experience-rates.html`: HTTP 404. This is a timing gap (2027 not yet published), not an access block.

## Open questions
- **AK-OQ-1.** 2026 wage base 54,200: derivation from the average annual wage x 75%. What would close it: the DOLWD "Tax Base Calculation worksheet" for 2026 (Research and Analysis Section, live.laborstats.alaska.gov), or the signed "AK UI Tax Rates 2026 Full Document" (signed 2026-01-21, attached to SB 217 on BASIS).
- **AK-OQ-2.** Earned vacation on separation. Is unused accrued vacation "wages" due under AS 23.05.140(b) absent a forfeiture policy? What would close it: the DOLWD Wage and Hour position (Pamphlet 100 index or the Wage and Hour FAQ), or Alaska Supreme Court case law read on an official host.
- **AK-OQ-3.** Paycards: no statute located. AS 23.10.040 requires money or a negotiable check, and AS 23.10.043 requires voluntary authorisation for a deposit. What would close it: a DOLWD Wage and Hour opinion on payroll cards.
- **AK-OQ-4.** Alaska IWO specifics (employer administrative fee, priority, remittance deadline) under AS 25.27.062. What would close it: the statute through VPN/akleg, or the CSED Business Portal employer guide.
- **AK-OQ-5.** Certified payroll frequency and form under AS 36.05.040, and the Pamphlet 600 edition in force. What would close it: AS 36.05.040 on akleg, and the current Pamphlet 600 (labor.alaska.gov/lss).
- **AK-OQ-6.** Paid sick leave coverage of employees who work partly in Alaska (or remote workers of Alaska employers). What would close it: a DOLWD LSS interpretation; the FAQ updated 2026-01-28 is silent.
- **AK-OQ-7.** Bulletin sweep: not done for the Alaska Administrative Register (8 AAC amendments in 2026) or for any 2026 special session. What would close it: the Lt. Governor's Online Public Notices / Administrative Register issues 2026-01..10, and the BASIS "Passed Legislation" list of the 34th Legislature (both need akleg/VPN).

## Confidence
| Domain | Confidence |
|---|---|
| labour_code | 95% |
| income_tax / local (none) | 98% |
| social_security (SUI rates derived) | 95% (wage base itself not derived) |
| payslip | 95% |
| reporting (TQ01C and CSV inspected) | 90% |
| leave | 95% |
| termination | 85% (vacation open) |
| benefits_in_kind (UI wage definition from an A.3 guide) | 80% |
| deductions/garnishment (amounts from the 2024 court form) | 85% |
| prevailing wage | 75% |
| indexation | 90% |
| data protection | 85% |
| live change | 80% (Admin Register not swept) |
| **Overall** | **about 88%** |
