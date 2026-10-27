# Denmark 2026 – compact facts (period September 2026). Source IDs refer to sources.md.

## 1. eIndkomst (monthly reporting)
Version in force: Indberetningsvejledning v16.9 (01.07–31.08.26) and v17.0 (from 12.10.26). No version is listed for 01.09–11.10.26 (INFERENCE: v16.9 applied). The field tables are identical in both versions [S01]. Teknisk vejledning v11.6 from 10.08.26 [S03].

### Field numbers (feltnr – name – section) [S01, S02, S03 §4.15]
| Felt | Meaning | Notes |
|---|---|---|
| 0011 | Ej automatisk beregning af befordringsfradrag | Discontinued (udgået) |
| 0013 | A-indkomst subject to AM-bidrag (am-bidragspligtig A-indkomst) | Gross before A-skat/AM. The employee's own ATP and deductible employer-administered pension are deducted. Includes taxable feriepenge, A-taxable benefits (19/20/21/26) and the store-bededag supplement (INFERENCE for the last one) [S02 §8.2] |
| 0014 | A-indkomst not subject to AM-bidrag | e.g. dagpenge, pensions, one-off non-compete payment [S02 §8.2] |
| 0015 | Indeholdt A-skat | [S02 §8.2] |
| 0016 | Indeholdt AM-bidrag | Leave EMPTY (not 0) for youths who are exempt from 2026 [S02 §8.2, §0] |
| 0019 | Value of free car (fri bil) | AM- and A-taxable; the amount must also be in 0013 [S02 §8.4.1] |
| 0020 | Free telephone etc. | AM- and A-taxable, also in 0013. 2026: 3.500 kr./year = 291,67 kr./month [S02 §8.4.1] |
| 0021 | Fri kost og logi | Standard rates. A-taxable groups also in 0013 [S02 §8.4.1] |
| 0022–0025 | Foreign/Swedish pension items | [S01] |
| 0026 | Employer-paid health insurance/treatment (incl. dental) | AM- and A-taxable, also in 0013 [S02 §8.4.1] |
| 0036 | B-indkomst subject to AM | [S02 §8.6] |
| 0037 | Public grants to the business | [S01] |
| 0038 | B-indkomst not subject to AM | [S02 §8.6] |
| 0039 | Hædersgaver | [S01] |
| 0040 | Naturalieydelser (tick box + text) | [S01] |
| 0041–0043 | Medarbejderinvesteringsselskab | [S01] |
| 0045 | ATP sats type (A–F; A is standard) | [S02 §8.2] |
| 0046 | Total ATP contribution (employee + employer) | [S02 §8.2] |
| 0047 | OP-bidrag (public payers only) | [S02 §8.2] |
| 0048 | Tax-free travel/mileage allowance (+ tax-free education benefit with indtægtsart 49) | [S02 §8.6] |
| 0050–0056 | Other benefits (housing, boat, media, other benefits) | [S01] |
| 0057–0059 | Aldersopsparing | [S01] |
| 0063 | Fri befordring (tick box) | [S01] |
| 0068 | Additional text information (text field) | "Kode 68" is also the name of the indtægtsart value set (record 6000 field 10) [S02 §8.6, S03 §4.9.1] |
| 0069 | Jubilæumsgratiale / fratrædelsesgodtgørelse / pension buy-out (gross, before the 8.000 kr. and before AM) | NOT in 0013 [S02 §8.4.3] |
| 0070 | Part of 0069 paid into a pension scheme | [S02 §8.4.3] |
| 0071 | Part of 0069 given as a gift in kind | [S02 §8.4.3] |
| 0083 | Sea days (sødage) | [S01] |
| 0089 | Obligatory foreign social security contribution | [S02 §8.5] |
| 0091 / 0096 | Group life / health insurance inside a pension contribution | [S01] |
| 0113 | A-indkomst paid as feriepenge (specification of 0013; bagudløn only) | [S02 §8.2] |
| 0147 / 0148 | Employee / employer share of a deductible employer-administered pension (excluding ATP) | [S02 §8.2] |
| 0198 | Gross holiday pay – hourly paid | [S02 §8.3.0] |
| 0200 | Number of paid hours (løntimer); max 2.000 per report | [S02 §8.1] |
| 0201 | Gross holiday pay | Discontinued (udgået) [S01] |
| 0202 | Net holiday pay – hourly paid | [S02 §8.3.0] |
| 0203 | Holiday days earned – hourly paid (2 decimals) | [S02 §8.3.0] |
| 0209 | SE number of the holiday-pay payer (FerieKonto 33088566) | [S02 §8.3.0] |
| 0210 / 0211 | Gross holiday pay / holiday days – continuing salaried employee | [S01] |
| 0220 | Tick box "no relation between pay and hours" | [S02 §8.1] |
| 0248 | Saving for public-holiday pay (søgnehelligdag), taxed but not paid out | [S02 §8.6] |
| 0249 | Saving for feriefridage | [S02 §8.6] |
| 0400 | AM-bidrag on a pension promise (tilsagnsordning) | [S01] |
| 0049, 0072, 0073, 0074, 0100 | NOT field numbers. These are indtægtsart (kode 68) codes: 0049 tax-free education benefit (felt 48); 0072 SU corrections (felt 14); 0073 tax-free soldier grant (felt 39); 0074 other pension (felt 14); 0100 taxable foundation distributions (felt 38) | [S03 §4.9.1] |

