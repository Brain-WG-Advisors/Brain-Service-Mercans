# Stage 5 — KS (Kansas) — 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Budget declared: 60 fetches / 2 h. Used: about 37 fetches (failed probes included) in about 20 minutes. Fetching stopped below the 75% mark (45 fetches).
Shard: `00-official-sources/_register-shards/S5-KS.csv` (US-KSS5-001..029, 29 rows, 20 columns each). New sources: `00-official-sources/ccg-sources/KS/` (25 files, 1.5 MB).
Files already on disk were reused in place, not copied: `00-official-sources/pdfs/KS/`. This covers KW-100, the KDOL pages and K.S.A. 44-313..325. Note: the Wayback copies in `pdfs/KS/` are **gzip-encoded** even though they are named `.html`. Decompress them before reading.

**Access.**
- From this machine the IP exits in Brazil, not on the US VPN.
- `www.ksrevenue.gov` times out on direct curl (HTTP 000). KDOR files were taken from Wayback `2026id_` copies: Notices 25-06 and 26-11, K-4 and K-2MT.
- `www.dol.ks.gov` returns 403. The existing Wayback copies from October 2026 were used.
- `www.ksrevisor.gov` and `kslegislature.gov` answer plain curl.

**Headline.**
- The 2026 Kansas withholding tables are the ones in force since **2024-07-01** (SB 1, 2024 special session). There are two rates, **5.2% / 5.58%**.
- KDOR certified that the rate-cut trigger of SB 269 (K.S.A. 79-32,110c) failed both years. Notice 25-06 covers tax year 2026 and Notice 26-11 covers tax year 2027. So the rates do not change in 2026 or 2027.
- The UI taxable wage base became indexed (25% of SAAW) from 2026: **15,100**.

## 1 — labour_code
- **Minimum wage:** USD **7.25/h** since 2010-01-01. The tipped cash wage is **2.13/h**, with a tip credit up to 7.25 (K.S.A. 44-1203) [US-KSS5-008, A.1].
  - The state law does not apply to employers or employees covered by the FLSA. In practice FLSA 7.25 governs most employers.
  - There is no indexation.
  - **2027:** no increase is enacted. SB 471 (USD 16/h) **died** at the end of the 2025-2026 biennium [US-KSS5-027].
  - Confidence: high.
- **Local minimum wages:** none. K.S.A. 12-16,130 bars cities and counties from requiring wages above the minimum wage, leave, paid leave, benefits or scheduling changes [US-KSS5-012, A.1]. Confidence: high.
- **Overtime beyond the FLSA:** only for employees not covered by FLSA s.7. They get 1.5x the regular rate after **46 hours** in a workweek; EMS, fire and law enforcement use 258 h per 28 days (44-1204) [US-KSS5-010].
- **Exclusions from the state minimum-wage/overtime law** (44-1202(e)) [US-KSS5-009]:
  - agriculture;
  - domestic service in a private home;
  - EAP employees and outside commission salespeople;
  - federal employees;
  - volunteers for nonprofits;
  - persons aged 18 or under employed occasionally or part-time (under 40 h/week, or students between terms);
  - unified school district EAP staff.
- **Pay frequency and timing** (44-314) [US-KSS5-013]:
  - pay at least **once per calendar month**, on regular paydays designated in advance;
  - the pay period may end **no more than 15 days before payday**.
- **Method of payment** (44-314) [US-KSS5-013]:
  - cash, negotiable check, EFT to an account the employee designates, or payroll card;
  - an EFT-only employer must offer a default alternative;
  - payroll card: one free withdrawal per period up to net pay, and no fees;
  - **30 days before** an EFT-only or card-only programme starts, the employer must hold an employee forum or distribute educational information.
- Confidence: 90%.

## 2 — income_tax
- **Authority and statute:** the Kansas Department of Revenue (KDOR) administers withholding. The rates are in K.S.A. 79-32,110 for tax year 2024 and later [US-KSS5-004, A.1]:
  - single/HoH/MFS: 5.2% up to 23,000, then 1,196 + 5.58%;
  - married filing jointly: 5.2% up to 46,000, then 2,392 + 5.58%.
- **Allowances and deductions:**
  - Standard deduction (79-32,119(c)(2)): single 3,605, married 8,240, HoH 6,180. These are fixed amounts with no indexation clause [US-KSS5-005].
  - Personal exemptions (79-32,121, tax year 2025 and later): 9,160 single/HoH/MFS, 18,320 MFJ, 2,320 per dependent [US-KSS5-006].
