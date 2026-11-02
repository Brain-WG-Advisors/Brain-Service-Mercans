# PASS 4 (wave 3E, 2026-10-29) - RI, SD, ND, MT

Method: WebFetch (non-blocked hosts), Wayback copies (2025/2026 snapshots saved under 00-official-sources/pdfs/<UF>/ and read locally with PyMuPDF, python -I), Claude in Chrome own tab (tax.ri.gov showed a bot-verification page: recorded gated, not bypassed; webserver.rilegislature.gov refused the connection). No javascript_tool. Shard: mandate-P5-W3E-r1.csv (18 rows). Parts worked = those listed missing in build-manifest `_seal_assessment_2026-10-29`; nothing from other PASS 4 sections applied to these four states.

## MT - Montana (US-MQ-46) - 6/6 touched; 4 answered, 2 partial
1. ANSWERED (US-MTP51-001/002). Effective 2026-01-01 (HB 337): annual table single/MFS 0% to 16,100, 4.7% to 63,600, then 2,233 + 5.65%; method now mirrors federal (federal standard deduction, no Montana allowances); amounts rounded UP to the nearest dollar; supplemental paid separately: aggregate method or flat 5 percent (guide text; a search summary said 6 percent and is wrong); certificate MW-4. Confidence H.
2. PARTIAL. Guide (21 pages) describes state withholding only and mentions no local wage tax; no positive statement that none exists. Confidence M-L.
3. ANSWERED (US-MTP51-005). 2026 base 47,300; new-employer rate by industry 1.00% to 2.00% (construction 2.00, services 1.10, ag/mining 1.30) plus Administrative Fund Tax 0.18%; employer-paid, no employee contribution on the sheet. Confidence H.
4. PARTIAL. No SDI/PFML/LTC levy appears in the guide or UI sheet; absence not proven by an official statement (search summary only says no state paid family leave; not used). Mineral royalty withholding 5.65% (2026) is not a wage levy. Confidence M-L.
5. ANSWERED (US-MTP51-003/004). Reciprocity with North Dakota only (Form MW-4 for ND residents); nonresident wages withheld unless under 30 days in Montana and more than one state worked (exclusions listed). Resident credit statute not read. Confidence H.
6. ANSWERED (US-MTP51-001/006/007). Pay statement MCA 39-3-101; POA: Montana Form POA (mail or TAP) or federal 2848 covering the employer return; UI POA/agent form not located; prevailing wage: state law exists, threshold 25,000 (DOL table, medium; statute not read); oracle: no calculator, official tables and formula (W = A + B x (G - C)) in the guide; primary-language notice: none found. Confidence M-H.

## RI - Rhode Island (US-MQ-59) - parts 1,2,5,6 touched; 2 answered, 2 partial
1. ANSWERED (US-RIP51-001). 2026 booklet: RI W-4 required in addition to federal; supplemental withholding rate 5.99%; tables and percentage method; no rounding rule stated in the booklet (real read). This corrects the earlier shard text "supplemental per federal method". Confidence H (rounding: not stated).
2. PARTIAL. Booklet and withholding page describe state withholding only; no local wage tax mentioned; no positive statement. Confidence M-L.
5. PARTIAL. Employers must withhold RI tax on nonresidents for RI-performed services; convenience withholding for RI residents with other-state employers (booklet instructions 3 and 13). No reciprocity agreement is stated in the booklet. Resident credit (RIGL 44-30-74) not read (Wayback has no copy). Confidence M.
6. ANSWERED (US-RIP51-002/003/004/005). Pay statement RIGL 28-14-2.1 (hours worked, deductions with explanation); prevailing wage RIGL 37-13-7 (Director of Labor and Training, contracts over 1,000); POA Form RI-2848 (Division of Taxation; use for a withholding filer inferred, not stated); UI POA not located; oracle: no calculator, percentage method and tables in the booklet; primary-language notice: none found. Confidence M-H.
Gated: https://tax.ri.gov/... (bot verification page in Chrome; copy taken from Wayback); https://webserver.rilegislature.gov (connection refused; Wayback used).

## SD - South Dakota (US-MQ-61) - parts 2,4,6 touched; 1 answered, 2 partial
2. PARTIAL. No state income tax (US-SD-001); no official statement on local wage taxes found. Confidence M.
4. PARTIAL. Handbook (Rev 07/2022, 25 pages) and FAQ: administrative fee not deductible from wages; no employee contribution, SDI or PFML appears (US-SDP51-002). Absence limited to these documents. Confidence M.
6. ANSWERED with one gap. Pay statement: SDCL 60-11 has no content provision (US-SD-003, earlier); UI POA: DLR Form POA Rev 01/2026 (tax, benefits, limited) (US-SDP51-001); withholding POA and calculator: not applicable (no wage tax); prevailing wage: none per DOL table (medium, US-SDP51-003; SDCL 5-18A is procurement). Confidence M.

## ND - North Dakota (US-MQ-48) - parts 2,4,6 touched; 1 answered, 2 partial
2. PARTIAL. Withholding guideline (31 pages) mentions no local wage tax; no positive statement (US-NDP51-001). Confidence M-L.
4. PARTIAL. No SDI/PFML/LTC levy on the pages read (guideline, UI schedules PDF read locally in pass 3: US-ND-004/005); absence not proven by an official statement. Confidence M-L.
6. ANSWERED with one gap. Pay statement: NDCC 34-14 has no content provision (US-ND-003); POA: Form 500 (Tax Commissioner), TAP Third party access; Job Service ND designated employer representative page not read (search listing only); prevailing wage: none per DOL table (medium, US-NDP51-003); oracle: withholding rate booklet tables (US-ND-001); primary-language notice: none found. Confidence M.

## Remaining gaps for the owner / next pass
- MT: UI POA or agent form (uid.dli.mt.gov host did not resolve; Wayback has only the rate sheets); explicit statement on local taxes / SDI.
- RI: resident credit statute 44-30-74; RI DLT UI POA; RIGL 44-30-71 text.
- SD, ND: official absence statements for local wage tax and SDI/PFML; ND Job Service POA page.
- Prevailing-wage rows rest on a WebFetch summary of the DOL table (revised 2023-01-01); read the DOL PDF itself to raise to H.
