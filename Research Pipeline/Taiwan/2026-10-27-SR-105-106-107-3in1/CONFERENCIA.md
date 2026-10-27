# CONFERENCIA — Taiwan SR-105 / SR-106 / SR-107 (lote 3-em-1 LI/NHI/LP) — specs v1.1

> **Rodada 2 aplicada (ver seção no fim): números e md5 atuais estão lá; as seções abaixo descrevem a rodada 1.**
> Tudo local. Nada foi gravado no Drive, YouTrack, e-mail ou chat. Specs v1.1 = **Draft** para o usuário revisar antes de qualquer envio.

## Pedido
Mohit (2026-09-15, nos 3 tickets): "Spec Review only and fill the gaps in specs." → revisar contra o formato oficial e preencher lacunas. Mais nada.

## Arquivos desta pasta
| Arquivo | md5 |
|---|---|
| [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/TW - SI electronic filing Salary Adjustment specification v1.1.xlsx\|TW - SI electronic filing Salary Adjustment specification v1.1.xlsx]] (SR-105) | `ba825791c28abc28fd3f1f44a368403f (rodada 2)` |
| [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/TW - SI Termination specification v1.1.xlsx\|TW - SI Termination specification v1.1.xlsx]] (SR-106) | `65d575e5863cd7e3db2afb3962fa56d6 (rodada 2)` |
| [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/TW - SI electronic filing Joiner Specification v1.1.xlsx\|TW - SI electronic filing Joiner Specification v1.1.xlsx]] (SR-107) | `7d02c8bade5d37693242ba814ee87cf5 (rodada 2)` |
| `comparacao_SR-105.md`, `comparacao_SR-106.md`, `comparacao_SR-107.md` | log célula a célula base × v1.1 |
| `validacao.md` | validação XML/pacote + gate do toolkit |
| `comentarios.md` | rascunho de comentário EN por ticket (não postado) |
| `scripts/` | `xlsxpatch.py` (edição por XML + repack), `common.py`, `build_SR-10x.py`, `compare.py`, `validate.py`, `dump.py`, `edits_SR-10x.json` |

Reproduzir: `python -I scripts/build_SR-105.py` (idem 106, 107) → `python -I scripts/compare.py <base> <v1.1> scripts/edits_SR-10x.json comparacao_SR-10x.md` → `python -I scripts/validate.py <base> <v1.1>`.

