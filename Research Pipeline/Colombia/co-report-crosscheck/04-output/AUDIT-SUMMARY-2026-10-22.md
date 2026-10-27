# Audit summary - Colombia (PMI), 22 Oct 2026
Sources: AUDIT-A (consistency, 28 findings: 6 HIGH / 15 MED / 7 LOW), AUDIT-B (commitments / trackers), AUDIT-C (Drive parity). HIGH items re-checked first-hand on 22 Oct.

## Batch 1 - wrong rules in delivered artifacts (HIGH, all re-checked)
1. Planilla M as a correction / arrears route: CO-DIAN-001 C41, -002 C40, -004 C40, -005 C41, CO-CESANTIAS-006 C43 ('PILA: a return type N (correcciones) or M (mora)'); CO-PILA-003 C41 / C49 limit M to periods before health period March 2014 (late payment = E). Same in DD v1.2 Country Fields W80 ('M for arrears') and Option Mappers F221.
2. Apprentice PILA codes: 5 specs C12 and DD F60 say '12 (lectiva) or 19 (productiva)'; AT2 v30 (local PDF pp. 82, 108, 242): 19 = 'Aprendices etapa lectiva Ley 2466 de 2025'; CO-PILA-003 already follows AT2 v30.
3. WTC v1.5 rows 156 'Annual leave payout' and 324 'Vacation compensated in cash': Subject to Health / Solidarity / Occupational risk / Pension = Yes; the sourced rule (CE 26941/2024; SU 25185/2021) excludes cash vacation from the health, pension and ARL IBC (payroll levies stay Yes). Column ownership (blue vs orange) to check before editing.
4. CCG v1.3 P3066 (PILA change-event table, VAC / LR): 'Contributions continue; vacation pay is in the base' vs P2477 / P2953 and PILA M110 (prior-month IBC; no ARL during enjoyed vacation).
5. RAIS voluntary contributions: 220 M47 / 2276 M32 / NE M193 use different source rules (AUDIT-A #6) - to align.

## Batch 2 - quality (MED)
- 84 cells with Spanish quotations altered by an English glossary swap (e.g., 350 M36 'SIN AGREEMENT / CON AGREEMENT' vs M39 'CON CONVENIO').
- NE: bare Res. 13 article numbers (art. 3 / 5 / 8 / 26) to be given as Res. 227 articles.
- CO-PILA-003: no scope row pointing employer-paid pensioners to CO-PILA-007.
- CO-PILA-003 M110: LMA / ARL rule stated as law although PENDING #38 is NOT LOCATED.
- CO-PILA-007: no rule for WT 62153 (June / December extra mesadas); pensioner WT lists differ from the 220.
- Cesantias monthly-advance block rests on a draft decree.
- ~15 rules in column M without citation (AUDIT-A #20).

## Batch 3 - trackers and closing (AUDIT-B)
- Q16: the NE files carry no day quantity (provider layout) -> say so in the closing e-mail; rounding rule (no DIAN source) into PENDING.
- Q1 retirees (amounts / WT 21140 as client inputs), WT 62150 (casilla 36 vs 42), CO-PILA-007 open items (NOTES s.3 / item 13) -> PENDING with disposition.
- PENDING #13 'September folder' -> close as superseded by the zip of 22 Oct.
- Delta content = ALINHAMENTO section B list + M183 + #41 + NE-REVIEW findings 3-6; one date for it.
- Tracker contradictions (delta 28 Oct vs end of Oct; ESTADO / session note still list the chat post; frente estados).
- correcoes.md phase-4 entries (follow-up v1 over scope; B5); state/report-spec-map.md stale; closing e-mail draft incl. 'inform Config' (#22, #36).
- Final re-check of all artifacts after the fixes; WTC baseline 'column A empty' waiver recorded.

## Drive
- CO-CESANTIAS-006 Sheet: empty column inserted at M by Ram Sakthi (22 Oct 08:51). A 'Replace spreadsheet' import would remove it -> fix this Sheet cell by cell, not by import.
