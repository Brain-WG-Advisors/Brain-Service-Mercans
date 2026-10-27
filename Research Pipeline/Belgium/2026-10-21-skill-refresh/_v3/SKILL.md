---
name: payroll-compliance-belgium
description: Belgium private-sector payroll compliance, income year 2026. NSSO/RSZ-ONSS filings (Dimona, DmfA, DmfA modification, DRS/ASR), FPS Finance filings (FinProf 274, Belcotax-on-web 281.10), Febelfin SEPA pain.001 and the Fedris work accident declaration. Gross-to-net (13.07% employee contribution, two-component social work bonus, special social security contribution, Annex III withholding tax), employer contributions, benefits in kind, CO2 solidarity contribution, leave and holiday pay, termination and notice indemnities. Carries the Wage Type Catalogue (827 rows, Global WTC 62/65/79 complete), the Data Dictionary with the NSSO code tables (92 option mappers), the 9 report specs, the payslip generator and the statutory integration register. Use for any question about Belgian payroll rates, thresholds, filings, wage types, field mappings or payslip layout.
---

# Belgium payroll compliance — router

**ALWAYS use the Read tool on the relevant reference file BEFORE answering. Do NOT answer
BE-specific rates, thresholds, or rules from general knowledge.**

Belgian payroll parameters step several times inside a single year, and three of them — the
social work bonus, the GMMI, and the CO2 solidarity multiplier — step on *different* calendars.
A figure recalled rather than read is a figure attached to the wrong date.

The reference files are verbatim conversions of the delivered artifacts. They are large; each
one opens with a line-numbered navigation index, so read with `offset`/`limit` rather than
pulling a whole file.

---

## Version of record

| Artifact | Version | Reference file |
|---|---|---|
The Google Shared Drive (Compliance Team › Country Folders › Belgium) is the version of record.
Version numbers below are the **Drive** numbers; the pipeline build numbers they replaced are in
brackets.

| Artifact (Drive) | Version | Reference file |
|---|---|---|
| CCG — `05 - Payroll Regulation Guide › BE-CCG-001-v1.0` | **v1.0** on the Drive, as at 21 October 2026 (= pipeline v1.2 of 16 September 2026 + the 13 October 2026 employer-rate correction) | `references/01-ccg.md` |
| WTC — `03 - WTC › BE-WTC-001-v1.2` | **v1.2**, 21 October 2026 (827 catalogue rows) | `references/02-wtc.md` |
| DD — `02- DD › BE-DD-001-v1.0` | **v1.0** on the Drive (content identical to pipeline v1.4 of 16 September 2026; only the Version Control differs) | `references/05-data-dictionary.md` |
| SIR — `17 - Statutory Integrations › BE-SIR-001-v1.0` | v1.0 | `references/03-sir.md` |
| Report specs — `12- Country Report Codes`, 9 workbooks | **v1.1**, 19 October 2026 (Field Explanation in English) | `references/04-reports-spec.md` |
| Payslip generator — `18 - Payslip` | as delivered | `references/06-payslip.md` |
| QA report | as at 2026-08-17 16:35 | `references/07-qa-report.md` |

**Refreshed 21 October 2026.** `01-ccg.md`, `02-wtc.md`, `04-reports-spec.md` and
`05-data-dictionary.md` were regenerated from the Drive files above. What is new since the
16 September package:

- **WTC v1.1 — Global WTC 62, 65 and 79 series completed.** 468 rows added at catalogue rows
  361–828, after BE-059 (so every row number cited elsewhere is unchanged): 62 series 247 (178
  five-digit, 69 four-digit 6201–6289), 65 series 148, 79 series 73, checked against Global Wage
  Type Catalogue 1.1 and 1.2 (identical in these series). **Each added row follows the Belgian
  treatment of an existing wage type named in its Formula column** — read that row for the legal
  basis. 17 added codes are NA with the reason stated (no statutory end-of-service gratuity,
  contractor payments, unpaid leave, parking allowance, donation recovery).
