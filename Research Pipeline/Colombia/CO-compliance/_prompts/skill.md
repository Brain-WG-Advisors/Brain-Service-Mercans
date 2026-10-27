# Colombia COMPLIANCE SKILL — GENERATOR (router pattern, v2.7)

You are generating a Mercans payroll-compliance skill for Colombia, in the
Chile "progressive-disclosure router" pattern: a THIN SKILL.md that routes to
one FULL reference file per artifact. It is uploaded to claude.ai and used by
compliance analysts. Faithful, COMPLETE content is the priority — do NOT
summarize.

## STEP 0 — REUSE STAGE 10'S ALREADY-EXTRACTED TEXT DUMPS IF PRESENT

Check ~/mercans-pipeline/CO-compliance/07-qa-crosscheck/_work/ FIRST. The
QA Cross-Check stage that just ran typically leaves plain-text dumps of every
artifact there (ccg.txt, wtc.txt, dd.txt, spec_*.txt, payslip.txt, sir.txt,
gwtc.txt) — read those directly instead of re-opening and re-parsing the
source .docx/.xlsx files yourself. They are current (produced this same
pipeline run) and reading plain text is far cheaper than re-parsing binary
files field-by-field. Only fall back to reading a source artifact directly if
its dump is missing from that folder. A prior attempt at this exact stage
spent its entire turn budget reading and produced no output file at all —
reusing the dumps is what leaves room to actually write the skill this time.

## STEP 1 — READ ALL SOURCE ARTIFACTS (use the LATEST version present)
In each folder, read the HIGHEST version number present (e.g. v1.2 over v1.0).
Do NOT assume a specific version in the filename — list the folder and pick the
newest. Read EVERY sheet of every workbook.
  CCG:          ~/mercans-pipeline/CO-compliance/01-ccg/                          (CO-CCG-001-*.docx)
  WTC:          ~/mercans-pipeline/CO-compliance/02-wtc/                          (CO-WTC-001-*.xlsx)
  SIR:          ~/mercans-pipeline/CO-compliance/03-statutory-integrations/       (CO-SIR-001-*.docx)
  Report Specs: ~/mercans-pipeline/CO-compliance/04-reports-spec/                 (EVERY *-Spec.xlsx)
  DD:           ~/mercans-pipeline/CO-compliance/05-data-dictionary/              (CO-DD-001-*.xlsx)
  Payslip:      ~/mercans-pipeline/CO-compliance/06-payslip/                      (CO_Compliance_Payslip_Generator.xlsx)
  QA Report:    ~/mercans-pipeline/CO-compliance/07-qa-crosscheck/CO-QA-REPORT.md

## STEP 2 — WRITE ONE FULL REFERENCE FILE PER ARTIFACT
Create these in ~/mercans-pipeline/CO-compliance/08-skill/co-compliance/references/ :
  01-ccg.md             - the ENTIRE CCG: every section, rate, table, bracket,
                          and leave / overtime / termination rule, with all legal
                          citations. Verbatim values.
  02-wtc.md             - the ENTIRE wage type catalogue: one row per wage type
                          (code, name, type, tax and SS treatment, accumulators),
                          rendered as markdown tables. Every code, no omissions.
  03-sir.md             - the ENTIRE statutory-integration research: each
                          institution, portal, channel, authentication, file
                          format, and inbound / outbound feed.
  04-reports-spec.md    - for EACH report spec: the report matrix, every field
                          row (format, mandatory / optional, system mapping),
                          filing rules, the verified submission channel / portal,
                          and the file structure.
  05-data-dictionary.md - the ENTIRE DD: every field (ID information, country
                          fields, option mappers) with format,
                          mandatory / conditional, and valid values.
  06-payslip.md         - payslip mandatory content plus the full field / line
                          list and the local-language labels from the generator.
  07-qa-report.md       - the ENTIRE QA report: open items, TBC / VERIFY flags,
                          known limitations, and accuracy notes.

RULES for the reference files:
- COMPLETE, never summarized. Dump every rate, row, code and citation verbatim.
  Each reference file must be at least as detailed as its source artifact.
- Preserve exact numbers, COP amounts, percentages, and legal citations
  (article / decree). Never round.
- Preserve local-language terminology (French for Colombia); translate inline
  only where it aids clarity.
- Use markdown tables for tabular data (WTC, DD, spec field lists, rate tables).
- Keep every item flagged TBC / [VERIFY WITH RA] from the QA report.

## STEP 3 — WRITE THE THIN ROUTER SKILL.md
Create ~/mercans-pipeline/CO-compliance/08-skill/co-compliance/SKILL.md.
It must be SHORT (a router, not a content dump) and contain:

1. YAML front-matter between --- lines:
     name: co-compliance
     description: a one-line description naming Colombia (CO), the tax
     authority, the social-security body, currency COP, the key
     statutory reports, and payslip rules.

2. A one-paragraph intro: you are an expert on Colombia payroll compliance for
   fiscal year 2026; the complete reference set lives in references/; ALWAYS
   use the Read tool on the relevant reference file BEFORE answering; do NOT
   answer Colombia-specific rates or rules from general knowledge.

3. A "Routing — read the right file FIRST" section. For each topic, give an arrow
   to the file to read. Map at least:
     - income tax (brackets, withholding, reliefs)        -> references/01-ccg.md
     - social security (rates, ceilings, contributions)   -> references/01-ccg.md
     - gross-to-net worked examples                       -> references/01-ccg.md
     - leave and public holidays                          -> references/01-ccg.md
     - termination, notice, severance                     -> references/01-ccg.md
     - wage type / earning-deduction codes, tax treatment -> references/02-wtc.md
     - government integrations, portals, file formats     -> references/03-sir.md
     - statutory report field specs, deadlines, structure -> references/04-reports-spec.md
     - master data fields, mandatory vs conditional       -> references/05-data-dictionary.md
     - payslip mandatory content                          -> references/06-payslip.md
     - known limitations / TBC / QA findings              -> references/07-qa-report.md
   Wrap every file path in backticks in the SKILL.md you write.

4. A "How to answer" section: identify the reference file(s); Read them BEFORE
   drafting; quote rates / thresholds / citations verbatim (no rounding); cite
   the legal basis; preserve French terminology; for values that change over time
   (SMIG, CNPS ceiling, brackets) flag reverification against the official source;
   if a question is not covered, say so and point to the authority (DGI for tax,
   CNPS for social security).

5. A "Scope and limits" section: Colombia only, fiscal year 2026,
   private-sector employers; for other countries use that country's skill.

Model the tone and layout on the Chile skill — a thin router that always defers
to references/. Keep SKILL.md well under ~12 KB.

## QUALITY BAR
- The value lives in references/ being COMPLETE and verbatim; SKILL.md only
  routes. If a reader asks "give me the CCG", the agent will Read 01-ccg.md and
  reproduce the full content — so 01-ccg.md must actually contain all of it.
- All amounts in COP; fiscal year 2026.
- Flag uncertainty with [VERIFY WITH RA]; cross-check every rate against the QA report.
