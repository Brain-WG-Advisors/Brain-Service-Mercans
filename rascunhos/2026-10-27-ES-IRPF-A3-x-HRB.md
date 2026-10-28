# Espanha — IRPF: lógica do A3 × HRB (Elessent, outubro/2026) — RASCUNHO 27/10, não enviado

Pedido: call "Spain Transition to HRB" (27/10, Mohamed: "Are we able to identify how A3 is doing the calculation?"; Wallisson: retorno hoje) e call com o Vinícius (27/10, 01:33:42–01:35:44: "pegar esses documentos e comparar", finalizar hoje). Feito pela janela Gmail, a pedido do usuário (tarefa vinda da janela Chat).

Entrada (Downloads, 27/10 14:34, enviados pelo Mohamed): `excel (1).xls` (alíquotas do A3, 8 funcionários, previsão 01/10/2026); `Elessent 1 EE - A138325 .docx` (Detalle del Cálculo do A3, julho/2026, 1 funcionário; o início do arquivo tem JavaScript colado, sem relação com o cálculo); `Gross To Net Spain 2026-10-01 - 2026-10-31.xlsx` (HRB, REF-P203-698). Sem nomes nem IDs aqui: funcionários = E1…E8 (ordem do G2N).

## Passo a passo

| Passo | A3 | HRB | Diverge? | Fonte |
|---|---|---|---|---|
| Renda anual | recebido no ano + pendente até dezembro | 58163 = 58149 + 58117 (8/8) | **Sim** (1) | RIRPF 83.2; CCG v1.6 §6.1.1 |
| Variáveis | maior entre ano anterior e ano corrente | 58901 existe | Sem efeito em out. (ano corrente > anterior nos 8) | RIRPF 83.2, regra 1.ª |
| Gastos | SS + 2.000 | 58590 + 2.000 | Não | LIRPF 19.2.f |
| Mínimo pessoal e familiar | 5.550 (E1, julho) | 58170 | Não | LIRPF 57.1; RIRPF 84 |
| Escala | 20.200 / 4.225,50 / 30%… | igual (58171) | Não | RIRPF 85.1 |
| Teto 43% (≤ 35.200) | aplica | não aparece no G2N | Não verificável; não pesou | RIRPF 85.3 |
| Regularização | (cota − retido) ÷ pendente | 58115 ÷ 58117 | Não | RIRPF 87.3 |
| Arredondamento | 2 decimais | 58118 com 3 casas, arredondado | **Sim** (2) | RIRPF 86.1, 87.3.c; algoritmo AEAT 2026 (TRUNCAR) |
| Voluntária | "semiautomático": nunca abaixo da "% Referencia" | 58217 = alíquota final do A3 (8/8); DD #23: "overrides the calculated rate", validação "≥ calculated" | **Sim** (3) | RIRPF 88.5; DD V5.1 |

## Números (conferidos por script)

| Func. | HRB 58115/58117 | 58118 | Modelo (HRB com 58165 no lugar de 58149) | A3 aplicado | Modo A3 / % Ref. | 58165 − 58149 |
|---|---|---|---|---|---|---|
| E1 | 13,22 | 0,132 | 14,25 | 18,45 | semi / 18,45 | 304,71 |
| E2 | 17,47 | 0,175 | 19,25 | 19,23 | semi / 17,00 | 534,08 |
| E3 | 11,95 | 0,12 | 13,66 | 18,50 | semi / 18,50 | 526,45 |
| E4 | 15,95 | 0,16 | 17,26 | 17,29 | auto / 0,00 | 383,96 |
| E5 | 16,81 | 0,168 | 18,20 | 18,19 | auto / 0,00 | 438,04 |
| E6 | 24,02 | 0,24 | 25,22 | 25,17 | semi / 22,00 | 579,53 |
| E7 | 17,76 | 0,178 | 18,11 | 18,10 | semi / 12,00 | 118,65 |
| E8 | 14,83 | 0,148 | 14,83 | 14,82 | auto / 0,00 | 0,00 |

- 58165 = fixas recebidas + variáveis recebidas do A3 (diferença ≤ 0,06 €). 2552 ÷ bruto = alíquota do A3 nos 8.
- Modelo usa a SS projetada do HRB (58590); a do A3 não está nos arquivos → explica até 0,05 p.p.
- Não explicado (não entra no texto): E3 tem 600 € a mais de redução no HRB (58167 → 58169).

## O que falta (pedido no texto)
- Composição por wage type de 58165 − 58149 (atrasos de anos anteriores ou outro valor excluído pelo art. 83.2 → HRB certo; senão, HRB deve incluir).
- Qual acumulador alimenta o 58163 (fórmula dos intermediários não está no WTC V4.7 nem no CCG).
- Opcional para fechar as inferências: "Detalle del Cálculo" de outubro dos 8 (alíquota calculada pelo A3, SS projetada, significado de "% Referencia"/"semiautomático").
- Depois da resposta do Mohamed → Lily: 58118 truncado em 2 decimais; regra do 58217 para jan/2027.

