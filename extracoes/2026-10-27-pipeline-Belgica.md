# Extração: pipeline, Bélgica (2026-10-27)

> Arquivo: `extracoes/2026-10-27-pipeline-Belgica.md`. Um cartão por item. Só entra o que muda a resposta certa.
> Material bruto: `raw/pipeline/Belgica/2026-10-27/` (qa, logs, notas, version-control) e `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` · Inventário: `inventarios/pipeline.md` (item 1, BE-compliance) · Padrão: [[PLANO]] §4 (níveis A/B/C/D) e §5 (validação, lotes de até 40).
> Convenções deste arquivo: `VC/` = `raw/pipeline/Belgica/2026-10-27/version-control/`; `QA/` = `raw/pipeline/Belgica/2026-10-27/qa/`; `NOTAS/` = `raw/pipeline/Belgica/2026-10-27/notas/`; `LOGS/` = `raw/pipeline/Belgica/2026-10-27/logs/`. Números de linha são do arquivo em `raw/` (não do original no pipeline). Base do brain para as versões: `Research Pipeline/Belgium/` (só listada, nenhum binário aberto).
> Nível: Version Control e relatório de QA fechado = B. Quando o QA cita lei/fonte oficial, a fonte A vem registrada como fonte e o cartão diz "B que cita A"; o usuário confere o A na validação. Valor sem A citado não entra: vira pendência.
> Antes de ler: o QA mais recente é `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` (escrito em 25/08, cópia no raw com esse nome) e `QA/handover_status.md` (2026-09-16). `QA/BE-QA-REPORT.md`, `BE-MASTER-PENDING-LIST-2026-08-24.md` e as investigações de 14/08 são anteriores e estão parcialmente superados; cada cartão diz em qual estado está.

## Resumo
- Itens do inventário neste lote: 1 (BE-compliance: 22 arquivos de qa, 66 logs, 12 notas, 12 Version Controls extraídos) · Cartões: 40 (15 versão final · 16 erro+causa · 1 alerta · 8 pendência) · Complementos de cartão existente: 29 (os outros 11 são novos) · Descartados: 29 linhas na tabela (14 itens "lote 2" e 15 já registrados, superados, ruído ou não relidos)
- Risco alto: 34 (100% vão para validação) · Amostra dos demais: 6 cartões normais, sorteio de 10% = 1 (mínimo 1)
- [INCERTO]: 3 (C04, C05, C38)
- Validação: ⏳ pendente
- Ingestão: ✅ feita em 2026-10-27 (hub; correcoes pela janela geral)

Divergências mais importantes (para a validação começar por elas): C25 (697,61 é o certo; o hub tem a direção invertida), C31 (o hub diz "6 blockers e 11 majors abertos", o QA final fechou 6 e 10 dos 11), C01–C03 (o mesmo número de versão significa conteúdo diferente no pipeline, no Drive/monday e no brain), C33 (o hub afirma como fato um ponto que o QA do pipeline rebaixou para "não resolvido").

## Cartões

### F6-20261027-BE-C01 · versão final · [[Belgica]]
- **Chave:** `BE | CCG | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues ("sem versão citada"; skill: v1.2) e hub §Ficha, linha "Versões de registro" (CCG v1.0 do Drive = v1.2 do pipeline + patronal 19,88% de 13/10)
- **Tipo:** versão final (com divergência)
- **Risco:** alto (versão vigente, divergência pipeline × Drive × monday)
- **Serviço:** [[research-pipeline]]
- **O que diz:** No pipeline o CCG é [[frentes/pipeline/mercans-pipeline/BE-compliance/01-ccg/BE-CCG-001-v1.2.docx|BE-CCG-001-v1.2.docx]] (arquivo de 2026-09-16, md5 `fa17e8d09d44fc3f13fce7c2c46a3695`), promovido (sem -DRAFT), renomeado de v1.1 para v1.2 no Stage 9.6. Não tem tabela de Version Control: só a linha "Version 1.2 — 16 September 2026 (supersedes version 1.1 of 21 August 2026)" (limitação BE-TF-011, "deixada em aberto, a decidir pelo dono"). O monday rotula o CCG como `BE-CCG-001 v1.0` (item 13064532271, atualizado 2026-09-16, status Done). O hub e a nota de refresh da skill dizem que o Google Doc do Drive se chama v1.0, mas a capa interna diz "Version 1.2 — 16 September 2026", e que o Drive já tem a correção patronal 19,88% de 13/10, que o pipeline não tem.
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a. O mesmo conteúdo-base circula com dois rótulos (v1.2 no pipeline, v1.0 no Drive/monday) e o Drive tem uma correção posterior.
- **Correto / novo:** Por número (regra 8) o maior é v1.2 (pipeline). Por conteúdo, o mais novo é o do Drive (v1.2 de capa + 19,88%), com rótulo "v1.0". Não escolhi em silêncio: decisão do usuário sobre qual rótulo registrar no hub. O CCG do pipeline é o que ainda traz a taxa patronal 24,92% (ver C32).
- **Nível de evidência:** B · **Fonte:** `VC/MANIFEST.md` (CCG sem VC; md5; data) + monday + hub + `Research Pipeline/Belgium/2026-10-21-skill-refresh/CONFERENCIA.md` (§Base e §Achados fora do pedido)
- **Localização no raw:** `VC/MANIFEST.md` linha 5; `QA/handover_status.md` linhas 283-298 (§8, Step 1: bump 1.1 → 1.2, BE-TF-011); `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` linha 10
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues (linha CCG) e §Ficha "Versões de registro"
- **Pergunta para o teste (Conjunto B)?** sim → "Qual é a versão vigente do CCG da Bélgica e onde está o texto com a taxa patronal correta?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C02 · versão final · [[Belgica]]
- **Chave:** `BE | WTC | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues ("sem versão citada"; skill: v1.1) e hub §Ficha ("WTC v1.3 (1.182 linhas)")
- **Tipo:** versão final (com divergência)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** Pipeline: `BE-WTC-001-v1.1.xlsx` (2026-09-16, md5 `c47ad5142ce7f1469d2b98074ad05d49`), 359 linhas na aba Wage Type Catalogue, Version Control com 2 linhas: `1 | 2026-08-13 | Draft` e `1.1 | 2026-09-16 | STAGE 9.5 GAP CLOSURE ... | Released`. O arquivo se chamava v1.0 até o Stage 9.6 (versão interna já era 1.1). monday: `BE-WTC-001-v1.0` (item 13064563990, atualizado 2026-09-16). Brain: `Research Pipeline/Belgium/2026-10-21-wtc-series-62-65-74/` tem v1.1, v1.2, v1.3, e a CONFERENCIA de lá diz que a aba Wage Type Catalogue do Drive v1.0 e do pipeline v1.1 é idêntica (359 linhas, 0 diferenças A–T).
- **Antes (se erro):** n/a
- **Causa (se erro):** Colisão de rótulo: o "v1.1" do pipeline (359 linhas, 16/09) não é o "v1.1" do brain (que acrescenta as linhas 361–828 das séries 62/65/79, 21/10). O Drive continua em v1.0.
- **Correto / novo:** Vigente = a de maior número do brain (v1.3, derivada da linhagem do Drive), não a do pipeline. O pipeline v1.1 é conteúdo-base idêntico ao Drive v1.0. Ao citar "WTC v1.1" é obrigatório dizer de qual linhagem.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control + CONFERENCIA do brain
- **Localização no raw:** `VC/BE-WTC-001-v1.1.md` linhas 11-12 (linhas 1 e 1.1 do VC); `VC/MANIFEST.md` linha 6; `QA/handover_status.md` linhas 285-289 (tabela do §8: interna 1.1, arquivo 1.0); `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` linha 9
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues (linha WTC)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual é o WTC vigente da Bélgica e quantas linhas tem?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C03 · versão final · [[Belgica]]
- **Chave:** `BE | DD | versão vigente` · **Já existe?** sim → complementa hub §Ficha ("DD v1.0 do Drive = v1.4 do pipeline; 92 blocos / 2.018 códigos")
- **Tipo:** versão final
- **Risco:** alto
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** Pipeline: [[frentes/pipeline/mercans-pipeline/BE-compliance/05-data-dictionary/BE-DD-001-v1.4.xlsx|BE-DD-001-v1.4.xlsx]] (2026-09-16, md5 `11f74851776f1bbb5a3af3573b3c1086`), VC com linhas 1.0, 1.1, 1.3, 1.4 `Released` e 1.2 "não registrada e não reconstruível" (sem descrição, status nem autor; 1.3 sem autor; BE-TF-008). Renomeado de v1.3 para v1.4 no Stage 9.6 (a versão de registro era 1.4 desde o Stage 9.5). monday: `BE-DD-001-v1.0` (item 13064616093). O hub e a nota de refresh dizem que o Drive v1.0 é idêntico ao v1.4 do pipeline, exceto Version Control e Introduction. Contagens do mapper em três lugares diferentes: VC 1.4 "87 blocos / 1.043 linhas → 92 blocos / 2.018 linhas"; handover §2 "92 blocos / 2.023 linhas"; handover §8 passo 4 "92 blocos / 1.816 linhas de código".
- **Antes (se erro):** n/a
- **Causa (se erro):** Três medidas distintas (linhas totais da aba, linhas com código, contagem na releitura) circulam como se fossem a mesma.
- **Correto / novo:** Vigente = DD do Drive (rótulo v1.0, conteúdo = pipeline v1.4). Não afirmar "2.018 códigos" sem dizer a medida; registrar as três e a fonte de cada uma.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control + handover
- **Localização no raw:** `VC/BE-DD-001-v1.4.md` linhas 11-15 (VC 1.0 a 1.4; texto da 1.4 traz "2,018 rows"); `QA/handover_status.md` linha 73 (2.023), linhas 285-288 e 331-334 (§8 passo 4, 1.816); `VC/MANIFEST.md` linha 17; `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` linha 8
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha (versões de registro) e §Artefatos entregues
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (as três contagens não se reconciliam só com o que está no raw)
- **Validação:** ◐ conferência independente: Causa trocada por: três contagens do mesmo mapper no raw (VC 1.4: 2.018 linhas; handover §2: 2.023; handover §8 passo 4: 1.816 linhas de código), sem dizer a medida de cada uma; linha 1.2 do VC sem descrição de mudança, status nem autor · humana ⏳

