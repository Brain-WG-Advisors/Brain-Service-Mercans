# CONFERENCIA: SR-108, TW SNHI report spec v1.2 (bônus, NHIA tipo 62)

> Construtor B, 2026-10-27. Tudo local: nada foi para Drive, YouTrack, e-mail ou chat. **Rascunho para o usuário revisar.**

## Pedido
Mohit, 15/09/2026: "Spec Review only and fill the gaps in specs." Só isso: revisar a spec contra a fonte oficial e preencher as lacunas. Não é teste nem configuração.

## Arquivos
| Arquivo | md5 | O que é |
|---|---|---|
| `raw/docs/drive-exports/2026-10-27/TW - SNHI report specification.xlsx` | `143efdc6d4da4f8696fd2bd6aa2f7730` | Base (export de hoje). Valores idênticos aos da export de 23/10 (0 diferenças célula a célula; o zip muda só por ser outra exportação) |
| `TW - SNHI report specification_v1.2.xlsx` | `abbcd1d7ec1dfae4290ecb327d7e0538` | v1.2 (Draft) após a rodada 2, com células alteradas/novas em azul-claro `FFDDEBF7` (o md5 da rodada 1 era `ec6d02d6…`, já substituído) |
| `scripts/edits_v12.py` | | Lista fechada das células: rodada 1 (49) + `ROUND2` (21, sendo 13 substituídas e 8 novas) = 57 (valor + fonte de cada uma) |
| `rodada2-diff.log` | | Rodada 1 → rodada 2: 21 diferenças = 21 esperadas |
| `scripts/build_v12.py` | | Cirurgia XML + zip: só `sheet1/2/3.xml` e `styles.xml` reescritos; as outras 25 partes saem com os mesmos bytes |
| `scripts/compare_v12.py` → `comparacao-celula-a-celula.md` | | Comparação célula a célula e parte a parte (resultado: PASS) |
| `scripts/check_layout.py` → `check_layout.log` | | Comprimentos por seção, amostra oficial NHIA, aba Testing |
| `validate_workbook.log` | | Gate `mercans-artifact-toolkit/validate_workbook.py` |

## Fontes (relidas por mim nesta sessão)
Pasta `raw/docs/oficiais/TW/`.
| # | Fonte | O que li |
|---|---|---|
| F1 | NHI Act art. 31 (`2026-10-23-nhi-act-L0060001-moj-wayback.txt`) | §1(1) bônus "全年累計逾當月投保金額四倍部分"; retenção no pagamento, recolhimento até o fim do mês seguinte |
| F2 | Supplementary Premium Regulations (`...-L0060027-moj-wayback.txt`) | art. 2 (data de pagamento = efetiva/transferência/remessa); art. 3(1) bônus = 年終獎金、節金、紅利 fora do insured amount; art. 4 bônus acima de 4× "全數計收"; art. 6 acumulado de 1º/jan até o pagamento, leaver = 4× o insured amount da saída; art. 10 anual até 31/01 (05/02 se 3+ feriados seguidos), ou junto com o recolhimento por meio eletrônico, o que dispensa a anual |
| F3 | Formato TXT tipo 62 (Drive `raw/docs/drive-exports/2026-10-23/SR-108-SNHI-doc-txt-bonus.txt`; posições conferidas também no PDF `2026-10-23-SNHI-nhia-bonus-62-detail-file-format-txt.pdf` via pdftotext) | todas as posições/tipos; ROC yyymm/yyymmdd; "不可為負值"; seção 三 campos 4–6 = contagem/soma das linhas de detalhe; nota 2 (C: esquerda + espaços à direita); nota 3 (ASCII e BIG5); nota 4 (93–101 投保單位代號 C 9; 102–107 投保金額 N 6; 108–117 acumulado N 10) |
| F4 | Formato CSV tipo 62 (PDF, lido com pypdf) | 申報編號: padrão "1"; "2", "3"… para o mesmo beneficiário, mesma data e mesmo tipo; ou numeração própria alfanumérica até 30, sem repetição |
| F5 | Resumo NHIA 115 (PDF) | código 62; 按月申報 网路/媒體 junto com o recolhimento; 年度申報 até 31/01; código 61 (empregador) "不需申報明細"; 2,11% |
| F6 | Introdução NHIA (PDF) | 2,11% desde 110/1/1 (2021-01-01) |
| Amostra | `raw/tickets/api/anexos/SR-108/20250723-1204 - SNHI_sample.txt` (anexo do ticket, ROC 105) | parse por posição: 4 linhas; 116.073 + 54.606 + 69.042 + 47.221 = 286.942; 740 + 468 + 617 + 276 = 2.101; telefone em 57–71 = `27065866#1111` |
| Internas | DD V3.3, WTC V2.8 (exports de 23/10), TW Tax Report Spec (H18/H33), TW SI Termination spec (F9/H9) | campos e PEs citados abaixo |

