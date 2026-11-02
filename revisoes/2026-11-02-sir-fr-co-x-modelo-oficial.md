# SIR (etapa 6) de França e Colômbia × modelo oficial si-discovery / si-runbook-research

Revisão só de leitura, 2026-11-02. Ligada a [[Franca]], [[Colombia]] e [[research-pipeline]].

## Resumo (5 linhas)
1. França e Colômbia têm o **mesmo desvio estrutural**: as pastas por autoridade (FR: NETENT-DSN, URSSAF-DPAE, DGFIP-EDI; CO: DIAN-NE) usam um P1–P7 **inventado** (perfil, credenciais, transporte, payload, retorno, teste, operação), não as fases da política (Compliance, Legal, Business onboarding, Business scope, Technical analysis, INT, QA/UAT). Nenhuma autoridade tem os runbooks `.docx` OUT/IN.
2. Itens do contrato por autoridade integrável (36 cada, 4 autoridades = 144): **OK 9 · FALTA 31 · DIVERGE 104**. O conteúdo técnico existe e é extenso, mas está no lugar e no formato errados para o checker e para os donos de cada fase.
3. `integration-landscape.json` (FR 5 autoridades, CO 4): faltam `receives_payroll_data`, `artefacts_public` e `source` em **todas** as 9 autoridades, além do `notes` no topo; `summary` virou objeto e `directions` virou lista. Totais: OK 48 · FALTA 29 · DIVERGE 16.
4. `si_scope_check.py` oficial em modo structural (do jeito que o pipeline chama): **FR 3/3 BLOCKED** (S1 FAIL, outras autoridades citadas fora do INTERLINKAGES); **CO 1/1 "OK"**, mas só porque o S1 não rodou (DIAN-NE é a única integrável). Com todas as autoridades do landscape no `--other`, **CO também dá BLOCKED**. S3 aponta **11 entregas faltando** em todas as 4 pastas.
5. O SIR que está no Drive (FR e CO `SIR-INDEX-001-v1.0.docx` de 29/09, e os Google Docs `FR-SIR-001 v1.0` / `CO-SIR-001 v1.1→v1.3`) é um **registro consolidado** (seções 0–6), exatamente o formato que o modelo manda não produzir; o índice curto original (27/08 FR, 18/09 CO) foi substituído por ele.

## O que foi comparado
| País | Peça | Versão comparada | Por quê |
|---|---|---|---|
| FR | runbooks por autoridade, landscape, logs | `~/mercans-pipeline/FR-compliance/03-statutory-integrations/` (27/08–03/09) | única cópia dos runbooks |
| FR | índice | `FR-SIR-INDEX-001-v1.0.docx` do pipeline, 29/09, md5 `889c19e1…` = cópia do Drive (`France/19 - Statutory Integration/`) | é a que está no Drive; a cópia do cérebro `Research Pipeline/França/SIR/` (27/08, md5 `42fc7657…`, 323 palavras) é o índice curto anterior |
| CO | runbook DIAN-NE | `brain-service/Research Pipeline/Colombia/CO-compliance/03-statutory-integrations/DIAN-NE/` (arquivos de 21/10, com `_previous/` de 18/09) | mais nova que a do pipeline (18/09); `_phase-index.md` e `P2` são idênticos (md5) nas duas |
| CO | landscape | `~/mercans-pipeline/CO-compliance/.../integration-landscape.json` (13/10) | mais novo que o do cérebro (18/09): tem a exclusão `CO-OUT-RETCONT` acrescentada em 13/10; estrutura de campos igual |
| CO | índice | `CO-SIR-INDEX-001-v1.0.docx` do pipeline, 29/09, md5 `f6923730…` = cópia do Drive | a do cérebro (18/09, 1.110 palavras, sem títulos) é a anterior |
| CO | SIR vigente (Google Doc) | `Research Pipeline/Colombia/2026-10-29-validacao-research/final/CO-SIR-001-v1.3-texto-final.md` (02/11; texto para colar sobre o Doc v1.1/v1.2) | é a versão mais nova do SIR da Colômbia; formato de registro (Document control, seções 1–6, Apêndice A). Só classificado quanto ao formato; conteúdo estatutário não avaliado |

