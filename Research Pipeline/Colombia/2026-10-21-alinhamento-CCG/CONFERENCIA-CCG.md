# CO-CCG-001 v1.3 - conferência (21 Oct 2026)

Base: [[Research Pipeline/Colombia/2026-10-21-alinhamento-CCG/base/CO-CCG-001_v1.2-gdoc-export-2026-10-21.docx|CO-CCG-001_v1.2-gdoc-export-2026-10-21.docx]] (md5 b051912c340f3246c078ca9ed65c0e4b). Result: [[Research Pipeline/Colombia/2026-10-21-alinhamento-CCG/CO-CCG-001-v1.3.docx|CO-CCG-001-v1.3.docx]] (round 3, md5 abd9e2595675df3ea8e96cca4d21e4cb; round 2 was b52beb6beeb4e59e5adee3b8db84c6f1; round 1 was 856176ec86858c73358f8810202d3886). Local only: nothing uploaded, Drive not touched.
Method: word/document.xml edited directly with lxml (unzip -> edit -> rezip); footer1.xml edited only for the version string; the other 17 zip entries copied byte for byte (checked). New or changed `w:t` carry `xml:space="preserve"`; edited text keeps the formatting of the run it sits in. Paragraph numbers below = index of `w:p` in the base document.xml (same as `para` in suggestions-raw.json). Scripts in the session scratchpad (`ccg13/build13.py`, `pack.py`, `verify.py`).

## Counts

| Check | Base | v1.3 |
|---|---|---|
| `w:ins` / `w:del` / `w:delText` elements | 125 / 59 / 63 | 0 / 0 / 0 |
| Tracked changes resolved | 93 in 87 paragraphs (S01-S87) | 85 ids accepted (37 ACCEPT, 48 ACCEPT_WITH_FIX), 2 rejected (S86, S87) |
| Res. DIAN 000013/2021 mentions | 27 | 2 (para 6092 "governed by Resolution DIAN 000227 of 2025, arts. 1.5.3.1.1 to 1.5.3.9.8 (which compile Resolution DIAN 000013 of 11 February 2021)"; Version Control row 1.3) |
| Res. DIAN 000227/2025 mentions | 8 | 35 |
| CO-RPT-00x ids | 12 | 0 |
| "art. 19 lit. c" / "point is not settled" (ARL on vacation) | 2 / 2 | 0 / 0 |
| 40% denominator claim ("both sides of the test") | 1 | 0 |
| Ticket refs "HRBS-" | 3 | 0 |
| TODO / TBD / XXX / lorem | 0 | 0 |
| "placeholder" | 1 | 1 (pre-existing NE surname rule "A placeholder must be emitted or validation fails"; not introduced) |
| Comments (range start / end / reference) | 1 / 1 / 1 | 1 / 1 / 1 |

inspect_docx.py (mercans-artifact-toolkit): base 1,384 paragraphs, 64,375 words (python-docx does not count text inside `w:ins`), 248 tables, 212 headings (H1 14, H2 38, H3 160), 1 residual marker; v1.3 1,383 paragraphs (S08+S09 merge), 68,334 words, 248 tables, 212 headings with identical text and levels, same 1 residual marker. python-docx opens v1.3 (1,383 paragraphs, 248 tables).

## Per suggestion

