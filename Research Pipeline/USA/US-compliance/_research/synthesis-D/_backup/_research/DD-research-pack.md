# DD research pack - United States (stage 4, Data Dictionary, unit 8_sheets)

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B worker (RSPEC + DD), 2026-11-02. Built only from active/partial tier-A register rows cited by the stage-5 findings; no fetching. Facts: `_research/DD-8_sheets-facts.json` (key `dd.{scope}.{field}`; `_consumers` names the report or calculation each field feeds).

## 0. Structure

The DD workbook has 8 sheets (mercans-artifact-toolkit structural contract, precedent `CZ_Data_Dictionary_V2_0.xlsx`): Version Control - Introduction - Instructions - ID Information - Country Fields - Country Option Mappers - Currency Codes (ISO 4217) - Country Codes (ISO 3166-1). This pack is organised by the sheets that carry country content: **ID Information**, **Country Fields** (split below by family), **Country Option Mappers**. Currency = USD only, 2 minor units (build manifest). Country = US; state codes are an option mapper, not ISO 3166-1 rows.

**F26 discipline.** Per-payrun computed amounts (tax withheld, taxable/excess wages, contributions, W-2 box 12 TP/TT/TA amounts, NV MBT wage match, AZ sick-time balances on the paycheck) are WTC/PSL/report computations and are deliberately **not** DD facts. Each field below is classified master / period input / derived; the derived ones are listed so the builder can exclude them consciously.

**Special populations (US-OWN-005).** All populations IN for the federal layer: ordinary, nonresident alien, statutory employee, household, agricultural, clergy, employee abroad -> one option-mapper field `special_population.category` [US-OWN-005, owner row; carried in `_owner_scope` of the facts file]; NRA needs its own flag and treaty data [US-FEDS5-016]; WA exempt corporate officers [US-WAS5-027]; FL E-Verify employer certification [US-FLS5-010]. Contractors / 1099-NEC OUT of scope (owner instruction 2026-10-29, SKELETON-MANIFEST scope line) - no contractor master data.

**Language seams (US-OWN-006).** No DD language field is needed for the payslip (English). Two notice seams need data: NY employee primary language [US-NYP9L-001] and CO workforce first languages at 5% [US-COL-001].

## Country Fields - hire data and special populations

| DD fact key | Field / content | Class | Consumers | register_id | Note |
|---|---|---|---|---|---|
| `dd.fed.new_hire.date_first_services` | date services first performed (new-hire report federal minimum) | master data | rspec.*.new_hire | US-FEDS5-024 |  |
| `dd.in.new_hire.job_comp` | job title, SOC, starting compensation, rate-of-pay basis | master data | rspec.in.new_hire | US-INS5-016 |  |
| `dd.md.new_hire.wage_health` | starting wage, employer health insurance offered, MD UI account number | master data | rspec.md.new_hire | US-MDS5-018 |  |
| `dd.ms.new_hire.extra` | DOB, gender, salary, pay frequency, medical-insurance eligibility | master data | rspec.ms.new_hire | US-MSS5-006 |  |
| `dd.ga.new_hire.extra` | DOB, medical-insurance availability, state of hire | master data | rspec.ga.new_hire | US-GAS5-012 |  |
| `dd.la.new_hire.occupation` | occupation | master data | rspec.la.new_hire | US-LAS5-010 |  |
| `dd.ia.new_hire.health` | dependent health coverage available and qualifying date; IWO address | master data | rspec.ia.new_hire | US-IAS5-012 |  |
| `dd.state.new_hire.dob` | date of birth required by GA, IA, ME, MS, NJ, OH, OR, WA, WI, WV new-hire reports | master data | rspec.*.new_hire | US-NJS5-018 | per-state rows in RSPEC facts |
| `dd.state.new_hire.rehire_gap_days` | 60 days | master data | rspec.*.new_hire | US-CTS5-019 | common rehire threshold (MA uses 30; LA none); per-state value in RSPEC facts |

## Country Fields - local jurisdiction codes

