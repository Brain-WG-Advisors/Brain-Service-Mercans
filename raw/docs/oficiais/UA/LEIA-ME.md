# UA: documentos oficiais (XSD e formas): 1-ПВ e Додаток 5 (J05)

Coleta feita em 2026-10-09. Material bruto: não editar (regra do `raw/`).

## Como foi obtido (acesso bloqueado)
- **tax.gov.ua** retorna `403 Access Denied` (Akamai, bloqueio geográfico) tanto via curl quanto via WebFetch. **zakon.rada.gov.ua** e **ukrstat.gov.ua** não respondem desta máquina (timeout na porta 443). **cabinet.tax.gov.ua** também não conecta. Os sites regionais `*.ukrstat.gov.ua` (ex.: ck.ukrstat.gov.ua) respondem normalmente.
- Por isso, os arquivos de tax.gov.ua e ukrstat.gov.ua foram baixados **das cópias do Internet Archive (web.archive.org, modo `id_`, byte a byte) das URLs oficiais**. A URL de cada linha abaixo é a URL oficial original, seguida da data da captura. Não é fonte de terceiros: é o arquivo publicado pelo órgão, só que capturado pelo arquivo.
- O `.arj` da ДПС foi extraído com um decodificador ARJ escrito para isso (método 1). Os arquivos extraídos foram conferidos: XML válido e PDF íntegro.

## Arquivos baixados

### 3. Додаток 5 (J05): ДПС
| Arquivo | Origem (URL oficial) | Versão / data | Instrumento |
|---|---|---|---|
| `2026-10-09-J0500110-pacote-xsd-pdf-DPS.arj` | `https://tax.gov.ua/data/material/000/357/453385/j0500110.arj` (captura 2026-04-24) | ARJ criado em **2026-04-23**. Contém J0500110 e J0510110…J0510610 (.xsd + .pdf), todos com versão 10 | Наказ Мінфіну від 24.01.2025 № 39, зі змінами наказом Мінфіну від 30.01.2025 № 53 (texto do `xs:documentation` do XSD) |
| `2026-10-09-J0510510-dodatok5-trudovi-vidnosyny.xsd` | extraído do .arj acima | C_DOC=J05, C_DOC_SUB=105, C_DOC_VER=10 (`fixed`) | idem |
| `2026-10-09-J0510510-dodatok5-forma.pdf` | extraído do .arj acima | imagem da forma Д5 | idem |
| `2026-10-09-J0500110-podatkovyi-rozrakhunok.xsd` | extraído do .arj acima | Податковий розрахунок (formulário principal), versão 10 | idem |
| `2026-10-09-common_types-DPS.xsd` | `https://tax.gov.ua/data/material/000/357/453385/common_types.xsd` (captura 2026-04-24) | tipos comuns incluídos pelo J0510510 (e também pelos XSD do Держстат) | — |

- Capturas anteriores do mesmo arquivo: j0500110.arj em 2025-12-22 (ARJ de 2025-10-14) e j0500109.arj em 2023/2024. Não há captura de `j0500111.arj`, então a **versão 10 é a vigente** na data da coleta.
- Encoding dos XSD: `windows-1251`.

