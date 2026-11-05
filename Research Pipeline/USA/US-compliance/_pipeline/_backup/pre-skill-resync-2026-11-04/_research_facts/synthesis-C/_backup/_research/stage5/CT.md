# Stage 5 — Connecticut (CT): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-26 (sealed at attempt 6; part 5 closed on US-CTP10-001).
Budget declared: 60 fetches / 2 h. Used: 24 fetches (curl, including Wayback) and 6 web searches (used as leads only), about 55 min. I stopped well before the 75% mark.
**Access note:** the VPN was **off** (ipinfo: Brazil exit). portal.ct.gov and ctpaidleave.org answered plain curl with HTTP 200. cga.ct.gov and prdext2.cga.ct.gov refused the connection (curl 000). Every statute chapter and the 2026 public act were therefore read from **Wayback 2026 captures** of the official cga.ct.gov files (capture timestamps are in the register rows).
Register shard: `00-official-sources/_register-shards/S5-CT.csv` (35 rows, US-CTS5-001..035, all active). Sources: `00-official-sources/ccg-sources/CT/` (17 files, 3.8 MB, no file > 5 MB). The chapter 557 Wayback copy and IP 2026(1) already held in `pdfs/CT/` were reused, not re-fetched.
**Active rows reused:** US-CTP10-001 (IP 2026(1), residents/nonresidents/15-day rule), US-CTP9V-001 and US-CTP7-002 (UI 2026 rates), US-CTP7-001 (CTPL 0.5%), US-CT-P5-1-005 (31-13a), US-CT-P5-1-006 (31-53), US-CTL-001/-002 (notices), US-CTP9W-001/-002 (no other DRS wage levy), US-CTP9L-001 (posters), US-CT-P5-2-002 (TPA).
**Rows to close at synthesis (the shard row now holds a local file):**
- US-CT-P5-1-002 (MANUAL, UI guide) is replaced by US-CTS5-031 (`supersedes` is set).
- US-CT-WH-001 (TPG-211, no local file) has its local copy in US-CTS5-010. Same edition, so `supersedes` is left empty.
- US-CT-WH-002 (snippet-based IP 2026(1) row) should be closed in favour of US-CTS5-011/-012/-013, which cite the held PDF (md5 a64b2bbb…).
- US-CT-PL-001 is succeeded by US-CTS5-022 (`supersedes` is set).
- US-CT-P5-1-006 is succeeded by US-CTS5-023 (`supersedes` is set).

---

## 1. labour_code
- **Minimum wage.** The statutory floor has been USD 15.00 since 2023-06-01. From then on it is indexed every 1 January by the ECI (wages and salaries, all civilian workers) over the 12 months to the preceding 30 June, rounded to the nearest cent. The Labor Commissioner announces it by 15 October. It is never lower than the federal minimum + 0.5% [US-CTS5-001, A.1].
  - **2026: USD 16.94/h** from 2026-01-01 [US-CTS5-008]. Derivation: 16.35 × 1.036 = 16.9386, which rounds to 16.94.
  - **2027: USD 17.48/h** from 2027-01-01, already announced [US-CTS5-009]. Derivation: 16.94 × 1.032 = 17.48208, which rounds to 17.48.
  - Both derivations were run in Python with Decimal ROUND_HALF_UP. Confidence: high.
- **Local minimum wages.** None. CT municipalities have only the powers expressly conferred on them (US-CT-P5-2-001, tier B lead). No municipal wage ordinance was located; see US-MQ-26 part 2.
- **Overtime.** 1.5× the regular rate above 40 hours in a workweek. There is no daily overtime. The regular rate exclusions are listed in 31-76b(1) [US-CTS5-003, A.1]. The CT Supreme Court allows the fluctuating-workweek method, except for certain delivery drivers and sales merchandisers (note of decisions under 31-76c, 326 C. 651).
- **Pay frequency and timing.**
  - Pay weekly or biweekly on a regular pay day designated in advance.
  - The pay period must end no more than 8 days before the pay day.
  - A pay day falling on a non-work day moves to the preceding work day.
  - The Commissioner may waive this to a less frequent schedule, but never less than monthly [US-CTS5-004, A.1].