- **Withholding method:** KW-100 web edition, "Withholding Tax Rates for wages paid on and after July 1, 2024" (Wayback 2026-10-21, the current edition) [US-KSS5-001, A.2].
  1. Compute gross pay for the period.
  2. Subtract the allowance for the period. Annual amounts: 9,160 Single, 18,320 Joint, 2,320 per dependent; HoH filers add one extra 2,320. Weekly amounts: 176.15 / 352.31 / 44.62.
  3. Apply the period table (Tables 1-8). Annual table: Single 0% to 3,605, then 5.2% to 26,605, then 1,196 + 5.58%; Married 0% to 8,240, then 5.2% to 54,240, then 2,392 + 5.58%.
  - Wage-bracket tables are an alternative.
  - The KW-100 header still prints "(For wages paid on and after January 1, 2021)" above the tables, but the figures are the 2024 values. Do not trust that header (rule 6).
- **G-DERIVE (done in Python):**
  - Each period threshold equals the annual amount divided by the number of periods:
    - weekly Single: 3,605/52 = 69.33 → **69**; 26,605/52 = 511.63 → **512**; 1,196/52 = **23.00**;
    - semi-monthly Married: 8,240/24 = **343.33**; 54,240/24 = **2,260**; 2,392/24 = **99.67**;
    - monthly Married: **687 / 4,520 / 199.33**.
  - All match the KW-100 tables.
  - The zero-bracket amounts equal the statutory standard deduction, and the 5.2% band equals the statutory 23,000/46,000 bracket.
  - Allowance: 9,160/52 = 176.15 ✓.
- **Certificate:** Form **K-4 (Rev. 7-24)** [US-KSS5-025]:
  - Allowance rate is "Single" or "Joint". A married employee whose spouse has income marks Single.
  - Without a K-4, the employer withholds at the **Single rate with no allowance**.
  - Exempt status requires verification with KDOR.
  - The federal W-4 is not accepted for Kansas.
- **Supplemental wages:** use the same method as for federal.
  - Aggregated with regular pay: use the tables.
  - Stated separately with the federal flat %: Kansas withholds **5%** of the payment.
  - Other payments with percentage federal withholding: also 5% [US-KSS5-001].
- **Rounding:** the percentage-method result may be rounded to the nearest dollar (under 50c down, 50c and over up) [US-KSS5-001].
- **Rates 2026 / 2027:** the SB 269 trigger was not met.
  - FY2025 collections were 88,481,523 below the inflation-adjusted base, so there is **no reduction for tax year 2026** (Notice 25-06) [US-KSS5-002].
  - FY2026 collections were 214,339,364 below, so there is **no reduction for tax year 2027** (Notice 26-11, 2026-10-15) [US-KSS5-003].
  - The differences were re-derived from the published figures.
- **Residents working in another state:** withhold the Kansas tax on total wages, less the other state's required withholding. If the other state's withholding is higher, nothing is due to Kansas [US-KS-P5-1-003, US-KSS5-001].
- **Nonresidents:**
  - Full-time in Kansas: withhold as for a resident.
  - Working inside and outside Kansas: Kansas tax on total wages x the Kansas share (hours, days or commissions). The employee may file a K-4C allocation statement.
  - Interstate carriers: Public Law 91-569.
  - Nonresident tax at assessment: 79-32,110(b) ratio [US-KSS5-001, US-KSS5-004].
  - **Level: withholding.**
- **Reciprocity:** none. KW-100 names no reciprocal agreement [US-KS-P5-1-003].
- **Local income taxes:** none.
  - The KDOR business-tax list shows withholding as the only wage-based tax [US-KSP9V-002].
  - KW-100 names no local wage tax.
  - K.S.A. 12-16,130 does not itself bar a local income tax. The absence rests on the KDOR source.
- **Nonresident aliens:** if federal withholding applies, Kansas withholding also applies [US-KSS5-001].
- Confidence: 95%.

