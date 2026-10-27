# SR-106 — TW - SI electronic filing Termination (退保三合一) — análise da spec

> Rascunho de análise (só leitura). Nada foi postado no YouTrack, enviado por e-mail ou alterado no Drive.
> Data: 2026-10-23. Analista: janela Suporte (repasse Manju → Shruti → nós).

## Metadados
| Item | Valor |
|---|---|
| Ticket | SR-106 — https://youtrack.hrblizz.dev/issue/SR-106 |
| Estado / fase | Open / Specification Phase - Research Analyst |
| BA / RA / Dev | Mohit Jain / Manju Shetija (→ Shruti → nós) / Katrin Rudi |
| Reporter | Lisa Quan (jquan), criado 2025-06-27 |
| Escopo descrito | "Combination of 1-4, 2-2 and 4-2 report" (numeração interna Mercans dos formulários BLI, pasta `01 - SOP/Report/Social Security/5. Withdraw` no Drive) |
| Spec analisada | `raw/docs/drive-exports/2026-10-23/TW - SI Termination specification.xlsx` (abas Version Control, Report Matrix, Spec, Options) — v1.0 "In Progress", sem data |
| Guia / sample do ticket | `SR-106-1-4 guide 02_Stop3Of1.txt` ("勞保、健保、勞退(3合1) 批次退保格式說明(104.10.05)"); `SR-106-1-4 sample 02_Stop3Of1.xlsx` |
| DD / WTC | Taiwan Data Dictionary V3.3; Taiwan WTC V2.8 |

## O que foi pedido a nós
Mohit (2026-09-15): "Assigned to Manju for Spec Review only and fill the gaps in specs. Assign back to me once done for Testing and Development." → revisar a spec contra o formato oficial, preencher lacunas, devolver ao Mohit. Pendente: pergunta do Manjit (2026-02-02) sobre o tipo do relatório ("available in TXT format already").

## Histórico do ticket
- 2025-07-02 Srushti: template da spec. 2025-07-09 Brenet pede comentários à Lisa; 07-10 Lisa atualiza.
- 2025-07-15 Brenet: "Lisa has update the descriptions" → pede mapeamento ao Mohit.
- 2025-08-08 Brenet: alinhar descrições com WT e DD; 08-12 Lisa: "check comments on file".
- 2026-02-02 Manjit: tipo do relatório (TXT?).
- 2026-09-15 Mohit: atribuído para revisão de spec. Nada feito desde então.
- Diferente das outras duas, esta spec **já tem a coluna de mapeamento preenchida** (F, "Report Field Mapping"), provavelmente pelo Mohit.

## Layout oficial (fonte primária)

### Fontes
| # | Fonte | Caminho local | Observação |
|---|---|---|---|
| F1 | NHIA/BLI — "勞保、健保、勞退(3合1) 批次退保格式說明(104.10.05)" (doc oficial `02_Stop3Of1.docx`, eservice.nhi.gov.tw/nhiweb1/INS/documents/) | cópia do Drive: `raw/docs/drive-exports/2026-10-23/SR-106-1-4 guide 02_Stop3Of1.txt` | ⚠️ original **não baixado** (eservice.nhi.gov.tw corta a conexão a partir daqui; sem cópia no Wayback). Data 104.10.05 = **2015-10-05**, anterior ao 災保 (2022) → pode haver versão mais nova |
| F2 | Sample 02_Stop3Of1 | `raw/docs/drive-exports/2026-10-23/SR-106-1-4 sample 02_Stop3Of1.xlsx` | dados fictícios |
| F3 | BLI — Formulário 承表L "勞、就、災、健保暨勞退合一退保申報表" **rev. 113.06** (exemplo) | `raw/docs/oficiais/TW/2026-10-23-BLI-form-L-termination-3in1-example-113.06.pdf` (bli.gov.tw/Files/8008; página 0009849 atualizada 2026-01-22) | versão em papel vigente |
| F4 | BLI — Manual "玖、網路申辦" (FAQ 2, 5, 6) | `raw/docs/oficiais/TW/2026-10-23-BLI-manual-cap9-online-filing-FAQ-batch.pdf` | "合一申報/加保、退保功能(包含單筆及批次申報)" |
| F5 | NHIA Divisão Leste — folheto 多憑證網路承保系統 | `raw/docs/oficiais/TW/2026-10-23-NHI-east-division-flyer-batch-excel.pdf` | "申報批次勞健合一(EXCEL檔)加保、退保、薪資調整" |

