# Extração: pipeline França (2026-10-27)

> Arquivo: `extracoes/2026-10-27-pipeline-Franca.md`. Um cartão por item. Só entra o que muda a resposta certa.
> Material bruto: `raw/pipeline/Franca/2026-10-27/` (abreviado **RAW** abaixo) e `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` · Inventário: `inventarios/pipeline.md` (item 3) · Padrão: [[PLANO]] §4 (níveis A/B/C/D) e §5 (validação, lotes de até 40).
> Fonte: F6 Passo 3 (cenário 3, pipeline local v2.12). Hub e correções consultados para deduplicar: [[Franca]], [[correcoes]] (linhas 68–71), `revisoes/2026-10-17-matriz-cobertura-FR-pipeline.md`.

## Resumo
- Itens do inventário neste lote: 1 (item 3, `FR-compliance/`) · Cartões: 40 · Complementos de cartão existente: 22 (18 "sim" + 4 "parcial") · Descartados: 14 linhas (agrupam ~40 arquivos)
- Por tipo: versão final 10 · erro+causa 16 · pendência 9 · alerta 5 (alerta = estado do hub desatualizado ou valor/vigência com fonte, fora dos 3 tipos do prompt)
- Risco alto: 21 (100% vão para validação) · Amostra dos demais: 2 de 19 (10%)
- [INCERTO]: 12 (viram pergunta ao usuário)
- Validação: ⏳ pendente
- Ingestão: ✅ feita em 2026-10-27 (hub; correcoes pela janela geral)

**Leitura-chave (vale para vários cartões).** O que está em `FR-compliance/` hoje é o **pacote reemitido de 2026-10-06** (numeração reiniciada em v1.0), promovido em 2026-10-09. Os relatórios de QA (v1 a v4, 2026-08-28 a 09-03) e o hub descrevem a **linhagem anterior** (CCG v1.3, WTC v1.2, DD v1.4, specs v1.1). A reemissão foi verificada só por amostra (Teste 0, 51 afirmações, 2026-10-09). Cada cartão diz a qual das duas linhagens a afirmação se aplica.

## Cartões

### F6-20261027-FR-C01 · versão final · [[Franca]]
- **Chave:** `FR | PACOTE | versão vigente = v1.0 reemitida em 2026-10-06` · **Já existe?** sim → complementa [[Franca]] §Artefatos entregues (linha do DD "exceção à regra 8"), que só vale essa exceção para o DD
- **Tipo:** versão final
- **Risco:** alto (versão vigente)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o PROMOTION-LOG de 06/10 promoveu CCG v1.1, WTC v1.1, DD v1.2, Payslip e 15 specs (changelogs internos v1.4/v1.5/v1.6) vindos de `fr-research-validation/final`; o de 09/10 arquivou CCG v1.1, WTC v1.1 e DD v1.2 e promoveu o pacote reemitido, todo com Version Control `1.0 | 2026-10-06 | Approved`. Pela regra 8 (maior número **e** promovida), a exceção "número menor, emissão mais nova" vale para CCG, WTC, DD, Specs e Payslip, não só para o DD.
- **Antes (se erro):** hub lista CCG v1.0 (~2026-08-26), WTC v1.0 (08-27, "Draft"), Specs "v1.1 vigente: maior versão", Payslip v1.0: são linhas da linhagem de agosto/setembro.
- **Causa (se erro):** a validação FR (`fr-research-validation`) renumerou o pacote ao emitir; o hub registrou a exceção só ao reemitir o DD.
- **Correto / novo:** vigente = pacote v1.0 de 2026-10-06 (arquivos md5 em `RAW/version-control/MANIFEST.md`), promovido em 2026-10-09; v1.1/v1.2/v1.3/v1.4 citadas nos QAs são histórico. Decisão D6 do inventário: finais FR = arquivos do pipeline.
- **Nível de evidência:** B · **Fonte:** PROMOTION-LOG-2026-10-06 e -2026-10-09 (Version Control dos artefatos)
- **Localização no raw:** `RAW/notas/PROMOTION-LOG-2026-10-06.md` linhas 3, 7–18 (promoção v1.1/v1.2) e `RAW/notas/PROMOTION-LOG-2026-10-09.md` linhas 7–14 e 66 (arquivou v1.1/v1.2, promoveu v1.0); `RAW/version-control/MANIFEST.md` tabela
- **Quem decidiu / pediu:** aprovado por Wallisson Gomes (Compliance Regulations Team Lead), PROMOTION-LOG 06/10 linha 3
- **Destino:** hub (Artefatos entregues, Situação)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual é a versão vigente do CCG da França e de onde vem?"
- **Confiança da extração:** alta
- **Validação:** ◐ conferência independente: Payslip sem Version Control e SIR com VC de 2026-08-27 fora da reemissão; Version Control 1.0 / 2026-10-06 vale para CCG, WTC, DD e 15 specs · humana ⏳

### F6-20261027-FR-C02 · versão final · [[Franca]]
- **Chave:** `FR | CCG | FR-CCG-001 versão vigente`  · **Já existe?** sim → complementa [[Franca]] §Artefatos entregues (CCG v1.0 ~2026-08-26)
- **Tipo:** versão final
- **Risco:** alto (versão vigente)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o CCG no pipeline é [[Research Pipeline/França/CCG/FR-CCG-001-v1.0.docx|FR-CCG-001-v1.0.docx]], Version Control `1.0 | 2026-10-06 | Initial version ... Approved`, md5 `a9f16a70bd6957dcab5d5411c26eeab0`, igual ao promovido em 09/10. **O mesmo nome de arquivo já designou três conteúdos**: o de agosto/setembro (arquivado em 06/10, sha `cf8675c1a56cb59a`; é o "CCG v1.0/v1.2/v1.3" dos QAs), o v1.1 (arquivado em 09/10, md5 `7c0e8421…`) e este. Só o md5 distingue.
- **Antes (se erro):** hub e monday dizem "v1.0" sem distinguir; monday (CCG – AI, Done) atualizado em 2026-09-15, **anterior** à reemissão: o link pode apontar a linhagem antiga (não verificável aqui).
- **Causa (se erro):** reuso do nome [[Research Pipeline/França/CCG/FR-CCG-001-v1.0.docx|FR-CCG-001-v1.0.docx]] na reemissão.
- **Correto / novo:** CCG vigente = md5 `a9f16a70…` (2026-10-06). Ao citar "CCG v1.0 da França", dizer a data e o md5.
- **Nível de evidência:** B · **Fonte:** Version Control do CCG + PROMOTION-LOG-2026-10-09
- **Localização no raw:** `RAW/version-control/FR-CCG-001-v1.0.md` tabela linha 1; `RAW/notas/PROMOTION-LOG-2026-10-09.md` linhas 7–8; `RAW/notas/PROMOTION-LOG-2026-10-06.md` linha 7 (sha cf8675…); `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` linha 19
- **Quem decidiu / pediu:** —
- **Destino:** hub (Artefatos entregues)
- **Pergunta para o teste (Conjunto B)?** sim → "O link do monday do CCG FR aponta a versão reemitida?"
- **Confiança da extração:** alta (versão); [INCERTO] só para o que o link do monday abre
- **Validação:** ◐ conferência independente: o nome FR-CCG-001-v1.0.docx designou 2 conteúdos (agosto/setembro e reemissão); o v1.1 tinha nome próprio · humana ⏳