## 3 — social_security (SUI; no SDI/TDI/PFML)
- **Agency:** Kansas Department of Labor (KDOL).
- **2026 rates** [US-KSS5-023 / US-KSP9V-001, A.2]: Schedule C (HB 2570); experience rates **0%–6.95%**; new employer **1.75%**; new construction employer **5.55%**; rated governmental employers **0.10%** (2025, 2026 and 2027).
- **New-employer rate in statute:** 1.75% / 5.55% until 24 months of chargeability (K.S.A. 44-710a(a)(1)) [US-KSS5-029].
- **2025 for comparison:** Schedule B, 0%–6.65%, wage base 14,000.
- **Taxable wage base 2026: USD 15,100** [US-KSS5-023].
  - The statutory formula (44-703(o)(2)): for rated groups 0–N11, 25% of the prior-year statewide average annual wage (SAAW), rounded to the nearest 100, for 2026–2027. It rises to 30% in 2028, 35% in 2029, 40% in 2030–31, and 40% or 45% from 2032 [US-KSS5-020, A.1].
  - **G-DERIVE:**
    - The maximum weekly benefit amount (WBA) is 55% of the statewide average weekly wage (SAWW) (44-704(c)) [US-KSS5-021].
    - The WBA of 637 from 2025-07-01 implies SAWW 1,158.18–1,160.00, so SAAW 60,225–60,320, and 25% of that is 15,056–15,080 → **15,100** ✓.
    - The same arithmetic on the 2026-07-01 WBA of 663 points to about **15,700 for 2027**. This is a projection, **not** a published figure; it is kept out of the facts.
- **Wages already paid under another state's UI law** count toward the Kansas base (44-703(o)(2)(C)(i)) [US-KSS5-020]. This answers the MULTI hand-off.
- **Employee contribution:** none. Federal list: only AK, NJ and PA [US-FED-P5-2-006].
- **No SDI/TDI/PFML programme** [US-LA-P5-2-002].
- **Employer levies:** none beyond UI (P7/P9 list) [US-KSP9V-001, US-KSP9V-002].
- **Coverage thresholds (44-703(h))** [US-KSS5-020]:
  - agricultural: USD 20,000 cash in a quarter, or 10 workers in 20 weeks;
  - domestic: USD 1,000 cash in a quarter.
- **Tips** reported at USD 20 or more a month are UI wages.
- **"Schedule C" vs the statutory table letters:** 44-710a carries its own schedule tables. The KDOL table was used for the 2026 schedule letter and the rate range. These figures were not re-traced into the statute tables.
- Confidence: 90%.

## 4 — payslip_statute
- **Pay statement:** no mandatory statement on every payday was found. The employer must furnish an **itemized statement of deductions on request**, for each pay period with deductions (K.S.A. 44-320(d)) [US-KS-P5-2-001, A.1].
- **Payroll card:** net wages are as shown on the "earnings statement" (44-314(d)). This implies the employee sees net pay, but it does not prescribe content [US-KSS5-013].
- **Records:** keep at least 3 years: name, occupation, rate, amount paid each period, and daily and weekly hours. FLSA-covered employers may keep FLSA records instead (44-1209) [US-KSS5-011]. KW-100 requires withholding records for 3 years [US-KSS5-001].
- **Electronic delivery:** no Kansas rule was located.
- Confidence: 80%. The absence of a statute is read on 44-313..325 and 44-1201..1213 only.

## 5 — reporting_instruments

### Withholding (KDOR)
- **Deposit frequency** (K.S.A. 79-3298, set from prior-year withholding) [US-KSS5-007, A.1; KW-100 US-KSS5-001]:
  - **Quad-monthly** (over 100,000 a year): periods end on the 7th, 15th, 21st and last day; pay within 3 banking days.
  - **Semi-monthly** (8,000–100,000): due the 25th and the 10th.
  - **Monthly** (1,200–8,000): due the 15th.
  - **Quarterly** (200–1,200): due the 25th of the month after the quarter.
  - **Annual** (200 or less): due January 25.
- **KW-5 deposit report:** filed for every period, even when nothing was withheld.
- **KW-3 annual return:** filed electronically by **January 31**, together with the state W-2s and the 1099s that carry Kansas withholding.
- **Business closure:** file within 30 days after the month of closure.
- **W-2 state copy** [US-KSS5-026]:
  - **51 or more forms must be filed electronically.** Formats: EFW2 with a Kansas **RS** record (K-2MT Rev. 10-25; RS of 512 bytes, Kansas wages only, required RA/RE/RW/RS/RT/RF) or KW-2CSV.
  - Box 15 carries the account number 036-XXXXXXXXXF-01.
  - Kansas withholding may not go through the federal combined filing programme (CF/SF).
  - The TY2026 K-2MT edition was not yet located.
- **Penalties:** 2% / 5% / 10% / 15%, plus 1%/month up to 24%; USD 50 per state W-2 not filed [US-KSS5-001].
- **Registration:** KDOR Customer Service Center; tax prefix 036 for withholding; POA via form DO-10 [US-KS-P5-1-005].