- **Employer basic contribution corrected in the CCG (13 October 2026):** category 1 workers
  **19.88%** from Q1 2018 (tax shift), plus wage moderation of up to 5.12% — about 25.00% in
  total. 24.92% was the basic rate from Q1 2015. Source cited in the CCG: ONSS DmfA instructions,
  "Les cotisations". **WTC v1.2 (21 October 2026)** applies the same correction to row 23671
  (Wage Type Catalogue!F58), checked against the NSSO administrative instructions 2025/4.
- **Report Specs v1.1** — Field Explanation translated to English in the 9 specs; codes, XML tags
  and masks unchanged.
- The Drive CCG keeps its internal cover line "Version 1.2 — 16 September 2026" under the
  Drive file name v1.0; both refer to the same text.

**Earlier refresh — 16 September 2026 (Stage 11).** What was new then, against the
2026-08-17 package:

- **DD Country Option Mappers closed out** — 87 blocks / 1,043 rows → **92 blocks / 2,018 rows**.
  Loaded from the authority's own publications: Bijlage 21 worker status (45 rows), Bijlage 2
  worker codes (186), Bijlage 27 employer categories (289), Bijlage 26 joint committees (225),
  Bijlage 44 work reorganisation (58), Bijlage 35 employment promotion (15), zone 00221
  Reference Type (9), NSSO contribution-payment purpose (5), DRS Bijlage 12 Risk Identification
  (78), DmfA Remuneration Code (44) and DmfA Service Code (52).
- **DmfA Remuneration Code and Service Code live in the DD, not the WTC.** The gap spec
  nominated `BE-WTC-001` for both; the WTC's structural contract is six sheets and twenty
  columns with no place for a code table, so they were loaded into the DD and the WTC's Form
  Reference Guide points at them. Route code-table questions to `05-data-dictionary.md`.
- **Social work bonus annual cap closed** — EUR 3,466.44 from 1 January 2026, EUR 3,523.92 from
  1 April 2026, **EUR 3,594.36 from 1 July 2026** (NSSO instructions 2026/3). In both
  `01-ccg.md` and `02-wtc.md`.
- **Article 11bis, Employment Contracts Act of 3 July 1978** — a written individual contract is
  required for *each* part-time employee, in place at the latest when performance starts.
- **DRS Bijlage 12 resolved, not left pending** — carried in the DD as Risk Identification, keyed
  on zone 00430 / `IdentificationOfRisk` / functional block 90064.
- **Contract Duration Type is resolved-not-applicable** — zone 00050 is a strict binary
  (0 = voltijds, 1 = deeltijds); "clearly defined work" is a labour-law concept, not a DmfA field.

Two known residuals, carried deliberately rather than papered over: `03-sir.md` and
`07-qa-report.md` are verbatim copies of the SIR and QA artifacts, which were outside the Stage
9.6 rename fence, so they still cite `BE-WTC-001-v1.0.xlsx`. Those are dated records of what was
true when written — read that filename as catalogue rows 2–360 of the current WTC v1.2, which are
unchanged. Likewise, CCG "v1.2" and DD "v1.4" in older text are today's Drive CCG v1.0 and DD v1.0.

---

## Design clarifications — confirmed corrections

Each item below was established against a primary source during the Belgium build, and each
corrects a mistake that was actually made — in this corpus or in general Belgian practice.
`(engine)` means it changes a calculated amount.

