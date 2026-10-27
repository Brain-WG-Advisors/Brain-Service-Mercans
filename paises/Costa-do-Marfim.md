# Costa do Marfim (Côte d'Ivoire, CI)

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-cotedivoire`

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-08-12 (snapshot) | Skill file entregue, monolítico (refactor para thin-router pendente); 7 Report Specs (CI-CNPS-001/002/003, CI-DGI-001/002/003/004) prontas para upload no Drive (chat: mercans-compliance). Versão do CCG/WTC não citada [INCERTO] |
| [[design]] | 🔄 | 2026-08-25 | Regulation Design do Claude (48 regs) v1.0/v1.1, revisado pelo Mohit em 25/08, precisa de revisão (contas, fórmulas, linguagem); Accuracy Score v2 ≈85% (2026-08-14); spec do produto CT-A-620 (+621/622/623) atualizada ~2026-08-07 (chat: design-dev-kb; CT-A-620) |
| Produção (outro time) | — | | |
| [[suporte]] | 🔄 | 2026-09-28 | HRBS-14996 Pending on reporter (cliente escalou ao Marko); HRBS-14714 sem resposta formal |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-cotedivoire`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026 (calendário), setor privado, moeda XOF (sem subunidade), país único.
- **Órgãos:** DGI (ITS, contribuições patronais, État 301; portal e-impots.gouv.ci), CNPS (previdência, DISA, coleta CMU; e-CNPS), CNAM (CMU), FDFP (TA/TFPC), Inspection du Travail, ARTCI (dados pessoais).
- **Relatórios principais:** declaração mensal de ITS (DGI, dia 15 do mês seguinte); contribution employeurs CE/CN/TA/TFPC (DGI, mensal); État de régularisation ITS (anual, 15/fev); État 301 (anual, 30/mai ou 30/jun); CNPS (mensal se ≥20 empregados, trimestral se <20); DISA + DASC (anual, 31/mar); declaração nominativa CMU (CNPS).
- **Confiança da skill:** a skill é só o SKILL.md (sem `references/` nem relatório de QA). Cita um QA interno com 2 achados MAJOR não resolvidos (bandas de hora extra; classificação do prime de panier). Vários itens marcados `[VERIFY WITH RA]`; códigos de campo/máscaras dos formulários são DERIVADOS (não há formulário/XSD oficial na fonte).

**Armadilhas confirmadas** (o que a skill marca como erro)
1. Mecânica pré-reforma do ITS (F18): IS, CN do empregado, IGR, abatimento de 20%, quociente familiar e CNPS deduzido da base do ITS estão abolidos desde 01/01/2024; ITS único sobre o bruto total, RICF como crédito → SKILL.md §0, §3
2. Calculadoras web (talent.com etc.) e tabelas "0/10/15/20/25/35%" ou "150k/300k/600k" estão erradas; a tabela válida é 0/16/21/24/28/32% → §3.1
3. "CN empregador 1,2%" é outro tributo (vigente), não confundir com a CN do empregado abolida → §0 e §2.2
4. Tetos/SMIG de PDFs velhos: pensão 3.375.000 (não 1.647.315/2.700.000) e SMIG 75.000 (não 36.607/60.000); PF/AM/AT-MP têm teto **75.000** desde 2023-01-01 (o 70.000 é pré-2023; a skill ainda diz 70.000, corrigir) → §2.1, risco 5 [corrigido em 2026-10-16, ver [[correcoes]] 2026-10-15]
5. Divisão local × expatriado: CE 0% local / 9,2% expat; carga patronal de impostos sobre salário 2,8% → 12% → §2.2
6. Prime de panier: CCG/art. 23 CPS excluem do CNPS até 3× SMIG horário, mas o WTC a codifica como totalmente sociável (CI-TX-01); tratar como CI-TX-03 e sinalizar o WTC → §8 risco 3, §9
7. Abatimento de 320.000 XOF vale só para pensionistas, não para ativos → §3.3

