# Agent 2 (source hunter): QA r3d fix

Date: 2026-11-02. Input: `_qa/CCG-review-r3d.json`. Scope: findings 1, 2, 3, 5, 6 and 8 (data side). Not touched: `01-ccg/`, finding 4 (TN builder vocabulary rule) and finding 7 (builder Sources wording). Backups: `_research/qa-r3d-fix/_backup/` (11 files, taken before the first write). Machine-readable diff: `diff-r3d.json`. Script: scratchpad `apply_r3d.py`.

## Decisions

- **F1 (Birmingham):** the number is removed from the `al.local.leeds.rate` note in the AL annex. The WTC fact note never carried it; the WTC `unresolved` entry `al.local.occupational_tax.list` did ('Birmingham 1% only tier C.'), so that sentence was also changed. Not touched (pack, outside the listed scope): `CCG-annex_AL-research-pack.md` l.49 still quotes the pre-r3c note.
- **F2 (per-period notes):** each object's note was restored from `_research/qa-r3c-fix/_backup/`. The r3c EXACT note stays only on the object it was written for: CO famli 2027, CO new_employer 2027, CO wage_base 2027 (note removed), FED 2027, IN in.pit.rate 2026 (annex) and 2027 (m06), IN LIT R46 2026-01-01 objects, MULTI il.partners 2026-01-01, NE annex, PA m06 2025-07-01 objects (note removed). Pipeline wording was removed from the restored notes: 'MULTI.md' -> 'MULTI', '(builder reads the chart)' removed, and the misplaced withholding-method derivation on Marion R47 replaced by the R47 chart reference the auditor expected. `pa.local.philadelphia.nonresident.rate` needed no change because its notes were not collapsed. Check: within each key, no two objects share a note that were distinct before r3c (0 regressions across all facts files).
- **Residual for the builder's planned cross-year check:** two restored 2026 notes mention the 2027 figure as context ('2027 1.70% combined', CO; '2027 2.90%', m06 in.pit.rate). This is the pre-r3c wording, restored as instructed.
- **F3 (CT locator):** option 2 was chosen. `US-CTP10-001` is the row whose `local_file` is the IP 2026(1) PDF itself (md5 a64b2bbb855163fb832396939efc74ef), so extending its locator keeps one row = one document with all cited pages, and the 556 + 11 table_c/d/e register_ids do not move. `US-CTB5-401` keeps its transcription file and its 5 keys. Pages checked in the PDF: Table C p.28, Table D p.29, Table E p.30, withholding tables pp.31-38 (the table pages render as graphics, and each page carries the 'IP 2026(1)' header).
- **F5 (CA SDI):** the GAP sentence is removed. Both rates are quoted from the local copy (md5 41ae368e0f6c68d6ffbe2924750bb72f), which carries 'The SDI withholding rate for 2026 is 1.3 percent' and '... for 2027 is 1.4 percent'.
- **F6 (OH 4141.23):** codes.ohio.gov live returned HTTP 000. The `/6-16-2026` version page has no Wayback capture, and the latest capture of the section page is the 2026-05-17 copy already held. The amending act was found from the version notice in that held page ('Amended by Senate Bill 101 - 136th General Assembly'; 'takes effect June 16, 2026'). Its enrolled text (Wayback id_ 20260413111315 of search-prod.lis.state.oh.us .../sb101/05_EN/pdf/, md5 bb0054d1f94a37c3952df65b6da3850e) is saved as `00-official-sources/ccg-sources/OH/OH_SB101-136GA_05_EN_wayback-20260413111315.pdf`. Sec. 4141.23(A), PDF p.4, still reads '... and shall not be deducted, in whole or in part, from the remuneration of individuals in the employer's employ.' No strike-through drawings sit over (A). Changes: new row US-OHR3D-001 (A.1, supersedes US-OHR3C-001); US-OHR3C-001 gets effective_to 2026-06-15 and status superseded. `oh.sui.employee.rate` is split into 2026-01-01..2026-06-15 (US-OHR3C-001) and 2026-06-16..2026-12-31 (US-OHR3D-001), value 0 in both. Limitation: this is the enrolled bill, not the codified page. The effective date comes from the codes.ohio.gov notice.
- **F8 (data side):** two keys were added, on US-IDB5-402 (the same row as sibling `id.sui.workforce_development.rate`). Its local transcription l.17 reads 'Standard | 1.000% | 0.97000% | 0.00000% | 0.03000%', and the PDF held under US-IDP52-004 shows the same row. US-IDB5-402 consumed_by already includes CCG/annex_ID. AL: every per-status minimum key already exists (`al.wh.std_deduction.single.min` 2500, `.married.min` 5000, `.married_separate.min` 2500, `.head_of_family.min` 2500), so no key was added. Tagging each status with its own key is the builder's job.