### F6-20261027-BE-C04 · versão final · [[Belgica]]
- **Chave:** `BE | SIR | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues (SIR sem versão) e §Ficha (SIR v1.0)
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** `BE-SIR-001-v1.0.docx`, arquivo de 2026-09-29 (md5 `835d476f10c3c8ff9e6909724d3b8e4b`). A tabela de VC tem 2 linhas, ambas "v1.0": 2026-08-14 "Initial issue" e 2026-08-17 "Revised after Stage 3 completed: the nine Report Specs are now named per flow". monday e hub concordam em v1.0 (monday atualizado 2026-09-29).
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a
- **Correto / novo:** Vigente = v1.0, sem divergência de rótulo. Anomalia: a data do arquivo (29/09) é posterior à última linha do VC (17/08), então existe uma alteração de 29/09 que o VC não registra. O handover §8 também lista o SIR com strings de versão antigas (DD ×2, WTC ×1, CCG ×3; BE-TF-012), fora do escopo daquele passo.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control
- **Localização no raw:** `VC/BE-SIR-001-v1.0.md` linhas 7-10 (tabela); `VC/MANIFEST.md` linha 7; `QA/handover_status.md` linhas 347-353; `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` linha 12
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues (linha SIR)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (não sei o que mudou em 29/09; o raw só dá a data do arquivo)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C05 · versão final · [[Belgica]]
- **Chave:** `BE | Report Spec Dimona (BE-NSSO-001) | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues ("Report Specs Bélgica (9 specs)") e §Ficha ("specs v1.1 (EN)")
- **Tipo:** versão final (com divergência; vale para C05–C13)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** Pipeline: última linha do VC = `1.3 | 2026-08-24 | ISSUE-B content re-alignment ... | Draft`; arquivo sem versão no nome (`BE-NSSO-001-Dimona-Spec.xlsx`, 2026-09-16, md5 `e519443bb95010bd194f0ddc03ab2414`). O brain tem [[Research Pipeline/Belgium/2026-10-19-specs-idioma-ingles/BE-NSSO-001-Dimona-Spec_v1.1.xlsx|BE-NSSO-001-Dimona-Spec_v1.1.xlsx]] (Field Explanation em inglês, base = exports do Drive "todos 1.0"). monday não tem item para Report Specs.
- **Antes (se erro):** n/a
- **Causa (se erro):** Colisão de rótulo: no pipeline a linha "1.1" é o "Stage 8 alignment patch" de 14/08; no brain "v1.1" é a tradução EN de 19/10. Além disso, todas as linhas de VC do pipeline estão "Draft" (ISSUE-G: nenhuma spec foi promovida de status).
- **Correto / novo:** Por número, o pipeline (1.3) é maior; o brain (v1.1 EN) é a base entregável. Não dá para dizer que o brain v1.1 contém o conteúdo da 1.3 (ex.: domínio completo de Days Justification 1–7): não comparei célula a célula (regra do prompt: não abrir binário). Ação sugerida: diff Drive 1.0 × pipeline 1.3 antes de afirmar qual é a vigente.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control (spec) + CONFERENCIA do brain
- **Localização no raw:** `VC/BE-NSSO-001-Dimona-Spec.md` linha 16 (linha 1.3) e linha 14 (linha 1.1); `VC/MANIFEST.md` linha 12; `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linhas 154-174 (Check 8: VC = Report Matrix); `QA/BE-MASTER-PENDING-LIST-2026-08-24.md` linha 363 (MP-RSPEC-02, todas "Draft"); brain: `Research Pipeline/Belgium/2026-10-19-specs-idioma-ingles/CONFERENCIA.md` (§Versionamento e §Entradas)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues (linha Report Specs)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual é a versão vigente da spec do Dimona na Bélgica?"
- **Confiança da extração:** [INCERTO] (equivalência de conteúdo entre o export 1.0 do Drive e o 1.3 do pipeline não verificada; vale para C06–C13 como "média, mesma dúvida do C05")
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C06 · versão final · [[Belgica]]
- **Chave:** `BE | Report Spec DmfA (BE-NSSO-002) | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final (divergência igual à do C05)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** Pipeline: VC `1.3 | 2026-08-24 | ... | Draft` (arquivo 2026-09-16, md5 `90ef6d76898e6750117552e9a11590d6`). Brain: `BE-NSSO-002-DmfA-Spec_v1.1.xlsx` (EN, 19/10). Na 1.2 de 16/08 foram reapontadas 82 células de System Mapping para campos do DD e 40 deixadas sem mapeamento por desenho.
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a (ver C05)
- **Correto / novo:** Pipeline 1.3 (Draft) × brain v1.1 EN; decisão como no C05.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control
- **Localização no raw:** `VC/BE-NSSO-002-DmfA-Spec.md` linhas 15-16; `VC/MANIFEST.md` linha 13
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (mesma dúvida do C05)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C07 · versão final · [[Belgica]]
- **Chave:** `BE | Report Spec DmfA Modification (BE-NSSO-003) | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final (divergência igual à do C05)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** Pipeline: VC `1.3 | 2026-08-24 | ... | Draft` (arquivo 2026-09-16, md5 `d71f9e80e5dae78a05f51f0bda7c1c83`). Brain: `BE-NSSO-003-DmfAModification-Spec_v1.1.xlsx` (EN). O layout de campos é idêntico ao da DmfA; a spec documenta a semântica da correção.
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a (ver C05)
- **Correto / novo:** Pipeline 1.3 (Draft) × brain v1.1 EN; decisão como no C05. O bloco-contêiner 90169 desta spec: ver C27.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control
- **Localização no raw:** `VC/BE-NSSO-003-DmfAModification-Spec.md` linhas 15-16; `VC/MANIFEST.md` linha 14
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (mesma dúvida do C05)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C08 · versão final · [[Belgica]]
- **Chave:** `BE | Report Spec DRS (BE-NSSO-004) | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final (divergência igual à do C05)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** Pipeline: VC `1.3 | 2026-08-24 | ... | Draft` (arquivo 2026-09-16, md5 `c1b3c69bad6642e0ef71442517dba821`). Brain: `BE-NSSO-004-DRS-Spec_v1.1.xlsx` (EN). Cobre os cenários DRS de indenização (134 zonas) e desemprego (67 zonas), glossários 2026/2.
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a (ver C05)
- **Correto / novo:** Pipeline 1.3 (Draft) × brain v1.1 EN; decisão como no C05.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control
- **Localização no raw:** `VC/BE-NSSO-004-DRS-Spec.md` linhas 15-16; `VC/MANIFEST.md` linha 15
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (mesma dúvida do C05)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C09 · versão final · [[Belgica]]
- **Chave:** `BE | Report Spec Limosa (BE-NSSO-005) | versão vigente` · **Já existe?** sim → complementa hub §Ficha ("Limosa descartado, só referência") e §Artefatos entregues
- **Tipo:** versão final (descartada por decisão de escopo)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** Pipeline: VC `1.3 | 2026-08-17 | DESCOPED ... | Descoped` (arquivo 2026-09-16, md5 `73234005f8abb84d38b7a2afdf378240`). O dono decidiu (BE-SCOPE-014 / L-14) que a declaração Limosa é feita pelo empregador estrangeiro que destaca o trabalhador; a spec é mantida como registro e **não é alvo de build**. Brain: `BE-NSSO-005-Limosa-Spec_v1.1.xlsx` (v1.1 só pela citação do DD).
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a
- **Correto / novo:** Limosa fora do escopo desde 2026-08-17; SIR OUT-08 é o único fluxo de saída ausente do manifest (18 entradas) por essa decisão. Não tratar o "v1.3" como versão entregável.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control + QA fechado
- **Localização no raw:** `VC/BE-NSSO-005-Limosa-Spec.md` linha 16; `VC/MANIFEST.md` linha 16; `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linhas 127-137 (Check 6)
- **Quem decidiu / pediu:** dono do pipeline (Updated By: Wallisson Gomes), ruling de 2026-08-17 sobre BE-SCOPE-014 / L-14
- **Destino:** hub §Artefatos entregues
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C10 · versão final · [[Belgica]]
- **Chave:** `BE | Report Spec FEDRIS acidente de trabalho (BE-FEDRIS-001) | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final (divergência igual à do C05)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** Pipeline: VC `1.3 | 2026-08-24 | ... | Draft` (arquivo 2026-09-16, md5 `5be19a9cfff78a68865c78b326d187bc`). Brain: `BE-FEDRIS-001-WorkAccident-Spec_v1.1.xlsx` (EN). Glossário NSSO DRS FAT cenário 1, edição 2026/2.
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a (ver C05)
- **Correto / novo:** Pipeline 1.3 (Draft) × brain v1.1 EN; decisão como no C05.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control
- **Localização no raw:** `VC/BE-FEDRIS-001-WorkAccident-Spec.md` linhas 15-16; `VC/MANIFEST.md` linha 9
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (mesma dúvida do C05)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C11 · versão final · [[Belgica]]
- **Chave:** `BE | Report Spec Finprof 274 (BE-FIN-001) | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final (divergência igual à do C05)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** Pipeline: última linha do VC = `1.2 | 2026-08-16 | DD version alignment ... | Draft` (arquivo 2026-09-16, md5 `ffb82f9ed91e30e2f4c7affc893109db`); esta spec **não** teve a rodada 1.3 de 24/08. Brain: `BE-FIN-001-Finprof274-Spec_v1.1.xlsx` (v1.1 só pela citação do DD). Fonte da spec: descrição de arquivo SS274EUR-XML do SPF Finanças; o QA registra que o período-código da série 2026 não é conhecido (ver C37).
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a (ver C05)
- **Correto / novo:** Pipeline 1.2 (Draft) × brain v1.1; decisão como no C05.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control
- **Localização no raw:** `VC/BE-FIN-001-Finprof274-Spec.md` linha 15; `VC/MANIFEST.md` linha 10; `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linhas 158-166 (Check 8: 1.2 = 1.2)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (mesma dúvida do C05)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C12 · versão final · [[Belgica]]
- **Chave:** `BE | Report Spec Belcotax 281.10 (BE-FIN-002) | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final (divergência igual à do C05)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** Pipeline: última linha do VC = `1.2 | 2026-08-16 | DD version alignment ... | Draft` (arquivo 2026-09-16, md5 `9f4054808eb3d4e4bf02be0b9d68276f`). Construída sobre a brochura Belcotax-on-web do ano de renda 2025 (v3.0 de 14/01/2026, 119 tags). Brain: `BE-FIN-002-Belcotax28110-Spec_v1.1.xlsx` (v1.1 só pela citação do DD). As quatro células que apontavam a lacuna do box 360 (L127, N127, File Structure A80, Population Rules E14) foram atualizadas em 17/08 (ver C24).
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a (ver C05)
- **Correto / novo:** Pipeline 1.2 (Draft) × brain v1.1; decisão como no C05.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control
- **Localização no raw:** `VC/BE-FIN-002-Belcotax28110-Spec.md` linha 15; `VC/MANIFEST.md` linha 11
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (mesma dúvida do C05)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C13 · versão final · [[Belgica]]
- **Chave:** `BE | Report Spec SEPA Credit Transfer (BE-FEBELFIN-001) | versão vigente` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final (divergência igual à do C05)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** Pipeline: última linha do VC = `1.2 | 2026-08-16 | DD version alignment ... | Draft` (arquivo 2026-09-16, md5 `f3ebcf519be7fe54ca01110968d15129`). Cobre SIR OUT-09 (salário líquido), OUT-10 (contribuições) e OUT-11 (retenção), ISO 20022 pain.001.001.09, guia Febelfin 2025 v1.3. Brain: `BE-FEBELFIN-001-SEPACreditTransfer-Spec_v1.1.xlsx` (v1.1 só pela citação do DD).
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a (ver C05)
- **Correto / novo:** Pipeline 1.2 (Draft) × brain v1.1; decisão como no C05.
- **Nível de evidência:** B · **Fonte:** artefato com Version Control
- **Localização no raw:** `VC/BE-FEBELFIN-001-SEPACreditTransfer-Spec.md` linha 15 (e linha 13 para o escopo OUT-09/10/11); `VC/MANIFEST.md` linha 8
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (mesma dúvida do C05)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C14 · versão final · [[Belgica]]
- **Chave:** `BE | Payslip Generator | versão` · **Já existe?** não (o hub não tem linha de Payslip em §Artefatos entregues)
- **Tipo:** versão final (artefato sem versão registrada)
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** [[frentes/pipeline/mercans-pipeline/BE-compliance/06-payslip/BE_Compliance_Payslip_Generator.xlsx|BE_Compliance_Payslip_Generator.xlsx]] (2026-09-16, md5 `d904c63e4957ab7d09572942b1a9788f`): sem aba de Version Control, sem versão no nome do arquivo e sem item no board do monday (o grupo Belgium só tem DD, WTC, CCG, Skill e SIR). Portanto não existe versão vigente declarada para o Payslip. O handover §8 lista ainda uma string de versão antiga do WTC dentro dele (BE-TF-012). O Payslip tem 8 abas (EN e NL; francês e alemão não construídos, L-16) e é o único artefato sem verificador funcional (`_verify_payslip.py` aborta com `NameError: IFERROR`, T-05).
- **Antes (se erro):** n/a
- **Causa (se erro):** O gerador de payslip nunca recebeu aba de VC (o Stage 12 o incluía no escopo e não encontrou VC; ver o MANIFEST).
- **Correto / novo:** Registrar no hub "Payslip BE: sem versão declarada (arquivo de 2026-09-16)" e não inventar número. Ficam como estão os pontos já no hub (FR/DE não construídos).
- **Nível de evidência:** B · **Fonte:** MANIFEST de VC + QA fechado
- **Localização no raw:** `VC/MANIFEST.md` linha 18 (última linha: "VC encontrado: não"); `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linhas 56 e 256 (T-05); `QA/handover_status.md` linhas 347-353; `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` linha 14 ("Sem item para Report Specs nem Payslip no grupo")
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues (acrescentar linha)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C15 · versão final · [[Belgica]]
- **Chave:** `BE | Skill payroll-compliance-belgium | versão` · **Já existe?** sim → complementa hub §Artefatos entregues (linha Skill) e §Ficha (skill lida em 2026-10-02; refresh de 21/10; v4 publicada em 23/10)
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** O Stage 11 do pipeline compilou a skill em 2026-09-16: `SKILL.md` 26.711 bytes (356 linhas) e 7 referências (3,1 MB), descrição de 1.078 caracteres (acima do limite de 1.024 do upload do claude.ai). monday: `payroll-compliance-belgium`, Done, 2026-09-16. O brain tem a skill mais nova (refresh de 21/10 pela linhagem do Drive, descrição de 863 caracteres, v4 publicada em 23/10).
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a
- **Correto / novo:** Vigente = a do brain (v4, 23/10). A skill do pipeline é mais velha que a data de leitura da Ficha (2026-10-02), então pela regra do Passo 3 **a Ficha do país não é atualizada a partir dela**.
- **Nível de evidência:** B · **Fonte:** log do build da skill + monday
- **Localização no raw:** `LOGS/skill_build.log` linhas 1-17 (árvore, tamanhos, descrição 1.078); `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` linha 11; brain: `Research Pipeline/Belgium/2026-10-21-skill-refresh/CONFERENCIA.md` (§O que mudou no pacote)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Artefatos entregues (sem mudança de conteúdo; só confirmar)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C16 · erro+causa · [[Belgica]]
- **Chave:** `BE | CCG+WTC | isenção básica na retenção` · **Já existe?** sim → complementa hub §Ficha, armadilha 2 e Valores-âncora ("Isenção básica na retenção 11.170")
- **Tipo:** erro+causa
- **Risco:** alto (valor estatutário, correção de erro)
- **Serviço:** [[research-pipeline]]
- **O que diz:** CCG e WTC usavam EUR 11.180 em todo lugar como isenção básica de 2026; o certo para a retenção na fonte é 11.170.
- **Antes (se erro):** CCG/WTC v1.0 do pipeline: isenção 11.180 e redução 2.990,65 (a investigação de 14/08 cita 21 ocorrências no texto do CCG). A revisão de conteúdo tinha marcado 11.180 como "confirmado" por fonte secundária (um prestador de serviços de folha belga).
- **Causa (se erro):** 11.180 é o valor contrafactual indexado do art. 131 CIR 92 (base antiga 4.785 × coeficiente 2,3356 = 11.175,85) que a reforma impediu de vigorar; nunca foi lei. As fontes secundárias também confundiam aanslagjaar 2026 (ano de renda 2025) com 2027 (rótulo deslocado em um ano).
- **Correto / novo:** retenção (Anexo III, nr. 32): isenção 11.170, redução 2.987,98, ano de renda 2026. Apuração (art. 131 CIR 92, aanslagjaar 2027): 11.550 (4.945 × 2,3356), após a Lei de 15/07/2026. A base não indexada passa de 4.785 para 4.945 a partir do aanslagjaar 2027.
- **Nível de evidência:** B que cita A · **Fonte:** Bijlage III do Real Decreto de 11/12/2025 (BS 29/12/2025, p. 97613), nr. 32; Lei de 15/07/2026 de reforma do IR (BS 29/07/2026, p. 40196, NUMAC 2026005724), arts. 2 e 4; aviso de indexação aanslagjaar 2027 (BS 12/08/2026, NUMAC 2026006085), Tabela I
- **Localização no raw:** `QA/ALLOWANCE_INVESTIGATION.md` linhas 9-19 (§1 tabela das três cifras) e linhas 31-65 (§2.1); `QA/TAX_ENGINE_FIX_APPLIED.md` linha 15 (§1, item 1); `QA/CCG_CONTENT_REVIEW.md` linha 14 (verificação inicial por fonte secundária); `LOGS/skill_build.log` (spot-check 1: `11,170`×16, `11,180`×0)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha armadilha 2 (acrescentar a causa e a fonte A com NUMAC)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual isenção básica entra na retenção belga de 2026 e por que não 11.180?"
- **Confiança da extração:** alta
- **Validação:** ◐ conferência independente: removida a frase '21 ocorrências no CCG' do 11.180 (as 21 ocorrências são do 11.170 já corrigido, MP-CCG-08) · humana ⏳