- **Method of payment** [US-CTS5-004]:
  - cash or negotiable check;
  - direct deposit, only at the employee's written or electronic request;
  - payroll card, only where direct deposit and check are both offered and the employee authorises the card voluntarily, in writing or electronically (31-71k).
- **Hiring notice.** A written notice of rate, hours and pay schedule is due at hire. Domestic workers get an extended notice [US-CTS5-007].
- **Tip credit.** The employer's share is a fixed USD 6.38/h (hotel and restaurant, non-bartenders) and USD 8.23/h (bartenders) [US-CTS5-002].
  - In 2026 that gives a maximum tip credit of 10.56 and 8.71. In 2027 it is 11.10 and 9.25 (derived).
  - Other industries: at most USD 0.35/h.
  - Meal allowances: USD 0.85 per full meal, USD 0.45 per light meal.
  - From 2026-10-01 there is no tip credit for cannabis establishments (PA 26-12 sec. 6, OLR summary) [US-CTS5-028/-029].

## 2. income_tax
- **Method: TPG-211 2026 Withholding Calculation Rules (Rev. 12/25)**, local copy [US-CTS5-010, A.2]. The 2026 rules and tables are unchanged from 2025. There is no percentage method: the employer uses either the rules or the tables.
- **The 16-step calculation:**
  1. Annualise the wages.
  2. Subtract the Table A exemption for the code: A 12,000; B 19,000; C 24,000; F 15,000; D 0. Each phases out by USD 1,000 per USD 1,000 of income.
  3. Apply the Table B rates: 2.0 / 4.5 / 5.5 / 6.0 / 6.5 / 6.9 / 6.99%. The bracket breaks are, for codes A, D and F, 10k / 50k / 100k / 200k / 250k / 500k; for B, 16k / 80k / 160k / 320k / 400k / 800k; for C, 20k / 100k / 200k / 400k / 500k / 1M.
  4. Add the Table C 2% phase-out add-back and the Table D recapture.
  5. Multiply by (1 − the Table E credit decimal).
  6. Divide by the number of pay periods.
  7. Add CT-W4 line 2 and subtract line 3.
- **Extraction warning for the builder.** `pdftotext -layout` drops the bounds of every other Table E row. A word-level PyMuPDF extraction of page 6 returns the complete table: the credit runs from .75 down to .00, and ends at A 52,500, B 78,500, C 100,500 and F 64,500. Use that extraction (or the PDF itself), never the layout text.
- **Oracle check (C37 candidate).** The IP 2026(1) examples are computed from the withholding **tables**:
  - Ex. 8: F, USD 700/week, 17.65
  - Ex. 9: A, USD 1,000/week, 39.97
  - Ex. 10: B, USD 2,300 biweekly, 78.82

  Re-running the TPG-211 **rules** gives 17.79, 39.86 and 79.30. The rules and the tables therefore differ by at most USD 0.48 per period, because the tables use wage brackets. The pay-period tables in IP 2026(1) pp. 31+ were not parsed (see Open questions). The oracle is DRS's own worked examples in IP 2026(1) p. 11-12 (held PDF, md5 a64b2bbb855163fb832396939efc74ef).
- **Form CT-W4 (Rev. 12/25)** [US-CTS5-011]. Codes A/B/C/D/E/F by filing status and expected income.
  - With no CT-W4, withhold a flat 6.99% without exemption.
  - Code E (exempt) certificates expire on 15 February. Without a new form, withhold 6.99% from 16 February.
  - Exempt certificates go to DRS where expected wages exceed 36,000 (MFS), 45,000 (single), 57,000 (HoH) or 72,000 (MFJ), i.e. 3 × the maximum exemption.
  - MSRRA spouses claim on CT-W4 and attach the LES and dependent ID.
