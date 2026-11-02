# Stage 5 — UT (Utah): findings by domain

Worker: compliance-source-hunter, 2026-11-02. Budget declared: 60 fetches and 2 h. Used about 46 network calls, including access probes, Wayback CDX lookups and blocked attempts. Fetching stopped at the 75% mark. Wall clock was about 1 h.
- **Shard:** `00-official-sources/_register-shards/S5-UT.csv` (US-UTS5-001..016, 16 rows).
- **New sources:** `00-official-sources/ccg-sources/UT/` (16 files, about 3.7 MB; largest is the R865-9I rule HTML, 1.16 MB).
- **Earlier UT files:** they stay in `00-official-sources/pdfs/UT/` and are cited through their existing active rows. Pub 14 Rev. 04/26 (US-UT-PIT-003) and the DWS Tax Rates page (US-UT-SUI-001 / US-UT-P5-1-003) were re-read locally, not re-fetched.

**Access picture (2026-11-02).** The VPN was off (exit IP in BR), so every Utah host was tested from that network.
- **Utah hosts that refuse or time out:**
  - `tax.utah.gov`, `jobs.utah.gov`, `laborcommission.utah.gov` and `tap.utah.gov` return 403.
  - `le.utah.gov` times out.
- **Utah hosts that answer plain curl:**
  - `adminrules.utah.gov` answers through its JSON API:
    - search: `POST /api/search` with `{"searchTerm":"R610-1","ruleTypeId":51}`;
    - version metadata: `POST /api/ruleVersion` with `{"ruleTypeId":51,"versionIds":[…]}`;
    - rule file: `GET /api/ruleVersionFile/{versionId}/file/{htmlName}`, which returns base64 HTML.
  - `ors.utah.gov` also answers.
  - **This is a reusable access route for every state unit that needs Utah admin rules.**
- **Statutes from le.utah.gov:** read only through Wayback. Each section page is a wrapper whose `versionDefault` names the version file. Only some version files are archived.
- **Federal hosts:** `www.dol.gov` answers. `acf.gov` returns 202 (bot challenge).

## 1 — labour_code
- **Minimum wage: 7.25 USD/h**, unchanged since 2009-07-24 [US-UTS5-011, A.1, high; DOL second authority US-UTS5-007, A.2].
  - Utah Code 34-40-103(2)(b) bars the Labor Commission from setting a state rate above the federal FLSA minimum. The Commission must review the rate at least every 3 years and whenever the federal rate changes [US-UTS5-010, A.1].
  - 2027: no change enacted. The rate can move only if the federal minimum moves.
  - DOL notes that the state law excludes any employment subject to the FLSA [US-UTS5-007].
- **Local minimum wages:** none possible. The statutory cap above leaves no local power to exceed the federal rate. I found no Utah local-rate ordinance. Confidence medium: the 34-40 local-preemption section was not read.
- **Minors:** at least 4.25/h for the first 90 days with an employer, then 7.25 [R610-1-3(B), US-UTS5-011].
- **Overtime:** there is no Utah overtime statute or rule. R610-1 has no premium-pay rule, and DOL lists no Utah premium-pay entry [US-UTS5-007]. Overtime follows the FLSA. Confidence medium-high.
- **Hours worked:** "hours employed" includes on-call time on the premises, meetings, training and rest breaks. Meal periods of 30 minutes or more with full relief are excluded [R610-1-2(B)].
- **Pay frequency** [Utah Code 34-28-3(1), US-UTP6-001, A.1]:
  - Pay at least semimonthly, within 10 days after the pay period closes.
  - Employees on a yearly salary may be paid monthly, on or before the 7th of the following month.
  - DOL corroborates this [US-UTS5-009].
- **Method of payment:**
  - Pay cards are allowed if three conditions are all met: one fee-free withdrawal of the full wages; full pay available on payday; and a statement of deductions every payday, on paper or electronically (easily and immediately accessible and printable at no cost) [R610-3-22, US-UTS5-012, A.1].
  - The direct-deposit consent rule was not read: 34-28-3 was read only in its 2014 version, and 34-28-2/-3 in the current version are not archived. See Open questions.