### F6-20261027-BE-C17 · erro+causa · [[Belgica]]
- **Chave:** `BE | CCG+WTC | tetos das faixas da retenção` · **Já existe?** sim → complementa hub §Ficha, armadilha 3
- **Tipo:** erro+causa
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** O CCG usava os tetos de faixa da escala de apuração dentro da fórmula de retenção; a retenção tem escala própria.
- **Antes (se erro):** Fórmula e exemplos de m06/m08/m09/m12 com tetos 16.720 / 29.510 / 51.070 (nove exemplos afetados; m12 E2 isolado).
- **Causa (se erro):** A escala do art. 130 CIR (apuração, aanslagjaar 2027) foi reaproveitada como se fosse a escala-base do Anexo III nr. 31; o Anexo III tem sua própria convenção de arredondamento para baixo.
- **Correto / novo:** tetos da retenção 16.710 / 29.500 / 51.050, com constantes acumuladas 4.469,93 / 9.944,05 / 20.320,38 (a da 4ª faixa não existia no CCG). Alíquotas 26,75 / 42,80 / 48,15 / 53,50% estavam certas. A tabela de apuração (16.720/29.510/51.070 a 25/40/45/50%) fica como está. Efeito pequeno e sistemático: +0,13 a +0,18 por mês na 3ª faixa; combinado com 11.170 e nr. 38: +0,36 a +0,40/mês sem filhos.
- **Nível de evidência:** B que cita A · **Fonte:** Bijlage III do RD de 11/12/2025 (BS 29/12/2025), nr. 31; RD de 24/07/2026 (BS 30/07/2026, NUMAC 2026005690) não alterou o nr. 31
- **Localização no raw:** `QA/BRACKET_INVESTIGATION.md` linhas 10-31 (§1) e §9 Sources; `QA/CHILDREN_SUPPLEMENT_INVESTIGATION.md` linha 289 (§6(a), onde o defeito apareceu); `QA/TAX_ENGINE_FIX_APPLIED.md` linha 17 (§1, item 3); `LOGS/skill_build.log` (spot-check 2)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha armadilha 3 (acrescentar causa e constantes)
- **Pergunta para o teste (Conjunto B)?** sim → "Quais os tetos de faixa da retenção belga de 2026?"
- **Confiança da extração:** alta
- **Validação:** ◐ conferência independente: módulos afetados = 6, 9 e 12 (m08 estava correto); causa = escala do art. 130 reaproveitada, tetos do nr. 31 não deriváveis por arredondamento (BRACKET §2.6) · humana ⏳

### F6-20261027-BE-C18 · erro+causa · [[Belgica]]
- **Chave:** `BE | CCG | alívio por filho dependente` · **Já existe?** não (a Ficha não lista essa armadilha)
- **Tipo:** erro+causa
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** O CCG tratava o alívio por filho como acréscimo à isenção básica; no Anexo III é uma redução fixa em euros depois do cálculo.
- **Antes (se erro):** CCG m06: `26,75% × (11.180 + suplementos 2.030 / 5.230 / 11.720)`; economia de EUR 116,59/mês com 2 filhos.
- **Causa (se erro):** Mecanismo errado, não só valor desatualizado. A origem dos 2.030/5.230/11.720 não foi explicada: a hipótese de confusão com o valor de contribuinte com deficiência (art. 132) não explica 5.230 nem 11.720.
- **Correto / novo:** Isenção continua 11.170 (redução 2.987,98) e depois uma redução fixa da basisbelasting (Anexo III nr. 38): 624 / 1.656 / 4.404 / 7.620 / 11.100 / 14.592 / 18.120 / 21.996 por ano para 1 a 8 filhos, mais 3.864 por filho além do 8º; filho com deficiência conta em dobro (nr. 8). Com 2 filhos: EUR 138,00/mês (1.656/12). Não residente na escala III não tem esse alívio (nr. 108/111). O handover de 16/09 reconfirma que o CCG cita "nr. 38" com esses valores, batendo linha a linha com o instrumento.
- **Nível de evidência:** B que cita A · **Fonte:** Bijlage III do RD de 11/12/2025, nr. 38 ("38. La réduction pour enfants à charge s'élève à...") e nr. 8
- **Localização no raw:** `QA/CHILDREN_SUPPLEMENT_INVESTIGATION.md` linhas 62-105 (§2.2-2.3), 196-232 (§4); `QA/TAX_ENGINE_FIX_APPLIED.md` linha 16 (§1, item 2) e linhas 77-85 (§3.3); `QA/handover_status.md` linhas 99-116 (§3.2)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha (nova armadilha) e skill `payroll-compliance-belgium`
- **Pergunta para o teste (Conjunto B)?** sim → "Como o Anexo III trata o alívio por filho na retenção belga?"
- **Confiança da extração:** alta
- **Validação:** ◐ conferência independente: origem do 2.030 = art. 131, 3º parágrafo (contribuinte com deficiência); art. 132 é a tabela de suplementos por filho (2.130/5.130/11.440) · humana ⏳

