# Sweden 2026 – facts for AGI validation, period 202609 (source IDs refer to sources.md)

## 1. AGI technical description (version in force for 202609)
- Technical description **1.1.18.2** is current (page modified 2026-05-20). XML schema **1.1**: `arbetsgivardeklaration_1.1.xsd` + `arbetsgivardeklaration_component_1.1.xsd`. [S01, S02, S03]
- The attachments are labelled 1.1.18.1 (Fältlista, Kontroller, Struktur: revision 2025-12-08). Summering och beräkningsregler: last revision 2026-01-16. No 1.1.18.2-labelled attachment exists; the 1.1.18.1 files are the ones linked from the 1.1.18.2 page. [S01, S04–S07]
- Root element `Skatteverket`, attribute `omrade="Arbetsgivardeklaration"`. Every data element carries a fixed `faltkod` attribute. UTF-8 with or without BOM. [S01 §10.3, §11.2]
- Mandatory on every HU and IU: FK006 RedovisningsPeriod (ÅÅÅÅMM) and FK201 AgRegistreradId (12 digits; legal persons use the prefix 16). FK570 Specifikationsnummer is mandatory on every IU and must be unique per payee, period and employer. [S01 §8.1; S06]
- Identity on an IU: one of FK215 BetalningsmottagarId, FK222 Fodelsetid or FK224 AnnatId. [S01 §8.3.1]
- Exactly one of 7 tax fields per IU: FK001 AvdrPrelSkatt, FK274 AvdrSkattSINK, FK275 AvdrSkattASINK, FK114 SkattebefrEnlAvtal, FK276 EjskatteavdragEjbeskattningSv, FK253 Lokalanstalld, FK094 AmbassadanstISvMAvtal. If an amount field applies but no tax was deducted, report 0. [S01 §8.3.2]
- Benefits paid in full by net-pay deduction must still be reported with value 0 (e.g. FK013). Fuel benefit FK018 = market value × 1.2. Net-pay deduction for fuel goes in FK098. [S01 §5.3]
- Field codes (complete list of 111 codes in `agi/fk_compact.tsv`, columns: FK, element, name, form, type, period from, period to). [S04] The main ones:

| FK | Element | Meaning | Form | Type |
|---|---|---|---|---|
| FK001 | AvdrPrelSkatt | Preliminary tax deducted | IU | BELOPP10 |
| FK006 | RedovisningsPeriod | Reporting period ÅÅÅÅMM | IU/HU/FU | REDOVISNINGSPERIOD |
| FK010 | AvrakningAvgiftsfriErs | Earlier contribution-free pay that is now subject to contributions | IU | BELOPP7 |
| FK011 | KontantErsattningUlagAG | Cash gross pay, basis for contributions | IU | BELOPP10 |
| FK012 | SkatteplOvrigaFormanerUlagAG | Other taxable benefits, basis for contributions | IU | BELOPP10 |
| FK013 | SkatteplBilformanUlagAG | Car benefit | IU | BELOPP7 |
| FK018 | DrivmVidBilformanUlagAG | Fuel with car benefit (×1.2) | IU | BELOPP7 |
| FK019 | AvdragUtgiftArbetet | Deduction for work expenses | IU | BELOPP8 |
| FK020 | AndraKostnadsers | Other expense allowances | IU | BELOPP10 |
| FK023 | AndelStyrelsearvode | Of which board fees | IU | BELOPP10 |
| FK030 | Tjanstepension | Occupational pension | IU | BELOPP10 |
| FK032 | ErsEjSocAvgEjJobbavd | Pay that gives no jobbskatteavdrag | IU | BELOPP10 |
| FK041/FK043 | Bostadsforman… | Housing benefit (house / not a house) | IU | KRYSS |
| FK048 | FormanHarJusterats | Benefit value adjusted | IU | KRYSS |
| FK050 / FK051 | Bilersattning / Traktamente | Mileage allowance / per diem paid (flag) | IU | KRYSS |
| FK060 | Arbetsstallenummer | Workplace number | IU | 0–99999 |
| FK062 / FK063 | Växa-stöd | **Ended 202512**; must not appear in 2026 periods | IU | KRYSS |
| FK098 | BetForDrivmVidBilformanUlagAG | Paid for fuel by net-pay deduction | IU | BELOPP7 |
| FK131–FK138 | …EjUlagSA | Pay not subject to tax deduction or contributions | IU | |
| FK201 | AgRegistreradId | Employer ID | IU/HU/FU | IDENTITET |
| FK205 | Borttag | Deletion | IU | KRYSS |
| FK215 | BetalningsmottagarId | Payee personnummer / samordningsnummer | IU/FU | IDENTITET |
| FK216–FK221, FK230 | Name / address | Required when FK215 is missing | IU | |
| FK222 / FK224 | Fodelsetid / AnnatId | Alternative identity | IU | |
| FK245 / FK246 | ArbetsplatsensGatuadress / Ort | Workplace address | IU | TEXT50 |
| FK252 / FK076 | TIN / LandskodTIN | Foreign TIN | IU | |
| FK274 / FK275 | AvdrSkattSINK / ASINK | SINK / A-SINK tax | IU | BELOPP10 |
| FK302 | EjFastDriftstalleISv | No permanent establishment in Sweden | HU | KRYSS |
| FK303 | EjFastDriftstalleIndivid | Payee not covered by the permanent establishment | IU | KRYSS |
| FK305 | KonventionMed | Social security convention code | IU | [1-9][A-Z] |
| FK463 | AnnatDriftstod | Other operating aid (**new from 202601**) | HU | BELOPP12 |
| FK470–FK477 | Ulag/Avdrag FoU, Regionalt stöd, Rederi | Deductions from contributions | HU | |
| FK481 / FK486 | UlagSlfVinstandel / SlfVinstandelFK486 | SLF on profit-sharing / sickness pension (24.26 %) | HU | BELOPP12 |
| **FK487** | SummaArbAvgSlf | **Total employer contributions + SLF** | HU | BELOPP12 |
| FK491 / FK495 | Pension/insurance tax basis / tax | | HU | BELOPP12 |
| FK492 / FK496 | Interest/dividend tax basis / tax | | HU | BELOPP12 |
| **FK497** | SummaSkatteavdr | **Total tax deducted** (prelim + SINK + A-SINK) | HU | BELOPP12 |
| FK499 | TotalSjuklonekostnad | Sick-pay cost (**ended 202406**) | HU | |
| FK570 | Specifikationsnummer | IU specification number 1–9999999999 | IU | |
| FK820–FK827 | Franvaro… | Absence record (FP/TFP), date, %, hours | FU | |

