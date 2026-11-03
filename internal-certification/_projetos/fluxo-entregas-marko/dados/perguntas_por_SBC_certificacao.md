# Perguntas por SBC derivadas das validações da Internal Certification

Gerado em 2026-11-02. Somente leitura das validações; nada foi enviado. Perguntas em inglês (para colar no Chat/e-mail depois do ok do usuário), explicações em pt-BR. Sem nome, ID ou salário de empregado (usado "1 employee" etc.).

Como ler:
- "NT" = controle da aba Not Tested da planilha de validação (maior versão). "F" = achado da aba Findings Register que depende de informação da SBC.
- Fonte = `arquivo:aba!célula`. Os arquivos ficam em `<País>/<Cliente> - <AAAA-MM>/02 Validation/` (caminho completo na seção de prova no fim).
- Prioridade (alta/média/baixa) vem da severidade do achado ou do efeito no veredito; vai no início da coluna "Por quê".
- Cada pessoa tem sua seção; dentro dela, um bloco por pacote com: tabela de perguntas, depois "Rascunho existente", "Já recebido" e "Descartado".

Resumo: 7 pessoas, 11 pacotes, 105 perguntas (NO 8, DK-SHERWIN 3, DK-KGS 4, NL-QUEST 7, NL-SHERWIN 6, NL-EXCERPTA 5, SE 7, KZ 7, UA-08 24, UA-09 11, UK 23). Nenhuma foi enviada.

---

## 1. Umesh Gaikwad (Primary SBC Noruega e Holanda)

### 1.1 Noruega, Henkel Norway AS, 2026-09 (Painel: NO 4 Not tested; validação Fechado)

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | NT-01 (valor do benefício do carro) | For each of the 6 company-car benefit lines, please send fuel type (petrol / diesel / EV / plug-in hybrid), first registration date and months of use in September 2026. | Média. Sem esses dados não dá para recalcular o benefício pela tabela (sjablong) 2026; hoje só temos o preço de lista. | NO_HenkelNorway_2026-09_Validation.xlsx:Not Tested!A4:D4 |
| 2 | NT-02 (OTP mínimo 2% até 12G) | Please send the OTP pension scheme terms (contribution % and whether the premium is charged monthly or annually). | Média. 2 empregados não têm prêmio em setembro mas têm prêmio acumulado no contracheque; sem as regras não dá para confirmar o mínimo obrigatório. | NO_HenkelNorway_2026-09_Validation.xlsx:Not Tested!A5:D5 |
| 3 | NT-03 (pagamento do forskuddstrekk) | Was the withholding tax (forskuddstrekk, KID 0091747289005260919) paid on or before the first working day after the 18-Sep-2026 salary payment? Please send the payment proof. | Média. Desde 2026 o prazo é o primeiro dia útil após o pagamento do salário; não há arquivo de pagamento de imposto no pacote. | NO_HenkelNorway_2026-09_Validation.xlsx:Not Tested!A6:D6 |
| 4 | NT-03 (pagamento da AGA) | Was the employer's national insurance contribution (arbeidsgiveravgift, term 5, 93,040 NOK) paid by its due date? Please send the payment proof. | Média. Mesma lacuna do item 3, para a AGA. | NO_HenkelNorway_2026-09_Validation.xlsx:Not Tested!A6:D6 |
| 5 | NT-04 (diária tributável, elemento 62137) | Please send the September 2026 travel-expense data (trips and rates applied) behind pay element 62137. | Baixa. O excesso tributável vem do sistema de despesas; sem as viagens não há como recalcular. | NO_HenkelNorway_2026-09_Validation.xlsx:Not Tested!A7:D7 |
| 6 | F-04 / G-01 (GL "CORRECTED") | Is the file "Mercans_GLImport_..._CORRECTED.csv" (sum 832,018.75) the final GL posted to the client ledger, replacing the GL Detailed report that prints 808,367.52? Yes / No (if No, which file is final). | Baixa. O rodapé do GL Detailed não bate com as linhas; precisamos saber qual versão vale. | NO_HenkelNorway_2026-09_Validation.xlsx:Findings Register!A7:I7; Coverage!A39:F39 |
| 7 | F-05 / G-04 (OTP no GL) | Is the OTP premium posting (credit 416020, debit 416035, both expense accounts) the mapping agreed with the client, with the pension liability recorded elsewhere? Yes / No. | Baixa (Observation). Hoje o prêmio zera no resultado e não aparece passivo com a seguradora neste arquivo. | NO_HenkelNorway_2026-09_Validation.xlsx:Findings Register!A8:I8; Coverage!A42:F42 |
| 8 | F-06 (cadastro) | Is nationality "Canada" correct for all 6 employees, who hold Norwegian ID numbers and Norwegian addresses? Yes / No (if No, which nationality). | Baixa (Observation). Qualidade de cadastro; não afeta a A-melding. | NO_HenkelNorway_2026-09_Validation.xlsx:Findings Register!A9:I9; Coverage!A44:F44 |

Rascunho existente (`Norway/.../02 Validation/followups.md`): cobre os itens 1, 2 e 6 (GL "CORRECTED", dados do carro, termos OTP). Falta cobrir 3, 4, 5, 7 e 8. O item 4 do rascunho ("nome do sindicato do elemento 21126") não depende de nenhum NT nem achado: o F-01 é sobre o fradrag, que não exige o nome do sindicato; pode sair.
Já recebido: pacote completo em 09-Oct (zip de 10 arquivos, `received.txt`: "nothing missing at first look"); recibo da A-melding (tilbakemelding) e resumo a-ordningen já estão no pacote (A-02 a A-04 Pass).
Descartado: F-01 (contribuição sindical fora da base, A-01 do painel), F-02 (renda tributável no contracheque, A-06) e F-03 (provisão de férias) são decisão nossa/configuração do Dev.

