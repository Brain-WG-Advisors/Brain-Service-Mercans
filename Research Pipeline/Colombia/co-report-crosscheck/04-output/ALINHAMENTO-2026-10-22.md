# Alinhamento pós-reunião, 22/10/2026 (rascunhos para revisão, nada enviado nem gravado)

## A. E-mail ao BAU (Reply all na thread "PMI Review") - RASCUNHO NO GMAIL v3 22/10, não enviado

Hi Heidy, Hi Cinthya,

Below is everything we still need from you to close the Colombia review. Please send it by Fri 23 Oct.

A. Files to send
1. The 871 electronic payroll files of September 2026, in one zip file, in a Google Drive folder shared with me. The folder 'September 2026 Payroll Validation Files' still shows 'You need access' for my account.

B. Questions (a short answer is enough)
2. Pensioners' run (CO - Pensionaries): are any of these pensions shared, or still to be shared, with Colpensiones? Yes / No. If Yes: how many are already recognised as shared, how many are still to be shared, and, for those still to be shared, is the pension contribution to Colpensiones paid today (inside or outside the payroll)? Why: it sets the pension type and the 'Pensión compartida' field of the pensioners' PILA file, and whether a pension contribution applies.
3. Does PMI pay a family compensation fund (CCF) contribution for any of its pensioners, inside or outside the payroll? Yes / No. If Yes, for how many? Why: the CCF contribution is optional for pensioners, so the pensioners' PILA file depends on it.

C. No action needed
- Q14 (late terminations) and Q17 (parafiscales on vacation): these are the rules the system will follow, as set in the specifications.
- Q16 (fractional vacation days): we will check it in the September files.

D. For the team that maintains the wage-type mapping (outside our scope)
While checking the specifications against your Conceptos CIR table, we noticed the points below. Wage-type classification is not part of our review, so please pass them to the team that maintains the mapping:
- WT 21330 and 25834 are marked as theoretical withholding. Only withholding actually practised enters Formulario 350 casilla 93 and Formulario 220 casilla 60 (ET arts. 378 and 379).
- WT 21644 (solidarity fund, pensioners) has no line in the table.
- WT 65820 (salary paid abroad) is on line 46; salary payments belong in casilla 36 under the Form 220 instructions.
- WT 62839 (AFC reimbursement) is mapped as an AFC contribution; a refunded deduction is not a contribution (casilla 57).
- WT 23552 'Income Tax - Benefit': its treatment is not defined in the table.
- Pensioners' run: your 21 Oct answer says only health is calculated. Pensions above 10 SMLMV also owe the solidarity pension fund contribution: 1% up to 20 SMLMV and 2% above (Ley 797 de 2003 art. 8).

Thanks a lot,
Wallisson

Fontes: perguntas 2 e 3 = AT3 v15 (campo 10 pp. 24-25; tabela 9 R6 pp. 107-108), conferido no PDF local em 22/10; Q2 completada e Q3 reescrita por sugestão do chat "Research Pipeline II" (22/10), que também confirmou que suas 6 perguntas de 21/10 (WT 21330/25834, 23552, 21644, 65820, 62839, aceite do 2276) eram mapeamento e não vão como pergunta. Bloco D: casillas 36/46/54/57 conforme o guia citado na CO-DIAN-004; FSP = Ley 797/2003 art. 8 (texto literal em RA-PENSIONERS-PILA-2026-10-21.md). Ponto interno (hub, não e-mail): os COP 1.613,1M da casilla 93 informados ao BAU em 19/10 incluem COP 69,3M do WT 21330.

## B. E-mail ao Mohit (cc Andy, Manju) - v2 após as notas do Gemini (checkpoint 22/10)

Subject: Colombia (PMI) – updated compliance artifacts and timeline

Hi Mohit,

The Colombia compliance review is closed and the artifacts are final on the Compliance Team Drive (Country Folders > Colombia). What changed for your design:
- New report spec CO-PILA-007: PILA for pensioners paid by the employer (Res. 2388/2016, Anexo Técnico 3). Health contribution only, 4% / 10% / 12% by pension band; no pension or ARL contribution.
- Nómina Electrónica (CO-DIAN-001): pensioners paid by the employer are in scope.
- Withholding (Formulario 350, Formulario 220, Formato 2276): totals cover employment income and pensions (Formulario 350 casillas 93 + 94); voluntary pension only for amounts deducted from the employee; six-month average per DIAN Concepto 4443 de 2025.
- PILA (CO-PILA-003): vacation paid in cash is outside the health and pension base but inside the CCF / SENA / ICBF base; no ARL contribution during enjoyed vacation.
- Termination date taken from the system Termination record (Nómina Electrónica, PILA, Formulario 220).
- Citations updated from Res. DIAN 000013 de 2021 to Res. 000227 de 2025 (specs, SIR, WTC, DD).
- CCG v1.3, WTC v1.5 and DD v1.2.

