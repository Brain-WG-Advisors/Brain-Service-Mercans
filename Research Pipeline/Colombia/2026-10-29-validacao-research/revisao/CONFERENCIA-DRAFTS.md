# Conferência independente dos DRAFTs COVAL (IEEE 1012 V&V), 2026-10-29

Verificador independente (não fez as edições). Escopo: os 11 DRAFTs em `revisao/{CCG,WTC,DD,PILA,NE,FORMS,PAYSLIP,SIR}`, contra a linha de base congelada, os CHANGELOGs, `mudancas-*.md`, o `COMPARATIVO-FINAL-CO-v1.0.xlsx` (veredito) e as fontes em `raw/docs/oficiais/CO/`. Nenhum DRAFT, base ou achado foi alterado. Rascunhos e scripts em `revisao/_check/` (diffs em JSON por artefato, `CCG_accept.txt`, `CCG_hunks.txt`, `ne_draft.xml`).

Método: md5 de cada base; diff próprio base × DRAFT (xlsx: valor de toda célula de todas as abas com openpyxl, só leitura, + entradas do zip byte a byte; docx: texto de "rejeitar tudo" e "aceitar tudo" a partir do `document.xml`); cada célula/parágrafo alterado cruzado com o CHANGELOG; releitura da fonte primária local para todos os S1/S2 e amostra de cerca de 40% dos demais; contas refeitas; `validate_workbook.py`; XSD 1.0.6 na amostra da NE; comprimento dos segmentos da amostra PILA.

Critério do veredito: **PASS** = integridade íntegra e nenhum problema S1–S3 no conteúdo; **FAIL** = algum S1–S3. Em todos os 11, a integridade mecânica (checagens 1, 2 e 5) passou. As falhas são de conteúdo, de omissão ou de consistência entre artefatos.

---

## CCG: CO-CCG-001 v1.5 DRAFT (docx): FAIL

| Checagem | Resultado | Evidência |
|---|---|---|
| 1. md5 da base | PASS | `8b087e4d008cb2d50506f32566ec48b0` (original e `_base-…`) |
| 2. Diff próprio × CHANGELOG | PASS | Só `word/document.xml` mudou. "Rejeitar tudo" = texto da v1.4 nos 7.970 parágrafos (idêntico). "Aceitar tudo": 88 blocos de diferença, todos na tabela "Antes e depois" (A-01, A-02, A-03, A-04, A-05, A-06, A-09, A-13, A-15, A-16, F-01, F-03, F-04, F-05, F-06 + linha de VC). Nenhuma edição fora do log. |
| 3. Mudança = proposta = fonte | **FAIL** | A-16: a frase sobre estrangeiros está no art. 15 **num. 2** ("En forma voluntaria"), não no num. 1. Lido na Ley 797/2003 art. 3 (SecretariaSenado) e na Ley 100 (FuncionPublica). A-04 ignora a Ley 962/2005 art. 46 (mod. Ley 1819/2016 art. 304), citada no próprio DUR e na Res. 13/2021. A-01: OK em DUR 1.2.4.1.8 e 1.2.4.1.13 (lidos), mas com hipótese não escrita. A-03: OK (Decreto 1772 art. 13, conhecido; a cópia local do Decreto 1072 perde a coluna de máximos). F-06 (Decreto 780 art. 2.2.3.6.1) e A-13 (ET 114-1) conferem. |
| 4. Contas | PASS (com ressalva) | A-01: 7.327.500 × 25% = 1.831.875; (5.495.625 − 4.975.530) × 19% = **98.818,05**; líquido 26.677.500 − 360.000 − 98.818,05 = **26.218.681,95**. Leitura 3: 58.500.000 ÷ 12 = 4.875.000 = 93,08 UVT → 0%. Ramo 204 UVT: salário 85,92 UVT (ou média de 93,08 UVT) < 204 → DUR 1.2.4.1.8, escolha correta **se** o teste for mensal. A-15: 19 dias; 1.520.000; 157.760,17; piso 1.108.906,50; 60.800; ARL 7.934,40 → 8.000; total 2.288.697,80: tudo confere. 204 × 52.374 = 10.684.296; 1 − 210/240 = 12,5%. |
| 5. Integridade | PASS | `validate.py` e python-docx abrem; demais entradas do zip byte a byte; autor e data das revisões conforme a regra 7; linha de VC presente. |
| 6. Consistência entre artefatos | **FAIL** | A citação corrigida (Decree 1072 art. 2.2.1.2.1.4) continua no DD (G61) e na PILA-003 (A36, M69, C22). O CCG diz que a Ley 2381 não está em vigor ("Not yet in force… 2027"), e a PILA-003 M120 agora aplica a tabela "N" da Ley 2381. Restam frases contraditórias no próprio CCG (P1042/P5810 "no averaging"). |