### Other eIndkomst rules
- Indkomsttype codes: 00 wage income; 01 SU; 02 special taxation (arbejdsudleje); 03 Greenland; 04 other personal income without AM; 05 B-income; 06 kontanthjælp; 07 sickness/maternity benefit from the public sector; 08 researcher scheme (KSL § 48E–F); 09 AM- and A-tax-free A-indkomst; 10 LG; 11 estate; 20 AFU; 24; 26 aldersopsparing; 28 LFF; 29 feriegarantiordning; 30/31/32 Skattestyrelsen only [S02 §3].
- Løntimer: full-time salaried staff are reported as 160,33 h/month (37 h/week), even after store bededag was abolished. Report 0 hours when only feriegodtgørelse, bonus or similar is paid on its own [S02 §8.1].
- Dispositionsdato sets the settlement month and the tax year. Forudløn uses the period start date [S02 §6].
- Afstemning ("Afstemning af indberetninger", §9): reconciliation menu in eIndkomst. It gives on-screen views and CSV files: VIRSUM (totals for the company), PERSUM (totals per employee) and detail per employee, with columns Feltnr 0013, 0014, 0015, 0016, 0019, …, 0046, 0113, 0147, 0148, 0200, … An empty field means nothing was reported; 0,00 means a report was received with a total of 0. A payroll bureau only sees what it reported itself [S02 §9, §9.4.2, §9.4.3].
- Payment line: ATP is NOT included in the Skattestyrelsen payment total (A-skat + AM only) [S02 §10].
- Amounts in record 6001: 16 digits, the last 6 are decimals [S03 §4.10].

### Deadlines (September 2026 period) [S04, S05]
- Large employer ("fremrykket betaling – stor virksomhed"): reporting AND payment 30.09.2026, i.e. the last bank day of the month the income relates to (OPKL § 2(6)). Threshold: A-skat > 1 mio. kr. or AM > 250.000 kr. in Oct-2024 to Sep-2025 (for calendar year 2026) [S05].
- SMV: reporting and payment 12.10.2026 (the general rule is the 10th of the following month, moved to the next bank day; OPKL § 2(5)) [S04, S05].
- Payment may be made at most 5 weekdays before the deadline (5-day rule) [S02 §10].