## Texto ao Mohamed — versão curta (é a que está no rascunho do Gmail, 27/10; Para: mnabil@mercans.com)

Hi Mohamed,

I compared A3 and HRB for Elessent, October 2026 (8 employees), using your A3 files and the HRB G2N (REF-P203-698).

1. Same logic. Both apply RIRPF arts. 83–87. Taking HRB's own figures and only using 58165 instead of 58149 as gross already paid, I get the A3 rate within 0.05 pp for the 6 employees whose A3 rate is not the "% Referencia".
2. Differences:
   a) Gross already paid: HRB uses 58149 (58163 = 58149 + 58117), while A3 uses the full amount paid (= 58165). The gap (EUR 118.65 to 579.53 for 7 employees; zero for the 8th) lowers the HRB rate by 0.35 to 1.78 pp.
   b) 58118 is rounded to 3 decimals (17.469% → 0.175). The rate is expressed with two decimals (RIRPF arts. 86.1 and 87.3.c), truncated as in the AEAT algorithm (17.46%).
   c) 58217 currently holds the A3 final rate for all 8 employees, so 2552 = gross × A3 rate. From January 2027 it should hold only the rate the employee requested in writing, never below the calculated rate (RIRPF art. 88.5).
3. Please send:
   - the YTD wage-type breakdown of 58165 − 58149. If it is arrears for prior years or another amount that art. 83.2 excludes, HRB is right; otherwise, please tell me why HRB leaves it out;
   - which accumulator feeds 58163.

Wallisson

## Texto ao Mohamed — versão longa (substituída pela curta)

Hi Mohamed,

I compared A3 and HRB for Elessent, October 2026 (8 employees), using the A3 rate report, the A3 calculation detail (July, one employee) and the HRB G2N (REF-P203-698).

1. Same method. Both follow RIRPF arts. 83–87: annual gross, less Social Security and EUR 2,000, the same scale and personal/family minimum, then (annual tax − tax already withheld) ÷ gross still to be paid. Taking HRB's own figures and only replacing 58149 with 58165 as the gross already paid, I get the A3 rate within 0.05 pp for the 6 employees where the A3 rate is not the "% Referencia".

2. Where they differ:
   a) Gross already paid this year. HRB's annual gross (58163) equals 58149 (Base subject to IRPF withholding, YTD) + 58117 for all 8 employees. A3 uses the full amount paid, which equals HRB 58165. The difference is between EUR 0 and EUR 579.53 per employee and lowers the HRB rate by 0.35 to 1.78 pp. Where the two fields are equal, HRB matches A3 (14.83% vs 14.82%).
   b) Rounding of 58118. HRB keeps 3 decimals, rounded (17.469% → 0.175). The rate is expressed with two decimals (RIRPF arts. 86.1 and 87.3.c), and the AEAT algorithm truncates (17.46%).
   c) Voluntary rate. In October, 58217 holds the A3 final rate for all 8 employees, including the 3 with "% Referencia" 0.00, so 2552 = gross × A3 rate. In the 5 "semiautomático" cases, the A3 rate is never below the "% Referencia" (equal in 2, higher in 3), which is in line with RIRPF art. 88.5 (an employee may only request a higher rate). From January 2027, 58217 should hold only the rate the employee requested in writing. It overrides the calculated rate, so it must never be below it (DD validation; RIRPF art. 88.5).

3. What I need:
   - the year-to-date wage-type breakdown of 58165 − 58149 for these employees. If the difference is arrears for prior years or another amount that RIRPF art. 83.2 excludes, HRB is right; if not, HRB must include it;
   - which accumulator feeds 58163 (58149 or 58165), as our CCG requires every taxable remuneration paid to date (§6.1.1).

Wallisson

## Fontes
- `raw/docs/oficiais/ES/2026-10-19-BOE-RIRPF-arts80-88.txt` (83.2, 85.1, 85.3, 86.1, 87.3, 88.5); `2026-10-19-BOE-LIRPF-Ley35-2006-consolidado.txt` (19.2.f, 57.1); `2026-10-19-AEAT-Algoritmo-Retenciones-2026-10sept.txt` (TRUNCAR, linhas 1284–1287 e 1410).
- CCG v1.6 (`Downloads\Spain_Payroll_Configuration_Guide_2026_v1_6 (1).docx`) §6.1.1 (YTD Gross); DD V5.1 Country Fields #23; WTC V4.7 (58149 "Gross Taxable Income YTM", 58163, 58165, 58217 sem fórmula de intermediário).
- Transcrições 27/10: `Downloads\Spain Transition to HRB.txt`; `Downloads\Meeting with Gomes, Wallisson(Global-V) (3).txt` (01:33:42–01:39:29).