1. **The social work bonus is TWO components, R_B + R_A — not one. (engine)**
   Since 1 April 2024 (RD of 5 March 2024) the reduction of the personal social security
   contribution has a component B and a component A, each with its own full-amount limit, its
   own maximum and its own degressive coefficient. They are computed separately and added:
   `P = R_B + R_A`. Component B's degressive band ends exactly where component A's full-amount
   limit sits, so the two dovetail.
   **The mistake:** reading it as "grant the full amount below the upper limit, nothing above"
   and granting a single maximum. Each component pays its maximum only at or below *its own*
   full-amount limit, pays a **degressive** amount between that limit and its own zero point,
   and pays nothing above it. This corpus made exactly that error: worked examples 2, 4 and 6
   granted only EUR 127.54 (white-collar) or EUR 137.74 (blue-collar) — those are the component
   A maxima alone — understating the bonus and every figure downstream of it. Read `01-ccg.md`
   Module 5.1.1, which governs, and select the parameter row **by the pay month**.

2. **Basic tax-free allowance for WITHHOLDING is EUR 11,170 (Annex III nr. 32) — not 11,180,
   not 11,550. (engine)**
   Delivered as a reduction of EUR 2,987.98 (`11,170 × 26.75%`).
   **The mistake:** all three figures circulate for income year 2026 and only one belongs in
   payroll. EUR **11,180** is the *counterfactual* indexed art. 131 ITC 92 amount — what the
   allowance would have been had the reform not passed — and it never took effect; it is wrong
   in every reading. EUR **11,550** is the *assessment* allowance (art. 131 ITC 92, income year
   2026 / assessment year 2027, post-reform), a different instrument for a different purpose.
   Withholding applies 11,170; the final assessment applies 11,550 and the difference is
   refunded to the employee. This corpus carried 11,180 until it was corrected.

3. **Annex III withholding bracket ceilings are 16,710 / 29,500 / 51,050 — the assessment
   brackets are 16,720 / 29,510 / 51,070. (engine)**
   They are not the same pair and are **not derivable from each other by any rounding rule**.
   Annex III nr. 31 sets its own scale and it must be read off the annex each year. The
   withholding rates (26.75% / 42.80% / 48.15% / 53.50%) are the assessment rates (25 / 40 /
   45 / 50%) increased by the notional 7%, but the ceilings are set independently and differ by
   EUR 10 to EUR 20.
   **The mistake:** using one pair for the other's purpose — a real, propagated error in this
   build.

4. **Notice indemnity withholding uses Annex III nr. 58, routed there by nr. 62 — NOT nr. 53.
   (engine)**
   nr. 58 is the arrears-and-severance scale: eighteen bands, 0.00% to **48.00%**. nr. 53, the
   general exceptional-payment table, tops out at 53.50% and **excludes notice indemnities in
   terms** (*andere exceptionele vergoedingen en toelagen dan opzeggingsvergoedingen*).
   Confirmed against multiple primary annex-text years. Under nr. 62 the percentage is keyed on
   the remuneration that served as the basis for determining the indemnity.
   **The mistake:** applying the nr. 53 table. On the CCG's worked settlement that is 53.50%
   instead of 38.96% — an over-withholding of **EUR 5,766.20 on one settlement**. Diagnostic: a
   large refund on a notice indemnity at assessment usually means nr. 53 was applied, because
   nr. 58 is built to approximate the ITC 92 art. 171 average rate.

5. **Company car age coefficient: 100% for the first 12 months, then −6 percentage points per
   elapsed year, floor 70%. Two elapsed years is 88%, not 94%. (engine)**
   Months 13–24 = 94%; months **25–36 = 88%** (`100% − 6 × 2`).
   **The mistake:** counting elapsed years from the *year of registration* instead of from the
   registration *date*, which lands one band too high. A car first registered in March 2024 is
   at 94% only until February 2026 and moves to 88% from March 2026. The coefficient is driven
   by the **benefit month**, not by the calendar year. This one-year miscalculation propagated
   through 8 figures in this corpus before it was corrected.

