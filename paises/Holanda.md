---
tipo: pais
codigo: "NL"
etapa_research: "concluida"
etapa_research_data: 
etapa_design: "aguardando"
etapa_design_data: 
etapa_producao: "Omnicom em Live/BAU"
etapa_suporte: "2 aberto(s): HRBS-14394, HRBS-14675"
etapa_suporte_data: 2026-10-27
ccg: v1.1
ccg_data: 
wtc: v3.3
wtc_data: 
dd: v1.0
dd_data: 
report_specs: 
report_specs_data: 
sir: 
sir_data: 
payslip: 
skill: "payroll-compliance-netherlands"
tickets_abertos: 2
tickets_conferidos_em: 2026-10-27
versoes_fonte: "nome do arquivo no Drive (Country Folders/Netherlands), lido em 2026-10-27; sem data de versão"
atualizado_em: 2026-10-27
---
# Holanda

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-netherlands` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | até 2026-09 | NL-CCG reconstruída após HRBS-10545; correção P13 V6 e test parts VTS v3 (cliente Mammoet) prontas; sign-offs do cliente pendentes |
| [[design]] | ⏳ | | [INCERTO] só o prompt de Client Manual variante NL e o fix pontual do bug do 30% ruling (2026-07-10) aparecem; sem design NL registrado |
| Produção (outro time) | — | | Omnicom em Live/BAU |
| [[suporte]] | 🔄 | 2026-10-27 | API 27/10: abertos: HRBS-14394 Open, HRBS-14675 Pending on reporter; 4 fechado(s): HRBS-10545, HRBS-1534, HRBS-5499, HRBS-9646. Antes (2026-09-21): HRBS-14675 sem resposta nossa; Mohit pediu ao Wallisson verificar se o report é statutory |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-netherlands`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano civil 2026, empregadores do setor privado, EUR, Holanda europeia. Fora: Caribe holandês (BES, sistema separado em USD), servidores públicos (Ufo 0,68% documentado, não construído), militares, zzp, regime de artistas/esportistas, Participatiewet. CAOs (~700) não construídos: nunca citar prêmio de hora extra como estatutário.
- **Órgãos:** Belastingdienst (loonheffingen), UWV (benefícios, polisadministratie), SZW (salário mínimo, tetos), Nederlandse Arbeidsinspectie, pensioenuitvoerder.
- **Relatórios principais:** Aangifte loonheffingen (mensal, via Digipoort M2M), Correctiebericht, Eindheffing WKR, Aangifte pseudo-eindheffing excessieve vertrekvergoedingen (única em papel), Jaaropgaaf, Loonstrook, UPA (pensão), Loonstaat.
- **Confiança da skill:** build do zero (2026-08-23), "READY FOR REVIEW". Abaixo do piso de 95%: UPA (~70%), layout do formulário em papel de vertrekvergoeding (~60%), durações/taxas WAZO (~75%). Parcial: tabela setorial Whk de 69 linhas (~85%; só 10 linhas publicadas), lista de feriados (~70%), listas de códigos do DD (90%, várias são ponteiros), IBAN `[VERIFY]`. Códigos `NL-xxx` do WTC são derivados (sem autoridade estatutária).