## WTC: CO-WTC-001 v1.7 DRAFT: FAIL

| Checagem | Resultado | Evidência |
|---|---|---|
| 1. md5 | PASS | `05b839bbf8af912c905fc227ed0653e6` |
| 2. Diff × CHANGELOG | PASS | 16 células (X312, N322, W123, V154, V155, V313, V323, V334, V335, B229, D229 + VC B19:F19) = log. Só sheet1, sheet2 e styles mudaram. |
| 3. Mudança = fonte | **FAIL** | D1, D2, D7 (só W) e D8 parcial conferem com o cabeçalho e as linhas irmãs. **D16:** "Discretionary bonus" foi inventado. O Global WTC (`shared/Global_WTC_V1_0.xlsx`, posição 229 = código 62591) tem "Birth and Marriage Allowance", e F229 descreve auxílio de nascimento/casamento. É a única divergência posicional com o Global. D10, D4 e DD-14 ficaram NÃO APLICADAS por exigirem decisão (justificado). |
| 4. Contas | n/a | — |
| 5. Integridade | PASS | Fill FFDDEBF7 em todas as 16; openpyxl só leitura; validate PASS; drawings/media idênticos. |
| 6. Consistência | **FAIL** | Janela noturna 19:00 (F108-F111) = NE e CCG (OK). Juros de moradia: o WTC não tem a verba que o DD (W115) diz estar "no WTC" (DD-14). |

## DD: CO-DD-001 v1.4 DRAFT: FAIL

| Checagem | Resultado | Evidência |
|---|---|---|
| 1. md5 | PASS | `f5a14676f2db93a7e2ed555b36a98bb1` |
| 2. Diff × CHANGELOG | PASS | 863 células: 30 pré-existentes (= as 30 listadas) + linhas novas acrescentadas em linhas vazias (CF l.108-174; Mappers 37, 73, 238-294) + VC l.17. Nenhuma linha inserida no meio. |
| 3. Mudança = fonte | PASS com ressalvas | Relidos no AT2 v30: p.81 (PE e PT), p.82 (comprimentos), pp.9-10 e 12 (aportante), p.13 (campo 17), p.88 (TAE em branco; IGE L e LMA P), p.92 (campo 41), p.98 (campo 79), p.117 (tipo 51), pp.132-133 (tipo 75), códigos 25-2/25-3/25-14. Tudo confere. Ressalva S4: as linhas 36-37 citam p.81/p.12, mas a regra do aportante está em pp.9-10. |
| 4. Contas | n/a | — |
| 5. Integridade | PASS (S4) | validate PASS; comments, drawings e media idênticos. 70 células de cabeçalho copiado (CF l.110; cabeçalhos dos mappers novos) sem FFDDEBF7, contra a regra 6 (declarado no log). |
| 6. Consistência | **FAIL** | DD-14: só existem as datas do certificado; a verba e o valor mensal não existem em lugar nenhum. Tipo 75 sem regra de NE (o mapper "Worker Type" alimenta a NIE041, onde o 75 não existe). Os campos novos "PILA Salary Type" e "PILA Special Pension Rate Indicator" não são usados pela PILA-003 (L107 e L152 continuam nas flags booleanas). W99 diz que a 006 "still names Employee.Cesantias_Fund_Code", mas a 006 v1.1 já mudou para Company.* (L10). |

