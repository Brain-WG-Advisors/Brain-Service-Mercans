# Triagem 2026-10-22 — tickets atribuídos à Enaakshi (evats) e à Shruti (skamble)

> Janela Suporte, só leitura. Consulta `for: evats #Unresolved` (9) e `for: skamble #Unresolved` (16), baixados em `raw/tickets/api/2026-10-22-for-evats/` e `raw/tickets/api/2026-10-22-for-skamble/` (22/10 16:30). Nada gravado no YouTrack.
> Legenda: 🔴 pergunta aberta para a assignee | 🟡 aguardando outro time/reporter | ⚪ parado/sem ação de pesquisa.

## Enaakshi (evats) — 9
| Ticket | País/cliente | O que está pendente | Quem pediu, quando |
|---|---|---|---|
| 🔴 HRBS-16252 | Iêmen / BH | Confirmar os itens a) base só com o basic, d) joiners/leavers/licença e e) transporte na base de SS. O Aasim perguntou de novo (22/10 11:35) se o cálculo é mensal ou fixo em janeiro; o cliente cita o GCSS ("January of each year"). A descrição diz que o CCG usa base fixa basic+housing e que o WTC tira o transporte; o Suman diz o contrário (WTC inclui o transporte). **Conferir no YE-CCG-001/YE-WTC-001.** Trava UAT. | Suman 22/10 11:26 |
| 🔴 HRBS-15863 | Gana / BH | O teto do bônus (5% final) é 15% do basic anual ou do YTD? Se for anual, dar a lógica do basic anual com mudança de salário e com joiners/leavers no meio do ano ou do mês. | Mohit 21/10 07:34 |
| 🔴 HRBS-16015 | Iraque / BH | Confirmar que o OT não entra na base de SS (o Suman já respondeu que não entra). | Suman 21/10 05:47 |
| 🔴 HRBS-16234 | Filipinas / McDermott | Ninguém de compliance respondeu ainda. Pedido: tratamento de Maternity Benefit e Salary Differential (RA 11210) no IR, SSS, PhilHealth, HDMF e 2316, com referência legal, e impacto em 1601-C, R3, RF-1 e Alphalist. Go-live em 01/01/2027. | Config (Vaishnavi) 20/10: "assign to regulation team" |
| 🔴 SR-367 | Líbia, spec PIT mensal | O "Gross salary" inclui o Exempt Income Amount? A Lily acha que sim. | Lily 20/10 |
| 🔴 SR-369 | Líbia, spec SUF | O campo fixo é 1.00% ou 1.000%? | Lily 20/10 |
| 🔴 SR-472 | Dinamarca, e-indkomst v3.5 | Confirmar o Submission ID (IndberetningsID) dos registros 3101, 4101 e 5000. O mapeamento de 0013/0069 já foi alterado (Drew, 16/10). | Ruchi 13/10 |
| ⚪ SR-434 | Suíça, certificação Swissdec ELM | Sem comentários desde 15/09. É decisão de negócio (escritório local, contratos de CHF 4.500 + 9.000), não pesquisa. O campo País está como IN. | — |
| ⚪ CT-4287 | Austrália, validação de QA com RA | Status "Not Relevant", sem comentários, sprint passado de trimestre em trimestre. Candidato a fechar. | — |