**Armadilhas confirmadas** (SKILL.md "Design clarifications")
1. Dois motores: LB/PVV com anualização não cumulativa (Lv = 54; F: mês 12, dia 260); prêmios WNV e Zvw usam VCR cumulativo → `01-ccg.md` §2–3 (engine)
2. Teto VCR é cumulativo, não fatia mensal (inhaaleffect; sem loontijdvak = sem prêmios; aanwas negativo ok para WNV, nunca para Zvw) → `01-ccg.md` (engine)
3. Maximumpremieloon 79.409 (dia 305,41 ÷ 260, congelado o ano todo, Wfsv art. 18(4)) vs maximumdagloon 304,25 / 309,91 desde 1 jul (÷ 261, só benefícios UWV e 70% de BW 7:629) → `01-ccg.md` §5 (engine)
4. Empregado ativo comum não tem dedução Zvw; empregador paga 6,10%; a bijdrage 4,85% só em casos listados, sobre o líquido; nunca as duas juntas → `01-ccg.md` (engine)
5. Prêmios de seguros de empregado 100% do empregador (Wfsv art. 20); exceção: até 50% do componente WGA do Whk, do líquido; ZW nunca recuperável → `01-ccg.md` §4.3 (engine)
6. `arkm2` 5.300 / `arkm3` 5.685 são tetos cumulativos; a Cijferbijlage imprime 132.290 por erro, o valor é 132.920 (arkg4) → `01-ccg.md`; QA U6a (engine)
7. Vakantiebijslag 8% limitado a 3x salário mínimo (6.883,20/mês até 30 jun; 7.011,00 desde 1 jul) → `01-ccg.md` §9 (engine)
8. Não existe prêmio estatutário de hora extra/noite/fim de semana; WML art. 13a só exige salário mínimo por hora → `01-ccg.md` §8 (engine)
9. Tabel bijzondere beloningen: dois percentuais (o de verrechening pode ser negativo) e jaarloon do ano anterior (ou estimativa para novo); arredondar a favor do empregado → `02-wtc.md` (engine)
10. AWf baixo (2,74%) exige J/J/N (indeterminado, escrito, não on-call); senão 7,74%; revisão retroativa (fim em 2 meses; >30% mais horas, limiar de 30 h/semana mudou em 2025) → `01-ccg.md`; `04-reports-spec.md` §1.7 (engine)
11. Digipoort é M2M real (WUS ≤ 15 MB, FTP; PKIoverheid); MBDZ limitado a 10 relações; não há relatório periódico UWV separado → `03-sir.md`
12. Sem eerstedagsmelding geral (só como sanção; desligar EDM); sem BSN/Opgaaf = anoniementarief 52%/108,30% → `03-sir.md`
13. Payslip deve trazer o salário mínimo da idade (14,71 → 14,99 em 1 jul 2026) e se o contrato é indeterminado/escrito/on-call, coerente com o AWf → `06-payslip.md`
14. Transitievergoeding usa tabela verde (sem arbeidskorting), máx. 102.000 ou 12 meses → `01-ccg.md` §10 (engine)

**O que mais dá errado** (do QA)
- Figuras de fontes secundárias erradas para 2026 estão corrigidas em U11; usar a skill, não fontes secundárias.
- Defeitos dentro de documentos oficiais: Cijferbijlage `arkg4`, narrativa Aof do Handboek §9.1 (U6a/U6c); offset de rótulo na tabela 12 (U10).
- Reverificar ao vivo (U13): Whk total e componentes (por empregador, pode ser negativo), classe de tamanho Aof (ano t-2), salário mínimo e maximumdagloon (semestral); banco do Belastingdienst mudou em 2026-05-01; Gegevensspecificaties v3.1 desde 2026-07-01.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- Conflito não resolvido no Handboek: limiar de comutação de pequena anuidade 5.429 (§9.3.6/§9.6.1) vs 5.513 (§3.3.1); não escolher lado (U6b).
- Faixa superior de 143.555 da tabela BB não reconstruível (U12).
- Fechar primeiro: Wet arbeid en zorg (U4), Codes voor de aangifte loonheffingen 2026 (U7), padrão SIVI UPA (U2).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Faixas LB/PVV | 35,75 / 37,56 / 49,50% | 2026-01-01 | Cijferbijlage LH-209 (2025-12-16) |
| Zvw (empregador) | 6,10% | 2026-01-01 | `01-ccg.md` (Wfsv) |
| AWf baixo / alto | 2,74% / 7,74% | 2026-01-01 | `01-ccg.md` |
| Aof baixo / alto; Opslag Wko | 6,27% / 7,63%; 0,50% | 2026-01-01 | `01-ccg.md` |
| Maximumpremieloon | 79.409/ano (305,41/dia) | 2026-01-01 | Wfsv art. 18(4) |
| Norma de renda da expatregeling (30%) | > 48.013; 30% em 2025-26, 27% desde 2027 | 2026-01-01 | Handboek §19.4 |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| CCG NL-CCG-001 | sem versão | reconstruída após HRBS-10545 (antes de 2026-08) | — | §7.1.4 "30% Ruling": cópia redlined gerada pelo drift-sync (HRBS-1534), aceite humano [INCERTO] |
| Correção P13 (Mammoet) | V6 | n/a | — | Passou em todas as checagens internas (14.226/14.226 cumulativos; gate 37 PASS/0 FAIL) (chat: mercans-compliance) |
| Test parts VTS (Mammoet) | v3 | n/a | — | Prontas para a Manju submeter |
| Report `netherland-ssc-pdf` | n/a | ~2026-09-15 | — | Custom Report, sem spec; % de SSI antigos; HRBS-14675 |
| Skill `payroll-compliance-netherlands` | n/a | n/a | skill Mercans | Existe |
| Prompt Master Client Manual (variante NL) | — | upload 2026-08-25 | — | Config sem fonte legal; qual variante (NL ou genérica) vale é [INCERTO] (chat: design-dev-kb) |