6. **CO2 solidarity multiplier: 4.00 from 1 January 2026 — and it multiplies the calculated
   contribution ONLY, never the minimum. (engine)**
   Law of 25 November 2021 organising the fiscal and social greening of mobility, Article 34, 1°
   (Belgian Official Gazette 3 December 2021, numac 2021033910) completes Article 38, §3quater,
   3° of the Law of 29 June 1981 with the full schedule: 2.25 from 1 July 2023, 2.75 from
   1 January 2025, **4.00 from 1 January 2026**, 5.50 from 1 January 2027.
   **The mistake:** applying the factor to the minimum contribution as well. The same Article
   34, 1° raises the minimum *separately*, in its point b) — EUR 25.99 non-indexed from
   1 January 2026, which is EUR 42.34 once indexed at the 2026 coefficient of 1.6291. Vehicles
   bought, leased or rented before 1 July 2023 are excluded from **both** increases, which is
   why two minimum-contribution rows exist (EUR 33.93 / EUR 42.34).
   *Corpus note:* `07-qa-report.md` §3 still lists `BE-X10-022` as an open blocker on the ground
   that this figure rested on four tier-B vendor sources marked `CONFIRMED`. That was true when
   the report was written and is no longer: the citation above was landed in the CCG **and** in
   WTC `Wage Type Catalogue!F59` afterwards. Read the cell, not the report.

7. **Special social security contribution: THREE separately-labelled household tables, and the
   fiscal-household situation selects the table. (engine)**
   Table 1, individually-assessed employee (quarterly cap EUR 182.82); Table 2, jointly assessed
   with a spouse **having** professional income (cap EUR 154.92); Table 3, jointly assessed with
   a spouse having **no** professional income (cap EUR 182.82).
   **The mistake:** treating it as one banded table, or selecting by the cap. Two of the three
   tables share the EUR 182.82 maximum, so the *situation* selects the table, not the maximum.
   Table 1 has a 3.38% band; **Tables 2 and 3 have none**. The fixed **EUR 15.45** low-band
   amount exists **only in Table 2** — only where the spouse has professional income — and must
   not be applied under Tables 1 or 3, where the employee pays nothing until the quarterly wage
   reaches EUR 5,836.15.

8. **That contribution is banded on the QUARTERLY wage, so months 1 and 2 are provisional.
   (engine)**
   Withhold provisionally and **correct at the last pay of the quarter**. A mid-quarter hire,
   termination or salary change moves the quarterly total and therefore the band; the same is
   true of the high-wage exemption. Both must be recomputed at quarter end rather than treated
   as monthly-final. The special social security contribution is **not deductible** from the
   taxable base, and it survives the one-fifth assignment cap because it is a deduction imposed
   by law.

9. **Reference-remuneration factor for the exceptional-payment brackets: Mercans standardizes on
   × 13.92. (engine)**
   Normal annual gross remuneration = monthly gross × 13.92 (twelve months plus double holiday
   pay plus end-of-year premium). A bonus paid to an employee on EUR 3,000/month is keyed on
   EUR 41,760, not EUR 36,000.
   **This one is genuinely disputed in Belgian practice, not a simple error** — respectable
   sources use a different factor. State it as a Mercans standardization. Keying the table on
   twelve monthly salaries understates the reference and selects a lower band.

10. **The GMMI calendar and the work-bonus calendar are NOT the same calendar. (engine)**
    The GMMI steps **1 January, 1 April and 1 August 2026**. The work bonus parameter set steps
    **five times — 1 January, 1 March, 1 April, 1 July and 1 September 2026 — and has no
    1 August row**. The 1 March and 1 September steps are not GMMI movements at all: they index
    the *upper* limit (the wage at which the bonus reaches zero) on the social-benefit calendar.
    **The mistake:** conflating the two — which sends a reader looking for an August work-bonus
    row that does not exist, or asserts that the GMMI moves on 1 July. Both errors occurred here,
    in two different artifacts. Module 5.1.1 governs; select by pay month.