## Fontes
| # | Fonte | Caminho | md5 |
|---|---|---|---|
| Base 105 | export Drive 2026-10-27 (conteúdo de células idêntico ao export de 23/10, conferido por dump) | [[raw/docs/drive-exports/2026-10-27/TW - SI electronic filing Salary Adjustment specification.xlsx\|TW - SI electronic filing Salary Adjustment specification.xlsx]] | `a8414b1c…cb0` |
| Base 106 | idem | [[raw/docs/drive-exports/2026-10-27/TW - SI Termination specification.xlsx\|TW - SI Termination specification.xlsx]] | `10d1865c…dce` |
| Base 107 | idem | [[raw/docs/drive-exports/2026-10-27/TW - SI electronic filing Joiner Specification.xlsx\|TW - SI electronic filing Joiner Specification.xlsx]] | `575c1a2e…31e` |
| G-ADJ | NHIA/BLI 三合一批次薪資調整格式說明 **(114.12.12修)** | [[raw/docs/oficiais/TW/2026-10-27-NHIA-03_Adj3Of1.docx\|2026-10-27-NHIA-03_Adj3Of1.docx]] (+ `.txt`) | `190f3d00…5da` |
| G-STOP | NHIA/BLI 三合一批次退保格式說明 **(114.12.12修)** | [[raw/docs/oficiais/TW/2026-10-27-NHIA-02_Stop3Of1.docx\|2026-10-27-NHIA-02_Stop3Of1.docx]] | `e73692b1…402c108` |
| G-APPLY | NHIA/BLI 三合一批次加保格式說明 **(115.03.11修)** | [[raw/docs/oficiais/TW/2026-10-27-NHIA-01_Apply3Of1.docx\|2026-10-27-NHIA-01_Apply3Of1.docx]] | `312e60ee…b91` |
| 承表S | BLI form S rev. 115.05 (instr. 6(3), 7, 8; notas 2–5) | [[raw/docs/oficiais/TW/2026-10-23-BLI-form-S-salary-adjustment-3in1-example-115.05.pdf\|2026-10-23-BLI-form-S-salary-adjustment-3in1-example-115.05.pdf]] | — |
| 承表L | BLI form L rev. 113.06 (notas 1, 3; instr. 2, 3, 6) | [[raw/docs/oficiais/TW/2026-10-23-BLI-form-L-termination-3in1-example-113.06.pdf\|2026-10-23-BLI-form-L-termination-3in1-example-113.06.pdf]] | — |
| 承表D | BLI form D rev. 115.01 (nota 2; instr. 8, 9(3), 11, 13) | [[raw/docs/oficiais/TW/2026-10-23-BLI-form-D-joiner-3in1-example-115.01.pdf\|2026-10-23-BLI-form-D-joiner-3in1-example-115.01.pdf]] | — |
| BLI 0022929 | 投保薪資調整申報作業 (item 二(一): média de 3 meses do 月薪資總額, inclui horas extras, 伙食津貼, 全勤/績效/生產獎金) | `raw/docs/oficiais/TW/2026-10-23-BLI-page-0022929-salary-adjustment-procedure.html` | — |
| NHIA insured-amount | 如何正確申報健保投保金額 (tabela O/X: 年終獎金, 考核獎金, 紅利, 節金 = X; 攻略 2: prazos ago/fev) | [[raw/docs/oficiais/TW/2026-10-23-SNHI-nhia-insured-amount-and-supplementary-premium-115v1.pdf\|2026-10-23-SNHI-nhia-insured-amount-and-supplementary-premium-115v1.pdf]] | — |
| NHIA flyer | Divisão Leste — 申報批次勞健合一(EXCEL檔) 加保/退保/薪資調整; 薪資調降 e 外籍人士加保 exigem upload de comprovante | [[raw/docs/oficiais/TW/2026-10-23-NHI-east-division-flyer-batch-excel.pdf\|2026-10-23-NHI-east-division-flyer-batch-excel.pdf]] | — |
| DD | Taiwan Data Dictionary V3.3 | [[raw/docs/drive-exports/2026-10-23/Taiwan Data Dictionary V3.3.xlsx\|Taiwan Data Dictionary V3.3.xlsx]] | — |
| WTC | Taiwan WTC V2.8 (52517, 52537, 58008, 58009, 58212, 6220x, 64550; 58139 não existe) | [[raw/docs/drive-exports/2026-10-23/Taiwan WTC V2.8.xlsx\|Taiwan WTC V2.8.xlsx]] | — |

Tudo acima foi lido por mim nesta sessão (guias novos: texto integral do `.docx`, tabela única, sem notas de rodapé; formulários: texto extraído do PDF).

## Guia antigo × guia atual (o que mudou)
Guias usados nas análises de 23/10: cópias do Drive 104.10.05 (adj., stop) e 113.03.31 (apply). Atuais: 114.12.12 / 114.12.12 / 115.03.11. Nº de colunas **não mudou** (14 / 16 / 27).

### 03_Adj3Of1 — 104.10.05 → 114.12.12 (SR-105)
| Campo | Antes (104.10.05) | Agora (114.12.12) |
|---|---|---|
| Cabeçalho | 勞保、健保、勞退(3合1) | 三合一; **aplica-se a unidades 勞(就)保/災保/勞退/健保 e 就保/災保/勞退/健保** |
| 1 | 「薪資調整」"3" | 「投保薪資調整」"3" |
| 2, 3 | 勞工保險證號 / 檢查碼 | **保險證號** / 保險證號檢查碼 |
| 6 外籍 | Y, 1, 2, branco | **+ L (永居外專)**; "1" inclui 港澳配偶; rótulo <外籍專用> |
| 7 姓名 | máx. **25**; chinês ≥ 2 | máx. **200**; nacional ≥ 2, estrangeiro ≥ 1; inglês em maiúsculas largura total |
| 8, 9 | 居留證號碼 | **居留證統一證號** |
| 11 | 調後月實際工資 (勞保、勞退專用) | **調後月薪資總額 [勞(就)保/災保/勞退]** (agora cobre o 災保) |
| 11 nota | "só NHI → deixar 2, 3 e 11 em branco" | **regra removida**; nova nota: abaixo do salário mínimo → preencher 特殊身分別 |
| 12, 13 | 投保薪資 | **投保金額** |
| 14 特殊身分別 | 1, 8, branco | **1, 2, 6, 7, 8, branco** |