## PILA: CO-PILA-003 v1.1 e CO-PILA-007 v1.1 DRAFT: FAIL

| Checagem | Resultado | Evidência |
|---|---|---|
| 1. md5 | PASS | 003 `12225906…`; 007 `4bfea698…` |
| 2. Diff × CHANGELOG | PASS | 003: 55 células = log. 007: 6 células = log. |
| 3. Mudança = fonte | **FAIL** | **P-02 (S2):** M120 afirma que a regra "a partir de julho/2025 só nos arquivos de saída das ACCAI" é do campo 51 e "not to this field". O AT2 v30 **p.158**, ainda dentro de 2.1.2.3.19 (campo 52; o 2.1.2.3.20 começa na p.159), repete essa regra para o campo 52. A frase nova é falsa, e o erro vem da própria proposta. D1 (p.98, campo 81), D2 (p.117), D7 (pp.31-32), P-14 (p.91), D3/75 (pp.132-133) e a tabela N (p.158) conferem. P-08 NÃO APLICADA com motivo válido (falta o anexo do Decreto 768/2022). |
| 4. Contas | n/a | — |
| 5. Integridade | PASS | Segmentos da amostra: 003 17/17 e 007 18/18 com o comprimento exato (`pos a-b` = b − a + 1). Campo 9 (228-237) em branco sem deslocar posições. validate PASS; fills OK. |
| 6. Consistência | **FAIL** | Os tipos 75 e 51 são iguais na 003 e no DD (OK). Problemas: L107 e L152 não usam os campos novos do DD; A36, M69 e C22 citam o Decree 1072 art. 2.2.1.2.1.4, que o CCG retirou; J47 ainda diz "ZERO-filled", mas o campo agora é branco (S4). |

## NE: CO-DIAN-001 v1.1 DRAFT: FAIL

| Checagem | Resultado | Evidência |
|---|---|---|
| 1. md5 | PASS | `b9f0d815d1dd7dc617fa11ca5145ee55` |
| 2. Diff × CHANGELOG | PASS | 63 células = log (conjuntos iguais). |
| 3. Mudança = fonte | **FAIL** | **NE-05 foi omitida:** no COMPARATIVO, a linha 144 tem veredito CONFIRMADO (S3, 95%). O log a trata como "PROVÁVEL" porque a linha de `mudancas-PENDENTES.md` saiu com os pipes quebrados. As 14 de `mudancas-NE.md` conferem: NE-17 19:00 (Ley 2466 art. 10); NE-16 (Ley 2466 art. 14); NE-02 = 5a + 2m + 20d = 1.880; SIM-03 617.232 = (8.190.000 − 7.856.100) × 0,28 + 523.740. |
| 4. Contas | PASS | 480.000 + 480.000 + 120.000 + 617.232 = 1.697.232; 12.000.000 − 1.697.232 = 10.302.768 (XML, Example Analysis, Spec K191/K213/K214). |
| 5. Integridade | PASS | Amostra reconstruída (`Sample File` A55:A161 → `_check/ne_draft.xml`) **VÁLIDA** contra `NominaIndividualElectronicaXSDV1.0.6.xsd`; validate PASS; fills OK. |
| 6. Consistência | PASS com ressalva | 19:00 = WTC e CCG. 617.232 = Payslip/CCG P139, mas os Forms 004/005/002 continuam com 617.000 e 7.404.000 (ver FORMS). |

## FORMS: CESANTIAS-006, DIAN-002, DIAN-004 e DIAN-005 v1.1 DRAFT: FAIL

