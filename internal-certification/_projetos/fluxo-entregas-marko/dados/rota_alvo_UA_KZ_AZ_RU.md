# Rota-alvo das entregas de payroll: UA, KZ, AZ, RU (29/10/2026)

> Só a **rota-alvo** (o que a fonte oficial prevê). A rota de hoje (monday: "External Supplier"; KZ no 1C ZUP local) não foi provada aqui.
> Downloads: `C:\Users\instituto\Documents\brain-service\raw\docs\oficiais\<CC>\2026-10-29-canal\` (LEIA-ME.md em cada pasta). Os trechos abaixo foram conferidos nos arquivos baixados.
> Convenção: **[Verify]** = sem fonte oficial lida; não é afirmação.
> Pasta base UA = `raw\docs\oficiais\UA\`, KZ = `...\KZ\2026-10-29-canal\`, RU = `...\RU\2026-10-29-canal\`.

---

## UA — Ucrânia (ДПС)

**Entregas (todas dentro do mesmo documento):**
1. **Податковий розрахунок (J0500111 / F0500111), mensal**: ПДФО + військовий збір + ЄСВ (Order Мінфіну № 4/2015, redação do Наказ № 243 de 07.05.2026). Prazo: 20 dias corridos após o mês (п. 5). Não há 1-ПВ nem ЄСВ separados para ДПС.
2. **1-ПВ (Derzhstat)**: estatística, **fora de ДПС** (autoridade = Держстат); não é entrega fiscal; ver `UA\2026-10-09-1PV-*` e `2026-10-13-VERIFICACAO.md`. Não pesquisada aqui a rota de transmissão ([Verify]).

| Entrega | Canal oficial | API ou só portal/operador | Representante | Credencial | Autorização | Recibo | Mudanças 2026–27 | Fonte |
|---|---|---|---|---|---|---|---|---|
| J0500111 (ПДФО, ВЗ, ЄСВ) | Eletrônico (PK ст. 42, 49.3 "в", Order 4 п. 11); Електронний кабінет (ст. 42-1) | **Previsto API aberta (EDI)** no Електронний кабінет como princípio legal; programa gratuito da ДПС também permitido. Endpoint/шлюз concreto e se terceiro pode usar: **[Verify]** | "Особисто платником або **уповноваженою на це особою**" (49.3 "а"); o diretor define a lista de pessoas autorizadas a assinar, enviar e receber no кабінет (42.6) | КЕП (qualified e-signature) de cada pessoa autorizada; validade do certificado | **O diretor do contribuinte** define/altera os autorizados e seus poderes (42.6); fluxo para quando o certificado do diretor expira/é cancelado ou o diretor muda no ЄДР | Квитанція de aceite: a declaração conta como aceita com "квитанції про прийняття" em envio eletrônico (49.9.1). Estrutura de квитанція №1/№2: **[Verify]** (Наказ 557/2017 não obtido) | Formas v11 em vigor de 17.07.2026; uso a partir de 01.08.2026 para o período de julho/2026 (Наказ 243 e 284/2026) | PK ст. 42.6, 42-1.1, 49.3, 49.9.1; Order 4 (UA\2026-10-16-ZIR-DPS...docx) |

**Trechos literais (PK = `UA\2026-10-29-canal\PK-2755-17-st42.htm`; captura Wayback de zakon.rada.gov.ua, ver LEIA-ME):**
- PK 42.6: "Керівник платника податків визначає, змінює перелік уповноважених осіб платника податків, які наділяються правом підписання, подання, отримання ними документів та інформації через електронний кабінет від імені платника податків, та визначає їхні повноваження." → *O dirigente do contribuinte define e altera a lista de pessoas autorizadas a assinar, enviar e receber documentos pelo cabinet em nome do contribuinte, e define os poderes delas.*
- PK 42.6: "Електронний документообіг ... здійснюється ... без укладення відповідного договору." → *O documento eletrônico circula sem contrato específico.*
- PK 42-1.1: "інтеграції із системами, що використовуються платниками податків, - у відкритому, вільному доступі розміщуються API програмного інтерфейсу для електронного обміну даними (EDI - Electronic data interchange)" → *integração com os sistemas do contribuinte: APIs abertas para troca eletrônica (EDI).*
- PK 49.3: "Податкова декларація подається ... а) особисто платником податків або уповноваженою на це особою; ... в) засобами електронного зв'язку в електронній формі ..." → *entregue pelo contribuinte ou por pessoa autorizada, ou por meio eletrônico.*
- PK 49.3 (último parágrafo): "Єдиною підставою для неприйняття податкової декларації засобами електронного зв'язку в електронній формі є недійсність кваліфікованого електронного підпису ..." → *único motivo de recusa no envio eletrônico: assinatura qualificada inválida.*
- PK 49.9.1: "... або квитанції про прийняття податкової декларації у разі її подання засобами електронного зв'язку ..." → *considera-se aceita com o recibo de aceite no envio eletrônico.*
- Order 4 п. 11: "Розрахунок ЮО ... подається платником в один із таких способів: в електронній формі у порядку передбаченому статтею 42 Кодексу; ..." e "... може бути складений платником із використанням безкоштовного спеціалізованого програмного забезпечення, актуальні версії якого розміщені на офіційному вебпорталі ДПС." → *Enviado em forma eletrônica (art. 42), podendo usar programa gratuito da ДПС.*
- Order 4 п. 5: "Розрахунок ЮО подається протягом 20 календарних днів, що настають за останнім календарним днем звітного (податкового) місяця" → *prazo: 20 dias corridos após o mês.*
- Mudança 2026: `UA\2026-10-15-VERIFICACAO-J05-v11.md` (notícia da ДПС 14/07/2026: formas novas "набирають чинності 17 липня 2026 року"; naquele arquivo, lida pelo Chrome do usuário porque tax.gov.ua dá 403).

**[Verify] UA:** (a) existe шлюз/API **utilizável por software de folha de terceiro** (a lei prevê API; a especificação não foi lida); (b) um **provedor** pode ser autorizado como pessoa do 42.6 usando a própria КЕП (o texto fala de "уповноважені особи платника", não distingue interno de externo); (c) texto de **квитанція №1 / №2** (Наказ Мінфіну № 557/2017, Порядок обміну електронними документами; tax.gov.ua 403 e Wayback 429); (d) edição do PK da captura (2025) vs. vigente em 2026; (e) **1-ПВ** Derzhstat: canal.

---

## KZ — Cazaquistão (КГД)

**Entregas:**
1. **Форма 200.00**, trimestral, até o dia 15 do 2º mês após o trimestre: ИПН + социальный налог + **ОПВ, ОПВР/ОППВ (ЕНПФ), социальные отчисления (ГФСС/Social Insurance Fund), ВОСМС/ООСМС** — tudo numa só declaração (Anexos 200.01–200.06). Não há, na fonte lida, entrega separada ao ГФСС/ЕНПФ; ver [Verify].

| Entrega | Canal oficial | API ou só portal/operador | Representante | Credencial | Autorização | Recibo | Mudanças 2026–27 | Fonte |
|---|---|---|---|---|---|---|---|---|
| Форма 200.00 (ИПН, СН, ОПВ, СО, ОСМС) | Eletrônico por: веб-приложение; налоговое мобильное приложение; **внешние информационные системы, подключенные к ИС налогового органа** (НК ст. 115 п. 3). Веб-приложение = «Кабинет налогоплательщика» knp.kgd.gov.kz | **Legalmente previsto: sistemas externos conectados à ИС** (ст. 115 п.3 3)). Especificação do API (ИС СОНО/ИСНА) **[Verify]**: página do kgd.gov.kz mudou para portal.kgd.gov.kz e não foi lida | **Уполномоченный представитель** (НК ст. 38, 40): empresa = por **учредительные документы e/ou доверенность** (civil) ou por **documento eletrônico** do contribuinte no sistema do órgão (ст. 40 п.1, últ. parágrafo). "Оператор" na ст. 38 é o de недропользование, **não** é provedor de folha | ЭЦП do **funcionário** emitida em nome dele; o diretor pode "наделять полномочиями работника ... или назначенного им лица" (Цифровой кодекс ст. 62 п.6). Chave privada **não transferível** (ст. 51). Para um provedor de folha: **usar a ЭЦП de uma pessoa nomeada pelo diretor, com poderes** | Diretor (ou substituto) do cliente nomeia; ou documento eletrônico no sistema do órgão (НК ст. 40) | **Уведомление о принятии/непринятии** em forma eletrônica, enviado até 1 dia útil; data de apresentação = data de aceite no nó central (Правила п. 30 3)); status "Документ принят" (п. 51) | **Novo Налоговый кодекс e Приказ МФ № 695 (12.11.2025) em vigor desde 01.01.2026** (formas, Правила). Цифровой кодекс (09.01.2026) revogou o Закон 370-II da ЭЦП. ИС СОНО desligada em 01.05.2026 → ИСНА: **[Verify]** (só leitura de resumo de busca, não fonte) | НК K2500000214 ст. 38, 40, 114–115, 562; Приказ 695 (V2500037390) anexo 8 (explicação 200.00) e anexo 29 (Правила); Цифровой кодекс K2600000255 ст. 51, 61, 62 |

**Trechos literais (KZ\...):**
- НК ст. 115 п. 3: "Налоговая отчетность представляется в форме электронного документа посредством: 1) веб-приложения; 2) налогового мобильного приложения; 3) внешних информационных систем, подключенных к информационной системе налогового органа в соответствии с Законом Республики Казахстан "Об информатизации"." → *A declaração é enviada por web, app móvel ou sistemas externos conectados ao sistema do órgão.*
- НК ст. 38 п. 1: "Налогоплательщик (налоговый агент) вправе участвовать ... через: ... 2) уполномоченного представителя, в том числе оператора." (operador definido para недропользователей, ст. 3 п. 9 e ст. 41.) → *Pode atuar por representante autorizado.*
- НК ст. 40 п. 1 (2): "юридическим лицом ... – на основании учредительных документов и (или) доверенности, выданной в соответствии с гражданским законодательством ..." e "вправе определить уполномоченного представителя путем оформления электронного документа ... посредством объекта информатизации налогового органа, в котором указываются соответствующие полномочия представителя." → *Representante: por estatuto/procuração, ou documento eletrônico no sistema do órgão com os poderes.*
- НК ст. 562 п. 1: "Декларация по индивидуальному подоходному налогу и социальному налогу представляется ... ежеквартально не позднее 15 числа второго месяца, следующего за отчетным периодом." → *Trimestral, até dia 15 do 2º mês seguinte.*
- Приказ 695, анекс 8, п. 1: "...предназначена для исчисления суммы ... ИПН, социального налога, единого платежа, а также для исчисления, удержания (начисления) и перечисления сумм обязательных пенсионных взносов ... в единый накопительный пенсионный фонд (ЕНПФ), начисления и перечисления сумм социальных отчислений в Государственный фонд социального страхования ..., отчислений и (или) взносов на обязательное социальное медицинское страхование (ОСМС)." → *Um só formulário cobre IR, imposto social e contribuições ao ЕНПФ, ГФСС e ОСМС.*
- Правила п. 30 3): "дата принятия ФНО центральным узлом ИС, указанная в электронном уведомлении, направляемом в адрес налогоплательщика (налогового агента) в срок не позднее одного рабочего дня с момента принятия системой – при представлении в электронной форме." → *Data de entrega = data de aceite no nó central, informada em notificação eletrônica em até 1 dia útil.*
- Правила п. 31: "Подписание и заверение ФНО допускаются с использованием одноразовых паролей ..." → *Assinatura também permitida com senha única.*
- Правила п. 51: "ФНО признается представленной при статусе "Документ принят" по итогам ФЛК в ИС ОГД." → *Considera-se entregue com status "Documento aceito".*
- Правила п. 34: "налогоплательщик (налоговый агент) регистрируется в веб-приложении "Кабинет налогоплательщика" или ином объекте информатизации ОГД." → *Registro no cabinet.*
- Цифровой кодекс ст. 62 п. 6: "Руководитель юридического лица или лицо, его замещающее, вправе наделять полномочиями работника данного юридического лица или назначенного им лица на подписание электронных документов. При этом каждый работник использует сертификат ... полученный на свое имя ..." → *O diretor pode dar poderes a um funcionário ou a pessoa que ele indicar; cada um usa o certificado emitido em seu próprio nome.*
- Цифровой кодекс ст. 51 п. 3: "Передача закрытых ключей другим лицам, а также использование закрытых ключей другими лицами не допускаются." → *Chave privada não pode ser passada nem usada por outra pessoa.*

**[Verify] KZ:** (a) **API de recepção de ФНО** (chaves SONO_FNO_SEND / GET_STATUS, via шлюз эл. правительства) e a migração para ИСНА em 01.05.2026: aparece só em resumo de busca; páginas oficiais redirecionam para portal.kgd.gov.kz (não lidas); (b) se há **pagamento/registro separado** de ОПВ/СО/ОСМС (reporte vai em 200.00; pagamento via outros órgãos) e se o ЕНПФ/ГФСС exige carga própria; (c) o **mecanismo de delegação de direitos** no pki.gov.kz ("Управление правами") citado em buscas: só fonte de terceiro, não lida a oficial; (d) texto do Приказ 695 vigente pode ter sido alterado depois de 12.11.2025.

---

## AZ — Azerbaijão (Vergilər Nazirliyi / DSMF)

**Não obtive nenhuma fonte primária.** taxes.gov.az, e-taxes.gov.az, e-qanun.az, e-gov.az, dsmf.gov.az, president.az: sem resolução DNS/conexão desta máquina e do Chrome do usuário; Wayback 429. Nada foi baixado (`raw\docs\oficiais\AZ\` não foi criada para não deixar pasta vazia).

**Entregas que a fonte oficial deve prever (lista de trabalho, ainda sem prova):** relatório/declaração do imposto de renda retido na fonte sobre rendimento de trabalho assalariado + DSMF + seguro-desemprego + seguro médico obrigatório (Código Tributário art. 98 e seguintes, conforme resumo de busca; **não é fonte**). Frequência e prazo: **[Verify]**.

| Entrega | Canal oficial | API ou só portal/operador | Representante | Credencial | Autorização | Recibo | Mudanças 2026–27 | Fonte |
|---|---|---|---|---|---|---|---|---|
| Relatório "muzdlu işlə bağlı" (IR na fonte, DSMF, desemprego, ОСМС) | [Verify] (provável e-taxes.gov.az "Internet Vergi İdarəsi") | [Verify] | [Verify] | [Verify]. Um resumo de busca cita registro eletrônico por assinatura eletrônica avançada incl. ASAN imza (não é fonte) | [Verify] | [Verify] | [Verify] | Nenhuma lida |

**Como fechar:** o usuário abrir em navegador com acesso ao Azerbaijão (VPN) `https://www.taxes.gov.az/az/page/suallar-ve-cavablar` e o Código Tributário em e-qanun.az (art. 98, art. 16 e seguintes sobre representante/agent) e salvar em `raw\docs\oficiais\AZ\2026-10-29-canal\`; ou o time AZ da Mercans fornecer o SOP.