## Decisões
1. **Onde editar.** Correção de formato nas colunas F (descrição) e G (descrição RA); mapeamento novo ou corrigido na coluna I (BA). Colunas J (Lisa) e K/L (Jani/Mohit) intocadas: são registro de quem perguntou e respondeu.
2. **Mapeamento que depende do motor/BA** não foi inventado: quando há candidato no DD/WTC, vai como "proposed" com `TO BE CONFIRMED BY MOHIT/BA`; o texto antigo do BA foi mantido como prefixo em I21/I26.
3. **UBN (A4/B14):** `company_registration_number` (公司統一編號), o mesmo campo que a própria spec usa em C33 e que a Lisa confirmou em J33. Os três registros levam o mesmo UBN (F3 campo 2 nas três seções). Não marquei TBC porque a spec já tinha a resposta do cliente; ver ⚠️ 4.
4. **Declaration Number (B20):** ~~regra do CSV ("1", "2", "3"…)~~, substituída na rodada 2 pela numeração própria única por linha do TXT (ver Rodada 2, achado 2). Sem DOB (dado pessoal desnecessário) e com espaço à direita (F3 nota 2).
5. **Periodicidade:** `Period` (mensal, com o recolhimento) e `Tax Year` (anual) como permitidas; `Period` como padrão, porque a declaração eletrônica mensal dispensa a anual (F2 art. 10 §3). Valores tirados da aba Options (validação de dados da célula).
6. **Aba Testing:** não mexida (registro do teste do Jani).
7. **Achado 58009/6220x:** só aqui (fora do pedido). Na spec, I21/I26 dizem apenas que o 58009 tem de ser a mesma base que alimenta o 2558.

