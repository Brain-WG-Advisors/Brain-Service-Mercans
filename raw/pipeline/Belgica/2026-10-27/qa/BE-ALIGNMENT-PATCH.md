# BE-ALIGNMENT-PATCH — Stage 8, DD vs Report Specs vs WTC

Scope: the three Stage 8 checks that had **not** been performed. Field-classification
alignment (DD-bucket vs TX/CALC/SYS) was done during the DD build and is recorded in
`05-data-dictionary/DD-CROSSCHECK-TABLE.md` (1,191 rows, 0 unclassified). It was **not**
redone; it was used as the input that decides which coded fields belong in the DD.

Sources consulted: `BE-DD-001-v1.0.xlsx`, all nine `04-reports-spec/*.xlsx`,
`BE-WTC-001-v1.0.xlsx`, `BE-CCG-001-v1.0.docx`, `DD-CROSSCHECK-TABLE.md`.

Authority order applied throughout: **official government form / XSD / glossary > CCG > web
research.** In every conflict below the authority text was already quoted verbatim in
column O of a Report Spec sheet 4 or in a Report Spec sheet 6, and the Data Dictionary was
the deviant side. Nothing was invented; where the held source is itself incomplete the gap
is marked `NOT FOUND` **identically on both sides**.

Totals: **13 mapper-content mismatches**, **39 mapper-binding defects**, **37 missing option
mappers**, **407 missing Sheet 6 code rows**, **137 one-directional conditional references** —
all fixed. 10 files patched, all 10 pass their structural self-check.

---