### 02_Stop3Of1 — 104.10.05 → 114.12.12 (SR-106)
| Campo | Antes | Agora |
|---|---|---|
| Cabeçalho | 勞保、健保、勞退(3合1) | aplica-se a unidades 勞(就)保/災保/勞退/健保 e 就保/災保/勞退/健保 |
| 2, 3 | 勞工保險證號 | **保險證號** |
| 6 投保別 | 2 = 勞保健保勞退; 3 = 健保 (pelo sistema NHIA) | **só "2"** = 勞(就)保/災保/勞退/健保 (valor 3 saiu) |
| 8 外籍 | Y, 1, 2 | **+ L**; "1" inclui 港澳配偶 |
| 9 姓名 | máx. 25 | **máx. 200**; estrangeiro ≥ 1 |
| 10, 11 | 居留證號碼 | **居留證統一證號**; "非本國籍人士" |
| 14 U | 喪失全民健康保險投保資格者 | **喪失健保法第8或第9條資格者** (nota: art. 8 perda de nacionalidade/戶籍遷出; art. 9 fim da residência) |
| Lembrete | só NHI → sistema NHIA | dependentes saem junto; só NHI → 健保署 |

### 01_Apply3Of1 — 113.03.31 → 115.03.11 (SR-107)
| Campo | Antes | Agora |
|---|---|---|
| Cabeçalho | 勞保、健保、勞退三合一 | aplica-se a unidades 勞(就)保/災保/勞退/健保 e **就保/災保/勞退/健保** |
| 2, 3 | 勞工保險證號 | **保險證號** |
| 5 投保別 | 2 = 勞保、健保、勞退; 3 = só 健保; 4 = 勞保職災、健保、勞退 | 2 = **勞(就)保/災保/勞退/健保**; 3 = 健保; 4 = **災保/勞退/健保** |
| 6 notas | só NHI → NHIA; só 勞保/勞退 → BLI e-service; 外籍 de unidade não-1ª categoria → online | **se 5 = "4", campo 27 obrigatório**; **só NHI ou加保 de 「外籍」→ LI e NHI separados, com o 健保署**; abaixo do mínimo → 特殊身分別 (a nota "só 勞保/勞退 → e-service" saiu) |
| 7 外籍 | Y, 1, 2 | **+ L (永居外專)**; "1" inclui 港澳配偶 |
| 8 ID | 居留證號碼, sem ARC → passaporte | **居留證統一證號** ou passaporte |
| 9 姓名 | máx. 25 | **máx. 200**; estrangeiro ≥ 1 |
| 11 | 月實際工資 (勞保、勞退專用) | **月薪資總額 [勞(就)保/災保/勞退]** |
| 12 | 健保投保薪資 | **健保投保金額** |
| 18 | 稱謂代碼 1–9 | 稱謂代號 1–9 (sem "P"; o 承表D 115.01 tem 受監護人) |
| 20 | S/P/A/H/G para眷屬 ≥ **20** anos | ≥ **18** anos |
| 23 "3" | 雇主個人自願提繳 | 雇主自願提繳 |
| 24, 25 | 雇主提繳率 / 個人自願提繳率 | com **(%)** no nome |
| 27 | 已領取社會保險給付種類 (勞保職災專用): 1 já recebe 老年給付; 2 **recebe outro benefício** e > 65 | **僅參加「災保」條件 (só 投保別 4)**: 1 já recebe 勞保老年給付; 2 **NÃO recebe** 勞保老年給付 e > 65 |

Consequências para as análises de 23/10: (a) SR-105 — sai a regra "só NHI → 2, 3, 11 em branco"; campo 14 aceita 1, 2, 6, 7, 8; (b) SR-106 — campo 6 é sempre "2"; 4-2/2-2 (sem NHI) continuam fora; (c) SR-107 — o indício de versão nova (análise F1 ⚠️) se confirmou; valor 4 e campo 27 mudaram de sentido; estrangeiros (外籍) saem do lote.