### F6-20261027-BE-C19 · erro+causa · [[Belgica]]
- **Chave:** `BE | CCG | retenção sobre indenização de aviso prévio` · **Já existe?** sim → complementa hub §Ficha, armadilha 4
- **Tipo:** erro+causa
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** O exemplo de rescisão retinha a indenização de aviso prévio pela tabela nr. 53; o certo é a escala de atrasados e rescisão (nr. 58 via nr. 62).
- **Antes (se erro):** m09 (CCG v1.0) 53,50%, retenção 21.216,78.
- **Causa (se erro):** O nr. 53 exclui por texto as `opzeggingsvergoedingen` ("voor andere exceptionele vergoedingen en toelagen dan opzeggingsvergoedingen"); o nr. 62 manda aplicar a escala dos nrs. 58 a 60.
- **Correto / novo:** 38,96% (remuneração-base 67.778,40, faixa 62.465,01–71.160,00): retenção 15.450,58; sobre-retenção do erro: 5.766,20. Cinco outras afirmações do CCG foram corrigidas na mesma passada e a tabela de 18 faixas do nr. 58 passou a ser publicada no Módulo 9.1. A referência pela fórmula x 13,92 cai na mesma faixa. Atrasados **não** foram mexidos (ver C34).
- **Nível de evidência:** B que cita A · **Fonte:** Bijlage III do RD de 11/12/2025, nrs. 53, 58-60, 62
- **Localização no raw:** `QA/TAX_ENGINE_FIX_APPLIED.md` linhas 29-43 (§2) e 129-171 (§3.7b); `QA/BRACKET_INVESTIGATION.md` linhas 318-399 (§6(a)); `LOGS/skill_build.log` (extras: "nr.58/nr.62/nr.53 routing with the EUR 5,766.20 delta PASS")
- **Quem decidiu / pediu:** autorização do item 5 dada na segunda passada de 14/08 (Wallisson Gomes, dono do pipeline); sem nome no raw além do campo "Updated By"
- **Destino:** hub §Ficha armadilha 4
- **Pergunta para o teste (Conjunto B)?** sim → "Qual tabela do Anexo III retém a indenização de aviso prévio?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C20 · erro+causa · [[Belgica]]
- **Chave:** `BE | CCG | retenção do holiday pay de saída (exemplo Módulo 9)` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** No exemplo de saída, a parte "dupla" do pecúlio de férias era retida a 47,44%; a faixa certa é 53,50% nas duas metades.
- **Antes (se erro):** `7,67% simples a 53,50%, 7,67% dupla a 47,44%` → retenção total EUR 1.213,60.
- **Causa (se erro):** Erro de seleção de faixa: a remuneração de referência anual (62.640) passa de 59.900 nas duas tabelas (exceptional payment e holiday pay), onde a faixa de topo é 53,50%; 47,44% é a segunda faixa (45.860,01–59.900,00).
- **Correto / novo:** 53,50% para as duas metades → retenção EUR 1.284,17 (líquido 1.116,14; Total do exemplo: retenção 24.201,73 / líquido 23.071,92 na época). O pecúlio de férias de saída não é rescisão, por isso continua no nr. 53 (a tabela do Módulo 8 foi confirmada correta). Valor do exemplo, não parâmetro estatutário novo.
- **Nível de evidência:** B · **Fonte:** revisão de conteúdo do CCG (recomputação em Python); tabela nr. 53, faixa de topo 53,50% (A via TAX_ENGINE)
- **Localização no raw:** `QA/CCG_CONTENT_REVIEW.md` linhas 143-147 (§Module 9, "Fixed"); `QA/TAX_ENGINE_FIX_APPLIED.md` linha 40 (§2, "What did not change": 1.284,17 nr. 53 faixa de topo)
- **Quem decidiu / pediu:** n/a
- **Destino:** skill `payroll-compliance-belgium` (referência 01-ccg) e hub §Ficha (o que mais dá errado), a critério do usuário
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C21 · erro+causa · [[Belgica]]
- **Chave:** `BE | CCG | exemplo: retenção do salário de abril (rescisão)` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** O exemplo de rescisão trazia a retenção do salário de abril sem o benefício do carro na base; o valor estava errado em qualquer método testado.
- **Antes (se erro):** EUR 1.003,36 (líquido 2.908,49).
- **Causa (se erro):** Não achada no cálculo: 1.003,36 não se reproduz por nenhum método (busca sistemática em 648.000 combinações; os 6 acertos exatos ficaram abaixo do ruído esperado); parâmetros de anos anteriores descartados por direção (movem o valor para cima, não para baixo). O ponto de julgamento foi se o benefício do carro de EUR 250/mês entra na base tributável do mês: entra, pela regra do próprio Módulo 6 (benefícios in natura entram na base do mês em que são gozados) e porque o carro esteve disponível até 30/04.
- **Correto / novo:** EUR 1.155,96 (líquido 2.755,89) na correção de revisão; depois do ajuste de parâmetros de 14/08 a figura do exemplo ficou em 1.156,36. Valor de exemplo, não parâmetro estatutário.
- **Nível de evidência:** B · **Fonte:** revisão de conteúdo do CCG; investigação dedicada `APRIL_SALARY_INVESTIGATION.md` (não relida por mim)
- **Localização no raw:** `QA/CCG_CONTENT_REVIEW.md` linhas 148-151 (§Module 9, "Fixed ... dedicated investigation"); `QA/TAX_ENGINE_FIX_APPLIED.md` linha 40 ("April-salary figure of 1,156.36")
- **Quem decidiu / pediu:** n/a
- **Destino:** nenhum hub (exemplo de CCG); só importa se alguém citar o valor 1.003,36
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (1.155,96 e 1.156,36 são dois passos; a ligação entre eles é minha leitura do TAX_ENGINE)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C22 · erro+causa · [[Belgica]]
- **Chave:** `BE | CCG | limiar de isenção de contribuição patronal para altos salários` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** alto (valor estatutário)
- **Serviço:** [[research-pipeline]]
- **O que diz:** O CCG afirmava um segundo limiar de 88.434 a partir de 1/7/2026; o limiar é 86.700 e não mudou.
- **Antes (se erro):** "EUR 88.434 a partir de 1 de julho de 2026" (6 ocorrências, Módulos 1, 3, 5 ×3 e 11).
- **Causa (se erro):** Inferência por padrão: o degrau de 2% de meio de ano visto em outros parâmetros (ex.: GMMI abril → agosto) foi aplicado a um limiar que não teve segundo reajuste em 2026.
- **Correto / novo:** Contribuição básica patronal e de moderação salarial não incide sobre a parte do salário trimestral acima de EUR 86.700, **a partir de 2026-01-01**, confirmado sem mudança ao menos até meados de 2026. A mudança de 1/7/2026 é de população: atletas pagos e ciclistas profissionais não podem combinar a medida com a redução específica do esporte (Lei-programa de 30/05/2026, arts. 109-110). 88.434 não deve ser usado.
- **Nível de evidência:** B que cita A · **Fonte:** instruções administrativas ONSS/RSZ de 16/01/2026 (86.700 desde 1/1/2026 por cruzamento do limiar do índice em dezembro/2025); VLAIO; Lei-programa de 30/05/2026 arts. 109-110
- **Localização no raw:** `QA/CCG_CONTENT_REVIEW.md` linhas 340-347 (§RESOLUTION - High-wage exemption threshold); `VC/BE-WTC-001-v1.1.md` linha 23 (remark "HIGH-WAGE EXEMPTION THRESHOLD - EUR 86,700, NOT EUR 88,434"); `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linha 73 (86.700 verificado em 2-5 artefatos sem contradição)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha, Valores-âncora (nova linha com vigência 2026-01-01 e fonte)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual o limiar de isenção patronal para altos salários na Bélgica em 2026?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C23 · erro+causa · [[Belgica]]
- **Chave:** `BE | CCG+WTC | multiplicador CO2` · **Já existe?** sim → complementa hub §Ficha, armadilha 6 e Valores-âncora ("Multiplicador CO2 4,00")
- **Tipo:** erro+causa
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** O valor 4,00 já está no hub; falta a causa dos dois erros em sequência e a fonte A certa.
- **Antes (se erro):** (1) CCG e WTC diziam 2,75 para 2026; (2) depois da correção para 4 a célula do WTC (F59) escrevia "4 for 2026 (CONFIRMED via Agoria, Cellule Mobilité, Van Mossel, Dynamik HR)".
- **Causa (se erro):** (1) 2,75 é o valor de 2025, carregado da extração rápida inicial para a lista de "valores verificados" do prompt do WTC sem verificação, e herdado pelo WTC ao ler o CCG. (2) Quatro fontes de nível B (federação, célula de mobilidade, uma concessionária e uma consultoria) concordando entre si não equivalem a fonte A, e a palavra CONFIRMED afirmava o contrário (bloqueador BE-X10-022).
- **Correto / novo:** multiplicador 2,25 (1/7/2023), 2,75 (1/1/2025), **4,00 (1/1/2026)**, 5,50 (1/1/2027), aplicado só à contribuição calculada, nunca ao mínimo não indexado (EUR 25,99 em 2026; 28,57 em 2027; 31,15 em 2028). Os valores 4 / 2,75 / 5,50 e os nomes dos fornecedores apareciam só no CCG (DD, spec DmfA e SIR citam o seletor "data do pedido", sem o valor).
- **Nível de evidência:** B que cita A · **Fonte:** art. 34, 1° da Lei de 25/11/2021 (BS 03/12/2021, numac 2021033910), que completa o art. 38 §3quater, 3° da Lei de 29/06/1981; repetido nas instruções ONSS 2026/2 (contribuições especiais, veículos de empresa)
- **Localização no raw:** `QA/CCG_CONTENT_REVIEW.md` linhas 394-398 (erro 2,75 → 4); `QA/BE-QA-REPORT.md` linhas 316-342 (BE-X10-022 e contenção); `VC/BE-WTC-001-v1.1.md` linha 27 (remark "CO2 SOLIDARITY CONTRIBUTION MULTIPLIER - NOW CITED TO THE LAW"); `LOGS/skill_build.log` (spot-check 4)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha armadilha 6 (acrescentar causa)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C24 · erro+causa · [[Belgica]]
- **Chave:** `BE | WTC | box 360 do fiscal work bonus` · **Já existe?** sim → resolve hub §Pendências (1ª e 3ª linhas: "falta box 360 no WTC"; "Divergência hub × skill")
- **Tipo:** erro+causa
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** A pendência do hub ("falta tax code box 360") está fechada no WTC do pipeline desde 17/08/2026 (bloqueador BE-X10-002).
- **Antes (se erro):** WTC coluna G do wage type BE-003 (fiscal work bonus) só com `284`: a parte de 52,54% nunca ia para o 281.10. A spec Belcotax apontava a lacuna em quatro células e pedia para levantá-la no próximo gate.
- **Causa (se erro):** A brochura lista o work bonus como um item com dois subitens; o WTC configurou só um deles.
- **Correto / novo:** BE-003 (linha 304 do catálogo) com Tax Code `284; 360`: 284 = crédito de 33,14% (tag `f10_2115_bonus`), 360 = crédito de 52,54% (tag `f10_2210_workbonus5254`). Um único wage type reportado em dois boxes (relief único, derivado do social work bonus, limite anual EUR 765, não indexado, desde o ano de renda 2025). O catálogo passou a ter 24 códigos de box distintos (23 do build inicial + 360). Quatro células da spec Belcotax atualizadas na mesma passada.
- **Nível de evidência:** B que cita A · **Fonte:** brochura Belcotax-on-web do SPF Finanças, ano de renda 2024 (06/12/2024) e 2025 (14/01/2026): subitens a) 33,14% box 284 / zona 2.115 e b) 52,54% box 360 / zona 2.210
- **Localização no raw:** `VC/BE-WTC-001-v1.1.md` linha 26 (remark "FISCAL WORK BONUS - DUAL BELCOTAX BOX CODE 284 AND 360") e linha 21 (24 códigos); `QA/BE-QA-REPORT.md` linhas 253-272 (BE-X10-002); `QA/BE-MASTER-PENDING-LIST-2026-08-24.md` linhas 50-56 (D-02)
- **Quem decidiu / pediu:** fix do Stage 10 de 17/08 (Updated By: Wallisson Gomes); a escolha "um wage type, dois boxes" é do QA/builder e consta no remark do VC
- **Destino:** hub §Pendências (marcar a 1ª linha como resolvida no WTC v1.1 do pipeline; confirmar se o WTC do Drive/brain já tem `284; 360`)
- **Pergunta para o teste (Conjunto B)?** sim → "Em quais boxes do 281.10 o fiscal work bonus é reportado?"
- **Confiança da extração:** alta (para o pipeline); o WTC do brain não foi aberto
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C25 · erro+causa · [[Belgica]]
- **Chave:** `BE | CCG | Módulo 9 Step 7, retenção do prêmio de fim de ano` · **Já existe?** sim → contradiz hub §Valores-chave ("697,42 (o CCG traz 697,61, errado)") e §Pendências (3ª linha)
- **Tipo:** erro+causa
- **Risco:** alto (correção de erro; divergência com o hub)
- **Serviço:** [[research-pipeline]]
- **O que diz:** O hub tem a direção invertida: o valor certo é 697,61; 697,42 era o erro e já foi corrigido no CCG do pipeline.
- **Antes (se erro):** CCG v1.0, Tabela 97: 697,42 (líquido 606,53; total retenção 18.588,53; total líquido 28.685,12). O hub registrou o contrário (chat: mercans-compliance, nível C).
- **Causa (se erro):** Erro aritmético de EUR 0,19 no passo 7 do exemplo (o documento era internamente coerente com o 697,42 errado).
- **Correto / novo:** 1.500,00 − 196,05 (13,07%) = 1.303,95; × 53,50% = 697,61325 → **697,61** (líquido 606,34; total retenção 18.588,72; total líquido 28.684,93). 697,42 não sai de nenhum insumo do exemplo (exigiria base 1.303,59 ou alíquota 53,4859%). O exemplo inteiro (passos 1-9, duas tabelas-resumo, totais) foi refeito e reconcilia; lint aritmético nas 148 tabelas sem erro. A skill do brain mostra 697,61 (hub §Pendências), coerente. Conflito B (recomputação) × C (chat): vale B; o hub deve ser corrigido.
- **Nível de evidência:** B · **Fonte:** recomputação do QA (1.303,95 × 53,50%)
- **Localização no raw:** `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linhas 209-221; `QA/BE-FIX-LOG-2026-08-21.md` linhas 1663-1688 (ITEM 5: "The brief reported 697.61 where 697.42 was correct. 697.61 is correct."); `LOGS/ccg_fix.log` linhas 25-29 (antes 697.42 → depois 697.61, com as 4 células dependentes); `QA/TAX_ENGINE_FIX_APPLIED.md` linhas 403-412 (§7(c), erro de 0,19 descoberto em 14/08)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Valores-chave (remover a linha 697,42) e §Pendências (fechar a 3ª linha); [[correcoes]] (entrada: chat registrou o sentido invertido)
- **Pergunta para o teste (Conjunto B)?** sim → "Quanto é a retenção de 53,50% sobre 1.303,95 no exemplo de prêmio do CCG da Bélgica?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C26 · erro+causa · [[Belgica]]
- **Chave:** `BE | CCG | citação "nr. 53/58" (Módulos 4 e 11)` · **Já existe?** sim → resolve hub §Pendências ("Investigar tabelas nr.53/58 e check digit do número RSZ", parte nr. 53/58)
- **Tipo:** erro+causa (falso positivo confirmado)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** A suspeita de que a citação "nr. 53/58" era inverificável é falsa; as citações estão certas e não foram removidas.
- **Antes (se erro):** Pedido da sessão 6 do FIX-LOG (25/08) para remover a citação "nr. 53/58" dos Módulos 4 e 11 por inverificável e trocá-la por provisões do ONSS (DmfA).
- **Causa (se erro):** A pesquisa que não confirmou os números procurou nas instruções, circulares e anexos do NSSO/ONSS, que é a autoridade errada: os nrs. 53, 58, 60 e 62 são pontos do Anexo III do RD de execução do CIR 92 (SPF Finanças, retenção na fonte), numerados de fato.
- **Correto / novo:** A string `53/58` aparece 0 vezes no CCG; os nrs. aparecem nos Módulos 1, 6 e 9 e citam o Anexo III. Verificado contra fonte independente: pontos 58-63 trazem a escala de atrasados e indenizações de rescisão; o ponto 62 fixa o percentual sobre a remuneração que serviu de base da indenização. Trocar por códigos DmfA anexaria uma autoridade de seguridade social a uma regra tributária (assuntos diferentes). A lacuna real é outra: ver C36.
- **Nível de evidência:** B que cita A · **Fonte:** Bijlage III do RD de 11/12/2025, nrs. 58-63
- **Localização no raw:** `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linhas 223-238; `QA/BE-FIX-LOG-2026-08-21.md` linhas 1773-1800 (ITEM 8)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Pendências (fechar a parte "tabelas nr.53/58"; o check digit continua, ver C38)
- **Pergunta para o teste (Conjunto B)?** sim → "As citações nr. 53/58 do CCG belga estão corretas?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C27 · erro+causa · [[Belgica]]
- **Chave:** `BE | Report Spec DmfA Modification | bloco 90169 rotulado ORIGINAL` · **Já existe?** sim → resolve parcialmente hub §Pendências ("90169 rotulado ORIGINAL")
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** O rótulo "DMFA ORIGINAL" no bloco 90169 da spec de modificação era um defeito real de 14/08, já corrigido; a raiz da declaração modificativa continua desconhecida e não foi chutada.
- **Antes (se erro):** Sheet 4 de BE-NSSO-003: `═══ BLOCK 90169 — DMFA ORIGINAL — DECLARATION TYPE CONTAINER — <DmfAOriginal> cardinality [1..1] ═══` (backup `.bak-before-regression-fix`, 14/08).
- **Causa (se erro):** A spec foi construída copiando a estrutura da BE-NSSO-002; o rótulo ORIGINAL ficou.
- **Correto / novo:** As 3 referências vivas a 90169 dizem agora que é a raiz da declaração ORIGINAL apenas e que a raiz da modificação é "NOT FOUND", sem adivinhar. Esse bloco é lacuna real de fonte (diferente do BE-X10-015) e **não** está em `known_limitations` ("registrada como devida"). Item aberto: BE-NSSO-003 sheet 4 linha 12, container nunca identificado.
- **Nível de evidência:** B · **Fonte:** log de fix + QA fechado
- **Localização no raw:** `QA/BE-FIX-LOG-2026-08-21.md` linhas 1690-1708 (ITEM 6); `LOGS/final_round2_research.log` (seção "Not closed, and stated rather than buried": container DmfA Mod); `QA/BE-MASTER-PENDING-LIST-2026-08-24.md` MP-RSPEC-19 (linha 428)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Pendências (marcar o rótulo como corrigido; deixar a raiz da modificação como lacuna aberta)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C28 · erro+causa · [[Belgica]]
- **Chave:** `BE | DD + Report Specs | domínio Days Justification (zona NSSO 00625)` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** alto (código estatutário NSSO)
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** O domínio do campo Days Justification (zona 00625) tem os códigos 1 a 7; as specs publicavam 5 códigos truncados e um "NOT FOUND".
- **Antes (se erro):** DmfA, DmfA-Mod e DRS com domínio francês truncado em 5 códigos; DD com 1-5 até a 1.3.
- **Causa (se erro):** Na promoção do DD v1.1 → v1.3 (21/08) o passe trocou o **texto** das citações para v1.3 sem checar se o **conteúdo** de cada citação tinha alargado; nove domínios do mapper tinham alargado.
- **Correto / novo:** códigos 1–7 (glossário DmfA 2026/2); as três specs declaram o domínio completo, atribuído ao mapper do DD, mantendo a citação original truncada e rotulada como cortada no valor 5. Específica do procedimento: após promover um artefato, re-medir o conteúdo que a citação representa, não só o texto da versão. 521 citações de coluna L em DD v1.3 sem nenhuma quebrada (QA final).
- **Nível de evidência:** B que cita A · **Fonte:** glossário NSSO DmfA edição 2026/2 (publicado em 01/06/2026), zona 00625
- **Localização no raw:** `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linhas 93-108 (Check 4); `QA/BE-FIX-LOG-2026-08-21.md` linhas 1162-1224 (FIX A); `VC/BE-DD-001-v1.4.md` linha 14 (VC 1.3: "Days Justification zone 00625 completed to codes 1-7 (was 1-5, truncated)")
- **Quem decidiu / pediu:** n/a
- **Destino:** skill `payroll-compliance-belgium` (referência 05-data-dictionary) e hub §Ficha (o que mais dá errado)
- **Pergunta para o teste (Conjunto B)?** sim → "Quais códigos tem o campo Days Justification da DmfA?"
- **Confiança da extração:** alta
- **Validação:** ◐ conferência independente: DD com 1-5 até a 1.2; a 1.3 (21/08) alargou para 1–7 e as três specs ficaram com 1-5 até 24/08 · humana ⏳