### Formato (o que dá para afirmar)
- **Arquivo Excel** de lote no sistema NHIA (F5); o guia F1 só define **ordem, valores válidos e observações**, sem posição/comprimento → não é TXT de largura fixa.
- **Prazo/efeito (F3):** o 退保 é feito **no dia** do desligamento (離職當日); LI/EI terminam às 24h do dia do envio; **NHI termina às 24h do dia do evento** (退保原因發生之當日). F3 填表說明 六.
- **Dependentes:** F1 nota final e F3 填表說明 三 — ao desligar o titular, os dependentes do NHI saem junto; não se informa linha de dependente.
- **Escopo do "combination":** F1 campo 6 aceita 2 (勞保健保勞退) e 3 (só 健保, que deve ir pelo sistema NHIA). Não há valor para "sem 健保" → o formulário **2-2 (勞、就、災保及勞退, sem NHI)** não cabe neste lote. Para **4-2 (災保+勞退)**: a cópia 104.10.05 não tem valor "4" no 投保別 (o guia de加保 113.03.31 tem). ⚠️ Confirmar no F1 atual.
- **勞退:** F4 FAQ 5 — se a data de fim do 勞退 for diferente da data do 退保, declarar separadamente no 勞退申辦作業 (não há campo para isso no lote).

### Campos oficiais (F1 104.10.05) — 16 colunas
| # | Campo | Valores (F1) |
|---|---|---|
| 1 | 異動別 | "2" (退保) |
| 2 | 勞工保險證號 | 8 dígitos |
| 3 | 勞工保險證號檢查碼 | 9º caractere, 1 letra maiúscula |
| 4 | 健保投保單位代號 | 9 dígitos |
| 5 | 健保業務組別 | 1–6 |
| 6 | 投保別 | 2 = 勞保健保勞退; 3 = 健保 (só via sistema NHIA) |
| 7 | 投保者 | 1 = 本人 |
| 8 | 被保險人外籍 | Y / 1 / 2 / branco |
| 9 | 被保險人姓名 | até 25 caracteres; estrangeiro em inglês: maiúsculas de largura total |
| 10 | 被保險人身份證號(居留證或護照號碼)(勞保專用) | nacional: 身分證號; estrangeiro: ARC ou passaporte, **o mesmo usado no 加保** |
| 11 | 被保險人居留證號碼(健保專用) | só estrangeiro: ARC; nacional em branco |
| 12 | 被保險人出生日期 | ROC AAAMMDD |
| 13 | 健保退保原因別 | 1 = 退保; 2 = 轉出 |
| 14 | 健保退保原因說明別 | 退保: M 死亡, E 失蹤滿六個月, U 喪失資格; 轉出: 1 離職, 2 退休, 3 停、歇業, 4 退會 |
| 15 | 健保退保原因說明 | texto: 退保 → 「死亡」「失蹤」「喪失資格」; 轉出 → 「離職」「退休」「停、歇業」「退會」 (sample: "離職", "失蹤") |
| 16 | 健保退保原因發生日期 | ROC AAAMMDD |

F3 (承表L) 填表說明 九: "轉出" = desligamento, aposentadoria etc. de 1ª categoria; "不具健保資格" só M/E/U. Para desligamento comum: 13 = "2", 14 = "1", 15 = "離職".

## Estado da spec
**Report Matrix**
| Item | Na spec | Conflito |
|---|---|---|
| File Format | XLSX | ok (F5) — ⚠️ extensão exata não confirmada |
| Filing Method | **Manual: Submit hardcopies offline** | conflito: lote eletrônico (F4, F5) |
| Comments | "within **3 days** of the last working day" | conflito: F3 — no **dia** do desligamento |
| Periodicity | Period; Inclusion: termination | ok |
| Version Control | país "<Country name>", sem data | lacuna |

**Aba Spec** — colunas: Field Name, Local Language, Data Format, Sample (vazia), Report Field Mapping (F), descrições TA/BA, coluna I (RA). Sem M/C/O, tipo, comprimento.