### UI (KDOL)
- **Quarterly wage report and contribution return:** due **Apr 30 / Jul 31 / Oct 31 / Jan 31** [US-KSS5-022].
- **Online filing threshold:** the FAQ says 26+ employees must file online and 25 or fewer may mail form K-CNS-100. The EDI section says employers with **25 or more employees (or TPAs with 25+ client employees) must e-file from 2024-07-01**. The page contradicts itself; the build should use **25+**, the stricter reading (Open question 2).
- **Upload formats:** MMREF / NASWA.
- **TPA link:** form K-CNS-032 [US-KS-P5-2-003].
- **PEOs:** client reporting state, forms K-CNS 010 / 015 [US-KSS5-023].

### New hire
- Report **within 20 business days** of hire, rehire or return to work (K.S.A. 75-5743) [US-KSS5-019].
  - Fields: employee name, address, SSN and first day of work; employer name, address and FEIN.
  - A rehire after 60 or more days of separation counts as new.
- The KDOL page says "within 20 days" [US-KSS5-023]. The statute governs.
- Multistate employers may elect a single state through HHS.

- Confidence: 90%.

## 6 — leave
- **Paid sick leave:** no state statute. Local mandates are pre-empted (12-16,130) [US-KSS5-012].
- **PFML:** none [US-LA-P5-2-002].
- **Paid-sick-leave coverage of multistate workers** (MULTI hand-off): not applicable.
- **Other mandated paid leave affecting payroll:** none located. Jury and military leave statutes were not read this pass (Open question 4).
- Confidence: 75%.

## 7 — termination
- **Final pay:** for both discharge and resignation, by the **next regular payday**, by mail if the employee asks. Willful non-payment costs 1% per day after the 8th day, capped at 100% (44-315) [US-KSS5-014].
- **Accrued vacation:** payout only under the employer's policy or contract. The Revisor annotations to 44-313 cite *Mid America Aerospace v. Dept. of Human Resources*, 10 Kan. App. 2d 144 (1985): absent agreement, nothing requires payout. *Sweet v. Stormont Vail*, 231 Kan. 604 (1982): conditions such as a notice period are enforceable [US-KSS5-015]. Status: case law in force. Level: final pay.
- **Final-wage deductions:** allowed with written notice for unreturned property, loans, overpayment and merchandise, never below the minimum wage (44-319(c),(e)) [US-KSS5-016].
- **UI separation notice to the employee:** not located (Open question 3).
- Confidence: 80%.

## 8 — benefits_in_kind
- **Conformity:** Kansas AGI = federal AGI plus listed modifications (79-32,117(a)) [US-KSS5-028]. Federal exclusions therefore flow through: 401(k), section 125, HSA, transit and group-term life.
- **Withholding** applies to IRC 3401(a) wages subject to federal withholding. Taxable fringe benefits are also subject to Kansas withholding [US-KSS5-001].
- **Public employers (departure from federal):** employee contributions **picked up by the employer** under K.S.A. 12-5005, 20-2603, 74-4919 and 74-4965 (KPERS and related systems) are an **addition** to Kansas income (79-32,117(b)(vi)). Whether Kansas *withholding* covers them is Open question 1.
- **529 contributions:** a return-level subtraction only.
- Confidence: 80%.

## 9 — deductions_garnishments
- **Authorised deductions** (44-319) [US-KSS5-016]:
  - deductions required by law;
  - medical care without benefit to the employer;
  - signed authorisation for the employee's benefit;
  - retirement auto-enrolment;
  - written agreement for loans, overpayment and merchandise;
  - charity and union dues.
  - No deduction may take pay below the minimum wage.
- **Creditor garnishment** (K.S.A. 60-2310) [US-KSS5-017]:
  - the lesser of 25% of disposable earnings, the excess over 30 x the federal minimum wage (USD 217.50/week), or the claim;
  - one garnishment per creditor per 30 days;
  - suspended for 2 months after recovery when the debtor was ill more than 2 weeks.
  - Support caps: 50%/60%, or 55%/65% with arrears older than 12 weeks.
  - No cap for bankruptcy or tax debts.
- **Child-support income withholding order (IWO)** (K.S.A. 23-3104/3105) [US-KSS5-018]:
  - start at the next pay after 14 days from service;
  - remit **within 7 business days** of payday;
  - **employer fee:** the lesser of USD 5 per pay period or USD 10 per month (lump sum: up to USD 10). The fee comes on top of the support.
  - **Total cap: 50% of CCPA disposable earnings, including the fee and medical premiums.** This is stricter than the CCPA 60/65%.
  - Before any lump-sum payment when there are arrears, contact the IV-D agency 14 days ahead.
  - The IWO has priority over all other process; multiple orders are prorated with current support first.
