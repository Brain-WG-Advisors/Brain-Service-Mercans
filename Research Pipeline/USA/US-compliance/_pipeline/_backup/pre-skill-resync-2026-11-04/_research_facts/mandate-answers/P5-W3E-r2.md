# PASS 4 round 2 (wave 3E, 2026-10-29) - RI, SD, ND, MT

Method: different sources from round 1 - statute sites (ndlegis.gov, sdlegislature.gov, mca.legmt.gov), agency lists (SD DOR municipal tax guide), legislative fiscal staff report (RI), Wayback 2026 snapshots saved under 00-official-sources/pdfs/<UF>/ and read locally with PyMuPDF (python -I). Budget: about 12 reads per state. Chrome: one own tab, tax.ri.gov PDF showed the Cloudflare bot check (gated, not bypassed); tab closed. No javascript_tool. Wayback pace: one request per 10 s; one HTTP 429 handled by a 60 s wait. Shard: mandate-P5-W3E-r2.csv (11 rows, ids US-<UF>-P5-2-NNN). Parts not listed below keep their round 1 status (P5-W3E-r1.md).

## RI - Rhode Island
- Part 2 (local wage tax): ABSENCE PROVEN, US-RIP52-001. House Fiscal Advisory Staff Local Aid report, October 2025: "the statutory prohibition preventing Rhode Island cities and towns from levying local option sales or income-based taxes"; property tax 96.9% of local tax revenue. Confidence M-H (the report does not cite the statute section; the Division list of taxes and the withholding booklet show no local wage tax either).
- Part 5 (multistate): ANSWERED. Reciprocity: none stated; the nonresident withholding instruction (booklet 2026, instruction 3 and 13) requires RI withholding on RI-source compensation of other-state residents with no exemption, and other-state employers may withhold RI tax voluntarily (convenience); keyword scan of the booklet for reciprocal/agreement/compact finds nothing (US-RIP52-003, effective 2026-01-01). Resident credit: 2025 RI-1040 resident instructions Schedule II - credit is the smallest of RI tax, tentative credit (RI tax x other-state income / modified federal AGI, capped 1.0000) and tax due and paid to the other state; RI-1040MU for several states (US-RIP52-002, tax year 2025). Statute section for the credit not located (the booklet does not cite it; the earlier guess 44-30-74 is not confirmed; Wayback has no copy of any 44-30 section page). Nonresident day/dollar thresholds: none stated in the booklet. Confidence M-H.

## SD - South Dakota
- Part 2: ABSENCE PROVEN, US-SDP52-001. DOR Municipal Tax Guide (July 2026, 13 pages) lists every municipal tax DOR administers (sales/use, gross receipts, tourism, telecom, motor vehicle, Sioux Falls lodging) with no income/payroll/wage tax; full text of SDCL Title 9 (municipalities) has no income or payroll tax authority. Confidence M-H.
- Part 4: ABSENCE PROVEN for the statute scope, US-SDP52-002. Full text of SDCL Titles 60, 61, 62 has no family leave, medical leave, temporary disability or payroll-tax levy; no employee UI contribution (round 1 handbook, US-SDP51-002). Confidence M-H.

## ND - North Dakota
- Part 2: ABSENCE PROVEN by enumeration, US-NDP52-001 (NDCC 40-05.1-06: home rule city taxes enumerated, later ordinances may not levy any tax not specified; no income/wage tax). Limit: non-home-rule cities and counties not read separately (they have only delegated powers). Confidence M-H.
- Part 4: ABSENCE PROVEN, US-NDP52-002/003. NDCC 34-01-15.1 shows no state paid family leave programme; 52-06-31 prohibits deducting UI contributions from wages (no employee UI contribution); chapters 34-02/03/05/06/14, 52-04, 65-01/04/05 scanned for TDI/PFML/employee levy: none. Workforce Safety and Insurance premiums are employer-paid workers compensation (title 65), not read in detail. Confidence M-H.

## MT - Montana
- Part 2: ABSENCE PROVEN (statutory), US-MTP52-001. MCA 7-1-112: self-government local governments cannot authorize a tax on income without delegation; no delegating statute located. Confidence M-H.
- Part 4: ABSENCE PROVEN, US-MTP52-002/003. Title 39 has 23 chapters, none for family leave, medical leave or temporary disability insurance; 39-51-3103 bars wage deductions for UI contributions (no employee contribution). Confidence M-H.

## Open after round 2
- RI statute sections (resident credit; local prohibition) text not read: webserver.rilegislature.gov refuses the connection and Wayback has no copies of 44-30 section pages. tax.ri.gov gated in Chrome (Cloudflare).
- Items were read via WebFetch for mca.legmt.gov (scripted fetch blocked); text is verbatim excerpt from the tool, not saved as a file.
