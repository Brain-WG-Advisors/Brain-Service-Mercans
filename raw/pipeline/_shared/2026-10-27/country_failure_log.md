# Country Failure Log — Mercans Compliance Research Pipeline

This log records every distinct failure pattern observed during real country builds,
the root cause, and the mitigation. Read this before starting any new country build.
Every check in `presubmission_audit_local.py` and every prompt instruction maps back
to one or more entries here.

**Version:** v2.12  |  **Updated:** 17 Oct 2026  |  **Source countries:** BG, HU, CL, ES, EG, FR, BE

---

## F1 — Option mapper mismatch (DD ↔ Specs)

**Source:** Bulgaria first build (April 2026)
**Observed:** DD `Option Mappers` sheet listed codes 1, 2, 3 for `EmploymentType`,
but Spec workbook for Declaration 1 had codes 1, 2, 3, 4, 5 — codes 4 and 5 leaked
in from an out-of-scope form.
**Root cause:** No cross-validation between DD option mapper rows and Spec field
constraints. The agent populated each independently.
**Mitigation:** Check C2 (Option Mapper Cross-Validation). For every code in a Spec
field, must exist in the corresponding DD option mapper, and vice versa. Audit-
correct loop re-runs the DD or Spec agent to reconcile.

---

## F2 — Out-of-scope codes leaked

**Source:** Bulgaria Declaration 6
**Observed:** Spec included contribution codes for self-employed persons even
though scope was "employer-paid contributions only."
**Root cause:** Source PDF was multi-purpose; agent didn't filter by scope.
**Mitigation:** Check C4 (Scope Manifest Compliance). Every code/field in every
Spec must be traceable to a scope_manifest.json entry. Codes outside scope flagged
for removal.

---

## F3 — Field classification errors

**Source:** Bulgaria CCG
**Observed:** "Health insurance premium" classified as `Earnings` when it's actually
a `Pre-tax deduction` per Bulgarian tax law.
**Root cause:** Agent inferred from English-language sources without checking
the legal classification in the local source.
**Mitigation:** Check C5 (Field Classification Audit). Every classification in CCG
Module 4-7 must cite the specific article of law that establishes the classification.

---

## F4 — Wrong file format

**Source:** Bulgaria Declaration 6 spec
**Observed:** Spec described XML output format; actual NRA system uses fixed-width
text format.
**Root cause:** Agent confused with Declaration 1 (XML); didn't verify D6 format
against source PDF.
**Mitigation:** Check C6 (File Format Verification). Every Spec must include a
"File Format" header field, and the value must match the format documented in
the source PDF cited in scope_manifest.

---

## F5 — Population Rules thin

**Source:** Bulgaria, all Specs initially
**Observed:** Population Rules sheet had 1-2 lines per field instead of the
conditional logic required for pipeline configuration.
**Root cause:** Agent thought "Population Rules" meant "what populates this field"
not "the conditional logic that decides if/how this field is populated."
**Mitigation:** Check C7 (Population Rules Depth). Every conditional field
(Mandatory=C) must have a Population Rules entry of at least 3 lines describing
the condition, the populated value, and the alternative.

---

## F6 — Open queries unanswered

**Source:** Bulgaria handover
**Observed:** CCG had "TBD" or "to be confirmed" in multiple places that the dev
team had to chase down later.
**Root cause:** Agent flagged uncertainty but never returned to resolve it.
**Mitigation:** Check C8 (Open Items Resolution). No "TBD", "to be confirmed",
"to be verified" markers may remain in any artifact at handover.

---

## F7 — WTC wage type tax codes wrong

**Source:** Spain SR-80 ticket review
**Observed:** WTC for Spain had wrong AEAT tax keys (L vs A) for some flex
remuneration benefits.
**Root cause:** Agent applied general "benefit in kind" treatment without checking
the Spain-specific dual-regime (IRPF-exempt but SS-subject) rules.
**Mitigation:** Check C9 (WTC Tax Code Verification). Every wage type tax code
must be verified against the country's specific tax authority publication, not
generic guidance.

---

## F8 — Inbound integration scoped out incorrectly

**Source:** Spain SR-80 (inbound CRA integration)
**Observed:** SIR scoped out the inbound CRA codes integration thinking it was
product-side; it's actually pipeline-side.
**Root cause:** Inbound vs outbound classification error.
**Mitigation:** Check C10 (SIR Inbound/Outbound Audit). Every integration in
SIR must be classified `inbound` or `outbound`, and `product_mapping_required`
set explicitly with rationale.

---

## F9 — Thin spec column schema (v2.4 NEW)

**Source:** HU-GAP-001 § 3.2 (Hungary, Manju Shetija, May 2026)
**Observed:** Initial Hungary 2608M spec built with 6 columns (Field Name EN/HU,
Row No., Column, Description, Notes) instead of the 21 columns required by NAV
validation architecture. Missing: ÉAZON Code, Mandatory flag, Conditional Reason,
XML Path, Field Length, Data Type, Example, System Mapping, Field Explanation,
Payroll Relevant, Code Table, Rounding, Negative Allowed, Value Type F/T,
Frequency, HK Error Code, HK Error Message.
**Root cause:** Spec template defined a minimal schema; agent didn't probe the
actual reporting authority's validation depth.
**Mitigation:** Check C12 (Spec Column Schema Depth). Every Spec workbook's
Field Specification sheet must populate at least 18 of the 21 standard columns.
For countries where the local tax/SS authority requires fewer columns, the
absent columns must be explicitly justified in the Spec's `Notes & Decisions`
sheet.

---

## F10 — Missing sub-forms (v2.4 NEW)

**Source:** HU-GAP-001 § 3.1 (Hungary 2608M)
**Observed:** Form 2608M built without sub-forms M-09, M-09-01, M-09-02, M-10,
M-11, M-12, leaving 6 entire reporting sections uncovered. Pipeline could not
generate kieső időszak, Szocho deduction relief, or EFO simplified employment
reporting.
**Root cause:** Source PDFs described sub-forms in Hungarian; agent missed them
when scanning for "sub-form" in English. No cross-check against CCG-mentioned
report sections.
**Mitigation:** Check C11 (CCG Template Coverage) AND Check C18 (Declaration
Form Scope Coverage). Every form mentioned in CCG Module 10.1 (Statutory
Reporting) must have a complete Spec including all sub-forms. The audit-correct
loop reads CCG section-by-section and verifies Spec coverage matches.

---

## F11 — Display-only rows treated as XML input (v2.4 NEW)

**Source:** HU-GAP-001 G-04 (Hungary 2608M-12 EFO calendar rows 25311-25341)
**Observed:** ÁNYK form displays calendar days as visual rows for user reference,
but these are NOT XML input fields — only the AA/BA/CA/DA/EA/FA/GA/QA columns
under the relationship are XML input. Pipeline would have submitted invalid XML.
**Root cause:** Source PDF showed rows visually; agent classified all visible
rows as data input fields.
**Mitigation:** Check C15 (Field Input/Output Classification). Every Spec field
must carry an explicit classification: `Input` (employer-provided), `Output`
(system-calculated), `Display-only` (visible in form but not in XML), or
`Calculated` (derived from other Input fields). No unclassified fields permitted
at handover.

---

## F12 — Composite key construction undocumented (v2.4 NEW)

**Source:** HU-GAP-001 G-02 (Hungary alkalmazás minősége 14-char composite key)
**Observed:** 2608M-08 uses a 14-character composite key (positions 1-2 = pension
code; 3-5 = employment type code; 6-11 = relationship start YYMMDD; 12-14 =
sequence number 001-999) that must be IDENTICAL across all companion sub-forms
M-08 through M-12 for the same employment relationship. The construction rule
was nowhere in the spec.
**Root cause:** Composite key was implicit in the source PDF examples; agent
captured field value but not construction logic.
**Mitigation:** Check C13 (Composite Key Documentation). When a Spec field's
length > 8 characters and contains structural sub-fields (date, code, sequence),
the Spec must include a "Composite Key Structure" note documenting each sub-
field's position, length, source, and persistence rule.

---

## F13 — Mutual exclusion rules undocumented (v2.4 NEW)

**Source:** HU-GAP-001 G-05 (Hungary M-11 ↔ M-07 rows 385-386)
**Observed:** When M-11 (Szocho deductions code 17-26) is populated for an
employee, M-07 rows 385-386 must be blank for that same employee — they're
mutually exclusive. This was undocumented in either row's notes.
**Root cause:** Inter-field constraints exist across sub-forms; agent processed
each sub-form independently.
**Mitigation:** Check C16 (Inter-field Constraint Documentation). Every Spec
field marked `Mandatory = C` (conditional) must have a Population Rules entry
referencing the other field(s) in the constraint, with bidirectional
documentation (both sides reference each other).

---

## F14 — Code prefix inconsistency with official source (v2.4 NEW)

