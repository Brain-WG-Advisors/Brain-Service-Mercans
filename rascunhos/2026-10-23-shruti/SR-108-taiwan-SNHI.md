# SR-108: TW, SNHI report (補充保險費, bônus acima de 4× o insured amount)

> Análise só leitura, 2026-10-23 (janela Suporte). Nada foi postado, enviado nem gravado no Drive.
> Rascunho para revisão do usuário antes de qualquer comentário no YouTrack.

## Metadados
| Campo | Valor |
|---|---|
| Ticket | SR-108, "TW - SNHI report" (https://youtrack.hrblizz.dev/issue/SR-108) |
| Estado / fase | In Review / Specification Phase - Research Analyst |
| Assignee | Wallisson (wgomes), vindo da Manju → Shruti |
| BA / RA / Dev | Mohit Jain / Manju Shetija / Katrin Rudi (configuração feita por Shaik Jani Sharif) |
| Reporter | Lisa Quan, criado em 2025-06-26; due date 2025-07-10 (vencida) |
| Report code | `tw-snhi` (configurado em nível país em 2026-02-10) |
| Spec analisada | `raw/docs/drive-exports/2026-10-23/TW - SNHI report specification.xlsx` (Version Control: 1.0 de 27/06/2025, 1.1 de 31/07/2025 "Approved", Mohit) |
| Anexos | `raw/tickets/api/anexos/SR-108/20250723-1204 - SNHI_sample.txt`; doc citado no ticket = `raw/docs/drive-exports/2026-10-23/SR-108-SNHI-doc-txt-bonus.txt` |
| Cópia do ticket | `raw/tickets/api/2026-10-23-ex-skamble/SR-108.md` |

## O que foi pedido a nós
Mohit, 15/09/2026: "Assigned to Manju for Spec Review only and fill the gaps in specs. Assign back to me once done for Testing and Development."
Ou seja: revisar a spec contra a fonte oficial, preencher as lacunas (descrição, mapeamento, validação) e devolver ao Mohit. Não é pedido de teste nem de configuração.

## Histórico do ticket
- 2025-06-26 Lisa pede o relatório SI de Taiwan; 2025-06-27 Brenet cria a spec TXT e pede o preenchimento de "Report field mappings".
- 2025-07-31 Mohit: mapeamento BA feito, mas "the specification file provided is not clear to me"; pede contato com a RA. Versão 1.1 registrada como "BA Mapping is completed. Kindly get in touch with RA".
- 2025-07-22 / 08-12 Lisa responde na coluna J (Clarifications by LISA).
- 2026-01-29 Jani: configuração concluída, 3 perguntas na spec (colunas K/L). 2026-02-02 Mohit: "Responses are updated" (coluna L).
- 2026-02-10 Jani: entidade de teste REF-LE-02-826 "Taiwan Testing" (Acceptance); relatório configurado em nível país, código `tw-snhi`.
- 2026-09-15 Mohit: atribuído para revisão de spec.

## Fonte primária
Todas as cópias em `C:\Users\instituto\Documents\brain-service\raw\docs\oficiais\TW\`.

| # | Fonte | Arquivo local | O que prova |
|---|---|---|---|
| F1 | NHI Act (全民健康保險法) arts. 31, 33, 34, texto do 全國法規資料庫 (via Wayback, salvo pela janela dos SR-105/106/107) | `2026-10-23-nhi-act-L0060001-moj-wayback.txt` | art. 31 §1(1): bônus "全年累計逾當月投保金額四倍部分"; retenção na hora do pagamento, recolhimento até o fim do mês seguinte; parte de pagamento único acima de NT$10 milhões isenta. art. 34: o empregador paga suplementar sobre (folha total − total dos insured amounts) |
| F2 | 全民健康保險扣取及繳納補充保險費辦法 (alterado em 2024-03-20, via Wayback) | `2026-10-23-nhi-supplementary-premium-regulations-L0060027-moj-wayback.txt` | art. 3(1): definição de bônus (年終獎金、節金、紅利…, renda salarial fora do insured amount); art. 4: bônus acima de 4× "全數計收" (sem piso de NT$20.000); art. 6: "全年累計" = de 1º de janeiro até o pagamento; leaver = 4× o insured amount da saída; art. 10: declaração do 扣費明細 até 31/01 do ano seguinte (05/02 se houver 3+ feriados) **ou** junto com cada recolhimento, por meio eletrônico, o que dispensa a anual; o detalhe deve trazer nome, ID, data de pagamento, tipo de renda, valor e prêmio |
| F3 | NHIA, formato oficial TXT do 扣費明細, tipo 62 | `2026-10-23-SNHI-nhia-bonus-62-detail-file-format-txt.pdf` (igual ao doc do Drive `SR-108-SNHI-doc-txt-bonus.txt`) | Posições, tipos N/C, ROC yyymm/yyymmdd, "不可為負值", soma do resumo = soma dos detalhes, codificação ASCII e BIG5, nome em caractere full-width, campo compartilhado 93–132 |
| F4 | NHIA, formato oficial CSV do mesmo detalhe | `2026-10-23-SNHI-nhia-bonus-62-detail-file-format-csv.pdf` | Regra do 申報編號: padrão "1"; 2, 3… quando o mesmo beneficiário tem 2+ pagamentos no mesmo dia e tipo; ou numeração própria, alfanumérica, até 30, sem repetição |
| F5 | NHIA, resumo 115 (2026) dos补充保費 | `2026-10-23-SNHI-nhia-115-supplementary-premium-summary.pdf` | Código 62; declaração mensal (網路/媒體, junto com o recolhimento) ou anual (網路/媒體/書面, até 31/01); prêmio do empregador (código 61) "不需申報明細"; bônus sem piso; teto de NT$10 milhões por pagamento |
| F6 | NHIA, introdução ao suplementar | `2026-10-23-SNHI-nhia-2nd-gen-supplementary-premium-intro.pdf` | Taxa 2,11% a partir de 2021-01-01 (110/1/1) |
| F7 | NHIA Southern Division, "如何正確申報健保投保金額" 115.1版 | `2026-10-23-SNHI-nhia-insured-amount-and-supplementary-premium-115v1.pdf` | 年終獎金、考核獎金、紅利、節金 entram no bônus SNHI; exemplo numérico: base = min(pagamento, acumulado − 4×insured) × 2,11% |
| F8 | NHIA, formulário em papel do detalhe tipo 62 | `2026-10-23-SNHI-nhia-bonus-62-detail-declaration-form.pdf` | Colunas do detalhe (data de pagamento, ID, nome, valor do bônus, prêmio, 投保單位代號, insured amount do mês, bônus acumulado no ano) |

Fontes internas (secundárias, só apoio): WTC V2.8, DD V3.3, Country SOP Taiwan 1.1 (exports de 2026-10-23).

## Estado da spec
Aba `Spec(TXT)`: 3 seções (A cabeçalho, B detalhe, C resumo), 38 linhas. Posições e comprimentos das colunas C/D conferem com F3 (todas as 3 seções somam 200). A aba `Testing` tem a saída da configuração.

### Lacunas (sem mapeamento ou sem regra)
| Linha | Campo | Situação |
|---|---|---|
| Report Matrix | Allowed Submission Frequency, Population Range, Inclusion Filter, Reporting Currency, Language, Introduction | vazios |
| A9 | Parent Unit Number (29–36) | sem mapeamento (só descrição) |
| A11 | Name of Withholding Agent | mapeado para `$legal_entity.name`, sem regra de full-width/padding |
| B18 | Income Payment Date (22–28) | **sem mapeamento** (só "YYYMMDD") |
| B23–B27 | Shared Field Area | linha-mãe com "Input 62" (incorreto: é um bloco, não um valor) |
| B29 | Recipient Name | mapeamento só na coluna RA (`$employee_name`), coluna BA vazia |
| C35 | Total Entries | **sem mapeamento** |
| A8 / B18 | Datas | sem conversão para ano ROC |

### Conflitos com a fonte oficial
| # | Linha / campo | Spec hoje | Fonte oficial | Fonte |
|---|---|---|---|---|
| C1 | Report Matrix, Periodicity | Quarterly | Mensal (junto com o recolhimento, eletrônico) **ou** anual até 31/01 do ano seguinte; um arquivo não cruza dois anos de pagamento | F2 art. 10; F5 p.1; F3 campo A4 |
| C2 | Report Matrix, Filing Method | "Manual: Submit hardcopies offline" | O TXT é para envio eletrônico (網路/媒體); papel é outro canal | F5 p.1; F2 art. 10 §3 |
| C3 | Report Matrix, Encoding | ASCII | "資料碼: ASCII及BIG5": nomes em caractere full-width exigem BIG5 | F3 nota 3 |
| C4 | A4 / B14 UBN (2–9) | `$legal_entity_hr.social_security_integrate_number` | 扣費單位統一編號 (UBN do扣費義務人). A própria spec usa `company_registration_number` na seção C (C33): os três precisam do mesmo campo | F3 seções 一/二/三 campo 2 |
| C5 | A8 File Creation Date | descrição "yyyymmdd", mapeamento `$report.generation_time` | `yyymmdd` (ano ROC, 7 posições) | F3 A6 |
| C6 | A6/A7 Income Start/End (col. F) | "Format: yyyymm" | `yyymm` (ROC, 5) | F3 A4/A5 (a coluna G da RA já está certa) |
| C7 | B20 Declaration Number | `CONCAT(DOB YYYYMMDD, Employee ID)` "left padded with 0" | Tipo C: alinhado à esquerda, completar à direita com espaços; alfanumérico, sem repetição. Com DOB+ID, dois bônus do mesmo empregado no ano repetem o número | F3 B8 e nota 2; F4 |
| C8 | B23 shared field, 93–101 (投保單位代號, 9) | `social_security_integrate_number` (DD: 8 dígitos, "統一編號") | Código da unidade segurada no NHI, 9 posições (exemplo oficial `123456789`) | F3 nota 4; F8 |
| C9 | B25 Monthly Insured Salary | `SUM(58139)` | 扣費當月投保金額. O PE 58139 **não existe** no WTC V2.8 | F3 nota 4; WTC V2.8 |
| C10 | C36 Total Bonus Amount | "Total of YTD 58009 for all employees" (Lisa: YTD) | 為扣費明細所得(收入)給付金額之總計 = soma do campo B (69–82) das linhas do arquivo | F3 seção 三 campo 5; a amostra oficial fecha: 116.073 + 54.606 + 69.042 + 47.221 = 286.942 |
| C11 | C37 Total Supplementary Fee | "Total of YTD 2558" (Lisa: YTD) | Soma do campo 83–92 das linhas do arquivo | F3 seção 三 campo 6; amostra: 740 + 468 + 617 + 276 = 2.101 |
| C12 | C39 Contact Name | `$legal_entity_hr.representative` (代表人) | 聯絡人姓名 (pessoa de contato), full-width | F3 seção 三 campo 8 |
| C13 | E37 / E38 (amostras) | `000000000000210127` / `065866#1111` | Lendo a amostra oficial pelas posições: total do prêmio = `0000000000002101` (41–56); telefone começa na 57 | F3 + parse do `SNHI_sample.txt` |
| C14 | Aba Testing | UBN ausente (as posições deslocam 8), data de pagamento `-191112`, prêmio `-28590` / `-57180`, resumo zerado | Campos N "不可為負值"; UBN obrigatório | F3. Observação: 28.590 é o salário mínimo de 2025 (F5 p.4), o que sugere campo-fonte errado |

Conferido e correto: posições/comprimentos de todas as linhas; Data ID 1/2/3; Income Type 62; Serial Number N com zeros à esquerda; Processing Type I/R; Trust Indicator e Data Note em branco para salário; Reserved em branco; Supplementary Fee = 2558 do período (prêmio efetivamente retido); YTD do bônus incluindo o pagamento atual (F2 art. 6).

## Proposta de preenchimento
> **Proposta**, não aplicada na spec. Mapeamentos novos marcados ⚠️ dependem de confirmação do BA (campo/PE do motor).

| Linha | Campo | Antes | Depois (proposto) | Fonte |
|---|---|---|---|---|
| RM | Periodicity / Allowed Submission Frequency | Quarterly / vazio | `Period` (mensal, junto com o recolhimento até o fim do mês seguinte ao pagamento) e `Tax Year` (anual, até 31/01 do ano seguinte). Um arquivo por ano de pagamento | F2 arts. 4 e 10; F3 A4 |
| RM | Filing Method | Manual: hardcopies | Electronic: Upload online | F5 |
| RM | Report Encoding | ASCII | BIG5 (campos ASCII em half-width; nomes em full-width) | F3 nota 3 |
| RM | Population / Inclusion Filter | vazio | Empregados com prêmio de bônus retido no período do arquivo (2558 do período > 0) ⚠️ confirmar se pagamentos de bônus sem retenção entram (F2 art. 10 fala em "扣取之補充保險費金額") | F2 art. 10 |
| RM | Rounding | No decimals | manter; prêmio arredondado no NT$ ("角以下4捨5入") | F3 B10 |
| A4, B14, C33 | UBN | `social_security_integrate_number` (A/B), `company_registration_number` (C) | `$legal_entity_hr.company_registration_number` nas três seções (公司統一編號, 8). ⚠️ O DD rotula os dois campos como "統一編號"; o BA confirma qual deles guarda o UBN | F3 campo 2 |
| A6 / A7 | Income Start / End | col. F "yyyymm" | Descrição: "ROC yyymm; menor/maior mês de pagamento das linhas do arquivo; mesmo ano". Mapeamento atual (data do 1º/último bônus) mantido | F3 A4/A5 |
| A8 | File Creation Date | `$report.generation_time` | `CONCAT(SUBTRACT(DATE_FORMAT($report.generation_time;'yyyy');1911); DATE_FORMAT($report.generation_time;'MMdd'))` (padrão já usado na Tax Report Spec, H18) | F3 A6 |
| A9 | Parent Unit Number | sem mapeamento | Em branco (8 espaços) se unidade única; campo de entidade se houver matriz ⚠️ não há campo no DD | F3 A7 |
| A11 / B29 / C39 | Nomes | sem regra | Converter para full-width e completar com espaço full-width até 25 caracteres (50 bytes BIG5). C39 = contato do empregador (fallback: representative) ⚠️ campo de contato não existe no DD | F3 A9, B13, C8 |
| B16 | Serial Number | "000000001" (resposta do Mohit à pergunta K16) | Sequencial por linha: `LPAD($row_number;9;'0')` (o Testing já sai 000000001…000000005) | F3 B4 |
| B18 | Income Payment Date | **vazio** | Data de pagamento do payrun em ROC `yyymmdd` ⚠️ variável do motor a indicar pelo BA | F3 B6; F2 art. 10 §4 |
| B20 | Declaration Number | DOB + Employee ID, zeros à esquerda | `CONCAT($employee.reference_code; DATE_FORMAT(payment date;'yyyyMMdd'))`, alinhado à esquerda com espaços à direita, sem DOB; se o mesmo empregado tiver 2+ bônus no mesmo dia, sufixo sequencial | F3 B8; F4 |
| B21 / B26 | Bonus Payment Amount / Annual Accumulated Bonus | 58009 período / YTD 58009 | Manter o desenho (valor cheio do pagamento atual; acumulado do ano incluindo o atual), **mas** usar a mesma base de bônus que alimenta o 2558. ⚠️ No WTC V2.8, 58009 = "sum of 6222% and 6221% series" (coluna U), o que deixa de fora 6220x "Bonus (Annual/Referral)"; o NHIA inclui 年終獎金 (F2 art. 3; F7) | F3 B9; F2 arts. 3 e 6 |
| B23 | Shared Field Area | "Input 62" | Remover o valor; a linha é o bloco 93–132 descrito nas linhas B24–B27 | F3 nota 4 |
| B24 | 投保單位代號 (93–101) | `social_security_integrate_number` | Código da unidade no NHI, 9 posições. Candidato: `$legal_entity_hr.insurance_certification_number` (DD: 保險證號, "8 digits + 1 text") ⚠️ confirmar se é o código do NHI e não o do Labor Insurance | F3 nota 4; F8 |
| B25 | Monthly Insured Salary | `SUM(58139)` (PE inexistente) | `SUM(64550)` (SNHI Interim Base = `$hr.nhi_grade::orLabel`) ⚠️ BA confirma; para leaver, insured amount da saída | F3 nota 4; F2 art. 6 |
| B27, A12, C40, B31 | Reserved | "Blank" | espaços half-width | F3 |
| C35 | Total Entries | vazio | `LPAD(COUNT(linhas tipo 2);9;'0')` | F3 seção 三 campo 4 |
| C36 | Total Bonus Amount | YTD 58009 de todos | Soma do campo 69–82 das linhas do arquivo, zeros à esquerda (20) | F3 seção 三 campo 5 |
| C37 | Total Supplementary Fee | YTD 2558 de todos | Soma do campo 83–92 das linhas do arquivo (16) | F3 seção 三 campo 6 |
| Todos N | Validação | parcial | Nunca negativo; sem vírgula ou símbolo; à direita com zeros. Todos C: à esquerda com espaços | F3 notas 1–2 |
| E37 / E38 | Samples | valores mal recortados | `0000000000002101` / telefone a partir da posição 57 | F3 + amostra |

## Status dos pontos do ticket
| Ponto (quem, quando) | Resposta dada | Status contra a fonte |
|---|---|---|
| Jani K16: de onde vem "062" no serial / pode ser o número da linha | Mohit: "fixed. it is now 000000001" | Parcial: o serial é numeração livre do empregador, N, zeros à esquerda (F3 B4). Deve **incrementar** por linha; o Testing já incrementa. Redigir na spec como sequencial |
| Jani K17: como diferenciar I e R | Mohit: produto não suporta R; sempre I | Compatível com F3 (R é para corrigir registro já declarado). Registrar na spec que correções saem fora do relatório |
| Jani K20: valor do Declaration Number | Mohit: DOB+Employee ID com zeros à esquerda | **Conflita** com F3/F4 (tipo C, espaço à direita) e pode repetir no ano. Ver proposta B20 |
| Mohit I37: total do prêmio é YTD ou período? | Lisa J37: YTD | **Resposta da fonte: nem YTD por empregado**: total = soma das linhas do arquivo (F3 seção 三; amostra oficial confere) |
| Mohit 2025-07-31: spec "not clear" | Lisa respondeu na coluna J | Coberto por esta revisão |

## Veredito
**Não está pronta para devolver ao Mohit.** Faltam: (1) corrigir os conflitos C1–C13 (periodicidade, canal, codificação, UBN, datas ROC, declaration number, código da unidade NHI, insured amount, totais do resumo, contato); (2) preencher B18 (data de pagamento) e C35 (total de linhas); (3) três confirmações do BA: base de bônus que alimenta o 2558 (inclui 6220x?), PE do insured amount (64550?) e campo do 投保單位代號 no DD. Feito isso, a spec fica pronta para o Mohit testar; a saída atual da aba Testing não passaria na validação do NHIA (negativos, UBN ausente, datas inválidas).

## Achados fora do pedido
1. **WTC V2.8, 58009**: coluna U diz que o bônus é a soma das séries 6221x e 6222x; a série 6220x "Bonus (Annual/Referral)" fica fora. Se a base do 2558 seguir o 58009, o bônus anual (年終獎金) não paga suplementar, contra F2 art. 3(1) e F7. Os PEs do SNHI (58132–58137, 58558) estão sem fórmula no WTC, então não dá para confirmar. Vai para o hub de Taiwan, não para o comentário.
2. A amostra anexada (`SNHI_sample.txt`) é de 2016 (ano ROC 105, taxa de 1,91% na época: 38.729 × 1,91% = 740). Não usar para testar a taxa; a atual é 2,11% desde 2021-01-01 (F6).
3. Prêmio do empregador (art. 34, código 61, PE 2568) não tem detalhe a declarar (F5: "不需申報明細"): correto que fique fora deste relatório.
4. F2 art. 6 §2: bônus pago depois do desligamento usa o insured amount da saída. A spec não trata leaver.
5. DD V3.3, option mapper "Identity Type", key 4: rótulo em inglês "mainland person living in Taiwan less than 183" × rótulo local "總機構在中華民國境外之在臺分公司" (correto conforme MOF). Afeta o SR-110, não este.

## Rascunho de comentário (EN)
> @mjain Spec review done; changes highlighted in the spec (v1.2). Main points, all from the NHIA TXT format for income type 62 and the Supplementary Premium Regulations:
> 1. Totals in section C (positions 21–40 and 41–56) are the sum of the detail lines in the file, not YTD (the NHIA sample adds up this way).
> 2. UBN (2–9) should be the company UBN in all three sections; positions 93–101 are the 9-character NHI insured-unit code, not the UBN.
> 3. Dates are ROC (yyymm / yyymmdd); Income Payment Date (22–28) and Total Entries (12–20) were unmapped and are now proposed.
> 4. Declaration Number is alphanumeric, left-aligned and padded with spaces, unique per line; proposed employee ID + payment date instead of DOB.
> 5. Frequency: monthly with the premium payment or annual by 31 January; filing is electronic; encoding BIG5.
> Three points need your confirmation: the bonus base feeding 2558 (does it include 6220x?), PE 58139 (not in WTC V2.8; 64550?) and the DD field holding the NHI unit code.

## O que precisa ser feito
1. Usuário revisa esta nota e decide o envio do comentário (nada foi postado).
2. Aplicar a proposta numa cópia da spec (destacar em `FFDDEBF7`, versão 1.2 na Version Control), só depois do ok.
3. Pedir ao Mohit as 3 confirmações (base de bônus, PE do insured amount, campo do código NHI).
4. Depois do ajuste, o Mohit retesta na REF-LE-02-826; os negativos e o UBN ausente da aba Testing precisam sumir.
5. Registrar no hub de Taiwan o achado do 58009/6220x (fora do pedido).

## Lacunas
- ⚠️ Se pagamentos de bônus sem prêmio retido (acumulado ainda abaixo de 4×) entram no detalhe: o art. 10 do F2 fala em prêmio "扣取", mas não li regra explícita de exclusão.
- ⚠️ Campo do DD para o código da unidade NHI (9) e para o nome de contato: não encontrados no DD V3.3.
- ⚠️ Fórmulas dos PEs do SNHI (2558, 58132–58137, 58558, 64550): vazias no WTC V2.8.
- O texto do NHI Act e do 辦法 foi lido da cópia Wayback do 全國法規資料庫 (law.moj.gov.tw recusa conexão daqui); conferir na fonte direta quando possível.
- Sem acesso ao ambiente de teste: o status real da configuração `tw-snhi` é o da aba Testing (fev/2026).
