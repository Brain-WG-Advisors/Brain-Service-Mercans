# Mandate answers P5-FED-r2 - FED, MULTI, FILING (PASS 4, second round, 2026-10-29)

Worker: compliance-source-hunter. Register shard: `00-official-sources/_register-shards/mandate-P5-FED-r2.csv` (ids US-FEDP52-001..013, plus US-TX/IL/MI-P5-2-008..012). Part mapping: p1 = federal tax (US-MQ-02), p2 = language (03), p3 = levies list (05), p4 = POA/filing (09), p5 = multistate (10), p6 = special populations (12).
Different approach from round 1: statute-site vs agency pages replaced by (a) text already saved locally (Pub 15, Rev. Proc. 2025-32 downloaded and read with PyMuPDF, python -I), (b) the DOL Comparison of State UI Laws (a federal all-state source), (c) ACF policy transmittal instead of the form page, (d) Wayback 2026 snapshots saved locally (TX C-42 page, MI payroll-provider page) and agency PDFs downloaded plainly (IL IDES, MI Form 151). About 25 reads. No javascript_tool, no filter bypass, one Wayback request per 10 s, no 429 seen. Chrome tab opened and closed. No document edited other than my own two files plus saved source copies under `00-official-sources/pdfs/{FED,TX,IL,MI}/`.

## FED

**p1 / US-MQ-02 currency, rounding - ANSWERED (90%).** New: Pub 15 (2026) section "Making a tax payment": "Payments of U.S. tax must be remitted to the IRS in U.S. dollars. Digital assets are not accepted." [US-FEDP52-001, A.2, 2026]. 31 U.S.C. 5103 (legal tender) and 26 U.S.C. 6316 (Secretary may allow foreign-currency payment by regulation, read in LII) give the legal frame [round 1 -001; 6316 read in round 2 but not registered, discretionary only]. Rounding/cents: unchanged (Pub 15-T optional whole-dollar, Form 941 and W-2 in cents; US-FED-001/005/P5-1-012). Remaining 10%: no instrument read that fixes the unit of the W-2/941 return itself (only payments); reg 301.6302-1 read through summarizer says nothing on currency. Treat the engine currency as USD with the Pub 15 sentence as the cited rule.

**p2 / US-MQ-03 - ABSENCE PROVEN at federal level (85%)** (unchanged from round 1: US-FED-020, US-FED-010).

**p3 / US-MQ-05 devolved domains, federal part - PARTIAL (80%).** IWO form OMB 0970-0154: the revised form carries OMB expiration 2026-08-31; state IV-D agencies had to generate it from 2024-10-01 (AT-23-13, 2023-10-05, archived page "current as of 2025-02-10") [US-FEDP52-003]. That date has now passed (today 2026-10-29): whether OMB extended the form is NOT located (acf.gov form page redirects to the employer page, Reginfo blocked by a domain-change check; a Federal Register notice 2026-04740 of 2026-03-11 turned up in search but concerns OMB 0970-0227, a different collection, and is not used). Employer duties: 42 U.S.C. 666(b)(6): standard format, pay to SDU within 7 business days of the date the amount would have been paid to the employee, priority over other State-law process, no liability if the notice is regular on its face [US-FEDP52-004, provisional: LII summarizer, check subsection wording]. Priority over other garnishments except an earlier IRS levy re-read on the ACF employer page [round 1 -006].

**p4 / US-MQ-09 federal filing instruments - PARTIAL (85%).** Form 8655 / Pub 1474 / Rev. Proc. 2012-32 already closed. EFW2 TY2026: SSA page re-read - both TY2026 and TY2025 list EFW2 Publication 42-007 and EFW2C 42-014, no revision date on the page [US-FEDP52-013, gated]. `26efw2.pdf` is `unreadable-pdf` in Chrome (get_page_text empty); Wayback availability API returns no snapshot for 26efw2.pdf or 26efw2c.pdf. Owner must download 26efw2.pdf (also reachable only through SSA). Version/revision date, record layouts and signature rules remain open.

**p5 / US-MQ-10 federal mobile-worker statutes - ANSWERED (80%)** (round 1 -007/-008/-009 unchanged). 26 U.S.C. 3306(c) read: it has no localization text (the uniform rule is state law, see MULTI p5); no new finding.

**p6 / US-MQ-12 special populations - PARTIAL (88%).** New: FEIE for taxable years beginning in 2026 = USD 132,900 (Rev. Proc. 2025-32, sec. 3 item .39, IRC 911(b)(2)(D)(i)); same text: expatriation reduction USD 910,000 (item .38) [US-FEDP52-002, A.2, effective 2026-01-01, read locally]. Pub 51 (discontinued) / Pub 15 coverage, farm, household, election worker thresholds, Pub 54 withholding on citizens abroad: round 1 (-002/-003/-004). Pub 54 read only to character 100,000 of 359,000 in round 1; not re-read. Owner limb (matrix sign-off) is the owner's.

## MULTI

**p1** not applicable (federal tax on FED).