## Decisões
1. **Edição por XML + repack** (skill §4): nenhuma `openpyxl.save()`. Partes não alteradas copiadas com bytes descomprimidos idênticos (20/22/21 partes, conferido). Texto novo como inline string; `sharedStrings.xml` intacto.
2. **Azul-claro `FFDDEBF7`** em toda célula alterada/nova (estilo próprio da célula clonado + fill). O comentário-modelo da aba Version Control (D12) diz "highlight changes in yellow" — mantida a regra do cérebro (azul) por pedido explícito; registrar para o usuário decidir.
3. **Report Matrix**: Filing Method = `Electronic: Upload online ` (texto exato da lista Options!A16, com espaço final, para passar na validação de lista); SR-105 Periodicity = `Period` (da lista; "Quarterly" saiu) e prazos semestrais em Introduction; SR-106/107 prazos "no dia" do desligamento/admissão em Comments (sem "within 3 days").
4. **Colunas novas** C/M/O e Data Type: SR-105 já tinha (D/E vazias → preenchidas); SR-106 em **J/K**, SR-107 em **K/L** (J8 tem a nota do Mohit).
5. **Rótulos locais** (coluna "Local Language") alinhados aos nomes do guia atual onde mudaram (保險證號, 居留證統一證號, 月薪資總額, 投保金額, 稱謂代號, 雇主提繳率(%), campo 27).
6. **Nada inventado**: campo sem DD/WTC → `NEW DD FIELD (proposed): …` ou `TO BE CONFIRMED BY MOHIT/BA: …`. Funções de fórmula só as já usadas nas specs (CONCAT, PREPAD, SUBTRACT, DATE_FORMAT, IF, EQUALS, UPPERCASE); o resto descrito em texto.
7. **SR-107 — aba "New Specification" removida** (é spec de 扣繳憑單/withholding tax: 縣市機關別, 所得格式, 扣繳稅額…). Removidas `sheet4.xml`, `_rels/sheet4.xml.rels`, `drawing4.xml` (logo da aba) e as referências em workbook.xml / rels / Content_Types. **O conteúdo não se perde**: continua no export original [[raw/docs/drive-exports/2026-10-27/TW - SI electronic filing Joiner Specification.xlsx|TW - SI electronic filing Joiner Specification.xlsx]] (e no de 23/10). Destino sugerido: Taiwan Tax Report Spec (SR-110) — não mexido aqui.
8. Version Control: linha 14 = 1.1 | 2026-10-27 | resumo | Draft | Wallisson Gomes; país "<Country name>" → "Taiwan" (SR-106/107). Obs.: a lista de validação de E13:E23 não tem "Draft" (só In Progress/Under Review/Approved) — valor gravado como pedido.
9. SR-106 C14 gravado como texto ISO `2026-10-27` (a célula C13 da base não tem formato de data); SR-105/107 como data (serial 46322, formato da linha 13).

## Antes → depois (resumo; detalhe célula a célula em `comparacao_SR-10x.md`)
| Spec | Células alteradas | Principais mudanças |
|---|---|---|
| SR-105 | **75** | Report Matrix: Quarterly → Period + prazos fev–jul/ago–jan; Manual → Electronic; resposta TXT em Comments. Título A1 (2014 → guia 114.12.12). 14 campos com mapeamento (col. L), C/M/O e Data Type. #6 + L; #7 máx. 200; #11 = 月薪資總額 (média 3 meses, sem bônus anual) → WT interino TO BE CONFIRMED; 58009/6220% fora; #12 nhi_grade anterior TO BE CONFIRMED; #13 nhi_grade atual + validação ≥ LI/LP; #14 só 1, 2, 6, 7, 8. Nota A45 trocada pela do guia atual (regra "só NHI" removida). |
| SR-106 | **76** | Report Matrix: Electronic; população sem NHI-only; Comments "no dia" + efeitos (承表L) + LP + resposta TXT. #6 sempre "2"; #8/#10/#11 sem `residential_status` (nacionalidade/`id_type`); #9 nome nacional/estrangeiro máx. 200; #13/#14 nome correto do DD (`withdraw`) + `::key`; #15 incluído (texto curto do guia); #16 com PREPAD; #14 U nova definição; nota A65 sem marca do Youdao; colunas J/K. |
| SR-107 | **119 + 1 aba removida** | Report Matrix: Electronic; Grouping = linha titular + linha por dependente; população (exclui só-NHI e 外籍); Comments "no dia" (承表D). Coluna F (vazia em todos) preenchida nos 27 campos; #5 si_enrollment_code (2/4) e "4" exige #27; #6 linha 1/2 (58212 fora; number_of_nhi_dependents = nº de linhas); #7 + L, sem residential_status; #11 salário na admissão TO BE CONFIRMED / NEW DD FIELD; #12 nhi_grade (58139 não existe); #20 idade 18; #22 por #7; #24/#25 (%) objeto TO BE CONFIRMED; #26 regra −1 a −6 dias; #27 novo sentido. Aba New Specification removida. |