| ID | Para | Section | Verdict | Done |
|---|---|---|---|---|
| S01 | 258 | Version Control | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S02 | 259 | Version Control | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S03 | 260 | Version Control | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S04 | 261 | Version Control | ACCEPT_WITH_FIX | Row 1.2 description replaced by the verdict fix_text. |
| S05 | 725 | Module 2: Master Data Configuration | ACCEPT_WITH_FIX | Insertion replaced: report specs cited by their real ids (CO-DIAN-001, CO-DIAN-002, CO-PILA-003, CO-DIAN-004, CO-DIAN-005, CO-CESANTIAS-006). |
| S06 | 914 | What employee fields are required for processing p | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S07 | 1214 | Deliverable: Provide a definitive, step-by-step de | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S08 | 1546 | How are deductions handled if they cannot be made  | ACCEPT_WITH_FIX | Judged with S09: the two paragraphs (one sentence) merged into one; the lead clause stays bold. |
| S09 | 1547 | How are deductions handled if they cannot be made  | ACCEPT_WITH_FIX | Merged paragraph = S09 fix_text (presumption that a court order already respects the cap removed; per-period cap at the art. 155 / 156 portion; CGP art. 593 num. 9; art. 344 kept). |
| S10 | 1555 | How are deductions handled if they cannot be made  | ACCEPT_WITH_FIX | Legal basis: "Funcion Publica" -> "Función Pública", joined with ";", and CGP (Ley 1564 de 2012) art. 593 num. 9 added. |
| S11 | 2351 | Provide a detailed definition for each classificat | ACCEPT_WITH_FIX | Paragraph = fix_text (bold clause kept): last IBC reported before the vacation; ARL not due on vacation (Decreto 1072/2015 art. 2.2.4.2.1.6 num. 1.3); non-existent "art. 19 lit. c" and "not settled" removed. |
| S12 | 2439 | Create a reference table classifying common pay co | ACCEPT_WITH_FIX | Cell "No" -> "Only above the 40% clamp". |
| S13 | 2544 | Create a reference table classifying common pay co | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S14 | 2552 | Create a reference table classifying common pay co | ACCEPT_WITH_FIX | Cell = fix_text (adds Consejo de Estado exp. 23856 of 2021). |
| S15 | 2553 | Create a reference table classifying common pay co | ACCEPT_WITH_FIX | Cell = fix_text (art. 51, SL588-2024; SL1659-2025 instance ruling, not settled case law). |
| S16 | 2562 | Create a reference table classifying common pay co | ACCEPT_WITH_FIX | Cell = fix_text (art. 206 nums. 1-2; 25% exemption of num. 10 still applies). |
| S17 | 2569 | Create a reference table classifying common pay co | ACCEPT_WITH_FIX | Cell = fix_text (same as S16). |
| S18 | 2576 | Create a reference table classifying common pay co | ACCEPT_WITH_FIX | Cell = fix_text (same as S16). |
| S19 | 2769 | For each mandatory contribution, provide the statu | ACCEPT_WITH_FIX | Paragraph = fix_text (UGPP "ABC" citation removed; Ley 797 art. 5, Ley 2381 art. 22). |
| S20 | 2950 | Deliverable: Comprehensive summary of current cont | ACCEPT_WITH_FIX | Last sentence = fix sentence with Decree 780 arts. 3.2.1.10 and 3.2.5.1; lead sentence kept bold, rest set regular. |
| S21 | 2996 | Deliverable: Comprehensive summary of current cont | ACCEPT_WITH_FIX | Inserted "CONFIRMED 19 September 2026 ..." replaced by fix_text (preceded by ". "). |
| S22 | 2999 | What is the step-by-step calculation logic for all | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S23 | 3000 | What is the step-by-step calculation logic for all | ACCEPT_WITH_FIX | Text after the bold lead = fix_text: rule 3 quote of SU 25185; unverified Spanish quote and the denominator claim removed. |
| S24 | 3197 | Can employees and employers make additional volunt | ACCEPT_WITH_FIX | Last two sentences = fix_text (control accounts arts. 1.2.4.1.28 / 1.2.4.1.12; withdrawals art. 1.2.4.1.37 and 1.2.4.1.35-36); lead kept bold, rest regular. |
| S25 | 3327 | What documents or declarations are required from a | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S26 | 3366 | Module 6: Income Tax Withholding System | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S27 | 4539 | What are the rules for processing statutory deduct | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S28 | 4599 | Are there protected earnings limits? | ACCEPT_WITH_FIX | Full stop added after "COP 201,819"; only that figure stays bold. |
| S29 | 4601 | Are there protected earnings limits? | ACCEPT_WITH_FIX | Insertion = fix_text (Law 1098 of 2006 art. 130 num. 1). |
| S30 | 4620 | Are there protected earnings limits? | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S31 | 4622 | Are there protected earnings limits? | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S32 | 4624 | Are there protected earnings limits? | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S33 | 4627 | Are there protected earnings limits? | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S34 | 4628 | Are there protected earnings limits? | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S35 | 4630 | Are there protected earnings limits? | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S36 | 4631 | Are there protected earnings limits? | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S37 | 4633 | Are there protected earnings limits? | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S38 | 4636 | Are there protected earnings limits? | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S39 | 4637 | Are there protected earnings limits? | ACCEPT_WITH_FIX | "Law 1098 of 2006 (Childhood and Adolescence Code)" -> "... art. 130". |
| S40 | 4664 | For each type of statutory leave, what are the eli | ACCEPT_WITH_FIX | Cell = fix_text (C-543 of 2007 floor). |
| S41 | 4667 | For each type of statutory leave, what are the eli | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S42 | 4693 | For each type of statutory leave, what are the eli | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S43 | 4694 | For each type of statutory leave, what are the eli | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S44 | 4695 | For each type of statutory leave, what are the eli | ACCEPT_WITH_FIX | Cell = fix_text (child condition, medical certificate). |
| S45 | 4696 | For each type of statutory leave, what are the eli | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S46 | 4697 | For each type of statutory leave, what are the eli | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S47 | 4698 | For each type of statutory leave, what are the eli | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S48 | 4699 | For each type of statutory leave, what are the eli | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S49 | 4700 | For each type of statutory leave, what are the eli | ACCEPT_WITH_FIX | Cell = fix_text (month-of-start contribution, certificate). |
| S50 | 4701 | For each type of statutory leave, what are the eli | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S51 | 4702 | For each type of statutory leave, what are the eli | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S52 | 4709 | For each type of statutory leave, what are the eli | ACCEPT_WITH_FIX | Cell = fix_text (Labour Code art. 57 num. 6(a), Law 2466 art. 15). |
| S53 | 4826 | How are unpaid or partially paid leaves handled? | ACCEPT_WITH_FIX | Inserted "RESOLVED 19 September 2026 ..." replaced by fix_text (one concept, 20 Oct 2023). Quote not read in the original: see OPEN-ITEMS. |
| S54 | 4827 | How are unpaid or partially paid leaves handled? | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S55 | 4927 | Are any other kinds of leave paid by government au | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S56 | 4928 | Are any other kinds of leave paid by government au | ACCEPT_WITH_FIX | Cell = fix_text. |
| S57 | 4929 | Are any other kinds of leave paid by government au | ACCEPT_WITH_FIX | Cell = fix_text (no percentage in art. 41; 50% from art. 227; C-543 floor). |
| S58 | 4930 | Are any other kinds of leave paid by government au | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S59 | 4931 | Are any other kinds of leave paid by government au | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S60 | 4932 | Are any other kinds of leave paid by government au | ACCEPT_WITH_FIX | Cell = fix_text (Law 1753 art. 67). |
| S61 | 4933 | Are any other kinds of leave paid by government au | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S62 | 4934 | Are any other kinds of leave paid by government au | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S63 | 4967 | Are any other kinds of leave paid by government au | ACCEPT_WITH_FIX | Insertion corrected per fix_text (favourable rehabilitation concept; Law 1753 art. 67); rest unchanged; lead kept bold, rest regular. |
| S64 | 4968 | Are any other kinds of leave paid by government au | ACCEPT_WITH_FIX | Taxability and SL588 / SL1659 attribution per fix_text; lead kept bold, rest regular. |
| S65 | 5030 | Provide the calculation logic for each leave type  | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S66 | 5032 | Provide the calculation logic for each leave type  | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S67 | 5048 | Provide the calculation logic for each leave type  | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S68 | 5059 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | Formula -> max(2,400,000 ÷ 30 × 2/3 ; 1,750,905 ÷ 30) × 2. |
| S69 | 5060 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | 116,727.00. |
| S70 | 5062 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | Same as S68. |
| S71 | 5063 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | 116,727.00. |
| S72 | 5069 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | Total gross 2,529,336.33. |
| S73 | 5071 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | Contribution-base line rewritten with the floor (see worked example below). |
| S74 | 5072 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | 2,280,121. |
| S75 | 5075 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | 91,300 (up to the nearest 100). |
| S76 | 5078 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | 91,300. |
| S77 | 5083 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | 2,529,336.33 − 182,600. |
| S78 | 5084 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | 2,346,736.33. |
| S79 | 5086 | Provide the calculation logic for each leave type  | ACCEPT_WITH_FIX | Part 1 kept; ARL sentence replaced by the verdict sentence (Decreto 1072/2015 art. 2.2.4.2.1.6 num. 1.3; Concepto 091961 non-binding). |
| S80 | 5277 | Describe the rules for statutory severance/redunda | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S81 | 5278 | Describe the rules for statutory severance/redunda | ACCEPT_WITH_FIX | Paragraph = fix_text (ticket ref and operator-calculator claim removed; written agreement; both mechanisms optional). |
| S82 | 6089 | Module 10: Reporting, Compliance & Finalisation | ACCEPT_WITH_FIX | First insertion -> real spec ids; second insertion (CO-SIR-INDEX-001, DIAN-NE P1-P7) unchanged. |
| S83 | 6266 | List all other mandatory reports, stating the freq | ACCEPT | Accepted: tracked change resolved (insertion kept, deletion dropped). |
| S84 | 7715 | Example 5 — Complex scenario: all-inclusive salary | ACCEPT_WITH_FIX | Three edits of the fix: UGPP / Ámbito Jurídico references removed; "void" sentence replaced; Ley 2381 art. 22 sentence added. |
| S85 | 7939 | Other prevalent non-statutory practices worth reco | ACCEPT_WITH_FIX | Ticket reference and "client processes" framing removed; paragraph = fix_text. |
| S86 | 7940 | Other prevalent non-statutory practices worth reco | REJECT | Rejected: inserted text removed (nothing had been deleted); the emptied paragraph removed. Text in REJECTED-S86-S87.md. |
| S87 | 7941 | Other prevalent non-statutory practices worth reco | REJECT | Rejected: same as S86. |