## 2 — income_tax
- **Rate: flat 4.45%** of state taxable income for taxable years from 2026-01-01. Utah Code 59-10-104, amended by Ch. 250, 2026 General Session; the version heading reads "Effective 1/1/2026" [US-UTS5-001, A.1, high].
  - This replaces tier-B US-UT-PIT-004 as the rate source. The 2025 rate was 4.5% according to tier-B only.
- **Withholding method:** Pub 14 Rev. 04/26 [US-UT-PIT-003, A.2, high; already registered and read locally].
  - There is no Utah W-4. Filing status comes from the federal W-4. Allowances and federal adjustments are ignored. Utah taxable wages are the wages subject to federal withholding (IRC 3401(a)).
  - The rules say the same thing in R865-9I-14(E)-(G) [US-UTS5-013, A.1].
  - Formula per pay period, with all lines rounded to whole dollars:
    - line 2 = wages × 4.45%;
    - line 6 = max(0, base allowance − 1.3% × max(0, wages − threshold));
    - withholding = max(0, line 2 − line 6).
  - **Annual parameters:**

    | Filing status | Base allowance | Phase-out threshold |
    |---|---|---|
    | Single (also head-of-household) | 485 | 9,348 |
    | Married | 970 | 18,696 |

  - **Per-period parameters (single / married):**

    | Pay period | Base allowance | Threshold |
    |---|---|---|
    | Weekly | 9 / 19 | 180 / 360 |
    | Biweekly | 19 / 37 | 360 / 719 |
    | Semimonthly | 20 / 40 | 390 / 779 |
    | Monthly | 40 / 81 | 779 / 1,558 |
    | Quarterly | 121 / 243 | 2,337 / 4,674 |
    | Semiannual | 243 / 485 | 4,674 / 9,348 |
    | Daily | 2 / 4 | 36 / 72 |

  - **G-DERIVE:** dividing the annual parameters by the number of periods reproduces every per-period figure (Python, round half up). Weekly: 485/52 = 9.33 → 9 and 9,348/52 = 179.77 → 180. Daily uses 260 days: 9,348/260 = 35.95 → 36 and 485/260 = 1.87 → 2.
  - All 6 worked examples in Pub 14 reproduce: weekly single 400 → 12; biweekly single 2,600 → 116; semimonthly married 1,200 → 18; monthly married 7,800 → 347; quarterly single 9,000 → 367; daily married 175 → 5.
  - Rounding is half up: 9,000 × 0.0445 = 400.5 → 401.
- **Effective date of the schedules: open.** Pub 14 Rev. 04/26 does not state it. Tier-B leads say the schedules apply to pay periods beginning on or after 2026-06-01, replacing allowances of 450/900 [US-UT-PIT-004, B, MANUAL]. That would be a mid-year table change. See Open questions.
- **Supplemental wages:** Pub 14 and R865-9I state no Utah supplemental flat rate (searched: "supplemental" has 0 hits in Pub 14). Build rule: supplemental pay is taxed through the regular schedules as part of Utah taxable wages. Confidence medium; no explicit statement either way.
- **Exempt certificate:** an employee who filed federal W-4E (no liability) is not withheld [R865-9I-15].
- **Nonresidents and multistate** [R865-9I-14(A)-(C), US-UTS5-013; Pub 14, US-UT-P5-1-002]:
  - Nonresidents are withheld on services performed in Utah. A nonresident working in and out of Utah is withheld on the portion allocable to Utah.
  - Residents are withheld on all wages. When the other state requires withholding, Utah withholding is reduced by that state's withholding.
  - **20-day safe harbour:** no Utah withholding for a nonresident who has no other Utah income, works 20 days or less in Utah, and lives in a no-tax state or a state with a similar exclusion. The harbour does not cover athletes, entertainers, per-event prominent persons, real-property laborers, or key/top-50 employees.
  - Interstate transportation employees: taxed only in the state of residence (49 USC 14503 / PL 101-322). The employee writes "Utah Only – Exempt, Interstate Transportation" in W-4 box 4c.
  - Military spouses: exempt. The W-4 box 4c note is "Utah Only – Exempt, Military Spouse"; wages are still reported in W-2 box 16.
