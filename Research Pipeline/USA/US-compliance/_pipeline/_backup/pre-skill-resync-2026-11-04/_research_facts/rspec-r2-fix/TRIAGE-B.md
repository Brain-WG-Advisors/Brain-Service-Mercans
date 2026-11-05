# RSPEC pre-QA-r3 text verification: triage B (states MO to WY)

Date: 2026-11-03. Agent 2 (source hunter). Input: `selfcheck/selfcheck-misses.json`.

**Scope.** Keys whose jurisdiction prefix is MO to WY. The prefix is the second token for `rspec.*` and `dd.*` keys, and the first token otherwise. That gives 66 elements across 36 keys in 5 files: `RSPEC-facts.json`, `DD-8_sheets-facts.json`, `CCG-annex_NV/OR/PA-facts.json`. The fed., multi. and AL to MS keys were not touched.

**Safety.**
- Backups and MD5s are in `_backup3/`: the 5 facts files plus `legal-basis-register.csv`.
- Every write took `facts.lock`, re-read the file, changed only the keys in scope, and replaced the file atomically.
- All 5 facts files validate against `shared/schemas/facts.schema.json` with 0 errors.
- Incident, now repaired: the edit script ran twice by mistake. The second run only added a duplicate `_figure_located` segment to 4 DD keys and then stopped on an assertion before touching RSPEC or the register. The duplicates were removed under the lock.

**Result.**
- Self-check rerun with a fresh text cache: 151 misses became 99 for the whole set. The other 85 belong to triage A.
- In this share, 66 misses became 14. The 14 left are matcher limits only. Each was read by hand, and its quote and page are in the fact's `_figure_located` (see `TRIAGE-B-adjudicated.json`). **Unadjudicated misses: 0.**

## Priority suspects
- **rspec.tx.ui_qtr.due.** The four calendar dates are not in 40 TAC 815.109 (US-TXS6-002) or 815.107. The value now states the rule as written: due on the first day of the month after the quarter and paid by the last day of that month (815.109(a)); a Saturday, Sunday or holiday rolls to the next business day (815.109(c), quoted); the report is filed within that month (815.107(d)); electronic media (815.107(a)(3)). Added `_also_register_ids` US-TXS6-001. The dates are a derivation and are no longer in the value. Unresolved: `rspec.tx.ui_qtr.due.calendar_dates`.
- **rspec.wv.local.charleston.service_fee_return.** "Paper" and the four dates are not in the CSF regulations (US-WVS6-001). The value now quotes the regulations: quarters ending Mar 31, Jun 30, Sep 30 and Dec 31, remitted "before the expiration of one month from the end of the reporting period", with no filing channel stated. Unresolved: `...charleston.service_fee_return.channel`.
- **rspec.or.local.portland_metro_multnomah.** W-2, EFW2 and the Jan 31 / no-extension rule are on the Portland withholding page (US-ORS5-004, p1, quoted), not in the XML guide. Added US-ORS5-004 to `_also_register_ids`. The value is unchanged.

## Changes per key
Notation: "+row" means the row was added to `_also_register_ids`. "FL" means the quote and page went into `_figure_located`.