### 1.2 Holanda, Sherwin Williams (Valspar B.V.), 2026-09 (Painel: NL-SHERWIN 5 Not tested; falta recibo)

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | NT-01 / F-01 (aceite da declaração) | Please send the Digipoort status response (or Belastingdienst receipt) for return 002879487L01P20260901. The response in the pack belongs to another payroll tax number (868240503L01). | Alta (F-01 High). Sem isso o aceite de setembro não está provado; além disso o pacote trouxe dado de envio de outro empregador. | NL_SherwinWilliams_2026-09_Validation_v1.1.xlsx:Not Tested!A4:D4; Findings Register!A4:I4 |
| 2 | NT-02 (taxa Whk) | Please send the 2026 Whk beschikking from the Belastingdienst (the return uses 1.83%). | Média. Só dá para confirmar a taxa exata do prêmio diferenciado com o ato oficial; hoje só passou no teste de plausibilidade. | NL_SherwinWilliams_2026-09_Validation_v1.1.xlsx:Not Tested!A5:D5 |
| 3 | NT-03 (retro por empregado) | Please send the original January to August 2026 loonaangifte messages (or the pay-element retro export) so the 8 correction blocks can be tied per employee. | Média. Sem as mensagens originais não dá para validar a alocação das correções retroativas. | NL_SherwinWilliams_2026-09_Validation_v1.1.xlsx:Not Tested!A6:D6 |
| 4 | NT-05 (acumulados do contracheque) | Please send the August 2026 payslips (or the year-to-date G2N through August). | Média. Sem agosto não dá para conferir se os acumulados de setembro rolam corretamente. | NL_SherwinWilliams_2026-09_Validation_v1.1.xlsx:Not Tested!A7:D7 |
| 5 | NT-07 / F-05 (AOK) | For the 2 AOW-age employees withheld on the column with alleenstaandeouderenkorting, do they receive AOW as a single person? Yes / No (per employee). | Baixa (Observation). A coluna com AOK só vale se tiver direito; se não, são EUR 19,83 a menos retidos em setembro. | NL_SherwinWilliams_2026-09_Validation_v1.1.xlsx:Not Tested!A8:D8; Findings Register!A8:I8 |
| 6 | F-06 (motivo do fim do vínculo) | For the 2 leavers reported with end-of-employment reason code 99 ("other reason"), what is the actual ground (e.g. 32 retirement, resignation, end of fixed term, dismissal)? | Média. Código 99 é residual; é rubrica declarada à UWV e pode exigir código específico. | NL_SherwinWilliams_2026-09_Validation_v1.1.xlsx:Findings Register!A9:I9 |

Rascunho existente (`Netherlands/Sherwin Williams - 2026-09/02 Validation/followups.md`, ação C-16): cobre 1 a 5 (o item 5 do rascunho cita IDs de empregados; trocar por "2 employees" ao enviar). Falta o item 6 (código 99).
Já recebido: pacote do zip de 08-Oct (`received.txt`); nada dos itens acima foi entregue depois (Painel: "Falta recibo", Ações C-06 "A verificar").
Descartado: F-02 (retenção de empregado em idade AOW), F-03 (horas declaradas 176 x 173,33), F-04, F-07 a F-11 são correção do Dev/configuração; F-08 (data "In dienst" no contracheque) é apresentação.

---

## 2. Rakshitha Nagesh (Dinamarca; quem enviou os pacotes) / Deepak Prakash Pardeshi (Primary SBC DK no board BAU Master, leitura de 29/10)

Confirmar com o usuário a quem enviar: os dois pacotes de setembro vieram da Rakshitha (`received.txt` de 12-Oct), mas o BAU Master lista Deepak como Primary SBC de todos os 6 clientes DK (Athul S como backup do KGS). As perguntas abaixo valem para qualquer um dos dois.

### 2.1 Dinamarca, Sherwin-Williams Denmark A/S, 2026-09 (Painel: DK-SHERWIN 2 Not tested)

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | F-02 / A-03 (arquivo enviado ao eIndkomst) | Please send the exact file uploaded to eIndkomst for period 09.2026. The file in the pack has the severance in field 0013 and no field 0069, while SKAT received 0069 = 571,251. | Média. O arquivo do pacote não é o que a SKAT recebeu; sem o arquivo real não dá para fechar a conferência entre envio e recibo. | DK_SherwinWilliams_2026-09_Validation.xlsx:Findings Register!A5:I5; Coverage!A6:F6 |
| 2 | NT-01 (skattekort) | Please send the eSkattekort extract (trækprocent and monthly fradrag) valid for September 2026 for all employees in the run. | Média. Hoje o A-skat é conferido com % e fradrag impressos no contracheque (decisão de 14-10), não com o cartão oficial. | DK_SherwinWilliams_2026-09_Validation.xlsx:Not Tested!A4:D4 |
| 3 | NT-02 (taxas de pensão) | Please send the pension agreement showing employee and employer contribution rates (optional). | Baixa. Pensão é contratual, não estatutária; só serve se quisermos conferir a cobrança. | DK_SherwinWilliams_2026-09_Validation.xlsx:Not Tested!A5:D5 |

Rascunho existente (`Denmark/Sherwin Williams Denmark - 2026-09/02 Validation/followups.md`, ação C-02): cobre só o item 1. Faltam 2 e 3.
Já recebido: relatório eIndkomst, Afstemning da SKAT, G2N, contracheques, GL, arquivos de banco EE/ER e cadastro de 17 empregados (12-Oct, nada faltando).
Descartado: F-01 (campo 0069 bruto, ação A-03), F-03 e F-04 (base do Store Bededag e do ferietillæg, decisão D-03) são decisão nossa/Dev; o CPR com hífen em F-02 é configuração.

### 2.2 Dinamarca, KGS Fire & Security Danmark ApS, 2026-09 (Painel: DK-KGS 4 Not tested)

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | F-01 (seguro-saúde, elemento 62610) | What type of cover is pay element 62610 "Value of Health Insurance"? Standard employer-paid health insurance / work-injury cover / medically justified addiction treatment / other (please specify). | Alta (F-01 High). Seguro-saúde pago pelo empregador é tributável (0026/0013) salvo as exceções DJV C.A.5.15.1; o tipo decide se há AM e A-skat não retidos. | DK_KGSFireSecurity_2026-09_Validation.xlsx:Findings Register!A4:I4 |
| 2 | NT-04 (cadastro) | Please send the master data export for September 2026 for the 6 employees. | Média. Não há cadastro no pacote; o G2N não traz CPR para 4 empregados e o contracheque imprime "CPR-nummer" vazio nos 6. | DK_KGSFireSecurity_2026-09_Validation.xlsx:Not Tested!A5:D5; Findings Register!A5:I5 |
| 3 | NT-01 (skattekort) | Please send the eSkattekort extract (trækprocent and monthly fradrag) for September 2026 for all employees, including the leaver whose payslip prints no tax-card data. | Média. O A-skat do desligado (6.286 sobre base de 17.458, 36,0%) não pôde ser conferido; o controle D-02 ficou "Not tested". | DK_KGSFireSecurity_2026-09_Validation.xlsx:Not Tested!A6:D6; Coverage!A14:F14 |
| 4 | NT-02 (taxas de pensão) | Please send the pension agreement with employee and employer contribution rates (optional). | Baixa. Contratual, não estatutário. | DK_KGSFireSecurity_2026-09_Validation.xlsx:Not Tested!A7:D7 |

Rascunho existente (`Denmark/KGS Fire & Security Denmark - 2026-09/02 Validation/followups.md`, ação C-03): cobre 1 e 2. Faltam 3 e 4.
Já recebido: Gross-to-Net, contracheques, relatório eIndkomst, Afstemning, GL padrão (12-Oct); não há arquivo de banco (cliente de movimentação de dinheiro, decisão de 14-10).
Descartado: NT-03 (banco/pagamento líquido) é fora de escopo por decisão de 14-10; F-02 (modelo de contracheque sem CPR e cálculo zerado no desligado, A-06) e F-03 (rótulos do GL) são Dev; F-01 em si (tributar o seguro, A-02) é configuração.

---

## 3. Athul Satheesh (Primary SBC Suécia; envia Holanda/Quest)

