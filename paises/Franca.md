---
tipo: pais
codigo: "FR"
etapa_research: "concluida"
etapa_research_data: 2026-10-09
etapa_design: "em andamento"
etapa_design_data: 2026-08-28
etapa_producao: "outro time (go-live em fevereiro)"
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: v1.1
ccg_data: 
wtc: v1.1
wtc_data: 
dd: "v1.0"
dd_data: 2026-10-06
report_specs: "15 × v1.0"
report_specs_data: 2026-10-06
sir: "v1.0"
sir_data: 2026-08-27
payslip: 
skill: "payroll-compliance-france"
tickets_abertos: 
tickets_conferidos_em: 
versoes_fonte: "nome do arquivo no Drive (Country Folders/France), lido em 2026-10-27; sem data de versão"
obs_versoes: "CCG v1.0→v1.1 (FR-CCG-001-v1.1.gdoc); WTC v1.0→v1.1 (FR-WTC-001-v1.1.gsheet); CONFERIR: pacote FR reemitido em 06/10 com numeração reiniciada"
atualizado_em: 2026-10-27
---
# França

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-france` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-08-28 | Pacote v1.0 entregue (Pipeline v2.4); QA cross-check 87/100 NEEDS PATCHES; F-1, F-2, F-3 bloqueiam a entrega ao dev. Prioridade nº 1 (entrega em setembro, go-live em fevereiro) (chat: mercans-compliance). → superada em parte por: QA v4 (2026-09-03) = READY FOR DEV TEAM, F-1..F-3 fechados na linhagem anterior (F6-20261027-FR-C11; validação humana pendente) e pacote reemitido v1.0 (linha abaixo). |
| [[research-pipeline]] (reemissão) | ✅ | 2026-10-09 | Pacote reemitido v1.0 (2026-10-06) promovido em 2026-10-09. Teste 0 de 2026-10-09 sobre ele: 51 afirmações por amostra (CCG 21, WTC 13, DD 8, Specs 9), 50 PASS, 1 UNVERIFIED (DPAE formato 120); Payslip e SIR fora da amostra; QA v2–v4 verificam só a linhagem anterior (F6-20261027-FR-C38, C11; validação humana pendente) |
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
| CCG FR-CCG-001 (13 módulos; 136/136 perguntas) | v1.0 | ~2026-08-26 | 01-ccg.md | QA PASS no formato. → superada por CCG v1.0 reemitido de 2026-10-06 (linha abaixo; F6-20261027-FR-C01, C02; validação humana pendente) |
| WTC FR-WTC-001 (374 WTs = 300 globais + 74 FR-0xx; 6 abas) | v1.0 | 2026-08-27 | 02-wtc.md | "Draft" no Version Control. → superada por WTC v1.0 reemitido, Approved em 2026-10-06 (linha abaixo; F6-20261027-FR-C03; validação humana pendente). Contagens 374 WTs / 164 campos são da linhagem de 08-27; a linhagem anterior medida pelo QA v2/v3 tem 378 WTs (FR-075..FR-078 por F-2) e 198 campos de DD (25 + 173); contagem do pacote reemitido não confirmada (≥ 379, FR-079 existe) (F6-20261027-FR-C10; validação humana pendente) |
| DD FR-DD-001 (25 ID + 164 campos de país; 54 mappers / 303 códigos) | v1.1 (histórico até 2026-10-06) | 2026-08-27 | 05-data-dictionary.md | Released. Histórico: arquivo nomeado v1.0 (m-2 do QA). Drive: [[Research Pipeline/França/DD/FR-DD-001-v1.1.xlsx\|FR-DD-001-v1.1.xlsx]] desde 2026-10-26 |
| DD FR-DD-001 (pacote reemitido; numeração reiniciada) | v1.0 (vigente a partir de 2026-10-06; exceção à regra 8: número menor, emissão mais nova) | 2026-10-06 | [[frentes/pipeline/mercans-pipeline/FR-compliance/05-data-dictionary/FR-DD-001-v1.0.xlsx\|FR-DD-001-v1.0.xlsx]] (md5 889f66d2…) = `fr-research-validation/final/` | Promovido em 09/10 (PROMOTION-LOG-2026-10-09). Drive 2026-10-26: Google Sheet `1bQcuzfLgHznJRMB_lFe2JloJyxEHEui9o85Pr3i4dLg` na raiz de `02- DD`, linkado no Monday (Compliance Artifacts › France › DD - AI); gsheet anterior (1oY8VZuz…) e o xlsx em `Archived` |
| Report Specs (15 workbooks: 10 outbound, 5 inbound) | v1.1 (vigente: maior versão) | 2026-08-27 | — | 15/15 no formato; anotação F-1 a corrigir. Histórico: v1.0. → superada por Report Specs v1.0 de 2026-10-06 (linha abaixo; F6-20261027-FR-C07; validação humana pendente) |
| SIR FR-SIR-INDEX-001 + integration landscape (5 autoridades, 3 M2M) | v1.0 | 2026-08-27 | 03-sir.md | HAS_INTEGRATIONS. Conferido no pipeline: arquivo [[Research Pipeline/França/SIR/FR-SIR-INDEX-001-v1.0.docx\|FR-SIR-INDEX-001-v1.0.docx]] (md5 `889c19e11e767d19a66f58b06de55fde`, arquivo de 2026-09-29), Version Control `v1.0 / 2026-08-27`; não foi reemitido nem aparece em PROMOTION-LOG. "FR-SIR-001" (monday e varredura do pipeline) é o rótulo do mesmo documento. Se o conteúdo mudou entre 08-27 e 09-29: não confirmado (F6-20261027-FR-C06; validação humana pendente) |
| Runbooks NETENT-DSN, URSSAF-DPAE, DGFIP-EDI (7 fases) | — | 2026-08-27 | 03-sir.md | BUILD-READY, com itens bloqueados/não verificados |
| Payslip FR-PSL-001 (8 abas; FR legal + EN cortesia) | v1.0 | — | 06-payslip.md | m-3 em aberto. O Payslip Generator não tem aba Version Control; vigente = arquivo md5 `d98d54163bcecaa866729b77b645334b` (2026-10-06, promovido em 2026-10-09); o rótulo "v1.0" (hub) × "v1.1" (changelog de 06/10) não se prova por Version Control: [INCERTO] (F6-20261027-FR-C08; validação humana pendente) |
| QA cross-check | — | 2026-08-28 | 07-qa-report.md | 87/100, NEEDS PATCHES (0 críticos, 3 maiores, 3 menores). → superada por QA v4 (2026-09-03): READY FOR DEV TEAM, zero defeitos de conteúdo abertos, 5 itens restantes não bloqueantes; F-1, F-2, F-3, m-1, m-2 fechados no QA v2 e m-3 reenquadrado; v2–v4 verificam a linhagem anterior (CCG v1.3, WTC v1.2, DD v1.4), não o pacote reemitido (F6-20261027-FR-C11; validação humana pendente) |
| Alignment patch DD x Specs | — | 2026-08-27 | 07-qa-report.md | 26/26 asserções OK |
| scope_manifest.json (lock 2026-08-26) | 1.1 | 2026-08-27 | — | Validação PASS (W-01..W-03) |
| Skill roteadora `fr-compliance` | — | upload 2026-09-06 | — | Ativa. Em 2026-10-09 a skill foi promovida a `08-skill/fr-compliance/` (SKILL.md md5 `6a208ed7d50fde31ec13b4269d740879`, referências 01–06 novas) e o `07-qa-report.md` foi arquivado sem substituto: a Ficha do país (lida em 2026-10-02) está defasada, reler (F6-20261027-FR-C09; validação humana pendente) |
| Design Method v3 (substitui v2 de 25/08) | v3 | 2026-08-28 | — | Autoritativo |
| Regulation Design FR, Bloco 1 (prefixo 9250; 7 regs, 21 flags, 13 bases, 18 contas) | v0.1 | ~2026-08-28 | — | Validado contra Ex. 1 do CCG |
| CCG FR-CCG-001 (pacote reemitido) | v1.0 (vigente a partir de 2026-10-06; exceção à regra 8: número menor, emissão mais nova) | 2026-10-06 | [[frentes/pipeline/mercans-pipeline/FR-compliance/01-ccg/FR-CCG-001-v1.0.docx\|FR-CCG-001-v1.0.docx]] (md5 `a9f16a70bd6957dcab5d5411c26eeab0`) | Version Control `1.0 / 2026-10-06 / Initial version / Approved`; promovido em 2026-10-09 (PROMOTION-LOG-2026-10-09). O nome [[Research Pipeline/França/CCG/FR-CCG-001-v1.0.docx\|FR-CCG-001-v1.0.docx]] designou dois conteúdos (agosto/setembro, sha `cf8675c1a56cb59a`, arquivado em 06/10; e este); o v1.1 (md5 `7c0e8421…`, arquivo [[frentes/pipeline/mercans-pipeline/FR-compliance/01-ccg/Archived/2026-10-09-promotion/FR-CCG-001-v1.1.docx\|FR-CCG-001-v1.1.docx]]) foi arquivado em 09/10. Ao citar "CCG v1.0 da França", dizer a data e o md5. Link do monday (atualizado em 2026-09-15, anterior à reemissão) não verificado (F6-20261027-FR-C01, C02; validação humana pendente) |
| WTC FR-WTC-001 (pacote reemitido) | v1.0 (vigente a partir de 2026-10-06; exceção à regra 8) | 2026-10-06 | [[frentes/pipeline/mercans-pipeline/FR-compliance/02-wtc/FR-WTC-001-v1.0.xlsx\|FR-WTC-001-v1.0.xlsx]] (md5 `8592d40b5d520110ec99f0bdc585caf7`) | "France (FR) - income year 2026"; Version Control `1.0 / 2026-10-06 / Initial version / Approved`; arquivo de 2026-10-09 (F6-20261027-FR-C03; validação humana pendente) |
| Report Specs (15 workbooks, pacote reemitido) | v1.0 (vigente a partir de 2026-10-06; exceção à regra 8) | 2026-10-06 | `mercans-pipeline/FR-compliance/04-reports-spec/` (md5 de cada spec em `raw/pipeline/Franca/2026-10-27/version-control/MANIFEST.md`) | Cada spec com uma só linha `1.0 / 2026-10-06 / Initial version / Approved`; arquivos de 2026-10-09 (re-sync). Linhas "Downstream alignment" dizem DD v1.0, WTC v1.0 e SIR-INDEX v1.0 DELIVERED (antes "NOT AVAILABLE"). Não há v1.1. O monday não tem item de Report Specs. O inventário (item 3) lista 8 specs; são 15 (F6-20261027-FR-C07; validação humana pendente) |
| WTC e DD reemitidos: md5 × PROMOTION-LOG | — | 2026-10-09 | `raw/pipeline/Franca/2026-10-27/notas/PROMOTION-LOG-2026-10-09.md` | O log registra WTC `553fb181ca8f0d8d3a3fe473d5b44730` e DD `8a91af3efd13c3488bd9a42bf7c2063d`; os arquivos coletados têm WTC `8592d40b…` e DD `889f66d2…` (este é o do hub), ambos com o mesmo Version Control `1.0 / 2026-10-06`. CCG e Payslip batem; as 15 specs divergem por causa do "Re-sync 2026-10-09" (ids belgas removidos de "Similar To"; rótulo de versão do Report Matrix = 1.0; arquivos pré-promoção em `04-reports-spec/Archived/2026-10-09-promotion/`). Para WTC e DD a causa não está registrada: [INCERTO]; ver Pendências (F6-20261027-FR-C04, C23; validação humana pendente) |
| DD FR-DD-001 v1.0: conferência | — | 2026-10-26 | monday (DD – AI), `FR-DD-001-v1.0` | O link do monday (`1bQcuzfLgHznJRMB_lFe2JloJyxEHEui9o85Pr3i4dLg`, atualizado em 2026-10-26) e o md5 `889f66d2…` batem com a linha acima. A divergência de nome do QA (m-2) não existe na reemissão. Resíduo: célula de título do Version Control com o placeholder `<France>` (F6-20261027-FR-C05; validação humana pendente) |

- Mapa dos arquivos desta pasta: [[Research Pipeline/França/fr-compliance/MAPA|mapa]]

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
| Taxe sur les salaires: taxa total por faixa | 4,25% (normal); 8,50% (2ª faixa, 4,25 + 4,25 adicional); 13,60% (3ª faixa, 4,25 + 9,35 adicional). 4,25% e 9,35% são as taxas **adicionais** das linhas do 2502-SD, não o total. Faixas: 2ª acima de 9.229/ano (769/mês, 2.307/tri) até 18.423/ano (1.535/mês, 4.606/tri); 3ª acima de 18.423 | 2026-01-01 (remunerações pagas a partir de) | | Notice 2501-NOT-SD 2026 e formulário 2501-SD 2026 (DGFiP); CGI art. 231; lido via FR-TEST0 R07/R08, não li a notice (F6-20261027-FR-C16; validação humana pendente) |
| Taxe sur les salaires: abatimento (CGI art. 1679 A) | 24.256 | 2026-01-01 | | Notice 2501-NOT-SD 2026 (DGFiP); ⚠️ não lida por nós, vem do Version Control da FR-DGFIP-003 (F6-20261027-FR-C31; validação humana pendente) |
| Taxe sur les salaires: abatimento (CGI art. 1679 A) | 24.041 | 2025-01-01 | 2025-12-31 | 2502-SD edição ANNEE 2025 (DGFiP), guardado nas fontes oficiais; ⚠️ vigência deduzida do rótulo da edição (F6-20261027-FR-C31; validação humana pendente) |
| RGDU: regra do Tdelta | Tdelta acompanha o porte do empregador (taxa do FNAL: 0,10% → 0,3781; 0,50% → 0,3821), **não** a natureza jurídica; expoente 1,75; SMIC de referência 21.876,40 (12,02 × 1.820 h), congelado em 2026 | 2026-01-01 | | URSSAF "La réduction générale des cotisations patronales (RGDU) 2026" (consultada 2026-10-09); Décret 2026-509; via FR-TEST0 C05/C02 (F6-20261027-FR-C21; validação humana pendente) |
| Agirc-Arrco (EE / ER) | T1 3,15% / 4,72%; T2 8,64% / 12,95%; CEG T1 0,86% / 1,29%, T2 1,08% / 1,62%; CET 0,14% / 0,21% | 2026-01-01 | | Circulaire Agirc-Arrco 2025-16-SG-DRJ (paramètres 2026), consultada 2026-10-09; via FR-TEST0 C06–C08 (F6-20261027-FR-C39; validação humana pendente) |
| Apec (cadres) (EE / ER) | 0,024% / 0,036%, até 4 PSS (192.240/ano = 16.020/mês) | 2026-01-01 | | URSSAF "Taux de cotisations – Secteur privé", consultada 2026-10-09; via FR-TEST0 C09/W05. Erro da validação (8 PMSS) corrigido na reemissão (F6-20261027-FR-C39; validação humana pendente) |
| Seguro-desemprego / AGS (ER) | 4,00% / 0,25%, até 4 PSS (192.240/ano) | 2026-01-01 | | URSSAF "Taux de cotisations – Secteur privé", consultada 2026-10-09; via FR-TEST0 C10 (F6-20261027-FR-C39; validação humana pendente) |
| CSG / CRDS | CSG dedutível 6,80% + não dedutível 2,40%; CRDS 0,50%; base 98,25% do bruto, até 192.240/ano | 2026-01-01 | | URSSAF (página CSG/CRDS), consultada 2026-10-09; via FR-TEST0 C11 (F6-20261027-FR-C39; validação humana pendente) |
| COTAM / CPF-CDD | COTAM 5,50% (empregado coberto pela seguridade francesa sem domicílio fiscal na França; base do art. L242-1 CSS); CPF-CDD 1% (CDD, qualquer porte) | 2026-01-01 | | URSSAF, consultada 2026-10-09; via FR-TEST0 C13/W08, C14/W07 (F6-20261027-FR-C39; validação humana pendente) |
| Taxe d'apprentissage / formação | Aprendizagem 0,59% + 0,09% (saldo) = 0,68%; formação 0,55% (< 11 empregados) ou 1% (≥ 11) | 2026-01-01 | | URSSAF, consultada 2026-10-09; via FR-TEST0 R06, C21 (F6-20261027-FR-C39; validação humana pendente) |
| Retenção de não residentes (CGI art. 182 A) | 0% até 17.275/ano (4.319 tri; 1.440 mês; 332 sem; 55 dia); 12% de 17.276 a 50.112 (4.320–12.528; 1.441–4.176; 333–964; 56–161); 20% acima; DOM 8% e 14,4% no lugar de 12% e 20% | 2026-01-01 (rendimentos pagos em 2026) | | BOI-BAREME-000043 de 02/04/2026 (DGFiP); via FR-TEST0 C17 (F6-20261027-FR-C40; validação humana pendente) |
| IJ de acidente do trabalho / doença profissional | 60% do salário diário nos primeiros 28 dias; 80% a partir do 29º; sem carência; salário diário = bruto do mês anterior ÷ 30,42 | ⚠️ vigência não citada na fonte do cartão (TEST0 de 2026-10-09) | | Service-Public F175; via FR-TEST0 C19 (F6-20261027-FR-C40; validação humana pendente) |
| Montant net social (L911-1) | Até 2026-12-31: parcela patronal de previdência complementar coletiva (L911-1) **fora** do cálculo (regra mantida no FR-TEST0 C18, PASS). A partir de 2027-01-01: parcela patronal incluída, mas só como **projeto de decreto** (⚠️ sem fonte A lida; ver Pendências) | 2023-07-01 (linha obrigatória no holerite); regra de 2026 acima | 2026-12-31 (regra de exclusão) | BOSS actualité de nov. 2023 e rubrique BOSS de 2026-10-02, via FR-TEST0 C18 (F6-20261027-FR-C37; validação humana pendente) |

## Decisões
- 2026-08-26: escopo travado no régime général privado; fora RATP, ENIM, CNBF, CRPCEN, CAVIMAC, CNIEG/CAMIEG, MSA, SSI/TNS, fonctionnaires, A1 inbound, Mayotte, LODEOM; dentro Alsace-Moselle e DOM (só PAS); mandataires sem chômage/AGS — regimes especiais não pesquisados — Wallisson, scope owner (chat: design-dev-kb)
- ~2026-08-27: PASRAU/NEORAU fora (FR-DGFIP-006); Art. 197 A não modelado; SIPSI fora (o manifest prevalece sobre o CCG M10) — nível de lançamento — Build/QA (chat: design-dev-kb)
- 2026-08-27: não adicionar ao DD linhas "sem contraparte"; share schemes S89 fora, sinalizados ao owner; Contract Nature 60 pendente; 32 e 80 excluídos — adicionar campo é mudança de escopo (Stage 4) — Wallisson (chat: design-dev-kb)
- 2026-08-27: colunas laranja do WTC (D, H, I, K, L, M, V, W) vazias para o dev; justificativa Yes-No na col. F; coluna "Notes" nos mappers do DD — precedente BE — Build (chat: design-dev-kb)
- 2026-08-27: DPAE formato 120 como alvo; modelo concentrateur para DSN/DPAE; Model A DGFIP-EDI é só recomendação a decidir no portfólio — Runbook (chat: design-dev-kb)
- 2026-08-28: m-3 (verde do net pay) não é corrigido só na FR; escalar ao standard owner (BE/TN usam navy) — QA (chat: design-dev-kb)
- ~2026-08-28: reconciliação progressiva do teto como default; flags booleanas 1/2; SMIC vivo e congelado em contas separadas (52572/52573); `_monthly` na 9250021; IDCC como flag sem override — Wallisson (chat: design-dev-kb)
- sem data: payslip no modelo simplificado (Arrêté 25/02/2016 alterado em 31/01/2023); não antecipar o modelo novo (adiado para 2027-01-01) — Build (chat: design-dev-kb)
- 2026-09-02: SIPSI fora do escopo, consistente no CCG Mod. 10, no scope_manifest e no WTC (QA v2); a criação de `FR-MOL-001` é inferida pela contagem de `out_of_scope` (13 → 14 → 15 in / 14 out), nenhum arquivo coletado nomeia a entrada — Build/QA — (F6-20261027-FR-C14; validação humana pendente)
- 2026-09-02: m-1 fechado (chaves compostas 90/90 documentadas) e m-2 fechado (nome do DD corrigido em 8/8 arquivos operacionais; resta a célula A1 da aba Field Option do Payslip citando `FR-DD-001-v1.0.xlsx`); m-3 não é defeito da FR (BE e Tunísia usam azul-marinho), segue pergunta ao standard owner — QA — (F6-20261027-FR-C15; validação humana pendente)
- 2026-09-03: Contract Nature (S21.G00.40.007) tinha 9 de 26 códigos; 53, 54 (emprego penitenciário) e 70 (ESAT) incluídos; 32 (CAPE) excluído (Código de Comércio art. L127-1); 60 (contrat d'engagement éducatif) segue decisão aberta do dono do escopo (Wallisson). O código 80 (contrat de génération, Ordonnance 2017-1387 de 22/09/2017) é do mapper `Public-Policy or Collectively Agreed Scheme (S21.G00.40.008)`, não do Contract Nature. TEST0 D03 conferiu `Country Fields!K32/W32` com o cahier technique CT2026.1.2: PASS — QA/Alignment Patch — (F6-20261027-FR-C19; validação humana pendente)
- 2026-09-03: escopo IDCC = tabelas de override por convenção coletiva são tarefa de implementação do cliente, não da pesquisa base (CCG v1.3; "cerca de 330 convenções ativas" é do QA, ⚠️ sem fonte) — Wallisson, QA v4 — (F6-20261027-FR-C36; validação humana pendente)
- 2026-09-03: colunas laranja do DD (Internal Code, 173 campos) e do WTC (In Period Reconciliation, YTD Load, YTD Remarks, Prorating Method, Calculation Type) vazias não são defeito (QA v4, B > chat C); manter vazias. O QA v4 nomeia 5 colunas do WTC e a decisão de 2026-08-27 lista 8; a conversa com o time de dev sobre a propriedade das colunas segue em aberto — QA v4 — (F6-20261027-FR-C35; validação humana pendente)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| — | _(nenhum ticket FR nas fontes)_ | | | |

## Pendências
- [ ] Corrigir F-1 (264 linhas "NO DD COUNTERPART": refazer join por nome + conceito), F-2 (criar 4 WTs de BIK refeição e NTIC no padrão 62400/62410/62403), F-3 (SIPSI fora do escopo; criar FR-MOL-001) e m-1/m-2 — Build/Wallisson — (chat: design-dev-kb, 07-qa-report) → ver F6-20261027-FR-C11, C12, C13, C14, C15 (2026-10-27): fechados no QA v2 na linhagem anterior; a aplicação ao pacote reemitido não foi verificada
- [ ] m-3 (verde do net pay) ao standard owner — QA — (chat: design-dev-kb) → ver F6-20261027-FR-C15 (2026-10-27)
- [ ] Scope W-01..W-03: promover L137-13 (30%) e L137-14 (10%) a in_scope; linha out_of_scope para o 182 A ter; A1 só como flag; rotular F1–F22 e acrescentar F23–F31 — scope owner — [INCERTO] ID sugerido FR-DGFIP-006 já é do PASRAU
- [ ] Decisões do owner: share schemes S89; Contract Nature 60; Version Control das specs (linhas 19–20) — Wallisson → ver F6-20261027-FR-C07 (2026-10-27): linhas 19–20 das specs reemitidas já dizem WTC/SIR DELIVERED; Contract Nature 60 segue aberto, ver C19
- [ ] SIR: FR-SI-Q1–Q5; NETENT-DSN (charte concentrateur, registro EDITEUR, pacote XSD, yml CNAM); DPAE (tabelas C_URSSAF e C_APPLICATION bloqueiam go-live, mais 10 itens não verificados); DGFIP-EDI Q1–Q7 (Q2 decide Model A) → ver F6-20261027-FR-C28, C30, C18 (2026-10-27)
- [ ] Design: Blocos 2 (contribuições + 6 matrizes), 3 e 4; mapear quais WTs ER alimentam 58130 (bloqueia 9250061); RA confirmar 24 [DERIVED]; escopo IDCC; 52560 sem valor; 52562/52563 fixo ou taxa — Wallisson/RA → ver F6-20261027-FR-C36 (2026-10-27): IDCC decidido como configuração por cliente (QA v4)
- [ ] Pesquisa: preencher Internal Code no DD e conformar ao v1.5; preencher colunas laranja do WTC; grade PAS em valores anuais; entregar FR-DGFIP-002 e FR-DSN-001 ao design — Research → ver F6-20261027-FR-C35 (2026-10-27): QA v4 trata Internal Code e colunas laranja vazios como não defeito; o pedido de preencher contradiz a decisão de 2026-08-27
- [ ] [INCERTO] Ex. 1 do FR-pack (bruto 2.915,50; contribuições 640,50; IR 126,61) vs CCG M12/payslip (2.800; 616,44; IR 94,06; líquido 2.089,50) — alvo de validação do design → ver F6-20261027-FR-C22 (2026-10-27)
- [ ] [INCERTO] Diálogo social 0,016% também EE (CCG M5.1, WTC FR-019) vs só ER (CCG M3, Ex. 1, payslip) → ver F6-20261027-FR-C27 (2026-10-27): nível B para "só empregador"; fonte A pendente; continua em aberto
- [ ] [INCERTO] CCG M4.2/Ex. 6 usa 151,67 mas o payslip manda 151,6667
- [ ] [INCERTO] CCG M10 cita "FR-NSSO / FR-FIN series" (resíduo da BE?); crítica cita WTC 378/DD 173 campos vs entregue 374/189 → ver F6-20261027-FR-C10 (2026-10-27)
- [ ] Prazo do 2502-SD: 31/jan vs 15/jan — (03-sir.md) (nenhum cartão F6 de 2026-10-27 resolveu)
- [ ] FR-CCG-001 v1.0 (pacote emitido em 06/10/2026), Mod. 12 Ex. 1: 3 números digitados que não fecham na conta. Termo interno impresso 0,875970 (correto 0,875870); 0,437985^1,75 impresso 0,235942 (correto 0,235805; o C final 0,1091 está certo); 2.915,50 × 13,00 % impresso 379,01 (correto 379,02, pela regra half-up do próprio CCG). O C38 reprova a CCG por isso, e um novo Stage 9 da França para nesse ponto. Decisão do usuário (17/10/2026): só registrar, sem v1.1 — Pipeline — (`revisoes/2026-10-17-matriz-cobertura-FR-pipeline.md`; `~/mercans-pipeline/IMPROVEMENT_LOG.md` 2026-10-07 Fase 2) → ver F6-20261027-FR-C22 (2026-10-27): o C38 não aparece em nenhum arquivo coletado do raw; a verificação "ao centavo" do QA v2/v3 (bruto 2.800,00) é do CCG anterior e não prova o CCG reemitido (bruto 2.915,50)
- [ ] Perguntar ao usuário: houve edição do WTC e do DD depois da promoção de 2026-10-09 sem nova linha no Version Control? (md5 do log × arquivos coletados; DD `8a91af3e…` × `889f66d2…`, WTC `553fb181…` × `8592d40b…`) (F6-20261027-FR-C04; validação humana pendente)
- [ ] Confirmar se o link do monday "CCG – AI" (atualizado em 2026-09-15, antes da reemissão) abre o CCG reemitido (md5 `a9f16a70…`) ou a linhagem antiga (F6-20261027-FR-C02; validação humana pendente)
- [ ] DD reemitido: corrigir o placeholder `<France>` na célula de título do Version Control (F6-20261027-FR-C05; validação humana pendente)
- [ ] SIR: confirmar se o conteúdo mudou entre o Version Control (2026-08-27) e o arquivo (2026-09-29) sem nova linha de versão (F6-20261027-FR-C06; validação humana pendente)
- [ ] Payslip: decidir o rótulo da versão vigente (md5 `d98d5416…`): "v1.0" (hub) ou "v1.1" (changelog de 2026-10-06); o arquivo não tem Version Control — usuário (F6-20261027-FR-C08; validação humana pendente)
- [ ] Reler a skill `fr-compliance` promovida em 2026-10-09 e reescrever a Ficha do país (a atual foi lida em 2026-10-02 e se apoia no `07-qa-report.md`, arquivado; a Ficha ainda cita "NEEDS PATCHES" e as armadilhas F-1..F-3) (F6-20261027-FR-C09; validação humana pendente)
- [ ] Contagem de WTs e de campos do DD do pacote reemitido: conferir abrindo os xlsx (linhagem anterior: 378 WTs / 198 campos; reemitido ≥ 379 WTs) (F6-20261027-FR-C10; validação humana pendente)
- [ ] F-1 ("NO DD COUNTERPART"): os baldes de reconciliação do QA v2 (88 + 63 + 52 + 36 + 9 + 8) somam 256, não 264; explicar as 8 linhas antes de afirmar "264/264" e "9 lacunas reais"; lista nominal das 9 lacunas não está nos arquivos coletados; verificar se a anotação sumiu das specs reemitidas (F6-20261027-FR-C12; validação humana pendente)
- [ ] F-2: valores dos BIK (refeição 5,50 / 11,00 / 2,75; ferramentas de comunicação 10 %) vêm do CCG Mod. 7 sem fonte A nos arquivos coletados; FR-075..FR-078 existem na linhagem anterior, reemitido não verificado (F6-20261027-FR-C13; validação humana pendente)
- [ ] FR-046 (base CSG/CRDS) com 23670–23673 (23673 = complemento de plano de poupança, confirmado no QA v4 contra 4 fontes não nomeadas): vale para o WTC v1.2 anterior; conferir no WTC reemitido (F6-20261027-FR-C20; validação humana pendente)
- [ ] SIR URSSAF-DPAE: `N_SIRET` com código de controle 02 corrigido para 01 (catálogo de erros P5 e caso T-09 do próprio SIR; nível B, artigo da URSSAF não citado nos arquivos); DGFIP-EDI 3 correções no `integration-landscape.json`; F27 (`integration_type` do FR-DGFIP-003) corrigido no scope_manifest (F6-20261027-FR-C18; validação humana pendente)
- [ ] Correções ligadas (abaixo), última linha: o hub atribui a `correcoes.md` o que ela não contém — a linha de "Description (NL)" não trata dos códigos 32/60/80; conferir e corrigir pela janela geral (F6-20261027-FR-C19; validação humana pendente)
- [ ] Diálogo social 0,016 %, só empregador: nível B (FR-TEST0 C12 PASS, passo B5 do PROMOTION-LOG de 2026-10-06, matriz `revisoes/2026-10-17-matriz-cobertura-FR-pipeline.md` linha 59); a citação da URSSAF no TEST0 não mostra o lado; falta fonte A (conferir a tabela patronal da página URSSAF "Taux de cotisations – Secteur privé"). Não fecha o [INCERTO] acima (F6-20261027-FR-C27; validação humana pendente)
- [ ] Pipeline, C29 (marcadores residuais): 6 "XXX" no exemplo `BNPAFRPPXXX` (Payslip EN/FR, DGFIP-001, DSN-001 ×3); possível BIC de exemplo (leitura nível D, nenhuma fonte de QA) — usuário decide se aceita como falso positivo e libera na lista do C29 (F6-20261027-FR-C24; validação humana pendente)
- [ ] Pipeline, C20 ("in-scope sem spec") reprova no recheck (sem data) enquanto C18 passa e o Stage 9 de 2026-09-02 dá C20 PASS (15 in-scope, 14 out-of-scope); tratar como não resolvido até rodar de novo (F6-20261027-FR-C25; validação humana pendente)
- [ ] Payslip, abas "How to set up Payslip" e "Compliance Payslip": QA v3/v4 pedem remover ("limpeza cosmética"), o override do C21 de 2026-09-02 diz que são abas padrão por desenho (desde a build de Moçambique); decidir com o dono do padrão (F6-20261027-FR-C26; validação humana pendente)
- [ ] Specs inbound sem layout oficial obtido: CPAM-003 (BPIJ: colunas dos exports csv/xls/pdf/xml não publicadas; 1º passo = export real de cliente com subrogação), CPAM-002 (IDAT: FORMAT TO CONFIRM; a spec cobre o cerfa 14463*03), DGFIP-002 (CRM PAS: só nível de bloco), CARSAT-001 (pode não existir layout publicado), AGIRC-001 (sem layout, XSD ou export); especificar a partir de amostra real antes de construir parser (F6-20261027-FR-C29; validação humana pendente)
- [ ] Itens abertos das specs a confirmar com a autoridade: BPIJ recuperável pela API da DSN e existência do XSD (net-entreprises a_id 3034); sinal do código 075 e dos CTP 996/997 (`S21.G00.23.005`) na FR-URSSAF-004 — até lá, não afirmar o sinal (F6-20261027-FR-C30; validação humana pendente)
- [ ] DPAE formato 120 (989 caracteres + LF = 990 bytes, ISO-8859-1, 24 campos, retornos 10/11/20/41): UNVERIFIED no FR-TEST0 R09 (host `www2.due.urssaf.fr` não respondeu em 2026-10-09); valor vem do runbook P4 (v5.4 com v5.3); repetir a conferência no PDF `v5.4_FormatDPAE_CFT.pdf` (F6-20261027-FR-C28; validação humana pendente)
- [ ] Taxe sur les salaires, abatimento do art. 1679 A: refazer a conferência quando sair o 2502-SD edição ANNEE 2026 (a edição guardada é 2025 e imprime 24.041; a notice 2501-NOT-SD 2026 dá 24.256; notice não lida por nós) (F6-20261027-FR-C31; validação humana pendente)
- [ ] SOLTéA: janela da campanha 2026 (26/05 a 21/10) vem do CCG Mod. 10, ⚠️ sem fonte A; o guia obtido descreve a campanha 2025; janela perdida não se recupera (saldo distribuído pela regra padrão); conferir na plataforma e lembrar o cliente anualmente (obrigação do payroll termina na FR-URSSAF-004: 0,09 % na DSN de abril, código 076) (F6-20261027-FR-C32; validação humana pendente)
- [ ] Pipeline: `wtc.log` e `payslip.log` terminam "Reached max turns (60)", `audit_content.log` "Reached max turns (80)", `reports.log` vazio; WTC e Payslip vieram da validação e das promoções, não de nova execução; não tratar esses logs como prova de conclusão (prova = Version Control, QA v3/v4, TEST0) (F6-20261027-FR-C33; validação humana pendente)
- [ ] Pipeline, C27 (768 mapeamentos sem link ao DD) e C33 (154 trechos possivelmente em idioma local) ficaram MANUAL no recheck; a amostra do C33 no JSON são linhas com símbolos de fórmula (`−`, `÷`, `^ 1.75`) rotuladas `non-latin-script` — provável falso positivo, a confirmar abrindo o CCG reemitido; divergência com o B10 do `ccg.log` (0 blocos) não explicada (F6-20261027-FR-C34; validação humana pendente)
- [ ] Montant net social: a inclusão da parcela patronal L911-1 a partir de 2027-01-01 depende de projeto de decreto (rubrique BOSS de 2026-10-02 e actualité BOSS de out/2026, citados só na nota do FR-TEST0); ⚠️ fonte A não lida, vigência não confirmada; o CCG registra a mudança numa nota datada (P178) (F6-20261027-FR-C37; validação humana pendente)
- [ ] SMIC anual do CCG M4.1 não verificado: a fonte imprime 21.876,64 (2026-01-01) e 22.404,20 (2026-06-01), que não batem com 12 × mensal (21.876,36; 22.404,24) nem com 12,02 × 1.820 (21.876,40, usado na RGDU); não citar a coluna anual do CCG; usar hora e mês (F6-20261027-FR-C40; validação humana pendente)

## Correções ligadas
- [[correcoes]]: QA das 12:21 deu 486/562 (86,5%); correto 720/984 (73,2%)
- [[correcoes]]: fontes secundárias com PASS derivado errado: 50.122 / faixa 4.440,01; correto 50.112 / 4.480,01 (usar o decreto, x1,02038)
- [[correcoes]]: manifest com DPAE "via net-entreprises" só XML; correto host da URSSAF, TXT 120 ou XML; DGFIP-003 é UN/EDIFACT INFENT DP nos dois sentidos
- [[correcoes]]: crítica de pesquisa dizia "não existe coluna de valor no mapper"; `local_value` existe no Master DD v1.5
- [[correcoes]]: cabeçalhos "Description (NL)" (resíduo da BE) para "Description (FR)"; códigos 32/60/80 excluídos sem nome para nomeados

## Fontes
- Cartões do pipeline (F6, 2026-10-27): [[extracoes/2026-10-27-pipeline-Franca|cartões]] · [[extracoes/2026-10-27-pipeline-Franca-conferencia|conferência]] · [[extracoes/2026-10-27-pipeline-Franca-correcoes-propostas|correções propostas]] · validação: [[extracoes/2026-10-27-pipeline-VALIDACAO|lotes]]
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- raw/chats/2026-10-01-mercans-compliance.md
- skill payroll-compliance-france (lida em 2026-10-02)
- `raw/pipeline/Franca/2026-10-27/` e `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` (F6, 2026-10-27)
