# Mandate answers R3-FED - US-MQ-03, US-MQ-05, US-MQ-12 (round 3, 2026-10-30)

Hunter: compliance-source-hunter. Register: `00-official-sources/_register-shards/mandate-R3-FED.csv` (11 rows, ids US-FEDR3-NNN). Route: WebFetch, Claude in Chrome own tab (get_page_text / find / read_page only, no javascript_tool, tab closed), then Wayback 2026 `id_` copies read locally with PyMuPDF (`python -I`), one request per 10 s, one 429 retry after waiting. No CAPTCHA, no login. MANDATE.md and build-manifest.json untouched.

Result: **closed: none. Still open: MQ-03, MQ-05, MQ-12 (narrowed).** Nothing is presented as sealed. What moved is listed per question; the remaining gap is exact.

Network limits met (so the next worker does not repeat them): ilga.gov, malegislature.gov, reginfo.gov (redirects to another domain, tool check refuses), web.archive.org through WebFetch (blocked), omb.report and the AZ DES policy site (403), maine.gov (CloudFront geo-block, also inside the Wayback copy), live acf.gov PDFs (no extractable text = `unreadable-pdf`).

## US-MQ-05 - federal IWO and state levy list

### Federal IWO form OMB 0970-0154 - NOT CLOSED (renewal outcome unknown)
- The form header says `Expiration Date: 08/31/2026` [US-FEDR3-003, Wayback 2026 copy, pymupdf].
- Renewal steps are in the Federal Register: 60-day notice 2026-03-11 (comments to 2026-05-11) [US-FEDR3-001] and 30-day OMB-review notice 2026-07-10 (ICR 202607-0970-002, comments to 2026-08-10) [US-FEDR3-002]. Both say "The current OMB approval expires August 31, 2026". The notices request approval; they do not grant it.
- The FR notice prints "Authority: 42 U.S.C. 666(a)(1), (a)(8), and (b)(6)": the 666(b)(6) citation is now backed by the agency text, no longer only the LII summarizer [US-FEDR3-001]. The statute text itself was not read.
- The extension is NOT confirmed. Search summaries disagree: one-year extension to 2027-08-31 (state agency and court-rules pages) versus 08/31/2029 (acf.gov instruction snippet, mirror) [US-FEDR3-004, `gated`]. Do not model any date. The decisive page is reginfo.gov ICR 202607-0970-002 or the live acf.gov PDFs; both are unreachable for the tools. **Owner action (30 s):** open https://www.reginfo.gov/public/do/PRAViewICR?ref_nbr=202607-0970-002 and read "Expiration date", or open https://acf.gov/sites/default/files/documents/ocse/omb_0970_0154.pdf and read the header.
- Practical consequence for the build: the IWO continues to be honoured after the printed expiry (ACF instruction text: the IWO sent on a case does not expire on the OMB date; seen in the 2026-03-21 Wayback instructions copy). Treat the printed date as a data item with `expiry_status = renewal pending/unknown`.

### State levy list (SDI/TDI, PFML, LTC, transit/other) for all 51 - compiled from the register, with sources
Employee- or employer-side payroll levies that exist in 2026 (rate, vigência, register id). Every figure was read from the cited row (page or statute); the compile itself is mine.

