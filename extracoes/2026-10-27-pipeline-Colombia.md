# Extração: pipeline Colômbia (2026-10-27)

> Arquivo: `extracoes/2026-10-27-pipeline-Colombia.md`. Um cartão por item. Só entra o que muda a resposta certa.
> Material bruto: `raw/pipeline/Colombia/2026-10-27/` (qa/, logs/, version-control/) + `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` · Inventário: `inventarios/pipeline.md` (linha 2) · Padrão: [[PLANO]] §4 (níveis A/B/C/D) e §5 (validação, lotes de até 40).
> Regra de leitura: as versões do pipeline (CCG v1.2, WTC v1.4, DD v1.0, specs v1.4–v1.6) são **históricas**. A vigente está no hub [[Colombia]] (CCG v1.4, WTC v1.6, DD v1.3, 7 specs, SIR v1.1). Cada cartão de versão registra a divergência; nenhum trata a versão do pipeline como vigente.
> Verificação adicional (só leitura, fora do `raw/`): arquivos de `Research Pipeline/Colombia/` e do Drive `G:\...\Colombia\` foram abertos para checar se o trabalho posterior ao pipeline fechou cada ponto. Esses locais vêm marcados como "Verificação adicional" na Localização.
> Datas internas dos relatórios (não são a data da coleta): scope_validation 2026-09-04; CO-ALIGNMENT-PATCH 2026-09-07; CO-QA-REPORT e handover_status 2026-09-07; CO-PAYSLIP-VERIFICATION 2026-07-12 (anterior ao build de setembro e à decisão do Conselho de Estado de 9-jul, ver C21); os arquivos têm mtime 2026-09-18.

## Resumo
- Itens do inventário neste lote: 1 (linha 2, `CO-compliance/`) · Cartões: 32 (12 versão final, 8 erro+causa, 12 pendência) · Complementos de cartão existente: 22 (19 "sim" + 3 "parcial") · Descartados: 19 linhas (+ 1 linha de lote 2)
- Risco alto: 12 (100% vão para validação) · Amostra dos demais: 2 de 20 (10%)
- Validação: ⏳ pendente
- Ingestão: ✅ feita em 2026-10-27 (hub; correcoes pela janela geral)
- [INCERTO]: 8 cartões (C16, C21, C24, C25, C27, C28, C31, C32; motivo em cada um).

## Cartões

### F6-20261027-CO-C01 · versão final · [[Colombia]]
- **Chave:** `CO | CCG | versão vigente e histórico` · **Já existe?** sim → complementa hub §Artefatos entregues (linhas "CO-CCG-001 v1.4" e "(histórico) v1.2") e [[correcoes]] 2026-10-13 (linhagem errada)
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o pipeline guarda dois arquivos. `CO-CCG-001-v1.1.docx` (2026-09-24) tem Version Control só com a linha 1.0 (3-set-2026, build inicial, 13 módulos). `CO-CCG-001-v1.2.docx` (2026-10-13) tem 1.0 e 1.1 (5-out-2026, FSP corrigido, Law 100 art. 27 / Law 797 art. 8) e uma linha em branco; **não tem linha 1.2**. Portanto o "v1.1" do nome do arquivo de 24/09 não é o "1.1" do Version Control (que é da linhagem do Drive, 5/10), e o "v1.2" do pipeline não está registrado no próprio arquivo. A vigente é a **v1.4** (Google Doc, 26/10); o monday mostra só o rótulo "CCG" (atualizado 2026-10-26), sem número.
- **Antes (se erro):** —
- **Causa (se erro):** nome de arquivo e Version Control seguem numerações diferentes (pipeline × Drive).
- **Correto / novo:** vigente = CCG v1.4 a partir de 2026-10-26 (hub). Histórico para o hub: 1.0 (pipeline, 3-set); 1.1 (Drive, 5-out); arquivo "v1.2" (pipeline, 13-out, sem linha no VC); v1.3 (21-out); v1.4 (26-out).
- **Nível de evidência:** B · **Fonte:** Version Control extraído dos dois arquivos + `MANIFEST.md` (md5 e686fa7b… e 428069b1…) + monday + hub
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-CCG-001-v1.2.md` (tabela de 4 linhas); `.../CO-CCG-001-v1.1.md` (tabela de 2 linhas); `.../version-control/MANIFEST.md` (linhas CO-CCG-001-v1.1 e v1.2); `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` seção "Colombia - CO", item Country Payroll Regulations Guide. Verificação adicional: `ls` de `G:\...\Colombia\05 - Payroll Regulation Guide` em 2026-10-27 mostra, além do `_v1.4.gdoc`, `CO-CCG-001-v1.docx` (05/10), `CO-CCG-001-v1.0.gdoc` (24/09) e `CO-CCG-001-v1.gdoc` (13/10) na raiz.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues: acrescentar o histórico de versões); o resto da pasta do Drive vai para "revisa o cérebro"
- **Pergunta para o teste (Conjunto B)?** sim → "Qual é a versão vigente do CCG da Colômbia e onde está?" (v1.4, Google Doc em `05 - Payroll Regulation Guide`, a partir de 26/10/2026)
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C02 · versão final · [[Colombia]]
- **Chave:** `CO | WTC | versão vigente e histórico` · **Já existe?** sim → complementa hub §Artefatos entregues (linhas "CO-WTC-001 v1.6" e "(histórico) v1.4")
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** duas linhagens de Version Control. (a) Pipeline `CO-WTC-001-v1.1.xlsx` (mtime 2026-09-24, md5 c120b884…): linhas 1 (2026-09-04, Released, 300 códigos globais + 102 da Colômbia), 2 (09-18, "Corrected": resíduo do template tcheco, MINOR-01), 3 (09-18, HRBS-12487: linha 317 prima de férias extralegal), 4 (09-18, MINOR-01/MINOR-09). (b) Pipeline `CO-WTC-001-v1.4.xlsx` (13/10, md5 69a9904d…), da linhagem do Drive: 1 (2026-09-24, Approved), 1.2 (5/10, Draft), 1.3 (5/10, Approved), 1.4 (13/10, Draft). A linhagem do Drive **reinicia** em "1.0 | 2026-09-24" e não herda as linhas 2–4 do pipeline. No arquivo vigente v1.6 (lido por mim), 1.0 e 1.3 estão "Approved" e 1.2, 1.4, 1.5 e 1.6 estão "Draft": a vigência de 1.4–1.6 vem do Drive/hub, não do status do Version Control.
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** vigente = WTC v1.6 a partir de 2026-10-26 (hub). A v1.4 do pipeline e a "v1.1" são histórico. Monday: rótulo "WTC" (item grafado "Wage Type Catelogue"), sem número, Done 2026-10-26.
- **Nível de evidência:** B · **Fonte:** Version Control dos 2 arquivos + `MANIFEST.md` + hub
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-WTC-001-v1.1.md` (aba Version Control, linhas 1–4); `.../CO-WTC-001-v1.4.md` (linhas 1, 1.2, 1.3, 1.4, coluna Status); `.../MANIFEST.md`; `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` item Wage Type Catelogue. Verificação adicional: `Research Pipeline/Colombia/2026-10-22-auditoria-lote1/CO-WTC-001-v1.6.xlsx`, aba Version Control; `ls` de `G:\...\03 - WTC` (ainda há `CO-WTC-001-v1.xlsx` de 05/10 e `CO-WTC-001_v1.4.xlsx` de 13/10 na raiz ao lado do `_v1.6.gsheet`).
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues: histórico de versões e o aviso de status "Draft" no Version Control das versões vigentes)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C03 · versão final · [[Colombia]]
- **Chave:** `CO | DD | versão vigente e histórico` · **Já existe?** sim → complementa hub §Artefatos entregues (linha "CO-DD-001 v1.3")
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** `CO-DD-001-v1.0.xlsx` (mtime 2026-09-24, md5 7c10b54c…) tem nome v1.0 mas o Version Control vai até **1.1** (2026-09-07, "DD↔SPEC ALIGNMENT PATCH", Released). Linha 1: 2026-09-04, Released. A vigente é a **v1.3** (Google Sheet, 26/10). Monday: rótulo "DD" (atualizado 2026-10-26), sem número.
- **Antes (se erro):** —
- **Causa (se erro):** o nome do arquivo não acompanha o Version Control.
- **Correto / novo:** vigente = DD v1.3 a partir de 2026-10-26 (hub). A "v1.0" do pipeline é, na verdade, a v1.1 do patch de alinhamento; histórico.
- **Nível de evidência:** B · **Fonte:** Version Control do arquivo + `MANIFEST.md` + hub
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-DD-001-v1.0.md` (aba Version Control, linhas 1 e 1.1); `.../MANIFEST.md` (linha CO-DD-001-v1.0); `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` item Data Dictionary.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues: histórico)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C04 · versão final · [[Colombia]]
- **Chave:** `CO | SIR-INDEX | versão e nome` · **Já existe?** parcial → complementa hub §Situação (cita "SIR v1.1") e [[correcoes]] / Pendências ("Achados da Cinthya", Res. 13 → 227); não há linha do SIR em §Artefatos entregues
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** pipeline: `CO-SIR-INDEX-001-v1.0.docx` (mtime 2026-09-29, md5 f6923730…), Version Control "v1.0 | 2026-09-04 | Initial issue". No Drive e no monday o documento vigente tem outro nome: **`CO-SIR-001-v1.1`** (Google Doc, 21/10, Res. 13/2021 → 227/2025 aplicada; monday atualizado 2026-10-22). O QA do pipeline disse que **não existe** "CO-SIR-001…007"; o nome "CO-SIR-001" é o rótulo atual do Drive. Hoje convivem os dois nomes.
- **Antes (se erro):** —
- **Causa (se erro):** renomeação no Drive sem registro no pipeline.
- **Correto / novo:** vigente = SIR v1.1 (Google Doc `CO-SIR-001-v1.1`, a partir de 2026-10-21); `CO-SIR-INDEX-001-v1.0` = histórico/base.
- **Nível de evidência:** B · **Fonte:** Version Control + monday + Drive (listagem)
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-SIR-INDEX-001-v1.0.md` (tabela de 2 linhas); `raw/monday/2026-10-27-artifacts-BE-CO-FR.md` seção Colombia, item Statutory Integration (rótulo CO-SIR-001-v1.1); `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` MAJOR-03 (linhas 394–399). Verificação adicional: `ls` de `G:\...\19 - Staturory Integration` (contém `CO-SIR-001-v1.1.gdoc` 21/10 e `CO-SIR-INDEX-001-v1.0.docx` 29/09); `Research Pipeline/Colombia/co-report-crosscheck/04-output/SIR-RES227-2026-10-21.md`.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues: linha nova do SIR com os dois nomes)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C05 · versão final · [[Colombia]]
- **Chave:** `CO | CO-DIAN-001 NominaElectronica Spec | versão` · **Já existe?** sim → complementa hub §Artefatos entregues (linha "Report Specs (7) … 1.0 (linha única)")
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o arquivo do pipeline se chama `…-Spec-v1.6.xlsx` (2026-09-24, md5 7e7a2f3b…), mas o Version Control tem **uma linha só**: `v1.0 | 2026-09-04 | Issued`. O QA e o patch de alinhamento dizem que cada spec recebeu linha v1.1 (2026-09-07); essa linha **não aparece** no arquivo coletado. O sufixo v1.6 do nome não tem registro. QA original: 225 linhas de campo na aba de spec. Vigente: spec com Version Control "1.0" (linha única, padrão do kit), no Drive `17 - Statutory Report`, 26/10, com as correções posteriores (M183 em 22/10, M89/M161 em 26/10, [[correcoes]]).
- **Antes (se erro):** —
- **Causa (se erro):** sufixo do arquivo sem registro no Version Control.
- **Correto / novo:** não citar "v1.6" como versão da spec; a versão é a do Version Control (1.0, linha única) e a vigente é a de 26/10 no Drive.
- **Nível de evidência:** B · **Fonte:** Version Control + `MANIFEST.md` + hub
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-DIAN-001-NominaElectronica-Spec-v1.6.md` (aba Version Control, 1 linha); `.../MANIFEST.md`; `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` Check 7 (linha 250) e Check 4 (linhas 180–181); `raw/pipeline/Colombia/2026-10-27/qa/CO-ALIGNMENT-PATCH.md` linhas 6–16.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues, observação de histórico)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (o sentido do sufixo v1.4–v1.6 no nome do arquivo não está documentado no raw)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C06 · versão final · [[Colombia]]
- **Chave:** `CO | CO-DIAN-002 Formulario350 Spec | versão` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** arquivo `…-Spec-v1.4.xlsx` (2026-09-24, md5 4a314c68…); Version Control com linha única `v1.0 | 2026-09-04 | Issued`; sem a linha v1.1 que o QA diz existir. QA original: 69 linhas de campo, 26 âmbar, 20 azuis, 13 vermelhas, 7 cinza (usa 4 das 5 cores). Vigente: spec com Version Control "1.0", Drive 26/10, com o ajuste do lote 1 (C40: PILA tipo N/E/M, [[correcoes]] 2026-10-22).
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** a versão é a do Version Control (1.0); não usar o sufixo v1.4 do nome.
- **Nível de evidência:** B · **Fonte:** Version Control + `MANIFEST.md` + hub
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-DIAN-002-Formulario350-Spec-v1.4.md` (1 linha); `.../MANIFEST.md`; `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` Check 7 (linha 251).
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (sufixo sem registro)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C07 · versão final · [[Colombia]]
- **Chave:** `CO | CO-DIAN-004 Formulario220 Spec | versão` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** arquivo `…-Spec-v1.4.xlsx` (2026-09-24, md5 ba32a14a…); Version Control com linha única `v1.0 | 2026-09-04 | Issued`. QA original: 75 linhas de campo. O patch de alinhamento criou a série do número do certificado (casilla 4: AAAA-NNNNNN, desenho Mercans, porque a DIAN não prescreve formato), que continua na spec final (`05-final`). Vigente: Drive 26/10, Version Control "1.0".
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** versão = Version Control (1.0); sufixo v1.4 do nome sem registro.
- **Nível de evidência:** B · **Fonte:** Version Control + `MANIFEST.md` + hub
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-DIAN-004-Formulario220-Spec-v1.4.md` (1 linha); `.../MANIFEST.md`; `raw/pipeline/Colombia/2026-10-27/qa/CO-ALIGNMENT-PATCH.md` linhas 130–138 (Check 5). Verificação adicional: `Research Pipeline/Colombia/co-report-crosscheck/05-final/CO-DIAN-004-Formulario220-Spec.xlsx`, aba "Formulario 220 Spec", linha 4.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (sufixo sem registro)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C08 · versão final · [[Colombia]]
- **Chave:** `CO | CO-DIAN-005 Formato2276 Spec | versão` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** arquivo `…-Spec-v1.4.xlsx` (2026-09-24, md5 290b2f18…); Version Control com linha única `v1.0 | 2026-09-04 | Issued`. QA original: 50 linhas de campo, layout XML marcado como DERIVED (ver C28). Vigente: Drive 26/10, Version Control "1.0", com M32/M33 corrigidos (lote 1, 22/10).
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** versão = Version Control (1.0); sufixo do nome sem registro.
- **Nível de evidência:** B · **Fonte:** Version Control + `MANIFEST.md` + hub
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-DIAN-005-Formato2276-Spec-v1.4.md` (1 linha); `.../MANIFEST.md`; `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` Check 7 (linhas 253 e 265–267).
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (sufixo sem registro)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C09 · versão final · [[Colombia]]
- **Chave:** `CO | CO-PILA-003 AportesSeguridadSocial Spec | versão` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs)
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** arquivo `…-Spec-v1.5.xlsx` (2026-09-24, md5 1fe1948f…); Version Control com linha única `v1.0 | 2026-09-04 | Issued`. QA original: 170 linhas de campo, marcada PRIMARY/BYTE-EXACT (A1 = 34 campos/567 posições; A2R1 = 22/359; A2R2 = 97/686), com base no Anexo Técnico 2 **versão 09** (ver C16). **CO-PILA-007** (pensionados) não existe no pipeline; nasceu em 21–22/10 (hub). Vigente: Drive 26/10, Version Control "1.0".
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** versão = Version Control (1.0); a PILA-003 do pipeline é a base, e a PILA-007 só existe do trabalho posterior.
- **Nível de evidência:** B · **Fonte:** Version Control + `MANIFEST.md` + hub
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-PILA-003-AportesSeguridadSocial-Spec-v1.5.md` (1 linha); `.../MANIFEST.md`; `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` Check 7 (linha 252 e 264–265).
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (sufixo sem registro)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C10 · versão final · [[Colombia]]
- **Chave:** `CO | CO-CESANTIAS-006 ConsignacionAnual Spec | versão` · **Já existe?** sim → complementa hub §Artefatos entregues (Report Specs) e [[correcoes]] 2026-10-23
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** arquivo `…-Spec-v1.4.xlsx` (2026-09-24, md5 b5b182fd…); Version Control com linha única `v1.0 | 2026-09-04 | Issued`. QA original: 52 linhas de campo, **incluía o bloco do adiantamento mensal de cesantías (MA01–MA05)**, removido em 23/10 (ver C20). Vigente: Drive 26/10, Version Control "1.0".
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** versão = Version Control (1.0); a spec do pipeline é histórica (com MA01–MA05).
- **Nível de evidência:** B · **Fonte:** Version Control + `MANIFEST.md` + hub
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-CESANTIAS-006-ConsignacionAnual-Spec-v1.4.md` (1 linha); `.../MANIFEST.md`; `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` Check 7 (linha 255).
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (sufixo sem registro)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C11 · versão final · [[Colombia]]
- **Chave:** `CO | Payslip Generator | versão e local` · **Já existe?** não (o hub não tem linha do Payslip em §Artefatos entregues; só cita o `06-payslip.md` da skill na ficha)
- **Tipo:** versão final
- **Risco:** alto (versão vigente de um artefato que não está no hub)
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** o `MANIFEST.md` lista `CO_Compliance_Payslip_Generator-v1.1.xlsx` (2026-09-18, md5 32ded04f…) e marca **"VC encontrado: não"**: a planilha **não tem Version Control**. No pipeline existem dois arquivos: `CO_Compliance_Payslip_Generator.xlsx` (md5 e82f51ee…, o que o QA de 7-set revisou, com 54 células "XXXXX") e `…-v1.1-DRAFT.xlsx` (md5 32ded04f…). Verifiquei que o arquivo do Drive `18 - Payslip\CO_Compliance_Payslip_Generator.xlsx` (2026-09-24) tem **o mesmo md5 32ded04f…** da v1.1-DRAFT. Ou seja, o que está no Drive é o "v1.1 DRAFT" sem Version Control; o `.gsheet` da mesma pasta é de 14/07. O monday não tem item de Payslip para a Colômbia.
- **Antes (se erro):** —
- **Causa (se erro):** o Payslip Generator é copiado do modelo da Espanha, que não leva aba de Version Control.
- **Correto / novo:** registrar no hub: Payslip Generator CO = v1.1 DRAFT (2026-09-18 no pipeline; Drive 2026-09-24, md5 32ded04f…), sem Version Control; não achei registro de trabalho posterior a 24/09 no hub, no `log.md` nem no `ESTADO.md`.
- **Nível de evidência:** B · **Fonte:** `MANIFEST.md` + comparação de md5 feita nesta extração
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/MANIFEST.md` (última linha, "VC encontrado: não"); `raw/pipeline/Colombia/2026-10-27/MANIFEST-coleta.md` (pasta payslip não listada; só QA/logs). Verificação adicional (só leitura): `md5sum` de `G:\Drives compartilhados\Compliance Team\Country Folders\Colombia\18 - Payslip\CO_Compliance_Payslip_Generator.xlsx` = `Research Pipeline/Colombia/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator-v1.1-DRAFT.xlsx`.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues: linha nova) + pergunta à frente pipeline se o Drive é o final
- **Pergunta para o teste (Conjunto B)?** sim → "Existe Payslip Generator da Colômbia? Qual versão e onde?"
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C12 · versão final · [[Colombia]]
- **Chave:** `CO | Skill (Stage 11) | co-compliance × payroll-compliance-colombia` · **Já existe?** parcial → complementa hub §Ficha do país (data de leitura da skill 2026-10-02) e Pendências ("skill instalar/atualizar (#17)")
- **Tipo:** versão final
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o pipeline compilou uma skill própria, `08-skill/co-compliance/` (SKILL.md de 7.596 bytes + 7 arquivos em `references/`, todos de 2026-09-18), a partir dos artefatos v1.0 e do QA de 7-set (94/100). Não é a `payroll-compliance-colombia` lida na ficha (pesquisa de 2026-08-27, lida em 2026-10-02): são duas skills diferentes. Pela regra do Passo 3 ("atualizar a ficha só se a skill compilada for mais nova que a data de leitura"), 2026-09-18 < 2026-10-02: **a ficha não muda por causa dela**. Ao mesmo tempo, as referências da skill do pipeline carregam texto depois corrigido (adiantamento mensal de cesantías, ver C20; incapacidades/ARL de 13/10; denominador dos 40% de 26/10). O `handover_status.md` de 7-set diz "08-skill vazio"; o `skill.log` mostra que as referências foram escritas e o SKILL.md veio depois.
- **Antes (se erro):** —
- **Causa (se erro):** —
- **Correto / novo:** não usar `co-compliance` do pipeline como fonte; vale o CCG/WTC/DD vigentes e a skill instalada, atualizada depois do fechamento (hub #17).
- **Nível de evidência:** B · **Fonte:** `skill.log` + `handover_status.md`
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/logs/skill.log` (últimas ~20 linhas: tabela de verificação e "What I wrote"); `raw/pipeline/Colombia/2026-10-27/qa/handover_status.md` linhas 335–337. Verificação adicional: `Research Pipeline/Colombia/CO-compliance/08-skill/co-compliance/` (datas de arquivo e contagem de "advance deposit" nas referências).
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Pendências: o item #17 passa a dizer que existe uma skill gerada pelo pipeline, obsoleta)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (conteúdo das referências só amostrado por contagem de termos)
- **Validação:** ◐ conferência independente: a "regra do Passo 3" não está em PLANO/inventário/ESTADO; é critério do extrator · humana ⏳

### F6-20261027-CO-C13 · erro+causa · [[Colombia]]
- **Chave:** `CO | Payslip | XXXXX, CUNE/QR e base das férias (MAJOR-01, MAJOR-02, MINOR-05)` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** alto (correção de erro em artefato; o QA exigia estes ajustes para "READY FOR DEV TEAM")
- **Serviço:** [[research-pipeline]]
- **O que diz:** o QA de 7-set deu "NEEDS PATCHES" ao Payslip por três pontos. Verifiquei no arquivo que está no Drive (md5 32ded04f…, ver C11) que foram tratados na v1.1 DRAFT, com um resíduo.
- **Antes (se erro):** (1) MAJOR-01: 36 células "XXXXX" nas abas `Colombia (EN)` e `(ES)` (linhas 21–24, 28–31, 38–43, 48–51), sem ligação com o WTC; (2) MAJOR-02: nenhum CUNE, data de geração, data de pagamento, prefixo/consecutivo ou QR (Res. DIAN 000013/2021 art. 5 e Anexo §13.1); (3) MINOR-05: provisão de férias `=ROUND(SUM($H$21:$H$23)*0.0417,0)` incluía a linha agrupada de horas extras.
- **Causa (se erro):** o Payslip nasceu como clone do modelo da Espanha, sem arquivo WTC da Colômbia disponível ("No CO-WTC file available", códigos ilustrativos) e sem os itens do art. 5.
- **Correto / novo:** na v1.1 DRAFT, `Colombia (EN)` traz códigos reais do WTC (ex.: CO-SALARIO-BASICO, CO-DED-SALUD, CO-RETENCION-FUENTE, CO-ER-SALUD, CO-PROV-CESANTIAS), CUNE (A11), Generation Date (A12), QR Code Reference (A13) e "Prefix / Consecutive" (G11); a provisão de férias passou a `=ROUND((H26+H28+H29)*0.0417,0)` (sem horas extras nem auxílio de transporte) e a provisão da prima (H56) usa `SUM(H26:H30)`. **Resíduo:** 18 células "XXXXX" nas duas abas genéricas ("How to set up Payslip", "Compliance Payslip") e o texto "[VERIFY WITH RA – illustrative placeholder]" com séries de contas ilustrativas em "Payslip Spec" (D33–D58) e "Unit Rate Details" (G2). Não conferi data/período de pagamento na aba EN.
- **Nível de evidência:** B · **Fonte:** CO-QA-REPORT MAJOR-01/02, MINOR-05 + leitura direta do xlsx do Drive (nesta extração)
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` MAJOR-01 (linhas 322–338), MAJOR-02 (342–378), MINOR-05 (452–459); `raw/pipeline/Colombia/2026-10-27/logs/payslip_batch.log` itens 3 e 4 ("Wage-type codes: illustrative placeholders"; "[VERIFY WITH RA] items"). Verificação adicional: `G:\...\Colombia\18 - Payslip\CO_Compliance_Payslip_Generator.xlsx` (openpyxl, só leitura), `Colombia (EN)` A11–A13, A26–A57, H56–H57.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Artefatos entregues, linha do Payslip) e [[correcoes]] só se a frente pipeline confirmar que o QA pedia estes ajustes
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (a correção foi inferida da comparação v1.0 × v1.1 DRAFT; nenhum registro no raw diz quem a fez nem quando)
- **Validação:** ◐ conferência independente: o veredito "NEEDS PATCHES" é do pacote inteiro; para o Payslip o QA diz "PASS WITH PATCHES"; as 3 correções são parte dos ajustes exigidos para "READY FOR DEV TEAM" · humana ⏳