**Source:** HU-GAP-001 G-21 (Hungary 2608M eazon prefixes)
**Observed:** Initial spec used wrong eazon prefixes (M-04=0C instead of 0B,
M-05=0D instead of 0C, etc.). Pipeline XML element naming would have failed
NAV validation.
**Root cause:** Agent inferred prefix pattern from a few examples; didn't verify
against full eazon list in source.
**Mitigation:** Check C19 (Code Prefix Verification). For every field with a
coded identifier (eazon, CRA, DT, DJ, etc.), the Spec must include a regex
pattern in the field's `Format` column, and the audit cross-checks every code
in the spec against the prefix pattern in the source PDF cited in
scope_manifest.

---

## F15 — Removed artifact without descoping decision (v2.4 NEW)

**Source:** HU-GAP-001 G-16, G-20, G-28, G-29 (Hungary 2608INT, T201INT,
Payslip Spec, 2601 Company Car Tax, KSH OSAP 2204 — five artifacts present
in old pipeline, absent from new with no decision recorded)
**Observed:** Five forms were dropped between pipeline versions with no audit
trail. Pipeline scope drifted silently. Some clients require these forms
(company car tax for fleet clients; KSH for ≥5 employee clients) — silent
removal = silent broken compliance.
**Root cause:** No mandatory descoping decision record at scope_manifest level.
**Mitigation:** Check C20 (Scope Decision Audit Trail). Every form/report
listed as in-scope in CCG must either have a Spec file OR have an explicit
descoping decision in scope_manifest.json with the form name, reason for
descoping, and the client-impact assessment. Audit-correct loop adds the
decision record if found missing.

---

## F16 — Stage 3 silent failure under default token limit (v2.5 NEW)

**Source:** Egypt T1 (Manju Shetija, 27 May 2026)
**Observed:** Stage 3 (Report Specs) produced 8 report specs with 9 sheets
each. Output exceeded Claude CLI's default 32,000 output token limit. The
stage appeared to complete but several spec sheets were truncated or
missing rows. Failure was silent — no error in the log, just incomplete
specs.
**Root cause:** Default CLAUDE_CODE_MAX_OUTPUT_TOKENS=32000 is insufficient
for the cumulative output of Stage 3 (multiple xlsx files, many rows each).
**Mitigation:** v2.5 sets CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 inline for
Stage 3 and Stage 5 only (scoped per stage, not globally). The recommended
run command in the script header includes the inline export. Global export
would cause F17 (see below).

---

## F17 — Global token override bloats Stage 1 input (v2.5 NEW)

**Source:** Egypt T2 (Manju Shetija, 27 May 2026)
**Observed:** When CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 was exported
globally before nohup, Stage 1 (CCG) became more aggressive about reading
input files. Combined with the 32MB Claude CLI input limit, Stage 1 began
failing on countries with many source PDFs.
**Root cause:** A larger output token budget signals to the CLI that
input ingestion can also expand; the side effect was unintended and hard
to diagnose because the variable was set far from the failing stage.
**Mitigation:** Set CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000 inline only on the
stages that need it (Stage 3 and Stage 5). Do NOT export it globally.

---

## F18 — Stale law references in CCG (v2.5 NEW)

**Source:** Egypt C2 (Manju Shetija, 27 May 2026)
**Observed:** CCG Module 13 used 90-day maternity leave from Labour Law
12/2003 and a 2-occasions sick-leave limit, instead of the correct values
under Law 14/2025 (4 months maternity, 3 occasions). Annual leave Year 1
structure was also missing. The agent picked up stale references from
older online sources and didn't cross-check against the current law.
**Root cause:** No instruction in the CCG prompt to prioritise the
newest applicable law and explicitly flag superseded references.
**Mitigation:** v2.5 CCG prompt instructs the agent to (1) identify the
current labour code / income tax law / SS law in force, (2) use the
newest as primary source, (3) explicitly flag any reference to a
superseded law. Search pattern added: "${COUNTRY} new labour code ${YEAR}".

---

## F19 — HR-scope report included in payroll handover (v2.5 NEW)