## 2. AM-bidrag
- 8 % of the AM base (AMBL § 1) [S06, S07]. 0 % up to and including 31 Dec of the year the person turns 17 (from 01.01.2026; LOV 96/2025) [S06, S08].
- The base includes any pay in cash or kind for work, including severance and pay during sickness/maternity (AMBL § 2(1) nr 1). It excludes amounts outside taxable income (§ 3 nr 3) and the obligatory ATP-type pension (§ 3 nr 5) [S07]. A-taxable benefits fri bil, fri telefon, sundhedsforsikring and fri kost/logi (listed groups) are AM-liable (KSL § 49 A(2)) [S10, S02].
- The employee's ATP share and deductible employer-administered pension are deducted before felt 13 [S02 §8.2]. INFERENCE: so they are also outside the AM base for the payroll.

## 3. A-skat
- Hovedkort: monthly fradrag + trækprocent. Bikort: trækprocent only, no fradrag. Frikort: no tax up to the frikort balance. No card: 55 % with no fradrag. KSL § 48(3), (5), (7)/(8); DJV A.B.4.1.1.2.2–.4 [S09, S10, S13].
- Card choice: bagudløn uses the card valid on the disposition date; forudløn the card valid on the period start [S13].
- AM-bidrag is deducted in personal income (PSL § 3(2) nr 6) [S14].
- INFERENCE formula (assembled, not stated verbatim in one official text, see N05): A-skat = (A-indkomst after the employee's ATP/pension − AM-bidrag − monthly fradrag) × trækprocent, where AM-bidrag = 8 % × felt 13.
- Rounding: KSL § 48(6) lets the minister require the base to be rounded DOWN to the nearest amount divisible by 10 kr. [S10]. DJV A.B.4.1.1.2.6 describes one acceptable method ("kan eksempelvis benyttes"): AM base and A-indkomst are rounded down to the nearest 10 kr., then the computed AM-bidrag and A-skat are rounded UP to whole kroner. Under that method the payslip shows them without øre [S09]. This is an example method, not a mandatory rule.
- Voluntary higher trækprocent: whole numbers only, once per calendar year, in writing (KSLBek § 24) [S11, S13].
- 2026 trækprocent = kommune + kirke + bundskat + mellemskat/topskat/toptopskat components, computed with 2 decimals (BEK 1094/2025 § 6) [S12].

## 4. ATP 2026 (A-sats, monthly paid) [S15, S16, S17]
| Hours/month | Employee | Employer | Total |
|---|---|---|---|
| ≥ 117 | 99,00 | 198,00 | 297,00 |
| 78–116 | 66,00 | 132,00 | 198,00 |
| 39–77 | 33,00 | 66,00 | 99,00 |
| < 39 | 0 | 0 | 0 |
- The split is 1/3 employee and 2/3 employer, as the amounts show. Total 297,00 from 01.01.2024 with no end date [S17]. Felt 46 = the total [S02].
- Unknown working time: hours = gross monthly pay / hourly rate. 2026: men 258,69, women 233,62 [S15, S17].
- 14-day paid: ≥54 h 52,20/104,40/156,60. Weekly: ≥27 h 26,10/52,20/78,30 [S15].

## 5. Ferieloven (LBK 152/2024) [S19]
- Accrual: 2,08 days per month (§ 5). Feriegodtgørelse is 12,5 % (§ 16(2)). Salaried staff with full pay on public holidays and sick days get løn under ferie plus a statutory ferietillæg of 1 % (§ 16(1)). 1,5 % is NOT statutory; no 2024–2026 amending law was found (INFERENCE: higher rates come from collective agreements or contracts). Option: 12 % feriegodtgørelse instead of pay plus tillæg (§ 16(3)).
- Ferietillæg is calculated like feriegodtgørelse under § 19 (§ 18). It is paid with the May pay (Sep–May) and August pay (Jun–Aug), or when the holiday starts.
- § 19 base: every taxable wage amount, plus the value of personalegoder the employee does NOT have during the holiday, plus the employee's own pension contributions, AM-bidrag and MIS contributions (§ 19(2)). No holiday pay is calculated on holiday pay itself (§ 19(4)). INFERENCE: benefits kept during the holiday (fri bil, fri telefon, health insurance) are NOT in the ferietillæg/feriegodtgørelse base.
- Leaving employees: feriegodtgørelse at 12,5 % for untaken holiday (§ 16(4)), normally via FerieKonto. The employer may pay ≤ 2.500 kr. net directly (§ 26(2)).

## 6. Rates 2026 (context) [S21]
Bundskat 12,01 %. Mellemskat 7,5 % > 641.200 kr. Topskat 7,5 % > 777.900 kr. Toptopskat 5 % > 2.592.700 kr. (thresholds are after AM-bidrag). Personfradrag 2026: NOT LOCATED (N01).

## 7. Employer contributions 2026 (Samlet Betaling) [S22]
AUB 705,25 kr.; Barsel.dk 550 kr.; Finansieringsbidrag 82 kr.; LFF admin 5 kr.; AFU 0; FerieKonto admin 4 kr./month per employee; ATP 891 kr. per employee. INFERENCE: these are per full-time employee per quarter, like the 2025 table; the 2026 table has no unit header. AES: NOT LOCATED (N02).

## A. Additional items (coordinator request)
- A1 Health insurance 2026: TAXABLE as A-indkomst and AM-liable. Report in felt 0026 and include it in felt 0013. The insurance premium is taxed when cover starts, or periodically if cover is tied to employment [S02 §8.4.1]. LL § 16(3) in the current LBK 1500/2025 taxes employer-paid health treatment and insurance premiums without the bagatel threshold [S24]. DJV C.A.5.15.1: taxable by default, with six exceptions (work injury, medically justified addiction treatment, small benefits, personnel care, covid) [S23]. No 2025/2026 law re-introducing a tax exemption was found in Retsinformation searches (INFERENCE: no change). Exception: health cover that is an integral part of a life/pension scheme is reported by the insurer in felt 38 with indtægtsart 37 [S02].
- A2 Severance: LL § 7 U gives 8.000 kr. per income year tax-free (not indexed, shared with jubilæum gifts). Conditions: the employee leaves completely, payment is close in time to leaving, and the amount does not replace pay for the notice period [S24, S25]. Felt 0069 = gross before the 8.000 and before AM, and is NOT included in 0013. A-skat and AM-bidrag are withheld on the part above 8.000 [S02 §8.4.3]. The AM base includes severance (AMBL § 2(1) nr 1) but not the tax-free part (§ 3 nr 3) [S07]. Pension-paid part goes in 0070; gift-in-kind part in 0071 (the value above 8.000 is A-taxable, not AM) [S02].
- A3 Rounding: see §3 above (KSL § 48(6); DJV A.B.4.1.1.2.6). No separate rounding rule for AM-bidrag was found in AMBL or KSLBek. KSL § 49 B applies §§ 46/49 to AM correspondingly, and the DJV method covers both [S09, S10].
- A4 Fri telefon 2026: 3.500 kr./year, 291,67 kr./month. A-indkomst and AM-liable, also in 0013. At start or end of employment at least 1/12 [S02 §8.4.1]. Fri bil (0019): AM- and A-taxable, also in 0013 (KSL § 49 A(2) nr 1) [S02, S10].
- A5 Store bededag: 0,45 % of årsløn for fixed-salary employees (LOV 214/2023 § 3(1)). It accrues monthly and is paid either twice a year with the May and August pay or with each pay; pro rata on leaving [S27]. Base: "sædvanlige og fastpåregnelige løn" as in FL § 17(1). It includes the employer's pension contribution, fixed supplements and personalegoder NOT received during holiday (valued at Skatterådets rates). It excludes overtime unless that is regular [S28]. INFERENCE: fri bil, fri telefon and health insurance that the employee keeps during holiday are NOT in the base. The supplement is ordinary pay, so it goes in felt 13 (INFERENCE).
- A6 Ferietillæg 2026: 1 % statutory (FL § 16(1)); base per § 19 (see §5) [S19].
- A7 Large employer deadline for September 2026 pay: reporting and payment 30.09.2026 [S04].
