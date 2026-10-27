# HRBS-15863 — Gana — teto de 15% do bônus no imposto final de 5% (2572): anual × YTD

> Análise só leitura feita em 2026-10-22. Nada foi postado no YouTrack, enviado nem alterado no Drive. Rascunho para o usuário revisar antes de qualquer gravação.

## Metadados
| Campo | Valor |
|---|---|
| Ticket | [HRBS-15863](https://youtrack.hrblizz.dev/issue/HRBS-15863) (Service Request, Medium, Open) |
| País / cliente | Gana / Baker Hughes (entidades 0400 e 4455; ambiente Production, LE em Implementation) |
| Assignee | evats (Compliance Support) |
| Pergunta de | Mohit Jain (Head of Compliance Product), 2026-10-21 07:34 UTC |
| Cópia do ticket | `raw/tickets/api/2026-10-22-for-evats/HRBS-15863.md` |
| Anexo | `raw/tickets/api/anexos/HRBS-15863/20261012-1052 - Payslip_Simulation_v2_...xlsx` (aba "7 Annual basic fix"; lido com `python -I` + openpyxl; nomes e salários individuais **não** foram copiados para esta nota) |
| Artefatos nossos | `raw/docs/drive-exports/2026-10-22/Ghana Payroll Configuration Guide Research v2.4.txt` (CCG v2.4, 05-Oct-26); `GH Wage Type Catalogue V2.5.xlsx` (WTC V2.5, 2026-09-11) |
| Fontes oficiais baixadas hoje | `raw/docs/oficiais/GH/2026-10-22-LI2244-Income-Tax-Regulations-2016.pdf` (md5 e6cd40eb31f0db114bdde68b27811b5e); `raw/docs/oficiais/GH/2026-10-22-GRA-Practice-Note-DT-2016-011-Employment.pdf` (md5 ea6011aee37d469b0ed6be78a64de845, idêntico à cópia em `G:\...\Ghana\10 - ICE Support\`); `raw/docs/oficiais/GH/2026-10-22-Act1178-Income-Tax-Amendment-2026.pdf` (aviso GRA, md5 a37b81074ee63658860dbfc9405cf8d8) |

## O que foi pedido a nós
Último comentário (Mohit → @evats, 2026-10-21):
> "At present regulations bonus tax cap is 15% of YTD Basic. Daniel is asking it to be 15% of annual basic. Please check and if you confirm it is 15% of annual basic, kindly provide logic to compute this annual basic for salary change scenario, mid-year joiners, mid-month joiners, mid-year leavers, mid-month leavers."

Só duas coisas: (1) confirmar se o teto é 15% do básico **anual**; (2) se sim, dar a **lógica de cálculo do básico anual** em 5 cenários. As perguntas 2 e 3 do reporter (base quando o salário muda; períodos afetados / re-run) só entram na medida em que a 2 se sobrepõe ao item (2); a 3 (re-run) não foi perguntada pelo Mohit → fica em "O que precisa ser feito".

## Histórico do ticket
| Data (UTC) | Quem | O quê |
|---|---|---|
| 2026-10-12 10:52 | Reporter (cliente, payroll BH Ghana) | Abre: 2572 limitado a 15% do básico YTD; esperado 15% do básico anual (cita página da GRA e resumo da KPMG; WTC do cliente: `P100 x 12 x 15%`). Regs de produção: **9288161** (58124 = 15% × 58123, básico cumulativo) e **9288141** (58118 = MIN(15% × 58120; 58117), 58120 = básico YTD). Dois casos de teste (mar/2026) com workbook. |
| 2026-10-12 14:05 | Support (averma) | Acknowledge. |
| 2026-10-14 08:59 | Reporter | Pede reunião. |
| 2026-10-14 10:13 | Support | Move para Compliance. |
| 2026-10-21 07:34 | Mohit | Pergunta acima para @evats. |

## O que nossos artefatos dizem
**CCG v2.4 (texto exportado)** — diz **anual** em todas as passagens:
- §4.5 Bonuses (linhas 507–509): *"Concessional Rule: The portion of an employee's total annual bonus that is up to 15% of their annual basic salary is subject to a final withholding tax of 5%."* / *"Treatment of Excess: Any bonus amount paid in excess of this 15% threshold is not eligible for the concessional rate. Instead, the excess amount must be added to the employee's regular assessable income for the period and taxed at the standard progressive income tax rates."* / *"This rule necessitates that the payroll system maintains a year-to-date accumulator for both basic salary and bonuses paid to accurately determine when the 15% threshold is crossed and apply the correct tax treatment."*
- Tabela de schedules (l. 690): *"5% on the portion of the annual bonus up to 15% of the employee's annual basic salary."*; l. 875: *"Bonus up to 15% of annual basic salary (Residents)"*; l. 1124 (Module 9): *"The portion up to 15% of the annual basic salary is taxed at a final rate of 5%."*
- Module 12, Scenario 2 (l. 1304–1320): *"Annual Basic Salary = GHS 96,000 / Concessional Bonus Limit (15% of Annual Basic): GHS 96,000×0.15=GHS 14,400"* (= 8.000 × 12).
- Fontes citadas no CCG para a regra: nota 10 (remotepeople.com — secundária) e nota 36 (página PAYE da GRA). **Não cita a L.I. 2244, reg. 5.**
- Ponto fraco: a frase final do §4.5 ("year-to-date accumulator for both basic salary and bonuses") é ambígua e é a provável origem do desenho com básico YTD.

**WTC V2.5 (master)**:
- Linha 9 — `2572 | Final Tax on Bonus | Tax | (Formula vazia) | Lump Sum | Recurring | ...` — **sem fórmula nem observação**.
- Linhas 77–106 — `62200–62229 Annual Bonus / Profit Sharing Bonus / One-time Annual Bonus (Final 5% Tax)`, Formula: *"5% tax upto of 15% of basic salary"* (não diz anual nem YTD).
- Intermediárias (linhas 26–35): `58117 Bonus YTM`, `58118 Bonus Current`, `58119 Bonus Cumulative`, `58120 Monthly Basic Salary YTM`, `58121 Monthly Basic Salary Current`, `58123 Monthly Basic Salary Cumulative`, `58124 Monthly Basic Salary Cumulative (15%)`, `58125 Bonus Tax Threshold`, `58126 Bonus Tax Threshold - Intermediary`. Os nomes mostram que o desenho mede o teto sobre o **básico cumulativo (YTD)** — coerente com as regs 9288161/9288141 citadas pelo reporter.
- Version Control: nenhuma versão (1.0 a 2.5) mexeu no bônus.

**Regs de produção (citadas no ticket, não abertas por nós):** 9288161 → 58124 = 15% × 58123 (básico cumulativo); 9288141 → 58118 = MIN(15% × 58120; 58117). ⚠️ conteúdo das regs só pelo ticket/anexo (não temos acesso ao HRB); o anexo reproduz os payslips "to the cent" com essa lógica, o que confirma o comportamento.

**Comparação:** CCG = anual (correto); WTC master = intermediárias YTD sem regra escrita; produção = YTD. A divergência está no desenho/configuração, não na pesquisa.

## Fonte primária
1. **Income Tax Regulations, 2016 (L.I. 2244)**, feitas sob a s. 127(1) do Income Tax Act, 2015 (Act 896); gazette 4 jul 2016 (`raw/docs/oficiais/GH/2026-10-22-LI2244-Income-Tax-Regulations-2016.pdf`, cópia publicada pela GNPC; texto da reg. 5(2) idêntico ao reproduzido pela GRA na Practice Note).
   - **Reg. 5(2):** *"Where an employer pays a bonus to an employee during a year of assessment, the employer shall, (a) if the total of the bonus payments made by that employer to the employee during the year of assessment does not exceed fifteen percent of the annual basic salary of that employee, withhold tax from the gross amount of the payment at the rate of five percent; or (b) if the total bonus payments made by that employer to the employee during the year of assessment exceeds fifteen percent of the annual basic salary of that employee, (i) add the excess payments to the employment income of that employee for that year; and (ii) withhold tax from the total amount obtained in accordance with the First Schedule of the Act."*
   - **Reg. 5(3):** *"Tax withheld under subregulation (1) or (2) is a final tax on the overtime or bonus payment and (a) the payment shall not be included in calculating income derived by the employee from that employment; and (b) the tax paid by withholding satisfies the tax liability of the employee with respect to the payment..."*
   - **Reg. 5(6):** *"A person shall, in calculating tax on bonus paid to an employee, calculate the tax on the basic salary of the employee for the year of assessment to which the bonus relates."*
   - **Reg. 4(2)–(3)** (PAYE geral, apoio para a projeção): o empregador usa *"qualifying cash payments still to be made by the employer to the employee during the year of assessment as estimated under subregulation (3)"*, e pode *"(a) make a reasonable estimate of ... (ii) the amount of qualifying cash payments yet to be made ... during the year of assessment; or (b) consider whether or not an estimate made under paragraph (a) is still accurate and, if not, make a new estimate"*.
   - Contraste útil: para **horas extras** a lei usa *"basic salary of that employee for the month"* (reg. 5(1)); para **bônus**, *"annual basic salary"* e *"for the year of assessment"*. O legislador distinguiu mês × ano de propósito.
2. **GRA Practice Note DT/2016/011 — Gains or Profits from Employment under Act 896** (6 out 2016; emitida sob o par. 2 da Seventh Schedule do Act 896) — `raw/docs/oficiais/GH/2026-10-22-GRA-Practice-Note-DT-2016-011-Employment.pdf`:
   - §4.11.2 repete a reg. 5(2) literalmente. Exemplo 1: *"annual Basic salary of GHS100,000.00 ... bonus of GHS14,000.00 in July, 2016 ... Annual bonus as a percentage of annual basic salary = 14 ... taxed at a concessionary rate of 5% ... GHS700.00"*. Exemplo 2: *"annual basic salary of GHS120,000.00 ... bonus of GHS20,000.00 in December ... 15% of Annual basic salary (120,000.00 x 15%) = GHS18,000.00 / Excess bonus paid = GHS2,000.00 ... added to Kwame's income for the year"*. (O exemplo de julho usa o básico do ano inteiro, não o YTD de julho.)
   - §4.1(c): *"In instances where employment commences on a date other than 1st January of a calendar year, the basis period for computation of the individual's income from the employment shall be the period starting from the date of commencement of the employment and ending on 31st December of the same year."*; §4.1(d): *"calculation of the tax payable shall be based on a twelve months period ending on 31st December each year."*
   - Formato de assessment (§5.0): *"Excess Bonus (Sect 4 & Reg. 5)"* — confirma a reg. 5 como base.
3. **GRA — página PAYE** (https://gra.gov.gh/domestic-tax/tax-types/paye/, lida em 2026-10-22): *"Total bonus payments made by employers to their employees in a year of assessment are taxed at 5% up to 15% of the annual basic salary of the employee. Where the bonus payment exceeds 15%, the excess will be added to the employment income of the employee and taxed at the graduated tax rate."* (mesma página: *"for a non-resident employee tax on bonus or overtime is 20%"*).
4. **ICE (consultor local) — `G:\...\Ghana\10 - ICE Support\ICE Clarification.docx`** (não é fonte oficial; apoio): *"it is applicable on the monthly income and the Bonus is on the annual income because that one is paid annually"*.
5. **Formulário anual da GRA** (`G:\...\Ghana\07 - Design\DT_0108a_employer_annual_tax_deduction_schedule_notes.docx`): colunas *"11. Bonus Income (up to 15% of Basic Salary)"*, *"12. Final Tax on Bonus"*, *"13. Excess bonus"* — o teto é reportado em base anual no Employer's Annual Tax Deduction Schedule.
6. Secundárias (só apoio): TaxLawGH (MSL Business School): *"Use the employee's basic salary for the year of assessment to which the bonus relates."* e *"Do not reset the limit every month ... Payroll needs year-to-date bonus records."*; BDO Ghana (2026) não trata joiners/leavers.

**O que a lei NÃO define:** nem a L.I. 2244, nem a Practice Note, nem a página da GRA dão fórmula de "annual basic salary" para mudança de salário, admissão ou desligamento no meio do ano/mês, nem dizem se o teto deve ser recalculado no fim do ano/rescisão. Não achamos definição de "basic salary" na L.I. 2244. Tudo na seção "Lógica proposta" é **proposta de design**, ancorada nas regs 4(3) e 5(6) e na §4.1(c) da Practice Note.

## Veredito
- **Anual, não YTD.** O teto é 15% do *annual basic salary* do empregado, para o *year of assessment to which the bonus relates* (L.I. 2244, reg. 5(2) e 5(6); GRA Practice Note DT/2016/011 §4.11.2; página PAYE da GRA). O lado do bônus é cumulativo no ano (*"the total of the bonus payments made by that employer ... during the year of assessment"*).
- As regs 9288161/9288141 (15% do básico YTD) não seguem a regra: com o YTD, um bônus pago cedo no ano recebe só uma fração do teto e o restante vai para a tabela progressiva (retenção a maior).
- **Ressalva sobre o pedido do cliente ("current monthly basic × 12"):** é uma estimativa que funciona para quem trabalha o ano todo com salário fixo, mas superestima o básico de quem entrou no meio do ano, quem sai, e quem teve aumento no meio do ano. Além disso, a reg. 5(6) aponta para o **ano a que o bônus se refere**: se o "Full Stream Bonus" pago em mar/2026 for de performance 2025, a base é o básico de 2025 — e não o salário de mar/2026 × 12. ⚠️ O ticket não diz a que ano o bônus se refere.

## Lógica proposta por cenário
> **Proposta de design** (não é texto de lei). Base legal da abordagem: reg. 5(2)/(6) (teto anual, ano a que o bônus se refere); reg. 4(3) (estimativa razoável dos pagamentos ainda a fazer no ano, revisável a cada período); Practice Note §4.1(c) (para quem entra no meio do ano, o período-base vai da admissão a 31/12).

**Definição geral (cada período p do ano Y):**
```
AB_p (annual basic estimate, ano Y) =
      Σ básico efetivamente pago de jan até p (inclui o próprio p, prorrateado se for o caso;
        inclui 62100 + 62101 arrears + 62102 adjustment que pertençam ao ano Y)
    + básico mensal contratual vigente em p × M_rest
M_rest = nº de meses inteiros de emprego ainda previstos no ano Y depois de p
       = 12 − mês(p)                               (empregado sem data de saída)
       = meses entre p e a data de saída conhecida (o último mês prorrateado pela mesma regra de proration do básico, CCG §4.3)
       = 0 no último período do ano ou na rescisão (aí AB = básico efetivo do ano)
Cap_p = 15% × AB_p
```
**Bônus cumulativo contra o teto anual (substitui 58118/58124):**
```
B_cum_p   = Σ bônus 5%-elegíveis pagos por este empregador no ano Y até p (58119)
F_cum_p   = MIN(B_cum_p ; Cap_p)                 → parte cumulativa que fica nos 5%
F_p       = F_cum_p − F_cum_(p−1)                → base 5% do período (58572)
2572_p    = 5% × F_p
Excess_p  = Bonus_p − F_p                         → entra na renda tributável do período (PAYE cumulativo)
```
Se `Cap_p` cair (ex.: saída conhecida depois), `F_p` pode ficar negativo — ver "Regularização".

**Ano de referência do bônus (reg. 5(6)):** campo/flag "bonus reference year" na entrada do bônus. Se = ano corrente → AB_p acima. Se = ano anterior → AB = básico efetivamente pago no ano anterior (histórico YTD do ano fechado); sem histórico → usar a estimativa do ano corrente e marcar exceção. ⚠️ A contagem cumulativa (B_cum) segue o ano em que o bônus é **pago** (reg. 5(2): "during the year of assessment"); combinar as duas leituras é ponto a confirmar (Lacunas).

Exemplos genéricos (GHS; básico mensal 10.000; sem dados do empregado real):

| # | Cenário | Dados | AB (proposta) | Cap 15% | Comparação |
|---|---|---|---|---|---|
| 1 | **Mudança de salário** | 10.000 jan–mar; 12.000 a partir de abr; bônus em abr | 30.000 + 12.000 + 12.000 × 8 = 138.000 | 20.700 | YTD (abr) = 42.000 → 6.300; "atual × 12" = 144.000 → 21.600 |
| 2 | **Admissão no meio do ano** | entra 1º jul; bônus em out | 6 × 10.000 = 60.000 (jul–dez) | 9.000 | "atual × 12" = 120.000 → 18.000 (superestima); YTD (out) = 40.000 → 6.000 |
| 3 | **Admissão no meio do mês** | entra 16 jul, jul prorrateado = 5.000 (pela regra de proration do CCG §4.3); bônus em out | 5.000 + 5 × 10.000 = 55.000 | 8.250 | "atual × 12" = 120.000 → 18.000 |
| 4 | **Desligamento no meio do ano** | jan–set, saída 30 set; bônus pago na rescisão | 9 × 10.000 = 90.000 | 13.500 | Se o bônus foi pago em mar (saída ainda desconhecida): AB estimado 120.000 → cap 18.000; na rescisão cai para 90.000 → regularizar |
| 5 | **Desligamento no meio do mês** | jan–ago + 15 set (set prorrateado = 5.000) | 8 × 10.000 + 5.000 = 85.000 | 12.750 | idem 4 |

**Bônus cumulativo (exemplo, cenário 1):** abr bônus 15.000 → F_cum = MIN(15.000; 20.700) = 15.000 → 2572 = 750; excesso 0. Nov bônus 10.000 → B_cum = 25.000; F_cum = 20.700; F_p = 5.700 → 2572 = 285; excesso 4.300 vai para o PAYE de nov.

**Regularização (último período do ano ou rescisão)** — proposta:
- No período de dezembro ou no último período de emprego, AB = básico efetivo do ano (M_rest = 0); recalcular `F_cum` e lançar a diferença:
  - Cap caiu (cenário 4: bônus 18.000 pago em mar com cap estimado 18.000 → 2572 = 900; na saída, cap = 13.500): F_p = 13.500 − 18.000 = −4.500 → 2572 = −225 e +4.500 na renda tributável do período final (PAYE cumulativo).
  - Cap subiu (ex.: aumento no fim do ano): F_p positivo → parte do excesso já tributado volta para os 5% e sai da renda tributável cumulativa.
- Justificativa: o teto é anual (reg. 5(2)) e o Employer's Annual Tax Deduction Schedule (DT_0108a, colunas 11–13) reporta bônus até 15%, imposto final e excesso em base anual; o PAYE já é cumulativo (CCG §6.2, reg. 4(3)(b) "make a new estimate").
- Alternativa mais simples (a decidir com o produto): sem regularização; cada pagamento usa a estimativa do momento (reg. 5(3) trata o 5% retido como final). Risco: o anual reportado não bate com 15% do básico efetivo de quem sai.

**Dados que o sistema precisa:** básico contratual mensal vigente (o "P100" do WTC do cliente), básico efetivamente pago YTD (58123), mês do período no ano, data de admissão (já usada em 58207) e data de saída, ano de referência do bônus, histórico de básico do ano anterior.

## Conferência das contas
Refeito de forma independente (script próprio, faixas anuais pré-Act 1178 do anexo — 0% até 5.880 … 35% acima de 605.000, conferidas contra o CCG v2.4 §6.2 — e o método PAYE cumulativo/anualizado do anexo; insumos de jan/fev conforme postados pelo HRB):

| Caso (bônus 62200, mar/2026) | Base do teto | Cap | 2572 | PAYE mar | Total mar |
|---|---|---|---|---|---|
| 1 — 20.000, HRB hoje (YTD) | básico jan–mar | 7.336,03 | 366,80 | 10.885,97 | 11.252,77 |
| 1 — 20.000, "atual × 12" (reporter) | 240.000 | 36.000,00 | 1.000,00 | 7.086,78 | 8.086,78 |
| 1 — 20.000, proposta (pago + projetado) | 228.906,84 | 34.336,03 | 1.000,00 | 7.086,78 | 8.086,78 |
| 2 — 100.000, HRB hoje (YTD) | básico jan–mar | 7.336,03 | 366,80 | 35.207,28 | 35.574,08 |
| 2 — 100.000, "atual × 12" (reporter) | 240.000 | 36.000,00 | 1.800,00 | 26.286,78 | 28.086,78 |
| 2 — 100.000, proposta (pago + projetado) | 228.906,84 | 34.336,03 | 1.716,80 | 26.785,97 | 28.502,77 |

- Os números do reporter batem ao centavo: HRB hoje e "expected" (366,80 / 10.885,97; 1.000,00 / 7.086,78; 366,80 / 35.207,28; 1.800,00 / 26.286,78) e as diferenças 3.165,99 (caso 1) e 7.487,30 (caso 2).
- Com a lógica proposta, o caso 1 não muda; no caso 2 a diferença para o HRB de hoje é 7.071,31 (e não 7.487,30), porque o salário só subiu em março.
- As duas bases do reporter assumem que o bônus é de 2026. Se for de performance 2025, a base pela reg. 5(6) é o básico de 2025 (não está no ticket) → os "expected" mudariam.

## Achados fora do pedido
1. **Hub do país inexistente:** não há `paises/Gana.md` no cérebro (nenhuma referência a Gana em `correcoes.md`). Criar o hub a partir de `modelos/` e registrar este ticket.
2. **CCG v2.4 não cita a fonte primária** da regra do bônus (cita remotepeople.com e a página da GRA; falta a L.I. 2244 reg. 5(2), 5(3), 5(6)) e não registra a regra do "ano a que o bônus se refere". A frase *"year-to-date accumulator for both basic salary and bonuses"* (§4.5) é ambígua.
3. **WTC V2.5:** 2572 sem fórmula; 62200–62229 com *"5% tax upto of 15% of basic salary"* (sem "annual"); as intermediárias 58120/58123/58124 são YTD.
4. **Não residentes:** a página PAYE da GRA diz *"for a non-resident employee tax on bonus or overtime is 20%"*; o CCG v2.4 só traz o 5% para residentes (l. 875) e 25% flat para não residentes. ⚠️ não conferido na lei (Act 896 First Schedule / emendas) — verificar.
5. **Material interno inconsistente:** `G:\...\Ghana\11 - Simulations\Sample.Tax.Calculation.2025.15.xlsx`, aba "Terminated employee": `D10 = D6*15%` (15% do básico **mensal**, rotulado "15% of Annual Basic Salary"), prorrateia o bônus e aplica 10% (`E22 = E10*10%`). Não usar como referência.
6. Faixas do Act 1178 (a partir de 2026-09-01) já estão no CCG v2.4; o anexo usa as faixas anteriores, o que está correto para mar/2026.

## Rascunho de resposta (EN)
> Para Mohit, no ticket. Só o perguntado; sem "I checked"; tom neutro. **Não postar sem ok do usuário.**

```
Hi Mohit,

Confirmed: the cap is 15% of the employee's ANNUAL basic salary, not year-to-date basic.

- Income Tax Regulations, 2016 (L.I. 2244), reg. 5(2): "if the total of the bonus payments made by that employer to the employee during the year of assessment does not exceed fifteen percent of the annual basic salary of that employee, withhold tax ... at the rate of five percent", and the excess is added to employment income and taxed under the First Schedule.
- Reg. 5(6): "calculate the tax on the basic salary of the employee for the year of assessment to which the bonus relates."
- GRA Practice Note DT/2016/011, s. 4.11.2, examples 1-2: a bonus paid in July is tested against the full annual basic (e.g. 15% x 100,000), not against basic paid to date.

The law does not give a formula for joiners, leavers or salary changes. Proposed logic (re-estimated each period, as reg. 4(3) allows for PAYE estimates):

Annual basic (AB) = basic actually paid in the tax year to date (incl. current period, prorated where applicable, and basic arrears/adjustments for that year) + current contractual monthly basic x remaining months of employment in the year.
Cap = 15% x AB. Bonus at 5% this period = MIN(cumulative bonus YTD; Cap) - amount already taxed at 5% in prior periods. The rest of the bonus goes to PAYE.

1. Salary change: 10,000 Jan-Mar, 12,000 from Apr, bonus in Apr: AB = 30,000 + 12,000 + 12,000 x 8 = 138,000; cap 20,700 (YTD basic would give 6,300).
2. Mid-year joiner (joins 1 Jul, 10,000): AB = 6 x 10,000 = 60,000; cap 9,000. The basis period for a joiner runs from the start date to 31 Dec (Practice Note s. 4.1(c)). Bonuses from a previous employer do not count ("made by that employer").
3. Mid-month joiner (joins 16 Jul, July prorated 5,000): AB = 5,000 + 5 x 10,000 = 55,000; cap 8,250.
4. Mid-year leaver (leaves 30 Sep): remaining months stop at the leaving date: AB = 9 x 10,000 = 90,000; cap 13,500.
5. Mid-month leaver (leaves 15 Sep, Sept prorated 5,000): AB = 8 x 10,000 + 5,000 = 85,000; cap 12,750.

True-up: in the December or final (termination) period, AB = actual basic paid in the year; recompute the 5% portion against the final cap and post the difference (2572 adjustment, with the amount moved into or out of PAYE). Example: bonus 18,000 paid in March against an estimated cap of 18,000, employee leaves 30 Sep, final cap 13,500: 2572 -225 and +4,500 to taxable income in the final period.

Two points to confirm with the client:
- "Current monthly basic x 12" overstates AB for joiners, leavers and mid-year increases. Under the logic above, case 2 in the workbook gives Other Tax 1,716.80 / PAYE 26,785.97, not 1,800.00 / 26,286.78 (case 1 is unchanged: 1,000.00 / 7,086.78).
- Per reg. 5(6), if the March bonus relates to performance year 2025, the cap uses the 2025 basic salary, not 2026.

Kind regards,
```

## O que precisa ser feito
| # | O quê | Quem | Urgência |
|---|---|---|---|
| 1 | Aprovar e postar a resposta acima (draftComment), depois de revisão do usuário | Usuário → janela Suporte | Alta (ticket do cliente em produção, retenção a maior em todo bônus pago antes de dezembro) |
| 2 | Especificar a mudança das regs 9288161 / 9288141: trocar o básico YTD (58120/58123) por AB_p (pago YTD + contratual × meses restantes); 58124 → 15% × AB_p; 58118 → F_cum_p − F_cum_(p−1); regularização no último período | Design (Compliance, nosso) → configuração no HRB pelo time de produto/configuração (fronteira) | Alta |
| 3 | WTC: nova versão (V2.6) com fórmula/observação em 2572 e 62200–62229 ("15% of ANNUAL basic salary for the year of assessment to which the bonus relates; cumulative bonus YTD; L.I. 2244 reg. 5(2),(6)") e intermediária nova "Annual Basic Salary Estimate" (+ eventual flag de ano de referência). Partir da maior versão no Drive; destacar em azul claro; não sobrescrever o .gsheet | Design (nosso) | Média (depois da decisão do Mohit) |
| 4 | CCG: v2.5 com a reg. 5(2)/(3)/(6) citada, a regra do ano de referência e a frase do §4.5 reescrita ("cap measured on annual basic salary; bonus accumulated YTD") + a lógica de joiners/leavers como regra de design | Research (nosso) | Média |
| 5 | Decidir períodos afetados e re-run (pergunta 3 do reporter): bônus 5%-elegíveis desde o go-live das regs em todas as entidades GH; correção do ano corrente pelo próprio PAYE cumulativo; ano fechado (2025) → restituição pela GRA (CCG §6, refund via Commissioner-General) | Mohit / produto + cliente | Média |
| 6 | Criar `paises/Gana.md` e registrar ticket, decisão e correção (WTC/regs YTD) — só pela janela competente, com ok do usuário | Janela Suporte / geral | Baixa |

## Lacunas
1. Conteúdo real das regs 9288161/9288141: só pelo ticket/anexo (sem acesso ao HRB).
2. A lei não define "annual basic salary" para joiners/leavers/mudança de salário, nem exige regularização no fim do ano: toda a "Lógica proposta" é design. Sem guia da GRA específico sobre isso (procurado na Practice Note, página PAYE e L.I. 2244).
3. Leitura conjunta de reg. 5(2) (bônus contados no ano em que são **pagos**) e 5(6) (básico do ano **a que o bônus se refere**) para bônus pagos num ano e relativos ao anterior: sem orientação oficial encontrada; e o ticket não diz a que ano o bônus de mar/2026 se refere.
4. Tratamento de básico arrears/adjustment de ano anterior pago no ano corrente (entra no AB de qual ano?) — não definido.
5. Texto consolidado do Act 896 e emendas (Act 907/2016, 2017, 2018, 2019, 2023, Act 1178/2026) não lido: não confirmamos se alguma emenda mexeu no bônus ou na L.I. 2244 reg. 5 (a página da GRA de out/2026 ainda traz a mesma regra, e o aviso do Act 1178 só muda faixas e o MTS). Taxa de 20% para não residentes também sem confirmação na lei.
6. A L.I. 2244 baixada é cópia publicada pela GNPC (não pela GRA nem pela Assembly Press); o texto da reg. 5(2) coincide com a Practice Note da GRA. A reg. 5(6) aparece só na cópia GNPC (e na TaxLawGH, secundária).
