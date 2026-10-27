# Rules to apply to the FINAL specs (16 Oct 2026, second pass)

You apply Wallisson's rules below to ONE final spec in `05-final/` and write `04-output/final-prep/<SPEC>-rules-map.json`. You do NOT edit any workbook; a script applies your map cell by cell and runs the checks (diff limited to your cells, zero formulas, zero masked tokens, zero review language).

Sources to cite (as given, no others needed): Formulario 220 instruction guide (Res. 000022/2024); Formato 2276 v4 Anexo T3.45 (Res. 000227/2025); Formulario 350 (Res. 000031/2024); Estatuto Tributario (ET).

## Standard (unchanged from the initial-version build)
- Columns T and U of the spec sheet stay empty; Version Control stays the single initial-version line; no review or process language (corrected, revised, review, verified, cross-check, round, previously, no longer, "was X", "not <number>" comparisons, "the client's ...", decisions, pending, queries, "Rule to be set at implementation" where the rule below now settles the point). Each explanation states the rule as it is with its legal source. Keep wage-type mappings, formats, positions, option values. No masked tokens or employee identifiers.
- Propagate every rule consistently: the Field Explanation (M), and wherever the same point is stated in Format (J), Example (K), System Mapping (L), Option Values (O), Rounding (P), Conditional Reason (G), the Field Options sheet, Population Rules, Example Analysis, Sample File, Report Matrix and Payroll Scope Summary. A worked example that contradicts a rule (e.g. a February deposit certified in the accrual year) must be changed to follow the rule.
- Where a rule below settles a "Rule to be set at implementation" sentence, replace that sentence by the rule. Where it does not, leave the sentence.
- `current` = exact current text of the FINAL cell (read it with openpyxl from `05-final/<file>`); `proposed` = full new text. A `proposed` of "" clears the cell.

## FORMULARIO 220 (CO-DIAN-004)
1. Amounts: pesos rounded to the nearest multiple of 1,000; zero when there is no value (instruction guide, Res. 000022/2024).
2. Casilla 4: number assigned by the issuer, no DIAN-prescribed format; alphanumeric allowed (Format becomes AN where the spec says N).
3. Pensions (jubilación, vejez, invalidez) in casilla 50; payments to retirees that are not a pension in casilla 46.
4. Vacation pay in casilla 42.
5. Per diems (viáticos) always in casilla 43.
6. Habitual bonuses in casilla 36; non-habitual bonuses in casilla 46.
7. Meals: for employees earning more than 310 UVT, in casilla 37; for employees up to 310 UVT, the excess over 41 UVT per month in casilla 38.
8. Casilla 49 = severance savings deposited to the fund in the tax year; the February deposit belongs to the year of the deposit (ET art. 27 num. 3).
9. Casilla 60 = withholding actually practised; no hypothetical or contingent amounts.
10. Casilla 33 = city where the withholding was practised; casillas 34/35 = DANE codes.
11. Document types: 12, 13, 21 (tarjeta de extranjería), 22 (cédula de extranjería), 31, 41.
Still open (keep as a configuration point, do not invent): employer contributions to institutional plans in casilla 56.

## FORMATO 2276 (CO-DIAN-005)
1. Address, department and municipality are mandatory only when the country of residence is Colombia; country is always mandatory.
2. Meals: above 310 UVT in pabop; up to 310 UVT in pagahuvt (up to 41 UVT per month) and vaex (the excess).
3. Per diems in pavia.
4. Habitual bonuses in pasa; non-habitual bonuses in potro.
5. Pensions in peju; one-off payments that are not a pension in potro.
6. Pensioners' health contributions in apos; solidarity in apof.
7. ceco = deposits made in the reported year.
8. vare = withholding actually practised.
9. Positive integer values; zero when there is no value.
(Use the Anexo T3.45 element names exactly as the spec already names them; map each rule to the numeral/field ids the spec uses.)

## FORMULARIO 350 (CO-DIAN-002)
1. Non-resident foreign natural persons go in the "Pagos al exterior" section with the concept and country of sheet 2, not in rentas de trabajo; base = nominal (gross) value, rate 20% (ET art. 408), no depuration.
2. Contingent withholding (ET arts. 126-1 / 126-4) is practised by the fund and does not enter Form 350, so the wage types that compute it stay out.
3. Withholding on pensions goes in the rentas de pensiones line; the electronic payroll RetencionFuente reconciles to the sum of the two lines (rentas de trabajo + rentas de pensiones).
4. Country code from the DIAN table (the same used for the RUT and exogenous information).

## NÓMINA ELECTRÓNICA (CO-DIAN-001)
1. Document type: cédula de extranjería = 22, tarjeta de extranjería = 21 (both valid; the code follows the document the employee holds, as recorded in the document-type field).

## Output
```json
{"spec":"CO-XXX-NNN","final":"05-final/<file>.xlsx",
 "edits":[{"sheet":"<sheet>","cell":"M41","field_id":"...","rule":"220-3","current":"<exact current text>","proposed":"<full new text>"}],
 "resolved_rule_to_be_set":["<sheet>!<cell> (<field>): <what the rule settled>"],
 "still_open":["<sheet>!<cell> (<field>): <what stays as a configuration point and why>"],
 "summary":{"cells":0,"by_sheet":{}}}
```
Final reply: cells per sheet, the resolved items, the still-open items.
