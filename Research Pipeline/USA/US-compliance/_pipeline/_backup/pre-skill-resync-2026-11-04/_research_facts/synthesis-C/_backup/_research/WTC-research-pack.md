# WTC research pack (US build, Stage 5: units global_baseline + country_specific)

Synthesis-B worker, 2026-11-02. No fetching: every value below comes from an `active` (or `partial`, flagged) row of `00-official-sources/legal-basis-register.csv` (2,533 rows), via the Stage 5 findings in `_research/stage5/{JUR}.md` and the run journal. Facts files:

- `_research/WTC-global_baseline-facts.json` (federal layer + multistate routing),
- `_research/WTC-country_specific-facts.json` (51 jurisdictions).

Both PASS `validate_contract.py facts` (schema 1.4.0). The contract allows `{ARTIFACT}-{unit}-facts.json`, so no fragments are needed.

**Key namespace.** `{jur}.{tax}.{concept}[.{qualifier}].{attribute}`, where `jur` is `fed`, `multi` or the lowercase USPS code. `tax` is one of `sit` (state income tax withholding), `sui`, `sdi`, `tdi`, `pfml` / `famli` / `pfl` / `paid_leave` (named as the state names the programme), `cares`, `levy`, `local`, `base` (wage-base inclusion/exclusion: non-conformity), `bik` or `oracle`. Rates carry `unit_of_measure: percent` and are written as percentages (6.2 means 6.2%). Indiana county LIT rates are the exception: they carry `ratio`, as DOR prints them (0.0171). A new year is a new fact object under the same key, with its own `effective_from`.

**Contract defect found (read this before binding keys).** 407 active register rows have ids with four or more segments (e.g. `US-CO-P5-1-003`, `US-UT-PIT-003`, `US-CA-EDD-004`). These fail the facts-schema `register_id` pattern `^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$`. Where no conforming row carries the same value, the value sits in `unresolved[]` with `_value`, `_register_id`, `_unit`, `_effective_from` and `_note`, plus a `why` that starts "Value is sourced". That is 13 entries in global_baseline and 64 in country_specific. These are **sourced values, not research gaps**: the builder may use them under their `_register_id`. A contract PATCH that widens the pattern moves them back into `facts[]` unchanged. Main examples: CO UI wage base 30,600/32,100, CO new-employer 3.05%/1.70%, UT Pub 14 method and examples, MN UI 44,000, NM UI 34,800, NV UI 43,700, CA ETT/SDI second rows, the MULTI reciprocity entries that cite P5 rows, MT UI maximum rate, and the WA Seattle payroll expense tax.

---

## 1. global_baseline: wage types and their federal treatment

| Wage type / item | FIT | FICA (OASDI 6.2/6.2 to 184,500; Medicare 1.45/1.45; Addl 0.9 >200,000) | FUTA (0.6% net on 7,000) | W-2 | register_id |
|---|---|---|---|---|---|
| Regular wages, salary, commissions | Pub. 15-T Worksheet 1A / tables | yes | yes | box 1/3/5 | US-FEDS5-001, US-FEDS5-005, US-FED-007 |
| Supplemental (bonus, separately identified) | 22% optional flat; 37% mandatory above 1,000,000 YTD | yes | yes | box 1 | US-FEDS5-003 |
| Overtime premium (qualified, P.L. 119-21) | fully wages; deduction at **assessment** only, reaches withholding only via W-4 Step 4(b) | yes | yes | box 12 **TT** | US-FEDS5-030, US-FEDS5-007 |
| Cash tips ≥ 20/month | wages; tips deduction at **assessment** only | yes | yes (FUTA extent) | box 12 **TP** + box 14b TTOC | US-FEDS5-030, US-FEDS5-007, US-FEDS5-013 |
| Trump-account employer contribution | excluded up to 2,500 (from 2026-07-04) | per row | per row | box 12 **TA** | US-FEDS5-030, US-FEDS5-007 |
| 401(k) elective deferral | excluded (402(g) 24,500; catch-up 8,000; 60-63 11,250) | **subject** | **subject** | box 12 D | US-FED-023 |
| Section 125 premiums / FSA (3,400; carry-over 680) | excluded | excluded | excluded | — | US-FEDS5-010 |
| HSA via 125 (4,400 / 8,750) | excluded | excluded | excluded | box 12 W | US-FED-024 |
| Dependent care assistance | excluded to **7,500** (3,750 MFS) | excluded to limit | excluded to limit | box 10 | US-FEDS5-008 |
| Transit / parking | excluded to 340/month each | excluded | excluded | — | US-FEDS5-008 |
| Educational assistance | excluded to 5,250 (permanent) | excluded | excluded | — | US-FEDS5-008 |
| Group-term life > 50,000 | Table 2-2 imputed cost | FICA wages | per row | box 12 C | US-FEDS5-008 |
| Moving expense / bicycle commuting | **taxable** (exclusions eliminated) | taxable | taxable | box 1 | US-FEDS5-008 |
| Severance | wages | wages | wages | box 1 | US-FEDS5-029 |
| State PFML employee contribution / employer-paid employee share | W-2 wages (Rev. Rul. 2025-4, Notice 2026-6) | — | — | box 14 (state label) | US-FEDS5-007 |
| NRA wages | Pub. 15-T add-on (T2 weekly 309.60 … annual 16,100) for the FIT computation only; not on 22%/37% | normal | normal | treaty-exempt wages on 1042-S | US-FEDS5-002, US-FEDS5-015, US-FEDS5-016 |
| Minister (common-law employee) | no withholding (voluntary agreement) | no withholding (SE tax) | — | parsonage excluded | US-FED-030 |
| Statutory employee | no FIT | FICA yes | — | box 13 | US-FEDR3-005 |
| Household employee | only by agreement | ≥ 3,000 cash (2026) | ≥ 1,000/quarter | Schedule H | US-FEDS5-029 |
| Agricultural | — | 150/worker or 2,500 total | farm tests | Form 943 | US-FEDR3-006 |

FUTA credit reductions: **final 2025** CA 1.2%, USVI 4.5%. **Potential 2026** CA 5.3%, USVI 4.8%, final only if the advance is unpaid on 2026-11-10 [US-FEDS5-009, partial]. Do not model 2026 as final.

The oracle is the two Pub. 15-T 2026 examples: NRA 526.90 → 31, and tribal 6,000 → 584.09 [US-FED-027]. Stage 9b re-derives the rest from Worksheet 1A and the Annual Percentage Method tables. The 2027 OASDI base of 192,300 is carried at confidence medium: ssa.gov returned 403 on 2026-11-02 [US-FED-022].

### Multistate routing (global_baseline, `multi.*`)

- **Reciprocity:** 16 jurisdictions are keyed in `multi.reciprocity.{st}.partners` (30 bilateral pairs). AZ is unilateral (`multi.reciprocity.az.unilateral`). Local taxes sit outside reciprocity: MI cities, IN counties, PA EIT, OH municipal and school-district tax, MD county special nonresident rate.
- **Nonresident day/dollar thresholds:** 15 jurisdictions, `multi.nonresident_threshold.{st}.rule`. LA moved to 30 days from 2026-01-01 [US-MULTIS5-021; LR 52:358, US-LAS5-002].
- **Resident credit operates at assessment** unless the residence state prescribes difference withholding (CT, KS, VT, MA, MN, MS, NJ, UT). The WTC must not model the credit as a payroll deduction.
- **MS correction (journal):** MS **does** withhold for residents working out of state, except to the extent the work state withholds [US-MSS5-019]. MULTI.md §2.2 is wrong for MS.
- **SUI localization:** localized > base of operations > direction/control > residence [US-MULTIS5-016]. PFML/SDI premium state = `sui_state` unless a state unit says otherwise: DC PFL uses a >50% work-time test [US-DCS5-007]; DE Paid Leave follows the principal work location.

---

## 2. country_specific: withholding methods and the traps from the journal

| Trap | Rule for the WTC/engine | register_id |
|---|---|---|
| SC Act 110 (1.99/5.21%) | Assessment for 2026 only; withholding stays on WH-1603 (0/3/6%) | US-SCS5-001, US-SCS5-004 |
| WI W-166 vs statute | Withholding uses W-166 3.54/4.65/5.30/7.65; the assessment brackets 3.50/4.40/5.30/7.65 must not enter the WTC | US-WIS5-011, US-WIS5-010 |
| NE Circular EN vs 77-2715.03 | Table rates 2.26–4.60%; statutory 4.55% top is assessment only. 24+ employees: minimum 1.5% | US-NES5-010, US-NES5-018 |
| KS KW-100 header | Header says 2021; figures are the 2024 values (5.2/5.58%). Ignore the header. No cut for 2026 or 2027 | US-KSS5-001, US-KSS5-003 |
| OH | Statute flat 2.75% above 26,050 (assessment); withholding schedule graduated to 3.4%. Mid-year table change on 2026-08-01; supplemental 2.75% | US-OHS5-007, US-OHS5-001, US-OHS5-017 |
| MI tips/overtime (2025 PA 24) | Assessment only; no withholding change (a tier-B summary said otherwise) | US-MIS5-015 |
| GA HB 463 | 5.19% withheld to 2026-05-10, 4.99% from 2026-05-11; retroactive at assessment. Tip/OT subtractions at assessment | US-GA-001, US-GAS5-009 |
| AL Act 2026-604 overtime | Assessment only; W-2 TT informational. AL deducts FIT from the AL base: compute FIT first | US-ALS5-004, US-ALS5-001 |
| CO OBBBA overtime | Not followed; overtime stays subject to CO withholding | US-COS5-007 |
| ME W-4 Step 4(b) | Not followed; ME withholding standard deduction 12,450/27,750 (not 15,300/30,600) | US-MES5-011 |
| MN | IRC conformity to 2023-05-01; H.R. 1 not adopted for withholding | US-MNS5-010 |
| HI Act 35 | Conforms to IRC 224 tips deduction; not to IRC 225 overtime (assessment) | US-HIS5-029 |
| IA OBBBA | Tips/overtime at assessment; senior deduction may be a W-4 allowance; rounding to the **cent** | US-IAS5-019, US-IAS5-005 |
| VA 2027 standard deduction | Statute 9,200/18,400 vs guide 3,000; neither is modelled until Virginia Tax publishes the 2027 formula | US-VAS5-018, US-VAS5-013 |
| DC 2026 method | Act 26-416 repealed personal exemptions; no 2026 withholding method published (D-4 under review): **blocking** unresolved | US-DCS5-021, US-DCS5-013 |
| CT tables vs TPG-211 rules | Differ by up to 0.48 per period; the engine must choose one (CT-OQ-1). Examples 17.65/39.97/78.82 are table results | US-CTS5-010 |
| MA tables vs percentage method | Differ by up to 0.02/week; use one method consistently | US-MAS5-024 |
| MS tables vs formula | Tables built at band upper bound; the two may differ by 1 USD; both authorised | US-MSS5-003 |
| ND booklet example | Printed 14 (734/yr) is stale; table/formula gives 13 (701.51/yr). Oracle uses the formula | US-NDS5-001 |
| NY example 2 | Booklet 258.51 vs re-derivation 258.50 (1-cent residual) | US-NY-P5-2-001 |
| OR publication | Federal subtraction cap 8,500 vs 8,750 inside the same publication; build on 8,750 (pp. 6–7). Example 1 prints 1,798; the arithmetic gives 1,789 | US-ORS5-009 |
| KY formula sheet | 35,730 is a typo for 35,640; the per-period result is 47.98 (the sheet prints 47) | US-KY-002 |
| ID mid-year | Tables changed on 2026-07-23 (16,100/32,200, prospective, no catch-up). The H1 edition (15,000/30,000) row is superseded | US-IDS5-011, US-IDS5-012 |
| UT Pub 14 effective date | Not stated; 2026-06-01 is tier B only: **blocking** unresolved | US-UT-PIT-003 |
| IN | DN#1 R47/10-26 from 2026-10-01; only the Boone county rate changed (0.0171). Supplemental flat 2.95% + county | US-INS5-007 |
| AR Act 1/2026 | Top 3.7% from 2026-01-01; table switch date not stated | US-ARS5-001 |
| WV SB 392 | Retroactive to 2026-01-01; table switch date not stated | US-WVS5-012 |
| MD | Biweekly/semimonthly exemption values are **truncated**; lump-sum bonus 6.50% + county top rate | US-MDS5-021 |
| NC NRA add-on | Rounded **up** (11/21/22/44); the general rule is nearest dollar | US-NC-001 |
| MT | Withholding rounded **up** to the next dollar; 2027 top 5.4% enacted, tables not published | US-MTS5-022 |

**Supplemental rates (flat options), 2026:**

| Rate | Jurisdictions |
|---|---|
| Federal | 22 / 37 |
| CA | 10.23 bonus & stock options, 6.6 other |
| NY | 11.70 (NYC/Yonkers supplemental rows superseded → unresolved) |
| MN | 6.25 |
| AL | 5 |
| KS | 5 |
| ME | 5 |
| MT | 5 |
| RI | 5.99 |
| NM | 5.9 |
| VA | 5.75 |
| OK | 4.5 |
| MO | 4.7 |
| NC | 4.09 |
| GA | rate in effect (4.99) |
| IA | 3.8 |
| AR | 3.7 |
| NE | 3.5 optional |
| ID | 5.3 |
| IN | 2.95 + county |
| OH | 2.75 |
| ND | 1.5 |
| OR | 8 |
| MI | 4.25 |
| PA | 3.07 (added to the period) |
| MA | 5 / 9 above the surtax threshold |
| MD | lump sum 6.50 + county top |
| WI | by estimated annual gross: 3.54 / 4.65 / 5.30 / 7.65 |
| VT | 30% of federal withholding |
| AZ | the elected A-4 % |
| Aggregate only | CT, DC, DE, HI, IL (wages), KY, LA, MS (top rate allowed), NJ, SC, UT (build rule), WV |

---

## 3. State non-conformity and wage-base differences (flags for the WTC)

**Income tax withholding base departs from federal:**

- **PA:** 401(k)/403(b)/457 deferrals **taxable** when made. Section 125 dependent care is taxable. GTL is never taxable (no 50k imputed income) [US-PAS5-011]. HSA payroll exclusion is open [US-PAS5-012].
- **NJ GIT:**
  - 403(b), 457 and other deferrals are taxable; 401(k) is excluded up to the federal limit.
  - HSA is **not excluded**.
  - IRC 129 dependent care and 137 adoption are included.
  - Section 125 is taxable except for qualifying plans [US-NJS5-006].
- **CA PIT:** HSA is taxable; the employer HSA contribution (code W) is added back. CA does not conform to OBBBA [US-CAS5-019, US-CAS5-020].
- **AL:** federal income tax withheld is a deduction. Agricultural wages do not follow federal [US-ALS5-001].
- **MA:** from TY2026 decoupled from same-year IRC amendments (c.62C s.90). Item-by-item treatment not read [US-MAS5-026].
- **WI:** box-16 wages are higher than federal for IRC 112, 127 student loans, 128 Trump accounts, 129 above the WI limit, and 132 moving/bicycle [US-WIS5-016].
- **NY:** public-employee 414(h) contributions are added back [US-NYS5-019]. The NYC 125 addback is open.
- **KS:** public-employer picked-up contributions are a KS addition. Withholding coverage is open [US-KSS5-028].
- **MN:** IRC as of 2023-05-01 [US-MNS5-010]. **SC:** IRC as of 2024-12-31 [US-SCS5-001].
- **Every other wage-taxing state:** follows federal withholding wages (conformity rows cited per state in the facts).

**SUI / SDI / PFML base departs from FUTA or from income tax:**

| Item | Treatment and states |
|---|---|
| 401(k) elective deferral **excluded** from UI (FUTA includes it) | AK [US-AKS5-005], RI (UI/TDI also excludes 125) [US-RIS5-017] |
| 401(k) deferral **included** in UI | GA, MO, NE, OK, SD, UT, VA, WV, MT, NJ (where cash electable), CA UI/SDI [US-GAS5-006, US-MOS5-012, US-NES5-019, US-OKS5-006, US-SDS5-013, US-UTS5-004, US-VAS5-014, US-WVS5-016, US-MTS5-023, US-NJS5-017, US-CAS5-019] |
| Section 125 **included** in UI | AL (cash option) [US-ALS5-007], MT [US-MTS5-023], SD [US-SDS5-013], WV (cafeteria) [US-WVS5-016], NJ (where cash electable) [US-NJS5-017], AK (dependent care / group legal / cash elections) [US-AKS5-005] |
| Section 125 **excluded** from UI | AR, GA, MO, OK, VA, RI |
| HSA in CA UI/SDI | subject unless via cafeteria plan [US-CAS5-019] |
| Ohio municipal base | Medicare wages less 125, so 401(k) taxable [US-OHS5-013] |
| WA UI vs PFML | tips included for UI, excluded for PFML [US-WAS5-023]. 125/401(k) treatment for UI/PFML/WA Cares **open and blocking** |
| Other-state wage credit toward SUI base | YES: AL, CT, FL, KS, KY, ME, MI, MS, NC, NE, NH, RI, SC, VT, WV, WY. NO: IA, MT. Open: DC, MD (implied yes), MO, UT, others |

---

## 4. Tips and overtime (P.L. 119-21), state treatment

The federal deductions work at **assessment** only. The employer duty is reporting (W-2 TP/TT/TA, box 14b) [US-FEDS5-030, US-FEDS5-007]; TY2025 carried penalty relief only [US-FEDS5-013].

- **No state reduces withholding for them**, as far as the rows read show.
- **Assessment-level state subtractions:**
  - AL overtime, up to 1,000 [US-ALS5-004];
  - GA tips and overtime, 1,750 each [US-GAS5-009];
  - MI tips and overtime (MCL 206.30(1)(ee)) [US-MIS5-015];
  - HI tips only [US-HIS5-029];
  - IA conformity [US-IAS5-019];
  - DC from TY2026 [US-DCS5-021].
- **Expressly not followed:** CO overtime stays subject [US-COS5-007]; CA non-conformity [US-CAS5-020]; MN (H.R. 1 not adopted) [US-MNS5-010]; ME (Step 4(b) ignored) [US-MES5-011].
- **GA reporting:** RLA employees "GA OT" in box 14a; the G-7 collects quarterly totals from 2027 [US-GAS5-009].

---

## 5. Employer levies and employee-side programme contributions (US-OWN-007 list)

| Kind | Items | register_id |
|---|---|---|
| Employee UI | AK 0.50%, NJ 0.3825% (+ WF/SWF 0.0425%), PA 0.07% (uncapped) | facts `ak/nj/pa.sui.employee.rate` |
| SDI / TDI | CA 1.3% (no cap); NJ DI 0.19% (2027 0.24%); RI TDI 1.1% on 100,000; NY DBL 0.5% max 0.60/week; HI TDI up to 0.5%, max 7.50/week | per facts |
| PFML | CA (in SDI); NJ FLI 0.23% (2027 0.24%); NY PFL 0.432% max 411.91; WA 1.13% (2027 1.2%); OR 1.0% (60/40); CO 0.88% (2027 0.86%); CT 0.5% employee; DE 0.80%; MA 0.88% / 0.46%; MN 0.88%; ME 1.0% / 0.5%; DC 0.75% employer-only; MD 0.9% from 2027; VA from 2028-04-01 | per facts |
| LTC | WA Cares 0.58% employee, no cap | US-WAS5-016 |
| Transit | OR STT 0.1% employee; TriMet 0.8237%; LTD 0.80%; NY MCTMT | US-ORS5-011, US-ORP7-001/-002, US-NYP7-001 |
| UI add-ons inside or beside the rate | AL ESA 0.06; AR admin 0.1; CA ETT 0.1; DC admin 0.2; DE Op&Tech 0.2 (0.175 from 2027, billed separately); GA admin 0.06 (to 2026-12-31); HI E&T 0.01; ID workforce 0.03; MA COVID 0.178–2.716, EMAC 0.12/0.24/0.34, WTF 0.056; ME CSSF 0.14 + UPAF 0.17; MN workforce 0.1; MS WIT 0.20 (applicability unconfirmed); MT AFT 0.18; NV CEP 0.05; NH FBR −1.0; NY RSF 0.075; OH TCSF 0.15; RI JDA 0.21; SC DACA 0.06; SD admin 0.08, investment 0.55; TX ETIA 0.1; WY factors inside the rate | per facts |
| Employer payroll taxes on separate returns | NV MBT 1.17% (FI/mining 1.554%); Newark/Jersey City 1%; Seattle payroll expense tax and Social Housing 5% > 1M; St. Louis 0.5%; Pittsburgh 0.55%; Denver OPT employer 4.00/month; WV SB 1053 fee (figure unresolved); VT Child Care 0.44% (employee up to 0.11%) | per facts |
| Other | NM workers' comp fee 2.55 employer / 2.25 employee per quarter; WA L&I employee share 50% of three components; OR WBF 0.018/hour split; HI Prepaid Health Care employee max 1.5% | per facts |

---

## 6. Local income taxes (T3 piggyback vs T4 separate return)