**O que mais dá errado** (do QA citado na skill)
- Bandas de hora extra em conflito (WTC: 41-46/>46/noite +75/domingo-feriado +100; leitura do Código: 41-48/>48 e faixa +75% diurna de domingo/feriado) → §5.2
- Panier como CI-TX-01 no WTC contra o CCG → §8
- Classe de AT/MP (2 a 5%) depende do setor do cliente; confirmar com a CNPS

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- Bandas de hora extra (QA MAJOR-1) e panier (QA MAJOR-2), sem resolução
- Forfaits por cômodo do Arrêté 1028 (valores em XOF não estão na fonte)
- Faixa de ITS fixa para não residentes / tratados; limite de isenção das indenizações de rescisão; divisor diário de férias (26 ou 30); idade de aposentadoria CNPS
- Arrêté que fixa os campos obrigatórios do bulletin de paie; datas de feriados islâmicos 2026; artigo exato da LF2026 sobre e-impôts
- RICF 2,5 partes (198.000 anual) marcado como verificar

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| ITS (bruto total, sem abatimento) | 0% até 75.000; 16% até 240.000; 21% até 800.000; 24% até 2.400.000; 28% até 8.000.000; 32% acima (mensal) | 2024-01-01 | Ordonnance 2023-719; CGI art. 119 bis |
| RICF | 5.500/mês por meia parte acima de 1 (2 partes = 11.000; máx. 5 partes) | 2024-01-01 | CGI art. 120 |
| CNPS pensão | ER 7,70% / EE 6,30%, teto 3.375.000/mês | 2026 | Loi 99-477; CLEISS |
| CNPS PF / AM / AT-MP (ER) | 5% / 0,75% / 2-5%, teto 75.000/mês | 2023-01-01 | Communiqué CNPS de 11/01/2023 (Décret 2022-986); Loi 99-477 art. 23 (raw/docs/oficiais/CI/2026-10-15-VERIFICACAO-teto-CNPS.md e 2026-10-16-VERIFICACAO-complemento-teto-CNPS.md) (a ficha dizia 70.000, da skill/CLEISS: errado) |
| Contribution employeurs | CE 0% local / 9,2% expat; CN 1,2%; TA 0,4%; TFPC 1,2% | 2026 | CGI art. 134-146 |
| SMIG | 75.000 XOF/mês | 2023-01-01 | Décret 2022-986 |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| Skill `payroll-compliance-cotedivoire` | [INCERTO] | — | skill | Monolítica; refactor thin-router pendente (chat: mercans-compliance) |
| Report Specs (7) | — | 2026-08-12 (snapshot) | Drive (a subir) | CI-CNPS-001/002/003, CI-DGI-001/002/003/004 (chat: mercans-compliance) |
| Parecer HRBS-14996 (ITS / regime único) | 2ª versão | 2026-09-23 | YouTrack | Substitui o parecer de 22/09 (ver Decisões e [[correcoes]]) |
| Regulation Design CI (Claude, 48 regs) | v1.1 | jul–ago/2026 | — | v1.0 sem intern/apprentice/first-employment/senior officer nem teto 320k; corrigido na v1.1 (chat: design-dev-kb) |
| Accuracy Score | v2 | 2026-08-14 | CI_Accuracy_Score_v2.md | ≈85% (v1.0 contra os 18 regs do dev) (chat: design-dev-kb) |
| Spec CT-A-620 (CI: Specifications) + CT-A-621 Taxable Gross, CT-A-622 Gross, CT-A-623 Tax Table | — | ~2026-08-07 (sub-artigos 2026-08-05) | YouTrack KB | Autoria Mohit Jain; spec de configuração do produto |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Teto CNPS PF / maternidade / AT-MP | 70.000 XOF/mês | 2025-01-01 ❌ | 2022-12-31 | CLEISS CI (HRBS-14996; chat: mercans-compliance). ❌ Vigência errada: o 70.000 é anterior a 2023 (página "Employeur" e guia de 2021 da CNPS). Ver [[correcoes]] 2026-10-15 |
| Teto CNPS PF / maternidade / AT-MP | 75.000 XOF/mês (900.000/ano; 225.000/trimestre) | 2023-01-01 | — | Communiqué CNPS de 11/01/2023 (Décret 2022-986); Loi 99-477 art. 23 (raw/docs/oficiais/CI/2026-10-15-VERIFICACAO-teto-CNPS.md e 2026-10-16-VERIFICACAO-complemento-teto-CNPS.md) |
| SMIG (piso da assiette, NÃO é teto) | 75.000 XOF/mês | 2025-01-01 ❌ | — | CLEISS CI (HRBS-14996). ❌ Vigência real 2023-01-01 (linha abaixo) e o SMIG também é o teto de PF/AM/AT-MP |
| SMIG = piso de todos os ramos CNPS | 75.000 XOF/mês | 2023-01-01 | — | Communiqué CNPS de 11/01/2023 (Décret 2022-986); Loi 99-477 art. 23 (raw/docs/oficiais/CI/2026-10-15-VERIFICACAO-teto-CNPS.md e 2026-10-16-VERIFICACAO-complemento-teto-CNPS.md). Nenhum decreto posterior encontrado (⚠️ só fontes secundárias, 2026-10-16) |
| Teto CNPS pensão | 3.375.000 XOF/mês (45 × SMIG) | 2025-01-01 ❌ | — | CLEISS CI (HRBS-14996). Valor certo, vigência real 2023-01-01 (linha abaixo) |
| Teto CNPS pensão | 3.375.000 XOF/mês | 2023-01-01 | — | Communiqué CNPS de 11/01/2023 (Décret 2022-986); Loi 99-477 art. 23 (raw/docs/oficiais/CI/2026-10-15-VERIFICACAO-teto-CNPS.md e 2026-10-16-VERIFICACAO-complemento-teto-CNPS.md) |
| Prestações familiares (ER) | 5% | 2025-01-01 | — | CLEISS CI (HRBS-14996) |
| Maternidade (ER) | 0,75% | 2025-01-01 | — | CLEISS CI (HRBS-14996) |
| AT/MP (ER) | 2–5% (cliente aplica 3%) | 2025-01-01 | — | CLEISS CI (HRBS-14996) |
| Máximos no teto (EE pensão / ER pensão / PF / AM / AT-MP 3%) | 212.625 / 259.875 / 3.500 / 525 / 2.100 XOF | derivado dos tetos | substituído em 2026-10-16 | cálculo de Wallisson (HRBS-14996), feito sobre o teto errado de 70.000 |
| Máximos no teto (EE pensão / ER pensão / PF / AM / AT-MP 3%) | 212.625 / 259.875 / 3.750 / 562,50 / 2.250 XOF | 2023-01-01 (derivado) | — | 6,3% e 7,7% × 3.375.000; 5%, 0,75% e 3% × 75.000 |
| CN empregador | 1,2% | 2026 (skill; data de início não informada) | — | CGI art. 146 (confirmado: skill §2.2; CT-A-620 reg. 4111, taxa 1,20) (citado por Wallisson, HRBS-14996) |
| CE expatriados | 9,2% (local 0%) | 2026 (skill; data de início não informada) | — | CGI arts. 134 e ss., 146 (confirmado: skill §2.2; CT-A-620 reg. 4111, taxa 9,20 com Worker Type = 1) (HRBS-14996) |
| Prime de transport isenta (Abidjan) | 30.000 XOF (Bouaké 24.000; demais 20.000); excluída do CNPS uma vez por mês | 2020-01-30 | — | Arrêté n° 2020-012/MEPS/CAB; CPS art. 23; NS n° 054/MFB/DGI-DLCD (chat: mercans-compliance; HRBS-14996) |
| RICF | 11.000 por parte acima de 1 (11.000 para 2 partes), mensal | 2024-01-01 | — | CGI art. 120 (confirmado: skill §3.2; CT-A-620 reg. 4171: MAX((58205 − 1) × 11.000; 0)) (HRBS-14996) |
| Faixas ITS | 0% até 75.000; 16% até 240.000; 21% até 800.000; 24% até 2.400.000; 28% até 8.000.000; 32% acima (mensal, sobre o bruto total, sem abatimento) | 2024-01-01 | — | Ordonnance 2023-719; CGI art. 119 bis (confirmado: skill §3.1; aritmética conferida por Wallisson, HRBS-14996) |
| Regime pétrolier (prestataires de services pétroliers): forfait sobre faturamento | 6% exploração / 2,17%; cobre impostos sobre salários (sem ITS na folha se inscrita); CNPS e CMU continuam devidos | LF 2019; taxas desde LF 2022 | — | CGI art. 1068 e ss.; Annexe fiscale 2019 art. 26, 2022 art. 9, 2025 art. 14 (chat: mercans-compliance) |
| Teto de faturamento do impôt des microentreprises | 200.000.000 XOF/ano | ⚠️ vigência? | — | DGI, Le Système Fiscal Ivoirien [INCERTO se a fonte cobre o teto] (HRBS-14996) |
| Previdência privada, cap | 320.000, anual e cumulativo (EE 10%, MIN(base; 320.000)) | ⚠️ vigência? | — | CCG; decidido por Mohit 2026-08-25 (chat: design-dev-kb) |
| CNPS pensão EE / ER | 6,30% / 7,70% | 2026 (skill; data de início não informada) | — | Loi 99-477; CLEISS (confirmado: skill §2.1; CT-A-620 reg. 4041) |
| Carta DGI aceitando o IFPGAZ 2025 | nº 0984/MFB/DGI/DGE | 2025-08-19 | — | carta DGI anexada pelo cliente (HRBS-14996) |
| CT-A-620 (Mohit, configuração; valores lidos do PDF original): CNPS pensão (reg. 4031) piso 900.000 / teto 40.500.000 (flag Intern/Apprentice 58216 ≤ 1, ou seja, não aprendiz) e 450.000 / 450.000 (aprendiz, 58216 = 2); CNPS PF/AM/AT-MP (reg. 4061) 840.000 / 840.000 (58216 ≤ 1) e 450.000 / 450.000 (aprendiz, 58216 = 2); CMU (reg. 4051) 6.000 / 6.000 (a extração do PDF também mostra uma banda 'Employer Rate 100, 6.000 / 6.000' no início da reg. 4061, provavelmente a CMU do empregador); DGI: CE 9,20% (Worker Type 58215 = 1) e CN 1,20% (reg. 4111, só se 58203 ≠ 1), TA 0,40% e TFPC 1,20% (reg. 4121); capping de estagiários 1.800.000 (regs. 4081/4091, conta YTM acumulada, 58216 = 1) | valores equivalem a 12 × os mensais da skill (900.000 = 12 × 75.000; 40.500.000 = 12 × 3.375.000; 840.000 = 12 × 70.000; 6.000 = 12 × 500; 1.800.000 = 12 × 150.000), ou seja, tratados como anuais/cumulativos; as taxas 9,20 / 1,20 / 0,40 / 1,20 são percentuais (não valores anuais) | 2026 (spec de 2026-08-05) | — | PDF original de CT-A-620 (raw/tickets/youtrack_tickets/21 …pdf); confirmado: skill §2.1 e §2.2 (tetos mensais × 12, taxas CE/CN/TA/TFPC, teto de estágio 150.000/mês, CGI art. 136). Observação: os pisos/tetos do aprendiz (450.000) e o 6.000 da CMU não constam na skill como anuais |

