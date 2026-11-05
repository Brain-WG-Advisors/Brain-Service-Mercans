# PSL fix R1 - facts ready (2026-11-04)

Scope: PSL-RQ-01..28 in `_research/PSL-research-request.json`. 17 were F44 misses (text not proven in the saved copy); 11 were open questions.
Backups: `_research/psl-fix/_backup/` (PSL-facts, register, gaps, request, ledger; MD5-BEFORE.txt). Writes under `_research/facts.lock`, released.
Web: 12 fetches (curl/Wayback id_/eCFR API; 3 WebFetch/curl probes failed: CA 403, IL refused, RI stale).

## A. The 17 F44 misses - all now 0 misses (f44_self: 160 tags, 0 misses; `validate_contract --all`: PASS 100 files)

| RQ | key | route | what changed |
|---|---|---|---|
| 01 | psl.ak.statement.content | reworded to copy | "FIT and FICA; AK ESA" -> "federal income tax and Federal Insurance Contribution Act deductions; Alaska Employment Security Act contributions" (8 AAC 15.100 list, pam100 p.51) |
| 04 | psl.ct.pay_code_guide.url_on_pay_record | reworded to copy | "URL" -> "Internet web site address ... on each record of hours" (PA 26-12 sec. 38, p.64) |
| 05 | psl.fed.statement.required | official copy downloaded | US-FED-010: eCFR 29 CFR 516.2 (version 2026-10-30) `ccg-sources/FED/FED_eCFR-29CFR516.2_2026-11-04.xml` |
| 06 | psl.hi.ssn.rule | reworded to copy, CORRECTED | copy of 487J-2(a)(5): bars printing an entire SSN on mailed materials UNLESS employer-to-employee communications or requested by the individual. The old value said mailing a visible full SSN is barred (wrong for payslips) |
| 09 | psl.ky.statement.content | reworded to copy | "KRS 337.070" -> "section 337.070" |
| 10 | psl.la.statement.scope | reworded to copy, still a limitation | saved copy is R.S. 23:631 only; value now "none read ... other sections not in the saved copy"; confidence low |
| 12 | psl.me.statement.content | reworded to copy | "26 MRSA 665(1)" -> "Title 26 section 665, subsection 1" |
| 13 | psl.mo.ssn.rule | reworded to copy | dropped "(since 2016)" (copy shows effective 28 Aug 2012; 2016 not proven); rule kept |
| 14 | psl.ms.statement.scope | reworded to copy, still a limitation | MDES posters page proves no statute; value now "none identified ... absence not proven by a statute copy"; confidence low |
| 16 | psl.nd.statement.content | reworded to copy | "NDAC 46-02-07-02(10)" -> "46-02-07-02, recordkeeping item 10" |
| 17 | psl.notice_language.co_comps | reworded to copy | "LEP" -> "limited English language ability" (COMPS 7.4.3) |
| 18 | psl.notice_language.ma | official copy added | US-MAL-002: Wayback 20261020174536 of malegislature.gov s.148C; (o) confirmed. Language list is by cross reference (c.151A s.62A(d)(iii)), not read |
| 19 | psl.notice_language.mi | official copy added + reworded | US-MIL-001: MCL 408.968(2) copy confirms English, Spanish, 10% language; "LEO" -> "the Department" |
| 20 | psl.notice_language.ny | existing copy bound | US-NYP51-003 -> `ccg-sources/NY/NY_LAB-195_2026-11-02.html` (LAB 195(1)(a) read) |
| 21 | psl.notice_language.or | official copy added | US-ORL-001: Wayback 20261013013758 of ORS 652 full text (652.610(6)(a)-(c) read). The row US-OR-004 copy was a short one and stays superseded |
| 25 | psl.sc.statement.exemptions | reworded to copy | exemption is from Section 41-10-30 (notification); "5" -> "five", "12" -> "twelve" |
| 27 | psl.tx.ssn.rule | reworded to copy | BC 501.001(a)(5): "material sent by mail"; dropped our gloss "mask on paper payslips" |

No number was changed; values with numbers (10+ employees, 100+, 10%, 3 years) are untouched. Each changed fact carries `_psl_fix_R1`; `_precheck_unmatched` removed from them.
Register rows with copy added (local_file, retrieved_on/verified_on, md5 appended to verification_method): US-FED-010 2f37f5b5..., US-MAL-002 01522db9..., US-MIL-001 d92a2d40..., US-NYP51-003 f4fe836e..., US-ORL-001 562cfb52....
Files kept under `00-official-sources/ccg-sources/{FED,MA,MI,OR}/` (all < 0.2 MB, each in one folder).

## B. The 11 open questions

Closed (1):
- RQ-15 NC retention: NC-30 (2026) Section 26, p.16, in the saved copy of US-NC-001: retain records at least **ten years** after the last filing or last payment, whichever is later. New fact `psl.nc.retention.withholding_records.years` = 10 (A.2, direct artifact inspection, effective 2026-01-01); figure added to the row; `PSL/8_sheets` added to its consumed_by.

Left open (10), with what was tried:
- RQ-02 CA electronic consent: leginfo LAB 226 403 by curl, Wayback and WebFetch. Closes with a browser read of LAB 226(a).
- RQ-24 RI 28-14-12 (2026 text): Wayback copy is the pre-2026 text (3 years, history to P.L. 1989), so not the H 5679 text. Closes with the enacted 2025 act or a current snapshot.
- RQ-07 IL 56 IAC 300.600: ilga.gov connection refused (curl, WebFetch); Wayback 404.
- RQ-03 CO, RQ-11 MA, RQ-22 NV, RQ-23 NY (electronic consent), RQ-08 IN, RQ-28 TX (scope confirmation), RQ-26 (SSN statutes of ~20 states): not an answer an official page gives quickly; RQ-26 is parallel by state and can be fanned out.

## C. Housekeeping
- `_research/gaps.json`: 18 PSL gaps set `closed-R1` (17 + RQ-15); the rest stay open. `PSL-research-request.json` left unchanged (builder owns re-issue).
- `PROPAGATION-LEDGER.md`: 3 lines added. The PSL workbook is not rebuilt (workbooks untouched); the builder must re-run for the 13 reworded cells, the HI correction and PSL-RQ-15.

STATUS: COMPLETE