## Shruti (skamble) — 16
| Ticket | País/cliente | O que está pendente | Quem pediu, quando |
|---|---|---|---|
| 🔴 HRBS-15790 | Egito / todas as entidades | Atualização de SI a partir de 01/01/2027: piso 3.200, teto 19.300, EE 11,5%, ER 19,25%. Em 21/10 o Mustafa corrigiu o valor anterior do ER para 18,75%. Ninguém de compliance respondeu. **Conferir na fonte oficial** (tabela da Lei 148/2019) e abrir a task de configuração antes das folhas de 08/01/2027. | Mustafa 09/10 e 21/10 |
| 🔴 HRBS-16029 | Singapura / GSK, SDL e 62866 | O Hayat respondeu às 6 perguntas em 21/10 (entidade 03-085, pago em dinheiro, acima de 4K, sem retroativo, sem aviso ao cliente). Falta abrir a mudança no WTC (62866 passa a CPF-able) e decidir os códigos 62867–62878. | Hayat 21/10 |
| 🔴 HRBS-15941 | Taiwan / British Council | Subsídio de creche: tributação, LI/EI/NHI, pagamento anual. Ninguém respondeu. A call com o cliente era em 20/10. | Archit 20/10 |
| 🔴 HRBS-3466 | Argélia / Henkel, relatório DAS | Falta a spec do relatório (por local, 2 arquivos, nome D"E"/D"S"+ano+CNSS). Pedida em 09/07; o relatório é necessário até o fim de dez/2026. | Vaishali 07/10 |
| 🔴 SR-105 a SR-110 (6) | Taiwan: SI Salary Adjustment, Termination, Joiner, SNHI, Payslip, Tax Report | "Spec Review only and fill the gaps in specs. Assign back to me." Nada feito desde então. Due dates de 2025, todos vencidos. | Mohit 15/09 |
| 🟡 HRBS-16010 | Reino Unido / McDermott, PGL1 | A Shruti pediu payload e mapeamento (20/10). O Mohit mandou o DPS Mapping (PGL1 LoanStartDate e PGL2 LoanStopDate em 58226, casando NINO com $hr.national_id) em 21/10. Agora é com a integração (Josh) comparar com a configuração. | Mohit 21/10 |
| 🟡 HRBS-14136 | Tailândia / GSK, EWF | O cálculo já está em produção. O relatório สกล.3 (TH-DLPW-001) foi para o dev em 16/10. **Primeira entrega em 15/11/2026.** | Shruti 16/10 |
| 🟡 HRBS-10878 | Vietnã / GSK, 58108 retro | A Shruti respondeu por inteiro em 06/10 (Lei 109/2025, Decreto 253/2026) com as mudanças de sistema. Pending on Development (CT-4468). | — |
| 🟡 HRBS-14988 | África do Sul / GSK, 4474 × 4493 | A Shruti respondeu em 05/10. A Vaishali cobra a configuração (Sohail) desde 09/10 e 19/10. | Vaishali 19/10 (para config) |
| 🟡 HRBS-15630 | Singapura / GSK (GWM), teto de AW | **Resposta nossa** (wgomes, 07/10): pedimos o YTD OW/AW (58553/58554) de 2 empregados. Sem retorno. | — |
| 🟡 HRBS-15764 | Singapura / GSK, MBMF top-up | Respondido em 09/10 (formulário MUIS, divisão conforme a escolha do empregado). Sem retorno; candidato a fechar. | — |

## Reatribuição (22/10, a pedido do usuário)
- Assignee trocado para wgomes pela API nos 17 pendentes (na pergunta ao usuário saiu "16", mas a lista nomeada tinha 17) (só o campo Assignee; Research Analyst dos SR mantido): HRBS-16252, HRBS-15863, HRBS-16015, HRBS-16234, SR-367, SR-369, SR-472 (eram da Enaakshi); HRBS-15790, HRBS-16029, HRBS-15941, HRBS-3466, SR-105, SR-106, SR-107, SR-108, SR-109, SR-110 (eram da Shruti). Conferido em `for: me #Unresolved` (18: os 17 + HRBS-15253, que já era nosso).
- Ficaram com elas: HRBS-10878, HRBS-14988, HRBS-15764, HRBS-15630, HRBS-14136, HRBS-16010, SR-434, CT-4287.

## Histórico de atribuição (activities da API, 22/10) — de quem era a demanda
Todos os 17 estavam com evats/skamble imediatamente antes da troca. Diferença entre "atribuído" e "pedido a ela":

| Ticket | Antes de wgomes | Como chegou | Nome dela aparece no ticket? |
|---|---|---|---|
| HRBS-16252 | evats | srai → evats 22/10, com @evats | Sim |
| HRBS-15863 | evats | mjain → evats 21/10, com @evats | Sim |
| HRBS-16015 | evats | srai → evats 21/10, com @evats | Sim |
| HRBS-16234 | evats | lbalamurugan → evats 20/10 ("assign to regulation team"), sem menção | Não (só no Assignee) |
| SR-367 | evats | lli → evats 20/10, com @evats; ela é Research Analyst e reporter | Sim |
| SR-369 | evats | lli → evats 20/10, com @evats; RA e reporter | Sim |
| SR-472 | evats | ela mesma pegou de rgupta 08/10; Ruchi: "you will check" (13/10) | Sim |
| HRBS-15790 | skamble | mjain → mshetija 16/10; skamble pegou para si 16/10 | Não (sem comentário de compliance) |
| HRBS-16029 | skamble | evats → skamble 16/10; Shruti respondeu | Sim |
| HRBS-15941 | skamble | anaik pediu à "Manju"; mshetija → skamble 20/10 | Não (pedido à Manju) |
| HRBS-3466 | skamble | clorincz pediu spec à Manju 09/07; mshetija → skamble 16/09 | Não (pedido à Manju) |
| SR-105 a SR-110 | skamble | mjain → mshetija → skamble 15/09 (1 min depois); comentário diz "Assigned to Manju"; RA = Manju Shetija | Não (Manju no comentário e no campo RA) |

**Decisão do usuário (22/10):** os 17 ficam com wgomes, inclusive HRBS-16029 e HRBS-15790 (da Shruti, sem repasse da Manju). Nenhuma devolução.

**23/10:** análises dos 7 da Enaakshi em `rascunhos/2026-10-22-enaakshi/` e dos 10 da Shruti em `rascunhos/2026-10-23-shruti/` (cada pasta com `00-CONSOLIDADO.md`). HRBS-15253 (Lituânia, já nosso) fica com a janela Pipeline por decisão do usuário (aviso de pipeline-c4): esta janela não mexe nele.
