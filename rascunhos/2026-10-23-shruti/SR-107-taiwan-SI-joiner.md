# SR-107 — TW - SI electronic filing Joiner (加保三合一) — análise da spec

> Rascunho de análise (só leitura). Nada foi postado no YouTrack, enviado por e-mail ou alterado no Drive.
> Data: 2026-10-23. Analista: janela Suporte (repasse Manju → Shruti → nós).

## Metadados
| Item | Valor |
|---|---|
| Ticket | SR-107 — https://youtrack.hrblizz.dev/issue/SR-107 |
| Estado / fase | Open / Specification Phase - Research Analyst |
| BA / RA / Dev | Mohit Jain / Manju Shetija (→ Shruti → nós) / Katrin Rudi |
| Reporter | Lisa Quan (jquan), criado 2025-06-26 |
| Escopo descrito | "Combination of 1-3, 4-1 and 2-1 report" (numeração interna Mercans dos formulários BLI, ver pasta `01 - SOP/Report/Social Security/1. Join` no Drive) |
| Spec analisada | `raw/docs/drive-exports/2026-10-23/TW - SI electronic filing Joiner Specification.xlsx` (abas Version Control, Report Matrix, Spec, New Specification, Options) — v1.0 "In Progress", 2025-10-07 |
| Guia / sample do ticket | `SR-107-1-3 guide 01_Apply3Of1.txt` (cabeçalho "勞保、健保、勞退三合一批次加保格式說明(113.03.31)"); `SR-107-1-3 Sample 01_Apply3Of1.xlsx` |
| DD / WTC | Taiwan Data Dictionary V3.3 (2025-09-08); Taiwan WTC V2.8 (2026-10-13) |
| Pedido especial | Mohit 2025-09-08: "We need to replace 58212 by $hr.number_of_nhi_dependents" |

## O que foi pedido a nós
Último comentário (Mohit, 2026-09-15): "Assigned to Manju for Spec Review only and fill the gaps in specs. Assign back to me once done for Testing and Development."
→ **Revisar a spec contra o formato oficial e preencher as lacunas**; devolver ao Mohit. Pendente também: a pergunta do Manjit Bali (2026-02-02) sobre o tipo de relatório ("these reports are available in TXT format already") e a troca 58212 → `$hr.number_of_nhi_dependents`.

## Histórico do ticket
- 2025-07-02 Jarwin: link do template da spec.
- 2025-07-07/15 Brenet pede ao Mohit o "Report Field Mapping"; 2025-07-09 Mohit: sem spec anexada → "Clarified".
- 2025-07-09 → 08-12 Lisa (RA) comenta a spec (coluna I "RA (LISA) Reply to BA Queries").
- 2025-08-14 Mohit: "Lisa has confirmed all the points. Please proceed."
- 2025-09-08 Mohit (2x): trocar 58212 por `$hr.number_of_nhi_dependents` (DD V3.3 de 2025-09-08 criou o campo, ord. 48).
- 2026-02-02 Manjit pergunta o tipo de relatório (TXT).
- 2026-09-15 Mohit: atribui para "Spec Review only and fill the gaps". Nada feito desde então.

## Layout oficial (fonte primária)

