Reply in the 'PMI Review' thread (Reply all). Replaces v1 (14 questions) and v2 (3 questions) after the scope review in section B (skill mercans-compliance-workflow §7; brain-service fronteiras.md: client WTC / WT classification = client / team lead, product mapping = Config / Product / BA).

## A. E-mail text

Hi Heidy, Hi Cinthya,

Thank you for the answers and for the Conceptos CIR 2025 file.

Electronic payroll: for the 871 files of September, please put them in one zip file in a Google Drive folder shared with me.
Folder access: the folder 'September 2026 Payroll Validation Files' linked in your 21 Oct e-mail shows 'You need access' for my account. Could you share it?

**Scope (Manju, Andy)**
Still open from 19 Oct: are the PILA and cesantías specs (new system functionality) in scope for the December go-live? And the PILA of the pension payer (454 pensioners, 21 retirees), which has a different layout from the employees' PILA: in or out of scope?

Thanks a lot,
Wallisson

## B. Scope review (internal)
Rule: compliance states the statutory rule per field / casilla and its source. Which client wage type carries which attribute (salary / non-salary, deducted from the employee / borne by the employer, withholding remitted / hypothetical) is the client's WTC and product mapping - not ours, not even as a question to the client.

| v2 item | Verdict | Why |
|---|---|---|
| 21330 / 25834 remitted or hypothetical | DROP | Classification of a client WT. Ours: the rule of casilla 93 (350), casilla 60 (220) and the NE withholding field = withholding actually practised; the WT attribute comes from the WTC. |
| 62830 nature | DROP | Classification of a client WT. Ours: pensions -> 220 casilla 50, other payments -> casilla 46 (instruction guide). |
| Institutional plans (21210-21212, 25820, 25821) | DROP | Classification of a client WT. The rule (casilla 56 / numeral 26 = amount deducted from the employee in the employee's name) is already in the specs (round 5, B4). |
| 871 NE files | KEEP | Answer to BAU's own question (Q21 of 21 Oct); evidence of the NE output of the other pay groups for the agreed cross-check of the specs. |
| Folder access | KEEP | Holds the files of BAU's 21 Oct answers. |
| Scope (Manju, Andy) | KEEP | Scope of our specs; unanswered since 19 Oct. |

Also out of scope (not carried to Phase 2): the 'spec items' of v2 section B that route individual client WTs (62150, 62224, 62837, 79419, 62137, CLA WTs, 21644).

Phase 2 item that stays (rule-level, ours): the three specs state the withholding rule differently (CO-DIAN-004 casilla 60 excludes 21330 / 25834 by name; CO-DIAN-002 casilla 93 and CO-DIAN-001 RetencionFuente include 21330 'where it carries the withholding actually deducted'). Harmonise to one rule stated the same way in all three, with the source, through a change map and the independent verifier.

RESOLVED 21 Oct - KEPT (see PENDING-2026-10-21 item 3: the spec already named 98 WT codes before round 5; B5 adds only codes consistent with the existing casilla rule). Original note: round 5 B5 (already applied) added to the CO-DIAN-004 / CO-DIAN-005 WT lists 12 client WT codes taken from the client's map (62182, 62211, 79403, 65813, 65826, 25819, 21141, 21142, 21154, 21648, 21649, 21155, and 65820 next to 25830). Under this scope rule that is client WT mapping. Keep or revert (revert = make_final with the previous text, previous copies in 05-final/_previous/)?