---

## RU — Rússia (ФНС / СФР)

**Entregas:**
1. **6-НДФЛ** (расчёт + справка о доходах), trimestral/anual: ст. 230 НК РФ.
2. **РСВ** (расчет по страховым взносам), trimestral: ст. 431 НК РФ (ФНС).
3. **Уведомление об исчисленных суммах** (КНД 1110355), por ст. 58 п. 9: НДФЛ duas vezes ao mês; sem uso se o РСВ coincide no prazo.
4. **ЕФС-1** (СФР): персонифицированный учёт + взносы НС/ПЗ; **СЗВ-ТД** (СФР).
5. (**Pagamento** via ЕНС; fora desta pesquisa.)

| Entrega | Canal oficial | API ou só portal/operador | Representante | Credencial | Autorização | Recibo | Mudanças 2026–27 | Fonte |
|---|---|---|---|---|---|---|---|---|
| 6-НДФЛ | Eletrônico por ТКС (ст. 230 п. 2); ≤ 9 pessoas pode ser em papel; ЛК налогоплательщика para estrangeiras (п. 6) | **Operador de ЭДО** (ТКС) ou ЛК; software de folha entrega via operador, não direto | Уполномоченный представитель (ст. 29) | **УКЭП do representante (física)** + **МЧД** desde 01.09.2024 | Dirigente assina МЧД com УКЭП da organização; formato приказ ФНС ЕД-7-26/648@; criação no serviço da ФНС | **Квитанция о приеме** ou уведомление об отказе, no próximo dia útil (Приказ ММВ-7-6/398@); ao entregar com representante, declaração indica documento de poderes (ст. 80) | Ст. 80 alterada pela ФЗ 26.06.2026 № 201-ФЗ (aplica-se a declarações entregues desde 26.07.2026): inclui entrega de informação sobre circunstâncias que excluem responsabilidade junto com a declaração | ст. 230, 80, 29; nalog.gov.ru |
| РСВ | Eletrônico por ТКС com УКЭП se > 10 pessoas (ст. 431 п. 10) | Operador de ЭДО (ст. 80 п. 5: lista de categorias via operador) | idem (ст. 29) | idem | idem | idem (ФНС) | idem | ст. 431, 80 |
| Уведомление | ТКС com УКЭП, ЛК ou papel (ст. 58 п. 9; ФНС) | ТКС = via operador | idem | idem | idem | [Verify] documento de recibo específico do уведомление | Prazos de 2026 na página da ФНС (26.01, 03.02 etc.) | ст. 58 п. 9; nalog-uvedomlenie-yanvar-2026.html |
| ЕФС-1 / СЗВ-ТД (СФР) | **≥ 11 segurados**: eletrônico com УКЭП (СФР); aceite via **Единая цифровая платформа (ЕЦП СФР)** desde 05.09.2025; ТКС permitido | Operadores de ЭДО conectam à ЕЦП (existe "Технологическая информация для операторов"); software de contabilidade deve ser ajustado | Representante com УКЭП física **+ МЧД** (formato приказ СФР 27.05.2024 № 848) | Poder **SFR_000001** (персонифицированный учёт) ou superior; classificador em lk.sfr.gov.ru/mchd.html | Dirigente emite МЧД com poderes | Квитанция о доставке; quitação de aceite; protocolo de controle (ТКС) | **Desde 01.07.2026**: novo formato xsd do ЕФС-1; **desde 01.09.2026**: SFR rejeita relatório com certificado sem os parâmetros keyAgreement/Data encipherment/Key encipherment | sfr.gov.ru/employers/general_information/eflow/ |