## Decisões
- 2026-08-14: pontuar a v1.0 (não a v1.1) no Accuracy Score, sem razão por contagem — comparável com IE/TD — autor do score (chat: design-dev-kb)
- 2026-08-25: cap de previdência privada 320.000 anual e cumulativo — CCG — Mohit (chat: design-dev-kb)
- 2026-08-25: automação de design começa por países pequenos (CI, Chad, Gabon, Iraq, Yemen) — Manju propôs, Mohit concordou (chat: design-dev-kb)
- s.d. [INCERTO data]: reconciliação dirigida por flag (58206) em vez de retro — retro de componente único é impraticável — Mohit (chat: design-dev-kb)
- ~2026-09-22: parecer 1 do HRBS-14996: nenhum flag STR, "ITS é devido" (impôt synthétique/microentreprises exclui ITS); teto 70.000 correto, 75.000 é SMIG [❌ errado: o teto é 75.000 desde 2023-01-01, ver [[correcoes]] 2026-10-15]; defeitos do GTN vão para tickets separados — Wallisson (HRBS-14996). SUBSTITUÍDO em 23/09 (ver [[correcoes]])
- 2026-09-22: transporte de 30.000 (Abidjan) é valor estatutário, excluído do CNPS uma vez por mês; no chat a base CNPS do cliente foi dada como correta — Wallisson (chat: mercans-compliance). [INCERTO] o ticket diz que o motor não exclui o transporte das bases ITS/CNPS (leituras a conciliar)
- 2026-09-23: parecer corrigido: o enquadramento é o regime des prestataires de services pétroliers (sem ITS na folha se a entidade estiver inscrita; CNPS/CMU devidos); pede ao cliente a Déclaration du Prestataire de service trimestral (BIC Pétrole/Gaz) e prova de nacionalidade estrangeira — Wallisson (HRBS-14996; chat: mercans-compliance)
- ~2026-09-25: nacionalidade estrangeira confirmada (succursale D1020 de empresa estrangeira); regime confirmado para 2025 pela carta DGI nº 0984/MFB/DGI/DGE de 19/08/2025; confirmação do flag para 2026 só com a declaração IFPGAZ 2026 — Wallisson (HRBS-14996)
- ~2026-09-28: cliente firme no processo de isenção e escalou ao Marko; pediu versão detalhada em inglês, "sem resposta de IA", e se os documentos são exigidos todo ano — Sivaranjani Subbarayula (HRBS-14996)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-09-28 | HRBS-14996 | "Single Tax Regime" e isenção de ITS (Baker Hughes EHO Ltd); tetos CNPS; defeitos do GTN REF-P201-861 | Pending on reporter. 3 respostas do Wallisson (22, 23, 25/09); flag de isenção NÃO criado; aguarda doc pendente e IFPGAZ 2026; cliente escalou ao Marko | Não (flag não criado; defeitos do GTN a abrir em tickets separados) |
| 2026-09-16 | HRBS-14714 | Aplicabilidade do ITS na folha da Baker Hughes CI (Live/BAU) | Open, sem resposta no snapshot; tratado na prática no HRBS-14996 [INCERTO se vinculados] | Não |
| ~2026-08-14 | CT-A-620 | Spec CI (artigo KB, não é ticket) | Spec de configuração do Mohit; tabela quebrada na extração de texto, mas lida do PDF original em 2026-10-05 (ver Valores-chave) | — |

