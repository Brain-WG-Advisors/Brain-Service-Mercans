# Colombia COUNTRY CONFIGURATION GUIDE — v2.4 TEMPLATE FORMAT

You are building the Colombia Country Configuration Guide using the OFFICIAL
Mercans CCG template. The output MUST follow the template's question-by-question
structure exactly, with every question appearing as an H3 heading and the answer
immediately below.

## CRITICAL — v2.4 FORMAT REQUIREMENTS

The Mercans CCG template has 13 Modules with sub-sections (1.1, 1.2, ...) and
approximately 96-150 specific questions. Each question MUST appear in your output
as an `### H3 heading` with the answer below.

This is a HARD requirement. The downstream auditor (Check C11) will count H3
headings against the template question list and FAIL the build if coverage is
below 95%.

## MANDATORY INPUTS

### v2.5 — USE THE NEWEST APPLICABLE LAW AS PRIMARY SOURCE (C2)

When researching Colombia payroll rules, you MUST:
1. Identify the CURRENT labour code / income tax law / social security law in force
   for 2026 (often this is a NEW law that has replaced an older one — e.g.,
   Egypt Labour Law 14/2025 replaced the old Law 12/2003).
2. Use the newest law as your primary source for: leave entitlements (maternity,
   annual, sick), severance, working hours, overtime rates, minimum wage.
3. EXPLICITLY FLAG any reference to a superseded/replaced law in your output.
   If a source PDF or web result cites the old law, do NOT use those values.
4. When in doubt, search: "Colombia new labour code 2026" /
   "Colombia labour law amendments 2026".
5. Filing mechanics (C4 — v2.7 CORRECTED): do NOT assume filings are separate.
   Whether wage taxes file as SEPARATE submissions or as ONE CONSOLIDATED grid
   is a research question — some portal/CEMAC regimes consolidate all salary
   taxes on a single monthly retenues grid (e.g. Cameroon DGI), others keep them
   separate. Determine the real answer for Colombia from the official portal /
   primary source and document it (with the source). Model accordingly.

### Failure pattern reference

This run must avoid F1-F22 documented in country_failure_log.md.
F16-F22 are Egypt failures (May 2026); pay particular attention to:
- F18: stale law references (use Law 14/2025 not Law 12/2003 type errors)
- F19: HR-scope reports incorrectly included (descope reports needing
       headcount-by-qualification or nationality data — flag as HR scope, C1)
- F20: WTC tax codes not from the country's defined legend (C3)
- F21: Annual/quarterly/monthly filing mechanics misunderstood (C4)

### Standard inputs

1. **Master template (read first, end-to-end):**
   ~/mercans-pipeline/shared/CCG_TEMPLATE_QUESTIONS.md
   This is the master list of all questions across 13 Modules. Every question
   here MUST appear as an H3 heading in your output.

2. **Gold standard reference (study before drafting):**
   ~/mercans-pipeline/shared/REFERENCE_CCG_Bulgaria.docx
   Bulgaria CCG follows the template format exactly. Use it as your structural
   model. Open it with python-docx, study how questions become H3 headings, how
   tables are used for quantitative data, how legal citations are placed.

3. **Failure prevention log:**
   ~/mercans-pipeline/shared/country_failure_log.md
   Read F1-F15. Specifically prevent F9 (thin schemas), F10 (missing sub-forms),
   F15 (artifact removal without descoping decision).

4. **Source PDFs (if available):**
   ~/mercans-pipeline/CO-compliance/00-official-sources/pdfs/
   Use pdfplumber to extract. Cite the specific article/section in your answers.

## 13 MODULES (do NOT merge, rename, split, or reorder)

- Module 1: Foundational Jurisdictional Parameters
- Module 2: Master Data Configuration
- Module 3: The Gross-to-Net Calculation Framework
- Module 4: Gross Compensation
- Module 5: Social Security & Pension Systems
- Module 6: Income Tax Withholding System
- Module 7: Deductions, Exemptions & Benefits
- Module 8: Statutory Leave Management
- Module 9: Termination & Irregular Payments
- Module 10: Reporting, Compliance & Finalisation
- Module 11: Advanced Scenarios & Cross-Cutting Logic
- Module 12: Gross-to-Net Worked Examples
- Module 13: Common Business Practices & Non-Statutory Rules

## STRUCTURE — mirror Bulgaria exactly

```
# Module 1: Foundational Jurisdictional Parameters

## 1.1 Fiscal, Currency, and Language

### What is the statutory tax year?

[Plain-prose answer with citation, e.g., "The statutory tax year in Colombia
runs from 1 January to 31 December (Income Tax Act Art. X)."]

### Can employers adopt an alternate tax year?

[Answer.]

### What is the official currency for payroll processing and reporting? Provide ISO code.

[Answer with COP as the ISO code and any relevant detail.]

[... continues for every question in the template ...]

*Legal basis: [List the laws/articles cited in this sub-section]*

## 1.2 Pay Cycles and Dates
[Same pattern.]
```