**Source:** Egypt C1 (Manju Shetija, 27 May 2026)
**Observed:** The Annual Workforce Report (Ministry of Labour, Art. 36
Labour Law 14/2025) was included as in-scope in the Egypt pipeline run.
The report requires headcount by qualification, occupation, nationality,
and gender — fields the payroll system does not capture. It cannot be
produced by the payroll engine alone.
**Root cause:** No scope filter to distinguish HR-scope reports from
payroll-scope reports.
**Mitigation:** v2.5 Stage 3 prompt includes an HR-scope descope rule:
any filing requiring headcount-by-qualification, workforce census,
talent/training plans, equal-opportunity data, or where >50% of fields
come from HRMS rather than payroll is descoped from the dev handover
with documented reason ("HR-scope — refer to HRMS team") and
\`product_mapping_required: false\`.

---

## F20 — WTC gaps and invalid tax codes (v2.5 NEW)

**Source:** Egypt C3 (Manju Shetija, 27 May 2026)
**Observed:** Three issues in the Egypt WTC:
- Commission wage type missing entirely from the catalogue
- Employer Life Insurance Premium had tax code EG-TX-3, which is not in
  the defined Egypt tax code legend (EG-TX-1 through EG-TX-7 are defined)
- 20 Expat Allowance rows had ambiguous SubjNOSI = 'Yes-No' without any
  explanation note
**Root cause:** No post-generation validation step to catch missing
wage types, invalid tax codes, or ambiguous taxability flags.
**Mitigation:** v2.5 Stage 5 WTC prompt includes a post-generation
validation checklist (Python snippet) that:
1. Confirms every wage type category from scope_manifest is present in
   the WTC output
2. Validates every tax code against the country's defined tax code
   legend (no codes from other countries' legends)
3. Requires an explanation cell for any 'Yes-No' on core taxability
   columns (Subject to Tax, Subject to SS, Subject to Pension)

---

## F21 — Filing mechanics misunderstood: monthly/quarterly/annual (v2.5 NEW)

**Source:** Egypt C4 (Manju Shetija, 27 May 2026)
**Observed:** Both EG-TAX-ANNUAL-004 and EG-TAX-QUARTERLY-003 are
mandatory SEPARATE employer filings, not auto-generated from monthly
submissions. The initial pipeline output treated them as derived from
the monthly filing, which would have led the dev team to skip building
two of the three required filing flows.
**Root cause:** Default assumption that an annual report can be derived
from the 12 monthly reports. In many jurisdictions, the annual filing
is a separate submission with its own form, validation, and deadline.
**Mitigation:** v2.5 CCG prompt includes filing-mechanics clarification
that monthly, quarterly, and annual employer filings are typically
SEPARATE submissions and must be confirmed for the specific country.
Specifically noted in the Egypt-Chad-similar context: ETA monthly,
quarterly, and annual forms all require separate employer submissions.

---

## F22 — 32MB input limit silently exceeded by oversized source PDFs (v2.5 NEW)

**Source:** Egypt P4+D1+D2 (Manju Shetija, 27 May 2026)
**Observed:** Two downloaded PDFs (13MB VAT guide irrelevant to payroll,
12MB scanned ministerial decree) pushed total source PDF folder over
the 32MB Claude CLI input limit. Stage 3 failed silently — the request
was rejected by the CLI before any agent processing.
**Root cause:** No pre-flight check for total PDF folder size. No per-
file size warning. No filter on which PDFs were payroll-relevant.
**Mitigation:** v2.5 pre-flight now:
1. Calculates total source PDF folder size; warns at 20MB, errors at 28MB
2. Lists the 5 largest files when exceeding threshold
3. Warns on any single PDF >5MB (likely scanned, low text extraction)
4. Auto-creates per-stage subfolders (ccg-sources/, spec-sources/, etc.)
   so source files can be partitioned per stage rather than all loaded
   into every stage
5. References country_source_checklist_template.md (R3) which lists
   payroll-relevant document categories — discourages downloading
   irrelevant material like VAT guidelines or corporate-tax guides

---

## How to use this log when planning a country build

1. **Before Stage 1**, read this log end-to-end. Each F-entry is a known
   failure pattern that the corresponding C-check will catch — but it's
   cheaper to prevent than to fix at audit.

2. **During Stage 2 (Scope Lock-In)**, populate scope_manifest.json with
   explicit decisions for every artifact (in-scope with spec, or descoped
   with reason). This prevents F15.

3. **During Stage 3-7 (Artifact Generation)**, the agent prompts reference
   the relevant F-entries inline ("Avoid F9: thin column schema — populate
   all 21 columns").

4. **During Stage 9 (Audit)**, presubmission_audit_local.py runs C1-C22.
   Any FAIL or MANUAL re-runs the corresponding fixer prompt.

5. **At handover**, the QA report cites which F-entries were checked and
   passed. This makes it easy to demonstrate to the dev team that known
   failure patterns have been actively prevented.

---


## F23 — Pre-flight PDF size check sums recursively (v2.5 BUG)

**Source:** Chad v2.5 first run (Wallisson Gomes, 27 May 2026)
**Observed:** Pre-flight check `Source PDFs total 43MB exceeds the 28MB safety
threshold` triggered when 3 PDFs (~11MB) were mirrored to 4 per-stage subfolders
(ccg/spec/wtc/dd-sources). The check counted each PDF 4 times = 44MB total.
This defeats the v2.5 per-stage partitioning design.
**Root cause:** Pre-flight uses recursive `find ... -name '*.pdf'` + total size,
not per-subfolder max.
**Mitigation (workaround until v2.6):** Keep PDFs in only ONE subfolder
(typically ccg-sources/). Stages without their own PDFs fall back to web research.
**v2.6 fix:** Change pre-flight to check max(per-subfolder size), not total.
---
## F24 — Stale scope/mandate document (v2.5 NEW)
**Source:** Canada CA-FED-COVERAGE.md (Wallisson Gomes, July 2026 external design review)
**Observed:** The top-level scope mandate document still read "Canada FEDERAL payroll
only (no Quebec...)" long after Québec had been deliberately built out as a full
parallel regime (Part II of the CCG, dual-jurisdiction WTC, RL-1/TPZ specs). An
external reviewer read the stale mandate as current and flagged Québec's presence
as a contradiction.
**Root cause:** No discipline requiring the mandate document to be updated the same
day a real scope decision changes — the artifacts implementing the expanded scope
were updated, but the document describing scope itself was not.
**Mitigation:** Treat the Scope line of any country's mandate document as a living
statement. Any time scope actually changes, update the mandate doc immediately,
with a dated changelog entry — do not wait for a downstream artifact or reviewer
to expose the drift.
---
## F25 — Report-Specs-built-before-DD naming drift (v2.5 NEW)
**Source:** Canada CA-DD-001 x Report Specs cross-check (Wallisson Gomes, July 2026)
**Observed:** Every Report Spec cited DD field names as literal "DD <CODE>" tokens.
Because Report Specs (Stage 3) build before the DD (Stage 4) in the standard
pipeline order, dozens of these tokens (SIN, PAY_PERIOD_TYPE, QC_EMPLOYER_IDENT,
and others) referenced names that did not match the DD's real Internal Codes once
it was actually built.
**Root cause:** Stage 3's DD-field citations are unavoidably forward guesses at
names that do not exist yet, and nothing in the pipeline forces a re-check once
Stage 4 completes.
**Mitigation:** The moment Stage 4 (DD) is complete, immediately run a dedicated
Report-Specs x DD field-name cross-check as part of Stage 4's own Definition of
Done, not a later audit.
---
## F26 — Calculated/transactional value misclassified into the DD (v2.5 NEW)
**Source:** Canada CA-DD-001 build correction (Wallisson Gomes, July 2026)
**Observed:** A research dossier's "artifact target" note for EI insurable
hours/earnings-by-pay-period casually said "DD <field name>." Followed literally,
this added the field to the DD, which violates the Stage 4 build prompt's own
EXCLUDE list ("Calculated amounts", "Transactional per-payrun data"). The field
had to be removed.
**Root cause:** A dossier's casual "DD <field>" phrasing was treated as an
instruction rather than checked against the Stage 4 scope rules.
**Mitigation:** Before adding any field a dossier calls a "DD field," check it
against the Stage 4 INCLUDE/EXCLUDE list explicitly. An accumulator's correct home
is the WTC's own Subject-to-X flag plus YTD-Load/YTD-Remarks mechanism, never a
new DD field.
---
## F27 — Downstream artifact not re-synced after a source correction (v2.5 NEW)
**Source:** Canada SIR x Report Specs / scope_manifest cross-check (Wallisson Gomes, July 2026)
**Observed:** The SIR's confidence percentages and a Report Spec's later-added
scope-limitation note (non-Québec provincial tax) were compared side by side. The
Report Spec and scope_manifest.json had already been updated with the new
limitation; the SIR, built earlier, had not been revisited and carried no matching
note.
**Root cause:** Nothing in the pipeline flags a downstream artifact for review when
the upstream artifact it quoted or summarized later changes.
**Mitigation:** Whenever a Report Spec's Accuracy Assessment or scope_manifest's
known_limitations changes, immediately re-open every artifact that ever quoted or
summarized that content and check for drift the same day.
---
## F28 — Skill file references/ going stale after source edits (v2.5 NEW)
**Source:** Canada skill-file build (Wallisson Gomes, July 2026)
**Observed:** The skill file's references/ folder is a flattened, verbatim copy of
the CCG/WTC/DD/SIR/Report-Specs/Payslip content, built once early in the process.
Every one of those source documents was edited multiple times afterward; the skill
was refreshed only once, for a single known issue, and otherwise went unsynced.
**Root cause:** No mechanism forces the skill file to notice when any of its six
source documents changes.
**Mitigation:** Log a one-line changelog note in the skill's own QA-report
reference file every time any source document changes, even if a full re-sync is
not done immediately, so the debt stays visible.

## F29 — One-directional fix certified as complete (v2.9 NEW)
**Source:** Belgium Stage 10 cross-artifact check (compliance-qa-auditor, 17 Aug 2026)
**Observed:** Four separate instances in one dossier, all the same shape. (1) The scope
manifest's inbound integration array was crosswalked to the SIR and grown from 12 entries
to 19; the outbound array in the same file was never opened and is still 12 against the
SIR's 19, short by exactly seven flows, three of which have a delivered v1.2 Report Spec
on disk. (2) A review log recorded a defect as "addressed in the fix pass" while all 538
target cells sat untouched in four files the fix pass never opened. (3) A Data Dictionary
Version Control cell certified that "the 35 NOT FOUND gap markers are registered in
scope_manifest.json known_limitations" — the workbook holds 36 and the register holds none
of them. (4) A Version Control cell recorded that 220 spec cells were "deliberately left
NOT FOUND ... no DD field by design" while those same 220 cells still read "mapping not yet
decided; requires the Stage 4 Data Dictionary".
**Root cause:** A fix pass writes its changelog from its *intent*, not from a re-read of the
artifact. Where a fact lives in two symmetrical places — inbound/outbound, spec/DD,
cell/changelog — closing the half that tripped the finding satisfies the finding's wording
and the certification then makes the other half invisible. This is worse than an unfixed
defect: an unregistered gap invites a reader to look, whereas an unregistered gap carrying a
written assurance of registration stops them looking.
**Mitigation:** A changelog line may not say "fixed", "addressed" or "registered" without
naming the file the change landed in, and the closing auditor must re-read that named file.
For any two-directional register (inbound/outbound, A-cites-B/B-cites-A, cell/certification),
the fix is not closed until both directions are measured — and the count on each side is
stated in the changelog, so a reader can falsify it without opening the artifact.

## F30 — Gap registers proliferate per artifact and no country-level register is their union (v2.9 NEW)
**Source:** Belgium Stage 10 cross-artifact check (compliance-qa-auditor, 17 Aug 2026)
**Observed:** Belgium ended with four unconnected gap registers and no union of them. The SIR
carried the best gap discipline in the dossier — 27 entries with integration, what-is-missing,
category and a named owner with real authority addresses — and all 27 were local to that
document. The report specs carried 848 NOT FOUND cells with per-spec accuracy statements. The
DD carried 36 markers. The CCG carried 1, correctly written with the exact source that would
close it and a warning not to extrapolate. `scope_manifest.json → known_limitations` held 7
entries and had not gained one in five days. Not one gap from any of the other three registers
had reached it. Separately, the Belcotax spec asked in four cells for a WTC catalogue gap to
be "raised at the next stage gate"; nobody raised it, because there was no register to raise
it into.
**Root cause:** Each stage's Definition of Done requires the *builder* to record its own gaps,
which they did well. Nothing requires anyone to compute the union, so the country-level
register stays at whatever the scope stage wrote on day one. G-CLEAN says an unresolvable gap
belongs in a named limitation rather than a marker in a table — but with four registers and no
owner of the whole, every artifact can satisfy G-CLEAN locally while the country satisfies it
nowhere.
**Mitigation:** At run close, build the country-level limitation register as the explicit union
of every artifact's local register plus the QA report's own, one row per gap with its consumers
and what would close it — and reconcile the count both ways. A local register is evidence the
builder was honest; it is not evidence the country disclosed the gap. Corollary: when one
artifact writes "raise this at the next stage gate", that sentence is an inbound work item for
the closing auditor, and grepping for it is cheap.

## F31 — A deterministic lint named "across ALL artifacts" covers a subset (v2.9 BUG)
**Source:** Belgium Stage 10 cross-artifact check (compliance-qa-auditor, 17 Aug 2026)
**Observed:** `mercans_pipeline_v2_9.sh` lines 2417-2462, the C29 residual-marker lint,
documented as running "across ALL artifacts". Measured: it scans `01-ccg`, `04-reports-spec`,
`02-wtc` and `05-data-dictionary` — not `03-statutory-integrations` (the SIR), not
`06-payslip`, not `scope_manifest.json`. For the one .docx it does read it uses
`'\n'.join(p.text for p in Document(...).paragraphs)`, which is paragraphs only, so every
table cell in the CCG is invisible to it — and the CCG's one live marker is inside a table.
Its marker list (`TODO`, `TBD`, `FIXME`, `VERIFY No`, `[placeholder]`, `[CHECK]`, `[?]`, "to
be confirmed", "to be verified") omits `NOT FOUND` and `PENDING`, both invented by the builds
themselves, omits bare `placeholder` outside brackets, and uses `\bXXX\b`, which cannot match
`XXXXX`. Net effect: a deterministic PASS is achievable over a corpus carrying 892
unresolved-gap markers. Two adjacent checks compound it — C18 ("every filing in
scope_manifest must have a Spec file") exists only as prompt text, and C9 (WTC tax codes
against the country's own legend) appears nowhere in the script at all, not even as prompt
text, though the Stage 5 Definition of Done depends on it. Between them C18 and C9 would have
caught two of Belgium's five surviving blockers.
**Root cause:** The marker vocabulary and the artifact set both grow with each country while
the lint's regex list and glob list are fixed at the version that introduced them. Nobody
feeds a build's newly invented gap token back into the check that exists to catch exactly it,
and the payslip and SIR were added to the pipeline after C29 was written.
**Mitigation:** Whenever a build invents a gap token, add it to the C29 marker list in the same
commit. Derive the lint's scan list from the artifact inventory rather than hardcoding four
directories, and read .docx tables as well as paragraphs. Test any marker lint by planting a
marker in each artifact type and confirming it FAILs on all of them — a lint never tested
against a positive is a lint that reports the absence of what it cannot see. And per L3: never
report a check as run without grepping the script body for the id first, using the
deterministic blocks' own reporting shape (`return ('Cnn', ...)`) rather than a `Cnn:` grep,
which matches prompt bullets and over-counts by five.

---

## F32 — DD↔Spec reconciliation run as a single method across structurally
heterogeneous specs (v2.9 NEW)

**Source:** FR-QA-REPORT.md Check 4 (720/984 = 73.2%) + manual reconciliation of all
264 flagged rows (France, Wallisson Gomes, 2 Sep 2026)
**Observed:** 264 spec rows across 12 of 15 France specs were flagged `NO DD
COUNTERPART ... registered as an open gap ... for scope owner adjudication`. Manual
reconciliation against the DD and the DSN Cahier Technique found the vast majority
false: 88 rows matched an existing DD field outright, 21 more matched after
stripping a "Former"/"Ancien(ne)" prefix and re-matching the current field. The
remainder clustered into three structural categories the reconciliation never
distinguished: (a) 41 rows belonged to non-native-code specs (DPAE cites Labour
Code articles, the accident declaration DAT cites Cerfa form field labels, the
payroll tax return cites form box positions) — no shared key with the DD's cited
norm codes ever existed, so these could not have matched regardless of whether the
DD field existed; (b) 58 of 59 "Former X" rows in correction/history blocks
(`Changements Contrat` and siblings) named a field whose *current* counterpart
already existed in the DD, but the reconciliation had no strip-prefix-and-rematch
step; (c) 8 rows belonged to inbound return-flow specs (data the collecting body
sends *to* the employer — CRM, AGIRC retour, CARSAT notification) and should never
have been tested against the DD at all, since the DD holds employer-side master
data, not authority-computed return values.
**Root cause:** The reconciliation assumed every spec in a country build shares one
identification system and one data direction. Neither holds: a country's
statutory reporting always includes non-native-code filings, correction blocks,
and inbound integrations, each needing different reconciliation logic.
**Mitigation:** Before running DD↔Spec reconciliation, classify every spec by (i)
field-identification system — native norm code vs. other official identifier
(statute article, form field label, form box position) — and (ii) data direction
— outbound (employer declares) vs. inbound (authority returns). Outbound
native-code specs reconcile by code match, stripping any "Former"/historical
prefix and re-matching the current field first. Outbound non-native specs are
flagged for primary-source reconciliation, not automated matching. Inbound specs
are excluded from DD reconciliation entirely. Related: complements F30 (this is a
single register's *content* being wrong, not the aggregation-across-registers gap
F30 describes) and F31 (a semantic reconciliation-method failure, distinct from
F31's mechanical lint-coverage failure).

---

## F33 — Reconciliation hint annotations asserted as verified without a lookup
ever being performed (v2.9 NEW)

**Source:** FR-ALIGN-001, manual reconciliation of column L "System Mapping"
annotations (France, Wallisson Gomes, 2 Sep 2026)
**Observed:** Every one of the 264 flagged rows carried a synthetic key
(`FR.DD.<ENTITY>.<FIELD>`, e.g. `FR.DD.OETH.NOMBRE`) immediately followed by
`[reconciled against FR-DD-001 v1.1 - NO DD COUNTERPART ...]`. The synthetic key
is the building agent's own guess at where the field should live in the DD — it
was never actually compared against a real DD field name. The word "reconciled"
asserts a verification step that provably did not happen for at least 176 of the
264 rows (the ones later found to have a real DD match, or to belong to a block
that should never have been tested at all).
**Root cause:** The agent generated a plausible-looking mapping hypothesis, then
reported it using language indistinguishable from a row that had genuinely been
checked. Unlike an explicit `TBD` (F6) or `NOT FOUND` (F31), this failure produces
no visible signal that the finding is unverified.
**Mitigation:** Any row whose System Mapping contains a synthetic
`<COUNTRY>.DD.<ENTITY>.<FIELD>`-style hint must be accompanied by the actual
lookup evidence — an exact-match result, a documented near-miss naming the real DD
field it was checked against, or an explicit statement that no DD field exists
under any name. A synthetic key with no lookup evidence fails regardless of what
the surrounding prose claims. Related: same failure family as F29 (an assertion of
completeness substituting for re-verification) — but F29 occurs during a fix pass
revisiting existing content, while this occurs during original construction,
before any fix pass exists to audit it.

---

## F34 — DD composite/address block built asymmetrically across structurally
parallel entities (v2.9 NEW)

**Source:** France Data Dictionary Country Fields sheet, place-of-work address gap
discovery (France, Wallisson Gomes, 2 Sep 2026)
**Observed:** The DD captured all 7 official DSN sub-rubriques for the employee's
personal address and for the employer entity's address, but only 3 of the same 7
for the place-of-work address — Street, Postal Code and Town were present; Country
Code, Foreign Distribution Code, Building Complement and Delivery Service
Complement were missing, even though the identical 4 fields exist for the other
two entities under the same norm pattern.
**Root cause:** The building agent modelled the personal-address and entity-address
blocks from a complete source enumeration but modelled the place-of-work address
from a partial one, likely stopping once Street/Postal/Town were found without
confirming the full rubrique range for that specific block.
**Mitigation:** Whenever the DD captures an address-like or other composite
multi-field block for more than one entity, compare the sub-field set captured
for each entity. Any entity missing a sub-field that another entity in the same
rubrique family has is flagged for verification against the source norm before
the DD is considered complete for that block.

---

## F35 — Column populated with content that contradicts its own header (v2.9 NEW)

**Source:** France and Belgium Wage Type Catalogues, defect found when the France
catalogue was read on screen by the artifact owner (Wallisson Gomes, 3 Sep 2026)
**Observed:** In BOTH delivered catalogues, column D "Wage Type Explanation" was
empty on every one of the 378 (FR) and 300+ (BE) rows, while column F "Formula"
carried the entire statutory explanation — legal citations, DSN declaration rules,
configuration warnings — averaging over 1,000 characters per cell. A column headed
Explanation explained nothing; a column headed Formula contained no formula. The
CZ V2.0 master template shows Formula is the HRB ENGINE EXPRESSION column
(`$hr.variable`, `MIN(48000;$hr.pension_contribution_cumulative)`,
`ADD($63955.amount;1)`), populated on only 19 of its 589 rows.
**Root cause:** The pipeline's own WTC prompt instructed `D: Explanation ORANGE`
(leave empty, dev team fills) while asking column F for a "plain language formula".
With D closed off, the generating agent pushed the whole explanation into F. Two
countries were built this way before anyone read the output as a reader rather than
as an auditor: every factual check passed, because the FACTS were correct — only
their location was wrong.
**Mitigation:** Pipeline prompt corrected — D is now BLUE and mandatory, F is ORANGE
and left for the development team, both with the incident recorded inline so the
rule is not "simplified" back later. As a general check: for every artifact, read
each column header and ask whether the content under it is what a reader would
expect to find there. A cell can be factually perfect and still be in the wrong
column, and no factual audit will ever catch it.

---

## F36 — Neighbouring field's text overwriting the wrong cell (v2.9 NEW)

**Source:** France Report Specs, found during the field-by-field content audit
(Wallisson Gomes, 3 Sep 2026)
**Observed:** 18 cells across 8 spec files carried the description belonging to an
adjacent field instead of their own. The clearest case repeated across 6 files: in
the shared S10 sender block, "Title code" was described as "Surname and forename of
the sender contact" and "Telephone number" as "Fax number of the sender contact" —
each field had taken its NEIGHBOUR's text. Also seen: Employment status described
as a public employer's internal number; INSEE municipality code and Legal nature
swapped; a Field Options code description carrying an entire different block's text.
**Root cause:** Text written into a shared or repeated block was offset by one row
relative to the field it belonged to, and the error propagated wherever that block
was reused. Every affected cell was individually plausible prose, so nothing looked
wrong until the cell was read against its own field name.
**Mitigation:** When a block of fields is shared across several specs, correct it
once and then run a GLOBAL scan for the same wrong text in every other file before
declaring it fixed — a defect in a shared block is never in one file only. At the
field level, read each description against its own field name and ask whether the
text describes THIS field; do not read descriptions as a continuous narrative,
which is what makes an off-by-one invisible.

---

## F37 — A rate restated in prose contradicting the same file's own calculation (v2.9 NEW)

**Source:** France FR-DGFIP-003 Taxe sur les salaires spec, found on an independent
re-scan AFTER the file had been signed off as complete (Wallisson Gomes, 3 Sep 2026)
**Observed:** Cell M14 explained the notice's worked example as "a 1,000 EUR salary
is taxed at 4.25% on the whole 1,000 and again at 4.25% on the part above the first
threshold". The second rate is 8.50%, not 4.25%. The workbook's own Example Analysis
sheet already computed the identical case correctly — `1 000 x 4,25 % = 42,50, plus
(1 000 - 769) x 8,50 % = 19,64` — so two sheets of one workbook disagreed with each
other. An earlier correction pass on this same file had fixed 12 rate cells and
missed this one.
**Root cause:** The earlier correction searched for the wrong VALUE PAIR (4.25/9.35)
in structured rate cells. This defect was a correct rate REPEATED where a different
rate belonged, living in free-text prose — a shape the search was not looking for.
Structured cells were audited; explanatory prose carrying the same numbers was not.
**Mitigation:** Free-text explanation cells carry rates too and must be audited with
the same rigour as the structured cells. Where a file states a worked example in more
than one place, cross-check the places against each other — an internal contradiction
is the cheapest defect to find and needs no external source. Do not treat a file as
closed because a correction pass ran on it: verify the specific claim, not the fact
that a pass happened.

---

## F38 — Template table objects carried into the country file (v2.9 NEW)

**Source:** France and Belgium Data Dictionaries, found when the artifact owner
opened the Belgium file and saw cells reading "Coluna1" (Wallisson Gomes, 10 Sep 2026)
**Observed:** Belgium opened in Excel as `BE-DD-001-v1.3 [Reparado]` with `Coluna1`
and `Coluna2` written into the middle of the ID Information data, in the two ORANGE
columns that are supposed to stay empty. France carried the identical defect,
undetected only because nobody had opened it in Excel yet: `Table_2` pointing at
`A13:V17`, `Table_3` at `B42:X292`, and `Table_7` with `headerRowCount="0"` and
`Column1` through `Column5` already written into the XML.
**Root cause:** The DD is built by loading `CZ_Data_Dictionary_V2_0.xlsx`, clearing
the data rows and repopulating. The CZ workbook contains thirteen Excel Table objects
whose ranges point at CZ's own rows. Clearing rows does not move or delete them, so
they survive into the country file pointing at ranges that no longer mean anything.
Excel treats the mismatch as damage, silently repairs the workbook on open, and
because a Table must have a non-empty unique name per column, it writes its own
default header names — localised, hence `Coluna1` on a Portuguese Excel — into the
cells its broken range treats as the header row. The values look like corrupted data
but are Excel's repair output. Note the refs were never random: `A13:V17` is exactly
where CZ's own second (employer) section sits.
**Mitigation:** Stage 4 prompt now requires the table parts to be deleted after
populating, by rewriting the xlsx archive (openpyxl will not remove them: drop
`xl/tables/tableN.xml`, strip `<tableParts>` from each sheet, strip the table
relationships and the `[Content_Types].xml` overrides). Cell fills, fonts, widths and
merges are cell-level and survive untouched. VERIFICATION IS VISUAL AND MANDATORY:
open the delivered file in Excel; if the title bar says `[Repaired]` / `[Reparado]`,
the tables are still there. No script check catches this, because the file is valid
until Excel opens it.

---

## F39 — Two-section sheet structure flattened into one block (v2.9 NEW)

**Source:** France Data Dictionary, raised by the artifact owner as "employee and
employer not clear" and confirmed by comparison against Belgium and the CZ master
(Wallisson Gomes, 10 Sep 2026)
**Observed:** France's ID Information held 25 fields and Country Fields held 173, each
as a single undivided block with employee-level and employer-level fields interleaved
and no visual break. Belgium and the CZ master both split each sheet into two
sections, each with its own title row and its own repeated column-header row:
employee fields first, then `Country-Specific Legal Entity Fields`. France had also
stranded one employer-level field (`Occupational Health Service Name and Address`) in
the middle of the employee block, and had left all 198 field-grouping cells (Parent
Field Group, its ordinal and internal code, Sub Group and its two) empty — the only
trace of the employee/employer distinction was an opening phrase buried at the start
of the Additional Notes prose on each row.
**Root cause:** The build agent populated the sheets as flat lists. Nothing in the
Stage 4 prompt described the two-section structure, and clearing CZ's data rows also
removed the second section's title and header rows, so the structure was not visible
in the template the agent was copying from either. The information was correct
throughout — only its arrangement was wrong, which is why every factual audit passed.
**Mitigation:** Stage 4 prompt now specifies the two-section layout explicitly for
both sheets, requires each group to stay contiguous, and requires the field-grouping
columns to be populated using the CZ master's own vocabulary verbatim
(`employer_information`, `wizard_step:personal`, `tax_and_social_security_details`,
`identification_information`, `wizard_step:contact`, `employment_details`,
`reporting_details`, `Dependent`) rather than invented keys, since the product matches
on those strings. General lesson, and the same one as F35: an artifact can be
factually perfect and still unusable because the content sits in the wrong place. Read
the delivered file as a reader would, not only as an auditor checking values.

---

## F40 — Shared builder defect copied into every report spec (v2.11 NEW)

**Source:** France validation of 6 Oct 2026. Specs review A (SA-01, SA-02, SA-03, SA-05,
SA-07), specs review B (SB-09) and the DSN-Val triage of FR-DSN-001 (SD-01 to SD-05),
`the France validation project's review notes (internal)`. Closed by the pipeline improvement
programme, Phase 1 (Wallisson Gomes, 7 Oct 2026). Root cause RC3.
**Observed:** One France builder (`04-reports-spec/_lib/`) wrote all 15 report specs, so
its defects showed up in every DSN-borne spec at once:
- Rule text was cut at 2,500 characters (`fr_norm.py` line 292, `[:2500]`). FR-DSN-001
  lost 71 control rules, and nothing in the spec showed the loss.