## Pendências
- [ ] Divergência hub × skill: o hub (parecer de 23/09, HRBS-14996) enquadra o cliente no regime des prestataires de services pétroliers (sem ITS na folha), mas a skill não menciona esse regime e diz que o ITS é retido sobre o bruto total de todos os empregados — verificar (skill lida em 2026-10-02)
- [ ] Divergência hub × skill: o hub registra "previdência privada, cap 320.000 anual (CCG)"; a skill só tem o abatimento de 320.000 para pensionistas (§3.3) e nada sobre cap de previdência privada de empregado ativo — verificar se são regras distintas (skill lida em 2026-10-02)
- [x] Divergência hub × skill sobre a vigência dos tetos/SMIG: resolvida em 2026-10-16. Vigência 2023-01-01, e o teto de PF/AM/AT-MP é 75.000, não 70.000 (communiqué CNPS de 11/01/2023)
- [ ] Documento que ainda falta no cliente + declaração IFPGAZ 2026 para confirmar o flag de 2026 — cliente (HRBS-14996)
- [ ] Resposta detalhada em inglês, sem "cara de IA"; responder se os documentos são exigidos todo ano — Wallisson (HRBS-14996)
- [ ] Abrir tickets separados dos defeitos do GTN REF-P201-861 (pensão CNPS lançada e estornada em 2517/2556 e 2537/2566; acima do teto de pensão; rótulos 2531, 2538, 2560, 2569 "EIS"; falta linha CE 9,2%; bases de transporte e moradia) — Wallisson [INCERTO se já abertos] (HRBS-14996)
- [ ] Transporte: parametrizar por localidade; exclusão de moradia exige base legal do cliente — Dev/config (HRBS-14996)
- [ ] Resposta formal no HRBS-14714 (ou vincular ao 14996) — Wallisson (HRBS-14714)
- [ ] Confirmar se o forfait petrolífero cobre também CN 1,2%, TA 0,4%, TFPC 1,2% e CE (corpo do art. 1068 bis ilegível); confirmar inscrição da entidade no regime; baixar o Formulaire Unique da DGI — Wallisson (chat: mercans-compliance)
- [ ] Refatorar a skill para thin-router — Wallisson (chat: mercans-compliance)
- [x] Conferir se o 9,20% (Worker Type = 1) da spec CT-A-620 é a linha CE que falta no GTN: confirmado no PDF original que o 9,20% é a CE do expatriado (reg. 4111, `58215 = 1`), 1,20% = CN; falta apenas ligar ao GTN do cliente (2026-10-05) (CT-A-620; HRBS-14996)
- [x] Conferir valores quebrados do CT-A-620 no original do YouTrack: feito em 2026-10-05, valores na tabela de Valores-chave (CT-A-620)
- [ ] **Importação em espera (decisão do usuário, 2026-10-16):** versões novas no Drive como .xlsx/.docx, NÃO importadas (WTC v1.3, CNPS-001 v1.4, CNPS-002 v1.5, CCG v1.3, Design v1_2). Importar só depois do retorno da Sivaranjani/cliente ao e-mail de 16/10 11:00. Conferência: `Research Pipeline/Costa do Marfim/2026-10-16-teto-CNPS/CONFERENCIA.md`
- [ ] Teto CNPS 70.000 → 75.000 nos artefatos: WTC v1.1, CNPS-001, CNPS-002 (DISA), CCG (definir a base entre v1.0 de 22/09 e v1.1), Regulation Design v1.1 → frente Pipeline (2026-10-16); skill payroll-compliance-cotedivoire §2.1/risco 5 (achar onde está instalada); avisar o Mohit sobre o CT-A-620 reg. 4061 (840.000 → 900.000). DD sem ocorrências
- [ ] Avisar o Mohit (fora do escopo, produção): CT-A-620 reg. 4061 e `ci.json` de produção (Drive, 07 - Design, ordinal 61) com piso e teto de 840.000/ano; o certo é 900.000 (75.000 × 12) desde 2023-01-01 — Wallisson (achado da frente Pipeline, 2026-10-16)
- [ ] DISA (CI-CNPS-002): o bloco DASC usa base de 240M para 45 empregados, impossível com qualquer teto — defeito à parte, verificar (frente Pipeline, 2026-10-16)
- [ ] DISA _v1.4 local (18/08) tem um bloco DASC que não está no Drive: decidir se entra na linhagem (frente Pipeline, 2026-10-16)
- [ ] Design CI: KT passo a passo + revisão de linguagem/estrutura (Wallisson); review points (Mohit); 3 flags string (`marital_status`, `transport_zone`, `benefit_in_kind_type`; o engine só lê números); local labels da Part 9 (266 códigos na 9384011); convenção de arredondamento; matriz da 9384011 — (chat: design-dev-kb)