## Conferência
- **Célula a célula** (`compare.py`, openpyxl sobre base × v1.1, todas as abas): 75 / 76 / 119 diferenças, **todas** na lista declarada (`edits_SR-10x.json`), **todas** com fill `FFDDEBF7`; 0 edições sem efeito; 0 células azuis fora da lista; 0 diferenças fora do escopo.
- **Pacote** (`validate.py`): todas as partes XML/rels bem-formadas; Content_Types e rels sem alvo quebrado; media/drawings/comments/vml/threaded iguais à base (SR-107: drawings 5 → 4 = logo da aba removida); openpyxl abre; logo da Version Control presente; Version Control 14 correta; B6/B7/B11 dentro das listas da aba Options.
- **Gate do toolkit** (`validate_workbook.py`): só achados **C29** = os marcadores `TO BE CONFIRMED` pedidos (6 / 5 / 14). Nenhum outro achado. Esperado enquanto as perguntas ao Mohit estiverem abertas.
- Afirmações das specs relidas por mim na fonte: guias atuais (todos os campos), 承表S instr. 6(3)/7/8, 承表L instr. 6 e nota 3, 承表D nota 2 e instr. 9(3)/13, BLI 0022929 二(一), tabela O/X da NHIA, folheto NHIA, DD V3.3 (campos/mappers citados), WTC V2.8 (códigos citados).

## ⚠️ Lacunas (não provadas)
- **Extensão aceita** no upload (.xls × .xlsx): nenhum guia diz; mantido "XLSX" que já estava.
- **就保/災保/勞退/健保 units**: o guia diz que vale para elas, mas não diz qual 投保別 usar (só há "2" = 勞(就)保/災保/勞退/健保 e, no 加保, "4" = 災保/勞退/健保). Não afirmei nada além do cabeçalho.
- **Estrangeiros no 加保**: a nota do campo 6 manda 「外籍」 para o 健保署 (LI e NHI separados), mas o campo 7 ainda lista Y/1/2/L. Se 1/2/L também saem do lote: não provado.
- **Ajuste só de NHI** (SR-105): a regra de 104.10.05 saiu; o guia atual não diz como fazer. Não provado.
- **Retirada de segurado com 投保別 4** (só 災保): o guia de退保 só aceita "2". Não provado como fica.
- Labor Insurance Act art. 14 não lido direto (law.moj.gov.tw inacessível); o conceito de 月薪資總額 está provado pelo BLI 0022929 e pelos formulários.
- Afirmação do Manjit de que "já existe em TXT": sem como verificar o que o produto gera.

## Perguntas ao Mohit (TO BE CONFIRMED / NEW DD FIELD)
1. **Nacionalidade do empregado** (campos 外籍 nas 3 specs; sexo no SR-107): não há campo no DD V3.3 → NEW DD FIELD (proposed) Employee Nationality + indicador de 永居外專 para "L".
2. **Conversão para largura total** (nomes em inglês): o motor tem função?
3. **SR-105 #11**: novo WT interino = média dos 3 meses anteriores do 月薪資總額 — lista de WTs que entram (critério: tabela O/X da NHIA e LSA ER art. 10).
4. **SR-105 #12**: o HR guarda o valor anterior de `$hr.nhi_grade`?
5. **SR-105**: ajuste só de NHI — ainda cabe no lote?
6. **SR-106 #13/#14**: padrão quando o HR estiver vazio (proposta 2 / 1).
7. **SR-107 #11**: campo HR do salário acordado na admissão (ou NEW DD FIELD).
8. **SR-107 #5 linha de dependente** "3"; **#20** motivo por dependente (NEW DD FIELD; proposta "4"); **#21** data do evento do dependente (NEW DD FIELD); `health_insurance_enrollment_start_date` e `labor_pension_contribution_date` tipados como Text no DD.
9. **SR-107 #15–17**: DD só tem ID/nome/nascimento para dependentes 1–3, mas relação para 1–6 → NEW DD FIELD 4–6; dependentes estrangeiros e稱謂 "P" (fora do lote?).
10. **SR-107 #24/#25**: objeto com a taxa inteira (52537/52517 dividem por 100).
11. **SR-107 #27**: rótulo do mapper key 2 (DD diz "received other social insurance benefits"; guia 115.03.11 diz "not received LI old-age benefit and > 65").
12. **SR-107 população**: 1/2/L do campo 7 também ficam fora do lote?
13. `labor_insure_id` tipado como Number no DD (tem letra e zero à esquerda).