| Jurisdiction | Levy | 2026 figure (vigência) | Register id |
|---|---|---|---|
| AK | employee UI contribution | 0.50% (2026-01-01 to 2026-12-31) | US-AKUI-001 |
| CA | SDI (employee) | 1.3%, no wage cap since 2024-01-01 | US-CAEDD-001, US-CAEDD-004 |
| CO | FAMLI | 0.88% (0.44 employer + 0.44 employee), to the OASDI cap | US-COFAMLI-001 |
| CT | Paid Leave | 0.5% employee deduction, to the OASDI cap | US-CTPL-001 |
| DE | Paid Leave | 0.8% combined (public plan), employer 10+ | US-DEP51-001, US-DEPL-001 |
| DC | Paid Family Leave | 0.75% 2026, employer-only, may not be deducted | US-DCP51-010, US-DCP51-011 |
| HI | TDI (employee share) | max 0.5% of weekly wage, max 7.50/week (2026) | US-HI-003 |
| MA | PFML | 0.88% (employers 25+) | US-MAP51-006 |
| MD | FAMLI | NO 2026 contribution; 0.9% from 2027-01-01 | US-MDP51-003, -004 |
| ME | PFML | ceiling 1.0% (26 MRSA 850-F); exact 2026 rate NOT read (geo-block) | US-MEP51-002, US-FEDR3-011 |
| MN | Paid Leave | 0.88% (family 0.27 + medical 0.61) | US-MNP52-003 |
| NJ | UI/DI/WF/FLI (employee) | 0.3825 / 0.19 / 0.0425 / 0.23 (2026) | US-NJP51-003, US-NJ-002 |
| NY | PFL / DBL / MCTMT | PFL 0.432%; DBL 0.5% max 0.60/week; MCTMT employer | US-NY-005, US-NY-010, US-NY-003 |
| OR | Paid Leave, statewide transit, WBF, TriMet/Lane | 1.0%; 0.1% employee; WBF 0.018; TriMet 0.008237, Lane 0.0080 | US-OR-002 |
| PA | employee UC | 0.07% (2023 onward) | US-PA-003 |
| RI | TDI/TCI | 1.1% to 100,000 | US-RI-003 |
| WA | PFML; WA Cares (LTC); workers' comp medical-aid share | 1.13%; 0.58%; employer deducts half of medical-aid per class | US-WAPFML-001, US-WALTC-001, US-WALTC-002 |
| Not yet in force | VA paid leave | benefits and premiums from 2028-04-01 | US-VAP51-004 |
| Voluntary only | NH, VT | no mandatory levy | US-NH-004, US-VTP51-006 |
| Bill only | NM | do not model | US-NM-004 |
| Employer-only business taxes | NV MBT | general business 1.17% from 2023-07-01 (first 50,000 of wages non-taxable, NRS 363B.110) | US-NVP51-002 |

