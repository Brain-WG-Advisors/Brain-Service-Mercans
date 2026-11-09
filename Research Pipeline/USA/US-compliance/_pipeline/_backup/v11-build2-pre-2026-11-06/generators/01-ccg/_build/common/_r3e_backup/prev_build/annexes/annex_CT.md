# Annex CT: Connecticut


This annex sets out the Connecticut payroll rules for the 2026 build year. Read with Annex FED (the federal layer every employee carries) and Annex MULTI (which routes an employee to this State by work location, residence or UI localization). Every value is shown with its effective dates and its source (list at the end of the annex). Federal values are not repeated here.

Classification: T3. Separate State withholding, UI and a separate Paid Leave contribution; no local wage tax.

## CT.1 Employment and labour code

State minimum wage USD [[FACT:ct.minwage.hourly=16.94]] for 2026 and USD [[FACT:ct.minwage.hourly=17.48]] for 2027, indexed [[FACT:ct.minwage.indexation=every 1 January by ECI (wages and salaries, all civilian workers) for 12 months to preceding 30 June, nearest cent; announced by 15 October; never below federal MW + 0.5%]].

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Minimum wage hourly | USD [[FACT:ct.minwage.hourly=16.94]] | 2026-01-01 to 2026-12-31 |  | S1 | Derivation: 16.35 x 1.036 (ECI) = 16.9386 -> [[FACT:ct.minwage.hourly=16.94]] (Decimal ROUND_HALF_UP). |
| Minimum wage hourly | USD [[FACT:ct.minwage.hourly=17.48]] | from 2027-01-01 |  | S2 | Announced; [[FACT:ct.minwage.hourly=16.94]] x 1.032 = 17.48208 -> [[FACT:ct.minwage.hourly=17.48]]. |
| Minimum wage indexation | [[FACT:ct.minwage.indexation=every 1 January by ECI (wages and salaries, all civilian workers) for 12 months to preceding 30 June, nearest cent; announced by 15 October; never below federal MW + 0.5%]] | from 2023-06-01 |  | S3 |  |
| Overtime weekly threshold hours | [[FACT:ct.overtime.weekly_threshold_hours=40]] hours | from 2026-01-01 |  | S4 | 1.5x; no daily OT; fluctuating workweek allowed except certain delivery drivers/sales merchandisers. |
| Pay frequency rule | [[FACT:ct.pay_frequency.rule=weekly or biweekly regular payday designated in advance; period ends no more than 8 days before payday; Commissioner waiver never less than monthly]] | from 2026-01-01 |  | S5 |  |
| Payment method | [[FACT:ct.payment.method=cash or check; direct deposit only at employee written/electronic request; payroll card only if DD and check also offered and employee authorises voluntarily (31-71k)]] | from 2026-01-01 |  | S5 |  |
| Tipped employer share hotel restaurant | USD [[FACT:ct.tipped.employer_share.hotel_restaurant=6.38]] | from 2026-01-01 |  | S6 | Fixed employer cash wage; maximum tip credit 2026 [[FACT:ct.tipped.max_tip_credit.hotel_restaurant=10.56]] (minimum wage [[FACT:ct.minwage.hourly=16.94]] less the employer share). Bartenders: employer share [[FACT:ct.tipped.employer_share.bartender=8.23]]. Other industries and meal credits: in the source. No cannabis tip credit from 2026-10-01 (PA 26-12 s.6). |
| Tipped employer share bartender | USD [[FACT:ct.tipped.employer_share.bartender=8.23]] | from 2026-01-01 |  | S6 |  |
| Tipped max tip credit hotel restaurant | USD [[FACT:ct.tipped.max_tip_credit.hotel_restaurant=10.56]] | 2026-01-01 to 2026-12-31 |  | S6 | [[FACT:ct.minwage.hourly=16.94]] - [[FACT:ct.tipped.employer_share.hotel_restaurant=6.38]]. |
| Minimum wage minor hourly | USD [[FACT:ct.minwage.minor.hourly=14.40]] | 2026-01-01 to 2026-12-31 |  | S3 | Under 18 not emancipated: greater of 85% of MW (first 90 days) or 10.10: 0.85 x [[FACT:ct.minwage.hourly=16.94]] = [[FACT:ct.minwage.minor.hourly=14.40]] (2027: 14.86). |

Not configured in this release [[GAP:RQ-504]]: Payslip consolidated text lag: not established from an official source.

## CT.2 Income tax withholding

**Method.** [[FACT:ct.wh.method=TPG-211 2026 Withholding Calculation Rules (Rev. 12/25) or DRS tables (IP 2026(1)); no percentage method; 2026 rules/tables unchanged from 2025]]. Certificate: [[FACT:ct.wh.certificate.form=CT-W4 (Rev. 12/25), codes A/B/C/D/E/F; exempt certificates to DRS above 36,000 MFS / 45,000 S / 57,000 HoH / 72,000 MFJ; MSRRA with LES]]. Without a certificate: [[FACT:ct.wh.no_certificate.rate=6.99]] %. Supplemental pay: [[FACT:ct.wh.supplemental.method=aggregate only (no flat supplemental rate)]].

```
annual_wages = period_wages x pay_periods
taxable      = annual_wages - TableA_exemption(code)
annual_tax   = TableB(code)(taxable) + TableC_phaseout_addback + TableD_recapture
annual_tax   = annual_tax x (1 - TableE_credit)
period_tax   = annual_tax / pay_periods + CTW4_line2 - CTW4_line3
```

Table A exemption (maximum) by code: A USD [[FACT:ct.wh.table_a.exemption.a=12,000]], B USD [[FACT:ct.wh.table_a.exemption.b=19,000]], C USD [[FACT:ct.wh.table_a.exemption.c=24,000]], F USD [[FACT:ct.wh.table_a.exemption.f=15,000]]. Table B rates [[FACT:ct.pit.rates=2.0 / 4.5 / 5.5 / 6.0 / 6.5 / 6.9 / 6.99 percent]]; band breaks: codes A, D, F [[FACT:ct.pit.bracket_breaks.a_d_f=10,000 / 50,000 / 100,000 / 200,000 / 250,000 / 500,000]]; code B [[FACT:ct.pit.bracket_breaks.b=16,000 / 80,000 / 160,000 / 320,000 / 400,000 / 800,000]]; code C [[FACT:ct.pit.bracket_breaks.c=20,000 / 100,000 / 200,000 / 400,000 / 500,000 / 1,000,000]]. **Tables C, D and E of TPG-211** (2026 Withholding Calculation Rules, printed in IP 2026(1)). Each band reads 'annualized salary more than the lower bound and less than or equal to the upper bound: amount'. Table C is the phase-out add-back of the lowest tax rate (USD), Table D the tax recapture amount (USD) and Table E the personal tax credit (a decimal applied as annual_tax x (1 - credit)).

| TPG-211 table | CT-W4 code | Bands (annualized salary: amount) |
|---|---|---|
| C, phase-out add-back | A, D | [[FACT:ct.wh.table_c.code_a_d=0-50,250: 0; 50,250-52,750: 25; 52,750-55,250: 50; 55,250-57,750: 75; 57,750-60,250: 100; 60,250-62,750: 125; 62,750-65,250: 150; 65,250-67,750: 175; 67,750-70,250: 200; 70,250-72,750: 225; over 72,750: 250]] |
| C, phase-out add-back | B | [[FACT:ct.wh.table_c.code_b=0-78,500: 0; 78,500-82,500: 40; 82,500-86,500: 80; 86,500-90,500: 120; 90,500-94,500: 160; 94,500-98,500: 200; 98,500-102,500: 240; 102,500-106,500: 280; 106,500-110,500: 320; 110,500-114,500: 360; over 114,500: 400]] |
| C, phase-out add-back | C | [[FACT:ct.wh.table_c.code_c=0-100,500: 0; 100,500-105,500: 50; 105,500-110,500: 100; 110,500-115,500: 150; 115,500-120,500: 200; 120,500-125,500: 250; 125,500-130,500: 300; 130,500-135,500: 350; 135,500-140,500: 400; 140,500-145,500: 450; over 145,500: 500]] |
| C, phase-out add-back | F | [[FACT:ct.wh.table_c.code_f=0-56,500: 0; 56,500-61,500: 25; 61,500-66,500: 50; 66,500-71,500: 75; 71,500-76,500: 100; 76,500-81,500: 125; 81,500-86,500: 150; 86,500-91,500: 175; 91,500-96,500: 200; 96,500-101,500: 225; over 101,500: 250]] |
| D, recapture | A, D, F | [[FACT:ct.wh.table_d.code_a_d_f=0-105,000: 0; 105,000-110,000: 25; 110,000-115,000: 50; 115,000-120,000: 75; 120,000-125,000: 100; 125,000-130,000: 125; 130,000-135,000: 150; 135,000-140,000: 175; 140,000-145,000: 200; 145,000-150,000: 225; 150,000-200,000: 250; 200,000-205,000: 340; 205,000-210,000: 430; 210,000-215,000: 520; 215,000-220,000: 610; 220,000-225,000: 700; 225,000-230,000: 790; 230,000-235,000: 880; 235,000-240,000: 970; 240,000-245,000: 1,060; 245,000-250,000: 1,150; 250,000-255,000: 1,240; 255,000-260,000: 1,330; 260,000-265,000: 1,420; 265,000-270,000: 1,510; 270,000-275,000: 1,600; 275,000-280,000: 1,690; 280,000-285,000: 1,780; 285,000-290,000: 1,870; 290,000-295,000: 1,960; 295,000-300,000: 2,050; 300,000-305,000: 2,140; 305,000-310,000: 2,230; 310,000-315,000: 2,320; 315,000-320,000: 2,410; 320,000-325,000: 2,500; 325,000-330,000: 2,590; 330,000-335,000: 2,680; 335,000-340,000: 2,770; 340,000-345,000: 2,860; 345,000-500,000: 2,950; 500,000-505,000: 3,000; 505,000-510,000: 3,050; 510,000-515,000: 3,100; 515,000-520,000: 3,150; 520,000-525,000: 3,200; 525,000-530,000: 3,250; 530,000-535,000: 3,300; 535,000-540,000: 3,350; over 540,000: 3,400]] |
| D, recapture | B | [[FACT:ct.wh.table_d.code_b=0-168,000: 0; 168,000-176,000: 40; 176,000-184,000: 80; 184,000-192,000: 120; 192,000-200,000: 160; 200,000-208,000: 200; 208,000-216,000: 240; 216,000-224,000: 280; 224,000-232,000: 320; 232,000-240,000: 360; 240,000-320,000: 400; 320,000-328,000: 540; 328,000-336,000: 680; 336,000-344,000: 820; 344,000-352,000: 960; 352,000-360,000: 1,100; 360,000-368,000: 1,240; 368,000-376,000: 1,380; 376,000-384,000: 1,520; 384,000-392,000: 1,660; 392,000-400,000: 1,800; 400,000-408,000: 1,940; 408,000-416,000: 2,080; 416,000-424,000: 2,220; 424,000-432,000: 2,360; 432,000-440,000: 2,500; 440,000-448,000: 2,640; 448,000-456,000: 2,780; 456,000-464,000: 2,920; 464,000-472,000: 3,060; 472,000-480,000: 3,200; 480,000-488,000: 3,340; 488,000-496,000: 3,480; 496,000-504,000: 3,620; 504,000-512,000: 3,760; 512,000-520,000: 3,900; 520,000-528,000: 4,040; 528,000-536,000: 4,180; 536,000-544,000: 4,320; 544,000-552,000: 4,460; 552,000-800,000: 4,600; 800,000-808,000: 4,680; 808,000-816,000: 4,760; 816,000-824,000: 4,840; 824,000-832,000: 4,920; 832,000-840,000: 5,000; 840,000-848,000: 5,080; 848,000-856,000: 5,160; 856,000-864,000: 5,240; over 864,000: 5,320]] |
| D, recapture | C | [[FACT:ct.wh.table_d.code_c=0-210,000: 0; 210,000-220,000: 50; 220,000-230,000: 100; 230,000-240,000: 150; 240,000-250,000: 200; 250,000-260,000: 250; 260,000-270,000: 300; 270,000-280,000: 350; 280,000-290,000: 400; 290,000-300,000: 450; 300,000-400,000: 500; 400,000-410,000: 680; 410,000-420,000: 860; 420,000-430,000: 1,040; 430,000-440,000: 1,220; 440,000-450,000: 1,400; 450,000-460,000: 1,580; 460,000-470,000: 1,760; 470,000-480,000: 1,940; 480,000-490,000: 2,120; 490,000-500,000: 2,300; 500,000-510,000: 2,480; 510,000-520,000: 2,660; 520,000-530,000: 2,840; 530,000-540,000: 3,020; 540,000-550,000: 3,200; 550,000-560,000: 3,380; 560,000-570,000: 3,560; 570,000-580,000: 3,740; 580,000-590,000: 3,920; 590,000-600,000: 4,100; 600,000-610,000: 4,280; 610,000-620,000: 4,460; 620,000-630,000: 4,640; 630,000-640,000: 4,820; 640,000-650,000: 5,000; 650,000-660,000: 5,180; 660,000-670,000: 5,360; 670,000-680,000: 5,540; 680,000-690,000: 5,720; 690,000-1,000,000: 5,900; 1,000,000-1,010,000: 6,000; 1,010,000-1,020,000: 6,100; 1,020,000-1,030,000: 6,200; 1,030,000-1,040,000: 6,300; 1,040,000-1,050,000: 6,400; 1,050,000-1,060,000: 6,500; 1,060,000-1,070,000: 6,600; 1,070,000-1,080,000: 6,700; over 1,080,000: 6,800]] |
| E, personal tax credit | A | [[FACT:ct.wh.table_e.code_a=12,000-15,000: 0.75; 15,000-15,500: 0.70; 15,500-16,000: 0.65; 16,000-16,500: 0.60; 16,500-17,000: 0.55; 17,000-17,500: 0.50; 17,500-18,000: 0.45; 18,000-18,500: 0.40; 18,500-20,000: 0.35; 20,000-20,500: 0.30; 20,500-21,000: 0.25; 21,000-21,500: 0.20; 21,500-25,000: 0.15; 25,000-25,500: 0.14; 25,500-26,000: 0.13; 26,000-26,500: 0.12; 26,500-27,000: 0.11; 27,000-48,000: 0.10; 48,000-48,500: 0.09; 48,500-49,000: 0.08; 49,000-49,500: 0.07; 49,500-50,000: 0.06; 50,000-50,500: 0.05; 50,500-51,000: 0.04; 51,000-51,500: 0.03; 51,500-52,000: 0.02; 52,000-52,500: 0.01; over 52,500: 0.00]] |
| E, personal tax credit | B | [[FACT:ct.wh.table_e.code_b=19,000-24,000: 0.75; 24,000-24,500: 0.70; 24,500-25,000: 0.65; 25,000-25,500: 0.60; 25,500-26,000: 0.55; 26,000-26,500: 0.50; 26,500-27,000: 0.45; 27,000-27,500: 0.40; 27,500-34,000: 0.35; 34,000-34,500: 0.30; 34,500-35,000: 0.25; 35,000-35,500: 0.20; 35,500-44,000: 0.15; 44,000-44,500: 0.14; 44,500-45,000: 0.13; 45,000-45,500: 0.12; 45,500-46,000: 0.11; 46,000-74,000: 0.10; 74,000-74,500: 0.09; 74,500-75,000: 0.08; 75,000-75,500: 0.07; 75,500-76,000: 0.06; 76,000-76,500: 0.05; 76,500-77,000: 0.04; 77,000-77,500: 0.03; 77,500-78,000: 0.02; 78,000-78,500: 0.01; over 78,500: 0.00]] |
| E, personal tax credit | C | [[FACT:ct.wh.table_e.code_c=24,000-30,000: 0.75; 30,000-30,500: 0.70; 30,500-31,000: 0.65; 31,000-31,500: 0.60; 31,500-32,000: 0.55; 32,000-32,500: 0.50; 32,500-33,000: 0.45; 33,000-33,500: 0.40; 33,500-40,000: 0.35; 40,000-40,500: 0.30; 40,500-41,000: 0.25; 41,000-41,500: 0.20; 41,500-50,000: 0.15; 50,000-50,500: 0.14; 50,500-51,000: 0.13; 51,000-51,500: 0.12; 51,500-52,000: 0.11; 52,000-96,000: 0.10; 96,000-96,500: 0.09; 96,500-97,000: 0.08; 97,000-97,500: 0.07; 97,500-98,000: 0.06; 98,000-98,500: 0.05; 98,500-99,000: 0.04; 99,000-99,500: 0.03; 99,500-100,000: 0.02; 100,000-100,500: 0.01; over 100,500: 0.00]] |
| E, personal tax credit | F | [[FACT:ct.wh.table_e.code_f=15,000-18,800: 0.75; 18,800-19,300: 0.70; 19,300-19,800: 0.65; 19,800-20,300: 0.60; 20,300-20,800: 0.55; 20,800-21,300: 0.50; 21,300-21,800: 0.45; 21,800-22,300: 0.40; 22,300-25,000: 0.35; 25,000-25,500: 0.30; 25,500-26,000: 0.25; 26,000-26,500: 0.20; 26,500-31,300: 0.15; 31,300-31,800: 0.14; 31,800-32,300: 0.13; 32,300-32,800: 0.12; 32,800-33,300: 0.11; 33,300-60,000: 0.10; 60,000-60,500: 0.09; 60,500-61,000: 0.08; 61,000-61,500: 0.07; 61,500-62,000: 0.06; 62,000-62,500: 0.05; 62,500-63,000: 0.04; 63,000-63,500: 0.03; 63,500-64,000: 0.02; 64,000-64,500: 0.01; over 64,500: 0.00]] |