## Validation

- facts.schema.json: 0 errors on all 10 touched facts files. For the new OH object, verification_method was first 'inspected directly', which is not in the facts enum; it is now 'quoted from authority page'.
- Scope check, backup vs current, whole-object compare: changed keys are only those listed below. No other top-level field changed. Register: only US-CAP7-002, US-CTP10-001, US-OHR3C-001 changed, plus US-OHR3D-001 added (2667 -> 2668 rows).
- Shared-note check: 0 keys where objects now share a note that they did not share before r3c.

## Diff (listed keys only)

### CCG-annex_AL-facts.json · `al.local.leeds.rate` · 2026-01-01 · note
- before: `City of Leeds: 1% of gross earnings, monthly return to Avenu, annual reconciliation, show on pay stub, records 5 years. A Birmingham 1% rate is not confirmed by an official source and is not stated here.`
- after: `City of Leeds: 1% of gross earnings, monthly return to Avenu, annual reconciliation, show on pay stub, records 5 years. A Birmingham occupational tax rate is not confirmed by an official source.`

### CCG-annex_CO-facts.json · `co.famli.total.rate` · 2026-01-01 · note
- before: `2027 total (CDLE FAMLI Business Brief 2026-09-30): 'The 2027 premium rate will be 0.86% of wages, down from 0.88% in 2026.' Split: co.famli.employee.rate / co.famli.employer.rate 2027 (derived, 50% cap).`
- after: `0.44% employer + 0.44% employee on wages up to the SS wage base (184,500); statutory cap 1.2%.`

### CCG-annex_CO-facts.json · `co.sui.new_employer.rate.total` · 2026-01-01 · note
- before: `2027 Introductory Rates, non-construction / general construction / trades: beginning 0.0153 + support .0017 + surcharge .00 = combined 0.0170 (page: 'The Solvency Surcharge is not in affect for the 2027 calendar year'); heavy construction 0.0406; political subdivision 0.0020.`
- after: `1.53% + support surcharge 0.17% + solvency 1.35% (non-construction); heavy construction 6.285%; 2027 1.70% combined, no solvency.`

### CCG-annex_CO-facts.json · `co.sui.wage_base` · 2026-01-01 · note
- before: (absent)
- after: `Chargeable wage limit; 32,100 for 2027; employer only.`

### CCG-annex_FED-facts.json · `fed.fica.oasdi.wage_base` · 2026-01-01 · note
- before: `SSA Contribution and Benefit Base page: 'For earnings in 2027, this base is $192,300.'`
- after: `G-DERIVE (US-FED-003, Federal Register 2025-19763): 60,600 x AWI(2024) 69,846.57 / AWI(1992) 22,935.42 = 184,548.71, rounded to a multiple of 300 = 184,500.`

### CCG-annex_IN-facts.json · `in.pit.rate` · 2027-01-01 · note
- before: `DOR rates page; IC 6-3-2-1 not read.`
- after: `DOR: "will adjust in 2027 to 2.90%"; statute not read.`

### CCG-annex_IN-facts.json · `in.local.lit.rate.boone` · 2026-10-01 · note
- before: `DN#1 R46/01-26 county chart (Boone 0.017, Marion 0.0202, Porter 0.005, Randolph 0.03); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01.`
- after: `DN#1 R47/10-26 county chart, from 2026-10-01 [US-INS5-007]. Was 0.017 to 2026-09-30 (R46).`

### CCG-annex_IN-facts.json · `in.local.lit.rate.marion` · 2026-10-01 · note
- before: `DN#1 R46/01-26 county chart (Boone 0.017, Marion 0.0202, Porter 0.005, Randolph 0.03); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01.`
- after: `DN#1 R47/10-26 county chart, from 2026-10-01 [US-INS5-007]; same rate as R46.`

### CCG-annex_IN-facts.json · `in.local.lit.rate.min` · 2026-10-01 · note
- before: `DN#1 R46/01-26 county chart (Boone 0.017, Marion 0.0202, Porter 0.005, Randolph 0.03); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01.`
- after: `DN#1 R47/10-26 county chart, from 2026-10-01 [US-INS5-007]: Porter.`

### CCG-annex_IN-facts.json · `in.local.lit.rate.max` · 2026-10-01 · note
- before: `DN#1 R46/01-26 county chart (Boone 0.017, Marion 0.0202, Porter 0.005, Randolph 0.03); periods 2026-01-01..2026-09-30; replaced by R47 (US-INS5-007) from 2026-10-01.`
- after: `DN#1 R47/10-26 county chart, from 2026-10-01 [US-INS5-007]: Randolph. Full 92-county chart in DN#1 R47/10-26.`