## Antes → depois, rodada 1 (49 células; a rodada 2 alterou 21, ver seção própria; tabela final em `comparacao-celula-a-celula.md`)
| Aba | Células | Antes → depois (resumo) | Fonte |
|---|---|---|---|
| Version Control | B15–F15 | nova linha: 1.2 · 27/10/2026 · resumo · Draft · Wallisson Gomes | pedido |
| Report Matrix | B5, B6 | vazio / Quarterly → `Period, Tax Year` / `Period` | F2 art. 10; F5 |
| Report Matrix | B8 | ASCII → BIG5 (código ASCII em 1 byte, nomes em full-width) | F3 nota 3 |
| Report Matrix | B11 | vazio → A: 1 linha; B: 1 linha por pagamento; C: 1 linha com os totais de B | F3 |
| Report Matrix | B12 | Manual: hardcopies → `Electronic: Upload online ` | F5; F2 art. 10 §3 |
| Report Matrix | B13, B15, B16, B17 | vazios → N/A (TXT) / população (ativos e desligados) / evento (2558 > 0; 1 arquivo por ano) / TWD | F2 arts. 6 e 10; F3 |
| Report Matrix | B21 | vazio → introdução (base legal, 2,11%, prazos, código 61 fora) | F1, F2, F5, F6 |
| Report Matrix | B23 | itens 1–4 mantidos + 5 (N nunca negativo) e 6 (totais de C = soma de B) | F3 |
| Spec(TXT) | G4, I4, G14, I14, E14 | `social_security_integrate_number` → `company_registration_number`; amostra 8628407 → `08628407` | F3 campo 2; J33; amostra |
| Spec(TXT) | F6, F7, F8, I8, F18 | yyyymm/yyyymmdd → ROC yyymm/yyymmdd; I8 = fórmula ROC (padrão da TW Tax Report Spec H18/H33) | F3 A4–A6, B6 |
| Spec(TXT) | I9, I11, I29 | vazio/sem regra → em branco se unidade única; nomes em full-width com U+3000 até 25 | F3 A7, A9, B13 |
| Spec(TXT) | I16, I17 | vazio → sequencial 000000001…; sempre I (resposta do Mohit L17) | F3 B4, B5 |
| Spec(TXT) | I18 | **vazio** → data efetiva de pagamento em ROC + TBC (variável do motor) | F3 B6; F2 art. 2 |
| Spec(TXT) | F20, I20 | DOB+ID com zeros à esquerda → "1"/"2"/"3", espaço à direita | F3 B8; F4 |
| Spec(TXT) | I21, I26 | mantidos + TBC (mesma base do 2558; art. 3) | F2 arts. 3 e 6 |
| Spec(TXT) | G23, I23 | "Input 62" → bloco das linhas 24–27 | F3 nota 4 |
| Spec(TXT) | B24, F24, I24 | "Social Security Integrate Number" / UBN → Insured Unit Code (投保單位代號), 9; proposto `health_insure_id` + TBC | F3 nota 4 |
| Spec(TXT) | I25 | `SUM(58139)` → TBC: 58139 não existe no WTC V2.8; proposto 64550; leaver = insured amount da saída | F3 nota 4; F2 art. 6 |
| Spec(TXT) | I35 | **vazio** → contagem das linhas B | F3 seção 三 campo 4 |
| Spec(TXT) | I36, I37 | YTD → soma das posições 69–82 / 83–92 das linhas B do arquivo | F3 seção 三 campos 5–6; amostra |
| Spec(TXT) | E36, E37, E38 | amostras mal recortadas → `00000000000000286942` / `0000000000002101` / `27065866#1111` | amostra NHIA |
| Spec(TXT) | I39 | `representative` → pessoa de contato (聯絡人姓名) + TBC (sem campo no DD) | F3 seção 三 campo 8 |

Por aba: Version Control 5 · Report Matrix 11 · Spec(TXT) 33 · Testing 0 · Options 0.

## Conferência
- **Célula a célula, rodada 1** (o log atual é o da rodada 2): todas as células das 5 abas comparadas em valor, preenchimento, fonte, borda, alinhamento e formato. 49 diferenças = 49 esperadas; 0 fora da lista; 0 não aplicadas. Nas 49, só o preenchimento mudou no estilo (fonte/borda/alinhamento/formato iguais). **PASS.**
- **Pacote:** 29 partes, mesma ordem; 25 idênticas byte a byte; as 4 alteradas (`sheet1/2/3.xml`, `styles.xml`) são idênticas à base fora das células editadas; `styles.xml` só ganhou 1 fill e 19 xf clonados no fim. Desenhos, imagem, comentários, threaded comments e validações de dados preservados.
- **XML:** todas as partes `.xml`/`.rels` passam no parser; openpyxl abre a v1.2. Build determinístico (rodado 2 vezes, mesmo md5).
- **Gate `validate_workbook.py` (rodada 1; na rodada 2 dá PASS):** 7 BLOCKER C29, todos o marcador `TO BE CONFIRMED` pedido (Version Control D15; Spec I18, I21, I24, I25, I26, I39). Esperado num Draft com perguntas em aberto; some quando o Mohit responder. Nenhum outro achado (a base dá PASS).
- **Layout** (`check_layout.log`): comprimentos somam 200 nas seções A, B e C; o bloco 93–132 soma 40. Na amostra oficial, os totais da seção 3 = soma das 4 linhas (contagem 4; 286.942; 2.101), o que prova a regra de C35–C37. E36/E37/E38/E14 da v1.2 batem com a amostra lida por posição.
- **Aba Testing (não alterada):** a saída da configuração de fev/2026 falharia no NHIA: falta o UBN (2–9), então todos os campos estão deslocados 8 posições (o "62" aparece em 2–3); data de pagamento `-191112`; prêmios negativos `-28590`/`-57180` (campos N "不可為負值"); o resumo sai com total de bônus zerado; A14 virou número científico na planilha. Precisa ser retestada pelo Mohit depois das respostas.