| DD fact key | Field / content | Class | Consumers | register_id | Note |
|---|---|---|---|---|---|
| `dd.oh.school_district_code` | four-digit Ohio school district code of residence (9999 full-year nonresident); W-2 and SD 101/141 | master data | rspec.oh.w2_state; rspec.oh.school_district | US-OHS5-019 | 2026 delta in US-OHS5-018 |
| `dd.pa.psd_code` | PA PSD code of work location and of residence (format xxxxxx-xx) | master data | rspec.pa.local.eit_lst | US-PAS5-017 | home-based employee residence is a worksite (US-PAS5-018) |
| `dd.in.county_residence_jan1` | Indiana county of residence and county of principal employment on Jan 1 (WH-4) | master data | rspec.in.w2_state RS county code; calc:IN county tax | US-INS5-021 |  |
| `dd.ny.nyc_yonkers_residence` | NYC / Yonkers resident status and resident period | master data | rspec.ny.nys45 Part C | US-NYS5-010 |  |
| `dd.ky.locality` | Kentucky locality of work (Louisville Metro, Lexington-Fayette) and residence (school board component) | master data | rspec.ky.local | US-KYP9W-001 |  |
| `dd.or.metro_multnomah` | Metro SHS / Multnomah PFA work location and opt-in/opt-out | master data | rspec.or.local | US-ORS5-004 |  |
| `dd.or.transit_district` | TriMet / Lane transit district of work | master data | rspec.or.oq | US-ORS5-010 |  |
| `dd.oh.municipality_work` | Ohio municipality of work (718.03) and residence; collector (CCA/RITA/city) | master data | rspec.oh.municipal | US-OHP52-003 (P) |  |
| `dd.md.county_residence` | Maryland county of residence (local rate tables) via MW507 | master data | calc:MD local; MW508 | US-MDP51-001 (P) |  |
| `dd.mi.city_residence_work` | Michigan city (e.g. Detroit) resident / nonresident predominant place of employment; DW-4 | master data | rspec.mi.local.detroit | US-MIP51-002 (P) |  |
| `dd.co.denver_opt` | Denver OPT work location and monthly earnings >=500 test | master data | rspec.co.local | US-COP52-001 (P) |  |
| `dd.ia.school_district_residence` | Iowa school district of residence (surtax at assessment; IA W-4 note) | master data | IA W-4 data only | US-IAP52-001 (P) | surtax computed on the individual return, not withheld (US-IAP51-005) |

## Country Fields - notice language seams

| DD fact key | Field / content | Class | Consumers | register_id | Note |
|---|---|---|---|---|---|
| `dd.ny.employee_primary_language` | employee primary language for the Labor Law 195.1 pay-rate/payday notice (English + primary language) | master data | notice template (not a report) | US-NYP9L-001 | notice seam only; payslip stays English (US-OWN-006) |
| `dd.co.workforce_first_language_5pct` | first languages spoken by at least 5% of the workforce (paid sick leave notice) | master data | notice template (not a report) | US-COL-001 | notice seam only (US-OWN-006) |

## Country Fields - report-specific fields

