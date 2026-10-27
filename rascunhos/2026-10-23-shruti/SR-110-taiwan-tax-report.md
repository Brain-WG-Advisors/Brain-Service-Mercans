# SR-110: TW, Tax Report (各類所得扣繳暨免扣繳憑單: anual residente, por pagamento não residente)

> Análise só leitura, 2026-10-23 (janela Suporte). Nada foi postado, enviado nem gravado no Drive.

## Metadados
| Campo | Valor |
|---|---|
| Ticket | SR-110, "TW - Tax Report" (https://youtrack.hrblizz.dev/issue/SR-110) |
| Estado / fase | In Review / Specification Phase - Research Analyst |
| Assignee | Wallisson (wgomes), vindo da Manju → Shruti |
| BA / RA / Dev | Mohit Jain / Manju Shetija / Katrin Rudi (mudanças feitas por Manjit Bali) |
| Reporter | Lisa Quan, criado em 2025-03-10 |
| Spec analisada | `raw/docs/drive-exports/2026-10-23/Taiwan Tax Report Spec.xlsx` (Version Control: só "1.0 In Progress"; `.gsheet` no Drive alterado em 19/03/2026) |
| Referências | `SR-110-Tax-report-sample-LisaComment.xlsx` (amostra da Lisa, layout MOF em CSV); Drive `G:\...\Taiwan\01 - SOP\Report\Tax\` |

## O que foi pedido a nós
Mohit, 15/09/2026: "Spec Review only and fill the gaps in specs. Assign back to me once done for Testing and Development."
Pontos herdados: as 3 issues do Mohit (23/01/2026), que o Manjit disse ter resolvido (30/01/2026).

## Histórico do ticket
- 2025-03-13 Lisa anexa a amostra. 2025-07-09 Mohit: sem descrição de campo, não dá para mapear.
- 2025-07-17 a 08-14 Lisa e Brenet completam descrições (colunas J/L/M/P).
- 2026-01-23 Mohit lista 3 issues: (1) residente (status 0) em modo YTD, senão mensal; (2) "Tax Exemption Amount is not coming"; (3) Period From/To hardcoded: residente = mês de admissão (ou 01) a mês de saída (ou 12); não residente = "month start and end date".
- 2026-01-30 Manjit: "The above changes has been done", propõe revisar junto.
- 2026-09-15 Mohit: atribuído para revisão de spec.

## Fonte primária
Cópias em `C:\Users\instituto\Documents\brain-service\raw\docs\oficiais\TW\` e no Drive (só leitura).

| # | Fonte | Arquivo local | O que prova |
|---|---|---|---|
| T1 | MOF, "112年度綜所稅資料電子申報作業要點" (formato oficial de e-filing; versão mais nova encontrada na máquina) | `G:\Drives compartilhados\Compliance Team\Country Folders\Taiwan\01 - SOP\Report\Tax\112年度綜所稅資料電子申報作業要點(公告)_1121211.pdf` (cap. 2, seção 1, pp. 4–22 da seção = pp. 11–29 do PDF) | Arquivo: UTF-8, campos separados por "\|", 32 campos (31 separadores), vazio = separadores juntos. Deve conter também o 申報書資料 e o 申報單位基本資料 (sem eles, "一律退查"). Regras campo a campo (abaixo) |
| T2 | MOF, "各類所得扣免繳憑單網路申報操作實務" | `G:\...\Tax\各類所得扣免繳憑單網路申報操作實務.pdf` (pp. 4–5, 41–46) | Nome do arquivo: residente `UBN(8).ROC年(3).U8`; não residente `UBN(8).data de pagamento(7).U8`. Caminhos aceitos: arquivo U8 completo (32 campos + 申報書 + 基本資料) direto; ou importar no IMX (CSV Big5 → U8, ou TXT 250 bytes) e gerar lá |
| T3 | Income Tax Act (所得稅法), MOF law-out (alterado em 2026-09-11) | `2026-10-23-taxreport-income-tax-act-mof-lawout.html` | art. 92 §1: residente, imposto recolhido até o dia 10 do mês seguinte; 扣繳憑單 ao fisco até o fim de janeiro do ano seguinte (até 05/02 se houver 3+ feriados) e ao contribuinte até 10/02. §2: não residente, recolhimento e 扣繳憑單 em até 10 dias da retenção (+5 se houver 3+ feriados) |
| T4 | MOF eTax, Q&A 1505 (atualizado em 2026-04-10) | `2026-10-23-taxreport-etax-QA1505-salary-withholding.html` | Não residente: 18% do total mensal; 6% se o total mensal ≤ 1,5× o salário mínimo (desde 2009). Fonte: 各類所得扣繳率標準 e 薪資所得扣繳辦法 (secundária oficial; o texto do regulamento não foi relido) |
| T5 | MOF, calendário fiscal 115 | `2026-10-23-taxreport-mof-tax-calendar-115.pdf` | Renda de 114 (2025): declaração de 01/01 a 02/02/2026; entrega ao contribuinte até 10/02 |

Fontes internas (secundárias): WTC V2.8, DD V3.3, Country SOP Taiwan 1.1 (frequência e prazos batem com T3).

## Estado da spec
Abas: `Report Matrix` (quase vazia), `Spec` (32 campos, colunas H mapeamento TA/BA, I–M descrições, P mapeamento do imposto), `Testing1` (saída CSV de 4 linhas) e `Testing` (outra tabela de campos, com descrições divergentes).

### Lacunas
| Linha | Campo | Situação |
|---|---|---|
| RM | Report Code, Frequency, File Name, Grouping, Currency, Rounding, Introduction | vazios; Dataset "Annual/Monthly" sem regra |
| RM | File Format / Delimiter | "XLSX" e "CSV" (ver conflito X1) |
| B10 | Total Payment | sem mapeamento na col. H; regra só na K |
| B11 | Tax withheld | col. H vazia; K e P divergem (X3) |
| B12 | Net Amount | só "(line 10 − line 11)" |
| B19 | Employee name | sem regra de full-width / nome de estrangeiro |
| B21 | Period | hardcoded 01–12 (X6) |
| B22 | Voluntary pension | H e K apontam para PEs diferentes, nenhum certo (X7) |

### Conflitos com a fonte oficial
| # | Campo (nº oficial) | Spec hoje | Fonte oficial | Fonte |
|---|---|---|---|---|
| X1 | Formato do arquivo | XLSX; delimitador "CSV"; `Testing1` com vírgula e campos completados com espaços | U8: UTF-8, "\|", vazio sem espaços; no IMX entra CSV Big5. Na `Testing1`, o endereço com ", " quebra a linha em 33 campos (2ª linha) | T1 p. 11–12; T2 pp. 5, 41 |
| X2 | Conteúdo do arquivo | só o registro de renda | O arquivo direto precisa também do 申報書資料 e do 申報單位基本資料; senão, gerar no IMX | T1 p. 11; T2 pp. 45–46 |
| X3 | 9 扣繳憑單扣繳稅額 ("Tax Exemption Amount") | nome errado; K11 = `58100 + 58105` (58100 = "Meal Allowance Pre-Tax Deduction"; 58105 não existe no WTC V2.8) | **Imposto retido** (zero se isento, nunca negativo). A coluna P da Lisa está certa: residente 2552+2572+2582+2592 YTD; formato 93 = 2594 YTD; não residente 2593 | T1 p. 12 (campo 9) e p. 25 item 9 |
| X4 | 2 流水號 | `$row_number` | Residente: 1º–2º alfanuméricos, 3º–8º dígitos. **Não residente: começa com "00"**, 3º alfanumérico, 4º–8º dígitos. Sem repetição no mesmo UBN | T1 p. 21 item 2 |
| X5 | 31 檔案製作日期/非居住者所得給付月日 | sempre data de geração (MMdd) | Residente: data do arquivo; **não residente: data do pagamento** (MMDD) | T1 p. 27–28 item 25 |
| X6 | 19 所得所屬期間 | `CONCAT(ano−1911;'01';ano−1911;'12')` fixo | 10 dígitos YYYMMYYYMM, ano e mês de início e fim da renda (ano ROC 3, mês 2) | T1 p. 26 item 17 |
| X7 | 20 自願提繳之退休金額 | H22 `$58105` (inexistente); K22 `58160` ("Severance Base Before Exemption") | Pensão **voluntária do empregado** pela 勞退條例 (salário); 0/vazio se não houver | T1 p. 26 item 18(1); WTC: 2517 "LPN EE" |
| X8 | 28 居住地國或地區代碼 | código do país se tipo ∈ {3,5,6,7,8,9,A}; **senão "ZZ"** | Para os outros tipos o campo é **vazio**; "ZZ" só quando não se sabe o país | T1 p. 27 item 22 |
| X9 | 29 租稅協定代碼 | "XX" fixo para tipos 5–9 | Código do anexo 42 ou vazio. "XX" não existe no anexo 42 | T1 p. 27 item 23; anexo 42 (p. 245) |
| X10 | 32 稅務識別碼 | `'NORTIN'` se `residential_status = 1` | Para tipos 3,5,6,7,8,9,A: TIN do país de residência ou **"NOTIN"**; vazio para os outros. Condição é o tipo de ID, não o status | T1 p. 28 item 26 |
| X11 | 26 憑單填發方式 | "2" (correto) | 1 = não emite, 2 = eletrônico, 3 = papel; nunca vazio. A aba `Testing` diz "1: electronic; 2: paper" (errado) | T1 p. 27 item 20 |
| X12 | 3 統一編號 | `company_registration_number` (correto) | UBN de 8 dígitos. A aba `Testing` aponta `social_security_integrate_number` | T1 p. 21 item 3 |
| X13 | 18 所得人地址 | `CONCAT(cidade; distrito; linha 1; ", " linha 2)` em inglês na `Testing1` | Os 3 primeiros caracteres devem ser o CEP em algarismos ou o nome de cidade/condado; endereço do 戶籍; estrangeiro sem endereço em chinês → **endereço do empregador**; não misturar full e half-width | T1 p. 26 item 16 e p. 28 nota 2 |
| X14 | 17 所得人姓名 | `$employee_name` | Chinês com no mínimo 2 caracteres; estrangeiro sem nome chinês → nome em inglês do passaporte; todo full-width ou todo half-width, sem espaços nas pontas | T1 p. 26 item 15; p. 28 nota 2 |
| X15 | 16 所得給付年度 | ano de `$meta.as_of_date` − 1911 | Ano ROC do **pagamento**. Para não residente, usar a data do pagamento | T1 p. 26 item 14 |

Conferido e correto: campo 1 稽徵機關代號 (DD `country_and_city_authorities_code`, 3 caracteres); 4 所得註記 vazio para salário; 5 所得格式 50 / 93 (série 6218x = severance → 93 退職所得); 6 ID (`$hr.id_card_number`); 7 證號別 (`$hr.identity_type`); 11 código do empregado (até 12); 12–13 vazios; 14 "A"; 15 vazio; 21–25 vazios; 27 Y/N só para tipos 5–9; 10 = 8 − 9 (T1 p. 28 nota 1).

## Proposta de preenchimento
> **Proposta**, não aplicada. ⚠️ = depende de variável/PE a confirmar pelo BA.

| Linha | Campo | Antes | Depois (proposto) | Fonte |
|---|---|---|---|---|
| RM | Dataset / Frequency | "Annual/Monthly" | Dois datasets. **Residente** (`residential_status = 0`): Tax Year, YTD, 1 arquivo por ano, até 31/01 do ano seguinte. **Não residente**: um arquivo por data de pagamento, até 10 dias após a retenção | T3 art. 92; T5 |
| RM | File Format / Delimiter / Encoding | XLSX / CSV | U8: UTF-8, separador "\|", 32 campos, vazio sem espaços. Se o produto só gerar CSV, registrar que o envio passa pelo IMX (import CSV Big5 → U8) | T1 p. 11–12; T2 pp. 41–46 |
| RM | File Name | vazio | Residente `{UBN}.{ROC年}.U8`; não residente `{UBN}.{ROC yyymmdd do pagamento}.U8` | T2 p. 5 |
| RM | Rounding | vazio | NT$ inteiro, sem decimais, sem negativos | T1 p. 25 itens 8–10 |
| RM | Registros adicionais | não existem | 申報書資料 e 申報單位基本資料 (gerados no IMX ou no produto) ⚠️ decisão de produto | T1 p. 11 |
| B4 | 2 流水號 | `$row_number` | Residente `LPAD($row_number;8;'0')`; não residente `CONCAT('00';LPAD($row_number;6;'0'))` | T1 p. 21 |
| B10 | 8 給付總額 | K10 `58008 + 58009 + 62200:62209` | Mesma regra, por formato: 50 = renda salarial tributável (YTD residente / do pagamento não residente) **sem** a série 6218x; 93 = 6218x. ⚠️ Confirmar se 6220x já está no 58008 (risco de contar duas vezes; o WTC não tem fórmula para 58008/58009) | T1 p. 25 item 8 |
| B11 | 9 扣繳稅額 | "Tax Exemption Amount", K11 `58100 + 58105` | Renomear "Tax Withheld Amount". Mapear pela coluna P: residente YTD de 2552+2572+2582+2592; formato 93 YTD de 2594; não residente 2593 do pagamento | T1 p. 25 item 9 |
| B12 | 10 給付淨額 | "(10−11)" | `campo 8 − campo 9`, nunca negativo | T1 p. 28 nota 1 |
| B13 | 11 | `$employee.reference_code` | Manter; truncar/validar em 12 caracteres | T1 p. 25 item 11(7) |
| B18 | 16 所得給付年度 | ano de `as_of_date` − 1911 | Residente: ano do período do relatório − 1911; não residente: ano da data de pagamento − 1911 | T1 p. 26 item 14 |
| B19 | 17 Nome | `$employee_name` | Nome em chinês (≥ 2 caracteres) se houver; senão nome do passaporte; sem espaços nas pontas; até 50 ⚠️ campo do nome chinês no DD | T1 p. 26 item 15 |
| B20 | 18 Endereço | cidade + distrito + linha 1 + ", " + linha 2 | Começar pelo CEP (`hr.employee_postcode`, como já sugere a aba `Testing`) ou pelo nome da cidade em chinês; sem vírgula se o arquivo continuar em CSV; estrangeiro sem endereço chinês → endereço do empregador; até 100 | T1 p. 26 item 16 |
| B21 | 19 Período | fixo 01–12 | Residente: `YYY` + (mês de admissão se admitido no ano, senão 01) + `YYY` + (mês de saída se saiu no ano, senão 12). Não residente: `YYYMM` do mês do pagamento repetido (ex.: `1140611406`) | T1 p. 26 item 17; issue 3 do Mohit |
| B22 | 20 Pensão voluntária | `$58105` / `58160` | Residente: YTD de **2517** (LPN EE); não residente: 2517 do pagamento; vazio/0 se não houver; só formato 50 | T1 p. 26 item 18(1); WTC V2.8 |
| B29 | 27 183 dias | `IF(tipo ∈ 5–9; IF(status=0;'Y';'N');'')` | Manter | T1 p. 27 item 21 |
| B30 | 28 País | `…; 'ZZ'` | `IF(tipo ∈ {3,5,6,7,8,9,A}; código do anexo 41 do país de residência, 'ZZ' se desconhecido; '')` ⚠️ conferir se o ISO2 do sistema bate com o anexo 41 | T1 p. 27 item 22 |
| B31 | 29 Tratado | `'XX'` | `''` (vazio) por padrão; código do anexo 42 só se o empregado invocar tratado ⚠️ não há campo no DD | T1 p. 27 item 23 |
| B33 | 31 Data | sempre `generation_time` | Residente: `DATE_FORMAT($report.generation_time;'MMdd')`; não residente: MMdd da data de pagamento | T1 p. 27–28 item 25 |
| B34 | 32 TIN | `IF(status=1;'NORTIN';'')` | `IF(tipo ∈ {3,5,6,7,8,9,A}; IF(vazio($hr.tax_number);'NOTIN';$hr.tax_number); '')` ⚠️ confirmar campo de TIN estrangeiro no DD | T1 p. 28 item 26 |
| Aba | `Testing` | descrições divergentes (X11, X12, "1: ≥183 days") | Apagar ou marcar como superada | — |
| VC | Version Control | só 1.0 | 1.1 (descrições Lisa/Brenet, jul–ago/2025), 1.2 (issues do Mohit, jan/2026), 1.3 (revisão de spec) | padrão |

## Status dos pontos do ticket
| Issue (Mohit, 23/01/2026) | Contra a fonte | Na spec exportada hoje |
|---|---|---|
| 1. Residente (0) em modo YTD, senão mensal | **Correto** (T3 art. 92 §1 e §2). Ajuste: o não residente é por **data de pagamento** (arquivo e campo 31), não por mês calendário | Report Matrix não traz a regra; H22 tem um `IF(residential_status…)` isolado. Não refletido |
| 2. "Tax Exemption Amount is not coming" | O campo oficial é **imposto retido** (扣繳稅額); o mapeamento K11 (`58100 + 58105`) é que está errado. A coluna P da Lisa tem o mapeamento certo | Não refletido (K11 continua 58100 + 58105) |
| 3. Período por admissão/saída | Lógica do residente **confere** com T1 (所得所屬起迄年月). Para o não residente, o campo é `YYYMMYYYMM` (ano/mês), **não** "month start and end date" | Não refletido (H21 continua 01–12 fixo) |
| Manjit, 30/01: "changes has been done" | — | Sem evidência: a spec não mudou e não há teste novo depois de 30/01. Pedir a saída atual ao Manjit/Mohit |

## Veredito
**Não está pronta para devolver ao Mohit.** Os 3 pontos dele estão certos na intenção (com o ajuste do não residente), mas nenhum aparece na spec, e há mais 10 conflitos com o formato do MOF: formato/arquivo (X1–X2), serial do não residente (X4), data do campo 31 (X5), pensão voluntária (X7), país/tratado/TIN (X8–X10), endereço e nome (X13–X14). Depois da proposta aplicada e de uma decisão sobre o caminho de envio (U8 completo × IMX), a spec fica pronta para teste.

## Achados fora do pedido
1. Um empregado que muda de não residente para residente no ano (o IMX trata a importação "所得人身分由非居住者轉變為居住者", T2 p. 51) não está previsto: as retenções de não residente já declaradas por pagamento × o anual de residente. ⚠️ Regra não pesquisada a fundo; vai para o hub.
2. DD V3.3, option mapper "Identity Type", key 4: rótulo em inglês "mainland person living in Taiwan less than 183" × T1 (【4】所得人為總機構在中華民國境外之在臺分公司). As chaves 5 e 7 é que são pessoas com menos de 183 dias. Corrigir o rótulo no DD.
3. O "Tax Exemption Amount" já foi citado como "tax exemption" no SOP 1.1 ("total income, tax exemption and net pay"): a mesma tradução errada está no SOP.
4. O PDF oficial local é o de 112年度 (renda de 2023). O calendário de 115 confirma o prazo da renda de 114; não achei na máquina o 要點 de 113/114 (versão mais nova, regra 8).
5. Taxa do não residente (18% / 6% até 1,5× o salário mínimo, T4) e o salário mínimo de 2026 (NT$29.500, citado pelo NHIA no SR-108, F5 p. 4): conferir o 2593 no WTC é tarefa de outro ticket.

## Rascunho de comentário (EN)
> @mjain Spec review done against the MOF e-filing rules (綜所稅資料電子申報作業要點); changes highlighted in the spec (v1.3).
> 1. Your 3 points are right; none was reflected in the spec yet. Two refinements: non-residents are filed per payment date (file name, serial starting "00", field 31 = payment date); the non-resident period is YYYMMYYYMM of the payment month, not dates.
> 2. Field 9 is the tax withheld, not an exemption: renamed and mapped per column P (2552+2572+2582+2592 YTD; 2594 for format 93; 2593 non-resident). The current mapping 58100+58105 is the reason it was not coming.
> 3. Also corrected: voluntary pension = 2517 (58105 does not exist), residence country blank unless ID type 3/5/6/7/8/9/A, treaty code blank instead of "XX", TIN "NOTIN" (not "NORTIN") by ID type, address starting with the postcode.
> 4. Format: the official file is UTF-8 pipe-delimited with the declaration and payer records; please confirm whether we generate the full .U8 or import a CSV into IMX.
> @manjitbali could you share the latest output after your January changes?

## O que precisa ser feito
1. Usuário revisa e aprova o texto (nada postado).
2. Aplicar a proposta numa cópia da spec (destaque `FFDDEBF7`, v1.3), depois do ok.
3. Decisão de produto com o Mohit: arquivo U8 completo × CSV para o IMX.
4. BA confirma: 6220x dentro ou fora do 58008; campos do DD para nome chinês, TIN estrangeiro e tratado.
5. Pedir a saída atual da configuração ao Manjit e retestar com 1 residente, 1 residente admitido no meio do ano, 1 desligado e 1 não residente.
6. Registrar no hub os achados 1–4.

## Lacunas
- ⚠️ 要點 de 113/114年度: não localizado; conferir se mudou algum campo (o 112 é de 12/2023).
- ⚠️ Fórmulas do 58008/58009 no WTC: vazias; não dá para afirmar se o 6220x já está no 58008.
- ⚠️ Lista do anexo 41 (códigos de país) × ISO2 do sistema: não comparada.
- O texto do 各類所得扣繳率標準 não foi relido (taxas via Q&A oficial do eTax).
- Sem acesso ao ambiente de teste: o status real da configuração é o da aba `Testing1`.