- One generic monthly block tree was copied into the event signals, with blocks in
  ascending ID order. CT2026.1.2 s.3 p.76 forbids that order.
- Example SIREN and SIRET values failed the Luhn key the norm checks on deposit, and a
  woman was given a NIR starting with 1.
- The sample DSN produced 51 DSN-Val anomalies, 44 of them blocking.
On the pre-validation issue (`Archived/issued-2026-09-10`), the new checks report:
- C34: 261 control rules missing (92 truncated, 169 absent);
- C35: 53, 54 and 29 blocking anomalies;
- C36: 44 invalid identifiers.
**Root cause:** Every country wrote its own spec builder, and nothing checked that builder's
output against the norm or against the authority's own validator. A defect in the
generic part (cell writing, rule joining, tree order, example identifiers) was therefore
invisible: each spec looked complete, and every factual audit passed.
**Mitigation:**
- The generic parts now live in one shared library, `shared/spec-builder/` (`mercans_spec`).
  France was re-pointed to it, and the rebuild reproduces the approved finals with
  0 cell differences.
- Three blocking Stage 9 checks were added. C34: every control rule of the norm is
  present and untruncated. C35: the sample validates with 0 blocking anomalies in the
  authority validator (France: DSN-Val batch). C36: identifier check digits are valid.
