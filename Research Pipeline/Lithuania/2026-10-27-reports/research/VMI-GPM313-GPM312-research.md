# VMI — GPM313 e GPM312: research pack de fontes oficiais (2026)

Data da coleta: 2026-10-27. Coletado por: janela Pipeline (agente de research).
Escopo: GPM313 (declaração mensal do GPM retido) e GPM312 (declaração anual das rendas pagas, com anexos GPM312L e GPM312U). Sem comparação com as specs internas.

**Como ler as citações:**
- `IN313-2026 §x` = `IN_GPM313_nuo_2026` (Aprašas do GPM313 vigente a partir de 2026), ponto x.
- `IN312 §x` = `IN_GPM312` (Taisyklės do GPM312, redação VA-24 de 2026-03-26), ponto x. `IN312 1 pr.` / `2 pr.` = anexos 1 e 2 dessas Taisyklės.
- `MXFD313` / `MXFD312` = arquivos do formulário eletrônico (`GPM313.mxfd`, `GPM312.mxfd`) baixados do EDS da VMI.
- `EDS-lista` = lista oficial de formulários do EDS (`deklaravimas.vmi.lt/lt/Formu_sarasas.aspx`), filtrada pelo código do formulário.

**Ressalva de fonte:** os textos das regras vieram do **EDS da VMI** (pacote "instrukcijos" de cada formulário), não do e-tar/e-seimas. Esses dois portais e o vmi.lt devolvem 403 (Cloudflare) a script. O número e a data dos atos e a redação constam no cabeçalho dos próprios documentos da VMI. Conferir no e-seimas/e-tar o texto consolidado e a data de entrada em vigor (ver "Precisa de navegador").

---

## 1. Fontes

Pasta: `C:\Users\instituto\Documents\brain-service\raw\docs\oficiais\LT\2026-10-27-VMI-reports\`. Todos os arquivos foram baixados em 2026-10-27 do EDS (`https://deklaravimas.vmi.lt/lt/Formu_sarasas.aspx?...`).

| # | Arquivo | URL de origem | Data/versão | md5 |
|---|---|---|---|---|
| F1 | `GPM313_mxfd.zip` → `x_GPM313_mxfd/GPM313.mxfd` | `…/Formu_sarasas.aspx?downloadmxfd=eb03e9ef-39b0-457f-8264-79e86f053009` | GPM313 v.1; EDS "Versija 2025-12-31"; MXFD `CreatedOn="2025-11-04"`, FormDefId `{EB03E9EF-39B0-457F-8264-79E86F053009}` | zip `dd3200bbb2a3c9e70d4a48da62b43de9`; mxfd `1108dc95681871ddeabd045eb3684d31` |
| F2 | `IN_GPM313_DOC.zip` → `x_IN_GPM313_DOC/IN_GPM313_nuo_2026.docx` (+ `…nuo_2022_iki_2025.docx`, `…nuo_2018_iki_2021.docx`) | `…/Formu_sarasas.aspx?downloadinstructionsmswordzip=eb03e9ef-39b0-457f-8264-79e86f053009` | Aprašas GPM313, VA-121 (2017-12-20), últimas alterações VA-105 (2025-11-20) | zip `faa1e85f69255290c019114701b07173`; 2026 docx `794dc24ec133564346d8839e37290476`; 2022–25 docx `c3d67c83c99de89752e6554006a15fb6`; 2018–21 docx `ac4cc0ef7b519e93e6bccd64b9c72966` |
| F3 | `IN_GPM313_PDF.zip` → `x_IN_GPM313_PDF/*.pdf` (mesmas 3 versões em PDF) | `…/Formu_sarasas.aspx?downloadinstructionspdfzip=eb03e9ef-39b0-457f-8264-79e86f053009` | igual a F2 | zip `9b3512ef12adf6f650788b202e9fb204`; 2026 pdf `fe9f5e1bf921e5c8b369453d9905ee28` |
| F4 | `GPM312_mxfd.zip` → `x_GPM312_mxfd/GPM312.mxfd` | `…/Formu_sarasas.aspx?downloadmxfd=dd0f88dd-a858-4595-af2f-3643d0069a39` | GPM312 v.1; EDS "Versija 2026-06-12"; MXFD `CreatedOn="2026-05-11"`, FormDefId `{DD0F88DD-A858-4595-AF2F-3643D0069A39}` | zip `0ea0d014a7df6d13b49a77b392526327`; mxfd `03514e02dbe17a9d1e5c0ded9dc2f5f6` |
| F5 | `IN_GPM312.pdf` | `…/Formu_sarasas.aspx?downloadinstructionspdf=dd0f88dd-a858-4595-af2f-3643d0069a39` | Taisyklės GPM312, VA-9 (2018-02-06), redação VA-24 (2026-03-26); 22 páginas | `fd56520504fe91b94489826d2a47c449` |
| F6 | `IN_GPM312_DOC.zip` → `x_IN_GPM312_DOC/IN_GPM312.docx` | `…/Formu_sarasas.aspx?downloadinstructionsmswordzip=dd0f88dd-a858-4595-af2f-3643d0069a39` | igual a F5 (mesmo cabeçalho) | zip `f931e625af013a16e7b9bee0954e6087`; docx `edc98185c1e1171b459a604e55f9bec1` |
| F7 | `EDS_Formu_sarasas_filtro_GPM313_2026-10-27.html` | `https://deklaravimas.vmi.lt/lt/Formu_sarasas.aspx` (postback com filtro "GPM313") | snapshot de 2026-10-27 | `80efa1cd30f6ed401fdda879010ec4a4` |
| F8 | `EDS_Formu_sarasas_filtro_GPM312_2026-10-27.html` | idem (filtro "GPM312") | snapshot de 2026-10-27 | `4a43ce6340efdb0b3c9a5be54a0fea1a` |
| F9 | `EDSUplaodFileViaWebService-v2-2010_08_19.doc` | `https://deklaravimas.vmi.lt/lt/Apie_formu_teikima/Apie_formu_teikima_1/CMSDownloadHandler.ashx?filekey=d0cc4698-edad-4835-a554-b81283850ee0` (página "Žiniatinklio paslauga") | 2010-08-19 (doc técnico do upload por web service; não lido em detalhe) | `aae02f129a57b2deff1253955a0bf8fa` |