Formatting: paragraphs 2950, 3197, 4967, 4968 had been inserted entirely in bold; the lead sentence stays bold and the rest is regular, as in the neighbouring paragraphs. Paragraph 4599: only "COP 201,819." stays bold.

## Worked example, Module 8 "Provide the calculation logic for each leave type where applicable" (C-543/2007 minimum-wage floor)

SMMLV 2026 = 1,750,905 (Decreto 1469/2025 art. 1); day = 58,363.50; 2,400,000 ÷ 30 × 2/3 = 53,333.33 < 58,363.50, so the floor governs. Every figure re-computed from its own rows.

| Line | Before (v1.2, suggestions as proposed) | After (v1.3) | Check |
|---|---|---|---|
| Sickness d1-2 label | Sickness, days 1–2, employer, 66.67% | Sickness, days 1–2, employer, 2/3 floored at the minimum wage | C-543/2007 |
| Sickness d1-2 formula | 2,400,000 ÷ 30 × 2/3 × 2 | max(2,400,000 ÷ 30 × 2/3 ; 1,750,905 ÷ 30) × 2 | |
| Sickness d1-2 amount | 106,666.67 | 116,727.00 | 58,363.50 × 2 |
| Sickness d3-4 label | Sickness, days 3–4, health insurer, 66.67% (advanced by the employer, recoverable) | Sickness, days 3–4, health insurer, 2/3 floored at the minimum wage (advanced by the employer, recoverable) | |
| Sickness d3-4 formula / amount | 2,400,000 ÷ 30 × 2/3 × 2 / 106,666.67 | max(2,400,000 ÷ 30 × 2/3 ; 1,750,905 ÷ 30) × 2 / 116,727.00 | |
| Salary for days worked / vacation pay / transport | 1,680,000.00 / 400,000.00 / 215,882.33 | unchanged | 2,400,000 × 21/30; 2,400,000 × 5/30; 249,095 × 26/30 |
| Total gross | 2,509,215.67 | 2,529,336.33 | 1,680,000 + 400,000 + 116,727 + 116,727 + 215,882.33 |
| Contribution base (text) | vacation IBC 366,667; sickness 213,333.33; 2,260,000.33 rounded up | vacation IBC 366,666.67 (2,200,000 × 5 ÷ 30); sickness 233,454.00; 2,280,120.67 rounded up to the peso (Decreto 780 art. 3.2.1.5, Decreto 1990/2016) | 1,680,000 + 366,666.67 + 233,454.00 |
| Contribution base | 2,260,001 | 2,280,121 | |
| Employee health 4% | 90,500 (up to the nearest 100) | 91,300 (up to the nearest 100) | 4% × 2,280,121 = 91,204.84 -> 91,300 |
| Employee pension 4% | 90,500 | 91,300 | same |
| Solidarity fund | 0 (base < 4 minimum wages) | unchanged | 2,280,121 < 7,003,620 |
| Net pay formula | 2,509,215.67 − 181,000 | 2,529,336.33 − 182,600 | |
| Net pay | 2,328,215.67 | 2,346,736.33 | |
| Note after the table (ARL) | "Decreto 1772 de 1994 art. 19 lit. c ... market practice ... not settled" | S79 sentence: ARL not due for vacation days (Decreto 1072/2015 art. 2.2.4.2.1.6 num. 1.3) | |

## Res. DIAN 000013/2021 -> Res. DIAN 000227/2025 (27 -> 2)

Map: brief + `co-report-crosscheck/04-output/SIR-RES227-2026-10-21.md`. Arts. 15 (-> 1.5.3.5.1.7) and 24 (-> 1.5.3.8.3) are cited in the CCG but are not in the brief's map; both read in the compilation notes of the DIAN normograma (`raw/docs/oficiais/CO/2026-10-21-Res-DIAN-0013-2021-normograma.htm`: 'Artículo compilado como artículo 1.5.3.5.1.7 / 1.5.3.8.3 en la Resolución 227 de 2025'). Implicit Res. 13 article numbers in the same sentence were mapped too (6409 'art. 5 content', 6421 'article 24').

