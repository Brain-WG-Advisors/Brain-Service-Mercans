# UA: verificação em fonte primária oficial (afirmações A–H dos rascunhos J05 / 1-ПВ)

Data: 2026-10-13. Material bruto: não editar (regra do `raw/`).
Acesso: tax.gov.ua, ukrstat.gov.ua, stat.gov.ua e zakon.rada.gov.ua estão bloqueados desta máquina. Por isso usei cópias do Internet Archive (modo `id_`, byte a byte) das URLs oficiais e baixei direto dos sites regionais `*.ukrstat.gov.ua`. Abaixo, cada URL é a **URL oficial original**, seguida da data da captura.

## Tabela de vereditos

| # | Afirmação | Veredito | Localização exata | URL oficial (captura) |
|---|---|---|---|---|
| A | C_REG / C_RAJ = código da região / do distrito do órgão da ДПС; C_STI_ORIG = código do órgão da ДПС | **CONFIRMADO**, com uma ressalva de redação (ver abaixo) | Наказ Міндоходів 29.11.2013 № 729, Додаток 1 "Формат (стандарт) електронного документа звітності суб'єктів господарювання": tabela do DECLARHEAD, linhas `<C_REG>`, `<C_RAJ>`, `<C_STI_ORIG>`, e regra do nome do arquivo (posições 1–4 e 40–43) | https://tax.gov.ua/data/normativ/000/000/63127/Dodatok1.doc (captura 2026-04-24); página do наказ: https://tax.gov.ua/elektronna-zvitnist/platnikam-podatkiv-pro/normativne-zabezpechennya/63127.html (captura 2021-06-14); SPR_STI.XML: https://tax.gov.ua/data/material/000/006/58782/SPR_STI.ZIP (captura 2026-04-24, arquivo de 06.03.2026) |
| B | J0510510 versão 10 é a vigente; não existe versão 11 | **CONFIRMADO até 06.03.2026** (data do SPR_VER; captura 2026-04-24). Para outubro de 2026: **NÃO CONFIRMADO** (não há captura mais recente) | SPR_VER.XML, ROW `C_DOC=J05, C_DOC_SUB=105, C_DOC_VER=10, D_BEGIN=01012014, D_END=(vazio)`; nenhuma ROW J05/105 com versão 11 | https://tax.gov.ua/data/material/000/006/58777/SPR_VER.ZIP (captura 2026-04-24); https://tax.gov.ua/data/material/000/357/453385/j0500110.arj (última captura 2026-04-24) |
| C | common_types.xsd do próprio Держстат; validar amostras | **CONFIRMADO / BAIXADO.** As duas amostras são **VÁLIDAS** com o common_types do Держстат. Há uma observação sobre OBL/C_REG (ver abaixo) | `po_doc/common_types.zip` → `common_types.xsd` (gravado em 14.05.2025). A página do Держстат anuncia que esse arquivo está em uso "починаючи з 16.06.2025" | https://www.ukrstat.gov.ua/elektr_zvit/po_doc/common_types.zip (captura 2025-08-09); aviso: https://www.ukrstat.gov.ua/elektr_zvit/po.htm (captura 2026-04-14) |
| D | Довідник причин (REASON_KOD): códigos e textos comparados com as 5 razões do blank | **CONFIRMADO**: 6 códigos. O blank do 1-ПВ usa 5 deles; o código 33 não aparece no blank | `PDF_XSD_XLS_2025/Список причин.xls` (colunas NUM, NAME). Роз'яснення 28.11.2024: mensal р. I п. 9, trimestral р. I п. 10 | https://ukrstat.gov.ua/elektr_zvit/2024/PDF_XSD_XLS_2025.zip (captura 2025-04-19) |
| E | r.1030 = ПДФО a qualquer alíquota (inclui 5% gig Дія Сіті), exclui ПДФО sobre тимчасова непрацездатність; військовий збір não entra | **Parcial.** (1) Exclusão da тимчасова непрацездатність: **CONFIRMADO**. (2) "Qualquer alíquota / inclui 5% gig": **NÃO CONFIRMADO**, as fontes não tratam do tema. (3) Військовий збір fora: **NÃO CONFIRMADO de forma explícita**; só há indícios (ver abaixo) | Blank наказ 117 (linha 1030); Роз'яснення 28.11.2024 № 19.1.2-12/24-24, р. I п. 8 e р. II п. 2; ГУС Львів 2026, slides 9 e 14 | https://stat.gov.ua/sites/default/files/2025-12/roz_1_pv_mis_2025_179.doc (captura 2026-02-25); https://www.lv.ukrstat.gov.ua/ukr/sr/presentation/1_pv_mis_2026.pdf (download direto) |
| F | Instrução 286: п. 2.1, 2.6.1–2.6.2, 3.1, 3.3 | **CONFIRMADO** (citações abaixo) | Інструкція зі статистики кількості працівників (наказ 286/2005, red. 04.10.2023 № 279), п. 2.1, 2.6.1, 2.6.2, 3.1, 3.3 | https://www.ukrstat.gov.ua/norm_doc/2023/279/279.pdf (local, 2026-10-09). Cópia idêntica (SHA-1 igual) em https://stat.gov.ua/sites/default/files/2026-03/286_2005.pdf (captura 2026-06-17) |
| G | r.3070 em todo trimestre; 3080/3090/3100 e seção V só no IV trimestre; coluna 1 de 7010/7030/7040 = середньооблікова/середня кількість | **CONFIRMADO** (com 2 observações sobre o XSD) | Blank 1-ПВ (квартальна), seção I e V; Роз'яснення № 19.1.2-12/25-24, р. II п. 1, 6–9 e р. V п. 1–3; template .xls, aba "Контролі", controles 6, 9 e 17–24 | https://www.ukrstat.gov.ua/norm_doc/2024/117/117_kv.pdf (local); https://stat.gov.ua/sites/default/files/2025-12/roz_1_pv_kv_2025_180.doc (captura 2026-02-25) |
| H | PERIOD_MONTH no trimestral = último mês do trimestre; PERIOD_TYPE=2 | **CONFIRMADO** | Держстат "Формат (стандарт) електронного документа звітності респондентів" (Format 3.1), Таблиця 1; igual no Додаток 1 do наказ 729/2013 da ДПС | https://www.ukrstat.gov.ua/elektr_zvit/po_doc/Format_.rar (captura 2025-08-09); https://tax.gov.ua/data/normativ/000/000/63127/Dodatok1.doc (captura 2026-04-24) |