Modelo oficial: `mercans-pipeline-v2.12.1-gitbash.zip` (`_distribuicao/2026-10-29-v2.12-guia/`), extraído em pasta temporária. Logs confirmam a improvisação: `FR-compliance/logs/si_discover.log`, `si_netent-dsn.log` ("I defined the P1–P7 decomposition myself") e `CO-compliance/logs/si_dian-ne.log` ("`shared/si-runbook/` is not installed… I reconstructed the phase model"). O `_phase-index.md` da DIAN-NE já avisava: "file names will need renaming and `si_scope_check.py` should be re-run".

## 1. Contrato oficial
### 1.1 `integration-landscape.json` (si-discovery)
- Topo: `country`, `code`, `verdict` (`HAS_INTEGRATIONS | MANUAL_ONLY | NO_INTEGRATIONS`), `summary` (texto de 2–3 frases), `authorities[]`, `notes`.
- Por autoridade: `code`, `name`, `receives_payroll_data` (bool), `integration` (bool), `channel`, `directions` (`out | in | both | none`), `dev_portal` (URL ou vazio), `artefacts_public` (`yes | partial | gated | unknown | n/a`), `source`.
- Regras: listar toda autoridade que recebe dados de folha; cada classificação com `source`; verdict = HAS_INTEGRATIONS se alguma `integration=true`; portal/papel nunca é integração; não escrever runbook.
### 1.2 Entregas por autoridade (si-runbook-research), em `03-statutory-integrations/{AUTH}/`
| Fase (dono) | Arquivo |
|---|---|
| P1 Compliance (Compliance Team) | `P1-compliance/{CODE}-{AUTH}-INT-OUT-001.docx` e `-INT-IN-001.docx` (um por direção); `statutory-report-templates.md`; `statutory-notifications-mapping.md`; `statutory-compliance-report.md` (com nota de walkthrough obrigatório) |
| P2 Legal onboarding (Director of Administration) | `P2-legal-onboarding/legal-entity-statement.md` (uma declaração sim/não + norma) |
| P3 Business onboarding (Operations + Technical PM) | `P3-business-onboarding/business-onboarding-requirements.md`; `credential-certificate-inventory.md` (onde, como, status) |
| P4 Business scope (Operations) | `P4-business-scope/reporting-scenarios.md` (com correções, frequência, canais, nota sobre Implementation) |
| P5 Technical analysis (Technical Analyst) | `P5-technical-analysis/authority-technical-documentation-register.md` (coletar e referenciar, não interpretar) |
| P6 Integration development (INT Team) | `P6-integration-development/int-actionable-inputs-checklist.md` |
| P7 QA/UAT | `P7-qa-uat/uat-scenarios-and-validation-environment.md` |
| Transversais | `INTERLINKAGES.md` (único lugar onde outra autoridade pode aparecer; uma linha por dependência), `effort-estimates.md` (por fase, ao PM), `_phase-index.md` (fase → time dono → arquivos → critério de entrada → status) |

Esqueleto de cada runbook `.docx` (10 seções): 1 Visão geral e fronteiras (Configuration Factory / Report Configuration Team / Platform / autoridade); 2 Pré-requisitos (2.1 **Step 0** lista de artefatos com URL, obrigatória; 2.2 credenciais; 2.3 autenticação verificada no artefato; 2.4 identificadores; 2.5 inputs do Report Configuration Team); 3 Pré-produção (3.1 registro de certificado como pré-requisito numerado + aviso de 403; 3.2 variáveis de ambiente n8n; 3.3 ConfigCheck; 3.4 credential store); 4 Onboarding e autorização por entidade; 5 Workflows por relatório (Report Spec, workflow n8n, endpoint, método, corpo, resposta); 6 Status; 7 Reconciliação; 8 Erros, retry, log e contrato de dados do dashboard; 9 Testes E2E e cutover; 10 Quick reference.