| # | Mapeamento atual (col. F) | Conflito/observação |
|---|---|---|
| 1 | Always "2" | ok; Data Format "2.0" → texto "2" |
| 2 | labor_insure_id 8 primeiros | ok; DD tipa como **Number** (perde zero à esquerda; tem letra) |
| 3 | labor_insure_id 9º caractere | ok (UPPERCASE) |
| 4 | health_insure_id 9 dígitos | ok; mesmo risco de tipo Number |
| 5 | `$legal_entity_hr.nhi_authority::key` | ok; coluna H ainda diz "Field not configured" (desatualizada) |
| 6 | `$hr.insurance_coverage::key` | ok (DD mapper "Insurance Coverage": 2, 3). Nota: "3" não deveria ir neste lote (F1 #6) |
| 7 | Always "1" | ok (F1 #7) |
| 8 | `IF(residential_status = '1'; 'Y'; '')` | **conflito**: `residential_status` = residência **fiscal** (DD mapper 0 Resident / 1 Non-Resident; WT 58218 "Tax Residency"). Estrangeiro residente sairia em branco; nacional não residente sairia "Y"; 1/2 (cônjuges) nunca saem. Descrição BA (col. H) inverte a lógica ("if dependent nationality != TW then 1") |
| 9 | `UPPERCASE($employee_name)` | conflito: F1 #9 exige **largura total** para nomes em inglês (sample "ＥＭＩＬＹ"); nacional deve ir em chinês; limite 25 |
| 10 | `IF(residential_status='1'; id_card_number; passport_number)` | **conflito**: nacional residente (0) receberia o **passaporte** em vez do 身分證號 |
| 11 | `IF(residential_status='0'; id_card_number; '')` | **conflito**: nacional receberia o 身分證號 num campo que deve ficar **em branco**; estrangeiro com ARC ficaria vazio se não residente fiscal |
| 12 | fórmula ROC com PREPAD | ok |
| 13 | `$hr.health_insurance_withdrawal_reason_code` | **nome não existe no DD**: o DD V3.3 tem `$hr.health_insurance_withdraw_reason_code`; falta `::key` |
| 14 | `$hr.health_insurance_withdrawal_reason_explanation` | idem (`…withdraw_reason_explanation`); Data Format com texto solto ("Surrender policy", "Transfer to") |
| 15 | **"Not needed field"** | **conflito**: F1 lista o campo 15 e o sample preenche ("離職", "失蹤"). Nome em inglês repete o do #14 |
| 16 | `CONCAT(SUBTRACT(yyyy;1911); MMdd)` de `$employee.last_working_date` | ok no conteúdo; sem PREPAD de 3 dígitos (inconsistente com #12) |
| — | Nota A65 | contém "以上翻译结果来自有道神经网络翻译" (lixo de tradutor) |

## Proposta de preenchimento
✅ = sustentado por F1/F3/DD; 🟡 = proposta.

| # | Campo | Antes | Depois (proposto) |
|---|---|---|---|
| — | Filing Method | Manual hardcopies | ✅ Electronic: Upload online (lote "勞健合一 EXCEL", NHIA) |
| — | Comments | 3 days | ✅ "File on the separation date; LI/EI coverage ends 24:00 on the filing date, NHI ends 24:00 on the reason date (BLI form 承表L 113.06). Dependants' NHI is transferred out automatically. If the LP stop date differs from the LI withdrawal date, file the LP stop separately in the BLI e-service." |
| — | Population | Employees terminated | 🟡 limitar a quem tem `$hr.insurance_coverage` = 2 (com NHI); quem não tem NHI (2-2/4-2) fica fora do lote |
| 1 | 異動別 | 2.0 | ✅ texto "2" |
| 2–4 | IDs do empregador | ok | ✅ manter; gerar como texto (PREPAD zeros) |
| 5 | 業務組別 | ok | ✅ `$legal_entity_hr.nhi_authority::key` (corrigir col. H) |
| 6 | 投保別 | insurance_coverage | ✅ `$hr.insurance_coverage::key`; 🟡 sempre "2" neste lote |
| 7 | 投保者 | "1" | ✅ "1" |
| 8 | 外籍 | residential_status | 🟡 mesma regra do SR-107: nacionalidade TW → ''; senão, se `$hr.spouse_nationality` = TW → (CN → "2", demais → "1"); senão "Y" (⚠️ campo universal de nacionalidade) |
| 9 | 姓名 | UPPERCASE | 🟡 nacional: nome em chinês (`name` 名字); estrangeiro: maiúsculas largura total, máx. 25 |
| 10 | ID (勞保) | residential_status | ✅ IF `id_type::key` IN (1,2) → `$hr.id_card_number`; IF 3 → `$hr.passport_number` |
| 11 | ARC (健保) | residential_status | ✅ IF `id_type::key` = 2 → `$hr.id_card_number`; senão '' |
| 12 | 出生日期 | ok | ✅ manter |
| 13 | 退保原因別 | nome errado | ✅ `$hr.health_insurance_withdraw_reason_code::key` (1/2); 🟡 padrão "2" (轉出) quando vazio |
| 14 | 原因說明別 | nome errado | ✅ `$hr.health_insurance_withdraw_reason_explanation::key` (M/E/U/1–4); 🟡 padrão "1" (離職) |
| 15 | 原因說明 | "Not needed" | ✅ texto derivado do #14: M→死亡, E→失蹤, U→喪失資格, 1→離職, 2→退休, 3→停、歇業, 4→退會 (rótulos curtos do F1 #15, não o "Local Value" longo do mapper) |
| 16 | 發生日期 | sem PREPAD | ✅ `CONCAT(PREPAD(SUBTRACT(DATE_FORMAT($employee.last_working_date;'yyyy');1911);3;'0');DATE_FORMAT($employee.last_working_date;'MMdd'))` |
| — | Colunas | ausentes | ✅ acrescentar M/C/O e Data Type; validar consistência 13×14 (1 → M/E/U; 2 → 1–4) |

## Veredito
**Quase pronta, mas não para devolver ainda.** O esqueleto e o mapeamento existem; faltam: corrigir #8, #10, #11 (lógica com residência fiscal — gera dado errado para nacionais), #13/#14 (nomes de campo inexistentes no DD), incluir #15, corrigir Report Matrix (método e prazo) e confirmar o guia oficial atual (o nosso é de 2015, antes do 災保).

**Pergunta do Manjit (TXT):** o lote oficial é Excel (F5) e o F1 não define posições → não há layout TXT oficial para este relatório. ⚠️ O que o produto já gera não é verificável daqui.

## Achados fora do pedido
- Mesmo erro de `residential_status` como "estrangeiro" no SR-107 (campo 22) — padrão a corrigir nas três specs.
- DD V3.3: tipos Number para `labor_insure_id`/`health_insure_id`; mapper "Health Insurance Withdraw Reason Explanation" tem "Local Value" longos, diferentes dos textos curtos exigidos no campo 15.
- Formulários do Drive (1-4 de 113.06.21) — o BLI publica 承表L com rodapé 113.06; conferir se é a mesma revisão.
- Nota A65 da spec com marca d'água do tradutor Youdao.

## Rascunho de comentário (EN)
> @mjain Spec reviewed against the official NHIA/BLI 3-in-1 batch withdrawal format (02_Stop3Of1). The batch is an Excel upload in the NHIA multi-certificate system, with no fixed positions, so there is no official TXT layout for this report. Changes in spec v1.1 (light blue):
> - Fields 8, 10, 11 used `$hr.residential_status`, which is tax residency. Remapped to nationality / `$hr.id_type`. As it was, nationals would get the passport in field 10 and their ID in field 11, which must be blank.
> - Fields 13/14 pointed to `…withdrawal_reason…`. The DD field is `$hr.health_insurance_withdraw_reason_code` / `_explanation` (::key).
> - Field 15 is part of the official format (text: 離職, 退休, 死亡…). Mapped from field 14.
> - Filing method set to electronic upload. Filing is due on the separation date, not within 3 days.
> - Employees without NHI (forms 2-2/4-2) cannot be filed in this batch.

*(Rascunho: não postar sem ok do usuário; pressupõe a spec v1.1 gravada com ok.)*

## O que precisa ser feito
1. Obter o **02_Stop3Of1.docx atual** (bloqueio geográfico do eservice.nhi.gov.tw) e checar se há valor para 災保 (4) no campo 6.
2. Com ok do usuário: gerar v1.1 da spec a partir do export de hoje, alterações em azul `FFDDEBF7`.
3. Levar ao Mohit: campo universal de nacionalidade; função de largura total; padrão para #13/#14 quando o HR não preencher.
4. Comentário e reatribuição ao Mohit só depois.

## Lacunas
- ⚠️ Guia F1 atual não lido (só a cópia 104.10.05).
- ⚠️ Tratamento de 2-2 e 4-2 (sem NHI) — fora do lote; se o produto precisar deles, é outro relatório (BLI e-service).
- ⚠️ Campos universais (nacionalidade, nome local) e valores de `$person.gender`/`id_type`.
- ⚠️ Extensão do arquivo aceita (.xls × .xlsx).
- Afirmação do Manjit sobre TXT existente: sem como verificar.