- Control rules: `agi/Bilaga_Kontroller_1.1.18.1.xlsx` (ba_ = processing, S_ = within form, B_ = across forms, R_ = reasonableness). B_006: FK487 must equal Skatteverket's computed IK587. B_007: FK497 must equal IK597. "Mindre beräkningsdifferens accepteras" (minor differences accepted; the tolerance is not quantified). [S05]
- Calculation of FK487 [S01 §12.6.1; S07]:
  1. Sum the contribution-liable pay per IU (AeIU). Öre from the fuel benefit are dropped.
  2. Sum per employer and period into a basis per rate: IK420 (full 31.42 %, Alder_1), IK422 (10.21 %, Alder_2 = born 1938–1958), IK423 (0 %, born ≤1937), IK7001 (youth, born 2003–2007, the first 25 000 kr per person and month, from 202604). For a person with several IUs, the pay is summed across all of them before splitting at 25 000.
  3. Fee = basis × rate per rate. **Öre are dropped on each rate separately.**
  4. Add or subtract FK486, FK475, FK476 and FK477.
  5. Sum.

## 2. Tax tables 2026 (monthly)
- Legal instrument: SKVFS 2025:20, in force 2026-01-01, applies to tax deductions from income paid in 2026. Only one 2026 set is published; no mid-year revision is listed as of 2026-10-14. [S13 p.3; S14]
- Tables 29–42 exist. The table number is the total municipal rate (municipality + region + burial fee, plus church fee if the person is a member) rounded to a whole number: 32.50 → 32, 32.51 → 33. Municipal rates are in `skattesatser-kommuner-2026.txt`. [S14; S16]
- Column meanings for 2026. The tax age test is 66 at the start of the year, i.e. born 1959 or earlier (INFERENCE from "fyllt 66 vid årets ingång"). [S13 p.5; S14]
  - Col 1: salaries, fees and similar pay to a person who had **not** turned 66 at 1 Jan. Pays allmän pensionsavgift and gets jobbskatteavdrag.
  - Col 2: pensions and similar income to a person who had turned 66. No pensionsavgift, no jobbskatteavdrag, higher basic allowance (förhöjt grundavdrag).
  - Col 3: salaries to a person who had turned 66. Higher jobbskatteavdrag and higher basic allowance. Also used for people born 1937 or earlier who have earned income.
  - Col 4: sickness and activity compensation to a person under 66.
  - Col 5: other pensionable payments (e.g. unemployment fund benefits) to a person born 1938 or later. No jobbskatteavdrag.
  - Col 6: pensions and similar income to a person under 66 (no pensionsavgift).
