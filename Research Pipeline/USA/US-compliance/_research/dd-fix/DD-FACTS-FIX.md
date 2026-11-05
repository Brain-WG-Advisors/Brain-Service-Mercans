# DD facts fix, 2026-11-03 (source hunter)

Files: `_research/DD-8_sheets-facts.json` (114 facts, 12 unresolved), `00-official-sources/legal-basis-register.csv` (+US-OHB5-403), `00-official-sources/code-tables/US-{IN-county,MD-county,OH-municipal-fips}.json`. Backups: `_research/dd-fix/backup/*.20261103-dd`. Web: 1 WebFetch (403) + 1 HTTP client attempt on mass.gov (403) + 2 search summaries (not used as sources). A Wayback attempt for the same PDF was refused by the permission classifier and was not pursued.

## Part 1. The four unsupported facts

| Key | Result | Quote (copy) |
|---|---|---|
| dd.ms.new_hire.extra | Re-bound to US-MSS5-007 (A.3, same authority, other page); fields now literal | "Required Employee Information: Employee's Name ... Employee's Social Security Number (SSN) Employee's Date of Hire Employee's Date of Birth Gender Salary Payment Frequency Medical Insurance Eligibility" (ccg-sources/MS/MS_SDNH-reporting-fundamentals_2026-11-02.html). US-MSS5-006 copy (law page) names none of these fields. |
| dd.ky.locality | Reworded to Louisville Metro only; Lexington-Fayette is new key dd.ky.locality.lexington on US-KYS5-024 | US-KYP9W-001 copy has no Lexington text (grep). US-KYS5-024: "The Lexington-Fayette Urban County Government assesses an occupational license fee of 2.25%. The fee applies to an individual's compensation and a business's net profits." |
| dd.state.w4.ny | Re-bound to US-NY-013, US-NY-001 as also-register | US-NY-013 copy (pdfs/NY/whtax_require_wb.html): "nonresidents ... See Form IT-2104.1, New York State, City of New York, and City of Yonkers Certificate of Nonresidence and Allocation of Withholding Tax". US-NY-001 copy: "Form IT-2104 -- Employee's Withholding Allowance Certificate" (IT-2104.1 does not occur in it). |
| dd.state.w4.nm | Reworded ("optional" is not in the copy) | FYI-104: "New Mexico does not have a state equivalent of the Federal Form W-4 ... writing 'For New Mexico State Withholding Only' ... This duplicate W-4 is not mandatory. It is a convenience for employer and employee." |

## Part 2. RQ-01 to RQ-05

| RQ | Result |
|---|---|
| RQ-01 dd.state.w4.line_structure | Open (non-blocking). About 40 State forms, not read line by line; recorded in unresolved[]. Natural shape for a fan-out: one lookup per State. |
| RQ-02 external code lists | Closed in part: dd.oh.municipal.code_list (US-OHB5-403 + US-OHB5-002; 678 in-force codes, 1,083 rows, 685 distinct codes ever), dd.in.county_code.list (US-INS5-007; 92 codes 01-92, contiguous), dd.md.county_code.list (US-MDS5-003; numeric 01-24 plus 25 alpha codes). Open: Ohio school district numbers (two-column PDF, names cannot be paired reliably), PA PSD, SOC and NAICS (not held; NAICS 2027 edition unconfirmed), Alaska occupational/geographic codes (manual not held). |
| RQ-03 UI adjustment reasons | Maryland closed: dd.md.ui.adjustment_reason.codes (US-MDS5-017 table 1.1.3, 00-10; 08 "Staff Amended" and 09 "Wages adjusted because worker(s) were hired/terminated" checked on the rendered page). Massachusetts open: spec PDF returned 403; held how-to page says only "Adjustment reason code, if needed". A search summary listed codes; not recorded (G-NUMBER). |
| RQ-04 depositor status | Closed: dd.fed.depositor_status.codes (US-FEDS5-004 copy, Pub. 15 2026): "monthly schedule depositor" / "semiweekly schedule depositor"; $50,000 lookback threshold. |
| RQ-05 special population | Left open: US-OWN-005 is an owner decision (tier owner); facts schema tier enum has no such value, so it cannot be a fact. unresolved[] records what would close it. |

Also closed (RQ-09, evidence local): The Finder help page names column 3 "Municipal FIPS Code" (US-OHB5-403, md5 b99bc20cb1a3c6ba010add52a2854ece); the unresolved entry dd.oh.municipal_rate_table.code_identity was removed. The existing value of dd.oh.municipal_rate_table was not reworded.

## Validation
- validate_contract facts: PASS. validate_contract --all: PASS (87 files). Register: 20 columns written by csv.DictWriter, one row added, consumed_by += DD on 11 rows.
- C71: FAIL, 1 difference: US-LOC-001 M3 prints the old dd.ky.locality wording. Expected effect of the reword; closes when the RSPEC generator re-issues the workbook (workbooks not touched here). Ledger line added.
- C41 FAIL is pre-existing (no bulletin-sweep.json; 986 rows not current), not caused by this change.