| Para | Before | After |
|---|---|---|
| 282 | 000013 of 2021 article 26 | 000227 of 2025 article 1.5.3.8.5 |
| 297 | 000013 of 2021 article 26 | 000227 of 2025 article 1.5.3.8.5 |
| 299 | 000013 of 2021 art. 26 | 000227 of 2025 art. 1.5.3.8.5 |
| 335 | 000013 of 2021 article 3 | 000227 of 2025 article 1.5.3.2.2 |
| 400 | 000013 of 2021 art. 8 | 000227 of 2025 art. 1.5.3.4.1.1 |
| 435 | 000013 of 2021 arts. 3 and 8 | 000227 of 2025 arts. 1.5.3.2.2 and 1.5.3.4.1.1 |
| 721 | 000013 of 2021 and its | 000227 of 2025, arts. 1.5.3.1.1 to 1.5.3.9.8, and its electronic payroll |
| 845 | 000013 of 2021 arts. 1, 5, 22 | 000227 of 2025 arts. 1.5.3.1.1, 1.5.3.3.1, 1.5.3.8.1 |
| 1074 | 000013 of 2021 | 000227 of 2025, arts. 1.5.3.1.1 to 1.5.3.9.8, |
| 1086 | 000013 of 2021 arts. 15 and 23 | 000227 of 2025 arts. 1.5.3.5.1.7 and 1.5.3.8.2 |
| 1089 | 000013 of 2021 art. 22 | 000227 of 2025 art. 1.5.3.8.1 |
| 1189 | 000013 of 2021 arts. 15, 22, 23 | 000227 of 2025 arts. 1.5.3.5.1.7, 1.5.3.8.1, 1.5.3.8.2 |
| 4527 | 000013 of 2021 | 000227 of 2025, arts. 1.5.3.1.1 to 1.5.3.9.8, |
| 6085 | 000013 of 2021 arts. 3 and 8 | 000227 of 2025 arts. 1.5.3.2.2 and 1.5.3.4.1.1 |
| 6092 | implemented by Resolution DIAN 000013 of 11 February 2021 | governed by Resolution DIAN 000227 of 2025, arts. 1.5.3.1.1 to 1.5.3.9.8 (which compile Resolution DIAN 000013 of 11 February 2021), |
| 6366 | 000013 of 11 February 2021 arts. 1, 2, 3, 5, 8, 15, 22, 23, 24, 26 | 000227 of 2025 arts. 1.5.3.1.1, 1.5.3.2.1, 1.5.3.2.2, 1.5.3.3.1, 1.5.3.4.1.1, 1.5.3.5.1.7, 1.5.3.8.1, 1.5.3.8.2, 1.5.3.8.3, 1.5.3.8.5 |
| 6409 | 000013 of 2021 art. 24 — but if issued, it must carry the art. 5 | 000227 of 2025 art. 1.5.3.8.3 — but if issued, it must carry the art. 1.5.3.3.1 |
| 6416 | 000013 of 2021 art. 22 | 000227 of 2025 art. 1.5.3.8.1 |
| 6421 | 000013 of 2021 article 5, which lists the mandatory content of the electronic payroll support document, combined with article 24 | 000227 of 2025 article 1.5.3.3.1, which lists the mandatory content of the electronic payroll support document, combined with article 1.5.3.8.3 |
| 6422 | 000013 of 2021 art. 5 | 000227 of 2025 art. 1.5.3.3.1 |
| 6472 | 000013 of 11 February 2021 arts. 5, 24, 26 | 000227 of 2025 arts. 1.5.3.3.1, 1.5.3.8.3, 1.5.3.8.5 |
| 6529 | 000013 of 2021 arts. 5 and 24 | 000227 of 2025 arts. 1.5.3.3.1 and 1.5.3.8.3 |
| 6585 | 000013 of 2021 arts. 5, 22, 24, 26; Resolution DIAN 000227 of 2025 | 000227 of 2025 (including arts. 1.5.3.3.1, 1.5.3.8.1, 1.5.3.8.3, 1.5.3.8.5) |
| 6691 | 000013 of 2021 art. 3 | 000227 of 2025 art. 1.5.3.2.2 |
| 6725 | 000013 of 2021 art. 3 | 000227 of 2025 art. 1.5.3.2.2 |
| 7803 | 000013 of 2021 art. 3 | 000227 of 2025 art. 1.5.3.2.2 |
| 7964 | 000013 of 2021 art. 3 | 000227 of 2025 art. 1.5.3.2.2 |

## Other corrections carried (brief steps 6, 7, 8)

- ARL on enjoyed vacation (Decreto 1072/2015 art. 2.2.4.2.1.6 num. 1.3): paras 2351 (S11) and 5086 (S79) corrected. Table "Create a reference table classifying common pay components", row "Vacation pay", column CB (legend: CB includes occupational risk): "Yes" -> "Yes – health and pension, on the last IBC reported before the vacation (Decree 780 of 2016 art. 3.2.5.1); no occupational-risk contribution (Decree 1072 of 2015 art. 2.2.4.2.1.6 num. 1.3)". Paras 2950 (S20) and 261 (S04) already state the rule.
- 40% denominator claim: only in para 3000; removed through the S23 fix. Other 40% mentions (1214, 1223, 2326, 2999, 3905-3919, 6047-6057, 6827, 7939) say nothing about the denominator.
- Report-spec ids: 725 (S05), 6089 (S82), 6133 "CO-RPT-001" -> "CO-DIAN-001"; Module 10.1 table ID column CO-RPT-001..006 -> CO-DIAN-001, CO-DIAN-002, CO-PILA-003, CO-DIAN-004, CO-DIAN-005, CO-CESANTIAS-006; CO-RPT-007 (disability-hiring report, out of scope per S83) -> "None (out of scope)".
- Pensioners' health (client answer Q1): the CCG did not state the rate. One sentence added to Module 5 'Deliverable: Comprehensive summary of current contribution rates', row 'Employed old-age pensioner' (para 2989): 4% for a pension of 1 minimum wage, 10% above 1 and up to 3, 12% above 3, from 2024 (Law 100 of 1993 art. 204 par. 5, inciso added by Law 2294 of 2023 art. 78; Resolution MSPS 1271 of 2023 art. 1, PILA Technical Annex 1). Read: Ley 100/1993 art. 204 par. 5 on Función Pública (`raw/docs/oficiais/CO/2026-10-21-Ley-100-1993-FuncionPublica.html`: from 2022 '1 SMLMV 4% / >1 SMLMV y hasta 2 SMLMV 10% / >2 ... 12%' and the inciso '(Adicionado por el Art. 78 de la Ley 2294 de 2023)': 'El aporte a salud a cargo de los pensionados que devengan entre 2 y 3 salarios mínimos se reducirá del 12% al 10%, el cual regirá a partir de la vigencia de 2024 previa reglamentación'); Res. MSPS 1271/2023 art. 1 num. 5 (`2026-10-21-Res-MSPS-1271-2023-colpensiones.htm`): 'A partir del año 2024 las tarifas a reportar serán las siguientes: ... 1 SMLMV 4% / >1 SMLMV y hasta 3 SMLMV 10% / >3 SMLMV 12%'.
- Version: cover 'Version 1.0' -> 'Version 1.3'; cover 'CO-CCG-001 v1.0' -> 'v1.3'; cover date 'September 2026' -> '21 October 2026'; footer 'CO-CCG-001 v1.0' -> 'v1.3'. Version Control row added after 1.2: '1.3 | 21 October 2026 | Wallisson Gomes | Suggested edits of 18 September – 13 October 2026 resolved against primary sources; Resolution DIAN 000013 of 2021 citations updated to Resolution DIAN 000227 of 2025; pensioners' health contribution rates added (Module 5).' Rows 1.0, 1.1, 1.2 kept (1.2 text = S04 fix). Date 21 October 2026 per the coordinator's correction of the brief.

| Date | Window | What |
|---|---|---|
| 2026-10-21 | geral (agent) | v1.3 built locally from the gdoc export; this conferência, OPEN-ITEMS.md and REJECTED-S86-S87.md written |

## Round 2 - verifier FAIL (55 required fixes, `CCG-verification.json`), applied 21 Oct 2026