- **Reciprocity:** none. Utah is not listed by any reciprocal state [MULTI.md].
- **Local income taxes:** none. "No local governments in Utah assess an income tax" [US-UTR3-002, A.3]. Pub 14 has no local content.
- **Employer de minimis:** an employer doing business in Utah for 60 days or less in a year may be exempted with Tax Commission approval; good cause can extend this by 30 days. The exemption is for the employer only [Pub 14, 59-10-402(2); statute still MANUAL US-UT-PIT-001].

## 3 — social_security (UI only; no SDI, TDI or PFML)
- **SUI 2026** [DWS Tax Rates page, US-UT-SUI-001 / US-UT-P5-1-003, A.2; Excess Wages page, US-UTS5-005]:
  - Taxable wage base **50,700** (calendar 2026).
  - Overall rate = benefit ratio × reserve factor + social cost.
  - 2026 reserve factor 1.10; social cost 0.001 (0.1%).
  - Minimum 0.1%, maximum 7.1%.
  - Delinquency surcharge of 1.0% if contributions for the prior fiscal year are unpaid.
- **New employer rate:** no single figure. The rate is the two-year average benefit ratio of the employer's industry. New out-of-state contractors get the maximum 7.1% [US-UT-SUI-001].
- **Employee contribution:** none [US-UT-P5-2-005].
- **SDI, TDI and PFML:** none. Utah is not among the 13 states + DC with PFML programmes [US-UT-P5-2-006].
- **Other employer levies:** the social-cost component and the delinquency surcharge only [US-UTP7-001/-002, US-UTP9V-001]. Taken from the P7/P9 rows, not redone.
- **Wage-base credit for wages reported to another state (MULTI-OQ-2):** not proven. The Excess Wages page shows a single-state example only. The taxable-wage definition in Utah Code 35A-4-303 is not archived. See Open questions.

## 4 — payslip_statute
- **When a deduction is made:** the employer gives a statement of the total amount of each deduction on each regular payday [34-28-3(4), US-UTP6-001, A.1].
- **Format:** all lawful offsets must be itemized on a statement or a detachable check stub [R610-3-20, US-UTS5-012].
- **Content beyond deductions:** there is no general content list (hours, rates, gross) for most employers.
- **Construction-trade licensees (Title 58 ch. 55):** they must give a written or electronic pay statement with name, base rate, pay-period dates, hours if hourly, and amounts and reasons for deductions [34-28-3(5), US-UTP6-001].
- **Electronic delivery:** allowed. The statement must be easily and immediately accessible and printable at no cost. This is stated explicitly for pay-card employees [R610-3-22(C)]. Applying it to all employees is an inference (medium).
- **Retention:**
  - UI wage records: 4 calendar years [US-UTS5-004].
  - Withholding records: at least 4 years from the due date of the return [Pub 14, US-UT-PIT-003].
- **Language:** no Utah language rule [US-UTL-001].

## 5 — reporting_instruments
- **Withholding registration:** through TAP (TC-69). Having Utah employees without a withholding licence is a class B misdemeanor [Pub 14].
- **Withholding returns (TC-941E):** e-filing only (paper rejected).
  - **Default:** quarterly return and payment for employers withholding under 1,000/month. Due Apr 30, Jul 31, Oct 31 and Jan 31.
  - **1,000 USD/month or more:** quarterly return with monthly payments, due the last day of the following month.
  - **Annual:** allowed for Schedule H or Form 944 filers, due Jan 31.
  - The federal semiweekly and next-day rules do not apply [Pub 14; R865-9I-17, US-UTS5-013].
- **Annual reconciliation:** combined with the Q4 or annual return, due **Jan 31**, filed electronically with all W-2s and 1099s. It is required even with zero activity.
  - Late penalties: 50 for a reconciliation more than 14 days late; per form, 30, 60 or 100 depending on lateness, with caps.
  - Refunds to employees are held until Mar 1 unless the employer e-files by Jan 31 [Pub 14].
- **State W-2:** SSA **EFW2** with the **Code RS record required** (it follows its RW record). Code RV is optional; corrections use RCS (RCV optional). The file must be a lowercase .txt [TI-03 Rev. 12/24, US-UTS5-014, A.2].
  - With 250 or more forms, a fixed-length .txt file is mandatory.
  - Each form carries the FEIN and the 14-digit Utah withholding account number ending in WTH [Pub 14].
  - W-2 content: the word "Utah" and the SSN [R865-9I-16].
  - A web-service channel also exists [US-UTS5-015].