11. **The fiscal work bonus is a percentage of the social work bonus granted, and the percentage
    differs BY COMPONENT: 33.14% of component A, 52.54% of component B. (engine)**
    Subject to the EUR 765 annual cap (applied from income year 2025). Available only to
    employees who actually receive the social work bonus; no separate declaration — it is
    derived.
    **The mistake:** applying one blended percentage. Two live gaps attach to it: the announced
    reinforcement (component B to 63%) is **NOT CONFIRMED AS ENACTED**, and the indexation status
    of the EUR 765 is **NOT RESOLVED**. See `01-ccg.md` Module 7.1.

12. **CBA no. 90 bonus has TWO different ceilings, and the gap between them is deliberate.
    (engine)**
    Social ceiling EUR **4,255** (2026): within it, a 33% special employer contribution and a
    13.07% employee solidarity contribution replace ordinary contributions. Tax ceiling EUR
    **3,701** (2026): within it, exempt from income tax.
    **The mistake:** using one ceiling for both — the CCG names it "a frequent configuration
    error". The amount between EUR 3,701 and EUR 4,255 is socially exempt but **taxable**.

13. **The inbound-taxpayer regime diverges between tax and social security above EUR 90,000 of
    reimbursement. (engine)**
    For tax: up to 35% of gross may be paid as an exempt reimbursement of the employer's own
    costs, the former EUR 90,000 annual cap **abolished** for tax purposes from income year 2025,
    minimum gross EUR **70,000** (reduced from 75,000; no minimum for researchers).
    **The NSSO did not adopt the same reform** — for social security purposes the prior
    EUR 75,000 minimum and EUR 90,000 cap on the exempt reimbursement still apply.
    **The mistake:** applying the tax parameters on the social security side. The tax-exempt and
    SS-exempt amounts must be computed separately above EUR 90,000.

14. **LIMOSA is OUT OF SCOPE — it is filed by the FOREIGN posting employer, never by the Belgian
    payroll client.**
    Programme Law (I) of 27 December 2006, Title IV Ch. VIII, arts. 137, 139, 141 and 155 (MB/BS
    28 December 2006), executed by the RD of 20 March 2007. The posted population stays on its
    home-country payroll under an A1 and is typically **not on Belgian payroll at all**, so the
    engine holds none of the source data. The only Belgian-side duty is the art. 141 check —
    verify the Limosa-1 acknowledgement, report to the NSSO only where it cannot be produced —
    which fires on a missing document, not on a pay run, and is HR/onboarding scope.
    `BE-NSSO-005-Limosa-Spec.xlsx` is retained on disk as a **descoped** artifact (the evidence
    of *why* it is out of scope), and SIR OUT-08 is retained and reclassified rather than
    deleted, so a reader finds the determination instead of a silent gap. A related mis-citation
    was corrected in the same pass: the Law of **11 February 2013** is not the basis of Limosa —
    it transposes Directive 2009/52/EC and governs employers of illegally staying third-country
    nationals.