| Checagem | Resultado | Evidência |
|---|---|---|
| 1. md5 | PASS | 006 `93b38907…`; 002 `ff91e90d…`; 004 `a9ebaf29…`; 005 `f48c5a76…` |
| 2. Diff × CHANGELOG | PASS | 004: 21; 005: 58; 002: 15; 006: 10 células = log (incluindo VC l.14). |
| 3. Mudança = fonte | **FAIL** | **SIM-03 (CONFIRMADO, cita 002, 004 e 005) não foi aplicada nem listada como NÃO APLICADA.** 004 C27 ainda diz "twelve ordinary months at COP 617,000 = 7,404,000" (deveria ser 7.406.784). 002 C15 ainda cita o "ET art. 868" para o arredondamento (deveria ser DUR 1.6.1.11.11), e D15 diz que a NE carrega "exactly 617,000.00". F-07: nomes `mas`/`Cab`/`rentra`/`entinfo` e "Versión 4" conferidos no Anexo 45 (p.6). Os demais atributos não foram reconferidos, porque só existem PNG das pp.1-6 e 14. F-08, F-05 e F-09: fontes não relidas pelo editor (declarado). |
| 4. Contas | PASS | 144 + 12 + 1,44 + 12 = **169.440.000**; 20% = 33.888.000; 7.404.000 / 169.440.000 = 4,37%; 33.888.000 / 7.404.000 = 4,58; (6 × 12 M + 6 M)/6 = 13.000.000 < 350 UVT = 18.330.900. |
| 5. Integridade | PASS | validate PASS nas 4 (o `--artifact RSPEC` FAIL é pré-existente, segundo o log); fills OK. |
| 6. Consistência | **FAIL** | NE v1.1 = 617.232/mês × Forms = 617.000 e 7.404.000. A 006 L10 aponta para Company.*, mas o texto do DD W99 diz o contrário. |

## PAYSLIP: Generator v1.2 DRAFT: FAIL

| Checagem | Resultado | Evidência |
|---|---|---|
| 1. md5 | PASS | `32ded04fef2977946aa71f55c5af7bb2` |
| 2. Diff × CHANGELOG | PASS | 115 células; todas no log (faixas "Spec B73:E81", "A14/C14", "D3 (was H3)"); I8, H50 e H67-69 mudaram só no valor em cache. |
| 3. Mudança = fonte | **FAIL** | **Juros de cesantías H55 = 16.000** é a fórmula de liquidação de um único período de 30 dias (oracle). Para um empregado em curso, o CCG (A-15: "1% × gross") e o WTC L322 ("monthly accrual 1.0000%") dão 1% × 19.200.000 = **192.000**. O 19.200 do achado também está errado. **SIM-08 marcada APLICADA, mas a fórmula arredonda cada parcela** (ROUNDUP por linha), que é justamente o que o SIM-08 diz estar errado (o certo é arredondar o total por cotizante e fundo). O resultado só coincide porque as parcelas são múltiplos de 100. PS-01..PS-12 e SIM-05 conferem. |
| 4. Contas | PASS | Base 17.472.000 − 3.447.955 = 14.024.045 → (14.024.045 − 7.856.100) × 0,28 + 523.740 = **2.250.764,60**; líquido **15.221.235,40**; aportes do empregador 5.764.300; 1.600.000 × 12% × 30/360 = 16.000 (a conta está certa, o método diverge). O log escreve "42,9765 UVT"; o certo é 42,9748 (S4). |
| 5. Integridade | PASS (S4) | Logo, drawings e media byte a byte; `fullCalcOnLoad=1`; caches conferem. validate: 2 blockers C29 pré-existentes. Sem linha de Version Control (o workbook não tem a aba), contra a regra 8. Marcadores novos `<Provider NIT>`/`<Software ID>`/`<CUNE>` (o lint não pega). |
| 6. Consistência | **FAIL** | Juros de cesantías divergem do CCG e do WTC (acima). |

## SIR: CO-SIR-001 v1.2 DRAFT (redline .md): FAIL

