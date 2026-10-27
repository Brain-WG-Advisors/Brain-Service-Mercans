# CLAUDE.md — Colombia (PMI): cross-check of report specs against the client's real reports

## Why this exists
Mercans is redesigning HR Blizz so the PMI Colombia payroll can run in the system. The BAU team prepares several reports MANUALLY today. A report SPEC is the mapping of a report: it tells the development team, field by field, what goes where so the system can generate that report. The most important column of a spec is **Field Explanation** — what goes in the field, from which payroll data, under which rule. This project checks that our 6 specs match the reality of the reports the client actually produces, in fields, field explanations and formats. Design completion is 31 Oct 2026; deltas go to Mohit's team before then.

Three statutory report families are mandatory in Colombia: income tax (withholding — Formulario 350, Formulario 220, Formato 2276), social security (PILA, cesantías) and Nómina Electrónica. Everything else the client produces is a client/operational report: record it, do not force it into a statutory spec (scope agreed 15 Oct 2026).

State of the work lives in `HANDOFF-2026-10-21.md` (latest: Windows resume, client answers of 21 Oct, round 5 tasks in section 5), `HANDOFF-2026-10-16.md` (decisions in force, section 3), this file and the latest `04-output/OPEN-POINTS-<date>.md` — not in the conversation. Since 21 Oct 2026 the kit runs on Windows inside the brain-service (`Research Pipeline/Colombia/co-report-crosscheck`): use `python`, not `python3`.

## Folders
| Folder / file | Content | Who reads it |
|---|---|---|
| `01-specs/` | Spec inputs used for the cross-check (do not edit) | agents |
| `02-client-reports-raw/` | The client's reports AS RECEIVED — contain personal data | **never read by Claude** (denied in `.claude/settings.json`) |
| `03-client-reports-masked/` (+ `round2/`, `round3/`) | Masked copies produced locally by `scripts/mask_reports.py` (round 1), `mask_round2.py`, `mask_round3.py`; the only client data agents may read | agents |
| `02-specs-out/` | Intermediate DRAFT v1.1 files (history only) | agents (read-only) |
| `05-final/` | **The 6 deliverable specs**, clean initial versions, same names as in Drive "17 - Statutory Report"; previous copies in `05-final/_previous/` | agents |
| `04-output/` | Profiles, mappings, findings, change maps, `OPEN-POINTS-<date>.md` (internal tracker, never sent to development), `round2/`, `round3/`, `final-prep/` (maps applied onto the finals) | agents |
| `99-local-only/` | Masking key (raw value → token). Delete or secure when the project ends | **never read by Claude** |

## Non-negotiable rules
1. **PII:** Claude never opens anything in `02-client-reports-raw/` or `99-local-only/`. Only masked copies are analysed. If a masked file still shows a person's name, ID, account, e-mail, phone or address, STOP and tell Wallisson which file and column.
2. **Primary source decides the law; the client's report shows the reality.** A client report is evidence of what data is produced and how it is labelled today — not proof of the legal rule. Where the client report and the spec disagree on a statutory rule, record it as a CONFLICT and cite the official source the spec relies on; never "fix" a spec to match the client without that check.
3. **Specs change only through change maps.** A cross-check writes proposed change maps in `04-output/`; a change is applied onto `05-final/` only when an official source (annex, law, instruction guide) or a decision of Wallisson's supports it and an independent verifier has confirmed it, through `04-output/final-prep/<SPEC>-<map>.json` and `scripts/make_final.py <SPEC> --on-final --map <map>` (previous copy kept in `05-final/_previous/`, checks run automatically). Everything else stays PROPOSED for Wallisson's approval.
4. **Never invent** a column, a code, a field or a mapping. If the evidence is not in a masked report or in the spec, the verdict is "Not evidenced".
5. English in every file; talk to Wallisson in Brazilian Portuguese.

## Standards (apply to every change — from HANDOFF-2026-10-16, which wins where it conflicts with this file)

**Specs that go to development**
- Issued as the initial version: Version Control has one line only — `1.0 | <date> | Initial version. | Approved | Wallisson Gomes` — until development has received them. After hand-over, normal versioning resumes (one sentence per change).
- Columns T ("Query to RA") and U ("RA Comments") on the spec sheet are for development's questions and our answers only. We never fill them ourselves.
- No review or process language anywhere ("corrected", "revised", "review", "verified", "cross-check", "round", "DRAFT", "previously", "pending", "rule to be set", comparisons with an earlier version, remarks about the client's own files). Each explanation states the rule as it is, with its legal source.
- No internal references (scope_manifest, CO-GAP-xx, CCG control cells).
- Anything without a defined rule stays out of the spec and goes to OPEN-POINTS.
- After every edit: diff, zero formula cells, zero masked tokens, zero review words (`make_final.py` runs these checks and prints PASS).

**Client data (PII)**
- Never run `mask_reports.py` over all files again: it would undo manual fixes. Mask only the new files (one script per round, dedupe by hash first).
- Rename any file whose name contains a person's name before it enters `02-client-reports-raw/`.
- PII audits by statistics only; never print values (`scripts/pii_audit_masked.py <dir>`, `scripts/probe_round3.py` for structure).

**Scope (agreed 15 Oct 2026)**: only the statutory reports are built — income tax (Formulario 350, Formulario 220, Formato 2276), social security (PILA, cesantías) and Nómina Electrónica. Client operational reports are out of scope.

## How to run
`/crosscheck-reports` — runs everything (masking check, profiling, classification, one cross-checker per spec in parallel, one independent verifier per spec, consolidation). Rounds 2 and 3 followed the same pattern on the new files only (brief in `04-output/round<n>/CROSSCHECK-BRIEF-round<n>.md`).
