# Browser pass P1 - 2026-11-02

Worker P1, per `_prompts/browser-pass-brief.md`. All reads in the user's Chrome (own tab, closed at the end). Shard: `00-official-sources/_register-shards/S5B-P1.csv` (20 rows, 20 columns). Page texts: `00-official-sources/ccg-sources/{JUR}/*_browser_2026-11-02.txt`; PDFs fetched by curl once the link was found in Chrome (md5 in the register row), each with a `.txt` extraction alongside.

About 65 page loads used (budget 80). No CAPTCHA, login or challenge was bypassed. The Cloudflare interstitial on tax.utah.gov cleared by itself after waiting.

## Summary: what closed, what stayed open

| Key / question | Result | Register |
|---|---|---|
| `oh.pit.school_district.full_list` | **Closed.** Full TY2026 list, effective January 2026: 214 districts, 68 on the earned-income base, with SD number, IRN and rate. | US-OHB5-001 |
| `oh.pit.municipal.rate_table` | **Closed (rates).** The Finder's official municipal rate table CSV: 678 municipalities in force. The table does not carry resident credits or the collector. | US-OHB5-002 (supersedes US-OHS5-023) |
| `ny.pfl.employee.rate.next_year` | **Closed.** 2027: 0.452%, annual max 451.81 (DFS decision dated 2026-08-31). | US-NYB5-001 (supersedes US-NYS5-022) |
| `ny.pfl.benefit.max_weekly` | **Closed for 2026.** NYSAWW 1,833.63, max weekly benefit 1,228.53, 0.432% / 411.91 (arithmetic checked). The 2027 NYSAWW amount is not published; only "+4.83%". | US-NYB5-002 |
| `ny.leave.nyc_pto` | **Closed.** DCWP FAQ updated 02/22/2026: 32 hours unpaid immediately available, 40/56 hours paid, 20 hours prenatal, 4 pay-statement items. | US-NYB5-003 (supersedes US-NYS5-023) |
| `ct.report.pfml.file_spec` (CT-OQ-3) | **Closed.** File Specification Toolkit v2.1.9 (10/5/26): XML/CSV, naming, ack file, return elements. CTPL wages follow FICA wages. | US-CTB5-001 |
| MI-OQ-2 new-hire fields/channels | **Partly closed.** Fields, 20 days, 12–16-day e-transmissions, rehire 60 days, channels, MSE. No MI statute or penalty on the page. | US-MIB5-001 (supersedes US-MIS5-026) |
| FED new-hire (ACF page) | **Closed.** 7 data elements, 20 days, 12–16 days, penalty cap 25/500, MSE option. | US-FEDB5-001 |
| WA-OQ-2 s.125/401(k)/HSA in UI, PFML, WA Cares | **Narrowed, not closed.** No WAC (192-510-025, ch. 192-310) and no PFML toolkit mentions 125, 401(k) or HSA. PFML and WA Cares = "gross wages without tips"; the only plan exclusion is *employer* payments to retirement or medical plans (WAC 192-510-025(2)(c)). Reading: employee elective deferrals stay in PFML and WA Cares wages. Confidence medium; no explicit text. UI: same silence in ch. 192-310 and RCW 50.04.320. | US-WAB5-001, -003, -004 |
| WA-OQ-3 PFML/WA Cares report fields | **Closed.** Hours (rounded up; salaried = 40/week; no hours for cash-outs or severance) and gross wages without tips. 2026: 1.13% (71.43/28.57) up to 184,500; WA Cares 0.58%, no cap. Penalties from 2026-08-01. | US-WAB5-002, -003 |
| MA DUA rate schedules A–G | **Read.** Full 45-row table transcribed from the PDF viewer, with a mechanical consistency check. | US-MAB5-001 |
| `ut.sdi.exists` | **Supports "no".** The USTC tax list has no SDI, paid-leave or local wage tax. | US-UTB5-003 |
| `ut.pit.schedule.effective_date` (UT-OQ-1) | **Still open.** The live Pub 14 HTML (Rev. 04/26) gives no effective date. The PDF link is 404 (files.tax.utah.gov and tax.utah.gov). No USTC news found. US-UT-PIT-004 (tier B, 2026-06-01) stays the only lead. | US-UTB5-001 |
| `ut.pit.supplemental` (UT-OQ-2) | **Unchanged.** Pub 14 HTML has no "supplemental" text, and the PDF is unavailable. | US-UTB5-001 |
| `dc.wh.method` (DC OQ-1) | **Still open (confirmed absent).** D-4/D-4A "currently under review" with no links. No 2026 FR-230 or notice found by OTR site search. The withholding-instructions page returns OTR's own "Access denied" (not a bot challenge). | US-DCB5-001 |
| DC TY2026 W-2 instructions | **Not yet published.** The newest is 2025 W2/W2C. TY2026 FR-900 bulk layouts and specs v2.0 are listed. | US-DCB5-002 |
| WY-OQ-1 2026 UI rates | **Still open.** No rate release or industry table on dws.wyo.gov (site search). The NAICS page has groups only. | US-WYB5-001 (partial) |
| WY-OQ-3 WYUI file format | **Partial.** Portal entry via "Method B" guide and spreadsheet (Google Drive, not read). No fixed-length spec is linked. | US-WYB5-001 |

