# Norway 2026 – extracted facts (Henkel Norway AS, period September 2026)

Read 2026-10-14. [Sxx] refers to sources.md. Values computed or interpreted here are marked INFERENCE.

## 1. A-melding
- Schema in force: a-meldingen **v2.3**, namespace `urn:ske:fastsetting:innsamling:a-meldingen:v2_3`, root `melding`, file 20240827, labelled "Gjeldende dokumentasjon" [S01, S05].
- Feedback (A03) schema: namespace `urn:ske:fastsetting:innsamling:a-meldingen-tilbakemelding:v2_3` (file 20240827). It carries mottakstatus, avvik/alvorlighetsgrad, KID for AGA and forskuddstrekk, forfallsdato, sumForskuddstrekk, sumArbeidsgiveravgift and sumForskuddstrekkPerLoennsutbetalingsdato [S02, S03].
- Code list in force: **Kodeliste R1 2026**. It has 82 Loennsbeskrivelse codes and 3 Fordel codes. The income type is the XSD choice loennsinntekt / ytelseFraOffentlige / pensjonEllerTrygd / naeringsinntekt. The only new code is `AktivitetspengerForUnge`, valid from 2026-09 [S04, S01].
- Business rules: Forretningsregler R1 2026. Sheet F197 lists the valid AGA rate per beregningskode and zone. F529 (stillingsprosent 0 with fastlønn) applies from 2026-10, so not to September [S04].
- Submission: from 2026 the a-melding can be sent from a system only through Skatteetaten's API [S05].
- Guidance: web-only "Veiledning til a-meldingen". It has no single version number; each page is dated (Forskuddstrekk 18.03.2026, AGA 22.01.2025) [S06].
- Feriepenger must be reported gross as feriepenger, with "trekk i lønn for ferie" reported negative [S06].

## 2. Arbeidsgiveravgift 2026
- Rates (ordinary industries): I 14,1 %; Ia 14,1 % (10,6 % until the de minimis fribeløp is used); II 10,6 %; III 6,4 %; IV 5,1 %; IVa 7,9 %; V 0 % [S07 § 3, S08, S09 pt. 4.2].
- Fribeløp (de minimis) is 850 000 kr per foretak or group in 2026 [S07 § 4(4)-(5), S08].
- No change in zones or rates from 2025 to 2026 [S09].
- Employees aged over 62: **N/A**. The 2026 vedtak has no age-based AGA rule [S07]. INFERENCE from the absence of any such provision.
- Extra AGA on high salaries: **does not apply**. It was abolished from 1 Jan 2025 [S06 Ekstra AGA page], and the 2026 vedtak has no such provision [S07].
- Basis: salary and other remuneration [S09 pt. 1.1]. AGA is also payable on employer pension contributions/premiums (OTP included), in the calendar month of payment, allocated across zones pro rata [S09 pt. 10.1, S10 § 23-2].
- Payment: bi-monthly terms, due 15 Jan, 15 Mar, 15 May, 15 Jul, 15 Sep and 15 Nov [S13 § 10-10(2), S09 pt. 8].
  - Term 5 (Sep–Oct 2026) falls due on 15 Nov 2026, which is a Sunday, so the due date is **Monday 16 Nov 2026** [S13 § 10-2]. INFERENCE: the weekday was computed.

## 3. Forskuddstrekk 2026
- Main employer uses tabelltrekk [S14 § 5-10-1, S15].
- Secondary employer uses prosenttrekk [S14 § 5-10-3, S15]. So do payments that relate to a different period than the salary they are paid with [S15].
- Supplements (overtime and similar) paid with the salary for the same period go through the table [S14 § 5-10-1(2)].
- Base for prosenttrekk: rounded down to the whole krone [S14 § 5-10-4].
- No tax card: **50 %** on salary, 30 % on pensions [S13 § 5-5(1), S15]. With no tax card there is no summer or Christmas exemption [S15, S13 § 5-7(2)].
- Holiday pay:
  - No trekk on statutory feriepenger paid in the ferieår [S13 § 5-7(1)a, S14 § 5-7-1(1)a].
  - Tariff feriepenger are exempt unless they exceed the statutory amount by more than 21 % [S14 § 5-7-1(1)b].
  - Monthly-paid staff may take the exemption as one normal monthly salary, in practice June. Any additional supplement up to 12,3 % is not subject to trekk [S14 § 5-7-1(2)].