- A mutation test (`shared/spec-builder/tests/test_mutations.py`) proves that a rule cut
  at 2,500 characters and a SIREN with a wrong key are both caught.
General lesson: a defect in shared code is a defect in every artifact it writes. Check
the output against the norm and the authority's validator, not against the builder's own
idea of completeness.

---

## F41 — Research never tested against an independent oracle before delivery (v2.11 NEW)

**Source:** France validation of Oct 2026. The suite `the France validation project (internal)`
ran 112 cases against modele-social 11.1.0, the URSSAF engine. The CCG review
(Test 0, 77.8 %) and the WTC/DD review (Test 0, 31/40 = 77.5 %) followed, and defects
D-01 to D-19 were logged. Closed by the pipeline improvement programme, Phase 2
(Wallisson Gomes, 7 Oct 2026). Root causes RC1 and RC6.
**Observed:** The delivered France research agreed with the official engine on 94.7 % of
lines. Four research defects only came to light in a separate validation project
after delivery:
- D-01: the APEC cap;
- D-03: net social for managerial staff;
- D-11: CPF-CDD missing;
- D-17: COTAM for non-residents.
The CCG itself re-verified only 17 of 149 questions (11 %). Test 0 scored about 78 %
against a 95 % target. After correction, the research reaches 2,403/2,462 = 97.6 %,
and every remaining residual is a confirmed engine defect with a primary source.
**Root cause:** The pipeline checked artifacts against each other and against their own
templates, never against an independent calculation of the law. Factual accuracy was
self-reported. An error that was consistent across artifacts therefore passed every
gate.
**Mitigation:**
- Stage 1 records the country's oracle: the authority's engine, or its official worked
  examples where no engine exists. Stage 2 checks that it is there, and
  `build-manifest.oracle` carries it (contract 1.1.0).