### Fontes
| # | Fonte | Caminho local | Observação |
|---|---|---|---|
| F1 | NHIA/BLI — "勞保、健保、勞退三合一批次加保格式說明(113.03.31)" (documento oficial `01_Apply3Of1.docx`, publicado em eservice.nhi.gov.tw/nhiweb1/INS/documents/) | cópia do Drive: `raw/docs/drive-exports/2026-10-23/SR-107-1-3 guide 01_Apply3Of1.txt` | ⚠️ O original **não pôde ser baixado** (eservice.nhi.gov.tw corta a conexão a partir daqui — curl, Python, WebFetch e Chrome; sem cópia no Wayback). Usada a cópia do ticket. |
| F2 | Sample do formato (01_Apply3Of1) | `raw/docs/drive-exports/2026-10-23/SR-107-1-3 Sample 01_Apply3Of1.xlsx` | Dados fictícios; cabeçalhos e comentários em chinês iguais ao F1. |
| F3 | BLI — Formulário 承表D "勞、就、災、健保暨勞退合一加保申報表" **rev. 115.01** (exemplo) | `raw/docs/oficiais/TW/2026-10-23-BLI-form-D-joiner-3in1-example-115.01.pdf` (bli.gov.tw/Files/10147, página 0103170 atualizada 2026-10-15) | Versão em papel vigente. |
| F4 | BLI — página 0103170 (加保申報表 合一) | `raw/docs/oficiais/TW/2026-10-23-BLI-page-0103170-joiner-form.html` | "投保薪資係依勞工之月薪資總額…" |
| F5 | BLI — Manual "玖、網路申辦" (FAQ 2, 3, 5, 6) | `raw/docs/oficiais/TW/2026-10-23-BLI-manual-cap9-online-filing-FAQ-batch.pdf` (bli.gov.tw/Files/18080) | Confirma o "合一加保作業(單筆、批次申報)". |
| F6 | NHIA Divisão Leste — folheto do 多憑證網路承保系統 | `raw/docs/oficiais/TW/2026-10-23-NHI-east-division-flyer-batch-excel.pdf` (nhi.gov.tw dl-74368) | "提供「申報批次勞健合一(EXCEL檔)」加保、退保、薪資調整等異動作業，一次上傳" |
| F7 | NHIA — "如何正確申報健保投保金額" (tabela de itens de salário que entram no 投保金額) | `raw/docs/oficiais/TW/2026-10-23-SNHI-nhia-insured-amount-and-supplementary-premium-115v1.pdf` (gravado por outra janela hoje) | Base legal citada no próprio doc: NHI Act §20, Enforcement Rules §46, LSA §2. |
| F8 | LSA Enforcement Rules art. 10 (exclusões do 經常性給與) | `raw/docs/oficiais/TW/2026-10-23-payslip-LSA-enforcement-rules-mol.html` (gravado por outra janela hoje) | Apoio para o conceito de 月薪資總額. |

### Formato (o que dá para afirmar)
- **Tipo de arquivo:** planilha Excel, upload em lote no 多憑證網路承保系統 da NHIA (F6: "申報批次勞健合一(EXCEL檔)"). O F1 traz apenas **ordem das colunas, valores válidos e observações**: não há posição inicial/final nem comprimento fixo → **não é layout TXT de largura fixa**. Não encontrei layout TXT oficial para o 三合一.
- **Cobertura:** um arquivo cobre 勞保(+就保)/災保 + 健保 + 勞退 numa linha. F1 campo 6: "僅申報「勞保」、「勞退」加保作業，請改用勞保局 e 化服務系統" → **sem 健保 o lote 三合一 não serve** (formulário 2-1 — 勞、就、職保及勞退, sem NHI — fica fora deste arquivo).
- **Prazo/efeito:** F3 nota 二: o pedido é feito **no dia** da admissão (到職當日); LI/EI valem a partir das 0h do dia do envio; se não for no dia, a partir do dia seguinte. NHI vale desde o dia em que se cumpre a condição (F3 填表說明 六(二)).
- **Ocupational Accident (災保, 2022):** já incluído — F1 campo 5 valor "4" ("勞保職災、健保、勞退") e campo 27 "(勞保職災專用)". F3 (115.01) é o formulário 勞、就、**災**、健保暨勞退.
- ⚠️ **Possível versão mais nova do F1:** o índice de busca do 01_Apply3Of1.docx atual mostra textos que **não estão** na cópia 113.03.31 (campo 5: "申報「勞(就)保/災保/勞退/健保」請輸入"2" … 申報「災保/勞退/健保」請輸入"4""; campo 27 ligado a "【僅參加「災保」條件】"). Não li o documento → **sem fonte primária lida**; precisa ser baixado de um IP de Taiwan antes de fechar a spec.