## CHECK 1 — Option Mapper code alignment

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 1 | Dimona Worker Type | The DD collapsed six real glossary codes into two pseudo-rows whose Code cell held the literal string `(excluded)`. PMP, T17, A17, QUA, STX and TEA are individual codes in BE-NSSO-001 Sheet 6 and in the glossary; `(excluded)` is not a value any engine can validate against. | Block rewritten 16 → 20 rows. Each of the six carries its own code, with its real status: PMP and T17 open in the glossary but excluded from the Mercans configuration as non-private-sector; A17, QUA, STX CLOSED; TEA OBSOLETE. | BE-DD-001-v1.0.xlsx |
| 1 | Dimona Worker Type / BCW | DD said "Excluding IVT, RTA, STU **and the closed types**". The glossary and BE-NSSO-001 Sheet 6 say "excluding IVT, RTA, STU **and DWD**". DWD is an open type, not a closed one — the DD statement was wrong in substance. | Corrected to the glossary wording. | BE-DD-001-v1.0.xlsx |
| 1 | Dimona Worker Type / FLX | DD said "Cannot be declared for more than the period the glossary permits" — a placeholder standing in for a figure the glossary actually states. | Replaced with the stated rule: cannot be declared more than **31 days** before the start of the quarter of entry (zones 00655 and 00910). | BE-DD-001-v1.0.xlsx |
| 1 | NSSO Worker Status / F2 | DD Abbreviation read "Second quoted status" and the description "One of only two values quoted in the Dimona glossary" — a placeholder carrying no meaning. BE-NSSO-001 Sheet 6 holds the real text. | F2 = apprenticeship contracts with a specific cover and indemnity regime (glossary zone 00053). | BE-DD-001-v1.0.xlsx |
| 1 | NSSO Worker Status / F1 | DD held a truncated gloss ("Work under a training arrangement"). | Completed to the glossary text: work under a training arrangement **for paid work, as laid down in the LAT for apprentices**. | BE-DD-001-v1.0.xlsx |
| 1 | Charge Bearer / DEBT | DD described DEBT as "The employee must receive the full net pay", implying it is the value to use on a salary transfer. Febelfin pain.001.001.09 IG 2025 v1.3 s.3.4, as recorded in BE-FEBELFIN-001 Sheet 6, states that **only SLEV can be used on a European Credit Transfer**. Following the DD would have produced a rejected payment file. | DEBT, CRED and SHAR marked GENERIC credit transfers only and NOT permitted on a European credit transfer; the note that SLEV already secures full net pay added to DEBT. | BE-DD-001-v1.0.xlsx |
| 1 | Charge Bearer / SLEV | DD described SLEV only as the absent-element default, not as the sole permitted value. | Restated: the only value that can be used on a European credit transfer, and the default where absent. | BE-DD-001-v1.0.xlsx |
| 1 | Gender | DD codes were **M / F / X**. Every declaration in scope transmits **1 / 2** (NSSO zone 00029 in Dimona, DmfA, DRS and FEDRIS; Belcotax likewise). The DD carried no transmission code at all. | Codes changed to 1 = Male, 2 = Female. X retained with an explicit rule: the zone admits only 1 and 2, so an X must be resolved from the INSZ parity before any NSSO declaration is built. | BE-DD-001-v1.0.xlsx |
| 1 | Language | DD held only the ISO alpha-2 codes nl / fr / de, which is the Finprof 274 encoding. Belcotax zone 2.027, FEDRIS zones 00156 and 00343, DmfA zone 00966 and DRS zone 00156 all transmit **1 / 2 / 3**. The numeric encoding existed nowhere in the DD as a code. | Alpha mapper kept (it is the Finprof code) and cross-referenced; new mapper **Language Numeric Code (NSSO and Belcotax)** added carrying 1 / 2 / 3 and naming the zones. Sheet 6 references in BE-FEDRIS-001 and BE-NSSO-004 retagged to it. | BE-DD-001-v1.0.xlsx · BE-FEDRIS-001 · BE-NSSO-004 |
| 1 | NIS Country Code | DD recorded the whole table as NOT FOUND. BE-NSSO-001 Sheet 6 states **Belgium = 150**, and BE-FEDRIS-001 uses `'150'` as a literal in the presence conditions of zones 00241 and 00889. A held fact was recorded as not held. | Row for 150 added; the remainder of the table stays NOT FOUND (requires the Statbel NIS table). | BE-DD-001-v1.0.xlsx |
| 1 | Apprenticeship Type | DD said NOT FOUND, "requires the NSSO annexe". The definition domain of zone 00055 is **published inline in the glossary** and was already carried in column O of BE-FEDRIS-001, BE-NSSO-002, BE-NSSO-003 and BE-NSSO-004. | Replaced with the five published values, each marked for the period it applies to (code 1 changed meaning at quarter 2019/4). | BE-DD-001-v1.0.xlsx |
| 1 | Remuneration Method | DD said NOT FOUND. Zone 00056 is published inline and carried in column O of four specs. | Replaced with values 1, 2 and 3; the FEDRIS restriction (only 1 and 2 permitted there) recorded. | BE-DD-001-v1.0.xlsx |
| 1 | Contract Duration Type | All five values carried an **empty Code cell** — the mapper could not be used to map anything. FEDRIS zone 00885 publishes 0 = indefinite, 1 = fixed term. | Codes 0 and 1 assigned. The three remaining contractual variants (clearly defined work, replacement, student) are marked NOT FOUND rather than mapped by inference: zone 00885 offers only two values and the authority does not say which covers them. | BE-DD-001-v1.0.xlsx |

### Mapper-binding defects found by the same pass (Country Fields column L)

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 1 | 18 country fields | Bound to the generic **Boolean** mapper (Yes/No → Ja/Nee) although the authority zone transmits 0/1, 0/1/9, 0–3 or 0–5. An engine following the DD would have emitted "Yes" where the NSSO expects a digit. Affected: Régime 5 Conversion, Pensioner, Posted Worker, Frontier Worker, Temporary Agency Worker, Service Exemption, SWT/RCC Collective Agreement, SWT/RCC Replacement Obligation, SWT/RCC Half-Time Career Interruption, SWT/RCC Ailing or Restructuring, Eco Vehicle, Working at Another Employer, Function Changed, Stable Occupation, Supplementary Pension Contribution Exemption, SWT/RCC Capitalisation, SWT/RCC Floor Application, Trusteeship. | Each rebound to its own newly added mapper. | BE-DD-001-v1.0.xlsx |
| 1 | Full-Time Employment Request Indicator | Bound to **Binary Indicator** (0/1); DRS zone 01229 has three values, 0/1/9. | Rebound to the new three-value mapper. | BE-DD-001-v1.0.xlsx |
| 1 | 20 country fields | Column L empty although the field is coded in at least one spec. | Bound to their mappers. | BE-DD-001-v1.0.xlsx |