In today's checkpoint call the plan moved to completion in mid-December (parallel run / UAT sign-off by 18 Dec), so the 31 Oct design date no longer holds. In that plan the compliance fixes need to be developed by 20 Nov. Could you confirm when your team can start the Colombia design and the completion date, so I can update the project plan?

Thanks a lot,
Wallisson

## C. "Columbia Regulation Plan" (Google Sheet 1wTWKlU7vFBAoRDebSY3mtTgwu8lKAOAzpOCyXpzk5dw) - passo 1, célula a célula (proposto, não gravado)

### Aba Plan (coluna E = Status; novas linhas 51-52)
| Célula | Hoje | Proposto |
|---|---|---|
| E13 (Consolidate gap list and send to Mohit) | No Started | In Progress – artifacts final 22 Oct; e-mail to Mohit |
| E21 (Contingent Withholding Report) | Waiting – file not received (...) | Complete – BAU 21 Oct: manual report, not system-generated; outside Formulario 350 |
| E40 (Field verification – NE, F350, F220, F2276, Cesantías) | In Progress | Complete |
| E42 (Send the Contingent Withholding Report – Cinthya) | In Progress | Complete – BAU 21 Oct: manual report |
| E47 (Close the Compliance open points) | In Progress | Complete |
| E48 (Send remaining September runs, NE files, PILA flat file – Cinthya) | Not Started | In Progress – answered 16 and 21 Oct; no PILA flat file (Mi Planilla); pending: 871 NE files (requested 22 Oct) |
| E50 (Approve the specs and send the deltas to Mohit) | Not Started | In Progress – specs v1.0 on Drive 22 Oct; deltas to Mohit by e-mail |
| B51:E51 (nova) | – | Statutory report specs / New spec CO-PILA-007 – PILA for pensioners paid by the employer (Res. 2388/2016, Anexo Técnico 3 v15) / Wallisson Gomes / Complete |
| B52:E52 (nova) | – | Statutory report specs / Align CCG (v1.3), WTC (v1.5) and DD (v1.2) with the final specs and the BAU answers / Wallisson Gomes / Complete |

Sem mudança: E11, E12, E14 (nossas, seguem como estão), E24 (design, Mohit: esperar a resposta dele), E43/E44 (Cinthya).

### Aba Dependencies (números de linha antigos -> linhas atuais da aba Plan, pelo nome da atividade)
Mapa: dev/config +16 (40->24, 42->26, 44->28, 45->29, 46->30, 48->32, 49->33, 50->34, 51->35, 52->36, 53->37); specs +17 (57->40, 58->41, 63->46, 64->47, 65->48, 67->50); relatórios 16–38 -> 16–22.
| Célula | Hoje | Proposto |
|---|---|---|
| C3 | 16–38 (files received 15 Oct) | 16–22 (files received 15 Oct) |
| C4 | 58 | 41 |
| C5 | 8, 10, 11, 12, 14, 57, 63, 64, 65 | 8, 10, 11, 12, 14, 40, 46, 47, 48 |
| A6 / C6 | 40 / 8, 10, 13, 57, 67 | 24 / 8, 10, 13, 40, 50 |
| A7 / C7 | 42 / 13, 40 | 26 / 13, 24 |
| A8 / C8 | 46 / 44, 45 | 30 / 28, 29 |
| A9 / C9 | 49 / 44, 45, 48 | 33 / 28, 29, 32 |
| A10 / C10 | 51 / 49 | 35 / 33 |
| A11 / C11 | 52 / 42, 46, 49, 50, 51 | 36 / 26, 30, 33, 34, 35 |
| A12 / C12 | 53 / 52 | 37 / 36 |
| A13 / C13 | 64 / 65 | 47 / 48 |
| D13 | WT 21330 cannot be closed until the client confirms whether it is actual or hypothetical withholding | The specs state the rule (only withholding actually practised); wage-type classification goes to the mapping team |
| E13 | 23 Oct | 22 Oct (done) |
| A14 / C14 | 67 / 63, 64, 65 | 50 / 46, 47, 48 |
| E14 | 28 Oct | 22 Oct (specs approved v1.0) |

Datas de design em diante (E6-E12): passo 3, depois da resposta do Mohit.