- **State tax levies:** not researched separately. The 60-2310(e)(3) exemption from the cap covers state and federal tax debts.
- Confidence: 90%.

## 10 — collective_agreements (prevailing wage)
- No state prevailing-wage law; it was repealed in 1987 (K.S.A. 44-201) [US-KS-P5-2-002, US-LA-P5-2-004]. Federal Davis-Bacon only.
- Confidence: high.

## 11 — indexation
| Item | Indexed? | Basis |
|---|---|---|
| Minimum wage 7.25 | No | 44-1203 [US-KSS5-008] |
| Standard deduction / exemptions | No (fixed amounts) | 79-32,119 / 79-32,121 [US-KSS5-005/006] |
| PIT rates | Only a revenue-contingent cut (K.S.A. 79-32,110c), certified each Aug 15 and published by KDOR notice; not triggered for 2026 or 2027 | [US-KSS5-002/003] |
| UI wage base | Yes: % of SAAW, set yearly by KDOL (25% for 2026–27) | 44-703(o)(2) [US-KSS5-020] |
| Max/min WBA | Yes: 55% of SAWW each July 1 | 44-704(c) [US-KSS5-021] |
| Rate schedule | Yearly by trust-fund computation (HB 2570; KDOL posts by Dec 1) | [US-KSS5-023] |

## 12 — data_protection
- **SSN:** no person may require or use an SSN for commercial purposes unless it is necessary and no other identifier serves. Internal administrative use and uses required by law are exempt. Civil penalty up to USD 1,000 per violation (K.S.A. 75-3520(b)) [US-KSS5-024].
- **Truncation:** no Kansas rule requires SSN truncation on pay statements. Federal W-2 truncation rules apply (FED unit).
- **Data breach:** K.S.A. 50-7a01 et seq. is cited in 75-3520 and was not read.
- Confidence: 70%.

## 13 — live_legal_change (2026-01-01 to 2026-11-02)
| Change | Status | Level | register_id |
|---|---|---|---|
| SB 269 rate-cut trigger, K.S.A. 79-32,110c | In force. Certification of 2026-08-15: **not triggered** for TY2027 (Notice 26-11, 2026-10-15); also not triggered for TY2026 (Notice 25-06) | Withholding (tables) and assessment | US-KSS5-002, US-KSS5-003 |
| UI wage base indexed (HB 2570) | In force from 2026: 15,100; 2027 to be published by KDOL (projection about 15,700, unconfirmed) | Employer UI contribution | US-KSS5-020, US-KSS5-023 |
| Max WBA 663 from 2026-07-01 | In force | Benefits only (no payroll calculation) | US-KSS5-023 |
| Rated governmental UI rate 0.10% for 2027 | Published | Employer UI | US-KSS5-023 |
| SB 471 minimum wage 16/h | **Died** (2025-26 biennium) | — | US-KSS5-027 |
| K.S.A. 79-32,121 unborn-child exemption (L. 2025 ch. 112) | In force from TY2025 | Assessment (the K-4 worksheet does not carry it) | US-KSS5-006 |

**Sweep coverage and limits:**
- Covered: the KDOR tax-notice PDFs reached through Wayback (25-06, 26-11), the KDOL news list (snapshot 2026-08-14), and the SB 471 status page.
- Not covered: the full KDOR notice index (ksrevenue.gov unreachable) and the Revisor's 2026 composite list (URL not found, 404).