---

## A. Cabeçalho ДПС: C_REG, C_RAJ, C_STI_ORIG

Fonte: Наказ Міністерства доходів і зборів від 29.11.2013 № 729, "Про затвердження Формату (стандарту) електронного документа звітності суб'єктів господарювання та Опису довідників…", Додаток 1. Arquivo: `2026-10-13-DPS-nakaz729-2013-Format-standart-dodatok1.doc`.
Esse наказ substituiu o наказ ДПА 03.05.2006 № 242, cancelado pelo наказ Міндоходів 29.11.2013 № 728. A página da ДПС (63127.html) cita o 729 como o formato vigente para o recebimento dos relatórios.

- Tabela do DECLARHEAD, linha `<C_REG>` "Код області":
  > "Значенням цього елемента є код області, на території якої розташований територіальний орган отримувача, до якого подається документ (оригінал або копія). Код області заповнюється згідно з довідником територіальних органів Міністерства доходів і зборів України (SPR_STI.XML)…"
  (Tradução: o valor é o código da região onde fica o órgão territorial destinatário ao qual o documento é apresentado. Preenche-se pelo diretório de órgãos territoriais, SPR_STI.XML.)
- Linha `<C_RAJ>` "Код адміністративного району":
  > "Значенням цього елемента є код адміністративного району, на території якого розташований територіальний орган отримувача, до якого подається документ (оригінал або копія). Код району заповнюється згідно з довідником … (SPR_STI.XML)…"
  (Tradução: código do distrito administrativo onde fica o órgão destinatário.)