## ⚠️ Lacunas (não provei)
1. Se pagamento de bônus **sem** prêmio retido (acumulado ainda abaixo de 4×) entra no detalhe. Escrevi "2558 > 0" porque o art. 10 manda declarar o prêmio "扣取"; não achei regra explícita de exclusão.
2. Variável do motor para a data de pagamento do payrun (I18): não existe em nenhuma spec local (só `$report.generation_time`, `$meta.as_of_date`, `$meta.generation_date`).
3. `health_insure_id` como 投保單位代號 (I24) e 64550 como insured amount (I25) são inferências por rótulo/descrição (DD "健保證號, 9 digits"; WTC "SNHI Interim Base = $hr.nhi_grade::orLabel"). Por isso TBC.
4. UBN: o DD rotula `social_security_integrate_number` como "統一編號" (8) e `company_registration_number` como "公司統一編號". Segui J33 (Lisa). Na aba Testing o UBN saiu vazio, o que sugere que o campo antigo não estava preenchido na entidade de teste, mas não prova qual campo o cliente usa.
5. Campo de pessoa de contato (I39) e de matriz (I9): não existem no DD V3.3.
6. NHI Act e Regulations lidos da cópia Wayback do 全國法規資料庫 (law.moj.gov.tw recusa conexão daqui).
7. Fórmulas dos PEs do SNHI (2558, 58132–58137, 58558, 64550) vazias no WTC V2.8: não deu para conferir o cálculo, só o relatório.

## Perguntas ao Mohit/BA (as 3 do comentário)
1. A base de bônus que alimenta o 2558 inclui a série 6220x (Bonus Annual/Referral)? O 58009 hoje é 6221x + 6222x.
2. PE do insured amount do mês (102–107): 58139 não existe no WTC V2.8; é o 64550?
3. Campos do DD/motor para: código da unidade NHI (proposto `health_insure_id`), data de pagamento do payrun e pessoa de contato.

## Para o hub de Taiwan (fora do pedido; não vai no ticket)
- WTC V2.8, 58009 = "sum of 6222% series and 6221% Series" (6222x Discretionary/One-Time + 6221x Profit Sharing): a série 6220x "Bonus (Annual/Referral)" fica fora. Se o 2558 seguir o 58009, o bônus anual (年終獎金) não paga suplementar, contra F2 art. 3(1).
- Amostra anexada é de ROC 105 (2016), taxa 1,91% na época: (522.329 − 4 × 120.900) = 38.729 × 1,91% = 739,7 → 740. Não serve para testar a taxa atual (2,11%).
- Prêmio do empregador (código 61, art. 34) corretamente fora deste relatório (F5 "不需申報明細").
- Leaver (F2 art. 6 §2): bônus pago após o desligamento usa o insured amount da saída; agora citado na spec (B15, I25).