- **Quarterly UI report:** the Employer's Quarterly Wage List and Contribution Report, filed online only and due within 30 days of quarter end (Apr 30, Jul 31, Oct 31, Jan 31). Zero reports are required. Domestic employers may elect annual filing by Jan 31 [US-UTS5-004, A.2]. The upload is a DWS wage file; the layout was not read.
- **New hire:** report within **20 days** of the first day of work, for new hires and rehires [US-UTS5-003, A.2].
  - Seven mandatory elements: employee name, SSN, address and hire/rehire date; employer name, FEIN and address. Date of birth is optional.
  - Filed with the DWS New Hire Registry (manual entry or file upload).
- **Powers of attorney:** TC-737 Rev. 9/26 and DWS UI POA Rev. 08/24 [US-UTP6-002/-003].

## 6 — leave
- **Paid sick leave:** Utah has no private-sector paid sick leave statute. None was found in Title 34 rules R610-1 or R610-3.
  - R610-3-4(B)(1) treats vacation, holiday, sick leave, PTO, severance and bonuses as recoverable wages only "if due under an agreement with the employer or under a policy of the employer" [US-UTS5-012, A.1].
  - Confidence medium-high: this is a negative finding, not a full-title search.
- **PFML:** none [US-UT-P5-2-006].
- **Other paid leave with pay impact:** none found. Jury duty and voting leave were not checked (budget).

## 7 — termination
- **Discharge (employer separates the employee)** [Utah Code 34-28-5, US-UTS5-002, A.1, high]:
  - Wages are due immediately and must be paid **within 24 hours**.
  - The deadline is met by mail postmarked within 1 day, or by direct deposit initiated or hand delivery within 24 h.
  - Penalty after a written demand: wages continue at the same rate until paid, for at most 60 days; the action must be filed within 60 days.
- **Resignation without a definite-term written contract:** due on the **next regular payday** (34-28-5(2)). The same applies to industrial disputes.
  - Commission sales agents with custody of accounts: the commission part may wait for audit.
- **Accrued vacation payout:** only if due under the employer's agreement or policy [R610-3-4(B)(1)]. There is no statutory payout.
- **UI separation notice:** no state notice form found. The DWS records duty includes the separation date and reason [US-UTS5-004].
- **State WARN:** none found (not searched further; low payroll relevance).

## 8 — benefits_in_kind
- **Withholding conformity:** Utah follows the federal definition. Utah taxable wages are wages subject to federal withholding [Pub 14; R865-9I-14(E)]. Federal exclusions (401(k) deferrals, §125, HSA, transit, group-term life within the limit) therefore flow through to Utah withholding. Confidence high for withholding.
  - Assessment-level adjustments under 59-10-114 were not read.
- **UI is different:** UI reportable wages include meals, lodging and in-kind payments, tips, and **deferred-compensation (401(k)) contributions** [US-UTS5-004]. Build: SUI wages are not the same as federal taxable wages.

## 9 — deductions_garnishments
- **Authorization:** R610-3-18 lists the lawful deductions, with written authorization for benefits, dues and financial-institution deductions, and conditions for employer-damage, advance and purchase offsets [US-UTS5-012, A.1, high]. No deduction is allowed where wages were paid late.
- **Garnishment limits:** valid garnishments in "proper amounts" are honoured [R610-3-18(H)]. A Utah limit that differs from the CCPA was not read: Utah Code 70C-7-103 and URCP 64D are not archived or not reached. Default: CCPA 25% / 30× federal minimum. Confidence low on whether a state variance exists.
- **Child support (ORS)** [US-UTS5-016, A.3]:
  - IWOs must be honoured; e-IWO is available.
  - Payments go by EFT/ACH or by check to ORS, PO Box 45011, Salt Lake City UT 84145-0011.
  - Not stated on the page: employer administrative fee, remittance deadline, and priority.
- **State tax levies:** not read.

## 10 — collective_agreements / prevailing wage
- **No state prevailing wage law:** repealed in 1981 [US-UT-P5-1-001, A.2]. Federal Davis-Bacon applies on federal contracts only. There is no state certified-payroll duty.

