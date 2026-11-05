# Mandate answers P5-W1B-r1 - PA, OH, NC, MI, GA (PASS 4, wave 1B, round 1, 2026-10-29)
Shard: `00-official-sources/_register-shards/mandate-P5-W1B-r1.csv` (27 rows, ids US-<UF>-P5-1-NNN). Only parts still missing after the earlier PASS 4 sections were worked. Method: WebFetch on official hosts, own Chrome tab (michigan.gov pages), official PDFs saved under `00-official-sources/pdfs/<UF>/` and read locally with PyMuPDF (`python -I`), Wayback copies 2025/2026 (one request per 10 s; one 429 handled with a 60 s wait). About 14 page reads in total. Not reachable: ncleg.gov HTML/Chrome (403/Cloudflare), codes.ohio.gov and legislature.mi.gov by WebFetch (ECONNREFUSED) and in Chrome (domain-change security check) - read via Wayback instead; michigan.gov PDFs unreadable in Chrome (no text layer) - read via Wayback.

Shared finding for part 4 (all five states): the federal DOL Women's Bureau page lists the 13 states + DC with mandatory paid family/medical leave and HI/NH/VT/VA special cases; PA, OH, NC, MI and GA are not on it (US-xx-P5-1-005/004/005/008/003). Absence is by enumeration of a federal page (tier B, page undated), not by a state statement. Confidence medium-high.

## PA - US-MQ-58 (missing: 1 rounding, 4, 6)
1. Rounding: still NOT LOCATED (REV-415 read earlier has no rounding rule). Open, low impact.
4. SDI/PFML: none; PA not on the DOL list; UC employee 0.07% already in US-PA-009 (US-PAP51-005). STATUS: answered by enumeration (medium-high).
6. Pay statement: 34 Pa. Code 231.36 (hours worked, rates, gross wages, deductions, net wages with every payment; US-PAP51-001, high). The WPCL (Act 329 of 1961) read in full has no pay-stub section (US-PAP51-002). Prevailing wage: Act 442 of 1961 (43 P.S. 165-1 ff.), Sec. 2(5) threshold 25,000 USD, Department of Labor and Industry / Bureau of Labor Law Compliance (US-PAP51-003, 006; high). POA: withholding REV-677 (US-PA-008); UI has no paper form, electronic UCMS handshake between employer and TPA (US-PAP51-004, high). Calculator: none, flat 3.07%. STATUS: answered.

## OH - US-MQ-55 (missing: 1 rounding, 4, 5, 6)
1. Rounding: NOT LOCATED (2026 Filing Guidelines, Rev. 11/25, zero hits; percentage-method PDF earlier). Open.
4. SDI/PFML: none; OH not on the DOL list (US-OHP51-004). STATUS: answered by enumeration (medium-high).
5. Multistate: employers withhold for residents and nonresidents; residents of MI, IN, KY, WV, PA are exempt; IT 4 (rev. 12/2020) is the single combined certificate and replaces IT 4NR (US-OHP51-002, high). No day/dollar threshold exists in the guideline file. Resident/nonresident credit (IT NRC) pages returned 404 and ORC 5747.05 was not read: credit detail open. STATUS: answered for withholding; credit detail partial.
6. Pay statement: ORC 4113.14 (effective 2025-04-09, HB 106): full content, 10-day request cure, report to the director of commerce (US-OHP51-001, high). Prevailing wage: ORC ch. 4115; DOL table: 250,000 USD new construction / 75,000 USD remodeling (US-OHP51-003; statute not re-read, medium). POA: TBOR 1 / ODJFS JFS 20107 / WT-8655 remain MANUAL (US-OH-013). Calculator: department tables and formula only. STATUS: answered except POA forms not opened.

## NC - US-MQ-47 (missing: 2, 4, 5, 6)
2. Local: G.S. 105-247 "No city, town, township, or county shall levy any tax on income or inheritance" (US-NCP51-001, high; Wayback 2026-02-17 copy read locally). STATUS: answered.
4. SDI/PFML: none; NC not on the DOL list (US-NCP51-005). STATUS: answered by enumeration (medium-high).
5. Multistate: NC-30 Section 5: residents taxed on all wages, but no withholding for services in another state if that state requires withholding; nonresidents taxed on any wages for NC services; double-withholding relief is the residence state's; no reciprocity agreement and no day/dollar threshold in the publication (US-NCP51-002, high). Statutory authority to enter reciprocity agreements exists in Article 4A (search summary) but none is published in NC-30. STATUS: answered.
6. Pay statement: G.S. 95-25.13(4) already (US-NCW1B-003). Prevailing wage: DOL table lists NC without a state prevailing wage law (US-NCP51-004, tier B, medium-high). POA: withholding GEN-58 (US-NCW1B-002); UI: DES Power of Attorney and Declaration of Representative, rev. 07/2025, roles and signer rules (US-NCP51-003, high). Calculator: NC-30 tables and percentage method 4.09%, round to the nearest dollar. STATUS: answered.