## Correções ligadas
- [[correcoes]]: 2026-09-23, parecer HRBS-14996 de 22/09 ("ITS é devido") substituído pelo regime pétrolier.
- [[correcoes]]: design CI v1.0 sem intern/apprentice/first-employment/senior officer nem teto 320k, corrigido na v1.1; `_table` sobre "parts" dava 44.000 para todos e defeito de 12× em faixas/pisos/tetos (chat: design-dev-kb).
- [[correcoes]]: 2026-10-15, teto CNPS de PF/AM/AT-MP era 70.000 no parecer de 22/09, no hub, na skill e nos artefatos; o certo é 75.000 desde 2023-01-01 (e-mail "Ceiling for Ivory coast", Sivaranjani). Artefatos em correção pela frente Pipeline (2026-10-16).
- Erros do cliente apontados (não são nossos, não entram em correcoes): ~~teto 75.000 (é o SMIG)~~ (o cliente estava certo, ver linha acima), rótulos "CNAMGS"/"FNH" (órgãos do Gabão; na CI são AT/MP 3% e PF+AM 5,75%), "Single Tax Regime isenta ITS".

## Fontes
- raw/tickets/extracao/2026-10-02-tickets-AF.md
- raw/chats/2026-10-01-mercans-compliance.md
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- raw/chats/2026-10-01-compliance-research.md
- skill payroll-compliance-cotedivoire (lida em 2026-10-02)