- **Supplemental wages.** There is no flat supplemental rate; only the aggregate method applies [US-CTS5-012]. Paid with regular wages, withhold as one payment. Paid separately, compute on regular + supplemental and withhold the difference.
- **Rounding.** TPG-211 states no rounding rule beyond the computed per-period amount. The DRS tables are in whole cents.
- **Wage definition.** CT follows the federal withholding wage definition: fringe benefits, supplemental pay, sick pay, severance [US-CTS5-011].
- **Residents and nonresidents, reciprocity.** Unchanged from the sealed mandate [US-CTP10-001]:
  - residents are withheld on all wages, prorated where another qualifying jurisdiction requires withholding;
  - nonresidents are withheld on CT-service wages, allocated on CT-W4NA or by records; with neither, on all wages (Ex. 10);
  - the 15-day rule applies;
  - there is **no reciprocity**;
  - the convenience-of-employer rule has applied from 2019 (reciprocal) [US-MULTI-020].
- **Local income taxes.** None (US-MQ-26 part 2).
- **Pension lump sums.** Withholding on lump-sum retirement distributions is suspended from 2025-07-01 to 2026-12-31. The payee may request it on CT-W4P [US-CTS5-010]. This is not wages.

## 3. social_security (UI, PFML, levies)
- **UI 2026** [US-CTP9V-001, reused]:
  - TWB 27,000;
  - new-employer rate 1.9%;
  - charged rate 0.1–8.9%, plus a 1.0% fund solvency tax (combined 1.1–9.9%);
  - no employee contribution [US-CTS5-031].
- **Wage-base indexation** (31-222(b)(1)(A)(vi)) [US-CTS5-016, A.1]. The base moves by the ECI and is rounded to the nearest USD 100.
  - G-DERIVE: 26,100 × 1.036 = 27,039.6, which rounds to **27,000**. This matches the DOL notice.
  - 2027 projection, **derived, not published**: 27,000 × 1.032 = 27,864, which rounds to 27,900. The DOL 2027 rate page returned 404 on 2026-11-02. Do not model 27,900 until DOL publishes it.
- **Other-state wage credit: YES.** Remuneration on which the employer paid another state's UI counts toward the CT maximum (31-222(b) and UI guide p. 17) [US-CTS5-016, US-CTS5-031]. Each concurrent employer reports to the maximum. A predecessor's wages count only for a successor.
- **Coverage** [US-CTS5-017]:
  - domestic service is covered at USD 1,000 cash in any quarter;
  - agricultural labour at USD 20,000 cash in a quarter, or 10 workers on 20 days in 20 weeks;
  - churches and ministers are excluded, as are family employment, student and student-spouse work, student nurses/interns, newspaper carriers under 18 and co-op students.
- **CT Paid Leave (PFML)** [US-CTS5-020 A.1, US-CTS5-022 A.2, US-CTS5-035 A.3]:
  - **Contribution.** The employee pays 0.5% in 2026 (the statutory cap is 0.5%). The base is subject earnings, i.e. UI total wages, excluding FICA-excluded benefits, capped at the SS wage base. 2026 = USD 184,500 [US-CTP7-001]. Each employer withholds to the cap separately. There is no employer share.
  - **Remittance.** Quarterly. Due on the last day of the quarter, with no penalty if paid by the last day of the following month. Channels: My Account portal, or batch SFTP in XML/CSV per the File Specification Toolkit.
  - **Benefit** (paid by the Authority, not through payroll). 95% of base weekly earnings up to 40 × MW, plus 60% above that. **Maximum 60 × MW = USD 1,016.40/week in 2026, USD 1,048.80 in 2027** (derived).
  - **Exclusions.** Government employers are excluded, except opted-in public employees.
  - **Multistate.** The Authority treats as working in CT any employee for whom the employer pays CT UI and CT payroll taxes. Coverage follows UI localization [US-CTS5-035].
- **Other levies.** None beyond UI and CTPL (US-CTP9W-001/-002 reused). No SDI/TDI exists.

## 4. payslip_statute
- With each wage payment the employer gives a record of hours worked, gross pay (straight time and overtime as separate entries), itemised deductions and net pay. Hours and the split do not apply to employees exempt from overtime.
- **Electronic delivery only with the employee's explicit consent**, with a secure, private way to access and print the record and confidentiality safeguards [US-CT-P5-1-005; US-CTS5-027].
- **New from 2026-10-01 (PA 26-12 sec. 38, 31-13a(c)):**
  - employers with **100+ employees**, including the state and municipalities, must publish a pay-code guide covering overtime and the most common pay differentials, with at least 10 codes where applicable;
  - the guide is in English, Spanish and other common languages, with a dispute contact;
  - the guide's **URL must appear on every pay record** and be given at hire;
  - a payroll provider's compliant guide satisfies the duty [US-CTS5-028, A.1].
  - **PSL impact:** add a "pay-code guide URL" field for 100+ employers.
