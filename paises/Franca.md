# França

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-france`

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-08-28 | Pacote v1.0 entregue (Pipeline v2.4); QA cross-check 87/100 NEEDS PATCHES; F-1, F-2, F-3 bloqueiam a entrega ao dev. Prioridade nº 1 (entrega em setembro, go-live em fevereiro) (chat: mercans-compliance). |
| [[design]] | 🔄 | ~2026-08-28 | Regulation Design Bloco 1 v0.1 (prefixo 9250); próximo é o Bloco 2 |
| Produção (outro time) | — | | go-live em fevereiro (outro time) |
| [[suporte]] | ⏳ | | sem tickets nas fontes |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-france`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026 (rendimentos 2026, avaliação 2027), setor privado, régime général, EUR, idioma francês (payslip FR + EN cortesia). Fora: régimes spéciaux, dirigentes não assalariados, autônomos, setor público, MSA. Mayotte tem SMIC próprio (9,56/h desde 2026-06-01); demais DOM usam o nacional. IDCC (convenções setoriais) é configuração por cliente.
- **Órgãos:** DGFiP (impots.gouv.fr), URSSAF, net-entreprises.fr (DSN), Agirc-Arrco, CPAM/ameli, CARSAT, France Travail.
- **Relatórios principais:** 10 outbound: DSN mensuelle (FR-DSN-001), FCTU, arrêt de travail/reprise (FR-DSN-002/003), DPAE, DOETH, solde taxe d'apprentissage, PAS (FR-DGFIP-001), taxe sur les salaires 2501-SD/2502-SD, DAT (FR-CPAM-002), SOLTéA. 5 inbound (recebidos, não são filings): CRM PAS, CRM URSSAF, retour Agirc-Arrco, taux AT/MP, BPIJ.
- **Confiança da skill:** QA de 2026-08-28: 87/100, NEEDS PATCHES (0 críticos, 3 maiores F-1..F-3, 3 menores m-1..m-3). Nenhum achado toca taxa, teto ou base legal. Nenhum filing foi testado em portal de autoridade (specs derivadas de fonte oficial); 3 autoridades com canal M2M e runbook, 2 só portal/manual. Não há seção TIER-B; valores variáveis (SMIC, PASS, grade PAS, taxa AT/MP) devem ser reverificados.

**Armadilhas confirmadas** (SKILL.md e `07-qa-report.md`)
1. Parâmetros mudam no meio do ano: SMIC em 1 jan e 1 jun; grade PAS padrão muda em 1 mai (Lei de Finanças de 2026-02-19); SMIC de referência da redução geral é congelado em janeiro o ano todo → `01-ccg.md` Mod 4, 5, 6
2. SMIC mensal = taxa horária x 35 x 52 / 12, não x 151,67 → `01-ccg.md` Mod 4
3. F-1: anotação "NO DD COUNTERPART" (264 linhas em 12 specs) é substancialmente falsa; checar o DD antes de repetir; FR-LIM-001 conta 199 e cita e-mail como omissão, mas o DD tem `E-mail Address` → `07-qa-report.md`
4. F-2: não existe wage type para BIK de refeição (5,50 por refeição; 11,00 por duas; sem benefício se o empregado paga >= 2,75) nem de ferramentas de comunicação (10% do preço) → `01-ccg.md` Mod 7
5. F-3: SIPSI está na tabela in-scope do CCG Mod 10, mas o `scope_manifest.json` e o Mod 11 o excluem; o manifest governa → `07-qa-report.md`
6. Specs inbound estão escritas no sentido inverso (recebidas/consultadas); não descrever como filings → `04-reports-spec.md`
7. m-2: DD sai como `FR-DD-001-v1.0.xlsx` mas o Version Control e as 15 specs dizem v1.1 → `07-qa-report.md`