## Valores-chave (com vigência)
> Valores de HRBS-14675 foram **pedidos pelo solicitante e não validados por nós**. Conteúdo geral: ver a skill.

| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Norma salarial do 30% ruling (teste anual) | EUR 48.013 (anual, sem a allowance) | 2026 | | Belastingdienst (HRBS-10545) |
| Correção de aangifte de ano anterior | Depois do prazo do último período do ano: losse correctie (correctiebericht separado) por período, com software/tabelas do ano corrigido; erro achado pela empresa: enviar em até 8 semanas; Belastingdienst emite naheffingsaanslag ou teruggaaf pela diferença; belastingrente se a correção sair depois de 31/03 do ano seguinte. Corrigíveis em 2026: 2021–2025. Pagamento retroativo de 2025 feito agora não é correção: é salário de 2026 (loon-over só dentro do mesmo ano) | Handboek 2026 (versão março/2026) | | Handboek Loonheffingen 2026, §14.2.4 (pp. 248–249), §14.4 e 14.4.2 (pp. 251–252), §14.5.1 (p. 253), §9.2 (p. 176). PDF em raw/docs/oficiais/NL/ |
| 30%-regeling no prazo cheio de 60 meses | cai para 27% | 2027-01-01 | | Belastingplan 2025 (chat: mercans-compliance); confirmado: skill `01-ccg.md` Handboek §19.4.7 (30% em 2025 e 2026, 27% desde 2027; exceção: quem iniciou até 2023-12-31 mantém 30%) |
| Samenvoegbepaling | vigente | 2027-01-01 | | ⚠️ sem fonte |
| Betalingskenmerk | 16 dígitos, módulo 11, ainda obrigatório; não implementar clieop03 (substituído pelo SEPA em 2014) | 2026 | | Belastingdienst (HRBS-9646) |
| Deduções pré-tax admitidas na base do 30% ruling | só salary sacrifice; pensão e allowances (ex.: gym) não reduzem | ⚠️ vigência? | | "legislative aspect", artigo não citado (HRBS-1534) |
| ZVW | 6,10% | 2026-01-01 | | skill `01-ccg.md` (Wfsv; werkgeversheffing Zvw); pedido em HRBS-14675, não validado pelo solicitante |
| AOF Laag / Hoog / Uit | 6,27% / 7,63% / 7,63% | 2026-01-01 | | skill `01-ccg.md` confirma Laag 6,27% e Hoog 7,63%; "Uit" ⚠️ sem fonte (HRBS-14675, não validado) |
| AWF Laag / Hoog | 2,74% / 7,74% | 2026-01-01 | | skill `01-ccg.md` (HRBS-14675, não validado pelo solicitante) |
| WKO | 0,50% | 2026-01-01 | | skill `01-ccg.md` (Opslag Wko) (HRBS-14675, não validado pelo solicitante) |
| Config do prompt de Client Manual | PAWW 0,10; 30% ruling 0,30 / 0,27; exclusão por idade >67 em flags WGA/PAWW/ZW-Flex/Aof/Wko/AWf | ⚠️ vigência? | | ⚠️ sem fonte legal (chat: design-dev-kb) |