| DD fact key | Field / content | Class | Consumers | register_id | Note |
|---|---|---|---|---|---|
| `dd.fed.w2.tipped_occupation_code` | Treasury Tipped Occupation Code per employee (W-2 box 14b, TY2026) | master data | rspec.fed.w2 | US-FEDS5-007 |  |
| `dd.fed.aca.fte_tracking` | full-time / FTE status per month for ALE determination and 1095-C | period input (hours) + derived monthly status | rspec.fed.aca | US-FEDS5-012 | row partial: TY2026 instructions not yet published; register row status partial |
| `dd.ak.ui.occupation_code` | 6- or 8-digit occupational code per employee | master data | rspec.ak.ui_qtr | US-AKS5-014 |  |
| `dd.ak.ui.geographic_code` | 2-digit Alaska geographic code per employee | master data | rspec.ak.ui_qtr | US-AKS5-014 |  |
| `dd.wa.ui.soc_code` | SOC code per employee | master data | rspec.wa.ui_qtr | US-WAS5-013 |  |
| `dd.wa.ui.hours_quarter` | hours worked in quarter, rounded up; 40/week for untracked salaried; paid leave hours included | period input (time data) | rspec.wa.ui_qtr; rspec.wa.pfml_ltc_qtr | US-WAS5-013 |  |
| `dd.wa.exempt_officer` | corporate officer without voluntary UI coverage flag | master data | rspec.wa.ui_qtr | US-WAS5-027 |  |
| `dd.vt.ui.gender_hourly` | gender and hourly wage for hourly workers | master data | rspec.vt.ui_qtr | US-VTS5-007 |  |
| `dd.ct.ui.occupation_hours_zip` | occupation, hours worked, worksite ZIP (optional from Q3 2026) | master (occupation, ZIP) + period input (hours) | rspec.ct.ui_qtr | US-CTS5-018 | no positions in 2022 file spec |
| `dd.mn.ui.paid_hours` | total paid hours worked per quarter (exempt FT = 40 h/week) | period input (time data) | rspec.mn.ui_qtr | US-MNS5-015 |  |
| `dd.ma.ui.hours_work_location` | hours worked, work location, 12th-of-month employment, adjustment reason code | period input + master (work location) | rspec.ma.ui_qtr | US-MAS5-018 |  |
| `dd.in.ui.soc_start_date` | SOC code (6 digits) and start date per worker | master data | rspec.in.ui_qtr; rspec.in.new_hire | US-INS5-014 |  |
| `dd.mo.ui.separation_probation` | separation dates and probationary flag P with dates (28 days or less) | master (separation date) + derived flag | rspec.mo.ui_qtr | US-MOS5-013 |  |
| `dd.oh.ui.weeks_paid` | number of weeks paid per employee | derived per quarter (F26) | rspec.oh.ui_qtr | US-OHS5-020 |  |
| `dd.nj.ui.base_weeks` | base weeks per employee (week >= 20 x prior-year minimum wage) | derived per quarter from wages: WTC/report computation, keep out of DD master data (F26); DD carries no input beyond pay dates | rspec.nj.ui_qtr | US-NJS5-017 |  |
| `dd.pa.ui.credit_weeks` | credit weeks per employee (week with remuneration >= 116) | derived per quarter (F26), as NJ base weeks | rspec.pa.ui_qtr | US-PAS5-013 |  |
| `dd.ne.ui.hours_job_title` | hours and job title (optional) | master data | rspec.ne.ui_qtr | US-NES5-011 |  |
| `dd.tx.ui.enhanced` | industry, occupation, full/part-time, county of primary employment, remote-work status | master data | rspec.tx.ui_qtr | US-TXS5-008 | TWC layout not read; mandatory-from quarter unknown |
| `dd.state.ui.month12_count` | covered on payroll in the pay period including the 12th of each month (employer monthly counts) | derived from employment status on the 12th (report computation) | rspec.*.ui_qtr | US-FLS5-021 | same item on AK TQ01C, ME UC-1, WV, MA |
| `dd.state.ui.out_of_state_wages` | wages reported to other states in the year (excess wage computation) | period input (prior wages reported to other states / predecessor) | rspec.*.ui_qtr | US-MULTIS5-010 | FL RT-6NF; AK Y/N flag |
| `dd.fl.everify_certified` | E-Verify certification (private employers 25+), certified on first RT-6 of the year | master data | rspec.fl.ui_qtr | US-FLS5-010 |  |
| `dd.fl.ssn_not_itin` | SSN required on RT-6; ITIN not accepted | master data | rspec.fl.ui_qtr | US-FLS5-024 | NJ WR-30 and MA new hire also refuse ITIN |
| `dd.wy.vacation_forfeiture_policy_acknowledged` | written forfeiture policy acknowledged in writing by employee (else accrued vacation payable at termination, 27-4-501(a)(iii)) | master data | calc:final pay | US-WYS5-002 |  |
| `dd.de.paid_leave.hours` | hours and wages per employee for Delaware Paid Leave quarterly report | period input (time data) | rspec.de.pfml_qtr | US-DES5-013 |  |
| `dd.or.form132.hours` | employee wage and hour detail (Form 132) | period input (time data) | rspec.or.oq | US-ORS5-010 |  |
| `dd.wv.ui.soc_county` | SOC or job title and county per employee | master data | rspec.wv.ui_qtr | US-WVUI-001 (P) |  |

