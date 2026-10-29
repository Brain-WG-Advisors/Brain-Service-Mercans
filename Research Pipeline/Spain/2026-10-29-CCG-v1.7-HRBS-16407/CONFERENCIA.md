# CCG Espanha v1.7 — HRBS-16407 (2026-10-29)

> Hub: [[Espanha]] · Correções: [[correcoes]] · Ticket: HRBS-16407 (STG, país ativo → regra 9: ticket ao Development)

## Base
- `base/Spain_Payroll_Configuration_Guide_2026_v1_6-export-2026-10-29.docx`: exportação .docx do gdoc oficial (Drive > Spain > 05 - Payroll Regulation Guide > `Spain_Payroll_Configuration_Guide_2026_v1_6`, id 1DA44DOGM…, modificado em 18/09), baixada em 29/10 com ok do usuário. md5 fd22e524be31250298340e706a6eb1af.
- A v1.6 tem 60 alterações rastreadas abertas desde 17/09 e 11/06 (autor "Claude"), que foram mantidas como estavam. As alterações da v1.7 foram feitas no mesmo padrão: rastreadas, autor "Claude", data 2026-10-29.

## Final
- `Spain_Payroll_Configuration_Guide_2026_v1_7.docx` · md5 8cee645a6eaa64e2469eefeb854cc58d · abre no Word (146 páginas, 75 revisões). Edição direta no XML; as outras 23 partes do zip foram copiadas sem alteração.

## Antes → depois (texto com as alterações aceitas)
| Seção | Antes (v1.6) | Depois (v1.7) | Fonte |
|---|---|---|---|
| Tabela de versões | — | Linha 1.7, 29-Oct-26, Updated, Wallisson Gomes | — |
| 6.1.2 pseudo-código | `CEILING(TRUNCATE(New_Rate, 2))` → sugestão v1.6 `ROUND(New_Rate, 2)` | `TRUNCATE(New_Rate, 2)` (sem arredondar para cima) | RIRPF art. 86.1 (l. 2558) e 87.3.c (l. 2614), "dos decimales"; algoritmo AEAT 2026, l. 1284–1287, TRUNCAR (TIPO) no 2º decimal; mesma regra da própria CCG em 6.1 (6. Final Withholding Rate: "truncated to two decimal places") |
| 7.3.2 (8. Worked Example) | 41,67 isento, sem explicação | Nota nova: 41,67 é o valor da folha do HRBS-11310 (500/12), não é limite mensal; €500/ano por pessoa coberta, com a lógica de acumulado do 7.2 | LIRPF art. 42.3.c 2.º (l. 1877); RIRPF art. 46 |
| 12.1 Scenario 3 | Isento fixo de €41,66/mês; tributável 158,34; base 2.808,34; IRPF 421,25; líquido 2.033,755 | Isenção anual de €500 por pessoa coberta, pela lógica de acumulado: jan e fev isentos (€200 cada), mar €100 isento + €100 tributável, de abr em diante €200 tributável (no ano, €500 isento e €1.900 tributável). Admitido ou desligado no meio do ano tem os €500 inteiros. Janeiro: base 2.650,00; IRPF 397,50; líquido 2.057,50 | LIRPF 42.3.c; RIRPF 46; DGT V1967-17, conclusão 1ª |

## Conferência
- Contas refeitas: 200+200+100 = 500; 2.400−500 = 1.900; 2.650 × 0,15 = 397,50; 2.650 − 195 − 397,50 = 2.057,50.
- Diff do texto aceito (v1.6 → v1.7): só os 9 parágrafos acima mudaram.
- XML bem formado; zip íntegro (testzip); abre no Word.

## Pendente
- ~~Drive~~ feito em 29/10 com ordem do usuário: docx (id 1XQutYfvmte09ZuQTXPKO1aQF1J3ka_pb, md5 igual) + Google Doc via "Save as Google Docs" (id 1kkDXufXwhBD3cKEyCZ6AalpVBZ39NiygZB3n4M6mllg; exportação conferida: 20 inserções e 7 exclusões de 29/10 como sugestões, textos novos presentes, 41.66/mo e ROUND ausentes no texto aceito). Monday (Compliance Artifacts, Spain - ES, item 9278601265) aponta para o Google Doc. Link no draft do HRBS-16407.
- Ticket de alteração ao Development (rascunho: `ticket-dev.md`).

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-10-29 | suporte | v1.7 criada (6.1.2 TRUNCATE; 12.1 Scenario 3; nota no 7.3.2 §8) |
| 2026-10-29 | suporte | v1.7 no Drive (docx + Google Doc), monday e draft do HRBS-16407 |