### 3.1 Holanda, Quest Software B.V., 2026-09 (Painel: NL-QUEST 5 Not tested; falta recibo)

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | NT-01 / F-08 (aceite da declaração) | Please send the Digipoort status response (or a Belastingdienst portal screenshot) for return 809615253L01P20260901. | Alta (F-08 High). O "Wage Tax Overview" do pacote é do HRBLIZZ, não da autoridade; aceite não provado. | NL_Quest_2026-09_Validation_v1.2.xlsx:Not Tested!A4:D4; Findings Register!A11:I11 |
| 2 | NT-02 / F-09 (taxa Whk) | Please send the 2026 Whk notice (mededeling or beschikking). Does it classify Quest Software B.V. as a small employer at 1.45% (sector 42)? | Média. 1,45% é a taxa do setor 42 para empregador pequeno; se o aviso trouxer médio/grande, a taxa e o valor declarado mudam. | NL_Quest_2026-09_Validation_v1.2.xlsx:Not Tested!A5:D5; Findings Register!A12:I12 |
| 3 | NT-03 (acumulados) | Please send the August 2026 payslips (or the year-to-date G2N through August) for the 4 employees. | Média. Sem agosto não dá para conferir a rolagem dos acumulados do contracheque de setembro. | NL_Quest_2026-09_Validation_v1.2.xlsx:Not Tested!A6:D6 |
| 4 | NT-05 (Jaarloon BT) | Please send the Jaarloon BT build-up per employee (prior-year wage used to set the special-rate percentage). | Baixa. A derivação precisa do salário do ano anterior, que não está no pacote. | NL_Quest_2026-09_Validation_v1.2.xlsx:Not Tested!A7:D7 |
| 5 | NT-06 / F-11 (auxílio home office) | Is the EUR 100 per month home allowance (3 employees) designated under the WKR (vrije ruimte / eindheffing)? Yes / No (paid under the targeted exemption of EUR 2.45 per home-working day) / Other. | Média (Observation). O limite sem designação é EUR 2,45 por dia (no máx. EUR 53,90 em setembro); até EUR 168,93 por mês podem ser salário se não houver designação. | NL_Quest_2026-09_Validation_v1.2.xlsx:Not Tested!A8:D8; Findings Register!A14:I14 |
| 6 | F-03 (arquivo bancário) | Which SEPA file was sent to the bank for the September net pay: the Deutsche Bank file (4 transfers, 48,884.10) or the file named "Kantar Netherlands Bank XML File"? | Média. O segundo arquivo é inválido em ISO 20022 (separador de milhar, EndToEndId repetido) e leva o nome de outro cliente; se fosse transmitido, seria rejeitado. | NL_Quest_2026-09_Validation_v1.2.xlsx:Findings Register!A6:I6 |
| 7 | F-07 (compra de férias, elemento 21216) | Is the vacation purchase (pay element 21216) a net-pay deduction by agreement, or a salary exchange that should reduce gross wage? Net deduction / Salary exchange. | Baixa (Observation). Hoje é deduzida do líquido e não reduz o salário fiscal nem o SV; se for troca de salário, o bruto deveria cair. | NL_Quest_2026-09_Validation_v1.2.xlsx:Findings Register!A10:I10 |

Rascunho existente (`Netherlands/Quest Software - 2026-09/02 Validation/followups.md`, ação C-15): cobre 1 a 4 e 6. Faltam 5 (WKR; a ação C-15 menciona, mas o texto do rascunho não) e 7.
Já recebido: zip de 09-Oct (8 arquivos); Audit Report v1.2 emitido sem esses documentos (decisão D-04).
Descartado: F-01 e F-02 (horas declaradas), F-04 (rótulos do GL), F-05 (data limite do Wage Tax Overview), F-06 (arbeidskorting), F-10 (SVW no contracheque) são Dev/configuração.

### 3.2 Suécia, One Identity Sweden AB (pasta "Quest Software - 2026-09"), 2026-09 (Painel: SE-ONEID 6 Not tested; falta recibo)

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | NT-01 / F-01 (Kvittens) | Please send the Skatteverket Kvittens for the AGI of One Identity Sweden AB (559400-9267), period 202609. The Kvittens in the pack belongs to Quest Software AB (556602-0433). | Alta (F-01 High). Sem o recibo correto o aceite da AGI de setembro não está provado; o pacote misturou duas entidades. | SE_OneIdentitySweden_2026-09_Validation.xlsx:Not Tested!A4:D4; Findings Register!A4:I4; Coverage!A6:F6 |
| 2 | NT-05 (data de entrega) | Was the One Identity AGI for 202609 submitted to Skatteverket on or before 12-Oct-2026? Yes (date and time) / No (actual date). | Média. A AGI foi criada em 22-09; a data de envio só aparece na Kvittens, que pertence a outra entidade. | SE_OneIdentitySweden_2026-09_Validation.xlsx:Not Tested!A8:D8 |
| 3 | NT-02 (arquivo bancário) | Please send the bank payment file of 28-09-2026 for pay group SWE_Monthly_OID. | Média. Não há arquivo de banco no pacote (pendente desde 09-Oct). | SE_OneIdentitySweden_2026-09_Validation.xlsx:Not Tested!A5:D5 |
| 4 | NT-03 / F-01 (cadastro) | Please send the master data export for One Identity Sweden AB (7 employees). The master data in the pack is for Quest Software (4 people). | Média. Sem o cadastro correto não dá para reconciliar a população da AGI nem os dados de cada empregado. | SE_OneIdentitySweden_2026-09_Validation.xlsx:Not Tested!A6:D6; Coverage!A30:F30 |
| 5 | NT-04 (skattebeslut) | Please send the Skatteverket tax decision (skattebeslut: table and column) on file for each of the 7 employees. | Média. D-01 hoje só prova que o valor retido existe em alguma tabela de 2026, não que seja a tabela certa do empregado. | SE_OneIdentitySweden_2026-09_Validation.xlsx:Not Tested!A7:D7 |
| 6 | F-05 (novo contratado) | For the employee hired on 01-09-2026 (withheld on table 39, which no municipality uses in 2026), is there a Skatteverket decision specifying table 39? Yes (send it) / No. | Média (Observation). Só a tabela 39 reproduz a retenção, mas nenhum município passa de 37; a AGI traz o condado em vez do município. | SE_OneIdentitySweden_2026-09_Validation.xlsx:Findings Register!A8:I8 |
| 7 | NT-06 (licença parental, elemento 79449) | Please send the collective-agreement terms for the parental-leave deduction (optional). | Baixa. A regra é contratual (acordo coletivo), não estatutária. | SE_OneIdentitySweden_2026-09_Validation.xlsx:Not Tested!A9:D9 |

Rascunho existente (`Sweden/Quest Software - 2026-09/02 Validation/followups.md`, ação C-04): cobre 1, 3, 4 e 6 (o item 4 do rascunho cita o nome do empregado; trocar por "the employee hired on 01-09-2026" ao enviar). Faltam 2, 5 e 7.
Já recebido: zip (09-Oct) e Kvittens do monday (do Quest AB, não serve). Segue pendente o arquivo de banco (`received.txt`).
Descartado: F-02 (payout de férias pela tabela de engångsbelopp, A-04/D-02) é decisão do Wallisson; F-03 (acumulados do contracheque) e F-04 (arredondamento FK487) são Dev; F-06 (endereços divergentes entre contracheque e AGI) é qualidade de dado de 3 empregados e foi deixado de fora por ser baixo valor (pode virar uma pergunta de confirmação se o usuário quiser).