## Country Fields - tax certificates

| DD fact key | Field / content | Class | Consumers | register_id | Note |
|---|---|---|---|---|---|
| `dd.fed.w4_2026.fields` | Step 1(c) filing status; Step 2 multiple-jobs checkbox; Step 3 dependents credit; Step 4(a) other income; 4(b) deductions; 4(c) extra withholding; exempt claim | master data | calc:FIT Pub.15-T | US-FEDS5-006 |  |
| `dd.fed.nra.flag` | nonresident alien flag + Notice 1392 W-4 and Form 8233 treaty exemption (exempt wages to 1042-S, not W-2 box 1) | master data | calc:FIT NRA add-on; W-2; 1042-S | US-FEDS5-016 |  |
| `dd.state.w4.al` | Form A4 (REV. 4/2025) | master data | calc:AL SIT | US-ALS5-005 |  |
| `dd.state.w4.ar` | AR4EC / AR4ECSP (R 12/04/2025) | master data | calc:AR SIT | US-ARS5-009 |  |
| `dd.state.w4.ca` | DE 4 (Rev. 56 1-26) | master data | calc:CA PIT | US-CAS5-015 |  |
| `dd.state.w4.co` | DR 0004 (2026) | master data | calc:CO SIT | US-COS5-012 |  |
| `dd.state.w4.ct` | CT-W4 codes A-F; Code E expires Feb 15; no CT-W4 = 6.99% | master data | calc:CT SIT; rspec.ct.new_hire | US-CTS5-011 |  |
| `dd.state.w4.dc` | D-4 / D-4A (marked under review on OTR page) | master data | calc:DC SIT | US-DCS5-013 |  |
| `dd.state.w4.de` | federal W-4 (DE worksheets; W-4NR nonresidents) | master data | calc:DE SIT | US-DES5-006 |  |
| `dd.state.w4.ga` | G-4 (Rev. 06/03/26) | master data | calc:GA SIT | US-GAS5-010 |  |
| `dd.state.w4.hi` | HW-4 (Rev. 2022); HW-6/HW-7 exempt nonresidents | master data | calc:HI SIT | US-HIS5-026 |  |
| `dd.state.w4.ia` | IA W-4 44-019a (11/13/2025); page 3 = new-hire form 44-019d | master data | calc:IA SIT; rspec.ia.new_hire | US-IAS5-029 |  |
| `dd.state.w4.id` | ID W-4 (EFO00307, 04-28-2025) | master data | calc:ID SIT | US-IDS5-013 | row partial; register row status partial |
| `dd.state.w4.il` | IL-W-4 (R-07/23) | master data | calc:IL SIT | US-ILS5-010 |  |
| `dd.state.w4.in` | WH-4 with county status | master data | calc:IN SIT + county | US-INS5-021 |  |
| `dd.state.w4.ks` | K-4 (Rev. 7-24) | master data | calc:KS SIT | US-KSS5-025 |  |
| `dd.state.w4.ky` | K-4 (exemption/additional only; flat 3.5%) | master data | calc:KY SIT | US-KY-001 |  |
| `dd.state.w4.ma` | M-4 | master data | calc:MA SIT | US-MAS5-014 |  |
| `dd.state.w4.me` | W-4ME | master data | calc:ME SIT | US-MES5-011 |  |
| `dd.state.w4.mi` | MI-W4 (Rev. 12-20) | master data | calc:MI SIT | US-MIS5-019 |  |
| `dd.state.w4.mo` | MO W-4 (Revised 12-2024) | master data | calc:MO SIT; rspec.mo.new_hire | US-MOS5-020 |  |
| `dd.state.w4.nc` | NC-4 family | master data | calc:NC SIT | US-NC-001 |  |
| `dd.state.w4.nd` | federal W-4 (no state certificate); NDW-R reciprocity | master data | calc:ND SIT | US-NDS5-001 |  |
| `dd.state.w4.nj` | NJ-W4 (1-21) | master data | calc:NJ SIT | US-NJS5-024 |  |
| `dd.state.w4.ny` | IT-2104 (IT-2104.1 nonresident allocation) | master data | calc:NY SIT | US-NY-001 |  |
| `dd.state.w4.oh` | IT 4 (zero exemptions if absent) | master data | calc:OH SIT | US-OH-002 |  |
| `dd.state.w4.ok` | OK-W-4 (Revised 3-2021) | master data | calc:OK SIT | US-OKS5-021 |  |
| `dd.state.w4.or` | OR-W-4 (150-101-402) | master data | calc:OR SIT | US-ORS5-012 |  |
| `dd.state.w4.ri` | RI W-4 mandatory since 2020 (allowances capped at 10) | master data | calc:RI SIT | US-RIS5-019 |  |
| `dd.state.w4.sc` | SC W-4 (2026, Rev. 12/5/25) | master data | calc:SC SIT; rspec.sc.new_hire | US-SCS5-003 |  |
| `dd.state.w4.ut` | federal W-4 (federal = state claims); W-4E no-liability | master data | calc:UT SIT | US-UTS5-013 |  |
| `dd.state.w4.va` | VA-4 (Rev. 04/26) | master data | calc:VA SIT | US-VAS5-021 |  |
| `dd.state.w4.vt` | W-4VT (Rev. 12/18) | master data | calc:VT SIT | US-VTS5-029 |  |
| `dd.state.w4.wv` | IT-104 / IT-104NR | master data | calc:WV SIT | US-WVS5-011 |  |
| `dd.state.w4.az` | Form A-4 (2026) withholding percentage election | master data | calc:AZ SIT | US-AZP51-001 (P) |  |
| `dd.state.w4.la` | L-4 (Form R-1300) | master data | calc:LA SIT | US-LAPIT-001 (P) |  |
| `dd.state.w4.md` | MW507 (MW507M, MW507P) | master data | calc:MD SIT | US-MDP51-001 (P) |  |
| `dd.state.w4.mn` | W-4MN (none = single, 0 allowances) | master data | calc:MN SIT | US-MNPIT-001 (P) |  |
| `dd.state.w4.ms` | Form 89-350 | master data | calc:MS SIT | US-MSPIT-001 (P) |  |
| `dd.state.w4.mt` | MW-4 (exemption claims sent to DOR via TAP) | master data | calc:MT SIT | US-MTP51-002 (P) |  |
| `dd.state.w4.ne` | W-4N (else single, no allowances) | master data | calc:NE SIT | US-NEP51-001 (P) |  |
| `dd.state.w4.nm` | federal W-4 marked for NM (optional) | master data | calc:NM SIT | US-NMP52-001 (P) |  |
| `dd.state.w4.wi` | WT-4 | master data | calc:WI SIT | US-WIP51-001 (P) |  |