### F6-20261027-CO-C14 · erro+causa · [[Colombia]]
- **Chave:** `CO | CCG | Módulo 10, nota de escopo CO-RPT-001…007 / CO-SIR-001…007 (MAJOR-03)` · **Já existe?** não em [[correcoes]]; fechado no CCG v1.3 (`CONFERENCIA-CCG.md`)
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o CCG v1.0 mandava o time de desenvolvimento procurar "CO-RPT-001 a CO-RPT-007" e "CO-SIR-001 a CO-SIR-007"; a tabela 10.1 listava CO-RPT-007 sem marca de fora de escopo.
- **Antes (se erro):** CCG v1.0, Módulo 10 (`m10_reporting.md` linhas 5–8, 116): faixas inexistentes.
- **Causa (se erro):** "007" parece erro de transcrição das 7 fases (P1–P7) do runbook do DIAN-NE; CO-RPT-007 (relatório de contratação de pessoas com deficiência, MinTrabajo) foi descartado como escopo de RH, então nunca teve spec.
- **Correto / novo:** a CCG v1.3 trocou os IDs da tabela 10.1 por CO-DIAN-001, CO-DIAN-002, CO-PILA-003, CO-DIAN-004, CO-DIAN-005, CO-CESANTIAS-006, e CO-RPT-007 por "None (out of scope)"; a segunda inserção (CO-SIR-INDEX-001, DIAN-NE P1–P7) ficou. Resolvido a partir de 2026-10-21. Resta conferir se a CCG v1.4 usa o nome atual do Drive para o SIR (`CO-SIR-001-v1.1`, C04).
- **Nível de evidência:** B · **Fonte:** CO-QA-REPORT MAJOR-03 + `CONFERENCIA-CCG.md`
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` MAJOR-03 (linhas 382–408) e Check 3 (146–148). Verificação adicional: `Research Pipeline/Colombia/2026-10-21-alinhamento-CCG/CONFERENCIA-CCG.md` linhas 109 (S82) e 178.
- **Quem decidiu / pediu:** —
- **Destino:** hub §Correções ligadas (uma linha); sem entrada em [[correcoes]] (já corrigido na origem)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C15 · erro+causa · [[Colombia]]
- **Chave:** `CO | CCG × WTC | gratificação ocasional e plano de saúde pré-pago do empregador × trava de 40%` · **Já existe?** não (complementa [[correcoes]] 2026-10-26, que trata do denominador e dos "pactados", sem citar estas linhas)
- **Tipo:** erro+causa
- **Risco:** alto (regra estatutária; artefatos vigentes se contradizem)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o QA de 7-set (MINOR-04) mandou corrigir o CCG 4.6 para "Only above the 40% clamp" nas linhas "Occasional gratuity" e "Employer-paid prepaid health premium", considerando o WTC "mais preciso". Depois, o WTC v1.2 (5/10, SU 25185/2021) reclassificou a gratificação ocasional (mera liberalidad) como **Non-Salary – non-remunerative**, com todas as colunas de IBC = No, **fora** da trava (a trava vale só para os pactados; decisão #56/#57, 26/10). O CCG v1.4 que está no Drive ainda diz "Only above the 40% clamp" para "Occasional gratuity". Li o WTC v1.6: linha 318 = No em saúde, FSP, ARL, parafiscais, pensão; linha 348 (plano de saúde do empregador) = Yes/No e "Non-Salary – pacted".
- **Antes (se erro):** CCG 4.6 v1.0: CB = "No" fixo para as duas linhas (QA); CCG v1.4: "Only above the 40% clamp" para a gratificação ocasional (lido por mim no docx).
- **Causa (se erro):** o QA validou o CCG contra o WTC v1.0 e o WTC mudou depois (SU 25185), sem propagar para a tabela do CCG.
- **Correto / novo:** gratificação ocasional (não pactada) fica fora da trava e fora do IBC, como no WTC v1.6 linha 318; plano de saúde pactado entra na trava. A tabela 4.6 do CCG v1.4 precisa seguir o WTC. Fontes a registrar como A: SU 25185/2021 regra 3 e UGPP ABC Empleadores 2025 p. 5 (já citadas em [[correcoes]] 2026-10-26).
- **Nível de evidência:** B (arquivos) · A pendente de leitura nesta extração · **Fonte:** CO-QA-REPORT MINOR-04; WTC v1.6 linha 318; CCG v1.4 tabela 4.6
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` MINOR-04 (linhas 441–450); `raw/pipeline/Colombia/2026-10-27/version-control/CO-WTC-001-v1.4.md` linha 1.2 (linha 318 reclassificada). Verificação adicional: `Research Pipeline/Colombia/2026-10-22-auditoria-lote1/CO-WTC-001-v1.6.xlsx` (aba Wage Type Catalogue, linhas 318 e 348) e `.../CO-CCG-001-v1.4.docx` (tabelas do Módulo 4.6, linhas "Occasional gratuity" e "Employer-paid prepaid health premium").
- **Quem decidiu / pediu:** —
- **Destino:** [[correcoes]] (complemento de 2026-10-26) + pedir à frente pipeline para alinhar o CCG v1.4 ao WTC v1.6
- **Pergunta para o teste (Conjunto B)?** sim → "A gratificação ocasional (mera liberalidad) entra na trava de 40% da Ley 1393 art. 30?" (não; fora do IBC e fora da trava, WTC v1.6 linha 318)
- **Confiança da extração:** média (a conclusão depende de gratificação ocasional ser "não pactada"; fonte A não relida aqui)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C16 · erro+causa · [[Colombia]]
- **Chave:** `CO | CO-PILA-003 e DD | tabelas PILA baseadas no Anexo Técnico 2 versão 09` · **Já existe?** sim → complementa [[correcoes]] 2026-10-22 (PILA tipo M, aprendizes 12/19) e 2026-10-23 (citações em espanhol)
- **Tipo:** erro+causa
- **Risco:** alto (formato de filing; correção de erro)
- **Serviço:** [[research-pipeline]]
- **O que diz:** o patch de alinhamento de 7-set montou as tabelas de código da PILA (tipo de documento CC/CE/TI/PA/CD/SC/RC/PE, Worker Sub-Type, administradoras, correção N/M) com o **Anexo Técnico 2 da Res. MSPS 2388/2016, versão 09 de 16-09-2019**. O lote 1 de 22/10 usou a **versão 30** e achou erros de regra (tipo N, tipo M só antes do período de saúde de março/2014, aprendizes 12/19). O "newest-law check" (C2) do QA só testou lei (Ley 2381), não a versão do anexo.
- **Antes (se erro):** specs e DD de setembro apoiados no AT2 v09.
- **Causa (se erro):** fonte desatualizada (versão do anexo em vez da vigente) e QA que não confere a versão do anexo.
- **Correto / novo:** fonte vigente = AT2 v30 (lote 1, [[correcoes]] 2026-10-22). Não confirmado no raw se as demais tabelas derivadas do v09 foram relidas contra o v30 (tipo de documento, Sub-Type, padrões `^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$`); o lote 2 (229 edições, 23/10) pode ter coberto.
- **Nível de evidência:** B · **Fonte:** CO-ALIGNMENT-PATCH + `CONFERENCIA.md` do lote 1
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-ALIGNMENT-PATCH.md` linhas 26–31 (fontes), 42 (Check 1, mapper PILA/Cesantías), 119 (Check 4, campo 3 verbatim). Verificação adicional: `Research Pipeline/Colombia/2026-10-22-auditoria-lote1/CONFERENCIA.md` (linhas da tabela, "AT2 v30").
- **Quem decidiu / pediu:** —
- **Destino:** [[correcoes]] (complemento) + lição de processo: conferir a versão do anexo técnico antes de fechar tabela de códigos
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (não dá para saber, só pelo raw, se as tabelas de documento e Sub-Type foram relidas no v30)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C17 · erro+causa · [[Colombia]]
- **Chave:** `CO | DD e specs | Worker Type 40, PEP, Worker Sub-Type e Principal Contributor Document Type` · **Já existe?** não; relacionado a hub Pendências (#41, código TipoTrabajador/SubTipo do pensionado)
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** o patch de 7-set corrigiu quatro erros de tabela de código no DD v1.0 e nas specs.
- **Antes (se erro):** (1) Worker Type código 40 ("Beneficiario UPC adicional") no DD, mas a tabela 5.5.3 do Anexo da NE admite 16 códigos (01 02 04 12 18 19 21 22 23 30 31 47 51 54 56 58) e 40 é tipo de cotizante PILA, não empregado; (2) tipo de documento 47 como "PE", mas a tabela 5.2.1 do Anexo imprime "PEP" ("PE" é o catálogo PILA/SOI); (3) Worker Sub-Type: a NE (tabela 5.5.4) admite só 00/01, a PILA usa 0–12 num dígito; (4) `Principal Contributor Document Type` (PILA T2R2-074) apontava para o mapper do empregador, que aceita NI e rejeita RC.
- **Causa (se erro):** dois catálogos oficiais com o mesmo nome (DIAN × PILA) tratados como um só; mapper errado.
- **Correto / novo:** código 40 removido; 47 = PEP (NE) e "PE" só como equivalente PILA; Sub-Type: no DD ficam 00/01/03/04/05/06/09 (subconjunto privado), com a armadilha de largura do código documentada; T2R2-074 usa o catálogo de cotizante (CC CE TI PA CD SC RC PE; PT só no layout XLS de cesantías, CO-GAP-06). Pista para a pendência #41 do hub: reler as tabelas 5.5.3 e 5.5.4 do Anexo Técnico da NE antes de afirmar "sem fonte oficial" para o pensionado.
- **Nível de evidência:** B (patch) citando A (Anexo Técnico NE v1.0 tabelas 5.2.1, 5.5.3, 5.5.4; AT2 v09 campo 3) · **Fonte:** CO-ALIGNMENT-PATCH Check 1
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-ALIGNMENT-PATCH.md` linhas 39–43 (Check 1) e 57–67 (divergências confirmadas corretas); `raw/pipeline/Colombia/2026-10-27/qa/scope_validation.md` linhas 64–65 (numeral 47 com dois significados).
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Pendências #41: pista) e `servicos/` do Design se virar regra de DD
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (tabelas do Anexo não relidas por mim)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C18 · erro+causa · [[Colombia]]
- **Chave:** `CO | QA do pipeline | FACT-CONFLICTS "PASS" vazio (C32)` · **Já existe?** não
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** `FACT-CONFLICTS.md` diz "PASS — no deterministic conflicts" e o handover registra C32 = PASS. Mas o próprio handover explica: "No `[[FACT:]]` tags (country pre-dates tagging)". Ou seja, o check de consistência entre artefatos **não testou nada** na Colômbia. Há contradições reais entre artefatos vigentes (C15, C21, C22).
- **Antes (se erro):** leitura de "PASS" como consistência verificada.
- **Causa (se erro):** o check C32 só compara fatos marcados com `[[FACT:]]`; sem marcas, passa em vazio.
- **Correto / novo:** tratar a consistência entre CCG, WTC, DD e specs da Colômbia como **não verificada pelo pipeline**; a conferência vem das auditorias de 22–26/10.
- **Nível de evidência:** B · **Fonte:** handover_status + FACT-CONFLICTS
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/handover_status.md` linha 106 (C32); `raw/pipeline/Colombia/2026-10-27/logs/FACT-CONFLICTS.md` linha 3; `raw/pipeline/Colombia/2026-10-27/logs/FACT-CONFLICTS.csv` (só cabeçalho).
- **Quem decidiu / pediu:** —
- **Destino:** `servicos/research-pipeline.md` ("o que já deu errado") e lições de processo
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C19 · erro+causa · [[Colombia]]
- **Chave:** `CO | Payslip e ficha da skill | citação da Res. DIAN 000013/2021 (compilada na Res. 227/2025)` · **Já existe?** sim → complementa [[correcoes]] (Res. 13 → 227, hub Pendências "Achados da Cinthya", 14/10 e 21/10)
- **Tipo:** erro+causa
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** em 21–22/10 a Res. DIAN 000013/2021 foi trocada pela Res. 000227/2025 (que a compila, arts. 1.5.3.1.1 a 1.5.3.9.8) no CCG v1.3, WTC v1.5, DD v1.2 e SIR v1.1. O Payslip do Drive (A78 de `Colombia (EN)`, e o equivalente em ES) ainda cita "Resolucion 000013 de 2021", e o hub (§Ficha, armadilha 14) cita "Res. DIAN 000013/2021 arts. 5 e 24". A verificação do Payslip (12-jul) também cita a 13/2021.
- **Antes (se erro):** Payslip e ficha com a Res. 13/2021 como norma em vigor.
- **Causa (se erro):** a correção de 21/10 cobriu CCG, WTC, DD e SIR, não o Payslip nem a ficha.
- **Correto / novo:** citar "Res. DIAN 000227 de 2025 (compila a Res. 13/2021)". O mapa artigo a artigo está em `SIR-RES227-2026-10-21.md`; os arts. 5 e 24 da Res. 13 não aparecem na tabela de correspondência lida, então o número exato na 227 fica a confirmar.
- **Nível de evidência:** A (Res. 227/2025, via mapa do normograma já feito pela frente) · **Fonte:** `SIR-RES227-2026-10-21.md`; Payslip do Drive A78
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-PAYSLIP-VERIFICATION.md` linha 67 (disclosure duty) e 181; `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` linhas 346–350 (art. 5 e art. 24 da Res. 13). Verificação adicional: `G:\...\18 - Payslip\CO_Compliance_Payslip_Generator.xlsx`, `Colombia (EN)` A78; `Research Pipeline/Colombia/co-report-crosscheck/04-output/SIR-RES227-2026-10-21.md`.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Pendências: Payslip) e ficha (artigo 14) se a skill instalada for atualizada
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** média (artigos 5 e 24 sem equivalente confirmado)
- **Validação:** ◐ conferência independente: nível de evidência é B citando A (mapa interno da frente; a Res. 227 não foi lida na fonte), não A · humana ⏳