| Checagem | Resultado | Evidência |
|---|---|---|
| 1. md5 | PASS | Captura `27e3807ed33a9d8f72c200a70f18474a` |
| 2. Diff × CHANGELOG | PASS | Os 8 "Antes" ocorrem uma vez cada na captura; 4 IDs aplicados e 4 SEM FONTE não aplicados. |
| 3. Mudança = fonte | PASS com ressalva | D8 e S-01/S-06 conferem com a proposta. S-02a cita "ET art. 771-2 **par. 3**", mas a proposta confirmada diz "inc. 3" (S4). A captura é um resumo, não o texto literal do Doc (risco ao colar, declarado). |
| 4. Contas | n/a | — |
| 5. Integridade | n/a | Sem docx; linha de VC no redline. |
| 6. Consistência | **FAIL** | O redline cita CCG v1.4, DD v1.3 e "7 specs" (v1.0). Os DRAFTs desta mesma rodada são CCG v1.5, DD v1.4, specs v1.1 e WTC v1.7. Se forem emitidos juntos, o SIR já sai desatualizado. |

---

## Todos os problemas encontrados

| Artefato | Local | Problema | Correção sugerida | Grav. |
|---|---|---|---|---|
| CCG | T20R2, P197, T72R3, P597, T85R3, P626, T104R8, P770, T213R2, T214R4, P1241 (A-16) | Cita "Law 100 art. 15 **num. 1**". O texto dos estrangeiros está no **num. 2** ("En forma voluntaria"), na Ley 100 original e na redação da Ley 797 art. 3. "requires pension affiliation … only where not covered" é leitura nossa de uma frase listada entre os afiliados voluntários. | Trocar para "art. 15 num. 2, 2º inciso (Ley 797 art. 3)". Marcar a regra de dispensa como interpretação e buscar doutrina (MinTrabajo/Colpensiones/Superfinanciera). Rever "May be waived"/"waiver". | S2 |
| PILA-003 | PILA Spec!M120 (P-02) | Afirma que a regra ACCAI (N, desde jul/2025) "belongs to campo 51, not to this field". O AT2 v30 p.158 (campo 52) traz a mesma regra. | Escrever que a regra vale para os campos 51 e 52 (AT2 pp.157-158). Corrigir também a proposta P-02 no COMPARATIVO. | S2 |
| DD × WTC | DD Country Fields l.115-116 e W115; WTC (DD-14) | DD-14 marcado APLICADA, mas só entraram as datas do certificado. O W115 manda o valor mensal para uma "WTC wage type" que não existe (WTC: NÃO APLICADA). A dedução de juros de moradia continua sem insumo. | Decidir o código, a categoria e o teto (100 UVT/mês já estão na aba Tax Credit do WTC) e criar a verba, ou criar no DD o campo do valor certificado. Até lá, status "PARCIAL". | S2 |
| NE | File Structure!B23, B24, B39, B43, B51, B69 (NE-05) | Mudança CONFIRMADA (COMPARATIVO linha 144, 95%) tratada como PROVÁVEL e não aplicada (linha com pipes quebrados em `mudancas-PENDENTES.md`). | Aplicar: nomes do XSD (Novedad, Periodo, Empleador, Trabajador, Pago, Cesantias…). Conferir também DD-08/A-03/A-12/F-01 (mesma quebra), que foram tratados certo. | S3 |
| FORMS | 004 Example Analysis!A27/C27, K52/K63; 005 C27/K37/A27/Sample A77; 002 Example Analysis!C15, D15 (SIM-03) | SIM-03 CONFIRMADO não foi aplicado nem listado como NÃO APLICADO: anual 7.404.000 (= 12 × 617.000) deveria ser 7.406.784; 002 cita "ET art. 868"; D15 afirma que a NE carrega 617.000,00 (a NE v1.1 carrega 617.232,00). | Aplicar a parte 002/004/005 (ou registrar como NÃO APLICADA com motivo, se depender de F-03). Trocar a citação por DUR 1.6.1.11.11. | S3 |
| CCG | T25R4 (A-04) | "Minimum 5 years … (art. 632)" ignora a Ley 962/2005 art. 46, mod. Ley 1819/2016 art. 304 (conservação = término de firmeza), citada no DUR 1625 e na Res. 13/2021 locais. A guarda pode passar de 5 anos (perdas). | Guarda = término de firmeza da declaração (ET 632 + Ley 962 art. 46 mod. Ley 1819 art. 304; firmeza: ET 714), ou indicar "o maior entre 5 anos e a firmeza", com a fonte. | S3 |
| CCG | P701, P1003, T86R5, Read 3 (A-01) | A periodicidade do teste de 204 UVT (mensal?) e a janela dos 12 meses (exclui o acerto de 31/8: férias 3.187.500 e prima 750.000) ficaram só no CHANGELOG. Se o acerto entrar na média, ela passa de 95 UVT e o 0% deixa de valer. | Escrever no CCG: "204 UVT de renda mensal" (rotular como leitura/doutrina) e "pagos anteriores à data do retiro; o acerto final não entra", com a decisão do usuário. | S3 |
| CCG | P5810 (P1042) | "There is no averaging … no separate schedule" contradiz a nova regra de média para a indenização. | Acrescentar a exceção da indenização (DUR 1.2.4.1.8). | S3 |
| CCG × PILA-003 | CCG Legal basis ("Law 2381 … Not yet in force … 2027") × 003 M120/G120 | A 003 agora aplica a tabela N da Ley 2381 (AT2 v30), e o CCG diz que a lei não está em vigor. | Alinhar a posição sobre a Ley 2381 (vigência × AT2) nos dois artefatos. | S3 |
| WTC | B229 (D16) | Nome curto inventado ("Discretionary bonus"). O Global WTC (62591, posição 229) = "Birth and Marriage Allowance", e F229 fala de nascimento/casamento. | B229 = "Birth and Marriage Allowance" (texto do baseline global). | S3 |
| PAYSLIP | Colombia (EN/ES)!H55 | Provisão de juros = 16.000 (liquidação de 30 dias). O CCG (1% × base mensal) e o WTC L322 (1%/mês) dão 192.000; H58, H68 e H69 dependem dela. | Usar `=ROUND(H54*12*0.01,0)`, que equivale a 1% × (H26:H30), ou documentar a convenção e alinhar o CCG e o WTC. Corrigir o achado SIM-01/PAY-14. | S3 |
| DD × NE | Mappers G64/l.73 (tipo 75) | Tipo 75 entra no mapper "Worker Type", que também alimenta a NIE041 (tabela 5.5.3), onde o 75 não existe; nenhuma regra diz o que a NE emite. | Regra de-para para a NE (ex.: 01) ou campo separado só para PILA. | S3 |
| DD × PILA-003 | 003 PILA Spec!L107 (campo 41), L152 (campo 79) | Mapeamento continua nas flags booleanas; os campos novos do DD ("PILA Salary Type", "PILA Special Pension Rate Indicator") não são usados. | Remapear L107/L152 (e G107) para os campos novos. | S3 |
| PILA-003, DD | 003 Report Matrix!A36, PILA Spec!M69, Population Rules!C22; DD Country Fields!G61 | Ainda citam o "Decree 1072 of 2015 art. 2.2.1.2.1.4" e "elected out", que o CCG retirou. C22 e I61 foram editados nesta rodada sem acertar isso. | Mesma redação do CCG (corrigida conforme a linha S2 acima). | S3 |
| SIR | Redline D8a/D8b | Referências a CCG v1.4, DD v1.3 e specs v1.0, mas a rodada gera CCG v1.5, DD v1.4, specs v1.1 e WTC v1.7. | Citar as versões que serão emitidas junto (ou "v1.4 + COVAL DRAFT") e acertar ao promover. | S3 |
| PAYSLIP | Formulas H34, H35, H44-H49 (SIM-08) | "APLICADA", mas arredonda cada parcela ao múltiplo de 100, o oposto da regra do SIM-08 (total por cotizante e fundo). O CCG deixou o mesmo item como NÃO APLICADA: status incoerente. | Status "NÃO APLICADA (regra de rateio sem fonte)" ou arredondar o total por fundo e documentar o rateio. | S4 |
| PAYSLIP | Workbook | Sem linha de Version Control (regra 8); marcadores `<Provider NIT>`, `<Software ID>`, `<CUNE>`; log com "42,9765 UVT" (certo: 42,9748). | Registrar a versão em "How to set up Payslip" ou no CHANGELOG oficial; valores ilustrativos rotulados; corrigir o log. | S4 |
| DD | Country Fields!W99 | Diz que a 006 "still names Employee.Cesantias_Fund_Code", mas a 006 v1.1 L10 já usa Company.*. | Atualizar W99 para refletir a 006 v1.1. | S4 |
| DD | Mappers F36/l.37 | Fonte citada p.81 / "p.12 field 9", mas a regra do aportante (PE e PT até 8) está no AT2 pp.9-10, campos 2-3 do arquivo tipo 1. | Corrigir a página e o campo. | S4 |
| DD | CF l.110; cabeçalhos dos mappers 238-289 | 70 células novas sem FFDDEBF7 (regra 6). | Aplicar o fill ou registrar a exceção. | S4 |
| CCG | T86R5 | "average of the taxable payments … divided by 12": média dividida por 12 em dobro. | "the sum … divided by 12". | S4 |
| CCG | T150R4 (P5224) | "Fully taxable withheld outside…" (falta pontuação). | "Fully taxable; withheld outside…". | S4 |
| CCG | T48R1 (A-15) | "12 to 30 August = 19 days (31 August counted as day 30 …)" é incoerente: na convenção de 30 dias o dia 31 é ignorado. | "12 to 30 August = 19 days (30-day month: day 31 is not counted)". | S4 |
| CCG | T72R3 e linhas de A-16 | Mantém "May be waived" / "waiver … claimed with evidence" / "Proof of affiliation", embora a lei não preveja escolha. | Reescrever junto com a correção S2 de A-16. | S4 |
| SIR | S-02a | "ET art. 771-2 par. 3"; a proposta confirmada diz "inc. 3". | Conferir no ET e usar o termo certo. | S4 |
| PILA-003 | PILA Spec!J47 | Formato ainda "ZERO-filled", mas a regra e o exemplo (K47) agora são branco. | Ajustar J47. | S4 |
| DIAN-002 | Formulario 350 Spec!K20 | Coluna de valor de exemplo recebeu texto ("Disabled - leave blank"). | Deixar K20 vazio e manter a explicação em M20. | S4 |