### Campos oficiais (F1 113.03.31) — 27 colunas
| # | Campo (oficial) | Valores / formato (F1) |
|---|---|---|
| 1 | 異動別 | "4" (加保) |
| 2 | 勞工保險證號 | 8 dígitos |
| 3 | 勞工保險證號檢查碼 | 9º caractere, 1 letra maiúscula |
| 4 | 健保投保單位代號 | 9 dígitos |
| 5 | 投保別 | 2 = 勞保、健保、勞退; 3 = só 健保; 4 = 勞保職災、健保、勞退 |
| 6 | 投保者 | 1 = 本人; 2 = 眷屬 |
| 7 | 被保險人外籍 | Y = 外籍; 1 = 外籍配偶; 2 = 大陸配偶; branco = 本國籍 |
| 8 | 被保險人身份證號(居留證或護照號碼) | nacional: 身分證號; estrangeiro: 居留證號碼, sem ARC → 護照號碼 |
| 9 | 被保險人姓名(外籍含全名) | até 25 caracteres; chinês ≥ 2; estrangeiro com nome inglês: **maiúsculas de largura total** (sample: "ＤＡＶＩＤ" no SR-105) |
| 10 | 被保險人出生日期 | AAAMMDD em ano ROC (ex. 0701203) |
| 11 | 月實際工資(勞保、勞退專用) | valor do salário mensal real; BLI faz a classificação na tabela de faixas |
| 12 | 健保投保薪資 | conforme "全民健康保險投保金額分級表" |
| 13 | 特殊身分別 | 1–8, A, B, S, T, branco |
| 14 | 勞基法特殊身分別 | conforme "勞基法特殊身分別說明" |
| 15 | 眷屬身份證號 | só dependente nacional |
| 16 | 眷屬姓名 | chinês ≥ 2 caracteres (sample: "最多6個字") |
| 17 | 眷屬出生日期 | ROC AAAMMDD |
| 18 | 稱謂代碼 | 1–9, branco |
| 19 | 健保業務組別 | 1–6 |
| 20 | 健保加保原因別 | 本人: 1 到職起薪, 2 入會; 眷屬: 4,5,6,7,8; 眷屬 ≥20 anos e 稱謂 3/5/7: S, P, A, H, G |
| 21 | 健保加保原因發生日期 | ROC AAAMMDD |
| 22 | 被保險人性別 | só estrangeiro: M/F; nacional em branco |
| 23 | 提繳身分別 | 1 強制, 2 自願, 3 雇主個人自願, branco |
| 24 | 雇主提繳率 | (勞退) — sample: "6" |
| 25 | 個人自願提繳率 | (勞退) |
| 26 | 勞退提繳日期 | só se diferente da data do LI; intervalo "申報當日之前1日至前6日"; senão em branco |
| 27 | 已領取社會保險給付種類(勞保職災專用) | 1 = já recebe 勞保老年給付; 2 = outro benefício e > 65 anos; branco |

Regra de linhas (F2 + F3 填表說明 三): o titular e cada dependente vão **em linhas separadas**; a linha do dependente repete os dados do titular (campos 2–12, 19) e preenche 15–18, 20–21 (no sample, linhas de dependente usam 投保別 "3" e 投保者 "2").

## Estado da spec
**Report Matrix**
| Item | Na spec | Conflito |
|---|---|---|
| Report Name / Code | TW - SI electronic filing Joiner / tw-si-joiner | ok |
| File Format | XLSX | ok (F6: Excel) — ⚠️ extensão exata aceita (.xls/.xlsx) não confirmada (F1 original inacessível) |
| Filing Method | **Manual: Submit hardcopies offline** | Conflito: o relatório é o lote eletrônico (F5, F6) → "Electronic: Upload online" |
| Delimiter / Start-End Pos | Not applicable | ok (sem posições no F1) |
| Comments | "Must be submitted within **3 days** of employment" | Conflito: F3 nota 二 — no **dia** da admissão |
| Inclusion Filter | Hire event or internal transfer | ok (transferência entre entidades = novo 加保) |
| Version Control | país "<Country name>" | lacuna de preenchimento |

**Aba Spec (27 campos)** — colunas: Section, Field Name, Local Language, Data Format, Sample, **Report Field Mapping (TA&BA) — vazia em todas as linhas**, Field description TA/BA, Reply RA. Não há colunas M/C/O, tipo, comprimento, regra de validação.