### F6-20261027-FR-C03 · versão final · [[Franca]]
- **Chave:** `FR | WTC | FR-WTC-001 versão vigente` · **Já existe?** sim → complementa [[Franca]] §Artefatos entregues (WTC v1.0, 2026-08-27, "Draft")
- **Tipo:** versão final
- **Risco:** alto (versão vigente)
- **Serviço:** [[research-pipeline]]
- **O que diz:** WTC vigente [[Research Pipeline/França/WTC/FR-WTC-001-v1.0.xlsx|FR-WTC-001-v1.0.xlsx]], Version Control `1.0 | 2026-10-06 | Initial version | Approved | Wallisson Gomes`, título "France (FR) - income year 2026"; arquivo de 2026-10-09; monday (WTC – AI) v1.0, atualizado 2026-09-15.
- **Antes (se erro):** hub: "Draft no Version Control" (08-27).
- **Causa (se erro):** o hub descreve o WTC da linhagem anterior; o reemitido está **Approved**.
- **Correto / novo:** status Approved, 2026-10-06. O md5 coletado diverge do PROMOTION-LOG (ver C04).
- **Nível de evidência:** B · **Fonte:** Version Control do WTC
- **Localização no raw:** `RAW/version-control/FR-WTC-001-v1.0.md` aba `Version Control`, linha "1.0 | 2026-10-06"; `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` linha 20
- **Quem decidiu / pediu:** —
- **Destino:** hub (Artefatos entregues)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C04 · versão final · [[Franca]]
- **Chave:** `FR | WTC+DD | md5 diverge do PROMOTION-LOG com o mesmo Version Control` · **Já existe?** não (o hub guarda o md5 do DD `889f66d2…`, não a divergência)
- **Tipo:** versão final
- **Risco:** alto (versão vigente)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o PROMOTION-LOG de 09/10 registra WTC `553fb181ca8f0d8d3a3fe473d5b44730` e DD `8a91af…`; os arquivos coletados têm WTC `8592d40b5d520110ec99f0bdc585caf7` e DD `889f66d2cb84c8959852834cb89e046a`. CCG e Payslip batem; as 15 specs divergem, mas isso o log explica (re-sync, ver C23). Para WTC e DD o log **não** explica, e o Version Control continua `1.0 | 2026-10-06 | Initial version`.
- **Antes (se erro):** —
- **Causa (se erro):** [INCERTO]. Hipótese: cópia atualizada depois da promoção (o hub diz que o DD de 09/10 = `fr-research-validation/final/` e que o DD foi reemitido ao Drive em 2026-10-26); para o WTC não há registro.
- **Correto / novo:** tratar WTC e DD do pipeline como "v1.0 com conteúdo posterior ao log"; perguntar ao usuário se houve edição sem nova linha no Version Control.
- **Nível de evidência:** B · **Fonte:** PROMOTION-LOG-2026-10-09 × MANIFEST-coleta
- **Localização no raw:** `RAW/notas/PROMOTION-LOG-2026-10-09.md` linhas 10 e 12; `RAW/MANIFEST-coleta.md` e `RAW/version-control/MANIFEST.md` (linhas FR-WTC-001-v1.0 e FR-DD-001-v1.0)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (causa da divergência; os md5 em si são fato)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C05 · versão final · [[Franca]]
- **Chave:** `FR | DD | FR-DD-001 v1.0 (2026-10-06)` · **Já existe?** sim → confirma [[Franca]] §Artefatos entregues (DD v1.0 vigente a partir de 2026-10-06)
- **Tipo:** versão final
- **Risco:** alto (versão vigente)
- **Serviço:** [[design]] / [[research-pipeline]]
- **O que diz:** Version Control do DD: `1.0 | 2026-10-06 | Initial version | Approved | Wallisson Gomes`; md5 `889f66d2…` = o do hub; monday (DD – AI) `FR-DD-001-v1.0`, atualizado 2026-10-26, link `1bQcuzfLgHznJRMB_lFe2JloJyxEHEui9o85Pr3i4dLg` = o do hub. A divergência de nome do QA (m-2: arquivo v1.0 × Version Control v1.1) **não existe** na reemissão. Resíduo: a célula de título do Version Control está como `<France>` (placeholder com colchetes).
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** nada a mudar no hub; acrescentar a conferência e o resíduo `<France>`.
- **Nível de evidência:** B · **Fonte:** Version Control do DD; monday
- **Localização no raw:** `RAW/version-control/FR-DD-001-v1.0.md` aba `Version Control`, linhas 2 e 4; `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` linha 21
- **Quem decidiu / pediu:** —
- **Destino:** hub (Artefatos entregues)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C06 · versão final · [[Franca]]
- **Chave:** `FR | SIR | FR-SIR-INDEX-001 × "FR-SIR-001"` · **Já existe?** sim → complementa [[Franca]] §Artefatos entregues (SIR FR-SIR-INDEX-001 v1.0, 2026-08-27)
- **Tipo:** versão final
- **Risco:** alto (versão vigente; identificador)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o arquivo é [[Research Pipeline/França/SIR/FR-SIR-INDEX-001-v1.0.docx|FR-SIR-INDEX-001-v1.0.docx]] (md5 `889e19c1…`), Version Control `v1.0 | 2026-08-27 | Mercans Compliance Regulations Team | Initial issue.`, mas o arquivo é de **2026-09-29**. O SIR **não aparece em nenhum PROMOTION-LOG** (não foi reemitido). O monday rotula o item "Statutory Integration" como `FR-SIR-001-v1.0` (atualizado 2026-09-29); a varredura do pipeline procurou `FR-SIR-001-v1*.docx` e não achou. As specs reemitidas apontam "FR-SIR-INDEX-001 v1.0 - DELIVERED" e explicam o id. O QA v4 confirma que "FR-SIR-001" existe sob o nome FR-SIR-INDEX-001, com runbooks de 28 arquivos.
- **Antes (se erro):** monday e a verificação do pipeline usam "FR-SIR-001".
- **Causa (se erro):** o registro da FR é um índice por autoridade, com id diferente do padrão `{CC}-SIR-001`.
- **Correto / novo:** id correto `FR-SIR-INDEX-001`; "FR-SIR-001" é o rótulo do monday para o mesmo documento. A data do Version Control (08-27) é anterior à do arquivo (09-29) sem linha nova: [INCERTO] se o conteúdo mudou.
- **Nível de evidência:** B · **Fonte:** Version Control do SIR; monday; specs reemitidas
- **Localização no raw:** `RAW/version-control/FR-SIR-INDEX-001-v1.0.md` tabela linha 1; `RAW/version-control/MANIFEST.md` linha FR-SIR-INDEX-001; `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` linha 23; `RAW/qa/audit_recheck_artifactfix.json` (check C29, `evidence.scan_errors`); `RAW/qa/FR-QA-REPORT-v4-20260903.md` linha 36; `RAW/version-control/FR-URSSAF-001-DPAE-Spec.md` linha 19
- **Quem decidiu / pediu:** —
- **Destino:** hub (Artefatos entregues)
- **Pergunta para o teste (Conjunto B)?** sim → "FR-SIR-001 e FR-SIR-INDEX-001 são o mesmo documento?"
- **Confiança da extração:** média ([INCERTO] quanto à data do conteúdo)
- **Validação:** ◐ conferência independente: md5 do SIR correto = 889c19e11e767d19a66f58b06de55fde · humana ⏳