- **dd.oh.school_district_code:** +US-OHB5-401 for SD 101, SD 141, W-2s and four-digit. FL also covers 9999 on US-OHS5-019 p1.
- **dd.pa.psd_code:** +US-PAS5-018 for PSD. Removed "format xxxxxx-xx" because no held copy prints it. Unresolved: `dd.pa.psd_code.format`.
- **dd.oh.municipality_work:** "CCA/RITA" changed to the ORC 718 wording ("central collection agency", "regional income tax agency").
- **dd.oh.municipal_rate_table** and **rspec.oh.municipal.rate_table:** removed "FIPS" because the CSV has no header and no held copy names the code. The value now says "5-digit municipal code (third column)", inspected directly. Unresolved: `dd.oh.municipal_rate_table.code_identity`.
- **rspec.mt.w2_state.format:** now "images and PDFs are not accepted" (p10, verbatim).
- **rspec.nm.ui_qtr.formats:** +US-NMS5-016 (p7: "must file their quarterly reports electronically").
- **rspec.ny.nys1.deposit:** "QTD" changed to the source wording ("accumulated tax withheld ... $700").
- **rspec.ok.ui_qtr.format:** "TPA" changed to the source wording ("third-party administrators", p2).
- **rspec.or.oq.due:** dates moved to ISO form, matching p5 of the 211-155-2.
- **rspec.ri.w2_state.format:** +US-RIS5-018 for EFW2, .txt, ASCII, 5 MB/49 MB (p7) and RS required (p8).
- **rspec.ri.ui_qtr.form:** "JDA" changed to "Job Development fund".
- **rspec.sc.wh_return.form:** "Q1-Q3" changed to "quarters 1, 2 and 3".
- **rspec.sd.ui_qtr.layout:** "SSN" changed to "social security no.".
- **rspec.va.wh_return.form:** "100-999" changed to "at least 100 but less than 1,000" (p16).
- **rspec.wi.w2_state.format:** "MTA, upload, sFTP" changed to "My Tax Account, Data File Transfer, sFTP". +US-WIS5-015 (pb172 p3; "no transmittal" on p5).
- **rspec.oh.school_district.list:** +US-OHB5-401 and +US-OHS5-018. FL covers 214/68 on US-OHB5-001 p5.
- **rspec.wa.ui_qtr.penalties:** "ESD" changed to "employment security department number" (WAC text).
- **rspec.nc.w2_state.ty2026_rs_layout:** "ZIP" changed to "Zip code".
- **rspec.wv.local.morgantown.service_fee_return:** "7 years" changed to "seven years".
- **rspec.wv.local.service_fee_returns:**
  - Register ids were removed from the value text.
  - +US-WVS6-002 and +US-WVR3-001.
  - The statutory pointer moved from US-WVP52-005 (8-13-13 as shown in introduced bill HB 2524, 2025) to US-WVR3-001 (the Code copy).
- **rspec.pa.local.pittsburgh_payroll_expense.return:** "paper ... USPS" changed to the form's mailing line. +US-PAS6-002 ("United States Post Office postmark will be the only proof").
- **rspec.wa.local.seattle.sht.due:**
  - "PET" is now spelled out as Payroll Expense Tax.
  - Kept "due quarterly beginning April 30, 2026" and "Q4 due Jan. 31, 2027" (US-WAS6-001, added).
  - Removed Jul 31 and Oct 31, which no held copy prints.
  - Unresolved: `rspec.wa.local.seattle.sht.quarterly_due_dates`.
- **nv.mbt.base:** "ESD" was spelled out. +US-NVS5-009.

## Residual 14 (matcher limits, quoted in `_figure_located`)
| Key | Element | What the source says |
|---|---|---|
| or.stt.employee.rate | 0.1 | ".001" |
| or.transit.trimet.employer.rate | 0.8237 | "0.008237" (p6, p15) |
| or.transit.lane.employer.rate | 0.8 | "0.0080" |
| pa.pit…payroll_expense.rate | 0.55 | "0.0055" |
| ne.newhire.report_days, oh.newhire.report_days | 20 | "twenty days" |
| rspec.oh.municipal.frequency | 2,399 and 200 | "two thousand three hundred ninety-nine dollars", "two hundred dollars" |
| rspec.oh.w2_state.school_district_code | W-2 | "W-2s" |
| rspec.nm.w2_state.due | txt | "(TXT)" |
| dd.oh.municipal_rate_table, rspec.oh.municipal.rate_table | 5, 678, 2026-11-01 | inspected directly in the CSV |

## Register
- 27 rows had `verified_on` stamped 2026-11-03.
- US-OHB5-401 had `DD/8_sheets` added to `consumed_by`. Every other cited row already listed its consumer.
- No other field changed.

## Open questions (the new `unresolved[]` entries)
- `dd.pa.psd_code.format`: closes with the DCED PSD code list or an Address Search report.
- `dd.oh.municipal_rate_table.code_identity`: closes with the ODT Finder file-layout page.
- `rspec.tx.ui_qtr.due.calendar_dates`: closes with the TWC due-date page or the C-3 instructions.
- `rspec.wv.local.charleston.service_fee_return.channel`: closes with the blank CSF-2 or the City Collector page.
- `rspec.wa.local.seattle.sht.quarterly_due_dates`: closes with the SHT quarterly form instructions or the SMC 5.39 text.