### 1.3 Modos, banners e regras
- Modo `structural`: capa "STRUCTURAL — NOT BUILD-READY", placeholders `[[NEEDS-ARTEFACT: <artefato + onde>]]`. Modo `build-ready`: capa "BUILD-READY", **nenhum** placeholder. Step 0-auto: baixar artefatos públicos para `integration-sources/<auth>/` e promover a build-ready o que vier deles.
- Uma autoridade por pasta; outras só no `INTERLINKAGES.md`. Entrada e saída em trilhas e documentos separados. `Source:` (ou `[[SRC: …]]`) em cada subseção. Não produzir registro consolidado de todas as integrações.
- Checker `si_scope_check.py`: S1 escopo (FAIL), S2 placeholders (FAIL só em build-ready), S3 13 arquivos + runbook (MANUAL), S4 `Source:` nos runbooks (MANUAL). O pipeline v2.12 chama em modo structural com `--other` = demais autoridades **integráveis** (`_integrable.txt`).

## 2. `si_scope_check.py` oficial (rodado com `python -I`, só lê, nada gravado)
| Autoridade | Execução principal (como o pipeline) | S1 | S2 | S3 | S4 | Complementar A (`--other` = todas do landscape) | Complementar B (`--mode build-ready`, sem `--other`) |
|---|---|---|---|---|---|---|---|
| FR NETENT-DSN | **BLOCKED** (exit 2) | FAIL: P1, P4, P7, `_phase-index` | MANUAL, 0 detectados | MANUAL, 11 faltando | SKIP (sem runbook) | BLOCKED (mesmos 6 achados) | OK (S2 PASS **falso**: 13 marcadores `[[NEEDS-ARTEFACT]]` sem dois-pontos não são vistos) |
| FR URSSAF-DPAE | **BLOCKED** | FAIL: P1, P3, P5, `_phase-index`, `effort-estimates` | MANUAL, 0 | MANUAL, 11 | SKIP | BLOCKED (7) | OK (S2 PASS falso: 9 marcadores) |
| FR DGFIP-EDI | **BLOCKED** | FAIL: P1, `_phase-index`, `effort-estimates` | MANUAL, 0 | MANUAL, 11 | SKIP | BLOCKED (6) | OK (S2 PASS falso: 2 marcadores) |
| CO DIAN-NE (cérebro, 21/10) | OK (exit 0) | SKIP (única integrável) | MANUAL, 0 | MANUAL, 11 | SKIP | **BLOCKED**: `_phase-index` (DIAN-MUISCA, PILA-OI, FONDOS-CESANTIAS), `effort-estimates` (FONDOS-CESANTIAS) e os arquivos de `_previous/` | OK (S2 PASS real: 0 marcadores) |
| CO DIAN-NE (pipeline, 18/09) | OK (exit 0) | SKIP | MANUAL, 0 | MANUAL, 11 | SKIP | BLOCKED (`_phase-index`, `effort-estimates`) | — |

Observações: (a) o checker varre subpastas, então `_previous/` na cópia do cérebro entra no S1; (b) S4 não avalia nada porque não há runbook `.docx`; (c) o "OK" da CO na execução principal não prova escopo, só que o S1 não rodou.

## 3. Comparação por autoridade (runbooks)
Legenda: OK = conforme; DIVERGE = existe com formato, lugar ou conteúdo diferente do contrato; FALTA = exigido e ausente. Arquivos citados ficam na pasta da autoridade.

