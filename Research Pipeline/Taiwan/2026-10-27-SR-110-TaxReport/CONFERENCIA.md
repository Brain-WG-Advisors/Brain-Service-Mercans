# SR-110 — Taiwan Tax Report Spec v1.3 (conferência)

> Construtor D, janela Suporte, 2026-10-27. Tudo local: nada foi para Drive, YouTrack, e-mail ou chat. **Rascunho para o usuário revisar.**

## Pedido
Mohit, 15/09/2026: "Spec Review only and fill the gaps in specs", incluindo as 3 issues dele de 23/01/2026 (residente YTD × não residente; "Tax Exemption Amount"; Period From/To). Análise de base: [[SR-110-taiwan-tax-report]] (`rascunhos/2026-10-23-shruti/SR-110-taiwan-tax-report.md`).

## Arquivos
| Arquivo | O que é |
|---|---|
| [[Research Pipeline/Taiwan/2026-10-27-SR-110-TaxReport/Taiwan Tax Report Spec_v1.3.xlsx\|Taiwan Tax Report Spec_v1.3.xlsx]] | Spec v1.3 (md5 `32cd0a803dd3ca530d693727df11e572`, rodada 2; rodada 1 era `50a250e8…`) |
| `edits_v1_3.py` | As células alteradas (rodada 1 + bloco `R2` da rodada 2), valor e se quebra linha |
| `build_v1_3.py` | Geração por XML + zip: só `styles.xml` (fill `FFDDEBF7` e 21 xf acrescentados no fim) e `sheet1/2/3.xml` mudam; as outras 26 partes copiadas byte a byte |
| `verify_v1_3.py` → `comparacao_celula_a_celula.txt` | Comparação base × v1.3: partes do zip, XML com as células editadas mascaradas, célula a célula em todas as abas (valor, fill, fonte, borda, formato, alinhamento, proteção), mesclagens e validações |
| `validacao_toolkit.txt` / `validacao_toolkit_rodada2.txt` | `mercans-artifact-toolkit/scripts/validate_workbook.py` na base e na v1.3 (rodadas 1 e 2) |
| `REVISAO-independente.md` | Revisão independente da rodada 1 (achados 1–9) |

Base: [[raw/docs/drive-exports/2026-10-27/Taiwan Tax Report Spec.xlsx|Taiwan Tax Report Spec.xlsx]] (md5 `8b19384f…`; conteúdo célula a célula igual ao export de 23/10). Para refazer: `python -I -X utf8 build_v1_3.py <base> <saída>` e `python -I -X utf8 verify_v1_3.py <base> <saída> <log>`.