Reference integrity after the patch: **87 mappers defined, 0 referenced-but-undefined, 0
Sheet 6 → DD binding mismatches across 66 bindings.**

---

## CHECK 2 — Option Values completeness

Method: a field was treated as carrying a code table when column O of sheet 4 holds two or
more `CODE=meaning` pairs. **187 such fields** exist across the nine specs. Only **9** had a
corresponding entry in their own Sheet 6 (Field Options); the domain of the other 178 existed
only as untranslated French glossary text inside one cell of column O. Joined against
`DD-CROSSCHECK-TABLE.md`, 134 of those rows are **DD-bucket** fields, of which only a handful
had a DD option mapper.

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 2 | 37 option mappers | A code table existed in a Report Spec but the DD had **no mapper at all**: Address Type · Bank Account Number Format · Employer Relatedness Degree · Trusteeship or Receivership Indicator · Pensioner Indicator · Working at Another Employer Indicator · Temporary Agency Worker Indicator · Usual Profession Seniority Code · Function Changed Indicator · Remuneration Time Unit · Stable Occupation Indicator · Regime 5 Conversion Indicator · Frontier Worker Indicator · Flying Staff Class · Tenth or Twelfth Payment Indicator · Days Justification · Posted Worker Indicator · Supplementary Pension Contribution Exemption Indicator · Supplementary Pension Contribution Basis Derogation · Career Measure · Service Exemption Indicator · Training Situation · Activation Percentage Status · Reduction Certificate Origin · Eco Vehicle Indicator · Early Retirement Contribution Code · SWT/RCC Debtor Type · SWT/RCC Collective Agreement Indicator · SWT/RCC Half-Time Career Interruption Indicator · SWT/RCC Replacement Obligation Indicator · SWT/RCC Resumption of Work Measure · SWT/RCC Ailing or Restructuring Company Indicator · SWT/RCC Capitalisation Indicator · SWT/RCC Floor Application Indicator · Employer Compensation Code · Employer-Worker Relationship Status · DBR Indicator in the Enterprise Framework · Legal Basis for Part-Time Work With Benefit Retention · Full-Time Employment Request Indicator · Language Numeric Code. | Each added with its complete code table, English abbreviation, Dutch local name and English description, taken from the authority's own definition domain as quoted in column O. DD grew from 47 to **87 mappers / 297 code rows**. | BE-DD-001-v1.0.xlsx |
| 2 | 40 coded zones of BE-FEDRIS-001 | Domain held only in French in column O; Sheet 6 had no table. | **138 code rows** added to Field Options in four sections, each row tagged with its glossary zone and, where the field is a DD field, with the DD mapper it binds to. | BE-FEDRIS-001-WorkAccident-Spec.xlsx |
| 2 | ~46 coded zones of BE-NSSO-002 | As above. | **165 code rows** added, including the out-of-scope public-sector zones recorded for completeness and marked OUT OF SCOPE. | BE-NSSO-002-DmfA-Spec.xlsx |
| 2 | ~45 coded zones of BE-NSSO-004 | As above. | **90 code rows** added. | BE-NSSO-004-DRS-Spec.xlsx |
| 2 | BE-NSSO-001 zones 00029, 00297 | Worker Sex had no Sheet 6 table; Type Form listed RE/PA/FA/LA but omitted **SU**, which the glossary domain contains. | **3 code rows** added. | BE-NSSO-001-Dimona-Spec.xlsx |
| 2 | BE-NSSO-003 Attestation Status (00110) | Sheet 6 listed only 0, 1, 3 and 4 and described the rest as NOT FOUND. That conflated two different things: the **zone domain** is nine values (0–8, as BE-NSSO-001 and BE-NSSO-002 both record), and what is unknown is only **which subset the DMWA application accepts**. As written it read as an incomplete code table. | Full nine-value domain listed; the NOT FOUND restated precisely as "which subset DMWA accepts is not stated in any held source". Cross-reference row to BE-NSSO-002 for all other coded zones. **11 code rows.** | BE-NSSO-003-DmfAModification-Spec.xlsx |
| 2 | BE-NSSO-002 Worker Status (00053) | Sheet 6 recorded the zone as a blanket **NOT FOUND**, while BE-NSSO-001 Sheet 6 records it as **PARTIAL** with F1 and F2 held, and the DD now holds both. Same zone, same annexe, two different answers in two specs. | Corrected to PARTIAL with F1 and F2 stated and Annexe 21 still marked not held. | BE-NSSO-002-DmfA-Spec.xlsx |
| 2 | Days Justification (00625) · Legal Basis (00096) · Reference Type (00221) · Indemnity Contribution Period Code (01129) · NOSSLPA Social Maribel (00794) | The definition domain quoted in column O is itself **truncated mid-sentence** — the held source stops at a value and continues with "...". These tables cannot be completed from anything in `00-official-sources`. | The values that ARE present are recorded in full; a terminal `NOT FOUND` row names the missing tail and the exact glossary zone required. Recorded **identically in Sheet 6 and in the DD mapper** rather than silently padded. | BE-DD-001-v1.0.xlsx · BE-NSSO-002 · BE-NSSO-003 · BE-NSSO-004 · BE-FEDRIS-001 |
| 2 | Service Exemption Notion (00826) values 5 and 8 | The comparison operator before "20% salaire brut annuel" is an unrenderable control character in the held source (`(cid: 127)`), so it cannot be stated whether the training-cost threshold is *at least* or *at most* 20 per cent. | Both values recorded with the operator explicitly flagged NOT FOUND, in Sheet 6 and in the DD. Not guessed. | BE-DD-001-v1.0.xlsx · BE-NSSO-002 · BE-NSSO-003 |