| # | Item do contrato | FR NETENT-DSN | FR URSSAF-DPAE | FR DGFIP-EDI | CO DIAN-NE |
|---|---|---|---|---|---|
| 1 | Pasta `03-statutory-integrations/{AUTH}/` | OK | OK | OK | OK |
| 2 | `integration-sources/<auth>/` com artefatos + manifesto | OK (`_source-manifest.md`, guia API v6.8, NEODeS/NEOReS) | OK (`_source-manifest.md`) | OK (`_MANIFEST.txt`, volumes EDI) | OK (`SHA256SUMS.txt`) |
| 3 | Runbook `P1-compliance/{CODE}-{AUTH}-INT-OUT-001.docx` | FALTA | FALTA | FALTA | FALTA |
| 4 | Runbook `…-INT-IN-001.docx` | FALTA | FALTA | FALTA | FALTA |
| 5 | `statutory-report-templates.md` | FALTA | FALTA | FALTA | FALTA |
| 6 | `statutory-notifications-mapping.md` | DIVERGE (P5 §5.5 "Returns that must reach payroll") | DIVERGE (P5 §5.5) | DIVERGE (P5 §5.4–5.5) | DIVERGE (P4 §3–6) |
| 7 | `statutory-compliance-report.md` + walkthrough obrigatório | FALTA | FALTA | FALTA | FALTA |
| 8 | `legal-entity-statement.md` (sim/não + norma) | FALTA | FALTA | FALTA (só a pergunta aberta Q2 sobre K-BIS/entidade francesa em P2 §2.9 e effort §6) | FALTA |
| 9 | `business-onboarding-requirements.md` | DIVERGE (P2 §2.1–2.2) | DIVERGE (P2 §2.1–2.2) | DIVERGE (P2 §2.2–2.7) | DIVERGE (P1 §6, P6 §1–2) |
| 10 | `credential-certificate-inventory.md` (onde/como/status) | DIVERGE (P2 §2.8 checklist) | DIVERGE (P2 §2.8) | DIVERGE (P2 §2.4–2.6) | DIVERGE (P2 §6 secrets inventory) |
| 11 | `reporting-scenarios.md` (com correções, nota Implementation) | DIVERGE (P1 §1.2 + P4 §4.9) | DIVERGE (P1 §1.2 + P4 §4.8 "no correction model") | DIVERGE (P1 §1.2 + P4 §4.9) | DIVERGE (P1 §3 + P3 §8 + P5 §6) |
| 12 | `authority-technical-documentation-register.md` (coletar, não interpretar) | DIVERGE (`_phase-index` "Source basis" + P3; interpreta) | DIVERGE (idem) | DIVERGE (idem + P3 §3.10 "Not published") | DIVERGE (P1 §7 artefact manifest + P2) |
| 13 | `int-actionable-inputs-checklist.md` | DIVERGE (P4 §4.11, P5 §5.9) | DIVERGE (P4 §4.11, P5 §5.8) | DIVERGE (P4 §4.10) | DIVERGE (P2 §7) |
| 14 | `uat-scenarios-and-validation-environment.md` | DIVERGE (P6) | DIVERGE (P6) | DIVERGE (P6) | DIVERGE (P6) |
| 15 | `INTERLINKAGES.md` (uma linha por dependência) | DIVERGE (139 linhas, "Shared risks") | DIVERGE (204 linhas, com `[[NEEDS-ARTEFACT]]`) | DIVERGE (132 linhas, sequenciamento) | DIVERGE (133 linhas, "Where the risk sits") |
| 16 | `effort-estimates.md` por fase da política | DIVERGE (fases próprias) | DIVERGE | DIVERGE | DIVERGE |
| 17 | `_phase-index.md` (dono, critério de entrada, status) | DIVERGE (sem dono/critério) | DIVERGE | DIVERGE | DIVERGE (com nota de proveniência) |
| 18 | §1 Fronteiras Factory / Report Config / Platform / autoridade | FALTA | FALTA | FALTA | FALTA |
| 19 | §2.1 Step 0 (artefatos com URL) | DIVERGE (lista no `_phase-index`/manifesto) | DIVERGE | DIVERGE | DIVERGE (`_phase-index` "Source artefacts", P1 §7) |
| 20 | §2.2–2.4 credenciais, autenticação, identificadores | DIVERGE (P2) | DIVERGE (P2) | DIVERGE (P2) | DIVERGE (P2 §3–4) |
| 21 | §2.5 Inputs do Report Configuration Team | DIVERGE (P4 payload) | DIVERGE (P4) | DIVERGE (P4) | DIVERGE (P3) |
| 22 | §3.1 Registro de certificado pré-produção numerado + aviso 403 | DIVERGE (P6 §6.2; 403 só como semântica HTTP) | DIVERGE (P6 §6.2) | DIVERGE (P2 §2.4, P6 §6.1) | DIVERGE (P6 §2) |
| 23 | §3.2/§3.4 Variáveis n8n e credential store | FALTA (n8n não aparece) | FALTA | FALTA | FALTA |
| 24 | §3.3 Pre-flight ConfigCheck | DIVERGE (P6 §6.3) | DIVERGE (P6 §6.3) | DIVERGE (P4 §4.10, P6 §6.2) | DIVERGE (P6 §2) |
| 25 | §4 Onboarding/autorização por entidade | DIVERGE (P2) | DIVERGE (P2) | DIVERGE (P2 §2.2) | DIVERGE (P6) |
| 26 | §5 Workflow por relatório → Report Spec + workflow n8n | DIVERGE (endpoints em P3; sem workflow n8n) | DIVERGE | DIVERGE | DIVERGE |
| 27 | §6 Status / respostas | DIVERGE (P5 §5.6) | DIVERGE (P5 §5.3–5.5) | DIVERGE (P5 §5.4) | DIVERGE (P4 §2–3) |
| 28 | §7 Reconciliação | DIVERGE | DIVERGE | DIVERGE (P5 §5.5) | DIVERGE (P4 §5) |
| 29 | §8 Erro, retry, log, contrato de dados do dashboard | DIVERGE (P7 §7.3–7.4) | DIVERGE (P7) | DIVERGE (P7; sem dashboard) | DIVERGE (P5 §4, P7 §4; sem dashboard) |
| 30 | §9 Testes E2E, conformidade, cutover | DIVERGE (P6) | DIVERGE (P6) | DIVERGE (P6) | DIVERGE (P6) |
| 31 | §10 Quick reference | FALTA | FALTA | FALTA | DIVERGE (P7 §7) |
| 32 | Banner/modo coerente | DIVERGE ("Mode structural" + "Overall status BUILD-READY" com placeholders) | DIVERGE (idem) | DIVERGE (idem) | DIVERGE ("Mode: structural" + "BUILD-READY") |
| 33 | Escopo de uma autoridade (S1) | DIVERGE (S1 FAIL) | DIVERGE (S1 FAIL) | DIVERGE (S1 FAIL) | DIVERGE (S1 FAIL na variante completa) |
| 34 | Placeholder `[[NEEDS-ARTEFACT: …]]` | DIVERGE (13× sem dois-pontos; checker não vê) | DIVERGE (9×) | DIVERGE (2×) | OK (nenhum; declara 0 lacunas) |
| 35 | `Source:` por subseção | DIVERGE (colunas "Source" em tabelas e 1 linha em 5 arquivos) | DIVERGE (sem linhas `Source:`) | DIVERGE (só "Source basis:" no topo e colunas) | DIVERGE (colunas e citações inline do Anexo) |
| 36 | Entrada e saída em documentos separados | DIVERGE (P4 × P5 separados; P1–P3, P6–P7 misturam) | DIVERGE | DIVERGE | DIVERGE (P3 × P4 separados; resto misturado) |
| | **Totais** | **OK 2 · FALTA 8 · DIVERGE 26** | **OK 2 · FALTA 8 · DIVERGE 26** | **OK 2 · FALTA 8 · DIVERGE 26** | **OK 3 · FALTA 7 · DIVERGE 26** |