- Linha `<C_STI_ORIG>` "Код територіального органу отримувача, до якого подається оригінал документа":
  > "Код територіального органу отримувача обирається з довідника територіальних органів …, є числовим значенням, яке відповідає формулі значення елемента C_REG*100 + значення елемента C_RAJ"
  (Tradução: código do órgão destinatário do original, tirado do diretório; C_STI_ORIG = C_REG×100 + C_RAJ.)
- Nome do arquivo: "позиції з 40 по 43 містять код територіального органу отримувача, до якого подається оригінал документа (значення елемента C_STI_ORIG…)".
- Confirmação no diretório vigente (`2026-10-13-DPS-SPR_STI-2026-03-06.zip`, SPR_STI.XML de 06.03.2026): `C_REG=26` "М.КИЇВ"; `C_STI=2650, C_RAJ=50`; `C_STI=1008, C_RAJ=8` (Київська обл.). A fórmula C_REG×100+C_RAJ se confirma.

**Ressalva de redação:** a fonte primária define C_REG e C_RAJ pelo **órgão destinatário ao qual o documento é apresentado**. Ela **não** fala em "onde o contribuinte está registrado". A ligação entre local de registro e órgão de entrega vem de outra norma (Податковий кодекс / regras de registro), que **não verifiquei** aqui. Sugestão de redação: "órgão da ДПС ao qual o documento é apresentado".

## B. J0510510 versão 10 vigente

- SPR_VER.XML (ДПС, "Довідник версій документів податкової звітності", arquivo de 06.03.2026; `2026-10-13-DPS-SPR_VER-2026-03-06.zip`):
  > `<C_DOC>J05</C_DOC> <C_DOC_SUB>105</C_DOC_SUB> <C_DOC_VER>10</C_DOC_VER> <D_BEGIN>01012014</D_BEGIN> <D_END></D_END> <NORM_DOC>Накази Мiнiстерства фiнансiв України вiд 24.01.2025 № 39 та №53 вiд 30.01.2025</NORM_DOC>`
  (Tradução: J05/105 versão 10, sem data de fim, base: наказы do Мінфін 24.01.2025 № 39 e 30.01.2025 № 53.)
  Histórico: v6 até 30.06.2021, v7 até 30.09.2022, v8 até 30.06.2023, v9 até 31.12.2024. **Não há linha J05/105 v11.**
- Pasta oficial `/data/material/000/357/453385/`: j0500102…j0500110. Última captura do j0500110.arj em **2026-04-24**. Nenhuma captura de j0500111.
- Limite: a evidência vale até 06.03.2026 (captura de 24.04.2026). Que a v10 continue vigente em outubro de 2026 **não está confirmado** por fonte primária posterior.

## C. common_types.xsd do Держстат e validação das amostras

- Baixado: `2026-10-13-common_types-Derzhstat-2025-05-14.xsd`, de `https://www.ukrstat.gov.ua/elektr_zvit/po_doc/common_types.zip` (captura 2025-08-09). Arquivo interno gravado em 14.05.2025. Zip original salvo como `2026-10-13-common_types-Derzhstat-po_doc.zip`.
- A página do Держстат "Інформація для розробників програмного забезпечення" (`2026-10-13-Derzhstat-po-informatsiia-rozrobnykam.htm`, captura 2026-04-14, modificada em 07.10.2025) diz:
  > "Повідомляємо, що починаючи з 16.06.2025 року в системі електронної звітності органів державної статистики буде використовуватись оновлений файл опису типів даних (common_types.xsd)"
  (Tradução: a partir de 16.06.2025 o sistema de relatório eletrônico do Держстат usa o arquivo atualizado de tipos de dados.)
