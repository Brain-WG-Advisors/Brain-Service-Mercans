# Auditoria UA 1-ПВ (mensal S0301016 / trimestral S0301121) — abas exceto Wage Fund Classification

Data: 2026-10-16. Escopo: M_* e Q_* listados (Spec mensal só linhas 1–16; Spec trimestral só linhas 1–30). Colunas V (BA Mapping) e W (Query to RA) não auditadas.

Fontes usadas (siglas):
- **ROZ-M** = Роз'яснення 1-ПВ (місячна), 28.11.2024 № 19.1.2-12/24-24 (`SRC_rozyasnennia_mensal.txt`)
- **ROZ-Q** = Роз'яснення 1-ПВ (квартальна), 28.11.2024 № 19.1.2-12/25-24 (`SRC_rozyasnennia_trimestral.txt`)
- **I286** = Інструкція № 286 ред. 2023 (`SRC_instrucao286.txt`); **I5** = Інструкція № 5 (`SRC_instrucao5_2004_red2023.txt`)
- **F31** = Format 3.1 (`SRC_format31.txt`); **XSD-M/XSD-Q** = `raw/docs/oficiais/UA/2026-10-09-S0301016…xsd` / `…S0301121…xsd`
- **CTRL-M/CTRL-Q** = `*-shablon.xls`, aba "Контролі"; **TECH** = `*-tekh-polia.xlsx`; **REASON** = `2026-10-13-Derzhstat-Spysok-prychyn-REASON_KOD.xls`
- **LVIV-M** = `2026-10-13-1PV-misiachna-GUS-Lviv-2026.pdf`; **LVIV-Q** = `2026-10-13-1PV-kvartalna-GUS-Lviv.pdf` (apresentação de 2024, da época da ordem 128; usada só para estrutura/prazo, confirmada pela ROZ-Q)
- **N117** = `2026-10-09-nakaz117-2024-Derzhstat-1PV.htm`

## (a) ERROS

### Mensal