**Method choice (configuration decision, 2026-11-02).** The Department of Revenue Services permits either the TPG-211 rules or its tables. The engine uses the DRS per-period withholding tables of IP 2026(1) (weekly, biweekly, semimonthly and monthly bands, one row per wage band and CT-W4 code, listed in CT.2 with their source), because the Department's worked examples are table-based and the tables reproduce them (CT.14). Wages above the table maximum of each period are computed with the TPG-211 rules, as the tables instruct. The TPG-211 rules above are shown as the reference method.

Lump-sum pension withholding: [[FACT:ct.wh.pension_lump_sum.suspension=withholding on lump-sum retirement distributions suspended 2025-07-01 to 2026-12-31 (CT-W4P on request)]].

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Withholding method | [[FACT:ct.wh.method=TPG-211 2026 Withholding Calculation Rules (Rev. 12/25) or DRS tables (IP 2026(1)); no percentage method; 2026 rules/tables unchanged from 2025]] | 2026-01-01 to 2026-12-31 |  | S7 | Steps: annualise; less Table A exemption; Table B rates; + Table C phase-out add-back + Table D recapture; x (1 - Table E credit); / periods; + CT-W4 line 2 - line 3. |
| Withholding table a exemption a | USD [[FACT:ct.wh.table_a.exemption.a=12,000]] | 2026-01-01 to 2026-12-31 |  | S7 | A [[FACT:ct.wh.table_a.exemption.a=12,000]]; B 19,000; C 24,000; F 15,000; D 0; phases out 1,000 per 1,000 of income. |
| Withholding table a exemption b | USD [[FACT:ct.wh.table_a.exemption.b=19,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| Withholding table a exemption c | USD [[FACT:ct.wh.table_a.exemption.c=24,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| Withholding table a exemption f | USD [[FACT:ct.wh.table_a.exemption.f=15,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| PIT rates | [[FACT:ct.pit.rates=2.0 / 4.5 / 5.5 / 6.0 / 6.5 / 6.9 / 6.99 percent]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| PIT bracket breaks a d f | [[FACT:ct.pit.bracket_breaks.a_d_f=10,000 / 50,000 / 100,000 / 200,000 / 250,000 / 500,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| PIT bracket breaks b | [[FACT:ct.pit.bracket_breaks.b=16,000 / 80,000 / 160,000 / 320,000 / 400,000 / 800,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| PIT bracket breaks c | [[FACT:ct.pit.bracket_breaks.c=20,000 / 100,000 / 200,000 / 400,000 / 500,000 / 1,000,000]] | 2026-01-01 to 2026-12-31 |  | S7 |  |
| Withholding no certificate rate | [[FACT:ct.wh.no_certificate.rate=6.99]] % | from 2026-01-01 |  | S8 | No CT-W4: flat [[FACT:ct.wh.no_certificate.rate=6.99]] % without exemption; code E expires 15 Feb, then [[FACT:ct.wh.no_certificate.rate=6.99]] % from 16 Feb. |
| Withholding certificate form | [[FACT:ct.wh.certificate.form=CT-W4 (Rev. 12/25), codes A/B/C/D/E/F; exempt certificates to DRS above 36,000 MFS / 45,000 S / 57,000 HoH / 72,000 MFJ; MSRRA with LES]] | from 2025-12-01 |  | S8 |  |
| Withholding supplemental method | [[FACT:ct.wh.supplemental.method=aggregate only (no flat supplemental rate)]] | from 2026-01-01 |  | S9 |  |
| Withholding pension lump sum suspension | [[FACT:ct.wh.pension_lump_sum.suspension=withholding on lump-sum retirement distributions suspended 2025-07-01 to 2026-12-31 (CT-W4P on request)]] | 2025-07-01 to 2026-12-31 |  | S7 |  |
| Withholding tables columns | [[FACT:ct.wh.tables.columns=wages_greater_than|wages_less_than_or_equal_to|A|B|C|D|F (USD; withholding code from Form CT-W4; amounts per pay period)]] | 2026-01-01 to 2026-12-31 |  | S10 | Layout of every ct.wh.table.<period>.row.<nnn> value. Lookup: the band with greater_than < taxable wages <= less_than_or_equal_to; take the code column. |
| Withholding table weekly max wages | USD [[FACT:ct.wh.table.weekly.max_wages=1,932]] | 2026-01-01 to 2026-12-31 |  | S10 | Wages over this amount: "Refer to TPG-211, Withholding Calculation Rules" (no table row). |
| Withholding table biweekly max wages | USD [[FACT:ct.wh.table.biweekly.max_wages=3,865]] | 2026-01-01 to 2026-12-31 |  | S10 | Wages over this amount: "Refer to TPG-211, Withholding Calculation Rules" (no table row). |
| Withholding table semimonthly max wages | USD [[FACT:ct.wh.table.semimonthly.max_wages=4,187]] | 2026-01-01 to 2026-12-31 |  | S10 | Wages over this amount: "Refer to TPG-211, Withholding Calculation Rules" (no table row). |
| Withholding table monthly max wages | USD [[FACT:ct.wh.table.monthly.max_wages=8,375]] | 2026-01-01 to 2026-12-31 |  | S10 | Wages over this amount: "Refer to TPG-211, Withholding Calculation Rules" (no table row). |
| Withholding table weekly row 001 | [[FACT:ct.wh.table.weekly.row.001=0|19|0.00|0.00|0.00|0.19|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 002 | [[FACT:ct.wh.table.weekly.row.002=19|38|0.00|0.00|0.00|0.57|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 003 | [[FACT:ct.wh.table.weekly.row.003=38|57|0.00|0.00|0.00|0.95|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 004 | [[FACT:ct.wh.table.weekly.row.004=57|76|0.00|0.00|0.00|1.33|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 005 | [[FACT:ct.wh.table.weekly.row.005=76|96|0.00|0.00|0.00|1.72|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 006 | [[FACT:ct.wh.table.weekly.row.006=96|115|0.00|0.00|0.00|2.11|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 007 | [[FACT:ct.wh.table.weekly.row.007=115|134|0.00|0.00|0.00|2.49|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 008 | [[FACT:ct.wh.table.weekly.row.008=134|153|0.00|0.00|0.00|2.87|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 009 | [[FACT:ct.wh.table.weekly.row.009=153|173|0.00|0.00|0.00|3.26|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 010 | [[FACT:ct.wh.table.weekly.row.010=173|192|0.00|0.00|0.00|3.65|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 011 | [[FACT:ct.wh.table.weekly.row.011=192|211|0.00|0.00|0.00|4.26|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 012 | [[FACT:ct.wh.table.weekly.row.012=211|230|0.00|0.00|0.00|5.11|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 013 | [[FACT:ct.wh.table.weekly.row.013=230|250|0.05|0.00|0.00|5.99|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 014 | [[FACT:ct.wh.table.weekly.row.014=250|269|0.14|0.00|0.00|6.87|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 015 | [[FACT:ct.wh.table.weekly.row.015=269|288|0.24|0.00|0.00|7.72|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 016 | [[FACT:ct.wh.table.weekly.row.016=288|298|0.37|0.00|0.00|8.38|0.02]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 017 | [[FACT:ct.wh.table.weekly.row.017=298|307|0.50|0.00|0.00|8.80|0.07]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 018 | [[FACT:ct.wh.table.weekly.row.018=307|317|0.65|0.00|0.00|9.23|0.12]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 019 | [[FACT:ct.wh.table.weekly.row.019=317|326|0.82|0.00|0.00|9.66|0.17]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 020 | [[FACT:ct.wh.table.weekly.row.020=326|336|1.00|0.00|0.00|10.09|0.21]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 021 | [[FACT:ct.wh.table.weekly.row.021=336|346|1.21|0.00|0.00|10.54|0.26]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 022 | [[FACT:ct.wh.table.weekly.row.022=346|355|1.44|0.00|0.00|10.96|0.31]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 023 | [[FACT:ct.wh.table.weekly.row.023=355|365|1.68|0.00|0.00|11.39|0.36]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 024 | [[FACT:ct.wh.table.weekly.row.024=365|375|1.81|0.02|0.00|11.84|0.49]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 025 | [[FACT:ct.wh.table.weekly.row.025=375|384|1.93|0.07|0.00|12.27|0.64]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 026 | [[FACT:ct.wh.table.weekly.row.026=384|394|2.22|0.12|0.00|12.70|0.80]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 027 | [[FACT:ct.wh.table.weekly.row.027=394|403|2.52|0.17|0.00|13.12|0.99]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 028 | [[FACT:ct.wh.table.weekly.row.028=403|413|2.84|0.21|0.00|13.55|1.20]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 029 | [[FACT:ct.wh.table.weekly.row.029=413|423|3.18|0.26|0.00|14.00|1.42]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 030 | [[FACT:ct.wh.table.weekly.row.030=423|432|3.44|0.31|0.00|14.43|1.67]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 031 | [[FACT:ct.wh.table.weekly.row.031=432|442|3.80|0.36|0.00|14.86|1.93]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 032 | [[FACT:ct.wh.table.weekly.row.032=442|451|4.17|0.41|0.00|15.28|2.05]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 033 | [[FACT:ct.wh.table.weekly.row.033=451|461|4.53|0.45|0.00|15.71|2.18]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 034 | [[FACT:ct.wh.table.weekly.row.034=461|471|5.65|0.60|0.02|16.16|2.31]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 035 | [[FACT:ct.wh.table.weekly.row.035=471|480|6.01|0.77|0.07|16.59|2.43]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 036 | [[FACT:ct.wh.table.weekly.row.036=480|490|7.19|0.96|0.12|17.02|2.83]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 037 | [[FACT:ct.wh.table.weekly.row.037=490|500|7.67|1.17|0.17|17.47|3.36]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 038 | [[FACT:ct.wh.table.weekly.row.038=500|509|8.89|1.39|0.21|17.89|3.93]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 039 | [[FACT:ct.wh.table.weekly.row.039=509|519|9.38|1.63|0.26|18.32|4.54]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 040 | [[FACT:ct.wh.table.weekly.row.040=519|528|10.64|1.90|0.31|18.75|4.90]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 041 | [[FACT:ct.wh.table.weekly.row.041=528|538|11.03|2.18|0.36|19.18|5.27]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 042 | [[FACT:ct.wh.table.weekly.row.042=538|548|12.21|2.31|0.41|19.63|5.65]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 043 | [[FACT:ct.wh.table.weekly.row.043=548|557|12.60|2.43|0.45|20.05|6.01]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 044 | [[FACT:ct.wh.table.weekly.row.044=557|567|13.76|2.56|0.50|20.48|6.38]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 045 | [[FACT:ct.wh.table.weekly.row.045=567|576|14.15|2.68|0.55|20.91|6.74]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 046 | [[FACT:ct.wh.table.weekly.row.046=576|586|15.31|2.80|0.72|21.34|7.84]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 047 | [[FACT:ct.wh.table.weekly.row.047=586|596|15.71|2.93|0.91|21.79|8.22]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 048 | [[FACT:ct.wh.table.weekly.row.048=596|605|16.88|3.06|1.11|22.21|9.32]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 049 | [[FACT:ct.wh.table.weekly.row.049=605|615|17.26|3.18|1.34|22.64|9.80]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 050 | [[FACT:ct.wh.table.weekly.row.050=615|625|18.45|3.31|1.58|23.09|11.06]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 051 | [[FACT:ct.wh.table.weekly.row.051=625|634|18.83|3.43|1.85|23.52|11.56]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 052 | [[FACT:ct.wh.table.weekly.row.052=634|644|19.99|3.56|2.13|23.95|12.84]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 053 | [[FACT:ct.wh.table.weekly.row.053=644|653|20.38|3.68|2.43|24.37|13.37]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 054 | [[FACT:ct.wh.table.weekly.row.054=653|663|21.54|4.10|2.55|24.80|14.53]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 055 | [[FACT:ct.wh.table.weekly.row.055=663|673|21.95|4.54|2.68|25.25|14.94]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 056 | [[FACT:ct.wh.table.weekly.row.056=673|682|23.11|5.08|2.81|25.68|16.10]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 057 | [[FACT:ct.wh.table.weekly.row.057=682|692|23.50|5.76|2.93|26.11|16.49]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 058 | [[FACT:ct.wh.table.weekly.row.058=692|701|23.88|6.13|3.05|26.53|17.65]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 059 | [[FACT:ct.wh.table.weekly.row.059=701|711|24.27|6.49|3.18|26.96|18.04]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 060 | [[FACT:ct.wh.table.weekly.row.060=711|721|24.67|6.87|3.31|27.41|19.22]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 061 | [[FACT:ct.wh.table.weekly.row.061=721|730|25.06|7.24|3.43|27.84|19.60]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 062 | [[FACT:ct.wh.table.weekly.row.062=730|740|25.44|8.33|3.56|28.27|20.77]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 063 | [[FACT:ct.wh.table.weekly.row.063=740|750|25.85|8.72|3.69|28.72|21.17]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 064 | [[FACT:ct.wh.table.weekly.row.064=750|759|26.23|9.82|3.81|29.14|22.34]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 065 | [[FACT:ct.wh.table.weekly.row.065=759|769|26.62|10.18|3.93|29.57|22.72]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 066 | [[FACT:ct.wh.table.weekly.row.066=769|778|27.00|11.28|4.37|30.00|23.88]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 067 | [[FACT:ct.wh.table.weekly.row.067=778|788|27.38|11.64|4.82|30.43|24.27]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 068 | [[FACT:ct.wh.table.weekly.row.068=788|798|27.79|12.76|5.30|30.88|25.45]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 069 | [[FACT:ct.wh.table.weekly.row.069=798|807|28.17|13.12|5.80|31.30|25.84]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 070 | [[FACT:ct.wh.table.weekly.row.070=807|817|28.56|14.22|5.96|31.73|27.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 071 | [[FACT:ct.wh.table.weekly.row.071=817|826|28.94|14.59|6.12|32.16|27.39]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 072 | [[FACT:ct.wh.table.weekly.row.072=826|836|29.33|15.68|6.28|32.59|28.55]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 073 | [[FACT:ct.wh.table.weekly.row.073=836|846|29.73|16.07|6.45|33.04|28.95]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 074 | [[FACT:ct.wh.table.weekly.row.074=846|855|30.12|17.37|6.70|33.46|30.12]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 075 | [[FACT:ct.wh.table.weekly.row.075=855|865|30.50|17.94|7.07|33.89|30.50]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 076 | [[FACT:ct.wh.table.weekly.row.076=865|875|30.91|19.31|7.45|34.34|30.91]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 077 | [[FACT:ct.wh.table.weekly.row.077=875|884|31.29|19.91|7.81|34.77|31.29]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 078 | [[FACT:ct.wh.table.weekly.row.078=884|894|31.68|21.29|8.18|35.20|31.68]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 079 | [[FACT:ct.wh.table.weekly.row.079=894|903|32.06|21.68|8.54|35.62|32.06]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 080 | [[FACT:ct.wh.table.weekly.row.080=903|913|32.45|22.84|8.90|36.05|32.45]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 081 | [[FACT:ct.wh.table.weekly.row.081=913|923|32.85|23.25|9.29|36.50|32.85]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 082 | [[FACT:ct.wh.table.weekly.row.082=923|932|33.61|24.41|10.39|36.93|33.24]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 083 | [[FACT:ct.wh.table.weekly.row.083=932|942|34.37|24.79|10.75|37.36|33.62]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 084 | [[FACT:ct.wh.table.weekly.row.084=942|951|35.14|25.96|11.85|37.78|34.01]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 085 | [[FACT:ct.wh.table.weekly.row.085=951|961|35.92|26.34|12.21|38.21|34.39]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 086 | [[FACT:ct.wh.table.weekly.row.086=961|971|36.77|27.53|13.49|38.71|34.84]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 087 | [[FACT:ct.wh.table.weekly.row.087=971|980|38.12|27.91|14.01|39.71|35.31]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 088 | [[FACT:ct.wh.table.weekly.row.088=980|990|39.03|29.08|15.31|40.23|35.78]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 089 | [[FACT:ct.wh.table.weekly.row.089=990|1000|39.97|29.48|15.89|40.78|36.27]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 090 | [[FACT:ct.wh.table.weekly.row.090=1000|1009|40.89|30.64|17.23|41.31|36.74]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 091 | [[FACT:ct.wh.table.weekly.row.091=1009|1019|41.83|31.03|17.62|41.83|37.21]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 092 | [[FACT:ct.wh.table.weekly.row.092=1019|1038|43.11|32.39|18.98|43.11|37.93]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 093 | [[FACT:ct.wh.table.weekly.row.093=1038|1057|44.15|33.94|20.53|44.15|38.87]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 094 | [[FACT:ct.wh.table.weekly.row.094=1057|1076|45.68|35.49|22.08|45.68|39.81]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 095 | [[FACT:ct.wh.table.weekly.row.095=1076|1096|46.75|37.06|23.65|46.75|40.78]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 096 | [[FACT:ct.wh.table.weekly.row.096=1096|1115|47.82|37.85|25.22|47.82|42.17]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 097 | [[FACT:ct.wh.table.weekly.row.097=1115|1134|49.35|38.62|26.76|49.35|43.11]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 098 | [[FACT:ct.wh.table.weekly.row.098=1134|1153|50.39|39.39|28.31|50.39|44.06]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 099 | [[FACT:ct.wh.table.weekly.row.099=1153|1173|51.95|40.18|29.88|51.95|45.52]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 100 | [[FACT:ct.wh.table.weekly.row.100=1173|1192|53.02|40.97|31.45|53.02|47.52]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 101 | [[FACT:ct.wh.table.weekly.row.101=1192|1211|54.06|41.74|33.00|54.06|49.99]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 102 | [[FACT:ct.wh.table.weekly.row.102=1211|1230|55.59|42.51|34.55|55.59|52.06]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 103 | [[FACT:ct.wh.table.weekly.row.103=1230|1250|56.66|43.30|36.11|56.66|54.19]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 104 | [[FACT:ct.wh.table.weekly.row.104=1250|1269|58.21|44.09|37.68|58.21|55.81]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 105 | [[FACT:ct.wh.table.weekly.row.105=1269|1288|59.26|44.86|39.23|59.26|56.86]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 106 | [[FACT:ct.wh.table.weekly.row.106=1288|1307|60.30|45.63|40.78|60.30|58.38]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 107 | [[FACT:ct.wh.table.weekly.row.107=1307|1326|61.83|46.40|42.33|61.83|59.43]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 108 | [[FACT:ct.wh.table.weekly.row.108=1326|1346|62.90|47.18|43.90|62.90|60.50]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 109 | [[FACT:ct.wh.table.weekly.row.109=1346|1365|64.46|47.97|45.47|64.46|61.57]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 110 | [[FACT:ct.wh.table.weekly.row.110=1365|1384|65.50|48.74|47.01|65.50|62.62]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 111 | [[FACT:ct.wh.table.weekly.row.111=1384|1403|66.55|49.51|47.78|66.55|64.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 112 | [[FACT:ct.wh.table.weekly.row.112=1403|1423|68.10|50.30|48.57|68.10|65.21]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 113 | [[FACT:ct.wh.table.weekly.row.113=1423|1442|69.17|51.66|49.36|69.17|66.29]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 114 | [[FACT:ct.wh.table.weekly.row.114=1442|1461|70.22|53.59|50.13|70.22|67.33]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 115 | [[FACT:ct.wh.table.weekly.row.115=1461|1480|71.26|55.56|50.90|71.26|68.38]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 116 | [[FACT:ct.wh.table.weekly.row.116=1480|1500|72.33|57.58|51.69|72.33|69.93]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 117 | [[FACT:ct.wh.table.weekly.row.117=1500|1519|73.41|59.63|52.48|73.41|71.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 118 | [[FACT:ct.wh.table.weekly.row.118=1519|1538|74.45|61.86|53.25|74.45|72.05]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 119 | [[FACT:ct.wh.table.weekly.row.119=1538|1557|75.50|62.80|54.02|75.50|73.09]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 120 | [[FACT:ct.wh.table.weekly.row.120=1557|1576|76.54|63.85|54.79|76.54|74.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 121 | [[FACT:ct.wh.table.weekly.row.121=1576|1596|77.61|64.92|55.58|77.61|75.69]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 122 | [[FACT:ct.wh.table.weekly.row.122=1596|1615|78.69|66.76|56.37|78.69|76.76]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 123 | [[FACT:ct.wh.table.weekly.row.123=1615|1634|79.73|67.81|57.14|79.73|77.81]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 124 | [[FACT:ct.wh.table.weekly.row.124=1634|1653|80.78|68.85|57.91|80.78|78.85]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 125 | [[FACT:ct.wh.table.weekly.row.125=1653|1673|81.85|69.93|58.70|81.85|79.93]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 126 | [[FACT:ct.wh.table.weekly.row.126=1673|1692|82.92|71.77|59.49|82.92|81.48]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 127 | [[FACT:ct.wh.table.weekly.row.127=1692|1711|83.97|72.81|60.26|83.97|82.52]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 128 | [[FACT:ct.wh.table.weekly.row.128=1711|1730|85.01|73.86|61.03|85.01|83.57]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 129 | [[FACT:ct.wh.table.weekly.row.129=1730|1750|86.08|74.93|61.82|86.08|84.64]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 130 | [[FACT:ct.wh.table.weekly.row.130=1750|1769|87.16|76.77|62.61|87.16|85.71]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 131 | [[FACT:ct.wh.table.weekly.row.131=1769|1788|88.20|77.82|63.38|88.20|87.24]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 132 | [[FACT:ct.wh.table.weekly.row.132=1788|1807|89.25|78.86|64.14|89.25|88.29]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 133 | [[FACT:ct.wh.table.weekly.row.133=1807|1826|90.29|79.91|64.91|90.29|89.33]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 134 | [[FACT:ct.wh.table.weekly.row.134=1826|1846|91.36|81.75|65.70|91.36|90.40]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 135 | [[FACT:ct.wh.table.weekly.row.135=1846|1865|92.44|82.82|67.23|92.44|91.48]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 136 | [[FACT:ct.wh.table.weekly.row.136=1865|1884|93.48|83.87|69.51|93.48|93.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 137 | [[FACT:ct.wh.table.weekly.row.137=1884|1903|94.53|84.91|71.81|94.53|94.05]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 138 | [[FACT:ct.wh.table.weekly.row.138=1903|1923|95.60|86.75|74.18|95.60|95.12]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table weekly row 139 | [[FACT:ct.wh.table.weekly.row.139=1923|1932|96.42|87.55|76.39|96.42|95.94]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 001 | [[FACT:ct.wh.table.biweekly.row.001=0|38|0.00|0.00|0.00|0.38|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 002 | [[FACT:ct.wh.table.biweekly.row.002=38|76|0.00|0.00|0.00|1.14|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 003 | [[FACT:ct.wh.table.biweekly.row.003=76|115|0.00|0.00|0.00|1.91|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 004 | [[FACT:ct.wh.table.biweekly.row.004=115|153|0.00|0.00|0.00|2.68|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 005 | [[FACT:ct.wh.table.biweekly.row.005=153|192|0.00|0.00|0.00|3.45|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 006 | [[FACT:ct.wh.table.biweekly.row.006=192|230|0.00|0.00|0.00|4.22|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 007 | [[FACT:ct.wh.table.biweekly.row.007=230|269|0.00|0.00|0.00|4.99|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 008 | [[FACT:ct.wh.table.biweekly.row.008=269|307|0.00|0.00|0.00|5.76|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 009 | [[FACT:ct.wh.table.biweekly.row.009=307|346|0.00|0.00|0.00|6.53|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 010 | [[FACT:ct.wh.table.biweekly.row.010=346|384|0.00|0.00|0.00|7.30|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 011 | [[FACT:ct.wh.table.biweekly.row.011=384|423|0.00|0.00|0.00|8.54|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 012 | [[FACT:ct.wh.table.biweekly.row.012=423|461|0.00|0.00|0.00|10.27|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 013 | [[FACT:ct.wh.table.biweekly.row.013=461|500|0.09|0.00|0.00|12.01|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 014 | [[FACT:ct.wh.table.biweekly.row.014=500|538|0.29|0.00|0.00|13.74|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 015 | [[FACT:ct.wh.table.biweekly.row.015=538|576|0.48|0.00|0.00|15.45|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 016 | [[FACT:ct.wh.table.biweekly.row.016=576|596|0.75|0.00|0.00|16.75|0.05]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 017 | [[FACT:ct.wh.table.biweekly.row.017=596|615|1.01|0.00|0.00|17.63|0.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 018 | [[FACT:ct.wh.table.biweekly.row.018=615|634|1.30|0.00|0.00|18.49|0.24]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 019 | [[FACT:ct.wh.table.biweekly.row.019=634|653|1.64|0.00|0.00|19.34|0.33]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 020 | [[FACT:ct.wh.table.biweekly.row.020=653|673|2.01|0.00|0.00|20.22|0.43]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 021 | [[FACT:ct.wh.table.biweekly.row.021=673|692|2.43|0.00|0.00|21.10|0.53]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 022 | [[FACT:ct.wh.table.biweekly.row.022=692|711|2.88|0.00|0.00|21.95|0.62]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 023 | [[FACT:ct.wh.table.biweekly.row.023=711|730|3.37|0.00|0.00|22.81|0.72]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 024 | [[FACT:ct.wh.table.biweekly.row.024=730|750|3.62|0.05|0.00|23.68|0.98]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 025 | [[FACT:ct.wh.table.biweekly.row.025=750|769|3.87|0.14|0.00|24.56|1.28]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 026 | [[FACT:ct.wh.table.biweekly.row.026=769|788|4.44|0.24|0.00|25.42|1.61]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 027 | [[FACT:ct.wh.table.biweekly.row.027=788|807|5.04|0.33|0.00|26.27|1.99]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 028 | [[FACT:ct.wh.table.biweekly.row.028=807|826|5.68|0.43|0.00|27.13|2.40]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 029 | [[FACT:ct.wh.table.biweekly.row.029=826|846|6.37|0.53|0.00|28.00|2.85]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 030 | [[FACT:ct.wh.table.biweekly.row.030=846|865|6.90|0.62|0.00|28.88|3.34]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 031 | [[FACT:ct.wh.table.biweekly.row.031=865|884|7.62|0.72|0.00|29.74|3.87]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 032 | [[FACT:ct.wh.table.biweekly.row.032=884|903|8.35|0.81|0.00|30.59|4.12]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 033 | [[FACT:ct.wh.table.biweekly.row.033=903|923|9.10|0.91|0.00|31.47|4.37]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 034 | [[FACT:ct.wh.table.biweekly.row.034=923|942|11.31|1.21|0.05|32.35|4.62]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 035 | [[FACT:ct.wh.table.biweekly.row.035=942|961|12.04|1.55|0.14|33.20|4.87]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 036 | [[FACT:ct.wh.table.biweekly.row.036=961|980|14.40|1.92|0.24|34.06|5.67]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 037 | [[FACT:ct.wh.table.biweekly.row.037=980|1000|15.34|2.33|0.33|34.93|6.73]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 038 | [[FACT:ct.wh.table.biweekly.row.038=1000|1019|17.81|2.79|0.43|35.81|7.88]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 039 | [[FACT:ct.wh.table.biweekly.row.039=1019|1038|18.77|3.28|0.53|36.67|9.10]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 040 | [[FACT:ct.wh.table.biweekly.row.040=1038|1057|21.31|3.80|0.62|37.52|9.83]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 041 | [[FACT:ct.wh.table.biweekly.row.041=1057|1076|22.08|4.36|0.72|38.38|10.55]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 042 | [[FACT:ct.wh.table.biweekly.row.042=1076|1096|24.43|4.62|0.81|39.25|11.30]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 043 | [[FACT:ct.wh.table.biweekly.row.043=1096|1115|25.22|4.87|0.91|40.13|12.04]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 044 | [[FACT:ct.wh.table.biweekly.row.044=1115|1134|27.54|5.12|1.01|40.99|12.77]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 045 | [[FACT:ct.wh.table.biweekly.row.045=1134|1153|28.31|5.37|1.10|41.84|13.50]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 046 | [[FACT:ct.wh.table.biweekly.row.046=1153|1173|30.66|5.62|1.44|42.72|15.72]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 047 | [[FACT:ct.wh.table.biweekly.row.047=1173|1192|31.45|5.87|1.82|43.60|16.46]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 048 | [[FACT:ct.wh.table.biweekly.row.048=1192|1211|33.78|6.12|2.23|44.45|18.66]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 049 | [[FACT:ct.wh.table.biweekly.row.049=1211|1230|34.55|6.37|2.68|45.31|19.61]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 050 | [[FACT:ct.wh.table.biweekly.row.050=1230|1250|36.89|6.62|3.17|46.18|22.11]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 051 | [[FACT:ct.wh.table.biweekly.row.051=1250|1269|37.68|6.87|3.70|47.06|23.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 052 | [[FACT:ct.wh.table.biweekly.row.052=1269|1288|40.01|7.12|4.27|47.92|25.70]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 053 | [[FACT:ct.wh.table.biweekly.row.053=1288|1307|40.78|7.37|4.87|48.77|26.76]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 054 | [[FACT:ct.wh.table.biweekly.row.054=1307|1326|43.11|8.20|5.11|49.63|29.09]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 055 | [[FACT:ct.wh.table.biweekly.row.055=1326|1346|43.90|9.08|5.37|50.50|29.88]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 056 | [[FACT:ct.wh.table.biweekly.row.056=1346|1365|46.24|10.18|5.62|51.38|32.22]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 057 | [[FACT:ct.wh.table.biweekly.row.057=1365|1384|47.01|11.55|5.87|52.24|32.99]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 058 | [[FACT:ct.wh.table.biweekly.row.058=1384|1403|47.78|12.27|6.12|53.09|35.32]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 059 | [[FACT:ct.wh.table.biweekly.row.059=1403|1423|48.57|13.02|6.37|53.97|36.11]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 060 | [[FACT:ct.wh.table.biweekly.row.060=1423|1442|49.36|13.76|6.62|54.85|38.46]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 061 | [[FACT:ct.wh.table.biweekly.row.061=1442|1461|50.13|14.49|6.87|55.70|39.23]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 062 | [[FACT:ct.wh.table.biweekly.row.062=1461|1480|50.90|16.69|7.12|56.56|41.56]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 063 | [[FACT:ct.wh.table.biweekly.row.063=1480|1500|51.69|17.43|7.37|57.43|42.34]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 064 | [[FACT:ct.wh.table.biweekly.row.064=1500|1519|52.48|19.65|7.62|58.31|44.69]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 065 | [[FACT:ct.wh.table.biweekly.row.065=1519|1538|53.25|20.38|7.87|59.17|45.46]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 066 | [[FACT:ct.wh.table.biweekly.row.066=1538|1557|54.02|22.58|8.74|60.02|47.79]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 067 | [[FACT:ct.wh.table.biweekly.row.067=1557|1576|54.79|23.30|9.65|60.88|48.56]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 068 | [[FACT:ct.wh.table.biweekly.row.068=1576|1596|55.58|25.52|10.61|61.75|50.91]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 069 | [[FACT:ct.wh.table.biweekly.row.069=1596|1615|56.37|26.27|11.60|62.63|51.70]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 070 | [[FACT:ct.wh.table.biweekly.row.070=1615|1634|57.14|28.46|11.92|63.49|54.02]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 071 | [[FACT:ct.wh.table.biweekly.row.071=1634|1653|57.91|29.19|12.25|64.34|54.79]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 072 | [[FACT:ct.wh.table.biweekly.row.072=1653|1673|58.70|31.41|12.58|65.22|57.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 073 | [[FACT:ct.wh.table.biweekly.row.073=1673|1692|59.49|32.15|12.91|66.10|57.93]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 074 | [[FACT:ct.wh.table.biweekly.row.074=1692|1711|60.26|34.76|13.43|66.95|60.26]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 075 | [[FACT:ct.wh.table.biweekly.row.075=1711|1730|61.03|35.90|14.16|67.81|61.03]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 076 | [[FACT:ct.wh.table.biweekly.row.076=1730|1750|61.82|38.61|14.90|68.68|61.82]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 077 | [[FACT:ct.wh.table.biweekly.row.077=1750|1769|62.61|39.83|15.65|69.56|62.61]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 078 | [[FACT:ct.wh.table.biweekly.row.078=1769|1788|63.38|42.61|16.37|70.42|63.38]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 079 | [[FACT:ct.wh.table.biweekly.row.079=1788|1807|64.14|43.38|17.10|71.27|64.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 080 | [[FACT:ct.wh.table.biweekly.row.080=1807|1826|64.91|45.70|17.83|72.13|64.91]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 081 | [[FACT:ct.wh.table.biweekly.row.081=1826|1846|65.70|46.49|18.57|73.00|65.70]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 082 | [[FACT:ct.wh.table.biweekly.row.082=1846|1865|67.23|48.84|20.79|73.88|66.49]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 083 | [[FACT:ct.wh.table.biweekly.row.083=1865|1884|68.76|49.61|21.52|74.74|67.26]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 084 | [[FACT:ct.wh.table.biweekly.row.084=1884|1903|70.30|51.94|23.71|75.59|68.03]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 085 | [[FACT:ct.wh.table.biweekly.row.085=1903|1923|71.88|52.73|24.46|76.47|68.82]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 086 | [[FACT:ct.wh.table.biweekly.row.086=1923|1942|73.57|55.07|26.99|77.44|69.70]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 087 | [[FACT:ct.wh.table.biweekly.row.087=1942|1961|76.27|55.84|28.05|79.45|70.64]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 088 | [[FACT:ct.wh.table.biweekly.row.088=1961|1980|78.08|58.17|30.65|80.49|71.58]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 089 | [[FACT:ct.wh.table.biweekly.row.089=1980|2000|79.93|58.96|31.78|81.57|72.54]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 090 | [[FACT:ct.wh.table.biweekly.row.090=2000|2019|81.81|61.31|34.48|82.64|73.51]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 091 | [[FACT:ct.wh.table.biweekly.row.091=2019|2038|83.68|62.08|35.25|83.68|74.45]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 092 | [[FACT:ct.wh.table.biweekly.row.092=2038|2076|86.21|64.79|37.96|86.21|75.86]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 093 | [[FACT:ct.wh.table.biweekly.row.093=2076|2115|88.33|67.91|41.08|88.33|77.77]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 094 | [[FACT:ct.wh.table.biweekly.row.094=2115|2153|91.41|71.02|44.20|91.41|79.67]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 095 | [[FACT:ct.wh.table.biweekly.row.095=2153|2192|93.53|74.14|47.31|93.53|81.58]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 096 | [[FACT:ct.wh.table.biweekly.row.096=2192|2230|95.64|75.70|50.43|95.64|84.35]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 097 | [[FACT:ct.wh.table.biweekly.row.097=2230|2269|98.72|77.26|53.55|98.72|86.25]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 098 | [[FACT:ct.wh.table.biweekly.row.098=2269|2307|100.84|78.82|56.66|100.84|88.16]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 099 | [[FACT:ct.wh.table.biweekly.row.099=2307|2346|103.92|80.38|59.78|103.92|91.07]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 100 | [[FACT:ct.wh.table.biweekly.row.100=2346|2384|106.04|81.94|62.90|106.04|95.04]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 101 | [[FACT:ct.wh.table.biweekly.row.101=2384|2423|108.15|83.50|66.01|108.15|100.01]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 102 | [[FACT:ct.wh.table.biweekly.row.102=2423|2461|111.23|85.05|69.13|111.23|104.17]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 103 | [[FACT:ct.wh.table.biweekly.row.103=2461|2500|113.35|86.61|72.25|113.35|108.41]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 104 | [[FACT:ct.wh.table.biweekly.row.104=2500|2538|116.43|88.17|75.37|116.43|111.62]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 105 | [[FACT:ct.wh.table.biweekly.row.105=2538|2576|118.52|89.71|78.46|118.52|113.71]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 106 | [[FACT:ct.wh.table.biweekly.row.106=2576|2615|120.64|91.27|81.58|120.64|116.79]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 107 | [[FACT:ct.wh.table.biweekly.row.107=2615|2653|123.72|92.83|84.70|123.72|118.91]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 108 | [[FACT:ct.wh.table.biweekly.row.108=2653|2692|125.83|94.39|87.81|125.83|121.03]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 109 | [[FACT:ct.wh.table.biweekly.row.109=2692|2730|128.91|95.95|90.93|128.91|123.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 110 | [[FACT:ct.wh.table.biweekly.row.110=2730|2769|131.03|97.51|94.05|131.03|125.26]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 111 | [[FACT:ct.wh.table.biweekly.row.111=2769|2807|133.15|99.07|95.61|133.15|128.34]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 112 | [[FACT:ct.wh.table.biweekly.row.112=2807|2846|136.23|100.63|97.17|136.23|130.46]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 113 | [[FACT:ct.wh.table.biweekly.row.113=2846|2884|138.34|103.32|98.72|138.34|132.57]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 114 | [[FACT:ct.wh.table.biweekly.row.114=2884|2923|140.46|107.20|100.28|140.46|134.69]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 115 | [[FACT:ct.wh.table.biweekly.row.115=2923|2961|142.58|111.16|101.84|142.58|136.81]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 116 | [[FACT:ct.wh.table.biweekly.row.116=2961|3000|144.70|115.18|103.40|144.70|139.89]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 117 | [[FACT:ct.wh.table.biweekly.row.117=3000|3038|146.81|119.27|104.96|146.81|142.01]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 118 | [[FACT:ct.wh.table.biweekly.row.118=3038|3076|148.90|123.72|106.50|148.90|144.10]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 119 | [[FACT:ct.wh.table.biweekly.row.119=3076|3115|151.02|125.64|108.06|151.02|146.21]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 120 | [[FACT:ct.wh.table.biweekly.row.120=3115|3153|153.14|127.75|109.62|153.14|148.33]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 121 | [[FACT:ct.wh.table.biweekly.row.121=3153|3192|155.26|129.87|111.18|155.26|151.41]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 122 | [[FACT:ct.wh.table.biweekly.row.122=3192|3230|157.37|133.53|112.74|157.37|153.53]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 123 | [[FACT:ct.wh.table.biweekly.row.123=3230|3269|159.49|135.65|114.30|159.49|155.65]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 124 | [[FACT:ct.wh.table.biweekly.row.124=3269|3307|161.61|137.76|115.86|161.61|157.76]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 125 | [[FACT:ct.wh.table.biweekly.row.125=3307|3346|163.73|139.88|117.42|163.73|159.88]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 126 | [[FACT:ct.wh.table.biweekly.row.126=3346|3384|165.84|143.54|118.97|165.84|162.96]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 127 | [[FACT:ct.wh.table.biweekly.row.127=3384|3423|167.96|145.65|120.53|167.96|165.08]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 128 | [[FACT:ct.wh.table.biweekly.row.128=3423|3461|170.08|147.77|122.09|170.08|167.19]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 129 | [[FACT:ct.wh.table.biweekly.row.129=3461|3500|172.20|149.89|123.65|172.20|169.31]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 130 | [[FACT:ct.wh.table.biweekly.row.130=3500|3538|174.31|153.54|125.21|174.31|171.43]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 131 | [[FACT:ct.wh.table.biweekly.row.131=3538|3576|176.40|155.63|126.75|176.40|174.48]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 132 | [[FACT:ct.wh.table.biweekly.row.132=3576|3615|178.52|157.75|128.31|178.52|176.60]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 133 | [[FACT:ct.wh.table.biweekly.row.133=3615|3653|180.64|159.87|129.87|180.64|178.72]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 134 | [[FACT:ct.wh.table.biweekly.row.134=3653|3692|182.76|163.53|131.43|182.76|180.83]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 135 | [[FACT:ct.wh.table.biweekly.row.135=3692|3730|184.87|165.64|134.47|184.87|182.95]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 136 | [[FACT:ct.wh.table.biweekly.row.136=3730|3769|186.99|167.76|139.03|186.99|186.03]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 137 | [[FACT:ct.wh.table.biweekly.row.137=3769|3807|189.11|169.88|143.67|189.11|188.15]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 138 | [[FACT:ct.wh.table.biweekly.row.138=3807|3846|191.23|173.53|148.37|191.23|190.27]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table biweekly row 139 | [[FACT:ct.wh.table.biweekly.row.139=3846|3865|192.87|175.13|152.82|192.87|191.91]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 001 | [[FACT:ct.wh.table.semimonthly.row.001=0|41|0.00|0.00|0.00|0.41|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 002 | [[FACT:ct.wh.table.semimonthly.row.002=41|83|0.00|0.00|0.00|1.24|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 003 | [[FACT:ct.wh.table.semimonthly.row.003=83|125|0.00|0.00|0.00|2.08|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 004 | [[FACT:ct.wh.table.semimonthly.row.004=125|166|0.00|0.00|0.00|2.91|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 005 | [[FACT:ct.wh.table.semimonthly.row.005=166|208|0.00|0.00|0.00|3.74|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 006 | [[FACT:ct.wh.table.semimonthly.row.006=208|250|0.00|0.00|0.00|4.58|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 007 | [[FACT:ct.wh.table.semimonthly.row.007=250|291|0.00|0.00|0.00|5.41|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 008 | [[FACT:ct.wh.table.semimonthly.row.008=291|333|0.00|0.00|0.00|6.24|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 009 | [[FACT:ct.wh.table.semimonthly.row.009=333|375|0.00|0.00|0.00|7.08|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 010 | [[FACT:ct.wh.table.semimonthly.row.010=375|416|0.00|0.00|0.00|7.91|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 011 | [[FACT:ct.wh.table.semimonthly.row.011=416|458|0.00|0.00|0.00|9.25|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 012 | [[FACT:ct.wh.table.semimonthly.row.012=458|500|0.00|0.00|0.00|11.14|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 013 | [[FACT:ct.wh.table.semimonthly.row.013=500|541|0.10|0.00|0.00|13.01|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 014 | [[FACT:ct.wh.table.semimonthly.row.014=541|583|0.31|0.00|0.00|14.87|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 015 | [[FACT:ct.wh.table.semimonthly.row.015=583|625|0.52|0.00|0.00|16.76|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 016 | [[FACT:ct.wh.table.semimonthly.row.016=625|645|0.81|0.00|0.00|18.16|0.05]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 017 | [[FACT:ct.wh.table.semimonthly.row.017=645|666|1.09|0.00|0.00|19.08|0.15]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 018 | [[FACT:ct.wh.table.semimonthly.row.018=666|687|1.41|0.00|0.00|20.03|0.26]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 019 | [[FACT:ct.wh.table.semimonthly.row.019=687|708|1.78|0.00|0.00|20.97|0.36]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 020 | [[FACT:ct.wh.table.semimonthly.row.020=708|729|2.19|0.00|0.00|21.92|0.47]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 021 | [[FACT:ct.wh.table.semimonthly.row.021=729|750|2.63|0.00|0.00|22.86|0.57]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 022 | [[FACT:ct.wh.table.semimonthly.row.022=750|770|3.12|0.00|0.00|23.78|0.68]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 023 | [[FACT:ct.wh.table.semimonthly.row.023=770|791|3.65|0.00|0.00|24.71|0.78]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 024 | [[FACT:ct.wh.table.semimonthly.row.024=791|812|3.92|0.05|0.00|25.65|1.06]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 025 | [[FACT:ct.wh.table.semimonthly.row.025=812|833|4.19|0.15|0.00|26.60|1.38]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 026 | [[FACT:ct.wh.table.semimonthly.row.026=833|854|4.81|0.26|0.00|27.54|1.75]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 027 | [[FACT:ct.wh.table.semimonthly.row.027=854|875|5.47|0.36|0.00|28.49|2.16]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 028 | [[FACT:ct.wh.table.semimonthly.row.028=875|895|6.16|0.47|0.00|29.41|2.60]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 029 | [[FACT:ct.wh.table.semimonthly.row.029=895|916|6.89|0.57|0.00|30.33|3.09]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 030 | [[FACT:ct.wh.table.semimonthly.row.030=916|937|7.46|0.67|0.00|31.28|3.62]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 031 | [[FACT:ct.wh.table.semimonthly.row.031=937|958|8.26|0.78|0.00|32.22|4.19]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 032 | [[FACT:ct.wh.table.semimonthly.row.032=958|979|9.07|0.88|0.00|33.17|4.47]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 033 | [[FACT:ct.wh.table.semimonthly.row.033=979|1000|9.87|0.99|0.00|34.11|4.74]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 034 | [[FACT:ct.wh.table.semimonthly.row.034=1000|1020|12.25|1.31|0.05|35.03|5.01]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 035 | [[FACT:ct.wh.table.semimonthly.row.035=1020|1041|13.03|1.67|0.15|35.96|5.27]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 036 | [[FACT:ct.wh.table.semimonthly.row.036=1041|1062|15.61|2.08|0.26|36.90|6.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 037 | [[FACT:ct.wh.table.semimonthly.row.037=1062|1083|16.61|2.53|0.36|37.85|7.29]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 038 | [[FACT:ct.wh.table.semimonthly.row.038=1083|1104|19.29|3.02|0.47|38.79|8.53]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 039 | [[FACT:ct.wh.table.semimonthly.row.039=1104|1125|20.35|3.55|0.57|39.74|9.87]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 040 | [[FACT:ct.wh.table.semimonthly.row.040=1125|1145|23.09|4.12|0.68|40.66|10.65]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 041 | [[FACT:ct.wh.table.semimonthly.row.041=1145|1166|23.92|4.73|0.78|41.58|11.44]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 042 | [[FACT:ct.wh.table.semimonthly.row.042=1166|1187|26.46|5.00|0.88|42.53|12.24]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 043 | [[FACT:ct.wh.table.semimonthly.row.043=1187|1208|27.31|5.28|0.99|43.47|13.04]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 044 | [[FACT:ct.wh.table.semimonthly.row.044=1208|1229|29.85|5.55|1.09|44.42|13.85]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 045 | [[FACT:ct.wh.table.semimonthly.row.045=1229|1250|30.70|5.82|1.20|45.36|14.65]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 046 | [[FACT:ct.wh.table.semimonthly.row.046=1250|1270|33.22|6.09|1.56|46.28|17.03]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 047 | [[FACT:ct.wh.table.semimonthly.row.047=1270|1291|34.05|6.35|1.96|47.21|17.81]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 048 | [[FACT:ct.wh.table.semimonthly.row.048=1291|1312|36.59|6.63|2.41|48.15|20.21]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 049 | [[FACT:ct.wh.table.semimonthly.row.049=1312|1333|37.44|6.90|2.90|49.10|21.26]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 050 | [[FACT:ct.wh.table.semimonthly.row.050=1333|1354|39.97|7.17|3.44|50.04|23.96]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 051 | [[FACT:ct.wh.table.semimonthly.row.051=1354|1375|40.82|7.45|4.01|50.99|25.07]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 052 | [[FACT:ct.wh.table.semimonthly.row.052=1375|1395|43.34|7.71|4.62|51.91|27.84]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 053 | [[FACT:ct.wh.table.semimonthly.row.053=1395|1416|44.17|7.98|5.27|52.83|28.99]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 054 | [[FACT:ct.wh.table.semimonthly.row.054=1416|1437|46.71|8.89|5.54|53.78|31.52]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 055 | [[FACT:ct.wh.table.semimonthly.row.055=1437|1458|47.56|9.84|5.82|54.72|32.37]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 056 | [[FACT:ct.wh.table.semimonthly.row.056=1458|1479|50.10|11.03|6.09|55.67|34.91]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 057 | [[FACT:ct.wh.table.semimonthly.row.057=1479|1500|50.95|12.53|6.36|56.61|35.76]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 058 | [[FACT:ct.wh.table.semimonthly.row.058=1500|1520|51.78|13.31|6.63|57.53|38.28]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 059 | [[FACT:ct.wh.table.semimonthly.row.059=1520|1541|52.61|14.09|6.90|58.46|39.11]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 060 | [[FACT:ct.wh.table.semimonthly.row.060=1541|1562|53.46|14.90|7.17|59.40|41.65]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 061 | [[FACT:ct.wh.table.semimonthly.row.061=1562|1583|54.31|15.70|7.44|60.35|42.50]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 062 | [[FACT:ct.wh.table.semimonthly.row.062=1583|1604|55.16|18.10|7.72|61.29|45.04]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 063 | [[FACT:ct.wh.table.semimonthly.row.063=1604|1625|56.01|18.90|7.99|62.24|45.89]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 064 | [[FACT:ct.wh.table.semimonthly.row.064=1625|1645|56.84|21.28|8.26|63.16|48.40]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 065 | [[FACT:ct.wh.table.semimonthly.row.065=1645|1666|57.67|22.06|8.52|64.08|49.24]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 066 | [[FACT:ct.wh.table.semimonthly.row.066=1666|1687|58.52|24.46|9.47|65.03|51.77]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 067 | [[FACT:ct.wh.table.semimonthly.row.067=1687|1708|59.37|25.26|10.46|65.97|52.62]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 068 | [[FACT:ct.wh.table.semimonthly.row.068=1708|1729|60.22|27.66|11.50|66.92|55.16]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 069 | [[FACT:ct.wh.table.semimonthly.row.069=1729|1750|61.07|28.46|12.57|67.86|56.01]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 070 | [[FACT:ct.wh.table.semimonthly.row.070=1750|1770|61.90|30.84|12.92|68.78|58.53]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 071 | [[FACT:ct.wh.table.semimonthly.row.071=1770|1791|62.74|31.62|13.27|69.71|59.36]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 072 | [[FACT:ct.wh.table.semimonthly.row.072=1791|1812|63.59|34.02|13.63|70.65|61.90]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 073 | [[FACT:ct.wh.table.semimonthly.row.073=1812|1833|64.44|34.83|13.98|71.60|62.75]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 074 | [[FACT:ct.wh.table.semimonthly.row.074=1833|1854|65.29|37.66|14.56|72.54|65.29]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 075 | [[FACT:ct.wh.table.semimonthly.row.075=1854|1875|66.14|38.92|15.36|73.49|66.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 076 | [[FACT:ct.wh.table.semimonthly.row.076=1875|1895|66.97|41.83|16.14|74.41|66.97]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 077 | [[FACT:ct.wh.table.semimonthly.row.077=1895|1916|67.80|43.13|16.93|75.33|67.80]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 078 | [[FACT:ct.wh.table.semimonthly.row.078=1916|1937|68.65|46.15|17.73|76.28|68.65]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 079 | [[FACT:ct.wh.table.semimonthly.row.079=1937|1958|69.50|47.00|18.53|77.22|69.50]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 080 | [[FACT:ct.wh.table.semimonthly.row.080=1958|1979|70.35|49.54|19.34|78.17|70.35]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 081 | [[FACT:ct.wh.table.semimonthly.row.081=1979|2000|71.20|50.39|20.14|79.11|71.20]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 082 | [[FACT:ct.wh.table.semimonthly.row.082=2000|2020|72.83|52.90|22.52|80.03|72.03]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 083 | [[FACT:ct.wh.table.semimonthly.row.083=2020|2041|74.48|53.74|23.30|80.96|72.86]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 084 | [[FACT:ct.wh.table.semimonthly.row.084=2041|2062|76.17|56.27|25.70|81.90|73.71]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 085 | [[FACT:ct.wh.table.semimonthly.row.085=2062|2083|77.88|57.12|26.50|82.85|74.56]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 086 | [[FACT:ct.wh.table.semimonthly.row.086=2083|2104|79.70|59.66|29.24|83.89|75.50]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 087 | [[FACT:ct.wh.table.semimonthly.row.087=2104|2125|82.65|60.51|30.40|86.09|76.54]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 088 | [[FACT:ct.wh.table.semimonthly.row.088=2125|2145|84.60|63.03|33.21|87.22|77.56]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 089 | [[FACT:ct.wh.table.semimonthly.row.089=2145|2166|86.58|63.86|34.41|88.34|78.57]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 090 | [[FACT:ct.wh.table.semimonthly.row.090=2166|2187|88.60|66.40|37.34|89.50|79.61]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 091 | [[FACT:ct.wh.table.semimonthly.row.091=2187|2208|90.65|67.25|38.19|90.65|80.65]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 092 | [[FACT:ct.wh.table.semimonthly.row.092=2208|2250|93.43|70.21|41.15|93.43|82.21]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 093 | [[FACT:ct.wh.table.semimonthly.row.093=2250|2291|95.71|73.58|44.52|95.71|84.26]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 094 | [[FACT:ct.wh.table.semimonthly.row.094=2291|2333|99.03|76.95|47.89|99.03|86.32]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 095 | [[FACT:ct.wh.table.semimonthly.row.095=2333|2375|101.34|80.34|51.27|101.34|88.40]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 096 | [[FACT:ct.wh.table.semimonthly.row.096=2375|2416|103.63|82.02|54.64|103.63|91.39]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 097 | [[FACT:ct.wh.table.semimonthly.row.097=2416|2458|106.95|83.70|58.01|106.95|93.44]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 098 | [[FACT:ct.wh.table.semimonthly.row.098=2458|2500|109.26|85.40|61.40|109.26|95.52]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 099 | [[FACT:ct.wh.table.semimonthly.row.099=2500|2541|112.59|87.08|64.77|112.59|98.66]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 100 | [[FACT:ct.wh.table.semimonthly.row.100=2541|2583|114.87|88.76|68.14|114.87|102.95]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 101 | [[FACT:ct.wh.table.semimonthly.row.101=2583|2625|117.18|90.46|71.52|117.18|108.35]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 102 | [[FACT:ct.wh.table.semimonthly.row.102=2625|2666|120.50|92.14|74.89|120.50|112.85]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 103 | [[FACT:ct.wh.table.semimonthly.row.103=2666|2708|122.78|93.82|78.26|122.78|117.43]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 104 | [[FACT:ct.wh.table.semimonthly.row.104=2708|2750|126.14|95.52|81.65|126.14|120.93]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 105 | [[FACT:ct.wh.table.semimonthly.row.105=2750|2791|128.42|97.21|85.02|128.42|123.21]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 106 | [[FACT:ct.wh.table.semimonthly.row.106=2791|2833|130.70|98.89|88.39|130.70|126.53]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 107 | [[FACT:ct.wh.table.semimonthly.row.107=2833|2875|134.05|100.59|91.77|134.05|128.84]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 108 | [[FACT:ct.wh.table.semimonthly.row.108=2875|2916|136.34|102.27|95.14|136.34|131.13]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 109 | [[FACT:ct.wh.table.semimonthly.row.109=2916|2958|139.66|103.95|98.51|139.66|133.41]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 110 | [[FACT:ct.wh.table.semimonthly.row.110=2958|3000|141.97|105.65|101.90|141.97|135.72]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 111 | [[FACT:ct.wh.table.semimonthly.row.111=3000|3041|144.25|107.33|103.58|144.25|139.04]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 112 | [[FACT:ct.wh.table.semimonthly.row.112=3041|3083|147.58|109.01|105.26|147.58|141.33]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 113 | [[FACT:ct.wh.table.semimonthly.row.113=3083|3125|149.89|111.94|106.96|149.89|143.64]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 114 | [[FACT:ct.wh.table.semimonthly.row.114=3125|3166|152.17|116.14|108.64|152.17|145.92]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 115 | [[FACT:ct.wh.table.semimonthly.row.115=3166|3208|154.45|120.41|110.32|154.45|148.20]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 116 | [[FACT:ct.wh.table.semimonthly.row.116=3208|3250|156.76|124.78|112.02|156.76|151.55]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 117 | [[FACT:ct.wh.table.semimonthly.row.117=3250|3291|159.04|129.20|113.71|159.04|153.84]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 118 | [[FACT:ct.wh.table.semimonthly.row.118=3291|3333|161.33|134.04|115.39|161.33|156.12]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 119 | [[FACT:ct.wh.table.semimonthly.row.119=3333|3375|163.64|136.14|117.09|163.64|158.43]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 120 | [[FACT:ct.wh.table.semimonthly.row.120=3375|3416|165.92|138.42|118.77|165.92|160.71]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 121 | [[FACT:ct.wh.table.semimonthly.row.121=3416|3458|168.20|140.70|120.45|168.20|164.03]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 122 | [[FACT:ct.wh.table.semimonthly.row.122=3458|3500|170.51|144.68|122.15|170.51|166.34]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 123 | [[FACT:ct.wh.table.semimonthly.row.123=3500|3541|172.79|146.96|123.83|172.79|168.63]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 124 | [[FACT:ct.wh.table.semimonthly.row.124=3541|3583|175.08|149.24|125.51|175.08|170.91]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 125 | [[FACT:ct.wh.table.semimonthly.row.125=3583|3625|177.39|151.55|127.21|177.39|173.22]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 126 | [[FACT:ct.wh.table.semimonthly.row.126=3625|3666|179.67|155.50|128.89|179.67|176.54]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 127 | [[FACT:ct.wh.table.semimonthly.row.127=3666|3708|181.95|157.78|130.57|181.95|178.83]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 128 | [[FACT:ct.wh.table.semimonthly.row.128=3708|3750|184.26|160.09|132.27|184.26|181.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 129 | [[FACT:ct.wh.table.semimonthly.row.129=3750|3791|186.54|162.38|133.96|186.54|183.42]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 130 | [[FACT:ct.wh.table.semimonthly.row.130=3791|3833|188.83|166.33|135.64|188.83|185.70]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 131 | [[FACT:ct.wh.table.semimonthly.row.131=3833|3875|191.14|168.64|137.34|191.14|189.05]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 132 | [[FACT:ct.wh.table.semimonthly.row.132=3875|3916|193.42|170.92|139.02|193.42|191.34]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 133 | [[FACT:ct.wh.table.semimonthly.row.133=3916|3958|195.70|173.20|140.70|195.70|193.62]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 134 | [[FACT:ct.wh.table.semimonthly.row.134=3958|4000|198.01|177.18|142.40|198.01|195.93]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 135 | [[FACT:ct.wh.table.semimonthly.row.135=4000|4041|200.29|179.46|145.68|200.29|198.21]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 136 | [[FACT:ct.wh.table.semimonthly.row.136=4041|4083|202.58|181.74|150.62|202.58|201.53]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 137 | [[FACT:ct.wh.table.semimonthly.row.137=4083|4125|204.89|184.05|155.65|204.89|203.84]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 138 | [[FACT:ct.wh.table.semimonthly.row.138=4125|4166|207.17|188.00|160.74|207.17|206.13]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table semimonthly row 139 | [[FACT:ct.wh.table.semimonthly.row.139=4166|4187|208.92|189.71|165.54|208.92|207.88]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 001 | [[FACT:ct.wh.table.monthly.row.001=0|83|0.00|0.00|0.00|0.83|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 002 | [[FACT:ct.wh.table.monthly.row.002=83|166|0.00|0.00|0.00|2.49|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 003 | [[FACT:ct.wh.table.monthly.row.003=166|250|0.00|0.00|0.00|4.16|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 004 | [[FACT:ct.wh.table.monthly.row.004=250|333|0.00|0.00|0.00|5.83|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 005 | [[FACT:ct.wh.table.monthly.row.005=333|416|0.00|0.00|0.00|7.49|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 006 | [[FACT:ct.wh.table.monthly.row.006=416|500|0.00|0.00|0.00|9.16|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 007 | [[FACT:ct.wh.table.monthly.row.007=500|583|0.00|0.00|0.00|10.83|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 008 | [[FACT:ct.wh.table.monthly.row.008=583|666|0.00|0.00|0.00|12.49|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 009 | [[FACT:ct.wh.table.monthly.row.009=666|750|0.00|0.00|0.00|14.16|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 010 | [[FACT:ct.wh.table.monthly.row.010=750|833|0.00|0.00|0.00|15.83|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 011 | [[FACT:ct.wh.table.monthly.row.011=833|916|0.00|0.00|0.00|18.52|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 012 | [[FACT:ct.wh.table.monthly.row.012=916|1000|0.00|0.00|0.00|22.28|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 013 | [[FACT:ct.wh.table.monthly.row.013=1000|1083|0.21|0.00|0.00|26.03|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 014 | [[FACT:ct.wh.table.monthly.row.014=1083|1166|0.62|0.00|0.00|29.77|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 015 | [[FACT:ct.wh.table.monthly.row.015=1166|1250|1.04|0.00|0.00|33.53|0.00]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 016 | [[FACT:ct.wh.table.monthly.row.016=1250|1291|1.62|0.00|0.00|36.34|0.10]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 017 | [[FACT:ct.wh.table.monthly.row.017=1291|1333|2.18|0.00|0.00|38.21|0.31]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 018 | [[FACT:ct.wh.table.monthly.row.018=1333|1375|2.83|0.00|0.00|40.10|0.52]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 019 | [[FACT:ct.wh.table.monthly.row.019=1375|1416|3.56|0.00|0.00|41.96|0.73]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 020 | [[FACT:ct.wh.table.monthly.row.020=1416|1458|4.37|0.00|0.00|43.83|0.94]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 021 | [[FACT:ct.wh.table.monthly.row.021=1458|1500|5.27|0.00|0.00|45.72|1.15]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 022 | [[FACT:ct.wh.table.monthly.row.022=1500|1541|6.25|0.00|0.00|47.59|1.35]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 023 | [[FACT:ct.wh.table.monthly.row.023=1541|1583|7.31|0.00|0.00|49.46|1.56]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 024 | [[FACT:ct.wh.table.monthly.row.024=1583|1625|7.85|0.10|0.00|51.35|2.12]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 025 | [[FACT:ct.wh.table.monthly.row.025=1625|1666|8.39|0.31|0.00|53.21|2.77]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 026 | [[FACT:ct.wh.table.monthly.row.026=1666|1708|9.62|0.52|0.00|55.08|3.50]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 027 | [[FACT:ct.wh.table.monthly.row.027=1708|1750|10.94|0.73|0.00|56.97|4.31]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 028 | [[FACT:ct.wh.table.monthly.row.028=1750|1791|12.33|0.94|0.00|58.84|5.21]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 029 | [[FACT:ct.wh.table.monthly.row.029=1791|1833|13.80|1.14|0.00|60.71|6.18]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 030 | [[FACT:ct.wh.table.monthly.row.030=1833|1875|14.96|1.35|0.00|62.60|7.25]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 031 | [[FACT:ct.wh.table.monthly.row.031=1875|1916|16.54|1.56|0.00|64.46|8.39]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 032 | [[FACT:ct.wh.table.monthly.row.032=1916|1958|18.13|1.77|0.00|66.33|8.93]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 033 | [[FACT:ct.wh.table.monthly.row.033=1958|2000|19.74|1.98|0.00|68.22|9.48]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 034 | [[FACT:ct.wh.table.monthly.row.034=2000|2041|24.51|2.62|0.10|70.09|10.02]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 035 | [[FACT:ct.wh.table.monthly.row.035=2041|2083|26.10|3.35|0.31|71.96|10.56]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 036 | [[FACT:ct.wh.table.monthly.row.036=2083|2125|31.26|4.17|0.52|73.85|12.32]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 037 | [[FACT:ct.wh.table.monthly.row.037=2125|2166|33.25|5.06|0.73|75.71|14.60]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 038 | [[FACT:ct.wh.table.monthly.row.038=2166|2208|38.57|6.04|0.94|77.58|17.07]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 039 | [[FACT:ct.wh.table.monthly.row.039=2208|2250|40.69|7.10|1.15|79.47|19.74]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 040 | [[FACT:ct.wh.table.monthly.row.040=2250|2291|46.21|8.25|1.35|81.34|21.33]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 041 | [[FACT:ct.wh.table.monthly.row.041=2291|2333|47.89|9.47|1.56|83.21|22.91]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 042 | [[FACT:ct.wh.table.monthly.row.042=2333|2375|52.96|10.02|1.77|85.10|24.52]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 043 | [[FACT:ct.wh.table.monthly.row.043=2375|2416|54.64|10.56|1.98|86.96|26.11]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 044 | [[FACT:ct.wh.table.monthly.row.044=2416|2458|59.70|11.10|2.19|88.83|27.69]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 045 | [[FACT:ct.wh.table.monthly.row.045=2458|2500|61.40|11.64|2.40|90.72|29.30]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 046 | [[FACT:ct.wh.table.monthly.row.046=2500|2541|66.46|12.18|3.12|92.59|34.08]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 047 | [[FACT:ct.wh.table.monthly.row.047=2541|2583|68.14|12.72|3.93|94.46|35.66]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 048 | [[FACT:ct.wh.table.monthly.row.048=2583|2625|73.21|13.27|4.83|96.35|40.46]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 049 | [[FACT:ct.wh.table.monthly.row.049=2625|2666|74.89|13.81|5.81|98.21|42.54]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 050 | [[FACT:ct.wh.table.monthly.row.050=2666|2708|79.95|14.35|6.87|100.08|47.92]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 051 | [[FACT:ct.wh.table.monthly.row.051=2708|2750|81.65|14.89|8.02|101.97|50.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 052 | [[FACT:ct.wh.table.monthly.row.052=2750|2791|86.71|15.43|9.25|103.84|55.70]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 053 | [[FACT:ct.wh.table.monthly.row.053=2791|2833|88.39|15.97|10.56|105.71|58.01]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 054 | [[FACT:ct.wh.table.monthly.row.054=2833|2875|93.46|17.79|11.10|107.60|63.09]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 055 | [[FACT:ct.wh.table.monthly.row.055=2875|2916|95.14|19.68|11.64|109.46|64.77]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 056 | [[FACT:ct.wh.table.monthly.row.056=2916|2958|100.20|22.07|12.18|111.33|69.82]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 057 | [[FACT:ct.wh.table.monthly.row.057=2958|3000|101.90|25.05|12.73|113.22|71.52]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 058 | [[FACT:ct.wh.table.monthly.row.058=3000|3041|103.58|26.64|13.27|115.09|76.58]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 059 | [[FACT:ct.wh.table.monthly.row.059=3041|3083|105.26|28.23|13.81|116.96|78.26]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 060 | [[FACT:ct.wh.table.monthly.row.060=3083|3125|106.96|29.83|14.35|118.85|83.34]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 061 | [[FACT:ct.wh.table.monthly.row.061=3125|3166|108.64|31.42|14.89|120.71|85.02]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 062 | [[FACT:ct.wh.table.monthly.row.062=3166|3208|110.32|36.19|15.43|122.58|90.07]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 063 | [[FACT:ct.wh.table.monthly.row.063=3208|3250|112.02|37.80|15.98|124.47|91.77]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 064 | [[FACT:ct.wh.table.monthly.row.064=3250|3291|113.71|42.58|16.52|126.34|96.83]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 065 | [[FACT:ct.wh.table.monthly.row.065=3291|3333|115.39|44.16|17.06|128.21|98.51]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 066 | [[FACT:ct.wh.table.monthly.row.066=3333|3375|117.09|48.96|18.96|130.10|103.59]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 067 | [[FACT:ct.wh.table.monthly.row.067=3375|3416|118.77|50.54|20.93|131.96|105.27]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 068 | [[FACT:ct.wh.table.monthly.row.068=3416|3458|120.45|55.32|22.99|133.83|110.32]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 069 | [[FACT:ct.wh.table.monthly.row.069=3458|3500|122.15|56.93|25.14|135.72|112.02]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 070 | [[FACT:ct.wh.table.monthly.row.070=3500|3541|123.83|61.70|25.85|137.59|117.08]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 071 | [[FACT:ct.wh.table.monthly.row.071=3541|3583|125.51|63.29|26.55|139.46|118.76]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 072 | [[FACT:ct.wh.table.monthly.row.072=3583|3625|127.21|68.08|27.27|141.35|123.84]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 073 | [[FACT:ct.wh.table.monthly.row.073=3625|3666|128.89|69.67|27.97|143.21|125.52]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 074 | [[FACT:ct.wh.table.monthly.row.074=3666|3708|130.57|75.32|29.11|145.08|130.57]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 075 | [[FACT:ct.wh.table.monthly.row.075=3708|3750|132.27|77.84|30.72|146.97|132.27]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 076 | [[FACT:ct.wh.table.monthly.row.076=3750|3791|133.96|83.68|32.30|148.84|133.96]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 077 | [[FACT:ct.wh.table.monthly.row.077=3791|3833|135.64|86.29|33.89|150.71|135.64]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 078 | [[FACT:ct.wh.table.monthly.row.078=3833|3875|137.34|92.34|35.50|152.60|137.34]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 079 | [[FACT:ct.wh.table.monthly.row.079=3875|3916|139.02|94.02|37.09|154.46|139.02]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 080 | [[FACT:ct.wh.table.monthly.row.080=3916|3958|140.70|99.07|38.67|156.33|140.70]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 081 | [[FACT:ct.wh.table.monthly.row.081=3958|4000|142.40|100.77|40.28|158.22|142.40]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 082 | [[FACT:ct.wh.table.monthly.row.082=4000|4041|145.68|105.83|45.05|160.09|144.08]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 083 | [[FACT:ct.wh.table.monthly.row.083=4041|4083|149.00|107.51|46.64|161.96|145.76]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 084 | [[FACT:ct.wh.table.monthly.row.084=4083|4125|152.38|112.59|51.44|163.85|147.46]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 085 | [[FACT:ct.wh.table.monthly.row.085=4125|4166|155.77|114.27|53.02|165.71|149.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 086 | [[FACT:ct.wh.table.monthly.row.086=4166|4208|159.40|119.32|58.48|167.78|151.01]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 087 | [[FACT:ct.wh.table.monthly.row.087=4208|4250|165.29|121.02|60.80|172.18|153.09]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 088 | [[FACT:ct.wh.table.monthly.row.088=4250|4291|169.23|126.08|66.45|174.46|155.14]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 089 | [[FACT:ct.wh.table.monthly.row.089=4291|4333|173.21|127.76|68.86|176.74|157.19]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 090 | [[FACT:ct.wh.table.monthly.row.090=4333|4375|177.26|132.84|74.71|179.05|159.27]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 091 | [[FACT:ct.wh.table.monthly.row.091=4375|4416|181.34|134.52|76.39|181.34|161.33]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 092 | [[FACT:ct.wh.table.monthly.row.092=4416|4500|186.86|140.42|82.30|186.86|164.42]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 093 | [[FACT:ct.wh.table.monthly.row.093=4500|4583|191.45|147.18|89.06|191.45|168.55]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 094 | [[FACT:ct.wh.table.monthly.row.094=4583|4666|198.10|153.92|95.79|198.10|172.66]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 095 | [[FACT:ct.wh.table.monthly.row.095=4666|4750|202.69|160.67|102.55|202.69|176.80]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 096 | [[FACT:ct.wh.table.monthly.row.096=4750|4833|207.28|164.06|109.31|207.28|182.80]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 097 | [[FACT:ct.wh.table.monthly.row.097=4833|4916|213.93|167.42|116.04|213.93|186.91]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 098 | [[FACT:ct.wh.table.monthly.row.098=4916|5000|218.52|170.80|122.80|218.52|191.05]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 099 | [[FACT:ct.wh.table.monthly.row.099=5000|5083|225.20|174.18|129.56|225.20|197.35]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 100 | [[FACT:ct.wh.table.monthly.row.100=5083|5166|229.76|177.54|136.29|229.76|205.93]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 101 | [[FACT:ct.wh.table.monthly.row.101=5166|5250|234.36|180.92|143.05|234.36|216.70]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 102 | [[FACT:ct.wh.table.monthly.row.102=5250|5333|241.03|184.31|149.81|241.03|225.72]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 103 | [[FACT:ct.wh.table.monthly.row.103=5333|5416|245.60|187.67|156.54|245.60|234.89]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 104 | [[FACT:ct.wh.table.monthly.row.104=5416|5500|252.27|191.05|163.30|252.27|241.86]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 105 | [[FACT:ct.wh.table.monthly.row.105=5500|5583|256.87|194.43|170.06|256.87|246.45]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 106 | [[FACT:ct.wh.table.monthly.row.106=5583|5666|261.43|197.79|176.79|261.43|253.10]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 107 | [[FACT:ct.wh.table.monthly.row.107=5666|5750|268.11|201.17|183.55|268.11|257.69]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 108 | [[FACT:ct.wh.table.monthly.row.108=5750|5833|272.70|204.56|190.31|272.70|262.28]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 109 | [[FACT:ct.wh.table.monthly.row.109=5833|5916|279.35|207.92|197.04|279.35|266.85]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 110 | [[FACT:ct.wh.table.monthly.row.110=5916|6000|283.94|211.30|203.80|283.94|271.44]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 111 | [[FACT:ct.wh.table.monthly.row.111=6000|6083|288.53|214.68|207.18|288.53|278.12]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 112 | [[FACT:ct.wh.table.monthly.row.112=6083|6166|295.18|218.04|210.54|295.18|282.68]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 113 | [[FACT:ct.wh.table.monthly.row.113=6166|6250|299.77|223.88|213.92|299.77|287.27]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 114 | [[FACT:ct.wh.table.monthly.row.114=6250|6333|304.37|232.30|217.31|304.37|291.87]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 115 | [[FACT:ct.wh.table.monthly.row.115=6333|6416|308.93|240.84|220.67|308.93|296.43]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 116 | [[FACT:ct.wh.table.monthly.row.116=6416|6500|313.52|249.56|224.05|313.52|303.11]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 117 | [[FACT:ct.wh.table.monthly.row.117=6500|6583|318.12|258.42|227.43|318.12|307.70]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 118 | [[FACT:ct.wh.table.monthly.row.118=6583|6666|322.68|268.10|230.79|322.68|312.26]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 119 | [[FACT:ct.wh.table.monthly.row.119=6666|6750|327.27|272.27|234.17|327.27|316.86]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 120 | [[FACT:ct.wh.table.monthly.row.120=6750|6833|331.87|276.87|237.56|331.87|321.45]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 121 | [[FACT:ct.wh.table.monthly.row.121=6833|6916|336.43|281.43|240.92|336.43|328.10]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 122 | [[FACT:ct.wh.table.monthly.row.122=6916|7000|341.02|289.36|244.30|341.02|332.69]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 123 | [[FACT:ct.wh.table.monthly.row.123=7000|7083|345.62|293.95|247.68|345.62|337.28]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 124 | [[FACT:ct.wh.table.monthly.row.124=7083|7166|350.18|298.51|251.04|350.18|341.85]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 125 | [[FACT:ct.wh.table.monthly.row.125=7166|7250|354.77|303.11|254.42|354.77|346.44]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 126 | [[FACT:ct.wh.table.monthly.row.126=7250|7333|359.37|311.03|257.81|359.37|353.12]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 127 | [[FACT:ct.wh.table.monthly.row.127=7333|7416|363.93|315.60|261.17|363.93|357.68]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 128 | [[FACT:ct.wh.table.monthly.row.128=7416|7500|368.52|320.19|264.55|368.52|362.27]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 129 | [[FACT:ct.wh.table.monthly.row.129=7500|7583|373.12|324.78|267.93|373.12|366.87]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 130 | [[FACT:ct.wh.table.monthly.row.130=7583|7666|377.68|332.68|271.29|377.68|371.43]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 131 | [[FACT:ct.wh.table.monthly.row.131=7666|7750|382.27|337.27|274.67|382.27|378.11]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 132 | [[FACT:ct.wh.table.monthly.row.132=7750|7833|386.87|341.87|278.06|386.87|382.70]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 133 | [[FACT:ct.wh.table.monthly.row.133=7833|7916|391.43|346.43|281.42|391.43|387.26]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 134 | [[FACT:ct.wh.table.monthly.row.134=7916|8000|396.02|354.36|284.80|396.02|391.86]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 135 | [[FACT:ct.wh.table.monthly.row.135=8000|8083|400.62|358.95|291.38|400.62|396.45]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 136 | [[FACT:ct.wh.table.monthly.row.136=8083|8166|405.18|363.51|301.26|405.18|403.10]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 137 | [[FACT:ct.wh.table.monthly.row.137=8166|8250|409.77|368.11|311.31|409.77|407.69]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 138 | [[FACT:ct.wh.table.monthly.row.138=8250|8333|414.37|376.03|321.51|414.37|412.28]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table monthly row 139 | [[FACT:ct.wh.table.monthly.row.139=8333|8375|417.91|379.47|331.13|417.91|415.82]] | 2026-01-01 to 2026-12-31 |  | S11 |  |
| Withholding table c code a d | [[FACT:ct.wh.table_c.code_a_d=0-50,250: 0; 50,250-52,750: 25; 52,750-55,250: 50; 55,250-57,750: 75; 57,750-60,250: 100; 60,250-62,750: 125; 62,750-65,250: 150; 65,250-67,750: 175; 67,750-70,250: 200; 70,250-72,750: 225; over 72,750: 250]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), 2% tax rate phase-out add-back (USD) by annualized salary (more than - less than or equal to); printed in IP 2026(1) Circular CT PDF p.28. 11 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |
| Withholding table c code b | [[FACT:ct.wh.table_c.code_b=0-78,500: 0; 78,500-82,500: 40; 82,500-86,500: 80; 86,500-90,500: 120; 90,500-94,500: 160; 94,500-98,500: 200; 98,500-102,500: 240; 102,500-106,500: 280; 106,500-110,500: 320; 110,500-114,500: 360; over 114,500: 400]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), 2% tax rate phase-out add-back (USD) by annualized salary (more than - less than or equal to); printed in IP 2026(1) Circular CT PDF p.28. 11 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |
| Withholding table c code c | [[FACT:ct.wh.table_c.code_c=0-100,500: 0; 100,500-105,500: 50; 105,500-110,500: 100; 110,500-115,500: 150; 115,500-120,500: 200; 120,500-125,500: 250; 125,500-130,500: 300; 130,500-135,500: 350; 135,500-140,500: 400; 140,500-145,500: 450; over 145,500: 500]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), 2% tax rate phase-out add-back (USD) by annualized salary (more than - less than or equal to); printed in IP 2026(1) Circular CT PDF p.28. 11 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |
| Withholding table c code f | [[FACT:ct.wh.table_c.code_f=0-56,500: 0; 56,500-61,500: 25; 61,500-66,500: 50; 66,500-71,500: 75; 71,500-76,500: 100; 76,500-81,500: 125; 81,500-86,500: 150; 86,500-91,500: 175; 91,500-96,500: 200; 96,500-101,500: 225; over 101,500: 250]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), 2% tax rate phase-out add-back (USD) by annualized salary (more than - less than or equal to); printed in IP 2026(1) Circular CT PDF p.28. 11 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |
| Withholding table d code a d f | [[FACT:ct.wh.table_d.code_a_d_f=0-105,000: 0; 105,000-110,000: 25; 110,000-115,000: 50; 115,000-120,000: 75; 120,000-125,000: 100; 125,000-130,000: 125; 130,000-135,000: 150; 135,000-140,000: 175; 140,000-145,000: 200; 145,000-150,000: 225; 150,000-200,000: 250; 200,000-205,000: 340; 205,000-210,000: 430; 210,000-215,000: 520; 215,000-220,000: 610; 220,000-225,000: 700; 225,000-230,000: 790; 230,000-235,000: 880; 235,000-240,000: 970; 240,000-245,000: 1,060; 245,000-250,000: 1,150; 250,000-255,000: 1,240; 255,000-260,000: 1,330; 260,000-265,000: 1,420; 265,000-270,000: 1,510; 270,000-275,000: 1,600; 275,000-280,000: 1,690; 280,000-285,000: 1,780; 285,000-290,000: 1,870; 290,000-295,000: 1,960; 295,000-300,000: 2,050; 300,000-305,000: 2,140; 305,000-310,000: 2,230; 310,000-315,000: 2,320; 315,000-320,000: 2,410; 320,000-325,000: 2,500; 325,000-330,000: 2,590; 330,000-335,000: 2,680; 335,000-340,000: 2,770; 340,000-345,000: 2,860; 345,000-500,000: 2,950; 500,000-505,000: 3,000; 505,000-510,000: 3,050; 510,000-515,000: 3,100; 515,000-520,000: 3,150; 520,000-525,000: 3,200; 525,000-530,000: 3,250; 530,000-535,000: 3,300; 535,000-540,000: 3,350; over 540,000: 3,400]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), tax recapture amount (USD) by annualized salary (more than - less than or equal to); printed in IP 2026(1) Circular CT PDF p.29. 50 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |
| Withholding table d code b | [[FACT:ct.wh.table_d.code_b=0-168,000: 0; 168,000-176,000: 40; 176,000-184,000: 80; 184,000-192,000: 120; 192,000-200,000: 160; 200,000-208,000: 200; 208,000-216,000: 240; 216,000-224,000: 280; 224,000-232,000: 320; 232,000-240,000: 360; 240,000-320,000: 400; 320,000-328,000: 540; 328,000-336,000: 680; 336,000-344,000: 820; 344,000-352,000: 960; 352,000-360,000: 1,100; 360,000-368,000: 1,240; 368,000-376,000: 1,380; 376,000-384,000: 1,520; 384,000-392,000: 1,660; 392,000-400,000: 1,800; 400,000-408,000: 1,940; 408,000-416,000: 2,080; 416,000-424,000: 2,220; 424,000-432,000: 2,360; 432,000-440,000: 2,500; 440,000-448,000: 2,640; 448,000-456,000: 2,780; 456,000-464,000: 2,920; 464,000-472,000: 3,060; 472,000-480,000: 3,200; 480,000-488,000: 3,340; 488,000-496,000: 3,480; 496,000-504,000: 3,620; 504,000-512,000: 3,760; 512,000-520,000: 3,900; 520,000-528,000: 4,040; 528,000-536,000: 4,180; 536,000-544,000: 4,320; 544,000-552,000: 4,460; 552,000-800,000: 4,600; 800,000-808,000: 4,680; 808,000-816,000: 4,760; 816,000-824,000: 4,840; 824,000-832,000: 4,920; 832,000-840,000: 5,000; 840,000-848,000: 5,080; 848,000-856,000: 5,160; 856,000-864,000: 5,240; over 864,000: 5,320]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), tax recapture amount (USD) by annualized salary (more than - less than or equal to); printed in IP 2026(1) Circular CT PDF p.29. 50 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |
| Withholding table d code c | [[FACT:ct.wh.table_d.code_c=0-210,000: 0; 210,000-220,000: 50; 220,000-230,000: 100; 230,000-240,000: 150; 240,000-250,000: 200; 250,000-260,000: 250; 260,000-270,000: 300; 270,000-280,000: 350; 280,000-290,000: 400; 290,000-300,000: 450; 300,000-400,000: 500; 400,000-410,000: 680; 410,000-420,000: 860; 420,000-430,000: 1,040; 430,000-440,000: 1,220; 440,000-450,000: 1,400; 450,000-460,000: 1,580; 460,000-470,000: 1,760; 470,000-480,000: 1,940; 480,000-490,000: 2,120; 490,000-500,000: 2,300; 500,000-510,000: 2,480; 510,000-520,000: 2,660; 520,000-530,000: 2,840; 530,000-540,000: 3,020; 540,000-550,000: 3,200; 550,000-560,000: 3,380; 560,000-570,000: 3,560; 570,000-580,000: 3,740; 580,000-590,000: 3,920; 590,000-600,000: 4,100; 600,000-610,000: 4,280; 610,000-620,000: 4,460; 620,000-630,000: 4,640; 630,000-640,000: 4,820; 640,000-650,000: 5,000; 650,000-660,000: 5,180; 660,000-670,000: 5,360; 670,000-680,000: 5,540; 680,000-690,000: 5,720; 690,000-1,000,000: 5,900; 1,000,000-1,010,000: 6,000; 1,010,000-1,020,000: 6,100; 1,020,000-1,030,000: 6,200; 1,030,000-1,040,000: 6,300; 1,040,000-1,050,000: 6,400; 1,050,000-1,060,000: 6,500; 1,060,000-1,070,000: 6,600; 1,070,000-1,080,000: 6,700; over 1,080,000: 6,800]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), tax recapture amount (USD) by annualized salary (more than - less than or equal to); printed in IP 2026(1) Circular CT PDF p.29. 50 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |
| Withholding table e code a | [[FACT:ct.wh.table_e.code_a=12,000-15,000: 0.75; 15,000-15,500: 0.70; 15,500-16,000: 0.65; 16,000-16,500: 0.60; 16,500-17,000: 0.55; 17,000-17,500: 0.50; 17,500-18,000: 0.45; 18,000-18,500: 0.40; 18,500-20,000: 0.35; 20,000-20,500: 0.30; 20,500-21,000: 0.25; 21,000-21,500: 0.20; 21,500-25,000: 0.15; 25,000-25,500: 0.14; 25,500-26,000: 0.13; 26,000-26,500: 0.12; 26,500-27,000: 0.11; 27,000-48,000: 0.10; 48,000-48,500: 0.09; 48,500-49,000: 0.08; 49,000-49,500: 0.07; 49,500-50,000: 0.06; 50,000-50,500: 0.05; 50,500-51,000: 0.04; 51,000-51,500: 0.03; 51,500-52,000: 0.02; 52,000-52,500: 0.01; over 52,500: 0.00]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), personal tax credit decimal by annualized salary (more than - less than or equal to); code D: 0.00; printed in IP 2026(1) Circular CT PDF p.30. 28 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |
| Withholding table e code b | [[FACT:ct.wh.table_e.code_b=19,000-24,000: 0.75; 24,000-24,500: 0.70; 24,500-25,000: 0.65; 25,000-25,500: 0.60; 25,500-26,000: 0.55; 26,000-26,500: 0.50; 26,500-27,000: 0.45; 27,000-27,500: 0.40; 27,500-34,000: 0.35; 34,000-34,500: 0.30; 34,500-35,000: 0.25; 35,000-35,500: 0.20; 35,500-44,000: 0.15; 44,000-44,500: 0.14; 44,500-45,000: 0.13; 45,000-45,500: 0.12; 45,500-46,000: 0.11; 46,000-74,000: 0.10; 74,000-74,500: 0.09; 74,500-75,000: 0.08; 75,000-75,500: 0.07; 75,500-76,000: 0.06; 76,000-76,500: 0.05; 76,500-77,000: 0.04; 77,000-77,500: 0.03; 77,500-78,000: 0.02; 78,000-78,500: 0.01; over 78,500: 0.00]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), personal tax credit decimal by annualized salary (more than - less than or equal to); code D: 0.00; printed in IP 2026(1) Circular CT PDF p.30. 28 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |
| Withholding table e code c | [[FACT:ct.wh.table_e.code_c=24,000-30,000: 0.75; 30,000-30,500: 0.70; 30,500-31,000: 0.65; 31,000-31,500: 0.60; 31,500-32,000: 0.55; 32,000-32,500: 0.50; 32,500-33,000: 0.45; 33,000-33,500: 0.40; 33,500-40,000: 0.35; 40,000-40,500: 0.30; 40,500-41,000: 0.25; 41,000-41,500: 0.20; 41,500-50,000: 0.15; 50,000-50,500: 0.14; 50,500-51,000: 0.13; 51,000-51,500: 0.12; 51,500-52,000: 0.11; 52,000-96,000: 0.10; 96,000-96,500: 0.09; 96,500-97,000: 0.08; 97,000-97,500: 0.07; 97,500-98,000: 0.06; 98,000-98,500: 0.05; 98,500-99,000: 0.04; 99,000-99,500: 0.03; 99,500-100,000: 0.02; 100,000-100,500: 0.01; over 100,500: 0.00]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), personal tax credit decimal by annualized salary (more than - less than or equal to); code D: 0.00; printed in IP 2026(1) Circular CT PDF p.30. 28 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |
| Withholding table e code f | [[FACT:ct.wh.table_e.code_f=15,000-18,800: 0.75; 18,800-19,300: 0.70; 19,300-19,800: 0.65; 19,800-20,300: 0.60; 20,300-20,800: 0.55; 20,800-21,300: 0.50; 21,300-21,800: 0.45; 21,800-22,300: 0.40; 22,300-25,000: 0.35; 25,000-25,500: 0.30; 25,500-26,000: 0.25; 26,000-26,500: 0.20; 26,500-31,300: 0.15; 31,300-31,800: 0.14; 31,800-32,300: 0.13; 32,300-32,800: 0.12; 32,800-33,300: 0.11; 33,300-60,000: 0.10; 60,000-60,500: 0.09; 60,500-61,000: 0.08; 61,000-61,500: 0.07; 61,500-62,000: 0.06; 62,000-62,500: 0.05; 62,500-63,000: 0.04; 63,000-63,500: 0.03; 63,500-64,000: 0.02; 64,000-64,500: 0.01; over 64,500: 0.00]] | 2026-01-01 to 2026-12-31 |  | S11 | TPG-211, 2026 Withholding Calculation Rules (Rev. 12/25), personal tax credit decimal by annualized salary (more than - less than or equal to); code D: 0.00; printed in IP 2026(1) Circular CT PDF p.30. 28 rows, each lower bound equals the previous upper bound, last row open-ended. Use: TPG-211 Steps 8 (Table C), 9 (Table D), 11-12 (Table E: withholding x (1.00 - decimal)). |

Withholding engine method (configuration decision of 2026-11-02): the DRS per-period tables of IP 2026(1) up to each table maximum, the TPG-211 rules above it; see the method choice in CT.2.

## CT.2b Non-resident regime and reciprocity

Rules: [[FACT:ct.nonres.rules=residents: all wages, prorated where another qualifying jurisdiction requires withholding; nonresidents: CT-service wages via CT-W4NA or records, else all wages; 15-day rule; no reciprocity; convenience-of-employer rule from 2019 (reciprocal)]].

**Resident / non-resident matrix (Connecticut income tax)**

| Income type | Resident | Non-resident |
|---|---|---|
| Regular salary | Rules or tables (CT.2) on all wages, prorated where another qualifying jurisdiction requires withholding | Rules or tables on Connecticut-service wages (CT-W4NA or records), otherwise all wages; day threshold and convenience rule in Annex MULTI |
| Annual bonus / supplemental pay | Aggregate only (no flat rate) | Same, on the Connecticut portion |
| Severance | Aggregate (federal wage definition) | Same, on the Connecticut portion |
| Equity | Aggregate; federal classification of equity income in Annex FED (FED.2b) | Same, on the Connecticut portion |
| Benefits in kind | Federal wage definition; Connecticut departures open (CT.8) | Same, on the Connecticut portion |
| Contractor pay | Out of scope | Out of scope |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Non-resident rules | [[FACT:ct.nonres.rules=residents: all wages, prorated where another qualifying jurisdiction requires withholding; nonresidents: CT-service wages via CT-W4NA or records, else all wages; 15-day rule; no reciprocity; convenience-of-employer rule from 2019 (reciprocal)]] | from 2026-01-01 |  | S11 |  |

## CT.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in CT.2.

## CT.3 Social insurance: unemployment, disability, paid leave and payroll levies

Employer UI on wages up to USD [[FACT:ct.sui.wage_base=27,000]] plus the fund-solvency rate ([[FACT:ct.sui.fund_solvency.rate=1]] %); no employee UI ([[FACT:ct.sui.employee.rate=0]] %). Connecticut Paid Leave: employee [[FACT:ct.pfml.employee.rate=0.5]] % on wages up to USD [[FACT:ct.pfml.wage_cap=184,500]]; coverage [[FACT:ct.pfml.multistate=employee for whom employer pays CT UI and CT payroll taxes is working in CT (follows UI localization)]]. No SDI or TDI.

```
ct_pfml = min(period_CTPL_wages, max(0, ct_pfml_wage_cap - ytd_CTPL_wages)) x ct_pfml_employee_rate
```

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI wage base | USD [[FACT:ct.sui.wage_base=27,000]] | 2026-01-01 to 2026-12-31 |  | S12 |  |
| SUI new employer rate | [[FACT:ct.sui.new_employer.rate=1.9]] % | 2026-01-01 to 2026-12-31 |  | S12 |  |
| SUI employer rate min | [[FACT:ct.sui.employer.rate.min=0.1]] % | 2026-01-01 to 2026-12-31 |  | S12 | Charged 0.1-[[FACT:ct.sui.employer.rate.max=8.9]]% plus [[FACT:ct.sui.fund_solvency.rate=1.0]]% fund solvency. |
| SUI employer rate max | [[FACT:ct.sui.employer.rate.max=8.9]] % | 2026-01-01 to 2026-12-31 |  | S12 |  |
| SUI fund solvency rate | [[FACT:ct.sui.fund_solvency.rate=1]] % | 2026-01-01 to 2026-12-31 |  | S12 |  |
| SUI employee rate | [[FACT:ct.sui.employee.rate=0]] % | from 2026-01-01 |  | S13 |  |
| SUI wage base other state credit | [[FACT:ct.sui.wage_base.other_state_credit=True]] | from 2026-01-01 |  | S14 | 31-222(b); each concurrent employer reports to the max; predecessor wages only for successor. |
| PFML employee rate | [[FACT:ct.pfml.employee.rate=0.5]] % | 2026-01-01 to 2026-12-31 |  | S15 | Statutory cap [[FACT:ct.pfml.employee.rate=0.5]] %; subject earnings = UI total wages excl. FICA-excluded benefits; each employer withholds to cap separately; no employer share. |
| PFML wage cap | USD [[FACT:ct.pfml.wage_cap=184,500]] | 2026-01-01 to 2026-12-31 |  | S15 | = SS wage base. |
| PFML benefit weekly max | USD [[FACT:ct.pfml.benefit.weekly_max=1,016.40]] | 2026-01-01 to 2026-12-31 |  | S16 | 60 x [[FACT:ct.minwage.hourly=16.94]]; 2027 60 x [[FACT:ct.minwage.hourly=17.48]] = 1,048.80. Paid by the Authority, not payroll. |
| PFML multistate | [[FACT:ct.pfml.multistate=employee for whom employer pays CT UI and CT payroll taxes is working in CT (follows UI localization)]] | from 2026-01-01 |  | S17 |  |
| PFML wages FICA basis | [[FACT:ct.pfml.wages.fica_basis=For FICA-covered employees, CTPL wages exclude any benefit excluded from FICA taxable wages (CTPL base follows FICA wages: s.125 excluded, 401(k) deferrals included); 0.5% up to the Social Security contribution and benefit base]] | from 2026-10-05 |  | S18 |  |

Not configured in this release [[GAP:RQ-499]]: SUI wage base next year: not established from an official source.

## CT.4 Pay statement

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Payslip items | [[FACT:ct.payslip.items=hours worked, gross pay with straight time and overtime separately, itemised deductions, net pay (hours/split not for OT-exempt); electronic only with explicit consent and secure access]] | from 2026-01-01 |  | S19 |  |
| Payslip pay code guide url employer threshold | [[FACT:ct.payslip.pay_code_guide_url.employer_threshold=100]] employees | from 2026-10-01 |  | S20 | PA 26-12 s.38 (31-13a(c)): guide (>=10 codes, en/es/other common languages, dispute contact) URL on every pay record and at hire. Consolidated 31-13a text lags (F18): cite PA 26-12. |

## CT.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Report withholding remitter class | [[FACT:ct.report.wh.remitter_class=weekly if lookback > 10,000 (Wednesday after Sat-Fri week); monthly 2,000-10,000 (15th); quarterly <= 2,000 (last day of month after quarter); all via myconneCT EFT]] | from 2026-01-01 |  | S21 |  |
| Report withholding ct941 | [[FACT:ct.report.wh.ct941=quarterly due 4/30, 7/31, 10/31, 1/31 even if zero; annual status on request by 31 March]] | from 2026-01-01 |  | S21 |  |
| Report W-2 ctw3 | [[FACT:ct.report.w2.ctw3=CT-W3 + all W-2s by 31 January via myconneCT (key-and-send, EFW2 upload or DRS CSV); box 15 CT + registration number; 5 per return up to 2,000]] | from 2026-01-01 |  | S21 |  |
| Report SUI quarterly | [[FACT:ct.report.sui.quarterly=ReEmployCT electronic (manual, upload, TPA, FSET); due 4/30, 7/31, 10/31, 1/31; 276-char fixed-length S/T records; zero report required; late file 25, late pay greater of 50 or 10%]] | from 2026-01-01 |  | S22 | Optional occupation/hours/worksite ZIP from Q3 2026 (31-225a(j)(1)(B)) have no positions in the 2022 spec. |
| Report SUI record length | [[FACT:ct.report.sui.record_length=276]] characters | from 2022-01-01 |  | S22 |  |
| Newhire report days | [[FACT:ct.newhire.report_days=20]] days | from 2026-01-01 |  | S23 | Rehire = separated > 60 days; copy of CT-W4, DOL website or fax. |
| Report PFML quarterly | [[FACT:ct.report.pfml.quarterly=My Account portal or batch SFTP XML/CSV; due last day of the quarter, no penalty if paid by last day of following month]] | from 2026-01-01 |  | S24 |  |
| Report PFML file spec | [[FACT:ct.report.pfml.file_spec=CT Paid Leave File Specification Toolkit v2.1.9 (2026-10-05): batch enrollment and quarterly return files in XML (XSD published) or CSV via SFTP; CSV return file under 5 MB and under 5,000 return records; underscore-node file naming; acknowledgement file with E (error, record rejected) / W (warning, accepted) levels]] | from 2026-10-05 |  | S18 |  |

Not configured in this release [[GAP:RQ-498]]: Report SUI optional fields layout: not established from an official source.

## CT.6 Leave

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Leave sick coverage threshold employees | [[FACT:ct.leave.sick.coverage_threshold_employees=11]] employees | 2026-01-01 to 2026-12-31 |  | S25 | CT headcount for week containing 1 Jan; [[FACT:ct.leave.sick.coverage_threshold_employees=1]]+ from 2027-01-01. |
| Leave sick coverage threshold employees | [[FACT:ct.leave.sick.coverage_threshold_employees=1]] employees | from 2027-01-01 |  | S25 |  |
| Leave sick accrual hours worked per hour | [[FACT:ct.leave.sick.accrual.hours_worked_per_hour=30]] hours | from 2026-01-01 |  | S25 | Cap 40 h/yr; carryover 40; use from day 120; pay greater of normal wage or MW; no payout; seasonal <= 120 days excluded. |
| Leave sick cap hours | [[FACT:ct.leave.sick.cap_hours=40]] hours | from 2026-01-01 |  | S25 |  |
| Leave sick use after days | [[FACT:ct.leave.sick.use_after_days=120]] days | from 2026-01-01 |  | S25 |  |

Not configured in this release [[GAP:RQ-501]]: Leave sick multistate: not established from an official source.

## CT.7 Termination and final pay

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Final pay rule | [[FACT:ct.final_pay.rule=discharge: business day after; quit/layoff: next regular payday]] | from 2026-01-01 |  | S26 | Vacation/PTO payout only if policy/CBA provides (31-76k). Double damages for unpaid wages from 2027-01-01 (PA 26-12 s.56). |
| Separation notice | [[FACT:ct.separation_notice=UC-21 Separation Packet with UC-21A to every separating employee]] | from 2026-01-01 |  | S13 |  |

## CT.8 Benefits in kind and taxable wages

Withholding follows the federal wage definition; no Connecticut departure was found for 401(k), cafeteria-plan, HSA, transit or group-term-life amounts (medium confidence; gap below). Paid Leave wages: [[FACT:ct.pfml.wages.fica_basis=For FICA-covered employees, CTPL wages exclude any benefit excluded from FICA taxable wages (CTPL base follows FICA wages: s.125 excluded, 401(k) deferrals included); 0.5% up to the Social Security contribution and benefit base]]. New 2026 subtractions operate at assessment level, not in withholding.

Not configured in this release [[GAP:RQ-500]]: PIT departures from federal: not established from an official source.

## CT.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Deductions rule | [[FACT:ct.deductions.rule=only if required by law, written authorisation on a Labor Commissioner-approved form, medical/hospital without employer benefit, auto-enrolment retirement/CRSP, or another state withholding requirement]] | from 2026-01-01 |  | S27 |  |
| Garnishment creditor max percent | [[FACT:ct.garn.creditor.max_percent=25]] % | from 2026-01-01 |  | S28 | 52-361a: lesser of [[FACT:ct.garn.creditor.max_percent=25]] % of disposable earnings or excess over 40 x higher of federal/CT MW; 20-day stay; one execution at a time. |
| Garnishment creditor weekly protected | USD [[FACT:ct.garn.creditor.weekly_protected=677.60]] | 2026-01-01 to 2026-12-31 |  | S28 | 40 x [[FACT:ct.minwage.hourly=16.94]]; 2027 699.20. |
| Garnishment child support remit business days | [[FACT:ct.garn.child_support.remit_business_days=7]] business days | from 2026-01-01 |  | S29 | 52-362: exempt greater of 85% of first 145/week disposable or CCPA amount; start first period after 14 days; SDU pro-rates, current support first. |

Not configured in this release [[GAP:RQ-502]]: Garnishment employer fee: not established from an official source.

## CT.10 Collective agreements and prevailing wage

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Prevailing wage threshold new construction | USD [[FACT:ct.prevailing_wage.threshold.new_construction=1,000,000]] | from 2026-01-01 |  | S30 | Remodeling/repair 100,000; weekly certified payroll to contracting agency (failure class D felony). |
| Prevailing wage threshold remodel | USD [[FACT:ct.prevailing_wage.threshold.remodel=100,000]] | from 2026-01-01 |  | S30 |  |

## CT.11 Indexation

One index drives both the minimum wage and the UI wage base: the Employment Cost Index (wages and salaries, all civilian workers) for the twelve months to 30 June ([[FACT:ct.minwage.indexation=every 1 January by ECI (wages and salaries, all civilian workers) for 12 months to preceding 30 June, nearest cent; announced by 15 October; never below federal MW + 0.5%]]). The minimum wage is rounded to the cent and the UI base to a round step stated in the source.

## CT.12 Payroll data protection and records

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Records retention years | [[FACT:ct.records.retention_years=3]] years | from 2026-01-01 |  | S19 | 31-66, at place of employment. |

## CT.13 Live legal change

In force in 2026: paid sick leave for employers with [[FACT:ct.leave.sick.coverage_threshold_employees=11]] or more employees; the pay-code guide duty (CT.4); the minor-league baseball exclusion and the end of the cannabis tip credit; optional UI report fields. Enacted for 2027: paid sick leave from [[FACT:ct.leave.sick.coverage_threshold_employees=1]] employee; minimum wage USD [[FACT:ct.minwage.hourly=17.48]]; double damages; UI shared-work non-charging; prevailing-wage records. The lump-sum pension withholding suspension ends with 2026 (CT.2). Public Acts known only from legislative summaries are listed as a gap below.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Oracle ip2026 1 ex8 withheld allocated | USD [[FACT:ct.oracle.ip2026_1.ex8.withheld_allocated=10.59]] | 2026-01-01 to 2026-12-31 |  | S11 | Example 8: table amount [[FACT:ct.oracle.ip2026_1.ex8.withholding=17.65]] (weekly band 692-701, code F) x 60% CT-W4NA share = [[FACT:ct.oracle.ip2026_1.ex8.withheld_allocated=10.59]]. |
| Oracle ip2026 1 ex9 week1 allocated | USD [[FACT:ct.oracle.ip2026_1.ex9.week1_allocated=15.99]] | 2026-01-01 to 2026-12-31 |  | S11 | Example 9: table amount [[FACT:ct.oracle.ip2026_1.ex9.withholding=39.97]] (weekly band 990-1000, code A) x 40% of days in CT = [[FACT:ct.oracle.ip2026_1.ex9.week1_allocated=15.99]]. |

Not configured in this release [[GAP:RQ-503]]: Live public act texts: not established from an official source.

## CT.14 Authority worked examples (oracle values)

Oracle values from the Department of Revenue Services informational publication IP 2026(1), examples 8 to 10 (table method), reproduced from the keyed per-period tables (CT.2).

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Oracle ip2026 1 ex8 withholding | USD [[FACT:ct.oracle.ip2026_1.ex8.withholding=17.65]] | 2026-01-01 to 2026-12-31 |  | S8 | IP 2026(1) Ex. 8: code F, 700 weekly (table-based). TPG-211 rules give 17.79 (residual 0.14). The weekly table band 692-701, code F, gives [[FACT:ct.oracle.ip2026_1.ex8.withholding=17.65]]. |
| Oracle ip2026 1 ex9 withholding | USD [[FACT:ct.oracle.ip2026_1.ex9.withholding=39.97]] | 2026-01-01 to 2026-12-31 |  | S8 | Ex. 9: code A, 1,000 weekly (tables). Rules give 39.86 (residual 0.11). The weekly table band 990-1000, code A, gives [[FACT:ct.oracle.ip2026_1.ex9.withholding=39.97]]. |
| Oracle ip2026 1 ex10 withholding | USD [[FACT:ct.oracle.ip2026_1.ex10.withholding=78.82]] | 2026-01-01 to 2026-12-31 |  | S8 | Ex. 10: code B, 2,300 biweekly (tables). Rules give 79.30 (residual 0.48). The biweekly table band 2269-2307, code B, gives [[FACT:ct.oracle.ip2026_1.ex10.withholding=78.82]]. |

## CT.15 Special populations

- Domestic workers: minimum wage and overtime exclude private-home domestic service except where FLSA covers it; UI above the quarterly cash-wage threshold; withholding voluntary (CT-941 HHE, CT-W3 HHE).
- Agricultural workers: withhold where federal withholding applies; annual CT-941 option.
- Minors: minor rate USD [[FACT:ct.minwage.minor.hourly=14.40]] in 2026; newspaper carriers under 18 excluded from UI.
- Tipped employees: employer share USD [[FACT:ct.tipped.employer_share.hotel_restaurant=6.38]] (hotel and restaurant) and USD [[FACT:ct.tipped.employer_share.bartender=8.23]] (bartenders); no cannabis tip credit.
- Clergy: UI excludes churches and ministers; withholding follows the federal definition.
- Students: UI exclusions; resident assistants excluded from the minimum wage.
- Non-resident aliens and statutory employees: no Connecticut rule beyond the federal one.
- Government: State and municipal service UI-covered; Paid Leave excludes governments unless they opt in.
- Military: non-resident military pay is not Connecticut wages; military spouses exempt on CT-W4.
- Seasonal employees: excluded from sick leave.

Not configured in this release [[GAP:RQ-516]]: The coverage thresholds that apply to these populations (quarterly cash-wage and headcount thresholds for UI coverage of domestic, agricultural and non-profit employment) are cited by statute only and are not established as values; the engine must not hard-code them until they are established.

## CT.16 Language

The pay-code guide must be offered in English, Spanish and other common languages; the 31-57w(b) sick-leave notice in English and Spanish. The payslip is in English.

## CT.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | Governor's press release: minimum wage [[FACT:ct.minwage.hourly=16.94]] USD from 2026-01-01 (ECI +3.6%) | Full release | Office of the Governor of Connecticut (announcing the Labor Commissioner's … |
| S2 | Governor's press release: minimum wage [[FACT:ct.minwage.hourly=17.48]] USD from 2027-01-01 (ECI indexation) | Full release | Office of the Governor of Connecticut (announcing the Labor Commissioner's … |
| S3 | Conn. Gen. Stat. 31-58(i) Minimum fair wage (chapter 558) | Sec. 31-58(i)(1)-(5) | Connecticut General Assembly |
| S4 | Conn. Gen. Stat. 31-76b to 31-76c overtime | Sec. 31-76b(1); 31-76c; 31-76e | Connecticut General Assembly |
| S5 | Conn. Gen. Stat. 31-71b, 31-71i, 31-71k pay frequency, pay day and method | Sec. 31-71b(a)-(b); 31-71i; 31-71k(b) | Connecticut General Assembly |
| S6 | Conn. Gen. Stat. 31-60(b)-(d) tip credit and board allowances | Sec. 31-60(b) and (d)(3) | Connecticut General Assembly |
| S7 | TPG-211 2026 Withholding Calculation Rules (Rev. 12/25) | Steps 1-16; Tables A-E | Connecticut Department of Revenue Services |
| S8 | IP 2026(1) Circular CT: CT-W4 codes and default withholding | pp. 10-11; Form CT-W4 (Rev. 12/25) p. 29 | Connecticut Department of Revenue Services |
| S9 | IP 2026(1) Circular CT: supplemental compensation | p. 12 Supplemental Compensation; Examples 11-12 | Connecticut Department of Revenue Services |
| S10 | DRS IP 2026(1) Connecticut Employer's Tax Guide (Circular CT): State of Connecticut 2026 Withholding Tables (Effective January 1, 2026), weekly, bi-weekly, … | pp. 31-38 (weekly 31-32, bi-weekly 33-34, semi-monthly 35-36, monthly 37-38); Examples 8-10 pp. 11-12 | Connecticut Department of Revenue Services |
| S11 | DRS Informational Publication 2026(1) Connecticut Employer's Tax Guide (Circular CT) | Q5 (gross CT wages); 'Residents working outside CT' (proration among qualifying jurisdictions); '15-Day Rule for Nonresident Employees' p.8; CT-W4NA … | Connecticut Department of Revenue Services |
| S12 | CTDOL Information on Unemployment Tax Rate for Calendar Year 2026 | Full page; PA 21-200, PA 22-67 | Connecticut Department of Labor |
| S13 | CT DOL Employer's Guide to Unemployment Compensation (updated 2026-04-23) | pp. 17, 20-21 (Taxable wage base; Filing of UI Tax and Wage Reports; due dates; penalties); Separation Packet UC-21/UC-21A | Connecticut Department of Labor |
| S14 | Conn. Gen. Stat. 31-222(b) UI taxable wages (indexed wage base; other-state wage credit) | Sec. 31-222(b)(1)(A)(v)-(vi) | Connecticut General Assembly |
| S15 | Connecticut Paid Leave employee contribution | Conn. Gen. Stat. 31-49e | CT official authority |
| S16 | Conn. Gen. Stat. 31-49e, 31-49g, 31-49o, 31-49q Paid Family and Medical Leave (CT Paid Leave) | Sec. 31-49e(4)(7)(8)(17); 31-49g; 31-49o(c); 31-49q | Connecticut General Assembly |
| S17 | CT Paid Leave Authority Guide for Employers (fact sheet updated October 2024) | Eligibility footnote | Connecticut Paid Leave Authority |
| S18 | CT Paid Leave File Specification Toolkit version 2.1.9 (10/5/26) | Latest updates; file naming convention; XML/CSV Enrollment and Return formats; acknowledgement file; versioning | Connecticut Paid Leave Authority |
| S19 | Conn. Gen. Stat. 31-13a(b) and 31-66 electronic statements and record retention | Sec. 31-13a(a)-(b) (ch. 557); 31-66 (ch. 558) | Connecticut General Assembly |
| S20 | Public Act 26-12 (Sub. HB 5003) omnibus workforce act - payroll-relevant sections | Sec. 6 (21a-421d cannabis), 38 (31-13a(c)), 40 (31-58(e)), 54 (31-53), 55-56 (31-72) | Connecticut General Assembly |
| S21 | IP 2026(1) Circular CT: remitter classes, CT-941, CT-W3, W-2 filing, EFT | pp. 4-6 and 12-14 | Connecticut Department of Revenue Services |
| S22 | CT DOL ReEmployCT Tax and Wage Report upload file format (276-character fixed length) | S record and T record layouts (4 pp.) | Connecticut Department of Labor |
| S23 | Conn. Gen. Stat. 31-254(b) state directory of new hires | Sec. 31-254(b) | Connecticut General Assembly |
| S24 | CT Paid Leave Authority: contributions and remittance pages (2026) | Contributions; Remit Contributions; Batch Process; I am an Employer | Connecticut Paid Leave Authority |
| S25 | Conn. Gen. Stat. 31-57r to 31-57s paid sick leave (as amended by P.A. 23-101 and P.A. 24-8) | Sec. 31-57r(2)(3)(11); 31-57s(a)-(f) and termination subsection | Connecticut General Assembly |
| S26 | Conn. Gen. Stat. 31-71c and 31-76k final pay and accrued fringe benefits | Sec. 31-71c(a)-(c); 31-76k | Connecticut General Assembly |
| S27 | Conn. Gen. Stat. 31-71e withholding of part of wages | Sec. 31-71e(1)-(5) | Connecticut General Assembly |
| S28 | Conn. Gen. Stat. 52-361a wage execution (creditor garnishment) | Sec. 52-361a(d)-(f) | Connecticut General Assembly |
| S29 | Conn. Gen. Stat. 52-362 income withholding for support | Sec. 52-362(e)(f) and allocation clause | Connecticut General Assembly |
| S30 | Conn. Gen. Stat. 31-53(f)-(h) prevailing wage certified payroll and thresholds | Sec. 31-53(f)(h) | Connecticut General Assembly |