## Special populations (US-OWN-005, state round)
| Population | Kansas rule | register_id |
|---|---|---|
| Domestic / household | Withholding follows federal 3401(a), so it is voluntary where federal is. UI covered at USD 1,000 cash per quarter. Excluded from the state minimum-wage law (FLSA governs) | US-KSS5-001, US-KSS5-020, US-KSS5-009 |
| Agricultural | Withholding follows the federal rule. UI covered at USD 20,000 per quarter or 10 workers in 20 weeks; non-cash agricultural pay is not UI wages. Excluded from the state minimum-wage law | US-KSS5-001, US-KSS5-020, US-KSS5-009 |
| Minors | Persons aged 18 or under employed occasionally or part-time are excluded from the state minimum-wage law. UI excludes newspaper delivery under 18 and a child under 21 employed by a parent. Child-labour hours not researched | US-KSS5-009, US-KSS5-020 |
| Tipped | Cash wage 2.13 with tip credit to 7.25 (non-FLSA employers). Tips reported at USD 20 or more a month are UI wages | US-KSS5-008, US-KSS5-020 |
| Clergy / religious | UI excludes church employment and ministers. Withholding follows federal (ministers exempt from mandatory withholding) | US-KSS5-020, US-KSS5-001 |
| Students | UI excludes students working for their own school and work-study programmes. Students under 18 between terms count as part-time for the minimum-wage exclusion | US-KSS5-020, US-KSS5-009 |
| Nonresident aliens | Kansas withholding applies whenever federal withholding applies | US-KSS5-001 |
| Statutory employees | No state rule beyond federal (KW-100 follows the federal employee definition; PEO = employer) | US-KSS5-001 |
| Government employees | Withholding required even though the employer is tax-exempt. Rated governmental UI rate 0.10%. KPERS picked-up contributions are a Kansas addition (Open question 1). The minimum-wage law excludes federal employees and USD EAP staff | US-KSS5-001, US-KSS5-023, US-KSS5-028, US-KSS5-009 |
| Motion-picture extras | Wages for under 14 days a year are exempt from Kansas withholding | US-KSS5-001 |

## MULTI hand-offs (Kansas answers)
- **SUI wage-base credit for wages reported to another state:** yes. "Employment" for the wage base includes service under another state's employment security law (44-703(o)(2)(C)(i)) [US-KSS5-020].
- **PFML/SDI coverage of multistate workers:** not applicable, Kansas has no programme.
- **Paid-sick-leave coverage of partial in-state work:** not applicable, no statute.
- **Pay-statement reach:** not applicable. There is only the on-request deduction statement (44-320).

## ACCESS gaps
- `https://www.ksrevenue.gov/kw100.html`: HTTP 000 (timeout). Wayback copy 2026-10-21 used.
- `https://www.ksrevenue.gov/taxnotices/notice25-06.pdf`, `.../notice26-11.pdf`: HTTP 000. Wayback used.
- `https://www.ksrevenue.gov/taxnotices.html`: Wayback `2026id_` returned 404. The full 2026 notice index was not reviewed.
- `https://www.dol.ks.gov/employers/employer-services`: HTTP 403. Wayback 2026-10-16 copy (already on disk) used.
- `https://admin.ks.gov/.../25-p-004-new-kansas-state-withholding-tables`: 404 (lead only; not needed).
- `https://www.ksrevisor.gov/statutes/2026CompositeListByKSA.html`: 404 (guessed URL).

## Open questions
1. **KPERS picked-up contributions:** 79-32,117(b)(vi) adds them back to Kansas income. Does KDOR require Kansas *withholding* on them (public-employer payroll)? **What would close it:** KDOR KW-100 PDF or a Revenue Ruling on picked-up contributions, or the Kansas Department of Administration payroll circular for state employees.
2. **KDOL e-filing threshold:** the FAQ says 26+ employees, the EDI section says 25+ (from 2024-07-01). **What would close it:** K.A.R. 50-2-? / the KDOL Employer Handbook section on electronic filing (KDOL), or the HB/SB that set the mandate.
3. **UI separation notice to employees:** is a Kansas form or notice required at separation? **What would close it:** the KDOL Employer Handbook (UI) section on separations, or K.A.R. 50-3.
4. **Other leave with pay impact:** jury duty (K.S.A. 43-173) and state military leave statutes were not read. **What would close it:** those Revisor pages.
5. **TY2026 K-2MT edition** (W-2 RS layout for the files due 2027-01-31). **What would close it:** KDOR `forms-btwh.html` when the Rev. 2026 edition is posted.
6. **2027 UI wage base:** the projection is about 15,700 (25% of the SAAW implied by the 663 maximum WBA). **What would close it:** KDOL Employer Tax Rates table for rate year 2027 (posted by Dec 1, 2026).
7. **The 44-710a Schedule C rate table** was not traced row by row against KDOL's 0%–6.95%. **What would close it:** a parse of the schedule tables in KSA_044_007_0010a (on disk).

## Supersession note for the merge
- US-KSS5-001 supersedes **US-KS-P5-1-001**. It is the same guide, now with the full 2024 tables and the arithmetic proof.
- US-KS-001 (MANUAL; its "06/21" header reading was wrong for the figures) and US-KS-002 (MANUAL) already have active successors: US-KS-P5-1-001 → US-KSS5-001, and US-KS-P5-1-002 / US-KSS5-023.
