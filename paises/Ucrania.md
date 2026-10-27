---
tipo: pais
codigo: "UA"
etapa_research: "concluida"
etapa_research_data: "2026-09"
etapa_design: "em andamento"
etapa_design_data: 2026-09-28
etapa_producao: 
etapa_suporte: "5 aberto(s): HRBS-14255, HRBS-15216, SR-161, SR-414, SR-415"
etapa_suporte_data: 2026-10-27
ccg: "V1.5"
ccg_data: 2026-09-21
wtc: "V4.4"
wtc_data: 2026-10-26
dd: "V3.10"
dd_data: 2026-09-25
report_specs: "D5 v3; D6 v3; D1, 4DF, 1-PV, UA-INTREP sem versão no hub"
report_specs_data: 2026-08-20
sir: 
sir_data: 
payslip: "sem versão no hub"
skill: 
tickets_abertos: 5
tickets_conferidos_em: 2026-10-27
atualizado_em: 2026-10-27
---
# Ucrânia

> Hub do país. Índice: [[00-INDEX]] · Skill: não há

Clientes ligados: Altium Ukraine (principal), GSK Ukraine (implementação), SDL Ukraine (citado no campo Company Name). Quem abre quase todos os tickets HRBS é Nataliia Hahan (especialista local de payroll UA do lado Mercans) [INCERTO: papel/time exato não declarado]. BA: Lily Li. Dev: Michael Mukosi John. Product: Mohit Jain. Datas de ticket são aproximadas (~).

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-09 | WTC, CCG, DD e Report Specs entregues; versões vigentes (regra 8: maior versão citada): WTC V4.1, CCG V1.5, DD V3.10. Nos tickets, WTC V3.9 e CCG V1.5 estavam em draft em ~2026-09-21 (HRBS-14331); o chat de 2026-10-01 cita WTC V4.1 e DD V3.10. |
| [[design]] | 🔄 | 2026-09-28 | Specs D1, 4DF, D5, D6 em "In Review" (BA/Dev), faltando XML de amostra real; 1-PV (SR-414/415) em Open com perguntas da BA; Payslip (SR-340) In Progress com Dev. Advance Payroll sem especificação de desenvolvimento (HRBS-14255). |
| Produção (outro time) | — | | Ver [[fronteiras]] |
| [[suporte]] | 🔄 | 2026-10-27 | API 27/10: abertos: HRBS-14255 Open, HRBS-15216 Open, SR-161 In Review, SR-414 In Review, SR-415 In Review; 13 fechado(s): HRBS-12181, HRBS-12368, HRBS-12548, HRBS-12631, HRBS-13389, HRBS-13392, HRBS-13499, HRBS-14324, HRBS-14331, SR-160, SR-162, SR-163, SR-340. Antes (2026-09-29): 18 tickets nos snapshots; vários sem resposta nossa (ver Pendências). |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| WTC master (gsheet 1rhjGwFM…, renomeado Ukraine_Wage_Type_Catalogue_Mercans_V4.4 em 2026-10-26) | V4.4 (vigente; VC (2026-10-26, Draft): linhas 644–646 voltaram a 79497–79499 "Other Leave Payout" (na V4.2 viraram 79097–79099 e duplicaram os units 717–719; ver [[correcoes]]). W/X dessas linhas = No (mudança da Lily em 26/10), decisão pendente da fonte primária (Poryadok 100 p.3; 1266 p.3) | — | — | — |
| WTC master | V4.1 (histórico; depois V4.2 30/09, V4.3 09/10) | V4.1 sem data; V3.9 ~2026-09-21 | Ukraine_Wage_Type_Catalogue_Mercans | Histórico: V3.2 (WT 62964, D1 accrual 13) → v3.4 → v3.5 (79417 Mobilization) → v3.6 (79414 Donor leave, 79415 Business trip) → v3.7 → v3.8 (20 PEs de gross-up) → V3.9. Lily publicou o "Finalized WTC" em Google Sheets (~2026-09-21). V3.9 (draft nos tickets) → V4.1 (chat: mercans-compliance) com "correções de maternidade pendentes de input do cliente". |
| CCG | V1.5 (vigente: maior versão; draft nos tickets) | ~2026-09-21 | Ukraine_Country_Configuration_Guide_FY2026 | Histórico: Module 8 v1.1 (~08-05) → v1.2 (~08-11) → V1.3 (~09-08, Advance Payroll) → V1.5 (V1.4 não citada). |
| Data Dictionary | V3.10 (vigente: maior versão) | ~2026-09-25 (V3.10); ~2026-08-19 (V3.8) | Ukraine_Data_Dictionary | Histórico: V3.3 (part_time_indicator) → V3.4 → V3.5 (HRBS-12368) → v3.7 → V3.8 (+ incremento chief_accountant_name; tickets) → V3.10 (chat), com chief_accountant_name, categoria D5 corrigida, No-Data Reason do 1-PV. |
| Report Spec D1 (UA-D1-001_UnifiedSocialContribution) | atualizada ~2026-08-20 | | SR-160 | In Review; falta XML de amostra real. |
| Report Spec 4DF (UA-4DF-001_PersonalTax) | atualizada ~2026-08-20 | | SR-161 | In Review; QC da Lily (09-28) com correções para o Dev. |
| Report Spec D5 (UA-D5-001_LabourRelations) | v3 | ~2026-08-20 | SR-162 | In Review. |
| Report Spec D6 (UA-D6-001_SpecialSeniority) | v3 | ~2026-08-20 | SR-163 | In Review; validação contra formulário J0510611 (v11), não v10 (chat). |
| Report Spec 1-PV mensal (UA-1PV-001, template Derzhstat S0301016) | sem número | | SR-414 | Open; perguntas da BA de 09-29. Chat: "pronta" em 12-08. |
| Report Spec 1-PV trimestral (UA-1PV-002, template S0301121) | sem número | | SR-415 | Open. |
| Report Spec UA-INTREP-001 (relatório interno) | sem número | snapshot 12-08-2026 | (chat: mercans-compliance) | "Pronta; nada postado no ticket" naquela data. [INCERTO: situação atual; liga-se ao HRBS-12548] |
| Payslip (Payslip Spec 1; templates Ukraine EN/UK) | sem número | | SR-340 | In Progress (Dev); template × spec inconsistentes. |
| WTC do cliente Altium (WTC_Altium_Ukraine_2026_2) | — | | HRBS-14331 | Mantido pela Nataliia/cliente. Fora do nosso escopo. |

## Valores-chave (com vigência)
Conteúdo estatutário geral: não há skill de país. Abaixo, só o discutido em ticket/chat. Salário mínimo, base máxima do ESV e tetos de per diem foram afirmados pela solicitante, não confirmados por nós.

| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Coeficiente de gross-up de benefício não monetário | 1.219512, só na base do PIT | 2026 (ticket: "applicable for 2026") | | Art. 164.5 PKU; pp. 164.2.17 PKU (HRBS-12181) |
| Base do Military Levy e do USC sobre BIK | valor bruto, sem coeficiente | ⚠️ vigência? (posição DPS 2025-2026) | | §16-1, pidrozd. 10, rozd. XX PKU (HRBS-12181/14331) |
| Divisor do 62209 (Monthly bonus compensation) | 0.82 | ⚠️ vigência? | 0.77 (pedido, rejeitado) | Raciocínio sobre Art. 164.5 (HRBS-14331) |
| PIT | 18% | ⚠️ vigência? | | ⚠️ sem fonte (exemplo do HRBS-12181) |
| Military Levy | 5% | ⚠️ vigência? | | ⚠️ sem fonte (exemplo do HRBS-12181) |
| PIT Diia City | 5% | ⚠️ vigência? | | ⚠️ sem fonte (HRBS-14324, proposto pela solicitante) |
| ESV (USC) padrão do empregador | 22% | ⚠️ vigência? | | ⚠️ sem fonte (HRBS-12368/14331); chat: Lei 2464 ch.1 art.7 |
| ESV com deficiência | 8.41% sobre a base real, sem complemento até a base mínima | ⚠️ vigência? | | Instruction 449 s.III; DPS 04.02.2026 (HRBS-12631) |
| ESV do empregado | 0,00 (abolido) | 2016-01-01 | | Law 77-VIII (SR-160) |
| ESV: base mínima no mês de admissão/desligamento | não se aplica (incide sobre o salário real) | ⚠️ vigência? | | Instruction 449 s.III (HRBS-12631) |
| ESV sobre seguro de vida | Sim (só seguro médico e previdenciário são isentos) | ⚠️ vigência? | | Poryadok/Resolution 1170, p. 2, rozd. II (HRBS-14331) |
| ESV sobre maternidade (custeada pelo Pension Fund) | Sim, 22%; isenta de PDFO e Military Levy | ⚠️ vigência? | | p.1 ch.1 art.7 + ch.5 art.8 Lei 2464; p. 165.1.1 PKU (chat: mercans-compliance; HRBS-14331) |
| Salário mínimo | UAH 8.647 | 2026-01-01 | | ⚠️ sem fonte (Nataliia, HRBS-14331) |
| Base máxima do ESV | UAH 172.940/mês (20 × salário mínimo) | 2026 | | Lei 2464-VI, art. 7 parte 1 (Nataliia, HRBS-14331) |
| Per diem doméstico: teto | UAH 864,70/dia (0,1 × salário mínimo) | 2026 | | p. 170.9.1 PKU (Nataliia) |
| Per diem exterior: teto | EUR 80/dia, taxa NBU do dia | 2026 | | p. 170.9.1 PKU (Nataliia; confirmado: HRBS-14331 PDF, "For 2026 ... EUR 80 per calendar day") |
| Presente: parte não tributável | 25% do salário mínimo de 1º de janeiro (HRBS-14324); "25%" sem base (HRBS-12181) | ⚠️ vigência? | | subpar. 165.1.39 PKU (confirmado: HRBS-14324 txt, base = salário mínimo de 1º de janeiro; HRBS-12181 txt cita só "25% threshold", sem conflito) |
| Presentes de aniversário não tributáveis | PIT/Military = Não, 4DF 160 | ⚠️ vigência? | | p. 165.1.39 PKU (HRBS-14331) |
| Pagamento a FOP com comprovante de registro | PIT/Military/USC = Não, 4DF 157 (WT 62942) | ⚠️ vigência? | | p. 177.8 PKU (HRBS-14331) |
| Despesas de representação documentadas e publicitárias | isentas de PIT | ⚠️ vigência? | | Art. 170.9 PKU (HRBS-12181) |
| Prazo de PDFO/Military Levy | no momento da transferência (salário por banco); 3 dias bancários só para dinheiro/não monetário | ⚠️ vigência? | | TCU Art. 168.1, confirmado pela DPS (HRBS-12631) |
| Frequência do 4DF/D1 (pessoa jurídica) | mensal (só FOP: trimestral) | 2026-01-01 | | Law 4536-IX; MinFin Orders 4/243/284 (HRBS-12631) |
| Média de férias | 12 meses | ⚠️ vigência? | | Poryadok 100 p.2 |
| Média de donor leave e viagem | 2 meses; viagem paga o maior entre média e diária do mês | ⚠️ vigência? | | Poryadok 100 §8; LC Art. 121 §4; LC Art. 124 (donor) |
| Média de sick leave/maternidade | 12 meses (HRBS-12631/13392) × 6 meses (HRBS-14331) [INCERTO: contradição nossa] | ⚠️ vigência? | | Poryadok 1266 p.4 |
| Indexação | base month + índice acumulado (não é média) | ⚠️ vigência? | | Procedure 1078 |
| Compensação de férias não gozadas (79401) | média nova de 12 meses no desligamento | ⚠️ vigência? | | Poryadok 100, p. 2, segundo parágrafo |
| Proração de salário | dias úteis do horário | ⚠️ vigência? | | cartas de 27.05.2019 nº 4340 e 15.04.2019 nº 553 (emissores: Держпраці nº 4340 e Мінсоцполітики nº 553; confirmado: HRBS-12631 PDF, UTF-8) |
| Adiantamento (Advance Payroll): piso de cálculo | dias trabalhados × oklad puro, sem bônus; pagamento ao menos 2× por mês | ⚠️ vigência? | | Law 108/95-VR Art. 24; LC Art. 115 (HRBS-14255) |
| Fusão do Social Insurance Fund no Pension Fund | — | 2023-01-01 | | ⚠️ sem fonte (HRBS-14331) |
| Sick leave: quem paga | empregador dias 1-5; Pension Fund do 6º dia; PF desde o 1º dia para maternidade e cuidado de familiar | ⚠️ vigência? | | ⚠️ sem fonte (regras da Nataliia aceitas, HRBS-14331) |
| Sick leave: % por tempo de seguro | faixas divergentes (HRBS-13389 × HRBS-14331; ver Pendências) | ⚠️ vigência? | | ⚠️ sem fonte |
| Tributação de sick leave comum | 18% PDFO + 5% ML + 22% ESV (8.41% deficiência) | ⚠️ vigência? | | ⚠️ sem fonte (HRBS-14331) |
| Código de acréscimo do D1 para top-up ao salário mínimo (WT 62964) | 13 | ⚠️ vigência? | | MFU ordem 4 §IV (SR-160) |
| Envio do 1-PV trimestral | XML S0301121, assinado com KEP, só eletrônico | ⚠️ vigência? | | Law 2524-IX art. 10(4) (SR-415); portal: Кабінет респондента (Respondent's Cabinet; confirmado: SR-415 PDF) |
| Formulário D6 vigente | J0510611 (v11) | 2026-07-17 | J0510610 (v10) | DPS (chat: mercans-compliance, SR-163) |
| Per diem: parcela dentro do teto | não tributável (PIT/ML) | ⚠️ vigência? | | pp. 170.9.1 PKU (chat: mercans-compliance) |
| Grant direto da matriz estrangeira | entidade UA não é agente fiscal | ⚠️ vigência? | | p. 171.1 PKU (chat: mercans-compliance) |
| Stock options com recharge | 4DF 101, ESV Sim, gross-up 1,219512 no PIT, ML sobre o nominal | ⚠️ vigência? | | ⚠️ sem fonte (chat: mercans-compliance) |

## Decisões
- ~2026-04/05: a coluna de categoria de segurado do WTC não mapeia para o XML do D1; renomeada "Insured Person Type for ESV Engine" (20 = trabalho; 21 = contrato civil), filtro de motor; D1 Graf 8 vem de $hr.esv_category_code — nós, validado pela BA (SR-160).
- ~2026-05/06: part_time_indicator (0/1) no DD V3.3, obrigatoriedade M, sem default; WT 62964 com D1 accrual 13 — Lily corrigiu CM→M e concordamos (SR-160).
- ~2026-06/07: relatórios D1, D5, D6 e 4DF desenvolvidos em ucraniano (requisito estatutário) (SR-160).
- Antes de 2026-08: 1-PV mensal e trimestral ficam como specs separadas — não há base no Derzhstat para envio conjunto — Team Lead (chat: mercans-compliance).
- ~2026-08-03: não criar a série BIK "PIT sem Military Tax" — sem base legal; é diferença de base, não de incidência; WT 79417 Mobilization criado — nós (HRBS-12181).
- ~2026-08-05: donor leave (79414) e business trip (79415) novos; sick leave por outro regulamento (1266), não pela fórmula de férias — nós (HRBS-12631).
- ~2026-08-11: gross-up 1.219512 só na base do PIT; separação PIT/Military é regra de motor, não coluna Formula — nós (HRBS-12181). Mesmo dia: correções do CCG v1.2 (ver Correções).
- ~2026-08-12/13: gross-up só para benefício não monetário, limitado a 20 PEs (restrição do produto), em vez dos 109 códigos 4DF=126 — correção da Nataliia aceita; Lily/Dev desenvolvem (HRBS-12181, WTC v3.8).
- ~2026-08-13: DD V3.5 com 15 campos novos; salário em USD não entra no DD (é lógica de WTC) — nós (HRBS-12368).
- ~2026-08-19: dados históricos pré-go-live em grupo próprio do DD ("Historical Payroll Data (Pre-Go-Live Migration)"); indexação usa só o base month (Effective Date of Current Salary) — nós (HRBS-13392).
- ~2026-08-20: D1, D6, 4DF e D5 são anexos do formulário J05; 011/012/013 → HZ/HZN/HZU com C_DOC_STAN 1/2/3; HBOS/HBUH adicionados; D5 orientado a eventos (7 tipos); D6 com gatilho de 2 camadas — nós, com a BA (SR-160/161/162/163).
- ~2026-09-08: requisitos do Advance Payroll estão no CCG (Module 4 §4.2, Module 1 §1.2, Module 13); Mohit: não basta, falta especificação de desenvolvimento — nós; Product (HRBS-14255).
- ~2026-09-09/10: seguro de vida com USC=Sim; contractor FOP 4DF 157 no 62942; feriado/fim de semana trabalhado conta como dia inteiro na proração de bônus; catálogo do cliente Altium fora do escopo (mantemos só o master) — nós (HRBS-14331).
- ~2026-09-21: 65894 não existe e não será criado; PEs novos entram no WTC sem código e a Lily atribui — Lily/nós (HRBS-14331).
- ~2026-09-24: "staff" do 1-PV mensal = Labour Registry Person Category (D5) 1-2; categoria 3 (CPC) excluída; 1-PV trimestral: XML S0301121, KEP, só eletrônico — nós (SR-414/415).
- ~2026-09-25: campo chief_accountant_name no DD (alimenta o HBUH) — nós, pedido da Lily (SR-160).
- Mantido contra a objeção da Nataliia: ressalva "(if main place of work)" do contrato civil (CPC) na base mínima do ESV — nós (HRBS-12631) [INCERTO: sem tréplica].

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| ~2026-09-01 | HRBS-12181 | WTC update: BIK sem Military Tax e gross-up (Altium) | Resolved. Série "PIT only" recusada; gross-up só na base do PIT, não monetário, 20 PEs; WTC v3.8 finalizado. Pendente: 65806/65808 (Art. 170.9), uso do 4DF 169. · **HRBS-12181 Resolved em 2026-08-18** (API, 27/10) | Sim: WTC v3.4→v3.8, 79417 |
| ~2026-08-17 | HRBS-12368 | Data Dictionary e master data dos EEs (Altium) | Paused/SLA Exempt. DD V3.5 entregue. Pendente: pedido de apagar option mapper de Region, sem resposta. · **HRBS-12368 Resolved em 2026-08-18** (API, 27/10) | Sim: DD V3.5 |
| ~2026-08-07 | HRBS-12548 | Relatórios estatísticos (1-PV, sick leave do Pension Fund, internos) | Paused; sem resposta no ticket. Gerou SR-414/415 e UA-INTREP-001. Itens 3-4 (Tab. 2 do PF, template de salário médio) bloqueados por input do cliente (chat). · **HRBS-12548 Resolved em 2026-10-13** (API, 27/10) | Sim: specs 1-PV |
| ~2026-09-28 | HRBS-12631 | Reserva de férias, salário médio, revisão do CCG (Altium) | Pending on reporter. WTC v3.6 (79414/79415), CCG v1.1→v1.2. Pergunta da Nataliia sobre relatório de reserva de férias sem resposta. · **HRBS-12631 Resolved em 2026-10-13** (API, 27/10) | Sim: WTC v3.6, CCG v1.2 |
| 2026-08-18 | HRBS-13389 | Insurance Record (tempo de seguro) | Open; sem resposta nossa · **HRBS-13389 Resolved em 2026-08-23** (API, 27/10) | Não |
| ~2026-08-20 | HRBS-13392 | 12 meses de histórico de payroll (média) | Open (L2). Respondido: 3 elementos num grupo novo do DD. Duas réplicas da Nataliia sem resposta. · **HRBS-13392 Resolved em 2026-09-08** (API, 27/10) | Sim: DD (grupo novo) |
| ~2026-08-24 | HRBS-13499 | Data Dictionary GSK Ukraine | Open; sem resposta nossa · **HRBS-13499 Resolved em 2026-08-27** (API, 27/10) | Não |
| ~2026-09-11 | HRBS-14255 | Advance Payroll no nível país | Pending on reporter. Requisitos no CCG V1.3; Product pede especificação de desenvolvimento. | Sim: CCG V1.3 |
| 2026-09-08 | HRBS-14324 | Fórmulas de salário médio e benefício adicional | Open; sem resposta nossa · **HRBS-14324 Resolved em 2026-09-22** (API, 27/10) | Não |
| ~2026-09-23 | HRBS-14331 | Checagem do catálogo WTC do cliente Altium | Resolved, com 6 perguntas novas da Nataliia sem resposta · **HRBS-14331 Resolved em 2026-09-28** (API, 27/10) | Sim: WTC V3.9 (draft), CCG V1.5 (draft) |
| 2026-09-25 | HRBS-15216 | Data Dictionary check (obrigatoriedade, SSC Rate) | New, Unassigned; sem resposta nossa | Não |
| 2026-09-28 | SR-160 | Report Spec D1 (ESV) | In Review; HBOS/HBUH, chief_accountant_name; falta XML real | Sim: spec D1, DD |
| 2026-09-28 | SR-161 | Report Spec 4DF (PIT) | In Review; QC da Lily com 8 achados para o Dev | Sim: spec 4DF |
| 2026-09-28 | SR-162 | Report Spec D5 | In Review; spec v3; QC da Lily para o Dev | Sim: spec D5 v3 |
| 2026-09-28 | SR-163 | Report Spec D6 | In Review; spec v3; sample validado contra v11 (não v10) | Sim: spec D6 v3, DD (d6_duration_unit) |
| 2026-08-10 | SR-340 | Payslip UA | In Progress (Dev); template × Payslip Spec 1 inconsistentes · **SR-340 Done em 2026-10-14** (API, 27/10) | Não |
| 2026-09-29 | SR-414 | 1-PV mensal, SPEC | Open, prazo 2026-09-30; novas perguntas da BA de 09-29 | Sim: UA-1PV-001 |
| 2026-09-29 | SR-415 | 1-PV trimestral, SPEC | Open, prazo 2026-09-30; 2 perguntas da BA | Sim: UA-1PV-002 |

- Rascunhos de comentário SR-162: [[rascunhos/2026-10-11-youtrack-drafts/SR-162-2026-10-13-followup|11/10 2026-10-13-followup]] · [[rascunhos/2026-10-11-youtrack-drafts/SR-162|11/10]] · [[rascunhos/2026-10-11-youtrack-drafts/v-anteriores/SR-162-2026-10-13-followup-1244|11/10 v-anteriores/-2026-10-13-followup-1244]] · [[rascunhos/2026-10-11-youtrack-drafts/v1-sem-skill/SR-162|11/10 v1-sem-skill]] · [[rascunhos/2026-10-11-youtrack-drafts/v2-skill-sem-verificacao/SR-162|11/10 v2-skill-sem-verificacao]] · [[rascunhos/2026-10-14-youtrack-drafts/SR-162|14/10]] · [[rascunhos/2026-10-14-youtrack-drafts/v1/SR-162|14/10 v1]] · [[rascunhos/2026-10-14-youtrack-drafts/v2/SR-162|14/10 v2]] · [[rascunhos/2026-10-14-youtrack-drafts/v3/SR-162-editado-pelo-usuario|14/10 v3/-editado-pelo-usuario]] · [[rascunhos/2026-10-14-youtrack-drafts/v3/SR-162|14/10 v3]] · [[rascunhos/2026-10-15-youtrack-drafts/SR-162|15/10]] · [[rascunhos/2026-10-15-youtrack-drafts/v1/SR-162|15/10 v1]] · [[rascunhos/2026-10-15-youtrack-drafts/v2/SR-162|15/10 v2]]
- Rascunhos de comentário SR-414: [[rascunhos/2026-10-11-youtrack-drafts/SR-414|11/10]] · [[rascunhos/2026-10-11-youtrack-drafts/v1-sem-skill/SR-414|11/10 v1-sem-skill]] · [[rascunhos/2026-10-11-youtrack-drafts/v2-skill-sem-verificacao/SR-414|11/10 v2-skill-sem-verificacao]] · [[rascunhos/2026-10-14-youtrack-drafts/SR-414|14/10]] · [[rascunhos/2026-10-14-youtrack-drafts/v1/SR-414|14/10 v1]] · [[rascunhos/2026-10-14-youtrack-drafts/v2/SR-414|14/10 v2]] · [[rascunhos/2026-10-15-youtrack-drafts/SR-414|15/10]] · [[rascunhos/2026-10-15-youtrack-drafts/v3/SR-414|15/10 v3]] · [[rascunhos/2026-10-15-youtrack-drafts/v4/SR-414|15/10 v4]] · [[rascunhos/2026-10-15-youtrack-drafts/v5/SR-414|15/10 v5]] · [[rascunhos/2026-10-16-youtrack-drafts/SR-414|16/10]] · [[rascunhos/2026-10-16-youtrack-drafts/v1/SR-414|16/10 v1]] · [[rascunhos/2026-10-16-youtrack-drafts/v2/SR-414|16/10 v2]] · [[rascunhos/2026-10-16-youtrack-drafts/v3/SR-414-v5.6|16/10 v3/-v5.6]] · [[rascunhos/2026-10-16-youtrack-drafts/v3/SR-414|16/10 v3]]
- Rascunhos de comentário SR-415: [[rascunhos/2026-10-11-youtrack-drafts/SR-415|11/10]] · [[rascunhos/2026-10-11-youtrack-drafts/v1-sem-skill/SR-415|11/10 v1-sem-skill]] · [[rascunhos/2026-10-11-youtrack-drafts/v2-skill-sem-verificacao/SR-415|11/10 v2-skill-sem-verificacao]] · [[rascunhos/2026-10-14-youtrack-drafts/SR-415|14/10]] · [[rascunhos/2026-10-14-youtrack-drafts/v1/SR-415|14/10 v1]] · [[rascunhos/2026-10-14-youtrack-drafts/v2/SR-415-editado-pelo-usuario|14/10 v2/-editado-pelo-usuario]] · [[rascunhos/2026-10-14-youtrack-drafts/v2/SR-415|14/10 v2]] · [[rascunhos/2026-10-16-youtrack-drafts/SR-415|16/10]] · [[rascunhos/2026-10-16-youtrack-drafts/v1/SR-415|16/10 v1]] · [[rascunhos/2026-10-16-youtrack-drafts/v2/SR-415|16/10 v2]] · [[rascunhos/2026-10-16-youtrack-drafts/v3/SR-415-v1.5-so-linhas|16/10 v3/-v1.5-so-linhas]] · [[rascunhos/2026-10-16-youtrack-drafts/v3/SR-415-v1.8|16/10 v3/-v1.8]] · [[rascunhos/2026-10-16-youtrack-drafts/v3/SR-415|16/10 v3]] · [[rascunhos/2026-10-19-youtrack-drafts/SR-415|19/10]] · [[rascunhos/2026-10-20-youtrack-drafts/SR-415|20/10]] · [[rascunhos/2026-10-20-youtrack-drafts/v1/SR-415|20/10 v1]]
- Rascunhos de comentário SR-160: [[rascunhos/2026-10-14-youtrack-drafts/SR-160|14/10]] · [[rascunhos/2026-10-15-youtrack-drafts/SR-160|15/10]] · [[rascunhos/2026-10-15-youtrack-drafts/v1/SR-160|15/10 v1]] · [[rascunhos/2026-10-16-youtrack-drafts/SR-160|16/10]] · [[rascunhos/2026-10-16-youtrack-drafts/v3/SR-160-com-G21|16/10 v3/-com-G21]] · [[rascunhos/2026-10-16-youtrack-drafts/v3/SR-160-duas-excecoes|16/10 v3/-duas-excecoes]] · [[rascunhos/2026-10-16-youtrack-drafts/v3/SR-160-item1-sem-excecoes|16/10 v3/-item1-sem-excecoes]]
- Rascunhos de comentário SR-161: [[rascunhos/2026-10-14-youtrack-drafts/SR-161|14/10]] · [[rascunhos/2026-10-15-youtrack-drafts/SR-161|15/10]] · [[rascunhos/2026-10-15-youtrack-drafts/v1/SR-161|15/10 v1]] · [[rascunhos/2026-10-15-youtrack-drafts/v2/SR-161|15/10 v2]]
- Rascunhos de comentário SR-163: [[rascunhos/2026-10-14-youtrack-drafts/SR-163|14/10]] · [[rascunhos/2026-10-14-youtrack-drafts/v3/SR-163|14/10 v3]] · [[rascunhos/2026-10-15-youtrack-drafts/SR-163|15/10]] · [[rascunhos/2026-10-15-youtrack-drafts/v1/SR-163|15/10 v1]] · [[rascunhos/2026-10-16-youtrack-drafts/SR-163|16/10]]
- Rascunhos de comentário HRBS-15216: [[rascunhos/2026-10-16-youtrack-drafts/HRBS-15216|16/10]] · [[rascunhos/2026-10-16-youtrack-drafts/v3/HRBS-15216-anterior|16/10 v3/-anterior]] · [[rascunhos/2026-10-16-youtrack-drafts/v3/HRBS-15216-pedido-Lily|16/10 v3/-pedido-Lily]]
- [[rascunhos/2026-10-09-UA-SR-162-414-415-respostas|2026-10-09-UA-SR-162-414-415-respostas]]: Material de resposta SR-162/414/415 da Ucrânia (J05 XSD, 1-ПВ) com fontes oficiais

## Internal Certification (Análise de Reports)
> Frente 5: `frentes/certificacao/estado.md` · Método: [[analise-reports]] · Pasta: `internal-certification/Ukraine`

| Pacote | Período | Pass / Finding / NT | Recibo | Situação |
|---|---|---|---|---|
| Altium | ago/26 | 33 / 13 / 12 | Recibo DPS do J0500111 (aceito 21/09/2026) | Validado; 0 High / 4 Medium / 9 Low |
| Altium | set/26 | 9 / 4 / 7 | Não | Parcial (report de setembro não preparado); 0 High / 2 Medium / 2 Low |

- Cadeia bancária e GL de agosto fecham com o declarado. Medium: férias pagas em atraso; empregado tempo integral no master × meio período no Д1.
- Falta: recibo do 1-PV, XML desempacotados, dados de julho (C-10).
- [[rascunhos/2026-10-16-auditoria-1PV/achados_OUTRAS|achados_OUTRAS]]: Achados da auditoria UA 1-ПВ nas abas fora do Wage Fund Classification (Specs mensal/trimestral)
- [[rascunhos/2026-10-16-auditoria-1PV/achados_WFC_M_1|achados_WFC_M_1]]: Achados da auditoria da aba Wage Fund Classification mensal, linhas 1-200 (códigos 62100-62653)
- [[rascunhos/2026-10-16-auditoria-1PV/achados_WFC_M_2|achados_WFC_M_2]]: Achados da auditoria da aba Wage Fund Classification mensal, linhas 201-400
- [[rascunhos/2026-10-16-auditoria-1PV/achados_WFC_M_3|achados_WFC_M_3]]: Achados da auditoria da aba Wage Fund Classification mensal, linhas 401-578
- [[rascunhos/2026-10-16-auditoria-1PV/achados_WFC_Q_1|achados_WFC_Q_1]]: Achados da auditoria da Wage Fund Classification trimestral, linhas 4-289
- [[rascunhos/2026-10-16-auditoria-1PV/achados_WFC_Q_2|achados_WFC_Q_2]]: Achados da auditoria da Wage Fund Classification trimestral, linhas 290-578
- [[internal-certification/Ukraine/Altium - 2026-09/02 Validation/followups|followups]]: Altium - 2026-09: rascunhos de follow-ups (não enviados) com pedidos de documentos/dados pendentes ao cliente
- [[internal-certification/Ukraine/Altium - 2026-09/02 Validation/resumo_PT|resumo_PT]]: Altium - 2026-09: resumo em português dos achados da validação
- [[internal-certification/Ukraine/Altium - 2026-09/02 Validation/summary_EN|summary_EN]]: Altium - 2026-09: resumo em inglês dos achados da validação (versão para o cliente)

## Pendências
- [x] DD V4.3 (2026-10-20, SR-415): importada (gsheet 09:55) e comentário enviado (12:56 UTC). Campos novos `derzhstat_region_code`, `derzhstat_district_code`, `statistical_district_code` (Country Fields 86–88). Conferência em `Research Pipeline/Ukraine/2026-10-20-SR-415-DD-V4.3/CONFERENCIA.md`
- [ ] DD UA, Country Fields O85 (C_STI_ORIG), fora do pedido: o texto "= C_REG × 100 + C_RAJ…" virou fórmula no Google Sheets e aparece `#ERROR!` (V4.2 e V4.3). Corrigir na próxima versão — Wallisson
- [ ] SPR_SSCU (diretório de órgãos do Держстат): só existe publicada a versão de 2016 (`spr_sscu_2016.ZIP`), anterior à reforma distrital de 2020; os campos C_REG/C_RAJ do Держстат na DD V4.3 não têm lista de valores. Confirmar com cliente/Держстат os códigos atuais quando houver caso real — nós
- [ ] Spec D1 (UA-D1-001), linha 30: T1RXXXXG21 rotulado "Labour Book Indicator ⚠ UNVERIFIED" e mapeado pela BA a `$hr.labour_book_holder_indicator`; o formulário oficial J0510111 (coluna 21) diz "Ознака основного місця роботи (1 - так, 0 - ні)". Corrigir em versão própria, fora do SR-160 (ver [[correcoes]] 16/10) — nós/usuário _(ticket SR-160 fechado; pendência mantida: SR-160 (Done 20/10, Lily/Michael) tratou so regras Y/C/N, header, formato de data/milhar e teste de aceitacao; nenhum comentario menciona a coluna 21 (T1RXXXXG21 / Labour Book Indicator vs 'Ознака основного місця роботи'). O…)_
- [ ] Specs UA (2026-10-15, fora do pedido; não enviado): D1 linhas 46–47 (HBOS/HBUH) com colunas deslocadas (exemplo em L, mapeamento em M, explicação em N); 4DF linha 4 com Position "XML attr" (HZ/HZN/HZU são elementos); D6 linha 47 (D_FILL) com tamanho 10 (XSD: 8) e linhas 46 (G/M "only HZN/HZU") a alinhar com a resposta de 14/10 (LINKED_DOCS em branco); Ukraine_Data_Dictionary_V4.1 editado em 15/10 06:56, mas o DD ativo/linkado no monday é a V4.2 — confirmar quem editou e se a edição precisa ir para a V4.2 — Wallisson
- [ ] SR-415 / 1-PV trimestral r.3080 (2026-10-14, fora do pedido; não enviado): a linha conta só tempo parcial por contrato ou "за згодою працівника" (Роз'яснення 19.1.2-12/25-24, II.7); o DD `part_time_indicator` não separa tempo parcial por acordo de tempo parcial imposto pelo empregador (se este entra ou não na 3080 não está dito na fonte; a seção III trata de horas perdidas por transferência a tempo parcial por motivo econômico). Avaliar campo/opção no DD se houver cliente com esse caso — Wallisson
- [x] SR-163 / spec D6: C_REG, C_RAJ, C_STI_ORIG (linhas 40, 41, 45) obrigatórios e mapeados aos campos do DD; linhas 46/48 alinhadas com o D5; implementado e 'Testing ok in acceptance' pela Lily em 2026-10-19 (SR-163 Done) — Wallisson/Lily — _fechada em 27/10 (SR-163): Wallisson 14/10: C_REG/C_RAJ/C_STI_ORIG obrigatorios (XSD J0510611) nas linhas 40/41/45 e linhas 46/48 seguem a logica das 49/51 do D5; Lily 16/10 listou os mapeamentos dps_region_code/dps_district_code/dps_tax_authority_code,…_
- [ ] SR-160 / spec D1: C_REG/C_RAJ/C_STI_ORIG (Seção F, spec v3.3) e LINKED_DOCS (xsi:nil=true quando em branco) resolvidos e testados em 2026-10-20; resta verificar se o LINKED_DOCS do D1 segue a mesma regra de anexo (rótulo da linha do Додаток 1 na seção 06 não confirmado) — Wallisson _(reescrita em 27/10 a partir do SR-160)_
- [x] SR-162 / spec UA-D5-001: C_DOC_VER fixo 11, D_FILL DDMMYYYY/8, HBOS/HBUH mapeados a nomes e linha 30 (G19S) omitida ('undocumented field'); aplicado e 'Testing ok in acceptance' em 2026-10-16 (SR-162 Done) — Wallisson/Lily — _fechada em 27/10 (SR-162): SR-162 Done 16/10: Lily listou e Wallisson atualizou C_DOC_VER fixo 11 (linha 40), D_FILL DDMMYYYY/8 (linha 50), HBOS/HBUH mapeados a director_authorized_person/chief_accountant_name (linhas 53-54); linha 30 (T1RXXXXG19S) ficou…_
- [ ] SR-415 / spec UA-1PV-002 (achados de 2026-10-13, fora do pedido): r.3070 marcada "Q4 only" mas é trimestral (só 3080/3090/3100 são anuais); linhas 18/21/22 (r.7010/7030/7040 col. 1) como contagem, formulário pede média — Wallisson
- [ ] Resolver nossa contradição sobre o período-base do sick leave: 6 meses (HRBS-14331, colunas K/X) × 12 meses (HRBS-12631 e 13392) — nós (HRBS-14331 × HRBS-12631/13392) _(ticket HRBS-14331 fechado; pendência mantida: Nataliia 17/09 definiu o periodo de calculo do sick leave como 12 meses; Wallisson 21/09 acrescentou as regras ao Guide. Mas a coluna X da WTC foi preenchida por Wallisson em 09/09 como 'Sick leave: 6-month base' e o ticket nao…)_
- [ ] Confirmar as faixas de % do sick leave por tempo de seguro (HRBS-13389: <5 anos 60%, 5-8 80%, 8+ 100% × HRBS-14331: <3 50%, 3-5 60%, 5-8 70%, >8 100%); não sabemos quais valores entraram no CCG V1.5 — nós/Nataliia (HRBS-13389, 14331) _(ticket HRBS-14331 fechado; pendência mantida: falta conferir se o CCG V1.5 traz 50/60/70/100; Wallisson 18/08 (HRBS-13389) corrigiu a faixa do pedido: Art. 17 Lei 1105-XIV = 50/60/70/100% a <3, 3-5, 5-8, >8 anos (nao 60/80/100); Nataliia 'noted'. Nataliia 17/09 (14331) deu…)_
- [x] Código 4DF 128 para maternidade: alinhado em HRBS-14331 (Nataliia 24/09; Wallisson 25/09): 128 só no benefício do Pension Fund (65700-65712, ESV Yes), 79406 → 101; master WTC atualizada — _fechada em 27/10 (HRBS-14331): Nataliia 24/09: o 128 vale so para o beneficio de maternidade pago pelo Pension Fund (126/140 dias), financiado integralmente desde 2023; demais codigos 101/126. Wallisson 25/09 aplicou: 65700/01/02/10/11/12 ESV No->Yes (mantem…_
- [ ] Pós-Resolved do HRBS-14331 ainda abertas: stock options 62890-62899/62990-62999 (cenário A recharge+remuneração / B direto da matriz / C benefício fora da folha: confirmar com o cliente); código '102' e código 'sem imposto' apontados por Nataliia em 22/09 (imagens não capturadas, sem resposta no ticket) — nós/cliente (HRBS-14331) _(reescrita em 27/10 a partir do HRBS-14331)_
- [ ] Decidir o desenho final do gross-up de BIK: regra de motor × PE agregado 58134 (nunca construído) — Compliance/BA/Dev (HRBS-14331, HRBS-12181) _(ticket HRBS-14331 fechado; pendência mantida: Wallisson 21/09 sinalizou que o arquivo traz dois desenhos contraditorios (regra de motor, conclusao de 11/08, sem linha na WTC x aba 'BIK Gross Up' com PE agregado 58134 nunca construido) e que precisa de acordo…)_
- [x] HRBS-13389 (Insurance Record): respondido por Wallisson em 2026-08-18/20 (campo no DD V3.7, inteiro em dias, histórico total acumulado como valor inicial na contratação); Nataliia aprovou o fechamento em 2026-08-23; ligação ao WTC de sick pay 'ainda não construída' — _fechada em 27/10 (HRBS-13389): Wallisson 18/08 e 20/08 respondeu a Nataliia: campo Insurance Record (at Hire Date) no DD V3.7, Integer (dias), condicionalmente obrigatorio na contratacao, valor inicial = historico total anterior e acumula depois; ligacao ao…_
- [x] HRBS-13499 (campos GSK): respondido por Wallisson em 2026-08-24 — Insurance Record Type vale para todos os clientes UA; Grade 2, City of Work e Manager sem base legal (campos organizacionais da GSK, não entram no DD de país); Nataliia fechou em 2026-08-27 — _fechada em 27/10 (HRBS-13499): Wallisson 24/08: Insurance Record Type (anos/meses/dias) vale para todos os clientes UA (Art. 17 Lei 1105-XIV, Art. 19); Grade 2 / City of Work / Manager nao tem base na lei trabalhista/tributaria, sao campos organizacionais da…_
- [x] HRBS-14324 (fórmulas): respondido por Wallisson em 2026-09-09 (base horária Art. 107, paralisação Art. 113, gross-up Variante 1, presentes) e incorporado ao CCG; Lily, 2026-09-22: fórmula de média a criar depois dos requisitos — _fechada em 27/10 (HRBS-14324): Wallisson 09/09 confirmou os quatro itens e incorporou ao CCG: medias (Порядок 100/1266), presentes (isencao 25% do salario minimo), gross-up Variante 1 (coeficiente 1/0,82 so na base do PIT; ML sobre valor real), Art. 107…_
- [ ] HRBS-15216: respondido em 25/09 e 28/09 (mudanças no DD; SSC Rate retirado). Em 16/10 a Vaishnavi (Config) devolveu: campos de regulação são de nível de país, Config não altera; pede que nós levemos adiante. Falta: confirmar se as mudanças estão no DD vigente e para quem vai a aplicação no nível de país — nós/usuário (HRBS-15216)
- [x] Spec 1-ПВ trimestral, diferenças Spec → Sample: alinhadas na v1.5 do SR-415 (16/10)
- [ ] Specs 1-ПВ mensal/trimestral, auditoria completa de 16/10 (fora do pedido do SR-414/415; trabalho separado, a decidir com o usuário). Achados em `rascunhos/2026-10-16-auditoria-1PV/` (cópia dos relatórios): Wage Fund Classification com erros pela Інструкція 5/2004 (red. 17.01.2023 № 15) e Роз'яснення (horas extras 2.2.4 em 5040; prêmios 2.3.2 em 5070; seguro médico voluntário 3.5/3.30 no fundo; ЦПД em 5020/1070) e ~300 wage types que precisam de definição da BA/cliente; demais abas: 3070 marcada como só 4º tri, 1070/5010 sem exclusões (mobilizados, licença-maternidade/cuidado), File Structure (XSD, windows-1251), Роз'яснення de 2023 citadas, U15/U16 do mensal ("Not identified" → N1/N2), digitação ("Кабінет ресивальниця", "місяцна", "МОНТНА", "Зведоу", "ФДРПОУ"); Sample sem os elementos que os controles do Держстат exigem (RUK, VIK_TEL, VIK_EMAIL, CEP/cidade dos endereços, KATOTTG_FACT; OBL/RAY no mensal). Se a Sample for completada: KVED/N2 com NOMER = 1 e RAY de Kyiv dependem do Держстат (consulta em `rascunhos/2026-10-16-consulta-Derzhstat-1PV.md`) — nós/usuário (SR-414, SR-415)
- [ ] Format da ДПС (наказ 729): "Між елементами не допускаються знаки пробілів, табуляцій" — os templates XML do Dev são indentados; não verificado se o arquivo final sai sem indentação. Prova em `raw/docs/oficiais/UA/2026-10-16-VERIFICACAO-D6-schemaLocation.md` §4 — Dev/Lily; nós só conferir (SR-160–163) _(ticket SR-160 fechado; pendência mantida: Nenhum comentario de SR-160 a SR-163 trata de indentacao/espacos entre elementos do XML; os templates foram refeitos e testados em acceptance (Lily 'Testing ok'), mas o ticket nao prova que o arquivo final sai sem indentacao…)_
- [ ] Templates do Dev UA (16/10, fora do pedido; não comentado nos tickets). Conferido nos anexos (`raw/tickets/api/anexos/SR-16x/20261016-*`) e validado com lxml contra os XSD oficiais v11 (`raw/docs/oficiais/UA/j0500111-extraido/`):
  - **4DF (SR-161):** template vigente `20261016-0837 - personal_tax new template.xml` linha 6 `<C_DOC_SUB>104</C_DOC_SUB>` ✔ (J0510411.xsd: fixed="104"). Só a amostra anterior `20261016-0820 - Personal Tax Report test sample.xml` linha 6 tem `101` (XSD: "does not match the fixed value constraint '104'"); a mesma amostra traz valores sem decimais (linhas 37/39/42/44/47, ex. `T1RXXXXG03A` = `36000`; padrão do XSD `-?[0-9]+\.[0-9]{2}`). Amostra nova não anexada: conferir quando sair.
  - **D1 (SR-160):** root `xsi:noNamespaceSchemaLocation="J0510111.xsd"` (template e amostra de 16/10 07:53, linha 2) ✔. Hipótese do `J0510411.xsd` não confirmada (era o texto da tabela da Lily).
  - **D6 (SR-163):** template e amostra de 16/10 08:32, linha 2, `J0510610.xsd` (nome do schema **v10**) com `<C_DOC_VER>11</C_DOC_VER>` (linha 7); no pacote v11 o arquivo é `J0510611.xsd`. A validação contra o XSD não depende desse atributo; efeito na recepção da ДПС não verificado.
  - Nas três amostras, `C_REG`/`C_RAJ`/`C_STI_ORIG` vazios (D1, 4DF) ou ausentes (D6: "PERIOD_MONTH not expected, expected C_REG"); são obrigatórios no XSD. Os templates omitem a tag quando o campo do DD está vazio, então depende do dado da entidade de teste; TIN/HTIN/HKBOS de teste também falham no padrão — Dev/Lily; nós só conferir (SR-160/161/163)
- [ ] SR-414 (1-PV mensal), perguntas da BA de 29/09, prazo 30/09 vencendo: categoria de "external part-time", formato de arquivo na Report Matrix, "No-Data Indicator", "average FTE headcount", exclusões do staff (maternidade, cuidado, mobilizados, suspensos; licença sem vencimento da lei marcial → 79410?), campos de deviation flag (25%/10%), option mapper inexistente na coluna O — nós (SR-414)
- [ ] SR-415 (1-PV trimestral), prazo 30/09: colunas E/F da Wage Fund Classification após mudança dos 4DF; coluna V em vermelho — nós (SR-415)
- [ ] XML de amostra real: D1, D5 e D6 feitos e testados (SR-160 Done 20/10, SR-162 Done 16/10, SR-163 Done 19/10; HDDGV/HNDGV omitidos; D_FILL ajustado); falta fechar o 4DF (SR-161, In Review) — nós (SR-161) _(reescrita em 27/10 a partir do SR-160)_
- [ ] HRBS-13392: conferir linha a linha o texto atual dos Порядки 1266 (п.4) e 100 (п.4) por diferença de lista de exclusão entre sick pay e férias (hoje um conjunto único: 62180, 79401, 79415, 79408, 79468, ligado aos WTC) — nós (HRBS-13392; DD v3.9) _(reescrita em 27/10 a partir do HRBS-13392)_
- [ ] HRBS-12631: relatórios de reserva de férias mapeados pela Lily em 2026-10-13 (a enviar ao Dev); em aberto: código de acréscimo do D1 para 79414/79415 (TBC), rótulo 'theoretical' da semana 53 (oferecido, sem resposta) e discordância da Nataliia sobre CPC (mantida por Wallisson) — nós (HRBS-12631) _(reescrita em 27/10 a partir do HRBS-12631)_
- [ ] HRBS-12368: option mapper de Region removido (DD V3.6, 2026-08-17); resta confirmar com a Lily o salário USD no WTC (não entrou no DD; pedido de 2026-08-13 sem resposta no ticket) — nós (HRBS-12368) _(reescrita em 27/10 a partir do HRBS-12368)_
- [ ] HRBS-12181: confirmar com a Altium 65806/65808 (Art. 170.9: PIT=Não?) e uso do 4DF 169; resolver conflito de nomes do 65808 (HRBS-12181 e WTC v3.8: 65808 = Representation expenses (financial), 65810 = Life insurance; Nataliia no HRBS-14331 chamou 65808 de "Life Insurance (BIK)" e nossa resposta repetiu o rótulo; ver proposta em rev-UA) — nós/cliente (HRBS-12181, 14331) _(ticket HRBS-12181 fechado; pendência mantida: HRBS-12181 Resolved 18/08 sem resposta da Altium sobre Art. 170.9 (65806/65808 PIT) nem sobre 4DF 169. Conflito de nomes do 65808: em HRBS-14331 Nataliia o chamou de 'Life Insurance (BIK)' e Wallisson respondeu repetindo 126/ESV…)_
- [ ] HRBS-12548: Lily mapeou em 2026-10-13 (a enviar ao Dev) e Wallisson abriu SR-414/415 (1-PV) em 2026-08-10; sem tratamento registrado do relatório do Pension Fund de sick leave (Tab. 2) e dos relatórios internos de salário médio (sick/férias/viagem) — nós (HRBS-12548; chat: itens 3-4 bloqueados por certificado em papel × eletrônico) _(reescrita em 27/10 a partir do HRBS-12548)_
- [ ] Classificação de maternidade, recharge das stock options e 65805/65809 em 4DF 126 → 125 aguardam contato do cliente (Altium) (chat: mercans-compliance)
- [x] SR-340: ESV Payer Number = EDRPOU (mesmo valor) e Division fora da spec, confirmado por Wallisson em 2026-08-11 e aceito pela Lily; templates Payslip EN/UK alinhados e 'Testing ok in acceptance' em 2026-10-14 (SR-340 Done) — _fechada em 27/10 (SR-340): Wallisson 11/08: ESV Payer Number = mesmo valor do EDRPOU (nao ha registro ESV separado); Division (banking) nao corresponde a dado do sistema. Lily 12/08: nao requeridos na spec; Michael ajustou os templates; 'Testing ok in…_
- [ ] SR-163: possível erro do Dev ("Chief Accountant RNOCPP" → director_signatory_rnocpp) — Dev/nós [INCERTO] (SR-163) _(ticket SR-163 fechado; pendência mantida: SR-163 Done 19/10, mas nenhum comentario trata do campo 'Chief Accountant RNOCPP' ($legal_entity_hr.director_signatory_rnocpp, pedido por Michael 23/07). Os mapeamentos finais no ticket so citam HBOS->director_authorized_person e…)_
- [x] Versões vigentes decididas pela regra 8 (2026-10-05): WTC V4.1, DD V3.10, CCG V1.5. Resta apenas confirmar o paradeiro da V1.4 do CCG (não citada) — nós (chat × tickets)
- [ ] HRBS-14255: confirmar se Compliance precisa entregar algo além do CCG V1.3 — Lily/Mohit (HRBS-14255)
- [ ] Valores sem fonte (PIT 18%, Military 5%, ESV 22%/8.41%, salário mínimo, base máxima do ESV, per diem) a confirmar com fonte oficial — nós (várias)
- [[rascunhos/2026-10-16-consulta-Derzhstat-1PV|2026-10-16-consulta-Derzhstat-1PV]]: Consulta ao Держстат com 3 pontos abertos do 1-ПВ mensal/trimestral (SR-414/415)

## Consolidado da sessão 2026-10-13
- **J05 / Додаток 5 (D5):** pacote **v11** (наказ Мінфіну № 4 de 13.01.2015, na redação do № 243 de 07.05.2026; `raw/docs/oficiais/UA/j0500111-extraido/`); `C_DOC_VER` fixo "11". Categorias D5 v11 (nota 8): 1 = за основним місцем роботи; 2 = за сумісництвом; 3 = ЦПХ; 4/6 = догляд за дитиною; 5 = вагітність і пологи; 7/8 = військовослужбовці; 9 = гіг-спеціалісти (na v10 a nota 9 dizia 1 = com трудова книжка / 2 = sem). Data de vigência da v11 não confirmada. Cabeçalho: C_REG/C_RAJ = região/distrito do órgão territorial da ДПС ao qual o documento é entregue; C_STI_ORIG = C_REG × 100 + C_RAJ (наказ Міндоходів № 729, Додаток 1); datas DDMMYYYY.
- **1-ПВ** (наказ Держстату № 117 de 15.04.2024): XML S0301016 (mensal) e S0301121 (trimestral), windows-1251 (Format 3.1); PERIOD_MONTH = último mês do período (trimestre: 3/6/9/12), PERIOD_TYPE 1 mês / 2 trimestre (Format 3.1, Таблиця 1). р.1020 = fundo de salário de todos com acréscimo no mês, inclusive licença-maternidade/cuidado de filho (exceto benefício do seguro social), militares e demitidos (Роз'яснення № 19.1.2-12/24-24, II.1); р.1030 = ПДФО retido, sem o de incapacidade temporária, sem recálculo do ano anterior (II.2); controles I.8 (1030 < 1020; 1030/1020 × 100 ≤ 18). REASON_KOD: 34/37/39/40/42 para os 5 motivos do formulário (Держстат "Список причин"). Seção III (5010–5090) só штатні; 3080/3090/3100 só no IV trimestre.
- **Tickets:** SR-414 e SR-415 enviados em 13/10 (specs v5.0 e v1.4 no Drive compartilhado); SR-162 com rascunho e spec v3.2 no Drive (aguarda importação e envio). Ver [[sessoes/2026-10-13]].
- **Cabeçalho ДПС (DECLARHEAD), verificado em 2026-10-13 (revisto em 2026-10-14):** LINKED_DOCS e SOFTWARE podem ficar em branco no D5/D6 e vão com `xsi:nil="true"` (resposta do SR-162 em 14/10; spec D5 v3.2 mantida, a v3.3 com LINKED_DOCS preenchido NÃO foi adotada). Regra de conteúdo quando preenchido: só LINKED_DOCS e SOFTWARE podem ficar vazios (наказ 729/2013, Додаток 1, п. 7); elemento com valor vazio leva `xsi:nil="true"` obrigatório (п. 10.4; o exemplo oficial do Додаток 2 usa `<SOFTWARE xsi:nil="true">`). A frase "elemento ausente = vazio" do п. 10.4 fala do DECLARBODY, não do cabeçalho. **D5 é anexo** do Податковий розрахунок J05 001 (seção 06, р.065, v10 e v11): LINKED_DOCS do anexo = um DOC TYPE="2" apontando para o principal (TYPE 1 = principal → anexo; 3 = recibo). Diretório SPR_STI.XML (06.03.2026): 161 órgãos, C_STI = C_REG × 100 + C_RAJ em todos; 2650 = ГУ ДПС у м. Києві (26/50). Esses códigos são a numeração da ДПС, não o КАТОТТГ nem a "Oblast (Region)" do empregado no DD.
- **DD V4.1 (13/10, SR-162):** export ativa V4.0 (13/10 12:17) + Country Fields 83–85 (Legal Entity HR, Employer Information / Reporting Details: `dps_region_code`, `dps_district_code`, `dps_tax_authority_code`, azul claro) + linha 4.1 no Version Control; zero diferenças fora disso (conferido célula a célula). Base: `youtrack_tickets/SR-162/FINAL_Ukraine_Data_Dictionary_V4.1.xlsx` com a data da 4.1 corrigida para data (era texto). A 4.1 anterior (Insured Record, 30/09) nunca subiu ao Drive e já está dentro da 4.0 ativa; o `V4.2.xlsx` do Downloads (outra sessão) foi descartado. SPR_STI: 3100 = Центральне міжрегіональне управління ДПС по роботі з великими платниками (C_REG 31).

## Entregas (conferências)
- 2026-10-20 · SR-415 · DD V4.3: campos do Держстат para o 1-PV: [[Research Pipeline/Ukraine/2026-10-20-SR-415-DD-V4.3/CONFERENCIA|conferência]]

## Correções ligadas
Registradas em [[correcoes]] (via consolidação do grupo UA):
- Seguro de vida: USC Não → Sim (Poryadok 1170); contradizia nossa resposta do HRBS-12181 (HRBS-14331).
- 65894: changelog dizia que a linha foi criada; não existe e foi retirado (HRBS-14331).
- Divisor do 62209: 0.77 → 0.82 (HRBS-14331).
- CCG v1.2: prazo PDFO/ML, base mínima do ESV na admissão/desligamento, deficiência 8.41%, proração por dias úteis, 4DF mensal (HRBS-12631).
- CCG 8.2: lista de exclusão do 1266 aplicada às férias; citação do Social Insurance Fund (HRBS-14331).
- Gross-up: escopo de 109 códigos → só não monetários, 20 PEs; exemplo com base errada (2.360 → 2.439,02) (HRBS-12181).
- SR-163: sample D6 validado contra o formulário v10 superado → v11 (chat).
- Outras: ver lista completa em `correcoes-UA` do scratchpad.
- [[rascunhos/2026-10-05-pacote-skill-UA|2026-10-05-pacote-skill-UA]]: Pacote de correções confirmadas do design da Ucrânia (HRBS-12181/12631/14331, SR-160/162/163/414) para a skill

## Fontes
- raw/tickets/extracao/2026-10-02-tickets-UA.md
- raw/chats/2026-10-01-mercans-compliance.md (trechos sobre Ucrânia)
- raw/chats/2026-10-01-compliance-research.md e raw/chats/2026-10-01-mercans-design-dev-kb.md (sem trechos sobre a Ucrânia)
