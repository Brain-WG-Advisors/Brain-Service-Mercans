# Lituânia — research dos reports (SAM, GPM313, GPM312) × specs do Drive — conferência

Origem: call do Wallisson (27/10): refazer a research dos reports a partir das fontes oficiais vigentes, cruzar com as specs do Drive (que ele não confia) e abrir um ticket por report. Caminho B decidido pelo usuário: research focada nos reports, com o método do pipeline, sem rodar o script completo.

Hub: [[Lituania]] · Atualização 2026 dos artefatos de cálculo: [[Research Pipeline/Lithuania/2026-10-27-atualizacao-2026/CONFERENCIA]].

## Specs comparadas (`specs-drive/`)
| Spec | Origem | Base declarada na própria spec |
|---|---|---|
| LT-SODRA-003-SAM-Spec v1.0 (2026-08-21) | export 10/10 do `.gsheet` (Drive sem alteração depois de 24/08) | `sam-v07.mxfd` + ordem V-243 (redação V-624/2018) |
| LT-VMI-001-GPM313-Spec v1.0 (2026-08-21) | export 10/10 do `.gsheet` | VA-121 na redação VA-105 (2025-11-20) |
| LT-VMI-002-GPM312-Spec v1.0 (2026-08-21) | Drive `.xlsx` (md5 72dea6b0bac798ae31e08a8e273195ab) | VA-9 na redação VA-24 (2026-03-26) |

## Fontes oficiais lidas
- **Sodra (pelo navegador, sodra.lt bloqueia script):** página do SAM (atualizada 2026-05-11), instrução de preenchimento (pontos 48–56, atualizada 2025-07-31) e MXFD `sam-v07.mxfd` (FormDef 2021-12-22) → `raw/docs/oficiais/LT/2026-10-27-Sodra-SAM/2026-10-27-sodra-SAM-v07-instrucao-e-MXFD_extrato.md`.
- **VMI (agente, pelo EDS; MXFDs abertos e conferidos por mim):** GPM313.mxfd (FormDef 2025-11-04; zip md5 dd3200bb…), GPM312.mxfd (FormDef 2026-05-11; zip md5 0ea0d014…), IN_GPM313 (texto `nuo_2026`, VA-105), IN_GPM312 (VA-24) → `raw/docs/oficiais/LT/2026-10-27-VMI-reports/`; pack em `research/VMI-GPM313-GPM312-research.md`.
- Pack do agente da Sodra (`research/Sodra-SAM-research.md`) ficou só com a V-243 de 2015; substituído pela leitura direta acima.

## Resultado por report

### SAM (Sodra) — spec ALINHADA
- Os 67 campos lógicos da spec (página SAM, SAM3SD, SAM3SDP) são exatamente os do `sam-v07.mxfd` vigente: nenhum a mais, nenhum a menos (comparação por script dos nomes XML).
- Batem com a instrução vigente: prazo dia 15 do mês seguinte (p. 52); anexos SAM3SD/SAM3SDP (p. 48, 51); códigos de motivo 01–10 (p. 51.2; lista do MXFD); A11 sem renda de esporte/artista, direitos autorais e tantiemas (p. 55.1); P3 = tarifa total no início do mês (p. 55.5); 6 linhas por folha no SAM3SD e 3 no SAM3SDP (MXFD).
- **Diferenças: nenhuma.** Ponto em aberto (não é erro da spec): a fonte não define a composição da "tarifa total" (P3) — fica como pergunta ao Development/Sodra se necessário.

### GPM313 (VMI) — conteúdo ALINHADO, formato eletrônico DIVERGENTE
- Conteúdo igual à regra vigente (VA-121/VA-105, texto `nuo_2026`): 12 campos, prazo dia 15, divisão do GPM pela data de pagamento até/depois do dia 15, faixas 20/25/32% e 15% sobre benefícios.
- **D1 — Formato:** a spec diz que não existe arquivo/XML ("no FFData or XML envelope", "Position notional"). Existe: o formulário é FFData gerado pelo MXFD GPM313 (upload ao EDS `EDSMdocUploadService`), com nomes `B_MM_ID`, `B_MM_Pavadinimas`, `B_ML_Metai`, `B_ML_Menuo`, `G5`…`G12`.
- **D2 — Tamanhos:** nome do pagador 200 → **116** (58 × 2 células); campos 5–12 15 → **14** dígitos com 2 decimais. (Campo 1 = 11, ano = 4, mês = 2: iguais.)