15. **Work bonus legal basis: Law of 20 December 1999 art. 2 → RD 17 January 2000 → RD 27 March
    2023 → RD 5 March 2024. NOT Programme Law of 24 December 2002 art. 353bis.**
    Article 353bis governs the continuation of the **employer-side target-group reduction** on
    restructuring or legal transformation (inserted by art. 200 of the Law of 22 December 2008,
    in force 1 January 2009) and says nothing about the employee's own contribution. The social
    work bonus is a reduction of the **personal** contribution. RD 17 January 2000 (BS 28 January
    2000, numac 2000022082) carries the formula and the parameters; RD 27 March 2023 (BS 12 April
    2023, erratum 21 April 2023) inserted the very-low-wage threshold; RD 5 March 2024 (BS
    18 March 2024) split the reduction into the two components and expressed each maximum as a
    percentage of the GMMI.
    **This was a real sourcing error in this build** — the wrong instrument was cited in the CCG
    and had propagated to five cells across the WTC and the payslip. Note also: **no 2026
    instrument sets the 2026 figures.** Each step follows parametrically from the decrees (maxima
    at 5.71% and 7.70% of the GMMI, component A's full-amount limit at 131.5328% of it), so the
    published NSSO figures are the operative source for the *values* and the decrees for the
    *mechanism*.

16. **The social work bonus annual cap after 1 July 2026 is NOT FOUND — and must not be
    extrapolated. (engine)**
    EUR 3,466.44 from 1 January 2026 and EUR 3,523.92 from 1 April 2026 are published (NSSO
    administrative instructions editions 2026/1 and 2026/2). The July value would be closed by
    the NSSO instructions covering Q3 2026, which did not exist at build time.
    **The mistake:** deriving it by applying the same ~2% indexation used on the other
    parameters. Do not. The gap is registered in `scope_manifest.json → known_limitations[9]`
    and carried as `NOT FOUND` in six downstream cells (in Dutch, `NIET GEVONDEN`).

17. **The language of a personnel document is imposed by the employer's SEAT OF OPERATION
    (exploitatiezetel) — not the employee's residence, the contract language, or the parties'
    preference.**
    Dutch-language region → Dutch, sanction **nullity** (Decree of 19 July 1973); French-language
    region → French, **nullity** (Decree of 30 June 1982); Brussels-Capital → the employee's
    language, sanction translation at the employer's expense with retroactive effect;
    German-language region → German, sanction replacement of the document. **A bilingual payslip
    is not permitted.** The establishment unit number carries the address that determines the
    regime. The same establishment-unit logic — not the employee's home region — drives the
    regionalised target-group reductions, child benefit and training incentives.

18. **The non-resident fixed 7% federal additional levy must NOT be modelled in payroll.**
    ITC 92 art. 245 applies a fixed 7% in place of municipal tax, because a non-resident has no
    Belgian commune of residence. In *Chefquet* (Case C-119/24, judgment of 12 March 2026) the
    CJEU held that fixed rate contrary to art. 45 TFEU. This is an **assessment-level** matter,
    not a withholding one: it must not be modelled in the WTC, the DD or the payslip. Regional
    and municipal surcharges generally are not withheld at source and are not modelled
    (`known_limitations[1]`).

19. **Wage-type references in the Report Specs join on `Mercans Code`, not on the English name.**
    Every spec cell naming a wage type now carries its code in square brackets **alongside** the
    name; the name is never removed. `BE-WTC-001` column A is the join key and it is populated
    for all catalogue rows. The specs were built against the 359 rows of September 2026; the
    468 Global WTC rows added in v1.1 (rows 361–828) are not referenced by any spec cell.
    **One deliberate exception:** tax code 250 is carried by **147 of those 359** rows and is *not*
    enumerated — that cell states the join rule and says the list was not written out, rather
    than truncating in silence. Verified counts: 233→9, 234→4, 252→14, 254→19, 285→5, 305→3,
    308→4, 317→6, 250→144.

20. **`contract_type` and `contract_duration_type` are two different mappers — and the collision
    survives in the payslip.**
    `contract_type` is the **full-time / part-time** mapper, and its two codes are the whole
    domain of the field (NSSO DmfA glossary). `contract_duration_type` is the six-value
    indefinite/fixed-term family, and **four of its six values carry `Code = "NOT FOUND"`** —
    NSSO zone 00885 publishes only 0 (indefinite) and 1 (fixed term). The manifest was renamed on
    2026-08-17 to separate them; `BE-X10-005` records that the payslip still carries the
    collision, **including in the delivered render**. Do not assume a "Contract Type" label in
    the payslip is the full-time/part-time mapper without checking which domain it holds.

---

## Routing table

| Topic | Read |
|---|---|
| Rates, thresholds, formulas, gross-to-net, worked examples, legal basis for any calculation | `references/01-ccg.md` (Drive v1.0, 21 October 2026) |
| Which CCG module | Mod 1 jurisdiction, calendars, rounding · Mod 2 master data · Mod 3 gross-to-net flow · Mod 4 gross compensation, GMMI, overtime, bonuses · Mod 5 social security, work bonus, special contribution · Mod 6 withholding tax, Annex III · Mod 7 deductions, BIK, company car, garnishment · Mod 8 statutory leave and holiday pay · Mod 9 termination and irregular payments · Mod 10 reporting and finalisation · Mod 11 advanced and cross-border · Mod 12 worked examples |
| Wage type codes, mapping to a payroll element, tax codes, Global WTC coverage, sick-leave-paid-by-employer bands, tax credits | `references/02-wtc.md` (v1.2, 827 catalogue rows; Global 62/65/79 slots at rows 361–828) |
| Which file goes where, filing channels, deadlines, SLAs, credentials, error and anomaly models, the inbound/outbound flow register (OUT-01…19 / IN-01…19), the 27-entry gap register G1–G27 | `references/03-sir.md` |
| Field-by-field layout of a statutory filing, XPath and XML labels, field lengths, code tables, population rules, sample files | `references/04-reports-spec.md` (9 workbooks; use the nav index — this file is ~2 MB) |
| Which report spec | Dimona · DmfA · DmfA modification · DRS/ASR · Limosa (**descoped**, reference only) · FinProf 274 · Belcotax 281.10 · Fedris work accident · Febelfin SEPA pain.001 |
| HRBLIZZ field names, data types, option mappers and their codes, ID information, employer/legal-entity vs employee fields, unresolved code tables | `references/05-data-dictionary.md` (Drive v1.0 — 92 option-mapper blocks, 2,018 code rows) |
| Payslip layout, line ordering, labels in EN and NL, payslip spec sections, field options, unit rates, population ranges | `references/06-payslip.md` |
| Accuracy band per artifact, open blockers and majors, what is unresolved versus defective, what would close each gap, how a claim was measured | `references/07-qa-report.md` |
| Anything about scope — in/out, descoped items, the integration register, known limitations | `references/07-qa-report.md` §§3–7, and the dossier's own `scope_manifest.json` |

---

## How to answer

1. **Read the reference file first.** Identify the topic, route with the table above, open the
   file's nav index, then read that section. Never answer a rate, threshold, date, field name,
   code or legal citation from general knowledge.
2. **Quote verbatim.** Reproduce the figure exactly as the artifact carries it — EUR 2,987.98,
   not "about EUR 2,988"; 26.75%, not "roughly 27%". Where the artifact gives a formula, give
   the formula.
3. **Cite the legal basis** the artifact cites, at the level of precision it uses: instrument,
   date, article. "Annex III nr. 58" and "RD of 5 March 2024" are answers; "Belgian tax law" is
   not.
4. **Give the date the parameter applies from.** Belgian 2026 parameters step mid-year on several
   different calendars. A figure without its from-date is not usable.
5. **Preserve the Dutch and French terms** where the artifact does — *werkbonus / bonus à
   l'emploi*, *bedrijfsvoorheffing*, *bijzondere bijdrage voor de sociale zekerheid*,
   *exploitatiezetel*, *uitzonderlijke vergoedingen*, *Limosa-1*, *DmfA*, *Dimona*. Filing
   channels and portal labels are language-specific.
6. **Flag `NOT FOUND` and `known_limitations` items as such.** Where the artifact records a value
   as NOT FOUND, say it is not found, name the source that would close it, and do not supply a
   plausible number. Do not extrapolate from a neighbouring parameter.
7. **Say plainly when something is not covered.** The dossier is private-sector, federal, income
   year 2026. If the question falls outside that — public sector, self-employed, company
   directors, regional surcharges, assessment-level taxation — say so and say why, rather than
   generalising from what is here.
8. **Where the QA report and an artifact disagree, read the artifact and say which you read.**
   `07-qa-report.md` is the record as of 2026-08-17 16:35 and was NOT regenerated in the 16 September refresh, so it predates the Stage 9.5 gap closure and the Stage 9.6 renames; several of its findings were
   closed later that evening — the CO2 multiplier citation, the work-bonus legal basis, the
   wage-type join key, 13 XML labels, 148 Belcotax queries. The dossier's
   `PROPAGATION-LEDGER.md` carries those closures.

---

## Scope and limits

- **Private sector, federal, income year 2026.** The scope is the Belgian federal private-sector
  employee population declared through Dimona and the DmfA. Company directors and self-employed
  persons are out of scope and sit under a different social security regime.
- **Currency EUR**, two minor units. Rounding conventions are in `01-ccg.md` Module 1.5 — read
  them before reproducing a computed amount.
- **Language: Dutch is built; French and German are not, and they are two different kinds of
  gap.** The payslip ships `Belgium (NL)` and `Belgium (EN)` and nothing else. Per
  `scope_manifest.json → known_limitations[5]`: **French (FR) is a mandatory second deliverable,
  not an option** — a French-region employer cannot be served without it, because the sanction
  for the wrong language is nullity of the document, not a translation duty. **German (DE) is an
  explicit unbuilt seam.** Neither has a payslip sheet, a label set, or a gap register of its
  own. Statutory content — rates, thresholds, field layouts — is language-independent and applies
  unchanged; what is missing is the rendered document and its labels.
- **Limosa is out of scope**: it is filed by the foreign posting employer, not by the Belgian
  payroll client (Programme Law of 27 December 2006, arts. 137/139/141/155).
- **Nine authority filings are specified; none has been submitted.** There is no portal
  round-trip and no accepted filing anywhere in the dossier. Treat every spec as
  official-source-derived, not production-proven.
- **No tier verdict exists for Belgium.** BE predates the tier convention, and no tier was
  invented for it. Do not quote one — see `07-qa-report.md` §1.
- **Sectoral (joint committee) minimum scales, end-of-year premium rules and index dates are
  per-client configuration** and are not enumerated in the dossier.

---

## What good answers look like

**GOOD**

> The withholding on a notice indemnity takes the Annex III **nr. 58** arrears-and-severance
> percentage, to which **nr. 62** routes notice indemnities — eighteen bands, 0.00% to **48.00%**,
> keyed on the remuneration that served as the basis for determining the indemnity. It is **not**
> the nr. 53 exceptional-payment table: nr. 53 excludes notice indemnities in terms (*andere
> exceptionele vergoedingen en toelagen dan opzeggingsvergoedingen*).
>
> On the CCG's worked example (Module 9.1, Step 6), an annual current remuneration of
> EUR 67,778.40 falls in the band EUR 62,465.01 – 71,160.00, so the rate is **38.96%**. Applying
> the nr. 53 top rate of 53.50% instead would have withheld EUR 21,216.78 — an over-withholding
> of EUR 5,766.20 on that single settlement.
>
> Legal basis: ITC 92 arts. 171, 5° and 270–275; Annex III to the RD implementing ITC 92,
> nrs. 53, 58–60 and 62. Source: `references/01-ccg.md` Module 9.1.
> Caveat: no filing has been round-tripped through FinProf — see `references/07-qa-report.md`
> §2.4.

Why it is good: verbatim figures, the negative stated explicitly (what it is *not*), the legal
instrument named down to the annex number, the module it was read from, and a cross-reference to
the QA report for the limit on confidence.

**BAD**

> Severance pay in Belgium is taxed separately at the employee's average rate from the previous
> year, and the employer withholds around 50% at source using the special table for exceptional
> payments. The tax-free allowance is roughly EUR 11,000.

Why it is bad: no citation and no source file; "the special table for exceptional payments" is
nr. 53, which is the wrong table and would over-withhold by thousands of euro; "around 50%" is
above nr. 58's 48.00% ceiling; and "roughly EUR 11,000" collapses three distinct figures —
11,170 withholding, 11,550 assessment, 11,180 never enacted — into a rounded number that is none
of them.