### F6-20261027-BE-C29 · erro+causa · [[Belgica]]
- **Chave:** `BE | DD | quatro conclusões revertidas (Bijlage 12, Bijlage 34, zona 00096, zona 00885)` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** alto (códigos estatutários)
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** Quatro afirmações do DD sobre fontes "não disponíveis" estavam erradas; os dados estavam nos glossários já baixados.
- **Antes (se erro):** (1) Work Schedule Days Indicator: "beco sem saída confirmado, exige navegar PDF com acesso restrito" (20/08); (2) Bijlage 12 possivelmente "aposentado" porque o índice de anexos da DmfA pula de 11 para 21; (3) zona 00096: "valores acima de 4 não confirmados"; (4) quatro linhas de Contract Duration Type citando "zona NSSO 00885".
- **Causa (se erro):** Os glossários mantidos em disco foram pesquisados para algumas zonas e não para outras. O salto 11 → 21 é real, mas a causa não é aposentadoria: a Bijlage 12 pertence à série de anexos DRS, que o glossário DmfA não carrega.
- **Correto / novo:** (1) Bijlage 34 está no glossário DRS/ONEM 2026/2: 28 códigos de dia, mesmo significado nas grades de 7/14/21/28. (2) Bijlage 12 "Identification du risque / Identificatie van het risico" existe, versão AN2025-1-FR12, 9 páginas, está nos 3 glossários DRS 2026/2: 78 linhas; zona 00430 `IdentificationOfRisk` com códigos 001–008; a identificação do formulário viaja na zona 00296. (3) zona 00096 vai de 1 a 10 (5/6 planos Vande Lanotte, 7 plano de redistribuição do setor público, 8–10 regimes de crédito-tempo da CCT 103). (4) a zona 00885 **não existe** em nenhum glossário; a zona do tipo de contrato é 00050 (`ContractType`, bloco 90015): 0 = tempo integral, 1 = tempo parcial. Também: limiar do Service Exemption Indicator é "pelo menos 20%" (`minstens 20 %`, instruções NSSO 2026/3).
- **Nível de evidência:** B que cita A · **Fonte:** glossários NSSO DRS/AMI, DRS/FAT e DRS/ONEM edição 2026/2 (publicados 01/06/2026, em produção 01/07/2026); instruções NSSO 2026/3
- **Localização no raw:** `QA/handover_status.md` linhas 79-127 (§3.1 a §3.3) e linha 68 (zona 00096); `VC/BE-DD-001-v1.4.md` linha 15 (VC 1.4)
- **Quem decidiu / pediu:** n/a
- **Destino:** skill `payroll-compliance-belgium` (referência 05-data-dictionary) e hub §Ficha
- **Pergunta para o teste (Conjunto B)?** sim → "Qual zona NSSO guarda o tipo de contrato (integral/parcial) e quais os valores?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C30 · erro+causa · [[Belgica]]
- **Chave:** `BE | Payslip | colisão contract_type × contract_duration_type (BE-X10-005)` · **Já existe?** sim → complementa hub §Ficha, armadilha 18 ("a colisão persiste no payslip (BE-X10-005)")
- **Tipo:** erro+causa
- **Risco:** alto
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** O hub diz que a colisão persiste no payslip. O QA final do pipeline conta o blocker como fechado.
- **Antes (se erro):** `Payslip Spec!E40` citava "BE-DD-001 Country Fields, 'Contract Type'" mas listava os valores de *Contract Duration Type* (indeterminado, prazo fixo...); o rótulo "Contract Type" aparecia sobre "Indefinite duration" na própria folha renderizada (EN!A24/C24). O DD tem os dois campos separados: Contract Type (0 integral / 1 parcial, zona 00050) e Contract Duration Type.
- **Causa (se erro):** O manifest já tinha consertado a sua instância em 17/08; o payslip era o terceiro portador e o único em que o par errado aparecia no documento entregue.
- **Correto / novo:** QA final (25/08): "all 6 blockers and 10 of the 11 majors carried by the 17 August handover are closed, each re-verified against the live artefacts". O fechamento específico do X10-005 não é detalhado linha a linha no FINAL2; a lista de pendências de 24/08 dizia "não retestado". Registrar como fechado pelo QA final, a confirmar no payslip.
- **Nível de evidência:** B · **Fonte:** QA final
- **Localização no raw:** `QA/BE-QA-REPORT.md` linhas 299-315 (BE-X10-005); `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linhas 269-272 (verdict); `QA/BE-MASTER-PENDING-LIST-2026-08-24.md` MP-PSL-03 (linha 520)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha armadilha 18 (atualizar o estado); skill se a armadilha estiver na referência 06-payslip
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (fechamento afirmado no agregado, não item a item)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C31 · alerta · [[Belgica]]
- **Chave:** `BE | QA | estado dos blockers e majors` · **Já existe?** sim → contradiz hub §Ficha ("Confiança da skill... 6 blockers e 11 majors abertos") e "O que mais dá errado"
- **Tipo:** alerta
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** O hub descreve o estado do QA de 17/08. O QA final (25/08) e o handover (16/09) mudam o quadro.
- **Antes (se erro):** Hub: "QA por artefato: SIR 93%, CCG 86%, WTC 85%, Report Specs 86%, DD 87%, Payslip 86%, scope_manifest 78%. 6 blockers e 11 majors abertos"; e em "O que mais dá errado": X10-001, X10-002, X10-003/004 e X10-022 como abertos.
- **Causa (se erro):** A Ficha foi extraída do `07-qa-report.md` da skill, que embute o `BE-QA-REPORT.md` de 17/08 (anterior a todas as correções).
- **Correto / novo:** QA final: 9 de 9 checks passam + 13/13 no teste de reprodutibilidade dos geradores; 6 blockers e 10 de 11 majors fechados (o hub lista como abertos X10-001 crosswalk de saída: fechado, manifest com 18+18 entradas e OUT-08 ausente por decisão de escopo; X10-002: ver C24; X10-003/004; X10-022: ver C23). Nível país no handover de 16/09: **NOT_READY** por BE-X10-010 (decisão do dono), BE-X10-006 (reescopar), T-05 (payslip sem verificador) e L-15 (nenhuma declaração jamais enviada por canal real); os 3 artefatos do Stage 9.5 (DD, WTC, CCG) estão READY_FOR_HANDOVER. As faixas de acurácia por artefato do QA de 17/08 não foram recalculadas depois; L-15 segura todas abaixo de 95%.
- **Nível de evidência:** B · **Fonte:** QA final e handover
- **Localização no raw:** `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linhas 19-43 (resumo), 267-277 (verdict); `QA/handover_status.md` linhas 19-34 (§1) e 255-274 (§7)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha ("O que mais dá errado" e "Confiança da skill")
- **Pergunta para o teste (Conjunto B)?** sim → "A Bélgica está pronta para handover?" (resposta: não, por 4 motivos de nível país)
- **Confiança da extração:** alta
- **Validação:** ◐ conferência independente: faixas de acurácia refeitas em 21/08 (BE-QA-REPORT-2026-08-21.md:350-360, 80–95%); FINAL2 diz que L-15 as mantém abaixo de 95% · humana ⏳