Linhas do EDS-lista (F7/F8), lidas em 2026-10-27:
- `GPM313 v.1 | Mėnesinė pajamų mokesčio deklaracija | Versija 2025-12-31 | nuo: 2018-01-01 | Teikiama tik elektroniniu būdu už 2018 m. ir vėlesnius mokestinius laikotarpius.`
- `GPM312 v.1 | Metinė gyventojams išmokėtų išmokų, priskiriamų A ir B klasės pajamoms, deklaracija | Versija 2026-06-12 | nuo: 2018-01-01 | Išmokų natūra deklaravimas`

---

## 2. GPM313: Mėnesinė pajamų mokesčio deklaracija

### 2.1 Ato, versão e vigência
| Item | Valor | Fonte |
|---|---|---|
| Ato que aprova o formulário e o Aprašas | Ordem do diretor da VMI de **2017-12-20 nº VA-121** ("Dėl Mėnesinės pajamų mokesčio deklaracijos GPM313 formos ir jos užpildymo ir pateikimo taisyklių patvirtinimo") | IN313-2026, cabeçalho; título do ato citado em IN312 §65 |
| Última alteração | Ordem **2025-11-20 nº VA-105** ("Paskutiniai pakeitimai 2025 11 20 įsakymu Nr. VA-105"). Com ela, o documento passou de "Taisyklės" a "**Tvarkos aprašas**" | IN313-2026, cabeçalho e §1 |
| Texto aplicável a 2026 | Pacote do EDS com três textos: `nuo_2018_iki_2021`, `nuo_2022_iki_2025` (alt. VA-2 de 2022-01-04) e **`nuo_2026`** | F2 (nomes dos arquivos) |
| Código/versão do formulário | **GPM313 v.1**, versão de arquivo EDS **2025-12-31**, válido "nuo 2018-01-01" | F7 |
| MXFD | criado em 2025-11-04 (ABBYY eFormDesigner 2.5). Histórico FormDefsHistory: 2018-01-05 … 2024-11-25 | F1 (`<FormDef … CreatedOn="2025-11-04">`) |
| Dispositivo legal do prazo | GPMĮ art. 24 §2 (citado pelo Aprašas, não lido no original) | IN313-2026 §12 |

### 2.2 Quem entrega, periodicidade e prazo
- **Quem:** entidades lituanas, estabelecimentos permanentes de entidades estrangeiras e pessoas residentes/não residentes com atividade individual por base fixa que, no mês, pagaram rendas de classe A a residentes ou não residentes. Também quem pagou rendas de classe B e reteve GPM sem obrigação legal de reter. (IN313-2026 §3.1–3.2)
- **Entrega mesmo sem pagamento:** quem teve empregados com contrato de trabalho no mês entrega mesmo sem pagamentos tributáveis; os campos ficam vazios ou com zero. (IN313-2026 §4)
- **Fora da declaração:** rendas de emprego pagas a residentes por trabalho em país com tratado, quando houver prova de imposto pago lá e a dupla tributação for eliminada. (IN313-2026 §5)
- **Periodicidade e prazo:** mensal, "iki kito mėnesio 15 dienos" (até o dia 15 do mês seguinte). (IN313-2026 §12)
- **Canal:** somente eletrônico, pelo EDS (`deklaravimas.vmi.lt`), conforme as regras de uso do EDS (VA-72 de 2021-10-26) e as regras de entrega VA-135 de 2004-07-09. (IN313-2026 §6, §13, §14)
- **Unidades:** entidade com filiais em outros municípios entrega uma declaração única. (IN313-2026 §15)
- **Falência ou reestruturação:** entrega em até 30 dias do início do processo. **Liquidação:** até o fim da atividade. (IN313-2026 §16–17)

### 2.3 Campos

Todos os campos estão numa única página (`PageDataDef Name="GPM313"`). Nome XML = `FieldName` do MXFD. O tamanho é o número de células do formulário. Os valores monetários têm 2 casas decimais e mínimo 0. (F1)