| Type | Jurisdictions |
|---|---|
| T3 piggyback | IN county LIT (92 counties; Boone 0.0171 from 2026-10-01; range 0.005–0.03); MD county (22 flat + 2 graduated; max 3.30; nonresident special 2.25); NY NYC / Yonkers (on NYS-45) |
| T4 separate return | PA EIT (higher of resident and work rates; LST max 52) and Philadelphia 3.735/3.425 from 2026-07-01; OH municipal (work location, ≤1% without a vote) and school district (residence); MI Detroit 2.4/1.2 (Treasury) plus 23 self-administered cities (uniform 1/0.5); KY Louisville 1.45/2.2 and Lexington 2.25 plus others (list open); AL municipal occupational (Leeds 1%; no state list); CO OPT (Denver, Greenwood Village, Glendale; Sheridan tier C); DE Wilmington 1.25%; MO St. Louis / Kansas City 1%; OR Metro SHS 1% and Multnomah PFA 1.5/3% (≥ 200,000); WV city service fees (Charleston 3.00/week) |
| Confirmed none | AK, AZ, CA, CT, DC (DC is the local layer), FL, GA, HI, IA (surtaxes at assessment), ID, IL, KS, LA (constitutional bar), MA, ME, MN, MS, MT, NC (prohibited), ND, NE, NH, NJ (employee side), NM, NV, OK, RI, SC, SD, TN, TX, UT, VA, VT, WA (employee side), WI, WY |

---

## 7. Decisions taken in this synthesis

**MA PFML split.** For 2026 payroll, use the DFML 2026 table [US-MAS5-012]:

- family 0.18%, employee up to 100%;
- medical 0.70%, employee up to 40% (0.28) and employer 0.42;
- total 0.88% for 25+ covered individuals, 0.46% below 25.

From **2027-01-01**, use the swapped split (family 0.70 at 40% employee; medical 0.18 at 100% employee).

The reasons:

- c.175M s.7(e) gives DFML the annual rate setting and the remittance table.
- Ch. 101 s.45's "taxable years beginning on or after January 1, 2026" is income-tax wording.
- DFML, the administering authority, applies ss.25–26 from 2027-01-01.
- The total 0.88% is identical either way; only the employee/employer split moves.

The conflicting row is US-MAS5-026. The residual risk is retroactive re-splitting of 2026 if DFML or DOR issue contrary transition guidance. Fact `ma.pfml.split.decision` (confidence medium); unresolved `ma.pfml.split.transition`.

**Other choices:**

- ME UPAF 0.17% (not 0.16%).
- OR federal subtraction cap 8,750.
- ND oracle from formula/table (not the booklet example).
- CT: no choice made; owner/engine decision (CT-OQ-1, unresolved).
- NY supplemental 11.70% re-pointed from the superseded US-NY-011 to the active US-NY-001. The NYC and Yonkers supplemental rates have no active row and stay unresolved.

---

## 8. Oracle collection (C37)

Every reproduced worked example is a fact under `{jur}.oracle.*` with its register_id, and residuals are noted in `note`. The full list is generated in §10 (keys containing `.oracle.`). Summary:

| Jurisdiction | Example and result |
|---|---|
| FED | 31 / 584.09 |
| CA | DE 44 E 4.13, F 7.17 |
| GA | 27.03 |
| MN | 91.27 |
| MI | 75.36; Detroit 47.45 |
| OH | 45.13 |
| NY | 8.01 / 258.51 (residual 1c) / 3,576.63 / 44.10 |
| IL | 32.13 |
| WI | 7.59 / 14.34 / 22.08 |
| VT | 45.77 |
| CT | 17.65 / 39.97 / 78.82 (tables; rules differ by up to 0.48) |
| MO | 707.81/yr |
| ME | 0 / 33 / 257 |
| NC | 4 |
| LA | 13.98 / 111.54 |
| AL | 29.59 |
| IN | 13.96 + 4.73 |
| OK | 37.00 |
| RI | 87.57 |
| HI | 9.58 |
| AR | 36.50 |
| ND | 13 (booklet prints 14 → stale) and 10 |
| UT | 12 / 116 / 18 / 347 / 367 / 5 (carried in unresolved because of the id-format defect) |
| IA | example 6 = 114.92 (derived; the other 9 formula examples reproduced in Stage 5 but are not individually transcribed) |
| MS | table row 9 |
| DE | 13.88 / 269.63 |
| KY | 47.98 |
| SC | 10.58 |
| ID | 31 |
| NM | 41.80 |
| OR | 1,789/yr |

---

## 9. Special populations (US-OWN-005) and language seams (US-OWN-006), as they bear on the WTC

**Special populations.** All populations are IN at the federal layer [US-OWN-005]. The wage-type consequences are in §1 (NRA, minister, statutory employee, household, agricultural). State-level carries:

- WA Cares NIV auto-exemption [US-WAS5-016].
- Household withholding is not required in MO and is by agreement in CA/MA; HI **requires** it on domestic and agricultural wages [US-MOS5-001, US-CAS5-004, US-MAS5-013, US-HIS5-004].
- AL does not follow federal on agricultural wages.
- Ministers are excluded from MS, OR, OK, HI and PA withholding.
- MT does not apply NRA treaty exclusions at withholding (assessment) and exempts H-2A workers [US-MTS5-005].
- OK NRA 8% (open) [US-OKS5-014].
- GA NRA: an 8233 copy must go to DOR [US-GAS5-004].
- AK UI covers dependent care and cash elections.
- Corporate-officer UI opt-outs: ID, OR, SC, ND (UI only; OR Paid Leave cannot be opted out).

**Language seams.** The payslip and authority-facing filings are in English [US-OWN-006]. Wage-type names in the WTC therefore stay English. Some state labels are fixed by the authority and must be reproduced verbatim: ME W-2 box 14 "MEPFML" [US-MES5-024]; OR local W-2 names "METRO" and "MULT" [US-ORS5-024]; WA paystub label "WA Cares Fund" [US-WAS5-016]; CA "VPDI" [US-CAS5-018]. The es-rank-2 seams (notices and posters) do not touch wage-type naming.

---

## 10. Per-jurisdiction facts (generated from the two facts files; value, effective dates, register_id)


### FED (global_baseline)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `fed.fica.oasdi.employee.rate` | 6.2 | percent | 2026-01-01 |  | US-FEDS5-005 (A.2) | high |
| `fed.fica.oasdi.employer.rate` | 6.2 | percent | 2026-01-01 |  | US-FEDS5-005 (A.2) | high |
| `fed.fica.oasdi.wage_base` | 184500 | USD | 2026-01-01 |  | US-FEDS5-005 (A.2) | high |
| `fed.fica.oasdi.wage_base` | 192300 | USD | 2027-01-01 |  | US-FED-022 (A.2) | medium |
| `fed.fica.medicare.employee.rate` | 1.45 | percent | 2026-01-01 |  | US-FEDS5-005 (A.2) | high |
| `fed.fica.medicare.employer.rate` | 1.45 | percent | 2026-01-01 |  | US-FEDS5-005 (A.2) | high |
| `fed.fica.medicare.wage_base.capped` | no |  | 2026-01-01 |  | US-FEDS5-005 (A.2) | high |
| `fed.fica.addl_medicare.employee.rate` | 0.9 | percent | 2026-01-01 |  | US-FEDS5-005 (A.2) | high |
| `fed.fica.addl_medicare.threshold` | 200000 | USD | 2026-01-01 |  | US-FEDS5-005 (A.2) | high |
| `fed.futa.gross.rate` | 6.0 | percent | 2025-01-01 |  | US-FED-007 (A.2) | high |
| `fed.futa.net.rate` | 0.6 | percent | 2025-01-01 |  | US-FED-007 (A.2) | high |
| `fed.futa.wage_base` | 7000 | USD | 2025-01-01 |  | US-FED-007 (A.2) | high |
| `fed.futa.credit_reduction.ca.rate` | 1.2 | percent | 2025-01-01 | 2025-12-31 | US-FEDS5-009 (A.2) | medium |
| `fed.futa.credit_reduction.vi.rate` | 4.5 | percent | 2025-01-01 | 2025-12-31 | US-FEDS5-009 (A.2) | medium |
| `fed.futa.credit_reduction.ca.potential.rate` | 5.3 | percent | 2026-01-01 |  | US-FEDS5-009 (A.2) | low |
| `fed.futa.credit_reduction.vi.potential.rate` | 4.8 | percent | 2026-01-01 |  | US-FEDS5-009 (A.2) | low |
| `fed.fit.method` | Pub. 15-T 2026 Worksheet 1A + Annual Percentage Method tables (STANDARD / Step-2-checked schedules); wage-bracket tables alternative |  | 2026-01-01 |  | US-FEDS5-001 (A.2) | high |
| `fed.fit.worksheet1a.line1g.mfj` | 12900 | USD | 2026-01-01 |  | US-FEDS5-001 (A.2) | high |
| `fed.fit.worksheet1a.line1g.other` | 8600 | USD | 2026-01-01 |  | US-FEDS5-001 (A.2) | high |
| `fed.fit.pre2020_allowance.value` | 4300 | USD | 2026-01-01 |  | US-FEDS5-001 (A.2) | high |
| `fed.fit.standard.single.thresholds` | 0/7500/19900/57900/113200/209275/263725/648100 |  | 2026-01-01 |  | US-FEDS5-001 (A.2) | high |
| `fed.fit.standard.mfj.thresholds` | 0/19300/44100/120100/230700/422850/531750/788000 |  | 2026-01-01 |  | US-FEDS5-001 (A.2) | high |
| `fed.fit.standard.hoh.thresholds` | 0/15550/33250/83000/121250/217300/271750/656150 |  | 2026-01-01 |  | US-FEDS5-001 (A.2) | high |
| `fed.fit.rates` | 0/10/12/22/24/32/35/37 |  | 2026-01-01 |  | US-FEDS5-001 (A.2) | high |
| `fed.fit.standard_deduction.single` | 16100 | USD | 2026-01-01 |  | US-FEDS5-010 (A.2) | high |
| `fed.fit.standard_deduction.mfj` | 32200 | USD | 2026-01-01 |  | US-FEDS5-010 (A.2) | high |
| `fed.fit.standard_deduction.hoh` | 24150 | USD | 2026-01-01 |  | US-FEDS5-010 (A.2) | high |
| `fed.fit.supplemental.optional_flat.rate` | 22 | percent | 2026-01-01 |  | US-FEDS5-003 (A.2) | high |
| `fed.fit.supplemental.mandatory.rate` | 37 | percent | 2026-01-01 |  | US-FEDS5-003 (A.2) | high |
| `fed.fit.supplemental.mandatory.threshold` | 1000000 | USD | 2026-01-01 |  | US-FEDS5-003 (A.2) | high |
| `fed.fit.backup_withholding.rate` | 24 | percent | 2026-01-01 |  | US-FEDS5-003 (A.2) | high |
| `fed.fit.rounding` | Wages may be rounded to the dollar; per-period tax may be rounded to nearest dollar (optional) |  | 2026-01-01 |  | US-FED-001 (A.2) | high |
| `fed.fit.nra_addon.table2.weekly` | 309.6 | USD | 2026-01-01 |  | US-FEDS5-002 (A.2) | high |
| `fed.fit.nra_addon.table2.biweekly` | 619.2 | USD | 2026-01-01 |  | US-FEDS5-002 (A.2) | high |
| `fed.fit.nra_addon.table2.semimonthly` | 670.8 | USD | 2026-01-01 |  | US-FEDS5-002 (A.2) | high |
| `fed.fit.nra_addon.table2.monthly` | 1341.7 | USD | 2026-01-01 |  | US-FEDS5-002 (A.2) | high |
| `fed.fit.nra_addon.table2.annual` | 16100 | USD | 2026-01-01 |  | US-FEDS5-002 (A.2) | high |
| `fed.fit.nra_addon.table1.weekly` | 226.9 | USD | 2026-01-01 |  | US-FEDS5-002 (A.2) | high |
| `fed.fit.nra_addon.table1.annual` | 11800 | USD | 2026-01-01 |  | US-FEDS5-002 (A.2) | high |
| `fed.fit.nra_addon.applies_to_supplemental_flat` | no |  | 2026-01-01 |  | US-FEDS5-002 (A.2) | high |
| `fed.fit.nra.w4_rule` | Single/MFS, write NRA below 4(c), cannot claim exempt |  | 2026-01-01 |  | US-FEDS5-015 (A.3) | high |
| `fed.fit.treaty_exempt_wages.reporting` | Form 8233 treaty-exempt wages reported on 1042-S, not W-2 box 1 |  | 2026-01-01 |  | US-FEDS5-016 (A.2) | high |
| `fed.obbba.tips_deduction.level` | assessment (withholding only via W-4 Step 4(b); employer reports W-2 box 12 TP + 14b) |  | 2026-01-01 |  | US-FEDS5-030 (A.2) | high |
| `fed.obbba.tips_deduction.cap` | 25000 | USD | 2025-01-01 | 2028-12-31 | US-FEDS5-030 (A.2) | high |
| `fed.obbba.overtime_deduction.cap.single` | 12500 | USD | 2025-01-01 | 2028-12-31 | US-FEDS5-030 (A.2) | high |
| `fed.obbba.overtime_deduction.cap.mfj` | 25000 | USD | 2025-01-01 | 2028-12-31 | US-FEDS5-030 (A.2) | high |
| `fed.w2.box12.code.tp` | cash tips (qualified tips reporting) |  | 2026-01-01 |  | US-FEDS5-007 (A.2) | high |
| `fed.w2.box12.code.tt` | qualified overtime compensation (premium portion) |  | 2026-01-01 |  | US-FEDS5-007 (A.2) | high |
| `fed.w2.box12.code.ta` | Trump account employer contribution |  | 2026-01-01 |  | US-FEDS5-007 (A.2) | high |
| `fed.trump_account.employer_contribution.exclusion` | 2500 | USD | 2026-07-04 |  | US-FEDS5-030 (A.2) | high |
| `fed.w2.threshold.no_withholding` | 2000 | USD | 2026-01-01 |  | US-FEDS5-003 (A.2) | high |
| `fed.bik.transit.monthly_exclusion` | 340 | USD | 2026-01-01 |  | US-FEDS5-008 (A.2) | high |
| `fed.bik.parking.monthly_exclusion` | 340 | USD | 2026-01-01 |  | US-FEDS5-008 (A.2) | high |
| `fed.bik.dependent_care.exclusion` | 7500 | USD | 2026-01-01 |  | US-FEDS5-008 (A.2) | high |
| `fed.bik.educational_assistance.exclusion` | 5250 | USD | 2026-01-01 |  | US-FEDS5-008 (A.2) | high |
| `fed.bik.group_term_life.exclusion_coverage` | 50000 | USD | 2026-01-01 |  | US-FEDS5-008 (A.2) | high |
| `fed.bik.moving_expense.excluded` | no |  | 2026-01-01 |  | US-FEDS5-008 (A.2) | high |
| `fed.bik.health_fsa.salary_reduction_cap` | 3400 | USD | 2026-01-01 |  | US-FEDS5-010 (A.2) | high |
| `fed.bik.health_fsa.carryover` | 680 | USD | 2026-01-01 |  | US-FEDS5-010 (A.2) | high |
| `fed.plan.402g.elective_deferral.limit` | 24500 | USD | 2026-01-01 |  | US-FED-023 (A.2) | high |
| `fed.plan.402g.catch_up_50.limit` | 8000 | USD | 2026-01-01 |  | US-FED-023 (A.2) | high |
| `fed.plan.402g.catch_up_60_63.limit` | 11250 | USD | 2026-01-01 |  | US-FED-023 (A.2) | high |
| `fed.plan.simple.limit` | 17000 | USD | 2026-01-01 |  | US-FED-023 (A.2) | high |
| `fed.plan.hsa.self_only.limit` | 4400 | USD | 2026-01-01 |  | US-FED-024 (A.2) | high |
| `fed.plan.hsa.family.limit` | 8750 | USD | 2026-01-01 |  | US-FED-024 (A.2) | high |
| `fed.aca.affordability.rate` | 9.96 | percent | 2026-01-01 |  | US-FEDS5-011 (A.2) | high |
| `fed.household.fica.threshold` | 3000 | USD | 2026-01-01 |  | US-FEDS5-029 (A.2) | high |
| `fed.household.futa.quarter_threshold` | 1000 | USD | 2026-01-01 |  | US-FEDS5-029 (A.2) | high |
| `fed.household.fit.withholding` | only by agreement |  | 2026-01-01 |  | US-FEDS5-029 (A.2) | high |
| `fed.agricultural.fica.per_worker_threshold` | 150 | USD | 2026-01-01 |  | US-FEDR3-006 (A.2) | high |
| `fed.agricultural.fica.total_threshold` | 2500 | USD | 2026-01-01 |  | US-FEDR3-006 (A.2) | high |
| `fed.minister.withholding` | no FIT/FICA withholding (SE tax); voluntary FIT agreement allowed |  | 2026-01-01 |  | US-FED-030 (A.2) | high |
| `fed.statutory_employee.treatment` | FICA yes, FIT no |  | 2026-01-01 |  | US-FEDR3-005 (A.2) | high |
| `fed.severance.treatment` | wages for FIT, FICA and FUTA |  | 2026-01-01 |  | US-FEDS5-029 (A.2) | high |
| `fed.pfml.employee_contribution.w2` | State PFML employee contributions are W-2 wages (Rev. Rul. 2025-4, Notice 2026-6) |  | 2026-01-01 |  | US-FEDS5-007 (A.2) | high |
| `fed.oracle.nra_wage_bracket.result` | 31 | USD | 2026-01-01 |  | US-FED-027 (A.2) | high |
| `fed.oracle.tribal_monthly.result` | 584.09 | USD | 2026-01-01 |  | US-FED-027 (A.2) | high |

### MULTI (global_baseline)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `multi.reciprocity.dc.partners` | MD,VA (DC exempts all nonresidents) |  | 2026-01-01 |  | US-MULTI-016 (A.3) | high |
| `multi.reciprocity.ia.partners` | IL |  | 2026-01-01 |  | US-MULTI-018 (A.2) | high |
| `multi.reciprocity.il.partners` | IA,KY,MI,WI |  | 2026-01-01 |  | US-MULTIS5-023 (A.2) | high |
| `multi.reciprocity.in.partners` | KY,MI,OH,PA,WI |  | 2026-01-01 |  | US-IN-002 (A.2) | high |
| `multi.reciprocity.ky.partners` | IL,IN,MI,OH,VA(daily commuters),WV,WI |  | 2026-01-01 |  | US-MULTI-009 (A.3) | high |
| `multi.reciprocity.md.partners` | DC,PA,VA,WV |  | 2026-01-01 |  | US-MULTI-008 (A.2) | high |
| `multi.reciprocity.mi.partners` | IL,IN,KY,MN,OH,WI |  | 2026-01-01 |  | US-MULTI-010 (A.2) | high |
| `multi.reciprocity.mn.partners` | MI,ND |  | 2026-01-01 |  | US-MULTI-013 (A.2) | high |
| `multi.reciprocity.nd.partners` | MN,MT |  | 2026-01-01 |  | US-MULTI-014 (A.2) | high |
| `multi.reciprocity.nj.partners` | PA |  | 2026-01-01 |  | US-MULTI-011 (A.2) | high |
| `multi.reciprocity.oh.partners` | IN,KY,MI,PA,WV |  | 2026-01-01 |  | US-MULTI-005 (A.2) | high |
| `multi.reciprocity.pa.partners` | IN,MD,NJ,OH,VA,WV |  | 2026-01-01 |  | US-MULTI-007 (A.2) | high |
| `multi.reciprocity.va.partners` | DC,KY(daily commuters),MD,PA,WV |  | 2026-01-01 |  | US-MULTI-004 (A.2) | high |
| `multi.reciprocity.wi.partners` | IL,IN,KY,MI |  | 2026-01-01 |  | US-MULTI-006 (A.2) | high |
| `multi.reciprocity.wv.partners` | KY,MD,OH,PA,VA |  | 2026-01-01 |  | US-MULTI-015 (A.2) | high |
| `multi.reciprocity.az.unilateral` | AZ exempts residents of CA,IN,OR,VA (Form WEC); one-way |  | 2026-01-01 |  | US-MULTI-017 (A.2) | high |
| `multi.nonresident_threshold.al.rule` | 30 days (multi-state, qualifying home state); day 31+ all AL wages |  | 2026-01-01 |  | US-MULTI-021 (A.2) | high |
| `multi.nonresident_threshold.az.rule` | 60 days |  | 2026-01-01 |  | US-MULTI-017 (A.2) | high |
| `multi.nonresident_threshold.ct.rule` | 15 days |  | 2026-01-01 |  | US-CTP10-001 (A.2) | high |
| `multi.nonresident_threshold.il.rule` | more than 30 working days |  | 2026-01-01 |  | US-MULTIS5-023 (A.2) | high |
| `multi.nonresident_threshold.la.rule` | 30 days from 2026-01-01; from day 31 all days |  | 2026-01-01 |  | US-MULTIS5-021 (A.1) | high |
| `multi.nonresident_threshold.wv.rule` | 30 days |  | 2026-01-01 |  | US-MULTI-015 (A.2) | high |
| `multi.convenience_rule.states` | NY (20 NYCRR 132.18), PA (61 Pa. Code 109.8), NE (from 2025); retaliatory NJ (2023) and CT (2019) |  | 2026-01-01 |  | US-MULTIS5-013 (A.2) | high |
| `multi.sui.localization_test` | localized > base of operations > direction or control > residence |  | 2026-01-01 |  | US-MULTIS5-016 (A.2) | high |
| `multi.transport.motor_carrier.rule` | residence state only (49 USC 14503) |  | 2026-01-01 |  | US-MULTIS5-001 (A.1) | high |
| `multi.transport.rail.rule` | residence state only (49 USC 11502) |  | 2026-01-01 |  | US-MULTIS5-002 (A.1) | high |
| `multi.transport.air.rule` | residence state plus state with >50% of pay (49 USC 40116(f)) |  | 2026-01-01 |  | US-MULTIS5-003 (A.1) | high |
| `multi.military_spouse.rule` | election of servicemember residence, spouse residence or duty station (50 USC 4001) |  | 2026-01-01 |  | US-MULTIS5-005 (A.1) | high |
| `multi.mobile_workforce_bill.status` | not enacted (S.1443, H.R.10271) - do not model |  | 2026-01-01 |  | US-MULTIS5-025 (A.1) | high |
| `multi.no_wage_income_tax.states` | AK,FL,NV,NH,SD,TN,TX,WA,WY |  | 2026-01-01 |  | US-FED-P5-2-005 (id-format: in unresolved) | - |
| `multi.reciprocity.mt.partners` | ND |  | 2026-01-01 |  | US-MT-P5-1-004 (id-format: in unresolved) | - |
| `multi.nonresident_threshold.hi.rule` | 60 days (paid from office outside HI) |  | 2026-01-01 |  | US-HI-P5-1-002 (id-format: in unresolved) | - |
| `multi.nonresident_threshold.id.rule` | under 1,000 USD |  | 2026-01-01 |  | US-ID-P5-2-002 (id-format: in unresolved) | - |
| `multi.nonresident_threshold.me.rule` | more than 12 days AND more than 3,000 USD |  | 2026-01-01 |  | US-ME-P5-2-003 (id-format: in unresolved) | - |
| `multi.nonresident_threshold.mt.rule` | under 30 days and multi-state |  | 2026-01-01 |  | US-MT-P5-1-003 (id-format: in unresolved) | - |
| `multi.nonresident_threshold.ne.rule` | more than 7 days |  | 2026-01-01 |  | US-NE-P5-1-002 (id-format: in unresolved) | - |
| `multi.nonresident_threshold.nm.rule` | 15 days or fewer |  | 2026-01-01 |  | US-NM-P5-2-002 (id-format: in unresolved) | - |
| `multi.nonresident_threshold.ok.rule` | 300 USD per quarter |  | 2026-01-01 |  | US-OK-P5-1-002 (id-format: in unresolved) | - |
| `multi.nonresident_threshold.ut.rule` | 20 days |  | 2026-01-01 |  | US-UT-P5-1-002 (id-format: in unresolved) | - |
| `multi.nonresident_threshold.vt.rule` | 30 days (out-of-state employers) |  | 2026-01-01 |  | US-VT-P5-2-003 (id-format: in unresolved) | - |
| `multi.resident_credit.level` | assessment (not a payroll deduction) unless the residence state prescribes difference withholding |  | 2026-01-01 |  | US-AZ-WH-003 (id-format: in unresolved) | - |
| `multi.sui.employee_contribution.states` | AK, NJ, PA |  | 2026-01-01 |  | US-FED-P5-2-006 (id-format: in unresolved) | - |