### F6-20261027-BE-C32 · erro+causa · [[Belgica]]
- **Chave:** `BE | WTC | contribuição patronal básica 24,92% (linha de exoneração de altos salários)` · **Já existe?** sim → complementa [[correcoes]] linha 2026-10-13 → 2026-10-21 (Belgica / BE-CCG Mod. 3 e 5; BE-WTC linha 23671)
- **Tipo:** erro+causa
- **Risco:** alto (valor estatutário, conflito A × B)
- **Serviço:** [[research-pipeline]]
- **O que diz:** O QA do pipeline validou a taxa patronal básica de 24,92% como "correta"; a fonte A (ONSS) diz 19,88% + moderação salarial.
- **Antes (se erro):** `WTC_REVIEW.md` lista como verificado "EUR 86,700 (employer exemption row, alongside the correct 24.92%/8.86%/3.80% breakdown)". O CCG v1.2 do pipeline não tem a correção feita no Drive em 13/10 (hub §Ficha).
- **Causa (se erro):** O WTC foi construído lendo o CCG como autoritativo e o QA conferiu o WTC contra o CCG; 24,92% era a taxa básica de 1º tri/2015, não a de 2026. Conferência B contra B não pega erro herdado.
- **Correto / novo:** conflito A × B → vale A (já em correcoes): 19,88% desde o 1º tri/2018 (categorias 1 e 3), mais moderação salarial de até 5,12%. Qualquer artefato do pipeline (CCG v1.2, WTC v1.1) que mostre 24,92% como taxa patronal 2026 está defasado. Não confundir com o 24,92 que aparece como limite de faixa de tabela de retenção.
- **Nível de evidência:** B (QA do pipeline) × A (instruções ONSS, via correcoes) · **Fonte:** ver [[correcoes]] (instruções administrativas ONSS, "Le pourcentage de cotisation globalisé" e "La cotisation de modération salariale")
- **Localização no raw:** `QA/WTC_REVIEW.md` linha 16; busca em `QA/` e `LOGS/` por `24.92`/`19.88`: nenhuma menção a 19,88% nos arquivos do pipeline
- **Quem decidiu / pediu:** n/a
- **Destino:** [[correcoes]] (acrescentar que o pipeline v1.2/v1.1 validou 24,92%) e hub §Artefatos entregues (marcar CCG v1.2 e WTC v1.1 do pipeline como defasados neste ponto)
- **Pergunta para o teste (Conjunto B)?** não (já coberto pelo Conjunto de correcoes)
- **Confiança da extração:** média (não abri o CCG v1.2 do pipeline; a ausência da correção nele vem do hub)
- **Validação:** ◐ conferência independente: 24,92 é percentual de uma faixa da tabela nr. 58 (26.885,01–34.790), não limite de faixa · humana ⏳

### F6-20261027-BE-C33 · pendência · [[Belgica]]
- **Chave:** `BE | CCG | regime de impatriados: alinhamento ONSS` · **Já existe?** sim → contradiz hub §Ficha, armadilha 13 ("NSSO mantém mínimo 75.000 e teto 90.000")
- **Tipo:** pendência (divergência de nível)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** O hub afirma como fato que o NSSO não adotou a reforma do regime de impatriados. O QA do pipeline tinha classificado isso como "genuinamente não resolvido, NÃO EDITAR até fonte primária".
- **Antes (se erro):** CCG m06_tax (linha do regime de impatriados): "NSSO/ONSS did not adopt the same reform — for social security purposes the prior EUR 75,000 minimum and EUR 90,000 annual cap ... still apply".
- **Causa (se erro):** A afirmação veio de fontes de nov-dez/2025 (três consultorias). Uma fonte posterior (Andersen, maio/2026, citando a mesma circular de 01/04/2026) afirma o oposto: reembolsos de custos "remain exempt from social contributions, even with the percentage increase and the cap removal". Podem ser compatíveis (o 90.000 pode referir-se a outra coisa), mas ninguém leu o texto da circular nem a orientação atual do ONSS.
- **Correto / novo:** Lado fiscal estável: até 35% do bruto, sem teto de 90.000, mínimo 70.000, circular 2026/C/51 de 01/04/2026 (a edição de 30% foi uma retratação do próprio revisor, desfeita; o módulo hoje diz 35%). Lado ONSS: **não resolvido**. Estado após o refresh de 16/09: o handover e o QA final não mencionam o ponto (0 ocorrências de `2026/C/51` e `75,000` em handover e FINAL2). A lista de pendências de 24/08 (MP-CCG-01) mantinha a afirmação no módulo e na linha do .docx.
- **Nível de evidência:** C (fontes secundárias discordantes; a circular 2026/C/51 é A mas não foi lida) · **Fonte:** Circulaire fiscale 2026/C/51 de 01/04/2026 (a ler); instruções administrativas ONSS vigentes
- **Localização no raw:** `QA/CCG_CONTENT_REVIEW.md` linhas 21-24 (retratação 35% × 30%) e 32-35 ("Downgraded to genuinely unresolved"); `QA/TAX_ENGINE_FIX_APPLIED.md` linhas 389-401 (§7(b)); `QA/BE-MASTER-PENDING-LIST-2026-08-24.md` linhas 86-94 (D-07) e 241-250 (MP-CCG-01)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha armadilha 13 (trocar "mantidos" por "não resolvido") e §Pendências (ler a circular 2026/C/51 e as instruções ONSS)
- **Pergunta para o teste (Conjunto B)?** sim → "O ONSS removeu o teto de 90.000 do regime de impatriados?" (resposta correta hoje: não está confirmado)
- **Confiança da extração:** alta (sobre o estado de "não resolvido"); o valor em si fica sem resposta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C34 · pendência · [[Belgica]]
- **Chave:** `BE | CCG+WTC | atrasados (arrears): nr. 58 ou nr. 53?` · **Já existe?** não (o hub só tem a pendência sobre a citação nr. 53/58, fechada no C26)
- **Tipo:** pendência
- **Risco:** alto (maior item de dinheiro não tratado do dossiê)
- **Serviço:** [[research-pipeline]]
- **O que diz:** O CCG tributa atrasados de anos anteriores pela tabela de pagamentos excepcionais (nr. 53). Possivelmente o certo é o nr. 58 (cabeçalho *Achterstallen*), como já foi feito para a indenização de aviso prévio. Não confirmado.
- **Antes (se erro):** m09 "retroactive increase relating to a previous year ... taxed at the exceptional-payment percentage"; m04 manda horas extras de ano anterior para as regras do Módulo 9.2; cerca de 14 wage types de atrasados do WTC repetem "percentual de remuneração excepcional × 13,92".
- **Causa (se erro):** O nr. 53 exclui por nome só as `opzeggingsvergoedingen`, não exclui atrasados; por isso o conserto da rescisão (C19) não se estendeu a atrasados.
- **Correto / novo:** Nada afirmável. A investigação classifica "atrasados também usam o nr. 58" como **provável, não confirmado** (rescisão: alta confiança). Falta ler o texto do Anexo III nrs. 53 e 58. Nenhum relatório posterior a 24/08 registra o fechamento.
- **Nível de evidência:** C · **Fonte:** a obter (Anexo III nrs. 53 e 58, RD de 11/12/2025)
- **Localização no raw:** `QA/TAX_ENGINE_FIX_APPLIED.md` linha 43 (⚠️ arrears NOT touched) e §5 (linha 337, item 1a); `QA/BRACKET_INVESTIGATION.md` §6/§7 (linhas 318-420); `QA/BE-MASTER-PENDING-LIST-2026-08-24.md` linhas 261-270 (MP-CCG-03)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Pendências
- **Pergunta para o teste (Conjunto B)?** sim → "Atrasados na Bélgica retêm pela tabela nr. 53 ou nr. 58?" (resposta hoje: não confirmado)
- **Confiança da extração:** média (o estado depois de 24/08 não está nos relatórios finais)
- **Validação:** ◐ conferência independente: acrescentado: FINAL2:230-231 e FIX-LOG:1790-1792 dizem ter conferido em fonte independente que os pontos 58–63 cobrem atrasados (evidência secundária; nível C mantido) · humana ⏳