### GPM312 (VMI) — conteúdo ALINHADO à VA-24, formato eletrônico DIVERGENTE
- Conteúdo igual à VA-24/2026: 63 códigos de renda (iguais aos do 2 priedas, sem o 06), marcadores L7 D/M/P/C e U7 D/M/P/C/U, alíquota de 25%, prazo 15 de fevereiro.
- **D3 — Formato:** mesma afirmação incorreta do GPM313 ("no FFData or XML"). Existe o MXFD GPM312 (páginas `GPM312`, `GPM312L`, `GPM312U`; nomes `B_MM_ID`, `B_MM_Pavad`, `G4`–`G7`, `L1-n`…`L13-n`, `U1-n`…`U15-n`, `LapoNr`).
- **D4 — Tamanhos (spec → MXFD):** nome do pagador 200 → 116; G4–G7 15 → 14; L1/U1 14 → **20**; L3/U3 70 → **34**; L8/U8 15 → **12**; L10, L11, L13, U10, U11 15 → **11**; L12/U14 3 → **2**; U12 "YYYYMMDD" (8) → **Date** (10 células, AAAA-MM-DD); U13 20 → **24**; U15 200 → **68**.

## Conclusão
As specs não estão erradas no conteúdo de 2026. O SAM está pronto. GPM313 e GPM312 precisam de uma v1.1 só para o formato eletrônico (existência do FFData/MXFD, nomes XML e tamanhos dos campos), porque o Development vai gerar o arquivo a partir delas.

## Etapas 1–2 — specs v1.1 (GPM313 e GPM312)
Arquivos: `LT-VMI-001-GPM313-Spec_v1.1.xlsx` (52 células alteradas) e `LT-VMI-002-GPM312-Spec_v1.1.xlsx` (105), todas em `FFDDEBF7`; edição direta no XML.
- Formato: coluna H = nomes XML do MXFD; coluna I = células do MXFD; File Structure (container FFData; L 10 e U 5 linhas por página); Report Matrix H2/J2; Version Control 1.1.
- Da revisão independente (1ª passada, 4 achados): mês sem zero (MXFD lista 1–12); textos que ainda diziam "sem layout"/"largura não publicada"; U12 como Date AAAA-MM-DD; L9/U9 como lista fechada do MXFD (L9 0/5/15/20/25/27/32; U9 + 7,5/10, sem verificar o uso de 27/7,5/10 em 2026); campos 5–7 (GPM313) e 4–6 (GPM312) como "C" (regra 4; IsRequired false); amostra do U1/U2 (regra 42: U1 só para código lituano).
- Checagens: (1) fonte — MXFD GPM313/GPM312 e IN313 `nuo_2026`/IN312 VA-24 da pasta `raw/docs/oficiais/LT/2026-10-27-VMI-reports/`; (2) mecânica — diff v1.0 × v1.1, nenhuma célula alterada sem destaque, `validate_workbook.py` PASS; (3) contas — tamanhos = células × linhas do MXFD (12/12 e 41/41 campos); (4) coerência — busca por frases antigas ("no FFData", "notional", "YYYYMMDD", "07"…) sem resto; (5) revisão independente — 2ª passada: todos resolvidos, 1 detalhe de formato (20,00 × 20.00) corrigido.

## Bloco 1 (27/10) — alíquotas L9/U9
- Validação do MXFD GPM312 para períodos ≥ 2026: L9 aceita 0/5/15/20/25/32; U9 aceita 0/5/7,5/10/15/20/25/32 (7,5 e 10 só no código 62); 27% sem código desde 2020. GPMĮ 2026 não tem 27%, 7,5% nem 10%. Spec GPM312 v1.1: J22, J39 e Field Options E90 atualizados; validador PASS.
- Códigos de erro do SAM (PDF da Sodra): não lidos (o site bloqueia o leitor de PDF); não constam dos e-mails.

## Não conferido
- Textos consolidados VA-121/VA-105/VA-9/VA-24 no e-TAR (o conteúdo veio dos textos publicados pela própria VMI no EDS); datas de entrada em vigor da VA-105 e da VA-24.
- XSD do FFData (a VMI e a Sodra só publicam o MXFD).
- Regras e códigos de erro da spec do SAM além dos campos (ex.: códigos C23xx, PT).

## Pesquisas (packs)
- [[Research Pipeline/Lithuania/2026-10-27-reports/research/VMI-GPM313-GPM312-research|VMI GPM313/GPM312]]: fontes oficiais 2026 com citação por ponto; base das specs v1.1.
- [[Research Pipeline/Lithuania/2026-10-27-reports/research/Sodra-SAM-research|Sodra SAM]]: ⚠️ **substituído, não usar como fonte**: só achou a ordem V-243 na redação de 2015; a SAM foi conferida pela leitura direta no navegador (seção Fontes acima).

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-10-27 | pipeline | Research dos 3 reports e comparação com as specs v1.0 do Drive; nada alterado no Drive |
| 2026-10-27 | pipeline | Drive: specs GPM313/GPM312 `_v1.1.xlsx` em 18 - Statutory Reports (import nas planilhas após aval); md5 conferido |
| 2026-10-28 | pipeline | Drive: cópias `_v1.1.xlsx` das specs apagadas a pedido do usuário; ficam só as `.gsheet` oficiais (v1.1 importada) |
| 2026-10-28 | geral | Links das notas para o grafo do Obsidian (seções/pesquisas/arquivos principais); conteúdo não alterado |
