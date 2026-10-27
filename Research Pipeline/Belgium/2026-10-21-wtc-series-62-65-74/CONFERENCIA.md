# BE-WTC — séries 62, 65 e "74" contra o Global WTC (2026-10-21)

Pedido: Suman (09/10, cobrado em 21/10), via janela Chat. Prazo BE: dia 30. Ligado a [[Belgica]].

## Base (regra 8 / base-linhagem-drive)
- Drive: `Belgium › 03 - WTC › BE-WTC-001-v1.0.gsheet` (exports em Downloads de 09/10 e 16/10).
- Pipeline: `~/mercans-pipeline/BE-compliance/02-wtc/BE-WTC-001-v1.1.xlsx` (16/09).
- **Aba Wage Type Catalogue idêntica** nas três (359 linhas, 0 diferenças célula a célula, A–T). Só o Version Control difere.
- Base usada: **export do Drive de 16/10** (`Downloads\BE-export-2026-10-16\BE-WTC-001-v1.0 (1).xlsx`, md5 `ed2446ae7699b7d318ef9b2edb989791`).

## Fonte do Global WTC
| Arquivo | Onde | 62 / 65 / 79 |
|---|---|---|
| Global Wage Type Catalogue **1.1** (xlsx exportado em 19/10) | `Downloads\Global Wage Type Catalogue 1.1.xlsx`, aba "Earning, Deductions, Contributi" | 418 / 148 / 73 |
| Global Wage Type Catalogue **1.2** | só `.gsheet` (`Country Folders/Argentina/`, cópias de 20/08 e 05/10) | lida em 21/10 pelo Chrome, cópia de **05/10** (id `15DAp9ykwGenQiWs1WXNhHHumItH36EI7FEYq3mcgvCY`, aba "Earning, Deductions, Contributions Classifications", visualização gviz, sem download): **708 códigos 62/65/79 idênticos à 1.1** em código, nome e tipo (mesmo hash da lista concatenada). A cópia de 20/08 não foi lida (é anterior) |
| Global WTC V1.0 (baseline do pipeline) | `~/mercans-pipeline/shared/Global_WTC_V1_0.xlsx` | 241 / 0 / 0 |

Usada a **1.1**; conferida contra a 1.2 (vigente) em 21/10: nas séries 62/65/79 não há diferença, então a v1.1 do WTC já está completa contra a 1.2.

## Decisões (usuário, 21/10: "ok nas 4")
- D1. "74" = **79** (Leave Payout Earnings). A série 74 não existe no Global 1.1, no HRB_Global_Pay_Elements_20231206 nem nos WTCs de país em Downloads. Confirmar com a Suman na entrega.
- D2. Começar pela Global 1.1; a 1.2 entra quando for exportada.
- D3. Incluídos os 69 códigos de 4 dígitos (6201–6289), como no CG v3.1 e no CI v1.1.
- D4. Versão **v1.1** (o Drive está em v1.0; a v1.1 do pipeline nunca foi para o Drive).

## Decisões de construção (Pipeline)
- Linhas novas **no fim do catálogo (361–828)**, depois de BE-059: nenhuma referência existente a número de linha muda (Version Control, Global WTC Coverage, specs Belcotax citam linhas).
- Coluna B = nome do Global 1.1 sem alteração; C = tradução para holandês (como as linhas existentes).
- Tratamento (E, G, J, N–R) **copiado da linha BE equivalente** já existente, cuja coluna F traz a base legal. A coluna F da linha nova diz qual é a linha equivalente (código e número da linha). Mapa completo: `mapeamento-v1.1.csv`.
  - "Arrears" de item tributável comum → padrão de 62101 (Tax Code 252, Table Tax No, Special Tax Yes).
  - "Adjustment / Advance / Addition" → mesmo tratamento da linha equivalente; Occurrence = Additional.
- 17 códigos sem tratamento belga → **NA** com motivo na coluna F: 6213 e 62909 (a Bélgica não tem gratuity de fim de serviço; ver 62900); 62940–62949 (contractors fora da folha); 79410 (licença não remunerada sem pagamento; ver 62109/21109); 62810, 62811, 62820 e 62821 (parking e donation recovery: tratamento belga não estabelecido nesta revisão).
- Colunas laranja (D, H, I, K, L, M, S, T) ficam vazias, como nas linhas existentes.
- Destaque **azul claro FFDDEBF7** em A–T das 468 linhas. Obs.: um comentário do modelo no Version Control pede amarelo para mudanças; segui a regra do cérebro (azul).
- Edição por XML (sem `openpyxl.save`): imagem, comentários e validações preservados. Script: `build_wtc_v1_1.py`.

## Resultado
| Série | Global 1.1 | Antes no BE | Acrescentados |
|---|---|---|---|
| 62 (5 dígitos) | 349 | 240 | 178 |
| 62xx (4 dígitos) | 69 | 0 | 69 |
| 65 | 148 | 0 | 148 |
| 79 | 73 | 0 | 73 |
| **Total** | | | **468** |

