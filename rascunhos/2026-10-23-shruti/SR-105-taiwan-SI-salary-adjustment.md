# SR-105 — TW - SI electronic filing Salary Adjustment (薪調三合一) — análise da spec

> Rascunho de análise (só leitura). Nada foi postado no YouTrack, enviado por e-mail ou alterado no Drive.
> Data: 2026-10-23. Analista: janela Suporte (repasse Manju → Shruti → nós).

## Metadados
| Item | Valor |
|---|---|
| Ticket | SR-105 — https://youtrack.hrblizz.dev/issue/SR-105 |
| Estado / fase | Open / Specification Phase - Research Analyst |
| BA / RA / Dev | Mohit Jain / Manju Shetija (→ Shruti → nós) / Katrin Rudi |
| Reporter | Lisa Quan (jquan), criado 2025-06-27 |
| Escopo descrito | "Combination of 1-5 and 2-3 report" (numeração interna Mercans; pasta `01 - SOP/Report/Social Security/2. Salary adjustment` no Drive) |
| Spec analisada | `raw/docs/drive-exports/2026-10-23/TW - SI electronic filing Salary Adjustment specification.xlsx` (abas Version Control, Report Matrix, Specification, Options) — v1.0 "In Progress", 2025-09-07 |
| Guia / sample do ticket | `SR-105-1-5 Guide 03_Adj3Of1.txt` ("勞保、健保、勞退(3合1) 批次薪資調整格式說明(104.10.05)"); `SR-105-1-5 Sample 03_Adj3Of1.xlsx` |
| DD / WTC | Taiwan Data Dictionary V3.3; Taiwan WTC V2.8 |

## O que foi pedido a nós
Mohit (2026-09-15): "Assigned to Manju for Spec Review only and fill the gaps in specs. Assign back to me once done for Testing and Development." → revisar contra o formato oficial e preencher lacunas. Pendente: pergunta do Manjit (2026-02-02) sobre TXT.

## Histórico do ticket
- 2025-07-02 Srushti: template. 2025-07-09 Brenet pede comentários à Lisa; 07-10 Lisa atualiza ("maybe we need Lily's UI review").
- 2025-07-15 Brenet pede mapeamento ao Mohit. 2025-08-08 Brenet: alinhar descrições a WT/DD.
- 2026-02-02 Manjit: tipo do relatório (TXT?).
- 2026-09-15 Mohit: revisão de spec. Nada feito desde então.

## Layout oficial (fonte primária)

### Fontes
| # | Fonte | Caminho local | Observação |
|---|---|---|---|
| F1 | NHIA/BLI — "勞保、健保、勞退(3合1) 批次薪資調整格式說明(104.10.05)" (doc oficial `03_Adj3Of1.docx`, eservice.nhi.gov.tw/nhiweb1/INS/documents/) | cópia do Drive: `raw/docs/drive-exports/2026-10-23/SR-105-1-5 Guide 03_Adj3Of1.txt` | ⚠️ original **não baixado** (eservice.nhi.gov.tw corta conexão daqui; sem Wayback). 104.10.05 = **2015-10-05** |
| F2 | Sample 03_Adj3Of1 | `raw/docs/drive-exports/2026-10-23/SR-105-1-5 Sample 03_Adj3Of1.xlsx` | dados fictícios |
| F3 | BLI — Formulário 承表S "勞、就、災、健保暨勞退合一投保薪資調整表" **rev. 115.05** (exemplo) | `raw/docs/oficiais/TW/2026-10-23-BLI-form-S-salary-adjustment-3in1-example-115.05.pdf` (bli.gov.tw/Files/10156; página 0103192 atualizada 2026-04-29) | versão em papel vigente |
| F4 | BLI — página 0022929 "投保薪資調整申報作業" (atualizada 2025-12-31) | `raw/docs/oficiais/TW/2026-10-23-BLI-page-0022929-salary-adjustment-procedure.html` | conceito de 月薪資總額 e efeito |
| F5 | BLI — Manual "玖、網路申辦" FAQ 8 | `raw/docs/oficiais/TW/2026-10-23-BLI-manual-cap9-online-filing-FAQ-batch.pdf` | "申報"批次"合一薪調時，調後勞保、勞退金額欄已合併為 1 欄" |
| F6 | NHIA Divisão Leste — folheto 多憑證網路承保系統 | `raw/docs/oficiais/TW/2026-10-23-NHI-east-division-flyer-batch-excel.pdf` | lote "勞健合一(EXCEL檔)" inclui 薪資調整; **薪資調降** exige upload de comprovante |
| F7 | NHIA — "如何正確申報健保投保金額" | `raw/docs/oficiais/TW/2026-10-23-SNHI-nhia-insured-amount-and-supplementary-premium-115v1.pdf` (gravado por outra janela hoje) | itens que entram (O) e não entram (X) no 投保金額 |
| F8 | LSA Enforcement Rules art. 10 | `raw/docs/oficiais/TW/2026-10-23-payslip-LSA-enforcement-rules-mol.html` (outra janela) | exclusões do 經常性給與 (年終獎金, 節金, 紅利…) |