| Nº | Nome XML | Rótulo no formulário (lituano) | Descrição (pt-BR) | Tipo / formato | Obrigatório | Fonte |
|---|---|---|---|---|---|---|
| — | `B_FormNr` | (cabeçalho) | Código do formulário | Text, 6 células, somente leitura | não | F1 |
| — | `B_FormVerNr` | "Versija" | Versão do formulário | Text, 2 células, somente leitura | não | F1 |
| 1 | `B_MM_ID` | Išmokas išmokėjusio asmens identifikacinis numeris (kodas) | Código do pagador no registro de contribuintes; filial ou representação de entidade estrangeira usa o código do Registro de Pessoas Jurídicas | Decimal, 0 casas, 11 células | **sim** | IN313-2026 §7.1; F1. O script do MXFD rejeita comprimento diferente de 9, 10 ou 11 dígitos |
| 2 | `B_MM_Pavadinimas` | Išmokas išmokėjusio asmens pavadinimas / vardas, pavardė | Razão social, ou nome e sobrenome se pessoa física | Text, 58×2 células | **sim** | IN313-2026 §7.2; F1 |
| 3 | `B_ML_Metai` | Metai | Ano a que se refere a declaração | Decimal, 4 células; lista 2021–2026 | **sim** | IN313-2026 §8; F1 |
| 4 | `B_ML_Menuo` | Mėnuo | Mês a que se refere a declaração | Decimal, 2 células; lista 1–12 | **sim** | IN313-2026 §8; F1 |
| — | (seção) | "Duomenys apie su darbo santykiais ir jų esmę atitinkančiais santykiais susijusias A klasės išmokas" | Rendas classe A ligadas a relação de emprego | — | — | F1; IN313-2026 §9 |
| 5 | `G5` | Išmokų, neatėmus NPD, GPM, VSDĮ ir PSDĮ, suma | Total do mês das rendas de emprego classe A tributáveis, sem deduzir NPD, GPM, VSD e PSD. Inclui a indenização do empregador pelos 2 primeiros dias de doença. Pagamentos do Garantinio fondo entram somados ao GPM, VSD e PSD devidos | Decimal(14), 2 casas | não | IN313-2026 §9.1; F1 |
| 6 | `G6` | Išskaičiuota ir / arba … lėšomis sumokėta GPM … iki mėnesio 15 d., suma | GPM retido sobre as rendas de emprego **pagas até o dia 15** (inclusive) | Decimal(14), 2 casas | não | IN313-2026 §9.2; F1 |
| 7 | `G7` | … po mėnesio 15 d. iki paskutinės mėnesio dienos, suma | GPM retido sobre as rendas de emprego **pagas do dia 16 ao último dia** do mês | Decimal(14), 2 casas | não | IN313-2026 §9.3; F1 |
| — | (seção) | "Duomenys apie su darbo santykiais … nesusijusias A klasės išmokas" | Rendas classe A não ligadas a relação de emprego | — | — | F1; IN313-2026 §10 |
| 8 | `G8` | Išmokų, neatėmus GPM ir VSDĮ, suma | Total das rendas classe A não ligadas a emprego, sem deduzir GPM, VSD e PSD | Decimal(14), 2 casas | não | IN313-2026 §10.1; F1 (o rótulo diz "GPM ir VSDĮ"; o §10.1 diz "GPM, VSD ir PSD") |
| 9 | `G9` | … iki mėnesio 15 d., suma | GPM retido sobre essas rendas pagas até o dia 15 | Decimal(14), 2 casas | não | IN313-2026 §10.2; F1 |
| 10 | `G10` | … po mėnesio 15 d. iki paskutinės mėnesio dienos, suma | GPM retido sobre essas rendas pagas depois do dia 15 | Decimal(14), 2 casas | não | IN313-2026 §10.3; F1 |
| — | (seção) | "Duomenys apie B klasės išmokas, nuo kurių išskaičiuotas ir / arba … sumokėtas GPM" | Rendas classe B com GPM retido ou pago pelo pagador | — | — | F1; IN313-2026 §11 |
| 11 | `G11` | Išmokų, neatėmus GPM, suma | Total das rendas classe B com GPM retido (sem obrigação legal), sem deduzir o GPM | Decimal(14), 2 casas | não | IN313-2026 §11.1; F1 |
| 12 | `G12` | Išskaičiuota ir / arba … sumokėta GPM nuo per mėnesį išmokėtų B klasės išmokų suma | GPM retido ou pago sobre essas rendas B. Se pago em mês posterior, entra na declaração do mês do pagamento da renda | Decimal(14), 2 casas | não | IN313-2026 §11.2; F1 |

Validações do formulário eletrônico (script do MXFD, F1; avisos ou erros):
- comprimento do campo 1;
- ano obrigatório;
- mês entre 1 e 12;
- aviso quando a renda é menor que o imposto (G5, G8, G11);
- aviso quando os campos 5–12 ficam vazios ("nada pago, nada retido");
- aviso de que rendas isentas não se declaram.

### 2.4 Códigos de renda e alíquotas (GPM313)
- **O GPM313 não usa códigos de tipo de renda.** Só tem totais por grupo: emprego A, não emprego A e B. (F1: só os campos G5–G12; IN313-2026 §9–11)
- **Alíquotas de 2026 citadas no Aprašas** (IN313-2026 §9.4–9.6 e §10.4–10.6):

| Grupo | Faixa (VDU = salário médio nacional usado na base do VSD do ano corrente) | Alíquota | Fonte |
|---|---|---|---|
| Doença (inclui os 2 primeiros dias pagos pelo empregador), maternidade, paternidade, cuidado de filho, *ilgalaikio darbo išmoka* | qualquer valor | 15% | §9.4 |
| Rendas de emprego (demais) | até 36 VDU | 20% | §9.5.1 |
| idem | > 36 VDU e até 60 VDU | 25% | §9.5.2 |
| idem | > 60 VDU | 32% | §9.5.3 |
| Dividendos; parcela de seguro de vida e de fundo de pensão igual às contribuições deduzidas | qualquer valor | 15% | §10.4.1 |
| Tantjemos e remuneração de conselho; direitos autorais pagos pelo empregador; dirigente de MB não membro; madeira e resíduos em atividade individual; atividade individual de esporte ou artista | ≤36 / 36–60 / >60 VDU | 20 / 25 / 32% | §10.4.2 |
| Venda de resíduos fora de atividade individual (residente) | ≤12 / 12–36 / 36–60 / >60 VDU | 5 / 20 / 25 / 32% | §10.4.3 |
| Outras rendas A não listadas | ≤12 / 12–36 / 36–60 / >60 VDU | 15 / 20 / 25 / 32% | §10.4.4 |

- **Progressividade a pedido:** se o empregado ou beneficiário pedir, aplicam-se as alíquotas progressivas do GPMĮ art. 6 sobre o total do ano (§9.6 e §10.5). **Tratado:** a alíquota do tratado vale para não residente com certificado de residência (§10.6).
- **Mudança em 2026:** o Aprašas de 2022–2025 não tinha a faixa de 25% nem a estrutura 36/60 VDU (confere no diff entre `nuo_2022_iki_2025` e `nuo_2026`, F2). A redação de 2026 vem da VA-105 de 2025-11-20.