**Trechos literais (RU\...):**
- ст. 230 п. 2: "...представляется налоговым агентом в электронной форме по телекоммуникационным каналам связи. При численности физических лиц, получивших доходы в налоговом периоде, до 10 человек налоговый агент может представить указанные сведения и расчет сумм налога на бумажных носителях." → *6-NDFL em formato eletrônico por canais de telecomunicação; até 10 pessoas pode ser papel.*
- ст. 431 п. 10: "Плательщики, у которых численность физических лиц ... превышает 10 человек ... представляют расчеты ... в налоговый орган в электронной форме с использованием усиленной квалифицированной электронной подписи по телекоммуникационным каналам связи." → *Acima de 10 pessoas, РСВ eletrônico com assinatura qualificada por ТКС.*
- ст. 80 п. 5 (abertura): "Налоговые декларации (расчеты) представляются ... по установленным форматам в электронной форме по телекоммуникационным каналам связи через оператора электронного документооборота, являющегося российской организацией ... следующими категориями налогоплательщиков" → *Certas categorias devem entregar via operador de EDO russo.*
- ст. 80 п. 4: "Налоговая декларация (расчет) может быть представлена ... лично или через представителя ... передана в электронной форме по телекоммуникационным каналам связи или через личный кабинет налогоплательщика." → *Pode ser entregue pessoalmente, por representante, por ТКС ou ЛК.*
- ст. 80 (abertura п. 1): "...заявление ... составленное в электронной форме и переданное по телекоммуникационным каналам связи с применением усиленной квалифицированной электронной подписи или через личный кабинет налогоплательщика..." → *Declaração eletrônica assinada com УКЭП ou via ЛК.*
- ст. 29 п. 3: "Уполномоченный представитель налогоплательщика-организации осуществляет свои полномочия на основании ... письменной доверенности или доверенности в форме электронного документа, подписанного усиленной квалифицированной электронной подписью налогоплательщика-организации" → *Representante de empresa: procuração escrita ou eletrônica assinada com УКЭП da empresa.*
- ст. 80 (representante): "Если достоверность и полноту сведений ... подтверждает уполномоченный представитель ..., в налоговой декларации (расчете) указывается основание представительства ..." → *O documento de poderes é indicado na declaração.*
- ст. 58 п. 9: "...уведомление ... представляется ... не позднее 25-го числа месяца ... в электронной форме по телекоммуникационным каналам связи с применением усиленной квалифицированной электронной подписи либо через личный кабинет ..." → *Aviso por ТКС com УКЭП ou ЛК.*
- ФНС (МЧД): "С 1 сентября 2024 года физические лица, действующие по доверенности от организации или ИП, должны использовать КЭП для физических лиц в сочетании с МЧД в едином формате ... Формат ... утвержден приказом ФНС России от 19.09.2023 № ЕД-7-26/648@." → *Desde 01.09.2024, representante usa certificado de pessoa física mais МЧД.* (nalog-MCHD-sozdat-na-sajte-FNS.html)
- ФНС (recibo), Приказ ММВ-7-6/398@, anexo: "квитанцию о приеме налоговой декларации (расчета) или уведомление об отказе в приеме налоговой декларации (расчета) не позднее следующего рабочего дня за днем поступления, направляет ... налогоплательщику (представителю) через оператора ЭДО." → *O órgão emite recibo de aceite ou recusa até o próximo dia útil, via operador.* (nalog-pril-fns398-310714.doc; texto por extração UTF-16, não é OCR)
- СФР: "после перехода на Единую цифровую платформу при подписании УКЭП физического лица обязательно наличие машиночитаемой доверенности (формат МЧД утвержден приказом СФР от 27 мая 2024 № 848)." → *Com a plataforma digital, certificado de pessoa física exige МЧД.*
- СФР: "Для взаимодействия с Фондом при представлении сведений для ведения индивидуального (персонифицированного) учета необходимо полномочие SFR_000001 ..." → *Poder SFR_000001 necessário.*
- СФР: "С 1 июля 2026 года СФР будет осуществлять прием сведений по форме ЕФС-1 в новом формате." e "...с 01 сентября 2026 года СФР не будет принимать отчётность ..., подписанную квалифицированным сертификатом ... без установки выше приведённых параметров." → *Novo formato desde 01.07.2026; certificado sem parâmetros rejeitado desde 01.09.2026.*