- Pay above the table: up to 80 000 kr the monthly table gives an amount in kronor. Above 80 000 it gives a **percentage of the whole monthly pay** in the "%" records, with bands that break whenever the percentage changes. The last band has no upper limit (e.g. table 33 col 1: 1 269 001 kr and above = 52 %). [S13 p.7 §5, p.26 §9; S10]
  - That the percentage applies to the whole amount (not only the excess) is read from the table structure and §5. Truncating öre in the result to whole kronor is an INFERENCE consistent with S01 §8 (AGI amounts are whole kronor).
- Brackets: 100 kr up to 20 000; 200 kr from 20 001 to 80 000. [S13 p.7]
- Income that is not main income: 30 % deduction. No deduction if total pay for the year is expected to be under 1 000 kr. [S14]
- **One-off amounts (engångsbelopp) 2026**, based on an average rate of 34. The percentage applies to the one-off amount and is chosen by the band of the annual salary ("Årslön"). [S13 §10 pp.26–28]

| Col | Annual salary band → % of one-off amount |
|---|---|
| 1 (under 66, work) | 0–25 041: 0 · 25 042–82 800: 10 · 82 801–192 000: 21 · 192 001–477 600: 26 · 477 601–660 000: 34 · 660 001+: 54 |
| 2 (66+, pension) | 0–65 800: 0 · 65 801–477 600: 26 · 477 601–660 000: 34 · 660 001+: 55 |
| 3 (66+, work) | 0–25 041: 0 · 25 042–331 200: 10 · 331 201–477 600: 26 · 477 601–660 000: 34 · 660 001+: 55 |
| 4 (sickness/activity comp.) | 0–25 041: 0 · 25 042–54 000: 3 · 54 001–192 000: 22 · 192 001–660 000: 26 · 660 001+: 46 |
| 5 (other pensionable) | 0–25 041: 0 · 25 042–32 400: 10 · 32 401–160 800: 29 · 160 801–184 800: 34 · 184 801–660 000: 38 · 660 001+: 54 |
| 6 (under 66, pension) | 0–25 041: 0 · 25 042–160 800: 29 · 160 801–184 800: 34 · 184 801–660 000: 38 · 660 001+: 54 |

  Whether "Årslön" includes the one-off amount itself was not verified in the text read. Treat it as open.
- **Machine-readable file** `skattetabeller/2026_allmanna-tabeller-manad.txt` [S10, S11]:
  - UTF-8 with BOM (strip `EF BB BF` from line 1). Fixed width, 49 characters per record. The last line is a 52-character trailer: ignore it.
  - Positions (1-based):

    | Pos | Len | Content |
    |---|---|---|
    | 1–2 | 2 | Period type: `30` = month (`14` = two-week, a different file) |
    | 3 | 1 | `B` = amount in kronor, `%` = percent |
    | 4–5 | 2 | Table number 29–42 |
    | 6–12 | 7 | Lowest income (right-aligned) |
    | 13–19 | 7 | Highest income (right-aligned; **blank on the last % record = open-ended**) |
    | 20–24 | 5 | Column 1 |
    | 25–29 | 5 | Column 2 |
    | 30–34 | 5 | Column 3 |
    | 35–39 | 5 | Column 4 |
    | 40–44 | 5 | Column 5 |
    | 45–49 | 5 | Column 6 |

  - Values can fill all 5 characters with no separating space (e.g. `30B33  79401  79600263832625523150232063067630676`). **Parse by position, never by splitting on whitespace.**
  - Record counts: about 480 B records and 81–92 % records per table; 7 965 data records in total.
  - Lookup: the record whose low ≤ monthly taxable pay ≤ high, for the table and column. A `B` value is the tax in kronor; a `%` value means tax = pay × value / 100.

## 3. Employer contributions (arbetsgivaravgifter) 2026
- Full rate **31.42 %** = socialavgiftslagen 2 kap. 26 § 18.80 % plus allmän löneavgift 12.62 %. [S18, S19, S17]
  - 2026 components: sjukförsäkring 3.55; föräldraförsäkring 2.00; ålderspension 10.21; efterlevandepension 0.30; arbetsmarknad 2.64; arbetsskada 0.10; allmän löneavgift 12.62.
  - 2025 for comparison: 3.55 / 2.60 / 10.21 / 0.60 / 2.64 / 0.20 / 11.62, also 31.42 in total.