### 2.5 Formato eletrônico
- O formulário é preenchido no EDS (portal) ou importado como arquivo FFData gerado a partir do MXFD. O MXFD declara `FFDataCollectServer="https://deklaravimas.vmi.lt/EDSMdocUploadService/MdocUploadService.svc"` e `URLUpdateForm="http://deklaravimas.vmi.lt/PublicServiceREST"`. (F1)
- Nomes dos campos para o XML: ver a tabela 2.3 (`B_MM_ID`, `B_MM_Pavadinimas`, `B_ML_Metai`, `B_ML_Menuo`, `G5`…`G12`, `B_FormNr`, `B_FormVerNr`). Página/schedule: `GPM313`. (F1)
- Versão: **GPM313 v.1**, arquivo de 2025-12-31 no EDS. (F7)
- **XSD do FFData:** NOT LOCATED. Não há XSD no pacote do formulário; a estrutura do FFData está implícita no MXFD.

### 2.6 Correção (tikslinimas)
- Corrige-se entregando uma **nova declaração completa do mesmo mês** (IN313-2026 §18).
- **É obrigatório corrigir** quando chega aviso da VMI (*informacinis pranešimas*) ou quando o próprio pagador acha erro (§19).
- **Erros que não se corrigem depois do fim do ano fiscal:**
  - GPM retido a mais (§19.2.1);
  - GPM a mais ou a menos por erro de NPD em renda de emprego de residente (§19.2.2).
- **Prazos:** o do aviso; por iniciativa própria, os da Lei de Administração Tributária (§20).
- **Dupla tributação (tratado):** a eliminação no mesmo ano é feita por declaração corrigida do mês do pagamento (§21).
- **Ligação com o GPM312:** se a correção do GPM312 mudar totais já declarados no GPM313 do mês, o GPM313 desse mês também tem de ser corrigido (IN312 §65).

---

## 3. GPM312: declaração anual (+ GPM312L, GPM312U)

### 3.1 Ato, versão e vigência
| Item | Valor | Fonte |
|---|---|---|
| Ato que aprova o formulário e as Taisyklės | Ordem do diretor da VMI de **2018-02-06 nº VA-9** | IN312, cabeçalho; rótulo do formulário em F4 |
| Redação vigente | "**2026 m. kovo 26 d. įsakymo Nr. VA-24 redakcija**" (2026-03-26). Data de entrada em vigor: NOT LOCATED (ver Precisa de navegador) | IN312 e F5, cabeçalho; F4, texto do formulário |
| Código/versão do formulário | **GPM312 v.1**, versão de arquivo EDS **2026-06-12**, válido "nuo 2018-01-01" | F8 |
| MXFD | criado em 2026-05-11. Histórico com 2026-01-08, 2026-04-16 e 2026-04-24 | F4 |
| Anexos | **GPM312L** (residentes, *nuolatiniai*) e **GPM312U** (não residentes, *nenuolatiniai*) | IN312 §1 |
| Dispositivos legais do prazo | GPMĮ art. 24 §2 e art. 33 §2 (citados, não lidos no original) | IN312 §57 |

### 3.2 Quem entrega, periodicidade e prazo
- **Quem:**
  - quem pagou no ano rendas classe A, tributáveis ou isentas, a residentes ou não residentes (§3.1);
  - entidades que pagaram rendas classe B (§3.2);
  - bancos e associações de direitos autorais como intermediários de dividendos, juros e direitos vindos do exterior (§4);
  - operadores de jogos, a partir de 2025-11-01, para apostas e prêmios acima de 1 000 EUR por dia (§5);
  - pagadores de dividendos de 2025-01-01 a 2025-06-30 e de juros a intermediários que não revelam os beneficiários (§6);
  - quem pagou a não residentes, mesmo renda que não é objeto de imposto (§7).
- **Dispensa:**
  - só rendas A isentas do 1 priedas;
  - rendas B de até 100 EUR (produtos florestais, outros bens);
  - loterias de até 1 000 EUR;
  - juros de mora agrícolas.
  
  (IN312 §8–9)
- **Dados que vêm por outra via (não pelo GPM312):** benefícios do Sodra e do Garantinio fondo, seguro de vida, juros e títulos de bancos. (§10)
- **Periodicidade e prazo:** anual, "**iki kito mokestinio laikotarpio vasario 15 d.**" (até 15 de fevereiro do ano seguinte). (IN312 §57)
- **Canal:** somente eletrônico pelo EDS (§11, §59). Declaração única por entidade (§60). Falência, reestruturação e liquidação seguem o §61–62.

### 3.3 Campos — formulário principal GPM312 (página `GPM312`, F4)
| Nº | Nome XML | Rótulo (lituano) | Descrição (pt-BR) | Tipo / formato | Obrigatório | Fonte |
|---|---|---|---|---|---|---|
| — | `B_FormNr`, `B_FormVerNr` | "Versija" | Código e versão do formulário | Text 6 e 2 células, somente leitura | não | F4 |
| 1 | `B_MM_ID` | Išmokas išmokėjusio asmens identifikacinis numeris (kodas) | Código do pagador; filial ou representação estrangeira usa o código JAR | Decimal, 11 células | **sim** | IN312 §12.1; F4 |
| 2 | `B_MM_Pavad` | Išmokas išmokėjusio asmens pavadinimas / vardas, pavardė | Nome do pagador | Text 58×2 | **sim** | IN312 §12.2; F4 |
| 3 | `B_ML_Metai` | Mokestinis laikotarpis | Ano fiscal | Decimal 4; lista 2020–2026 | **sim** | IN312 §13; F4 |
| 4 | `G4` | Bendra išmokų, neatėmus NPD, GPM, VSDĮ ir PSDĮ, suma | Soma de todos os L8 e U8 (as apostas de jogo não entram) | Decimal(14), 2 casas | não (calculado) | IN312 §14; F4 |
| 5 | `G5` | Bendra išskaičiuota GPM suma | Soma de L10 e U10 | Decimal(14), 2 casas | não (calculado) | IN312 §15; F4 |
| 6 | `G6` | Bendra išmokas išmokėjusio asmens lėšomis sumokėta GPM suma | Soma de L11 e U11 | Decimal(14), 2 casas | não (calculado) | IN312 §16; F4 |
| 7 | `G7` | Bendra užsienio valstybėse sumokėta GPM suma | Soma de L13 | Decimal(14), 2 casas | não (calculado) | IN312 §17; F4 |