## Country Fields - work/residence jurisdiction

| DD fact key | Field / content | Class | Consumers | register_id | Note |
|---|---|---|---|---|---|
| `dd.multi.work_state` | work state per assignment (withholding sourcing; UI localization) | master data | rspec.*.wh_return; rspec.*.ui_qtr | US-MULTIS5-017 | localization test order: localized / base of operations / direction-control / residence |
| `dd.multi.sui_state` | single UI state per employee per period under the localization test; also keys WA PFML | master data | rspec.*.ui_qtr; pfml | US-MULTIS5-024 |  |
| `dd.multi.residence_state` | residence state (reciprocity, resident credit, transport-worker federal rules) | master data | calc:SIT | US-MULTIS5-001 | 49 USC 14503 motor carriers taxable only by residence state |
| `dd.multi.transport_worker_type` | motor carrier / rail / air carrier / seaman flag | master data | calc:SIT sourcing | US-MULTIS5-003 | air 40116(f); rail 11502 (US-MULTIS5-002); seamen 11108 (US-MULTIS5-004) |
| `dd.multi.military_spouse` | military spouse residence election (SCRA sec. 511) | master data | calc:SIT | US-MULTIS5-005 |  |
| `dd.multi.ny_convenience_days` | NY working days / total working days for nonresident allocation (convenience of employer test) | period input (working days) | calc:NY SIT; NYS-45 | US-MULTIS5-013 |  |
| `dd.multi.pa_working_days` | PA working days / total for nonresident employees | period input (working days) | calc:PA SIT | US-MULTIS5-014 |  |
| `dd.la.workday_counter` | per-employee count of LA workdays for nonresident employees (Act 382, employer plus related entities) | period input accumulated per year | calc:LA SIT nonresident threshold | US-MULTIS5-021 | applies to periods from 2026-01-01 |