- **Retention.** Hours and wage records are kept 3 years at the place of employment (31-66) [US-CTS5-027].
- **Codification lag (F18).** The held chapter 557 copy (Wayback 2026-10-20) still prints 31-13a without subsection (c). Cite PA 26-12 sec. 38 until the consolidated text catches up.

## 5. reporting_instruments
- **Withholding** [US-CTS5-013, A.2]:
  - **Channel.** Everything is electronic via myconneCT, with payment by EFT. The waiver form is DRS-EWVR.
  - **Remitter class**, by the 12-month lookback ending 30 June of the prior year:

    | Class | Lookback liability | Remit by |
    |---|---|---|
    | Weekly | > USD 10,000 | Wednesday after the Sat–Fri week |
    | Monthly | USD 2,000–10,000 | the 15th of the next month |
    | Quarterly | ≤ USD 2,000 | the last day of the month after the quarter |

    New employers are mostly quarterly.
  - **CT-941** is quarterly, due 4/30, 7/31, 10/31 and 1/31, even with zero tax and even for federal 944 filers. Annual filer status is available on request by 31 March.
  - **CT-W3 plus all W-2s** are due 31 January via myconneCT, by key-and-send, **EFW2 upload** or the DRS pre-defined CSV. The W-2 carries box 15 = "CT" plus the CT Tax Registration Number. The penalty is USD 5 per return, up to USD 2,000.
  - **Household:** CT-W3 HHE by 31 January; CT-941 HHE annually by 15 April if registered. **Agricultural:** annual CT-941 [US-CTS5-014].
- **UI quarterly Tax and Wage Report** [US-CTS5-018 A.1, US-CTS5-031 A.2, US-CTS5-032 A.2]:
  - **Channel.** Electronic via ReEmployCT: manual entry, upload, TPA or FSET. Corporate bulk upload for subsidiaries requires TPA registration.
  - **Deadlines.** Due 4/30, 7/31, 10/31, 1/31; reimbursing employers get 15 more days. A zero-wage report is required.
  - **File format.** A 276-character fixed-length .txt file with S (employee) and T (employer) records. Positions were extracted and checked to sum to 276 [US-CTS5-032].
  - **New optional data from Q3 2026** (31-225a(j)(1)(B)): occupation, hours worked and worksite ZIP. The 2022 file spec has no fields for them (see Open questions).
  - **Penalties.** Late file fee USD 25. Late payment: interest plus a penalty of the greater of USD 50 or 10%.
- **New hire** [US-CTS5-019 A.1, US-CTS5-015 A.2]:
  - report within **20 days** of hire, rehires included (rehire = separated more than 60 days);
  - fields: name, address and SSN, by copy of CT-W4 (which carries the new/rehired flag, hire date and FEIN), the CT DOL New Hire website or fax;
  - the duty applies to any employer with an office in CT or transacting business in CT.
- **CT Paid Leave quarterly return** [US-CTS5-022]: the portal or batch XML/CSV. The File Specification Toolkit PDF was not downloaded; RSPEC needs it.
- **Registration.** DRS withholding registration through myconneCT (REG-1). Every employer that must withhold registers, even with an out-of-state payroll department [US-CTS5-011, IP p. 9]. Registration with DOL UI and CTPL is in ReEmployCT [US-CTS5-031] and CTPL My Account [US-CTS5-022].