Mapa do P1–P7 improvisado para as fases oficiais: FR P1 perfil → P4/P5 oficiais; P2 credenciais → P3 oficial; P3 transporte e P4/P5 payload/retorno → P5 oficial + runbook §5–7; P6 teste → P7 oficial; P7 operação → runbook §8. CO: P1 perfil, P2 conectividade, P3 payload, P4 resposta, P5 validação, P6 habilitação, P7 operação, mesma lógica.

## 4. Landscape e índice
| Item | FR | CO |
|---|---|---|
| `country`, `code`, `verdict`, `authorities[]` | OK (verdict HAS_INTEGRATIONS; 3 integráveis de 5) | OK (HAS_INTEGRATIONS; 1 de 4) |
| `summary` (2–3 frases) | DIVERGE (objeto com contagens; texto vai para `verdict_rationale`) | DIVERGE (idem) |
| `notes` | FALTA (há `open_questions`, `limitations`, `modelling_note`) | FALTA (há `open_questions`, `research_method`) |
| `code`, `name`, `integration`, `channel` por autoridade | OK (5×4) | OK (4×4) |
| `receives_payroll_data` | FALTA (5/5) | FALTA (4/4) |
| `directions` (`out/in/both/none`) | DIVERGE (lista `["outbound","inbound"]`, 5/5) | DIVERGE (lista, 4/4) |
| `dev_portal` (URL ou vazio) | OK 3; DIVERGE leve 2 (`null` em CNAM-DIRECT, CDC-SOLTEA) | OK 1 (DIAN-NE); DIVERGE 3 (`null` em DIAN-MUISCA e FONDOS-CESANTIAS; texto junto da URL em PILA-OI) |
| `artefacts_public` | FALTA (5/5; a informação está em `specifications[].public`) | FALTA (4/4; está em `public_artefacts[]`/`artefact_readiness`) |
| `source` | FALTA (5/5; há `evidence` em texto e `sources` no topo) | FALTA (4/4; há `evidence[]`) |
| **Totais landscape** | **OK 27 · FALTA 16 · DIVERGE 8** | **OK 21 · FALTA 13 · DIVERGE 8** |
| Índice `SIR-INDEX-001` (curto, uma linha por autoridade + local do runbook) | DIVERGE: a versão do Drive (29/09) é registro completo (seções 0–6, 13 tabelas, ~3.070 palavras); a curta (27/08) ficou só no cérebro | DIVERGE: idem (29/09, 12 tabelas, ~2.650 palavras) |
| SIR em Google Doc | `FR-SIR-001-v1.0.gdoc` no Drive: formato de registro (não aberto; `.gdoc` não legível pelo disco) | `CO-SIR-001` v1.1 no Drive, v1.3 em preparo: registro consolidado (seções 1–6 + Apêndice A) → DIVERGE do modelo |