## RULES

1. **Use the question text verbatim** as the H3 heading. Do NOT paraphrase. If
   the template says "What is the statutory tax year?", use that exact text.

2. **Answer every question.** If genuinely not applicable to Colombia, write
   "Not Applicable — [brief reason in 1-2 sentences]."

3. **Tables for quantitative data.** Tax brackets, SS rates, ceilings, thresholds
   must be tabular. No long bullet lists for numerical data.

4. **Cite sources.** Every rate, threshold, or rule must have a citation either
   inline or in the legal basis block at the end of each sub-section.

5. **Worked examples in Modules 3-9, 11-13** must be step-by-step with every
   line of calculation shown using actual 2026 numbers in COP.

6. **Dev-team filtering rules:**
   - Module 2: concise field summaries + reference to DD. Do NOT reproduce DD
     field tables.
   - Module 10: summary table + reference to Report Specs. Do NOT reproduce
     field-level spec content.
   - Module 1.4 (Holidays): simple date table only. No admin workflows.

7. **Plain business language, not jargon.**
   WRONG: "Contributions at rate X% BASE_SS_ER applied to MIN_INS_INCOME-capped earnings."
   RIGHT: "Employer SS is X% of insurable earnings capped at [max] for 2026.
           Example: an employee earning [amount] pays [result]."

## SCOPE MANIFEST — REQUIRED OUTPUT (S3 v2.5)

After completing the CCG body, produce `scope_manifest.json` at:
~/mercans-pipeline/CO-compliance/scope_manifest.json

Load and follow this template EXACTLY:
~/mercans-pipeline/shared/scope_manifest_template.json

CRITICAL — use the EXACT field names from the template (S3 fix):
- For descoped filings: use `"descoping_reason"` (NOT "reason")
- For `integrations.inbound`: use an ARRAY of OBJECTS, NOT a plain string
  Example: `"inbound": [{"id": "X", "from": "Y", "format": "Z"}]`
  NOT: `"inbound": "X"`
- For `product_mapping_required`: must be `true` or `false` (boolean),
  not the string "true"/"false" and not null.
- For HR-scope reports requiring headcount/qualification/nationality data
  beyond payroll (C1): include in `authority_filings.out_of_scope` with
  `"descoping_reason": "HR-scope — requires data beyond payroll system"`
  and `"client_impact": "Refer to HRMS team"`. Do NOT include such reports
  in `in_scope`.

Use this exact structure:

```json
{
  "country": "Colombia",
  "code": "CO",
  "currency": "COP",
  "year": "2026",
  "generated": "<ISO datetime>",
  "employment_types": {
    "in_scope": [<list>],
    "out_of_scope": [<list>],
    "rationale": "<reasoning>"
  },
  "authority_filings": {
    "in_scope": [
      {
        "filing_id": "<id>",
        "authority": "<name>",
        "frequency": "<monthly/annual/etc>",
        "format": "<XML/CSV/TXT/XLSX>",
        "integration_type": "<inbound/outbound/both>",
        "product_mapping_required": <true/false with rationale>
      }
    ],
    "out_of_scope": [
      {"filing_id": "<id>", "descoping_reason": "<reason>", "client_impact": "<assessment>"}
    ]
  },
  "wage_type_categories": {<in_scope/out_of_scope buckets>},
  "option_mapper_scope": {<in_scope/out_of_scope codes per mapper>},
  "integrations": {
    "outbound": [<list>],
    "inbound": [<list>],
    "both": [<list>]
  },
  "known_failure_patterns_to_check": ["F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","F11","F12","F13","F14","F15","F16","F17","F18","F19","F20","F21","F22"]
}
```

## SOURCES (read in priority order)

1. Source PDFs (if any): ~/mercans-pipeline/CO-compliance/00-official-sources/pdfs/
2. Web research: "Colombia income tax 2026", "Colombia social security 2026",
   "Colombia payroll regulations 2026", "Colombia labor code 2026"
3. Government sources only (tax authority, social security, labor ministry,
   official gazette). Avoid blogs, accounting firm marketing pages.

## BUILD APPROACH

1. Read CCG_TEMPLATE_QUESTIONS.md end-to-end. Count the questions per module.
2. Read REFERENCE_CCG_Bulgaria.docx via python-docx, study the structure.
3. For each Module, draft answers to every question. Save as 13 markdown files:
   ~/mercans-pipeline/CO-compliance/01-ccg/modules/m01_foundational.md
   m02_master_data.md, m03_g2n.md, m04_compensation.md, m05_social_security.md,
   m06_tax.md, m07_deductions.md, m08_leave.md, m09_termination.md,
   m10_reporting.md, m11_advanced.md, m12_examples.md, m13_practices.md