## 6. leave
- **Paid sick leave** (31-57r/s, as amended by PA 23-101 and PA 24-8) [US-CTS5-021, A.1]:
  - **Coverage** phases in by CT headcount (payroll for the week containing 1 January): **11+ from 2026-01-01, 1+ from 2027-01-01** (25+ from 2025).
  - **Accrual:** 1 hour per 30 hours worked, up to 40 h/year. Up to 40 h carries over, or the employer front-loads.
  - **Use** from day 120 of employment.
  - **Pay rate:** the greater of the normal hourly wage (variable pay: the prior period's average) or the minimum wage. Exempt staff are presumed to work 40 h.
  - **No payout** on termination unless a policy or CBA provides one.
  - Seasonal employees (≤ 120 days) are excluded.
  - Multistate: the statute counts and covers employees "in the state". No apportionment rule for partly-in-state work was located (see Open questions).
- **CT FMLA** gives 12 weeks of job-protected leave from employers with 1+ employees. Unpaid weeks may be compensated through CTPL [US-CTS5-033].
- **CTPL benefits** are paid by the Authority, not through payroll. Income-tax withholding on them is elective [US-CTS5-020].

## 7. termination
- **Final pay** [US-CTS5-005, A.1]:
  - discharge: by the **business day after** discharge;
  - quit, or layoff/labour-dispute suspension: by the **next regular pay day**.
- **Vacation and PTO payout:** only if the employer's policy or a CBA provides for it. It is then paid as wages at no less than the average rate earned during the accrual period (31-76k) [US-CTS5-005].
- **Separation notice:** the Separation Packet (UC-21 with the UC-21A Unemployment Notice) goes to **every** separating employee whatever the reason, and is mailed if handing it over is impracticable [US-CTS5-031].
- **From 2027-01-01** an unpaid-wage claim carries double damages, reduced to single where the employer shows good faith (PA 26-12 sec. 56) [US-CTS5-028].
- WARN: PA 26-15 sec. 26 (2026-10-01) requires federal WARN notices to DOL to disclose AI-related layoffs [US-CTS5-029, pointer only].

## 8. benefits_in_kind
- **Withholding** follows the federal wage definition (IP 2026(1) "Income Subject to CT Withholding") [US-CTS5-011]. No CT departure was located in the 2026 guide for 401(k), section 125, HSA, transit or group-term life. Confidence: medium. The DRS guide states conformity in general terms only; the chapter 229 modification list (12-701(a)(20)) was not read in this pass.
- **CTPL base** excludes benefits excluded from FICA wages [US-CTS5-022].
- **UI base** excludes employer-paid FICA for domestic/agricultural workers [US-CTS5-016].
- **2026 session:** no new wage-exclusion for withholding. The new subtractions (honor guard, National Guard state active duty from 2027; PHS corps retirement from 2026) operate at **assessment** [US-CTS5-030].

## 9. deductions_garnishments
- **Wage deductions** need one of the following [US-CTS5-006, A.1]:
  - a requirement or empowerment under law;
  - written authorisation **on a form approved by the Labor Commissioner**;
  - a medical/hospital deduction with no benefit to the employer;
  - auto-enrollment 401(k)/403(b)/408/408A/457 or the CT Retirement Security Program;
  - another state's income-tax withholding requirement.
- **Creditor wage execution** (52-361a) [US-CTS5-024]:
  - **the lesser of 25% of disposable earnings or the excess over 40 × the higher of the federal or CT minimum wage.** 2026 protects USD 677.60/week, 2027 USD 699.20. This is stricter than the CCPA's 30 × federal;
  - there is a 20-day stay after service on the employer;
  - only one execution runs at a time.
- **Child support IWO** (52-362) [US-CTS5-025]:
  - exempt amount: the greater of 85% of the first USD 145/week of disposable income, or the CCPA 1673 amount;
  - withholding starts with the first pay period after 14 days from service;
  - remit to the SDU within **7 business days**;
  - with several orders, the SDU pro-rates with priority to current support;
  - support has priority over wage executions.
  - No employer administrative fee was found in the sections read (see Open questions).
- **State tax levies:** not researched (low priority; DRS collections).

## 10. collective_agreements (prevailing wage)
- **31-53** [US-CTS5-023, A.1, superseding US-CT-P5-1-006]:
  - **weekly certified payroll** goes to the contracting agency and is a public record; failing to file is a class D felony;
  - **thresholds:** new construction ≥ USD 1,000,000; remodeling/repair ≥ USD 100,000.
- **2026 changes** (OLR pointer, texts not read) [US-CTS5-029]:
  - PA 26-12 sec. 54 amends 31-53 (2026-10-01);
  - PA 26-68 secs 371-373 add daily attendance records submitted weekly and price the benefits portion at the journeyman rate (2027-01-01);
  - PA 26-17 allows the comptroller to withhold payment to violators (2026-10-01).

## 11. indexation
| Item | Mechanism | 2026 | 2027 | Source |
|---|---|---|---|---|
| Minimum wage | ECI 12 months to 30 June, nearest cent, announced by 15 October | 16.94 (16.35 × 1.036) | 17.48 (16.94 × 1.032) | US-CTS5-001/-008/-009 |
| UI taxable wage base | ECI, nearest USD 100 | 27,000 (26,100 × 1.036) | not published; derived 27,900 | US-CTS5-016, US-CTP9V-001 |
| CTPL contribution base | SS wage base | 184,500 | SSA 2027 figure | US-CTS5-020, US-CTP7-001 |
| CTPL max weekly benefit | 60 × MW | 1,016.40 | 1,048.80 | US-CTS5-020 (derived) |
| Garnishment protected amount | 40 × max(federal, CT MW) | 677.60 | 699.20 | US-CTS5-024 (derived) |
| Withholding tables | annual TPG-211 reissue | unchanged from 2025 | TPG-211 2027 (Rev. 12/26) expected Dec 2026 | US-CTS5-010 |
| Tipped employer share | fixed in statute | 6.38 / 8.23 | same | US-CTS5-002 |

The 2025 ECI (4.2%) is **implied**, not separately sourced: 15.69 × 1.042 = 16.349, which rounds to 16.35. It also reproduces the 2025 wage base (25,000 × 1.042 = 26,050, which rounds to 26,100). The caliber is the same ECI series in both statutes (G-CALIBER: one index, two uses).

## 12. data_protection
- **SSNs** (42-470) [US-CTS5-026, A.1]: no public display, no SSN on access cards, no SSN over the internet unless the connection is secure or encrypted, and no SSN-only web login.
- **Personal information** (42-471): safeguard it and destroy it before disposal. Anyone collecting SSNs must publish a privacy protection policy.
- **No statute requiring SSN truncation on pay statements was located.** 31-13a does not require the SSN at all.
- **Electronic pay records** need confidentiality safeguards (31-13a(b)) [US-CTS5-027].

## 13. live_legal_change (2026-01-01 → 2026-11-02)
| Change | Instrument | Status / effective | Level | Register |
|---|---|---|---|---|
| Sick-leave coverage 11+ | 31-57r as amended (PA 23-101, PA 24-8) | in force 2026-01-01 | employer leave accrual | US-CTS5-021 |
| Sick-leave coverage 1+ | same | enacted, effective 2027-01-01 | employer leave accrual | US-CTS5-021 |
| MW 17.48 | 31-58(i) indexation | announced, effective 2027-01-01 | wage floor | US-CTS5-009 |
| Pay-code guide URL on every pay record (100+ employers) | PA 26-12 sec. 38 (31-13a(c)) | in force 2026-10-01 | pay statement | US-CTS5-028 |
| Minor-league baseball excluded from MW/OT | PA 26-12 sec. 40 | in force 2026-10-01 | wage floor | US-CTS5-028 |
| No cannabis tip credit | PA 26-12 sec. 6 | in force 2026-10-01 | wage floor | US-CTS5-028/-029 |
| Double damages for unpaid wages; subcontractor-wage claims against contractor | PA 26-12 secs 55-56 (31-72) | enacted, 2027-01-01 | wage payment liability | US-CTS5-028 |
| Optional occupation/hours/ZIP in the UI wage report | 31-225a(j)(1)(B) | in force from Q3 2026 | employer reporting (optional) | US-CTS5-018 |
| UI shared-work non-charge | PA 26-68 sec. 195 | enacted, 2027-01-01 | employer UI experience | US-CTS5-029 |
| Prevailing wage: daily attendance records; journeyman benefits rate | PA 26-68 secs 371-373 | enacted, 2027-01-01 | certified payroll | US-CTS5-029 |
| Pension lump-sum withholding suspension ends | TPG-211 / IP 2026(1) | suspension ends 2026-12-31 | withholding (pension payers) | US-CTS5-010 |
| Income-tax subtractions (honor guard, National Guard SAD 2027; PHS corps retirement 2026) | 2026 session (DRS overview) | enacted | assessment | US-CTS5-030 |
| No change to withholding rates or method for 2026 | TPG-211 Rev. 12/25 | in force | withholding | US-CTS5-010 |

No court ruling affecting CT payroll was found in this sweep. The sweep covered the DRS 2026 developments, the OLR 2026 business acts report and PA 26-12. The OLR "2026 Acts Affecting Taxes" (2026AA-0076) was located but not read.

## Special populations (state level, US-OWN-005)
| Population | CT rule | Register |
|---|---|---|
| Domestic / household workers | MW/OT: private-home domestic service excluded except FLSA-defined domestic service employment. UI: covered at USD 1,000 cash in a quarter. Withholding voluntary (CT-941 HHE annual by 15 April; CT-W3 HHE by 31 January even if not registered). Extended written hiring notice | US-CTS5-034, -017, -014, -007 |
| Agricultural | Withhold CT where federal withholding applies (Pub. 51); annual CT-941 option for 943 filers. UI at USD 20,000/quarter or 10 workers on 20 weeks | US-CTS5-014, -017 |
| Minors | Under 18 (not emancipated): 85% of MW for the first 90 days or USD 10.10, whichever is greater (2026: 14.40; 2027: 14.86). Newspaper carriers under 18 excluded from UI. Hours limits 31-12ff (not detailed) | US-CTS5-001, -017 |
| Tipped employees | Employer share USD 6.38 (hotel/restaurant) and 8.23 (bartenders); 0.35 elsewhere; no cannabis tip credit from 2026-10-01 | US-CTS5-002, -028 |
| Clergy / religious | UI excludes churches and ordained ministers. Withholding follows the federal wage definition; no CT-specific rule located | US-CTS5-017, -011 |
| Students | UI excludes students working for their own school (and a spouse in student-aid work), student nurses/interns and co-op credit programmes. MW: college head residents/RAs excluded; learner subminimum by regulation | US-CTS5-017, -034 |
| Nonresident aliens | No state rule beyond federal located. CT follows the federal withholding wage definition and CT-W4 codes; IP 2026(1) has no NRA section (full-text checked: no "nonresident alien") | US-CTS5-011 |
| Statutory employees | No state rule beyond federal (federal wage definition followed); not separately addressed in IP 2026(1) | US-CTS5-011 |
| Government employees | UI: other states' and US government service excluded; CT state/municipal service covered. CTPL: governments excluded except opted-in covered public employees. Sick leave: no government exclusion in 31-57r (wording "any person... or other entity"). Comptroller pays state employees by direct deposit | US-CTS5-017, -020, -021, -004 |
| Military / MSRRA | Nonresident servicemembers' military pay is not CT wages; CT-resident military pay is subject; MSRRA spouses exempt on CT-W4 with LES and ID | US-CTS5-014 |
| Seasonal | Excluded from paid sick leave (≤ 120 days); seasonal CT-941 filer status on request | US-CTS5-021, -014 |

## MULTI hand-offs (answers for CT)
- **SUI wage-base credit for wages reported to another state: YES.** 31-222(b)(1)(A) and UI guide p. 17 [US-CTS5-016, US-CTS5-031].
- **PFML coverage of multistate workers: follows UI localization.** The CTPL Guide for Employers says an employee "for whom an employer is paying CT unemployment insurance and CT payroll taxes" is working in CT [US-CTS5-035, A.3]. The statute's "service to an employer in this state" and the UI-based subject earnings [US-CTS5-020] are consistent with this.
- **Paid sick leave for partly-in-state work:** the statute covers "employees in the state" and counts headcount "in the state". No apportionment or threshold rule exists in 31-57r/s. Still open (see Open questions).
- **Pay-statement reach:** 31-13a applies to "each employer" with "each employee", with no territorial clause. Default: the CT work location. No reach rule located.

## ACCESS gaps (exact URLs)
1. `https://www.cga.ct.gov/current/pub/chap_558.htm`, `chap_567.htm`, `chap_906.htm`, `chap_743dd.htm`: curl 000 (connection refused, VPN off). All were read from Wayback 2026 captures (`web.archive.org/web/2026id_/…`, captures 20261013–20261024).
2. `https://prdext2.cga.ct.gov/2026/ACT/PA/PDF/2026PA-00012-R00HB-05003-PA.PDF` and `https://prdext2.cga.ct.gov/2026/rpt/pdf/2026-R-0081.pdf`: curl 000. Read from the Wayback copies of the cga.ct.gov URLs.
3. `https://portal.ct.gov/dol/divisions/unemployment-insurance-tax/information-on-unemployment-tax-rate-for-calendar-year-2027`: HTTP 404 (not yet published, not a block).
4. `https://portal.ct.gov/DOLUI/ReEmployCT-for-Employers_File-Formats_Excel-Sheet-Templates_Info-for-Bulk-Filers`: redirects to the TPA page (US-CT-P5-2-002). The bulk-filer ICESA/MMREF specification page named in search leads was not reached. The 276-character format [US-CTS5-032] was obtained directly.

## Open questions
- **CT-OQ-1 (WTC/PSL oracle).** The exact per-period withholding comes from the DRS withholding tables (IP 2026(1) pp. 31+, held PDF), which were not parsed. The TPG-211 rules differ from the tables by up to USD 0.48 per period. What would close it: the builder decides which method the engine implements (DRS permits either, US-CTS5-010). If tables, parse IP 2026(1) pp. 31-39 and reproduce Examples 8–10 exactly (17.65 / 39.97 / 78.82).
- **CT-OQ-2 (RSPEC).** The ReEmployCT 276-character layout (2022) has no positions for the optional occupation/hours/worksite-ZIP data allowed from Q3 2026 (31-225a(j)(1)(B)). The search leads also say bulk filers may use ICESA or MMREF. What would close it: the CT DOL bulk-filer file-format page or an updated ReEmployCT file specification (CT DOL Employer Tax Accounting Unit, dol.etau@ct.gov).
- **CT-OQ-3 (RSPEC/SIR).** The CT Paid Leave File Specification Toolkit (PDF, XML/CSV return and enrollment files) is linked from `ctpaidleave.org/remit-contributions/batch-process` but was not downloaded. What would close it: download and parse the toolkit (CT Paid Leave Authority).
- **CT-OQ-4.** The 2027 UI taxable wage base is not published. The derived value (27,900) is a projection only. What would close it: the CT DOL "Information on Unemployment Tax Rate for Calendar Year 2027" page (normally published in December).
- **CT-OQ-5 (benefits_in_kind).** State departures from federal exclusions were checked only in DRS guide terms. What would close it: Conn. Gen. Stat. 12-701(a)(20) (chapter 229) modification list, read for any add-back of HSA, 125 or 401(k) amounts (expected none). Separately, whether CT adds back the new federal tips/overtime deductions is an assessment question, not withholding.
- **CT-OQ-6 (leave, multistate).** Paid sick leave for employees working partly in CT: the statute has no threshold. What would close it: CT DOL Wage and Workplace Standards paid-sick-leave FAQ (2025/2026 edition).
- **CT-OQ-7 (garnishment).** Is an employer administrative fee permitted for IWO or wage execution in CT? It is not seen in the 52-361a/52-362 text read. What would close it: a full read of 52-362 (held file) and 52-361a(j)–(k).
- **CT-OQ-8 (PA texts).** PA 26-68 (secs 195, 371-373), PA 26-17 and PA 26-15 sec. 26 were summarised by OLR only (A.3 pointer). What would close it: the act PDFs on cga.ct.gov (Wayback route works).
- **CT-OQ-9 (codification lag).** The consolidated 31-13a online text (2026-10-20 capture) predates PA 26-12 sec. 38. Re-verify the consolidated text at the next synthesis; cite PA 26-12 until then.

## Corpus
- `00-official-sources/ccg-sources/CT/`: 17 files, 3.8 MB. Largest file: chapter 567 HTML, 0.6 MB.
- `pdfs/CT/CT_IP-2026-1_2026-11-02.pdf` (6.8 MB, already held by the scaffolder) was reused and not duplicated.
- No archives were involved.