Os campos extras (FR `operations`, `authentication`, `formats`, `test_environment`; CO `endpoints`, `artefact_gaps`, `onboarding_gating` etc.) não violam o contrato e carregam boa parte do que faltaria. Os dois arquivos dizem, em `schema_note`, que o esquema foi reconstruído porque o agente não estava instalado.

## 5. Impacto prático (time de configuração de integrações e donos de fase)
- **Sem runbook `.docx` OUT/IN no esqueleto de 10 seções**, o time de configuração não tem o guia passo a passo que espera: não há fronteira de responsabilidade (§1), variáveis n8n e credential store (§3.2/3.4) nem nome de workflow n8n por relatório (§5). Ele terá de montar isso a partir de 7 arquivos técnicos por autoridade.
- **Donos de fase sem entrega própria:** Director of Administration (sem declaração de entidade legal), Operations (sem cenários de reporte nem templates), Technical Analyst (recebe material já interpretado, não um registro de documentos), INT (checklists espalhados), QA/UAT (cenários dentro do P6 técnico). A política exige entrega separada por time.
- **Status enganoso:** os índices dizem "Mode structural" e "BUILD-READY" ao mesmo tempo, e a FR ainda tem 24 marcadores `[[NEEDS-ARTEFACT]]` (login/charte/schema pack). No formato atual, o checker não os vê e daria build-ready falso.
- **Escopo:** as pastas FR citam as outras autoridades fora do INTERLINKAGES (o mesmo motivo da recusa do Illia na Espanha); a CO falha quando as autoridades manuais entram no fence.
- **Drive:** o que o cliente interno vê é o registro consolidado, formato que o modelo substituiu. Quem for configurar a partir do Drive não encontra os runbooks por autoridade, que estão só no pipeline/cérebro.
- Ponto a favor: o conteúdo técnico (endpoints, autenticação, payload, retornos, testes, fontes baixadas com hash) é extenso e serve de matéria-prima para quase todos os itens DIVERGE. Isso é uma observação de estrutura; **o conteúdo estatutário e técnico não foi verificado em fonte nesta revisão.**