### 3.4 Anexo GPM312L: rendas pagas a residentes (página `GPM312L`; 10 linhas por folha, campos `Lk-1`…`Lk-10`; F4)
Cabeçalho da folha: `LapoNr` ("Lapo numeris", Decimal 7, nº sequencial da folha, IN312 §21). `B_MM_ID` (1) e `B_ML_Metai` (3) são copiados do formulário principal (somente leitura, IN312 §22).

| Campo | Nome XML (linha n) | Rótulo (legenda do formulário) | Descrição (pt-BR) | Tipo / valores | Fonte |
|---|---|---|---|---|---|
| L1 | `L1-n` | identifikacinis numeris (kodas) | Código do beneficiário. Na ordem: código de contribuinte; 8 primeiros caracteres do *verslo liudijimas*; código de IVA com "LT"; nº da *individualios veiklos pažyma*; passaporte (série + espaço + número), cartão de identidade ou autorização de residência | Text 20 | IN312 §23; F4 |
| L2 | `L2-n` | identifikacinio numerio (kodo) rūšis | Tipo do código em L1: 1 contribuinte; 2 verslo liudijimas; 3 IVA; 4 pažyma; 5 passaporte, ID ou autorização de residência | Text 1; lista 1–5 | IN312 §24; F4 |
| L3 | `L3-n` | vardas, pavardė | Nome e sobrenome (todos, se couber) | Text 34 | IN312 §25; F4 |
| L4 | `L4-n` | išmokos klasė | Classe da renda (A/B) conforme o 2 priedas; vazio na linha de apostas de jogo | Text 1; lista A, B | IN312 §26; F4 |
| L5 | `L5-n` | išmokos rūšis | Código do tipo de renda (2 priedas). Os 2 primeiros dias de doença vão no código 03. Apostas de jogo: 42 | Text 2; lista de 64 códigos | IN312 §27; F4 |
| L6 | `L6-n` | išmoka natūra | Só para renda em espécie: **A** = uso pessoal de carro de terceiro; **N** = outras. Parte em dinheiro vai em linha separada | Text 1; lista A, N | IN312 §28; F4 |
| L7 | `L7-n` | išmokos požymis | Marcador: **D** = atividade individual paga por quem é empregador do beneficiário; **M** = MB a membro por contrato civil (limite de 100 000 EUR/ano); **P** = arrendamento de terra (código 23); **C** = apostas pagas a operador de jogos | Text 1; lista D, M, P, C | IN312 §29; F4 |
| L8 | `L8-n` | išmokos, neatėmus NPD, GPM, VSDĮ ir PSDĮ, suma | Valor no ano, em EUR e centavos: A tributável (bruto), A isenta, B (bruto de GPM), apostas. Classe, tipo e alíquota diferentes vão em linhas separadas. Sem IVA. Renda de emprego no exterior com dupla tributação eliminada entra como A isenta, com L13 | Decimal 12, 2 casas | IN312 §30; F4 |
| L9 | `L9-n` | GPM tarifas | Alíquota aplicada (preencher mesmo se o GPM der zero pelo NPD). **0** para isentas, B sem retenção, intermediário e apostas | Decimal 5, 2 casas; lista 0; 5; 15; 20; 25; 27; 32. Em 2026 o script aceita 0/5/15/20/25/32 | IN312 §31; F4 |
| L10 | `L10-n` | išskaičiuota GPM suma | GPM retido no ano (EUR e centavos); 0 ou vazio nos casos do §32.2 | Decimal 11, 2 casas | IN312 §32; F4 |
| L11 | `L11-n` | išmokas išmokėjusio asmens lėšomis už gyventoją sumokėta GPM suma | GPM pago com recursos do pagador; numa linha só se parte foi retida e parte paga pelo pagador | Decimal 11, 2 casas | IN312 §33; F4 |
| L12 | `L12-n` | užsienio valstybės kodas | País: de origem da renda (intermediário) ou onde foi pago o imposto sobre trabalho no exterior. Se preenchido neste caso, L13 é obrigatório | Text 2; lista de países (UE / DTT / "tikslinės teritorijos") | IN312 §34; F4 |
| L13 | `L13-n` | užsienio valstybėje sumokėta GPM suma | Imposto pago no exterior sobre renda de emprego (EUR e centavos); 0 se não pago. Exige documento comprobatório junto com a declaração | Decimal 11, 2 casas | IN312 §35; F4 |

### 3.5 Anexo GPM312U: rendas pagas a não residentes (página `GPM312U`; 5 linhas por folha, campos `Uk-1`…`Uk-5`; F4)
Cabeçalho: `LapoNr`, `B_MM_ID` e `B_ML_Metai`, copiados do formulário principal (IN312 §40–41).