**O que mais dá errado** (do QA)
- Defeitos concentrados na camada de reconciliação DD x Spec, não em pesquisa; nada exige nova fonte.
- m-1: chaves compostas (C13) documentadas em 53 de 90 linhas elegíveis; m-3: verde do net pay ausente (navy, igual BE/TN; problema do standard owner).
- W-01: contribuição patronal L137-13 (30%) só aparece como subordinada numa linha out-of-scope; W-02: CGI art. 182 A ter instruído mas não escopado.
- Linhas 19-20 do Version Control das specs ainda dizem WTC/SIR "NOT AVAILABLE".

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- FR-LIM-001: até 148 campos sem contraparte no DD (decisão de escopo Stage 4); share schemes S89 (30 rubriques) e Contract Nature 60 pendentes de decisão do owner.
- W-01..W-03 do scope lock-in (não bloqueiam).
- Nenhuma spec foi round-tripped por portal de autoridade.

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| SMIC horário | 12,31 (mensal 1.867,02) | 2026-06-01 | skill (SKILL.md); base legal em `01-ccg.md` Mod 4 |
| SMIC Mayotte | 9,56/h | 2026-06-01 | skill (SKILL.md) |
| SMIC de referência da redução geral | congelado no valor de janeiro | 2026-01-01 | skill (SKILL.md) |
| Grade PAS padrão | muda em 1 mai (LF 2026, promulgada 2026-02-19) | 2026-05-01 | skill (SKILL.md); `01-ccg.md` Mod 6 |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| CCG FR-CCG-001 (13 módulos; 136/136 perguntas) | v1.0 | ~2026-08-26 | 01-ccg.md | QA PASS no formato |
| WTC FR-WTC-001 (374 WTs = 300 globais + 74 FR-0xx; 6 abas) | v1.0 | 2026-08-27 | 02-wtc.md | "Draft" no Version Control |
| DD FR-DD-001 (25 ID + 164 campos de país; 54 mappers / 303 códigos) | v1.1 (histórico até 2026-10-06) | 2026-08-27 | 05-data-dictionary.md | Released. Histórico: arquivo nomeado v1.0 (m-2 do QA). Drive: `02- DD/Archived/FR-DD-001-v1.1.xlsx` desde 2026-10-26 |
| DD FR-DD-001 (pacote reemitido; numeração reiniciada) | v1.0 (vigente a partir de 2026-10-06; exceção à regra 8: número menor, emissão mais nova) | 2026-10-06 | `mercans-pipeline/FR-compliance/05-data-dictionary/FR-DD-001-v1.0.xlsx` (md5 889f66d2…) = `fr-research-validation/final/` | Promovido em 09/10 (PROMOTION-LOG-2026-10-09). Drive 2026-10-26: Google Sheet `1bQcuzfLgHznJRMB_lFe2JloJyxEHEui9o85Pr3i4dLg` na raiz de `02- DD`, linkado no Monday (Compliance Artifacts › France › DD - AI); gsheet anterior (1oY8VZuz…) e o xlsx em `Archived` |
| Report Specs (15 workbooks: 10 outbound, 5 inbound) | v1.1 (vigente: maior versão) | 2026-08-27 | — | 15/15 no formato; anotação F-1 a corrigir. Histórico: v1.0 |
| SIR FR-SIR-INDEX-001 + integration landscape (5 autoridades, 3 M2M) | v1.0 | 2026-08-27 | 03-sir.md | HAS_INTEGRATIONS |
| Runbooks NETENT-DSN, URSSAF-DPAE, DGFIP-EDI (7 fases) | — | 2026-08-27 | 03-sir.md | BUILD-READY, com itens bloqueados/não verificados |
| Payslip FR-PSL-001 (8 abas; FR legal + EN cortesia) | v1.0 | — | 06-payslip.md | m-3 em aberto |
| QA cross-check | — | 2026-08-28 | 07-qa-report.md | 87/100, NEEDS PATCHES (0 críticos, 3 maiores, 3 menores) |
| Alignment patch DD x Specs | — | 2026-08-27 | 07-qa-report.md | 26/26 asserções OK |
| scope_manifest.json (lock 2026-08-26) | 1.1 | 2026-08-27 | — | Validação PASS (W-01..W-03) |
| Skill roteadora `fr-compliance` | — | upload 2026-09-06 | — | Ativa |
| Design Method v3 (substitui v2 de 25/08) | v3 | 2026-08-28 | — | Autoritativo |
| Regulation Design FR, Bloco 1 (prefixo 9250; 7 regs, 21 flags, 13 bases, 18 contas) | v0.1 | ~2026-08-28 | — | Validado contra Ex. 1 do CCG |

## Valores-chave (com vigência)
> Conteúdo estatutário completo: skill `payroll-compliance-france`. Abaixo, só pontos decididos/discutidos nos chats.

| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| PASS | 4.005/mês; 48.060/ano | 2026-01-01 | | Arrêté 22/12/2025 (chat: design-dev-kb) |
| PASS 2025 | 3.925/mês | ⚠️ vigência? (2025) | 2025-12-31 | chat: design-dev-kb |
| SMIC | 12,02/h; 1.823,03/mês | 2026-01-01 | 2026-05-31 | L3231-1 (chat: design-dev-kb) |
| SMIC | 12,31/h; 1.867,02/mês (+2,41%) | 2026-06-01 | | Décret 1/6/2026 |
| SMIC congelado para RGDU | 21.876,40 o ano todo | 2026-01-01 | | Décret 2026-509 |
| RGDU | Tmin 0,0200; Tdelta 0,3781 (FNAL 0,10%) ou 0,3821 (FNAL 0,50%); corte em 65.629,20 | 2026-01-01 | | L241-13; D241-2-4; Décrets 2025-1446 / 2026-509 |
| Grade PAS | 20 faixas, 0% (<1.620) a 43% (>=55.062) | 2026-01-01 | 2026-04-30 | BOI-BAREME-000037 |
| Grade PAS | +0,9%; 0% <1.635 a 43%; DOM começa em 1.875 (GP/MQ/RE) e 2.008 (GF/YT); aplica-se pela data de pagamento | 2026-05-01 | | LOI 2026-103; BOI-BAREME-000037-20260407 |
| Taxas reduzidas de 7% (saúde) e 3,45% (família) | revogadas, absorvidas pela RGDU | 2026-01-01 | | chat: design-dev-kb |
| Contribuição ER sobre rupture conventionnelle | 40% (antes 30%) | 2026 | | L137-12 (LFSS 2026 art. 15) |
| Diálogo social | 0,016% | 2026 | | UNEDIC; [INCERTO] se também EE (skill: CCG M5.1 e WTC FR-019 dizem 0,016% de cada lado, ER e EE; CCG M3 e Ex. 6 só mostram o lado ER; ver Pendências) |
| Prazo 2502-SD | 31/jan (Vol. III-C) ou 15/jan (impots.gouv e manifest) | ⚠️ vigência? | | [INCERTO] não resolvido (confirmado: skill 03-sir.md Q1 "unresolved, P1 §1.8"; CCG M10: 15/jan se imposto < €4.000, 31/jan se houve instalments) |
| Revisões datadas | PPV ampliado acaba em 2026-12-31; DPAE na DSN não antes de 2027-01-01; payslip novo em 2027-01-01 | 2026/2027 | | 01-ccg.md; 02-wtc.md |

## Decisões
- 2026-08-26: escopo travado no régime général privado; fora RATP, ENIM, CNBF, CRPCEN, CAVIMAC, CNIEG/CAMIEG, MSA, SSI/TNS, fonctionnaires, A1 inbound, Mayotte, LODEOM; dentro Alsace-Moselle e DOM (só PAS); mandataires sem chômage/AGS — regimes especiais não pesquisados — Wallisson, scope owner (chat: design-dev-kb)
- ~2026-08-27: PASRAU/NEORAU fora (FR-DGFIP-006); Art. 197 A não modelado; SIPSI fora (o manifest prevalece sobre o CCG M10) — nível de lançamento — Build/QA (chat: design-dev-kb)
- 2026-08-27: não adicionar ao DD linhas "sem contraparte"; share schemes S89 fora, sinalizados ao owner; Contract Nature 60 pendente; 32 e 80 excluídos — adicionar campo é mudança de escopo (Stage 4) — Wallisson (chat: design-dev-kb)
- 2026-08-27: colunas laranja do WTC (D, H, I, K, L, M, V, W) vazias para o dev; justificativa Yes-No na col. F; coluna "Notes" nos mappers do DD — precedente BE — Build (chat: design-dev-kb)
- 2026-08-27: DPAE formato 120 como alvo; modelo concentrateur para DSN/DPAE; Model A DGFIP-EDI é só recomendação a decidir no portfólio — Runbook (chat: design-dev-kb)
- 2026-08-28: m-3 (verde do net pay) não é corrigido só na FR; escalar ao standard owner (BE/TN usam navy) — QA (chat: design-dev-kb)
- ~2026-08-28: reconciliação progressiva do teto como default; flags booleanas 1/2; SMIC vivo e congelado em contas separadas (52572/52573); `_monthly` na 9250021; IDCC como flag sem override — Wallisson (chat: design-dev-kb)
- sem data: payslip no modelo simplificado (Arrêté 25/02/2016 alterado em 31/01/2023); não antecipar o modelo novo (adiado para 2027-01-01) — Build (chat: design-dev-kb)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| — | _(nenhum ticket FR nas fontes)_ | | | |