All other states: no SDI/TDI/PFML/LTC levy, shown by absence from the federal lists (DOL TDI list CA, HI, NJ, NY, RI [US-FEDP52-007]; DOL Women's Bureau paid leave list [US-PAP51-005, US-LAP52-002]) and by per-state absence proofs in the pass-4/R3 shards. This is the same absence basis as "route (d)" in the seal assessment, which the owner has not accepted; the 51-row matrix is therefore **complete as a list but its absences stay at the weaker basis for AL, AZ, KY, MO, TX, WI, WV**.

Gaps that keep MQ-05 open: (1) IWO renewal date (above); (2) Maine 2026 PFML rate (primary page geo-blocked); (3) transit/workforce levies outside NY/OR: none located, but no state-by-state absence proof exists for them (confidence Medium); (4) MD FAMLI is settled (no 2026 contribution).

## US-MQ-12 - special-populations matrix L10 (sources finished; OWNER sign-off still pending)
Sources read this round, all from the primary text:
- Statutory employees [US-FEDR3-005]: Pub. 15-A (2026), four categories; FICA withheld, **no** income tax withholding, W-2 box 13; FUTA only for categories 1 and 4.
- Agricultural [US-FEDR3-006]: Pub. 15 (2026) $150 / $2,500 tests, FUTA farmworkers $20,000 per quarter or 10 workers in 20 weeks, Form 943. Pub. 51 was discontinued (IRS about page, "will no longer be revised -- 23-JAN-2024"), so the earlier 404 is explained and Pub. 51 is no longer a source to chase.
- Employees abroad [US-FEDR3-007]: Pub. 54 (12/2025) read in full from the local page text: Form 673 mechanics, American-employer and foreign-affiliate FICA coverage, totalization. Pub. 54 no longer prints the FEIE amount (it points to the Rev. Proc.); earlier register note of FEIE 132,900 stays attached to US-FED-025 and is not restated here.
- Already in the register: NRA [US-FED-001, US-FED-004], household/Schedule H [US-FED-004, US-FED-007], students and abroad (Pub. 15) [US-FED-029], clergy [US-FED-030], election workers (Pub. 15 2026: $2,500).
Remaining: the **owner must accept the L10 matrix** (IN: ordinary employees, NRA, statutory employees; FLAG/OUT: household, agricultural, clergy, employees abroad). That is a decision, not a source gap. Confidence on the research limbs: 90%.

## US-MQ-03 - language rules (census of 51) - NOT CLOSED
Read from the primary or agency text this round (earlier rows unchanged: federal English designation [US-FED-020], 29 CFR 516.2 no language and no pay statement [US-FED-010]):

| State | Rule | Basis | Register id | Confidence |
|---|---|---|---|---|
| CA | Hire notice (Lab. Code 2810.5) in the language the employer normally uses to communicate employment information; DLSE templates in Spanish, Chinese, Korean, Vietnamese, Tagalog; own form allowed | Labor Commissioner FAQ rev. 2016-03-11, chrome-read; statute text on leginfo still gated | US-FEDR3-009 | Medium-High |
| NY | Hire notice (Lab. Law 195(1)(a)) in English and in the employee's identified primary language where a Commissioner template exists; signed acknowledgment in both; otherwise English only | nysenate.gov, chrome-read earlier [US-NY-004], quoted again via WebFetch this round | US-NY-004 | High |
| MN | Hire notice in English, employee may request another language | Minn. Stat. 181.032 | US-MNPAY-001, US-MNR3-005 | High |
| DC | Written notice at hire in English and, where the Mayor has a template, in the primary language | D.C. Code 32-1008(c) | US-DCP51-012 | High |
| NJ | Earned sick leave notice in the primary language if on the NJDOL website; scope is the ESL notice, not wages | NJDOLWD guide, undated | US-FEDR3-010 | Medium (statute unread) |
| IL | No mandatory language: 820 ILCS 175/10(c) only has the Department recommend multilingual staff (day/temporary labor agencies). A search summary claiming a Spanish/Polish mandate was wrong | statute text, Wayback 2026-09-03 | US-FEDR3-008 | High |

- Bilingual documents: permitted wherever the statute fixes the notice language by "also in" (NY, DC) or lets the employer choose its usual language (CA); no state read prohibits a bilingual payslip. Not a proven universal statement.
- Authority-facing filings: English forms and instructions; no state or federal language statute found (unchanged).
- Census status: 6 of 51 states read for a language rule (CA, NY, MN, DC, NJ-ESL, IL negative). For the other 45 the pay-statement statutes in the pass-4/R3 shards carry no language clause where read, but a clause-by-clause absence statement per state has not been made. I did not try to infer absence from search results. **Still missing to close:** (1) CA statute text itself (leginfo gated: owner download or print-to-PDF); (2) the remaining 45 states' wage-notice or pay-statement provisions checked for a language clause (MA, MD, OR, WA, CO, CT, NM, HI, NV, RI and ME sick-leave or wage-notice laws are the likeliest, none verified; ilga.gov, malegislature.gov hosts unreachable from the tools this round); (3) the G-LANG employment-share axis for the `en` first build / `es` seam. Suggested owner decision to cut scope: accept "no federal language rule; state rules only where a CCG row cites them (CA, NY, MN, DC, NJ ESL); es seam rank by employment share" as the closing answer, and record that the other 45 were not individually proven absent.

## Bloco de prova
- **Pedido -> resposta:** MQ-03 (CA 2810.5, NY 195(1) done; census partial), MQ-05 (IWO: FR notices, form header, renewal unresolved; levy list for 51 compiled), MQ-12 (sources finished; owner acceptance pending).
- **Fontes:** FR 2026-04740 and 2026-13910 (govinfo PDFs, pymupdf); IWO form header (Wayback copy); Pub. 15-A, 15, 54 and IRS About Pub. 51 (irs.gov, local text); 820 ILCS 175/10 (Wayback copy of ilga.gov); CA Labor Commissioner FAQ (chrome-read); NJDOLWD guide (pymupdf); NY Labor Law 195 (nysenate.gov).
- **Teste:** register shard parses with 20 columns in all 11 rows; Pub. 54 WebFetch summary contradicted the local text and was corrected; the IL search summary was contradicted by the statute text and was corrected.
- **Confianca:** IWO form expiry and FR steps 98%; levy table figures per the cited rows 90% (compiled, not re-read); statutory/agricultural/abroad 95%; language census 35% complete, so MQ-03 is not presented as answered.