- New blocking check C37 (Stage 9b, External Validation), run by
  `shared/validation-suite-template/run_suite.py`. It needs three things: every residual
  backed by a confirmed engine defect with a primary source, no regression against the
  country baseline, and agreement of at least 98 %.
- New blocking check C39 (Test 0) at Stage 10: at least 40 risk-weighted assertions,
  each with a primary source and a quote, scoring at least 95 %.
- The France suite is the reference instance (`FR-compliance/_validation/`). It reproduces
  baseline 20261006-093517 exactly. A changed CSG rate (6.80 % to 6.70 %) produces 275
  unexplained residuals and 275 regressions, and C37 fails.
General lesson: agreement between artifacts is not accuracy. Measure accuracy against
an independent oracle and against the primary text, inside the pipeline, before delivery.

---

## F42 — Worked examples typed instead of computed (v2.11 NEW)

**Source:** France CCG review of 6 Oct 2026 (worked examples with arithmetic and logic
errors, F-11 and F-13; cent residues), and check C38 run on FR-CCG-001 v1.0 and the
approved v1.1 (7 Oct 2026). Root cause RC8.
**Observed:** C38 found three errors in Example 1 of the approved v1.1. The RGDU table
prints the inner term (3 × 21,876.40 ÷ 34,986.00) − 1 as 0.875970; the correct value is
0.875870. It prints 0.437985 ^ 1.75 as 0.235942; the correct value is 0.235805. The
final coefficient 0.1091 is right, so the printed intermediate values were typed, not
carried. The employer health line shows 2,915.50 × 13.00 % = 379.01, but the exact
product is 379.015, which the CCG's own half-up rule rounds to 379.02.
**Root cause:** The examples were written as prose tables with hand-entered numbers.
Nothing regenerated them from the facts, and nothing recomputed them, so they were
reviewed by eye.
**Mitigation:**
- Stage 1 and artifact-builder: every numeric example is produced by a script from
  the facts (`01-ccg/_examples/`), with the arithmetic written out.
- New blocking check C38 (`shared/validation-suite-template/worked_examples_check.py`)
  recomputes every base × rate, every written expression and every total. Base × rate
  and totals must match exactly; chained expressions are allowed one unit of the last
  decimal.
- A mutation test injects a one-cent error and a ten-cent total error, and both are caught.

---

## F43 — Special populations not covered systematically (v2.11 NEW)

**Source:** France validation, Oct 2026 (defects D-11 and D-17; CCG review F-01 to F-28;
WTC/DD review). Closed by the pipeline improvement programme, Phase 3 (Wallisson Gomes,
7 Oct 2026). Root cause RC2.
**Observed:** The France research was organised by legal domain and missed populations the
law treats differently. Missing outright:
- COTAM for employees affiliated to French social security but not tax-domiciled in France
  (D-17);
- the 1 % CPF-CDD employer contribution on every fixed-term contract (D-11);
- the AT/MP daily benefit.
Wrong: the Apec cap, net social for managerial staff, the managerial prévoyance in net
taxable, and part-time / RGDU proration.
**Root cause:** The 13-domain sweep asks what each law says. Nothing asked what payroll
does for each kind of person, and the only population check (C31) covered residents
against non-residents.
**Mitigation:**
- A mandatory 13-row coverage matrix, `facts.coverage_matrix`, contract 1.2.0, in
  `_research/CCG-coverage-facts.json`. It covers resident and non-resident employees,
  fixed-term, part-time, officers without a contract, apprentices, maternity / paternity /
  parental leave, work accident, termination, mid-month joiner and leaver, annual
  regularisation, overtime and multiple employers. Every row is answered with its
  income-tax, social-security and reporting effect, a CCG location and a primary source,
  or marked not applicable with a reason.
- New blocking check C40 (`shared/research-checks/research_checks.py`). It also checks that
  each CCG location is a real heading.
- A test proves that an empty row, a source-less answer and a dangling location each fail
  Stage 9, and that the contract rejects the first two.

---

## F44 — Single-pass research: numbers never re-verified, no final bulletin sweep (v2.11 NEW)

**Source:** France validation, Oct 2026. The CCG self-reports that 17 of 149 questions
(11 %) were re-verified. The WTC/DD Test 0 scored 77.5 %; for example, the minimum garanti
was 4.22 € where the BOSS gives 4.25 € (W26, finding F-14). Closed by the pipeline
improvement programme, Phase 3. Root cause RC1.
**Observed:** Values were researched once and then trusted. Reviews WebFetched only a
sample of citations. No step searched the official bulletins for changes published during
the build year before delivery, so a mid-year change could only be caught after delivery.
**Root cause:** Verification was a sample, not a census, and currency had no owner.
`verified_on` existed in the register but nothing enforced it, and there was no final sweep.
**Mitigation:**
- The adversarial gate: in each artifact review, compliance-qa-auditor re-verifies 100 % of
  the numeric facts and base rules (pass P2, step 6), and records the result in
  `review.numeric_verification` (contract 1.2.0). The contract rejects a PASS with any
  unverified key.
- New blocking check C41 has two parts. Every register row in force needs an
  `effective_from` and a `verified_on` no more than 120 days old. The final sweep of the
  national official bulletins, from 1 January of the build year to today, must be recorded
  in `00-official-sources/bulletin-sweep.json` no more than 14 days before release, with an
  action for every hit.
- Stage 9's content fixer and compliance-source-hunter run the sweep.

---

## F45 — No cross-artifact consistency on facts and versions (v2.11 NEW)

**Source:** France validation, Oct 2026 (CCG review F-19; specs reviews SA-06 / SB-34;
WTC/DD review F-20), and checks C42-C46 run on the pre-validation copy and on the finals
(7 Oct 2026). Closed by the pipeline improvement programme, Phase 4. Root cause RC4.
**Observed:**
- Versions disagreed. A v1.0 CCG carried "Version 1.3". The finals still show
  CCG v1.1 with Version Control 1.3, WTC v1.1 with 1.4, and DD v1.2 with 1.6.
- All 15 finals specs cite FR-DD-001 v1.1 (up to 578 times in FR-DSN-001) against
  a delivered DD v1.2.
- Another country's ids were left in the text: "FR-NSSO / FR-FIN series" in the CCG, and
  BE-NSSO-002/004 in the Report Matrix of FR-DSN-001/002/003.
- The payslip carries a note citing REFERENCE_Payslip_Tunisia.xlsx.
- scope_manifest.json disagrees with the specs on 8 formats, among them DPAE "XML"
  against "NOT XML" and SOLTéA "XLSX" against "a web application".
- The 264 false "NO DD COUNTERPART" lines came from the same lack of a shared reference.
**Root cause:** Every artifact typed its own numbers, versions and cross-references, and
copied structure from precedent files of other countries. Nothing held one value per
fact, one version per package or one format per filing, and C32 read a fact-key
registry (`shared/fact-keys.yaml`) that did not exist.
**Mitigation:**
- `shared/fact-keys.yaml` now exists.
- Stage 1 writes `_research/CCG-facts.json`, and every number in text is carried as
  `[[FACT:key=value]]`. Stage 13 strips the markup.
- `scope_manifest.package` and `build-manifest.package` (contract 1.3.0) hold one version
  and one issue date for the delivery.
- New blocking checks: C42 (foreign leftovers, with each country's series read from the
  dossiers on disk), C43 (one package version, including cross-references), C44
  (manifest formats equal spec formats) and C46 (every tag equals the facts file), in
  `shared/consistency-checks/`.
