# HRBS-15941 — Taiwan / British Council: subsídio de creche pago pelo empregador (1×/ano via payroll)

> Análise só leitura, feita em 2026-10-23 pela janela Suporte (subagente). Nada foi postado, enviado ou alterado no Drive. Rascunho para o usuário decidir.

## Metadados
| Campo | Valor |
|---|---|
| Ticket | [HRBS-15941](https://youtrack.hrblizz.dev/issue/HRBS-15941) — "Taiwan childcare subsidy execution and application" |
| Estado | In Progress · Question / Inquiry · Medium · Production · Live/BAU |
| Cliente / entidade | British Council (Taiwan) Limited (REF-889) |
| Reporter | Merlin Raja (mraja) · Assignee: wgomes (veio da fila da Shruti/skamble) |
| Criado / atualizado | 2026-10-13 / 2026-10-22 |
| Fonte do ticket | `raw/tickets/api/2026-10-23-ex-skamble/HRBS-15941.md`; anexo `raw/tickets/api/anexos/HRBS-15941/20261020-0745 - image.png` |
| Artefatos lidos | `Taiwan WTC V2.8.xlsx` (md5 6082ad8b71da…), `Taiwan Data Dictionary V3.3.xlsx` (d7f1c7504ab5…), `Country SOP Taiwan 1.1.txt` (c32b1f1d5ece…), `Taiwan Tax Report Spec.xlsx` (d1928c7f401e…), `TW Payslip Specification.xlsx` (c92ecae4d5c5…), `SR-108-SNHI-doc-txt-bonus.txt` — todos em `raw/docs/drive-exports/2026-10-23/` |
| Hub / correções | Não existe `paises/Taiwan.md`. `correcoes.md`: nada sobre Taiwan, creche ou welfare committee. |
| Skill | `mercans-compliance-workflow` carregada. Não há `payroll-compliance-taiwan`. |

## O que foi pedido a nós
Último comentário com pedido: Archit Naik (20/10 07:45) à Manju, que repassou à Shruti (pela janela geral; isso não aparece no ticket). Agora é nosso. Quatro pontos:
1. **Tributação:** o subsídio de creche pago pelo empregador pode ser não tributável? Qual a base legal? Mesmo isento, precisa ir em algum reporte anual?
2. **Seguros:** entra na remuneração de Labour Insurance (LI), Employment Insurance (EI), NHI (e outras, como Labour Pension)? Afeta a faixa de insured salary ou exige ajuste/reporte? Se ficar fora, qual a base legal?
3. **Pagamento único anual:** há implicação estatutária ou de payroll?
4. **Melhor prática:** processar no payroll ou fora? (Na pergunta original do cliente também: o que a Mercans precisa, setup, lead time, se a Mercans gerencia o pagamento e o "refund application", e como aparece no holerite e nos relatórios.)

A call com o cliente era em 20/10. Ninguém respondeu ainda.

## Histórico do ticket
| Data (UTC) | Quem | O quê |
|---|---|---|
| 13/10 11:19 | Merlin Raja | Abre o ticket com a pergunta do cliente (4 blocos: setup, tributação, seguros, requisitos de processamento). Proposta: pagar 1×/ano. |
| 20/10 07:23 | Merlin | Cobra o Archit e pede que mande ao compliance research. |
| 20/10 07:45 | Archit | Resume em 4 perguntas para a Manju (tributação, seguros, frequência anual, melhor prática) e pede base legal. Anexa `image.png`. |
| 22/10 | (interno) | Atualização; ticket passa para wgomes. |

O anexo `image.png` **não tem relação com o ticket**: é um e-mail interno (uma pessoa confirma ao Archit que assume dois outros clientes). Não usar.

## O que nossos artefatos dizem

**WTC V2.8** (aba `WTC` = `Wage Type Catalogue`; colunas: Tax Code, Calculation Type, Occurrence, Table Tax - Resident, Non-Resident Taxability, One time tax, Severance Tax, Subject to Old Pension, Subject to EWF, YTD Load):
- **Não existe wage type de creche, de child allowance ou de subsídio de educação infantil.** A busca por child/care/nursery/kinder/family/托/育/幼 não acha nada.
- Mais perto: `62700 Education Allowance` (e 62701, 62720–62741 Education and Schooling Allowance 2–4): Earning, Pro Rata, **Recurring**, Table Tax = Yes, NR = Yes, One time tax = No. É uma allowance mensal tributável e não serve para um pagamento único anual.
- Pagamento não mensal tributado à parte: a série `6221x Bonus (Profit Sharing)` e `6222x Bonuses (Discretionary or One-Time)` usa Table Tax = No e **One time tax = Yes** (os 5% de "variable income" da SOP).
- **O WTC não tem colunas de LI/EI/NHI/LP nem de SNHI.** LI/EI/NHI/LP/OAI saem de **grade** informada no HR (`$hr.li_grade`, `$hr.ei_grade`, `$hr.nhi_grade`, `$hr.new_pension_grade`, `$hr.oai_grade` no DD V3.3). A SOP diz isso: "The Mercans system adopts the Type 2 calculation method. Therefore, users must manually select the appropriate insurance band". Então um pagamento avulso **não muda a faixa automaticamente**.
- SNHI de bônus do empregado: `58009 Taxable Gross Additional Monthly`, que diz "It is sum of 6222% series and 6221% Series", `58132 SNHI Interim Base 4 Times`, `58133 … YTM`, `58558 SNHI Base`. As fórmulas de 58558/58132 **não estão no export** (coluna Formula vazia nessas linhas). Pela descrição, se o subsídio for posto na série 6221x/6222x, ele entra na base do SNHI de bônus. Isso estaria errado (ver Fonte primária, NHI).
- SNHI do empregador (`2568 SNHI Contribution ER`): sem fórmula no export. Não dá para confirmar se a base é "salário total (formato 50) −投保金額", como diz a lei (art. 34).
- `Subject to EWF` / DD `EWF Applicability` (`$legal_entity_hr.ewf_applicability`): o sistema já trata o desconto para o Employee Welfare Fund. Não sabemos se a entidade da BC tem welfare committee.

**Tax Report Spec**: Income Format só **50** (salário) e **93** (rescisão). "Total Payment by ER" = `58008 + 58009 + 62200:62209`. **Não há formato de "其他所得" (outros rendimentos)**. Um pagamento feito pelo welfare committee não caberia nesse relatório, e nem deveria, porque quem declara é o comitê (ver abaixo).

**Payslip Specification**: a seção Earnings lista cada pay element pelo nome (`62100:62103+62106:62999+65500:65859+79401:79450`). Um WT novo na faixa 62xxx aparece sozinho como linha própria.

**SOP Taiwan 1.1**: variable income com 5% quando "taxable variable income reaches 88,501 (in the year 2025)". Para 2026 o valor é 90,501 (ver Fonte). SNHI de bônus: "the total amount of the year that exceeds 4 times the monthly insured amount".

## Fonte primária
Cópias locais em `raw/docs/oficiais/TW/` (prefixo `2026-10-23-`). O site `law.moj.gov.tw` estava inacessível daqui (timeout em curl, WebFetch e Chrome). As leis foram lidas na **cópia do Wayback Machine** da própria página do MOJ (data do snapshot no nome do arquivo e abaixo). A vigência foi conferida pela linha "修正日期" de cada página.

### Tributação (Income Tax Act 所得稅法, alterado em 2026-09-11 [民國115年09月11日]; snapshot 2026-10-18)
- **Art. 14(1), Categoria 3 (薪資所得), item 4:** 「第一款薪資收入包括：薪金、俸給、工資、津貼、歲費、獎金、紅利及**各種補助費**。但為雇主之目的，執行職務而支領之差旅費、日支費及加班費不超過規定標準者，及依第四條規定免稅之項目，不在此限。」
  Tradução: a renda salarial inclui salário, ordenado, allowances, bônus, gratificações e **todo tipo de subsídio**. As únicas exceções são viagens/diárias/hora extra dentro do padrão e os itens isentos pelo art. 4.
- **Art. 4(1):** a lista de isenções **não tem subsídio de creche ou de cuidado infantil pago pelo empregador**. O item 17 isenta doação (贈與), mas tem a ressalva 「但取自營利事業贈與之財產，不在此限」 (não vale para doação vinda de empresa). O MOF isentou o subsídio de creche **pago pelo governo** municipal como "doação do governo" (台財稅字第09700315650號, 2008-06-30: 「核屬政府之贈與，可依所得稅法第4條第1項第17款規定，免納所得稅」). Isso é o oposto do caso de um empregador pagando.
- **Art. 17 (dedução do contribuinte, não do empregador):** 「6.幼兒學前特別扣除：自中華民國一百十三年一月一日起，納稅義務人六歲以下之子女，第一名子女每年扣除十五萬元，第二名及以上子女每人每年扣除二十二萬五千元。」 É uma dedução especial para pré-escolar na declaração anual do empregado, a partir de 2024-01-01. Não torna isento o subsídio do empregador.
- **Retenção:** Regulamento de Retenção sobre Salário (薪資所得扣繳辦法, alterado em 2024-12-31), art. 6: 「兼職所得及非每月給付之薪資，扣繳義務人按給付額扣取百分之五」 (salário não mensal: 5% sobre o valor pago). Art. 7: dispensa se 「每次給付金額未達薪資所得扣繳稅額表無配偶及受扶養親屬者之起扣點」, mas 「前二項薪資，扣繳義務人應依本法第八十九條第三項規定列單申報」 (mesmo sem retenção, o empregador declara). Portal tributário do MOF, Q&A 1506 (atualizado em 2026-04-10): limite de 2026 (115年度) = **NT$90,501**.
- **Reporte anual:** Art. 92 (扣繳憑單, até 31/01, com retenção) e art. 89(3) (免扣繳憑單, rendimentos não retidos, até o fim de janeiro, com entrega ao contribuinte até 10/02).
- **Se for pago pelo Employee Welfare Committee (職工福利委員會):**
  - MOF 台財稅第38505號 (1978-12-26; base MOF law-out, atualizada em 2026-09-22): o subsídio pago por comitê constituído pelo 職工福利金條例 e aprovado 「應屬來自另一團體之所得，與本機關發給之補助不同，可不列入本機關薪資所得扣繳」 (é renda vinda de outra entidade, não entra na retenção salarial do empregador). O beneficiário 「將所領各項補助費，列入其他所得申報」 (declara como "outros rendimentos").
  - Portal MOF Q&A 1156 (atualizado em 2026-04-10, citando 財政部72年2月2日台財稅第30794號函): 「…都算是受領人的其他所得，應該要合併綜合所得申報，給付時不用扣繳，但要由職工福利委員會依照所得稅法第89條第3項的規定…申報免扣繳憑單」.
  - Ou seja: **também é tributável** (Categoria 10 「其他所得」, art. 14), só que **sem retenção na fonte**, e quem declara é o **comitê**, em 免扣繳憑單. Código de formato "91": ⚠️ sem fonte primária lida.

### Seguros
- **Labor Standards Act (勞動基準法, alterado em 2024-07-31), art. 2(3):** 「工資：指勞工因工作而獲得之報酬；包括工資、薪金及按計時、計日、計月、計件以現金或實物等方式給付之獎金、津貼及其他任何名義之經常性給與均屬之。」 (salário = remuneração pelo trabalho, inclusive qualquer pagamento habitual, com qualquer nome.)
- **Regulamento da LSA (勞動基準法施行細則), art. 10** (snapshot MOJ de 2025-09-19; o texto é idêntico à cópia MOL já baixada na pasta, `2026-10-23-payslip-LSA-enforcement-rules-mol.html`): 「本法第二條第三款所稱之其他任何名義之經常性給與係指左列各款以外之給與。…二、獎金：指年終獎金…及其他非經常性獎金。…四、醫療補助費、勞工及其子女教育補助費。…六、婚喪喜慶由雇主致送之賀禮、慰問金或奠儀等。」 (lista o que não é pagamento habitual, entre eles subsídio médico e subsídio de educação do empregado e dos filhos.) Creche não aparece com esse nome (ver Lacunas).
- **Labour Insurance Act (勞工保險條例, alterado em 2026-01-21), art. 14:** 「月投保薪資，係指由投保單位按被保險人之月薪資總額，依投保薪資分級表之規定，向保險人申報之薪資」 (o insured salary sai do total mensal de salário). §2: a faixa só é ajustada quando o salário muda (fev–jul → avisar até o fim de agosto; ago–jan → até o fim de fevereiro).
- **Regulamento da LI (勞工保險條例施行細則, alterado em 2025-01-06), art. 27:** 「本條例第十四條第一項所稱月薪資總額，以勞動基準法第二條第三款規定之工資為準」.
- **BLI, interpretações sobre insured salary** (`bli.gov.tw/0022930.html`, atualizada em 2025-12-31): ordem do CLA 95年10月26日勞保2字第0950114071號令, em vigor desde 2006-11-01: 「至於勞動基準法施行細則第10條規定之獎金，倘係雇主所為非經常性之給與，或單方目的且給付具有勉勵、恩惠性質之給與，則不計入月薪資總額。另符合『勞務對價』性質之工資，不論其名稱為何，均計入月薪資總額申報勞保投保薪資。」 (pagamento não habitual, ou unilateral e de caráter benevolente, fica fora do total mensal; o que for contraprestação do trabalho entra, com qualquer nome.) Também o 書函 勞動2字第0940051013號 (2005): pagamento 「具有勉勵、恩惠性質之給與，即非為勞工之工作給付之對價…得不列入工資範圍之內」.
- **Employment Insurance Act (就業保險法, alterado em 2022-01-12), art. 40:** 月投保薪資 e ajustes 「準用勞工保險條例及其相關規定辦理」 (seguem as regras da LI).
- **Labor Pension Act (勞工退休金條例, alterado em 2019-05-15), art. 3:** 工資 「依勞動基準法第二條規定」. **Art. 14:** contribuição 「不得低於勞工每月工資百分之六」, por tabela de 月提繳工資.
- **NHI Act (全民健康保險法, alterado em 2023-06-28):**
  - Art. 20(1)(1): empregado 「以其薪資所得為投保金額」.
  - Regulamento do NHI (施行細則, alterado em 2025-10-20), art. 46(2)(2): 「應以合於勞動基準法規定之工資計算其投保金額」 (insured amount calculado sobre o salário no sentido da LSA).
  - **Art. 31(1)(1):** SNHI do empregado sobre 「所屬投保單位給付全年累計逾當月投保金額四倍部分之獎金」 (bônus acumulado no ano acima de 4× o insured amount).
  - **Regulamento do SNHI (全民健康保險扣取及繳納補充保險費辦法, alterado em 2024-03-20), art. 3(1)(1):** 「獎金：符合所得稅法第十四條第一項第三類規定應納入薪資收入項目，且未列入投保金額計算之**具獎勵性質**之各項給予，如年終獎金、節金、紅利等。」 (só conta como bônus o que tem caráter de **recompensa**.)
  - **Art. 34:** o empregador paga SNHI próprio quando 「每月支付之薪資所得總額逾其受僱者當月投保金額總額」 (salário total pago no mês acima da soma dos insured amounts).
- **NHIA (健保署), Q&A** `nhi.gov.tw/ch/cp-2962-46747-3150-1.html` (lida no navegador em 2026-10-23): 「投保單位給付所屬員工之『教育補助費』屬補助費性質，非獎勵性質獎金，不需扣繳補充保險費。」 (subsídio de educação é subsídio, não bônus de recompensa, e não sofre SNHI do empregado.)
- **NHIA, folheto "如何正確申報健保投保金額" (Divisão Sul, versão 115.1, 2026)**, `2026-10-23-SNHI-nhia-insured-amount-and-supplementary-premium-115v1.pdf`, baixado por outra janela. Tabela: 「各項補助費(註4)」 → entra no insured amount: **X** · entra na base do SNHI do empregador: **O** · entra na base do SNHI de bônus: **X**. Nota 4: 勞動基準法施行細則§10. O exemplo usa 子女教育補助費 10,000 assim e calcula 「(薪資所得總額−投保金額總額)×2.11%」 para 115/5. O resumo NHIA 115 (`2026-10-23-SNHI-nhia-115-supplementary-premium-summary.pdf`) diz que a base do empregador inclui todo rendimento de formato 50/79A/79B, 「不論發放性質：獎勵、補助」 (qualquer que seja a natureza, recompensa ou subsídio).

### Programa do governo (MOL)
- **Gender Equality in Employment Act (性別平等工作法, alterado em 2023-08-16), art. 23:** empregador com **100 ou mais empregados** deve oferecer 「托兒設施或適當之托兒措施」, e 「主管機關…應給予經費補助」 (o governo subsidia).
- **MOL, comunicado 88331 (2026-03-04, regime novo a partir de 2026-05-01)** sobre a alteração do 「哺集乳室與托兒設施措施設置標準及經費補助辦法」: 「取消育兒補貼補助須以員工子女送托托兒服務機構之要件」 (não precisa mais que a criança esteja em creche credenciada) e 「提高補助雇主提供每位員工育兒補貼之金額及比率，每人每年最高1萬元」 (até NT$10.000 por empregado/ano).
- **MOL, comunicado 90847 (2026-06-01):** 「育兒補貼：每年最高補助100萬元…未滿100人企業，補助實支數70%，100-499人企業，補助實支數60%，500人以上企業，補助實支數50%」. Pedido em `childcare.mol.gov.tw`. Mesmo comunicado: o Executive Yuan aprovou em 2026-05-28 o novo art. 23-1 do 性平法 (dedução de 200% no IR da empresa sobre gastos com creche). **Ainda é projeto de lei.**
- **Medida de Taipé (臺北市補助雇主辦理哺集乳室與托兒設施或措施經費實施辦法, alterada em 2025-03-04, anterior ao regime de maio/2026):** art. 3 (filhos menores de 12 anos) e art. 8(3), documentos para o 托兒津貼: 「受僱者子女托兒名冊」, 「雇主補助托兒津貼之證明文件、資料」. Ou seja, o empregador prova o pagamento, e o registro de payroll serve como prova.
- Isso explica o "refund application" da pergunta do cliente: é o **pedido de reembolso parcial do empregador ao MOL ou à secretaria local do trabalho**. Não é uma obrigação de payroll.

## Veredito por pergunta

**(1) Tributação: tributável. Não há base para tratar como isento.**
- **Pago pelo empregador (via payroll):** é 薪資所得 (art. 14(1) Cat. 3 item 4, "各種補助費"), e nenhum item do art. 4 se aplica. Como é pago 1×/ano, é "salário não mensal": retenção de **5%** (residente) se o pagamento chegar a **NT$90.501 (2026)**; abaixo disso, sem retenção (薪資所得扣繳辦法 arts. 6–7). Em qualquer caso, **entra na declaração anual de rendimentos salariais (formato 50)** até 31/01 do ano seguinte (art. 92 / art. 89(3)). Não residente: retenção sobre cada pagamento pela regra de não residente (⚠️ alíquotas 6%/18% só pela SOP; fonte primária não lida nesta análise).
- **Pago pelo Employee Welfare Committee** (comitê constituído pelo 職工福利金條例 e aprovado): é **"其他所得"** do empregado, **sem retenção**. O **comitê** declara em 免扣繳憑單 (art. 89(3); MOF 38505; Q&A 1156/30794). Continua tributável na declaração anual do empregado. Não é isenção.
- O empregado pode usar à parte a dedução 幼兒學前特別扣除 (filho de até 6 anos) na própria declaração (art. 17). Isso não muda o tratamento do subsídio.

**(2) Seguros: no formato proposto (1×/ano, valor discricionário de bem-estar), fica fora da base de LI/EI/LP e do insured amount do NHI. Não muda a faixa nem exige ajuste.**
- LI/EI/LP/NHI usam o conceito de 工資 da LSA (LI Act art. 14 + regulamento art. 27; EI Act art. 40; LPA arts. 3 e 14; NHI regulamento art. 46). Pagamento não habitual, unilateral e de caráter benevolente não entra (LSA art. 2(3) + regulamento art. 10; CLA 勞保2字第0950114071號令). O NHIA classifica 「各項補助費」 como **fora** do insured amount.
- Sem mudança no total mensal de salário → **sem 2-3/1-5 Adjust Insurance Declare**. A faixa só muda quando o salário muda (LI art. 14(2)).
- **Ressalva:** a classificação depende dos fatos. Se o subsídio for fixo e mensal, prometido em contrato, ou ligado a desempenho ou presença, vira 工資 e entra na faixa. Ver o 書函 0940051013: 「依其發給之性質、目的、方式，依個案事實認定」 (decide-se caso a caso).
- **NHI tem dois efeitos, e um deles existe:**
  - SNHI do **empregado** (bônus > 4× insured amount): **não se aplica**. Subsídio não é 「具獎勵性質」 (regulamento SNHI art. 3(1)(1); Q&A NHIA do 教育補助費; folheto NHIA 115.1: X).
  - SNHI do **empregador** (art. 34, 2,11% sobre "salário total pago no mês − soma dos insured amounts"): **se aplica** quando pago como salário (formato 50). No mês do pagamento, o subsídio aumenta a base e gera um custo de 2,11% para o empregador (folheto NHIA 115.1: O).
  - Pago pelo **welfare committee** ("其他所得", não é salário do empregador): não entra no art. 34. Também não está entre as 6 categorias do art. 31. **Sem SNHI** (conclusão a partir do texto dos arts. 31/34; não há Q&A do NHIA específica lida).
- OAI (職業災害保險): ⚠️ sem fonte. A lei do OAI não foi lida. Em princípio usa a mesma base (insured salary), mas não foi conferido.

**(3) Pagamento único anual: favorece a classificação como "não habitual" (fora dos seguros) e faz a retenção seguir a regra de "não mensal".**
- Tributação: 5% sobre o valor pago, se ≥ NT$90.501 (2026); sem retenção abaixo disso; entra no formato 50 anual.
- Seguros: sem mudança de faixa (ver item 2).
- NHI: SNHI de bônus do empregado **não se aplica** (não é bônus de recompensa, então a regra de 4× não entra). Só existe o SNHI do empregador (art. 34) no mês do pagamento.
- Reembolso do MOL: o teto é **por ano** (NT$10.000/empregado). Um pagamento anual combina com o ciclo do pedido.

**(4) No payroll ou fora? Os dois caminhos são legais e o resultado fiscal muda pouco. A escolha depende de quem paga.**
- **Pagar pelo empregador → no payroll** é o caminho simples e auditável. Salário não mensal tributável, retenção correta, reporte anual automático (formato 50), linha própria no holerite, e o registro de payroll serve de prova de pagamento para o pedido ao MOL. Custo extra: SNHI do empregador (2,11%) no mês.
- **Pagar pelo welfare committee → fora do payroll** do empregador. O comitê é outra entidade, sem retenção, e declara em 免扣繳憑單. Nosso Tax Report só tem os formatos 50/93 e não deve levar isso. Só faz sentido se a BC tiver comitê constituído e aprovado e usar o 福利金.
- Para processar no payroll: um WT dedicado (ver O que precisa ser feito) e, por pagamento, os dados: empregado (ID), valor aprovado, mês/data de pagamento, confirmação de que é discricionário/anual (não contratual) e, para o pedido ao MOL, o cadastro do filho (nome/idade/vínculo), mantido pelo cliente. **Lead time, se a Mercans "gerencia" o pedido ao MOL e o custo do serviço: fora do nosso escopo** (Operations/Implementation e Product). O pedido de subsídio é do empregador junto ao MOL ou à secretaria local do trabalho.

## Achados fora do pedido
1. **WTC não tem WT de creche/child allowance**, e o mais próximo (`62700 Education Allowance`) é mensal e recorrente. Usar a série 6221x/6222x levaria o valor para a base do SNHI de bônus do empregado (58009 = "6222% + 6221%"), o que estaria errado pelo NHIA.
2. **Não dá para conferir pelo export a base do SNHI do empregador (2568) nem as fórmulas de 58558/58132**: a coluna Formula está vazia nessas linhas. É preciso confirmar com o Dev que a base do art. 34 inclui todo formato 50, inclusive subsídios.
3. **SOP Taiwan 1.1** ainda traz o limite de 2025 (88,501). Em 2026 é 90,501 (Q&A 1506 do MOF). Também diz que o Welfare Fund "may be offered… such as subsidies", mas não explica que o subsídio pago pelo comitê é "其他所得", sem retenção e declarado pelo comitê.
4. **Tax Report Spec** só cobre 50/93. Não há caminho para "其他所得". Hoje está certo para o escopo do empregador; fica registrado para quando algum cliente quiser pagar via comitê pelo sistema.
5. Taiwan **não tem hub** (`paises/Taiwan.md`). Hoje há 4 notas Taiwan neste dia (SR-105/106/107 e esta).
6. Projeto do novo art. 23-1 do 性平法 (dedução de 200% no IR da empresa sobre gastos com creche) aprovado pelo Executive Yuan em 2026-05-28. Acompanhar; é IR corporativo, fora da folha.
7. O anexo `image.png` do ticket é de outro assunto (troca de responsável por outros clientes). Não deve ir no comentário.

## Rascunho de resposta (EN)
> Para o Archit/Merlin repassarem. Não postado.

Hi @anaik,

Please find below our position for British Council (Taiwan) on the employer-paid childcare subsidy.

**1. Tax treatment: taxable**
- Paid by the employer, the subsidy is salary income. Income Tax Act art. 14(1), Category 3, item 4: salary income includes "各種補助費" (all kinds of subsidies). None of the art. 4 exemptions applies. The government childcare subsidy is exempt only because it is a government gift (MOF ruling 09700315650, under art. 4(1)(17)); that exemption does not cover payments from the employer.
- As a once-a-year payment, it is "non-monthly salary": 5% withholding for residents (Withholding Regulations for Salary Income, art. 6). No withholding if the payment is below NT$90,501 (2026 threshold; art. 7, MOF tax portal Q&A 1506). Either way, it must be reported in the annual salary withholding statement (income format 50) by 31 January of the following year (Income Tax Act arts. 89(3) and 92).
- If it is paid by a duly established Employee Welfare Committee (職工福利委員會) from welfare funds instead, it is the employee's "other income" (其他所得). There is no withholding, and the Committee (not the employer) files the non-withholding statement (MOF rulings 台財稅第38505號 and 台財稅第30794號; Income Tax Act art. 89(3)). It is still taxable in the employee's annual return.

**2. Statutory insurance: excluded, no bracket change**
- LI, EI, Labour Pension and the NHI insured amount are based on "wages" under Labor Standards Act art. 2(3). See Labour Insurance Act art. 14 and Enforcement Rules art. 27; Employment Insurance Act art. 40; Labor Pension Act arts. 3 and 14; NHI Enforcement Rules art. 46.
- A one-off, discretionary welfare payment is not a recurring wage. It does not count towards the monthly insured salary (LSA Enforcement Rules art. 10; Council of Labor Affairs Order 勞保2字第0950114071號). The NHIA treats "各項補助費" (subsidies) as outside the NHI insured amount (NHIA South Division guide "如何正確申報健保投保金額", v115.1).
- So it does not change the employee's insured salary bracket and no adjustment filing is needed. This holds only while the subsidy stays discretionary and annual. If it becomes a fixed monthly or contractual entitlement, it becomes a wage and must go into the bracket.

**3. One-off annual payment**
- NHI employee supplementary premium (bonus above 4× insured amount, NHI Act art. 31(1)(1)) does not apply. Only incentive-type payments count as "bonus" (Regulations on Supplementary Premiums art. 3(1)(1)), and the NHIA confirms that subsidies are not incentive bonuses and are not subject to it (NHIA Q&A on education subsidy).
- The employer supplementary premium (NHI Act art. 34: 2.11% on monthly salary paid above total insured amounts) does apply in the month of payment when the subsidy is paid as salary.
- Tax follows the non-monthly rule in point 1.

**4. Payroll vs outside payroll**
- If the employer pays it, processing it through payroll as a separate one-off earning gives the correct withholding, annual reporting and an audit trail. That trail can also serve as proof of payment for the Ministry of Labor employer childcare subsidy (育兒補貼: up to NT$10,000 per employee per year, 50–70% of actual cost depending on company size; MOL announcements of 4 March and 1 June 2026). The MOL subsidy is applied for by the employer at childcare.mol.gov.tw.
- If it is paid by the Welfare Committee, it should stay outside the employer's payroll and tax reporting.
- Per payment we would need: employee ID, approved amount, payment month, and confirmation that the payment is discretionary/annual. The child details for the MOL application stay with the client.
- On the payslip, it would show as its own earning line.
- Set-up lead time and whether Mercans can manage the MOL application are for Operations to confirm.

Regards,

## O que precisa ser feito
- **Antes de responder:** o usuário confirma o tom e se a resposta vai para o Archit ou direto ao Merlin. Também decide se responde as perguntas operacionais (lead time, serviço de "refund application") ou deixa explicitamente para Operations (o rascunho deixa).
- **WTC Taiwan (se o cliente seguir pelo payroll):** criar WT dedicado, por exemplo `Childcare Subsidy` (育兒/托兒補助). Earning, Lump Sum, **Additional**. **Table Tax - Resident = No / One time tax = Yes** (5% não mensal), Non-Resident Taxability = Yes, Subject to Old Pension = No, Subject to EWF = No, YTD Load = Yes, Remark com a base legal. **Fora das bases de LI/EI/LP/NHI** (ficam na grade). **Fora da base do SNHI de bônus** (não pode cair em 58009/6221x/6222x). **Dentro da base do SNHI do empregador (art. 34)** e do gross do Tax Report formato 50. Faixa sugerida: 628xx–629xx livre, para cair no range Earnings do payslip. Mudança de WTC = V2.9 (colunas azuis nossas; Formula/config com o Dev).
- **Dev/Config:** confirmar as fórmulas de 58558/58132 (SNHI de bônus) e 2568 (SNHI ER). O WT novo precisa entrar no art. 34 e não no art. 31. O Tax Report "Total Payment by ER" precisa incluir o WT novo (hoje `58008 + 58009 + 62200:62209`).
- **SOP Taiwan:** atualizar o limite 2026 (90,501) e incluir uma linha sobre subsídio pago pelo welfare committee (fora do payroll, "其他所得").
- **Cérebro (com ok do usuário, pela janela própria):** criar `paises/Taiwan.md` e registrar esta decisão, com vigência e fonte.

## Lacunas
- **Creche × "子女教育補助費":** o art. 10(4) do regulamento da LSA e a Q&A do NHIA falam de "教育補助費" (subsídio de educação). Não achei interpretação do MOL ou do NHIA que cite **托兒/育兒補助** pelo nome. A conclusão de "fora da base" se apoia no critério geral (não habitual + benevolente: Ordem 0950114071) e no "各項補助費" do folheto NHIA. Se o cliente quiser certeza formal: consultar o BLI/NHIA ou um assessor local (Jhan Ye/ICE).
- **Fatos do cliente que mudam o veredito:** se o subsídio é contratual ou de política fixa, e qual o valor (passa ou não de NT$90.501); se há Employee Welfare Committee aprovado; número de empregados (≥100 → obrigação do 性平法 art. 23); cidade da entidade (a medida de Taipé foi usada só como exemplo de documentos).
- **Texto consolidado do 哺集乳室與托兒設施措施設置標準及經費補助辦法 alterado (2026):** não lido. A idade-limite (<12) e os documentos vêm da medida de Taipé de 2025 e de citação em comunicado do MOL. Os percentuais e tetos vêm dos comunicados do MOL de 2026-03-04 e 2026-06-01.
- **Não residente:** alíquotas 6%/18% só pela SOP. 各類所得扣繳率標準 não lido nesta análise.
- **OAI:** lei do 勞工職業災害保險及保護法 não lida.
- **Código de formato "91"** para "其他所得" no 免扣繳憑單: ⚠️ sem fonte primária.
- **Leis lidas via Wayback** (law.moj.gov.tw inacessível). Vigência conferida pela data de alteração no topo de cada página. O regulamento da LSA (art. 10) é do snapshot de 2025-09-19 e tem texto idêntico à cópia MOL baixada hoje por outra janela.
- **Fórmulas do WTC** (58558, 58132, 2568) não estão no export. A conclusão sobre a base do SNHI no sistema é só pela descrição.
- Não li: "Taiwan Payroll Regulation Guide 1.3" e "BC TWN5 Payroll_2024" no Drive (são `.gdoc`/`.gsheet`, não legíveis pelo disco).
