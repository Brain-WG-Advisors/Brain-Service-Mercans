# Mandate answers P5-FED-r1 - FED, MULTI, FILING (PASS 4, 2026-10-29)

Worker: compliance-source-hunter. Register shard: `00-official-sources/_register-shards/mandate-P5-FED-r1.csv` (ids US-FEDP51-001..018). Sources order used: WebFetch, Claude in Chrome (own tab, closed), Wayback availability check (no 2025/2026 snapshots for SSA 26efw2.pdf, TX C-42; Pub 51 only 2024, rejected). No javascript_tool, no filter bypass. About 35 reads. Part mapping for the three entries: p1 = federal tax (US-MQ-02), p2 = language (03), p3 = levies list (05), p4 = POA/filing (09), p5 = multistate (10), p6 = special populations (12).

Housekeeping note: while writing my script I deleted `scratchpad/mk.py` (14:12, an older temporary script of an earlier worker, not a deliverable) by mistake. Nothing in the register or answers depends on it.

## FED (federal layer)

**p1 / US-MQ-02 currency, rounding - PARTIAL (90% on rounding, USD limb open).** Rounding unchanged from pass 2 (US-FED-001/005/007/027): Pub 15-T rounding optional, Form 941 in cents. New: 31 U.S.C. 5103 says US coins and currency are legal tender for taxes [US-FEDP51-001, A.3 LII]. W-2 instructions require decimal point and cents [US-FEDP51-012]; no sentence requiring USD found in the 100,000 of 280,104 characters read. Gap: an instrument that states federal returns/W-2 must be in USD (likely only implicit; remaining 180k chars of the W-2 instructions and the 941 instructions not scanned for "U.S. dollars"). Confidence 85%.

**p2 / US-MQ-03 language - ABSENCE PROVEN at federal level (85%).** No federal instrument fixes payslip or filing language: US-FED-020 (English designation, no private-employer duty) and US-FED-010 (29 CFR 516.2 records only). State side is in the MULTI entry.

**p3 / US-MQ-05 devolved domains, federal part - PARTIAL (70%).** IWO: the required standard form, OMB 0970-0154, FR notice of 2023-07-12 (prior approval expired 2023-09-30; 3-year extension) [US-FEDP51-005]. Priority: honor the IWO before other garnishments except an earlier-entered IRS levy [-006]. CCPA limits and new-hire reporting unchanged (US-FED-011/017). NOT LOCATED: current OMB expiration and the PDF URL of the form (acf.gov form page redirects to the employer page).

**p4 / US-MQ-09 federal filing instruments - PARTIAL (85%).** Form 8655 / Pub 1474 / Rev. Proc. 2012-32 closed earlier (US-FED-008/028, US-FIL-001). EFW2 TY2026: still NOT READ - `26efw2.pdf` gives 403 to WebFetch, no text in Chrome (`unreadable-pdf`, owner to download), no Wayback snapshot [-013, gated]. Version and revision date remain unconfirmed (SSA landing page: Publication 42-007).

**p5 / US-MQ-10 federal mobile-worker statutes - ANSWERED (80%).** 49 U.S.C. 14503 (motor carrier employees with regular duties in 2+ States are taxed only by the residence State; the 50 percent time test applies to the water-carrier limb; effective 1996-01-01) [-007]; 49 U.S.C. 11502 (rail: residence State/subdivision only, information returns only there, no 50 percent test) [-008]; 4 U.S.C. 114 is retirement income only, not wages [-009]. There is no federal statute limiting State taxation of general mobile employees. Reads came through the WebFetch summarizer (A.3 LII): check subsection letters before quoting in the CCG. Airline (49 U.S.C. 40116) and vessel (46 U.S.C. 11108) statutes not read.

**p6 / US-MQ-12 special populations - PARTIAL (85%).** Pub 51: discontinued; the IRS page says it will no longer be revised (2024-01-23) [-003] and Pub 15 (2026), read locally, says Pub 15 is for all employers incl. agricultural and territories [-002]. Farmwork: 150 USD per employee or 2,500 USD total tests; FUTA farmworkers 20,000 USD in a quarter or 10 workers in 20 weeks; household 3,000 USD; election workers 2,500 USD; H-2A not statutory employees [-002]. Pub 54 is a continuous-use revision (Dec 2025) without the inflation-indexed amounts; employer withholds on US citizens abroad unless foreign law requires foreign withholding; none if the FEIE is reasonably expected (first 100k of 359k chars) [-004]. The FEIE 2026 amount sits in Rev. Proc. 2025-32 (US-FED-002/025), not re-extracted. Clergy and students unchanged (US-FED-029/030). The owner limb of the matrix (US-MQ-12) remains the owner's.

## MULTI (cross-state census)

**p1** not applicable at this level (federal tax is on FED).

**p2 / US-MQ-03 state primary-language notices (census of 51) - PARTIAL, about 4 of 51.** Read and active: MN (Minn. Stat. 181.032 hire notice in English with right to request another language, US-MNPAY-001) and NY (Labor Law 195(1)(a) hire notice in English and primary language, US-NY-004). CA Labor Code 2810.5: read attempt failed (403 and no Chrome text) [-018, gated]; the rule is a lead only. DC Code 32-1008: page opened in Chrome but the statute body was truncated in the tool output; not confirmed. The other 45+ states: no read; do not model. Absence proof for any state needs its own pay-statement/wage-notice statute read (belongs to each state shard part 6).