- On the archived France copy the checks flag all the known issues: the version label,
  the DD version, NSSO/FIN, and the DPAE/SOLTéA formats.

---

## F46 — Technical design not derived from the research (v2.11 NEW)

**Source:** France regulation design review (`docs/history/2026-10-06-final-release/
FR-DESIGN-v1_1-CHANGES.md`, R-35, R-36, R-42), and check C45 on the live 6 Oct design.
Closed by the pipeline improvement programme, Phase 4. Root cause RC5.
**Observed:** Flags 58209 (company officer) and 58222 (reconcile RGDU) take only the
values 1 and 2, but gates read `LESS($58209;1)` (×3) and `LESS($58222;1)` (×2), so
those gates could never fire. The review also lists five design-vs-research conflicts.
The design was written outside the pipeline, after the research, and was not checked
against it.
**Root cause:** No pipeline stage produced the design from the facts, and nothing
evaluated whether a gate could ever be true.
**Mitigation:**
- New Stage 12 Design generates the regulation design from the facts, the coverage
  matrix, the CCG, the WTC and the DD (`shared/design-template/`, with the approved FR
  design as reference). Every flag declares its values.
- Blocking check C45 evaluates every LESS / GREATER / EQUALS gate against the flag's
  declared values. C46 checks the design's numbers against the facts.
- On France: 5 dead gates on the live design, 0 on the approved one.

---

## F47 — Revision history written into the deliverables (v2.11 NEW)