### CCG-annex_MULTI-facts.json · `multi.reciprocity.il.partners` · 2026-02-01 · note
- before: `Bilateral; confirmed on both sides (MULTI 2.3). Local taxes are outside reciprocity.`
- after: `Bilateral exemption from work-State withholding on the employee nonresidence certificate; 30 pairs confirmed on both sides (MULTI 2.3). Local taxes are outside State reciprocity. LEVEL: withholding.`

### CCG-annex_MULTI-facts.json · `ne.sui.wage_base.other_state_credit` · 2025-09-11 · note
- before: `48-648.02.`
- after: `Wages the same employer already paid under another State's UI law in the same calendar year count toward this State's taxable wage base. 48-648.02. LEVEL: employer UI reporting.`

### CCG-annex_PA-facts.json · `pa.local.philadelphia.resident.rate` · 2025-07-01 · note
- before: (absent)
- after: `Sterling Act (Act 32 does not apply).`

### CCG-m06_tax-facts.json · `in.pit.rate` · 2026-01-01 · note
- before: `DOR rates page; IC 6-3-2-1 not read.`
- after: `2027 2.90%. County rates change in January and October (DN#1 R47/10-26).`

### CCG-m06_tax-facts.json · `pa.local.philadelphia.resident.rate` · 2026-07-01 · note
- before: (absent)
- after: `Nonresident 3.425% from 2026-07-01 (3.74/3.43 before). Mid-year change.`

### WTC-country_specific-facts.json · `al.local.occupational_tax.list` · (unresolved) · why
- before: `No state list of ~26 municipal/county occupational taxes; Birmingham 1% only tier C.`
- after: `No state list of ~26 municipal/county occupational taxes; Birmingham occupational tax rate not confirmed by an official source.`

### CCG-annex_ID-facts.json · `id.sui.new_employer.ui_component.rate` · 2026-01-01 · NEW
- before: (absent)
- after: `{"key": "id.sui.new_employer.ui_component.rate", "value": 0.97, "unit_of_measure": "percent", "effective_from": "2026-01-01", "effective_to": "2026-12-31", "register_id": "US-IDB5-402", "tier": "A.2", "verification_method": "quoted from authority page", "authority": "Idaho Department of Labor", "url": "https://www.labor.idaho.gov/wp-content/uploads/2024/12/Tax-rate_Class-array_2026.pdf", "confidence": "high", "note": "Standard (new employer) rate 1.000%: UI contribution rate component 0.97000% (IDOL Rate Class Array effective 01/01/2026, row \"Standard\").", "_domain": "social_security"}`

### CCG-annex_ID-facts.json · `id.sui.new_employer.admin_component.rate` · 2026-01-01 · NEW
- before: (absent)
- after: `{"key": "id.sui.new_employer.admin_component.rate", "value": 0.0, "unit_of_measure": "percent", "effective_from": "2026-01-01", "effective_to": "2026-12-31", "register_id": "US-IDB5-402", "tier": "A.2", "verification_method": "quoted from authority page", "authority": "Idaho Department of Labor", "url": "https://www.labor.idaho.gov/wp-content/uploads/2024/12/Tax-rate_Class-array_2026.pdf", "confidence": "high", "note": "Standard (new employer) rate 1.000%: administrative rate component 0.00000% (IDOL Rate Class Array effective 01/01/2026, row \"Standard\").", "_domain": "social_security"}`

### CCG-annex_OH-facts.json · `oh.sui.employee.rate` · 2026-01-01 · effective_to
- before: `2026-12-31`
- after: `2026-06-15`

### CCG-annex_OH-facts.json · `oh.sui.employee.rate` · 2026-06-16 · NEW
- before: (absent)
- after: `{"key": "oh.sui.employee.rate", "value": 0, "unit_of_measure": "percent", "effective_from": "2026-06-16", "effective_to": "2026-12-31", "register_id": "US-OHR3D-001", "tier": "A.1", "verification_method": "quoted from authority page", "authority": "Ohio General Assembly (136th GA), Sub. S.B. 101 as enrolled", "url": "https://search-prod.lis.state.oh.us/api/v2/general_assembly_136/legislation/sb101/05_EN/pdf/", "confidence": "high", "note": "Ohio Rev. Code 4141.23(A), version effective 2026-06-16 (Sub. S.B. 101, 136th GA): contributions are paid by the employer 'and shall not be deducted, in whole or in part, from the remuneration of individuals in the employer's employ.' Division (A) is unchanged from the prior version."}`