## 6. O que seria preciso para alinhar (não executado)
1. Instalar o módulo oficial em `~/mercans-pipeline` (`.claude/agents/si-discovery.md`, `si-runbook-research.md`, `shared/si-runbook/*`) e acrescentar FR e CO em `si-authorities.yaml`. O pipeline não tem remote: só com ok do usuário.
2. Landscape (FR e CO): acrescentar `receives_payroll_data`, `artefacts_public`, `source` por autoridade e `notes` no topo; `summary` em texto; `directions` em `out|in|both|none`; `dev_portal` vazio em vez de `null`/texto. Os campos extras podem ficar.
3. Por autoridade (4 pastas): reorganizar o conteúdo nas pastas oficiais `P1-compliance/` … `P7-qa-uat/` com os 13 arquivos do S3; escrever os dois runbooks `.docx` OUT e IN no esqueleto de 10 seções, com banner coerente com o modo.
4. Escrever o que não existe em nenhum lugar: §1 fronteiras, §3.2/3.4 n8n, §10 quick reference (FR), `statutory-report-templates.md`, `statutory-compliance-report.md` com nota de walkthrough, `legal-entity-statement.md` (precisa de pesquisa com fonte; na FR há pergunta aberta sobre K-BIS/entidade francesa para DGFIP-EDI).
5. Padronizar `[[NEEDS-ARTEFACT: <artefato + onde>]]` com dois-pontos (FR, 24 ocorrências) e decidir o modo de cada autoridade (FR fica structural enquanto houver item gated).
6. Tirar as menções a outras autoridades de P1/P3/P4/P5/P7/`_phase-index`/`effort-estimates`, deixando-as só no INTERLINKAGES (em linhas curtas); tirar `_previous/` de dentro da pasta da DIAN-NE no cérebro (ou mover) para não poluir o S1.
7. Colocar `Source:` por subseção nos runbooks e reexecutar `si_scope_check.py` com `--other` = todas as autoridades do landscape, nos dois modos.
8. Decidir com o usuário o destino do formato registro no Drive (`SIR-INDEX` de 29/09 e Google Docs `FR-SIR-001`/`CO-SIR-001`): voltar ao índice curto + runbooks por autoridade, ou manter o registro como peça à parte. FR e CO estão ativos? Se sim, a regra 9 (ticket ao Development) vale antes de qualquer troca.

## Bloco de prova
- **Pedido → resposta:** contrato listado (§1); cada autoridade de FR e CO comparada item a item (§3, §4); scope check oficial rodado nas 4 pastas, mais a cópia antiga da CO (§2); FALTA/DIVERGE/OK e impacto (§3–5); nada corrigido; conteúdo estatutário não avaliado.
- **Fontes:** agentes e checker do zip v2.12.1; Stage 6 de `~/mercans-pipeline/mercans_pipeline_v2_12.sh` (linhas ~1940–2080, `--other` = `_integrable.txt`, `MODE=structural`); logs `si_*.log` de FR e CO; arquivos das pastas citadas na tabela "O que foi comparado".
- **Teste:** `si_scope_check.py` executado (exit 2 = BLOCKED em FR; exit 0 em CO principal; exit 2 em CO complementar); campos do JSON lidos por script; títulos `#`/`##` de cada `.md` extraídos; md5 de índices × Drive; contagem de `[[NEEDS-ARTEFACT` por arquivo.
- **Confiança: 90%.** Falta: abrir os Google Docs `FR-SIR-001`/`CO-SIR-001` no Drive (só o texto v1.3 local foi lido); a classificação DIVERGE × FALTA de alguns itens de esqueleto (§2.5, §3.1, §4) é julgamento de equivalência de conteúdo feito por títulos e trechos, não leitura integral dos ~4.000 linhas.