| Campo | Nome XML | Rótulo | Descrição (pt-BR) | Tipo / valores | Fonte |
|---|---|---|---|---|---|
| U1 | `U1-n` | identifikacinis numeris (kodas) | Código LT do beneficiário: contribuinte, verslo liudijimas, IVA "LT…", pažyma, autorização de residência ou código da entidade intermediária. Pode ficar vazio se não houver dado | Text 20 | IN312 §42; F4 |
| U2 | `U2-n` | identifikacinio numerio (kodo) rūšis | 1 contribuinte; 2 verslo liudijimas; 3 IVA; 4 pažyma; 5 autorização de residência; **6** código de entidade LT ou estrangeira. Vazio se U1 vazio | Text 1; lista 1–6 | IN312 §43; F4 |
| U3 | `U3-n` | vardas, pavardė | Nome e sobrenome | Text 34 | IN312 §44; F4 |
| U4 | `U4-n` | išmokos klasė | A/B; vazio na linha de apostas | Text 1; A, B | IN312 §45; F4 |
| U5 | `U5-n` | išmokos rūšis | Código do 2 priedas (doença dos 2 primeiros dias = 03; apostas = 42) | Text 2; 64 códigos | IN312 §46; F4 |
| U6 | `U6-n` | išmoka natūra | A ou N, como em L6 | Text 1 | IN312 §47; F4 |
| U7 | `U7-n` | išmokos požymis | D, M, P, C, como em L7, e **U** (novo para 2026+): trabalho no exterior (código 01), artista ou esportista no exterior (52/51), imóvel no exterior (17/18), bem móvel não registrável (16), aluguel de imóvel no exterior (23) | Text 1; D, M, P, C, U | IN312 §48; F4 (o script só libera "U" para ano > 2025) |
| U8 | `U8-n` | išmokos, neatėmus NPD, GPM, VSDĮ ir PSDĮ, suma | Valor bruto, mesmo quando não é objeto de imposto (GPMĮ art. 5 §4); demais regras como em L8 | Decimal 12, 2 casas | IN312 §49; F4 |
| U9 | `U9-n` | GPM tarifas | Alíquota aplicada; 0 para isentas, B sem retenção e apostas | Decimal 5; lista 0; 5; 7,5; 10; 15; 20; 25; 27; 32. Em 2026 o script aceita 0/5/7,5/10/15/20/25/32 | IN312 §50; F4 |
| U10 | `U10-n` | išskaičiuota GPM suma | GPM retido | Decimal 11, 2 casas | IN312 §51; F4 |
| U11 | `U11-n` | … lėšomis … sumokėta GPM suma | GPM pago pelo pagador | Decimal 11, 2 casas | IN312 §52; F4 |
| U12 | `U12-n` | gimimo data | Data de nascimento (ano, mês, dia) | **Date**, 10 células | IN312 §53; F4 |
| U13 | `U13-n` | mokesčių mokėtojo kodas užsienio valstybėje | TIN estrangeiro ou nº de documento estrangeiro; pode ficar vazio se não houver | Text 24 | IN312 §54; F4 |
| U14 | `U14-n` | valstybės kodas | País de residência fiscal (para intermediário: país do intermediário) | Text 2; lista de países | IN312 §55; F4 |
| U15 | `U15-n` | adresas užsienio valstybėje | Endereço no exterior | Text 68 | IN312 §56; F4 |

Obrigatoriedade nos anexos: o MXFD não marca nenhum campo L/U como `IsRequired` (F4). A obrigação vem das regras: "turi būti įrašomas" (§23–56) e das validações do script.

### 3.6 Códigos de tipo de renda (IN312, 2 priedas, redação VA-24/2026)
Fonte: IN312 2 priedas (tabela "A IR B KLASĖS IŠMOKŲ KODAI"). A coluna "Classe" segue o texto do anexo. A coluna "Alíquotas aceitas para residente classe A em 2026" vem do script de validação do MXFD (F4, bloco `B_ML_Metai >= 2026`, alíquotas 0/5/15/20/25/32). Ela mostra o que o formulário aceita, **não é norma**: as alíquotas legais estão no GPMĮ art. 6 e no IN313-2026 §9–10.