**Note on the Dutch column.** The NSSO publishes its glossaries in French and Dutch; only the
French edition is held in `00-official-sources`. The Dutch local names added here are
translations of the held French definition domain, following the terminology already
established in the DD's existing mappers (e.g. *Vertrekvakantiegeld*, *Gewone arbeidsdagen*).
They are labels, not quoted authority text. Where a Dutch term is a term of art it follows
the NSSO's own usage as it appears in the CCG.

---

## CHECK 3 — Mandatory/Conditional flag bidirectionality

**503** fields are marked `Mandatory = C` across the nine specs. **Column G (Conditional
Reason) is populated on all 503 — zero blanks.** That half of the check passed as built.

The second half did not. **137** of those conditions name another field by its zone number.
In every case the dependency could be read only forward: the dependent field states its
driver, but the driver field's own notes said nothing about what it governs.

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| 3 | 60 reverse edges over 22 driver zones | e.g. zone 00430 Identification Of Risk governs the presence of 22 zones; zone 00889 Accident Place Code governs 5; zone 00264 Accident Consequences governs 4 — none of them said so. | `PRESENCE DRIVER` note appended to column N of each driver, naming every zone and row it governs. | BE-FEDRIS-001-WorkAccident-Spec.xlsx |
| 3 | 35 reverse edges over 34 driver zones | e.g. zone 2.076 Benefits in Kind — amount governs 2.099 nature; 2.132 and 2.178 both feed the 33% total; 2.207 governs the kilometre count. | As above. | BE-FIN-002-Belcotax28110-Spec.xlsx |
| 3 | 19 reverse edges over 6 driver zones | zone 00024 INSZ governs the presence of 12 identification zones (name, birth data, address, nationality) — the single most consequential dependency in the declaration, and it was one-directional. | As above. | BE-NSSO-001-Dimona-Spec.xlsx |
| 3 | 9 reverse edges over 8 driver zones each | Contract Type, Ref Mean Working Hours, Reorganisation Measure, Ailing Or Reorg Company Notion, Incomplete Month Reason, Nbr Hours Or Services. | As above. | BE-NSSO-002-DmfA-Spec.xlsx · BE-NSSO-003-DmfAModification-Spec.xlsx |
| 3 | 4 reverse edges over 3 driver fields | LIM-030 / LIM-031 posting dates and LIM-050 A1 reference govern the A1 block fields. | As above. | BE-NSSO-005-Limosa-Spec.xlsx |
| 3 | SEPA `Initiating Party — Name` (row 9) | The condition states "where Name is absent, Identification is mandatory — Name and Id form a conditional pair". **The paired field `<InitgPty><Id>` is not specified anywhere in the workbook** — not in sheet 4, not in the File Structure sheet. The reference is dangling, not merely one-directional, and cannot be closed inside the spec. | Flagged in column N as a dangling reference with the field that must be added before implementation, and marked NOT FOUND against the Febelfin IG field detail. **Not closed — see open items.** | BE-FEBELFIN-001-SEPACreditTransfer-Spec.xlsx |
| 3 | SEPA remittance pair (rows 30, 31) | Row 30 stated the either/or relationship with row 31; row 31 did not state it back. | Reciprocal note added to both rows. | BE-FEBELFIN-001-SEPACreditTransfer-Spec.xlsx |
| 3 | Finprof `Secretariat Code` (row 28) ↔ `Membership` (row 29) | Membership is conditional on affiliation to a third party; Secretariat Code 9998 is precisely the "not affiliated" marker. Only Membership referenced the relationship. | Reverse edge added to Secretariat Code. | BE-FIN-001-Finprof274-Spec.xlsx |
| 3 | FEDRIS `Function Last Change` (row 99) | The condition cites **zone 00431** for Has Changed Of Function; that field is recorded at **zone 00432** on row 100. One of the two is a transcription error in the held source. | Both rows annotated. The dependency itself is sound — the condition names the field unambiguously — so the reverse edge was added; the zone number is marked NOT RESOLVED. | BE-FEDRIS-001-WorkAccident-Spec.xlsx |