## Fontes
| # | Fonte | Arquivo local |
|---|---|---|
| T1 | MOF/財政資訊中心, **綜合所得稅資料電子申報作業要點, 114年12月修正** (公告 2025-12-10; aplica-se à renda de 114 = 2025, declarada em jan/2026). **Versão mais nova encontrada** (página FIA: https://www.fia.gov.tw/singlehtml/3?cntId=22c32144f9ee4c6d8d6c8b9739e77a7a). Cap. 2, seção 1, pp. 1–24 da seção (PDF pp. 9–32) | [[raw/docs/oficiais/TW/2026-10-27-綜合所得稅資料電子申報作業要點_1141210.pdf\|2026-10-27-綜合所得稅資料電子申報作業要點_1141210.pdf]] (md5 `150a9c87…`) |
| T1-112 | Edição 112 (a que a spec citava), para comparar | [[raw/docs/oficiais/TW/2026-10-27-112年度綜所稅資料電子申報作業要點(公告)_1121211.pdf\|2026-10-27-112年度綜所稅資料電子申報作業要點(公告)_1121211.pdf]] |
| T2 | MOF, 各類所得扣免繳憑單網路申報操作實務 (pp. 4–5 nome do arquivo; pp. 40–46 fluxos IMX) | [[raw/docs/oficiais/TW/2026-10-27-各類所得扣免繳憑單網路申報操作實務.pdf\|2026-10-27-各類所得扣免繳憑單網路申報操作實務.pdf]] |
| T3 | Income Tax Act art. 92 (MOF law-out) | `raw/docs/oficiais/TW/2026-10-23-taxreport-income-tax-act-mof-lawout.html` |
| Int. | WTC V2.8, DD V3.3 (exports de 23/10) | `raw/docs/drive-exports/2026-10-23/` |

Não existe ainda 要點 de 115 (a minuta costuma sair em novembro; o de 114 saiu como 草案 em 13/11/2025). Nenhum ⚠️ de versão: usado o 114.

### 112 × 114 (só o que toca salário)
Diff do texto dos itens (二)各欄項內容 feito por script e lido por mim:
- Campo 20 (item 18(1)): 112 "依勞退條例或教職員退撫條例**自願提繳**之退休金額" → 114 "依勞工、軍公教及政務人員退撫相關法令提(撥)繳(**不計入薪資課稅**)之金額". Mesmo uso para empregado comum (contribuição voluntária do 勞退, não tributada).
- Não residente: prazo de 10 dias a partir do pagamento, **+5 dias** se houver 3+ feriados nacionais seguidos (pagamentos desde 114-01-01) (T1 p. 2–3 da seção; ITA art. 92 §2 igual).
- Campo 19: 14 dígitos (com dia) só para 98A/98B/99A/99B/25A–E/26F; salário continua **10 dígitos YYYMMYYYMM**.
- Itens 2, 5 (50/93), 7, 8–10, 14–17, 20–26 e notas 1–2: sem mudança que afete salário (item 2 ganhou regra de serial para 決算/清算, não se aplica).

## Decisões
1. Correções em H (mapeamento) e J (descrição RA); nas colunas K/L (BA) só onde o mapeamento antigo estava ali (K10, K11, K22, K34, L34): texto "Superseded in v1.3, see H…" com o valor anterior citado (não se perde histórico).
2. Report Matrix: B:C é mesclado, então as regras foram para a coluna B. B6 ("Annual/Monthly") e B10 mantidos (lista de validação); B7 "XLSX" → "TXT" (está na lista; o U8 é texto). A regra residente anual × não residente por pagamento está em B5 e B9.
3. Version Control: linha 14 = 1.3 | 2026-10-27 | resumo | **Under Review** (rodada 2; "Draft" estava fora da validação E13:E23) | Wallisson Gomes. Linhas 1.1/1.2 (propostas na análise) não criadas: o pedido foi só a linha 1.3.
4. Abas Testing/Testing1 **não tocadas** (comparação confirma 0 diferença). Os erros delas (X1 vírgula/33 campos, X11 "1: electronic", X12 UBN) ficam registrados aqui e na B16 ("pre-v1.3 test record").
5. Variáveis que não existem no DD (data de pagamento, admissão/desligamento, endereço do empregador, país de residência, TIN estrangeiro, código de tratado, nome chinês) escritas como `<…>` + "TO BE CONFIRMED BY MOHIT/BA". Nada inventado.

## Antes → depois (rodada 1: 48 células; ver Rodada 2 abaixo)
| Aba | Nº | Células |
|---|---|---|
| Version Control | 5 | B14:F14 |
| Report Matrix | 10 | B4, B5, B7, B8, B9, B11, B12, B13, B14, B16 |
| Spec | 33 | I7, J9, H4, J4, H10, K10, B11, H11, K11, H12, D13, J13, H18, J18, H19, J19, H20, J20, H21, J21, H22, J22, K22, H30, J30, H31, J31, H33, J33, H34, J34, K34, L34 |

| Ponto | Antes | Depois | Fonte (T1 = 要點 114, cap. 2 seç. 1) |
|---|---|---|---|
| Issue 1 Mohit (residente YTD / não residente) | não refletido | RM B5/B9; H10, H11, H18, H22, H33 por status; não residente **por data de pagamento**, não por mês | ITA art. 92 §1–2; T1 itens 25, notas do 貳 |
| Issue 2 / X3 campo 9 | "Tax Exemption Amount", K11 `58100 + 58105` | B11 "Tax Withheld Amount"; H11 50 res. YTD 2552+2572+2582+2592, 93 res. YTD 2594, não res. 2593 | T1 item 9 (扣繳稅額; 0 se 免扣繳, nunca negativo); WTC V2.8 |
| Issue 3 / X6 campo 19 | 01–12 fixo | residente mês de admissão (ou 01) a mês de saída (ou 12); não residente YYYMMYYYMM do mês a que a renda se refere | T1 item 17 |
| X1/X2 formato | XLSX, delimitador "CSV" | TXT; "\|", UTF-8, 32 campos; U8 completo precisa de 申報書 + 申報單位基本資料, ou CSV via IMX → **TO BE CONFIRMED** | T1 參.一, 參.二, 參.三.(一); T2 pp. 5, 41–46 |
| Nome do arquivo | vazio | `{UBN}.{ROC ano}.U8` / `{UBN}.{yyymmdd pagamento}.U8` | T2 p. 5 |
| X4 campo 2 | `$row_number` | residente zero-pad 8; não residente "00" + 6 | T1 item 2 |
| X5 campo 31 | sempre geração | residente geração; não residente data de pagamento | T1 item 25 |
| X7 campo 20 | `$58105` / K 58160 | 2517 (LPN EE) só formato 50 | T1 item 18(1); WTC V2.8 (58105 não existe) |
| X8 campo 28 | senão "ZZ" | senão vazio; ZZ só se país desconhecido | T1 item 22 |
| X9 campo 29 | "XX" | vazio; anexo 42 se tratado aplicado | T1 item 23 |
| X10 campo 32 | "NORTIN" se status = 1 | "NOTIN" por tipo de ID 3/5/6/7/8/9/A | T1 item 26 |
| X13 campo 18 | cidade + distrito + linha 1 + ", " + linha 2 | CEP primeiro, sem vírgulas; estrangeiro sem endereço chinês → empregador | T1 item 16; nota 2 |
| X14 campo 17 | `$employee_name` | regras de nome chinês/passaporte, full/half-width | T1 item 15; nota 2 |
| X15 campo 16 | ano de as_of_date | residente idem (ano do relatório); não residente ano do pagamento | T1 item 14 |
| Campo 10 | "(10−11)" | campo 8 − campo 9, exato, nunca negativo | T1 nota 1, item 10 |
| Campo 11 | Numeric(12) | Alphanumeric(12) (tipo X) | T1 tabela de campos, item 11(9) |
| J9 tipos de ID | [4] "mainland <183", [5] "alien or mainland >183", [6] texto truncado | lista oficial 0–A | T1 item 7 |
| I7 formatos | "53 rental, 51 professional, 9B…" | 50 salário, 93 退職所得 | T1 item 5 |
| X11 / X12 | só na aba Testing | sem mudança (aba não tocada); H28 "2" e H5 UBN já corretos | T1 itens 20, 3 |

## TO BE CONFIRMED BY MOHIT/BA
1. U8 completo (com 申報書 e 申報單位基本資料) × CSV para importar no IMX (RM B16).
2. 6220x (62200:62209) já dentro do 58008? e 6218x fora de 58008/58009 (H10). O WTC não traz fórmula de 58008.
3. Conta do imposto quando formato 93 é pago a não residente (H11).
4. Variáveis: data de pagamento (H18, H33), admissão/desligamento (H21), endereço do empregador (H20), país de residência (H30 — o país do endereço pode ser Taiwan), TIN estrangeiro (H34), código de tratado (H31), nome chinês (H19).
5. Nome da função de zero-pad e se o contador do não residente é por arquivo ou por ano no mesmo UBN (J4).
6. Report Code (RM B4).
7. (rodada 2) 62640:62649 "Pension" e 62930 "Gratuity/EOS/Post-termination": formato 93 ou 50 (J7); função FULLWIDTH (J20) e de largura do nome (J19); variável do contador do não residente por UBN no ano (J4).

## Conferência
- `comparacao_celula_a_celula.txt`: **PASS** — 48 células editadas, todas com o valor pretendido, fill `FFDDEBF7`, fonte/borda/formato mantidos; **0 diferença fora do escopo** em todas as 6 abas (Version Control 1004×26, Report Matrix 17×3, Spec 991×26, Testing1, Testing, Options); 26 partes do zip idênticas; `sheet1/2/3.xml` idênticos à base com as células editadas mascaradas; `styles.xml` só com acréscimos (fills 9→10, cellXfs 87→108); mesclagens e validações iguais.
- XML: as 4 partes alteradas passam no parser (well-formed); desenhos, comentários, hyperlinks (M10/M11) e imagem intactos (partes byte a byte).
- `validacao_toolkit.txt`: C29 acusa 14 marcadores "TO BE CONFIRMED" — **intencionais** (pedido do usuário) — mais 1 pré-existente na aba Testing (G21 "Placeholder"). O contrato `--artifact RSPEC` falha igualmente na base (template antigo, cabeçalhos diferentes); não é regressão.
- Contas e leitura: cada regra do quadro acima relida por mim no PDF 114 (texto extraído e páginas da seção 1). Art. 92 relido no HTML local.

## O que não consegui provar
- Que 2517 seja exatamente o valor "não computado no salário" (o teto de 6% está no 勞工退休金條例; não relido hoje). Mapeamento segue a análise + WTC.
- Se 6220x já está no 58008 (sem fórmula no WTC).
- Anexo 41 (códigos de país) × chave de país do sistema: não comparado.
- Saída atual da configuração depois das mudanças do Manjit (30/01): sem acesso ao ambiente.

## Achados fora do pedido (para o hub [[Taiwan]], não para o ticket)
1. Mudança de não residente para residente no mesmo ano (IMX trata a importação "所得人身分由非居住者轉變為居住者", T2 p. 51): não prevista na spec.
2. DD V3.3, option mapper "Identity Type", key 4: rótulo EN "mainland person living in Taiwan less than 183" × oficial 【4】總機構在中華民國境外之在臺分公司 (o rótulo local do DD está certo; o EN não). Key 6 EN também está errado ("Various Income withholding…").
3. SOP Taiwan 1.1 repete a tradução errada "tax exemption" para o campo 9.
4. Spec J5 ainda cita "page 181 do 112年度…" (campo 3 está certo; só a referência é antiga).
5. Prazo do 扣繳憑單 ao empregado: ITA art. 92 atual = 10/02, **15/02** se janeiro tiver 3+ feriados (análise de 23/10 só citava 10/02).

## Rodada 2 (2026-10-27): achados 1–9 da revisão independente
Cada item relido no 要點 1141210 (texto extraído; páginas do PDF). Rodada 1 × rodada 2: **22 células** (VC 1, Spec 21). Base × v1.3 final: **60 células** (VC 5, RM 10, Spec 45).

| # | Célula(s) | Antes (rodada 1) | Depois | Fonte |
|---|---|---|---|---|
| 1 | H4, J4 | residente `LPAD(row;8;'0')` = "00000001", igual ao do não residente | residente `CONCAT('01'; LPAD(row;6;'0'))` (nunca "00"; sem letra na posição 1, reservada ao 檔案識別碼 A–Y); não residente `'00'` + contador único por UBN no ano (não reinicia por arquivo); TBC (função e variável do contador) em J4 | 要點 114 item 2 (PDF p.24): "非居住者…前２位固定為「００」"; "申報單位統一編號相同時流水號不可重複"; "流水號第1碼應為英文字母大寫A~Y表示之「檔案識別碼」" |
| 2 | H19, J19, H20, J20 | "all full-width or all half-width" + CONCAT de larguras mistas; TBC no H | H19: nome chinês convertido inteiro para full-width; nome do passaporte inteiro half-width. H20: `FULLWIDTH(CONCAT(...))`, CEP incluído (ex.: １００). TBC (função, campo do nome chinês, endereço do empregador) movido para J19/J20 | 參.三.(三) nota 2 (PDF p.32): "此欄位須全部為全形或全部為半形"; itens 15–16 (PDF p.29) |
| 3 | H7, J7, H10, H11, H22 | H7 vazio | H7: um registro por formato; '93' = 62180:62182 (únicas PEs com Severance Tax = Yes no WTC V2.8, conferido por script nas abas WTC e Wage Type Catalogue); '50' = demais contas de H10; empregado com os dois gera 2 registros. H10/H11/H22 começam com "Format per H7". J7: TBC sobre 62640:62649 "Pension" e 62930 "Gratuity/EOS/Post-termination" (tributadas por tabela no WTC; ITA art. 14 cat. 9 inclui 退休金、資遣費、退職金、離職金 no 退職所得) | 要點 114 item 5 (PDF pp.24–26, 【５０】/【９３】); ITA art. 14 (HTML local) |
| 4 | VC!E14 | "Draft" | "Under Review" (na lista) | validação E13:E23 |
| 5 | I22 | "Applies to retirement payments only" | contribuição voluntária do empregado, só formato 50, vazio no 93 | item 18(1) |
| 6 | L10, L11 | "Non-resident: Monthly…" | "Superseded in v1.3, see H10/H11" + texto anterior | ITA art. 92 §2; item 25 |
| 7 | G31 | "TW" | "(blank)" | item 23 (anexo 42 ou vazio) |
| 8 | D18, D21, D28, D33 | Numeric(3/10/1/4) | Alphanumeric(3/10/1/4) | tabela de campos (PDF p.13–14): 16 X3, 19 X10, 26 X1, 31 X4 |
| 9 | J5, J8 | "page 181 of 112…", "Page 179" | 要點 114 item 3 (PDF p.24) + anexo 7/7-1 (pp.188–189); item 6 (PDF p.27) + anexo 6/6-1 (pp.186–187) | páginas conferidas no PDF 114 |

**Conferência rodada 2:** `comparacao_celula_a_celula.txt` (seções 1–4) **PASS**: 60 células com valor pretendido e `FFDDEBF7`, 0 diferença fora do escopo em todas as abas; 26 partes do zip idênticas; `sheet1/2/3.xml` idênticos à base com as células mascaradas; `styles.xml` só com acréscimos (fills 9→10, cellXfs 87→111); 4 partes alteradas well-formed. Seção 4 = rodada 1 × rodada 2 (só as 22 células acima). Toolkit C29: 15 marcadores "TO BE CONFIRMED" intencionais + 1 pré-existente (Testing!G21).

**Novos TO BE CONFIRMED BY MOHIT/BA (rodada 2):** 62640:62649 e 62930 em 93 ou 50; função FULLWIDTH; variável do contador do não residente. Amostras G18/G21 continuam numéricas (fora dos achados; não alteradas).

## Linhas por frente
| Data | Frente | O quê |
|---|---|---|
| 2026-10-27 | Suporte (construtor D) | v1.3 gerada (48 células, 要點 114), comparação célula a célula PASS, comentario.md em rascunho; nada enviado nem copiado para o Drive |
| 2026-10-27 | Suporte (construtor D, rodada 2) | achados 1–9 da revisão independente corrigidos (22 células; total 60), comparação PASS, md5 `32cd0a80…`; comentario.md atualizado; nada enviado |

## Arquivos da entrega
- [[Research Pipeline/Taiwan/2026-10-27-SR-110-TaxReport/REVISAO-independente|REVISAO-independente]]: Revisão independente da Tax Report spec v1.3 Taiwan: FAIL rodada 1, 3 MAJOR, fonte MOF 1141210 conferida.
- [[Research Pipeline/Taiwan/2026-10-27-SR-110-TaxReport/comentario|comentario]]: Rascunho de comentário (EN, não postado) sobre a spec v1.3 e os 3 pontos do Mohit.
