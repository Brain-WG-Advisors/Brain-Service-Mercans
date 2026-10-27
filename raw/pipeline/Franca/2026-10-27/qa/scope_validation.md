# FR — SCOPE LOCK-IN VALIDATION

**Gate:** Stage 0 scope lock-in — BLOCKING. No downstream stage may start until this gate passes.
**Artifact validated:** `FR-compliance/scope_manifest.json` — 62,284 bytes, mtime 2026-08-27 17:48, **scope_version 1.1**
**Schema:** `shared/scope_manifest_template.json`
**Validated on:** 2026-09-01
**Validator profile:** v2.8 — B7 decision rows and B1 non-resident rule enabled
**Scope owner of record:** Wallisson Gomes, lock date 26 August 2026; v1.1 amendment 27 August 2026

**Supersedes:** the validation of 27 August 2026 11:11, preserved at `scope_validation.md.bak-20260901-105500`.
That run validated **scope_version 1.0**. The manifest was amended to v1.1 at 17:48 the same day —
after the previous gate ran — so the prior PASS no longer covers the file on disk. See
*Supersession and carried-forward findings* below for what changed and what did not.

---

## VERDICT

**PASS** — all six checks satisfied against scope_version 1.1. **No B1 blocking finding.**

Five non-blocking findings are recorded: two carried forward **still open** from the previous
gate (C-01, C-02) and three raised here (W1–W3).

| Check | Subject | Result |
|---|---|:--|
| 1 | File exists, valid JSON | **PASS** |
| 2 | All required sections present and non-empty | **PASS** — 14/14 paths |
| 3 | `authority_filings.in_scope` field completeness and enums | **PASS** — 15/15 |
| 4 | `integrations.inbound` → `product_mapping_required` set | **PASS** — 8/8 set, all `true`, no F8 WARN |
| 5 | No code in both `in_scope` and `out_of_scope` for the same mapper | **PASS** — 0 collisions |
| 6 | `known_failure_patterns_to_check` populated F1–F15 | **PASS** — F1–F22 present |
| B1 | Non-resident handling for every covered income type | **PASS** — no blocking finding |

---

## SUPERSESSION AND CARRIED-FORWARD FINDINGS

The v1.1 amendment is recorded in `scope_manifest_changelog` and was verified here rather than
taken on trust. What it did:

| Change | Verified |
|---|---|
| Added `spec_file`, `spec_link_basis`, `sir_authority`, `sir_runbook` to all 15 in-scope filings | **Confirmed** — 15/15 carry all four, none blank |
| Seeded `known_limitations`, previously null, with three open items | **Confirmed** — FR-LIM-001/002/003, each with `raised_by`, `consumers`, `what_would_close_it` |
| Added one `authority_filings.out_of_scope` row (12 → 13) | **Confirmed** — the new row is `FR-DGFIP-006` |

The changelog's own account of why is corroborated: before v1.1, **0 of 15** filings declared a
spec link, C18 could not resolve coverage mechanically and C20 reported FAIL. The links were read
from each spec's own Document ID cell and gated on an exact 1:1 bijection rather than inferred from
filenames. Independently re-verified at this gate: **15/15 `spec_file` paths resolve on disk**.

Two findings from the previous gate were **not** closed by the amendment, and both are re-confirmed
against the live file:

### C-01 (was W-01) — STILL OPEN — the L137-13 / L137-14 contributions have no scope row

`grep` for `L137-13` and `L137-14` across `scope_manifest.json` returns **0 hits**. The 30% employer
contribution still exists only as a subordinate clause inside the *out-of-scope* free-shares row:
*"Only the 30% employer contribution (and, above EUR 300,000, the 10% employee contribution) touch
the DSN."*

The CCG is unambiguous that this is a live payroll obligation. `m11_advanced.md` line 150: the
employer specific contribution is *"**30%**, raised from 20% with effect for shares acquired from
1 March 2025, under Social Security Code Article L137-13 … **payable in the month following the
acquisition or the grant, and declared in the DSN**."* Line 161 records the 10% employee
contribution above EUR 300,000 under L137-14. `m04_compensation.md` line 216 carries the same rule.

So a DSN-declared obligation with an employer/employee split exists with no in-scope wage type to
attach it to. That is the F3 shape exactly, and under B7 it is an unrecorded scope decision.
**Severity: WARN** — it does not fail any of the six checks and does not bite B1 (a contribution is
not a covered income type lacking non-resident handling).
**Action:** before the WTC stage, promote both contributions to explicit
`wage_type_categories.in_scope` rows — declaration-only, outside the ordinary contribution bands —
while leaving the *gain* descoped. An addition, not a reversal.

### C-02 (was W-02) — STILL OPEN — CGI Article 182 A ter is instructed but never scoped

`grep` for `182 A ter` across `scope_manifest.json` returns **0 hits**. The CCG issues an explicit
instruction that the manifest never closes — `m06_tax.md` §6.0, equity row, non-resident column:
*"The acquisition gain from French-source awards is subject to a **specific withholding under
General Tax Code Article 182 A ter**, operated by the entity making the award … This is not the
ordinary payroll withholding and **must be modelled separately**."*

Note for the record: the previous gate recommended closing this with a new out-of-scope row under
the suggested id **FR-DGFIP-006**. That id was subsequently consumed by the v1.1 amendment for a
**different** descoping — PASRAU — so the reserved id is no longer available and the 182 A ter
instruction remains unaddressed. Any fix must allocate a fresh id.

**B1 does not bite here:** 182 A ter attaches to free-share and share-option gains, which are a
*descoped* income type, so this is not missing non-resident handling for a *covered* type. The
covered types are handled — see the B1 section.
**Severity: WARN.**
**Action:** add one `authority_filings.out_of_scope` row under a new id, descoping 182 A ter as
attaching to a descoped income type and operated by the awarding entity rather than by payroll.

The previous gate's W-03 (FR-CPAM-002 and FR-CDC-001 carrying `product_mapping_required=false`) is
re-confirmed as **correctly decided** — both are outbound, so neither is an F8 exposure. It is
retained as an observation, not a finding.

---

## CHECK 1 — FILE EXISTS AND IS VALID JSON

`scope_manifest.json` exists and parses cleanly under `json.load` (UTF-8). Header block fully
populated, no placeholder or empty-string values surviving from the template:

| Field | Value |
|---|---|
| country / country_code / code | France / FR / FR |
| currency | EUR |
| year | 2026 |
| scope_version | 1.1 |
| scope_decided_by / scope_decided_on | Wallisson Gomes / 2026-08-26 |
| generated | 2026-08-26T16:40:00+02:00 |
| source_artifact | FR-CCG-001-v1.0.docx |
| mandate_document | FR-compliance/00-official-sources/ccg-sources/FR-CCG-source-register.md |

A superseded revision is retained on disk as `scope_manifest.json.bak-20260827-084033` (47,965
bytes). The live file is the later and larger one; the two are not in conflict, and the changelog
documents the 1.0 → 1.1 delta.

**Result: PASS.**

---

## CHECK 2 — REQUIRED SECTIONS PRESENT AND NON-EMPTY

Every required section is present, correctly shaped, and non-empty. No section is `null`, an empty
string, an empty list or an empty dict.