### F6-20261027-CO-C20 · erro+causa · [[Colombia]]
- **Chave:** `CO | scope_manifest, skill e CCG | adiantamento mensal de cesantías (8,33%, Ley 2466 art. 64 par. 1)` · **Já existe?** sim → complementa [[correcoes]] 2026-10-23
- **Tipo:** erro+causa
- **Risco:** alto (regra estatutária tratada como operável)
- **Serviço:** [[research-pipeline]]
- **O que diz:** [[correcoes]] 2026-10-23 retirou o adiantamento mensal da CO-CESANTIAS-006 (MA01–MA05), do DD v1.3 e do WTC v1.6 porque o decreto que regulamenta o par. 1 é só minuta e o PILA AT2 v30 não tem tipo de cotização de cesantías. Os artefatos **derivados do pipeline** ainda o tratam como opção que o motor deve suportar: o `scope_manifest` validado ("Optional monthly 8.33% advance deposit … which the engine must support as a configurable option"), o `reports.log` ("built MA01–MA05, flagged DRAFT and switched off") e a skill do pipeline (45 ocorrências de "advance deposit" / "monthly advance" nas referências, contadas por mim). A [[correcoes]] diz que o CCG v1.4 continua descrevendo a lei, sem campo de spec.
- **Antes (se erro):** `scope_manifest.json` e skill do pipeline com o adiantamento como funcionalidade configurável.
- **Causa (se erro):** base numa minuta de decreto do MinTrabajo (fonte não vinculante).
- **Correto / novo:** par. 1 não operável até o decreto e o PILA; par. 2 (juros mensais) é lei vigente e só exige acordo escrito (Ley 50/1990 art. 99 par. 2, já lido em 22/10). Não usar o `scope_manifest` nem a skill do pipeline como referência sobre este ponto.
- **Nível de evidência:** B (pipeline) × A (Ley 50/1990 art. 99, já arquivada em `raw/docs/oficiais/CO/2026-10-22-Ley-50-1990-FuncionPublica.pdf`) · **Fonte:** scope_validation + reports.log
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/scope_validation.md` linha 249 (OUT CO-OUT-CESANTIAS); `raw/pipeline/Colombia/2026-10-27/logs/reports.log` "Three things worth your attention", item 2. Verificação adicional: `Research Pipeline/Colombia/CO-compliance/scope_manifest.json` (7 ocorrências de "advance"); `Research Pipeline/Colombia/2026-10-22-auditoria-lote1/CONFERENCIA.md` seção "23/10".
- **Quem decidiu / pediu:** opção (b) do usuário em 2026-10-23 (já registrada em [[correcoes]])
- **Destino:** [[correcoes]] (complemento: artefatos derivados não atualizados) e frente pipeline (atualizar `scope_manifest`)
- **Pergunta para o teste (Conjunto B)?** sim → "O adiantamento mensal de cesantías (8,33%) já é operável na Colômbia?" (não, ver C20)
- **Confiança da extração:** alta
- **Validação:** ◐ conferência independente: a citação "which the engine must support as a configurable option" não existe (a frase real do scope_manifest é "configurable engine options"); o reports.log diz "not operable"/"switched off"; contagens recontadas: skill 54, scope_manifest 8 · humana ⏳

### F6-20261027-CO-C21 · pendência · [[Colombia]]
- **Chave:** `CO | CCG, Payslip, ficha | SMMLV 2026: qual decreto sustenta o valor (1469/2025 × 0159/2026)` · **Já existe?** sim → conflita com hub §Ficha (armadilha 1) e §Valores-chave (SMMLV)
- **Tipo:** pendência
- **Risco:** alto (valor estatutário)
- **Serviço:** [[research-pipeline]] / [[suporte]]
- **O que diz:** o **valor** é o mesmo em tudo (COP 1.750.905). O **instrumento** diverge. Hub (ficha, lida em 2026-10-02): vale o Decreto 0159/2026; o 1469/2025 está suspenso. Verificação do Payslip (12-jul): 1469 suspenso em 12/2 e substituído pelo 0159. CCG v1.0 do pipeline e CCG v1.4 do Drive: em **9-jul-2026** o Conselho de Estado revogou a suspensão (notícia de 17-jul) e o **Decreto 1469/2025 "recuperou força plena"; o 0159 está exaurido**. Payslip do Drive (A83): "Decreto 1469 de 2025, reinstated by Consejo de Estado auto of 9-Jul-2026". O QA de 7-set descreve a sequência sem dizer qual é o operativo.
- **Antes (se erro):** —
- **Causa (se erro):** a verificação do Payslip (12-jul) é anterior ao auto (9-jul, divulgado em 17-jul); a ficha vem de pesquisa de 27-ago, mas ainda trata o 1469 como suspenso.
- **Correto / novo:** **conflito sem resolução** (B × B; mais recente: CCG v1.4, 26/10, mas apoiado em notícia, não no auto). Manter só o valor; para citar o instrumento, ler o auto do Conselho de Estado de 9-jul-2026 (processo 11001-03-25-000-2026-00004-00) e o Decreto 0159 de 19-fev-2026. Registrar no hub as duas versões até lá.
- **Nível de evidência:** B × B (A não lido) · **Fonte:** CO-QA-REPORT §6; CO-PAYSLIP-VERIFICATION; CCG v1.4 Módulo 4; Payslip A83
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-PAYSLIP-VERIFICATION.md` linhas 18–23, 31–32 e 101–109; `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` linhas 604–607. Verificação adicional: `Research Pipeline/Colombia/2026-10-22-auditoria-lote1/CO-CCG-001-v1.4.docx` (parágrafo "The legal instrument for 2026 requires a specific note" e a lista "Legal basis"); `G:\...\18 - Payslip\...xlsx`, `Colombia (EN)` A83.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Pendências + §Valores-chave: SMMLV) e skill `payroll-compliance-colombia` (armadilha 1)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual decreto fixa o SMMLV 2026 da Colômbia?" (valor 1.750.905 certo; instrumento a confirmar)
- **Confiança da extração:** [INCERTO] (fontes B em conflito; auto de 9-jul não lido)
- **Validação:** ◐ conferência independente: a verificação do Payslip (12-jul) é posterior ao auto de 9-jul; é anterior só à divulgação (17-jul): não incorpora o auto divulgado em 17-jul · humana ⏳