### Formato (o que dá para afirmar)
- **Arquivo Excel** de lote (F6); F1 só define ordem, valores e observações → sem posições, **não é TXT de largura fixa**.
- **Uma coluna para LI e LP:** F1 #11 e F5 FAQ 8 — o "調後月實際工資(勞保、勞退專用)" é único; o BLI classifica nas tabelas de LI e LP e só ajusta o LP se o trabalhador for contribuinte do 勞退.
- **Quando declarar (F3 填表說明 七; F7 攻略 2):** salário mudou entre fev e jul → declarar até o **fim de agosto**; entre ago e jan → até o **fim de fevereiro**; efeito no **dia 1º do mês seguinte** à declaração (F3 注意事項 二; F4 二(二)).
- **Base (F4 二(一)):** média do 月薪資總額 dos **3 meses anteriores**; não só o salário-base — inclui horas extras, 伙食津貼, 全勤獎金, bônus de desempenho/produção… F7 marca como **X** (fora) 年終獎金, 考核獎金, 節金, 紅利; F8 art. 10 exclui esses itens do 經常性給與.
- **Regra NHI (F3 填表說明 六(三)):** 健保投保金額 ≥ salário segurado de LI/EI/OAI e ≥ salário do LP.
- **Só NHI:** F1 #11 — para ajustar só o 健保, deixar em branco 勞工保險證號, 檢查碼 e 調後月實際工資.
- **Escopo do "combination":** o lote sempre tem a parte NHI (#4, #5, #12, #13). O formulário **2-3 (勞、就、災保及勞退, sem NHI)** não tem coluna própria aqui; ⚠️ não há no F1 104.10.05 indicação de como declarar LI/LP sem NHI pelo lote (provável: BLI e-service, por analogia ao guia de加保 113.03.31 #6 — não confirmado).
- **災保:** F3 é o formulário 勞、就、**災**、健保暨勞退; o 災保 é classificado a partir do mesmo 月薪資總額 (F3 填表說明 五(一)). F1 (2015) não menciona 災保 — ⚠️ confirmar se há versão nova.

### Campos oficiais (F1 104.10.05) — 14 colunas
| # | Campo | Valores (F1) |
|---|---|---|
| 1 | 異動別 | "3" (薪資調整) |
| 2 | 勞工保險證號 | 8 dígitos (em branco se só NHI) |
| 3 | 勞工保險證號檢查碼 | 1 letra maiúscula (em branco se só NHI) |
| 4 | 健保投保單位代號 | 9 dígitos |
| 5 | 健保業務組別 | 1–6 |
| 6 | 被保險人外籍 | Y / 1 / 2 / branco |
| 7 | 被保險人姓名 | até 25; estrangeiro: maiúsculas largura total (sample "ＤＡＶＩＤ") |
| 8 | 被保險人身份證號(居留證號碼或護照號碼)(勞保專用) | nacional: 身分證號; estrangeiro: ARC ou passaporte usado no 加保 |
| 9 | 被保險人居留證號碼(健保專用) | só estrangeiro |
| 10 | 被保險人出生日期 | ROC AAAMMDD |
| 11 | 調後月實際工資(勞保、勞退專用) | salário mensal real após ajuste (em branco se só NHI) |
| 12 | 健保調前投保薪資 | faixa NHI anterior (tabela 全民健康保險投保金額分級表) |
| 13 | 健保調後投保薪資 | faixa NHI nova |
| 14 | 特殊身分別 | **só** 1 (部分工時), 8 (部分工時及庇護性身心障礙就業者), branco |

Sample F2: valores com zero à esquerda e 6 dígitos ("040000", "031800") — tratar como texto.

## Estado da spec
**Report Matrix**
| Item | Na spec | Conflito |
|---|---|---|
| Periodicity | **Quarterly** | conflito: janelas semestrais (fev–jul → até fim de ago; ago–jan → até fim de fev) e evento a evento — F3 說明 七 |
| Allowed Submission Frequency | "submit only if adjustment is needed" | ok |
| File Format | XLSX | ok (F6) — ⚠️ extensão |
| File Naming | "Usually unspecified; may follow CompanyCode_Adjustment_YYYYQX.xlsx" | sem fonte; trimestral é errado |
| Filing Method | **Manual: Submit hardcopies offline** | conflito: lote eletrônico (F5, F6) |
| Rounding | "No rounding; salary must be exact" | ok para #11 (BLI classifica); #12/#13 são valores de faixa |
| Introduction | "Submitted quarterly unless there's an urgent change" | conflito (ver Periodicity) |
| Comments | "Employer must print the form and submit with company seal" | vale para o formulário em papel (F3), não para o lote |
| Título A1 da aba Specification | "(October 5, **2014**)" | erro: 104.10.05 = **2015-10-05** |

**Aba Specification** — colunas: Field Name, Local, **C/M/O (vazia)**, **Data Type (vazia)**, Rounding (vazia), Data Format, Start/End Pos (n/a), **Sample (vazia)**, **Report Field Mapping K e L (vazias em todos os campos)**, descrição TA (M), descrição BA (N), coluna O (RA).

| # | Situação | Conflito/observação |
|---|---|---|
| 1 | Data Format "3.0" | texto fixo "3"; sem mapeamento |
| 2–3 | BA: `labor_insure_id` "confirm with RA"; RA: 8 primeiros / última letra | sem mapeamento escrito; DD tipa como **Number**; regra "em branco se só NHI" ausente |
| 4 | BA: "check with RA"; RA "Yes" | sem mapeamento; Number × zero à esquerda |
| 5 | BA: "No such HR field"; RA: mapper "NHI Authority" | o campo existe: `$legal_entity_hr.nhi_authority` (DD V3.3) |
| 6 | BA "No such HR field"; RA "check nationality of employee and spouse" | DD tem `$hr.spouse_nationality`; falta nacionalidade do empregado ⚠️ |
| 7 | "Universal Field" | sem regra de largura total / limite 25 |
| 8, 9 | "Refer $hr.id_type and $hr.id_card_number" | sem fórmula |
| 10 | "Universal Field" | sem fórmula ROC |
| 11 | BA: 58008 + 58009 + 6220%, "check with RA"; RA: "updated LI and LP contribution base amount" | **conflito duplo**: (a) RA descreve como base de contribuição (faixa) — o F1/F5 pedem o **salário real**, o BLI faz a faixa; (b) 58009/6220x = adicionais/bônus anuais (WTC: 62200–62203 "Bonus (Annual/Referral)") → excluídos (F7 年終獎金 X; F8 art. 10); 58008 é **tributável** e deixa de fora 伙食津貼 isento e horas extras que F4/F7 incluem; (c) F4 pede média de 3 meses, não um mês |
| 12 | BA "No Idea"; RA "NHI base before adjustment" | sem mapeamento |
| 13 | BA "No Idea"; RA "NHI base adjusted" | sem mapeamento |
| 14 | RA: mapper "Special Identity Code"; Data Format "1. 8. Blank" | sem regra de filtro: o mapper tem 1–8, A, B, S, T, mas aqui só 1 e 8 são aceitos |
| — | Nota A45 | ok (tradução da nota do F1 #11) |

## Proposta de preenchimento
✅ = sustentado; 🟡 = proposta (decisão RA/BA).

| # | Campo | Antes | Depois (proposto) |
|---|---|---|---|
| — | Periodicity / Introduction | Quarterly | ✅ "Event-driven. Wage changes Feb–Jul: file by end of August; Aug–Jan: file by end of February; effective the 1st of the month after filing (BLI form 承表S 115.05, instr. 7)" |
| — | Filing Method / Comments | Manual / print and seal | ✅ Electronic: Upload online (lote "勞健合一 EXCEL"). Redução de salário exige comprovante (F6) |
| — | Título A1 | October 5, 2014 | ✅ "(2015-10-05, ROC 104.10.05)" |
| — | Population | regular employees | 🟡 empregados com mudança de faixa LI/OAI/LP ou NHI; só NHI → campos 2, 3, 11 em branco |
| 1 | 異動別 | 3.0 | ✅ texto "3" |
| 2 | 勞工保險證號 | — | ✅ 8 primeiros de `$legal_entity_hr.labor_insure_id` (texto); branco se ajuste só NHI |
| 3 | 檢查碼 | — | ✅ 9º caractere UPPERCASE; branco se só NHI |
| 4 | 健保投保單位代號 | — | ✅ `$legal_entity_hr.health_insure_id` PREPAD 9 '0' |
| 5 | 業務組別 | "no field" | ✅ `$legal_entity_hr.nhi_authority::key` |
| 6 | 外籍 | — | 🟡 regra comum às 3 specs: nacionalidade TW → ''; senão `$hr.spouse_nationality` = TW → (CN → "2", demais → "1"); senão "Y" |
| 7 | 姓名 | Universal | 🟡 nacional: nome chinês (`name` 名字); estrangeiro: maiúsculas largura total, máx. 25 |
| 8 | ID (勞保) | — | ✅ `id_type::key` IN (1,2) → `$hr.id_card_number`; 3 → `$hr.passport_number` |
| 9 | ARC (健保) | — | ✅ `id_type::key` = 2 → `$hr.id_card_number`; senão '' |
| 10 | 出生日期 | — | ✅ `CONCAT(PREPAD(SUBTRACT(DATE_FORMAT($person.birth_date;'yyyy');1911);3;'0');DATE_FORMAT($person.birth_date;'MMdd'))` |
| 11 | 調後月實際工資 | 58008+58009+6220% | 🟡 média dos 3 meses anteriores do 月薪資總額 (pagamentos regulares do trabalho: base, adicionais mensais, horas extras, 伙食津貼, bônus mensais de desempenho/assiduidade; **sem** 年終獎金, 考核獎金, 節金, 紅利 — F4, F7, F8). Não existe hoje no WTC um agregado "base LI/NHI" → precisa de um WT interino novo ou lista de WTs aprovada pelo RA. Branco se só NHI |
| 12 | 健保調前投保薪資 | — | 🟡 `$hr.nhi_grade::orLabel` **vigente antes** da alteração (exige histórico/valor anterior do campo HR — ⚠️ confirmar se o produto guarda) |
| 13 | 健保調後投保薪資 | — | ✅ `$hr.nhi_grade::orLabel` atual; validação ≥ faixa LI/OAI e ≥ faixa LP (F3 六(三)) |
| 14 | 特殊身分別 | mapper inteiro | ✅ `IF($hr.special_identity_code::key IN ('1','8'); key; '')` |
| — | Colunas C/M/O, Data Type, Sample | vazias | ✅ preencher: 1,4,5,7,8,10,13 = M; 2,3,11 = C (vazios se só NHI); 6,9,14 = C; 12 = M; tipos Text (IDs/códigos/datas ROC) e Numeric inteiro (11–13) |

## Veredito
**Não está pronta para devolver.** É a menos completa das três: **nenhum** campo tem mapeamento nas colunas K/L, C/M/O e Data Type estão vazios, a Report Matrix tem periodicidade e método errados, e o campo 11 tem uma proposta (58009/6220%) que contraria a definição oficial. Para fechar: decisão do RA sobre a composição do 月薪資總額 (WT interino novo), fonte do NHI anterior (#12) e o guia oficial atual (o nosso é de 2015, antes do 災保).

**Pergunta do Manjit (TXT):** lote oficial em Excel (F6); F1 sem posições → não há layout TXT oficial. ⚠️ O que o produto já gera não é verificável daqui.

## Achados fora do pedido
- WTC V2.8 não tem coluna "subject to LI/NHI/LP" nem agregado de 月薪資總額; o SOP Taiwan 1.1 diz que as faixas são escolhidas **manualmente** (`$hr.li_grade`, `$hr.nhi_grade`…). O produto não sinaliza quando a média de 3 meses muda de faixa — risco de ajustes não declarados nas janelas de agosto/fevereiro.
- Faixas no DD: "LI and EI Bands 2025" e "NHI Bands 2025" — sem as de 2026 (F4 já cita 最低工資 29.500 e F3 cita máximo do 災保 72.800). Conferir se o DD precisa de bandas 2026 (outro ticket).
- SOP Taiwan 1.1: 1-5 "Adjust Insurance Declare" sem prazos; "2-3/1-5 Employer, Employee, Dependent information" — o薪調 não tem dependentes.
- Mesmo padrão de erro nas 3 specs: `residential_status` usado como nacionalidade (SR-106, SR-107).

## Rascunho de comentário (EN)
> @mjain Spec reviewed against the official NHIA/BLI 3-in-1 batch salary adjustment format (03_Adj3Of1). The batch is an Excel upload in the NHIA multi-certificate system, with no fixed positions, so there is no official TXT layout for this report. Changes in spec v1.1 (light blue):
> - All 14 fields now have mappings. Fields 2, 3 and 11 stay blank for NHI-only adjustments (official note on field 11).
> - Field 11 is the actual average monthly wage of the last 3 months, excluding year-end/festival bonuses (BLI salary-adjustment page; NHIA insured-amount guide). 58009/6220% must not be included. The WTC has no aggregate for this, so a new interim pay element is needed; please advise.
> - Fields 12/13: NHI insured amount before/after (`$hr.nhi_grade::orLabel`, previous and current value).
> - Field 14 accepts only 1 and 8.
> - Periodicity is not quarterly: Feb–Jul changes are filed by end of August, Aug–Jan changes by end of February, effective the 1st of the following month (BLI form 承表S). Filing method set to electronic upload.

*(Rascunho: não postar sem ok do usuário; pressupõe a spec v1.1 gravada com ok.)*

## O que precisa ser feito
1. Obter o **03_Adj3Of1.docx atual** (bloqueio geográfico do eservice.nhi.gov.tw).
2. Com ok do usuário: gerar v1.1 da spec a partir do export de hoje, alterações em azul `FFDDEBF7`.
3. Levar ao Mohit: WT interino para 月薪資總額 (lista de WTs que entram, por F7), histórico do `nhi_grade` para o #12, campo de nacionalidade, função de largura total.
4. Comentário e reatribuição ao Mohit depois disso.

## Lacunas
- ⚠️ Guia F1 atual não lido (só 104.10.05); pode ter coluna para 災保 ou mudanças.
- ⚠️ Como o 2-3 (sem NHI) é declarado em lote — não confirmado.
- ⚠️ Se o HR Blizz guarda o valor anterior de `$hr.nhi_grade` (necessário para #12).
- ⚠️ Lista exata de WTs do 月薪資總額 — decisão RA (F7 dá os critérios, não os códigos Mercans).
- ⚠️ Labor Insurance Act art. 14 não lido diretamente (law.moj.gov.tw inacessível daqui).
- ⚠️ Extensão do arquivo aceita (.xls × .xlsx).
- Afirmação do Manjit sobre TXT existente: sem como verificar.