**[Verify] RU:** (a) a lista de categorias do ст. 80 п. 5 que obriga o operador e se 6-НДФЛ/РСВ entram nela (parágrafos seguintes não verificados); (b) forma e prazo atuais de 6-НДФЛ (ЕД-7-11/649@ aparece só em buscas); (c) o **efeito concreto da ФЗ 201-ФЗ de 26.06.2026** para o nosso fluxo (só li a nota do Consultant sobre a vigência); (d) se Mercans precisa de **fornecedor russo** de ЭДО (ст. 80 exige operador russo); (e) vigência atual do Приказ ММВ-7-6/398@ (2014); (f) onde o **provedor** guarda a УКЭП do representante.

---

## Resposta às 5 perguntas do pedido, por país

| Pergunta | UA | KZ | AZ | RU |
|---|---|---|---|---|
| (1) Canal; software transmite direto? | Електронний кабінет; API prevista em lei (ст. 42-1), spec não lida | Кабинет налогоплательщика; sistemas externos permitidos por lei (ст. 115 п.3); spec do API não lida | [Verify] | ТКС via operador de ЭДО (ou ЛК); sem envio direto ao ФНС pelo software |
| (2) Provedor envia em nome do empregador | "Уповноважена особа" (49.3, 42.6); provedor externo: [Verify] | "Уполномоченный представитель" (доверенность/doc eletrônico, ст. 40); ou funcionário nomeado com ЭЦP | [Verify] | Representante (ст. 29) com УКЭП física + МЧД |
| (3) Autorização do empregador | КЕП do diretor define autorizados (42.6) | Diretor nomeia (Цифр. кодекс 62.6) ou emite doc eletrônico (НК 40) | [Verify] | Diretor assina МЧД com УКЭП da organização |
| (4) Recibo | Квитанція (49.9.1); №1/№2 [Verify] | Уведомление о принятии (Правила 30 3), 51) | [Verify] | Квитанция о приеме (ФНС); СФР: квитанция о доставке + приеме |
| (5) Mudanças 2026–27 | v11 (17.07.2026, uso 01.08.2026) | НК e Приказ 695 desde 01.01.2026; Цифр. кодекс; ИСНА [Verify] | [Verify] | ст. 80 (201-ФЗ, 26.07.2026); ЕФС-1 novo formato 01.07.2026; certificado SFR 01.09.2026 |