### legal-basis-register.csv · `US-CTP10-001` · - · article_or_section
- before: `Q5 (gross CT wages); 'Residents working outside CT' (proration among qualifying jurisdictions); '15-Day Rule for Nonresident Employees' p.8; CT-W4NA allocation`
- after: `Q5 (gross CT wages); 'Residents working outside CT' (proration among qualifying jurisdictions); '15-Day Rule for Nonresident Employees' p.8; CT-W4NA allocation; Table C '2% Tax Rate Phase-Out Add-Back' p.28, Table D 'Tax Recapture' p.29, Table E 'Personal Tax Credits' p.30; State of Connecticut 2026 Withholding Tables pp.31-38 (weekly 31-32, bi-weekly 33-34, semi-monthly 35-36, monthly 37-38)`

### legal-basis-register.csv · `US-CTP10-001` · - · figure_or_rule_carried
- before: `Resident employees: CT wages = all wages regardless of where services performed; where employer must withhold for another state, CT tax is prorated and only the excess remitted (Example 4). Nonresidents: CT wages = wages for services performed in CT, allocated on CT-W4NA; 15-day rule: no withholding if 15 days or less in CT in the calendar year, but if more than 15 days, withhold on all CT-service pay including the first 15 days (PS 2015(6)). No reciprocity agreement appears anywhere in IP 2026(1) (full-text search 'reciproc': none).`
- after: `Resident employees: CT wages = all wages regardless of where services performed; where employer must withhold for another state, CT tax is prorated and only the excess remitted (Example 4). Nonresidents: CT wages = wages for services performed in CT, allocated on CT-W4NA; 15-day rule: no withholding if 15 days or less in CT in the calendar year, but if more than 15 days, withhold on all CT-service pay including the first 15 days (PS 2015(6)). No reciprocity agreement appears anywhere in IP 2026(1) (full-text search 'reciproc': none). Also carries: Tables C, D and E (pp.28-30) by withholding code; 2026 Withholding Tables (pp.31-38): withholding amount per wage band and code A/B/C/D/F, 139 bands per payroll period (weekly, bi-weekly, semi-monthly, monthly); above the last band, TPG-211 calculation rules.`

### legal-basis-register.csv · `US-CAP7-002` · - · figure_or_rule_carried
- before: `1.3% withheld, no wage ceiling since 2024-01-01; no employer share; payer=employee; base=no cap; scope=statewide; GAP: WebFetch summary of 1.4% is wrong`
- after: `2026: 1.3% ("The SDI withholding rate for 2026 is 1.3 percent"); 2027: 1.4% ("The SDI withholding rate for 2027 is 1.4 percent"); no wage ceiling since 2024-01-01; no employer share; payer=employee; base=no cap; scope=statewide`

### legal-basis-register.csv · `US-OHR3C-001` · - · effective_to
- before: ``
- after: `2026-06-15`

### legal-basis-register.csv · `US-OHR3C-001` · - · status
- before: `active`
- after: `superseded`

### legal-basis-register.csv · `US-OHR3D-001` · - · NEW
- before: (absent)
- after: `{"id": "US-OHR3D-001", "domain": "social_security", "instrument_name": "Ohio Revised Code 4141.23 Contributions; payment (version effective 2026-06-16), as amended by Sub. S.B. 101, 136th General Assembly (enrolled text)", "instrument_type": "statute", "tier": "A.1", "authority": "Ohio General Assembly (Legislative Service Commission bill text service)", "url": "https://search-prod.lis.state.oh.us/api/v2/general_assembly_136/legislation/sb101/05_EN/pdf/", "article_or_section": "Section 1, Sec. 4141.23(A) (PDF p.4)", "publication_date": "", "effective_from": "2026-06-16", "effective_to": "", "supersedes": "US-OHR3C-001", "figure_or_rule_carried": "Contributions accrue and are paid by each employer 'and shall not be deducted, in whole or in part, from the remuneration of individuals in the employer's employ.' Division (A) unchanged by S.B. 101 (no struck or inserted text in (A)). Effective date 2026-06-16 per the codes.ohio.gov version notice held in US-OHR3C-001 ('takes effect June 16, 2026'; 'Amended by Senate Bill 101 - 136th General Assembly').", "language": "en", "local_file": "00-official-sources/ccg-sources/OH/OH_SB101-136GA_05_EN_wayback-20260413111315.pdf", "retrieved_on": "2026-11-02", "verified_on": "2026-11-02", "verification_method": "inspected directly (Wayback id_ 20260413111315 of the enrolled bill PDF; pdftotext + PyMuPDF: no strike-through drawings over division (A)); md5 bb0054d1f94a37c3952df65b6da3850e; codes.ohio.gov live host and the /6-16-2026 version page not reachable (HTTP 000, no Wayback capture)", "consumed_by": "CCG/annex_OH", "status": "active"}`