### F6-20261027-BE-C35 · pendência · [[Belgica]]
- **Chave:** `BE | CCG | alívio por filho em remuneração excepcional (nr. 55) e Escala II / limiares do cônjuge (nrs. 33, 40.2, 40.3)` · **Já existe?** não
- **Tipo:** pendência
- **Risco:** alto (possível sobre-retenção sistemática em bônus)
- **Serviço:** [[research-pipeline]]
- **O que diz:** O Anexo III nr. 55 concede alívio por filho em percentual sobre pagamentos excepcionais (bônus, prêmio de fim de ano, double holiday pay), com teto de renda; o CCG não modela nenhuma redução por filhos nesses pagamentos. Os limiares da Escala II e do cônjuge (nrs. 33, 40.2, 40.3) não foram conferidos contra o CCG.
- **Antes (se erro):** m04/m08 sem referência a filhos em remuneração excepcional (a busca por `nr. 55` dava 0 ocorrências em 24/08; `nr. 40`: 0).
- **Causa (se erro):** A investigação de filhos só tratou o mecanismo de remuneração ordinária; viu o nr. 55 e deixou como achado adjacente.
- **Correto / novo:** Não aplicado. Se confirmado, o CCG retém a mais em bônus de empregados com filhos abaixo do teto. Valores lidos pela investigação no Anexo III (a conferir por nós, não entram no hub): limiares líquidos mensais EUR 174 / 290 / 579 e reduções 1.740 / 3.474 (nr. 11.2: bruto menos contribuições sociais, menos 20%). Não residente na escala III não tem alívio por filho (nr. 108/111), isso o CCG já diz corretamente.
- **Nível de evidência:** C (achado da investigação, sem passe de aplicação) · **Fonte:** Bijlage III do RD de 11/12/2025, nrs. 55, 33, 40.2, 40.3 (a ler)
- **Localização no raw:** `QA/CHILDREN_SUPPLEMENT_INVESTIGATION.md` linhas 130-143 (§2.5(a)), 308 (§6(c)) e 310 (§6(d)); `QA/BE-MASTER-PENDING-LIST-2026-08-24.md` linhas 290-299 (MP-CCG-06/07)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Pendências
- **Pergunta para o teste (Conjunto B)?** sim → "O CCG belga modela alívio por filho sobre bônus?" (resposta hoje: não, e pode estar errado)
- **Confiança da extração:** média
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C36 · pendência · [[Belgica]]
- **Chave:** `BE | CCG | rescisão: lado da seguridade social (DmfA)` · **Já existe?** não
- **Tipo:** pendência
- **Risco:** alto (códigos estatutários)
- **Serviço:** [[research-pipeline]]
- **O que diz:** O CCG documenta a tributação da rescisão em detalhe e a declaração de seguridade social só de forma genérica.
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a (lacuna de autoria, não erro)
- **Correto / novo:** Confirmados contra as instruções administrativas ONSS vigentes: código de remuneração DmfA **3** (indenizações de fim de contrato expressas em tempo de trabalho) e **9** (vantagens de fim de contrato não expressas em tempo). **Não confirmado**: código de contribuição do trabalhador **812** no bloco **90001** (fundo de fechamento): a página do ONSS sobre fim de contrato não o traz; não registrar sem fonte própria. Também não documentada a regra de alocação por trimestre e de modificação específica de rescisão. Roteado ao `compliance-source-hunter` como autoria nova, não como troca de citação.
- **Nível de evidência:** B que cita A (códigos 3 e 9) / sem fonte (812) · **Fonte:** instruções administrativas ONSS (DmfA), páginas de fim de contrato
- **Localização no raw:** `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linhas 240-248; `QA/BE-FIX-LOG-2026-08-21.md` linhas 1800-1816 (tabela de status); `QA/handover_status.md` linhas 270-272
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Pendências
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C37 · pendência · [[Belgica]]
- **Chave:** `BE | WTC+Report Specs | fontes do ano de renda 2026 ainda sem leitura (Finprof, Belcotax, art. 412 CIR)` · **Já existe?** não
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** Três pontos de formato e prazo repousam em documentos de anos anteriores ou em fonte inadequada, e o pipeline os registrou como "fora de alcance, não resolvível só por pesquisa em documentação".
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a
- **Correto / novo:** L-07: a série de códigos de período do Finprof para o ano de renda 2026 é desconhecida (a tabela publicada para em 2015 e a série roda em ciclo de 4 anos); os dígitos 8 a 10 da referência de pagamento da retenção dependem dela (erro silencioso: pagamento sem correspondência). L-08: o schema Belcotax do ano de renda 2026 não existe nas fontes (o registro se declara IY2026 e nomeia só artefatos IY2025); a coluna Tax Code do WTC vem da brochura IY2024 e **deve ser revalidada** contra a brochura IY2026 antes de alimentar um filing. L-09: os limiares do art. 412 CIR 92 vêm de um manual de zona de polícia, com equivalência de "indexação" que implica um coeficiente 2,0096 não declarado em lugar nenhum: não configurar com base nessa fonte. Contatos citados pelo QA: `info.finprof@minfin.fed.be`, `belcotax@minfin.fed.be`. Em 16/09 o handover mantém L-06 a L-09 como não trabalhados.
- **Nível de evidência:** B · **Fonte:** QA (lista de limitações) + remark do WTC
- **Localização no raw:** `QA/BE-QA-REPORT.md` linhas 444-446 (L-07, L-08, L-09); `VC/BE-WTC-001-v1.1.md` linha 21 (remark "TAX CODE COLUMN - SOURCE AND REVALIDATION REQUIRED"); `QA/handover_status.md` linha 270
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Pendências
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C38 · pendência · [[Belgica]]
- **Chave:** `BE | DD | check digit do número de empregador RSZ/NSSO de 9 posições` · **Já existe?** sim → complementa hub §Ficha, lacuna "Check digit do número RSZ/NSSO de 9 dígitos (não resolvido)" e §Pendências ("Investigar... check digit")
- **Tipo:** pendência (conflito interno no raw)
- **Risco:** alto
- **Serviço:** [[research-pipeline]]
- **O que diz:** O raw se contradiz: o QA e o handover tratam o algoritmo como não resolvido (L-06), mas o Version Control do DD diz que a fórmula foi aplicada em 21/08.
- **Antes (se erro):** QA de 17/08 §6.1: o texto do corpus ("prefixo da categoria + número de registro + dois dígitos de módulo 97") não especifica as posições cobertas na variante de 9 posições nem se o resultado é o resto ou o complemento a 97; a revisão de specs: o algoritmo "base × 100, mod 97, subtrair de 96" não reproduz o exemplo "02" (dá 49 para a base 1234567). O Finprof 274 mostra que o complemento e o resto são usados em números diferentes.
- **Causa (se erro):** Fórmula só em fonte secundária; falta a documentação de identificação de empregador do NSSO ou o XSD da DmfA (TechLib).
- **Correto / novo:** Conflito: `VC/BE-DD-001-v1.4.md` (linha 1.3, 2026-08-21) diz "Applied 2026-08-21 research: NSSO employer check-digit formula (ID Information)" e o log do fix diz que `ID Information!F20` foi reescrita "to carry the NSSO check-digit formula"; mas o handover §7 (cópia do snapshot de 25/08, "unchanged and unworked") mantém L-06 aberta e o scope manifest proíbe implementar mod-97 no número de empregador até a autoridade. Não sei de onde veio a fórmula do DD F20 nem se ela é A. Até resolver: não implementar nem citar a fórmula.
- **Nível de evidência:** C (conflito B × B no mesmo raw) · **Fonte:** a obter (documentação NSSO de identificação do empregador ou XSD DmfA)
- **Localização no raw:** `QA/BE-QA-REPORT.md` linhas 398-421 (§6.1) e linha 443 (L-06); `QA/REPORTS_SPEC_REVIEW.md` linhas 88-98; `VC/BE-DD-001-v1.4.md` linha 14; `QA/BE-FIX-LOG-2026-08-21.md` linhas 627-629; `QA/handover_status.md` linha 270
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha (lacuna) e §Pendências; pergunta de fonte
- **Pergunta para o teste (Conjunto B)?** sim → "Como se valida o dígito de controle do número de empregador do NSSO de 9 posições?" (resposta hoje: não confirmado)
- **Confiança da extração:** [INCERTO] (o raw tem duas afirmações incompatíveis e nenhuma fonte A)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C39 · pendência · [[Belgica]]
- **Chave:** `BE | WTC+CCG | teto anual do social work bonus após 2026-07-01` · **Já existe?** sim → resolve hub §Ficha, Lacunas ("Teto anual do social work bonus após 2026-07-01 ... skill internamente inconsistente: confirmar") e Valores-âncora (3.594,36 "conflito")
- **Tipo:** pendência (fechada pelo pipeline)
- **Risco:** alto (valor estatutário)
- **Serviço:** [[research-pipeline]]
- **O que diz:** O pipeline fechou a lacuna em 16/09; o relatório que dizia "NOT FOUND" (QA §6.2, design item 16) é anterior ao fechamento.
- **Antes (se erro):** CCG e WTC (4 células: Version Control C25, Wage Type Catalogue F303, Tax Credit B6 e o texto do VC) e Payslip (EN/NL N83) traziam o valor de 1/7/2026 como lacuna aberta, com a instrução de não extrapolar do passo de 2%.
- **Causa (se erro):** n/a (a instrução de não extrapolar foi obedecida, o valor foi publicado depois: instruções NSSO edição 2026/3).
- **Correto / novo:** teto anual do social work bonus: EUR 3.466,44 (a partir de 2026-01-01), EUR 3.523,92 (a partir de 2026-04-01) e **EUR 3.594,36 (a partir de 2026-07-01)**. Citação literal das instruções NSSO 2026/3, anexo werkbonus: "het totaal van de vermindering per werknemer niet meer bedragen dan 3.594,36 EUR per kalenderjaar". Reconcilia: máximos dos componentes em vigor desde 1/7 (171,99 + 127,54 = 299,53/mês empregado de escritório) × 12 = 3.594,36. Skill do refresh está certa; o QA §6.2 está defasado.
- **Nível de evidência:** B que cita A · **Fonte:** instruções administrativas NSSO edição 2026/3, anexo werkbonus (componente B 171,99; componente A 127,54)
- **Localização no raw:** `QA/handover_status.md` linhas 229-233 (§6 item 1: L-05 e L-10 fechados) e 64-66 (§2: itens "Work bonus cap" Y); `VC/BE-WTC-001-v1.1.md` linhas 12 (VC 1.1, ponto 1) e a remark "PARAMETERS THAT MOVE DURING 2026" (mesmo arquivo, linha do remark); `QA/BE-QA-REPORT.md` linhas 423-430 (§6.2, estado anterior)
- **Quem decidiu / pediu:** n/a
- **Destino:** hub §Ficha (Lacunas e Valores-âncora: tirar o "conflito", registrar a fonte)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual o teto anual do social work bonus a partir de 1/7/2026?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-BE-C40 · pendência · [[Belgica]]
- **Chave:** `BE | SIR | lacunas G1–G26 e conflito do OUT-10` · **Já existe?** sim → complementa hub §Pendências ("Registro único de limitações do país... não existe")
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** O SIR carrega um registro de lacunas G1 a G27 (G27 fechada); 21 só fecham por consulta a uma autoridade nomeada e 5 só por contrato de dados do cliente. Há ainda um conflito de decisão e uma ambiguidade de contagem.
- **Antes (se erro):** n/a
- **Causa (se erro):** n/a
- **Correto / novo:** G1–G21 (autoridade): codificação do XML da DmfA, vida do token OAuth, validade do certificado X.509, política de retentativas, idempotência do `POST /declarations`, SLA do Dimona/lote, retenção de respostas, lista de anomalias posterior à Anexo 30 2024/1, limite de arquivo e códigos de anomalia do Finprof, SLA de reconhecimento, vigência da descrição de arquivo Finprof de 26/09/2011, encoding e limite do Belcotax, limiar de recusa por erros dispensáveis, SLA do Checkinatwork, feeds do NSSO/Student@work/certificado de férias/RJV-ONVA/penhora. G22–G26 (contrato com o cliente, não país): dados de frota, emissores de vales, arquivo de prêmios de previdência complementar, canal bancário SEPA, T&A e contábil. OUT-10 `product_mapping_required`: SIR diz `false`, manifest diz `true` (conflito sinalizado desde 17/08, decisão do dono). BE-TF-010: SIR diz "onze fluxos governados" (§2 preâmbulo e G27) e "dez por spec viva + 1 descoped + 8 nenhum" (§2.3); ambos somam 19, reconciliáveis lendo "live".
- **Nível de evidência:** B · **Fonte:** registro `s08_gaps.md` do SIR via lista de pendências; QA final
- **Localização no raw:** `QA/BE-MASTER-PENDING-LIST-2026-08-24.md` linhas 444-480 (MP-SIR-01), 488-493 (MP-SIR-03); `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linha 259 (BE-TF-010)
- **Quem decidiu / pediu:** n/a (decisão pendente do dono)
- **Destino:** hub §Pendências
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (lista de 24/08; não recontei G1–G27 no SIR)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