## Per target URL

### 1. DC
- `otr.cfo.dc.gov/page/income-tax-withholding-instructions-and-tables`: **blocked.** OTR's own "Access denied - You are not authorized to access this page." This is site-side, not a challenge.
- `otr.cfo.dc.gov/page/withholding-tax-forms`: **read.** US-DCB5-001.
- OTR site search (its own Google CSE box) for "withholding tables" and "2026 withholding personal exemption D-4": no 2026 method, FR-230 or notice. Only 2013/2018 D-4 and the 2025 D-40 booklet came up.
- `otr.cfo.dc.gov/publication/bulk-filing-sales-and-use-withholding-and-information-returns`: **read.** US-DCB5-002. TY2026 W-2 instructions not listed.
- Not covered: `dc.law.fy2027bsa.permanent` and `dc.pit.std_deduction.cola` (not in P1 list).

### 2. UT
- `tax.utah.gov/withholding`: **read** after the Cloudflare interstitial cleared by itself. US-UTB5-002.
- `tax.utah.gov/forms-pubs/pubs/pub-14/`: **read** (Rev. 04/26). US-UTB5-001.
- Pub 14 PDF (`files.tax.utah.gov/tax/forms/pubs/pub-14.pdf`, `tax.utah.gov/forms/pubs/pub-14.pdf`): **404** in Chrome.
- `tax.utah.gov/business/utah-taxes/` (List of All Tax Types): **read.** US-UTB5-003.
- `incometax.utah.gov/paying/tax-rates`: **read.** US-UTB5-004. Still the TY2025 site; it shows 4.5% "current".
- USTC site search "withholding schedules 2026": no notice.
- `jobs.utah.gov/ui/employer/Public/Questions/TaxRates.aspx`: **blocked.** 403 Forbidden in Chrome, and the extension also refused to read the domain. `ut.ui.rates.next_year` stays open.
- `le.utah.gov` (59-10-402, 35A-4-303 exact version files): **blocked.** Chrome shows its own network error page (connection fails from this network). 34-40-104, 35A-4-205 and 70C-7-103 were not attempted after two failures. `ut.labour.minwage.exemptions`, `ut.ui.wage_base.other_state_credit` and `ut.garn.limits_and_iwo` stay open.

### 3. OH
- `tax.ohio.gov/business/ohio-business-taxes/municipal-income-tax`: "No content found" shell.
- `tax.ohio.gov/business/employer-withholding`: **read** (link list). It links School_Districts_2026.pdf and the 2026 filing guidelines, both already held (md5 identical; duplicates deleted).
- `tax.ohio.gov/researcher/tax-analysis/tax-data-series/tds1`: **read.** It led to `sdit_list.pdf`. US-OHB5-001.
- `thefinder.tax.ohio.gov` > File Downloads > Municipal: **read.** CSV fetched in-page. US-OHB5-002. Help page layout quoted. JEDD/JEDZ CSV not saved: the second download in the same call did not land.