### F6-20261027-CO-C22 · pendência · [[Colombia]]
- **Chave:** `CO | CCG, DD, WTC | retenção do não residente: 20% fixo (ET art. 408) e contradição no Módulo 2.2` · **Já existe?** sim → preenche hub §Valores-chave ("Expat / não residente 20% … ⚠️ sem fonte legal")
- **Tipo:** pendência
- **Risco:** alto (valor estatutário)
- **Serviço:** [[research-pipeline]] / [[suporte]]
- **O que diz:** o pipeline fixou, com fonte, que o estrangeiro **não residente** com contrato colombiano sofre retenção de **20% sobre o bruto** (ET art. 408), sem depuração (art. 388), sem renda isenta de 25%, sem deduções do art. 387 e sem faixa isenta, até adquirir a residência (ET art. 10: mais de 183 dias em 365). A troca para a tabela do art. 383 é **prospectiva**, a partir do pagamento seguinte ao cumprimento do teste de 183 dias (DIAN Conceito 011108 de 29-jun-2026, que rejeitou retenção pela tabela desde o primeiro dia). Para isso o motor precisa de um flag de residência com data de vigência e de um acumulador de dias de presença. O WTC marca `CO-TX-08` sem nenhuma linha atribuída: é um overlay por empregado via coluna P "Special Tax", e a legenda foi anotada assim (MINOR-09, tratado na "v1.1" do WTC de 18-set). **Contradição aberta:** o CCG (Módulo 2.2) diz que o não residente é retido "exatamente como o residente", pela tabela do art. 383, enquanto o Módulo 6.2 diz 20% fixo; o `dd.log` registrou isso para correção "fora desta tarefa". A CCG v1.4 do Drive ainda tem os dois parágrafos.
- **Antes (se erro):** CCG Módulo 2.2 (tabela 383 para o não residente).
- **Causa (se erro):** módulos escritos em momentos diferentes; o QA conferiu a regra no escopo, não a consistência interna do CCG.
- **Correto / novo:** 20% sobre o bruto, até a residência, pela fonte abaixo; corrigir o Módulo 2.2 do CCG. Antes de promover, ler o Conceito 011108/2026 e o ET art. 408 (só citados, não lidos nesta extração; o art. 408 trata de pagamentos a não residentes e a aplicação a salário de contrato local é o que o Conceito deve confirmar).
- **Nível de evidência:** B citando A (ET arts. 10 e 408; DIAN Conceito 011108 de 2026-06-29) · **Fonte:** scope_validation B1 + QA Check 5 + dd.log
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/scope_validation.md` linhas 21, 75–80, 102 e 192; `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` linhas 224–225 e 484–491 (MINOR-09); `raw/pipeline/Colombia/2026-10-27/logs/dd.log` "Three things worth your attention", item 2. Verificação adicional: `Research Pipeline/Colombia/CO-compliance/01-ccg/modules/m06_tax.md` linhas 8–25 (Módulo 6.2) e `…/2026-10-22-auditoria-lote1/CO-CCG-001-v1.4.docx` (parágrafo "The same progressive art. 383 table…").
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Valores-chave, linha "Expat / não residente", com fonte e vigência a partir de 2026) + frente pipeline (corrigir CCG Módulo 2.2)
- **Pergunta para o teste (Conjunto B)?** sim → "Como se retém imposto de renda de um empregado estrangeiro não residente na Colômbia?" (20% sobre o bruto até a residência; tabela 383 só depois)
- **Confiança da extração:** média (leis e conceito citados, não lidos; contradição interna confirmada no docx)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C23 · pendência · [[Colombia]]
- **Chave:** `CO | WTC | bônus de férias: limite de 95 UVT (HRBS-12487)` · **Já existe?** sim → preenche hub §Valores-chave ("Limite vacation bonus para SS + retenção 95 UVT … ⚠️ sem fonte")
- **Tipo:** pendência
- **Risco:** alto (valor estatutário)
- **Serviço:** [[research-pipeline]] / [[suporte]]
- **O que diz:** a "v1.1" do WTC do pipeline registra (linha 3 do Version Control, 2026-09-18, HRBS-12487) que **não existe limite estatutário de 95 UVT para o bônus de férias**; o número é só o teto da faixa de alíquota zero da tabela do art. 383 do ET (0–95 UVT = 0%). O mesmo número aparece na verificação do Payslip: limiar de retenção "> 95 UVT = COP 4.975.530/mês" (52.374 × 95 = 4.975.530, conferido). A linha 317 (prima de férias extralegal, pacto escrito CST art. 128) foi criada com o mesmo tratamento da 316.
- **Antes (se erro):** hub: "95 UVT para SS + retenção", sem fonte.
- **Causa (se erro):** o solicitante (PMI) tratou o teto da faixa 0% como limite próprio do bônus.
- **Correto / novo:** não há limite de 95 UVT próprio; vale a tabela do art. 383 (UVT 2026 = COP 52.374, Res. DIAN 000238 de 2025) e, para seguridade social, a trava de 40% dos pactados (Ley 1393 art. 30). Falta a fonte A lida (ET art. 383 já está no hub, §Valores-chave "Tabela Art. 383").
- **Nível de evidência:** B (VC) citando A (ET art. 383) · **Fonte:** WTC v1.1 do pipeline, Version Control linha 3
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/version-control/CO-WTC-001-v1.1.md` (aba Version Control, linha de versão 3); `raw/pipeline/Colombia/2026-10-27/qa/CO-PAYSLIP-VERIFICATION.md` linha 40.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Valores-chave, linha "Limite vacation bonus…": trocar "⚠️ sem fonte" pela conclusão e fonte) e ticket HRBS-12487 (só pela janela Suporte)
- **Pergunta para o teste (Conjunto B)?** sim → "Existe limite de 95 UVT para o bônus de férias na Colômbia?" (não; é o teto da faixa 0% do art. 383)
- **Confiança da extração:** média (o raciocínio completo estava na linha 3 do VC e não foi reencontrado na linha 317 da v1.6)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C24 · pendência · [[Colombia]]
- **Chave:** `CO | CCG, skill | reforma de pensão Ley 2381/2024: Sentencia C-264/2026 e 1-abr-2027` · **Já existe?** sim → conflita com hub §Ficha (armadilha 13: "não fixar a data de 2027-04-01, só imprensa")
- **Tipo:** pendência
- **Risco:** alto (regra estatutária e data)
- **Serviço:** [[research-pipeline]]
- **O que diz:** a ficha (skill, pesquisa de 27-ago) diz que a reforma não vale em 2026 (Auto 841/2025 a suspendeu) e que a data de 1-abr-2027 só estava na imprensa. O pipeline (CCG, 3-set) traz a cadeia: art. 94 da lei fixava vigência em 1-jul-2025; Auto 841 de 18-jun-2025 suspendeu; **Sentencia C-264 de 25-ago-2026** (caso D-15989) declarou o art. 94 constitucional "no entendimento de que os dispositivos mantidos entram em vigor em 1-abr-2027" (mais de 80 artigos mantidos; nove devolvidos à Câmara). Conclusão operacional igual nas duas fontes: nada da Ley 2381 vale para 2026. O QA a lista como "C2 newest-law check ✅". As fontes que o `ccg.log` cita para a sentença são Forbes, Ámbito Jurídico e Infobae (imprensa).
- **Antes (se erro):** —
- **Causa (se erro):** a pesquisa da skill é de 27-ago, dois dias depois da sentença, e a ficha cita só a imprensa.
- **Correto / novo:** manter "não vale em 2026". Registrar a data 2027-04-01 como **não confirmada em fonte A** até ler o comunicado/sentença da Corte Constitucional (C-264/2026). Se confirmada, atualizar a ficha (armadilha 13) e a skill.
- **Nível de evidência:** B (pipeline) × B (ficha); A (sentença) pendente · **Fonte:** QA C2; ccg.log; CCG Módulo 5
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` linha 588 (C2); `raw/pipeline/Colombia/2026-10-27/logs/ccg.log` "What I changed", item 2 e linha de fontes. Verificação adicional: `Research Pipeline/Colombia/CO-compliance/01-ccg/modules/m05_social_security.md` linhas 57–75.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Ficha, armadilha 13: nota "Pipeline cita C-264/2026; data 2027-04-01 a confirmar") e skill `payroll-compliance-colombia`
- **Pergunta para o teste (Conjunto B)?** sim → "A reforma de pensão (Ley 2381/2024) vale em 2026 na Colômbia?" (não; vigência 1-abr-2027 a confirmar)
- **Confiança da extração:** [INCERTO] (a data depende de uma sentença que o raw só cita via imprensa)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C25 · pendência · [[Colombia]]
- **Chave:** `CO | WTC, CCG | incapacidade: tarifa dos 2 primeiros dias e piso do salário mínimo` · **Já existe?** sim → complementa hub §Ficha "Lacunas abertas" (Q-6, Q-7) e §Pendências (CCG v1.3: piso C-543)
- **Tipo:** pendência
- **Risco:** alto (valor estatutário)
- **Serviço:** [[research-pipeline]] / [[suporte]]
- **O que diz:** o handover de 7-set deixou dois itens abertos no CCG, ambos com "default Mercans configurável": (1) tarifa do empregador nos 2 primeiros dias de incapacidade por doença geral: 66,67% (a norma, Decreto 2943/2013 art. 1, compilado no Decreto 780 art. 3.2.1.10, atribui os dias ao empregador mas **não diz a taxa**; CST art. 227 dá 2/3 nos 90 primeiros dias; parte da prática paga 100%); (2) piso de 1 SMMLV sobre o pagamento ("fonte regulatória primária não recuperada"). Li a aba "Employer Sick Pay" do **WTC v1.6 (vigente)**: os dois itens continuam como "OPEN ITEM 1" e "OPEN ITEM 2", com o mesmo texto. O hub diz que o CCG v1.3 passou a trazer o "piso C-543" no exemplo de licença médica; então CCG e WTC divergem sobre o piso estar ou não fundamentado.
- **Antes (se erro):** —
- **Causa (se erro):** sem fonte A para a tarifa e para o piso.
- **Correto / novo:** a tarifa de 66,67% e o piso seguem como **default configurável**, sem fonte A; o piso tem apoio na Sentencia C-543 citada no CCG v1.3 (não lida aqui). Ao responder, dizer que a norma não fixa a taxa dos dias 1–2.
- **Nível de evidência:** B · **Fonte:** handover_status; WTC v1.6 aba Employer Sick Pay
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/handover_status.md` linhas 366–369 (Next steps, item 3); `raw/pipeline/Colombia/2026-10-27/qa/scope_validation.md` linha 157 (incapacidade, "66.67%"). Verificação adicional: `Research Pipeline/Colombia/2026-10-22-auditoria-lote1/CO-WTC-001-v1.6.xlsx`, aba "Employer Sick Pay", linhas 30–41.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Pendências: Q-6/Q-7, com o estado de 26/10) e frente pipeline (alinhar WTC e CCG sobre o piso)
- **Pergunta para o teste (Conjunto B)?** sim → "Qual a taxa que o empregador paga nos 2 primeiros dias de incapacidade por doença geral?" (a norma não fixa; default 66,67% configurável)
- **Confiança da extração:** [INCERTO] (se a C-543 do CCG v1.3 fecha o item do piso não está no raw)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C26 · pendência · [[Colombia]]
- **Chave:** `CO | CCG | Circular MinTrabajo 101/2025 §5.1: erro de 75% no adicional dominical` · **Já existe?** não (a ficha lista D-1 a D-4, não este)
- **Tipo:** pendência
- **Risco:** alto (valor estatutário)
- **Serviço:** [[research-pipeline]] / [[suporte]]
- **O que diz:** o QA registra, entre os "defeitos em fontes oficiais", o erro da Circular 101 de 2025 §5.1. O CCG explica: depois de afirmar corretamente a escada 80/90/100% no §4, o §5.1 volta a falar em "75% de adicional" para domingos e feriados (valor anterior à reforma). Vale a escada do §4 (CST art. 179 conforme Ley 2466 art. 14): 80% até 2026-06-30, 90% desde 2026-07-01, 100% desde 2027-07-01. Os 75% do §5.1 são resíduo e **não devem ser configurados**. Mesma Circular (22-set-2025) traz a tabela do divisor: 220 até 14-jul-2026 e 210 desde 15-jul-2026.
- **Antes (se erro):** —
- **Causa (se erro):** inconsistência interna do documento oficial.
- **Correto / novo:** não usar o §5.1; confirmar lendo a Circular 101/2025 §4 e §5.1 (o texto não foi lido aqui) antes de responder ticket sobre dominical/festivo. Valores 80%→90% já estão no hub.
- **Nível de evidência:** B (QA e CCG) citando A (Circular 101/2025; CST art. 179; Ley 2466 art. 14) · **Fonte:** CO-QA-REPORT §6 item 5; CCG Módulo 4
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` linhas 599–607 (escada 80→90→100) e 617–619. Verificação adicional: `Research Pipeline/Colombia/CO-compliance/01-ccg/modules/m04_compensation.md` linhas 275–290 e 597–601.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Ficha: armadilha 3, nota "Circular 101 §5.1 tem erro de 75%") e skill
- **Pergunta para o teste (Conjunto B)?** sim → "Qual o adicional de domingo/feriado na Colômbia em julho de 2026?" (90%, não os 75% do §5.1 da Circular 101)
- **Confiança da extração:** média (descrição só pelo CCG; circular não lida)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C27 · pendência · [[Colombia]]
- **Chave:** `CO | CO-DIAN-001 / SIR | defeitos do Anexo Técnico da NE (SendBillSync, NumeroDocumento, SegundoApellido)` · **Já existe?** parcial → complementa hub §Ficha "O que mais dá errado" (D-2 CUNE, D-3 QR, D-4 enum)
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** além dos quatro defeitos que a ficha já lista, o pipeline registra defeitos novos do Anexo Técnico da Nómina Electrónica: (a) §9.7 diz "Metodo: SendBillSync" enquanto o texto, o envelope e os dois WSDL dizem `SendNominaSync` (vale o WSDL); (b) `Trabajador/@NumeroDocumento` é `xsd:integer`, o que nenhum passaporte satisfaz; (c) `SegundoApellido` é obrigatório e a maioria dos estrangeiros não tem; (d) discrepância "dois parágrafos anunciados × três promulgados" no art. 15 da Ley 2466; (e) modelo de autenticação descrito de dois modos (Anexo: mTLS; WSDL: certificado em nível de mensagem), resolvido pelo WSDL e a confirmar em habilitação.
- **Antes (se erro):** —
- **Causa (se erro):** inconsistências nos documentos oficiais.
- **Correto / novo:** tratar (a)–(c) como alertas ao configurar a NE para estrangeiros; o QA não dá o local exato da (b) e (c) no XSD, então o item entra como alerta sem valor. Ler o XSD v1.0.6 antes de afirmar.
- **Nível de evidência:** B · **Fonte:** QA §6 item 5; si_discover.log; si_dian-ne.log
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` linhas 617–622; `raw/pipeline/Colombia/2026-10-27/logs/si_discover.log` ("Three things worth flagging", item 3) e `raw/pipeline/Colombia/2026-10-27/logs/si_dian-ne.log` ("Three findings", item 3).
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Ficha, "O que mais dá errado") e `servicos/design.md` (nota para a configuração da NE)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (os itens (b)–(e) aparecem em uma linha do QA/log, sem o trecho do XSD)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C28 · pendência · [[Colombia]]
- **Chave:** `CO | CO-DIAN-005 Formato2276 | layout XML marcado como DERIVED (anexo técnico não obtido)` · **Já existe?** não
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** o QA diz que a spec do Formato 2276 está "DERIVED para o layout XML porque o anexo técnico não está em mãos"; o handover deixa a pergunta aberta: a DIAN publica um XSD próprio do 2276 v4, ou o pré-validador é o único validador? Isso "afeta a fidelidade da spec 005". Não há registro, no hub ou no raw, de que tenha sido fechada: o hub só trata M32/M33 da spec (lote 1).
- **Antes (se erro):** —
- **Causa (se erro):** anexo técnico do 2276 não obtido na época do build.
- **Correto / novo:** tratar o layout XML do 2276 como derivado, não A, até achar o anexo/XSD oficial (Res. DIAN 000227/2025 arts. 1.3.7.1.1 e 1.3.9.1 é a base legal já citada).
- **Nível de evidência:** B · **Fonte:** QA Check 7; handover_status
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` linhas 265–267; `raw/pipeline/Colombia/2026-10-27/qa/handover_status.md` linhas 326–333 (pergunta 2); `raw/pipeline/Colombia/2026-10-27/qa/scope_validation.md` linha 125.
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Pendências)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (não dá para saber se o trabalho de 22–26/10 achou o anexo)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C29 · pendência · [[Colombia]]
- **Chave:** `CO | CCG e ficha | CO-RPT-007 (relatório MinTrabajo) fora de escopo × ficha lista como relatório principal` · **Já existe?** sim → conflita com hub §Ficha ("Relatórios principais … relatório MinTrabajo (CO-RPT-007)" e Q-12)
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** a ficha da skill lista, entre os relatórios principais, o "relatório MinTrabajo (CO-RPT-007)" e a lacuna Q-12 (25%). No pipeline, CO-RPT-007 (relatório de contratos com pessoas com deficiência ao MinTrabajo) foi **descartado como escopo de RH**, junto com a cota de aprendizes do SENA e as notificações do RUAF-ND; o `scope_manifest` traz `descoping_reason` e `client_impact: "Refer to HRMS team"`. O hub registra a decisão de 15/10 (escopo = só relatórios estatutários de folha), coerente com o descarte; a ficha não foi ajustada.
- **Antes (se erro):** ficha com CO-RPT-007 como relatório da Colômbia a especificar.
- **Causa (se erro):** a ficha reproduz a skill de agosto, anterior ao scope_manifest de setembro.
- **Correto / novo:** CO-RPT-007 = fora do escopo (RH; não há spec). A ficha deve dizer isso; o Q-12 deixa de ser lacuna de spec.
- **Nível de evidência:** B · **Fonte:** QA Check 3; scope_validation (filings fora de escopo); handover
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` linhas 140–144; `raw/pipeline/Colombia/2026-10-27/qa/scope_validation.md` linhas 46 e 127–129; `raw/pipeline/Colombia/2026-10-27/qa/handover_status.md` linhas 63–66.
- **Quem decidiu / pediu:** decisão de escopo de 2026-10-15 (hub §Decisões, checkpoint call)
- **Destino:** hub (§Ficha, relatórios principais e lacunas) quando a skill for atualizada
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C30 · pendência · [[Colombia]]
- **Chave:** `CO | WTC | códigos Mercans numéricos (102 linhas CO- derivadas)` · **Já existe?** não
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]] / [[design]]
- **O que diz:** o WTC tem 300 códigos globais e 102 linhas específicas da Colômbia; os números Mercans das 102 são **DERIVED**: "nenhuma faixa numérica foi atribuída à Colômbia, então usam-se códigos mnemônicos `CO-`, que devem ser renumerados na configuração do sistema". Li o WTC v1.6 vigente: a coluna "Mercans Code" está vazia em toda a aba, e o aviso de DERIVED continua na aba "Global WTC Coverage". Os tickets do PMI citam wage types numéricos (63123, 62837, 52552, 21125…) e o Payslip tem séries de contas ilustrativas ("62100:62999"). Nada no hub diz quem atribui a faixa.
- **Antes (se erro):** —
- **Causa (se erro):** faixa de códigos da Colômbia não atribuída.
- **Correto / novo:** sem faixa atribuída: não afirmar o código numérico de nenhuma linha `CO-`; perguntar à Config/Product quando sair a faixa.
- **Nível de evidência:** B · **Fonte:** CO-QA-REPORT §4 (DERIVED flag)
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` linhas 554–557. Verificação adicional: `Research Pipeline/Colombia/2026-10-22-auditoria-lote1/CO-WTC-001-v1.6.xlsx` (coluna A da aba Wage Type Catalogue; aba Global WTC Coverage linha 15).
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Pendências) e [[fronteiras]] (Config atribui a faixa)
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** alta
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C31 · pendência · [[Colombia]]
- **Chave:** `CO | CO-CESANTIAS-006 e skill | base das cesantías com auxílio de transporte (CST art. 253) e calculadora do operador` · **Já existe?** sim → conflita com hub §Ficha "Lacunas abertas" (Q-21: auxílio na base de prestações é "prática consolidada, não lei (~90%)")
- **Tipo:** pendência
- **Risco:** alto (base de cálculo estatutária)
- **Serviço:** [[research-pipeline]] / [[suporte]]
- **O que diz:** o pipeline afirma que a base das cesantías **inclui o auxílio de transporte** por força do CST art. 253 (spec CO-CESANTIAS-006: "CST art. 253 requires it"), e que a calculadora do próprio operador (`salario básico × dias/360`) o omite, depositando COP 1.750.905 em vez de COP 2.000.000 para quem ganha o mínimo (déficit de COP 249.095 por empregado, penalizado com um dia de salário por dia de atraso, sem teto). A ficha diz que isso é prática consolidada, não lei (~90%). Conferi: 1.750.905 + 249.095 = 2.000.000. A spec final de `05-final` mantém a regra.
- **Antes (se erro):** —
- **Causa (se erro):** citação do art. 253 sem leitura do texto no raw; fonte da regra pode ser outra norma (decreto/lei do auxílio).
- **Correto / novo:** regra operacional (incluir o auxílio na base) está nos artefatos; a **fonte legal exata** é pendência. Não repetir "art. 253 exige" em ticket sem ler o artigo.
- **Nível de evidência:** B · **Fonte:** reports.log; spec CO-CESANTIAS-006 (final)
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/logs/reports.log` "Three things worth your attention", item 1; `raw/pipeline/Colombia/2026-10-27/qa/CO-QA-REPORT.md` linha 622 (bug da calculadora do operador); `raw/pipeline/Colombia/2026-10-27/qa/CO-PAYSLIP-VERIFICATION.md` linha 36 (auxílio fora do IBC). Verificação adicional: `Research Pipeline/Colombia/co-report-crosscheck/05-final/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` (Population Rules linha 7; Field Options linhas 48–49).
- **Quem decidiu / pediu:** —
- **Destino:** hub (§Ficha, Q-21: nota de divergência) e skill
- **Pergunta para o teste (Conjunto B)?** sim → "A base das cesantías inclui o auxílio de transporte?" (sim; fonte legal exata a confirmar)
- **Confiança da extração:** [INCERTO] (norma exata não confirmada; artigo citado não lido)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