Distribuição do tratamento: 316 Tax Yes / SS Yes; 102 isentos (No/No); 23 Tax Yes / SS No; 8 Tax Yes / SS Yes-No; 19 NA.
Linhas equivalentes mais usadas: 62670 (98: "Benefit earning" 65800–65899 e benefícios genéricos), 62966 (62: "Other leave payout"), BE-059 (52: reembolsos de despesa), 62220 (21: bônus genéricos).

## Antes → depois
- `Wage Type Catalogue`: linhas 361–828 (eram vazias e formatadas) → 468 códigos novos. Linhas 2–360 sem alteração.
- `Version Control` B14:F14: vazio → `1.1 | 21/10/2026 | Added the Global WTC 1.1 codes missing from the 62, 65 and 79 series (...) | Under Review | Wallisson Gomes`.
- Demais abas: sem alteração.

## Conferência (2026-10-21)
- Partes do xlsx alteradas: só `sheet1.xml` (VC), `sheet2.xml` (WTC) e `styles.xml`; as outras são cópia byte a byte.
- Célula a célula contra a base, em todas as abas: as únicas diferenças são WTC 361–828 e VC B14:F14.
- 468 linhas novas × lista de faltantes: código e nome iguais ao Global 1.1, linha por linha. E/G/J/N–R iguais ao `mapeamento-v1.1.csv`. C e F preenchidos, colunas laranja vazias, todas com fill FFDDEBF7. A linha 829 continua vazia.
- `validate_workbook.py --artifact WTC`: **PASS** (0/0/0).
- `diff_wtc_baseline.py` (contra Global V1.0): MISSING 0; RENAMED 299. Já era assim **antes** (o build de 2026-08/09 renomeou as descrições Global nas linhas existentes). Não mexi; é achado fora do pedido.
- Lint C29 (TODO/TBD/placeholder…): 0 ocorrências nas linhas novas.
- md5 v1.1: `40597553aa126f026574c41cc18bcf56`.

## Pendências / achados fora do pedido
- ~~Global 1.2: exportar e refazer o cruzamento~~ → feito em 21/10: idêntica à 1.1 nas três séries.
- Revisão dos 2 grupos (21/10): a regra jurídica de 65800–65899 é a da linha 62670 e a de 62891–62999 é a da linha 62890, ambas da v1.0 aprovada (texto relido). Não consegui reler a fonte primária do ONSS: `socialsecurity.be` estava fora do ar em 21/10 ("Application is not available"). A escolha da linha equivalente para slots genéricos é convenção nossa e está declarada na coluna F.
- A aba "Global WTC Coverage" cobre só a base de 300 códigos; não foi estendida (fora do pedido).
- RENAMED 299 (acima): a decisão de manter os nomes belgas é anterior.
- Para 62810/62811 (parking) e 62820/62821 (donation recovery), é preciso decidir o tratamento belga, com fonte, se algum cliente usar.
- Revisão de conteúdo sugerida antes do Drive: 65800–65899 → 62670 (benefício sem isenção própria) e 62891–62999 → 62890 (opções da Lei de 26/03/1999), com alternativas indicadas na coluna F.

## v1.2 (2026-10-21) — taxa patronal da linha 23671
- Pedido do usuário: buscar a fonte oficial e responder sobre a linha 23671 (24,92%).
- **Fonte:** instruções administrativas ONSS, "Les cotisations". O site `socialsecurity.be` e o `ejustice` estavam fora do ar em 21/10; lida pelo Chrome a edição **2025/4**, cópia arquivada em 07/12/2025 (web.archive.org). A mesma página foi lida no site em 13/10.
  - "Le pourcentage de cotisation globalisé": setor privado 24,92% a partir do 1º tri/2015; "Conséquence du tax-shift": categorias 1 e 3 da redução estrutural → **19,88% a partir do 1º tri/2018** (Lei de 26/12/2015 e Lei de 16/05/2016). Repartição patronal: pensões 8,86; saúde 3,80; indenizações 2,35; desemprego 1,46; doenças profissionais 1,00; acidentes de trabalho 0,30.
  - "La cotisation de modération salariale": categorias 1 e 3 → **máximo de 5,12% [(19,88 × 0,0427) + 4,27]**.
- **Antes → depois:** Wage Type Catalogue!F58 "basic employer contribution 24.92% (...) giving a facial rate of approximately 25% after the tax shift" → "19.88% from Q1 2018 (...) plus wage moderation of at most 5.12% (...) approximately 25.00%" (o resto da célula, operários e BE-033, igual). VC B15:F15 = linha 1.2.
- A outra ocorrência de 24,92% (linha 120, 62180) é uma faixa da tabela nr. 58 de retenção, sem relação com a taxa patronal. Não mexi.
- **Conferência:** célula a célula contra a v1.1 em todas as abas, só F58 e VC B15:F15 mudaram; F58 em FFDDEBF7; `validate_workbook.py --artifact WTC` PASS; md5 `407411a16d27f98e04698782a9c76b72`. Script: `build_wtc_v1_2.py`.
- Copiado para o Drive em 21/10 com ok do usuário (`Belgium › 03 - WTC › BE-WTC-001-v1.2.xlsx`, md5 idêntico `407411a16d27f98e04698782a9c76b72`). Skill republicada (v3) citando a v1.2.