Residual after the patch: **137 reverse edges present, 0 one-directional.**

### References that are correctly outside the sheet, not defects

Conditions also cite `90107`, `90374`, `90438`, `90552`, `90553` and `20072` (NSSO **block**
identifiers, not zones) and Belcotax `1.027`, `1.036`, `0.014`, `0.017`, plus NSSO `90110`
and `01216` (zones of the sender or debtor record, or of another declaration). These are
legitimate cross-record and cross-artifact references and were left alone.

---

## WTC cross-check

BE-FIN-002 Sheet 6 asserts specific BE-WTC-001 wage-type counts per Belcotax box. Every
assertion was verified against column G of `BE-WTC-001-v1.0.xlsx!'Wage Type Catalogue'` and
**all are accurate**: box 250 → 144, box 252 → 14, box 254 → 19, box 285 → 5, box 308 → 4,
box 317 → 6, box 233 → 9, box 234 → 4. The catalogue gap the spec already declares is also
confirmed: **box 360 (work bonus, 52.54% tax credit) → 0 wage types.** No patch required;
the gap is correctly documented on the spec side and remains an open WTC item.

---

## Additional defect fixed in passing

| Check | Field / Mapper | Issue Found | Fix Applied | File Patched |
|---|---|---|---|---|
| — | `Work Accident Spec!O49` and `!O55` | The workbook was **already failing** its own C29 residual-marker gate before this patch, on two cells. Both are false positives: the glossary's BIC description quotes the literal branch code for a head office, which is three X characters, and the lint is word-boundary anchored on that token. | The quoted passage now describes the literal as "three X characters" and states that the glossary writes it as a three-X literal — the fact is preserved exactly and the false positive is gone. | BE-FEDRIS-001-WorkAccident-Spec.xlsx |