| Código | Renda (resumo pt-BR) | Classe | Alíq. aceitas no L (A, 2026) |
|---|---|---|---|
| 01 | Rendas de emprego, inclusive isentas pelo art. 37 (exceto 04 e 08) | A | 0, 20, 25, 32 |
| 02 | Entidade de responsabilidade ilimitada ou MB a sócio, tratadas como emprego (art. 2 §34) | A não residente; B residente | — (B) |
| 03 | Doença, maternidade, paternidade, cuidado de filho, ilgalaikio darbo | A | 0, 15 |
| 04 | Rendas de emprego apuradas até 2018-12-31 e pagas de 2019 em diante | A | 0, 15 |
| 05 | Diárias de viagem (Dec. Gov. nº 99/2003) | A; B se pagas a sócio de entidade ilimitada ou MB (residente) | 0 |
| 07 | Prêmios e presentes do empregador até 200 EUR/ano | A | 0 |
| 08 | Rendas de emprego isentas pelo art. 17 (exceto 05 e 07) | A | 0 |
| 09 | Auxílio-doença de marítimos isento (art. 17 §1 p.45) | A | 0 |
| 12 | Venda de instrumentos financeiros e derivativos | B | — |
| 13 | Venda de outros bens (exceto 12, 14–18, 34) | B | — |
| 14 | Venda de madeira em pé ou toras | A | 0, 15, 20, 25, 32 |
| 15 | Venda de resíduos fora de atividade individual | A | 5, 20, 25, 32 |
| 16 | Venda de bem móvel registrável ou imóvel por lei | A não residente; B residente | — |
| 17 | Venda de imóvel por natureza (exceto 18) | A não residente; B residente | — |
| 18 | Venda de moradia (com o terreno) | A não residente; B residente | — |
| 34 | Venda de produtos florestais colhidos pelo próprio | B | — |
| 23 | Aluguel de imóvel por natureza | A | 15, 20, 25, 32 |
| 24 | Aluguel de outros bens | A | 15, 20, 25, 32 |
| 26 | Dividendos (inclusive via intermediário) | A; B se pagos a membro de MB residente | 0, 15 |
| 27 | Lucro de entidade de responsabilidade ilimitada ao sócio | A não residente; B residente | — |
| 29 | Distribuição de lucro de cooperativa | A | 0, 15 |
| 30 | Prêmio de esporte de alto rendimento (organizações listadas) | A | 0 |
| 31 | Prêmios e ganhos de fora do empregador (exceto 07, 30, 42, 43) | A | 0, 15, 20, 25, 32 |
| 42 | Ganhos de jogos de azar | B | — |
| 43 | Ganhos de loteria (entidades que pagam o imposto sobre loterias) | B | — |
| 46 | Doações de pessoas jurídicas (sem relação de emprego) | A | 15, 20, 25, 32 |
| 48 | Pensões, anuidades, rendas | A | 0, 15, 20 |
| 71 | Benefícios de acumulação de pensão até as contribuições | A | 0, 15, 20 |
| 76 | Benefícios de acumulação de pensão acima das contribuições | A | 0, 15, 20, 25, 32 |
| 55 | Juros de P2P e crowdfunding | A não residente; B residente | — |
| 56 | Juros de depósito no EEE (contratos até 2013-12-31) | A não residente; B residente | — |
| 58 | Juros de empréstimos | A não residente e residente→residente; B residente | 15, 20, 25, 32 |
| 59 | Outros juros (exceto 55, 56, 58, 64–67, 69) | A não residente; B residente | — |
| 64 | Juros de depósito (contratos de 2014-01-01 em diante) | A não residente; B residente | — |
| 65 | Juros de títulos de governos do EEE comprados até 2013-12-31 | A não residente; B residente | — |
| 66 | Juros de títulos de dívida comprados até 2013-12-31 (resgate ≥ 366 dias) | A não residente; B residente | — |
| 67 | Juros de títulos de dívida comprados de 2014-01-01 em diante | A não residente; B residente | — |
| 69 | Juros de títulos do governo LT pagos a não residente | A | 0 |
| 33 | Pagamentos compensatórios (lei agrária) | A | 0 |
| 36 | Pagamentos diretos (agricultura) | B | — |
| 37 | Auxílios de entidade sem fins lucrativos a membros (de quotas) | A | 0 |
| 38 | Prêmio de entidade sem fins lucrativos isento (art. 17 §1 p.52) | A | 0 |
| 39 | Prêmio isento (art. 17 §1 p.36) | A | 0 |
| 44 | Tantjemos e remuneração de conselho | A | 20, 25, 32 |
| 45 | Bolsa por contrato tripartite acima de 2 500 EUR/ano | A | 15, 20, 25, 32 |
| 47 | Bolsas (exceto 45) | A | 0, 15, 20 |
| 51 | Atividade esportiva não individual e não de emprego | A | 0, 15, 20, 25, 32 |
| 52 | Atividade de artista não individual e não de emprego | A | 15, 20, 25, 32 |
| 60 | Direitos autorais pagos pelo empregador | A | 20, 25, 32 |
| 61 | Direitos autorais de fora do empregador | A | 15, 20, 25, 32 |
| 62 | Honorários (inclusive via intermediário) | A | 0, 15, 20, 25, 32 |
| 70 | Outras rendas A tributáveis sem código próprio | A | 0, 15, 20, 25, 32 |
| 73 | Seguro-saúde voluntário pago pelo empregador, isento (art. 17 §1 p.14/14¹) | A | 0 |
| 74 | Seguro de vida e pensão pagos pelo empregador, isentos (art. 17 §1 p.14/14¹) | A | 0 |
| 77 | Contrato de serviços fora de atividade individual (sem código especial) | A; B se pago por MB a membro residente | 15, 20, 25, 32 |
| 78 | Isentas do art. 17 §1 sem código especial | A | 0 |
| 88 | Pagos com *paslaugų kvitas* | B | — |
| 89 | Dirigente de MB (não membro), por contrato civil | A | 20, 25, 32 |
| 35 | Atividade individual agrícola | B | — |
| 92 | Atividade individual com *verslo liudijimas* | B | — (o script exige L9 vazio ou 0) |
| 93 | Atividade individual (exceto 35, 92, 96, 97) | A (madeira, resíduos, esporte e artista, nota 5); B nos demais | 0, 15, 20, 25, 32 |
| 96 | Manutenção de membro de *šeimyna* | B | — |
| 97 | Venda de ativo fixo agrícola (não imóvel) | B | — |

- **Classe B (residentes), 2026:** o script aceita 0, 5, 15, 20, 25 ou 32 em L9; para não residentes, também 7,5 em U9. (F4, script)
- **Classe A (não residentes), 2026:** a matriz do U9 é mais ampla. Alguns exemplos:
  - 5%: códigos 15, 26 e 62;
  - 7,5% e 10%: só código 62;
  - 15%: inclui 27 e um código "10", que não existe no 2 priedas.
  
  Não foi transcrita aqui (F4, script, linhas ~2946–3150 do `ScriptModule`).

**Mudanças nos códigos em 2026:**
- **Código 06 saiu para 2026.** Era a compensação de despesas maiores de trabalho móvel ou itinerante prevista no Código do Trabalho. Situação:
  - não aparece no 2 priedas da redação VA-24;
  - o script do MXFD o tira da lista para `B_ML_Metai >= 2026`;
  - continua na lista de 2021–2025.
  
  A lista estática do campo L5/U5 ainda mostra os 64 códigos, porque o script filtra por ano. (IN312 2 priedas; F4, script: diff das listas `pajamos` de 2021–2025 × 2026)
- **Alíquota de 25% nova:** só é aceita para ano ≥ 2026 ("L9 laukelyje pasirinkti 25 proc. galima tik pildant deklaraciją už 2026 ir vėlesnius metus"). (F4, script)
- **27%** fica na lista estática, mas só vale para 2019. (F4, script, bloco `A - 27%`)
- **Marcador U em U7:** novo para ano > 2025. (F4, script; IN312 §48.5)
- **Códigos novos em 2026:** nenhum (o diff de 2021–2025 para 2026 não acrescentou código; F4).

**1 priedas (rendas A isentas que não se declaram):** 22 itens, entre eles:
- prêmios de até 200 EUR de quem não é empregador, até 6 vezes por ano;
- bolsa tripartite de até 2 500 EUR;
- passe de transporte público pago pelo empregador;
- pensões estatais;
- auxílios do orçamento;
- compensações legais, exceto as da rescisão de contrato, as férias não gozadas e as diárias.

(IN312 1 priedas, p. 1–22)

### 3.7 Formato eletrônico
- **Formulário:** GPM312 v.1, arquivo EDS de 2026-06-12, com as páginas `GPM312`, `GPM312L` (10 linhas por folha) e `GPM312U` (5 linhas por folha). Os nomes dos campos estão nas tabelas 3.3–3.5. (F4, F8)
- **Envio:** o mesmo serviço FFData do GPM313 (`FFDataCollectServer=…/EDSMdocUploadService/MdocUploadService.svc`). (F4)
- **XSD do FFData:** NOT LOCATED (mesma situação do GPM313). O documento do web service de upload (F9, 2010) foi baixado, mas não analisado.