## D. Notas do Gemini (checkpoint 22/10) - impacto nos rascunhos
- Decisões: (1) relatórios não estatutários numa aba separada (Andy; a aba "Out of Scope Reports" já existe); (2) Wallisson atualiza o plano e alinha a nova data com o Mohit; (3) teste em entidade nova e limpa, não réplica da PMI (Marko; tarefa da Cinthya).
- Manju perguntou se o Mohit sabe das mudanças nos artefatos -> o e-mail B lista as mudanças.
- Meta: conclusão em meados de dezembro (Dependencies: fixes 20 Nov, regressão 4 Dec, UAT 18 Dec).
- Wallisson disse que a revisão termina "esta semana" -> o prazo de 26/10 no e-mail A conflita; decidir 23/10 ou 26/10.
- Wallisson pediu ajuda em perguntas de artefato e a Cinthya pediu 4 horas para responder -> a frase "All our other questions are closed" do e-mail A só fica se essas perguntas (item 2) já estiverem respondidas.

## E. Gravação na planilha (22/10) - ESTADO PARCIAL, correção bloqueada
Erro nosso: a leitura gviz/CSV pula a linha 38 (vazia) da aba Plan; da seção "Statutory report specs" em diante as linhas reais são +1 em relação ao mapeado (C acima está errado nessa parte: PILA=40, NE etc.=41, cross-check=42, Contingent=43, Gantt=46, apply corrections=47, open points=48, BAU files=49, scope=50, approve specs=51; o mapa da aba Dependencies passa a ser -16 para tudo: 57->41, 58->42, 63->47, 64->48, 65->49, 67->51).
Gravado certo: E13, E21. Sem efeito (já era Complete): E40, E47.
Gravado ERRADO (falta corrigir): E42 = "Complete – BAU 21 Oct: manual report" (voltar para "Complete"); E48 = "In Progress – answered 16 and 21 Oct; ..." (deve ser "Complete"); E50 = "In Progress – specs v1.0 on Drive 22 Oct; deltas to Mohit by e-mail" (voltar para "Complete").
Ainda não gravado: E41 Complete; E43 "Complete – BAU 21 Oct: manual report"; E49 "In Progress – answered 16 and 21 Oct; no PILA flat file (Mi Planilla); pending: 871 NE files (requested 22 Oct)"; E51 "In Progress – specs v1.0 on Drive 22 Oct; deltas to Mohit by e-mail"; linhas novas 52-53; aba Dependencies inteira.
A correção pelo navegador foi bloqueada pelo classificador de permissões; decisão do usuário.

## F. Correção e conclusão da gravação (22/10, autorizada pelo usuário)
Plan (linhas reais): E42, E50 de volta a "Complete"; E48 = Complete; E41 = Complete; E43 = "Complete – BAU 21 Oct: manual report"; E49 = "In Progress – answered 16 and 21 Oct; no PILA flat file (Mi Planilla); pending: 871 NE files (requested 22 Oct)"; E51 = "In Progress – specs v1.0 on Drive 22 Oct; deltas to Mohit by e-mail"; linha 52 (CO-PILA-007) e 53 (CCG v1.3 / WTC v1.5 / DD v1.2), Wallisson Gomes, Complete.
Dependencies (mapa -16): A4 16–22; C3 16–22 (files received 15 Oct); C4 42; C5 8, 10, 11, 12, 14, 41, 47, 48, 49; A6-A14 24, 26, 30, 33, 35, 36, 37, 48, 51; C6 8, 10, 13, 41, 51; C7 13, 24; C8 28, 29; C9 28, 29, 32; C10 33; C11 26, 30, 33, 34, 35; C12 36; C13 49; C14 47, 48, 49; D13 "The specs state the rule (only withholding actually practised); wage-type classification goes to the mapping team"; E13 22 Oct (done); E14 22 Oct (specs approved v1.0).
Conferência: diff do arquivo inteiro contra o retrato tirado antes da 1ª gravação = 39 células (15 Plan + 24 Dependencies), exatamente as previstas; A4 conferida na tela (o gviz não lê essa célula). Out of Scope Reports sem mudança. Datas de design em diante (Dependencies E6-E12) e barras do Gantt: aguardam o Mohit.

## G. E-mails (22/10)
- E-mail ao BAU (v3, seção A): ENVIADO pelo usuário às 14:01 na thread "PMI Review" (conferido em Enviados).
- E-mail ao Mohit (v3): rascunho no Gmail, novo e-mail, Para mjain@mercans.com, Cc ahames@mercans.com e mshetija@mercans.com, assunto "Colombia (PMI) – report specs ready for design and timeline"; corpo conferido (14 linhas, assinatura 1x); não enviado. Aviso do Gmail: Mohit fora do escritório, volta amanhã (23/10).
- Mudanças da v2 para a v3 (comparativo realizado × timeline): "review closed" -> "specs final for design" + o que falta até 28 Oct; regra da PILA-007 corrigida (saúde 4/10/12, FSP 1%/2%, pensão só nos tipos que exigem, CCF opcional); ponto aberto do código TipoTrabajador na NE; local dos arquivos (Drive e Monday).