## Decisões
- antes de 2026-08: leave-relief do 30% ruling é configuração manual controlada pelo cliente, sem proração automática — HRBS-10545 — Team Lead/Wallisson (chat: mercans-compliance)
- antes de 2026-08: não implementar clieop03 — substituído pelo SEPA em 2014 — Team Lead (chat: mercans-compliance)
- ~2026-07 (resolução HRBS-1534): só salary sacrifice reduz a base do 30% ruling; dedução pré-tax de pensão e gym allowance não reduzem — "legislative aspect" — Wallisson (HRBS-1534; chat: compliance-research)
- 2026-07-10: bug do 30% ruling (valor cumulativo indo para bônus) resolvido com fix pontual, não redesign — bug fix tem escopo restrito por padrão — Mohit (chat: design-dev-kb)
- 2026-09-21: verificar se `netherland-ssc-pdf` é statutory report de compliance — Mohit Jain pediu ao Wallisson (HRBS-14675)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-10-27 | HRBS-14394 | Reabre HRBS-5499: PE 52990 "Maximum Social Security Base" exibe €5.509 (G2N de fev/2026); Config não altera PE de compliance | 15/10: teto 2026 confirmado (mês €6.617,41; tabel 11, Handboek Loonheffingen 2026). 27/10 (11:40 UTC): 52990 fora do WTC (Delete na v2.0, 31/07/2025); fórmula na configuração (L2, 14/10); pedido ao @mjain atualizar para os valores 2026. Aguardando Mohit | Não |
| 2026-10-28 | HRBS-16487 | Omnicom: residente na Áustria com imposto e previdência na Holanda; Mohit pediu a diferença no cálculo × residente | **Resolved em 02/11 pelo Mohit** ("requires proper research & development in order to release this feature"; sjalihal informa o cliente). Publicado 28/10 19:22 UTC (4-204234): mesmos passos e alíquotas; só a parte de prêmio do AHK (fator 0,77343 abaixo da idade AOW: €2.410 × €3.115; fator 0,04948 × 0,06398); ARK cheio; na idade AOW AHK €850, OUK €1.130, AOK €295. Fonte: Rekenvoorschriften 2026 v2, cap. 8 + anexo p. 4–6 × 10–12 (`raw/docs/oficiais/NL/2026-10-28-rekenvoorschriften-2026/`). Solução no sistema ($58207 só cheio/nenhum, segundo o Romano): Mohit | Não |
| 2026-09-21 | HRBS-14675 | Omnicom: report `netherland-ssc-pdf` com % de SSI desatualizados (2026); Reports diz que é Custom Report sem spec | Sem resposta nossa; Pending on reporter | Não |
| ~2026-07 | HRBS-1534 | 30% ruling: por que gym allowance e dedução pré-tax de pensão ficaram fora (Omnicom/Excerpta Medica) | Só salary sacrifice reduz a base | Sim, como proposta (redline em NL-CCG-001 §7.1.4 pelo drift-sync) |
| antes de 2026-08 | HRBS-10545 | 30% ruling: teste anual EUR 48.013; leave-relief manual | Respondido; NL-CCG reconstruída | Sim |
| antes de 2026-08 | HRBS-9646 | Betalingskenmerk | Módulo 11 de 16 dígitos obrigatório; não usar clieop03 | Não |

- Rascunhos de comentário HRBS-14394: [[rascunhos/2026-10-15-youtrack-drafts/HRBS-14394|15/10]] · [[rascunhos/2026-10-15-youtrack-drafts/v1/HRBS-14394|15/10 v1]] · [[rascunhos/2026-10-16-youtrack-drafts/HRBS-14394|16/10]] · [[rascunhos/2026-10-27-youtrack-drafts/HRBS-14394|27/10]]
- [[rascunhos/2026-10-05-HRBS-14675|2026-10-05-HRBS-14675]]: Rascunho HRBS-14675: relatório netherland-ssc-pdf com % de SSI antigos; atualizar para 2026

## Internal Certification (Análise de Reports)
> Frente 5: `frentes/certificacao/estado.md` · Método: [[analise-reports]] · Pasta: `internal-certification/Netherlands`