### F6-20261027-CO-C32 · pendência · [[Colombia]]
- **Chave:** `CO | pipeline | etapas mortas: wtc.log e payslip.log` · **Já existe?** não
- **Tipo:** pendência
- **Risco:** normal
- **Serviço:** [[research-pipeline]]
- **O que diz:** dois logs de etapa terminam em erro: `wtc.log` = "Error: Reached max turns (60)" e `payslip.log` = "API Error: Connection lost mid-response" (112 bytes). O WTC e o Payslip existem e o QA os revisou, e há uma passagem pós-handover em 18-set (Version Control do WTC, linhas 2–4; Payslip v1.1 DRAFT), mas não há log de uma execução completa final dessas duas etapas. O `payslip_batch.log` mostra a execução que de fato gerou o Payslip.
- **Antes (se erro):** —
- **Causa (se erro):** limite de turnos (WTC) e queda de conexão (Payslip) no pipeline.
- **Correto / novo:** não tratar o log dessas etapas como prova de conclusão; a prova são os artefatos e o QA.
- **Nível de evidência:** B · **Fonte:** logs
- **Localização no raw:** `raw/pipeline/Colombia/2026-10-27/logs/wtc.log` (linha única); `raw/pipeline/Colombia/2026-10-27/logs/payslip.log` (2 linhas); `raw/pipeline/Colombia/2026-10-27/logs/payslip_batch.log` (relatório final de construção).
- **Quem decidiu / pediu:** —
- **Destino:** `servicos/research-pipeline.md` ("o que já deu errado")
- **Pergunta para o teste (Conjunto B)?** não
- **Confiança da extração:** [INCERTO] (não se sabe se houve reexecução fora dos logs coletados)
- **Validação:** ✔ conferência independente (2026-10-27) · humana ⏳