### 4. WA
- `app.leg.wa.gov/WAC/default.aspx?cite=192-310-030`: **read.** This is the UI penalty rule, not a wage definition. US-WAB5-004.
- Chapter 192-310 TOC: **read.** No section on 125 or deferrals.
- `cite=192-510-025`: **read.** US-WAB5-001.
- `paidleave.wa.gov/employer-roles-responsibilities/`: **read.** US-WAB5-002.
- Employer Wage Reporting and Premiums Toolkit v25.1 (June 2026): fetched by curl. US-WAB5-003.
- ESD site search ("401k cafeteria taxable wages", "deferred compensation"): 0 results.
- Not reached (budget): RCW 26.23 live, RCW 50.24.010, RCW 51.32.073. Use app.leg.wa.gov in Chrome; it is now readable (the earlier TLS failure did not recur).

### 5. FED
- `ssa.gov/oact/cola/cbb.html`: **blocked.** The Chrome extension has no read permission for ssa.gov ("Permission denied for reading page content on this domain"). `fed.fica.oasdi.wage_base.next_year_reverification` stays open.
- `acf.hhs.gov/.../new-hire-reporting` (now acf.gov): **read.** US-FEDB5-001.
- Multistate registration page: the guessed URL `acf.gov/css/employers/employer-responsibilities/multistate-employer-registration` is 404. The MI portal names `https://www.acf.hhs.gov/css/resource/multistate-employer-registration-form-instructions` (not read).

### 6. NY
- DFS 2027 PFL decision: **read.** US-NYB5-001.
- `paidfamilyleave.ny.gov/2026`: **read.** US-NYB5-002.
- `nyc.gov/site/dca/about/paid-sick-leave-law.page` and the FAQ page: **read.** FAQ PDF fetched by curl (49 pp., Updated 02/22/2026). US-NYB5-003.

### 7. WY
- dws.wyo.gov site search (2 queries), WYUI page and NAICS grouping page: **read.** US-WYB5-001 (partial). WY-OQ-1 stays open. Next step: the DWS helpline 307-235-3217, or a DWS rate notice (WYUI correspondence, behind login).
- `newhire-reporting.com/wy-newhire`: not attempted (budget).

### 8. MA, CT, VA, NH, MI
- **MA:**
  - `mass.gov/info-details/employer-contributions-to-unemployment`: read (link list).
  - Schedules A–G PDF: read in the viewer. US-MAB5-001.
  - The "UI and Covid Recovery Assessment rates" PDF is the same file already held (`MA_DUA-UI-COVID-RA-rates-2026_2026-11-02.pdf`, md5 5584297682d1fffcbf39e290c35acca7).
  - M-3 and the new-hire layout: not reached (budget).
- **CT:** `ctpaidleave.org/remit-contributions/batch-process` (www host) read, toolkit fetched. US-CTB5-001. CT DRS tax types: not reached.
- **VA:** `vec.virginia.gov/employers/Tax-Rate-Information`: **blocked.** F5 "Request Rejected", 403, also in Chrome. `va.ui.pool_cost_and_new_employer` stays open.
- **NH:** `gc.nh.gov/rules/state_agencies/emp300.html`: **blocked.** "Web Page Blocked, Attack ID 20000018" by client IP, also in Chrome. Emp 300 and NHES 0047 stay open; they need a US IP or VPN.
- **MI:** `mi-newhire.com` > New Hire Requirements & FAQs: **read.** US-MIB5-001. UIA rate page: not reached.

## Notes for the synthesis
- **OH municipal layer.** OHMuniRateTable.csv is the official A.2 rate source. Residence credits and the collector (RITA/CCA/self) still come from each municipality.
- **WA deferrals.** Without an explicit ESD statement, the build should treat employee 401(k) and s.125 elective deferrals as included in PFML and WA Cares gross wages. That rests on the absence of any exclusion plus the "employer payment" wording of WAC 192-510-025(2)(c). Flag it as medium confidence. CT contrasts: its toolkit ties CTPL wages to FICA wages, so s.125 is excluded and 401(k) included.
- **Utah rate page.** incometax.utah.gov still shows 4.5% as "current". Do not read it as contradicting 4.45% for 2026; it is the TY2025 instructions site.
- **Mishap, fixed.** A scratchpad file name collision with another worker briefly appended 9 foreign rows (US-VAS5-001..009, copies of S5-VA.csv) to S5B-P1.csv. The file was deleted and rebuilt from P1's own rows only before anything read it.
- Screenshots of the MA schedule: `C:\Users\INSTIT~1\AppData\Local\Temp\claude-chrome-screenshots-mTCj2N\screenshot-1793624656708-3.jpg` and `screenshot-1793624667481-4.jpg`.