### SPECIAL_POPULATION (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `special_population.wa_cares.niv_exempt` | non-immigrant work visa holders auto-exempt from WA Cares from 2026-01-01 unless they opt in in writing |  | 2026-01-01 |  | US-WAS5-016 (A.2) | high |
| `special_population.household.state_withholding` | not required in MO, MA (by agreement); HI requires on domestic/agricultural |  | 2026-01-01 |  | US-MOS5-001 (A.2) | medium |
| `special_population.agricultural.al` | AL does not follow federal withholding on agricultural cash wages |  | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `special_population.minister.ms_or` | ministers excluded from MS and OR withholding |  | 2026-01-01 |  | US-MSS5-004 (A.1) | high |

### AK (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ak.sit.applies` | no |  | 2026-01-01 |  | US-AKP9W-001 (A.2) | high |
| `ak.local.wage_tax.applies` | no |  | 2026-01-01 |  | US-AKR3-001 (A.2) | high |
| `ak.sui.wage_base` | 54200 | USD | 2026-01-01 |  | US-AKS5-003 (A.2) | high |
| `ak.sui.employee.rate` | 0.5 | percent | 2026-01-01 |  | US-AKS5-003 (A.2) | high |
| `ak.sui.employer.rate.classes_01_20` | 1.0 | percent | 2026-01-01 |  | US-AKS5-003 (A.2) | high |
| `ak.sui.employer.rate.class_21` | 5.4 | percent | 2026-01-01 |  | US-AKS5-003 (A.2) | high |
| `ak.sui.new_employer.rate` | 1.0 | percent | 2026-01-01 |  | US-AKS5-004 (A.2) | high |
| `ak.sui.abcr` | 0.004615 | ratio | 2026-01-01 |  | US-AKS5-006 (A.2) | high |
| `ak.sui.base.401k_deferral` | excluded (departs from FUTA) |  | 2026-01-01 |  | US-AKS5-005 (A.3) | medium |
| `ak.sui.base.cafeteria.dependent_care` | included (UI wages) |  | 2026-01-01 |  | US-AKS5-005 (A.3) | medium |
| `ak.sdi_pfml.applies` | no |  | 2026-01-01 |  | US-AKS5-001 (A.1) | high |

### AL (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `al.sit.method` | Booklet formula: annualise; minus standard deduction (phase-out), annualised FIT withheld, personal exemption, dependents; 2/4/5% |  | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.fit_deductible` | yes |  | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.rate.top` | 5 | percent | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.brackets.single` | 2% first 500; 4% next 2,500; 5% above 3,000 |  | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.brackets.married` | 2% first 1,000; 4% next 5,000; 5% above 6,000 |  | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.personal_exemption.single` | 1500 | USD | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.personal_exemption.married` | 3000 | USD | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.standard_deduction.single.max` | 3000 | USD | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.standard_deduction.married.max` | 8500 | USD | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.supplemental.rate` | 5 | percent | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.base.exclusions` | IRC 125, 219, 401(k), SIMPLE 401(k), 403(b), 408(k), 408(p), 457 excluded |  | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.severance.exempt_max` | 50000 | USD | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.sit.certificate` | A4 REV. 4/2025 (federal W-4 not accepted); default zero exemptions |  | 2026-01-01 |  | US-ALS5-005 (A.2) | high |
| `al.sit.overtime_deduction.level` | assessment only (Act 2026-604, 2026-2028, up to 1,000 premium); W-2 TT informational |  | 2026-01-01 |  | US-ALS5-004 (A.2) | high |
| `al.oracle.m2_weekly_850.result` | 29.59 | USD | 2026-01-01 |  | US-ALS5-001 (A.2) | high |
| `al.local.leeds.rate` | 1 | percent | 2026-01-01 |  | US-ALS5-017 (A.2) | high |
| `al.sui.wage_base` | 8000 | USD | 2026-01-01 |  | US-ALS5-009 (A.1) | high |
| `al.sui.new_employer.rate` | 2.7 | percent | 2026-01-01 |  | US-ALS5-007 (A.2) | high |
| `al.sui.employer.rate.min` | 0.2 | percent | 2026-01-01 |  | US-ALS5-007 (A.2) | high |
| `al.sui.employer.rate.max` | 6.8 | percent | 2026-01-01 |  | US-ALS5-007 (A.2) | high |
| `al.sui.esa.rate` | 0.06 | percent | 2026-01-01 |  | US-ALS5-007 (A.2) | high |
| `al.sui.employee.applies` | no |  | 2026-01-01 |  | US-ALR3-001 (A.2) | high |
| `al.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-ALS5-009 (A.1) | high |
| `al.sui.base.cafeteria_cash_option` | included (UC wages) |  | 2026-01-01 |  | US-ALS5-007 (A.2) | high |

### AR (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ar.sit.method` | DFA formula: annualise, minus 2,470 standard deduction, 100-band midpoint, bracket with subtraction, round to dollar, minus 29 credit per exemption |  | 2026-01-01 |  | US-ARS5-001 (A.2) | high |
| `ar.sit.standard_deduction` | 2470 | USD | 2026-01-01 |  | US-ARS5-001 (A.2) | high |
| `ar.sit.personal_credit` | 29 | USD | 2026-01-01 |  | US-ARS5-001 (A.2) | high |
| `ar.sit.rate.top` | 3.7 | percent | 2026-01-01 |  | US-ARS5-001 (A.2) | high |
| `ar.sit.brackets` | 0-5,599 0%; 5,600-11,199 2%-111.98; 11,200-15,999 3%-223.97; 16,000-26,399 3.4%-287.97; 26,400-94,700 3.7%-367.16; 97,601+ 3.7%-79.90 |  | 2026-01-01 |  | US-ARS5-001 (A.2) | high |
| `ar.sit.supplemental.rate` | 3.7 | percent | 2026-01-01 |  | US-ARS5-001 (A.2) | medium |
| `ar.oracle.monthly_2127_2ex.result` | 36.5 | USD | 2026-01-01 |  | US-ARS5-001 (A.2) | high |
| `ar.sit.low_income_tables` | AR4EC line 5: table-only low-income method (no formula) |  | 2026-01-01 |  | US-ARS5-011 (A.2) | high |
| `ar.sit.certificate` | AR4EC (R 12/04/2025); default zero exemptions |  | 2026-01-01 |  | US-ARS5-009 (A.2) | high |
| `ar.sui.wage_base` | 7000 | USD | 2026-01-01 |  | US-ARP9V-001 (A.3) | high |
| `ar.sui.new_employer.rate` | 2.0 | percent | 2026-01-01 |  | US-ARP9V-001 (A.3) | high |
| `ar.sui.employer.rate.min` | 0.2 | percent | 2026-01-01 |  | US-ARP9V-001 (A.3) | high |
| `ar.sui.employer.rate.max` | 5.1 | percent | 2026-01-01 |  | US-ARP9V-002 (A.2) | high |
| `ar.sui.base.section125` | excluded |  | 2026-01-01 |  | US-ARP9V-001 (A.3) | high |

### AZ (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `az.sit.method` | Flat % of gross taxable (federal) wages elected on A-4: 0.5/1.0/1.5/2.0/2.5/3.0/3.5; default 2.0 |  | 2026-01-01 |  | US-AZS5-024 (A.2) | high |
| `az.sit.default.rate` | 2.0 | percent | 2026-01-01 |  | US-AZS5-024 (A.2) | high |
| `az.sit.supplemental` | same elected percentage (no separate rate) |  | 2026-01-01 |  | US-AZS5-020 (A.1) | medium |
| `az.sit.base` | federal wages (IRC 3401); federal exclusions flow through |  | 2026-01-01 |  | US-AZS5-024 (A.2) | high |
| `az.sui.wage_base` | 8000 | USD | 2026-01-01 |  | US-AZR3-001 (A.2) | high |
| `az.sui.new_employer.rate` | 2.0 | percent | 2026-01-01 |  | US-AZR3-002 (A.2) | high |
| `az.sui.employer.rate.range` | 0.03%-8.36% |  | 2026-01-01 |  | US-AZR3-003 (A.2) | high |
| `az.sui.employee.applies` | no |  | 2026-01-01 |  | US-AZR3-001 (A.2) | high |
| `az.sui.operating_fund_diversion.rate` | 3.15 | percent | 2027-01-01 |  | US-AZR3-004 (A.2) | high |
| `az.local.wage_tax.applies` | no |  | 2026-01-01 |  | US-AZR3-006 (A.2) | high |

### CA (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ca.sit.method` | DE 44 Method A (wage bracket) or Method B (exact calculation) |  | 2026-01-01 |  | US-CAS5-001 (A.2) | high |
| `ca.sit.low_income_exemption.single` | 18896 | USD | 2026-01-01 |  | US-CAS5-001 (A.2) | high |
| `ca.sit.low_income_exemption.married_hoh` | 37791 | USD | 2026-01-01 |  | US-CAS5-001 (A.2) | high |
| `ca.sit.standard_deduction.single` | 5706 | USD | 2026-01-01 |  | US-CAS5-001 (A.2) | high |
| `ca.sit.standard_deduction.married_hoh` | 11412 | USD | 2026-01-01 |  | US-CAS5-001 (A.2) | high |
| `ca.sit.allowance_credit` | 168.3 | USD | 2026-01-01 |  | US-CAS5-001 (A.2) | high |
| `ca.sit.estimated_deduction_allowance` | 1000 | USD | 2026-01-01 |  | US-CAS5-001 (A.2) | high |
| `ca.sit.rate.top` | 14.63 | percent | 2026-01-01 |  | US-CAS5-001 (A.2) | high |
| `ca.sit.supplemental.bonus.rate` | 10.23 | percent | 2026-01-01 |  | US-CAS5-004 (A.2) | high |
| `ca.sit.supplemental.other.rate` | 6.6 | percent | 2026-01-01 |  | US-CAS5-004 (A.2) | high |
| `ca.sit.certificate` | DE 4 Rev. 56 (1-26); default Single 0 allowances |  | 2026-01-01 |  | US-CAS5-015 (A.2) | high |
| `ca.oracle.de44_example_f.result` | 7.17 | USD | 2026-01-01 |  | US-CAS5-001 (A.2) | high |
| `ca.oracle.de44_example_e.result` | 4.13 | USD | 2026-01-01 |  | US-CAS5-001 (A.2) | high |
| `ca.sui.wage_base` | 7000 | USD | 2026-01-01 |  | US-CAS5-016 (A.2) | high |
| `ca.sui.employer.rate.max` | 6.2 | percent | 2026-01-01 |  | US-CAP7-003 (A.2) | high |
| `ca.ett.rate` | 0.1 | percent | 2026-01-01 |  | US-CAP7-001 (A.2) | high |
| `ca.sdi.employee.rate` | 1.3 | percent | 2026-01-01 |  | US-CAP7-002 (A.2) | high |
| `ca.sdi.wage_cap.applies` | no |  | 2026-01-01 |  | US-CAP7-002 (A.2) | high |
| `ca.base.hsa.pit` | taxable (employer HSA code W added back) |  | 2026-01-01 |  | US-CAS5-020 (A.2) | high |
| `ca.base.hsa.ui_sdi` | subject unless through a cafeteria plan |  | 2026-01-01 |  | US-CAS5-019 (A.2) | high |
| `ca.base.401k_deferral.ui_sdi` | subject |  | 2026-01-01 |  | US-CAS5-019 (A.2) | high |
| `ca.base.401k_deferral.pit` | not subject |  | 2026-01-01 |  | US-CAS5-019 (A.2) | high |
| `ca.base.gtl_over_50k.ui_sdi` | not subject (PIT reportable, not withheld) |  | 2026-01-01 |  | US-CAS5-019 (A.2) | high |
| `ca.obbba.tips_overtime.conformity` | not conformed (no state deduction) |  | 2026-01-01 |  | US-CAS5-020 (A.2) | high |
| `ca.bik.meals.daily` | 15.85 | USD | 2026-01-01 |  | US-CAS5-003 (A.2) | high |
| `ca.bik.lodging.weekly_min` | 66.1 | USD | 2026-01-01 |  | US-CAS5-003 (A.2) | high |
| `ca.bik.lodging.monthly_max` | 2038 | USD | 2026-01-01 |  | US-CAS5-003 (A.2) | high |
| `ca.sui.max_per_employee` | 434 | USD | 2026-01-01 |  | US-CAS5-016 (A.2) | high |
| `ca.sui.new_employer.rate` | 3.4 | percent | 2026-01-01 |  | US-CA-EDD-001 (id-format: in unresolved) | - |
| `ca.sui.employer.rate.min` | 1.5 | percent | 2026-01-01 |  | US-CA-EDD-001 (id-format: in unresolved) | - |

### CO (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `co.sit.method` | Annualise, minus 5,500 (11,000 MFJ) or DR 0004 line 2, x4.40%, / periods, + DR 0004 line 3 (DR 1098) |  | 2026-01-01 |  | US-COS5-007 (A.2) | medium |
| `co.sit.rate` | 4.4 | percent | 2026-01-01 |  | US-COS5-012 (A.2) | high |
| `co.sit.obbba_overtime.withholding` | not followed: qualified overtime stays subject to CO withholding |  | 2026-01-01 |  | US-COS5-007 (A.2) | high |
| `co.sit.certificate` | IRS W-4 or optional DR 0004 (rev. 10/29/25) |  | 2026-01-01 |  | US-COS5-012 (A.2) | high |
| `co.local.denver.opt.employee.monthly` | 5.75 | USD | 2026-01-01 |  | US-COP7-004 (A.2) | medium |
| `co.local.denver.opt.employer.monthly` | 4.0 | USD | 2026-01-01 |  | US-COP7-005 (A.2) | medium |
| `co.local.greenwood_village.opt.employee.monthly` | 2 | USD | 2026-01-01 |  | US-COS5-015 (A.2) | high |
| `co.local.greenwood_village.opt.employer.monthly` | 2 | USD | 2026-01-01 |  | US-COS5-015 (A.2) | high |
| `co.local.glendale.opt.employee.monthly` | 5 | USD | 2026-01-01 |  | US-COS5-016 (A.2) | high |
| `co.local.glendale.opt.employer.monthly` | 5 | USD | 2026-01-01 |  | US-COS5-016 (A.2) | high |
| `co.famli.total.rate` | 0.86 | percent | 2027-01-01 |  | US-COS5-008 (A.2) | high |
| `co.famli.total.rate` | 0.88 | percent | 2026-01-01 |  | US-CO-FAMLI-001 (id-format: in unresolved) | - |
| `co.sui.wage_base` | 30600 | USD | 2026-01-01 |  | US-CO-P5-1-003 (id-format: in unresolved) | - |
| `co.sui.wage_base` | 32100 | USD | 2027-01-01 |  | US-CO-P5-1-003 (id-format: in unresolved) | - |
| `co.sui.new_employer.total.rate` | 3.05 | percent | 2026-01-01 |  | US-CO-P5-1-003 (id-format: in unresolved) | - |
| `co.sui.new_employer.total.rate` | 1.7 | percent | 2027-01-01 |  | US-CO-P5-1-004 (id-format: in unresolved) | - |