| # | Arquivo/aba | Célula | Atual | Correto | Citação da fonte | Por quê |
|---|---|---|---|---|---|---|
| 1 | M_Version_Control | B10 | "1-ПВ (місяцна)" | "1-ПВ (місячна)" | N117: "№ 1-ПВ (місячна) "Звіт із праці"" | Erro de grafia |
| 2 | M_Version_Control | D17 (v5.0) | "column X (XML element) added to the Spec sheet" | "column U (XML element)" | Spec U1 = "XML Element (S0301016)"; X1 = "RA Comments"; o próprio D20 cita "U15/U16: XML elements" | Referência de coluna desatualizada/errada |
| 3 | M_Report_Matrix | A1 | "1-ПВ (МİSYACHNA)" (İ turco) | "1-ПВ (МІСЯЧНА)" ou "(MISIACHNA)" | N117: "№ 1-ПВ (місячна)" | Texto truncado/misturado (cirílico + latino + İ turco) |
| 4 | M_Report_Matrix | B5 | "№ 1-ПВ (місяцна)" | "№ 1-ПВ (місячна)" | N117 (idem) | Erro de grafia no nome oficial do formulário |
| 5 | M_Report_Matrix | B7 | "Державна служба статистики україни" | "…України" | N117: "ДЕРЖАВНА СЛУЖБА СТАТИСТИКИ УКРАЇНИ" | Nome próprio com minúscula |
| 6 | M_Payroll_Scope_Summary | A1 | "1-ПВ (МОНТНА)" | "1-ПВ (МІСЯЧНА)" | N117 (idem) | Palavra deturpada (mistura de "monthly" com cirílico) |
| 7 | M_Payroll_Scope_Summary | A4 | "Header block (Зведоу, EDRPOU, …)" | Termo inexistente; pelo conteúdo do cabeçalho, provavelmente "Звітний місяць" (Spec B5) | Spec B5: "Звітний місяць" | Palavra deturpada/inexistente em ucraniano |
| 8 | M_Payroll_Scope_Summary | A7 | "1040 -- Average FTE headcount, staff" | "1040 -- Average headcount (середньооблікова кількість), staff" | I286 p.1.8 define "еквівалент повної зайнятості" como conversão do tempo pago em trabalhadores de jornada integral; p.3.2/2.4.3: na середньооблікова os de jornada parcial "враховуються … як цілі одиниці"; LVIV-M: "особи прийняті на 0,25; 0,5; 0,75; 1,5 ставки … враховуються як ціла одиниця" | "FTE" é outro indicador (I286 cap. 4); a linha 1040 conta pessoas, não FTE. O mesmo rótulo aparece no nome da aba "Average FTE Headcount" (corrigir junto) |
| 9 | M_Payroll_Scope_Summary | C7 | "Pure derivative of the payroll population table (who has an active payroll record this month), not of an HR hiring/firing event log." | A 1040 se calcula sobre a contagem diária do quadro (облікова кількість), conferida com ordens de admissão/transferência/desligamento e com o controle de ponto | I286 p.3.2: "розраховується на підставі щоденних даних про облікову кількість штатних працівників, які повинні уточнюватись відповідно до наказів про прийом, переведення … та припинення трудового договору … має відповідати даним табельного обліку" | A afirmação contradiz a instrução; além disso, quem está em licença sem vencimento continua no quadro (I286 p.2.5.7), mesmo sem pagamento no mês |
| 10 | M_Payroll_Scope_Summary | C9 | "1070 … Same as 1020, filtered by employment-type flag" | Filtrar o tipo de contrato não basta: a 1070 também exclui os valores apurados para mobilizados/convocados, para quem está em licença-maternidade ou licença para cuidar de filho e para desligados | I5 p.1.5: "При визначенні фонду оплати праці штатних працівників … також виключаються суми нараховані працівникам, які перебувають у відпустці у зв'язку з вагітністю та пологами та для догляду за дитиною, … звільненим з роботи на момент здійснення нарахувань"; ROZ-M I.8: "фонду оплати праці всіх працівників можуть бути більшими на суму нарахувань особам, які не враховуються в середньообліковій кількості"; LVIV-M sl.12: 1070 menor que 1020 pelos valores pagos a "мобілізованим працівникам" | Regra de população incompleta: os mobilizados continuam na categoria 1 (Spec X12) e, por esse filtro, entrariam na 1070 |
| 11 | M_UA_1PV_001_Spec | B6 | "Ідентифікаційний код ФДРПОУ" | "Ідентифікаційний код ЄДРПОУ" | LVIV-Q: "Ідентифікаційний код ЄДРПОУ" | Erro de grafia (Ф no lugar de Є) |
| 12 | M_UA_1PV_001_Spec | M9 | "reason-code list (from Derzhstat's own роз'яснення 27.04.2023)" | Роз'яснення de 28.11.2024 № 19.1.2-12/24-24, item I.9 | ROZ-M (fim): "Роз'яснення … від 27 квітня 2023 року № 19.1.2-12/9-23 є недійсними з 01 лютого 2025 року"; ROZ-M I.9 lista as 5 causas | A fonte citada foi revogada; X9 e Field Options já usam a lista atual |
| 13 | M_UA_1PV_001_Spec | L11 | "SUM(PIT withheld on the row-1020 components) MINUS PIT withheld specifically on sick-pay wage types" | IR retido sobre o fundo da 1020 (que já exclui o auxílio-doença), sem recálculos do ano anterior; não há o que subtrair de novo | I5 p.3.2–3.3: o auxílio-doença (по тимчасовій непрацездатності, inclusive "перших п'яти днів … за рахунок коштів підприємства") não entra no фонд оплати праці; ROZ-M II.2: "…із фонду оплати праці всіх працівників, без перерахунків за попередній рік" | Se os componentes da 1020 já excluem o auxílio-doença, subtrair o IR sobre ele desconta duas vezes; também falta a regra "sem recálculo do ano anterior" |
| 14 | M_UA_1PV_001_Spec | A12 | "Average FTE headcount, staff" | "Average headcount, staff (середньооблікова кількість)" | I286 p.1.8 × p.3.2 (ver #8) | Rótulo técnico errado (FTE ≠ середньооблікова); B12 está correto |
| 15 | M_UA_1PV_001_Spec | L12 | "AVERAGE of (count of staff employees with an active payroll record) over each calendar day" | Contagem diária do quadro (todos com vínculo de trabalho, inclusive em licença sem vencimento), menos as exclusões da ROZ-M II.3; em fim de semana/feriado vale a contagem do dia útil anterior | I286 p.2.3: "усі працівники, які перебувають у трудових відносинах"; p.2.5.7: "у відпустках без збереження заробітної плати за згодою сторін"; p.3.2.1: "за вихідний, святковий і неробочий день приймається на рівні … за попередній робочий день" | O critério "active payroll record" deixa de fora quem está no quadro sem pagamento no mês; e a regra do fim de semana não aparece em L12 (só em V12/X12) |
| 16 | M_UA_1PV_001_Spec | X12 | "maternity leave: D5 category 5 or 7 — confirmed" e, no mesmo texto, "D5 categories 7/8 are for military servicemen" | Uma das duas afirmações está errada (a categoria 7 não pode ser as duas coisas) | Contradição interna na própria célula X12 | Contradição objetiva; conferir na nota 8 do D5 (citada em X14) e corrigir |
| 17 | M_UA_1PV_001_Spec | L14 | Staff = cat. 1 + cat. 2 com flag 1; exclui só cat. 2 flag 0 e cat. 3 | Também excluir os valores apurados para mobilizados (que seguem na cat. 1), para quem está em licença-maternidade ou licença para cuidar de filho e para desligados no momento da apuração | Ver #10 (I5 p.1.5; ROZ-M I.8; LVIV-M sl.12) | Mesma lacuna do #10, agora no mapeamento do sistema |
| 18 | M_UA_1PV_001_Spec | I15, J15, R15; I16, J16, R16 | "Dropdown, reason list" / "Code + free text" / "Code + Text" | "Free text" / "Text" | X15/X16 e O15/O16: "No code list: the form has a free-text box"; XSD-M: N1, N2 `type="xs:string"` | Contradiz a própria correção da linha (O e X) e o XSD |
| 19 | M_UA_1PV_001_Spec | B16 | "Відхилення по середнйй заробітній платі" | "…по середній заробітній платі" | LVIV-M sl.13: "Середня заробітна плата штатного працівника" | Erro de grafia ("середнйй") |
| 20 | M_UA_1PV_001_Spec | I8, J8 | "5, format XX.XX" / "Numeric, dotted" | Texto, até 20 caracteres | TECH-M: "FIRM_KVED \| 20 \| Текст \| Код КВЕД" | Tipo e tamanho divergem da lista técnica oficial |
| 21 | M_Average_FTE_Headcount | A2 | "Mapping: UA-1PV-001, column U, row 1040" | "column V (BA Mapping), row 12 (1040)" | Spec U1 = "XML Element (S0301016)"; a fórmula está em V12, que remete a esta aba | Referência de coluna desatualizada (U virou coluna XML na v5.0) |
| 22 | M_Field_Options | A1 | "1-ПВ (МОНТНА)" | "1-ПВ (МІСЯЧНА)" | N117 | Palavra deturpada |
| 23 | M_Field_Options | E5 | "…since 1020/1070 = 5010's total" | A 5010 (trimestral) é o fundo só do pessoal do quadro no trimestre: ≥ soma das 1070 dos meses; não é igual à 1020 nem à 1070 | ROZ-Q IV.1: "Дані за показником щодо фонду оплати праці штатних працівників можуть бути більше або дорівнювати даним … форми № 1-ПВ (місячна) (за місяці відповідного кварталу)"; CTRL-Q nº 33: "ряд. 5010 > або = ряд. 1070 гр. 1 форми № 1-ПВ (місячна)" | A 1020 inclui quem não é do quadro; a 5010 é trimestral, exclui mobilizados e a relação é ≥, não = |
| 24 | M_File_Structure | B3 | "Кабінет ресивальниця" (Respondent's Cabinet) | "Кабінет респондента" | LVIV-Q: "онлайн-сервісу «Кабінет респондента» (https://statzvit.ukrstat.gov.ua)" | Nome do portal deturpado (Report Matrix B9 está correto) |
| 25 | M_File_Structure | B5 | "Cyrillic … portal is a modern web form, no legacy encoding constraint" | XML em windows-1251 | F31: "Кожний документ починається з директиви XML <?xml version="1.0" encoding="windows-1251"?> … Кодовою сторінкою є "windows-1251""; XSD-M e M_Sample A4 em windows-1251 | Afirmação falsa para o arquivo XML que a própria spec gera |
| 26 | M_File_Structure | B7 | "Generate the VALUES needed to fill the portal form … No schema/XSD/fixed-width validation applies." | O arquivo XML é validado contra o XSD S0301016 (o preenchimento online continua sendo um canal possível) | XSD-M (S0301016, C_DOC_VER 16); F31: "Порядок елементів у xml-документі повинен точно відповідати порядку, описаному XML-схемою"; Report Matrix B8 e Sample A2 ("Validated against Derzhstat XSD S0301016") | Contradiz o XSD oficial e o resto da spec (v4.0/v5.0) |
| 27 | M_Population_Rules | B6 | "reason-code list pending Derzhstat clarification" | Lista fechada: 34, 37, 39, 40, 42 (Field Options linhas 11–15) | ROZ-M I.9: "…за однією із наведених причин … Інші причини відсутності даних не використовуються"; REASON: 34/37/39/40/42 | Pendência já resolvida (v5.1); texto desatualizado e contraditório com Field Options |

### Trimestral

| # | Arquivo/aba | Célula | Atual | Correto | Citação da fonte | Por quê |
|---|---|---|---|---|---|---|
| 28 | Q_Version_Control | D17 (v1.4) | "column X (XML element) added to the Spec sheet" | "column U (XML element)" | Q Spec U1 = "XML Element (S0301121)"; X1 = "RA Comments" | Referência de coluna errada |
| 29 | Q_Report_Matrix | B8 | "\"Кабінет ресивальниця\" web portal" | "Кабінет респондента" | LVIV-Q (ver #24); o próprio B16 diz "Кабінет респондента" | Nome do portal deturpado; contradição interna com B16 |
| 30 | Q_Report_Matrix | B14 | "Block III here = the whole content of the monthly form's single block, at finer breakdown." | O bloco III detalha só o fundo do pessoal do quadro (≈ 1070 acumulada no trimestre); não traz 1020, 1030, 1040 nem 1060 | ROZ-Q IV.1 (ver #23); LVIV-Q: "IІІ. Склад фонду оплати праці штатних працівників" | Equivalência falsa: o bloco mensal tem quantidade de pessoas, horas, IR e fundo de todos os trabalhadores |
| 31 | Q_Payroll_Scope_Summary | A1 | "1-ПВ (КВАРТАЛьНА)" | "1-ПВ (КВАРТАЛЬНА)" | N117: "№ 1-ПВ (квартальна)" | Erro de digitação (ь minúsculo) |
| 32 | Q_Payroll_Scope_Summary | A6 | "3070 Year-end headcount (Q4 only)" | "3070 Headcount at end of reporting period (every quarter)" | ROZ-Q II.6: "облікову кількість штатних працівників на останню дату звітного періоду"; CTRL-Q nº 17: "ряд. 3070 = ряд. 3070 … попереднього звіту + ряд. 3020 … – ряд. 3040"; LVIV-Q: "Показники у ряд. 3080, 3090, 3100 не заповнюються у звітах за І, ІІ та ІІІ квартали" (a 3070 não está nessa lista) | A 3070 é trimestral; só 3080/3090/3100 (e o bloco V) são do 4º trimestre |
| 33 | Q_Payroll_Scope_Summary | C6 | "Snapshot headcount, same logic as 1040" | Lógica diferente: a 3070 é a contagem em uma data (облікова) e inclui maternidade, licença para cuidar de filho, mobilizados, contratos suspensos e licença sem vencimento sem prazo; a 1040 é uma média e exclui todos esses | ROZ-Q II.6: "…включно з працівниками, призваними … під час мобілізації … призупинено дію трудового договору … у відпустках без збереження заробітної плати без обмеження строку"; ROZ-M II.3 (1040 "крім тих…") | Equiparação errada entre os indicadores |
| 34 | Q_Payroll_Scope_Summary | A7 | "3080 … / 3090 … / 3100 …" sem marcação de período | Marcar "(Q4 only, as at 31 December)" | LVIV-Q: "ряд. 3080, 3090, 3100 … тільки раз на рік у звіті за ІV квартал"; ROZ-Q II.1: "окремих категорій штатних працівників станом на 31 грудня" | Omissão: a marcação de 4º trimestre está na 3070 (errado) e falta nestas (certo) |
| 35 | Q_UA_1PV_002_Spec | A25, B25, F25, G25 | "Year-end headcount (Q4 only)" / "Облікова кількість на кінець року" / C / "Q4/annual only" | "Headcount at end of period" / "Облікова кількість штатних працівників на кінець звітного періоду" / trimestral | ROZ-Q II.6; CTRL-Q nº 17 e 51 (ver #32) | Nome oficial e periodicidade errados (S25 = "Per Quarter" está certo e contradiz G25) |
| 36 | Q_UA_1PV_002_Spec | M25 | "Snapshot, same logic as 1040." | Ver #33 | ROZ-Q II.6 × ROZ-M II.3 | Mesmo erro do #33 |
| 37 | Q_UA_1PV_002_Spec | F26–F28; S26–S28 | F = "Y"; S = "Per Quarter" | F = "C" (só no 4º trimestre); S = "Annual (Q4 report)" | X26–X28: "Q4 only. Reported once a year as at 31 December"; LVIV-Q (ver #34) | Contradição interna com a coluna X e com a fonte |
| 38 | Q_UA_1PV_002_Spec | U25, U26, U28 | "A3070_1", "A3080_1", "A3100_1" | Também A3070_2, A3080_2, A3100_2 (coluna "у т.ч. жінки") | XSD-Q: `A3070_2`, `A3080_2`, `A3100_2`; CTRL-Q nº 5–6 (gr.1 ≥ gr.2); LVIV-Q: "У сього / У т.ч. жінки" | Omissão: a coluna 2 (mulheres) do formulário fica sem linha |
| 39 | Q_UA_1PV_002_Spec | M8 | "= 5040+5050+5051+5052+portion of 5090." | 5030 ≥ 5040+5050+5051+5052 (e, como alerta, ≥ com a 5090) | ROZ-Q IV.2: "фонду додаткової заробітної плати мають бути більше або дорівнювати сумі даних за показником щодо надбавок … премій … індексацією … компенсацій"; CTRL-Q nº 35–36 | A 5030 contém outros itens da I5 p.2.2 (ex.: 2.2.3 comissões, 2.2.4 horas extras) que não têm linha própria; a igualdade é falsa |
| 40 | Q_UA_1PV_002_Spec | L16 | "Vacation/business-trip/sick pay etc." | Férias e demais itens da I5 p.2.2.12 e 2.3.1; sem auxílio-doença e sem viagem a serviço | ROZ-Q III/IV.10: a 5090 é o que está "у підпункті 2.2.12 … та підпункті 2.3.1"; I5 p.2.1.6: "Оплата праці за час перебування у відрядженні" (fundo básico); I5 p.3.3: auxílio-doença dos 5 primeiros dias fora do фонд оплати праці | Auxílio-doença não é FOP; viagem a serviço é fundo básico (5020), não 5090 |
| 41 | Q_UA_1PV_002_Spec | L6 (vale para L6–L16, bloco III) | 5010 = 5020+5030+5060 do pessoal do quadro, sem exclusões | Excluir os valores apurados para convocados/mobilizados | ROZ-Q IV.1: "…фонду оплати праці штатних працівників (крім призваних на строкову військову службу, … під час мобілізації, на особливий період або прийнятими на військову службу за контрактом)" | Regra de exclusão ausente (mobilizados seguem na cat. 1) |
| 42 | Q_UA_1PV_002_Spec | B27 | "у відпустці вагітністю та пологах" | "у відпустці у зв'язку з вагітністю та пологами" | LVIV-Q: "які знаходяться у відпустці у зв'язку з вагітністю та пологами" | Texto truncado/agramatical |
| 43 | Q_UA_1PV_002_Spec | R18, R20, R21, R22, R25, R26, R27, R28 | "Text" | "Integer" | XSD-Q: A7010, A7030, A7040, A3070_1, A3080_1, A3090_2, A3100_1 `xs:integer`; C7010 `DGdecimal0` | Tipo de valor diverge do XSD (J dessas linhas já diz "integer") |
| 44 | Q_UA_1PV_002_Spec | L26 | "COUNT(WHERE employment_pct<100)" | Só quem tem jornada parcial pelo contrato ou por acordo; ficam de fora as jornadas reduzidas por lei | ROZ-Q II.7: "…згідно із трудовим договором прийняті на роботу на умовах неповного робочого дня (тижня) або яким надалі було встановлено неповний робочий день (тиждень) за згодою працівника"; I286 p.2.4.3: "не належать ті категорії працівників, яким відповідно до законодавства встановлюється скорочена тривалість робочого часу, зокрема: працівники, молодші 18 років; зайняті на роботах зі шкідливими умовами праці…" | Um percentual de jornada < 100 conta também quem tem jornada reduzida por lei |
| 45 | Q_Field_Options | D7 | "Instruction No.5 s.2.2.2/2.2.3" (prêmios sistemáticos → 5050) | "s.2.2.2" | ROZ-Q IV.4: "премій і винагород, що мають систематичний характер …, визначених підпунктом 2.2.2"; I5 p.2.2.3: "Відсоткові або комісійні винагороди" | Comissões (2.2.3) ficam na 5030 sem sub-linha, não na 5050 |
| 46 | Q_Field_Options | C10 | "відпустка/відрядження тощо -> row 5090 (part)" | "відпустки та інші виплати за невідпрацьований час (I5 p.2.2.12) -> row 5090"; sem відрядження | I5 p.2.1.6 (viagem a serviço = fundo básico); ROZ-Q IV.10 | Viagem a serviço classificada no lugar errado |
| 47 | Q_Field_Options | C11, D11 | "Премії/винагороди разового характеру -> row 5070" / "s.2.3.2/2.3.3" | Prêmios pontuais (I5 p.2.3.2) → só 5060; a 5070 é ajuda material sistemática (p.2.3.3) | ROZ-Q IV.8: "Показник щодо матеріальної допомоги містить дані … передбаченої підпунктом 2.3.3"; LVIV-Q: "Матеріальна допомога (із ряд.5060) 5070"; a própria Spec X13: "one-off bonuses (INCENTIVE, p. 2.3.2) have no sub-row and sit in 5060 only" | Linha de destino errada; contradiz a Spec X13 |
| 48 | Q_Field_Options | A16–E16 | "TBC / Pending / роз'яснення від 27.04.2023 / OPEN" | Códigos 34, 37, 39, 40, 42 (iguais aos do mensal); fonte: ROZ-Q I.10 | ROZ-Q I.10: as mesmas 5 causas, "Інші причини відсутності даних не використовуються"; REASON; TECH-Q: "REASON_KOD \| 2 \| Число"; XSD-Q: REASON_KOD | Pendência resolvida; a data 27.04.2023 é da Роз'яснення **mensal** antiga (a trimestral antiga é de 11.10.2023 № 19.1.2-12/33-23), e ambas perderam validade em 01.02.2025 |
| 49 | Q_File_Structure | B2 | "Web form-fill via statzvit.ukrstat.gov.ua -- same as UA-1PV-001. No byte-position layout applies." | Arquivo XML (windows-1251) no template S0301016/S0301121, validado contra o XSD, ou preenchimento online no Кабінет респондента | XSD-Q; F31 (windows-1251); Q_Report_Matrix B16 | Contradiz a Report Matrix B16 e o Sample |
| 50 | Q_File_Structure | B4 | "Row 3070 (year-end headcount) and all of Block V are ONLY populated in the Q4 filing." | "Rows 3080, 3090, 3100 and all of Block V are populated only in the Q4 filing; row 3070 every quarter." | Ver #32/#34 | Periodicidade errada (3070) e omissão de 3080–3100 |
| 51 | Q_Population_Rules | B3 | "3070 and Block V -- blank/N-A in Q1-Q3." | "3080, 3090, 3100 and Block V -- blank in Q1–Q3" | Ver #32/#34 | Mesmo erro |
| 52 | Q_Population_Rules | B4 | "Amounts: thous. UAH, 1 decimal." | Para as 8030/8040: UAH (não milhares), 2 casas decimais | LVIV-Q: "8030 … грн (із двома десятковими знаками)"; XSD-Q: A8030/A8040 `DGdecimal2` | Regra incompleta (impacto baixo: bloco V está fora do escopo) |
| 53 | Q_Sample | A26–A33 (corpo) | Sem A5040 e A5051 | Incluir `<A5040>298.2</A5040>` e `<A5051>0.4</A5051>` (exemplos da Spec K9 e K11) | Q Spec K9 = 298.2 (5040), K11 = 0.4 (5051); demais valores conferem (5010 = 4440.3 + 23756.7 = 28197.0) | O Sample não traz dois valores não nulos dos exemplos da Spec |

## (b) Não verificável (sem fonte primária nas pastas indicadas)

- **Lei nº 2524-IX, art. 10(4)** e **Ordem nº 3 de 12.01.2011 do Derzhstat** (M_Report_Matrix B8; M_File_Structure B2; Q_Report_Matrix B16): nenhuma das duas está nas fontes. A LVIV-Q confirma só que "З 1 січня 2023 року статистична та фінансова звітність подається респондентами виключно в електронній формі".
- **Prazo do mensal "até o dia 7"** (M_Report_Matrix B11; M_File_Structure B8): o texto do formulário em branco (S0301016/nakaz117) sai deturpado pela codificação da fonte do PDF; só se lê o fragmento "7-". Para o trimestral, a LVIV-Q confirma: "не пізніше 7-го числа місяця, наступного за звітним періодом".
- **Assinatura com KEP "dos responsáveis"** (M_File_Structure B4; Q_Report_Matrix B16): não consta nas fontes.
- **M Spec U15/U16 = N1/N2**: o XSD-M tem N_1, N_2, N1 e N2 sem descrição, e a lista técnica não os descreve. Não dá para confirmar qual elemento recebe cada explicação.
- **M Spec M8** ("KVED … auto-determined by the portal ('визначається автоматично')"): nos controles, essa expressão aparece só para o KATOTTG (CTRL-M nº 20). Sobre o FIRM_KVED, a TECH-M traz só "так \| =+G4", sem texto claro.
- **M Spec X10**: "Rivne oblast presentation" (só há apresentações de Lviv e Cherkasy) e "116 IN / 22 OUT / 20 pending".
- **M Spec X12**: "(Law No. 2136, art. 12)" para a licença sem vencimento sem prazo. A ROZ-M II.3 cita "без обмеження строку, встановленого частиною першою статті 26 Закону України "Про відпустки"" e não menciona a Lei 2136. Também não verificáveis aqui: o mapeamento de categorias D5 (4/5/6/7/8) e o WT 79417.
- **M Spec X14** (D5 v11, nota 8) e **Q Spec X21** (D5 col. 07): não há fonte D5 legível nas pastas.
- **M Spec M13 / M_Payroll_Scope C8** (5.440 h "exact match" com o relatório do cliente), **Q Spec M10, M27** (amostra real do 2º tri/2026): dados do cliente, não estão nas fontes.
- **Larguras de campo** (M Spec I10–I13 "9 digits + 1 decimal", "7 digits"; Q Spec J6 "N(11,1)", J18 "N(4)"): o XSD não limita o tamanho (DGdecimal1/xs:integer).
- **Q Spec X28** ("Labour Code art. 179"): o código do trabalho não está nas fontes. A parte "Instruction No.5 p. 3.2" confere.
- **M_Report_Matrix B13–B14** (4 specs UA no Drive; D6 = "seniority"): não verificável.
- **Q_Version_Control C16** = "2026-10-09 00:00:00": resto de formatação de data (as outras linhas usam AAAA-MM-DD). Não é afirmação factual.

### Observações (não contadas como erro)
- **M_Sheet1**: os 718 códigos batem linha a linha com a coluna M (Subject to PIT) da WTC V4.3: 0 divergências e nenhum código faltando. A WTC tem, porém, os códigos 79097, 79098 e 79099 **duplicados** (linhas 644–646 "Earning", PIT = Yes; linhas 717–719 "Unit", PIT = NA). Uma busca por código no Sheet1 (VLOOKUP/MATCH) devolve sempre a primeira ocorrência. O problema é da WTC, mas afeta o uso desta tabela.
- **Arredondamento da 1040**: a I286 manda arredondar pela regra do dígito par ("правилом парної цифри … якщо остання значуща цифра "5", … парна залишається без змін"). O exemplo (6,77 → 7) está certo, mas a regra não está escrita em X12/P12/Population B3. O ROUND do Excel arredonda .5 para cima (o arredondamento .5 em si está na coluna V, que não foi auditada).
- **M_Average_FTE_Headcount**: a conta está certa (203 pessoas-dia ÷ 30 = 6,77 → 7). Também estão de acordo com a I286 p.3.2.1 e p.5.5 o tratamento do desligado em 19/06 (sex) — contado até o fim de semana e excluído a partir de 22/06 — e o da admissão em domingo (K não entra em 28/06).
- **M_Sample**: A1020–A1070 = 9706.7 / 1747.2 / 37 / 5440 / 9702.4, iguais aos exemplos K10–K14 da Spec. Os controles também passam: 1030/1020 × 100 = 17,9998 ≤ 18 (CTRL-M nº 7); 1020 ≥ 1070 (nº 4); 1020 − 1070 = 4,3 (M14).
- **Linhas de 4º trimestre (verificado)**: 3080, 3090 (só a coluna de mulheres; no XSD só existe A3090_2) e 3100, além de 8010–8040 (bloco V, "станом на 31 грудня звітного року (раз на рік у звіті за IV квартал)"). A 3070 é trimestral.

## (c) Contagem de erros por aba

| Aba | Erros |
|---|---|
| M_Version_Control | 2 |
| M_Report_Matrix | 3 |
| M_Payroll_Scope_Summary | 5 |
| M_UA_1PV_001_Spec (linhas 1–16) | 10 |
| M_Average_FTE_Headcount | 1 |
| M_Sheet1 | 0 |
| M_Field_Options | 2 |
| M_File_Structure | 3 |
| M_Population_Rules | 1 |
| M_Sample | 0 |
| **Subtotal mensal** | **27** |
| Q_Version_Control | 1 |
| Q_Report_Matrix | 2 |
| Q_Payroll_Scope_Summary | 4 |
| Q_UA_1PV_002_Spec (linhas 1–30) | 10 |
| Q_Field_Options | 4 |
| Q_File_Structure | 2 |
| Q_Population_Rules | 2 |
| Q_Sample | 1 |
| **Subtotal trimestral** | **26** |
| **Total** | **53** |