## Descartados
| Item (ID no inventário) | Motivo |
|---|---|
| Inventário item 1: `QA/BE-QA-REPORT.md` §3 BE-X10-001 (7 fluxos de saída fora do manifest) | fechado no QA final (manifest 18+18, OUT-08 ausente por decisão); estado de fechamento em C31, sem cartão próprio |
| Inventário item 1: `QA/BE-QA-REPORT.md` §3 BE-X10-003 e BE-X10-004 (WTC dizendo que specs não existem; DD certificando registro que não tinha) | fechados (C31); sem informação nova |
| Inventário item 1: `QA/CCG_CONTENT_REVIEW.md` linhas 182-185 (INSZ de exemplo 345,67 → 345,62) | lote 2: erro de exemplo, sem impacto na resposta de produção |
| Inventário item 1: `QA/WTC_REVIEW.md` linhas 47-80 e `QA/BE-FIX-LOG-2026-08-21.md` linhas 1709-1772 (coluna A do WTC vazia como chave de junção; `'None'` literal em 8 células da linha BE-059) | lote 2: defeito de construção corrigido, causa de processo |
| Inventário item 1: `QA/CCG_CONTENT_REVIEW.md` linhas 268-271 (opções de ações: "dobrado" → +1 p.p. por ano após 5 anos; 0,5 no regime reduzido) | lote 2: a correção se apoia no Conseil Supérieur des Finances e em fontes secundárias, sem artigo de lei citado; não pode virar valor sem fonte A |
| Inventário item 1: `QA/BE-QA-REPORT.md` BE-X10-010 (coluna YTD Load do WTC vazia nas 359 linhas; decisão do dono) | lote 2: decisão do dono pendente, sem valor estatutário |
| Inventário item 1: `QA/BE-generator-drift-diagnosis-2026-09-16.md` (geradores não reproduzem DD v1.4, WTC v1.1, CCG v1.2; verificador "SKIP" cego; 2 extratores quebrados) | lote 2: risco de reconstrução reverter correções; só importa a quem reconstruir o pipeline |
| Inventário item 1: `QA/handover_status.md` §7 (BE-TF-008 changelog do DD, BE-TF-009 7 linhas `===` como fórmula, BE-TF-011 CCG sem VC, BE-TF-012 versões antigas dangling no SIR, Payslip, skill e ledger) | lote 2: defeitos pequenos (BE-TF-011 e BE-TF-012 já citados em C01, C04 e C14) |
| Inventário item 1: `QA/handover_status.md` linhas 185-191 (§4.4: `diff_wtc_baseline.py` RENAMED 299 / "BASELINE VIOLATED", idêntico antes do Stage 9.5) | lote 2: pergunta de nomenclatura Bélgica × baseline Global, decisão do dono |
| Inventário item 1: `VC/BE-WTC-001-v1.1.md` remark "PARAMETERS..." e linha 12 (taxas de referência do empréstimo ao empregado do ano de renda 2026 só existem após o decreto de fevereiro/2027; vale a base IY2025 provisória) | lote 2: dependência futura conhecida, sem efeito hoje |
| Inventário item 1: `VC/BE-WTC-001-v1.1.md` remark "ITEMS FLAGGED RATHER THAN GUESSED" (reforma da contribuição especial; mobility allowance BE-023; taxas de BE-039/BE-040 sem fonte) | lote 2: nenhum valor para registrar; já deixados sem valor no artefato |
| Inventário item 1: `QA/BE-QA-REPORT.md` linha 452 (L-15: nenhuma declaração enviada por canal real) | lote 2: já citado em C31 como razão de NOT_READY |
| Inventário item 1: `QA/BE-MASTER-PENDING-LIST-2026-08-24.md` MP-CCG-04 e MP-CCG-05 (tetos de horas extras 360/280 do RD de 24/07/2026; citação do decreto) | lote 2: o handover de 16/09 (linha 67) marca "Overtime-ceiling citation" como Y (item não descrito); estado incerto |
| Inventário item 1: `QA/BE-MASTER-PENDING-LIST-2026-08-24.md` MP-CCG-10 e MP-CCG-11 (taxa de 38,07% do mobility budget ausente do CCG; backlog "não verificado" do CCG) | lote 2: backlog de pesquisa, sem erro confirmado |
| Inventário item 1: `QA/handover_status.md` §7 e `QA/BE-QA-REPORT-FINAL2-2026-08-24.md` linha 261 (Work Reorganisation / Employment Promotion Measure sem spec; Health Insurance Fund Code sem binding) | lote 2: lacuna menor do DD |
| Inventário item 1: `QA/PAYSLIP_REVIEW.md` linhas 49-62 (BE-PSL-001: Payslip Spec 37 → 126+ linhas) | lote 2: histórico de construção do payslip |
| Inventário item 1: `QA/CCG_CONTENT_REVIEW.md` e `BE-MASTER-PENDING-LIST` MP-CCG-12 (fator 13,92 é convenção Mercans, tier B) | já registrado: hub §Ficha armadilha 9 |
| Inventário item 1: MP-CCG-02 (fiscal work bonus 63% × 52,54%; exemplos do m12 sem ressalva) | já registrado: hub §Pendências ("Reforço do fiscal work bonus ... não confirmado") |
| Inventário item 1: `LOGS/ccg_fix.log` Fix 3, Fix 4 e `QA/BE-FIX-LOG-2026-08-21.md` (work bonus em duas componentes; três tabelas da contribuição especial; GMMI × calendário do work bonus) | já registrado: hub §Ficha armadilhas 1, 7, 8 e 10; sem informação nova |
| Inventário item 1: `LOGS/final_round2_research.log` BE-X10-008 (cadeia legal do work bonus; art. 353bis errado) | já registrado: hub §Ficha armadilha 14 |
| Inventário item 1: `QA/BE-QA-REPORT.md` BE-X10-007/-009/-011/-015/-016 (datas do GMMI no Módulo 4; 220 células "NOT FOUND" nas specs; chave de junção; 13 campos sem nome; 148 queries em bloco) | fechados no QA final; defeitos de estrutura sem impacto na resposta |
| Inventário item 1: `NOTAS/BE-COVERAGE.md` (carta de escopo: federal, idiomas, regional/municipal não construídos) | já registrado: hub §Ficha (escopo) e armadilha 16 |
| Inventário item 1: L-14 Limosa e L-16 payslip FR/DE | já registrado: hub §Ficha (Limosa descartado; francês e alemão não construídos); a spec Limosa está em C09 |
| Inventário item 1: `NOTAS/BE_stage9-5_verification.md`, `BE_stage9-6...`, `BE_stage9-7...`, `BE_stage9-8...`, `BE_stage9-9...`, `BE_stage11...`, `BE_stage12...`, `BE_stage12b_f38_fix.md`, `BE_gap_closure_patch_spec.md`, `BE_payslip_reformat_colombia.md` | são prompts/instruções de execução, não resultados; o resultado está no handover (usado em C01-C03, C29, C39) |
| Inventário item 1: `NOTAS/PROPAGATION-LEDGER.md` (116 KB, 15–18/08) | histórico de propagação superado pelo FINAL2; só aparece como localização quando útil |
| Inventário item 1: `LOGS/*` (66 logs de scripts, fixes e regressões) | ruído de ferramenta/script: saídas de build e de scripts já resumidas nos relatórios de QA; usados apenas `ccg_fix.log` (C25) e `skill_build.log` (C15, C16, C23) |
| Inventário item 1: ferramentas do pipeline (`_verify_payslip.py` com `NameError: IFERROR`, `verify_specs.py` C6/C20 desatualizados, `selfcheck_be_wtc.py` ORANGE, extratores `extract_dd.py`/`extract_wtc_corrections.py` quebrados, `_audit_v24_mechanical.py` com caminho antigo) | ruído de ferramenta, sem impacto na resposta de um artefato |
| Inventário item 1: `LOGS/FACT-CONFLICTS.md` / `.csv` | sem conflitos ("PASS — no deterministic conflicts"); nada a extrair |
| Inventário item 1: `QA/ALIGNMENT_PATCH_REVIEW.md`, `BE-ALIGNMENT-PATCH.md`, `scope_validation.md`, `APRIL_SALARY_INVESTIGATION.md`, `BE-QA-REPORT-2026-08-21.md`, `BE-QA-REPORT-FINAL-2026-08-24.md` | não relidos linha a linha neste lote: superados pelo QA final (24/08 e 25/08) ou usados só indiretamente; reabrir se a validação pedir |