| Pacote | Período | Pass / Finding / NT | Recibo | Situação |
|---|---|---|---|---|
| Quest Software B.V. | set/26 | 60 / 9 / 5 | Não | Validação v1.2; Audit Report v1.1 emitido 14/10, v1.2 (correção Whk) e relatório interno v1.0 em 16/10 |
| Sherwin Williams (Valspar B.V.) | set/26 | 48 / 18 / 5 | Não (recibo de outro LH) | Validação completa v1.1 |
| Excerpta Medica B.V. | set/26 | 60 / 5 / 5 | Não | Validação v1.2 e Audit Report v1.1 (correção Whk, 16/10) |

- 2026-10-14: systematiek **loon-over** (decisão do usuário); outbound = Audit Report no modelo Mammoet, documentos ausentes como limitação de escopo (D-04).
- Achados principais: imposto do empregado em idade AOW (Excerpta e Sherwin, High), horas declaradas 176 × 173 (Medium), arquivo SEPA "Kantar" malformado (Quest), taxa Whk Quest 1,45% = taxa do setor 42 para pequeno empregador (Tabel 10; a v1.1 citava 1,25% da linha errada, corrigido em 16/10 — ver [[correcoes]]); falta só o porte no mededeling (Observation). Base: Handboek Loonheffingen 2026.
- 2026-10-16: feedback da Manju (relatório da Quest era para uso externo; quer versão interna com lacunas autoexplicativas e números reconciliados) → [[internal-certification/Netherlands/Quest Software - 2026-09/02 Validation/NL_Quest_2026-09_Internal_Validation_Report_v1.0.docx|NL_Quest_2026-09_Internal_Validation_Report_v1.0.docx]] em `02 Validation` (cadeia bruto→líquido→bases→imposto/prêmios→TotTeBet→banco/GL, 11 cartões de lacuna). Quest: Audit Report v1.2 + workbook v1.2; Excerpta: Audit Report v1.1 + workbook v1.2 (correção Whk).
- Falta: recibo Digipoort dos 3 (o Athul diz que não guardam confirmação da Belastingdienst; o pacote da Sherwin traz uma). Cobranças C-14/15/16 em rascunho.
- [[rascunhos/2026-10-20-DESCANSO-gate-pre-marko|2026-10-20-DESCANSO-gate-pre-marko]]: Assunto pausado: gate pré-Marko para parar o ciclo de erros nas entregas Mammoet NL
- [[rascunhos/2026-10-20-feedback-manju-montage-P09|2026-10-20-feedback-manju-montage-P09]]: Feedback à Manju sobre Montage P09 V12 (SUPERADO: FND-01/02/05/06 retirados)
- [[rascunhos/2026-10-20-mensagem-manju-P10|2026-10-20-mensagem-manju-P10]]: Mensagem à Manju com o relatório forense do P10 (Montage V7)
- [[rascunhos/2026-10-20-mensagem-manju-P11|2026-10-20-mensagem-manju-P11]]: Mensagem à Manju com o relatório forense do P11 (Montage V4) e dois pontos a confirmar
- [[rascunhos/2026-10-20-mensagem-manju-final-deliverables-P09-P13|2026-10-20-mensagem-manju-final-deliverables-P09-P13]]: Mensagem à Manju sobre Final deliverables P09-P13 (substituir, criar P12/P13)
- [[rascunhos/2026-10-20-mensagem-marko-final-deliverables|2026-10-20-mensagem-marko-final-deliverables]]: Mensagem ao Marko com as entregas finais Montage P09-P13 (após ok da Manju)
- [[rascunhos/2026-10-20-pedido-automation-P12-P13|2026-10-20-pedido-automation-P12-P13]]: Pedido/registro ao chat AUTOMATION para P12 e P13 (Montage)
- [[rascunhos/2026-10-21-entrega-V3-P12-P13-manju-marko|2026-10-21-entrega-V3-P12-P13-manju-marko]]: Entrega Montage P12/P13 V3 + nota v1.2 a Manju e Marko
- [[rascunhos/2026-10-21-marko-entrega-P09-P13-itens-nao-alterados|2026-10-21-marko-entrega-P09-P13-itens-nao-alterados]]: Entrega ao Marko com a lógica dos itens não alterados (OB-5), nota v1.3
- [[rascunhos/2026-10-21-montage-entrega-drafts-por-destinatario|2026-10-21-montage-entrega-drafts-por-destinatario]]: Drafts da entrega Montage P09-P13 organizados por destinatário
- [[rascunhos/2026-10-21-pedido-automation-EM01-P09-P13|2026-10-21-pedido-automation-EM01-P09-P13]]: Pedido ao AUTOMATION: aplicar a regra EM-01 do Marko em P09-P13
- [[internal-certification/Netherlands/Excerpta Medica - 2026-09/02 Validation/followups|followups]]: Excerpta Medica - 2026-09: rascunhos de follow-ups (não enviados) com pedidos de documentos/dados pendentes ao cliente
- [[internal-certification/Netherlands/Mammoet Montage - P13-2025/2026-10-21-V3/CONFERENCIA|CONFERENCIA]]: CONFERENCIA da entrega V3 Mammoet P12/P13 2025: correções EH/EM do relatório v3.0, fontes e antes/depois
- [[internal-certification/Netherlands/Quest Software - 2026-09/02 Validation/followups|followups]]: Quest Software - 2026-09: rascunhos de follow-ups (não enviados) com pedidos de documentos/dados pendentes ao cliente
- [[internal-certification/Netherlands/Sherwin Williams - 2026-09/02 Validation/followups|followups]]: Sherwin Williams - 2026-09: rascunhos de follow-ups (não enviados) com pedidos de documentos/dados pendentes ao cliente