### CT (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ct.sit.method` | TPG-211 rules (16 steps) or IP 2026(1) tables; codes A/B/C/D/F; rates 2.0-6.99% |  | 2026-01-01 |  | US-CTS5-010 (A.2) | high |
| `ct.sit.rates` | 2.0/4.5/5.5/6.0/6.5/6.9/6.99 |  | 2026-01-01 |  | US-CTS5-010 (A.2) | high |
| `ct.sit.exemption.code_a` | 12000 | USD | 2026-01-01 |  | US-CTS5-010 (A.2) | high |
| `ct.sit.exemption.code_b` | 19000 | USD | 2026-01-01 |  | US-CTS5-010 (A.2) | high |
| `ct.sit.exemption.code_c` | 24000 | USD | 2026-01-01 |  | US-CTS5-010 (A.2) | high |
| `ct.sit.exemption.code_f` | 15000 | USD | 2026-01-01 |  | US-CTS5-010 (A.2) | high |
| `ct.sit.no_certificate.rate` | 6.99 | percent | 2026-01-01 |  | US-CTS5-011 (A.2) | high |
| `ct.sit.supplemental` | aggregate method only (no flat rate) |  | 2026-01-01 |  | US-CTS5-012 (A.2) | high |
| `ct.sit.method_choice.decision` | tables vs TPG-211 rules differ up to 0.48/period; engine must choose one (CT-OQ-1) |  | 2026-01-01 |  | US-CTS5-010 (A.2) | high |
| `ct.oracle.ip2026_ex8.result` | 17.65 | USD | 2026-01-01 |  | US-CTS5-010 (A.2) | high |
| `ct.oracle.ip2026_ex9.result` | 39.97 | USD | 2026-01-01 |  | US-CTS5-010 (A.2) | high |
| `ct.oracle.ip2026_ex10.result` | 78.82 | USD | 2026-01-01 |  | US-CTS5-010 (A.2) | high |
| `ct.sui.wage_base` | 27000 | USD | 2026-01-01 |  | US-CTS5-016 (A.1) | high |
| `ct.sui.new_employer.rate` | 1.9 | percent | 2026-01-01 |  | US-CTP9V-001 (A.2) | high |
| `ct.sui.employer.rate.range` | 0.1-8.9% plus 1.0% fund solvency (1.1-9.9%) |  | 2026-01-01 |  | US-CTP9V-001 (A.2) | high |
| `ct.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-CTS5-016 (A.1) | high |
| `ct.pfml.employee.rate` | 0.5 | percent | 2026-01-01 |  | US-CTS5-020 (A.1) | high |
| `ct.pfml.wage_base` | 184500 | USD | 2026-01-01 |  | US-CTP7-001 (A.2) | high |

### DC (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `dc.sit.method` | percentage method or tables similar to IRC 3402; no standard deduction allowance in withholding (47-1812.08(b)(1A)) |  | 2026-01-01 |  | US-DCS5-025 (A.1) | medium |
| `dc.sit.supplemental` | no flat rate; bonuses withheld as regular wages |  | 2026-01-01 |  | US-DCR3-001 (A.1) | high |
| `dc.sit.nonresident` | DC cannot tax nonresidents (Home Rule Act); D-4A stops withholding |  | 2026-01-01 |  | US-MULTI-016 (A.3) | high |
| `dc.obbba.deductions.level` | assessment only from TY2026 (D.C. Act 26-416) |  | 2026-01-01 |  | US-DCS5-021 (A.1) | high |
| `dc.sui.wage_base` | 9000 | USD | 2026-01-01 |  | US-DCS5-017 (A.1) | high |
| `dc.sui.new_employer.rate` | 2.7 | percent | 2026-01-01 |  | US-DCS5-016 (A.2) | high |
| `dc.sui.employer.rate.min` | 1.9 | percent | 2026-01-01 |  | US-DCS5-017 (A.1) | high |
| `dc.sui.employer.rate.max` | 7.4 | percent | 2026-01-01 |  | US-DCS5-017 (A.1) | high |
| `dc.sui.admin_assessment.rate` | 0.2 | percent | 2026-01-01 |  | US-DCP7-001 (A.2) | high |
| `dc.sui.employee.applies` | no |  | 2026-01-01 |  | US-DCS5-017 (A.1) | high |
| `dc.pfl.employer.rate` | 0.75 | percent | 2026-01-01 |  | US-DCS5-020 (A.1) | high |
| `dc.pfl.wage_cap.applies` | no |  | 2026-01-01 |  | US-DCS5-020 (A.1) | high |
| `dc.sit.rates` | 4% to 10,000; 400+6% to 40,000; 2,200+6.5% to 60,000; 3,500+8.5% to 250,000; 19,650+9.25% to 500,000; 42,775+9.75% to 1,000,000; 91,525+10.75% above |  | 2026-01-01 |  | US-DC-P5-2-001 (id-format: in unresolved) | - |

### DE (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `de.sit.method` | Annualise; minus standard deduction 3,250 single / 6,500 MFJ; table 0/66/261/741/1,001/2,943.50 + marginal; minus 110 per exemption; / periods |  | 2026-01-01 |  | US-DES5-006 (A.2) | high |
| `de.sit.rates` | 0% to 2,000; 2.2% to 5,000; 3.9% to 10,000; 4.8% to 20,000; 5.2% to 25,000; 5.55% to 60,000; 6.6% above |  | 2014-01-01 |  | US-DES5-003 (A.1) | high |
| `de.sit.standard_deduction.single` | 3250 | USD | 2026-01-01 |  | US-DES5-006 (A.2) | high |
| `de.sit.standard_deduction.mfj` | 6500 | USD | 2026-01-01 |  | US-DES5-006 (A.2) | high |
| `de.sit.personal_credit` | 110 | USD | 2026-01-01 |  | US-DES5-006 (A.2) | high |
| `de.sit.supplemental` | aggregate: with regular wages one payment; separately annualised-with minus annualised-without; deferred comp recommended 5% |  | 2026-01-01 |  | US-DES5-006 (A.2) | high |
| `de.oracle.guide_ex1.result` | 13.88 | USD | 2026-01-01 |  | US-DES5-006 (A.2) | high |
| `de.oracle.guide_ex2.result` | 269.63 | USD | 2026-01-01 |  | US-DES5-006 (A.2) | high |
| `de.sit.certificate` | federal W-4 (exemption mapping for 2020+ W-4 open) |  | 2026-01-01 |  | US-DES5-008 (A.3) | medium |
| `de.sui.wage_base` | 14500 | USD | 2026-01-01 |  | US-DES5-010 (A.1) | high |
| `de.sui.wage_base` | 16500 | USD | 2027-01-01 |  | US-DES5-010 (A.1) | high |
| `de.sui.new_employer.rate` | 1.0 | percent | 2026-01-01 |  | US-DES5-022 (A.2) | high |
| `de.sui.employer.rate.min` | 0.3 | percent | 2026-01-01 |  | US-DES5-022 (A.2) | high |
| `de.sui.employer.rate.max` | 5.4 | percent | 2026-01-01 |  | US-DES5-022 (A.2) | high |
| `de.sui.op_tech_assessment.rate` | 0.2 | percent | 2026-01-01 |  | US-DEP7-001 (A.2) | high |
| `de.sui.op_tech_assessment.rate` | 0.175 | percent | 2027-01-01 |  | US-DEP7-001 (A.2) | high |
| `de.pfml.total.rate` | 0.8 | percent | 2026-01-01 |  | US-DES5-012 (A.1) | high |
| `de.pfml.medical.rate` | 0.4 | percent | 2026-01-01 |  | US-DES5-012 (A.1) | high |
| `de.pfml.family_caregiving.rate` | 0.08 | percent | 2026-01-01 |  | US-DES5-012 (A.1) | high |
| `de.pfml.parental.rate` | 0.32 | percent | 2026-01-01 |  | US-DES5-012 (A.1) | high |
| `de.pfml.employee_share.max` | 50 | percent | 2026-01-01 |  | US-DES5-012 (A.1) | high |
| `de.local.wilmington.eit.rate` | 1.25 | percent | 2026-01-01 |  | US-DE-P5-2-001 (id-format: in unresolved) | - |

### FL (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `fl.sit.applies` | no |  | 2026-01-01 |  | US-FL-001 (A.1) | high |
| `fl.sui.wage_base` | 7000 | USD | 2026-01-01 |  | US-FLS5-003 (A.1) | high |
| `fl.sui.new_employer.rate` | 2.7 | percent | 2026-01-01 |  | US-FLS5-004 (A.1) | high |
| `fl.sui.employer.rate.min` | 0.1 | percent | 2026-01-01 |  | US-FLS5-018 (A.2) | high |
| `fl.sui.employer.rate.max` | 5.4 | percent | 2026-01-01 |  | US-FLS5-018 (A.2) | high |
| `fl.sui.employee.applies` | no |  | 2026-01-01 |  | US-FLS5-004 (A.1) | high |
| `fl.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-FLS5-020 (A.3) | high |
| `fl.sui.rounding` | fraction under half a cent dropped; half cent or more rounds up |  | 2026-01-01 |  | US-FLS5-004 (A.1) | high |

### GA (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ga.sit.rate` | 4.99 | percent | 2026-05-11 |  | US-GAS5-009 (A.1) | high |
| `ga.sit.rate` | 5.19 | percent | 2026-01-01 | 2026-05-10 | US-GA-001 (A.2) | high |
| `ga.sit.standard_deduction.single` | 15000 | USD | 2026-01-01 |  | US-GAS5-001 (A.2) | high |
| `ga.sit.standard_deduction.mfj` | 30000 | USD | 2026-01-01 |  | US-GAS5-001 (A.2) | high |
| `ga.sit.dependent_allowance` | 5000 | USD | 2026-01-01 |  | US-GAS5-001 (A.2) | high |
| `ga.sit.method` | tables or percentage method (Tables E/F): wages - std deduction - 5,000 x allowances, x 4.99% |  | 2026-01-01 |  | US-GAS5-001 (A.2) | high |
| `ga.sit.supplemental` | rate in effect when paid (4.99% from 2026-05-11) |  | 2026-01-01 |  | US-GAS5-004 (A.2) | high |
| `ga.oracle.mfj_semimonthly_2000.result` | 27.03 | USD | 2026-01-01 |  | US-GAS5-001 (A.2) | high |
| `ga.sit.tips_overtime.level` | assessment only (HB 463 subtractions up to 1,750 each); do not reduce withholding |  | 2026-01-01 |  | US-GAS5-009 (A.1) | high |
| `ga.sui.new_employer.rate` | 2.64 | percent | 2026-01-01 |  | US-GAS5-013 (A.1) | high |
| `ga.sui.admin_assessment.rate` | 0.06 | percent | 2026-01-01 | 2026-12-31 | US-GAS5-013 (A.1) | high |
| `ga.sui.new_employer.rate` | 2.7 | percent | 2027-01-01 |  | US-GAS5-013 (A.1) | high |
| `ga.sui.base.401k_deferral` | included (UI wages) |  | 2026-01-01 |  | US-GAS5-006 (A.3) | high |
| `ga.sui.base.section125` | excluded |  | 2026-01-01 |  | US-GAS5-006 (A.3) | high |
| `ga.sui.wage_base` | 9500 | USD | 2013-01-01 |  | US-GA-W1B-001 (id-format: in unresolved) | - |

### HI (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `hi.sit.method` | Booklet A (Rev. 2025): wage-bracket tables, annualised formula or per-period formula |  | 2026-01-01 |  | US-HIS5-004 (A.2) | high |
| `hi.sit.allowance` | 1144 | USD | 2026-01-01 |  | US-HIS5-004 (A.2) | high |
| `hi.sit.lump_sum_allowance` | 4350 | USD | 2026-01-01 |  | US-HIS5-004 (A.2) | high |
| `hi.sit.brackets.single` | 1.4% to 9,600; 134+3.2% to 14,400; 288+5.5% to 19,200; 552+6.4% to 24,000; 859+6.8% to 36,000; 1,675+7.2% to 48,000; 2,539+7.6% to 125,000; 8,391+7.9% above |  | 2026-01-01 |  | US-HIS5-004 (A.2) | high |
| `hi.sit.brackets.married` | 1.4% to 19,200; 269+3.2% to 28,800; 576+5.5% to 38,400; 1,104+6.4% to 48,000; 1,718+6.8% to 72,000; 3,350+7.2% to 96,000; 5,078+7.6% to 250,000; 16,782+7.9% above |  | 2026-01-01 |  | US-HIS5-004 (A.2) | high |
| `hi.sit.supplemental` | no flat rate; aggregate or average |  | 2026-01-01 |  | US-HIS5-004 (A.2) | high |
| `hi.oracle.single3_weekly500.result` | 9.58 | USD | 2026-01-01 |  | US-HIS5-004 (A.2) | high |
| `hi.sit.certificate` | HW-4 (Rev. 2022); no exempt status; default Single 0 |  | 2026-01-01 |  | US-HIS5-026 (A.2) | high |
| `hi.sit.tips_overtime.conformity` | conforms to IRC 224 tips deduction; not to IRC 225 overtime (assessment level) |  | 2026-01-01 |  | US-HIS5-029 (A.2) | high |
| `hi.sui.wage_base` | 64500 | USD | 2026-01-01 |  | US-HIS5-010 (A.1) | high |
| `hi.sui.new_employer.rate` | 2.4 | percent | 2026-01-01 |  | US-HIP9V-001 (A.2) | high |
| `hi.sui.employer.rate.max` | 5.6 | percent | 2026-01-01 |  | US-HIP9V-001 (A.2) | high |
| `hi.sui.et_assessment.rate` | 0.01 | percent | 2026-01-01 |  | US-HIS5-011 (A.2) | high |
| `hi.sui.employee.applies` | no |  | 2026-01-01 |  | US-HIS5-010 (A.1) | high |
| `hi.tdi.employee.rate.max` | 0.5 | percent | 2026-01-01 |  | US-HIS5-014 (A.1) | high |
| `hi.tdi.employee.weekly_cap` | 7.5 | USD | 2026-01-01 |  | US-HIS5-015 (A.2) | high |
| `hi.tdi.max_weekly_wage_base` | 1500.21 | USD | 2026-01-01 |  | US-HIS5-015 (A.2) | high |
| `hi.phc.monthly_wage_threshold` | 1387 | USD | 2026-01-01 |  | US-HIS5-015 (A.2) | high |
| `hi.phc.employee.rate.max` | 1.5 | percent | 2026-01-01 |  | US-HIS5-015 (A.2) | high |
| `hi.sui.et_assessment.rate.2026` | 0.01 | percent | 2026-01-01 |  | US-HIL-003 (A.2) | high |

### IA (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ia.sit.rate` | 3.8 | percent | 2025-01-01 |  | US-IAS5-006 (A.1) | high |
| `ia.sit.method` | T1=G-D; T2=T1x3.80%; T3=T2-W/P; T4=T3+A (2026 formula) |  | 2026-01-01 |  | US-IAS5-005 (A.2) | high |
| `ia.sit.deduction.other` | 13000 | USD | 2026-01-01 |  | US-IAS5-005 (A.2) | high |
| `ia.sit.deduction.hoh` | 19500 | USD | 2026-01-01 |  | US-IAS5-005 (A.2) | high |
| `ia.sit.deduction.mfj_qss` | 26000 | USD | 2026-01-01 |  | US-IAS5-005 (A.2) | high |
| `ia.sit.dependent_allowance` | 40 | USD | 2026-01-01 |  | US-IAS5-029 (A.2) | high |
| `ia.sit.supplemental.rate` | 3.8 | percent | 2026-01-01 |  | US-IAS5-016 (A.2) | high |
| `ia.sit.rounding` | to the cent |  | 2026-01-01 |  | US-IAS5-005 (A.2) | high |
| `ia.oracle.ex6_monthly_5000_hoh.result` | 114.92 | USD | 2026-01-01 |  | US-IAS5-005 (A.2) | medium |
| `ia.sit.tips_overtime.level` | assessment (no withholding allowance in 2026) |  | 2026-01-01 |  | US-IAS5-019 (A.2) | high |
| `ia.sui.wage_base` | 20400 | USD | 2026-01-01 |  | US-IAS5-010 (A.2) | high |
| `ia.sui.wage_base` | 21100 | USD | 2027-01-01 |  | US-IAS5-010 (A.2) | high |
| `ia.sui.new_employer.rate` | 1.0 | percent | 2026-01-01 |  | US-IAS5-011 (A.1) | high |
| `ia.sui.new_construction.rate` | 5.4 | percent | 2026-01-01 |  | US-IAS5-011 (A.1) | high |
| `ia.sui.employer.rate.max` | 5.4 | percent | 2026-01-01 |  | US-IAP9V-001 (A.2) | high |
| `ia.sui.employee.applies` | no |  | 2026-01-01 |  | US-IAS5-024 (A.1) | high |
| `ia.sui.other_state_credit` | no |  | 2026-01-01 |  | US-IAS5-024 (A.1) | high |

### ID (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `id.sit.rate` | 5.3 | percent | 2025-01-01 |  | US-IDS5-007 (A.1) | high |
| `id.sit.method` | STC tables EPB00744/EPB00745: percentage (round to dollar), annualised or wage bracket; allowance value 0 |  | 2026-01-01 |  | US-IDS5-008 (A.2) | high |
| `id.sit.zero_bracket.single` | 16100 | USD | 2026-07-23 |  | US-IDS5-011 (A.2) | high |
| `id.sit.zero_bracket.married` | 32200 | USD | 2026-07-23 |  | US-IDS5-011 (A.2) | high |
| `id.sit.supplemental.rate` | 5.3 | percent | 2026-01-01 |  | US-IDS5-008 (A.2) | high |
| `id.oracle.single_biweekly_1212.result` | 31 | USD | 2026-01-01 |  | US-IDS5-008 (A.2) | high |
| `id.sit.rounding` | percentage computation rounded to nearest whole dollar |  | 2026-01-01 |  | US-IDS5-008 (A.2) | high |
| `id.sui.wage_base` | 58300 | USD | 2026-01-01 |  | US-IDP7-001 (A.2) | medium |
| `id.sui.new_employer.rate` | 1.0 | percent | 2026-01-01 |  | US-IDP7-001 (A.2) | high |

### IL (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `il.sit.rate` | 4.95 | percent | 2026-01-01 |  | US-ILR3-001 (A.2) | high |
| `il.sit.exemption.line1` | 2925 | USD | 2026-01-01 |  | US-ILR3-001 (A.2) | high |
| `il.sit.exemption.line2` | 1000 | USD | 2026-01-01 |  | US-ILR3-001 (A.2) | high |
| `il.sit.method` | flat 4.95% on (wages - (line1 x 2,925 + line2 x 1,000)/periods) + line 3 (IL-700-T R-12/25) |  | 2026-01-01 |  | US-ILR3-001 (A.2) | high |
| `il.sit.supplemental` | no separate rate; bonuses, overtime and commission are wages |  | 2026-01-01 |  | US-ILR3-002 (A.2) | high |
| `il.oracle.il700t_weekly_800.result` | 32.13 | USD | 2026-01-01 |  | US-ILR3-001 (A.2) | high |
| `il.sui.wage_base` | 14250 | USD | 2026-01-01 |  | US-ILS5-015 (A.2) | high |
| `il.sui.new_employer.rate` | 3.35 | percent | 2026-01-01 |  | US-ILS5-015 (A.2) | high |
| `il.sui.employer.rate.min` | 0.75 | percent | 2026-01-01 |  | US-ILS5-015 (A.2) | high |
| `il.sui.employer.rate.max` | 7.05 | percent | 2026-01-01 |  | US-ILS5-015 (A.2) | high |
| `il.local.income_tax.applies` | no |  | 2026-01-01 |  | US-IL-P5-2-001 (id-format: in unresolved) | - |
| `il.secure_choice.deduction` | Secure Choice Roth IRA payroll deduction (employee, opt-out) |  | 2026-01-01 |  | US-IL-P5-2-002 (id-format: in unresolved) | - |