## Bloco de prova

- **Pedido → resposta:** checagens 1-6 para os 11 DRAFTs (tabelas por artefato) e tabela única de problemas.
- **Fontes lidas nesta conferência:** AT2 v30 pp.9-13, 31-32, 81-82, 88, 91-92, 98, 117, 132-133, 157-159; DUR 1625 arts. 1.2.4.1.6 par. 3, 1.2.4.1.8, 1.2.4.1.13 e menções à Ley 962 art. 46; Ley 797/2003 arts. 3 e 7; Ley 100 art. 15; Decreto 780 arts. 2.2.3.6.1 e 3.2.1.5; Decreto 1072 art. 2.2.4.3.5; ET 114-1; Res. 13/2021 (conservação); Anexo 45 p.6 (PNG); Global_WTC_V1_0.xlsx; XSD NE 1.0.6.
- **Teste mecânico:** md5 das 11 bases; diff célula a célula e por entrada do zip; aceitar/rejeitar no docx; XSD (VÁLIDO); comprimento dos segmentos PILA (35/35); `validate_workbook.py` (9 PASS; Payslip FAIL com 2 blockers pré-existentes); contas em aritmética exata.
- **Confiança:** 90%. Não reconferidos: atributos 2-36 do Anexo 45 (pp.7-13 sem imagem); ET 588, 632 e 401-3, Oficio 15662/2026 e Res. 22/2024 (sem cópia local legível). A leitura "num. 2" de A-16 é literal do texto local.