- Diferenças em relação à versão antiga (doc_2021, de 2015): `DGdecimal0` passou a aceitar só inteiros (`\-{0,1}[0-9]+`). `DGdecimal1` passou a exigir exatamente 1 casa decimal (`[0-9]+\.[0-9]{1}`). Foi acrescentado `DGsti` (0–99). `STATRAY` passou a ter o padrão `[0-9]{3}`.
- O pacote de 2025 (PDF_XSD_XLS_2025.zip) **não** traz common_types próprio: ele é distribuído à parte.
- **Validação (lxml, cópias em pasta temporária; amostras intactas):**
  - `rascunhos/2026-10-09-S0301016-amostra.xml` contra S0301016.xsd + common_types do Держстат: **VALID**
  - `rascunhos/2026-10-09-S0301121-amostra.xml` contra S0301121.xsd + common_types do Держстат: **VALID**
- **Observação sobre as amostras (não é erro de schema):**
  - As duas amostras usam `C_REG=26` e `OBL=26` para Kyiv, com `KATOTTG_FACT=UA80…`.
  - Na codificação do Держстат, Kyiv é **80** e 26 é a **Івано-Франківська область**. Isso vale no SPR_SSCU (`2026-10-13-Derzhstat-spr_sscu-2016.xml`: `<CODE>26</CODE><NAME>Івано-Франківська область</NAME>`, `<CODE>80</CODE><NAME>м. Київ</NAME>`) e no КАТОТТГ (UA80 = Kyiv).
  - O mapa de campos técnicos do Держстат define OBL como "Код області відповідно до КАТОТТГ".
  - 26 é o código de Kyiv **na ДПС** (SPR_STI). Ou seja, parece que a codificação da ДПС foi usada num relatório do Держстат.
  - O Format 3.1 do Держстат (seção H) manda preencher C_REG/C_RAJ "згідно з довідником органів державної статистики (SPR_SSCU.XML)", com C_RAJ de 3 posições no nome do arquivo. As amostras trazem `C_RAJ=5`.
  - O SPR_SSCU encontrado é de 2016 (anterior à reforma distrital). **Não achei** versão atual. Recomendo revisar OBL/C_REG/C_RAJ das amostras antes de usá-las.

## D. Lista de razões de ausência de dados (REASON_KOD)

Fonte: `PDF_XSD_XLS_2025/Список причин.xls` dentro do pacote oficial de formatos 2025 do Держстат (arquivo de 18.10.2021). Salvo como `2026-10-13-Derzhstat-Spysok-prychyn-REASON_KOD.xls`.

| NUM (REASON_KOD) | NAME (ucraniano) | Tradução | No blank 1-ПВ (наказ 117)? |
|---|---|---|---|
| 33 | Не здійснюється вид економічної діяльності, який спостерігається | O tipo de atividade econômica observado não é exercido | **Não** |
| 34 | Одиниця припинена або перебуває в стадії припинення | Unidade extinta ou em extinção | Sim |
| 37 | Здійснюється сезонна діяльність або економічна діяльність, пов'язана з тривалим циклом виробництва | Atividade sazonal ou de ciclo produtivo longo | Sim |
| 39 | Тимчасово призупинено економічну діяльність через економічні чинники/карантинні обмеження | Atividade suspensa temporariamente (fatores econômicos/quarentena) | Sim |
| 40 | Проведено чи проводиться реорганізація або передано виробничі фактори іншій одиниці | Reorganização ou transferência de fatores de produção | Sim |
| 42 | Відсутнє явище, яке спостерігається | Ausência do fenômeno observado | Sim |

