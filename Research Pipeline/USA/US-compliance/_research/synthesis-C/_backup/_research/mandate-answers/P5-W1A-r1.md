# Mandate answers P5-W1A-r1 - CA, TX, NY, FL, IL (PASS 4 wave 1, 2026-10-29)
Shard: 00-official-sources/_register-shards/mandate-P5-W1A-r1.csv. Only parts still missing/partial after earlier PASS 4 sections (G1 CA, G2 FL/IL, G4 NY, G6 TX) were worked. Budget ~10 reads/state; used ~3 per state (WebFetch, PyMuPDF on saved PDFs, 1 Chrome tab). Chrome get_page_text could not read the TX statutes site (script-rendered, only chapter title "CHAPTER 2258. PREVAILING WAGE RATES" shown); ILGA unreachable from this machine.

## CA
All five targeted parts (1,2,3,5,6) were already answered in G1 PASS 4. No new reads. Remaining caveat: Labor Code 226 text on leginfo returns HTTP 403 (gated again, https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=226.); part 6 rests on the DIR FAQ [US-CA-LAB-001], High.

## TX
- Part 3: statute Labor Code 204.006(a) (TWC compilation PDF) sets the new-employer rate as greater of major-group rate less 0.1 pt or 2.6% [US-TX-P5-1-001]. This contradicts the 2.70% in an earlier summary and in a search snippet; actual 2026 entry rate NOT read from TWC rates page (geo-blocked). Status: partial, Medium. Base 9,000 and range 0.32-6.32% stand from G6.
- Part 2/4: unchanged (absence, Medium); no explicit negative statement found.
- Part 6 prevailing wage: Gov. Code ch.2258 title "Prevailing Wage Rates" confirmed on the official site (text did not render); sections 2258.021 text still unread. Medium. Remaining parts unchanged from G6.

## NY
- Part 5: convenience rule text, 20 NYCRR 132.18, read on Cornell LII mirror (secondary): out-of-state days count only if necessity, not convenience [US-NY-P5-1-001]. Medium-high. Reciprocity: still no page states "no reciprocity"; no agreement located (Medium).
- Part 6: Labor Law 195(3) re-read on nysenate.gov [US-NY-P5-1-003] High. Prevailing wage Labor Law 220 read on nysenate.gov, Commissioner of Labor is fiscal officer on state projects [US-NY-P5-1-002] High. POA-1 and IA 900 unchanged. Oracle: none.
- Part 1 rounding: still NOT LOCATED as a rule (no new read). Part 2 unchanged (High).

## FL
- Part 6 pay statement: no general employer pay-statement section in Fla. Stat. ch.448 (2025); only labor pools, 448.24(2)(g) [US-FL-P5-1-001]. Medium-high (section index read through WebFetch extraction, not a keyword scan of full text). Not proven for the rest of the Florida Statutes.
- Part 6 prevailing wage: ch.255 first 100,000 of 281,447 characters show no wage-rate rule [US-FL-P5-1-002]; partial, Medium-low. No statewide private prevailing wage located.
- Parts 2,3,4: unchanged from G2 (answered; part 4 by absence, Medium). POA DR-835 unchanged.

## IL
- Part 5: Pub-130 February 2026 read in full (13 pp): reciprocity IA, KY, MI, WI via IL-W-5-NR, plus military-spouse; no convenience rule in the pub [US-IL-P5-1-001]. High (supersedes the Aug 2022 edition US-IL-003).
- Part 1: 4.95%, allowance 2,925, effective 2026-01-01 (IL-700-T R-12/25); rounding: NO rounding rule in the 22-page booklet (full-text search) [US-IL-P5-1-002]. Answered, High on formula; "no rounding rule" is absence from the booklet.
- Part 2: Pub-130 has no mention of city/municipal tax (keyword scan: none). Medium-high.
- Part 4: Paid Leave for All Workers Act (820 ILCS 192) still only from search listing (ILGA and labor.illinois.gov not readable). Medium, MANUAL.
- Part 6: pay stub 820 ILCS 115/10, Prevailing Wage Act 820 ILCS 130, IL-2848, IDES forms unchanged (prevailing wage, IDES forms MANUAL: labor.illinois.gov URLs returned 404).
