# PDOC (CRA): bônus sem salário no período (teste de 2026-10-21)

Teste feito pelo Claude in Chrome (janela Gmail), para a pergunta da Ruchi no chat "CA Clarifications - Oct 14" (21/10): no K2 dela, sem renda regular no período, o lado regular dá 0; isso está ok?

- PDOC: https://apps.cra-arc.gc.ca/ebci/rhpd/beta/ (Salary calculation, versão 2026-06-11), Ontario, semanal, pago em 2026-10-23.
- Step 2, opção "A bonus payment", campo "Total current bonus payable", nota literal:
  > Note: The employee's salary or wages income per pay period is required to estimate the annual taxable income. PDOC does not calculate tax on stand-alone bonuses.
  (print: 2026-10-21-pdoc-nota-bonus-stand-alone.png)
- Salário = 0 e bônus = 2.500, "Next": o PDOC recusa.
  > Error: Only a value greater than zero will be accepted in this field.
  (print: 2026-10-21-pdoc-erro-salario-zero.png)
- Junto com a T4127 jan/2026, cap. 5, pp. 18-19: "If I = 0, use the most recent I."

## Pesquisa em fontes oficiais (21/10, mesma pergunta)
- **Income Tax Regulations, C.R.C., c. 945, art. 103(2)** (Justice Laws, "current to 2026-09-30"; cópia 2026-10-21-income-tax-regulations-CRC-c945-s103.html): imposto do bônus = [art. 102 sobre ("the amount of regular remuneration paid by the employer to the employee in the pay period in which the remuneration is paid" + bônus ÷ nº de períodos)] − [art. 102 sobre a mesma regular remuneration], × nº de períodos. A letra fala em remuneração regular **paga no período**; não trata o caso de zero.
- **T4001 (Employers' Guide), "Bonuses, retroactive pay increases, or irregular amounts"** (cópia 2026-10-21-t4001-employers-guide.html), Example 1: soma bônus ÷ 52 ao "current pay rate of $400" e usa as tabelas T4032 (tax on $405.77 − tax on $400) × 52. Não trata período sem salário.
- **T4127 jan/2026, pp. 18-19:** "If I = 0, use the most recent I."
- Nenhuma fonte oficial fala do K2 (crédito CPP/EI) quando não há renda regular no período.