- As 5 razões do blank (mensal e trimestral) batem palavra por palavra com os códigos 34, 37, 39, 40 e 42.
- Роз'яснення 28.11.2024 (mensal р. I п. 9; trimestral р. I п. 10) lista as mesmas 5 e diz: "Інші причини відсутності даних не використовуються." (Tradução: outras razões de ausência de dados não são usadas.) Portanto **o código 33 não se aplica ao 1-ПВ**.
- Template .xls, aba "Контролі", controle 12 (mensal) / 54 (trimestral): quando houver a marca "V", a razão é obrigatória, "крім причини: "Не здійснюється вид економічної діяльності, який спостерігається"".
- Ressalva: o arquivo se chama "Список причин". Não encontrei um documento com o título exato "Довідник причин неподання або відсутності даних…" (é o nome usado na aba "Довідники", com fonte "бланк, роз'яснення").

## E. Linha 1030 (1-ПВ mensal)

- Blank (наказ 117/2024), linha 1030:
  > "Сума податку з доходів фізичних осіб, що відрахована з фонду оплати праці усіх працівників (крім тимчасової непрацездатності), тис.грн (з одним десятковим знаком)"
  (Tradução: valor do ПДФО retido do ФОП de todos os empregados, exceto incapacidade temporária.)
- Роз'яснення 28.11.2024 № 19.1.2-12/24-24, р. II п. 2:
  > "Показник щодо суми податку з доходів фізичних осіб, що відрахована з фонду оплати праці всіх працівників (крім тимчасової непрацездатності), містить дані про суму податку з доходів фізичних осіб із фонду оплати праці всіх працівників, без перерахунків за попередній рік."
  (Tradução: … sem recálculos referentes ao ano anterior.) Os ГУС de Львів e Черкаси (2026) dizem "без перерахунків за попередні періоди" (períodos anteriores): há divergência de redação entre o Роз'яснення e os órgãos regionais.
- Роз'яснення, р. I п. 8: "(ПДФО ÷ ФОП всіх працівників) × 100 … є меншим або дорівнює вісімнадцяти" (≤ 18).
- ГУС Львів 2026, slide 14:
  > "Суми, нараховані по листках тимчасової непрацездатності, до фонду оплати праці не включаються до даних рядків: 1020, 1030, 1070!"