## ID Information - employer / account identifiers

| DD fact key | Field / content | Class | Consumers | register_id | Note |
|---|---|---|---|---|---|
| `dd.md.naics` | NAICS code (employer) in MW508 RV record | master data | rspec.md.w2_state | US-MDS5-016 |  |
| `dd.employer.state_account_ids` | per-state withholding account / UI account / PFML account ids (e.g. UT 14-digit ...WTH, KS 036-...-01, MD 8-digit CRN, IA 9-digit permit) | master data | rspec.* | US-UTS5-013 | KS US-KSS5-026; MD US-MDS5-021; IA US-IAS5-018 |
| `dd.employer.ny_mctmt_zone` | MCTMT zone payroll | master data | rspec.ny.mctmt | US-NY-003 |  |

## Country Option Mappers (enumerations to carry)

- Federal W-4 filing status: Single/MFS; MFJ/QSS; HoH [US-FEDS5-006]. State certificate codes: CT-W4 A-F [US-CTS5-011]; per-state allowance/exemption enumerations per form in the tax-certificate table.
- Special population category (7 values) [US-OWN-005].
- Ohio school district 4-digit codes (9999 = full-year nonresident) [US-OHS5-019, 2026 changes US-OHS5-018]; PA PSD codes [US-PAS5-017/018]; Indiana county codes (2-digit, EFW2 RS 306-307) [US-INS5-013]; Maryland county local-rate tables [US-MDP51-001].
- SOC codes (6-digit) for WA, IN, WV, AK (6/8-digit occupational code) [US-WAS5-013, US-INS5-014, US-WVUI-001, US-AKS5-014]; AK 2-digit geographic codes [US-AKS5-014]; NAICS (MD RV record) [US-MDS5-016].
- UI adjustment reason codes: MD 00-10 [US-MDS5-017]; MA adjustment reason code [US-MAS5-018].
- Transport-worker type (motor / rail / air / seaman) [US-MULTIS5-001..004].

## R. RSPEC x DD reconciliation

The mapping table (RSPEC -> DD) and the consumer check (DD -> RSPEC/calc) are in `_research/RSPEC-research-pack.md` section R; both directions were generated mechanically from the two facts files. Result: 0 gaps. Report fields that depend on still-unread layouts (TX 204.0025 enhanced fields, CT Q3 2026 optional fields, WA PFML report fields) are carried as DD fields now and flagged in Open questions.

## Open questions

Mirrors `unresolved[]` of `DD-8_sheets-facts.json`.

- **dd.tx.ui.enhanced_mandatory_from** (non-blocking). Which Labor Code 204.0025 fields are mandatory from which quarter is unknown (TWC layout not read) Attempted: twc.texas.gov. What would close it: TWC implementing rule/layout for 204.0025
- **dd.ct.ui.q3_2026_positions** (non-blocking). CT optional occupation/hours/worksite ZIP have no positions in the 2022 file spec Attempted: US-CTS5-032. What would close it: CT DOL file spec edition for Q3 2026
- **dd.oh.municipal_rate_table** (non-blocking). No consolidated Ohio municipal rate table could be fetched; only The Finder (partial A.3) per address Attempted: tax.ohio.gov municipal; US-OHS5-023 partial. What would close it: Ohio municipal rate data set from the Department of Taxation or each collector (CCA, RITA)

The RSPEC open questions on unread file layouts also limit the DD wherever a layout could add a field (see `RSPEC-research-pack.md` Open questions).