---

## Bloco de prova
- **Pedido → resposta:** UA, KZ, RU cobertos com fonte; **AZ sem nenhuma fonte primária** (sites inacessíveis); UA sem texto de квитанція №1/№2 e KZ sem a spec do API (lacunas declaradas).
- **Fontes lidas:** UA: PK ст. 42, 42-1, 49 (captura Wayback do zakon.rada.gov.ua) e Order 4/2015 red. 243 (já em `raw`); KZ: НК РК (K2500000214), Приказ 695 (V2500037390), Цифровой кодекс (K2600000255), Закон 370 (revogado); RU: НК РФ ст. 26 (baixada, não citada), 29, 58, 80, 230, 431 (consultant.ru), páginas ФНС e СФР e anexo do Приказ 398.
- **Conferido mecanicamente:** cada trecho citado foi achado por busca de texto nos arquivos baixados (extração HTML→texto; .doc por UTF-16; docx pelo `document.xml`). Não conferi md5 contra a fonte. Edição do PK é de 2025 (não a de out/2026).
- **Limites de fonte:** Consultant.ru é reprodução do texto da lei, não o site da autoridade; a captura do PK vem do Wayback, não do zakon.rada.gov.ua direto. Resumos de buscador (API de KZ, ASAN imza de AZ, МЧД formato 5.02) foram usados só para achar fontes e ficam como [Verify].
- **Confiança:** UA 70%, KZ 80% (lei sim, API/ИСНА não), RU 80% (lei e ФНС/СФР sim; lista ст. 80 п.5 e 201-ФЗ incompletos), AZ 0%.
- **O que falta:** (1) AZ inteiro, via VPN ou time local; (2) UA Наказ 557/2017; (3) KZ spec API/ИСНА em portal.kgd.gov.kz; (4) RU lista de categorias da ст. 80 п.5 e texto da 201-ФЗ.