- ГУС Черкаси 2026: aponta como erro típico incluir em 1030 "суми оподаткування по тимчасовій непрацездатності".
- **Alíquota / 5% gig Дія Сіті:** nenhuma das fontes (blank, Роз'яснення, ГУС Львів, ГУС Черкаси) menciona alíquota, Дія Сіті ou gig-специалісти. **NÃO CONFIRMADO.**
- **Військовий збір:** nenhuma fonte o exclui expressamente. Há só indícios: a linha cita apenas "податок з доходів фізичних осіб", e o teto de controle é ≤ 18% (= alíquota básica do ПДФО). **NÃO CONFIRMADO de forma explícita.**

## F. Instrução 286 (red. 04.10.2023 № 279), citações literais

- **п. 2.1:**
  > "В облікову кількість штатних працівників включаються усі наймані працівники, які уклали письмово трудовий договір (контракт) і виконували постійну, тимчасову або сезонну роботу один день і більше, а також власники підприємства, якщо, крім доходу, вони отримували заробітну плату на цьому підприємстві."
  (Tradução: entram na облікова кількість штатних todos os empregados com contrato de trabalho escrito que trabalharam um dia ou mais, além dos proprietários que recebem salário na empresa.)
- **п. 2.6:** "Не включаються до облікової кількості штатних працівників такі категорії:"
  - **2.6.1:** "прийняті на роботу за сумісництвом з інших підприємств." Complemento: "Працівник, який отримує на одному підприємстві дві, півтори ставки, тобто оформлений за сумісництвом на тому самому підприємстві, де й основне місце роботи (внутрішнє сумісництво), або менше однієї ставки, в обліковій кількості штатних працівників враховується як одна фізична особа;"
  - **2.6.2:** "залучені до виконання робіт за цивільно-правовими договорами (договорами підряду)." Complemento: "Працівник, який перебуває в обліковому складі підприємства і уклав цивільно-правовий договір з цим самим роботодавцем, враховується в обліковій та середньообліковій кількості працівників один раз за місцем основної роботи та не враховується у кількості працюючих за цивільно-правовими договорами;"
- **п. 3.1:**
  > "Середня кількість працівників підприємства за період (місяць, квартал, з початку року, рік) визначається як сума таких показників: середньооблікової кількості штатних працівників; середньої кількості зовнішніх сумісників; середньої кількості працюючих за цивільно-правовими договорами."
- **п. 3.3 (regra de cálculo para зовнішні сумісники e ЦПД):**
  > "Середня кількість зовнішніх сумісників і працюючих за цивільно-правовими договорами за місяць розраховується аналогічно до методології визначення середньооблікової кількості штатних працівників, викладеної у пункті 3.2 цієї Інструкції. При цьому працівники цих категорій ураховуються як цілі одиниці, незалежно від тривалості робочого часу протягом усього терміну дії договору. Кількість працівників за вихідний або святковий і неробочий день ураховується на рівні робочого дня, що їм передував. До кількості працюючих за цивільно-правовими договорами не належать громадяни-підприємці, які виконували роботи згідно з цивільно-правовими договорами. Середня кількість зовнішніх сумісників і працюючих за цивільно-правовими договорами за період з початку року і рік визначається шляхом підсумовування середньої кількості цих працівників за усі місяці з початку року і ділення отриманої суми на кількість місяців…"
  (Tradução: mesma metodologia da п. 3.2, contando cada pessoa como unidade inteira, independentemente da jornada, durante toda a vigência do contrato. Fins de semana e feriados assumem o número do dia útil anterior. ФОП-підприємці com ЦПД não entram. Para períodos, soma-se a média mensal e divide-se pelo número de meses.)

## G. 1-ПВ trimestral: periodicidade e coluna 1 da seção IV

- **Blank**, seção I: a linha 3070 "Облікова кількість штатних працівників на кінець звітного періоду" fica **antes** do subtítulo "Станом на 31 грудня звітного року (раз на рік у звіті за IV квартал)". Só 3080, 3090 e 3100 ficam sob esse subtítulo. A seção V (8010–8040) se chama "Інформація про укладання колективних договорів станом на 31 грудня звітного року (раз на рік у звіті за IV квартал)".
- **Роз'яснення № 19.1.2-12/25-24, р. II п. 1:** os indicadores contêm dados "щодо прийому на роботу та звільнення штатних працівників у звітному кварталі, їх облікової кількості на кінець звітного кварталу, а також окремих категорій штатних працівників станом на 31 грудня". Os пп. 7–9 (3080/3090/3100) dizem "станом на 31 грудня". As regras cruzadas com 3080/3090/3100 levam "(для звіту за ІV квартал)".
- **Controles** (template S0301121, aba "Контролі"): nº 17 (3070 = 3070 do relatório anterior + 3020 − 3040) **não** tem restrição de trimestre. Os nº 6 e 18–24 (3080/3090/3100) e 47–48 (8010–8030) levam "(для 4 кварталу)".
- **Coluna 1 de 7010/7030/7040:** no blank, o cabeçalho da coluna 1 é "Середньо-облікова кількість, осіб (у цілих числах)" para as três linhas. O Роз'яснення р. V detalha:
  - п. 1 (жінки, 7010): "середньооблікова кількість – про середньооблікову кількість штатних працівників-жінок…";
  - п. 2 (зовнішні сумісники, 7030): "середня кількість – про їх середню кількість";
  - п. 3 (ЦПД, 7040): "середня кількість – про їх середню кількість".
- Observações sobre o XSD S0301121 v21:
  - 3090 só tem `A3090_2` (mulheres). O controle 9 exige "ряд. 3090 гр.1 = 0".
  - A coluna 3 (людиногодини) só existe para 7010 (`C7010`). **Não há** `C7030` nem `C7040` no XSD, embora o blank tenha a coluna 3 nessas linhas.

## H. PERIOD_MONTH / PERIOD_TYPE no 1-ПВ trimestral

- Держстат, "Формат (стандарт) електронного документа звітності респондентів" (Format_3_1.doc de 2010, ainda publicado em `ukrstat.gov.ua/elektr_zvit/po_doc/Format_.rar`, captura 2025-08-09), Таблиця 1:
  > `<PERIOD_MONTH>` "Звітним місяцем вважається останній місяць у звітному періоді (для 1,2,3,4 кварталів це 3,6,9,12 місяць відповідно, для року – 12)."
  > `<PERIOD_TYPE>` "1-місяць, 2-квартал, 3-півріччя, 4-9 місяців, 5-рік."
- A mesma Tabela 1 define C_REG/C_RAJ do Держстат: "код області, на території якої розташовується орган державної статистики, до якого подається документ… згідно з довідником органів державної статистики (SPR_SSCU.XML)". Ver a observação em C.
- O "Уніфікований формат транспортного повідомлення" do Держстат (2014) traz exemplo trimestral com `<PERIOD_MONTH>6</PERIOD_MONTH> <PERIOD_TYPE>2</PERIOD_TYPE>`.
- O padrão da ДПС (наказ 729, Додаток 1) define o mesmo para PERIOD_MONTH/PERIOD_TYPE.
- Ressalva: o Format 3.1 é de 2010. A página atual de desenvolvedores do Держстат (po.htm, 2026) não o lista mais. Ele continua hospedado e é coerente com o XSD vigente (DGMonth 1–12, DGPType 1–5). Não encontrei versão mais nova.

## Pacote 2026 do Держстат (risco aberto)
A página po.htm (captura 2026-04-14) aponta "Формати звітних документів" para `elektr_zvit/2024/PDF_XSD_XLS_2026.zip`. **Não há captura desse arquivo.** Não dá para excluir que ele traga versões novas do S0301016/S0301121. Contra essa hipótese:
- as formas publicadas em stat.gov.ua em 12/2025 (`1_pv_mis_2025.doc`, `1_pv_kv_2025.docx`) ainda são as do наказ 117;
- a lista Perelik_form_2026 mantém S0301016/S0301121.

## Arquivos salvos nesta verificação (prefixo 2026-10-13-)
- `common_types-Derzhstat-2025-05-14.xsd`, `common_types-Derzhstat-po_doc.zip`: tipos comuns do Держстат (C)
- `Derzhstat-po-informatsiia-rozrobnykam.htm`: aviso de 16.06.2025 e links atuais (C, H)
- `Derzhstat-Format-standart-3_1.rar` / `.doc`: formato do documento eletrônico do Держстат (H)
- `Derzhstat-Unif-format-2014.doc`: formato unificado de transporte (H)
- `Derzhstat-spr_sscu-2016.xml`: diretório de órgãos estatísticos (observação em C)
- `Derzhstat-Spysok-prychyn-REASON_KOD.xls`: lista de razões (D)
- `rozyasnennia-1PV-misiachna-19.1.2-12-24-24.doc`, `rozyasnennia-1PV-kvartalna-19.1.2-12-25-24.doc`: Роз'яснення oficiais de 28.11.2024, de stat.gov.ua (E, G, D). Isso fecha a lacuna nº 1 do LEIA-ME de 2026-10-09.
- `1PV-misiachna-GUS-Lviv-2026.pdf`, `1PV-kvartalna-GUS-Lviv.pdf`: ГУС у Львівській області (E)
- `DPS-SPR_VER-2026-03-06.zip`, `DPS-SPR_STI-2026-03-06.zip`: diretórios da ДПС (A, B)
- `DPS-nakaz729-2013-Format-standart-dodatok1.doc`, `DPS-nakaz729-2013-Opys-dovidnykiv-dodatok2.doc`, `DPS-nakaz729-2013-storinka.htm`: formato do documento eletrônico da ДПС (A, H)