| Path | Status | Size |
|---|:--:|--:|
| employment_types.in_scope | OK | 12 |
| employment_types.out_of_scope | OK | 13 |
| employment_types.rationale | OK | 1,063 chars |
| authority_filings.in_scope | OK | 15 |
| authority_filings.out_of_scope | OK | 13 |
| wage_type_categories | OK | 3 keys |
| wage_type_categories.in_scope | OK | 35 |
| wage_type_categories.out_of_scope | OK | 7 |
| wage_type_categories.special_rules | OK | 16 |
| option_mapper_scope | OK | 9 mappers + `_comment` |
| integrations.outbound | OK | 12 |
| integrations.inbound | OK | 8 |
| integrations.both | OK | 1 |
| known_failure_patterns_to_check | OK | 22 |

`option_mapper_scope` carries the five template mappers (`personal_id_type`, `insurance_type`,
`contract_type`, `correction_codes`, `benefit_type`) plus four France-specific additions
(`working_time_type`, `withholding_rate_type`, `residence_status`, `leave_type`) — 51 codes in
total once the one explanatory `Note:` entry is excluded.

The manifest is a **superset** of the template. Beyond the schema it adds `code`, `generated`,
`source_artifact`, `mandate_document`, per-filing `rationale` / `spec_file` / `spec_link_basis` /
`sir_authority` / `sir_runbook`, per-descoping `client_impact`, and the three blocks
`failure_pattern_notes`, `scope_manifest_changelog` and `known_limitations`. Nothing the template
requires is absent.

**Result: PASS.**

---

## CHECK 3 — authority_filings.in_scope FIELD COMPLETENESS

All 15 in-scope filings carry `filing_id`, `authority`, `frequency`, `format`, `integration_type`
and `product_mapping_required`. `integration_type` is within `{inbound, outbound, both}` in every
case. `product_mapping_required` is a JSON boolean in every case — never `null`, never a string.

| # | filing_id | authority (head) | frequency | format | integration_type | pmr |
|---|---|---|---|---|:--:|:--:|
| 1 | FR-DSN-001 | URSSAF (and, through the same flow, the other bodies) | monthly | TXT | outbound | true |
| 2 | FR-DSN-002 | France Travail, via net-entreprises.fr | per event | TXT | outbound | true |
| 3 | FR-DSN-003 | CPAM, via net-entreprises.fr | per event | TXT | outbound | true |
| 4 | FR-URSSAF-001 | URSSAF, via net-entreprises.fr | per hire | XML | outbound | true |
| 5 | FR-DGFIP-001 | Direction Générale des Finances Publiques | monthly | TXT | **both** | true |
| 6 | FR-DGFIP-002 | DGFiP | monthly, quarterly | TXT | **inbound** | true |
| 7 | FR-CARSAT-001 | CARSAT | annual, and on change | XML | **inbound** | true |
| 8 | FR-URSSAF-002 | URSSAF, via net-entreprises.fr | monthly | TXT | **inbound** | true |
| 9 | FR-URSSAF-003 | URSSAF, on behalf of Agefiph | annual | TXT | outbound | true |
| 10 | FR-URSSAF-004 | URSSAF | annual | TXT | outbound | true |
| 11 | FR-DGFIP-003 | DGFiP | monthly, quarterly | XML | outbound | true |
| 12 | FR-CPAM-002 | CPAM, via net-entreprises.fr | per event | XML | outbound | **false** |
| 13 | FR-CDC-001 | Caisse des Dépôts, SOLTeA | annual | XLSX | outbound | **false** |
| 14 | FR-CPAM-003 | CPAM | per event | TXT | **inbound** | true |
| 15 | FR-AGIRC-001 | AGIRC-ARRCO institutions | monthly | TXT | **inbound** | true |

The two `product_mapping_required=false` entries are both **outbound**, so neither is an F8
exposure — F8 concerns inbound files wrongly excluded from product mapping.

**Supplementary integrity checks — not required by the gate, run anyway:**

| Test | Result |
|---|---|
| v1.1 audit fields (`spec_file`, `spec_link_basis`, `sir_authority`, `sir_runbook`) present | 15/15, none blank |
| `spec_file` paths resolve on disk | **15/15 exist** under `04-reports-spec/` |
| Filings missing from `integrations` | **none** |
| `integrations` IDs not in filings | 6, all correctly non-authority: FR-BANK-001, FR-CLIENT-001, FR-CLIENT-002, FR-COURT-001, FR-GL-001, FR-PAYSLIP-001 |
| `integration_type` on filing vs. its bucket in `integrations` | **0 mismatches** |
| `product_mapping_required` on filing vs. `integrations` | **0 mismatches** |
| Out-of-scope filings with a non-empty `descoping_reason` | 13/13 (133–573 chars) |
| Out-of-scope filings with a `client_impact` | 13/13 |

**Result: PASS.**

---

## CHECK 4 — INBOUND INTEGRATIONS AND product_mapping_required (F8)

| Bucket | Entries | pmr set | =true | =false |
|---|--:|--:|--:|--:|
| inbound | 8 | 8/8 | 8 | 0 |
| both | 1 | 1/1 | 1 | 0 |

All eight inbound integrations — FR-DGFIP-002, FR-URSSAF-002, FR-CARSAT-001, FR-CPAM-003,
FR-AGIRC-001, FR-CLIENT-001, FR-CLIENT-002, FR-COURT-001 — and the one `both` integration,
FR-DGFIP-001, declare `product_mapping_required=true`, each with a `from`/`with`, `format`,
`frequency` and a substantive `note`.

**No F8 WARN is raised.** The manifest carries the anti-F8 guard verbatim in `integrations._note`:
*"Inbound files where HRB must parse/act = product_mapping_required=true. Never default
inbound=not-in-scope."*

Three inbound notes define hard data contracts and are surfaced here for the downstream stages:

- **FR-DGFIP-002** — the withholding rate, its type and its validity period, described as *"the ONLY
  lawful source of an employee's rate — the employer never collects a tax number."* Correctly forces
  the rate to be received, never derived.
- **FR-CLIENT-002** — year-to-date counters on provider migration, with the note that a provider
  change does not change the employer, so every cumulative mechanism (capped and uncapped bases,
  ceiling proration) continues across the cut-over.
- **FR-CARSAT-001** — the establishment-specific AT/MP net rate and risk code, stored per SIRET.

Outbound entries do not carry `product_mapping_required` — see **W2**. Check 4 governs inbound only.

**Result: PASS, no WARN.**

---

## CHECK 5 — IN-SCOPE / OUT-OF-SCOPE COLLISION

Tested on every section that maintains both lists. `option_mapper_scope` is in-scope-only by
template design — each mapper lists the codes that ARE in scope — so it cannot self-collide; it was
instead tested against the out-of-scope lists of the other sections.

| Section | in_scope | out_of_scope | Exact collisions |
|---|--:|--:|:--:|
| employment_types | 12 | 13 | **0** |
| authority_filings | 15 | 13 | **0** |
| wage_type_categories | 35 | 7 | **0** |

Two head-token near-matches were surfaced by the collision heuristic; both cleared as false
positives on inspection:

- *"Employee and employer contributions to the compulsory health cover…"* (in) vs. *"Employee
  payments into a company savings plan or collective retirement savings plan"* (out) — different
  instruments. The second is a saving, not a contribution, and the manifest says so in the row.
- *"Holiday bonus (prime de vacances)"* (in) vs. *"Holiday pay in the construction, public works and
  entertainment sectors"* (out) — a bonus paid by the employer vs. holiday pay paid by a sector fund
  (CIBTP). Distinct payers, distinct instruments.

Two genuine **cross-section** boundary candidates were then examined in full, because that is the
shape which leaks codes downstream (F2). Both are explicitly reconciled by the manifest itself:

1. **Overseas departments.** `withholding_rate_type` carries the territorial default grids
   (Guadeloupe, Martinique, La Réunion; Guyane, Mayotte) as in scope, while
   `employment_types.out_of_scope` descopes the overseas departments. Not a contradiction: the
   descoping reason states that the territorial withholding grids and the reduced non-resident rates
   (8% and 14.4%) *are* documented in the CCG and that only the **LODEOM exemption arithmetic** is
   unmodelled. `employment_types.rationale` draws the same line independently: *"Two territorial
   layers are IN scope because they modify the régime général rather than replace it … What is out
   of scope in the overseas departments is only the LODEOM exemption arithmetic."* The boundary is
   drawn on the same axis in both places.
2. **A1 posted workers.** `residence_status` carries *"Posted worker holding a portable document A1
   for another state — no French contributions"* as an in-scope classification value, while
   `employment_types.out_of_scope` descopes workers posted into France under a foreign contract.
   Reconciled: the descoping reason is that the foreign employer pays them and there is no French
   payslip, whereas the mapper value is the flag needed to *recognise and exclude* such a person.
   CCG `m11_advanced.md` treats this expressly as a third category. Recorded as **W3** so that a
   downstream builder cannot misread the mapper value as a modelled population.

**Result: PASS.**

---

## CHECK 6 — known_failure_patterns_to_check

Populated with 22 entries, `F1` through `F22`, contiguous. F1–F15 are all present, none missing;
F16–F22 are additional beyond the required floor.

`failure_pattern_notes` gives France-specific substance for F18–F22, and it is of real operational
value rather than boilerplate:

- **F18 — stale law.** Names eight superseded parameter families that may not appear in any France
  artifact: the pre-2026 Fillon coefficients (0.3193 / 0.3233 at 1.6 SMIC), the separate 7% reduced
  employer sickness rate capped at 2.25 SMIC, the separate 3.45% reduced family-allowance rate
  capped at 3.5 SMIC — all three replaced by the single degressive general reduction from
  1 January 2026 — the 2025 default withholding grids, **the 2025 non-resident scale**, the 30% (now
  40%) mutually-agreed-termination contribution, the 1.8 SMIC (now 1.4) sickness daily-allowance cap,
  and capital social levies at 17.2% (now 18.6%).
- **F19 — HR-scope reports.** Flags the professional equality index as the highest-risk descoping
  because it looks like a pay report but needs promotion rates, pay-rise rates and the sex of the ten
  highest earners, which payroll does not hold.
- **F20 — WTC tax codes** must come from France's own legend — the DSN remuneration, bonus/indemnity,
  contribution-base and individual contribution codes of NEODeS CT2026.1.2 — not from a neighbouring
  country's catalogue.
- **F21 — filing mechanics**, marked VERIFIED, NOT ASSUMED (C4): France **consolidates**. Social
  contributions and withheld income tax are declared inside one monthly DSN and collected by direct
  debit initiated from it; there is no separate income tax return for payroll. Deadlines follow
  **headcount, not pay frequency** — DSN and contributions on the 5th (50+ employees) or the 15th,
  the withholding remittance on the 8th or the 18th. The sub-11-employee quarterly option changes the
  payment rhythm only; the DSN remains monthly. The disabled-worker return and the apprenticeship tax
  balance are discharged **inside the April DSN**, not as separate filings.

**Result: PASS**, with **W1** on the presentation of F1–F17.

---

## B1 — NON-RESIDENT HANDLING ACROSS COVERED INCOME TYPES

Non-resident employees working in France and affiliated to the French scheme are an **in-scope
employment type**, so B1 applies. Tested at scope level and then against the downstream artifacts,
because a scope manifest declares the population and mechanism while the per-income-type treatment
lives in the CCG.

**Present in the manifest:**

| Element | Location | Content |
|---|---|---|
| Population | `employment_types.in_scope` | Non-resident employees working in France and affiliated to the French scheme, withheld under General Tax Code Article 182 A |
| Withholding mechanism | `option_mapper_scope.withholding_rate_type` | *Retenue à la source non-resident* — Article 182 A, 0/12/20 bands, or 0/8/14.4 for overseas-source income |
| Residence classification | `option_mapper_scope.residence_status` | Tax resident (Art. 4 B, as modified by treaty), non-resident, French-scheme affiliation, A1 posted worker — plus an explicit note that tax residence and social security affiliation are **independent tests decided by independent criteria** |
| Parameter currency | `failure_pattern_notes.F18` | The 2025 non-resident scale is named as superseded and barred from every artifact |
| Boundary — Art. 182 B | `authority_filings.out_of_scope` FR-DGFIP-004 | The 25% withholding on sums paid to a non-resident for services rendered in France is an accounts-payable obligation on self-employed providers, not an employer withholding on remuneration |
| Boundary — Art. 197 A | `authority_filings.out_of_scope` FR-DGFIP-005 | The 20%/30% minimum assessment rate (14.4%/20% overseas) is assessment-level. `client_impact` states it must **NOT** be modelled in the engine, the WTC or the DD, and records that an assessment-level levy was wrongly propagated into withholding artifacts on an earlier country |

**Present downstream, per income type.** CCG `m06_tax.md` opens with **§6.0 "Resident and
Non-Resident Treatment Matrix"** — a two-column matrix, resident PAS against non-resident Article
182 A, with a row for:

| Income type | Non-resident treatment stated |
|---|---|
| Regular salary | Article 182 A scale, applied to the base after the 10% deduction |
| Severance and termination payments | The exempt fraction stays outside; the taxable excess enters the 182 A base |
| Equity and share incentives | Specific withholding under Article 182 A ter, operated by the awarding entity — *see C-02, the manifest never closes this instruction* |
| Contractor / labour-service pay | Not in payroll scope; Article 182 B, accounts payable |
| Benefits in kind | Included in the Article 182 A base at the same statutory values, after the 10% deduction |

followed by the additional non-resident rules: the overseas 8% / 14.4% rates, the assessment-level
minimum rate held expressly apart from withholding, and the separation of tax residence from social
security liability. The module further carries the per-period 182 A scale for 2026 (annual,
quarterly, monthly, weekly, daily), a resident/non-resident comparison across rate source and DSN
reporting, the **libératoire** character of the 12% band, and a worked non-resident example
(Example 2, June 2026). `m09_termination.md` and `m02_master_data.md` carry further non-resident
treatment.

The two **residence-conditional** in-scope income types were checked specifically, since they are
where a non-resident population and a covered income type could silently contradict each other:

- **Impatriation premium, Article 155 B** (`wage_type_categories.in_scope[29]`) — `m11_advanced.md`
  states the qualifying condition explicitly: employees *"who **were not French tax resident in the
  five calendar years preceding** the year they take up duties"*, with the duration, the flat-30%
  versus real-amount election, the 50% / 20% cap election, and the exclusion of self-employed
  workers and majority-shareholding managers.
- **Expatriation supplements, Article 81 A** (`wage_type_categories.in_scope[30]`) — covered in
  `m11_advanced.md` as the outbound-assignee relief, with the day-count and foreign-tax tests, the
  40% partial exemption, and the effective-rate rule under Article 197 C.

The same passage reconciles the third category — inbound workers under a foreign contract holding an
A1 — with the manifest's descoping of that population.

Every income type the manifest covers therefore carries a stated non-resident treatment, either
directly in §6.0 or through the residence condition attached to the regime.

**Result: PASS — no B1 blocking finding.**

---

## NON-BLOCKING FINDINGS RAISED AT THIS GATE

### W1 — `known_failure_patterns_to_check` entries are bare tokens

**Location:** `scope_manifest.json` → `known_failure_patterns_to_check`
**Severity:** WARN — does not affect Check 6, which requires F1–F15 to be populated; they are.

The list holds `"F1"`, `"F2"` … `"F22"` with no descriptive text, where the template pairs each code
with its meaning (`"F1 - Option mapper alignment DD<->Specs"`). F18–F22 are described in
`failure_pattern_notes`, but **F1–F17 have no text anywhere in the file**. This manifest is the
contract every downstream agent reads; a bare `"F9"` obliges the reader to resolve the code against
an external failure log that may drift.

**Action:** restore the `"Fn - description"` form for F1–F17.

### W2 — `product_mapping_required` is asymmetric between sections

**Location:** `integrations.outbound` (12 entries) vs. `authority_filings.in_scope`
**Severity:** WARN — advisory.

All 15 `authority_filings.in_scope` entries declare `product_mapping_required`, but within
`integrations` only the 8 inbound and 1 `both` entries do; the 12 outbound entries omit the key.
Check 4 governs inbound only, and the two representations agree wherever both exist (0 mismatches),
so nothing is contradictory. It does mean a consumer reading `integrations.outbound` in isolation
gets no mapping signal at all.

**Action:** populate the key on outbound entries, or state in `integrations._note` that it is
deliberately inbound-only.

### W3 — A1 posted-worker value sits in an in-scope mapper while the population is descoped

**Location:** `option_mapper_scope.residence_status` vs. `employment_types.out_of_scope`
**Severity:** ADVISORY — correct as designed, recorded to prevent later reinterpretation.

The code must exist for the engine to recognise and suppress the population, and CCG
`m11_advanced.md` treats the category expressly. But the mapper itself carries no note saying so, so
an artifact-builder reading `option_mapper_scope` alone could construct pay logic behind the value —
the F2 shape.

**Action:** annotate the value as a classification and exclusion flag, not a modelled population, so
the DD and Report Spec stages implement it as routing only and never as a payslip-producing
population.

---

## OBSERVATIONS — NO ACTION REQUIRED

- **The manifest is a superset of the template.** Nothing required is absent; the additions
  (`rationale`, `spec_file`, `spec_link_basis`, `sir_authority`, `sir_runbook`, `client_impact`,
  `failure_pattern_notes`, `scope_manifest_changelog`, `known_limitations`) all add auditability.
- **Every descoping is reasoned twice.** All 13 out-of-scope filings and all 13 out-of-scope
  employment types carry both a `descoping_reason` and a `client_impact` naming who picks the item
  up — HRMS team, finance, fleet, corporate secretariat, the client's accountant, the mobility
  function, or a sector fund.
- **Three open items are registered** in `known_limitations`, each with `raised_by`, `consumers` and
  `what_would_close_it`: FR-LIM-001 (199 spec rows marked payroll master data with no DD
  counterpart, of which employee e-mail address looks like a genuine omission), FR-LIM-002 (CARSAT
  notification layout, Position/Length recorded as **NOT OBTAINED** rather than invented — correct
  under C4), FR-LIM-003 (SOLTeA employer guide is an image-only PDF; text extraction failed, and
  CDC-SOLTeA is portal-only so no runbook depends on it).
- **`wage_type_categories.special_rules` (16 entries) is the strongest part of the manifest.** It
  records the three-way separation of contribution / social-levy / income-tax liability, the five
  distinct bases, the three net figures that must appear on every payslip, the **two simultaneously
  live 2026 minimum-wage parameters** (EUR 12.02 to 31 May and EUR 12.31 from 1 June for live pay,
  against EUR 12.02 frozen all year inside the general reduction per Décret n° 2026-509), the **two
  coexisting 2026 withholding grids** keyed to date of payment, the general-reduction **cliff** at
  Tmin = 0.0200, the 10-PASS (EUR 480,600) termination cliff tested before any other exemption, the
  no-salary-sacrifice principle, negative gross as a DSN regularisation rather than a pay line, IDCC
  as a first-class configuration key, and the value-sharing bonus enhanced regime expiring
  31 December 2026.
- **One out-of-scope wage type is a negative assertion:** *"Student loan repayments — NO SUCH
  DEDUCTION EXISTS IN FRANCE. Recorded explicitly so that a requirement referring to one is raised as
  an error rather than configured."* Recorded as irreversible in the register below — reversing it
  would introduce an obligation that does not exist in French law.

---

## B7 — SCOPE DECISION REGISTER

Every scope decision in the manifest, one row each. **152 rows: 119 in-scope, 33 out-of-scope.**

**Column definitions**

- **IN-SCOPE** — Y if the item sits in a `*.in_scope` list or an in-scope mapper list; N if descoped.
- **OWNED-UPSTREAM** — Y where the subject matter is owned outside this payroll build (the client's
  HRMS, finance, fleet or corporate secretariat, the mobility function, an authority, a sector fund,
  a scheme administrator, or the outgoing provider), so the build consumes or refers rather than
  produces.
- **INBOUND-DATA-CONTRACT** — Y where the decision creates or depends on an inbound file or feed the
  build must parse and act on.
- **REVERSIBLE** — Y where the decision can be revisited later additively, without invalidating
  delivered artifacts. N where reversal forces a rebuild of delivered content, or — for the negative
  assertions FR-DGFIP-004, FR-DGFIP-005 and student loan repayments — where reversal would model
  something that must not be modelled.
- **BASIS** — the manifest path and the recorded reason.