## Pendências
- [ ] Decidir se `netherland-ssc-pdf` é statutory; se for, fornecer spec com % 2026 validados; se não, devolver ao Reports (Shaik Jani Sharif) — Wallisson — (HRBS-14675)
- [ ] Validar os % de SSI pedidos contra fonte oficial antes de passar ao Reports — Wallisson — (HRBS-14675)
- [ ] Sign-offs do cliente Mammoet: decisão 2559, recuperação de EUR 17,48, memo de systematiek — Wallisson/cliente — (chat: mercans-compliance)
- [ ] Reconciliação P09/P10 (Mammoet) — Wallisson — (chat: mercans-compliance)
- [ ] HRBS-14394: confirmar com o Mohit se o 52999 traz o mesmo teto por período (alternativa não incluída na resposta por falta de prova); leitura de regulations NL no backoffice dá 403 para nós — Wallisson
- [ ] Tickets do Statutory Alert 2027 prontos para colar — Wallisson — (chat: mercans-compliance)
- [ ] 28/10: Belastingdienst (ODB) publicou a Release LH2027 v1.6, a release definitiva da Loonheffingen Aangifte 2027, com Cao-lijst 01-2027 (xlsx/xml), Opmerkingen BD 01-2027 e Coderingenlandennatsector 1-1-2027. Os Rekenvoorschriften da versão Prinsjesdag ainda são provisórios. O Marko encaminhou ao grupo Compliance sem pedir nada. Insumo para o alerta de 2027; nada baixado — Wallisson — (Gmail 28/10)
- [ ] Redline §7.1.4 do NL-CCG-001: aceitar/rejeitar — humano (Wallisson) — (chat: compliance-research) [INCERTO]
- [x] O chat mercans-compliance lista "HRBS-10563 / Holanda / Modelo BCCC/BCCP"; confirmado em 2026-10-27 pelo ticket (campo País = Spain) que HRBS-10563 é da Espanha (ver [[Espanha]]); rótulo 'Holanda' no chat era erro. — _fechada em 27/10 (HRBS-10563): O ticket HRBS-10563 tem Pais = Spain (título 'Wage Type Configurations, Taxability Matrix, and Statutory Leave Logic Gaps'; menciona BCC/BCCP; Resolved 13/10/2026 por Lily Li). Confirma que o rótulo 'Holanda' no chat é erro._
- [ ] [INCERTO] Prompt NL de Client Manual com inconsistências (58202, permanent_disability, start_date vs begin_date, ordinais duplicados) — (chat: design-dev-kb)