**Source:** France release of 6 Oct 2026. Changelogs, "corrected vs ...", review ids and
version churn were removed by hand with sim_fr/single_issue.py and finalize_release.py.
Closed by the pipeline improvement programme, Phase 5. Root cause RC7.
**Observed:** On a copy of the FR finals, the release cross-check finds 2,544 traces in
20 files. Examples:
- Version Control rows narrating each round ("FRVAL corrections of 2026-10-06 ...
  CHANGELOG.md ... Regenerated by the corrected builder");
- review ids in the content ("FRVAL SB-27", "SA-25 - ...");
- "Corrected 2026-09-02 per master_verification_v2.py audit" stamps;
- pipeline-internal references ("v2.7 STEP 3.5", "v2.4 C9");
- file names and covers on four different versions;
- template metadata (creator "openpyxl", created 2024, custom properties, customXml).
**Root cause:** Each correction round wrote its own history into the artifact, because
the template asked for a Version Control history. No release step separated the rule in
force from the record of how it was reached.
**Mitigation:**
- New Stage 13 Release (`shared/release/release.py`, XML surgery only). It collapses
  Version Control to one row and moves the history to `_audit/`, moves own references
  to the package version, and strips build tags, review ids, stamps and internal
  references (country rules in `_release/release_rules.json`). It then sets the package
  metadata and removes customXml and custom properties.
- Blocking check C47: `release_crosscheck.py` must report 0 findings, and
  `open_check.ps1` must open every file in Word / Excel without repair.
- On the FR finals copy: 2,544 findings → 0, and 20/20 files open cleanly.
- `REPORT_SPEC_STANDARD_FORMAT.md` now specifies ONE Version Control row.

---

## F48 — Reporting code taken by analogy, not from the authority's code table (v2.12, from proposal F48)

**Source:** France validation, WTC F-02/F-03: Agirc-Arrco declared with code 105 (valid only to regularise periods before 2025) instead of 131 / 132; ticket catalogue F48 (official layout never diffed). Approved on 17 Oct 2026 only as far as the coverage-matrix fix needs it.
**Observed:** The WTC "Tax Code" column carried a contribution code that exists, but not for the build year.
**Root cause:** No code table of the authority was saved, so nothing could compare the code with its period of validity.
**Mitigation:** Blocking check **C48** (`shared/content-checks/content_checks.py`): every reporting code of `_research/WTC-crosswalk.json` exists in `00-official-sources/code-tables/*.json` for the whole build year, and the WTC row carries it. No code table is a FAIL unless `validation_exemptions.C48` is recorded.

---

## F49 — Wage-type code cited that the WTC does not have (v2.12, from proposal F49)

**Source:** France Payslip F-29 (payslip codes not matching the WTC); tickets SR-82/85/342/415, HRBS-10563. Approved on 17 Oct 2026 as far as gap P0-2 needs it.
**Observed:** Payslip, DD and specs cited wage-type codes independently of the catalogue.
**Root cause:** No cross-check from the citing artifact back to the WTC.
**Mitigation:** Blocking check **C49**: every code cited as "<code> - <label>" or "WT <code>" in the CCG, DD, specs or payslip exists in the WTC. Labels are not compared (the payslip prints a short legal label; comparing them gave 27 false positives on France).

---

## F50 — Tax / contribution flag or side without a legal basis (v2.12, from proposal F50)

**Source:** France: CDS 0.016 % written for both sides in dozens of boilerplate cells (S1, CCG F-02 / WTC F-04); employer Agirc-Arrco flagged subject to CSG while FR-046 said no (WTC F-07); work-accident benefit "fully taxable" in the WTC while the CCG said 50 % (Test 0 F1). Ticket patterns HRBS-12181/14331/12483/12072. Approved on 17 Oct 2026 as far as gap P0-2 needs it.
**Root cause:** Flags were typed cell by cell; nothing tied a flag to a legal basis or the WTC to one source.
**Mitigation:** The WTC is built from `_research/WTC-crosswalk.json` (artifact-builder, Stage 5). Blocking check **C50**: every WTC flag equals the crosswalk; every flag has a `basis` that is a register id; the side (EE / ER / BOTH / NONE) agrees with the category and the explanation; "fully taxable" is never written against a partial or exempt flag.

---

## F53 — SIR direction or identity wrong (v2.12, from proposal F53)

**Source:** France SIR-01..09: FR-URSSAF-002 described as outbound (it is the inbound CRM), "FR-SIR-001" written inside FR-SIR-INDEX-001, a spec id (FR-CNAM-001) that does not exist. Tickets SR-80/432, HRBS-12839. Approved on 17 Oct 2026 as far as gap P2-13 needs it.
**Mitigation:** Blocking check **C53**: the SIR "Document ID" equals the file id; every spec appears in a SIR row whose direction agrees with the spec's Report Type (and with `scope_manifest` `direction` when given); a spec named in the SIR exists.

---

## F56 — Mandatory spec field with no data source (v2.12, from proposal F56)

**Source:** France SD-02 / SA-05: the OPS identifier and the collecting-body SIRET "produced by the payroll calculation" (they are master data); 264 false "NO DD COUNTERPART" notes. Tickets SR-414, HRBS-13389/15216. Approved on 17 Oct 2026 as far as gap P1-8 needs it.
**Root cause:** `guards.missing_sources` existed since v2.11 but was never called, and was not calibrated.
**Mitigation:** Blocking check **C56**: a mandatory or conditional field is never "produced by the payroll calculation" / "no DD counterpart" without a System Mapping, and it has a System Mapping or a cited source.

---

## F57 — Payslip without its legal items, or a layout change that drops them (v2.12, from proposal F57)

**Source:** France Payslip F-25..F-28 (three S1): a visual realignment deleted 8 statutory lines and shifted formulas (net overstated by about EUR 400); R3243-1 items missing; a meal benefit added to gross and never deducted. Tickets SR-340, HRBS-12472/13757. Approved on 17 Oct 2026 as far as gap P0-3 needs it.
**Root cause:** Only the sheet structure was checked (C21 / C26); the payslip was not even sampled by Test 0.
**Mitigation:** The builder writes `_research/PSL-legal-items.json` (items of the payslip statute, each with a register id, and the net-pay reconciliation). Blocking check **C57**: every legal item and every crosswalk wage type with `payslip: true` is on the payslip; the net reconciles to the cent; a benefit in kind is added and deducted. Stage 10 Test 0 now samples PSL.

---

## F67 — Facts file with nothing bound to it (v2.12 NEW)

**Source:** France coverage matrix of 17 Oct 2026, gap P0-1. C46 and C32 passed France with 0 `[[FACT:]]` tags, so the Apec cap (wrong "in agreement" in CCG, WTC and skill), CDS on both sides, the 7,500 overtime cap written three ways and the "three years' pay" text left in WTC / DD were all invisible to the consistency checks.
**Root cause:** The binding rule existed only as an instruction; the check treated "no tag" as a note.
**Mitigation:** **C46** reinforced: 0 tags is a FAIL, and every distinctive occurrence of a fact value written without its tag is a FAIL (binding below 100 %). C32 with 0 tags is a FAIL. On France: 0 tags, 4,261 untagged fact values.

---

## F68 — Validation check skipped silently for lack of country support (v2.12 NEW)

**Source:** Matrix gap P0-4. Only France has a norm file, an authority validator and an identifier plugin; for any other country C34 and C35 returned SKIP and C36 checked IBAN / RF only, and a SKIP did not stop Stage 9.
**Mitigation:** `spec_checks.py`: a SKIP of C34 / C35 / C36 for a missing norm, validator or plugin is a FAIL unless `validation_exemptions.<check>` (reason, official source URL, decided_on) is recorded in the build manifest (contract 1.4.0). The same rule applies to C48, C50, C57 and C71. The fixer may not write an exemption itself. C38 with no worked-example table at all now exits 1 too.

---

## F69 — Oracle suite that does not exercise the research (v2.12 NEW)

**Source:** Matrix gap P0-4 / L-C. In France the defects were caught only where a case happened to exist (CDD, non-resident, AT/MP, above 4 PMSS). The `official_examples` reference path had never run.
**Mitigation:** Blocking check **C69** (`validation-suite-template/suite_coverage_check.py`): every answered coverage row and every CCG worked example maps to a suite case (`rules.json` `test_cases.<id>.coverage`); official examples carry a source URL; an engine defect needs test cases and a primary source. The `official_examples` path now has a passing and a failing test.

---

## F70 — Citation not read, repealed, or a source gap that is not one (v2.12 NEW)

**Source:** France D-08 (FNAL on the repealed CSS L834-1, 4 times), CCG F-06 / F-25 / F-26 / F-28 (wrong decree, wrong articles); SA-25 / SB-05 (DPAE guide and CRM PAS declared "not obtained" while another artifact of the build had them).
**Mitigation:** Blocking check **C70**: every article / instrument cited in the deliverables is in the legal-basis register; no register row marked repealed / withdrawn is cited; every "not obtained / not retrievable" statement carries `[[GAP:id]]` recorded in `_research/gaps.json` with the sources searched, and no gap is already answered by the register or a SIR document.

---

## F71 — Issued binary that the build script does not produce (v2.12 NEW)

**Source:** France: corrections typed into the issued .xlsx, undone by every regeneration; one hand patch introduced an S1 (SB-19). On the FR dossier the rebuild still differs from the issued specs (leftover "countries built so far", "FR-DD-001 v1.1" citations, Version Control), because the clean-up was done on the binary.
**Mitigation:** Blocking check **C71** (`spec-builder/regen_check.py`): Stage 9 rebuilds the specs into a temp folder with `spec_checks.json` `build_command` and compares them cell for cell; no build command is a FAIL unless exempted.

---

## F72 — Change of a value during the year, or a bulletin, not captured (v2.12 NEW)

**Source:** France CCG F-16 (BOSS section of 24 Jul 2026 missed), F-18 (DSN norm CT2027.1.2 not anticipated), F-24 (minimum protected amount without "from 1 April 2026"), net social 2026 / 2027.
**Mitigation:** **C41** reinforced: one bulletin sweep per authority of the register; a `next_year` entry (published norm / rates of the following year); every fact whose `effective_from` falls inside the build year has its date written in the CCG or the design.
**Superseded values (owner decision of 17 Oct 2026).** A fact whose `effective_to` is already past is not a C41 problem when it ends on or after 1 January of the build year and a successor fact starts the next day: the old value still governs the pay periods inside its validity, and any later correction of those periods. Primary source (read on the BOSS page saved in `FR-compliance/00-official-sources/_fetched-2026-10-09/boss-assiette.md`, Bulletin officiel de la sécurité sociale, *Assiette générale*, chapter on the rattachement principle): §490 "La législation applicable (afin notamment de déterminer l'assiette, le taux, le plafonnement, les exonérations et exemptions applicables aux rémunérations versées) est donc celle en vigueur au cours de la période au titre de laquelle ces rémunérations sont dues" (reference texts CSS L.136-1, L.242-1, R.242-1); §530 "les cotisations et contributions sont calculées en tenant compte des règles d'assiette, de taux, de plafonnement, d'exonération et d'exemption en vigueur lors de la période de travail à laquelle ces éléments de rémunération se rapportent". For income tax, BOI-BAREME-000037 gives the two grids "à compter du 1er mai 2025" and "à compter du 1er mai 2026" (pages saved in the same folder), so the 2025 grid governs January-April 2026. This is the French rule; another country needs its own source before the same reading is relied on.

---

## F73 — Promoted files, skill or Drive copy drifting from the issued package (v2.12 NEW)

**Source:** France: finals changed after promotion (49 inconsistencies), skill references whose source hash nobody checked, a Drive DD older than the pipeline (DD F-36). On the FR dossier, 21 promoted files no longer have the MD5 recorded in PROMOTION-LOG-2026-10-09.md (they equal the current validation `final/`, so the log, not the content, is out of date).
**Mitigation:** `shared/release/promote.py` (archive, copy, MD5 log, byte-for-byte verification; `--log-only` for the Stage 13 package) and blocking check **C73** (`promotion_check.py`, Stage 13): every promoted file still has its logged MD5, every skill provenance row matches its source, and (`DRIVE_DIR`) the Drive copy is the same bytes.

---

## F74 — Design parameter in the wrong unit, or read before it is produced (v2.12 NEW)

**Source:** France design v1.0: 52577 = 0.49 for 0.49 percentage points (R-05); a formula reading an account produced later in the sequence.
**Mitigation:** **C45** reinforced: a parameter whose row states "<v> %" while the value is <v>, or a "rate" parameter above 1 without a % sign, is a FAIL; a regulation that reads an account produced only by a later regulation of the Part 3 sequence is a FAIL. A formula that contradicts its own text (R-44) is not mechanically detectable; it stays with C37 / C69.

---

## Log change history

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 16 Apr 2026 | Wallisson Gomes | Initial — F1-F4 from Bulgaria |
| 1.1 | 8 May 2026 | Wallisson Gomes | F5-F6 from Bulgaria handover review |
| 1.2 | 14 May 2026 | Wallisson Gomes | F7-F8 from Spain SR-80 review |
| 2.4 | 23 May 2026 | Wallisson Gomes | F9-F15 from HU-GAP-001 (Manju Shetija) |
| 2.5 | 27 May 2026 | Wallisson Gomes | F16-F22 from Egypt pipeline run (Manju Shetija) |
| 2.5 BUG | 27 May 2026 | Wallisson Gomes | F23 from Chad v2.5 first run |
| 2.5 | Jul 2026 | Wallisson Gomes | F24-F28 from Canada external design review / cross-checks |
| 2.9 | 17 Aug 2026 | compliance-qa-auditor | F29-F31 from Belgium Stage 10 cross-artifact check |
| 2.9 | 2 Sep 2026 | Wallisson Gomes | F32-F34 from FR-ALIGN-001 (France DD↔Spec manual reconciliation) |
| 2.9 | 9-10 Sep 2026 | Wallisson Gomes | F35-F39 from the France artifact-owner review (row added 7 Oct 2026; entries were already in the log) |
| 2.11 | 7 Oct 2026 | Wallisson Gomes | F40 from the France validation (improvement programme Phase 1, root cause RC3; checks C34-C36) |
| 2.11 | 7 Oct 2026 | Wallisson Gomes | F41-F42 from the France validation (improvement programme Phase 2, root causes RC1/RC6/RC8; checks C37-C39) |
| 2.11 | 7 Oct 2026 | Wallisson Gomes | F43-F44 from the France validation (improvement programme Phase 3, root causes RC1/RC2; checks C40-C41, adversarial review in contract 1.2.0) |
| 2.11 | 7 Oct 2026 | Wallisson Gomes | F45-F47 from the France validation (improvement programme Phases 4-5, root causes RC4/RC5/RC7; checks C42-C47). RC1-RC8 now each have an entry: F40 (RC3), F41 (RC1/RC6), F42 (RC8), F43 (RC2), F44 (RC1), F45 (RC4), F46 (RC5), F47 (RC7) |
| 2.12 | 17 Oct 2026 | Wallisson Gomes | France coverage matrix (the France coverage matrix of 17 Oct 2026 (internal review)), gaps P0-P2: F48, F49, F50, F53, F56, F57 taken from the ticket-catalogue proposals only as far as these fixes need them (F51, F52, F54, F55, F58-F66 still wait for a decision; F58 and F65 enter only as C40 rows); new F67-F74. New checks C48, C49, C50, C53, C56, C57, C69, C70, C71, C73; reinforced C38, C40, C41, C45, C46, C27, C31, C32 and the C34-C36 SKIP rule |

**Note (2 Sep 2026):** This table's position was corrected today — it had been
sitting mid-document since the F23 addition (27 May 2026), so F23 through F31
were never logged here despite being present in the body above. This gap is
itself an instance of the pattern F24 describes: no discipline required this
table to move or grow the same day the entries below it did. The header
"Version: v2.5" at the top of this document was left unchanged pending
confirmation of whether it tracks this document's own version or the pipeline
script version active when each entry was written — those two counters appear
to have diverged after 27 May 2026 and a real decision is needed before either
is bumped again.