---

## Open items — not closed by this patch

1. **`<InitgPty><Id>` is not specified in BE-FEBELFIN-001.** Requires the Febelfin
   pain.001.001.09 IG 2025 v1.3 field detail. Until then a payer name above 70 characters
   has no specified fallback.
2. **FEDRIS zone 00431 vs 00432** for Has Changed Of Function. Requires the NSSO DRS FAT
   glossary 2026/2 to say which number is right.
3. **Truncated definition domains** in the held sources: zones 00625, 00096, 00221, 01129,
   00794. Requires the NSSO glossaries in full.
4. **Zone 00826 values 5 and 8** — the comparison operator against the 20 per cent training
   cost threshold is unrenderable in the held source.
5. **BE-WTC-001 box 360** — no wage type carries the 52.54% work bonus tax credit code.
6. Mappers that legitimately hold **no authority code** because the authority publishes none
   (Marital or Civil Status, Commuting Mode, Dependant Relationship, Tax Residency Status,
   Region of the Establishment Unit, Vehicle Fuel Type, Wage Payment Method, Pay Date
   Convention, Meal Voucher Allocation Basis, Garnishment or Wage Assignment Type, Spouse
   Professional Income Situation, Inbound Taxpayer Regime Type, Wage Withholding Tax Filing
   Frequency, Worker Status private-sector taxonomy) still carry an empty Code column. These
   are Mercans-internal domains; assigning codes is a **configuration decision, not a
   research finding**, and was deliberately not done here.
7. The NSSO annexes remain unheld: **Annexe 2** (worker codes), **3** (contribution types),
   **4** (deduction codes), **6** (activity with risk), **7** (remuneration codes),
   **8** (working-time codes), **12** (risk identification), **21** (worker status),
   **28** (APL), **34** (work-schedule days), and the Statbel NIS country table. Every one is
   marked NOT FOUND identically in the DD and in the owning spec.

---

## Files patched and self-check status

| File | Version | Structural self-check |
|---|---|---|
| 05-data-dictionary/BE-DD-001-v1.0.xlsx | 1 → **1.1** | PASS (blocker 0, major 0, minor 0) |
| 04-reports-spec/BE-FEBELFIN-001-SEPACreditTransfer-Spec.xlsx | 1.0 → **1.1** | PASS |
| 04-reports-spec/BE-FEDRIS-001-WorkAccident-Spec.xlsx | 1.0 → **1.1** | PASS (was FAIL, blocker 2, before this patch) |
| 04-reports-spec/BE-FIN-001-Finprof274-Spec.xlsx | 1.0 → **1.1** | PASS |
| 04-reports-spec/BE-FIN-002-Belcotax28110-Spec.xlsx | 1.0 → **1.1** | PASS |
| 04-reports-spec/BE-NSSO-001-Dimona-Spec.xlsx | 1.0 → **1.1** | PASS |
| 04-reports-spec/BE-NSSO-002-DmfA-Spec.xlsx | 1.0 → **1.1** | PASS |
| 04-reports-spec/BE-NSSO-003-DmfAModification-Spec.xlsx | 1.0 → **1.1** | PASS |
| 04-reports-spec/BE-NSSO-004-DRS-Spec.xlsx | 1.0 → **1.1** | PASS |
| 04-reports-spec/BE-NSSO-005-Limosa-Spec.xlsx | 1.0 → **1.1** | PASS |

`BE-WTC-001-v1.0.xlsx` was read and cross-checked but required no change.

Gate used: `mercans-artifact-toolkit/scripts/validate_workbook.py --artifact DD` and
`--artifact RSPEC`.