## H. Resposta da BAU (Heidy, 22/10 14:01) e imagem de status
- (1) zip com os 871 arquivos da NE compartilhado; pede confirmação de acesso. (2) Nenhum pensionado com pensão compartilhada com a Colpensiones. (3) A PMI não paga CCF para pensionados, nem dentro nem fora da folha (situação atual). (4) Pontos de mapeamento e FSP dos pensionados encaminhados ao time do mapeamento.
- Imagem de status refeita com isso: Research Pipeline/Colombia/2026-10-22-status/CO-status-2026-10-22.png (script status_img.py na mesma pasta).
- Rascunho Reply all na thread "PMI Review" com a imagem anexada (Heidy, Cinthya, Jose, Manju, Andy); não enviado.
- Rascunho do Mohit: a linha "Still open... BAU's answers on shared pensions and the CCF" ficou desatualizada -> ajustar antes de enviar.

## I. Ajustes finais (22/10)
- Rascunho do Mohit encurtado a pedido do usuário: assunto "Colombia (PMI) – specs ready for design; new dates?"; 4 parágrafos (specs prontas e onde estão + PILA-007; 31 Oct não vale, UAT 18 Dec, correções 20 Nov, pergunta das datas; delta até 28 Oct). Não enviado.
- Imagem de status refeita no design do "One-page – A4.png" (imagem que abriu a thread PMI Review em 14/10; logo recortado do original): Research Pipeline/Colombia/2026-10-22-status/CO-status-2026-10-22.png (script onepage_a4.py). Anexo do rascunho da thread PMI Review trocado por esta versão (1 anexo, 287 KB). Não enviado.
- Rascunho do Mohit reescrito a pedido (só alinhamento de data, sem falar de relatórios/documentos): assunto "Colombia (PMI) – timeline"; texto: ainda em revisão com o BAU dos artefatos do cliente para garantir que a pesquisa está robusta; pesquisa termina até o fim de outubro; nova data estimada de início do time dele: 20 Nov. Não enviado. Atenção: no plano do Andy, 20 Nov hoje é o fim do desenvolvimento das correções (Dependencies); atualizar depois da resposta do Mohit.

## J. Estado em 22/10 ~15h
- Correção de horário: o e-mail ao BAU (v3) foi enviado às 12:38; a resposta da Heidy chegou às 14:01 (seção G dizia 14:01 para o envio).
- E-mail ao Mohit "Colombia (PMI) – timeline": ENVIADO pelo usuário às 14:59 (conferido em Enviados).
- Imagem de status refeita (pílulas: Research completion end of Oct 2026 / Design start (estimate) 20 Nov; linha do Mohit; rodapé sem os marcos antigos; "received (one zip)"). O usuário tinha trocado o anexo por imagem no corpo e removido o texto; a imagem do corpo foi substituída pela nova (colada via área de transferência), corpo mantido como o usuário deixou. Rascunho na thread PMI Review, não enviado.
- Zip "09 September PMI Share.zip" no Downloads: 871 arquivos .txt (contagem sem abrir nomes/conteúdo).
- Rascunho da thread PMI Review: saudação recolocada acima da imagem ('Hi Heidy, Hi Cinthya, / Thank you for the answers and for the files. Below is the current status of the Colombia review, with what is pending and with whom.') e fecho 'Thanks a lot, Wallisson' abaixo da imagem; não enviado.

## K. Timeline alinhada com a imagem e o e-mail do Mohit (22/10, ~15h30, pedido do usuário)
Plan: E13 "In Progress – delta to Mohit's team by 28 Oct; research completion end of Oct"; E24 "Not Started – start 20 Nov (estimate, sent to Mohit 22 Oct); awaiting confirmation"; E49 "Complete – answered 16, 21 and 22 Oct; 871 NE files received 22 Oct; no PILA flat file (Mi Planilla)"; E51 "In Progress – specs v1.0 on Drive 22 Oct; delta to Mohit's team by 28 Oct".
Dependencies: E2 e E3 "31 Oct"; E6 "Start 20 Nov (estimate, sent to Mohit 22 Oct) – awaiting confirmation"; E7 "20 Nov – to be re-planned after Mohit's confirmation"; E11 "4 Dec – to be re-planned after Mohit's confirmation"; E12 "18 Dec – to be re-planned after Mohit's confirmation". E5 (28 Oct) sem mudança. Barras do Gantt não alteradas (aguardam o Mohit). Cada célula conferida na tela.