---

## 4. Suresh Jalihal (Primary SBC Holanda; envia Excerpta Medica)

### 4.1 Holanda, Excerpta Medica B.V., 2026-09 (Painel: NL-EXCERPTA 5 Not tested; falta recibo)

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | NT-01 / F-06 (aceite da declaração) | Please send the Digipoort status response (or Belastingdienst ontvangstbevestiging) for return 822945526L01P20260901. | Alta (F-06 High). Sem isso o aceite da declaração de setembro não está provado. | NL_Excerpta_2026-09_Validation_v1.2.xlsx:Not Tested!A4:D4; Findings Register!A9:I9 |
| 2 | NT-02 (taxa Whk) | Please send the 2026 Whk beschikking (differentiated premium); the return uses 1.71%. | Média. Só o ato oficial confirma a taxa; hoje só passou na plausibilidade. | NL_Excerpta_2026-09_Validation_v1.2.xlsx:Not Tested!A5:D5 |
| 3 | NT-03 / F-03 (correção de agosto) | Please send the August 2026 loonaangifte as first submitted. | Média (Observation). O bloco de correção de agosto traz um empregado com saldo zero; sem a mensagem original não se vê o que mudou. | NL_Excerpta_2026-09_Validation_v1.2.xlsx:Not Tested!A6:D6; Findings Register!A6:I6 |
| 4 | NT-05 (acumulados) | Please send the August 2026 payslips (or the year-to-date G2N through August). | Média. Só há contracheques de setembro; não dá para conferir a rolagem dos acumulados. | NL_Excerpta_2026-09_Validation_v1.2.xlsx:Not Tested!A7:D7 |
| 5 | NT-07 / F-08 (auxílio-telefone, elemento 62805) | Is the Phone Allowance (EUR 21.00 to 33.50, 10 employees) designated under the WKR (vrije ruimte / eindheffing)? Yes / No. | Média (Observation). Auxílio fixo de telefone não tem isenção específica; sem designação são EUR 260 por mês de salário não tributado. Home office e transporte já cabem nas isenções por dia/km. | NL_Excerpta_2026-09_Validation_v1.2.xlsx:Not Tested!A8:D8; Findings Register!A11:I11 |

Rascunho existente (`Netherlands/Excerpta Medica - 2026-09/02 Validation/followups.md`, ação C-14): cobre 1 a 4 e o item 5 (o rascunho também pergunta sobre home office e transporte, que a validação v1.2 já aceita como isenção; pode encurtar para só o telefone).
Já recebido: zip de 08-Oct; nenhuma resposta aos itens acima.
Descartado: F-01 (retenção do empregado em idade AOW), F-02 (centavos de arredondamento), F-04 (crédito de loonheffingskorting em segundo vínculo, regra do motor), F-05 (data limite) e F-07 (SVW no contracheque) são Dev/configuração.

---

## 5. Malika Iskakova (In-Country Expert Cazaquistão)