4. Assemble the 13 modules into a single Word document using python-docx:
   - Arial 11pt body, 14pt H1, 12pt H2, 11pt H3 (bold)
   - Title page: "Colombia Country Configuration Guide — CO-CCG-001 v1.0"
   - TOC on page 2 (use docx TOC field)
   - Page breaks between Modules
   - Footer: "CO-CCG-001 v1.0 | Mercans Compliance Regulations Team | 2026"
   - Save as: ~/mercans-pipeline/CO-compliance/01-ccg/CO-CCG-001-v1.0.docx

## SELF-CHECK BEFORE SAVING

```python
from docx import Document
doc = Document('/Users/wallissongomes/mercans-pipeline/CO-compliance/01-ccg/CO-CCG-001-v1.0.docx')
h3s = [p.text for p in doc.paragraphs if p.style.name in ('Heading 3', 'Heading3')]
print(f"H3 count: {len(h3s)}")
# Expected: 90+ (matches template question count). If < 90, you've missed questions.
```

If H3 count is below 90, re-read CCG_TEMPLATE_QUESTIONS.md and add the missing
H3 headings before saving the final docx.

## REPORT BACK

When complete, report:
- H3 heading count
- Any questions marked "Not Applicable" with their reasons
- scope_manifest.json location confirmed
- Final docx size

=== v2.8 CROSS-CUTTING RESEARCH CONTROLS (Enaakshi B1/B2/B4/B7 — mandatory) ===
B1 RESIDENT vs NON-RESIDENT MATRIX: in the income-tax module, BEFORE writing prose,
   build a table with one row per income type (regular salary, annual/13th bonus,
   severance, equity / share incentives, labour-service or contractor pay, benefits in
   kind) and TWO explicit columns — RESIDENT and NON-RESIDENT — giving the rate, method
   and base for each. An empty non-resident cell is a BLOCKING gap, not an omission:
   fill it from primary law, or write "non-resident: not in scope" with the reason. The
   audit (C31) checks a non-resident treatment is present.
B2 ONE-CALIBER WAGE RULE: if any social-security ceiling, floor or cap derives from a
   published "average wage", list EVERY average-wage figure the country publishes and
   name its caliber (e.g. full-caliber vs on-post-staff vs employed-persons). For every
   parameter that depends on it (SI ceiling, housing/HPF ceiling, severance cap) declare
   which caliber it uses, then reconcile. Where a ceiling can be reproduced from a wage
   figure (e.g. ceiling = 3 x average wage / 12), record that derivation as the proof of
   caliber. Never mix calibers across sections.
B4 CITATION-TO-ARTICLE VALIDATION: every cited statute article must actually say what the
   sentence claims; if the same statute is cited in two places for the same rule, the
   article numbers MUST agree. Build the fetched statute article map once and self-check
   before finalising.
B7 SCOPE DECISIONS ARE FIRST-CLASS AND REVERSIBLE: for every in / out-of-scope call,
   record (a) what is in, (b) what is explicitly owned upstream (plan administrator,
   client, authority), (c) the inbound data contract it implies (which fields the engine
   must receive), so a later reversal is a contained edit, not a four-file hunt.
B10 ENGLISH-ONLY PROSE (CCG): the ENTIRE narrative of this CCG must be written in
   English. Every heading, sentence, table cell, worked example, note and caption is
   English. This is a reader-facing compliance document for a global audience — no
   passages, phrases or stray words in Spanish (or any non-English language) may
   appear in the prose. The ONLY permitted non-English text is a statutory/legal term
   of art cited for traceability, and it MUST be handled as: English wording first,
   with the original term immediately after in parentheses on FIRST use only, e.g.
   "professional expenses (frais professionnels)", "the employer wage tax (Taxe
   Forfaitaire Employeur, TFE)". After first use, use the English term (or the
   established abbreviation) alone. Do NOT drop into Spanish for a whole sentence,
   bullet, or table cell. Names of authorities/forms/statutes may keep their official
   proper name (e.g. "Direction Générale des Impôts (DGI)") — that is a proper noun,
   not prose. NOTE: this English-only rule applies to the CCG's PROSE only; it does NOT
   apply to the DD, WTC or Payslip, which carry DEDICATED local-language fields/sheets
   by design (Name Local (Spanish) columns, the "Colombia (ES)"
   payslip sheet) — those local-language fields are correct and required.
=== end v2.8 controls ===