| # | Situação | Conflito/observação (com fonte) |
|---|---|---|
| 1 | Data Format "4.0" (numérico) | Deve ser texto "4" (F1 #1) |
| 2–3 | BA: `$legal_entity_hr.labor_insure_id` (8 primeiros / último caractere) | DD V3.3 define `labor_insure_id` como **Number**, mas o 9º caractere é letra (F1 #3; F3 "8 位數字+1 位英文檢查碼"); DD também tem `insurance_certification_number` ("8 digits + 1 text", marcado "Tax Report") → dois campos para o mesmo dado; zero à esquerda (sample "01999999") se perde em Number |
| 4 | BA: `health_insure_id` — "check with RA" | DD Number "9 digits": mesmo risco de zero à esquerda (sample "000000000") |
| 5 | BA lista pay elements 58140/58120/2517/2560 | Conceito errado: 投保別 é categoria do registro (F1 #5), não contribuição. DD já tem `$hr.si_enrollment_code` (mapper "SI Enrollment code": 2/3/4). RA: "no comment needed" → lacuna |
| 6 | BA: 58212; pedido de troca por `$hr.number_of_nhi_dependents` | 58212 no WTC é "Total Number of **Tax** Dependents" (fórmula com dependentes de IR) → errado para NHI. Porém `number_of_nhi_dependents` também **não é** o valor do campo: o campo é 1/2 **por linha** (F1 #6; F2). O número de dependentes NHI define **quantas linhas "2"** gerar |
| 7 | "No field in DD" / "Spouse nationality not available" | DD V3.3 já tem `$hr.spouse_nationality` (ord. 39). Falta a nacionalidade do empregado (campo universal) ⚠️ |
| 8 | "Refer $hr.id_type and $hr.id_card_number" | Sem fórmula. DD: `id_type` (1 身份證, 2 居留證, 3 護照), `id_card_number`, `passport_number` |
| 9 | "Universal Field" | Falta regra de largura total para nomes em inglês (F1 #9) e limite 25 |
| 10 | "Universal Field" | Sem fórmula ROC (as outras specs já usam a fórmula correta) |
| 11 | BA: 58008 + 58009 + 6220%; RA "Yes" | Conflito: (a) no evento de admissão ainda não há folha; (b) 58009/6220x são adicionais/bônus anuais — F7 marca 年終獎金/考核獎金/節金/紅利 como **X** no 投保金額; F8 art. 10 exclui esses itens do 經常性給與; (c) 58008 é **tributável**, e F7 inclui 伙食津貼 isento (≤3.000) e horas extras no LI/LP |
| 12 | BA: "Pay Element **58139**" | 58139 **não existe** no WTC V2.8. O WTC usa `$hr.nhi_grade::orLabel` (64550) como base NHI |
| 13 | `$hr.special_identity_code::key` | ok; DD mapper "Special Identity Code" rotula **T** como "Vocational student & part-time" (deveria ser 建教生 só) e o campo duplicado na aba Country Fields aponta o mapper errado ("Received Social Insurance Benefits…") |
| 14 | BA "check with RA"; RA "Added on DD" | Mapeamento não escrito: DD tem `labor_standards_act_special_identity` (mapper 0/3/8/9/A/B) |
| 15–17 | "Universal Field" | DD tem `id_card_number_dependent_1..3`, `name_dependent_1..3`, `birthday_dependent_1..3` (só **3**), mas `dependent_1..6_relationship` (**6**) → descompasso |
| 18 | `$hr.dependent_1..6_relationship` | Mapper "Social Security Dependent Code" 1–9 + **P 受監護人**; F3 (115.01) lista "p 受監護人" mas F1 113.03.31 não → ⚠️ confirmar no F1 atual |
| 19 | `$legal_entity_hr.nhi_authority::key` | ok |
| 20 | `$hr.health_insurance_enrollment_code::key` | Um campo único não serve para linhas diferentes (titular = 1; cada dependente tem seu motivo) |
| 21 | fórmula ROC sobre `$hr.health_insurance_enrollment_start_date` | DD define o campo como **Text**, mas a fórmula usa DATE_FORMAT |
| 22 | IF(residential_status = '1') → M/F | Conflito: `residential_status` é **residência fiscal** (mapper: 0 Resident, 1 Non-Resident; WT 58218 "Tax Residency"), não nacionalidade. Estrangeiro residente fiscal ficaria sem sexo (F1 #22 exige para todo estrangeiro) |
| 23 | `$hr.pension_contribution_identity::key` | ok; DD tem também `$hr.contribution_identity` (ord. 33) duplicado |
| 24 | "52537" | WTC 52537 "LPN ER %" tem fórmula `DIVIDE($52537.amount;100)` → resultado fracionário; o campo espera a taxa em % (sample "6") |
| 25 | "52517" | idem (LPN EE %) |
| 26 | fórmula ROC sobre `$hr.labor_pension_contribution_date` | Falta a regra "só se diferente da data do LI; janela −1 a −6 dias" (F1 #26; F5 FAQ 5); DD tipo Text |
| 27 | `$hr.received_social_insurance_benefits_type_occupational_accident::key` | ok; condicional a 投保別 = 4 não escrita; ⚠️ rótulo pode ter mudado no F1 atual |

**Aba "New Specification"**: é uma spec de **扣繳憑單 (withholding tax)** — 縣市機關別, 所得格式, 扣繳稅額, 租稅協定代碼… Não tem relação com o 加保. Ver Achados.

## Proposta de preenchimento
Legenda: ✅ = sustentado por F1/F3/DD; 🟡 = proposta (precisa de decisão RA/BA); "Linha T" = registro do titular; "Linha D" = registro de dependente.

| # | Campo | Antes | Depois (proposto) |
|---|---|---|---|
| — | Report Matrix → Filing Method | Manual: hardcopies | ✅ Electronic: Upload online (NHIA 多憑證網路承保系統, lote "勞健合一 EXCEL") |
| — | Report Matrix → Comments | "within 3 days" | ✅ "File on the hire date (到職當日); LI/EI effective 00:00 on the filing date, next day if filed late (BLI form 承表D 115.01, note 2). Batch covers LI(+EI)/OAI + NHI + LP; LI/LP-only enrolments (form 2-1) are filed in the BLI e-service, not in this file." |
| — | Regra de geração de linhas | (ausente) | ✅ 1 Linha T por admitido + 1 Linha D por dependente NHI (quantidade = `$hr.number_of_nhi_dependents`; dados de cada dependente nos campos dependent_N) |
| 1 | 異動別 | 4.0 | ✅ texto fixo "4" |
| 2 | 勞工保險證號 | só descrição | ✅ `SUBSTRING($legal_entity_hr.labor_insure_id;0;8)` (texto, manter zero à esquerda) 🟡 confirmar qual campo DD é o oficial (`labor_insure_id` × `insurance_certification_number`) |
| 3 | 檢查碼 | só descrição | ✅ 9º caractere, `UPPERCASE` |
| 4 | 健保投保單位代號 | "check with RA" | ✅ `$legal_entity_hr.health_insure_id` como texto de 9 dígitos (PREPAD 9 '0') |
| 5 | 投保別 | pay elements | ✅ Linha T: `$hr.si_enrollment_code::key` (2 ou 4). 🟡 Linha D: "3" (como no sample F2) — confirmar no F1 atual |
| 6 | 投保者 | 58212 | ✅ Linha T: "1"; Linha D: "2" (substitui 58212; `$hr.number_of_nhi_dependents` = número de Linhas D) |
| 7 | 外籍 | sem campo | 🟡 IF nacionalidade = TW → ''; ELSE IF `$hr.spouse_nationality` = TW: (nacionalidade = CN → "2"; senão → "1"); ELSE "Y". F5 FAQ 4/16: 外籍配偶 inclui 港澳配偶. ⚠️ nome do campo universal de nacionalidade |
| 8 | ID | só referência | ✅ IF `id_type::key` IN (1,2) → `$hr.id_card_number`; IF 3 → `$hr.passport_number` |
| 9 | 姓名 | Universal | 🟡 Nacional: nome em chinês (campo `name` 名字 da aba ID Information); estrangeiro: nome completo em maiúsculas **largura total**, máx. 25 — exige função de conversão (⚠️ confirmar se o motor tem) |
| 10 | 出生日期 | Universal | ✅ `CONCAT(PREPAD(SUBTRACT(DATE_FORMAT($person.birth_date;'yyyy');1911);3;'0');DATE_FORMAT($person.birth_date;'MMdd'))` |
| 11 | 月實際工資 | 58008+58009+6220% | 🟡 Salário mensal total acordado na admissão (base + adicionais fixos mensais, incl. 伙食津貼; sem bônus anual/節金/紅利 — F7, F8 art. 10). Como não há folha no evento, usar campo HR do salário contratado (⚠️ nome) — não 58008/58009 |
| 12 | 健保投保薪資 | 58139 | ✅ `$hr.nhi_grade::orLabel` (mesma base do WTC 64550). Regra: ≥ salário segurado LI/OAI e ≥ salário do LP (F3 說明 九(三)) |
| 13 | 特殊身分別 | ok | ✅ `$hr.special_identity_code::key`; branco se vazio |
| 14 | 勞基法特殊身分別 | vazio | ✅ `$hr.labor_standards_act_special_identity::key`; branco se vazio |
| 15 | 眷屬身份證號 | Universal | ✅ Linha D: `id_card_number_dependent_N`; só dependente nacional (F1 #15); Linha T: branco |
| 16 | 眷屬姓名 | Universal | ✅ Linha D: `name_dependent_N` (chinês ≥ 2); Linha T: branco |
| 17 | 眷屬出生日期 | Universal | ✅ Linha D: fórmula ROC sobre `birthday_dependent_N`; Linha T: branco |
| 18 | 稱謂代碼 | dependent_1..6_relationship | ✅ Linha D: `$hr.dependent_N_relationship::key` (1–9); Linha T: branco. 🟡 "P" só se o F1 atual aceitar |
| 19 | 健保業務組別 | ok | ✅ `$legal_entity_hr.nhi_authority::key` |
| 20 | 健保加保原因別 | campo único | ✅ Linha T: "1" (到職起薪). 🟡 Linha D: motivo por dependente (novo campo dependent_N; padrão "4" 依附投保) |
| 21 | 加保原因發生日期 | enrollment_start_date | ✅ Linha T: fórmula ROC sobre `$employee.hire_date` (ou `health_insurance_enrollment_start_date` se preenchido); 🟡 Linha D: data do evento do dependente |
| 22 | 性別 | residential_status | ✅ IF campo 7 ≠ '' → M/F de `$person.gender`; senão branco (⚠️ valores reais do gender) |
| 23 | 提繳身分別 | ok | ✅ `$hr.pension_contribution_identity::key` (só Linha T) |
| 24 | 雇主提繳率 | 52537 | 🟡 taxa em % inteira (ex. 6) = valor de entrada de 52537 (antes do DIVIDE) — confirmar com Mohit qual objeto contém o "6" |
| 25 | 個人自願提繳率 | 52517 | 🟡 idem; branco se 0 |
| 26 | 勞退提繳日期 | fórmula | ✅ preencher só se ≠ data do LI e dentro de −1 a −6 dias da data do arquivo; senão branco |
| 27 | 已領取社會保險給付種類 | ok | ✅ `…occupational_accident::key`, só quando campo 5 = "4"; ⚠️ confirmar rótulo no F1 atual |
| — | Colunas da spec | ausentes | ✅ acrescentar M/C/O e Data Type (Text/Numeric/Date ROC) por campo; Start/End Pos = N/A |

## Veredito
**Não está pronta para devolver ao Mohit.** Falta: (1) o guia oficial **atual** (o da spec é 113.03.31; há indício de versão mais nova); (2) decisões RA nos campos 5–7, 9, 11, 20, 24–25; (3) correção de DD (tipo de `labor_insure_id`/`health_insure_id`, dependentes só até 3, campo de nacionalidade, mapper T); (4) remover a aba "New Specification" (é de IR). Com o F1 atual em mãos e as decisões acima, a spec fica completa — os demais campos já têm proposta sustentada.

**Pergunta do Manjit (TXT):** pelo que as fontes oficiais mostram, o lote 三合一 é **Excel** (F6) e o guia não define posições/comprimentos (F1) — não há layout TXT oficial para este relatório. Se o produto já gera "TXT" para Taiwan, isso não está nos materiais que temos (⚠️ não verificável daqui) — pode ser outro relatório (ex.: 扣繳 de IR, que é TXT).

## Achados fora do pedido
- Aba "New Specification" da spec do Joiner contém a spec de **扣繳憑單 (withholding tax)** — deve ir para a "Taiwan Tax Report Spec", não aqui.
- DD V3.3: `labor_insure_id` e `health_insure_id` tipados como Number (perdem zero à esquerda; o ID do LI tem letra); `insurance_certification_number` duplica o dado; `contribution_identity` × `pension_contribution_identity` duplicados; mapper "Special Identity Code" com rótulo errado em T; Country Fields ord. 46 aponta mapper errado; campos de data (`health_insurance_enrollment_start_date`, `labor_pension_contribution_date`) tipados como Text.
- WTC V2.8 tem duas abas ("WTC" e "Wage Type Catalogue") com fórmulas diferentes para 58216/58221.
- `residential_status` (residência fiscal) sendo usado como "estrangeiro" também nas specs SR-106 — mesmo erro em vários relatórios.
- Drive tem um "Join - SI Report Spec.gsheet" em `01 - SOP/Report/Social Security/1. Join` — possível segunda spec do mesmo relatório (não consegui abrir .gsheet pelo disco).
- Formulários do Drive (1-3 de 113.07.16) estão defasados: BLI publica 承表D rev. 115.01.
- SOP Taiwan 1.1 diz "minimum wage 2025 NT$28,590"; a página BLI 0022929 (atualizada 2025-12-31) já fala em 最低工資 "目前為29,500元" → SOP desatualizado para 2026.

## Rascunho de comentário (EN)
> @mjain Spec reviewed against the official NHIA/BLI 3-in-1 batch enrolment format (01_Apply3Of1). The batch is an Excel upload in the NHIA multi-certificate system, with no fixed positions, so there is no official TXT layout for this report. Gaps filled in the spec v1.1 (changes in light blue); main points:
> - Field 6 (投保者) is a per-row value: 1 = employee row, 2 = one extra row per NHI dependent. `$hr.number_of_nhi_dependents` drives the number of dependent rows, so 58212 (tax dependents) is no longer used.
> - Field 12 references 58139, which does not exist in WTC V2.8. Mapped to `$hr.nhi_grade::orLabel`.
> - Fields 7/22 used `$hr.residential_status`, which is tax residency, not nationality. Remapped to nationality + `$hr.spouse_nationality`.
> - Field 11 must be the total monthly wage excluding annual bonuses (NHIA insured-amount guide), not 58009/6220%.
> - Filing method changed to electronic upload. Filing is due on the hire date, not within 3 days.
> - The "New Specification" tab is a withholding tax spec and was removed from this file.
> Pending: latest version of 01_Apply3Of1 (ours is 113.03.31).

*(Rascunho: não postar sem ok do usuário. A versão final depende de a spec ter sido de fato atualizada, o que exige ok do usuário para editar.)*

## O que precisa ser feito
1. Obter o **01_Apply3Of1.docx atual** (eservice.nhi.gov.tw bloqueia acesso de fora de Taiwan): pedir ao usuário, à Lisa/Lily ou ao consultor local (Jhan Ye) — e gravar em `raw/docs/oficiais/TW/`.
2. Decidir com o usuário se atualizamos a spec (export → v1.1, alterações em azul `FFDDEBF7`) com a tabela de proposta acima.
3. Levar ao Mohit os pontos 🟡 (fonte do salário na admissão, objeto da taxa do LP, motivo/linha de dependente, campo universal de nacionalidade, função de largura total).
4. Abrir item de DD (tipos, dependentes 1–6, mapper T, duplicidades) — fora deste ticket.
5. Só depois: comentário ao Mohit e reatribuição.

## Lacunas
- ⚠️ Versão atual do guia F1 não lida (bloqueio geográfico); campos 5, 18 (P) e 27 podem ter mudado.
- ⚠️ Extensão aceita no upload (.xls × .xlsx) não confirmada.
- ⚠️ Nome dos campos universais de nacionalidade, nome local e salário contratado no HR Blizz.
- ⚠️ Se o motor de fórmulas tem conversão para largura total.
- ⚠️ Se `dependent_N_relationship` são dependentes de NHI ou de IR (o DD mistura "Tax Exemption Dependent" e "Social Security Dependent Code").
- ⚠️ Labor Insurance Act art. 14 (definição de 月薪資總額) não lido diretamente (law.moj.gov.tw inacessível daqui); usados F4/F7/F8 e a página BLI 0022929.
- Afirmação do Manjit de que "já existe em TXT": sem como verificar.