### F6-20261027-FR-C07 · versão final · [[Franca]]
- **Chave:** `FR | Report Specs (15) | versão vigente = v1.0 (2026-10-06)` · **Já existe?** sim → corrige [[Franca]] §Artefatos entregues ("v1.1 vigente: maior versão") e fecha a pendência "Version Control das specs (linhas 19–20)"
- **Tipo:** versão final
- **Risco:** alto (versão vigente)
- **Serviço:** [[research-pipeline]]
- **O que diz:** as 15 specs têm, cada uma, uma só linha de versão `1.0 | 2026-10-06 | Initial version | Approved | Wallisson Gomes` (linha 13 do Version Control extraído), arquivos de 2026-10-09 (re-sync). As linhas "Downstream alignment / Wage types / SIR cross-reference" (17–19) dizem agora DD v1.0, WTC v1.0 e SIR-INDEX v1.0 **DELIVERED** (antes "NOT AVAILABLE"). Não há v1.1 nelas. O monday não tem item de Report Specs. O inventário (item 3) lista só 8 specs; o Version Control mostra 15.
- **Antes (se erro):** hub: specs "v1.1 (vigente: maior versão); histórico v1.0" e Pendência "linhas 19–20 ainda dizem WTC/SIR NOT AVAILABLE".
- **Causa (se erro):** reemissão com numeração reiniciada (C01).
- **Correto / novo:** vigente v1.0 (2026-10-06); pendência das linhas 19–20 resolvida na reemissão. md5 de cada spec: `RAW/version-control/MANIFEST.md`. Corrigir a contagem do inventário (15, não 8).
- **Nível de evidência:** B · **Fonte:** Version Control das 15 specs
- **Localização no raw:** `RAW/version-control/FR-{AGIRC-001,CARSAT-001,CDC-001,CPAM-002,CPAM-003,DGFIP-001,DGFIP-002,DGFIP-003,DSN-001,DSN-002,DSN-003,URSSAF-001,URSSAF-002,URSSAF-003,URSSAF-004}-*-Spec.md` linhas 13 e 17–19; `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` (sem item de Report Specs, linha 25)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Artefatos entregues; Pendências)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual a versão vigente das Report Specs da França?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C08 · versão final · [[Franca]]
- **Chave:** `FR | Payslip | FR_Compliance_Payslip_Generator sem Version Control` · **Já existe?** não (o hub só diz "Payslip FR-PSL-001 v1.0, 8 abas")
- **Tipo:** versão final
- **Risco:** alto (versão vigente)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o Payslip Generator **não tem Version Control** (achado: coleta marca "não"). md5 `d98d54163bcecaa866729b77b645334b` = o promovido em 09/10; arquivo de 2026-10-06. O PROMOTION-LOG de 06/10 promoveu o Payslip com changelog chamado `...-v1.1-CHANGELOG.md` e arquivou o anterior como `...-v1.0-2026-09-02.xlsx`; o de 09/10 re-promoveu o do pacote reemitido. O número "v1.0" do hub não é provável por Version Control.
- **Antes (se erro):** hub: Payslip v1.0.
- **Causa (se erro):** o template do Payslip não carrega aba de versão.
- **Correto / novo:** versão vigente do Payslip = o arquivo md5 `d98d5416…`; o rótulo ("v1.0" do hub × "v1.1" do changelog de 06/10) fica [INCERTO]: decisão do usuário.
- **Nível de evidência:** B · **Fonte:** PROMOTION-LOGs; MANIFEST
- **Localização no raw:** `RAW/version-control/MANIFEST.md` última linha (VC encontrado: não); `RAW/notas/PROMOTION-LOG-2026-10-06.md` linhas 16–18; `RAW/notas/PROMOTION-LOG-2026-10-09.md` linhas 13–14
- **Quem decidiu / pediu:** —
- **Destino:** hub (Artefatos entregues); `servicos/research-pipeline`
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (rótulo da versão)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C09 · versão final · [[Franca]]
- **Chave:** `FR | Skill | fr-compliance promovida em 2026-10-09 × ficha lida em 2026-10-02` · **Já existe?** sim → complementa [[Franca]] §Ficha do país (da skill)
- **Tipo:** versão final
- **Risco:** alto (a ficha responde perguntas e está defasada)
- **Serviço:** [[research-pipeline]]
- **O que diz:** em 09/10 a skill foi promovida a `08-skill/fr-compliance/` (SKILL.md `name: fr-compliance`, md5 `6a208ed7…`; referências 01–06 novas) e `07-qa-report.md` foi **arquivado sem substituto**. A ficha do hub foi lida da skill em 2026-10-02 e se apoia no `07-qa-report.md` (F-1..F-3, 87/100). Regra do Passo 3: skill de Stage 11 mais nova que a data de leitura → reler a ficha. O passo B5 de 06/10 terminou `APEC 4 PSS present: CHECK` (não OK); o TEST0 C09 depois confirmou Apec até 4 PSS (C39).
- **Antes (se erro):** ficha com "QA 87/100 NEEDS PATCHES" e armadilhas F-1..F-3, m-2.
- **Causa (se erro):** a ficha foi extraída antes da reemissão.
- **Correto / novo:** reler a skill promovida e reescrever a ficha (data nova); a skill recompilada em 06/10 usou CCG v1.1/WTC v1.1/DD v1.2, e a de 09/10 veio da reemissão.
- **Nível de evidência:** B · **Fonte:** PROMOTION-LOG-2026-10-09 (+ 06/10 Step 2)
- **Localização no raw:** `RAW/notas/PROMOTION-LOG-2026-10-09.md` linhas 58–59 (arquivou 07-qa-report e SKILL.md anterior) e 60–66 (promoveu 01–06 e SKILL.md); `RAW/notas/PROMOTION-LOG-2026-10-06.md` linhas 70–82 (Step 2, B2/B5)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Ficha do país); skill `payroll-compliance-france`
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C10 · versão final · [[Franca]]
- **Chave:** `FR | WTC+DD | contagens (374 WTs; 189 campos)` · **Já existe?** sim → complementa [[Franca]] §Artefatos entregues
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o hub dá WTC "374 WTs = 300 + 74 FR-0xx" e DD "25 ID + 164 campos de país". O QA v2/v3 mede WTC **378** (F-2 acrescentou FR-075..FR-078) e DD **198** campos (25 + 173, após 9 campos novos em 09-02); o audit mecânico confirma `WTC-378-codes PASS`. No WTC reemitido, o TEST0 cita FR-079 (COTAM) na linha 380: consistente com ≥ 379, mas a contagem final não está em nenhum arquivo coletado.
- **Antes (se erro):** 374 / 164 do hub (linhagem de 08-27).
- **Causa (se erro):** itens acrescentados por F-2 e pelo reforço do DD em 09-02.
- **Correto / novo:** linhagem antiga: 378 WTs, 198 campos. Reemitido: contagem [INCERTO] (conferir abrindo o xlsx).
- **Nível de evidência:** B · **Fonte:** QA v2, v3; audit_v3_mechanical; TEST0
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v2-20260902.md` linhas 125–137 e 49–52; `RAW/qa/FR-QA-REPORT-v3-20260903.md` linhas 16–25; `RAW/qa/audit_v3_mechanical.json` (check `WTC-378-codes`); `RAW/qa/FR-TEST0.json` assertion W08 (`Wage Type Catalogue!D380`)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Artefatos entregues)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (contagem do pacote reemitido)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C11 · erro+causa · [[Franca]]
- **Chave:** `FR | QA | veredito vigente (F-1..F-3 fechados; READY FOR DEV TEAM)` · **Já existe?** sim → corrige [[Franca]] §Situação, §Pendências (1ª linha) e §Ficha ("Confiança da skill")
- **Tipo:** alerta (estado do hub desatualizado)
- **Risco:** alto (correção de estado)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o hub segue com "87/100, NEEDS PATCHES; F-1, F-2, F-3 bloqueiam". O QA v2 (2026-09-02) fechou F-1, F-2, F-3, m-1 e m-2 e reenquadrou m-3; o v3 (09-03) deu 12/12 no audit mecânico; o v4 (09-03, o mais recente) dá **READY FOR DEV TEAM, zero defeitos de conteúdo abertos** (5 itens restantes, nenhum bloqueante). Limite: v2–v4 verificam a linhagem anterior (CCG v1.3, WTC v1.2, DD v1.4, cabeçalho do v4 linha 5), não o pacote reemitido, que só passou pelo TEST0 (C38). Cobertura declarada: v2 amostrou 18/378 WTs e deixou 132/150 H3 do CCG sem leitura; v3 afirma 378/378 e 13/13 módulos (o mais recente prevalece).
- **Antes (se erro):** hub: NEEDS PATCHES (QA de 2026-08-28).
- **Causa (se erro):** os QAs v2–v4 não chegaram ao hub.
- **Correto / novo:** veredito vigente do QA = v4, 2026-09-03; marcar F-1..F-3, m-1, m-2 como fechados (linhagem anterior); m-3 segue como pergunta ao dono do padrão.
- **Nível de evidência:** B · **Fonte:** FR-QA-REPORT v2/v3/v4
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v4-20260903.md` linhas 5, 11 e 62–66; `RAW/qa/FR-QA-REPORT-v2-20260902.md` linhas 120–145; `RAW/qa/FR-QA-REPORT-v3-20260903.md` linhas 11–25
- **Quem decidiu / pediu:** —
- **Destino:** hub (Situação, Pendências)
- **Pergunta para o teste (Conjunto B)?** sim → "A França está pronta para o time de dev? Quais achados do QA ainda estão abertos?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C12 · erro+causa · [[Franca]]
- **Chave:** `FR | Report Specs | F-1 "NO DD COUNTERPART" (264 linhas)` · **Já existe?** sim → complementa [[Franca]] §Pendências (F-1) e §Ficha armadilha 3
- **Tipo:** erro+causa
- **Risco:** alto (correção de erro)
- **Serviço:** [[research-pipeline]]
- **O que diz:** 264 linhas de 12 specs afirmavam "sem contraparte no DD". Causa raiz: o join foi feito pela rubrique NEODeS e 6 filings não são NEODeS (DPAE cita artigos do Código do Trabalho, DAT cita rótulos do cerfa, taxe sur les salaires cita posições do formulário), então o join não rodou e o "não achado" foi gravado como achado. Resolução (QA v2, 2026-09-02): 264/264 reconciliadas, 0 sem solução: 88 com campo do DD, 63 reclassificadas CALC, 52 dados transacionais corretamente fora, 36 de regime fora do escopo, 9 lacunas reais, 8 retornos inbound (SYS); amostra de 40 das já confirmadas: 40/40. Padrões F32–F34 entraram no failure log. FR-LIM-001 contava 199 e citava o e-mail como omissão: o DD tem `E-mail Address`.
- **Antes (se erro):** hub: "Corrigir F-1" (pendente); ficha: "264 linhas (substancialmente falsa)".
- **Causa (se erro):** reconciliação pela chave errada, escrita nos 12 workbooks como achado.
- **Correto / novo:** fechada na linhagem anterior; 9 lacunas reais, sem lista nominal nos arquivos coletados (não inventar). As specs reemitidas passaram pelo builder corrigido (ver C17); não verificado se a anotação sumiu delas.
- **Nível de evidência:** B · **Fonte:** QA v1 (F-1) e QA v2 (fechamento)
- **Localização no raw:** `RAW/qa/FR-QA-REPORT.md` linhas 155–213 (Check 4) e 341–367 (F-1); `RAW/qa/FR-QA-REPORT-v2-20260902.md` linhas 62–74 e 124–137; `RAW/logs/alignment.log` (199 linhas "payroll master data" sem contraparte)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências → fechar; Ficha armadilha 3 → atualizar); [[correcoes]] só se o usuário quiser registrar o erro de método
- **Pergunta para o teste (Conjunto B)?** sim → "Por que 264 linhas das specs da FR diziam 'NO DD COUNTERPART' e elas são verdadeiras?"
- **Confiança da extração:** média (aplicação à reemissão não verificada)
- **Validação:** ◐ conferência independente: baldes do QA v2 somam 256, não 264; não afirmar "9 lacunas reais" como fechado · humana ⏳