**p2 / US-MQ-03 state notice language (51) - PARTIAL (about 4 of 51, unchanged).** MN and NY read in round 1; CA 2810.5 in Chrome: leginfo returns no text (`gated`, page opens but get_page_text empty; WebFetch 403). The DOL page on state pay-day requirements read this round (dol.gov/agencies/whd/state/payday) lists only pay frequency, no pay-statement or language column, so it cannot be used to prove absence. Needed to close: one pay-statement/wage-notice statute read per state (state shards part 6). Not closed.

**p3 / US-MQ-05 state levy list - PARTIAL (72%, up from 60%).** New, official all-state frame from the DOL Comparison of State UI Laws, edition reflecting law as of 2023-01-01 (2024-2026 editions: expected URLs 404; the OUI index page lists no link in extractable text):
- Employee UI contributions exist in only three states: AK (27% of average benefit cost rate, 0.5-1.0%), NJ (0.425%), PA (0.0-0.08%) [US-FEDP52-006]. So "employee SUI contribution: no" for the other 48 + DC is supported at the 2023 edition; 2026 rates must come from the AK, NJ, PA state shards.
- Employee/employer temporary disability programmes: exactly six - CA, HI, NJ, NY, PR, RI (PR outside the 51) [US-FEDP52-007]; 2023 contribution table carried with a stale flag.
- PFML/LTC levies are outside the DOL UI Comparison; the DOL paid-leave page was not reachable (404 on guessed URLs); round-1 list (CA, CO, CT, DE, DC, HI, NJ, NY, OR, RI, WA, MN, plus MD/MA/ME not located) stands. Transit/workforce levies outside NY: not located.

**p4 / US-MQ-09 state POA/agent forms (withholding AND UI) - PARTIAL, improved.** Closed this round:
- TX UI: Form C-42 page (Wayback 2026-03-13): authorises an individual or service company to represent the employer in all matters before TWC; submitted online in UTS (Account Info, Third Party Authorization). TX has no wage income tax [US-TXP52-008].
- IL UI: IDES Service Bureau MOU (POA option) and E-POA bulk-upload format (rev. 9/5/17): POA copy retained, produced within 72 h; upload FEIN + 7-digit UI account number + correspondence flags + termination flag; one file per business day, max 1,000 rows [US-ILP52-009/010]. IL withholding (IDOR IL-2848 already read, US-IL-004).
- MI withholding: Treasury Form 151 Rev. 11-21 (Wayback 2025-09-06) and the Tax Professionals eService page (Wayback 2026-04-10): Form 151 must be on file for SUW accounts [US-MIP52-011/012]. MI UI (UIA 1488): not read.
Remaining: about 30 states not read (AZ authorization page Cloudflare-gated; NJ M-5008-R unreadable-pdf; NY POA-1/IA 900 already via Wayback in US-NY-012). The 51-state matrix is not complete.

**p5 / US-MQ-10 state sourcing, credit, thresholds, SUI localization - PARTIAL (improved).** SUI localization four-test text now read from an official all-state source: order of application (1) localized; (2) base of operations (place the worker starts work and customarily returns for instructions); (3) place of direction or control; (4) residence [US-FEDP52-005, A.2, law as of 2023-01-01]; it states the provisions were put into all states' laws in the 1940s from DOL model legislation, so one text covers all states at the policy level; state statute citations remain per-state (only FL 443.1216 read, US-MULTI-001). Resident credit rule per state, nonresident day/dollar thresholds: not read here (state shards).

**p6 / US-MQ-12 matrix** - federal rows only (FED p6); state matrix not built.

## FILING (PROCESSO-FILING-TERCEIROS.md, "O que falta" table)
- EFW2 2026 (version, records, signature/PIN): STILL OPEN (gated, see FED p4) [US-FEDP52-013].
- TX C-42: CLOSED on the authorisation limb (US-TXP52-008). TWC wage-report layout (ICESA/TXUS): not read.
- IL (IDES POA upload): CLOSED for UI (US-ILP52-009/010). IDES ICESA/CSV layout and IDOR FSET: not read.
- MI Treasury 151: CLOSED (US-MIP52-011/012). UIA 1488 and SUW 2026 handbook: not read.
- FL RT-6 layout, PA DOR batch, GA DOR G-7 batch, NC DOR POA: not attempted this round.
- Market: unchanged (vendor pages; a TX tier-B help page seen in search is not used).
The process note was NOT edited (not my file); the filing window should add the TX/IL/MI lines and the P5-2 ids.

## Status after this round

| Entry | p1 | p2 | p3 | p4 | p5 | p6 |
|---|---|---|---|---|---|---|
| FED | answered | absence_proven | partial | partial | answered | partial |
| MULTI | n/a | partial | partial | partial | partial | partial |
| FILING | partial | n/a | n/a | partial | n/a | n/a |

Gated or unreadable: ssa.gov/employer/efw/26efw2.pdf (unreadable-pdf, no Wayback); leginfo CA 2810.5 (no text); acf.gov IWO form page (redirect, no date); reginfo.gov (domain-change check); michigan.gov live pages (403 to WebFetch, read via Wayback); omb.report (403).
Confidence summary: FED p1 90%, p2 85%, p3 80%, p4 85%, p5 80%, p6 88%.