## MI - US-MQ-42 (missing: 1 rounding, 2, 3, 4, 6)
1. Rounding: NOT LOCATED (Guide 446 TY2026 read locally, zero hits). Reciprocity from Guide 446: IL, IN, KY, MN, OH, WI (US-MIP51-001, high). Open: rounding only.
2. Local: Detroit read in full: 2.4% residents / 1.2% nonresidents; Form 5527 certificate; monthly Form 5323 due the 15th; annual Form 5321 due 2027-02-28 for TY2026; resident working in another taxing city gets rate 2.4% minus the other city's nonresident rate (US-MIP51-002, high). The other 23 cities (list in US-MILOC-001) administer their own filing; their rates are NOT LOCATED (no Treasury guide covers them; Chrome cannot read the michigan.gov city PDFs). STATUS: partial (Detroit answered).
3. SUI: 2026 summary page: new employer 2.7%, construction 5.0%, range 0.06%-12.2% (15.2% with penalty) (US-MIP51-003, chrome-read, high); 9,000 reduced base and 9,500 for delinquent employers via Form 6354 (US-MIP51-004, chrome-read, high); no employee contribution. MiUI went live 2026-02-23 for employers and TPAs. STATUS: answered.
4. SDI/PFML: none; MI not on the DOL list (US-MIP51-008). STATUS: answered by enumeration (medium-high).
6. Pay statement: MCL 408.479(2) read locally (hours, gross wages, pay period, separate itemization of deductions, at time of payment; 3-year records) (US-MIP51-005, high). Prevailing wage: Act 10 of 2023, effective 2024-02-13, amended by Act 110 of 2024, LEO commissioner (US-MIP51-006, high); the DOL table still says repealed in 2018 and is stale (US-MIP51-007, superseded). POA: Form 151 (US-MIPOA-001, MANUAL); UI via MiWAM/MiUI TPA arrangement. Calculator: Treasury withholding calculator named in Guide 446 (US-MIP51-001). STATUS: answered except Form 151 not opened.

## GA - US-MQ-30 (missing: 4, 5, 6 after W1B)
4. SDI/PFML: none; GA not on the DOL list (US-GAP51-003); GDOL FAQ: no state law requires vacation/sick/personal leave. STATUS: answered by enumeration (medium-high).
5. Multistate: 2026 DOR guide (rev. September 2026): residents withheld wherever they work except where the other state requires withholding; taxable nonresidents (more than 5% or 5,000 USD of wages attributable to Georgia) withheld for Georgia services; no reciprocity text (US-GAP51-001, high). The 23-calendar-days-per-quarter exemption appears only in a search summary and is NOT in the guide: open (needs O.C.G.A. 48-7-101 read; Justia returned 403). STATUS: partial.
6. Pay statement: no GDOL page addresses it (US-GAP51-004); NO Georgia Code title 34 statute located and absence not proven. Prevailing wage: DOL table lists GA without a state law (US-GAP51-002, medium-high). POA: RD-1061/1062/1063 and GDOL POA already in US-GAW1B-001/003. Calculator: guide percentage-method examples. STATUS: partial (pay-statement statute open).

## Gaps for the next round (owner-visible)
- MI: rates and filing rules of the 23 non-Detroit cities; Form 151 not opened.
- GA: O.C.G.A. 48-7-101 (23-day rule) and any Title 34 pay-statement section.
- OH: IT NRC / ORC 5747.05 credits; ORC 4115 read; POA forms TBOR 1, JFS 20107, WT-8655; RITA still gated.
- Rounding rule: not stated in the official withholding guides of PA, OH, MI (searched, zero hits); GA none found; NC states round to the nearest dollar.
- Gated or unreadable: ncleg.gov (403/Cloudflare), codes.ohio.gov and legislature.mi.gov (ECONNREFUSED to WebFetch), michigan.gov PDFs in Chrome (unreadable-pdf, read via Wayback instead), tax.ohio.gov FAQ pages (404).