## Pendências
- [ ] Corrigir F-1 (264 linhas "NO DD COUNTERPART": refazer join por nome + conceito), F-2 (criar 4 WTs de BIK refeição e NTIC no padrão 62400/62410/62403), F-3 (SIPSI fora do escopo; criar FR-MOL-001) e m-1/m-2 — Build/Wallisson — (chat: design-dev-kb, 07-qa-report)
- [ ] m-3 (verde do net pay) ao standard owner — QA — (chat: design-dev-kb)
- [ ] Scope W-01..W-03: promover L137-13 (30%) e L137-14 (10%) a in_scope; linha out_of_scope para o 182 A ter; A1 só como flag; rotular F1–F22 e acrescentar F23–F31 — scope owner — [INCERTO] ID sugerido FR-DGFIP-006 já é do PASRAU
- [ ] Decisões do owner: share schemes S89; Contract Nature 60; Version Control das specs (linhas 19–20) — Wallisson
- [ ] SIR: FR-SI-Q1–Q5; NETENT-DSN (charte concentrateur, registro EDITEUR, pacote XSD, yml CNAM); DPAE (tabelas C_URSSAF e C_APPLICATION bloqueiam go-live, mais 10 itens não verificados); DGFIP-EDI Q1–Q7 (Q2 decide Model A)
- [ ] Design: Blocos 2 (contribuições + 6 matrizes), 3 e 4; mapear quais WTs ER alimentam 58130 (bloqueia 9250061); RA confirmar 24 [DERIVED]; escopo IDCC; 52560 sem valor; 52562/52563 fixo ou taxa — Wallisson/RA
- [ ] Pesquisa: preencher Internal Code no DD e conformar ao v1.5; preencher colunas laranja do WTC; grade PAS em valores anuais; entregar FR-DGFIP-002 e FR-DSN-001 ao design — Research
- [ ] [INCERTO] Ex. 1 do FR-pack (bruto 2.915,50; contribuições 640,50; IR 126,61) vs CCG M12/payslip (2.800; 616,44; IR 94,06; líquido 2.089,50) — alvo de validação do design
- [ ] [INCERTO] Diálogo social 0,016% também EE (CCG M5.1, WTC FR-019) vs só ER (CCG M3, Ex. 1, payslip)
- [ ] [INCERTO] CCG M4.2/Ex. 6 usa 151,67 mas o payslip manda 151,6667
- [ ] [INCERTO] CCG M10 cita "FR-NSSO / FR-FIN series" (resíduo da BE?); crítica cita WTC 378/DD 173 campos vs entregue 374/189
- [ ] Prazo do 2502-SD: 31/jan vs 15/jan — (03-sir.md)
- [ ] FR-CCG-001 v1.0 (pacote emitido em 06/10/2026), Mod. 12 Ex. 1: 3 números digitados que não fecham na conta. Termo interno impresso 0,875970 (correto 0,875870); 0,437985^1,75 impresso 0,235942 (correto 0,235805; o C final 0,1091 está certo); 2.915,50 × 13,00 % impresso 379,01 (correto 379,02, pela regra half-up do próprio CCG). O C38 reprova a CCG por isso, e um novo Stage 9 da França para nesse ponto. Decisão do usuário (17/10/2026): só registrar, sem v1.1 — Pipeline — (`revisoes/2026-10-17-matriz-cobertura-FR-pipeline.md`; `~/mercans-pipeline/IMPROVEMENT_LOG.md` 2026-10-07 Fase 2)

## Correções ligadas
- [[correcoes]]: QA das 12:21 deu 486/562 (86,5%); correto 720/984 (73,2%)
- [[correcoes]]: fontes secundárias com PASS derivado errado: 50.122 / faixa 4.440,01; correto 50.112 / 4.480,01 (usar o decreto, x1,02038)
- [[correcoes]]: manifest com DPAE "via net-entreprises" só XML; correto host da URSSAF, TXT 120 ou XML; DGFIP-003 é UN/EDIFACT INFENT DP nos dois sentidos
- [[correcoes]]: crítica de pesquisa dizia "não existe coluna de valor no mapper"; `local_value` existe no Master DD v1.5
- [[correcoes]]: cabeçalhos "Description (NL)" (resíduo da BE) para "Description (FR)"; códigos 32/60/80 excluídos sem nome para nomeados

## Fontes
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- raw/chats/2026-10-01-mercans-compliance.md
- skill payroll-compliance-france (lida em 2026-10-02)