## 11 — indexation
- **Minimum wage:** not indexed; capped at the federal rate [US-UTS5-010].
- **SUI wage base:** recomputed every year. The DWS publishes the new rates and wage base by mid-November, once the BLS data arrive in early November [US-UTS5-006, A.3].
  - The 2027 base was not published in any copy read; the latest captures date from 2026-06. Check around 2026-11-15.
  - The 75%-of-average-wage formula in 35A-4-303 was not read, so **no G-DERIVE is possible**.
- **Income-tax schedules:** the base allowance and threshold are revised when the law changes. Pub 14 is reissued; the latest read is Rev. 04/26.
- **Rate:** set by statute, not indexed.

## 12 — data_protection
- **W-2:** must carry the full SSN [R865-9I-16(A)(5)].
- **Pay statements:** no Utah SSN-truncation rule was found. Utah Code Title 13 ch. 45 (Protection of Personal Information Act) was not read (le.utah.gov not reachable). Confidence low. See Open questions.

## 13 — live_legal_change
- **Rate cut:** 4.5% → 4.45%, retroactive to 2026-01-01 (Ch. 250, 2026 GS) [US-UTS5-001, A.1].
- **Withholding schedules:** Pub 14 Rev. 04/26 schedules (base allowance 485/970) [US-UT-PIT-003]. Mid-year effective date 2026-06-01 per tier-B only [US-UT-PIT-004]. Already in MANDATE line 51.
- **SUI 2027:** rates and wage base due mid-November 2026 [US-UTS5-006].
- **Admin rules R610-1 and R610-3:** continued unchanged on 2026-01-08. R865-9I was last changed 2026-01-01.
- **Bulletin sweep (Tax Commission news, DWS):** not possible (403 from this network). See ACCESS gaps. No 2027 Utah payroll change was found among the sources read.

## Special populations (state level)
| Population | Utah rule | register_id |
|---|---|---|
| Domestic / household | Utah withholding only if employer and employee agree; annual withholding filing allowed with Schedule H; UI annual filing election by Jan 31 | US-UT-PIT-003; US-UTS5-013; US-UTS5-004 |
| Agricultural | Minimum-wage exemptions under 34-40-104 not read (version not archived); UI coverage per 35A-4-205 not read | gap: see ACCESS |
| Minors | 4.25/h for the first 90 days with an employer, then 7.25 | US-UTS5-011 |
| Tipped | Cash wage 2.13; tips of at least 30/month; credit-card fee deduction allowed; pooling only among tipped staff; written notice at hire | US-UTS5-011; US-UTS5-008 |
| Clergy / religious | No state rule beyond federal: Utah withholding follows federal income-tax-withholding wages (R865-9I-14(E)), so no Utah withholding where federal withholding does not apply | US-UTS5-013 |
| Students | No state rule beyond federal for withholding; UI exemption (35A-4-205) not read | US-UTS5-013; gap |
| Nonresident aliens | Utah wages = federal withholding wages; no separate Utah NRA rule found | US-UTS5-013; US-UT-PIT-003 |
| Statutory employees | Utah withholding only where federal income-tax withholding applies, with employee status per IRS guidelines | US-UTS5-013 |
| Government employees | Minimum wage covers "private and public employees within the state" (34-40-103(2)(a)) | US-UTS5-010 |
| Interstate transport / military spouses | Exempt from Utah withholding, using the federal W-4 box 4c notes (wording in section 2) | US-UT-PIT-003 |
| Nonresident short-term workers | 20-day safe harbour (see section 2) | US-UT-P5-1-002 |

## MULTI hand-offs (answers for UT)
- **OQ-2, SUI credit for wages reported to another state:** unresolved for UT (statute not reached).
- **OQ-3, PFML/SDI:** not applicable; Utah has no programme.
- **OQ-4, paid sick leave:** not applicable; no statute.
- **OQ-8, pay-statement reach:** no Utah extraterritorial rule. The duty in 34-28-3(4) attaches to Utah employment; default is the work-location rule.