Base of round 2 = round-1 v1.3 (md5 856176ec86858c73358f8810202d3886). Only word/document.xml changed; the other 18 zip entries are byte-identical to round 1 (checked). Paragraph numbers = `w:p` index in v1.3 (the verifier's numbering). Every verifier "current" text was matched exactly before replacing, and every result equals the verifier's "proposed" text (para 3002: equal apart from line breaks, which stay as `w:br` lines of the code block). Edits are character-level diffs, so the run formatting around them is kept. Where the diff left bold in the wrong place, bold was set deliberately: 5019, 5271, 3024 and 5385, where bold now marks the rule ("No", "does not enter ... base", "does enter the payroll-levy base").

Checks after round 2: `w:ins`/`w:del` 0; python-docx opens it (1,383 paragraphs, 248 tables); inspect_docx gives 68,659 words and 212 headings with the same text as the base; 1 residual marker (the pre-existing "placeholder" NE rule). "Open item", "RESOLVED", "CONFIRMED", "this pass" and "not verified" are gone from the resolved items. What remains is the genuine open items the verifier said to keep (884, 896, 3453, 4087, 6909) and ordinary uses of "confirmed by <source>". The only literal "*" left is in 4461, where the asterisks are bullets in a code-block flowchart.

### Fixes applied

| # | Para | Before (changed part) | After (changed part) | Why |
|---|---|---|---|---|
| V00 | 2484 | Yes | No – vacation paid in cash is not salary and stays out of the health, pension and occupational-risk base (Consejo de Estado, Sección Cuarta, exp. 26941 of 4 April 2024; unification ruling exp. 25185 of 9 December 2021, rule 1) | Row 'Cash compensation of vacation (up to half)', column CB (legend para 2362: health, pension, occupational risk, solidarity fund) says 'Yes'; verified rule: excluded. PL cell 2485 'Yes' is correct and stays. |
| V02 | 3024 | Yes — paid rest | No for health, pension and occupational risk – vacation paid in cash is not salary (Consejo de Estado, Sección Cuarta, exp. 26941 of 4 April 2024; unification ruling exp. 25185 of 9 December 2021, rule 1); it does enter the payroll-levy base (Law 21 of 1982 art. 17) | Termination-month table 'In the contribution base?' row 'Accrued vacation paid in cash' says 'Yes — paid rest'. |
| V03 | 5019 | also enters the social-security contribution base and the payroll-levy base, because vacation is paid rest, not a statutory benefit | is not salary, so it does not enter the health, pension and occupational-risk contribution base (Consejo de Estado, Sección Cuarta, exp. 26941 of 4 April 2024; unification ruling exp. 25185 of 9 December 2021, rule 1); it does enter the payroll-levy base for the family compensation fund, SENA and ICBF, because Law 21 of 1982 art. 17 covers paid rest whether taken or paid in cash (Law 89 of 1988 art. 1 par. 1; Consejo de Estado, Sala de Consulta, concept 2027 of 4 October 2010) | States the payout 'also enters the social-security contribution base'. |
| V04 | 5271 | Contributory. Vacation is paid rest, not a statutory benefit, so the payout enters the contribution base and the payroll-levy base. This is the single most frequently missed line | Not in the health, pension and occupational-risk contribution base: vacation compensation is not salary (Consejo de Estado, Sección Cuarta, exp. 26941 of 4 April 2024; unification ruling exp. 25185 of 9 December 2021, rule 1). It does enter the payroll-levy base (family compensation fund, SENA, ICBF: Law 21 of 1982 art. 17; Law 89 of 1988 art. 1 par. 1). The payroll-levy line is the one most frequently missed | Module 9 tax table, row 'Social security': 'Contributory ... enters the contribution base'. |
| V05 | 5385 | Yes | No (Consejo de Estado, Sección Cuarta, exp. 26941 of 4 April 2024; unification ruling exp. 25185 of 9 December 2021, rule 1) | ETP reference table, row 'Unused vacation, paid in cash', column 'Contribution base' = 'Yes'. Column 'Payroll-levy base' (5386) 'Yes' stays. |
| V06 | 5388 | Most commonly missed contributory | Payroll-levy base only (Law 21 of 1982 art. 17; Law 89 of 1988 art. 1 par. 1); the most commonly missed levy | Notes cell 'Most commonly missed contributory line' implies a social-security contribution. |
| V07 | 5615 | and the vacation payout are contributory. The service bonus, severance savings, interest and the indemnity are not | is contributory to health, pension and occupational risk. The vacation payout is not salary and stays out of that base (Consejo de Estado, Sección Cuarta, exp. 26941 of 4 April 2024; unification ruling exp. 25185 of 9 December 2021, rule 1), but it enters the payroll-levy base (Law 21 of 1982 art. 17; Step 10). The service bonus, severance savings, interest and the indemnity are in neither base | Step 7 intro counts the vacation payout as contributory. |
| V08 | 5620 | + 3,187,500 vacation | (vacation payout excluded) | Step 7 contribution-base computation includes 3,187,500 vacation. |
| V09 | 5621 | 7,687,500 | 4,500,000 | Recomputed base. |
| V10 | 5626 | 307,500 | 180,000 | 4% x 4,500,000 = 180,000 (already a multiple of 100; Decreto 780/2016 art. 3.2.1.5 num. 2). |
| V11 | 5627 | 307,500 | 180,000 | 4% x 4,500,000 = 180,000 (already a multiple of 100; Decreto 780/2016 art. 3.2.1.5 num. 2). |
| V12 | 5629 | 307,500 | 180,000 | 4% x 4,500,000 = 180,000 (already a multiple of 100; Decreto 780/2016 art. 3.2.1.5 num. 2). |
| V13 | 5630 | 307,500 | 180,000 | 4% x 4,500,000 = 180,000 (already a multiple of 100; Decreto 780/2016 art. 3.2.1.5 num. 2). |
| V14 | 5632 | 7,687,500 ≥ 4 minimum wages (7,003,620) → triggered | 4,500,000 < 4 minimum wages (7,003,620) → not triggered | Solidarity fund no longer triggered once the vacation payout is out of the base. |
| V15 | 5633 | 76,900 (up to the nearest 100) | 0 | Recomputed. |
| V16 | 5636 | 691,900 | 360,000 | 180,000 + 180,000 + 0. |
| V17 | 5638 | is what pushes the base over the 4-minimum-wage solidarity trigger. Without it the base would have been 4,500,000 and no solidarity contribution would have been due | does not enter the health and pension base, so it does not trigger the solidarity fund: the base stays at 4,500,000, below 4 minimum wages (7,003,620). It does enter the payroll-levy base (Step 10) | The note asserts the opposite rule. |
| V18 | 5651 | 691,900 | 360,000 | (B) non-taxable mandatory contributions actually deducted change with Step 7. |
| V19 | 5654 | 21,995,600 | 22,327,500 | 22,687,500 − 360,000. |
| V20 | 5659 | 21,995,600 = 5,498,900 | 22,327,500 = 5,581,875 | Recomputed. |
| V21 | 5662 | 21,995,600 = 8,798,240 | 22,327,500 = 8,931,000 | Recomputed. |
| V22 | 5665 | 21,995,600 | 22,327,500 | Recomputed. |
| V23 | 5666 | 18,547,645 | 18,879,545 | Recomputed. |
| V24 | 5668 | 18,547,645 | 18,879,545 | Recomputed. |
| V25 | 5669 | 354.1384 | 360.4755 | Recomputed. |
| V26 | 5671 | 150 and ≤ 360 → marginal 28% | 360 and ≤ 640 → marginal 33% | Base now falls in the 33% band (CCG table paras 3474-3476: '(base − 360) × 33% + 69'). |
| V27 | 5674 | 354.1384 − 150) × 28% + 10 = 57.1588 + 10 = 67.1588 | 360.4755 − 360) × 33% + 69 = 0.1569 + 69 = 69.1569 | Recomputed. |
| V28 | 5677 | 67.1588 | 69.1569 | Recomputed. |
| V29 | 5678 | 3,517,372.60 | 3,622,024.65 | Full-precision method used by the original line (24,905 × 33% + 69 × 52,374 = 8,218.65 + 3,613,806). |
| V30 | 5703 | 3,517,372.60 | 3,622,024.65 | Recomputed. |
| V31 | 5722 | 307,500 | 180,000 | Recomputed. |
| V32 | 5724 | 307,500 | 180,000 | Recomputed. |
| V33 | 5726 | 76,900 | 0 | Solidarity fund not triggered. |
| V34 | 5728 | 3,517,372.60 | 3,622,024.65 | Recomputed. |
| V35 | 5730 | 22,468,227.40 | 22,695,475.35 | 26,677,500 − 180,000 − 180,000 − 0 − 3,622,024.65. |
| V36 | 5739 | 7,687,500 | 4,500,000 | Employer pension base = contribution base without the vacation payout. |
| V37 | 5740 | 922,500 | 540,000 | 12% × 4,500,000. |
| V38 | 5743 | 7,687,500 | 4,500,000 | Health base (exempt anyway). |
| V39 | 5747 | 7,687,500 | 4,500,000 | ARL base excludes the vacation payout. |
| V40 | 5748 | 40,128.75 → 40,200 | 23,490.00 → 23,500 | 0.522% × 4,500,000 = 23,490 → next 100. |
| V41 | 5764 | 1,270,200 | 871,000 | 540,000 + 0 + 23,500 + 307,500 (CCF on the 7,687,500 payroll-levy base, which correctly keeps the vacation payout) + 0 + 0. |
| V42 | 5772 | 27,947,700 | 27,548,500 | 26,677,500 + 871,000. |
| V43 | 5074 | substituted by Decreto 1990 de 2016 | modified by Decreto 1990 de 2016 art. 1 | Decreto 1990/2016 art. 1 says 'Modifíquese el artículo 3.2.1.5' (art. 2 is the one that substitutes Title 2). Figures themselves are correct. |
| V44 | 2996 | and a reduced retirement age. Rate not verified for 2026 — see the open item | of 10 percentage points (26% total) and a reduced retirement age — see the note | Says 'Rate not verified for 2026' while para 2999 (S21, v1.3) states the 10 points are confirmed from Decreto-Ley 2090/2003 art. 5. |
| V45 | 2999 | Open item — high-risk pension activities. Decree-Law 2090 of 2003 establishes the high-risk activities that carry an additional employer pension contribution and a reduced retirement age, and the electronic payroll XML carries a required AltoRiesgoPension flag. The contribution-return rate table of Resolution 2388 of 2016 shows a total pension rate of 26% for a high-risk contributor (against the standard 16%), implying an additional 10 percentage points borne by the employer. CONFIRMED: the | High-risk pension activities. Decree-Law 2090 of 2003 establishes the high-risk activities that carry an additional employer pension contribution and a reduced retirement age, and the electronic payroll XML carries a required AltoRiesgoPension flag. The contribution-return rate table of Resolution 2388 of 2016 shows a total pension rate of 26% for a high-risk contributor (against the standard 16%), implying an additional 10 percentage points borne by the employer. The | Residual process markers ('Open item', 'CONFIRMED:') on a rate that is now confirmed; the genuine open point stays in the 'Still open:' sentence. |
| V46 | 3106 | the open item in Module | Module | Points to an 'open item' that is now a confirmed rule with one residual open point. |
| V47 | 4815 | See the open item below | 66.67% (two thirds) of salary, never below the minimum wage (Labour Code art. 227; Constitutional Court C-543 of 2007; Concepto MinSalud 202311602174531 of 20 October 2023) | Rate cell still points to an open item that v1.3 resolved (S53/S54). |
| V48 | 4924 | 66.67% (see the open item | 66.67%, never below the minimum wage (Constitutional Court C-543 of 2007 | '(see the open item)' is stale after S53/S54. |
| V49 | 4827 | Open item — the rate for the employer's first two days. Decree 2943 of 2013 art. 1, compiled at Decree 780 of 2016 art. 3.2.1.10, allocates *"the | Rate for the employer's first two days. Decree 2943 of 2013 art. 1, compiled at Decree 780 of 2016 art. 3.2.1.10, allocates "the | Residual 'Open item —' label and a stray Markdown asterisk ('*"the cash...'); paras 4827-4829 are one sentence split over three w:p (pre-existing). |
| V50 | 4828 | not* | not | Stray Markdown asterisk ('does not*'). |
| V51 | 4829 | Carried in the QA report. RESOLVED: | Resolution: | 'Carried in the QA report.' followed by 'RESOLVED:' in the same paragraph (S53). |
| V52 | 4830 | Open item — the minimum-wage floor on incapacity payments. Where 66.67% of the employee's salary falls below the minimum wage, market practice and settled administrative doctrine top the payment up to one minimum wage. The primary regulatory source for that floor was not retrieved this pass. Mercans default: apply the floor, configurable. Carried in the QA report. RESOLVED 19 September 2026: Corte Constitucional Sentencia C-543 de 2007 holds that the monetary sickness benefit (auxilio monetario por enfermedad de origen comun | The minimum-wage floor on incapacity payments. Where 66.67% of the employee's salary falls below the minimum wage, market practice and settled administrative doctrine top the payment up to one minimum wage. Mercans default: apply the floor, configurable. Corte Constitucional Sentencia C-543 de 2007 holds that the monetary sickness benefit (auxilio monetario por enfermedad de origen común | Residual process markers ('Open item', 'not retrieved this pass', 'Carried in the QA report', 'RESOLVED 19 September 2026') contradicting the resolved rule in the same paragraph (S54). |
| V53 | 7718 | CONFIRMED AGAIN 19 September 2026, directly from the statute's own sequence: Ley 100 de 1993 art. 18, as rewritten by Ley 797 de 2003 art. 5, states the rules in this order within the SAME article -- (i) the base is the monthly salary, (ii) "el limite de la base de cotizacion sera de 25 salarios minimos", THEN, as the article's next and final substantive rule, (iii) "las cotizaciones de los trabajadores cuya remuneracion se pacte bajo la modalidad de salario integral, se calculara sobre el 70% de dicho salario." Rule (iii) computes what "la base de cotizacion" IS for an integral-salary worker; ... | The statute's own sequence confirms this: Ley 100 de 1993 art. 18, as rewritten by Ley 797 de 2003 art. 5, states the rules in this order within the SAME article -- (i) the base is the monthly salary, (ii) "el limite de la base de cotizacion sera de 25 salarios minimos", THEN, as the article's next and final substantive rule, (iii) "las cotizaciones de los trabajadores cuya remuneracion se pacte bajo la modalidad de salario integral, se calculara sobre el 70% de dicho salario." Rule (iii) computes what "la base de cotizacion" IS for an integral-salary worker; that resulting figure is then the  ... | S84 removed the UGPP guidance citations but left 'This is not merely UGPP's reading' (orphan reference) and the dated 'CONFIRMED AGAIN 19 September 2026' marker. |
| V54 | 725 | substituted by Decree 1990 of 2016 art. 1; Tax Code (Decree-Law 624 of 1989) art. 577; Resolution DIAN 000227 of 2025, arts. 1.5.3.1.1 to 1.5.3.9.8, and its electronic payroll Technical Annex §1.1.1.1; Resolution DIAN 000227 of 2025 art. 1.3.7.1.1. | amended by Decree 1990 of 2016 art. 1; Tax Code (Decree-Law 624 of 1989) art. 577; Resolution DIAN 000227 of 2025 arts. 1.3.7.1.1 and 1.5.3.1.1 to 1.5.3.9.8, and its electronic payroll Technical Annex §1.1.1.1. | Cosmetic: the Res. 227 replacement left the same resolution cited twice in a row in this legal-basis line. Also "as substituted" -> "as amended" here (same art. 1, same reason as 5074). |
| V01 | 3002 | pay INCLUDED /         1.2  Apply the 40% clamp: if PACTED non-salary payments > 40% of total remuneration, /              add the excess back into the base   (Law 1393 of 2010 art. 30) /         1.3  All-inclusive salary: base = 70% of the salary /         1.4  Floor: base >= 1 minimum wage, pro-rated to contributory days /         1.5  Ceiling: base <= 25 minimum wages = 43,772,625 /         1.6  Round the base UP to the nearest whole peso /  / STEP 2  Build the PAYROLL-LEVY BASE (separate, no ceiling) /         2.1  Sum all salary elements PLUS statutory and contractual paid rest days /  | taken: health and pension on the IBC reported before the vacation began, not on the vacation pay (Decree 780 of 2016 art. 3.2.5.1); no occupational-risk contribution for those days (Decree 1072 of 2015 art. 2.2.4.2.1.6 num. 1.3) /              - vacation paid in cash (during employment or on termination) EXCLUDED (CE S4 exp. 26941 of 2024; SU exp. 25185 of 2021, rule 1) /         1.2  Apply the 40% clamp: if PACTED non-salary payments > 40% of total remuneration, /              add the excess back into the base   (Law 1393 of 2010 art. 30) /         1.3  All-inclusive salary: base = 70% of the ... | Module 5.2 STEP 1.1 says 'vacation pay INCLUDED' in the contribution base (which also feeds ARL in STEP 5): wrong for cash vacation and imprecise for vacation taken (prior-IBC rule, no ARL). STEP 2.1 clarification aligns with Q4. (Lines are separated by spaces in the extracted text; keep the origina |
| A644 | 644 | substituted | amended | Not in the JSON: same wording error as 5074 (Decreto 1990/2016 art. 1 "Modifíquese el artículo 3.2.1.5"), aligned for consistency. |

Markdown asterisks (coordinator item 5): the 13 listed paragraphs, plus the paragraphs that hold the other half of a pair or the same artefact: 432, 433, 434, 1227, 1253, 1769, 5277, 5278, 5825, 6163, 6187, 6478, 6483. `*term*` became italic (Spanish terms and emphasis, the document's convention, e.g. *auxilio monetario*); `**text**` became bold (431-432, 433-434, 1768-1769, 1797). The quotes split across paragraphs (1226-1227, 1252-1253, 4827-4828) became plain text in quotation marks. In 1227 and 4828 the italic had landed on the wrong words (" A valid written non-salary pact ...", " to the employer, but does not"), so those runs were set to regular. 4461 not touched (bullets inside the code block).

### Module 9 termination worked example - recomputed (coordinator item 2)

Rules used, all stated in the CCG itself: contribution base = salary only (vacation paid in cash out: CE S4 exp. 26941/2024, SU 25185/2021 rule 1); employee 4% + 4%, solidarity 1% only if base >= 4 SMMLV; contributions rounded up to the next 100 (Decreto 780/2016 art. 3.2.1.5 num. 2, as amended by Decreto 1990/2016 art. 1); art. 388 depuration (A) - (B) mandatory contributions = (C); 25% exempt income of ET art. 206 num. 10 capped at 790 UVT / 12 per month; 40% check; ET art. 383 table; payroll levies on salary + vacation payout (Ley 21/1982 art. 17). UVT 2026 = 52,374; SMMLV 2026 = 1,750,905.

| Line | v1.3 round 1 | My recomputation | Verifier | Computation |
|---|---|---|---|---|
| Contribution base | 7,687,500 | 4,500,000 | 4,500,000 | salary only |
| Health 4% / pension 4% | 307,500 / 307,500 | 180,000 / 180,000 | 180,000 / 180,000 | 4% × 4,500,000, already a multiple of 100 |
| Solidarity 1% | 76,900 | 0 | 0 | 4,500,000 < 4 × 1,750,905 = 7,003,620 |
| Total employee SS | 691,900 | 360,000 | 360,000 | |
| (A) taxable payments | 22,687,500 | 22,687,500 | - | 4,500,000 + 3,187,500 + 15,000,000 (unchanged) |
| (C) subtotal | 21,995,600 | 22,327,500 | 22,327,500 | 22,687,500 − 360,000 |
| (E) 25% exempt | 25% = 5,498,900, capped 3,447,955 | 25% = 5,581,875, capped 3,447,955 | same | cap = 790 × 52,374 ÷ 12 = 3,447,955 |
| (F) 40% check | 8,798,240 | 8,931,000 | 8,931,000 | 40% × 22,327,500; 3,447,955 within |
| (G) taxable base | 18,547,645 | 18,879,545 | 18,879,545 | 22,327,500 − 3,447,955 |
| (H) in UVT | 354.1384 | 360.4755 | 360.4755 | 18,879,545 ÷ 52,374 = 360.47552 |
| Band | >150-360, 28% | >360-640, 33% | same | ET art. 383 table (CCG paras 3474-3476) |
| Withholding in UVT | 67.1588 | 69.1569 | 69.1569 | (360.4755 − 360) × 33% + 69 |
| Withholding COP | 3,517,372.60 | 3,622,024.65 | 3,622,024.65 | full precision, the same method as the original line: (18,879,545 − 360 × 52,374) × 33% + 69 × 52,374 = 24,905 × 0.33 + 3,613,806 = 8,218.65 + 3,613,806 (69.1569 × 52,374 at 4 decimals would give 3,622,023.48; the CCG line shows the UVT figure rounded and computes COP at full precision) |
| Read 2 (service bonus) | 0.00 | 0.00 | - | unchanged |
| Total gross | 26,677,500 | 26,677,500 | - | unchanged |
| Net settlement | 22,468,227.40 | 22,695,475.35 | 22,695,475.35 | 26,677,500 − 180,000 − 180,000 − 0 − 3,622,024.65 |
| Employer pension 12% | 922,500 (base 7,687,500) | 540,000 (base 4,500,000) | same | |
| Employer health 8.5% | 0 (exempt) | 0 (exempt, base 4,500,000) | same | Tax Code art. 114-1 |
| Occupational risk 0.522% | 40,128.75 → 40,200 | 23,490.00 → 23,500 | same | 0.522% × 4,500,000, up to the next 100 |
| Family compensation fund 4% | 307,500 (base 7,687,500) | 307,500 (base 7,687,500, unchanged) | same | payroll-levy base keeps the vacation payout |
| SENA / ICBF | 0 exempt (base 7,687,500) | unchanged | same | |
| Employer contributions | 1,270,200 | 871,000 | 871,000 | 540,000 + 0 + 23,500 + 307,500 |
| Total employer cost | 27,947,700 | 27,548,500 | 27,548,500 | 26,677,500 + 871,000 |

My figures equal the verifier's in every line (script recomputation, `ccg13` scratchpad), so the verifier's proposed texts were applied as given.

| 2026-10-21 | geral (agent) | Round 2: 55 verifier fixes + "as amended" in 725/644 + Markdown asterisks; md5 b52beb6beeb4e59e5adee3b8db84c6f1 |

## Round 3 - verifier round 2 (`CCG-verification.json` -> round2.required_fixes), applied 21 Oct 2026

Base = round-2 v1.3 (md5 b52beb6beeb4e59e5adee3b8db84c6f1). Only word/document.xml changed (two paragraphs); the other 18 zip entries are byte-identical (checked); no `w:ins`/`w:del`; python-docx opens it (1,383 paragraphs). Before replacing, each "current" text matched exactly; each result equals the "proposed" text (character-level diff, run formatting kept; both paragraphs are regular text).

| Para | Before | After | Source |
|---|---|---|---|
| 1225 (Module 3, Step 2 contribution base) | ... Vacation pay is included, because vacation is paid rest, not a statutory benefit in the art. 128 sense. | ... Vacation is paid rest, not a statutory benefit in the art. 128 sense: for vacation taken, health and pension are paid on the contribution base reported before the vacation began, not on the vacation pay (Decree 780 of 2016 art. 3.2.5.1), with no occupational-risk contribution for those days (Decree 1072 of 2015 art. 2.2.4.2.1.6 num. 1.3); vacation paid in cash, during employment or on termination, is excluded (Consejo de Estado, Sección Cuarta, exp. 26941 of 4 April 2024; unification ruling exp. 25185 of 9 December 2021, rule 1). | CE S4 26941/2024; SU 25185/2021 rule 1; Decreto 780/2016 art. 3.2.5.1; Decreto 1072/2015 art. 2.2.4.2.1.6 num. 1.3 |
| 5222 (Module 9, residence-status table, "Social security on the settlement") | Vacation is contributory; the other accrued entitlements and the indemnity are not | Accrued vacation paid on termination is not in the health, pension and occupational-risk base (Consejo de Estado, Sección Cuarta, exp. 26941 of 4 April 2024; unification ruling exp. 25185 of 9 December 2021, rule 1) but enters the payroll-levy base (Law 21 of 1982 art. 17); the other accrued entitlements and the indemnity are in neither | CE S4 26941/2024; SU 25185/2021 rule 1; Ley 21/1982 art. 17; Ley 89/1988 art. 1 par. 1 |

| 2026-10-21 | geral (agent) | Round 3: paras 1225 and 5222; md5 abd9e2595675df3ea8e96cca4d21e4cb |
| 2026-10-21 | geral (Colômbia) | Copiado para o Drive com o ok do usuário; md5 da cópia idêntico |

| 2026-10-22 | geral (Colômbia) | Convertido em Google Doc novo CO-CCG-001_v1.3 (Save as Google Docs); export txt = docx local (Res. 227 x34, Res. 13 x2 só no VC, exemplos corrigidos, 0 marcas de revisão); o Doc v1.2 continua na pasta |

## Arquivos da entrega
- [[Research Pipeline/Colombia/2026-10-21-alinhamento-CCG/OPEN-ITEMS|OPEN-ITEMS]]: Itens que ficaram abertos na CCG v1.3 (módulo, item, o que fecha); nada inventado para fechar lacuna.
- [[Research Pipeline/Colombia/2026-10-21-alinhamento-CCG/REJECTED-S86-S87|REJECTED-S86-S87]]: Sugestões S86 e S87 rejeitadas (texto literal) na linha do bônus do Módulo 13 da CCG v1.2.
- [[Research Pipeline/Colombia/2026-10-21-alinhamento-CCG/SUGGESTIONS-DECISIONS-2026-10-22|SUGGESTIONS-DECISIONS-2026-10-22]]: Decisão e motivo por sugestão (93 alterações da CCG v1.2, lotes A-D) com fonte nos vereditos.