## v1.3 (2026-10-22) — aba "All Codes" do Global WTC 1.1
- **Pedido da Suman (DM, 22/10 03:04):** "this is 79 series" (fecha a D1) + "Please use this complete Global WTC for creating the one for Belgium" (link: Global Wage Type Catalogue 1.1, id `1zRVe25LJ_gzn8SQUGM8UVtiQtB07jCvfmx0ptxULCE0`, aba **All Codes**, gid 1123343809, 6.884 códigos). A v1.1 tinha usado a aba "Earning, Deductions, Contributions Classifications".
- **Leitura:** pelo Chrome, export csv em memória (sem download), 22/10. Séries 62/65/79 na All Codes: 489 / 142 / 413 = 1.044 códigos, sem duplicata. **Faltavam 355** na v1.2: 62105; 65110–65119; 65508, 65509, 65609, 65659; série 79: 183 unidades de licença (Leave/Unit), 105 acumulados taken/balance/increment (Cumulative/Unit), 52 "calculated payout days" (Earning/Amount/Additional). Na outra direção, 65880–65899 (20) estão na BE (vindos da aba de classificação) e não na All Codes: mantidos.
- **Decisões de construção:** linhas 829–1183 (as 829–1000 já existiam vazias; 1001–1183 criadas), azul, mesmos estilos da v1.1.
  - 62105 (rate) → Intermediary, NA, remete à 62100.
  - 65110–65119 (despesa da contribuição patronal) → Employer Contribution, NA, segue a 23671.
  - 65508/65509 → 62500; 65609 → BE-057; 65659 → BE-056 (tratamento copiado).
  - Unidades e acumulados 79 → Intermediary, NA (contador, não pagamento), remetendo à linha 794NN do mesmo tipo de licença; 79010/79110/79210 remetem a 62109/21109; "General Leave Unit" remete às linhas 79401–79499.
  - 795NN → tratamento copiado da 794NN (79510 = NA, licença não remunerada).
  - Nomes = All Codes sem alteração (inclusive 79240, que no Global se chama "Other leave 39 year 1 transitional taken" no bloco de saldos); holandês por padrão (opgenomen, saldo, opbouw, eenheid, berekende uitbetaling).
- **Conferência:** só `sheet1.xml` (VC B16:F16) e `sheet2.xml` mudaram; célula a célula contra a v1.2: só VC B16:F16 e WTC 829–1183 (4.260 células = 355 × 12). 355 códigos únicos, em ordem, contagem por tipo igual à leitura (183/105/52/10/4/1). C e F preenchidos, laranja vazia, 7.100 células com FFDDEBF7. Lint 0. `validate_workbook.py` PASS; `diff_wtc_baseline.py` MISSING 0 / RENAMED 299 (igual à v1.2). md5 `def7afa421b56337aa3b306591f369de`. Script `build_wtc_v1_3.py`; auditoria `mapeamento-v1.3.csv`.
- Copiado para o Drive em 22/10 com ok do usuário (`Belgium › 03 - WTC › BE-WTC-001-v1.3.xlsx`, md5 idêntico `def7afa421b56337aa3b306591f369de`). Resposta à Suman deixada **digitada no DM, não enviada** (pergunta: só 62/65/79 ou todas as séries da All Codes).

## Frentes que mexeram
- 2026-10-21 · Pipeline · cruzamento Global 1.1 × WTC BE (62/65/79), conferência da base Drive × pipeline, CSV de faltantes.
- 2026-10-21 · Pipeline · BE-WTC-001-v1.1.xlsx gerado e conferido (468 linhas).
- 2026-10-21 · Pipeline · com ok do usuário, copiado para o Drive `Belgium › 03 - WTC › BE-WTC-001-v1.1.xlsx` (md5 idêntico `40597553aa126f026574c41cc18bcf56`). O `.gsheet` v1.0 ficou intacto; o usuário importa. Nada enviado à Suman.
- 2026-10-21 · Pipeline · WTC v1.2 (linha 23671, 19,88% + moderação até 5,12%, fonte ONSS 2025/4) gerada, conferida e copiada para o Drive com ok do usuário (md5 idêntico).
- 2026-10-22 · Pipeline · v1.3 (355 códigos da aba All Codes, a pedido da Suman) gerada e conferida localmente.
- 2026-10-22 · Pipeline · v1.3 copiada para o Drive com ok do usuário (md5 idêntico); mensagem à Suman em rascunho no DM.
- 2026-10-22 · Pipeline · com pedido do usuário, v1.3 importada pelo Chrome no `.gsheet` BE-WTC-001-v1.0 (Arquivo › Importar › Substituir planilha). Conferido via gviz: VC até 1.3; 1.123 códigos numéricos, 6201–79999, soma 71.433.862 = arquivo local; amostras 23671/62105/65110/79240/79506/79999 iguais.
- 2026-10-23 · Pipeline · Suman confirmou o escopo (só 62/65/79): v1.3 é a final. Skill BE v4 publicada citando a v1.3.