### F6-20261027-FR-C13 · erro+causa · [[Franca]]
- **Chave:** `FR | WTC+Payslip | F-2 BIK refeição e ferramentas de comunicação` · **Já existe?** sim → complementa [[Franca]] §Pendências (F-2) e §Ficha armadilha 4
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o CCG Mod. 7 exigia valorar dois benefícios em espécie (refeição, ferramentas de comunicação) sem wage type no WTC. Fechado no QA v2: FR-075 a FR-078 criados no WTC, na aba Unit Rate Details e na fórmula do Payslip Spec, e no exemplo visual, "cross-consistent". O QA v3 achou ainda: a fórmula "Benefits in Kind" usava intervalo numérico `62400:62499`, incompatível com os códigos-texto novos (virou lista explícita) e contava indevidamente auxílio-moradia em dinheiro como BIK.
- **Antes (se erro):** WTC sem tipo para refeição/NTIC; fórmula do Payslip por intervalo.
- **Causa (se erro):** os BIK do CCG não viraram wage types; fórmula escrita para códigos numéricos.
- **Correto / novo:** FR-075..FR-078 existem (linhagem anterior). Os valores 5,50 / 11,00 / 2,75 / 10 % vêm do CCG Mod. 7 sem fonte primária nos arquivos coletados: **⚠️ sem fonte A neste lote**, não entram.
- **Nível de evidência:** B · **Fonte:** QA v1 (F-2), v2, v3
- **Localização no raw:** `RAW/qa/FR-QA-REPORT.md` linhas 92–105 e 371–388; `RAW/qa/FR-QA-REPORT-v2-20260902.md` linhas 38–46 e 125; `RAW/qa/FR-QA-REPORT-v3-20260903.md` linha 47
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências → fechar F-2)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C14 · erro+causa · [[Franca]]
- **Chave:** `FR | CCG+scope_manifest | F-3 SIPSI (declaração de trabalhador destacado)` · **Já existe?** sim → complementa [[Franca]] §Pendências (F-3) e §Decisões (SIPSI fora)
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o CCG Mod. 10 listava a SIPSI como "in scope" enquanto o manifest e o Mod. 11 a excluíam; o registro de filings não a tinha em nenhum lado. O QA v2 diz "Confirmed consistent (Module 10, scope_manifest, WTC)". Indício de que `FR-MOL-001` entrou: `out_of_scope` tinha 13 entradas em 2026-09-01 e o Stage 9 de 09-02 conta "15 in-scope, 14 out-of-scope"; nenhum arquivo coletado nomeia a entrada.
- **Antes (se erro):** CCG × manifest em contradição.
- **Causa (se erro):** o CCG foi escrito antes da decisão de escopo.
- **Correto / novo:** SIPSI fora do escopo (manifest governa), consistente nos 3 artefatos na linhagem anterior. Criação de `FR-MOL-001`: [INCERTO] (inferida pela contagem).
- **Nível de evidência:** B · **Fonte:** QA v1 (F-3), v2, stage9_rerun, scope_validation
- **Localização no raw:** `RAW/qa/FR-QA-REPORT.md` linhas 392–412; `RAW/qa/FR-QA-REPORT-v2-20260902.md` linhas 58–60 e 126; `RAW/qa/stage9_rerun_20260902.json` (check C20); `RAW/qa/scope_validation.md` linhas 36–48
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências → fechar F-3)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (FR-MOL-001)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C15 · erro+causa · [[Franca]]
- **Chave:** `FR | QA | m-1 / m-2 / m-3 fechados` · **Já existe?** sim → complementa [[Franca]] §Ficha armadilha 7 e §Decisões (m-3)
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** m-1 (chaves compostas, C13): de 53/90 para **90/90** documentados (QA v2). m-2 (DD v1.0 no nome × v1.1 no Version Control): referências de nome corrigidas em 8/8 arquivos operacionais; sobrou texto histórico (célula A1 da aba Field Option do Payslip ainda cita `FR-DD-001-v1.0.xlsx`) e a skill carregou m-2 por não existir arquivo v1.1. m-3 (verde do net pay): QA v2 reenquadra como **não defeito da FR** (BE e Tunísia usam azul-marinho); o QA v1 já dizia "não corrigir só a França".
- **Antes (se erro):** 53/90; nome v1.0 × VC v1.1; "m-3 pendente".
- **Causa (se erro):** documentação não aplicada de modo uniforme; versão renomeada só no conteúdo.
- **Correto / novo:** m-1 e m-2 fechados; m-3 continua pergunta ao dono do padrão (decisão de 2026-08-28 vale), não defeito da FR.
- **Nível de evidência:** B · **Fonte:** QA v1, v2; audit C21; skill.log
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v2-20260902.md` linhas 126–130 e 98–106; `RAW/qa/FR-QA-REPORT.md` linhas 418–448; `RAW/qa/stage9_rerun_20260902.json` (C21 override); `RAW/logs/skill.log` (últimos parágrafos)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências; Ficha)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C16 · erro+causa · [[Franca]]
- **Chave:** `FR | FR-DGFIP-003 | taxe sur les salaires: 4,25 / 8,50 / 13,60 % e faixas 2026` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** alto (valor estatutário + correção de erro)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o QA v3 achou na FR-DGFIP-003 as taxas "4,25 % / 9,35 %" onde o correto era 8,50 % / 13,60 % (CGI art. 231), em 12 células de 6 abas; o QA v4 achou um resíduo (célula M14 repetindo 4,25 % onde o cálculo exigia 8,50 %). **Cuidado com a leitura:** na spec reemitida (TEST0, 2026-10-09) 4,25 % e 9,35 % são as taxas **adicionais** da 2ª e 3ª faixas (linhas do 2502-SD), e o total por faixa é 4,25 % (normal) / 8,50 % / 13,60 %. As duas afirmações são compatíveis; o erro era usar a taxa adicional como total. Faixas para remunerações pagas **a partir de 2026-01-01**: 2ª faixa acima de 9.229/ano (769/mês, 2.307/trimestre) até 18.423/ano (1.535/mês, 4.606/trimestre); 3ª acima de 18.423.
- **Antes (se erro):** taxas adicionais gravadas como taxa total (spec v1.0/v1.1 de agosto).
- **Causa (se erro):** confusão entre taxa adicional (majorada) e taxa da faixa.
- **Correto / novo:** 4,25 % normal; 8,50 % (4,25 + 4,25) na 2ª faixa; 13,60 % (4,25 + 9,35) na 3ª; limiares 9.229 / 18.423 (a partir de 2026-01-01).
- **Nível de evidência:** B (QA/TEST0 fechados), com fonte A citada: Notice 2501-NOT-SD 2026 e formulário 2501-SD 2026 (DGFiP), CGI art. 231 · **Fonte:** idem
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v3-20260903.md` linha 41 (e tabela linha 20); `RAW/qa/FR-QA-REPORT-v4-20260903.md` linha 20; `RAW/qa/FR-TEST0.json` assertions R07 e R08 (citações do 2501-NOT-SD)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Valores-chave, com vigência); [[correcoes]] (erro da spec de agosto) se o usuário aprovar
- **Pergunta para o teste (Conjunto B)?** sim → "Quais as taxas e faixas da taxe sur les salaires em 2026?"
- **Confiança da extração:** média (leio a nota do TEST0, não o formulário)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C17 · erro+causa · [[Franca]]
- **Chave:** `FR | Report Specs | contaminação de texto em 18 células de 8 arquivos (+ AGIRC-001)` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o QA v3 achou um padrão recorrente: a descrição de um campo vizinho sobrescrevendo a célula errada, em 18 lugares de 8 arquivos (inclusive no bloco de envelope comum às specs da DSN, "Title code / Telephone number", e nas tabelas Field Options de DGFIP-EDI e NETENT-DSN); mais 1 contaminação de dados em AGIRC-001 Field Options (Alignment Patch). Todos corrigidos e relidos do disco. Na reemissão de 06/10, o builder corrigido foi reinstalado e as 15 specs reconstruídas ficaram idênticas, célula a célula, às promovidas (A2–A4).
- **Antes (se erro):** texto trocado entre campos vizinhos.
- **Causa (se erro):** script de reconciliação escrevendo na célula adjacente.
- **Correto / novo:** corrigido na linhagem anterior; builder corrigido na reemissão.
- **Nível de evidência:** B · **Fonte:** QA v3; PROMOTION-LOG 06/10 Step 2
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v3-20260903.md` linhas 20, 41 e 18; `RAW/notas/PROMOTION-LOG-2026-10-06.md` linhas 72–75
- **Quem decidiu / pediu:** —
- **Destino:** [[correcoes]] ou skill `mercans-pipeline-methodology` (padrão de falha; já tem F32–F34 do mesmo tipo de reconciliação)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C18 · erro+causa · [[Franca]]
- **Chave:** `FR | SIR | 4 correções (URSSAF-DPAE N_SIRET 02→01; 3 no landscape do DGFIP-EDI)` · **Já existe?** parcial → [[correcoes]] linhas 69–70 tratam do manifest (DPAE host/TXT/XML; DGFIP-003 EDIFACT); N_SIRET é novo
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** QA v3: 4 correções no SIR (formato, direção, código de controle do SIRET), todas relidas do disco: DGFIP-EDI 3 correções em `integration-landscape.json`; NETENT-DSN 0; URSSAF-DPAE 1: o código de controle de `N_SIRET` era **02** e passou a **01**, conferido contra o catálogo de erros P5 e o caso de teste T-09. No QA v2, o F27 (campo `integration_type` do FR-DGFIP-003 com texto livre em vez do enum) foi achado e corrigido no `scope_manifest.json`.
- **Antes (se erro):** `N_SIRET` com controle 02.
- **Causa (se erro):** divergência entre o runbook e o catálogo de erros do próprio documento do URSSAF (não detalhada no raw).
- **Correto / novo:** controle 01 (nível B: catálogo P5 do SIR, sem citar o artigo da URSSAF nos arquivos coletados).
- **Nível de evidência:** B · **Fonte:** QA v3; QA v2
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v3-20260903.md` linhas 19 e 37–38; `RAW/qa/FR-QA-REPORT-v2-20260902.md` linhas 79–86 e 150 (Check 6)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências SIR)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C19 · erro+causa · [[Franca]]
- **Chave:** `FR | DD | Contract Nature (S21.G00.40.007): 9 de 26 códigos` · **Já existe?** sim → complementa [[Franca]] §Decisões (32/80 excluídos; 60 pendente) e [[correcoes]] linha 71
- **Tipo:** erro+causa
- **Risco:** alto (código de domínio da DSN)
- **Serviço:** [[design]] / [[research-pipeline]]
- **O que diz:** o mapper de Contract Nature tinha só 9 dos 26 códigos da norma. Dos faltantes, 12 foram corretamente excluídos pelo filtro privado; **53/54 (emprego penitenciário) e 70 (ESAT) eram lacunas reais e entraram**; o código 32 (CAPE) fica excluído (Código de Comércio art. L127-1); o 60 (contrat d'engagement éducatif) segue como decisão aberta do dono do escopo; o 80 (contrat de génération) foi nomeado como regime histórico encerrado (Ordonnance 2017-1387 de 22/09/2017). Na reemissão, o TEST0 D03 conferiu `Country Fields!K32/W32` (Contract Nature) com o cahier technique: PASS.
- **Antes (se erro):** 9/26 códigos; 32, 60 e 80 excluídos sem nome.
- **Causa (se erro):** filtro do regime geral aplicado sem listar cada exclusão.
- **Correto / novo:** 53, 54 e 70 incluídos; 32 e 80 excluídos com fundamento; 60 pendente (decisão do dono).
- **Nível de evidência:** B, fonte A: DSN cahier technique CT2026.1.2 (GIP-MDS/net-entreprises) · **Fonte:** QA v3; Alignment Patch; TEST0
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v3-20260903.md` linha 43; `RAW/qa/FR-ALIGNMENT-PATCH.md` linhas 24–26 (tabela, checks 1); `RAW/qa/FR-TEST0.json` assertion D03
- **Quem decidiu / pediu:** dono do escopo (Wallisson Gomes) para o código 60
- **Destino:** hub (Decisões); skill `payroll-compliance-france`
- **Pergunta para o teste (Conjunto B)?** sim → "Quais códigos de Contract Nature ficaram de fora do DD da FR e por quê?"
- **Confiança da extração:** média
- **Validação:** ◐ conferência independente: código 80 é do mapper S21.G00.40.008, não do Contract Nature; correcoes.md l.71 não trata de 32/60/80; locators patch l.29–30, QA v3 l.44 · humana ⏳

### F6-20261027-FR-C20 · erro+causa · [[Franca]]
- **Chave:** `FR | WTC | FR-046 base CSG/CRDS sem o 23673` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** a fórmula do FR-046 (base da CSG/CRDS) agora nomeia os quatro wage types constituintes (23670, 23671, 23672, 23673); o 23673 (complemento de plano de poupança) faltava e foi confirmado contra quatro fontes externas (não nomeadas no QA). Pertence ao WTC v1.2 (linhagem anterior); se a reemissão manteve a correção não está nos arquivos coletados.
- **Antes (se erro):** FR-046 sem 23673.
- **Causa (se erro):** omissão na lista de wage types da base.
- **Correto / novo:** FR-046 inclui 23670–23673.
- **Nível de evidência:** B · **Fonte:** QA v4
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v4-20260903.md` linhas 19 e 35
- **Quem decidiu / pediu:** —
- **Destino:** hub (Artefatos/Pendências WTC)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (reemissão não verificada)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C21 · erro+causa · [[Franca]]
- **Chave:** `FR | DD | Local Value: Tdelta da RGDU segue o porte (FNAL), não a natureza jurídica` · **Já existe?** não (o hub tem os valores da RGDU)
- **Tipo:** erro+causa (falso positivo da revisão do dev)
- **Risco:** alto (valor estatutário)
- **Serviço:** [[design]]
- **O que diz:** a revisão de prontidão do dev propôs ligar "Employer Legal Nature" ao Tdelta da RGDU; o QA v4 rejeitou: o Tdelta acompanha o porte do empregador (taxa do FNAL), não a natureza jurídica, e o CCG o mostra no exemplo. Outro candidato citava o mapper errado. Foi acrescentada a coluna Local Value ao DD só para o mapper com taxa verificada (Alsace-Moselle, 1,30 %). Valores confirmados no TEST0 C05: Tmin 0,0200; Tdelta 0,3781 (FNAL 0,10 %) ou 0,3821 (FNAL 0,50 %); expoente 1,75; SMIC de referência 21.876,40 (12,02 × 1.820 h, congelado em 2026).
- **Antes (se erro):** proposta de vincular natureza jurídica ao Tdelta.
- **Causa (se erro):** leitura literal do nome do campo.
- **Correto / novo:** não vincular; Tdelta por FNAL (porte). Vigência 2026-01-01, Décret 2026-509 para o SMIC congelado.
- **Nível de evidência:** B, fonte A: URSSAF "La réduction générale des cotisations patronales (RGDU) 2026" (consultada 2026-10-09) · **Fonte:** QA v4; TEST0 C05
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v4-20260903.md` linhas 17 e 32; `RAW/qa/FR-TEST0.json` assertions C05 e C12
- **Quem decidiu / pediu:** QA v4 (Wallisson Gomes)
- **Destino:** hub (Valores-chave RGDU: acrescentar a regra do porte)
- **Pergunta para o teste (Conjunto B)?** sim → "O Tdelta da RGDU depende da natureza jurídica do empregador?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C22 · erro+causa · [[Franca]]
- **Chave:** `FR | CCG | Mod. 12 Ex. 1: verificado com bruto 2.800,00 × reemitido 2.915,50` · **Já existe?** sim → [[Franca]] §Pendências (CCG Mod. 12 Ex. 1, C38; INCERTO do Ex. 1 do FR-pack)
- **Tipo:** erro+causa
- **Risco:** alto (exemplo numérico de pagamento)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o QA v3 achou e corrigiu 6 erros aritméticos nos exemplos dos Módulos 3, 9 e 12 do CCG e deixou o Ex. 1 do Mod. 12 igual ao Payslip: seis números recalculados batem ao centavo (616,44 / 94,06 / 2.089,50 / 954,17 / 3.754,17 e bruto 2.800,00; QA v2). Esse exemplo é o do CCG anterior. O hub registra que o CCG **reemitido** usa bruto 2.915,50 e que o C38 reprova 3 números digitados (0,875970 → 0,875870; 0,235942 → 0,235805; 379,01 → 379,02). **O C38 não aparece em nenhum arquivo coletado em RAW**, então o defeito não é confirmável aqui: a fonte é o hub/`revisoes/2026-10-17`.
- **Antes (se erro):** 6 erros de conta no CCG anterior; 3 números no reemitido (segundo o hub).
- **Causa (se erro):** conta digitada à mão nos exemplos.
- **Correto / novo:** não usar a verificação "ao centavo" do QA v2/v3 como prova do CCG reemitido; decisão do usuário (17/10): só registrar, sem v1.1 (hub).
- **Nível de evidência:** B · **Fonte:** QA v2, v3
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v3-20260903.md` linhas 31–32; `RAW/qa/FR-QA-REPORT-v2-20260902.md` linhas 38–46
- **Quem decidiu / pediu:** usuário (17/10/2026, no hub)
- **Destino:** hub (Pendências: acrescentar que a verificação de agosto/setembro é da CCG anterior)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (qual Ex. 1 está no CCG reemitido; C38 não confirmável no raw)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C23 · erro+causa · [[Franca]]
- **Chave:** `FR | Report Specs | ids belgas em "Similar To" e rótulo de versão do Report Matrix` · **Já existe?** não (parente: [[correcoes]] linha 71, "Description (NL)")
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o "Re-sync 2026-10-09" recopiou as 15 specs depois de dois ajustes de texto na mesma emissão: rótulo de versão do Report Matrix = 1.0 e **ids de documentos belgas removidos de "Similar To"**. Explica por que os md5 das 15 specs diferem da tabela do PROMOTION-LOG (C04). Os arquivos pré-promoção ficam em `04-reports-spec/Archived/2026-10-09-promotion/`.
- **Antes (se erro):** specs reemitidas com ids da BE e rótulo de versão divergente.
- **Causa (se erro):** resíduo de cópia da spec da Bélgica.
- **Correto / novo:** specs v1.0 pós-re-sync = as coletadas.
- **Nível de evidência:** B · **Fonte:** PROMOTION-LOG-2026-10-09
- **Localização no raw:** `RAW/notas/PROMOTION-LOG-2026-10-09.md` linhas 68–70
- **Quem decidiu / pediu:** —
- **Destino:** [[correcoes]] (padrão de resíduo BE) · skill `mercans-pipeline-methodology`
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C24 · erro+causa · [[Franca]]
- **Chave:** `FR | pipeline C29 | 6 "XXX" residuais = BIC de exemplo` · **Já existe?** não
- **Tipo:** erro+causa (provável falso positivo)
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o recheck do audit (`audit_recheck_artifactfix.json`) reprova o C29 (marcadores residuais) por 6 ocorrências de "XXX", todas no exemplo `BNPAFRPPXXX` (Payslip EN/FR, DGFIP-001, DSN-001 ×3); `sanctioned_x_placeholders: 21` mostra que existe lista de exceções. O audit mecânico anterior também reprova C29 (6 ocorrências). Nenhum QA diz que é falso positivo; o código parece um BIC de 11 caracteres (a leitura é minha, nível D).
- **Antes (se erro):** C29 FAIL.
- **Causa (se erro):** o lint trata "XXX" como marcador não substituído.
- **Correto / novo:** pergunta ao usuário: aceitar como falso positivo e liberar "BNPAFRPPXXX" na lista do C29?
- **Nível de evidência:** B (resultado do audit) · **Fonte:** audit_recheck_artifactfix
- **Localização no raw:** `RAW/qa/audit_recheck_artifactfix.json` check `C29` (items 1–6); `RAW/logs/audit_v24_mechanical.json` check `C29`
- **Quem decidiu / pediu:** —
- **Destino:** backlog de lições do pipeline (F6)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (que seja BIC válido; nenhuma fonte de QA)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C25 · erro+causa · [[Franca]]
- **Chave:** `FR | pipeline C20 | "in-scope sem spec" persiste no recheck` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o recheck reprova o C20 ("In-scope without spec": os 15 filings) e passa o C18 ("all 15 in-scope filing(s) declare an existing Spec file"); o `scope_validation` de 2026-09-01 já mostra 15/15 `spec_file` resolvendo e o Stage 9 de 09-02 dá C20 PASS ("15 in-scope, 14 out-of-scope"). O audit mecânico antigo (C18 MANUAL "0/15 declare spec link") reprovava o C20 pelo mesmo motivo antes do manifest v1.1. O recheck não tem data; a causa do C20 FAIL ali não está documentada.
- **Antes (se erro):** C20 FAIL.
- **Causa (se erro):** [INCERTO] (caminho/nome de spec lido em pasta errada?).
- **Correto / novo:** tratar como não resolvido até alguém rodar de novo.
- **Nível de evidência:** B · **Fonte:** audit_recheck_artifactfix; scope_validation; stage9_rerun
- **Localização no raw:** `RAW/qa/audit_recheck_artifactfix.json` checks `C18` e `C20`; `RAW/qa/stage9_rerun_20260902.json` check `C20`; `RAW/qa/scope_validation.md` linhas 36–45
- **Quem decidiu / pediu:** —
- **Destino:** backlog de lições do pipeline (F6)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (causa e data do recheck)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C26 · erro+causa · [[Franca]]
- **Chave:** `FR | Payslip | abas "How to set up Payslip" e "Compliance Payslip": remover ou manter` · **Já existe?** não
- **Tipo:** erro+causa (decisões contraditórias)
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** QA v3 e v4 listam as duas abas como "limpeza cosmética" que o build pedia para remover e não foi feita. O override do C21 (2026-09-02) diz o contrário: são as abas padrão de introdução/guia, presentes **por desenho** desde a build de Moçambique, e a checagem de "5 abas" é que está obsoleta. O Payslip tem 8 abas no hub.
- **Antes (se erro):** QA: remover.
- **Causa (se erro):** regra do prompt de build (5 abas) × padrão real (7–8).
- **Correto / novo:** pergunta ao usuário/dono do padrão; o override documentado (mais antigo) e o QA v4 (mais recente) discordam.
- **Nível de evidência:** B · **Fonte:** QA v3/v4; stage9_rerun
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v3-20260903.md` linha 49; `RAW/qa/FR-QA-REPORT-v4-20260903.md` linha 51; `RAW/qa/stage9_rerun_20260902.json` check `C21` (detail)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências) e padrão do Payslip
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (qual disposição vale)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C27 · erro+causa · [[Franca]]
- **Chave:** `FR | CCG+WTC | Contribuição de diálogo social 0,016 %: só empregador` · **Já existe?** sim → resolve o [INCERTO] de [[Franca]] §Valores-chave ("Diálogo social") e §Pendências
- **Tipo:** erro+causa
- **Risco:** alto (valor estatutário)
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** o hub tem [INCERTO]: CCG M5.1/WTC FR-019 diziam 0,016 % dos dois lados; CCG M3 e Ex. 6 só do ER. Na reemissão, o passo B5 da recompilação da skill (2026-10-06) verifica a **ausência** de "Social dialogue | 0.016 % | 0.016 %" (lado do empregado): OK; o TEST0 C12 (PASS) valida "Social dialogue contribution — (employer only) 0,016 %" contra a página URSSAF "Taux de cotisations – Secteur privé" (consultada 2026-10-09), onde o item aparece na tabela patronal. A citação não diz "somente empregador" em palavras.
- **Antes (se erro):** 0,016 % também no empregado (CCG M5.1, WTC FR-019, linhagem anterior).
- **Causa (se erro):** boilerplate repetido nas células do WTC (queixa F-04 da validação).
- **Correto / novo:** 0,016 % **só empregador**, 2026 (reemissão), fonte URSSAF.
- **Nível de evidência:** B, fonte A: URSSAF taux de cotisations secteur privé · **Fonte:** TEST0 C12; PROMOTION-LOG 06/10 B5
- **Localização no raw:** `RAW/qa/FR-TEST0.json` assertion C12; `RAW/notas/PROMOTION-LOG-2026-10-06.md` linha 80
- **Quem decidiu / pediu:** —
- **Destino:** hub (Valores-chave; fechar o INCERTO)
- **Pergunta para o teste (Conjunto B)?** sim → "A contribuição de diálogo social de 0,016 % é do empregado, do empregador ou dos dois?"
- **Confiança da extração:** média (o lado vem da estrutura da tabela citada e do artefato, não de texto expresso)
- **Validação:** ◐ conferência independente: nível B (TEST0 C12, PROMOTION-LOG 06/10, matriz 17/10 l.59), falta fonte A; não fecha o [INCERTO] do hub · humana ⏳

### F6-20261027-FR-C28 · pendência · [[Franca]]
- **Chave:** `FR | FR-URSSAF-001 | DPAE formato 120: tamanho de registro não verificado` · **Já existe?** parcial → [[Franca]] §Pendências (C_URSSAF/C_APPLICATION); R09 não consta
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o TEST0 (51 afirmações) tem 50 PASS e 1 **UNVERIFIED**: R09, formato 120 do DPAE (989 caracteres + LF = 990 bytes por registro, ISO-8859-1, 24 campos, retornos 10/11/20/41). O site `www2.due.urssaf.fr` não respondeu (conexão reiniciada); o guia da API DPAE confirma só que existem os formatos flat e XML e os códigos de retorno, não o tamanho do registro. Não foi chutado. A spec afirma o valor a partir do runbook P4 (dessin v5.4 com v5.3).
- **Antes (se erro):** —
- **Causa (se erro):** host fora do ar na sessão de 2026-10-09.
- **Correto / novo:** valor **sem verificação independente**; repetir a conferência no PDF `v5.4_FormatDPAE_CFT.pdf`.
- **Nível de evidência:** B · **Fonte:** FR-TEST0 (R09); Version Control da FR-URSSAF-001
- **Localização no raw:** `RAW/qa/FR-TEST0.json` assertion R09 (`result: UNVERIFIED`, `note`); `RAW/version-control/FR-URSSAF-001-DPAE-Spec.md` linha "Format and channel"
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C29 · pendência · [[Franca]]
- **Chave:** `FR | Specs inbound | layouts não obtidos (CPAM-003, CPAM-002/IDAT, DGFIP-002, CARSAT-001, AGIRC-001)` · **Já existe?** não ([[Franca]] só tem "nenhuma spec round-tripped")
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** os Version Control das specs listam o que **não** foi obtido: CPAM-003 (BPIJ): layout das colunas dos exports csv/xls/pdf/xml não publicado (primeiro passo = obter um export real de cliente com subrogação); CPAM-002 (DAT): especificação do serviço eletrônico IDAT, marcada FORMAT TO CONFIRM (a spec cobre o cerfa 14463*03); DGFIP-002 (CRM PAS): layout do registro não obtido, só nível de bloco; CARSAT-001: layout da notificação AT/MP não publicado (pode não existir); AGIRC-001: a ferramenta online não tem layout, XSD nem export. A spec deliberadamente não inventa colunas.
- **Antes (se erro):** —
- **Causa (se erro):** fontes oficiais não publicam o layout.
- **Correto / novo:** tratar esses fluxos como "especificar a partir de amostra real" antes de construir parser.
- **Nível de evidência:** B · **Fonte:** Version Control das specs
- **Localização no raw:** `RAW/version-control/FR-CPAM-003-BPIJ-Spec.md` linhas 23–25; `FR-CPAM-002-AccidentTravail-Spec.md` linhas 23–24; `FR-DGFIP-002-CompteRenduPAS-Spec.md` linha "The honest limit"; `FR-CARSAT-001-NotificationTauxATMP-Spec.md` linha "What was not obtained"; `FR-AGIRC-001-RetourAgircArrco-Spec.md` linha "What is NOT specified here"
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências)
- **Pergunta para o teste (Conjunto B)?** sim → "Existe layout oficial do export do BPIJ / da notificação AT/MP?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C30 · pendência · [[Franca]]
- **Chave:** `FR | Specs | itens abertos "Open item (to confirm with the authority)"` · **Já existe?** parcial → DPAE (C_URSSAF, C_APPLICATION) já em [[Franca]] §Pendências; BPIJ e URSSAF-004 não
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** além dos 2 do DPAE, há 1 item aberto na FR-CPAM-003 (se o BPIJ é recuperável pela API da DSN e se o XSD em XML existe; a fiche net-entreprises a_id 3034 só diz que havia trabalho em curso desde 2021) e 1 na FR-URSSAF-004 (o **sinal** do código 075 e dos CTP 996/997, `S21.G00.23.005`: o CT permite valores negativos e as fontes lidas não dizem).
- **Antes (se erro):** —
- **Causa (se erro):** fontes lidas não cobrem.
- **Correto / novo:** confirmar com a autoridade; até lá, não afirmar o sinal.
- **Nível de evidência:** B · **Fonte:** Version Control das specs
- **Localização no raw:** `RAW/version-control/FR-CPAM-003-BPIJ-Spec.md` linha 25; `RAW/version-control/FR-URSSAF-004-SoldeTaxeApprentissage-Spec.md` linha 24; `RAW/version-control/FR-URSSAF-001-DPAE-Spec.md` linha 25
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C31 · pendência · [[Franca]]
- **Chave:** `FR | FR-DGFIP-003 | abatimento CGI art. 1679 A: 24.041 (2025) × 24.256 (2026)` · **Já existe?** não
- **Tipo:** pendência
- **Risco:** alto (valor estatutário com duas versões)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o formulário 2502-SD guardado nas fontes oficiais é a edição **ANNEE 2025** e imprime o abatimento de 24.041 EUR (2025); a notice 2501-NOT-SD (edição 2026) dá **24.256 EUR para 2026**. A spec traz os **dois** valores (na linha e em Field Options), sem preferir um em silêncio, e manda atualizar quando sair o 2502-SD de 2026. A estrutura de linhas e códigos do formulário é estável; o teto do abatimento é por ano.
- **Antes (se erro):** —
- **Causa (se erro):** o formulário de 2026 ainda não estava publicado.
- **Correto / novo:** abatimento 2026 = 24.256 (notice 2501-NOT-SD 2026, DGFiP) · 2025 = 24.041 (2502-SD 2025); fonte lida só via Version Control da spec (não li a notice).
- **Nível de evidência:** B, fonte A citada: Notice 2501-NOT-SD 2026, DGFiP · **Fonte:** Version Control da FR-DGFIP-003
- **Localização no raw:** `RAW/version-control/FR-DGFIP-003-TaxeSurLesSalaires-Spec.md` linha 23 ("A version gap, stated rather than hidden")
- **Quem decidiu / pediu:** —
- **Destino:** hub (Valores-chave com vigência; Pendências)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual o abatimento da taxe sur les salaires em 2026?"
- **Confiança da extração:** média
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C32 · pendência · [[Franca]]
- **Chave:** `FR | FR-CDC-001 SOLTéA | janela da campanha 2026 (26/05 a 21/10) sem confirmação` · **Já existe?** não
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]] / [[suporte]]
- **O que diz:** a spec chama de "fato mais perecível" as datas da campanha: o CCG Mod. 10 registra a janela 2026 como 26 de maio a 21 de outubro, mas o guia obtido descreve a campanha 2025; as datas mudam todo ano e uma janela perdida não se recupera (o saldo é distribuído pela regra padrão). A obrigação do payroll termina na FR-URSSAF-004 (0,09 % declarado na DSN de abril, código 076); a responsabilidade é um lembrete anual ao cliente.
- **Antes (se erro):** —
- **Causa (se erro):** guia de 2025 usado como base.
- **Correto / novo:** as datas 26/05–21/10/2026 são do CCG (B), **⚠️ sem fonte A** neste lote: não usar sem conferir na plataforma SOLTéA.
- **Nível de evidência:** B · **Fonte:** Version Control da FR-CDC-001
- **Localização no raw:** `RAW/version-control/FR-CDC-001-SOLTeA-Spec.md` linhas 21–22 ("The most perishable fact...", "What payroll actually owes here")
- **Quem decidiu / pediu:** —
- **Destino:** hub (Pendências)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual a janela de alocação do SOLTéA em 2026?" (resposta correta: não confirmada)
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C33 · pendência · [[Franca]]
- **Chave:** `FR | pipeline | stages WTC, Payslip e audit de conteúdo terminaram em erro no log, sem nova execução no pipeline` · **Já existe?** não
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** `wtc.log` e `payslip.log` têm o mesmo conteúdo (md5 `9100585f…`): "Error: Reached max turns (60)"; `audit_content.log` termina "Reached max turns (80)"; `reports.log` está vazio. Os artefatos existem e foram auditados, mas vieram da validação (`fr-research-validation`) e das promoções de 06/09-10, não de nova execução desses stages. Os logs do CCG, DD, skill e QA terminam com resumo de conclusão.
- **Antes (se erro):** —
- **Causa (se erro):** limite de turnos do agente nos stages 5, 7 e do audit de conteúdo.
- **Correto / novo:** não tratar esses logs como prova de conclusão; a prova do WTC/Payslip é o Version Control, o QA v3/v4 e o TEST0.
- **Nível de evidência:** B · **Fonte:** logs do pipeline
- **Localização no raw:** `RAW/logs/wtc.log`, `RAW/logs/payslip.log`, `RAW/logs/audit_content.log`, `RAW/logs/reports.log` (arquivo vazio); md5 em `RAW/MANIFEST-coleta.md` linhas wtc.log e payslip.log
- **Quem decidiu / pediu:** —
- **Destino:** backlog de lições do pipeline (F6)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C34 · pendência · [[Franca]]
- **Chave:** `FR | pipeline C27/C33 | MANUAL nunca fechados (768 mapeamentos; 154 trechos em idioma local)` · **Já existe?** não
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o recheck deixa MANUAL o C27 (768 mapeamentos de spec sem link ao DD ou classe derived/structural; 770 no audit antigo) e o C33 (154 trechos possivelmente em idioma local na prosa do CCG, que o fixer deveria traduzir, regra B10). Convivem com o `ccg.log` ("B10 English-only prose: 0 blocos") e com o Alignment Patch (403 mapeamentos resolvidos e 952 marcados reconciliados com motivo). A divergência (C33 × B10) não foi explicada.
- **Antes (se erro):** —
- **Causa (se erro):** [INCERTO] (heurística do C33 pega termos estatutários franceses mantidos de propósito?)
- **Correto / novo:** abrir o CCG reemitido e conferir amostra.
- **Nível de evidência:** B · **Fonte:** audit_recheck; ccg.log; alignment.log
- **Localização no raw:** `RAW/qa/audit_recheck_artifactfix.json` checks `C27` e `C33`; `RAW/logs/ccg.log` (tabela B10); `RAW/logs/alignment.log` ("column L, 1,357 rows")
- **Quem decidiu / pediu:** —
- **Destino:** backlog de lições do pipeline (F6)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO]
- **Validação:** ◐ conferência independente: causa corrigida: itens do C33 são símbolos de fórmula (non-latin-script), provável falso positivo · humana ⏳

### F6-20261027-FR-C35 · pendência · [[Franca]]
- **Chave:** `FR | DD+WTC | colunas laranja: preencher × deixar vazias` · **Já existe?** sim → contradiz [[Franca]] §Pendências ("Pesquisa: preencher Internal Code no DD ... colunas laranja do WTC") e confirma §Decisões (2026-08-27)
- **Tipo:** pendência (decisão contraditória)
- **Risco:** normal
- **Serviço:** [[design]] / [[research-pipeline]]
- **O que diz:** o QA v4 trata `Internal Code` vazio no DD (173 campos) e as cinco colunas do WTC (In Period Reconciliation, YTD Load, YTD Remarks, Prorating Method, Calculation Type) como **não defeito**: colunas laranja, do time de dev; recomenda esclarecer a convenção com o revisor em vez de preencher. O `dd.log` confirma "20 colunas laranja vazias". A decisão do hub de 2026-08-27 vale a mesma coisa, mas a lista de Pendências pede à Pesquisa preencher. O Version Control do WTC reemitido tem 4 linhas e **não** traz a nota da linha 23 que o QA v4 cita.
- **Antes (se erro):** Pendência do hub: preencher.
- **Causa (se erro):** pendência escrita antes do QA v4.
- **Correto / novo:** B (QA v4) > C (chat): manter vazias; a conversa com o time de dev sobre a propriedade das colunas laranja segue em aberto (usuário). A nota do Version Control do WTC reemitido: [INCERTO] se foi removida.
- **Nível de evidência:** B · **Fonte:** QA v4
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v4-20260903.md` linhas 31–33 e 55; `RAW/logs/dd.log` ("Column discipline exact"); `RAW/version-control/FR-WTC-001-v1.0.md` (4 linhas)
- **Quem decidiu / pediu:** dono do escopo (decisão de 2026-08-27, no hub)
- **Destino:** hub (Pendências → remover o pedido de preenchimento)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média ([INCERTO] quanto à nota do WTC reemitido)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C36 · pendência · [[Franca]]
- **Chave:** `FR | CCG | escopo IDCC: decisão formal` · **Já existe?** sim → fecha [[Franca]] §Pendências ("escopo IDCC") e confirma §Ficha ("IDCC é configuração por cliente")
- **Tipo:** pendência (fechamento)
- **Risco:** normal
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** o QA v4 registra no CCG v1.3 a decisão formal: tabelas de override por convenção coletiva (IDCC) são tarefa de **implementação do cliente**, não da pesquisa base (cerca de 330 convenções ativas, com disposições materialmente diferentes, e sem exposição de reporte estatutário ao adiar). O CCG v1.3 também recuperou uma lista de três itens prometida e nunca entregue (fontes de variação não estatutária). Linhagem anterior; reemissão não verificada. O número "330" é do QA, sem fonte.
- **Antes (se erro):** IDCC "não escopado".
- **Causa (se erro):** —
- **Correto / novo:** IDCC = configuração por cliente (decisão registrada em 2026-09-03).
- **Nível de evidência:** B · **Fonte:** QA v4
- **Localização no raw:** `RAW/qa/FR-QA-REPORT-v4-20260903.md` linhas 18 e 37
- **Quem decidiu / pediu:** Wallisson Gomes (QA v4)
- **Destino:** hub (Decisões; fechar a pendência)
- **Pergunta para o teste (Conjunto B)?** sim → "As convenções coletivas (IDCC) estão cobertas no CCG da FR?"
- **Confiança da extração:** média
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C37 · alerta · [[Franca]]
- **Chave:** `FR | CCG M3.1 | montant net social: regra de 2026 e mudança prevista para 2027` · **Já existe?** não (o hub só lista "payslip novo em 2027-01-01")
- **Tipo:** alerta
- **Risco:** alto (valor estatutário com troca de vigência)
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** o montant net social é linha obrigatória do holerite desde 2023-07-01 e é transmitido na DSN. Em 2026, a parcela patronal de previdência complementar coletiva (L911-1) fica **fora** do cálculo; a rubrica ao vivo do BOSS (atualizada 2026-10-02) já lista a parcela patronal como **incluída**, e a notícia do BOSS de outubro de 2026 diz que isso vale para rendimentos devidos a partir de **2027-01-01**, com base em **projeto** de decreto. O CCG registra isso numa nota datada (P178). O TEST0 C18 manteve a regra de 2026 (PASS).
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** até 2026-12-31: parcela patronal L911-1 excluída; a partir de 2027-01-01 (se o decreto sair como projeto): incluída. Fonte: BOSS (actualité de nov. 2023 e rubrique de 2026-10-02); condição "projeto de decreto".
- **Nível de evidência:** B (TEST0), fonte A citada: BOSS · **Fonte:** FR-TEST0 C18
- **Localização no raw:** `RAW/qa/FR-TEST0.json` assertion C18 (`note`, `source.quote`)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Valores-chave com vigência; Revisões datadas)
- **Pergunta para o teste (Conjunto B)?** sim → "A parcela patronal de prévoyance entra no montant net social em 2026? E em 2027?"
- **Confiança da extração:** média (decreto é projeto)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C38 · alerta · [[Franca]]
- **Chave:** `FR | TEST0 | 50 PASS / 1 UNVERIFIED sobre o pacote reemitido (2026-10-09)` · **Já existe?** não
- **Tipo:** alerta (evidência de qualidade da reemissão)
- **Risco:** alto (base da confiança nos valores da versão vigente)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o Teste 0 de 2026-10-09 sobre o pacote v1.0 reemitido: 51 afirmações com risco (CCG 21, WTC 13, DD 8, Specs 9), cada fonte buscada em 09/10 e citada; 50 PASS, 1 UNVERIFIED (R09, C28). Notas de fonte: a coluna anual do SMIC difere entre o CCG e a fonte (ver C40); o rótulo "Luhn" do SIREN não consta no cahier (não afirmado).
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** a reemissão tem verificação por amostra; as afirmações PASS podem ser usadas com a fonte do TEST0. A amostra não cobre Payslip nem SIR.
- **Nível de evidência:** B · **Fonte:** FR-TEST0.json
- **Localização no raw:** `RAW/qa/FR-TEST0.json` campos `run_date`, `package`, `sampling`, `assertions[*].result`
- **Quem decidiu / pediu:** —
- **Destino:** hub (Situação); skill `payroll-compliance-france`
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C39 · alerta · [[Franca]]
- **Chave:** `FR | CCG+WTC | contribuições 2026 confirmadas no TEST0 (Agirc-Arrco, Apec, Unédic, AGS, CSG/CRDS, COTAM, CPF-CDD, aprendizagem)` · **Já existe?** não ([[Franca]] §Valores-chave não lista estes)
- **Tipo:** alerta (valores com fonte)
- **Risco:** alto (valor estatutário)
- **Serviço:** [[research-pipeline]]
- **O que diz:** valores do CCG reemitido que o TEST0 confirmou (a partir de 2026-01-01; limite 4 PSS = 192.240/ano = 16.020/mês). Colunas: empregado / empregador. Agirc-Arrco T1 3,15 % / 4,72 %; T2 8,64 % / 12,95 %; CEG T1 0,86 % / 1,29 %, T2 1,08 % / 1,62 %; CET 0,14 % / 0,21 %; Apec (cadres, até 4 PSS) 0,024 % / 0,036 %. Seguro-desemprego 4,00 % (empregador, até 4 PSS); AGS 0,25 % (empregador, até 4 PSS). CSG dedutível 6,80 %, não dedutível 2,40 %, CRDS 0,50 %, sobre 98,25 % do bruto até 192.240/ano. COTAM 5,50 % (empregado coberto pela seguridade francesa mas sem domicílio fiscal na França; base do art. L242-1 CSS). CPF-CDD 1 % (CDD, qualquer porte). Taxe d'apprentissage 0,59 % + 0,09 % (saldo) = 0,68 %; formação 0,55 % (<11 empregados) ou 1 % (≥11).
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** como acima, vigência 2026-01-01. Atenção: a Apec foi um erro da validação (8 PMSS no lugar de 4 PSS; matriz `revisoes/2026-10-17`), já corrigido na reemissão.
- **Nível de evidência:** B (TEST0), fonte A citada: URSSAF "Taux de cotisations – Secteur privé" e página CSG/CRDS; Circulaire Agirc-Arrco 2025-16-SG-DRJ (paramètres 2026), consultadas em 2026-10-09 · **Fonte:** idem
- **Localização no raw:** `RAW/qa/FR-TEST0.json` assertions C06, C07, C08, C09, C10, C11, C12, C13, C14, C21, W05, W07, W08; `RAW/qa/FR-TEST0.json` assertion R06 (aprendizagem 0,59 + 0,09)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Valores-chave, com vigência e fonte); skill `payroll-compliance-france` (conferir)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual a alíquota de Agirc-Arrco T1/T2 em 2026, empregado e empregador?" e "Qual a base e o teto da CSG/CRDS?"
- **Confiança da extração:** média (leio a citação do TEST0, não a fonte; CET sem a faixa porque a coluna "32.040" do CCG não é explicada)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-FR-C40 · alerta · [[Franca]]
- **Chave:** `FR | CCG | art. 182 A 2026, IJ de AT/MP e arredondamentos do SMIC anual` · **Já existe?** parcial → [[Franca]] §Valores-chave tem SMIC, RGDU e PAS; não tem 182 A nem a IJ
- **Tipo:** alerta (valores com fonte)
- **Risco:** alto (valor estatutário)
- **Serviço:** [[research-pipeline]]
- **O que diz:** (1) Retenção de não residentes, CGI art. 182 A, rendimentos pagos em 2026: 0 % até 17.275/ano (4.319 tri; 1.440 mês; 332 sem; 55 dia), 12 % de 17.276 a 50.112 (4.320–12.528; 1.441–4.176; 333–964; 56–161) e 20 % acima; nos DOM 12 % e 20 % caem para 8 % e 14,4 %. (2) IJ de acidente do trabalho/doença profissional: 60 % do salário diário nos primeiros 28 dias e 80 % a partir do 29º, sem carência; salário diário = bruto do mês anterior ÷ 30,42. (3) Nota do TEST0: o SMIC anual impresso pela fonte (21.876,64 em 2026-01-01; 22.404,20 em 2026-06-01) não bate com 12 × mensal (21.876,36; 22.404,24) nem com 12,02 × 1.820 (21.876,40, usado na RGDU); o TEST0 conferiu só hora e mês, **não** a coluna anual do CCG M4.1 (T27).
- **Antes (se erro):** —
- **Causa (se erro):** a fonte e o CCG arredondam o anual de modos diferentes.
- **Correto / novo:** não citar o SMIC anual do CCG como verificado; usar hora e mês (12,02/1.823,03 até 2026-05-31; 12,31/1.867,02 desde 2026-06-01).
- **Nível de evidência:** B (TEST0), fonte A citada: BOI-BAREME-000043 de 02/04/2026 (DGFiP); Service-Public F175; Service-Public/DILA (Décret 2026-509) · **Fonte:** idem
- **Localização no raw:** `RAW/qa/FR-TEST0.json` assertions C17, C19, C02 e C03 (`note`)
- **Quem decidiu / pediu:** —
- **Destino:** hub (Valores-chave)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual a escala da retenção do art. 182 A em 2026?"
- **Confiança da extração:** média
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