### 1 e 2. 1-ПВ (місячна) S0301016 e 1-ПВ (квартальна) S0301121: Держстат
| Arquivo | Origem (URL oficial) | Versão / data | Instrumento |
|---|---|---|---|
| `2026-10-09-S0301016-1PV-misiachna.xsd` | dentro de `https://ukrstat.gov.ua/elektr_zvit/2024/PDF_XSD_XLS_2025.zip` (captura 2025-08-09), pasta `S0301016 1-ПВ(місячна)/` | C_DOC=S03, C_DOC_SUB=010, C_DOC_VER=16. Comentário no XSD: `29.08.2024`; arquivo de 2024-09-25 | Наказ Держстату від 15.04.2024 № 117 |
| `2026-10-09-S0301016-1PV-misiachna-forma.pdf` / `-shablon.xls` / `-tekh-polia.xlsx` | mesmo zip | forma, template e mapa de campos técnicos | idem |
| `2026-10-09-S0301016-1PV-misiachna-erratum-xsd.docx` | mesmo zip | correções oficiais do XSD (FIRM_EDRPOU e KATOTTG_FACT: `xs:string`, nillable, minOccurs=0) | — |
| `2026-10-09-S0301121-1PV-kvartalna.xsd` | mesmo zip, pasta `S0301121 1-ПВ(квартальна)/` | C_DOC=S03, C_DOC_SUB=011, C_DOC_VER=21. Comentário `27.08.2024`; arquivo de 2024-09-26 | Наказ Держстату від 15.04.2024 № 117 |
| `2026-10-09-S0301121-1PV-kvartalna-forma.pdf` / `-shablon.xls` / `-tekh-polia.xlsx` / `-erratum-xsd.docx` | mesmo zip | idem (erratum também para NOMER e N2) | idem |
| `2026-10-09-nakaz117-2024-Derzhstat-1PV.htm` | `https://www.ukrstat.gov.ua/norm_doc/2024/117/117_2024.htm` (captura 2024-04-28) | Наказ № 117 de 15.04.2024: mensal a partir do relatório de **janeiro de 2025**, trimestral a partir do **1º trimestre de 2025**. Revoga o наказ № 128/2023 a partir de 01.02.2025 | — |
| `2026-10-09-nakaz117-2024-1PV-misiachna-blank.pdf` | `https://www.ukrstat.gov.ua/norm_doc/2024/117/117_mis.pdf` (captura 2024-04-26) | formulário aprovado (mensal) | наказ 117 |
| `2026-10-09-nakaz117-2024-1PV-kvartalna-blank.pdf` | `https://www.ukrstat.gov.ua/norm_doc/2024/117/117_kv.pdf` (captura 2024-04-26) | formulário aprovado (trimestral) | наказ 117 |
| `2026-10-09-Derzhstat-perelik-form-elektronni-2025-2026.htm` | `https://ukrstat.gov.ua/elektr_zvit/2023/Perelik_form_2026_.htm` (captura 2025-12-27) | lista oficial de formas eletrônicas **2025–2026**: S0301016 "зі звіту за січень 2025 року" e S0301121 "зі звіту за І квартал 2025 року". Confirma que esses templates **valem em 2026** | — |
| `2026-10-09-instruktsiia286-statystyka-kilkosti-pratsivnykiv-red2023.pdf` | `https://www.ukrstat.gov.ua/norm_doc/2023/279/279.pdf` (captura 2025-07-14) | Інструкція зі статистики кількості працівників (наказ Держкомстату 28.09.2005 № 286), texto consolidado com alterações de 05.10.2006 № 466 e **04.10.2023 № 279** (registrado no Мін'юст 19.10.2023 № 1826/40882) | — |
| `2026-10-09-1PV-misiachna-narada-GUS-Cherkasy-2026.pdf` | `https://ck.ukrstat.gov.ua/source/arch/2026/1pv_m_internet-narada.pdf` (download direto) | apresentação do ГУС у Черкаській області (órgão territorial do Держстат), 2026: código S0301016, fontes normativas e erros típicos | — |

Observações:
- Os XSD do Держстат fazem `xs:include` de `common_types.xsd`. Os tipos usados (`DGdecimal1`, `STATOBL`, `STATRAY`, `DGLong`, `DGDate`…) existem no `common_types.xsd` da ДПС salvo aqui, porque o formato é unificado.
- Nenhuma captura de um pacote `PDF_XSD_XLS_2026.zip` foi encontrada. A lista 2025–2026 mantém os mesmos códigos (S0301016 / S0301121), então o pacote 2025 é o vigente.

## O que não foi encontrado e por quê
1. **Роз'яснення do Держстат de 28.11.2024** (№ 19.1.2-12/24-24 mensal; № 19.1.2-12/25-24 trimestral, em vigor desde 01.02.2025): não localizei o arquivo oficial. ukrstat.gov.ua está inacessível e não achei captura no Internet Archive. Só há reproduções em sites privados (buhgalter.com.ua, prokadry), que não foram usadas. A resposta sobre штатні abaixo usa a forma aprovada e a Instrução 286, ambas oficiais.
2. **Інструкція зі статистики заробітної плати** (наказ № 5 de 13.01.2004, com alterações de 17.01.2023 № 15): não baixada. zakon.rada.gov.ua está bloqueado, a captura disponível vem comprimida/ilegível e a versão de ukrstat é de 2018 (sem a alteração de 2023).
3. **Página "Структура електронних документів" / "Реєстр форм" da ДПС** em versão 2026: não foi aberta (403). O pacote foi localizado pelo caminho oficial `/data/material/000/357/453385/`, o mesmo onde a ДПС publica as versões 02→10 do J05.
4. **cabinet.tax.gov.ua**: sem conexão. Não foi necessário.

## J0510510 (Додаток 5, C_DOC=J05 / C_DOC_SUB=105 / C_DOC_VER=10): elementos pedidos, conforme o XSD
Regra do XSD: elemento sem `minOccurs` é **obrigatório** (minOccurs=1) e **não** nillable. Todos estão em `xs:sequence`, então **a ordem é obrigatória**.

| Elemento | Onde | Tipo XSD | Restrição (tamanho / padrão) | Obrigatório? | nillable |
|---|---|---|---|---|---|
| C_REG | DECLARHEAD | `DGsti` (xs:integer) | 0 a 99 | Sim (minOccurs=1) | Não |
| C_RAJ | DECLARHEAD | `DGsti` (xs:integer) | 0 a 99 | Sim | Não |
| C_STI_ORIG | DECLARHEAD | `DGc_dpi` (xs:integer) | pattern `((3070)\|(3[1-5]00)\|(9001)\|(9191)\|(9393)\|(9494)\|(9900)\|(9911)\|(9970)\|(999[1-9])\|(2[0-8][0-9]{2})\|(1[0-9]{3})\|([1-9][0-9]{2}))`, ou seja, 3 ou 4 dígitos (código do órgão ДПС) | Sim | Não |
| C_DOC_STAN | DECLARHEAD | `DGSTAN` (xs:integer) | 1 a 3 | Sim | Não |
| D_FILL | DECLARHEAD (depois de LINKED_DOCS) | `DGDate` (xs:string) | length=8, `ddmmyyyy` com validação de calendário (anos 19xx/20xx) | Sim | Não |
| SOFTWARE | DECLARHEAD (último) | xs:string | sem restrição | Não (minOccurs=0) | **Sim** |
| HZ | DECLARBODY (1º, dentro de `xs:choice`) | `DGchk` (xs:int) | enumeração única `1` | **Exatamente um** entre HZ / HZN / HZU (o choice não é opcional) | Não |
| HZN | idem | `DGchk` | `1` | idem | Não |
| HZU | idem (em sequência com HTIN1 e HFIL, opcionais e nillable) | `DGchk` | `1` | idem | Não |
| HDDGV | DECLARBODY (depois de HNAME) | `DGDate` | `ddmmyyyy`, length=8 | Não (minOccurs=0) | **Sim** |
| HNDGV | DECLARBODY | xs:string | sem restrição | Não (minOccurs=0) | **Sim** |
| HFILL | DECLARBODY (rodapé, 1º) | `DGDate` | `ddmmyyyy`, length=8 | Sim | Não |
| HKBOS | DECLARBODY (rodapé) | `DGDRFO_10` (xs:string) | maxLength=10; pattern `([0-9]{10}\|[АБВГДЕЄЖЗИІКЛМНОПРСТУФХЦЧШЩЮЯ]{2}[0-9]{6}\|[0-9]{9})` (РНОКПП de 10 dígitos, série+nº de passaporte ou ID-card de 9 dígitos) | Sim | Não |
| HBOS | DECLARBODY (rodapé) | `DGHBOS` (xs:string) | minLength=1 | Sim | Não |
| HKBUH | DECLARBODY (rodapé) | `DGDRFO_10` | igual a HKBOS | Não (minOccurs=0) | **Sim** |
| HBUH | DECLARBODY (rodapé, último) | `DGHBUH` (xs:string) | minLength=1 | Não (minOccurs=0) | **Sim** |

Ordem do cabeçalho: `TIN, C_DOC, C_DOC_SUB, C_DOC_VER, C_DOC_TYPE, C_DOC_CNT, C_REG, C_RAJ, PERIOD_MONTH, PERIOD_TYPE, PERIOD_YEAR, C_STI_ORIG, C_DOC_STAN, LINKED_DOCS?, D_FILL, SOFTWARE?`.
Ordem do corpo: `(HZ | HZN | HZU [HTIN1] [HFIL]), HZY, HZM, HNAME, HDDGV?, HNDGV?, HTIN, T1RXXXXG5 … T1RXXXXG20 (0..999999 cada), HFILL, HKBOS, HBOS, HKBUH?, HBUH?`.
Outros do corpo: HZY `DGYear` 1981–2099; HZM `DGMonth` 1–12; HNAME minLength 1; HTIN `DGHTINJ` (ЄДРПОУ, 5 a 10 dígitos); HTIN1 `DGLong`; HFIL inteiro de 1 a 99999999. Todos obrigatórios, exceto HTIN1 e HFIL.

## 1-ПВ: as linhas de número médio e de fundo de salário referem-se só a штатні працівники?
**Depende da linha. Mensal: sim para 1040 e 1070; não para 1020/1030. Trimestral: sim para todas as linhas de número médio e de ФОП, exceto 7030/7040, que tratam justamente dos não-штатні.**

Pela forma aprovada (наказ № 117 de 15.04.2024; blanks e XSD acima):
- **1-ПВ (місячна), S0301016**:
  - ряд. **1040** "Середньооблікова кількість штатних працівників" (A1040): só штатні.
  - ряд. **1070** "Фонд оплати праці штатних працівників (із ряд.1020)" (A1070): só штатні.
  - ряд. **1020** "Фонд оплати праці **усіх** працівників" (A1020): штатні + сумісники + ЦПД. O ГУС Черкаси (2026) explica: "Рядок 1020 містить дані про суму нарахованого фонду оплати праці усіх працівників … зокрема штатних працівників (рядок 1070); тих, що працюють за сумісництвом; осіб, які виконують роботи за цивільно-правовими договорами". Pagamentos a mobilizados vão **só** na 1020.
  - ряд. **1030** (ПДФО) segue a base da 1020.
- **1-ПВ (квартальна), S0301121**:
  - Seção I (3020–3100): "Кількість штатних працівників" (movimento e облікова кількість).
  - Seção III (5010–5090): "Склад фонду оплати праці **штатних** працівників", com 5010 = 5020 + 5030 + 5060.
  - Seção IV: ряд. **7010** "Із середньооблікової кількості штатних працівників: жінки"; ряд. **7030** "зовнішні сумісники" e **7040** "працюють за цивільно-правовими договорами", agrupados como "Працівники, які не перебувають в обліковому складі (позаштатні)", cada um com sua própria середньооблікова кількість, ФОП e людиногодини.

Pela Інструкція зі статистики кількості працівників (наказ 286/2005, red. 04.10.2023 № 279):
- **п. 2.1**: entram na облікова кількість штатних працівників todos os empregados com contrato de trabalho escrito.
- **п. 2.6.1 e 2.6.2**: não entram na облікова кількість штатних os "прийняті на роботу за сумісництвом з інших підприємств" (externos) nem os "залучені до виконання робіт за цивільно-правовими договорами". O sumisnyk interno conta como uma pessoa física.
- **п. 1.8**: o indicador de середньооблікова кількість штатних conta o trabalhador "тільки один раз (за місцем основної роботи)". Já o indicador de "загальна кількість працівників" inclui também os сумісники externos e os ЦПД.
- **п. 3.1**: середня кількість працівників = середньооблікова штатних + середня зовнішніх сумісників + середня працюючих за ЦПД.
- **п. 3.2.2**: a середньооблікова кількість штатних exclui quem está em licença-maternidade ou licença para cuidado de filho. As orientações de 2026 do ГУС Черкаси também excluem os mobilizados/militares e os com contrato suspenso.