- Born **1938–1958** (had turned 67 at 1 Jan 2026): only ålderspensionsavgift, **10.21 %**. Legal basis: SAL 2 kap. 27 § ("vid årets ingång har fyllt 67 år"). AGI categories: Alder_2 for 2026 = birth dates 19380101–19581231; Alder_1 = born 1959 or later. [S18, S07, S17, S25]
  - Note: the age limit for contributions in 2026 is 67 at the start of the year, while the tax-table age is 66 (§2).
- Born **1937 or earlier**: **0 %** (SAL transitional provisions 2000:980 point 5; P_004 = 0 from 201907). [S18, S07]
- **Youth reduction**: Lag (2026:100), in force 2026-04-01, covers pay given out from 1 Apr 2026 to 30 Sep 2027. [S20, S17, S07]
  - Who: people who at 1 Jan had turned 18 but not 23. For 2026 that is born **2003–2007** (Alder_5 = 20030101–20071231, periods 202604–202612).
  - What: full ålderspensionsavgift plus half of the other contributions and of allmän löneavgift. Each halved rate is taken to 2 decimals with further decimals dropped. That gives **20.81 %** on pay **up to 25 000 kr per calendar month**. Pay above 25 000 is charged 31.42 %.
  - Arithmetic check (INFERENCE, matches the published 20.81): 10.21 + 1.77 + 1.00 + 0.15 + 1.32 + 0.05 + 6.31 = 20.81.
  - Applies to period 202609.
  - In the AGI calculation the youth pay goes to IK7001 (capped at 25 000 per person summed over all of that person's IUs). The excess goes to IK420.
- Pay under 1 000 kr to a person in the year is contribution-free (SAL 2 kap. 14 §). [S18; S17]
- Växa-stöd no longer exists in AGI from 202601 (FK062/FK063 end 202512). [S01; S04]
- Employers without a permanent establishment in Sweden: 18.80 % from 202601 (P_005). Not expected to apply to One Identity Sweden AB (INFERENCE). [S07; S17]

## 4. Rounding and deadlines
- All AGI amounts are reported as **whole kronor**. Schema amount types are `xs:long` with a minimum of 0, so no decimals and no negatives. [S01 §8; S03]
- Employer contributions: öre are dropped on each rate separately. Fuel benefit öre are dropped when the per-IU sum is built. [S01 §12.6.1]
- Whether öre on individual pay amounts should be truncated or rounded before reporting: Skatteverket's position 131 238881-17/111 is **NOT LOCATED** (the site blocked the download). Truncation is an INFERENCE based on the "öretal bortfaller" wording. [NL01]
- Due dates [S23, S22]:
  - Turnover up to 40 MSEK: the 12th of the month after the payment month; the **17th** for the July period (due in August) and the December period (due in January). SFL 26 kap. 26 § / 32 §.
  - **Period 202609 is due 12 October 2026.**
  - Over 40 MSEK: the 26th (27 December for November). SFL 26 kap. 30 §. Period 202609 is then due **26 October 2026**, but payment is still due on the 12th (the 17th in January).
  - A deadline that falls on a weekend or public holiday moves to the next weekday (e.g. 13 Apr 2026, 18 Jan 2027). The general law behind this was not downloaded (INFERENCE from the S22 table).
  - Absence records (frånvarouppgifter) are filed with the first AGI for the period and cannot be corrected afterwards. [S01 §9.3]
  - Late-filing fee: 625 kr. [S22]
- Reporting period: pay is reported in the AGI for the month in which it is **paid out** (e.g. January pay for December work goes in the January AGI). [S22 FAQ]

## 5. Special payroll tax on pension costs (context)
- Särskild löneskatt on pension costs: **24.26 %**, Lag (1991:687) 1 §. It is declared annually, not in AGI. [S24]
- SLF on profit-sharing foundation contributions / sickness pension reported in AGI HU (FK481 → FK486): 24.26 % (P_034). [S07]

## 6. Benefit values (context only, not complete)
- Kostförmån 2026: breakfast 62 kr; lunch or dinner 124 kr; free meals for the whole day 310 kr. [S25]
- Fuel with car benefit: contribution basis = market value incl. VAT; AGI/tax value = × 1.2. [S25; S01 §5.3.1]
- Car benefit calculation: NOT LOCATED, skipped by scope. [NL02]
- Other 2026 values: PBB 59 200; IBB 83 400; state tax limit 643 000 (brytpunkt 660 400 under 66 / 760 500 for 66+). [S13; S25]