## Descartados
| Item (ID no inventário) | Motivo |
|---|---|
| Defeitos conhecidos "FR-NSSO" no CCG M10, "BE-NSSO" na Report Matrix das FR-DSN-001/002/003, nota do Payslip citando a Tunísia, formatos do `scope_manifest` (item 3; fonte: memória do pipeline) | Não confirmados em RAW: `grep` por NSSO nos arquivos coletados não acha nenhum; "Tunisia" só aparece no QA v1 comparando a cor do net pay (m-3). O "FR-NSSO" do CCG M10 já é [INCERTO] no hub. Só memória = nível D. Conferir direto nos artefatos num lote 2 |
| CCG C38 (3 números digitados no Ex. 1) (item 3) | Já no hub (Pendências) e em `revisoes/2026-10-17`; não há saída do C38 em RAW. Entra só como contexto no C22 |
| `logs/FACT-CONFLICTS.md/.csv` (item 3) | "PASS, no deterministic conflicts", CSV vazio; nenhuma etiqueta `[[FACT:]]` (C32 aprova sem etiqueta: lacuna L-A já na matriz de 17/10) |
| `qa/c1_result.json`, `qa/c1b_result.json` (178 itens cada) | Pontuação intermediária de casamento CCG × WTC por conceito, sem veredito; ruído de ferramenta (o resultado útil está no QA v1 Check 1) |
| `logs/_pilot_c35/` (7 amostras .txt e 7 .xml) | Amostras de teste do C35 (specs DSN); sem decisão nem valor |
| `logs/si_dgfip-edi.log`, `si_netent-dsn.log`, `si_urssaf-dpae.log`, `si_discover.log`, `sir_index.log` | Conteúdo do SIR/runbooks já no hub (Q1–Q5, DGFIP-EDI Q1–Q7, correções do manifest em [[correcoes]] linha 70); estimativas de esforço (59/50/74 dias-pessoa) são suposição declarada, nível D |
| `qa/scope_validation.md` (C-01, C-02, W1–W3, B7 com 152 linhas) | C-01/C-02/W-01..W-03 já em [[Franca]] §Pendências; o PASS do manifest v1.1 entra como contexto no C14 e C25 |
| `qa/FR-QA-REPORT.md` checks 1, 2, 5, 6, 7, 8 (PASS estruturais: 136/136, 300/300, 15/15, 21 colunas) | Sem impacto na resposta; o resultado de F-1..F-3 e m-1..m-3 está nos cartões C11–C15 |
| `logs/ccg.log`, `logs/dd.log` (resumo de build) | Escopo de regimes especiais no CCG M5 §5.1 e S89/Contract Nature 60 já no hub (Decisões, Pendências); "FR-compliance sem git" é aviso de ferramenta |
| `qa/FR-ALIGNMENT-PATCH.md` (demais linhas: Check 2 sem alteração, 650/650 códigos iguais, 1.357 marcadores `[provisional]`) | Sem erro novo; o "Description (NL)" já está em [[correcoes]] linha 71; o resto é conferência que passou |
| `qa/audit_v3_mechanical.json` e `qa/stage9_rerun_20260902.json` (12/12 e 7/7 PASS) | Usados como contexto em C10, C14 e C26. O 12/12 é um conjunto de checks diferente do C1–C33 do `audit_v24_mechanical` (que tem FAIL em C20/C29); não comparar números |
| `logs/audit_v24_mechanical.json` (14 PASS / 3 MANUAL / 2 FAIL) | Anterior ao manifest v1.1; os mesmos FAIL e MANUAL reaparecem no recheck e estão em C24, C25 e C34 |
| Cartões individuais por Report Spec (14 specs além da DSN-001) (item 3) | Agrupados em C07: Version Control idêntico (`1.0 | 2026-10-06 | Approved`); o md5 por spec está em `RAW/version-control/MANIFEST.md` |
| Notas de QA v1 sobre valores sem fonte A (5,50/11,00/2,75 BIK; 330 convenções) | Sem fonte primária nos arquivos coletados: valor não entra (regra 1); registrados como "sem fonte" em C13 e C36 |
| Excedente para "lote 2" | Nenhum: 40 cartões, no limite |