## Pergunta do Manjit (TXT) — respondida na Report Matrix (Comments) das 3 specs
O lote oficial é **Excel** enviado no sistema 多憑證網路承保 da NHIA (folheto: 申報批次勞健合一(EXCEL檔)); os 3 guias só definem ordem das colunas, valores e observações — **sem posições e sem layout TXT oficial**.

## Achados fora do pedido (não alterados; ir para o hub Taiwan)
- DD V3.3: `labor_insure_id`/`health_insure_id` como Number; `insurance_certification_number` duplica o dado; `contribution_identity` × `pension_contribution_identity`; mapper Special Identity Code com T = "Vocational student & part-time"; Country Fields ord. 46 aponta mapper errado; ord. 43 (`health_insurance_enrollment_code`) aponta o mapper "SI Insured Person"; mapper Pension Contribution identity "3" com rótulo antigo (雇主個人自願提繳).
- `$hr.id_type` 4/5 (deficiência, carteira de motorista) cairiam no `id_card_number` pelas fórmulas de ID — não há valor oficial para eles no lote.
- Aba "New Specification" (IR) deve ir para a Taiwan Tax Report Spec.

## Registro por frente
| Data | Frente | O quê |
|---|---|---|
| 2026-10-27 | Suporte (construtor A) | v1.1 das 3 specs a partir dos exports de 27/10, ajustadas aos guias NHIA atuais (114.12.12 / 114.12.12 / 115.03.11); 75 / 76 / 119 células + aba removida no SR-107; comparação célula a célula sem diferença fora do escopo; validação XML OK; rascunhos de comentário em `comentarios.md`. Nada enviado. |

## Rodada 2 (2026-10-27) — correção dos achados 1–11 de `REVISAO-independente.md`
Mesmo método (XML + repack, `FFDDEBF7`, builds refeitos a partir dos exports-base; blocos "ROUND 2" no fim de cada `build_SR-10x.py`; `xlsxpatch.py` ganhou suporte a formato numérico para a data).