## Descartados
| Item (ID no inventário) | Motivo |
|---|---|
| MINOR-01 (resíduo do template tcheco no VC do WTC) e MINOR-09 (nota de CO-TX-08) | já tratados na "v1.1" do WTC do pipeline (VC linhas 2 e 4); o Version Control da linhagem do Drive nem tem o resíduo; MINOR-09 está dentro de C22 |
| MINOR-02 (PILA sem rótulo de chave composta T2R2-003+004) | consistência interna da spec, sem impacto na resposta; estado atual não verificado |
| MINOR-03 (códigos 11, CD, SC, PT fora da lista do manifesto) | o patch os deixou como "referência apenas" (PT só no layout XLS de cesantías, CO-GAP-06); sem impacto na resposta |
| MINOR-06, 07, 08, 10, 12 (paleta do Payslip, rótulos de cabeçalho, ordem das colunas do Version Control, código do WTC na coluna L, cores do F350) | cosméticos ou de padrão de formato, sem efeito na resposta estatutária |
| MINOR-11 (flag de pensionista ativo sem campo próprio no DD) | tratado pelo trabalho de pensionados (G1, 21–22/10, hub Pendências); sem informação nova |
| Falhas de ferramenta C12, C20, C27, C29, C33 do harness (F24, F25, F27, F28) e backup `_audit_v24_mechanical.py.bak` | ruído de ferramenta (falsos positivos do auditor; correções só na cópia da CO); registrado como lição em `country_failure_log` |
| C33 (substantivo "auxilio" sem tradução no CCG, linha 1.0 rev B) | correção de redação, sem impacto na resposta |
| C25 (XML de exemplo da NE é reconstrução, não amostra oficial) | já documentado na própria aba "Sample File" ("NOT an official DIAN sample"); sem impacto |
| C16 (45 referências reversas), 82 citações de "Spec ref" do DD, Check 4 (138 ponteiros), Check 6 (padrões de código) do CO-ALIGNMENT-PATCH | consistência interna dos artefatos; sem impacto na resposta |
| Casilla 4 do Formulário 220 (série AAAA-NNNNNN desenhada pela Mercans) | já está na spec final (`05-final`, aba "Formulario 220 Spec", linha 4); sem informação nova |
| Prazo de cesantías 2027 (14-fev é domingo; depositar até 12-fev) | já está na spec final (aba "Sample File", linhas 156 e 161); a base legal (Ley 50/1990 art. 99 num. 3) é conhecida |
| Verificação do Payslip: taxas, tetos e faixas (saúde 12,5%, pensão 16%, parafiscais, UVT 52.374, tabela do art. 383, ARL I–V) | confirma valores que já estão na ficha e no hub; sem informação nova. A observação "FSP 2% acima de 20 SMMLV" vem de blog e diverge só na redação do payslip (16); fonte secundária |
| Reconciliação do Payslip (retenção 2.250.765; líquido 15.221.235) e do exemplo 12 do CCG | exemplo fictício de teste de fórmulas, sem dado de cliente e sem impacto na resposta |
| Pergunta aberta: algum operador PILA além de ARUS/SuAporte tem API contratual | sem impacto: a PILA é portal de qualquer forma (handover) |
| Esforço de ~79 pessoa-dias, modelo de autenticação da DIAN e runbook P1–P7 (`si_dian-ne.log`, `sir_index.log`, `si_discover.log`) | integração do sistema, outro time ([[fronteiras]]); a parte de defeitos do Anexo está em C27 |
| Observações 2–4 do scope_validation (sem mapper de worker type, mapeadores descritivos, 11 known_gaps) | notas para o DD, já absorvidas pelo DD v1.0 (C17); sem impacto |
| Contagens divergentes de lacunas: 11 `known_gaps` (scope_validation, 4-set) × 14 `CO-GAP-01…14` (QA, 7-set) × `CO-GAP-15` (hub) | lote 2: a lista CO-GAP-01…14 está no `scope_manifest.json` e em `07-qa-report.md` da skill, não nos arquivos de `qa/` coletados |
| Datas internas dos relatórios (payslip 2026-07-12, scope 09-04, QA 09-07) × mtime 09-18 | registrado no cabeçalho deste arquivo; sem cartão |
| `audit_v24_ccg.json`, `audit_v24_mechanical.json`, `audit_v24_recheck.json`, `audit_content.log`, `audit_recheck.err`, `alignment.log`, `scope_validation.log`, `qa.log`, `verify_CO.log`, `ccg.log`, `dd.log`, `reports.log`, `sir_index.log`, `si_*.log` | resumos dos mesmos relatórios já extraídos (QA, handover, patch, verificação do Payslip); só as partes novas viraram cartão (C24, C27, C22, C31) |
| Aceitos por desenho do patch (12 linhas Mandatory=Y com texto na coluna G; mappers só de referência; PT) | convenção interna, sem impacto na resposta |
| lote 2 | nenhum item excedeu o limite de 40 cartões; a única entrada é a lista CO-GAP-01…14 acima |