### IN (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `in.sit.rate` | 2.95 | percent | 2026-01-01 |  | US-INS5-009 (A.2) | high |
| `in.sit.rate` | 2.9 | percent | 2027-01-01 |  | US-INS5-009 (A.2) | medium |
| `in.sit.method` | gross per period minus WH-4 constants (1,000 exemption; 1,500 dependent; 3,000 adopted, /periods) x 2.95% + county rate (DN#1 R47/10-26) |  | 2026-10-01 |  | US-INS5-007 (A.2) | high |
| `in.sit.exemption.personal` | 1000 | USD | 2026-01-01 |  | US-INS5-007 (A.2) | high |
| `in.sit.exemption.dependent` | 1500 | USD | 2026-01-01 |  | US-INS5-007 (A.2) | high |
| `in.sit.exemption.adopted_child` | 3000 | USD | 2026-01-01 |  | US-INS5-007 (A.2) | high |
| `in.sit.supplemental` | flat 2.95% + county rate, no exemptions |  | 2026-01-01 |  | US-INS5-007 (A.2) | high |
| `in.oracle.dn1_weekly_800.state` | 13.96 | USD | 2026-01-01 |  | US-INS5-007 (A.2) | high |
| `in.oracle.dn1_weekly_800.county` | 4.73 | USD | 2026-01-01 |  | US-INS5-007 (A.2) | high |
| `in.local.county_lit.rule` | 92 counties; county of residence on Jan 1 (out-of-state resident: principal work county); fixed for the year; reported with state on WH-1/WH-3 |  | 2026-01-01 |  | US-INS5-008 (A.2) | high |
| `in.local.county_lit.rate.boone` | 0.0171 | ratio | 2026-10-01 |  | US-INS5-007 (A.2) | high |
| `in.local.county_lit.rate.marion` | 0.0202 | ratio | 2026-01-01 |  | US-INS5-007 (A.2) | high |
| `in.local.county_lit.rate.min` | 0.005 | ratio | 2026-01-01 |  | US-INS5-007 (A.2) | high |
| `in.local.county_lit.rate.max` | 0.03 | ratio | 2026-01-01 |  | US-INS5-007 (A.2) | high |
| `in.sui.wage_base` | 9500 | USD | 2026-01-01 |  | US-INS5-014 (A.2) | medium |
| `in.sui.new_employer.rate` | 2.5 | percent | 2026-01-01 |  | US-INS5-014 (A.2) | high |
| `in.sui.employer.rate.min` | 0.5 | percent | 2026-01-01 |  | US-INS5-014 (A.2) | high |
| `in.sui.employer.rate.max` | 7.4 | percent | 2026-01-01 |  | US-INS5-014 (A.2) | high |

### KS (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ks.sit.method` | KW-100 (wages paid on/after 2024-07-01): gross - allowance (9,160 S / 18,320 J / 2,320 dep) then table; header still says 2021 - ignore |  | 2026-01-01 |  | US-KSS5-001 (A.2) | high |
| `ks.sit.annual_table.single` | 0% to 3,605; 5.2% to 26,605; 1,196 + 5.58% above |  | 2026-01-01 |  | US-KSS5-001 (A.2) | high |
| `ks.sit.annual_table.married` | 0% to 8,240; 5.2% to 54,240; 2,392 + 5.58% above |  | 2026-01-01 |  | US-KSS5-001 (A.2) | high |
| `ks.sit.allowance.single` | 9160 | USD | 2026-01-01 |  | US-KSS5-006 (A.1) | high |
| `ks.sit.allowance.joint` | 18320 | USD | 2026-01-01 |  | US-KSS5-006 (A.1) | high |
| `ks.sit.allowance.dependent` | 2320 | USD | 2026-01-01 |  | US-KSS5-006 (A.1) | high |
| `ks.sit.supplemental.rate` | 5 | percent | 2026-01-01 |  | US-KSS5-001 (A.2) | high |
| `ks.sit.rounding` | percentage result may be rounded to nearest dollar |  | 2026-01-01 |  | US-KSS5-001 (A.2) | high |
| `ks.sit.rate.2027` | no reduction (SB 269 trigger not met, Notice 26-11) |  | 2027-01-01 |  | US-KSS5-003 (A.2) | high |
| `ks.sui.wage_base` | 15100 | USD | 2026-01-01 |  | US-KSS5-023 (A.2) | high |
| `ks.sui.new_employer.rate` | 1.75 | percent | 2026-01-01 |  | US-KSS5-023 (A.2) | high |
| `ks.sui.new_construction.rate` | 5.55 | percent | 2026-01-01 |  | US-KSS5-023 (A.2) | high |
| `ks.sui.employer.rate.max` | 6.95 | percent | 2026-01-01 |  | US-KSS5-023 (A.2) | high |
| `ks.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-KSS5-020 (A.1) | high |

### KY (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ky.sit.rate` | 3.5 | percent | 2026-01-01 |  | US-KYS5-009 (A.1) | high |
| `ky.sit.standard_deduction` | 3360 | USD | 2026-01-01 |  | US-KY-002 (A.2) | high |
| `ky.sit.method` | (period wage x periods - 3,360) x 3.5% / periods |  | 2026-01-01 |  | US-KY-002 (A.2) | high |
| `ky.oracle.biweekly_1500.result` | 47.98 | USD | 2026-01-01 |  | US-KY-002 (A.2) | high |
| `ky.local.lexington.rate` | 2.25 | percent | 2026-01-01 |  | US-KYS5-024 (A.2) | high |
| `ky.local.louisville.nonresident.rate` | 1.45 | percent | 2026-01-01 |  | US-KYP9W-001 (A.2) | high |
| `ky.local.louisville.resident.rate` | 2.2 | percent | 2026-01-01 |  | US-KYP9W-001 (A.2) | high |
| `ky.sui.wage_base` | 12000 | USD | 2026-01-01 |  | US-KYS5-012 (A.1) | high |
| `ky.sui.new_employer.rate` | 2.7 | percent | 2026-01-01 |  | US-KY-003 (A.2) | high |
| `ky.sui.employer.rate.min` | 0.3 | percent | 2026-01-01 |  | US-KY-003 (A.2) | high |
| `ky.sui.employer.rate.max` | 9.0 | percent | 2026-01-01 |  | US-KY-003 (A.2) | high |
| `ky.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-KYS5-018 (A.1) | high |
| `ky.base.exclusions` | 125, DCAP, health, GTL, 401(k), SEP, TSP: no withholding (42A003 chart) |  | 2026-01-01 |  | US-KYS5-023 (A.2) | high |

### LA (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `la.sit.rate` | 3.09 | percent | 2026-01-01 |  | US-LAS5-001 (A.2) | high |
| `la.sit.method` | W = (S - 12,875/N) x 3.09% (L-4 1) or (S - 25,750/N) x 3.09% (L-4 2); no deduction: S x 3.09% (R-1306 1/26, emergency rule) |  | 2026-01-01 |  | US-LAS5-001 (A.2) | high |
| `la.sit.deduction.single` | 12875 | USD | 2026-01-01 |  | US-LAS5-001 (A.2) | high |
| `la.sit.deduction.joint` | 25750 | USD | 2026-01-01 |  | US-LAS5-001 (A.2) | high |
| `la.oracle.weekly_700.result` | 13.98 | USD | 2026-01-01 |  | US-LAS5-001 (A.2) | high |
| `la.oracle.biweekly_4600.result` | 111.54 | USD | 2026-01-01 |  | US-LAS5-001 (A.2) | high |
| `la.sui.wage_base` | 7000 | USD | 2026-01-01 |  | US-LAP9V-001 (A.2) | high |
| `la.sit.nonresident.threshold` | 30 days from 2026-01-01 (Act 382/2025; LAC 61:I.1923 adopted LR 52:358, eff. 2026-03-20); from day 31 all days |  | 2026-01-01 |  | US-LAS5-002 (A.1) | high |

### MA (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ma.sit.rate` | 5.0 | percent | 2026-01-01 |  | US-MAR3-002 (A.2) | high |
| `ma.sit.surtax.rate` | 4.0 | percent | 2026-01-01 |  | US-MAR3-002 (A.2) | high |
| `ma.sit.surtax.threshold` | 1107750 | USD | 2026-01-01 |  | US-MAR3-002 (A.2) | high |
| `ma.sit.method` | Circular M tables or percentage method: wages - FICA/retirement (max 2,000/yr) - exemption (annual 1,000n + 3,400) x 5% - HoH/blind reduction |  | 2026-01-01 |  | US-MAS5-013 (A.2) | high |
| `ma.sit.fica_retirement_deduction.annual_max` | 2000 | USD | 2026-01-01 |  | US-MAS5-013 (A.2) | high |
| `ma.sit.exemption.weekly` | 19n + 66 |  | 2026-01-01 |  | US-MAS5-013 (A.2) | high |
| `ma.sit.exemption.annual` | 1,000n + 3,400 |  | 2026-01-01 |  | US-MAS5-013 (A.2) | high |
| `ma.sit.method_choice` | tables and percentage method differ up to 0.02/week; engine uses one consistently |  | 2026-01-01 |  | US-MAS5-024 (A.2) | high |
| `ma.sit.supplemental` | 5% if annualised regular + supplemental YTD <= 1,107,750; above: lesser of 9% of payment or 9% of excess + 5% of remainder |  | 2026-01-01 |  | US-MAS5-013 (A.2) | medium |
| `ma.sui.wage_base` | 15000 | USD | 2015-01-01 |  | US-MAS5-020 (A.2) | high |
| `ma.sui.new_employer.rate` | 2.42 | percent | 2026-01-01 |  | US-MAS5-022 (A.2) | medium |
| `ma.sui.new_construction.rate` | 6.08 | percent | 2026-01-01 |  | US-MAS5-022 (A.2) | medium |
| `ma.sui.employer.rate.min` | 0.94 | percent | 2026-01-01 | 2026-12-31 | US-MAS5-020 (A.2) | high |
| `ma.sui.employer.rate.max` | 14.37 | percent | 2026-01-01 | 2026-12-31 | US-MAS5-020 (A.2) | high |
| `ma.levy.covid_recovery.rate.min` | 0.178 | percent | 2026-01-01 | 2026-12-31 | US-MAS5-020 (A.2) | high |
| `ma.levy.covid_recovery.rate.max` | 2.716 | percent | 2026-01-01 | 2026-12-31 | US-MAS5-020 (A.2) | high |
| `ma.levy.emac.year4.rate` | 0.12 | percent | 2026-01-01 |  | US-MAS5-021 (A.2) | high |
| `ma.levy.emac.year5.rate` | 0.24 | percent | 2026-01-01 |  | US-MAS5-021 (A.2) | high |
| `ma.levy.emac.year6plus.rate` | 0.34 | percent | 2026-01-01 |  | US-MAS5-021 (A.2) | high |
| `ma.levy.workforce_training.rate` | 0.056 | percent | 2026-01-01 |  | US-MAP7-001 (A.2) | medium |
| `ma.pfml.total.rate.25plus` | 0.88 | percent | 2026-01-01 | 2026-12-31 | US-MAS5-012 (A.2) | high |
| `ma.pfml.family.rate` | 0.18 | percent | 2026-01-01 | 2026-12-31 | US-MAS5-012 (A.2) | high |
| `ma.pfml.medical.rate` | 0.7 | percent | 2026-01-01 | 2026-12-31 | US-MAS5-012 (A.2) | high |
| `ma.pfml.total.rate.under25` | 0.46 | percent | 2026-01-01 | 2026-12-31 | US-MAS5-012 (A.2) | high |
| `ma.pfml.total.rate.25plus` | 0.88 | percent | 2027-01-01 |  | US-MAS5-012 (A.2) | high |
| `ma.pfml.family.rate` | 0.7 | percent | 2027-01-01 |  | US-MAS5-012 (A.2) | high |
| `ma.pfml.medical.rate` | 0.18 | percent | 2027-01-01 |  | US-MAS5-012 (A.2) | high |
| `ma.pfml.total.rate.under25` | 0.46 | percent | 2027-01-01 |  | US-MAS5-012 (A.2) | high |
| `ma.pfml.split.decision` | 2026 split per DFML 2026 table; swap from 2027-01-01 per DFML, not from 2026-01-01 per Ch.101 s.45 |  | 2026-01-01 |  | US-MAS5-012 (A.2) | medium |
| `ma.pfml.wage_cap` | Social Security wage base (184,500 in 2026) |  | 2026-01-01 |  | US-MAS5-010 (A.1) | high |
| `ma.conformity.same_year_irc` | decoupled from same-year IRC amendments from TY2026 (c.62C s.90) |  | 2026-01-01 |  | US-MAS5-026 (A.1) | high |

### MD (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `md.sit.state_rates` | 2/3/4/4.75/5/5.25/5.5/5.75/6.25/6.50; single 6.25 >500k, 6.50 >1M; joint 6.25 >600k, 6.50 >1.2M |  | 2026-01-01 |  | US-MDS5-001 (A.1) | high |
| `md.sit.exemption.annual` | 3200 | USD | 2026-01-01 |  | US-MDS5-021 (A.2) | high |
| `md.sit.standard_deduction` | 3400 | USD | 2026-01-01 |  | US-MDS5-021 (A.2) | medium |
| `md.sit.method` | percentage method: wages - standard deduction - exemptions x per-period, then combined state+county table (ten local tables 2.25..3.30; use table equal or slightly above county rate) |  | 2026-01-01 |  | US-MDS5-021 (A.2) | high |
| `md.sit.per_period_rounding` | biweekly/semimonthly exemption values truncated (130.76, 141.66) |  | 2026-01-01 |  | US-MDS5-021 (A.2) | high |
| `md.sit.supplemental.lump_sum.state_rate` | 6.5 | percent | 2026-01-01 |  | US-MDS5-021 (A.2) | high |
| `md.sit.nonresident.special.rate` | 2.25 | percent | 2026-01-01 |  | US-MDS5-021 (A.2) | high |
| `md.local.county.rate.max` | 3.3 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.worcester.rate` | 2.25 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.talbot.rate` | 2.4 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.garrett.rate` | 2.65 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.cecil.rate` | 2.74 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.washington.rate` | 2.95 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.carroll.rate` | 3.03 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.charles.rate` | 3.03 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.harford.rate` | 3.06 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.allegany.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.baltimore_county.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.baltimore_city.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.calvert.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.caroline.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.howard.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.montgomery.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.prince_georges.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.queen_annes.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.st_marys.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.somerset.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.wicomico.rate` | 3.2 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.dorchester.rate` | 3.3 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.kent.rate` | 3.3 | percent | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.anne_arundel.rate` | graduated: single 2.70 to 50,000 / 2.94 to 400,000 / 3.20 over; joint 2.70 to 75,000 / 2.94 to 480,000 / 3.20 over |  | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.local.county.frederick.rate` | graduated: single 2.25 to 25,000 / 2.75 to 50,000 / 2.96 to 150,000 / 3.20 over; joint 2.25 / 2.75 to 100,000 / 2.96 to 250,000 / 3.20 over |  | 2026-01-01 |  | US-MDS5-003 (A.2) | high |
| `md.sui.employer.rate.range` | 0.30-7.50% (Table A); new employers 1.0-2.6% |  | 2026-01-01 |  | US-MDP9V-001 (A.2) | high |
| `md.famli.total.rate` | 0.9 | percent | 2027-01-01 |  | US-MDS5-014 (A.2) | high |
| `md.famli.contribution.2026` | no |  | 2026-01-01 | 2026-12-31 | US-MDS5-014 (A.2) | high |
| `md.sui.wage_base` | 8500 | USD | 2026-01-01 |  | US-MD-SUI-001 (id-format: in unresolved) | - |

### ME (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `me.sit.standard_deduction.single` | 12450 | USD | 2026-01-01 |  | US-MES5-011 (A.2) | high |
| `me.sit.standard_deduction.married` | 27750 | USD | 2026-01-01 |  | US-MES5-011 (A.2) | high |
| `me.sit.brackets.single` | 5.80% below 27,400; 1,589 + 6.75% to 64,850; 4,117 + 7.15% above |  | 2026-01-01 |  | US-MES5-011 (A.2) | high |
| `me.sit.brackets.married` | 5.80% below 54,850; 3,181 + 6.75% to 129,750; 8,237 + 7.15% above |  | 2026-01-01 |  | US-MES5-011 (A.2) | high |
| `me.sit.rounding` | per-period result rounded to nearest dollar |  | 2026-01-01 |  | US-MES5-011 (A.2) | high |
| `me.sit.supplemental.rate` | 5 | percent | 2026-01-01 |  | US-MES5-011 (A.2) | high |
| `me.sit.w4_step4b` | not followed (do not reduce ME withholding for federal 4(b)) |  | 2026-01-01 |  | US-MES5-011 (A.2) | high |
| `me.oracle.booklet_ex1.result` | 0 | USD | 2026-01-01 |  | US-MES5-011 (A.2) | high |
| `me.oracle.booklet_ex2.result` | 33 | USD | 2026-01-01 |  | US-MES5-011 (A.2) | high |
| `me.oracle.booklet_ex3.result` | 257 | USD | 2026-01-01 |  | US-MES5-011 (A.2) | high |
| `me.sui.wage_base` | 12000 | USD | 2026-01-01 |  | US-MES5-020 (A.1) | high |
| `me.sui.upaf.rate` | 0.17 | percent | 2026-01-01 |  | US-MES5-021 (A.2) | medium |
| `me.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-MES5-020 (A.1) | high |
| `me.pfml.total.rate.15plus` | 1.0 | percent | 2025-01-01 | 2027-12-31 | US-MES5-024 (A.1) | medium |
| `me.pfml.total.rate.under15` | 0.5 | percent | 2025-01-01 | 2027-12-31 | US-MES5-024 (A.1) | medium |
| `me.sit.allowance` | 5300 | USD | 2026-01-01 |  | US-ME-P5-2-001 (id-format: in unresolved) | - |
| `me.sui.new_employer.total.rate` | 2.54 | percent | 2026-01-01 |  | US-ME-P5-1-001 (id-format: in unresolved) | - |

### MI (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `mi.sit.tips_overtime.level` | assessment only (2025 PA 24, MCL 206.30(1)(ee), TY2026-2028); withholding unchanged |  | 2026-01-01 |  | US-MIS5-015 (A.1) | high |
| `mi.local.detroit.resident.rate` | 2.4 | percent | 2026-01-01 |  | US-MIR3-002 (A.2) | high |
| `mi.local.detroit.nonresident.rate` | 1.2 | percent | 2026-01-01 |  | US-MIR3-002 (A.2) | high |
| `mi.local.detroit.exemption` | 600 | USD | 2026-01-01 |  | US-MIR3-002 (A.2) | high |
| `mi.oracle.detroit_resident_biweekly_2000.result` | 47.45 | USD | 2026-01-01 |  | US-MIR3-002 (A.2) | high |
| `mi.local.uniform_ordinance.resident.rate` | 1.0 | percent | 2026-01-01 |  | US-MIR3-003 (A.1) | high |
| `mi.local.uniform_ordinance.nonresident.rate` | 0.5 | percent | 2026-01-01 |  | US-MIR3-003 (A.1) | high |
| `mi.sui.wage_base` | 9000 | USD | 2026-01-01 |  | US-MIS5-025 (A.2) | high |
| `mi.sui.wage_base.delinquent` | 9500 | USD | 2026-01-01 |  | US-MIS5-010 (A.1) | high |
| `mi.sui.new_employer.rate` | 2.7 | percent | 2026-01-01 |  | US-MIS5-012 (A.1) | high |
| `mi.sui.new_construction.rate` | 5.0 | percent | 2026-01-01 |  | US-MIS5-012 (A.1) | high |
| `mi.sui.employer.rate.range` | 0.06-12.2% (15.2% with penalty) |  | 2026-01-01 |  | US-MIP9W-001 (A.2) | high |
| `mi.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-MIS5-010 (A.1) | high |
| `mi.sit.rate` | 4.25 | percent | 2026-01-01 |  | US-MI-PIT-001 (id-format: in unresolved) | - |
| `mi.sit.exemption` | 5900 | USD | 2026-01-01 |  | US-MI-PIT-001 (id-format: in unresolved) | - |
| `mi.sit.method` | (wages - 5,900 x exemptions / periods) x 4.25% |  | 2026-01-01 |  | US-MI-PIT-001 (id-format: in unresolved) | - |
| `mi.sit.supplemental.rate` | 4.25 | percent | 2026-01-01 |  | US-MI-PIT-001 (id-format: in unresolved) | - |
| `mi.oracle.biweekly_2000_1ex.result` | 75.36 | USD | 2026-01-01 |  | US-MI-PIT-001 (id-format: in unresolved) | - |

### MN (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `mn.sit.method` | annualise; minus 5,300 x allowances; apply chart; / periods; may round to dollar (DOR 2026 computer formula) |  | 2026-01-01 |  | US-MNS5-010 (A.2) | high |
| `mn.sit.allowance` | 5300 | USD | 2026-01-01 |  | US-MNS5-010 (A.2) | high |
| `mn.sit.chart.single` | 5.35% over 4,700 to 38,010; 1,782.09 + 6.80% to 114,130; 6,958.25 + 7.85% to 207,850; 14,315.27 + 9.85% above |  | 2026-01-01 |  | US-MNS5-010 (A.2) | high |
| `mn.sit.chart.married` | 5.35% over 14,700 to 63,400; 2,605.45 + 6.80% to 208,180; 12,450.49 + 7.85% to 352,630; 23,789.82 + 9.85% above |  | 2026-01-01 |  | US-MNS5-010 (A.2) | high |
| `mn.sit.supplemental.rate` | 6.25 | percent | 2026-01-01 |  | US-MNS5-010 (A.2) | high |
| `mn.sit.backup.rate` | 9.85 | percent | 2026-01-01 |  | US-MNS5-010 (A.2) | high |
| `mn.sit.nonresident.threshold` | 15300 | USD | 2026-01-01 |  | US-MNS5-010 (A.2) | high |
| `mn.oracle.biweekly_2000_single1.result` | 91.27 | USD | 2026-01-01 |  | US-MNS5-010 (A.2) | high |
| `mn.sit.conformity` | IRC as amended through 2023-05-01; H.R.1 (2025) withholding changes not adopted |  | 2026-01-01 |  | US-MNS5-010 (A.2) | high |
| `mn.paid_leave.total.rate` | 0.88 | percent | 2026-01-01 |  | US-MNS5-018 (A.1) | medium |
| `mn.levy.workforce_development.rate` | 0.1 | percent | 2026-01-01 |  | US-MNP7-001 (A.2) | high |
| `mn.sui.wage_base` | 44000 | USD | 2026-01-01 |  | US-MN-P5-2-001 (id-format: in unresolved) | - |
| `mn.sui.base.rate` | 0.4 | percent | 2026-01-01 |  | US-MN-P5-2-001 (id-format: in unresolved) | - |
| `mn.sui.employer.rate.max` | 8.9 | percent | 2026-01-01 |  | US-MN-P5-2-001 (id-format: in unresolved) | - |
| `mn.sui.additional_assessment.rate` | 14 | percent | 2026-01-01 |  | US-MN-P5-2-001 (id-format: in unresolved) | - |
| `mn.paid_leave.total.rate.deed` | 0.88 | percent | 2026-01-01 | 2027-12-31 | US-MN-P5-2-003 (id-format: in unresolved) | - |

### MO (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `mo.sit.standard_deduction.single` | 16100 | USD | 2026-01-01 |  | US-MOS5-001 (A.2) | high |
| `mo.sit.standard_deduction.married_nonworking_spouse` | 32200 | USD | 2026-01-01 |  | US-MOS5-001 (A.2) | high |
| `mo.sit.standard_deduction.hoh` | 24150 | USD | 2026-01-01 |  | US-MOS5-001 (A.2) | high |
| `mo.sit.brackets` | 1,348-wide: 0/2/2.5/3/3.5/4/4.5% then 4.7% over 9,436 |  | 2026-01-01 |  | US-MOS5-001 (A.2) | high |
| `mo.sit.rate.top` | 4.7 | percent | 2026-01-01 |  | US-MOS5-018 (A.1) | high |
| `mo.sit.rounding` | per-period result rounded to whole dollar |  | 2026-01-01 |  | US-MOS5-001 (A.2) | high |
| `mo.sit.supplemental.rate` | 4.7 | percent | 2026-01-01 |  | US-MOS5-001 (A.2) | high |
| `mo.oracle.dor_example_35000.annual` | 707.81 | USD | 2026-01-01 |  | US-MOS5-001 (A.2) | high |
| `mo.local.st_louis.earnings.rate` | 1.0 | percent | 2026-01-01 |  | US-MOP7-001 (A.2) | high |
| `mo.local.st_louis.payroll_expense.rate` | 0.5 | percent | 2026-01-01 |  | US-MOP7-002 (A.2) | high |
| `mo.local.kansas_city.earnings.rate` | 1.0 | percent | 2026-01-01 |  | US-MOP9W-001 (A.2) | high |
| `mo.sui.wage_base` | 9000 | USD | 2026-01-01 |  | US-MOS5-012 (A.1) | high |
| `mo.sui.base.401k_deferral` | included (UI wages) |  | 2026-01-01 |  | US-MOS5-012 (A.1) | high |
| `mo.sui.base.section125` | excluded (not FUTA wages) |  | 2026-01-01 |  | US-MOS5-012 (A.1) | high |

### MS (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ms.sit.method` | AGP - (EX + STDED); (TI - 10,000) x 4% ; / periods; round to whole dollars (formula = oracle; tables at band upper bound, diff up to 1) |  | 2026-01-01 |  | US-MSS5-003 (A.2) | high |
| `ms.sit.rate` | 4.0 | percent | 2026-01-01 |  | US-MSS5-001 (A.1) | high |
| `ms.sit.zero_band` | 10000 | USD | 2026-01-01 |  | US-MSS5-001 (A.1) | high |
| `ms.sit.std_deduction.single` | 2300 | USD | 2026-01-01 |  | US-MSS5-003 (A.2) | high |
| `ms.sit.std_deduction.hoh` | 3400 | USD | 2026-01-01 |  | US-MSS5-003 (A.2) | high |
| `ms.sit.std_deduction.married` | 4600 | USD | 2026-01-01 |  | US-MSS5-003 (A.2) | high |
| `ms.sit.exemption.single` | 6000 | USD | 2026-01-01 |  | US-MSS5-002 (A.2) | high |
| `ms.sit.exemption.married` | 12000 | USD | 2026-01-01 |  | US-MSS5-002 (A.2) | high |
| `ms.sit.exemption.head_of_family` | 9500 | USD | 2026-01-01 |  | US-MSS5-002 (A.2) | high |
| `ms.sit.exemption.dependent` | 1500 | USD | 2026-01-01 |  | US-MSS5-002 (A.2) | high |
| `ms.oracle.table_a_single_weekly_460.result` | 9 | USD | 2026-01-01 |  | US-MSS5-003 (A.2) | high |
| `ms.sit.supplemental` | aggregate; top-bracket rate 4% allowed where aggregation over-withholds |  | 2026-01-01 |  | US-MSS5-002 (A.2) | high |
| `ms.sit.resident_working_out_of_state` | withhold MS on all wages except to the extent the work state withholds (journal: MULTI 2.2 wrong for MS) |  | 2026-01-01 |  | US-MSS5-019 (A.3) | high |
| `ms.sui.wage_base` | 14000 | USD | 2026-01-01 |  | US-MSS5-011 (A.1) | high |
| `ms.sui.new_employer.year1.rate` | 1.0 | percent | 2026-01-01 |  | US-MSS5-011 (A.1) | high |
| `ms.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-MSS5-011 (A.1) | high |
| `ms.levy.workforce_investment_training.rate` | 0.2 | percent | 2026-01-01 |  | US-MSL-002 (A.2) | low |
| `ms.sui.new_employer.year2.rate` | 1.1 | percent | 2026-01-01 |  | US-MS-P5-1-003 (id-format: in unresolved) | - |
| `ms.sui.new_employer.year3.rate` | 1.2 | percent | 2026-01-01 |  | US-MS-P5-1-003 (id-format: in unresolved) | - |
| `ms.sui.employer.rate.max` | 5.4 | percent | 2026-01-01 |  | US-MS-P5-1-003 (id-format: in unresolved) | - |

### MT (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `mt.sit.method` | W = A + B(G - C): single 0% to 16,100; 4.7% to 63,600; 2,233 + 5.65% above; round UP to next dollar (federal std deduction, no allowances) |  | 2026-01-01 |  | US-MTS5-022 (A.1) | high |
| `mt.sit.rate.top` | 5.65 | percent | 2026-01-01 |  | US-MTS5-022 (A.1) | high |
| `mt.sit.rate.top` | 5.4 | percent | 2027-01-01 |  | US-MTS5-022 (A.1) | high |
| `mt.sit.supplemental` | aggregate or flat 5% |  | 2026-01-01 |  | US-MTS5-005 (A.2) | medium |
| `mt.sit.nra_treaty.level` | assessment (treaty exclusions not applied at withholding); H-2A exempt |  | 2026-01-01 |  | US-MTS5-005 (A.2) | high |
| `mt.sui.wage_base` | 47300 | USD | 2026-01-01 |  | US-MTS5-024 (A.2) | high |
| `mt.levy.aft.rate` | 0.18 | percent | 2026-01-01 |  | US-MTP7-001 (A.2) | high |
| `mt.sui.base.section125` | taxable for UI |  | 2026-01-01 |  | US-MTS5-023 (A.1) | high |
| `mt.sui.base.401k_deferral` | taxable for UI |  | 2026-01-01 |  | US-MTS5-023 (A.1) | high |
| `mt.sui.base.dependent_care_129` | taxable for UI |  | 2026-01-01 |  | US-MTS5-023 (A.1) | high |
| `mt.sui.other_state_credit` | no |  | 2026-01-01 |  | US-MTS5-025 (A.3) | high |
| `mt.sui.employer.rate.max` | 6.12 | percent | 2026-01-01 |  | US-MT-P5-1-005 (id-format: in unresolved) | - |

### NC (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `nc.sit.rate` | 3.99 | percent | 2026-01-01 |  | US-NCS5-011 (A.1) | high |
| `nc.sit.withholding.rate` | 4.09 | percent | 2026-01-01 |  | US-NC-001 (A.2) | high |
| `nc.sit.standard_deduction.single` | 12750 | USD | 2026-01-01 |  | US-NCS5-010 (A.1) | high |
| `nc.sit.standard_deduction.hoh` | 19125 | USD | 2026-01-01 |  | US-NCS5-010 (A.1) | high |
| `nc.sit.standard_deduction.mfj` | 25500 | USD | 2026-01-01 |  | US-NCS5-010 (A.1) | high |
| `nc.sit.allowance` | 2500 | USD | 2026-01-01 |  | US-NC-001 (A.2) | medium |
| `nc.sit.supplemental.rate` | 4.09 | percent | 2026-01-01 |  | US-NC-001 (A.2) | high |
| `nc.sit.nra_addon.weekly` | 11 | USD | 2026-01-01 |  | US-NC-001 (A.2) | high |
| `nc.oracle.weekly_450_single2.result` | 4 | USD | 2026-01-01 |  | US-NC-001 (A.2) | high |
| `nc.local.income_tax.applies` | no |  | 2026-01-01 |  | US-NCS5-012 (A.1) | high |
| `nc.sui.wage_base` | 34200 | USD | 2026-01-01 |  | US-NCP9V-001 (A.2) | high |
| `nc.sui.new_employer.rate` | 1.0 | percent | 2026-01-01 |  | US-NCS5-014 (A.1) | high |
| `nc.sui.employer.rate.min` | 0.06 | percent | 2026-01-01 |  | US-NCP9V-001 (A.2) | high |
| `nc.sui.employer.rate.max` | 5.76 | percent | 2026-01-01 |  | US-NCP9V-001 (A.2) | high |
| `nc.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-NCS5-015 (A.1) | high |

### ND (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `nd.sit.method` | 2026 annual percentage method (2020+ W-4) or tables; federal W-4 used |  | 2026-01-01 |  | US-NDS5-001 (A.2) | high |
| `nd.sit.single` | 0% to 57,625; 1.95% to 258,450; 3,916.09 + 2.50% above |  | 2026-01-01 |  | US-NDS5-001 (A.2) | high |
| `nd.sit.mfj` | 0% to 57,500; 1.95% to 168,525; 2,164.99 + 2.50% above |  | 2026-01-01 |  | US-NDS5-001 (A.2) | high |
| `nd.sit.hoh` | 0% to 78,475; 1.95% to 289,675; 4,118.40 + 2.50% above |  | 2026-01-01 |  | US-NDS5-001 (A.2) | high |
| `nd.sit.pre2020_allowance.annual` | 5050 | USD | 2026-01-01 |  | US-NDS5-001 (A.2) | high |
| `nd.sit.supplemental.rate` | 1.5 | percent | 2026-01-01 |  | US-NDS5-001 (A.2) | high |
| `nd.sit.rounding` | nearest whole dollar; under 1.00 need not be withheld |  | 2026-01-01 |  | US-NDS5-001 (A.2) | high |
| `nd.oracle.weekly_1800_single.result` | 13 | USD | 2026-01-01 |  | US-NDS5-001 (A.2) | high |
| `nd.oracle.section1_weekly_1800_single2.result` | 10 | USD | 2026-01-01 |  | US-NDS5-001 (A.2) | high |
| `nd.sui.wage_base` | 46600 | USD | 2026-01-01 |  | US-NDS5-012 (A.2) | high |
| `nd.sui.new_employer.rate` | 1.0 | percent | 2026-01-01 |  | US-NDS5-012 (A.2) | high |
| `nd.sui.new_construction.rate` | 9.67 | percent | 2026-01-01 |  | US-NDS5-012 (A.2) | high |

### NE (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ne.sit.method` | Circular EN 2026: percentage method or tables; W-4N; allowance 2,440 |  | 2026-01-01 |  | US-NES5-010 (A.2) | high |
| `ne.sit.allowance` | 2440 | USD | 2026-01-01 |  | US-NES5-010 (A.2) | high |
| `ne.sit.withholding_rates` | 2.26/3.22/4.21/4.35/4.48/4.60 (DOR table rates, NOT statutory rates) |  | 2026-01-01 |  | US-NES5-010 (A.2) | high |
| `ne.sit.single.thresholds` | 3,430/6,710/21,810/31,610/40,130/75,370 |  | 2026-01-01 |  | US-NES5-010 (A.2) | high |
| `ne.sit.married.thresholds` | 8,190/13,010/32,400/50,400/62,530/82,920 |  | 2026-01-01 |  | US-NES5-010 (A.2) | high |
| `ne.sit.minimum.rate` | 1.5 | percent | 2026-01-01 |  | US-NES5-010 (A.2) | high |
| `ne.sit.supplemental.rate` | 3.5 | percent | 2026-01-01 |  | US-NES5-010 (A.2) | medium |
| `ne.sit.statutory_top.rate` | 4.55 | percent | 2026-01-01 |  | US-NES5-018 (A.1) | high |
| `ne.sui.wage_base` | 9000 | USD | 2026-01-01 |  | US-NES5-011 (A.3) | high |
| `ne.sui.wage_base.category20` | 24000 | USD | 2026-01-01 |  | US-NES5-011 (A.3) | high |
| `ne.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-NES5-011 (A.3) | high |
| `ne.sui.base.401k_deferral` | included |  | 2026-01-01 |  | US-NES5-019 (A.3) | high |
| `ne.sui.new_employer.rate` | 1.25 | percent | 2026-01-01 |  | US-NE-P5-1-003 (id-format: in unresolved) | - |
| `ne.sui.new_construction.rate` | 5.4 | percent | 2026-01-01 |  | US-NE-P5-1-003 (id-format: in unresolved) | - |

### NH (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `nh.sit.applies` | no |  | 2026-01-01 |  | US-NHP9W-003 (A.2) | high |
| `nh.sui.wage_base` | 14000 | USD | 2026-01-01 |  | US-NHS5-007 (A.1) | high |
| `nh.sui.new_employer.rate` | 1.7 | percent | 2026-01-01 |  | US-NHP9W-001 (A.2) | medium |
| `nh.sui.fbr.rate` | 1.0 | percent | 2026-01-01 |  | US-NHP9W-001 (A.2) | high |
| `nh.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-NHS5-007 (A.1) | high |
| `nh.pfml` | voluntary (Granite State Paid Family Leave); no mandatory levy |  | 2026-01-01 |  | US-NHS5-015 (A.1) | high |

### NJ (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `nj.sit.method` | NJ-WT percentage method (wages paid on/after 2020-10-01), rate tables A-E by NJ-W4; allowance 1,000/yr |  | 2026-01-01 |  | US-NJS5-006 (A.2) | high |
| `nj.sit.allowance.annual` | 1000 | USD | 2026-01-01 |  | US-NJS5-006 (A.2) | high |
| `nj.sit.supplemental` | no flat rate; with regular wages combined; separately without allowances |  | 2026-01-01 |  | US-NJS5-006 (A.2) | medium |
| `nj.sui.employee.rate` | 0.3825 | percent | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.wf_swf.employee.rate` | 0.0425 | percent | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.tdi.employee.rate` | 0.19 | percent | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.tdi.employee.rate` | 0.24 | percent | 2027-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.fli.employee.rate` | 0.23 | percent | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.fli.employee.rate` | 0.24 | percent | 2027-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.sui.wage_base` | 44800 | USD | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.sui.wage_base` | 46400 | USD | 2027-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.tdi_fli.employee.wage_base` | 171100 | USD | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.tdi_fli.employee.wage_base` | 177100 | USD | 2027-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.sui.new_employer.rate` | 2.6825 | percent | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.tdi.new_employer.rate` | 0.5 | percent | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.wf_swf.new_employer.rate` | 0.1175 | percent | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.sui.employer.rate.range` | total 0.5-5.8% (UI part 0.3825-5.6825%), FY 2026-27 Table C |  | 2026-01-01 |  | US-NJS5-023 (A.2) | high |
| `nj.base.403b_457.git` | taxable when contributed |  | 2026-01-01 |  | US-NJS5-006 (A.2) | high |
| `nj.base.401k.git` | excluded up to federal limit |  | 2026-01-01 |  | US-NJS5-006 (A.2) | high |
| `nj.base.hsa.git` | not excluded (taxable); A2634 not enacted |  | 2026-01-01 |  | US-NJS5-006 (A.2) | high |
| `nj.base.dependent_care_129.git` | included |  | 2026-01-01 |  | US-NJS5-006 (A.2) | high |
| `nj.base.section125.git` | taxable except qualifying plans requiring minimum medical/life/LTD purchase |  | 2026-01-01 |  | US-NJS5-006 (A.2) | high |
| `nj.base.401k_125.ui_tdi_fli` | included where cash was electable |  | 2026-01-01 |  | US-NJS5-017 (A.3) | high |
| `nj.local.newark.payroll_tax.rate` | 1.0 | percent | 2026-01-01 |  | US-NJP6-001 (A.2) | high |
| `nj.local.jersey_city.payroll_tax.rate` | 1.0 | percent | 2026-01-01 |  | US-NJP6-002 (A.2) | high |
| `nj.bik.room_board.weekly` | 301.5 | USD | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.bik.lodging.weekly` | 129.2 | USD | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.bik.meals.daily` | 34.5 | USD | 2026-01-01 |  | US-NJS5-010 (A.2) | high |
| `nj.local.newark.payroll_tax.note` | Newark 1% (0.50% element per MANDATE levy line); employer-only, no employee deduction |  | 2026-01-01 |  | US-NJP6-002 (A.2) | medium |

### NM (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `nm.sui.employer.rate.min` | 0.33 | percent | 2026-01-01 |  | US-NMS5-008 (A.2) | high |
| `nm.sui.employer.rate.max` | 5.4 | percent | 2026-01-01 |  | US-NMS5-008 (A.2) | high |
| `nm.levy.wc_fee.employer.quarterly` | 2.55 | USD | 2025-07-01 | 2028-06-30 | US-NMS5-012 (A.2) | high |
| `nm.levy.wc_fee.employee.quarterly` | 2.25 | USD | 2025-07-01 | 2028-06-30 | US-NMS5-012 (A.2) | high |
| `nm.sit.method` | FYI-104 Rev. 11/2025 percentage tables (1.5-5.9%), standard deduction built in, no allowances |  | 2026-01-01 |  | US-NM-P5-2-001 (id-format: in unresolved) | - |
| `nm.sit.single.annual` | zero to 8,050; bands from 0/5,500/16,500/33,500/66,500/210,000 taxable at 1.5/3.2/4.3/4.7/4.9/5.9% |  | 2026-01-01 |  | US-NM-P5-2-001 (id-format: in unresolved) | - |
| `nm.sit.supplemental.rate` | 5.9 | percent | 2026-01-01 |  | US-NM-P5-2-001 (id-format: in unresolved) | - |
| `nm.oracle.weekly_married_1000.result` | 41.8 | USD | 2026-01-01 |  | US-NM-P5-2-001 (id-format: in unresolved) | - |
| `nm.sui.wage_base` | 34800 | USD | 2026-01-01 |  | US-NM-P5-1-001 (id-format: in unresolved) | - |
| `nm.sui.new_employer.rate` | greater of NAICS average or 1% (1.00-1.28 in 2026) |  | 2026-01-01 |  | US-NM-P5-1-002 (id-format: in unresolved) | - |

### NV (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `nv.sit.applies` | no |  | 2026-01-01 |  | US-NVS5-014 (A.1) | high |
| `nv.sui.wage_base` | 45400 | USD | 2027-01-01 |  | US-NVS5-019 (A.2) | high |
| `nv.sui.new_employer.rate` | 2.95 | percent | 2026-01-01 |  | US-NVS5-006 (A.1) | high |
| `nv.levy.cep.rate` | 0.05 | percent | 2026-01-01 |  | US-NVS5-006 (A.1) | high |
| `nv.levy.mbt.general.rate` | 1.17 | percent | 2026-01-01 |  | US-NVS5-012 (A.2) | high |
| `nv.levy.mbt.general.quarterly_exclusion` | 50000 | USD | 2026-01-01 |  | US-NVP7-001 (A.2) | high |
| `nv.levy.mbt.financial_mining.rate` | 1.554 | percent | 2026-01-01 |  | US-NVP7-002 (A.2) | high |
| `nv.sui.wage_base` | 43700 | USD | 2026-01-01 |  | US-NV-P5-1-001 (id-format: in unresolved) | - |
| `nv.sui.employer.rate.range` | 0.25-5.40% |  | 2026-01-01 |  | US-NV-P5-1-001 (id-format: in unresolved) | - |

### NY (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ny.sit.method` | NYS-50-T-NYS (1/26): Method I tables, Method II exact calculation, Method III above 1,077,550 |  | 2026-01-01 |  | US-NY-001 (A.2) | high |
| `ny.sit.supplemental.rate` | 11.7 | percent | 2026-01-01 |  | US-NY-001 (A.2) | high |
| `ny.sui.wage_base` | 17600 | USD | 2026-01-01 |  | US-NYS5-010 (A.2) | high |
| `ny.sui.new_employer.total.rate` | 4.1 | percent | 2026-01-01 |  | US-NYP9V-001 (A.2) | high |
| `ny.sui.employer.rate.range` | 1.625-9.425% |  | 2026-01-01 |  | US-NYP9V-001 (A.2) | high |
| `ny.pfl.employee.rate` | 0.432 | percent | 2026-01-01 |  | US-NYP8-001 (A.2) | high |
| `ny.pfl.employee.annual_max` | 411.91 | USD | 2026-01-01 |  | US-NYP8-001 (A.2) | high |
| `ny.dbl.employee.rate` | 0.5 | percent | 2026-01-01 |  | US-NY-005 (A.2) | high |
| `ny.dbl.employee.weekly_max` | 0.6 | USD | 2026-01-01 |  | US-NY-005 (A.2) | high |
| `ny.levy.mctmt` | MCTMT per P7 list |  | 2026-01-01 |  | US-NYP7-001 (A.2) | high |
| `ny.levy.rsf` | Re-employment Service Fund 0.075% |  | 2026-01-01 |  | US-NYP7-004 (A.2) | high |
| `ny.base.414h.addback` | NY public employee 414(h) contributions added back |  | 2026-01-01 |  | US-NYS5-019 (A.2) | high |
| `ny.sit.deduction_allowance.single.annual` | 7400 | USD | 2026-01-01 |  | US-NY-P5-2-001 (id-format: in unresolved) | - |
| `ny.sit.deduction_allowance.married.annual` | 7950 | USD | 2026-01-01 |  | US-NY-P5-2-001 (id-format: in unresolved) | - |
| `ny.sit.exemption.annual` | 1000 | USD | 2026-01-01 |  | US-NY-P5-2-001 (id-format: in unresolved) | - |
| `ny.oracle.example1.result` | 8.01 | USD | 2026-01-01 |  | US-NY-P5-2-001 (id-format: in unresolved) | - |
| `ny.oracle.example3.result` | 3576.63 | USD | 2026-01-01 |  | US-NY-P5-2-001 (id-format: in unresolved) | - |
| `ny.oracle.example4.result` | 44.1 | USD | 2026-01-01 |  | US-NY-P5-2-001 (id-format: in unresolved) | - |
| `ny.oracle.example2.result` | 258.51 | USD | 2026-01-01 |  | US-NY-P5-2-001 (id-format: in unresolved) | - |

### OH (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `oh.sit.statutory_rate` | TY2026+: 0 to 26,050; 332.00 + 2.75% above (ORC 5747.02(A)(3)) - assessment level, NOT the withholding schedule |  | 2026-01-01 |  | US-OHS5-007 (A.1) | high |
| `oh.sit.method` | from pay dates 2026-08-01: TW = pay x PP - 650 x exemptions; 1.6% to 26,050; 416.80 + 2.99% to 100,000; 2,627.91 + 3.4% above; / PP |  | 2026-08-01 |  | US-OHS5-001 (A.2) | high |
| `oh.sit.method` | pay dates 2025-10-01 to 2026-07-31: 650/exemption; 1.775/2.990/3.640% (breaks 26,050 and 100,000) |  | 2025-10-01 | 2026-07-31 | US-OH-002 (A.2) | medium |
| `oh.sit.exemption` | 650 | USD | 2026-08-01 |  | US-OHS5-001 (A.2) | high |
| `oh.sit.supplemental.rate` | 2.75 | percent | 2026-01-01 |  | US-OHS5-017 (A.1) | high |
| `oh.oracle.biweekly_2000_1ex.result` | 45.13 | USD | 2026-08-01 |  | US-OHS5-001 (A.2) | high |
| `oh.local.school_district.rule` | withheld by residence in taxing district (ch. 5748); traditional or earned-income base |  | 2026-01-01 |  | US-OHS5-018 (A.2) | high |
| `oh.local.municipal.rule` | work-location based (ch. 718); base = Medicare wages less s.125, so 401(k) deferrals taxable; 20-day occasional entrant; >1% needs voter approval |  | 2026-01-01 |  | US-OHS5-013 (A.1) | high |
| `oh.local.school_district.westerville.rate` | 0.75 | percent | 2026-01-01 |  | US-OHS5-018 (A.2) | high |
| `oh.local.school_district.findlay.rate` | 1.0 | percent | 2026-01-01 |  | US-OHS5-018 (A.2) | high |
| `oh.sui.wage_base` | 9000 | USD | 2026-01-01 |  | US-OHS5-002 (A.2) | high |
| `oh.sui.new_employer.rate` | 2.85 | percent | 2026-01-01 |  | US-OHS5-002 (A.2) | high |
| `oh.sui.new_construction.rate` | 5.85 | percent | 2026-01-01 |  | US-OHS5-002 (A.2) | high |
| `oh.sui.employer.rate.range` | 0.55-10.25% including TCSF 0.15% |  | 2026-01-01 |  | US-OHS5-002 (A.2) | high |
| `oh.levy.tcsf.rate` | 0.15 | percent | 2026-01-01 |  | US-OHP7-003 (A.2) | high |

### OK (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ok.sit.statutory_rates` | single 0% first 3,750; 2.5% next 1,150; 3.5% next 2,300; 4.5% remainder (MFJ double) |  | 2026-01-01 |  | US-OKS5-009 (A.1) | high |
| `ok.sit.standard_deduction.single` | 6350 | USD | 2026-01-01 |  | US-OKS5-011 (A.1) | high |
| `ok.sit.standard_deduction.mfj` | 12700 | USD | 2026-01-01 |  | US-OKS5-011 (A.1) | high |
| `ok.sit.standard_deduction.hoh` | 9350 | USD | 2026-01-01 |  | US-OKS5-011 (A.1) | high |
| `ok.sit.allowance` | 1000 | USD | 2026-01-01 |  | US-OK-001 (A.2) | high |
| `ok.sit.annual_table.single` | 0 to 10,100; 2.5% to 11,250; 28.75 + 3.5% to 13,550; 109.25 + 4.5% above |  | 2026-01-01 |  | US-OK-001 (A.2) | high |
| `ok.sit.annual_table.married` | 0 to 20,200; 2.5% to 22,500; 57.50 + 3.5% to 27,100; 218.50 + 4.5% above |  | 2026-01-01 |  | US-OK-001 (A.2) | high |
| `ok.sit.rounding` | nearest whole dollar; nothing if quarterly tax < 0.25 |  | 2026-01-01 |  | US-OKS5-010 (A.1) | high |
| `ok.sit.supplemental.rate` | 4.5 | percent | 2026-01-01 |  | US-OKS5-014 (A.1) | high |
| `ok.oracle.semimonthly_married2_1825.result` | 37 | USD | 2026-01-01 |  | US-OK-001 (A.2) | high |
| `ok.sit.nra.rate` | 8 | percent | 2026-01-01 |  | US-OKS5-014 (A.1) | low |
| `ok.sui.wage_base` | 25000 | USD | 2026-01-01 |  | US-OK-002 (A.2) | high |
| `ok.sui.wage_base` | 24400 | USD | 2027-01-01 |  | US-OKS5-018 (A.2) | high |
| `ok.sui.new_employer.rate` | 1.5 | percent | 2026-01-01 |  | US-OK-002 (A.2) | high |
| `ok.sui.employer.rate.min` | 0.2 | percent | 2026-01-01 |  | US-OK-002 (A.2) | high |
| `ok.sui.employer.rate.max` | 5.8 | percent | 2026-01-01 |  | US-OK-002 (A.2) | high |
| `ok.sui.employer.rate.min` | 0.1 | percent | 2027-01-01 |  | US-OKS5-018 (A.2) | high |
| `ok.sui.employer.rate.max` | 5.5 | percent | 2027-01-01 |  | US-OKS5-018 (A.2) | high |
| `ok.sui.base.elective_deferrals` | included (UI wages) |  | 2026-01-01 |  | US-OKS5-006 (A.1) | high |
| `ok.sui.base.section125` | excluded |  | 2026-01-01 |  | US-OKS5-006 (A.1) | high |

### OR (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `or.sit.method` | annual formula: BASE = wages - federal tax (cap 8,750, phase-out) - std deduction (2,910 / 5,820); bands 4.75/6.75/8.75/9.9%; minus 263 per allowance |  | 2026-01-01 |  | US-ORS5-009 (A.2) | high |
| `or.sit.federal_tax_subtraction.cap` | 8750 | USD | 2026-01-01 |  | US-ORS5-009 (A.2) | medium |
| `or.sit.standard_deduction.single` | 2910 | USD | 2026-01-01 |  | US-ORS5-009 (A.2) | high |
| `or.sit.standard_deduction.married` | 5820 | USD | 2026-01-01 |  | US-ORS5-009 (A.2) | high |
| `or.sit.allowance_credit` | 263 | USD | 2026-01-01 |  | US-ORS5-009 (A.2) | high |
| `or.sit.supplemental.rate` | 8 | percent | 2026-01-01 |  | US-ORS5-009 (A.2) | high |
| `or.oracle.example1_annual.result` | 1789 | USD | 2026-01-01 |  | US-ORS5-009 (A.2) | high |
| `or.local.metro_shs.rate` | 1.0 | percent | 2026-01-01 |  | US-ORS5-024 (A.2) | high |
| `or.local.multnomah_pfa.rate` | 1.5 | percent | 2026-01-01 |  | US-ORS5-004 (A.2) | high |
| `or.levy.statewide_transit.employee.rate` | 0.1 | percent | 2026-01-01 |  | US-ORS5-011 (A.2) | high |
| `or.levy.trimet.employer.rate` | 0.8237 | percent | 2026-01-01 |  | US-ORP7-002 (A.2) | medium |
| `or.levy.lane_transit.employer.rate` | 0.8 | percent | 2026-01-01 |  | US-ORP7-003 (A.2) | medium |
| `or.levy.wbf.hourly` | 0.018 | USD | 2026-01-01 |  | US-ORS5-010 (A.2) | high |
| `or.sui.wage_base` | 56700 | USD | 2026-01-01 |  | US-ORS5-003 (A.2) | high |
| `or.sui.new_employer.rate` | 2.4 | percent | 2026-01-01 |  | US-ORS5-003 (A.2) | high |
| `or.sui.employer.rate.range` | 0.9-5.4% (Schedule III) |  | 2026-01-01 |  | US-ORS5-015 (A.1) | high |
| `or.pfml.total.rate` | 1.0 | percent | 2026-01-01 |  | US-ORS5-013 (A.3) | high |
| `or.pfml.employee_share` | 60 | percent | 2026-01-01 |  | US-ORS5-013 (A.3) | high |
| `or.pfml.employer_share` | 40 | percent | 2026-01-01 |  | US-ORS5-013 (A.3) | high |

### PA (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `pa.sit.rate` | 3.07 | percent | 2026-01-01 |  | US-PAS5-009 (A.2) | high |
| `pa.sit.supplemental` | added to current period x 3.07% |  | 2026-01-01 |  | US-PA-008 (A.2) | high |
| `pa.base.401k_403b_457_deferral.pit` | taxable when made (employer contributions not) |  | 2026-01-01 |  | US-PAS5-011 (A.2) | high |
| `pa.base.section125.dependent_care.pit` | not excluded (taxable) |  | 2026-01-01 |  | US-PAS5-011 (A.2) | high |
| `pa.base.gtl.pit` | employer premiums never taxable (no 50k imputed income) |  | 2026-01-01 |  | US-PAS5-011 (A.2) | high |
| `pa.base.hsa.pit` | follows federal (deduction); payroll exclusion at withholding open |  | 2026-01-01 |  | US-PAS5-012 (A.2) | medium |
| `pa.local.eit.rule` | withhold greater of resident EIT and work-location nonresident EIT (DCED register per address); PSD code; annual by 28 Feb |  | 2026-01-01 |  | US-PAS5-017 (A.1) | high |
| `pa.local.lst.annual_cap` | 52 | USD | 2026-01-01 |  | US-PAS5-017 (A.1) | high |
| `pa.local.philadelphia.resident.rate` | 3.735 | percent | 2026-07-01 |  | US-PAS5-022 (A.2) | high |
| `pa.local.philadelphia.nonresident.rate` | 3.425 | percent | 2026-07-01 |  | US-PAS5-022 (A.2) | high |
| `pa.local.philadelphia.resident.rate` | 3.74 | percent | 2025-07-01 | 2026-06-30 | US-PAS5-022 (A.2) | high |
| `pa.local.philadelphia.nonresident.rate` | 3.43 | percent | 2025-07-01 | 2026-06-30 | US-PAS5-022 (A.2) | high |
| `pa.local.pittsburgh.payroll_expense.rate` | 0.55 | percent | 2026-01-01 |  | US-PAP7-005 (A.2) | high |
| `pa.sui.wage_base` | 10000 | USD | 2018-01-01 |  | US-PAS5-019 (A.1) | high |
| `pa.sui.new_employer.rate` | 3.822 | percent | 2026-01-01 |  | US-PA-009 (A.2) | high |
| `pa.sui.new_construction.rate` | 10.5924 | percent | 2026-01-01 |  | US-PA-009 (A.2) | high |
| `pa.sui.employer.rate.range` | 1.4190-10.3734% |  | 2026-01-01 |  | US-PA-009 (A.2) | high |
| `pa.sui.employee.rate` | 0.07 | percent | 2026-01-01 |  | US-PAS5-019 (A.1) | high |

### RI (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ri.sit.annual_brackets` | 3.75% to 82,050; 3,076.88 + 4.75% to 186,450; 8,035.88 + 5.99% above (all statuses) |  | 2026-01-01 |  | US-RIS5-019 (A.2) | high |
| `ri.sit.exemption` | 1000 | USD | 2026-01-01 |  | US-RIS5-019 (A.2) | high |
| `ri.sit.exemption.cutoff_wages` | 290800 | USD | 2026-01-01 |  | US-RIS5-019 (A.2) | high |
| `ri.sit.supplemental.rate` | 5.99 | percent | 2026-01-01 |  | US-RIS5-019 (A.2) | high |
| `ri.oracle.weekly_2195_1ex.result` | 87.57 | USD | 2026-01-01 |  | US-RIS5-019 (A.2) | high |
| `ri.sui.wage_base` | 30800 | USD | 2026-01-01 |  | US-RIP9V-001 (A.2) | high |
| `ri.sui.wage_base.highest_rate` | 32300 | USD | 2026-01-01 |  | US-RIP9V-001 (A.2) | high |
| `ri.sui.new_employer.rate` | 1.21 | percent | 2026-01-01 |  | US-RIP9V-001 (A.2) | high |
| `ri.levy.jda.rate` | 0.21 | percent | 2026-01-01 |  | US-RIP7-001 (A.2) | high |
| `ri.sui.employer.rate.range` | 0.9-9.4% (Schedule F) |  | 2026-01-01 |  | US-RIP9V-001 (A.2) | high |
| `ri.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-RIS5-013 (A.1) | high |
| `ri.tdi.employee.rate` | 1.1 | percent | 2026-01-01 |  | US-RIP9V-001 (A.2) | high |
| `ri.tdi.wage_base` | 100000 | USD | 2026-01-01 |  | US-RIP9V-001 (A.2) | high |
| `ri.tdi.employee.annual_max` | 1100 | USD | 2026-01-01 |  | US-RIP9V-001 (A.2) | high |
| `ri.base.401k_125.ui_tdi` | excluded (departs from FUTA) |  | 2026-01-01 |  | US-RIS5-017 (A.2) | high |

### SC (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `sc.sit.method` | WH-1603F 2026: annualise; minus 5,000 per allowance; minus 10% std deduction (cap 7,500, only with 1+ allowance); 0% below 3,640; 3% - 109.20 to 18,230; 6% - 656.10 above |  | 2026-01-01 |  | US-SCS5-004 (A.2) | high |
| `sc.oracle.wh1603f_weekly_750_3al.result` | 10.58 | USD | 2026-01-01 |  | US-SCS5-004 (A.2) | high |
| `sc.sit.act110_rates.level` | assessment only for 2026 (1.99/5.21%); NOT in 2026 withholding tables (journal trap) |  | 2026-01-01 |  | US-SCS5-001 (A.1) | high |
| `sc.sit.supplemental` | no flat rate; bonuses through the tables |  | 2026-01-01 |  | US-SCS5-002 (A.2) | high |
| `sc.sui.wage_base` | 14000 | USD | 2026-01-01 |  | US-SCS5-014 (A.1) | high |
| `sc.sui.daca.rate` | 0.06 | percent | 2026-01-01 |  | US-SCS5-014 (A.1) | high |
| `sc.sui.new_employer.total.rate` | 1.06 | percent | 2026-01-01 |  | US-SC-003 (A.2) | high |
| `sc.sui.employer.rate.range` | 0.060-5.460% total (class 1-20) |  | 2026-01-01 |  | US-SC-003 (A.2) | high |
| `sc.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-SCS5-014 (A.1) | high |

### SD (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `sd.sit.applies` | no |  | 2026-01-01 |  | US-SD-001 (A.2) | high |
| `sd.sui.wage_base` | 15000 | USD | 2015-01-01 |  | US-SDS5-002 (A.1) | high |
| `sd.sui.new_employer.year1.rate` | 1.2 | percent | 2026-01-01 |  | US-SDS5-002 (A.1) | high |
| `sd.sui.new_employer.later.rate` | 1.0 | percent | 2026-01-01 |  | US-SDS5-002 (A.1) | high |
| `sd.sui.employer.rate.max` | 8.52 | percent | 2026-01-01 |  | US-SDS5-018 (A.2) | high |
| `sd.levy.admin_fee.rate` | 0.08 | percent | 2026-01-01 |  | US-SDS5-002 (A.1) | high |
| `sd.levy.investment_fee.new_employer.rate` | 0.55 | percent | 2026-01-01 |  | US-SDS5-002 (A.1) | high |
| `sd.sui.base.deferrals_125` | included in RA wages |  | 2026-01-01 |  | US-SDS5-013 (A.2) | high |

### TN (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `tn.sit.applies` | no |  | 2026-01-01 |  | US-TN-001 (A.2) | high |
| `tn.sui.wage_base` | 7000 | USD | 2026-01-01 |  | US-TNS5-002 (A.2) | high |
| `tn.sui.new_employer.rate` | 2.7 | percent | 2026-01-01 |  | US-TNS5-004 (A.3) | high |
| `tn.sui.employer.rate.min` | 0.01 | percent | 2026-01-01 |  | US-TNS5-003 (A.2) | high |
| `tn.sui.employer.rate.max` | 10.0 | percent | 2026-01-01 |  | US-TNS5-003 (A.2) | high |

### TX (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `tx.sit.applies` | no |  | 2026-01-01 |  | US-TXS5-001 (A.1) | high |
| `tx.sui.wage_base` | 9000 | USD | 2026-01-01 |  | US-TXS5-007 (A.1) | high |
| `tx.sui.new_employer.rate` | 2.7 | percent | 2026-01-01 |  | US-TXS5-019 (A.2) | medium |
| `tx.sui.employer.rate.min` | 0.32 | percent | 2026-01-01 |  | US-TXR3-003 (A.2) | high |
| `tx.sui.employer.rate.max` | 6.32 | percent | 2026-01-01 |  | US-TXR3-003 (A.2) | high |
| `tx.levy.etia.rate` | 0.1 | percent | 2026-01-01 |  | US-TXS5-008 (A.1) | high |

### UT (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `ut.sit.rate` | 4.45 | percent | 2026-01-01 |  | US-UTS5-001 (A.1) | high |
| `ut.sit.withholding_base` | wages subject to federal withholding (IRC 3401(a)) |  | 2026-01-01 |  | US-UTS5-013 (A.1) | high |
| `ut.sui.wage_base` | 50700 | USD | 2026-01-01 |  | US-UTS5-005 (A.2) | high |
| `ut.sui.base.401k_deferral` | included (UI wages) |  | 2026-01-01 |  | US-UTS5-004 (A.2) | high |
| `ut.sit.method` | Pub 14 Rev. 04/26: wages x 4.45% minus max(0, base allowance - 1.3% x (wages - threshold)); all lines whole dollars; filing status from federal W-4 |  | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.sit.base_allowance.single` | 485 | USD | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.sit.base_allowance.married` | 970 | USD | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.sit.threshold.single` | 9348 | USD | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.sit.threshold.married` | 18696 | USD | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.sit.phaseout.rate` | 1.3 | percent | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.oracle.pub14.weekly_single_400.result` | 12 | USD | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.oracle.pub14.biweekly_single_2600.result` | 116 | USD | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.oracle.pub14.semimonthly_married_1200.result` | 18 | USD | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.oracle.pub14.monthly_married_7800.result` | 347 | USD | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.oracle.pub14.quarterly_single_9000.result` | 367 | USD | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.oracle.pub14.daily_married_175.result` | 5 | USD | 2026-01-01 |  | US-UT-PIT-003 (id-format: in unresolved) | - |
| `ut.sui.employer.rate.min` | 0.1 | percent | 2026-01-01 |  | US-UT-SUI-001 (id-format: in unresolved) | - |
| `ut.sui.employer.rate.max` | 7.1 | percent | 2026-01-01 |  | US-UT-SUI-001 (id-format: in unresolved) | - |
| `ut.sui.social_cost.rate` | 0.1 | percent | 2026-01-01 |  | US-UT-SUI-001 (id-format: in unresolved) | - |

### VA (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `va.sit.method` | T = G x P - [8,750 + 930 x E1 + 800 x E2]; 2% to 3,000; 60 + 3% to 5,000; 120 + 5% to 17,000; 720 + 5.75% above; / P |  | 2026-01-01 |  | US-VAS5-013 (A.2) | high |
| `va.sit.standard_deduction.single` | 8750 | USD | 2026-01-01 | 2026-12-31 | US-VAS5-018 (A.1) | high |
| `va.sit.personal_exemption` | 930 | USD | 2026-01-01 |  | US-VAS5-018 (A.1) | high |
| `va.sit.aged_blind_exemption` | 800 | USD | 2026-01-01 |  | US-VAS5-018 (A.1) | high |
| `va.sit.standard_deduction.2027` | statute: 9,200 / 18,400 for TY2027 (guide says 3,000 - wrong); NOT modelled until Virginia Tax publishes 2027 formula |  | 2027-01-01 |  | US-VAS5-018 (A.1) | medium |
| `va.sit.supplemental.rate` | 5.75 | percent | 2026-01-01 |  | US-VAS5-013 (A.2) | high |
| `va.sui.wage_base` | 8000 | USD | 2026-01-01 |  | US-VAS5-014 (A.3) | high |
| `va.sui.new_employer.rate` | 2.5 | percent | 2026-01-01 |  | US-VAS5-014 (A.3) | high |
| `va.sui.employer.rate.range` | 0.1-6.2% base rates plus add-ons |  | 2026-01-01 |  | US-VAS5-014 (A.3) | high |
| `va.sui.fund_building.rate` | 0.2 | percent | 2026-01-01 |  | US-VAR3-003 (A.1) | high |
| `va.sui.base.section125` | excluded |  | 2026-01-01 |  | US-VAS5-014 (A.3) | high |
| `va.sui.base.401k` | included |  | 2026-01-01 |  | US-VAS5-014 (A.3) | high |
| `va.pfml.contributions.start` | 2028-04-01 (rate fixed by 2027-10-01); none in 2026-2027 |  | 2026-01-01 |  | US-VAS5-017 (A.3) | high |

### VT (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `vt.sit.method` | GB-1210-2026: wages minus W-4VT allowances (5,400 each) then percentage table; effective 2026-01-01 to 2026-12-31 |  | 2026-01-01 | 2026-12-31 | US-VTS5-016 (A.2) | high |
| `vt.sit.allowance` | 5400 | USD | 2026-01-01 | 2026-12-31 | US-VTS5-016 (A.2) | high |
| `vt.sit.single` | 0-3,925 nil; 3.35% to 54,675; 1,700.13 + 6.60% to 126,775; 6,458.73 + 7.60% to 260,225; 16,600.93 + 8.75% above |  | 2026-01-01 | 2026-12-31 | US-VTS5-016 (A.2) | high |
| `vt.sit.married` | 0-11,775 nil; 3.35% to 96,475; 2,837.45 + 6.60% to 216,525; 10,760.75 + 7.60% to 323,825; 18,915.55 + 8.75% above |  | 2026-01-01 | 2026-12-31 | US-VTS5-016 (A.2) | high |
| `vt.sit.supplemental` | estimate at 30% of federal withholding; NQDC 6% |  | 2026-01-01 |  | US-VTS5-016 (A.2) | high |
| `vt.oracle.gb1210_weekly_1800_married2.result` | 45.77 | USD | 2026-01-01 |  | US-VTS5-016 (A.2) | high |
| `vt.sit.min_tax.level` | 3% minimum tax on federal AGI > 150,000 is assessment only |  | 2026-01-01 |  | US-VTS5-018 (A.1) | high |
| `vt.sui.wage_base` | 15400 | USD | 2026-01-01 |  | US-VTS5-004 (A.2) | high |
| `vt.sui.new_employer.rate` | 1.0 | percent | 2004-07-01 |  | US-VTS5-009 (A.3) | high |
| `vt.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-VTS5-010 (A.1) | high |
| `vt.levy.child_care.total.rate` | 0.44 | percent | 2026-01-01 |  | US-VTS5-030 (A.2) | high |
| `vt.levy.child_care.employee.max_rate` | 0.11 | percent | 2026-01-01 |  | US-VTS5-030 (A.2) | high |

### WA (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `wa.sit.applies` | no |  | 2026-01-01 |  | US-WAS5-017 (A.2) | high |
| `wa.sui.wage_base` | 78200 | USD | 2026-01-01 |  | US-WAS5-012 (A.2) | high |
| `wa.sui.employer.rate.range` | 0.27-6.02% total (experience 0-5.40 + social cost 0.24-0.72 + EAF 0.02-0.03) |  | 2026-01-01 |  | US-WAS5-012 (A.2) | high |
| `wa.sui.new_employer.rate` | 115% of industry average, floor 1% |  | 2026-01-01 |  | US-WAS5-029 (A.2) | medium |
| `wa.pfml.total.rate` | 1.13 | percent | 2026-01-01 |  | US-WAS5-015 (A.2) | high |
| `wa.pfml.employee_share.max` | 71.43 | percent | 2026-01-01 |  | US-WAS5-015 (A.2) | high |
| `wa.pfml.total.rate` | 1.2 | percent | 2027-01-01 |  | US-WAS5-015 (A.2) | high |
| `wa.pfml.employee_share.max` | 70.7 | percent | 2027-01-01 |  | US-WAS5-015 (A.2) | high |
| `wa.pfml.base.tips` | excluded from PFML wages (included for UI) |  | 2026-01-01 |  | US-WAS5-023 (A.1) | high |
| `wa.cares.employee.rate` | 0.58 | percent | 2026-01-01 |  | US-WAS5-016 (A.2) | high |
| `wa.cares.wage_cap.applies` | no |  | 2026-01-01 |  | US-WAS5-016 (A.2) | high |
| `wa.wc.employee_deduction` | 50% x (Stay-at-Work + Medical Aid + Supplemental Pension) per hour by risk class |  | 2026-01-01 |  | US-WAS5-019 (A.2) | high |
| `wa.wc.supplemental_pension.rate` | 0.1912 | USD per hour | 2026-01-01 |  | US-WAS5-019 (A.2) | high |
| `wa.wc.class101.employee_hourly` | 0.3532 | USD | 2026-01-01 |  | US-WAS5-019 (A.2) | high |
| `wa.local.seattle.social_housing.rate` | 5.0 | percent | 2026-01-01 |  | US-WAP9V-001 (A.2) | high |
| `wa.local.seattle.payroll_expense_tax` | employer business tax on Seattle payroll expense (threshold 9,074,409 in 2026); not withheld |  | 2026-01-01 |  | US-WA-P5-1-001 (id-format: in unresolved) | - |

### WI (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `wi.sit.withholding_schedule` | 3.54% to 12,760; 4.65% to 25,520; 5.30% to 280,950; 7.65% above (W-166; NOT the assessment brackets) |  | 2022-01-01 |  | US-WIS5-011 (A.2) | high |
| `wi.sit.withholding_rates.2026` | unchanged (DOR Update 2026-1) |  | 2026-01-01 |  | US-WIS5-016 (A.2) | high |
| `wi.oracle.weekly_350_single1.result` | 7.59 | USD | 2026-01-01 |  | US-WIS5-011 (A.2) | high |
| `wi.oracle.weekly_500_single3.result` | 14.34 | USD | 2026-01-01 |  | US-WIS5-011 (A.2) | high |
| `wi.oracle.biweekly_1000_married3.result` | 22.08 | USD | 2026-01-01 |  | US-WIS5-011 (A.2) | high |
| `wi.sit.supplemental` | aggregate or flat by estimated annual gross: 3.54/4.65/5.30/7.65% |  | 2026-01-01 |  | US-WIS5-011 (A.2) | medium |
| `wi.base.box16_differences` | WI wages higher than federal for IRC 112, 127 student-loan, 128 Trump accounts, 129 above WI exemption, 132 moving/bicycle |  | 2026-01-01 |  | US-WIS5-016 (A.2) | high |
| `wi.sui.wage_base` | 14000 | USD | 2026-01-01 |  | US-WIS5-014 (A.1) | high |
| `wi.sui.new_employer.rate.small` | 3.05 | percent | 2026-01-01 |  | US-WIS5-019 (A.2) | high |
| `wi.sui.new_employer.rate.large` | 3.25 | percent | 2026-01-01 |  | US-WIS5-019 (A.2) | high |
| `wi.sui.employer.rate.max` | 12.0 | percent | 2026-01-01 |  | US-WIS5-019 (A.2) | high |
| `wi.sit.exemption` | 400 | USD | 2026-01-01 |  | US-WI-P5-1-001 (id-format: in unresolved) | - |

### WV (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `wv.sit.rates` | 2.11/2.81/3.16/4.22/4.58% at 10,000/25,000/40,000/60,000 (SB 392, retroactive 2026-01-01) |  | 2026-01-01 |  | US-WVS5-012 (A.2) | high |
| `wv.sit.optional_table` | one-earner: constants 211.00 / 632.50 / 1,106.50 / 1,950.50 |  | 2026-01-01 |  | US-WVS5-012 (A.2) | high |
| `wv.sit.two_earner_table` | default: brackets 7,500/18,750/30,000/45,000; constants 158.25 / 474.38 / 829.88 / 1,462.88 |  | 2026-01-01 |  | US-WVS5-012 (A.2) | high |
| `wv.sit.exemption.annual` | 2000 | USD | 2026-01-01 |  | US-WVS5-012 (A.2) | medium |
| `wv.sui.wage_base` | 9500 | USD | 2024-07-01 |  | US-WVS5-001 (A.1) | high |
| `wv.sui.new_employer.rate` | 2.7 | percent | 2026-01-01 |  | US-WVS5-002 (A.1) | high |
| `wv.sui.foreign_construction.rate` | 8.5 | percent | 2026-01-01 |  | US-WVS5-015 (A.1) | medium |
| `wv.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-WVS5-001 (A.1) | high |
| `wv.sui.base.401k_cafeteria` | included (UI gross) |  | 2026-01-01 |  | US-WVS5-016 (A.2) | high |
| `wv.local.charleston.service_fee.weekly` | 3.0 | USD | 2026-01-01 |  | US-WVR3-001 (A.1) | medium |

### WY (country_specific)

| key | value | unit | from | to | register_id | conf |
|---|---|---|---|---|---|---|
| `wy.sui.wage_base` | 33800 | USD | 2026-01-01 |  | US-WYS5-008 (A.2) | high |
| `wy.sui.wage_base` | 34900 | USD | 2027-01-01 |  | US-WYS5-008 (A.2) | high |
| `wy.sui.employer.rate.max` | 10.0 | percent | 2026-01-01 |  | US-WYS5-011 (A.2) | high |
| `wy.sui.other_state_credit` | yes |  | 2026-01-01 |  | US-WYS5-003 (A.1) | high |
| `wy.sit.applies` | no |  | 2026-01-01 |  | US-WY-P5-1-001 (id-format: in unresolved) | - |

---

## Open questions (mirror of `unresolved[]`, same keys and wording)


### global_baseline

- `fed.fica.oasdi.wage_base.2027_reverify`: The 2027 OASDI base 192,300 rests on US-FED-022; ssa.gov returned 403 on 2026-11-02 so it was not re-verified this run. What would close it: SSA cbb.html / Fact Sheet 2027 read from a US IP (browser pass), stamping verified_on on US-FED-022.
- `fed.futa.credit_reduction.2026.final`: 2026 credit reductions are potential until the DOL determination of 2026-11-10. What would close it: DOL ETA FUTA credit reduction final list for 2026 (published after 2026-11-10).
- `fed.fit.2027.tables`: Pub. 15-T 2027 and the 2027 inflation Rev. Proc. not published at 2026-11-02. What would close it: IRS Pub. 15-T (2027) and the 2027 inflation Rev. Proc.
- `fed.plan.402g.elective_deferral.limit_2027`: 2027 retirement plan limits notice not yet published (only tier-B projections). What would close it: IRS notice for 2027 plan limits (expected Nov 2026).
- `fed.bik.mileage.rate`: 2026 business standard mileage rate not printed in Pub. 15-B and not fetched. What would close it: IRS notice on 2026 standard mileage rates (IRS newsroom).
- `multi.sui.other_state_wage_credit.matrix`: Whether other-state wages count toward each state SUI base is verified only state by state (see country_specific *.sui.other_state_credit keys). What would close it: Per-state UI statute reading for states not yet confirmed (MULTI open questions).
- Plus 13 sourced values carried in `unresolved[]` only because of the register-id pattern defect (see the header); what would close them: a contract PATCH widening the `register_id` pattern.

### country_specific

- `ak.sui.wage_base.2027`: 2027 base not published (2027-experience-rates.html 404 on 2026-11-02); 54,200 not re-derived (average-wage worksheet missing). What would close it: DOLWD 2027 experience-rate page and the Tax Base Calculation worksheet (AK-OQ-1).
- `al.sui.schedule.2026`: 2026 schedule letter and shared-cost figure not located on an official page. What would close it: Workforce Alabama 2026 rate notice / UC-216 (AL-OQ-1).
- `al.local.occupational_tax.list`: No state list of ~26 municipal/county occupational taxes; Birmingham 1% only tier C. What would close it: League/city ordinances per locality; Birmingham ordinance (AL census).
- `ar.sit.table_switch_date`: Date employers had to switch to 3.7% tables not stated. What would close it: DFA withholding notice for Act 1/2026 (AR-OQ-1).
- `ar.sit.base.hsa_transit_gtl`: HSA outside 125, transit and GTL not listed in AR employer guide. What would close it: DFA withholding guide statement or ACA 26-51-404 reading (AR-OQ-3).
- `ca.sdi.employee.rate.2027`: 2027 SDI rate not published on EDD at read time; 1.4% exists only in a tier-B summary. What would close it: EDD 2027 SDI rate announcement / DE 44 2027 (CA open question 3).
- `ca.local.minimum_wage`: No local minimum wage registered (DIR does not keep a list). What would close it: City ordinances per locality (CA open question 1).
- `co.local.sheridan.opt`: Sheridan OPT 3/3 rests on tier C only. What would close it: City of Sheridan OPT ordinance or tax page.
- `co.famli.split.2027`: 2027 FAMLI split and small-employer exemption not read on a primary page. What would close it: famli.colorado.gov 2027 premium page (ACCESS gap).
- `ct.sit.tables.parsing`: IP 2026(1) pay-period tables pp.31+ not parsed; tables vs rules choice open. What would close it: Parse IP 2026(1) tables (PyMuPDF) and owner decision on CT-OQ-1.
- `ct.sui.wage_base.2027`: 27,900 is a derivation only; CT DOL 2027 page 404. What would close it: CT DOL 2027 taxable wage base notice.
- `dc.sit.method.2026` **[blocking]**: D.C. Act 26-416 repealed personal exemptions; D-4/D-4A under review; no 2026 withholding method reflecting it is published (journal trap: DC 2026 method unpublished). What would close it: OTR 2026 withholding instructions / revised D-4 (ACCESS gap: OTR 403).
- `dc.sui.interest_surcharge.2026`: 0.1% interest surcharge billing in 2026 not confirmed. What would close it: DOES 2026 rate notice.
- `de.pfml.rate.2027`: 2027 Paid Leave rate set by DOL actuarially (cap 1.00%) not published on 2026-11-02. What would close it: Delaware DOL Paid Leave 2027 rate notice.
- `de.levy.blue_collar_training`: Blue Collar training tax remains MANUAL (US-DEL-004). What would close it: Delaware DOL Division of UI tax rate notice showing the training tax.
- `fl.sui.base.401k_deferral`: Florida text excludes 401(a) trust payments; DOR guide silent on 401(k) elective deferrals (FUTA adds them back). What would close it: FloridaCommerce/DOR ruling or RT-6 instructions on 401(k) deferrals.
- `ga.sui.rate_range.2026`: 2026 experience rate range not on an A-tier source (0.04-8.10% is tier B). What would close it: GA DOL 2026 rate table (Q2).
- `ga.sit.rate.2027`: 4.865% for 2027 is conditional on OPB report 2026-12-01; not a fact. What would close it: OPB revenue trigger report 2026-12-01 and DOR 2027 guide.
- `hi.sit.2027`: Act 24/2026 changes 2027 brackets (new 13% band); 2027 withholding indeterminate. What would close it: DOTAX Booklet A 2027.
- `hi.sui.min_rate`: Schedule C minimum rate not transcribed (Table 2 absent from page text). What would close it: DLIR UI rate Table 2 (capitol.hawaii.gov 403).
- `ia.sui.table.2027`: 2027 IA rate table not yet published. What would close it: IWD 2027 rate table notice.
- `id.sit.zero_bracket.2026_h1`: Table edition 04-28-2025 (15,000/30,000) applied 2026-01-01..2026-07-22 but row US-IDS5-012 is superseded; value not carried as a fact. What would close it: Keep as historical in the WTC change log citing US-IDS5-012; no action unless the engine must replay H1 2026.
- `id.sui.wage_base.2027`: 2027 wage base not yet published (last snapshot 2026-08-03). What would close it: IDOL 2027 rates page.
- `id.sit.certificate.2026`: ID W-4 2026 edition not captured (US-IDS5-013 partial). What would close it: Idaho STC form EFO00307 2026 edition.
- `il.sui.wage_base.2027`: 2027 IL wage base not yet published (IDES usually December). What would close it: IDES 2027 rate/wage base notice.
- `in.sui.solvency_surcharge.2026`: 2026 solvency surcharge and schedule not obtained (US-INS5-015 partial). What would close it: DWD 2026 rate-computation notice.
- `in.local.county_lit.full_table`: Full 92-county rate chart lives in DN#1 R47/10-26; only exemplars carried as keys. What would close it: Builder transcribes the DN#1 county chart from the local file of US-INS5-007.
- `ks.sui.wage_base.2027`: ~15,700 is a projection only. What would close it: KDOL 2027 rate notice.
- `ks.sit.pickup_contributions`: Whether KS withholding covers employer-picked-up KPERS contributions (79-32,117(b)(vi) addition) is open. What would close it: KDOR guidance on KPERS pick-up withholding (KS OQ1).
- `ky.sit.rate.2027`: 2027 rate depends on Budget Director report; statute says 3.5%. What would close it: KY Budget Director 2026 report and DOR 2027 formula (Q1).
- `ky.local.occupational.list`: Other cities, counties and school districts levy occupational taxes (KOLA list not read). What would close it: KOLA / DLG occupational tax list (Q3).
- `la.sit.final_rule`: Tables set by emergency rule; standard deduction may change after Jan-2026 CPI-U; final rule not checked. What would close it: LDR final rule LAC 61:I.1501 for 2026.
- `la.base.cafeteria`: No LA source on cafeteria-plan / benefits treatment read (Wayback 404). What would close it: LDR FAQ on cafeteria-plan contributions (LA-OQ-8).
- `ma.base.item_departures`: 401(k)/125/HSA/transit/GTL item-by-item MA treatment not read in a DOR source. What would close it: DOR TIR / Circular M wage-definition section on fringe benefits (MA Q11).
- `ma.pfml.split.transition`: Ch.101 s.45 (2026-01-01) vs DFML (2027-01-01) conflict on the split swap; decision taken but no transition notice exists. What would close it: DFML/DOR notice or 458 CMR 2.00 amendment on the transition (MA Q14).
- `md.sui.other_state_credit`: BEACON field implies other-state wages count toward 8,500, but the statute was not located. What would close it: Md. LE taxable-wage definition section (MD Q2).
- `mi.local.23_cities`: Rates, forms and due dates of the 23 self-administered MI city income taxes not read. What would close it: Each city income tax department page (parallel fan-out; MI open questions).
- `mi.sit.exemption.2027`: 2027 MI personal exemption not yet published. What would close it: Treasury 2027 Guide 446.
- `mo.local.earnings_tax.renewal`: St. Louis / KC earnings tax renewal votes April 2026 not re-confirmed. What would close it: City election results / Collector of Revenue notice (MO-OQ-1).
- `mo.sui.other_state_credit`: 288.036 text read has no other-state wage credit. What would close it: DES guidance on wages reported to other states (MO-OQ-2).
- `ms.sit.rate.2027`: 3.75% for 2027 is enacted, but 2027 tables are not published. What would close it: MDOR 2027 Pub 89-700 / formula.
- `ms.base.hsa_transit_gtl`: HSA, transit and GTL over 50k MS treatment not confirmed (default follow federal). What would close it: MDOR regulation 35.III.2 reading on fringe benefits.
- `mt.sui.rate_schedule`: Schedule 1 range 0.00-6.12% and new-employer 1.00-2.00% rest on US-MT-P5-1-005 (multi-segment id; carried below). What would close it: Contract pattern fix.
- `mt.sit.tables.2027`: 2027 DOR withholding tables/guide not obtained. What would close it: Montana DOR 2027 withholding guide.
- `nc.sit.rate.2027`: 3.49% for 2027 is a projection only (do not model). What would close it: NCDOR NC-30 for 2027.
- `ne.sit.tables.2027`: 2027 withholding guide PDF not read. What would close it: Nebraska DOR Circular EN 2027.
- `nh.sui.base.elective_deferrals`: 282-A:15 has no express exclusion for 401(k)/125 deferrals. What would close it: NHES ruling or Emp rules (ACCESS gap nh.gov 403).
- `ny.pfl.employee.rate.2027`: 2027 PFL 0.452% / max 451.81 is MANUAL lead only (DFS page 403). What would close it: DFS PFL 2027 rate decision (ACCESS gap).
- `ny.sui.wage_base.2027`: 2027 NY UI base not published on pages read. What would close it: NYS DOL 2027 wage base notice.
- `ny.base.nyc_125_addback`: NYC flexible-benefits (IRC 125) addback via IT-225 not read. What would close it: DTF IT-225 instructions / NYC employer guidance.
- `oh.local.municipal.rate_table` **[blocking]**: No consolidated 2026 municipal rate table obtained (The Finder / RITA). What would close it: tax.ohio.gov municipal rate table / The Finder (ACCESS gap).
- `oh.local.school_district.full_list_2026`: No consolidated 2026 school-district list (2025 list US-OHS5-019 + 2026 changes US-OHS5-018). What would close it: ODT 2026 school district income tax rate list.
- `or.local.multnomah_pfa.step`: +0.8% PFA step year conflicts (2027 vs 2028). What would close it: Multnomah County ordinance text / Portland Revenue Division confirmation (OR-OQ-1).
- `or.levy.transit_rates.2026_verify`: TriMet/LTD rates rest on P7 rows not re-read this pass. What would close it: Oregon DOR transit tax rate page 2026.
- `pa.local.eit.rate_table`: No static EIT rate table; DCED Address Search per address. What would close it: DCED Address Search integration (per-address lookup) - design item, not research.
- `tx.sui.base.deferrals_125`: TWC treatment of 401(k) deferrals and s.125 reductions not read. What would close it: TWC Employer Handbook wage definition section.
- `tn.sui.base.definition`: TN Employment Security Law wage exclusions not read (Lexis). What would close it: T.C.A. 50-7-213 text via official access (TN Q5).
- `ut.sit.schedule.effective_date` **[blocking]**: Pub 14 Rev. 04/26 does not state its effective date; 2026-06-01 (replacing 450/900 allowances) is tier-B only - possible mid-year change. What would close it: Utah Tax Commission notice / Pub 14 effective-date statement (ACCESS gap tax.utah.gov 403).
- `ut.sit.supplemental`: No Utah supplemental rate stated; build rule runs supplemental through regular schedules. What would close it: Utah Tax Commission confirmation (R865-9I).
- `va.sui.pool_cost.2026`: 2026 pool-cost charge not obtained at tier A (0.03% is tier B). What would close it: VEC 2026 pool cost charge notice (VA Q2).
- `va.sit.formula.2027`: 2027 formula not published; statute 9,200/18,400 vs guide 3,000 conflict. What would close it: Virginia Tax 2027 withholding formula (VA Q1).
- `vt.sui.schedule.2026_07`: Schedule in force for the rate year from 2026-07-01 not confirmed. What would close it: VT DOL rate-year 2026-27 schedule notice (VT Q4; labor.vermont.gov 403).
- `wa.base.125_401k.ui_pfml_cares` **[blocking]**: Whether pre-tax s.125 / 401(k) deferrals are excluded from UI, PFML and WA Cares remuneration not answered (WAC 192-310-030, ch. 192-510 not read). What would close it: WAC 192-310-030 and WAC 192-510 text (ACCESS priority).
- `wa.sui.wage_base.2027`: 2027 WA UI base not published at 2026-11-02. What would close it: ESD 2027 taxable wage base notice.
- `wv.sui.sb1053_fee`: SB 1053 fee text (7% of taxable wages) vs design (7% shift of contributions) diverge. What would close it: WorkForce WV notice on the SB 1053 automation fee (WV Q4).
- `wv.local.service_fees`: Only Charleston 3.00/week confirmed; other city fees tier B. What would close it: City ordinances (Huntington, Wheeling, Morgantown, Parkersburg, Fairmont...) (WV Q3).
- `wv.sit.tables.switch_date`: Date employers had to apply March 2026 tables not stated. What would close it: WV Tax Division notice on SB 392 table implementation (WV Q1).
- `wy.sui.rates.2026`: 2026 minimum rate, industry new-employer rates and factor values not published on pages read. What would close it: DWS January 2026 rate memo (WY-OQ-1; dws.wyo.gov 403 outside US).
- `ky.sit.supplemental`: Register row US-KY-P5-1-001 is MANUAL/A.2; the value cannot be carried as a fact. What would close it: Replace US-KY-P5-1-001 with an active A.1/A.2 row (see _research/stage5/ACCESS-GAPS.md).
- `ny.local.nyc.supplemental.rate`: Register row US-NY-011 is superseded/A.2; the value cannot be carried as a fact. What would close it: Replace US-NY-011 with an active A.1/A.2 row (see _research/stage5/ACCESS-GAPS.md).
- `ny.local.yonkers.resident.supplemental.rate`: Register row US-NY-011 is superseded/A.2; the value cannot be carried as a fact. What would close it: Replace US-NY-011 with an active A.1/A.2 row (see _research/stage5/ACCESS-GAPS.md).
- `ny.local.yonkers.nonresident.supplemental.rate`: Register row US-NY-011 is superseded/A.2; the value cannot be carried as a fact. What would close it: Replace US-NY-011 with an active A.1/A.2 row (see _research/stage5/ACCESS-GAPS.md).
- Plus 64 sourced values carried in `unresolved[]` only because of the register-id pattern defect (see the header); what would close them: a contract PATCH widening the `register_id` pattern.