## ACCESS gaps (exact URLs, 2026-11-02, from a BR exit IP)
- **403 direct; Wayback version not archived or not tried:**
  - `https://tax.utah.gov/withholding`
  - `https://tax.utah.gov/forms/pubs/pub-14.pdf` (the Pub 14 HTML is held via Wayback)
  - `https://jobs.utah.gov/ui/employer/Public/Questions/TaxRates.aspx` (held via Wayback 2026-06-11)
  - `https://laborcommission.utah.gov/divisions/antidiscrimination-and-labor-ald/wage-claims/`
  - `https://tap.utah.gov/`
- **Timeout direct; Wayback 404 for the current version file:**
  - `https://le.utah.gov/xcode/Title34/Chapter40/C34-40-S104_2023050320230503.html` (minimum-wage exemptions)
  - `https://le.utah.gov/xcode/Title59/Chapter10/C59-10-S402_2022050420230101.html` and `.pdf` (withholding duty; R865-9I-14 used instead)
  - `https://le.utah.gov/xcode/Title35A/Chapter4/C35A-4-S303_2021111020211116.html` (SUI wage base and other-state wages)
  - `https://le.utah.gov/xcode/Title35A/Chapter4/C35A-4-S205_1800010118000101.html` (exempt employment)
  - `https://le.utah.gov/xcode/Title70C/Chapter7/C70C-7-S103_2014040320140327.html` (garnishment limit)
- **202 bot challenge:** `https://acf.gov/css/contact-information/state-income-withholding-contacts-and-program-requirements` (UT IWO fee and remittance timing).
- **Wayback CDX:** `laborcommission.utah.gov/*` returned empty or "Temporarily Offline" (2026-11-02).
- **Route for the orchestrator's pass:** with a US exit IP, `le.utah.gov` will likely serve these sections directly. The versions named above are the current files.

## Open questions
- **UT-OQ-1. Effective date of the Pub 14 Rev. 04/26 schedules** (base allowance 485/970, thresholds 9,348/18,696). Tier-B says pay periods beginning on or after 2026-06-01; the earlier allowances were 450/900. What would close it: the Tax Commission notice or the Pub 14 PDF cover page at `https://tax.utah.gov/forms/pubs/pub-14.pdf` (Utah State Tax Commission, Withholding), read from a US IP.
- **UT-OQ-2. Supplemental-wage treatment.** No flat rate is published. What would close it: Pub 14 PDF text, or a Tax Commission answer (801-297-2200), confirming that supplemental pay uses the regular schedules.
- **UT-OQ-3. SUI credit for wages reported to another state (MULTI-OQ-2).** What would close it: Utah Code 35A-4-208/-303 current text on le.utah.gov, or the DWS Employer Handbook, Contributions chapter (`https://jobs.utah.gov/ui/employer/public/handbook/Employer_Handbook.pdf`).
- **UT-OQ-4. 2027 SUI wage base and rate range.** These are due mid-November 2026 on the DWS Tax Rates page. Re-read after 2026-11-15.
- **UT-OQ-5. Direct-deposit consent rule.** What would close it: Utah Code 34-28-2/-3, current version (le.utah.gov).
- **UT-OQ-6. 34-40-104 exemptions** (agricultural, seasonal, domestic and others) for the special-populations table. What would close it: le.utah.gov C34-40-S104_2023050320230503.
- **UT-OQ-7. State garnishment limits versus the CCPA, and ORS IWO fee/remittance timing.** What would close it: Utah Code 70C-7-103 and Utah Code 62A-11-406 (le.utah.gov); the ACF state IWO requirements page (browser pass).
- **UT-OQ-8. SSN truncation on pay statements.** What would close it: Utah Code 13-45 (le.utah.gov).
- **UT-OQ-9. US-UT-PIT-001 (59-10-402) is still MANUAL.** Its substance is now carried by A.1 rule R865-9I-14 (US-UTS5-013). The synthesis can keep the statute row MANUAL, or re-point citations to US-UTS5-013.
- **UT-OQ-10. US-UT-PIT-004 (tier-B rate row).** The rate is now proven by US-UTS5-001. The synthesis should re-point rate citations; the 2026-06-01 date stays open (UT-OQ-1).

**Parallel shape of the remaining work.** The open statute reads (OQ-3, 5, 6, 7, 8) are 5 independent le.utah.gov sections. One pass with a US exit IP closes them.