## Rodada 2 (2026-10-27, achados de `REVISAO-independente.md`)
| # | Achado | Correção | Células |
|---|---|---|---|
| 1 | Os marcadores TBC e o placeholder `<payment date>` estavam no mapeamento (gate C29 FAIL) | Na coluna I fica só a proposta, marcada "Proposed" quando é inferência. As perguntas foram para a coluna K (Questions, como K16/K17/K20). O D15 agora aponta "3 open questions in column K" | I18, I21, I24, I25, I26, I39; K18, K21, K24, K25, K39 (novas); D15 |
| 2 | I20 seguia a regra do CSV ("1" para todos), mas o TXT 二.8 diz 「由申報單位自行編號，以英數字為限，不得重覆，不足位數右補空白」 (reli o texto do F3) | `CONCAT(PREPAD(UBN;8;'0'); '62'; Income Payment Date 22-28; Serial 12-20)`, 26 caracteres, alinhado à esquerda e completado com espaços até 30. **Decisão minha:** acrescentei a data de pagamento ao padrão da amostra (UBN+62+número) porque o serial recomeça a cada arquivo mensal e, sem a data, o número se repetiria no ano | I20 |
| 3 | `company_registration_number` é Number "Maximum 8 digits" (DD V3.3 Country Fields r59, relido): um UBN com zero à esquerda sai com 7 caracteres | `PREPAD(...; 8; '0')`; I24 = `PREPAD($legal_entity_hr.health_insure_id; 9; '0')`, o mesmo padrão das specs TW SI v1.1 (Joiner F6, Salary Adj. L9, Termination F9) | I4, I14, I33 (nova na lista), I24 |
| 4 | O filtro "2558 > 0" não estava marcado como inferência e divergia de I5 | Agora vem como "Proposed (inference from art. 10)". Explica que I5 (`MAX(58133+58009+58132;0) > 0`) e 2558 > 0 devem pegar os mesmos pagamentos, mas a fórmula do 2558 não está no WTC. A pergunta entrou em K21 | B16 |
| 5 | I6/I7 sem conversão para ROC | Texto do BA mantido + `CONCAT(PREPAD(SUBTRACT(DATE_FORMAT(...;'yyyy');1911);3;'0'); DATE_FORMAT(...;'MM'))` | I6, I7 |
| 6 | I8 sem PREPAD do ano ROC | Mesmo padrão das specs TW SI v1.1 (Termination F40/F60) | I8 |
| 7 | B23 dizia "ASCII or BIG5" | "ASCII and BIG5" (F3 nota 3: 「ASCII及BIG5」) | B23 |
| 8 | comentario.md dizia "Income Payment Date mapped" | Agora: "proposed (engine variable to confirm)" | comentario.md |

**Conferência da rodada 2**
- Base → v1.2 final: 57 diferenças = 57 esperadas (Version Control 5, Report Matrix 11, Spec(TXT) 41, Testing 0, Options 0). Nenhuma fora da lista, todas em `FFDDEBF7`, com fonte, borda, alinhamento e formato iguais aos da base. 25 de 29 partes idênticas byte a byte; o XML é idêntico fora das células editadas; todas as partes passam no parser. **PASS** (`comparacao-celula-a-celula.md`).
- Rodada 1 → rodada 2: 21 diferenças = 21 esperadas (`rodada2-diff.log`).
- Gate `validate_workbook.py`: **PASS** (0 blocker). Os 7 C29 da rodada 1 sumiram.
- Layout e amostra (`check_layout.log`): inalterados, tudo OK.
- Lacunas ⚠️ 1–7 continuam valendo, agora como perguntas na coluna K (K18, K21, K24, K25, K39). A lacuna 1 (bônus sem prêmio retido) entrou em K21.

## Registro por frente
| Data | Frente | O quê |
|---|---|---|
| 2026-10-27 | Suporte (construtor B) | v1.2 gerada (49 células em azul), comparação célula a célula PASS, 7 TBC para Mohit/BA, CONFERENCIA e comentário EN em rascunho; nada enviado nem copiado para o Drive |
| 2026-10-27 | Suporte (construtor B), rodada 2 | Achados 1–8 da revisão independente: 21 células (13 substituídas, 8 novas: I33, K18, K21, K24, K25, K39 e mais as reescritas), TBC saíram do mapeamento e foram para a coluna K, I20 segue a regra do TXT, PREPAD no UBN e no código NHI, ROC em I6/I7/I8; comparação PASS, gate PASS; nada enviado |