| # | GROUP | DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE | BASIS |
|---|---|---|:--:|:--:|:--:|:--:|---|
| 1 | Employment type | Permanent contract (contrat a duree indeterminee, CDI) | Y | N | N | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 2 | Employment type | Fixed-term contract (contrat a duree determinee, CDD), including the 10% end-of-contract indemnity | Y | N | N | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 3 | Employment type | Part-time employees, including the prorated social security ceiling and additional hours (heures complementaires) | Y | N | N | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 4 | Employment type | Managerial grade (cadre) and non-managerial employees | Y | N | N | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 5 | Employment type | Employees on an annual day-count arrangement (forfait annuel en jours) | Y | N | N | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 6 | Employment type | Apprenticeship contracts (contrat d'apprentissage) | Y | N | N | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 7 | Employment type | Professionalisation contracts (contrat de professionnalisation) | Y | N | N | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 8 | Employment type | Interns (stagiaires) receiving a statutory gratuity, exempt to 15% of the hourly ceiling per hour of attendance | Y | N | N | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 9 | Employment type | Temporary-agency workers (interimaires), where the client is the agency and therefore the employer | Y | Y | N | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 10 | Employment type | Company officers treated as employees (assimiles salaries): chair or managing director of a SAS or SA, minority or equal-shareholding manager of a SAR... | Y | N | N | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 11 | Employment type | Employees whose place of work is in Alsace-Moselle (Bas-Rhin, Haut-Rhin, Moselle): the general scheme plus the 1.30% local employee health contributio... | Y | N | Y | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 12 | Employment type | Non-resident employees working in France and affiliated to the French scheme, withheld under General Tax Code Article 182 A | Y | N | Y | N | employment_types.in_scope; regime general private-sector lock, rationale para 1 |
| 13 | Employment type | RATP scheme (Paris transport) | N | Y | N | Y | employment_types.out_of_scope: Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. Rates and mechanics deliberately not researched. |
| 14 | Employment type | ENIM scheme (maritime and seafarers) | N | Y | N | Y | employment_types.out_of_scope: Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| 15 | Employment type | CNBF scheme (lawyers) | N | Y | N | Y | employment_types.out_of_scope: Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| 16 | Employment type | CRPCEN scheme (notarial staff) | N | Y | N | Y | employment_types.out_of_scope: Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| 17 | Employment type | CAVIMAC scheme (clergy) | N | Y | N | Y | employment_types.out_of_scope: Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| 18 | Employment type | CNIEG and CAMIEG schemes (gas and electricity sector) | N | Y | N | Y | employment_types.out_of_scope: Regime special outside the regime general. Descoped before Stage 1 by the scope owner, 26 August 2026. |
| 19 | Employment type | Any other sector-specific caisse outside the regime general | N | N | N | Y | employment_types.out_of_scope: Catch-all for the regimes speciaux. Acknowledged as existing in the CCG; rates and mechanics deliberately not researched, per the locked scope decision of 26 August 2026. |
| 20 | Employment type | Agricultural employees under the MSA scheme (regime agricole) | N | Y | N | Y | employment_types.out_of_scope: A separate collection network (Mutualite Sociale Agricole) with its own DSN channel, its own contribution set and its own paid-leave arrangements. Outside the URSSAF regime general to which this buil... |
| 21 | Employment type | Majority-shareholding managers of a SARL, and other self-employed workers (travailleurs non salaries) | N | Y | N | Y | employment_types.out_of_scope: Self-employed under the SSI scheme. Contributions are assessed and paid personally, outside payroll entirely. Not an employment type the engine can process. |
| 22 | Employment type | Public-sector statutory staff (fonctionnaires) and their pension schemes | N | Y | N | Y | employment_types.out_of_scope: Outside the private-sector regime general to which this build is scoped. |
| 23 | Employment type | Workers posted into France who remain affiliated to a foreign scheme under a portable document A1 | N | Y | N | Y | employment_types.out_of_scope: No French social security contributions are due and the foreign employer pays the worker. There is no French payslip to produce. The posting declaration (SIPSI) is an administrative obligation of the... |
| 24 | Employment type | Mayotte | N | N | N | Y | employment_types.out_of_scope: A distinct social security scheme with its own contribution set and its own minimum wage (EUR 9.56 an hour from 1 June 2026 against EUR 12.31 nationally). Documented in the CCG for awareness; not mod... |
| 25 | Employment type | Overseas departments - the LODEOM specific exemption schemes (Guadeloupe, Martinique, Guyane, La Reunion) | N | N | N | Y | employment_types.out_of_scope: The general degressive reduction is replaced by the overseas exemption schemes, which are more generous and structured differently. Their existence, the reduced non-resident withholding rates (8% and... |
| 26 | Authority filing | FR-DSN-001 - URSSAF (and, through the same file, CNAV, CPAM, AGIRC-ARRCO,... (monthly, TXT, outbound) | Y | N | N | N | authority_filings.in_scope; spec=FR-DSN-001-DSNMensuelle-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 27 | Authority filing | FR-DSN-002 - France Travail, via net-entreprises.fr (per event, TXT, outbound) | Y | N | N | N | authority_filings.in_scope; spec=FR-DSN-002-FinContratUnique-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 28 | Authority filing | FR-DSN-003 - Caisse Primaire d'Assurance Maladie (CPAM), via net-entrepri... (per event, TXT, outbound) | Y | N | N | N | authority_filings.in_scope; spec=FR-DSN-003-ArretTravailReprise-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 29 | Authority filing | FR-URSSAF-001 - URSSAF, via net-entreprises.fr (per hire, XML, outbound) | Y | N | N | N | authority_filings.in_scope; spec=FR-URSSAF-001-DPAE-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 30 | Authority filing | FR-DGFIP-001 - Direction Generale des Finances Publiques (DGFiP) (monthly, TXT, both) | Y | Y | Y | N | authority_filings.in_scope; spec=FR-DGFIP-001-PrelevementSource-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 31 | Authority filing | FR-DGFIP-002 - DGFiP (monthly, TXT, inbound) | Y | Y | Y | N | authority_filings.in_scope; spec=FR-DGFIP-002-CompteRenduPAS-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 32 | Authority filing | FR-CARSAT-001 - Caisse d'Assurance Retraite et de la Sante au Travail (CARSA... (annual, XML, inbound) | Y | Y | Y | N | authority_filings.in_scope; spec=FR-CARSAT-001-NotificationTauxATMP-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 33 | Authority filing | FR-URSSAF-002 - URSSAF, via net-entreprises.fr (monthly, TXT, inbound) | Y | Y | Y | N | authority_filings.in_scope; spec=FR-URSSAF-002-CompteRenduMetier-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 34 | Authority filing | FR-URSSAF-003 - URSSAF, on behalf of Agefiph (annual, TXT, outbound) | Y | N | N | N | authority_filings.in_scope; spec=FR-URSSAF-003-DOETH-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 35 | Authority filing | FR-URSSAF-004 - URSSAF (annual, TXT, outbound) | Y | N | N | N | authority_filings.in_scope; spec=FR-URSSAF-004-SoldeTaxeApprentissage-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 36 | Authority filing | FR-DGFIP-003 - DGFiP (monthly, XML, outbound) | Y | N | N | N | authority_filings.in_scope; spec=FR-DGFIP-003-TaxeSurLesSalaires-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 37 | Authority filing | FR-CPAM-002 - CPAM, via net-entreprises.fr (per event, XML, outbound) | Y | N | N | N | authority_filings.in_scope; spec=FR-CPAM-002-AccidentTravail-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 38 | Authority filing | FR-CDC-001 - Caisse des Depots, SOLTeA platform (annual, XLSX, outbound) | Y | N | N | N | authority_filings.in_scope; spec=FR-CDC-001-SOLTeA-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 39 | Authority filing | FR-CPAM-003 - Caisse Primaire d'Assurance Maladie (CPAM) (per event, TXT, inbound) | Y | Y | Y | N | authority_filings.in_scope; spec=FR-CPAM-003-BPIJ-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 40 | Authority filing | FR-AGIRC-001 - AGIRC-ARRCO institutions, via the DSN return flow (monthly, TXT, inbound) | Y | Y | Y | N | authority_filings.in_scope; spec=FR-AGIRC-001-RetourAgircArrco-Spec.xlsx; link basis=Verified at the pre-submission audit gate, 27 Aug 2026: the named work... |
| 41 | Authority filing | FR-HR-001 - Ministry of Labour, Egapro platform | N | Y | N | Y | authority_filings.out_of_scope: HR-scope - requires data beyond payroll system. The professional equality index (Index de l'egalite professionnelle femmes-hommes), due annually by 1 March from employers with 50 or more employees, ... |
| 42 | Authority filing | FR-HR-002 - Works council (comite social et economique) | N | Y | N | Y | authority_filings.out_of_scope: HR-scope - requires data beyond payroll system. The social report (bilan social), due from employers with 300 or more employees, requires recruitment, training, health-and-safety, industrial-relatio... |
| 43 | Authority filing | FR-HR-003 - Works council | N | Y | N | Y | authority_filings.out_of_scope: HR-scope - requires data beyond payroll system. The economic, social and environmental database (BDESE) requires investment, environmental and governance data. |
| 44 | Authority filing | FR-HR-004 - DARES, Ministry of Labour statistical service | N | Y | N | Y | authority_filings.out_of_scope: HR-scope - requires data beyond payroll system. The ACEMO survey of labour activity and employment conditions is a sampled statistical survey requiring vacancy and working-conditions data. |
| 45 | Authority filing | FR-HR-005 - Ministry of Labour | N | Y | N | Y | authority_filings.out_of_scope: HR-scope - requires data beyond payroll system. The gender-balance obligation for senior executives and governing bodies, applying to employers above 1,000 employees with a 30% target from 1 March 2... |
| 46 | Authority filing | FR-FIN-001 - DGFiP | N | Y | N | Y | authority_filings.out_of_scope: Not a payroll filing. The taxes on the use of vehicles for economic purposes (which replaced the former taxe sur les vehicules de societe) are assessed on the fleet - emissions, age and use - not on... |
| 47 | Authority filing | FR-FIN-002 - DGFiP | N | Y | N | Y | authority_filings.out_of_scope: Not a payroll filing. The construction investment obligation (participation des employeurs a l'effort de construction) for employers of 50 or more is discharged by direct investment, with a levy on ... |
| 48 | Authority filing | FR-MSA-001 - Mutualite Sociale Agricole | N | N | N | Y | authority_filings.out_of_scope: Outside the regime general. The agricultural scheme has its own collection network, its own DSN channel and its own contribution set. |
| 49 | Authority filing | FR-CIBTP-001 - Sector paid-leave funds (caisses de conges payes) in constru... | N | N | N | Y | authority_filings.out_of_scope: Sector-specific flow not built for the baseline France build. In these sectors the FUND pays the employee's holiday pay and the employer pays a contribution to the fund, so the employer shows no hol... |
| 50 | Authority filing | FR-DGFIP-004 - DGFiP | N | Y | N | N | authority_filings.out_of_scope: Not a payroll obligation. The withholding under General Tax Code Article 182 B, at 25% on sums paid to a non-resident for services rendered or used in France, is an accounts-payable obligation on pa... |
| 51 | Authority filing | FR-DGFIP-005 - DGFiP | N | N | N | Y | authority_filings.out_of_scope: Assessment-level, not withholding-level. The minimum assessment rate for non-residents under General Tax Code Article 197 A (20% up to EUR 29,579 of French net taxable income and 30% above; 14.4% an... |
| 52 | Authority filing | FR-URSSAF-005 - URSSAF | N | Y | N | Y | authority_filings.out_of_scope: Out of the employment-type scope. Contributions for company officers who are self-employed (majority-shareholding SARL managers and other travailleurs non salaries) are assessed and paid personally ... |
| 53 | Authority filing | FR-DGFIP-006 -  | N | Y | N | Y | authority_filings.out_of_scope: Not an employer payroll filing for the regime general. PASRAU (NEORAU norm, technical specification CT2026.1.1 for 2026) is the withholding-at-source declaration for income OTHER than wages and sala... |
| 54 | Wage type | Base salary for the contractual working time (salaire de base), smoothed at 151.67 hours for a full-time 35-hour week | Y | N | N | N | wage_type_categories.in_scope |
| 55 | Wage type | Overtime, base and premium (25% for the first eight hours beyond 35 in the week, 50% thereafter, floor of 10% by agreement) | Y | N | N | N | wage_type_categories.in_scope |
| 56 | Wage type | Additional hours for part-time employees (heures complementaires), 10% within the first tenth and 25% beyond | Y | N | N | N | wage_type_categories.in_scope |
| 57 | Wage type | Days worked beyond an annual day-count arrangement, premiumed at at least 10% | Y | N | N | N | wage_type_categories.in_scope |
| 58 | Wage type | Seniority bonus (prime d'anciennete) | Y | N | N | N | wage_type_categories.in_scope |
| 59 | Wage type | Thirteenth month (13eme mois) | Y | N | N | N | wage_type_categories.in_scope |
| 60 | Wage type | Holiday bonus (prime de vacances) | Y | N | N | N | wage_type_categories.in_scope |
| 61 | Wage type | Performance and objectives bonus | Y | N | N | N | wage_type_categories.in_scope |
| 62 | Wage type | Commission, including a contractual guaranteed minimum against commission | Y | N | N | N | wage_type_categories.in_scope |
| 63 | Wage type | On-call, shift, Sunday and night premiums | Y | N | N | N | wage_type_categories.in_scope |
| 64 | Wage type | Paid annual leave pay, computed as the higher of the one-tenth rule and the salary maintenance rule | Y | N | N | N | wage_type_categories.in_scope |
| 65 | Wage type | Public holiday pay, including the 100% premium for work on 1 May | Y | N | N | N | wage_type_categories.in_scope |
| 66 | Wage type | Working-time reduction days (jours de RTT) and their monetisation | Y | N | N | N | wage_type_categories.in_scope |
| 67 | Wage type | Employer top-up on sickness (90% for 30 days, 66.66% for the next 30, after one year's service and a seven-day waiting period) | Y | N | N | N | wage_type_categories.in_scope |
| 68 | Wage type | Daily social security benefits transiting the payslip where the employer is subrogated | Y | Y | Y | N | wage_type_categories.in_scope |
| 69 | Wage type | Partial activity (activite partielle) allowance | Y | Y | Y | N | wage_type_categories.in_scope |
| 70 | Wage type | Benefits in kind: company vehicle, accommodation, meals (EUR 5.50 per meal for 2026), communication tools | Y | N | N | N | wage_type_categories.in_scope |
| 71 | Wage type | Meal vouchers, employer share exempt to EUR 7.32 per voucher at 50% to 60% of face value | Y | N | N | N | wage_type_categories.in_scope |
| 72 | Wage type | 50% reimbursement of the public transport season ticket (compulsory) | Y | N | N | N | wage_type_categories.in_scope |
| 73 | Wage type | Sustainable mobility allowance | Y | N | N | N | wage_type_categories.in_scope |
| 74 | Wage type | Professional expense reimbursements, within and above the statutory limits | Y | N | N | N | wage_type_categories.in_scope |
| 75 | Wage type | Value-sharing bonus (prime de partage de la valeur), standard and enhanced regimes | Y | N | N | N | wage_type_categories.in_scope |
| 76 | Wage type | Compensatory notice indemnity (ordinary pay) | Y | N | N | N | wage_type_categories.in_scope |
| 77 | Wage type | Compensatory leave indemnity (ordinary pay) | Y | N | N | N | wage_type_categories.in_scope |
| 78 | Wage type | Fixed-term end-of-contract indemnity, 10% or 6% (ordinary pay) | Y | N | N | N | wage_type_categories.in_scope |
| 79 | Wage type | Non-compete indemnity (ordinary pay) | Y | N | N | N | wage_type_categories.in_scope |
| 80 | Wage type | Statutory and collectively agreed redundancy payments, with the three-layer exemption | Y | N | N | N | wage_type_categories.in_scope |
| 81 | Wage type | Mutually agreed termination and compulsory retirement indemnities, with the 40% employer contribution | Y | N | N | N | wage_type_categories.in_scope |
| 82 | Wage type | Voluntary retirement indemnity (fully contributable and taxable outside a collective redundancy plan) | Y | N | N | N | wage_type_categories.in_scope |
| 83 | Wage type | Impatriation premium under General Tax Code Article 155 B, real amount or 30% flat | Y | N | N | N | wage_type_categories.in_scope |
| 84 | Wage type | Expatriation supplements exempt within 40% under General Tax Code Article 81 A | Y | N | N | N | wage_type_categories.in_scope |
| 85 | Wage type | Employee and employer contributions to the compulsory health cover, death-and-disability cover and supplementary pension schemes | Y | N | N | N | wage_type_categories.in_scope |
| 86 | Wage type | Advance on the current month (acompte) as a netting line, NOT a separate pay run | Y | N | N | N | wage_type_categories.in_scope |
| 87 | Wage type | Advance in the strict sense (avance), recoverable at one tenth of pay per period | Y | N | N | N | wage_type_categories.in_scope |
| 88 | Wage type | Wage attachments, maintenance orders paid by direct payment, and tax levy notices | Y | Y | Y | N | wage_type_categories.in_scope |
| 89 | Wage type | Attendance fees (jetons de presence) paid to non-executive directors - taxed as investment income at 12.8% plus capital social levies of 18.6%, with a... | N | N | N | Y | wage_type_categories.out_of_scope: Attendance fees (jetons de presence) paid to non-executive directors - taxed as investment income at 12.8% plus capital social levies of 18.6%, with a 20% flat social contribution owed by the com... |
| 90 | Wage type | Free share acquisition gains and share option exercise gains - taxable in the year of DISPOSAL, outside withholding at source and outside the ordinary... | N | N | N | Y | wage_type_categories.out_of_scope: Free share acquisition gains and share option exercise gains - taxable in the year of DISPOSAL, outside withholding at source and outside the ordinary contribution bands. Only the 30% employer co... |
| 91 | Wage type | Profit-sharing and incentive-scheme amounts (participation, interessement) once invested - outside gross pay, with their own regime and their own sche... | N | Y | N | Y | wage_type_categories.out_of_scope: Profit-sharing and incentive-scheme amounts (participation, interessement) once invested - outside gross pay, with their own regime and their own scheme administrator |
| 92 | Wage type | Employee payments into a company savings plan or collective retirement savings plan - a saving, not a contribution | N | Y | N | Y | wage_type_categories.out_of_scope: Employee payments into a company savings plan or collective retirement savings plan - a saving, not a contribution |
| 93 | Wage type | Self-employed contractor invoices - not remuneration, no employer withholding | N | Y | N | Y | wage_type_categories.out_of_scope: Self-employed contractor invoices - not remuneration, no employer withholding |
| 94 | Wage type | Holiday pay in the construction, public works and entertainment sectors - paid by the sector fund, not by the employer | N | Y | N | Y | wage_type_categories.out_of_scope: Holiday pay in the construction, public works and entertainment sectors - paid by the sector fund, not by the employer |
| 95 | Wage type | Student loan repayments - NO SUCH DEDUCTION EXISTS IN FRANCE. Recorded explicitly so that a requirement referring to one is raised as an error rather ... | N | N | N | N | wage_type_categories.out_of_scope: Student loan repayments - NO SUCH DEDUCTION EXISTS IN FRANCE. Recorded explicitly so that a requirement referring to one is raised as an error rather than configured |
| 96 | Option mapper: personal_id_type | NIR - numero d'inscription au repertoire, 15 characters (13 digits + 2-digit key); key = 97 minus (the 13-digit number modulo 97); Corsican department... | Y | N | N | N | option_mapper_scope.personal_id_type (in-scope code list; no out_of_scope list for this mapper) |
| 97 | Option mapper: personal_id_type | NTT - numero technique temporaire, up to 40 characters, conventionally the SIRET plus an internal sequence; used only until the NIR is issued and must... | Y | N | N | N | option_mapper_scope.personal_id_type (in-scope code list; no out_of_scope list for this mapper) |
| 98 | Option mapper: insurance_type | Regime general - URSSAF, CNAM, CNAV | Y | N | N | N | option_mapper_scope.insurance_type (in-scope code list; no out_of_scope list for this mapper) |
| 99 | Option mapper: insurance_type | Regime general plus the Alsace-Moselle local health scheme (additional 1.30% employee contribution, triggered by the place of work) | Y | N | N | N | option_mapper_scope.insurance_type (in-scope code list; no out_of_scope list for this mapper) |
| 100 | Option mapper: insurance_type | AGIRC-ARRCO supplementary pension (bands 1 and 2) | Y | N | N | N | option_mapper_scope.insurance_type (in-scope code list; no out_of_scope list for this mapper) |
| 101 | Option mapper: insurance_type | Compulsory supplementary health cover (complementaire sante), employer share at least 50% | Y | N | N | N | option_mapper_scope.insurance_type (in-scope code list; no out_of_scope list for this mapper) |
| 102 | Option mapper: insurance_type | Managerial-grade death-and-disability cover, 1.50% of the capped band, wholly employer-paid | Y | N | N | N | option_mapper_scope.insurance_type (in-scope code list; no out_of_scope list for this mapper) |
| 103 | Option mapper: insurance_type | Optional death-and-disability and supplementary pension schemes, collective and compulsory | Y | N | N | N | option_mapper_scope.insurance_type (in-scope code list; no out_of_scope list for this mapper) |
| 104 | Option mapper: contract_type | CDI - permanent contract | Y | N | N | N | option_mapper_scope.contract_type (in-scope code list; no out_of_scope list for this mapper) |
| 105 | Option mapper: contract_type | CDD - fixed-term contract | Y | N | N | N | option_mapper_scope.contract_type (in-scope code list; no out_of_scope list for this mapper) |
| 106 | Option mapper: contract_type | Apprenticeship contract | Y | N | N | N | option_mapper_scope.contract_type (in-scope code list; no out_of_scope list for this mapper) |
| 107 | Option mapper: contract_type | Professionalisation contract | Y | N | N | N | option_mapper_scope.contract_type (in-scope code list; no out_of_scope list for this mapper) |
| 108 | Option mapper: contract_type | Temporary-agency assignment | Y | N | N | N | option_mapper_scope.contract_type (in-scope code list; no out_of_scope list for this mapper) |
| 109 | Option mapper: contract_type | Internship agreement (convention de stage) - gratuity, not a wage | Y | N | N | N | option_mapper_scope.contract_type (in-scope code list; no out_of_scope list for this mapper) |
| 110 | Option mapper: working_time_type | Full-time 35-hour week, 151.67 hours a month | Y | N | N | N | option_mapper_scope.working_time_type (in-scope code list; no out_of_scope list for this mapper) |
| 111 | Option mapper: working_time_type | Part-time, with the social security ceiling prorated on the hours ratio | Y | N | N | N | option_mapper_scope.working_time_type (in-scope code list; no out_of_scope list for this mapper) |
| 112 | Option mapper: working_time_type | Annual day-count arrangement (forfait annuel en jours), typically 218 days - no overtime | Y | N | N | N | option_mapper_scope.working_time_type (in-scope code list; no out_of_scope list for this mapper) |
| 113 | Option mapper: withholding_rate_type | Taux personnalise - personal rate transmitted by the tax administration | Y | Y | Y | N | option_mapper_scope.withholding_rate_type (in-scope code list; no out_of_scope list for this mapper) |
| 114 | Option mapper: withholding_rate_type | Taux individualise - individualised rate within a couple | Y | N | N | N | option_mapper_scope.withholding_rate_type (in-scope code list; no out_of_scope list for this mapper) |
| 115 | Option mapper: withholding_rate_type | Taux non personnalise - the statutory default grid, by territory (metropolitan; Guadeloupe, Martinique and La Reunion; Guyane and Mayotte) and by peri... | Y | N | N | N | option_mapper_scope.withholding_rate_type (in-scope code list; no out_of_scope list for this mapper) |
| 116 | Option mapper: withholding_rate_type | Retenue a la source non-resident - General Tax Code Article 182 A, 0/12/20 bands, or 0/8/14.4 for overseas-source income | Y | N | N | N | option_mapper_scope.withholding_rate_type (in-scope code list; no out_of_scope list for this mapper) |
| 117 | Option mapper: correction_codes | Cancel-and-replace declaration for a month whose deadline has not passed | Y | N | N | N | option_mapper_scope.correction_codes (in-scope code list; no out_of_scope list for this mapper) |
| 118 | Option mapper: correction_codes | Contribution regularisation carried in the contribution-base block with the start and end dates of the period of attachment | Y | N | N | N | option_mapper_scope.correction_codes (in-scope code list; no out_of_scope list for this mapper) |
| 119 | Option mapper: correction_codes | Withholding regularisation carried in the dedicated block, dated to the month of the original error | Y | N | N | N | option_mapper_scope.correction_codes (in-scope code list; no out_of_scope list for this mapper) |
| 120 | Option mapper: correction_codes | Amending or cancelling event signal | Y | N | N | N | option_mapper_scope.correction_codes (in-scope code list; no out_of_scope list for this mapper) |
| 121 | Option mapper: benefit_type | Company vehicle | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 122 | Option mapper: benefit_type | Accommodation | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 123 | Option mapper: benefit_type | Meals | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 124 | Option mapper: benefit_type | Communication tools | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 125 | Option mapper: benefit_type | Meal vouchers | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 126 | Option mapper: benefit_type | Public transport season ticket reimbursement | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 127 | Option mapper: benefit_type | Sustainable mobility allowance | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 128 | Option mapper: benefit_type | Compulsory health cover | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 129 | Option mapper: benefit_type | Death-and-disability cover | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 130 | Option mapper: benefit_type | Supplementary pension scheme | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 131 | Option mapper: benefit_type | Company savings plan and collective retirement savings plan employer contributions | Y | N | N | N | option_mapper_scope.benefit_type (in-scope code list; no out_of_scope list for this mapper) |
| 132 | Option mapper: residence_status | Tax resident (domicilie fiscalement en France) under General Tax Code Article 4 B, as modified by any applicable treaty | Y | N | N | N | option_mapper_scope.residence_status (in-scope code list; no out_of_scope list for this mapper) |
| 133 | Option mapper: residence_status | Non-resident | Y | N | N | N | option_mapper_scope.residence_status (in-scope code list; no out_of_scope list for this mapper) |
| 134 | Option mapper: residence_status | Affiliated to the French social security scheme | Y | N | N | N | option_mapper_scope.residence_status (in-scope code list; no out_of_scope list for this mapper) |
| 135 | Option mapper: residence_status | Posted worker holding a portable document A1 for another state - no French contributions | Y | Y | N | N | option_mapper_scope.residence_status (in-scope code list; no out_of_scope list for this mapper) |
| 136 | Option mapper: leave_type | Paid annual leave (conges payes), in working days (jours ouvrables, 30 a year) or worked days (jours ouvres, 25 a year) - the two units must NEVER be ... | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 137 | Option mapper: leave_type | Working-time reduction days (jours de RTT) | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 138 | Option mapper: leave_type | Seniority leave (conges d'anciennete) | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 139 | Option mapper: leave_type | Maternity, paternity and child-welcome, adoption, birth leave | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 140 | Option mapper: leave_type | Supplementary birth leave (new from 1 July 2026, up to 2 months per parent at 70% then 60% of net pay) | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 141 | Option mapper: leave_type | Sick leave, non-occupational | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 142 | Option mapper: leave_type | Work accident and occupational disease leave | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 143 | Option mapper: leave_type | Family event leave, and bereavement leave for a child | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 144 | Option mapper: leave_type | Parental education leave, carer's leave, parental presence leave | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 145 | Option mapper: leave_type | Unpaid leave by agreement (conge sans solde) - no statutory framework, agreed in writing case by case | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 146 | Option mapper: leave_type | Time savings account (compte epargne-temps) | Y | N | N | N | option_mapper_scope.leave_type (in-scope code list; no out_of_scope list for this mapper) |
| 147 | Integration (non-authority) | FR-BANK-001 - The employee's bank (outbound, XML) | Y | N | N | N | integrations.outbound; product_mapping_required=n/a (outbound) |
| 148 | Integration (non-authority) | FR-PAYSLIP-001 - The employee, and the electronic archiving service (outbound, PDF) | Y | N | N | N | integrations.outbound; product_mapping_required=n/a (outbound) |
| 149 | Integration (non-authority) | FR-GL-001 - The client's general ledger (outbound, CSV) | Y | N | N | N | integrations.outbound; product_mapping_required=n/a (outbound) |
| 150 | Integration (non-authority) | FR-CLIENT-001 - The client's HRMS (inbound, CSV) | Y | Y | Y | N | integrations.inbound; product_mapping_required=True |
| 151 | Integration (non-authority) | FR-CLIENT-002 - The outgoing payroll provider, on migration (inbound, XLSX) | Y | Y | Y | N | integrations.inbound; product_mapping_required=True |
| 152 | Integration (non-authority) | FR-COURT-001 - Court enforcement officers (commissaires de justice) an... (inbound, PDF) | Y | Y | Y | N | integrations.inbound; product_mapping_required=True |