### 3.8 Correção (tikslinimas)
- Corrige-se entregando **uma nova declaração com os anexos L e/ou U do mesmo ano** (IN312 §63).
- **É obrigatório corrigir** quando chega aviso da VMI ou quando o próprio pagador acha erro (§64).
- **Erros que não se corrigem:**
  - GPM a mais ou a menos por erro de NPD em renda de emprego (§64.2.1);
  - GPM retido a mais (§64.2.2).
- **Ligação com o GPM313:** se a correção mudar totais já declarados no GPM313, o GPM313 do mês correspondente também tem de ser corrigido (§65).
- **Prazo:** o do aviso da VMI (§66).

---

## 4. Mudanças 2025–2026
| Data | Mudança | Fonte |
|---|---|---|
| 2025-11-01 | Operadores de jogos passam a declarar no GPM312 (L e U) apostas e prêmios acima de 1 000 EUR por dia; marcador **C** em L7/U7; código 42 também para apostas | IN312 §5, §20, §29.4, §39, §48.4; F4 (o script libera C para ano ≥ 2025) |
| 2025 (só o ano de 2025) | U obrigatório para dividendos pagos de 2025-01-01 a 2025-06-30 a intermediários que não revelam os acionistas; U2 = 6 | IN312 §6, §37, §42, §43.6, §55 |
| 2025 (ano ≥ 2025) | Marcador **P** (arrendamento de terra) em L7/U7 | F4 (lista `ismokos_7` para ano ≥ 2025); IN312 §29.3, §48.3 |
| 2025-11-20 | VA-105 altera a VA-121: GPM313 passa a "Tvarkos aprašas", com as alíquotas progressivas de 2026 (20/25/32% com 36/60 VDU; 15/20/25/32% e 5/20/25/32% com 12/36/60 VDU). Os campos 1–12 não mudam | IN313-2026, cabeçalho e §9–10; diff com `nuo_2022_iki_2025` (F2) |
| 2025-12-31 | Nova versão do arquivo do formulário GPM313 no EDS (MXFD de 2025-11-04) | F7; F1 |
| 2026-03-26 | VA-24: nova redação das Taisyklės do GPM312 (sem o código 06 no 2 priedas; marcador U em U7) | IN312, cabeçalho e §48.5; 2 priedas |
| 2026-06-12 | Nova versão do arquivo do formulário GPM312 no EDS (MXFD de 2026-05-11). Para ano ≥ 2026: alíquota 25%, sem código 06, U7 = U | F8; F4, script |

A ligação dessas mudanças com a Lei XV-343 (faixas 20/25/32%) é **inferida**, não lida: os documentos da VMI citam só o "GPMĮ 6 straipsnis". O número da lei: NOT LOCATED nestas fontes.

---

## 5. Precisa de navegador
Bloqueados para script (403 Cloudflare em curl e em WebFetch, 2026-10-27):
1. **VA-121 (GPM313), texto consolidado vigente:**
   - e-seimas `https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/9c2ec9b4e69f11e7b4d1bdd5f1a9ff0e` (edições: `…/portal/legalActEditions/lt/TAD/9c2ec9b4e69f11e7b4d1bdd5f1a9ff0e`);
   - e-tar `https://www.e-tar.lt/portal/lt/legalAct/9c2ec9b4e69f11e7b4d1bdd5f1a9ff0e/asr`.
   
   Uma busca mostrou a redação "nuo 2022-01-05 iki 2025-11-20" (`…/rs/actualedition/9c2ec9b4e69f11e7b4d1bdd5f1a9ff0e/aaEwzWkFTi/`), o que indica nova redação a partir de 2025-11-21. Confirmar a data exata de entrada em vigor.
2. **VA-105 de 2025-11-20 (ato de alteração):** confirmar número, data, publicação no TAR e entrada em vigor. Candidato não verificado: `https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/e4254852c64f11f08962cdb35f3f1615`.
3. **VA-9 de 2018-02-06 (GPM312) e VA-24 de 2026-03-26:** texto consolidado e entrada em vigor da VA-24. Candidato não verificado para a VA-9: `https://e-seimas.lrs.lt/portal/legalAct/lt/TAD/0fd387a01ccb11e88a05839ea3846d8e`.
4. **Páginas do vmi.lt:** `https://www.vmi.lt/evmi/formos-ir-ju-pildymo-taisykles` e `https://www.vmi.lt/evmi/formos`, com a lista de formulários e as notícias de alteração.
5. **GPMĮ (Lei do Imposto de Renda da Pessoa Física), consolidado em 2026:** art. 6 (alíquotas), art. 24 §2 e art. 33 §2 (prazos). Confirmar também o número da lei que criou as faixas de 2026 (XV-343?).

---

## 6. Lacunas
- **XSD ou especificação do FFData** (estrutura XML de importação do GPM313/GPM312): NOT LOCATED. Só há os nomes dos campos no MXFD.
- **Data de entrada em vigor** da VA-105 e da VA-24: NOT LOCATED (só a data de assinatura, no cabeçalho dos documentos da VMI).
- **Alíquota por código de renda como norma:** o 2 priedas não traz alíquota. A matriz código × alíquota acima vem do script de validação do EDS (o que o formulário aceita); a norma é o GPMĮ art. 6 (não lido).
- **Código "10"** na matriz do U9 a 15% (script) não existe no 2 priedas: origem NOT LOCATED (provável resíduo do script).
- **Motivo da saída do código 06 em 2026:** NOT LOCATED (sem nota explicativa nas fontes lidas).
- **Lei XV-343:** não confirmada nas fontes desta coleta (ver Precisa de navegador, item 5).
- **Notícias do EDS** (`Naujienos/NaujienosVISI.aspx`) com o histórico de versões dos formulários: não coletadas.