## Entregas (conferências)
- 2026-10-20 · — · Mammoet Montage P09 2025: relatório forense v1.2 (set V12): [[internal-certification/Netherlands/Mammoet Montage - P09-2025/2026-10-20-forensic-v1.2/CONFERENCIA|conferência]]
- 2026-10-20 · — · Mammoet Montage P10 2025: relatório forense v1.0 (set V7): [[internal-certification/Netherlands/Mammoet Montage - P10-2025/2026-10-20-forensic-v1.0/CONFERENCIA|conferência]]
- 2026-10-20 · — · Mammoet Montage P10 2025: relatório forense v1.1: [[internal-certification/Netherlands/Mammoet Montage - P10-2025/2026-10-20-forensic-v1.1/CONFERENCIA|conferência]]
- 2026-10-20 · — · Mammoet Montage P10 2025: relatório forense v1.2: [[internal-certification/Netherlands/Mammoet Montage - P10-2025/2026-10-20-forensic-v1.2/CONFERENCIA|conferência]]
- 2026-10-20 · — · Mammoet Montage P11 2025: relatório forense v1.0 (set V4): [[internal-certification/Netherlands/Mammoet Montage - P11-2025/2026-10-20-forensic-v1.0/CONFERENCIA|conferência]]
- 2026-10-20 · — · Mammoet Montage P11 2025: relatório forense v1.1: [[internal-certification/Netherlands/Mammoet Montage - P11-2025/2026-10-20-forensic-v1.1/CONFERENCIA|conferência]]
- 2026-10-21 · — · Mammoet Montage P12 e P13 2025: V3: [[internal-certification/Netherlands/Mammoet Montage - P12-2025/2026-10-21-V3/CONFERENCIA|conferência]]
- 2026-10-21 · — · Mammoet Montage EM-01 aplicado: P09 V15: [[internal-certification/Netherlands/Mammoet Montage - P09-2025/2026-10-21-V15-EM01/CONFERENCIA|conferência]]
- 2026-10-21 · — · Mammoet Montage EM-01 aplicado: P10 V10: [[internal-certification/Netherlands/Mammoet Montage - P10-2025/2026-10-21-V10-EM01/CONFERENCIA|conferência]]
- 2026-10-21 · — · Mammoet Montage EM-01 aplicado: P11 V8: [[internal-certification/Netherlands/Mammoet Montage - P11-2025/2026-10-21-V8-EM01/CONFERENCIA|conferência]]
- 2026-10-21 · — · Mammoet Montage EM-01 aplicado: P12 V4: [[internal-certification/Netherlands/Mammoet Montage - P12-2025/2026-10-21-V4-EM01/CONFERENCIA|conferência]]
- 2026-10-21 · — · Mammoet Montage EM-01 aplicado: P13 V4: [[internal-certification/Netherlands/Mammoet Montage - P13-2025/2026-10-21-V4-EM01/CONFERENCIA|conferência]]

## Correções ligadas
- [[correcoes]]: resposta do 30% ruling (HRBS-10545) com lente de consultoria fiscal; correto: lente de provedor de software de folha (chat: mercans-compliance)
- [[correcoes]]: proposta de redesign completo para o bug do 30% ruling; correto: fix pontual (2026-07-10)
- [[correcoes]]: NL-CCG-001 §7.1.4 não dizia quais deduções pré-tax entram na base do 30% ruling (drift detectado, HRBS-1534); proposta de redline

## Fontes
- raw/tickets/extracao/2026-10-02-tickets-OUT.md
- raw/chats/2026-10-01-compliance-research.md
- raw/chats/2026-10-01-mercans-compliance.md
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- skill payroll-compliance-netherlands (lida em 2026-10-02)
- [[internal-certification/Netherlands/_tool/skill-references/2025/bijzondere-beloning-2025|bijzondere-beloning-2025]]: Referência oficial 2025 transcrita da Belastingdienst usada pela ferramenta de validação NL: bijzondere-beloning
- [[internal-certification/Netherlands/_tool/skill-references/2025/codes-2025|codes-2025]]: Referência oficial 2025 transcrita da Belastingdienst usada pela ferramenta de validação NL: codes
- [[internal-certification/Netherlands/_tool/skill-references/2025/controls-2025|controls-2025]]: Referência oficial 2025 transcrita da Belastingdienst usada pela ferramenta de validação NL: controls
- [[internal-certification/Netherlands/_tool/skill-references/2025/rates-2025|rates-2025]]: Referência oficial 2025 transcrita da Belastingdienst usada pela ferramenta de validação NL: rates