**p3 / US-MQ-05 state levy list (SDI/PFML/LTC/transit) - PARTIAL (60%).** DOL page: 13 states plus DC have paid family and medical leave programmes; Hawaii has paid temporary disability; NH, VT, VA voluntary; the page does not name the 13 [-011, undated]. Named from state shards (employee/employer levy 2026): CA SDI 1.3% (US-CAEDD-001/004); CO FAMLI 0.88% split 0.44/0.44 (US-COFAMLI-001); CT 0.5% employee (US-CTPL-001); DE Paid Leave (rate not in shard); DC PFL 0.62% employer only (US-DCPFL-001); HI TDI weekly cap 1,500.21 (US-HI-003); NJ UI/TDI/FLI employee shares (US-NJ-002); NY MCTMT (US-NY-003), DBL/PFL via insurers (US-NY-005, M); OR Paid Leave 1.0% (US-OR-002); RI TDI/TCI (US-RI-003); WA PFML 1.13% and WA Cares 0.58% employee (US-WAPFML-001, US-WALTC-001); MN Paid Leave gated (US-MNPFML-001). NOT LOCATED on a read page: MD, MA, ME, VT, NH (voluntary, US-NH-004 read), transit/workforce levies outside NY. DOL UI table [US-FEDP51-010] added as the official all-state cross-check for SUI wage bases.

**p4 / US-MQ-09 state POA/agent forms, withholding AND UI (51) - PARTIAL.** Read and active before this pass: CA DE 48 (UI/SDI/PIT, US-FIL-005), PA REV-677 and UC handshake (US-FIL-009/010), OH WT 8655 plus bulk filer (US-FIL-011/012), NC DES POA and GEN-58 (US-FIL-013, US-NCW1B-002), FL DR-835 (US-FIL-015), GA RD-1061 and RD-1062 (US-GAW1B-003), IL-2848 (US-IL-004). New this pass: MA withholding - M-2848 does not give MassTaxConnect account access; payroll provider uses third-party access initiated in MassTaxConnect with online or paper approval (page updated 2023-03-21) [-014]. CO UI - no paper POA: TPA account in MyUI Employer+ associated with the employer EAN, employer approves; withholding POA DR 0145 is only a search-result lead [-015]. WA UI - POA form per client company, TPA in the representative sections, mail or fax; WA has no wage income tax [-016]. Gated: NJ M-5008-R (6/26) opened without text, coverage of withholding unconfirmed [-017]; TX C-42 (twc.texas.gov geo-block, no Wayback snapshot); MI Forms 151/1488; IL IDES; NY POA-1 and IA 900 (US-NY-012 has them read via Wayback); AZ payroll service company authorization (Cloudflare "Just a moment", not solved). Remaining about 35 states: not read.

**p5 / US-MQ-10 state sourcing, credit, thresholds, SUI localization - PARTIAL.** Reciprocity pairs, convenience rules and thresholds unchanged from pass 2 (see FED-MULTI.md). New: CO page tells TPAs that out-of-state wage credit requests are manual and multi-state wages must be reported correctly [-015]. Federal mobile-worker statutes: see FED p5. SUI four-test text: the uniform localization provision is read only in FL 443.1216 (US-MULTI-001); no second state statute read this pass. Resident-credit rule and nonresident day/dollar thresholds for the other states: not read here (state shards).

**p6 / US-MQ-12 matrix** - federal rows only (FED p6); state matrix not built.

## FILING (PROCESSO-FILING-TERCEIROS.md, "O que falta")

Table items and status after this pass:
- EFW2 2026 version, records, signature/PIN: STILL OPEN (gated, unreadable PDF; owner download) [-013].
- TX C-42 and TWC layout: STILL OPEN (no snapshot, geo-block). IL IDES/IDOR FSET: STILL OPEN (host unreachable on this machine). MI UIA 1488 / Treasury 151 / SUW 2026: STILL OPEN here (a Michigan 446 Withholding Guide 2026 tab belongs to another worker).
- FL RT-6 layout, PA DOR, GA DOR, NC DOR POA/lot: PA, GA, NC, FL form-level POA are now read in the register (US-FIL-010/013/015, US-GAW1B-003); layouts RT-6 not read.
- Market: unchanged (vendor pages only).
New filing facts: MA, CO, WA agent mechanics above. The process note itself was NOT edited (this worker writes only its own files); the owner or the filing window should add the MA/CO/WA lines and the P5 ids.

## Status after this pass

| Entry | p1 | p2 | p3 | p4 | p5 | p6 |
|---|---|---|---|---|---|---|
| FED | partial | absence_proven | partial | partial | answered | partial |
| MULTI | n/a | partial | partial | partial | partial | partial |
| FILING | partial | n/a | n/a | partial | n/a | n/a |

Gated or unreadable URLs: ssa.gov/employer/efw/26efw2.pdf (unreadable-pdf); leginfo CA 2810.5; nj.gov m5008r.pdf (unreadable-pdf); azdor.gov (anti-bot); acf.hhs.gov and acf.gov form page (403/redirect); irs.gov/pub/irs-pdf/p51.pdf (404, discontinued); law.justia.com (403); web.archive.org blocked inside WebFetch (curl availability API used for checks only).