| # | Achado | Correção | Fonte conferida |
|---|---|---|---|
| 1 | SR-105 E36/E38/E40 numéricos | "Text (official sample: 6 digits with leading zero, e.g. 040000; padding/width TO BE CONFIRMED)". Por coerência, o mesmo no SR-107 L14/L16 (amostra oficial "36000"/"36300", texto) | amostras [[raw/docs/drive-exports/2026-10-23/SR-105-1-5 Sample 03_Adj3Of1.xlsx\|SR-105-1-5 Sample 03_Adj3Of1.xlsx]] e [[raw/docs/drive-exports/2026-10-23/SR-107-1-3 Sample 01_Apply3Of1.xlsx\|SR-107-1-3 Sample 01_Apply3Of1.xlsx]] (formato `@`) |
| 2 | `special_identity_code` aponta mapper errado | SR-105 L42 e SR-107 F17: `$hr.special_identity_code::key` = **ID Information ord. 36** (mapper "Special Identity Code") + TO BE CONFIRMED, porque o mesmo código existe em Country Fields ord. 46 com o mapper "Received Social Insurance Benefits Type" (só 1, 2) | DD V3.3 (dump próprio): ID Information ord. 36; Country Fields ord. 46 |
| 3 | perguntas faltando | `comentarios.md` reescrito: uma pergunta por marcador TBC, agrupadas | — |
| 4 | Sample vazia | SR-105 col. J (oculta na base), SR-106 e SR-107 col. E com valores da **amostra oficial fictícia**. Campos que a amostra deixa em branco ficaram em branco (SR-105 #14; SR-106 nenhum; SR-107 #7, #13, #14, #22, #25, #26). "離職" sem os espaços finais da amostra | amostras oficiais do Drive (2026-10-23) |
| 5 | "Draft" fora da lista | E14 = "Under Review" nas 3 | validação E13:E23 |
| 6 | B9 com nome inventado | SR-106/107: "Not prescribed by the official format guide (…)" | guias 02/01: sem regra de nome |
| 7 | B20 só "BLI" | SR-106/107: BLI e NHIA juntos num lote 3-em-1, que pode ir no sistema 多憑證 da NHIA (申報批次勞健合一 EXCEL) **ou** no e-service do BLI (合一申報, 單筆及批次) | folheto NHIA Leste; manual BLI cap. 9 FAQ 2, 6, 8 — **novo**: o manual mostra que o BLI também recebe o lote; B22 das 3 specs fala só do sistema NHIA (não está errado, só incompleto; não mexido) |
| 8 | SR-106 F60 | data do fato por motivo: 1–4 → `last_working_date`; M/E/U → data do evento → NEW DD FIELD (proposed) + TO BE CONFIRMED | guia 02 #16; 承表L instr. 6(二) |
| 9 | SR-107 B14 × F10/F26 | F10: linhas "Y" não entram no lote (B14); 1/2/L mantidos até confirmação. F26: só para linhas que ficam no lote | guia 01 nota do #6 |
| 10 | nome em prosa | `IF(EQUALS(<campo 外籍>; ''); $hr.name; FULLWIDTH(UPPERCASE($hr.name)))` + TBC da função FULLWIDTH e de o `$hr.name` trazer o nome em inglês (SR-105 L23, SR-106 F29, SR-107 F12) | DD ID Information `name` |
| 11 | SR-106 C14 texto | data serial 46322 com formato `mm/dd/yyyy` (o mesmo de SR-105/107; numFmt novo no styles do SR-106) | — |

**Números finais (base × v1.1):**
| Spec | md5 | Células alteradas vs base | Células da rodada 2 (v1.1 r1 × r2) | Marcadores TBC (C29) |
|---|---|---|---|---|
| SR-105 | `ba825791c28abc28fd3f1f44a368403f` | 88 | 19 | 10 |
| SR-106 | `65d575e5863cd7e3db2afb3962fa56d6` | 94 | 22 | 6 |
| SR-107 | `7d02c8bade5d37693242ba814ee87cf5` | 143 + aba removida | 30 | 17 |

**Conferência da rodada 2:** `compare.py` refeito nas 3 (`comparacao_SR-10x.md`): todas as diferenças na lista declarada, todas em `FFDDEBF7`, 0 fora do escopo, 0 sem efeito; partes não tocadas idênticas (20/22/21). `validate.py`: OK nas 3 (XML bem-formado, rels/Content_Types íntegros, media/comments iguais, E14 dentro da lista, C14 como data nas 3). Toolkit: só C29 (os marcadores TBC). Delta rodada 1 → 2 medido célula a célula contra cópias da rodada 1 (valor e formato numérico).

| Data | Frente | O quê |
|---|---|---|
| 2026-10-27 | Suporte (construtor A, rodada 2) | Achados 1–11 da revisão independente corrigidos: 19 / 22 / 30 células; comparação e validação refeitas; `comentarios.md` com uma pergunta por TBC. Nada enviado. |

## Arquivos da entrega
- [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/REVISAO-independente|REVISAO-independente]]: Revisão independente das specs v1.1 SR-105/106/107: 105 e 107 FAIL, 106 PASS com MINOR (rodada 1).
- [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/comentarios|comentarios]]: Rascunhos de comentário (EN, não postados) com uma pergunta por TO BE CONFIRMED das 3 specs 3-em-1 NHIA/BLI.
- [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/comparacao_SR-105|comparacao_SR-105]]: Diff célula a célula da spec Salary Adjustment base x v1.1 (88 células).
- [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/comparacao_SR-106|comparacao_SR-106]]: Diff célula a célula da spec Termination base x v1.1 (94 células).
- [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/comparacao_SR-107|comparacao_SR-107]]: Diff célula a célula da spec Joiner base x v1.1 (142 células, aba removida).
- [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/validacao|validacao]]: Validação XML/pacote das 3 specs v1.1 (md5, validate.py, validate_workbook).