### 5.1 Cazaquistão, Mastercard (escritório de representação), 2026-10 (Painel: KZ 5 Not tested, mas v1.1 tem 4; validado, qualified)

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | F-06 (período declarado, ação C-18) | Does the payroll in the pack (labelled October 2026 in 1C and on the payslip, payment orders for period 10/2026) belong to September 2026 or October 2026? | Alta (F-06 High). Os mesmos valores aparecem no 200.00 do 3T como 3º mês, assinado em 25-09, antes do fim do trimestre e dos pagamentos de 03-15.10. | KZ_Mastercard_2026-10_Validation_v1.1.xlsx:Findings Register!A5:I5; Coverage!A30:F30 |
| 2 | F-06 (condicional ao item 1) | If the payroll belongs to October 2026, how and in which form 200.00 period will it be reported (Q4 2026)? | Alta. Se outubro foi declarado como setembro, as obrigações de setembro nas contas pessoais KGD/ГФСС ficam atendidas por pagamentos marcados como outubro. | KZ_Mastercard_2026-10_Validation_v1.1.xlsx:Findings Register!A5:I5 |
| 3 | F-02 (nome do arquivo do contracheque) | Is the payslip file named "Payslips August" the payslip of this same October payroll? Yes / No. | Média. O nome diz agosto, a pasta diz outubro, e o contracheque imprime 20 dias contra 21 no 1C. | KZ_Mastercard_2026-10_Validation_v1.1.xlsx:Findings Register!A6:I6; Coverage!A21:F21 |
| 4 | F-03 (modelo PRE) | Is the PRE template in the pack (transaction dates 2026-07-15, PR560 = 909,883.40, cells with #NAME?, a different employee number) the final version sent to the client for the 15-Oct cycle? Yes / No (if No, please send the final). | Média. O relatório de funding do cliente fica pouco confiável se esta for a versão enviada; os valores do Payroll-Local estão corretos. | KZ_Mastercard_2026-10_Validation_v1.1.xlsx:Findings Register!A7:I7; Coverage!A23:F23 |
| 5 | NT-04 (cadastro) | Please send the employee master record (residency, pensioner or disability status, exemptions) for October 2026. | Baixa. A isenção hoje é inferida da data de nascimento no IIN (1985); não há cadastro. | KZ_Mastercard_2026-10_Validation_v1.1.xlsx:Not Tested!A6:D6 |
| 6 | NT-02 (ИПН acumulado, opcional) | Please send the 2026 year-to-date ИПН tax card (налоговая карточка) for the employee. | Baixa. F-01 já está fechado (faixa de 15% confirmada pela linha 200.01.008); o cartão só confirma a faixa. | KZ_Mastercard_2026-10_Validation_v1.1.xlsx:Not Tested!A4:D4 |
| 7 | NT-03 (GL, praticamente respondido) | Does the client keep an accounting ledger outside 1C ZUP? Yes (please send the October 2026 export) / No. | Baixa. A remetente já disse em 19-Oct que o 1C ZUP não tem lançamentos contábeis; só falta saber se existe razão em outro sistema. | KZ_Mastercard_2026-10_Validation_v1.1.xlsx:Not Tested!A5:D5; 01 Received/received.txt (update 19-Oct) |

Rascunho existente (`Kazakhstan/Mastercard - 2026-10/02 Validation/followups.md`): o bloco C-18 cobre 1, 2 e 3 (item 2 só em parte: "how it will be reported for Q4"). O bloco C-05 (itens 1, 2, 3, 4) ficou substituído: 200.00 do 3T com recibo KGD chegou em 19-Oct, o GL não existe no 1C. Faltam 4, 5, 6 e 7.
Já recebido: 200.00 do 3T e comprovante de entrega (19-Oct, ação C-05 "Parcial"); resposta de que não há GL no 1C ZUP.
Descartado: NT-01 (200.00 e recibo, fechado na v1.1), NT-05 (regra de arredondamento do СО/ВОСМС/ООСМС: é fonte oficial a localizar por nós), F-04 (СО +0,62 KZT), F-05 (rótulos do PRE) e a parte de modelo do F-02 (A-06) são Dev.

---

## 6. Nataliia Hahan (Primary SBC Ucrânia)

Não existe `followups.md` para agosto (UA-08). Setembro tem o rascunho C-17. Itens de julho aparecem nos dois pacotes (uma só resposta resolve ambos).

### 6.1 Ucrânia, Altium, 2026-08 (Painel: UA-ALTIUM-08 12 Not tested; planilha tem 14 linhas na aba Not Tested)

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | F-01 (XML do relatório unificado) | Can you export the filed unified report (J0500111 / J0510111 / J0510411 / J0510511) as plain unpacked XML from the filing software, or download it from the DPS Electronic Cabinet? | Alta. O arquivo recebido é um contêiner "PACKED_XML" que não decodifica; sem o XML puro não há validação contra o XSD da DPS. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A2:D2 |
| 2 | F-01 (recibos DPS) | Please send DPS receipt No.1 for the August unified report (receipt No.2, J1499202, was received on 08-Oct). | Média. A planilha pede os recibos No.1 e No.2; só o No.2 consta em `received.txt`. Conferir se o No.1 já não está em 01 Received antes de enviar. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A2:D2; 01 Received/received.txt |
| 3 | F-02 (XML do 1-PV) | Please send the monthly 1-PV for August (S0301016) as plain unpacked XML. | Média. Mesmo contêiner empacotado; hoje só se conferiu o formulário impresso. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A3:D3 |
| 4 | F-02 / C-10 (recibo do 1-PV) | Please send the State Statistics receipt (statzvit) for the August 1-PV. | Alta (Painel: C-10 "recibo do 1-PV"; recibo "Parcial"). Sem recibo o envio do 1-PV não está provado. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A3:D3; Acompanhamento_Internal_Certification.xlsx:Ações!A20:I20 |
| 5 | R-07b (período de férias) | For the employee on leave 25.08 to 13.09.2026 (20 calendar days, paid for 17), was 28 to 30.08 worked (leave split in two parts) or is vacation pay missing for those 3 days? Worked / Pay missing. | Média. Há 3 dias de diferença no pagamento; pode haver subpagamento. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A4:D4 |
| 6 | R-07b (comprovante do item 5) | Please send the leave order and the time sheet (табель) for that employee. | Média. Necessário para fechar o item 5. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A4:D4 |
| 7 | R-17 (indexação) | Please send the indexation calculation sheet (base month and CPI series) for the 3 employees paid indexation in August. | Baixa. Sem base nem série de índice não dá para recalcular. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A5:D5 |
| 8 | X-05 / C-08 (julho) | Please send the July 2026 payslips and G2N. | Média. A rolagem dos acumulados e o consumo do teto da base de agosto dependem de julho; também destrava o 1-PV do 3T (UA-09). | UA_Altium_2026-08_Validation.xlsx:Not Tested!A6:D6, A9:D9 |
| 9 | C-08 (Д1 de julho) | Please send the July 2026 Д1 (J0510111) as filed. | Média. Vacation/bonus pagos em meses anteriores consomem a base máxima de agosto (4 empregados). | UA_Altium_2026-08_Validation.xlsx:Not Tested!A9:D9 |
| 10 | C-06 (1-PV: ФОП e horas) | Please send the 1-PV working file with the ФОП breakdown (rows 1020, 1070, 1030, 1060) for August. | Média. A linha 1020 (9.132,9 mil) não se reconstrói do G2N; precisa da alocação por mês de trabalho (Instrução No.5). | UA_Altium_2026-08_Validation.xlsx:Not Tested!A7:D7 |
| 11 | C-07 (Д1 col. 13/22/26) | Please send the August time sheets showing unpaid-leave days, part-time and fixed-hours status for all employees. | Média. A coluna 13 do Д1 está em branco em todas as linhas e não há tabelas de horas nem contratos. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A8:D8 |
| 12 | M-04 (mobilizados) | Please send the mobilisation orders or an HR status report for the 3 employees reported under Д1 category 47. | Média. O cadastro não tem campo de mobilização/suspensão. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A10:D10 |
| 13 | M-04 (desligamento) | Please send a master-data extract dated after the 31.08.2026 dismissal. | Baixa. O cadastro é de 10.08, anterior ao desligamento. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A10:D10 |
| 14 | M-05 (headcount 37) | Please send the average-headcount calculation (табель) behind the 37 reported in form 091 and 1-PV row 1040. | Baixa. 37 só é coerente com 40 menos 3 mobilizados por inferência. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A11:D11 |
| 15 | NT-BANKST (extratos) | Please send the bank statements from 14.08 to 04.09.2026 showing the actual value dates of the advance, balance and budget payments (PIT, military levy, ЄСВ). | Média. Datas de 1C, arquivo de banco e G2N divergem (F-08); o vencimento do PIT/ML depende da data real. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A12:D12; Findings Register!A9:I9 |
| 16 | NT-GLBAL (saldos do razão) | Please send the August trial balance or account cards for 661, 663, 641, 642 and 651. | Baixa. O GL recebido só tem o documento de provisão, sem saldos nem lançamentos de banco. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A13:D13 |
| 17 | NT-INS (tempo de seguro) | Please send the Pension Fund insurance record (ОК-5 / ОК-7) behind the 70% sick-leave rate (62 months). | Baixa. O cadastro não tem o campo de tempo de seguro. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A14:D14 |
| 18 | NT-LEAVE (saldos de férias) | Please send the leave ledger and the vacation calculation sheets for the employee dismissed on 31.08 (3 days compensated) and for 2 employees with vacation calculations to confirm. | Baixa. Saldos de férias e compensação na rescisão não foram suprimidos. | UA_Altium_2026-08_Validation.xlsx:Not Tested!A15:D15 |
| 19 | F-02 / R-12 (norma de horas) | What is the approved August 2026 working-time norm for the client: 19 days / 152 h (as used in the run), 21 days / 168 h (martial-law calendar) or 20 days / 160 h? Please send the internal order or work schedule. | Média (F-02 Medium). A norma de 19 dias não bate com nenhum calendário; 10 empregados com salário proporcional podem ter sido pagos a mais (cerca de 19 mil UAH). | UA_Altium_2026-08_Validation.xlsx:Findings Register!A3:I3 |
| 20 | F-09 (GL, código 126) | Is the August GL export complete? The posting Dt 949 / Kt 661 for the in-kind benefit (income code 126) has no amount. If not, please re-export it. | Baixa. O razão não reflete 222.175,45 UAH de renda código 126 reportada no 4ДФ. | UA_Altium_2026-08_Validation.xlsx:Findings Register!A10:I10 |
| 21 | F-12 (regime de trabalho) | Is the part-time employee recorded as "Full Time" in master data actually part-time (19 h per month) as reported in Д1 column 22? Part-time / Full-time. | Média (F-12 Medium). Como full-time o salário ficaria abaixo do mínimo e acionaria a base mínima de ЄСВ; no relatório está como part-time. | UA_Altium_2026-08_Validation.xlsx:Findings Register!A13:I13 |
| 22 | F-13 (conta de contratado) | Please send the valid 29-character UA IBAN for the civil-contract person whose account in 1C and master data has only 6 characters. | Baixa. Não dá para rastrear o pagamento; nada no arquivo de banco. | UA_Altium_2026-08_Validation.xlsx:Findings Register!A14:I14 |
| 23 | F-10 (nascimento invertido) | For 2 employees whose master-data date of birth has day and month swapped against the RNOKPP, which is correct: master data or RNOKPP? | Baixa. Sem efeito nos valores de agosto; risco em regras por idade. | UA_Altium_2026-08_Validation.xlsx:Findings Register!A11:I11 |
| 24 | F-11 (data de admissão) | For 1 employee, which hire date is correct: master data (18.04.2023) or G2N (22.04.2023)? | Baixa. Afeta direitos por tempo de casa; sem impacto no relatório de agosto. | UA_Altium_2026-08_Validation.xlsx:Findings Register!A12:I12 |

Rascunho existente: nenhum para agosto (só o C-17, que reforça o C-10 "recibo do 1-PV" e pede julho). O C-17 cobre os itens 4, 8, 9 em parte. Falta redigir todo o restante para agosto.
Já recebido: master data (09-Oct, antes do item 12/13 serem preparados); GL, arquivo DBF do banco, relatório de pagamento, folha do 1C, recibo No.2 do relatório unificado (08-Oct); 1-PV mensal reenviado idêntico (09-Oct). Segue sem receber: recibo do 1-PV/estatística e Д1 de julho (`received.txt`).
Descartado: F-03 (férias pagas fora do prazo, confirmado pelo arquivo de banco), F-04/F-05 (centavos), F-06 (categoria 47), F-07 (rótulo do G2N em inglês), F-01 do contracheque (benefício in natura, A-06) e C-01b/A-05 (fora de escopo) são decisão nossa/Dev/sem SBC. O resumo de contagem do Painel fala em 12; a aba Not Tested tem 14 linhas.

### 6.2 Ucrânia, Altium, 2026-09 (Painel: UA-ALTIUM-09 7 Not tested; Interim)

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | S-11 (relatório unificado de setembro) | Please send the filed unified tax report for September 2026 (Д1, 4ДФ, Д5) as submitted, with the DPS receipts. If not filed yet, what is the expected filing date? | Alta. Sem o relatório de setembro não há validação final; a remetente disse que ainda não estava preparado. | UA_Altium_2026-09_Validation.xlsx:Not Tested!A2:D2 |
| 2 | S-13 (contracheques) | Please send the September 2026 payslips. | Alta. O contracheque é a âncora da validação. | UA_Altium_2026-09_Validation.xlsx:Not Tested!A3:D3 |
| 3 | S-14 (GL) | Please send the September 2026 GL export. | Média. Mesma lacuna que em agosto. | UA_Altium_2026-09_Validation.xlsx:Not Tested!A4:D4 |
| 4 | S-14 (banco) | Please send the September 2026 bank payment file. | Média. Sem arquivo de banco de setembro não se confere pagamento. | UA_Altium_2026-09_Validation.xlsx:Not Tested!A4:D4 |
| 5 | S-12 (1-PV mensal de setembro) | Please send the September monthly 1-PV and its State Statistics receipt. | Média. Só chegou o 1-PV trimestral do 3T. | UA_Altium_2026-09_Validation.xlsx:Not Tested!A8:D8 |
| 6 | S-15 (julho) | Please send the July 2026 G2N, payslips and Д1 (J0510111). | Média. Necessários para o 1-PV do 3T e para o consumo do teto da base de agosto (mesmo pedido do item 8/9 de agosto). | UA_Altium_2026-09_Validation.xlsx:Not Tested!A7:D7 |
| 7 | Q-04 (1-PV 3T, linha 7040) | Does 1-PV row 7040 (2 persons, 59.3 thousand UAH) include July civil-contract pay of 17.8 thousand UAH (August 22.0 + September 19.5 = 41.5)? Yes / No. | Baixa. Só o valor de julho fecha a conta; julho não está no pacote. | UA_Altium_2026-09_Validation.xlsx:Not Tested!A5:D5 |
| 8 | Q-05 (1-PV 3T, fundo salarial) | Please send the Q3 1-PV working file (wage fund 5010 to 5090 and women 7010 breakdown). | Média. 5010 = 27.799,9 mil não se reconstrói sem julho e sem o 1-PV mensal de setembro. | UA_Altium_2026-09_Validation.xlsx:Not Tested!A6:D6 |
| 9 | Q-05 (indexação 5051) | What indexation amount was paid in July 2026? The Q3 1-PV row 5051 shows 1.1 thousand UAH against 0.79 thousand for August plus September. | Baixa. Julho teria de ser 0,26 a 0,36 mil, abaixo do nível de agosto e setembro: sem explicação. | UA_Altium_2026-09_Validation.xlsx:Not Tested!A6:D6 |
| 10 | F-02 / S-06 ("Overpayment in August") | Is there a Pension Fund refusal or reversal behind the sick-benefit amount recovered from 1 employee in September as "Overpayment in August"? Yes (send the Fund document) / No (to be reversed). | Média (F-02 Medium). Em agosto foi pago como benefício normal financiado pelo Fundo; a recuperação pode ser indevida e duplica PIT/ML. | UA_Altium_2026-09_Validation.xlsx:Findings Register!A3:I3; Coverage!A7 |
| 11 | S-15 / C-10 (recibo estatístico de agosto e 3T) | Please send the State Statistics receipts for the August monthly 1-PV and for the Q3 quarterly 1-PV. | Alta (C-10/C-17). Painel: recibo "Parcial" em agosto, "Não" em setembro. | UA_Altium_2026-09_Validation.xlsx:Not Tested!A5:D8; Acompanhamento_Internal_Certification.xlsx:Ações!A32:I32 |

Rascunho existente (`Ukraine/Altium - 2026-09/02 Validation/followups.md`, ação C-17, aguarda ok do usuário): cobre 1, 2, 3 e 4 (juntos no texto "payslips, GL export and bank file"), 5, 6, 10 e 11. Faltam 7, 8 e 9 (valem se o usuário quiser fechar o 3T).
Já recebido: G2N de setembro (UKR e GTN) e 1-PV trimestral do 3T (07 e 09-Oct). Nada de relatório, contracheques, GL ou banco de setembro.
Descartado: F-01 (férias pagas depois do prazo, 6 casos), F-03 (centavos no PIT 126) e F-04 (título do G2N de setembro "за серпень") são Dev/observação sem pedido à SBC. S-09 (título errado) foi deixado de fora porque o arquivo é impresso e arquivado pelo cliente; pode ser avisado numa linha se o usuário quiser.

---

## 7. Srikanth Kondam (Primary SBC Reino Unido)

### 7.1 Reino Unido, McDermott UK, 2026-09 (Painel: UK-MCDERMOTT 17 Not tested; validado, qualified)

A planilha de validação é de 07-Oct; o Audit Report de 16-Oct incorporou o que chegou em 09-Oct (recibos HMRC e cadastro de 73 linhas). NT-01 está fechado e NT-02 foi reduzido. Os itens abaixo seguem o que o Audit Report ainda lista como "não fornecido".

| # | Controle/achado (ID) | O que pedimos | Por quê | Fonte |
|---|---|---|---|---|
| 1 | NT-02 (avisos HMRC) | Please send the HMRC DPS notice log (P6 / P6B / P9, SL1 / SL2, PGL1 / PGL2) received for the employees in tax year 2026-27. | Média. A planilha só prova o período contra o código aplicado; os códigos (incluindo 15 K codes e 1 escocês) não foram provados contra a HMRC. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A5:D5 |
| 2 | NT-03 (arquivo criptografado) | What does the PGP-encrypted file mcd3.1505120120260928.txt.gpg contain (a second payment batch, an HMRC or pension payment?) and what is its total? | Média. O nome difere do arquivo de banco legível (...1001... x ...1201...); o conteúdo é desconhecido. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A6:D6 |
| 3 | NT-04 (FPS de agosto) | Please send the August 2026 FPS as submitted, plus the first HRBLIZZ FPS of 2026-27. | Média. Destrava a rolagem dos acumulados, o histórico de mudança de Payroll ID (F-02, 65 de 69 registros) e o desligado reportado de novo (F-06). | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A7:D7 |
| 4 | NT-04 (contracheques de agosto) | Please send the August 2026 payslips (or the G2N) for the 69 employees. | Média. Sem agosto não se testa a rolagem do acumulado do mês 6. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A7:D7 |
| 5 | NT-05 (Apprenticeship Levy: folha acumulada) | Please send the year-to-date pay bill by month including employees who left before September. | Média. O EPS declara levy YTD de 9.032,00; o piso do FPS é 8.026,71 e só fecha se os desligados somarem cerca de GBP 201 mil. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A8:D8 |
| 6 | NT-05 (allowance do grupo) | How is the GBP 15,000 Apprenticeship Levy allowance allocated across the connected companies of the McDermott UK group? | Baixa. A EPS usa AnnualAllce de 15.000; a alocação do grupo não está no pacote. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A8:D8 |
| 7 | NT-06 (Employment Allowance) | Does the McDermott UK group claim the Employment Allowance? Yes / No (the EPS has EmpAllceInd = no). | Baixa. "No" é coerente com não reivindicar, mas a elegibilidade do grupo é desconhecida. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A9:D9 |
| 8 | NT-07 (SMP) | Please send the SMP calculation record for the employee on maternity leave (MATB1 date, average weekly earnings, leave start date, KIT days used). | Média. Só a taxa de setembro (GBP 194,32) e a recuperação de 92% foram testadas, não o período de 39 semanas nem a fase de 90% da AWE. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A10:D10 |
| 9 | NT-08 (PBIK, registro) | Was payrolling of medical and dental benefits registered with HMRC before 6 April 2026? Yes (send confirmation) / No. | Média. Os itens 60/149 do FPS só são válidos com registro prévio. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A11:D11 |
| 10 | NT-08 (contribuição do empregado) | Do employees contribute towards the medical and dental cover (cost "made good")? Yes (send the policy terms) / No. | Baixa. Define o valor tributável do benefício. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A11:D11 |
| 11 | NT-09 (childcare voucher: avaliação) | Please send the 2026-27 basic earnings assessment for the 1 employee on the childcare-voucher salary sacrifice. | Baixa. O valor sacrificado (2 x GBP 124) bate com o limite de contribuinte de taxa maior por inferência. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A12:D12 |
| 12 | NT-09 (childcare voucher: adesão) | What is the scheme join date of that employee? | Baixa. A isenção depende da data de entrada no plano. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A12:D12 |
| 13 | NT-10 (reembolso de mobilidade, natureza) | For the "Mobility_TE Repayment" that reduces taxable and NICable pay (also in August) for 1 employee, was the original payment taxable earnings or an exempt relocation payment? Taxable / Exempt relocation / Other. | Média. Reembolso de ganho anterior normalmente não reduz o Class 1 do período seguinte; a posição só se confirma sabendo a natureza. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A13:D13 |
| 14 | NT-10 (reembolso de mobilidade, acordo) | Please send the mobility policy or repayment agreement for that case. | Baixa. Complementa o item 13. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A13:D13 |
| 15 | NT-11 (P45 do desligado) | Was a P45 issued to the employee who left on 31-07-2026? Yes (date) / No. | Média. Se houve P45, um pagamento posterior usa 0T week1/month1 e não geraria o reembolso de imposto de agosto (GBP 1.090,35) mostrado no Variance Report. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A14:D14 |
| 16 | NT-12 / MD-01 (faixa de horas) | What are the contracted weekly hours of the employee on 20 hours reported in hours band D (30+)? 20 h (band B, 16 to 23.99) / 30 h or more (band D). | Média. Item do Audit Report 16/10 (novo): se forem 20 h, o item 54 do FPS está errado. Os demais 68 registros foram conferidos pelo cadastro. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A15:D15; Acompanhamento_Internal_Certification.xlsx:Achados!A85:K85 |
| 17 | NT-13 (publicação dos contracheques) | On what date and time were the September payslips made available to employees (payslip publication log)? | Baixa. A entrega até o payday não está evidenciada. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A16:D16 |
| 18 | NT-14 (starter) | Was a P45 or a starter checklist completed for the 1 starter on starter declaration B (1257L month 1)? P45 given / Starter checklist (send it). | Baixa. Declaração B assume que não houve P45. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A17:D17 |
| 19 | NT-15 (auto-enrolment, status) | For the 3 employees with pay but no pension deduction: opted out / postponed (waiting period) / not eligible? | Média. Sem o status não se sabe se faltou inscrição automática. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A18:D18 |
| 20 | NT-15 (auto-enrolment, regras) | Please send the pension scheme contribution basis and rates. | Baixa. Necessário para confirmar a base de contribuição. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A18:D18 |
| 21 | NT-17 (P32 e pagamento) | Please send the P32 and the HMRC payment confirmation for tax month 6 (due 22-10-2026). | Média. A obrigação indicativa é GBP 253.354,64 antes da recuperação de SMP e do levy do mês; não há prova de pagamento. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A20:D20 |
| 22 | NT-17 (EPS de agosto) | Please send the August 2026 EPS as submitted. | Baixa. Necessário para fechar a recuperação de SMP e o levy do mês de setembro. | UK_McDermott_2026-09_Validation.xlsx:Not Tested!A20:D20 |
| 23 | MD-02 (cabeçalho do cadastro) | The master data extract header says 73 employees but lists 69. Does the extract omit 4 active employees? Yes (send them) / No. | Baixa (Observation, Audit Report 16/10). Os 69 batem com o FPS; o cabeçalho diverge. | Acompanhamento_Internal_Certification.xlsx:Achados!A86:K86 |

Rascunho existente: nenhum (`United Kingdom/McDermott UK - 2026-09/02 Validation/` não tem `followups.md`). Falta redigir tudo.
Já recebido: NT-01 resolvido (ACKs FPS e EPS colados no Chat em 09-Oct, IRmarks conferem; ação C-09 concluída em 2026-10-09); cadastro de empregados (`Custom_73_Employees_September2026.xlsx`, 09-Oct) cobriu o que o NT-02 pedia sobre códigos de imposto, categoria NI, planos de empréstimo estudantil e datas de início (69 registros batem com o FPS, MD-02), restando o log de avisos HMRC (item 1); NT-12 ficou reduzido ao item 16.
Descartado: NT-16 (algoritmo do dígito de controle da referência do Accounts Office) é fonte oficial a localizar por nós; F-01 (credenciais no XML, High), RF-02 (FPS depois do payday), F-02 (Payroll ID changed), F-03/F-04 (centavos), F-05 a F-08 (contracheque, arquivos de teste) são Implementation/Dev.

---

## Bloco de prova

Pedido -> resposta: seção por pessoa, tabela por pacote com ID, pergunta fechada em inglês, motivo em pt-BR e fonte com aba!célula, mais rascunho existente, recebido e descartado. Sem dados pessoais de empregados.

Arquivos lidos (maior versão usada; abertos com openpyxl `read_only=True, data_only=True`):
- Norway/Henkel Norway - 2026-09/02 Validation: NO_HenkelNorway_2026-09_Validation.xlsx (única versão); followups.md; 01 Received/received.txt.
- Denmark/Sherwin Williams Denmark - 2026-09: DK_SherwinWilliams_2026-09_Validation.xlsx (única); followups.md; received.txt.
- Denmark/KGS Fire & Security Denmark - 2026-09: DK_KGSFireSecurity_2026-09_Validation.xlsx (única); followups.md; received.txt.
- Netherlands/Quest Software - 2026-09: NL_Quest_2026-09_Validation_v1.2.xlsx (existem base, v1.1, v1.2); followups.md; received.txt.
- Netherlands/Sherwin Williams - 2026-09: NL_SherwinWilliams_2026-09_Validation_v1.1.xlsx (existem base e v1.1); followups.md; received.txt.
- Netherlands/Excerpta Medica - 2026-09: NL_Excerpta_2026-09_Validation_v1.2.xlsx (existem base, v1.1, v1.2); followups.md; received.txt.
- Sweden/Quest Software - 2026-09 (One Identity): SE_OneIdentitySweden_2026-09_Validation.xlsx (única); followups.md; received.txt.
- Kazakhstan/Mastercard - 2026-10: KZ_Mastercard_2026-10_Validation_v1.1.xlsx (existem base e v1.1; a base foi lida só para a contagem de NT); followups.md; received.txt.
- Ukraine/Altium - 2026-08: UA_Altium_2026-08_Validation.xlsx (única); sem followups.md; received.txt.
- Ukraine/Altium - 2026-09: UA_Altium_2026-09_Validation.xlsx (única); followups.md; received.txt.
- United Kingdom/McDermott UK - 2026-09: UK_McDermott_2026-09_Validation.xlsx (única, datada de 07-Oct); UK_McDermott_2026-09_Audit_Report.docx (16-Oct, lido para saber o que mudou depois); sem followups.md; received.txt.
- Acompanhamento_Internal_Certification.xlsx: abas Painel, Achados (linhas 44, 83 a 86 conferidas), Ações (C-01 a C-18).
- `_projetos/fluxo-entregas-marko/dados/monday_12paises.md` (Primary SBC por país; DK = Deepak Prakash Pardeshi).

Contagem de Not tested conferida contra o Painel:

| Pacote | Painel | Aba Not Tested da maior versão | Resultado |
|---|---|---|---|
| NO-HENKEL | 4 | 4 (NT-01 a NT-04) | confere |
| DK-SHERWIN | 2 | 2 | confere |
| DK-KGS | 4 | 4 (NT-01 a NT-04; no Coverage são 1 Not tested + 1 Out of scope) | confere pela aba |
| NL-QUEST | 5 | 5 (NT-01, 02, 03, 05, 06) em v1.2 | confere |
| NL-SHERWIN | 5 | 5 (NT-01, 02, 03, 05, 07) em v1.1 | confere |
| NL-EXCERPTA | 5 | 5 (NT-01, 02, 03, 05, 07) em v1.2 | confere |
| SE-ONEID | 6 | 6 (NT-01 a NT-06; no Coverage são 2) | confere pela aba |
| KZ-MASTERCARD | 5 | 4 em v1.1 (NT-02 a NT-05); v1.0 tinha 5 | diverge: Painel ainda mostra a v1.0 (NT-01 foi fechado em 19-10) |
| UA-ALTIUM-08 | 12 | 14 linhas na aba (10 no Coverage como Not tested, mais 4 itens NT-*); 12 = 10 Not tested + 2 Out of scope do Coverage | diverge: 14 na aba x 12 no Painel |
| UK-MCDERMOTT | 17 | 17 (NT-01 a NT-17); no Coverage são 4 Not tested + 2 Out of scope | confere pela aba |
| UA-ALTIUM-09 | 7 | 7 | confere |

Outras divergências:
- Painel (colunas Pass e Finding) está defasado em NL-QUEST (60/9 no Painel contra 57/8 na v1.2) e em NL-SHERWIN/NL-EXCERPTA/KZ; não afeta as perguntas.
- Planilha do UK é de 07-Oct e ainda diz "não recebido" para NT-01 e NT-02; o `received.txt` e o Audit Report de 16-Oct mostram que chegaram em 09-Oct. Tratei NT-01 como fechado e NT-02 como reduzido.
- UA-08: o `received.txt` diz "recibo do 1-PV/estatística e Д1 de julho ainda não recebidos", mas a planilha pede também o recibo No.1 do relatório unificado e só o No.2 está nos arquivos; o item 2 de 6.1 precisa conferir 01 Received antes de enviar.
- Dinamarca: o Painel e os pacotes citam Rakshitha; o BAU Master (29/10) indica Deepak Prakash Pardeshi como Primary SBC. Decisão do usuário sobre a quem enviar.
- Nos rascunhos existentes (NL Sherwin, SE) há IDs ou nome de empregado; trocar por "N employees" ao enviar (regra 3 do cérebro).
- Contagem de linhas por pacote (conferida contra as tabelas): NO 8, DK-S 3, DK-KGS 4, NL-Q 7, NL-S 6, NL-E 5, SE 7, KZ 7, UA-08 24, UA-09 11, UK 23 = 105.

Confiança: 85%. Alta (95%) para identificação e texto dos itens Not tested e dos achados, que foram lidos direto das células. Menos certa (70%) em: (a) classificar o que "depende da SBC" em achados Observation (julgamento meu); (b) se o recibo No.1 do UA-08 já está em 01 Received; (c) se o cadastro do UK de 09-Oct já cobre mais do NT-02 do que o Audit Report afirma. Nada foi enviado nem gravado fora deste arquivo.