- Half tax: monthly-paid staff are exempt for the **second half of November or the first half of December** (employer's choice) [S14 § 5-7-2(1), S13 § 5-7(1)a].
  - September has **no** exemption; full tabelltrekk applies. INFERENCE from S13/S14.
- Tables 2026:
  - Format: table number with 4 digits. 8000–8400 = deduction steps of 10 000 kr; 9010–9400 = addition steps of 10 000 kr. Special tables: 6xxx, 7xxx, 0100, 0101.
  - Standard tables assume 10,5 months of trekk per year [S17].
  - Text file record: table (4) + period (1; 1 = month) + type (1; 0 = lønn) + trekkgrunnlag (6) + trekk (6) [S16].
- Minimum limits: no trekk if total trekk is ≤ 100 kr per month, or if trekkpliktige ytelser are ≤ 500 kr per month [S14 § 5-4-3].
- Payment of withheld tax from 2026: **first working day after the salary payment**. The skattetrekkskonto was abolished and the bi-monthly terms no longer apply to trekk [S13 § 10-10(1), in force 1 Jan 2026; S22; S15].
- Skattevedtak 2026, context for any tax recalculation [S12]:
  - Trinnskatt: 1,7 % above 226 100; 4,0 % above 318 300; 13,7 % above 725 050; 16,8 % above 980 100; 17,8 % above 1 467 200.
  - Fellesskatt 8,25 %. Personfradrag 114 540. Minstefradrag maximum 95 700.
- Wage tables after the June 2026 amendment: the skattevedtak was amended 19.06.2026 (nr. 1243). The amendment visible on 2026-10-14 is § 6-5, the pension tax credit, from 1 July 2026. No reissue of the wage trekktabeller was found; the 2026 file is dated 2025-12-07 [S16].
  - INFERENCE: the published 2026 wage tables (8xxx/9xxx) still apply to September 2026. Confirming this is NOT LOCATED.

## 4. Feriepenger (ferieloven)
- 10,2 % of the feriepengegrunnlag [S18 § 10(2)].
- **+2,3 pp** for workers over 60, but not on the part of the grunnlag above 6 G. The G used is the one at 31 December of the opptjeningsår [S18 § 10(3)].
  - Feriepenger paid in 2026 (earned 2025): G = 130 160, so 6 G = 780 960 kr [S20]. INFERENCE: computed.
- Grunnlag = arbeidsvederlag paid in the opptjeningsår [S18 § 10(1)]. Excluded:
  - feriepenger paid in that year;
  - share of net dividend;
  - fixed pay earned regardless of holiday absence;
  - benefits in kind (free board is included);
  - expense reimbursements.
- 12 % (5th week): **N/A in statute**. It comes from collective agreements. The trekk exemption on tariff feriepenger is limited to 21 % above the statutory amount [S14 § 5-7-1(1)b].
- Extra holiday: 25 virkedager, plus 6 virkedager from the ferieår in which the worker turns 60 [S18 § 5].

## 5. Trygdeavgift and G
- Wages (ages 17–69): **7,6 %** [S07 § 7, S11].
- Pension, and persons under 17 or over 69: 5,1 % [S07 § 6, S11].
- Business income: 10,8 % [S07 § 8].
- Lower limit **99 650 kr**. Trygdeavgift may not exceed 25 % of the income above 99 650 [S10 § 23-3, S11].
- Collected through forskuddstrekk; it is built into the tables. INFERENCE: S17 describes special tables as "Trygdeavgift mellomsats / lav sats / ikke trygdeavgift".
- G from 1 May 2026: **136 549 kr**. G from 1 May 2025: **130 160 kr** [S20].

## 6. OTP
- At least **2 % of salary up to 12 G**, from the first krone. The law in force has no 1 G floor [S19 § 4(1)-(2)].
- INFERENCE: 12 G = 1 638 588 kr with G 136 549, or 1 561 920 kr with G 130 160. Which G the scheme applies depends on its rules.
- Administration costs are paid by the employer on top of the contribution [S19 § 4(4)].
- AGA is payable on the contributions [S09 pt. 10.1].

## 7. Deadlines
- A-melding is due the **5th of the following month** [S21 forskrift § 2-1, S22]. A deadline on a weekend or public holiday moves to the next working day.
- A-melding for September 2026 is due **Monday 5 Oct 2026**. INFERENCE: the weekday was computed.
- Forskuddstrekk is due on the first working day after payday [S13 § 10-10(1)].
- AGA term 5 (Sep–Oct) is due 15 Nov, moved to 16 Nov 2026 [S13 §§ 10-10(2), 10-2].
