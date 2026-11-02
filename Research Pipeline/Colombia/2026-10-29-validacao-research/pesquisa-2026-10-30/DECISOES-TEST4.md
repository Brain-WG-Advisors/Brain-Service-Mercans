# Decisões do Test 4: pontos abertos da research CO (pesquisa de 30/10/2026)

Origem: [[RELATORIO-TEST4]] (`../test4-folha-setembro/RELATORIO-TEST4.md`), achado #1, achado #8, "Pontos abertos" (integral × Ley 1393) e a pergunta sobre ARL e parafiscais. Hub: [[Colombia]]. Conferência da frente: `../CONFERENCIA.md`.
Data de acesso de todas as fontes: **30/10/2026**. Nenhum artefato foi alterado. O oráculo (`../oracle/`) só foi lido.

Hierarquia usada: Constituição > lei (ET, CST, Ley 100, Ley 1393, DL 1295) > decreto regulamentar (DUR) > resolução MinSalud (PILA) > doutrina DIAN/UGPP > jurisprudência. A sentença de unificação do Consejo de Estado (CE) prevalece sobre a doutrina na interpretação. A jurisprudência reiterada da CSJ Sala Laboral é doctrina probable.

---

## 1. ET art. 114-1: o que conta no teste de "menos de 10 SMMLV"

**Decisão.** No teste dos 10 SMMLV entram **só os pagamentos que constituem salário no mês** (CST art. 127): básico, horas extras, comissões, bonificações habituais e as demais parcelas salariais. Ficam fora:
- os pagamentos não salariais (CST art. 128, Ley 344/1996 art. 17);
- as férias pagas (são descanso remunerado, não salário);
- as prestações sociais;
- a indenização.

O teste é estrito (`< 10 SMMLV`). A posição do provedor (salarial + não salarial + férias), que a PILA-003 v1.0/v1.1-DRAFT repete, **não é a vigente**.

**Por quê (fontes):**

1. **O texto do Decreto 1828/2013 art. 7 ("totalidad de lo devengado") não está mais em vigor.** Ele foi compilado no DUR 1625/2016 como **art. 1.5.1.4.1**, que hoje traz a nota *"<Artículo eliminado por el artículo 2 del Decreto 2201 de 2016>"*.
   - Fonte: DUR 1625, normograma DIAN, cópia local `raw/docs/oficiais/CO/2026-10-13-DUR-1625-2016-DIAN.htm`, Libro 1, Parte 5, Título 1, Capítulo 4.
   - Nenhum outro artigo vigente do DUR repete "totalidad de lo devengado": a busca no arquivo inteiro deu zero ocorrências.
   - O art. 1.2.6.6 (autorretenção, Decreto 2201/2016) só repete a fórmula da lei: *"trabajadores que devenguen, individualmente considerados, menos de diez (10) salarios mínimos"*.
2. **Doutrina DIAN vigente.** Concepto 008380 int. 956 de 30/10/2024, confirmado "en todos sus términos" pelo Concepto 007196 int. 1066 de 03/06/2025, que negou o pedido de reconsideração do ICBF:
   - Tese (8380/2024): *"No. Los pagos no constitutivos de salario no se encuentran incluidos dentro del cálculo para efectos de la exoneración de aportes parafiscales."*
   - §7: *"el término «devengado» por el trabajador, para efectos del artículo 114-1 del Estatuto Tributario, hace referencia a lo recibido por concepto de salario mensual"*.
   - URLs: https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_8380_2024.htm e https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_7196_2025.htm.
   - Cópias locais: `raw/docs/oficiais/CO/2026-10-30-DIAN-Oficio-8380_2024-normograma.htm` e `...-7196_2025-normograma.htm`.
   - O Concepto 005299 de 07/04/2026 (`...-5299_2026-normograma.htm`) reitera o teste "menos de diez (10) SMMLV" por trabalhador.
3. **Jurisprudência do CE, Sección Cuarta (linha reiterada, sem sentença de unificação encontrada sobre o ponto):**
   - exp. 25302 (24/02/2022), 24963 (30/06/2022), 27774 (07/03/2024), 26984 (06/06/2024) e 28038 (09/09/2024; ação contra o ICBF, que exclui do teste também as "primas de vacaciones y de navidad" extralegais não salariais);
   - todas são citadas no Concepto DIAN 7196/2025, nota 2;
   - trecho do 26984/2024 (cópia local `2026-10-22-CE-S4-26984-2024-SENA-normograma.htm`): *"para establecer los trabajadores respecto de los cuales se aplica la exoneración de aportes, se deben considerar únicamente los pagos con connotación salarial."*
4. **UGPP (posição contrária, mais antiga e sem base regulamentar vigente).**
   - O "ABECE Pago correcto empleadores V1" (https://www.ugpp.gov.co/sites/default/files/Parafiscales/ABECE-Pago-Correcto-Empleadores-V1.pdf, local `2026-10-30-UGPP-ABECE-Pago-Correcto-Empleadores-V1.pdf`, p. 5) e a apresentação "Empleadores IBC 2021" (local `2026-10-21-UGPP-Empleadores-IBC-2021.pdf`) dizem: *"Total devengado = Total pagos salariales + Total pagos no salariales + Vacaciones pagadas"*. É exatamente a regra do provedor.
   - O ABC Empleadores 2025 da UGPP (local `2026-10-22-UGPP-ABC-Empleadores-2025.pdf`) **não repete** essa definição.
   - O ABC salário integral de fev/2026 (https://www.ugpp.gov.co/wp-content/uploads/2026/02/ABC-Trabajadores-dependientes-que-devengan-salario-integral.pdf, local `2026-10-30-UGPP-ABC-salario-integral-2026.pdf`, p. 6) fala em quem "devengan 10 o más SMMLV".
   - Doutrina da UGPP não se sobrepõe à lei, nem à doutrina da DIAN (dona do ET), nem ao CE.
5. **Restrição operacional da PILA (vale para o motor).** Anexo Técnico 2, v30 de 24/07/2026 (Res. MSPS 1529/2026), §2.1.2.3.39, campo 76 (local `2026-10-29-MinSalud-AT2-v30-2026-07-24-PILA-activos.txt`, l. 9013-9024): *"Cuando el valor del campo "43 – IBC Salud" sea igual o superior a 10 SMLMV este campo debe ser N."*
   - É regra de validação do operador PILA. Ela não define o conceito legal, mas a planilha não aceita "S" quando o IBC de saúde é ≥ 10 SMMLV.

**Posição mais defensável hoje:** a da lei, lida como a DIAN (doutrina vigente e confirmada em reconsideração) e o CE (linha reiterada desde 2022). O único texto regulamentar que sustentava "totalidad de lo devengado" foi eliminado em 2016.

**O que o motor deve fazer:** `exonerado = (empregador elegível) E (salário do mês < 10 SMMLV) E (IBC salud < 10 SMMLV)`.
- O segundo teste é a trava da PILA (campo 76).
- Quando o salário for < 10 mas o IBC de saúde for ≥ 10, o que só acontece com excesso da Ley 1393 ou com IBC de férias/incapacidade, o motor **não exonera** e marca o caso para revisão: o empregador pode ter direito, mas a PILA recusa o "S".
- Salário integral nunca exonera: o mínimo é 13 SMMLV, e o ABC UGPP 2026 diz o mesmo.

**Confiança: 90%.** Falta: nenhuma sentença de unificação do CE sobre o termo "devengo" e a UGPP sem pronunciamento novo publicado. Os 10% restantes são o risco de a UGPP fiscalizar pela regra antiga, um risco que se discute no CE e em que o contribuinte tem vencido.

**Impacto na research:**
- **PILA-003** (M150, v1.0 e v1.1-DRAFT): trocar "total devengado… salary and non-salary alike" (Decreto 1828 art. 7) por "salary-constituting payments only (DIAN Concepto 8380/2024, confirmado pelo 7196/2025; Decreto 1828 art. 7, compilado no DUR 1625 art. 1.5.1.4.1, eliminado pelo Decreto 2201/2016)" e acrescentar a trava do campo 76.
- **CCG v1.4:** já está certo ("salary < 10 minimum wages"); acrescentar a fonte e a trava do campo 76.
- **Oráculo:** `devenga = salary_pay` está certo (`oracle.py` l. 184); falta a trava `IBC < 10 SMMLV`.
- Os 8 empregados do Test 4 (~16,7 M COP) seguem como erro do provedor, salvo os casos em que o IBC de saúde passa de 10 SMMLV. É preciso reconferir esses 8 com a trava.

---

## 2. Salário integral + não salariais acima de 40% (Ley 1393 art. 30): ordem do cálculo

**Decisão: opção (a).** `IBC = 70% × salário integral + excesso`, com:
- `excesso = max(NS − 40% × (salário integral 100% + NS), 0)`;
- `NS` = só os pagamentos **desalarizados por pacto** (ver a nota da SU 25185).

Depois vêm o piso (1 SMMLV), o teto (25 SMMLV) e o arredondamento. O excesso **não** sofre o redutor de 70%. O fator prestacional de 30% do integral **não** conta como "NS" no numerador, mas entra no "total da remuneração", no denominador.

**Por quê (fontes):**

1. **Ley 100/1993 art. 18:** *"Las cotizaciones de los trabajadores cuya remuneración se pacte bajo la modalidad de salario integral, se calculará sobre el 70 % de dicho salario."* O 70% incide sobre "dicho salario", isto é, o salário integral. O excesso da Ley 1393 não é salário integral: é pagamento não salarial que a lei manda computar.
   - Local: `2026-10-21-Ley-100-1993-FuncionPublica.html`. A mesma regra está na Ley 789/2002 art. 49 para os parafiscais.
2. **Ley 1393/2010 art. 30:** *"…para los efectos relacionados con los artículos 18 y 204 de la Ley 100 de 1993, los pagos laborales no constitutivos de salario de las trabajadores particulares no podrán ser superiores al 40% del total de la remuneración."*
   - Local: `2026-10-21-Ley-1393-2010-SecretariaSenado.html`.
   - "Total de la remuneración" é tudo o que é pago no mês, o que inclui o integral inteiro.
3. **CE, Sección Cuarta, SU de 09/12/2021, exp. 25185** (CP Milton Chaves García), regra 3, transcrita no CE exp. 25907, de 06/10/2022 (CP Stella Jeannette Carvajal Basto, rad. 25000-23-37-000-2015-01546-01):
   - *"El pacto de "desalarización" no puede exceder el límite previsto en el artículo 30 de la Ley 1393 de 2010… En estos eventos, los aportes se calcularán sobre todos aquellos factores que constituyen salario… y, además, los factores que las partes de la relación laboral pacten que no integrarán el IBC, en el monto que exceda el límite del 40% del total de la remuneración."*
   - A estrutura é "base salarial + excesso". Para o integral, a base salarial legal é o 70% (Ley 100 art. 18).
4. **CE exp. 25907/2022, sobre o integral:** a Sala manda a UGPP *"determinar los aportes de los trabajadores que devengaron salario integral teniendo en cuenta el porcentaje salarial del 70% sobre el 100% del salario sin importar que el IBC resulte inferior a los 10 SMMLV"*. O 70% é aplicado sobre o salário, e não sobre o salário somado a outros valores.
   - Texto lido pelo navegador na cópia do portaltributariodecolombia.com: https://www.portaltributariodecolombia.com/wp-content/uploads/normativa2023/CONSEJO%20DE%20E.%20C.%20CONST.%20Y%20CORTE%20S.%20DE%20JUSTICIA/C.E%20EXP.%2025907%20OCTUBRE%206%20DE%202022.%20UGPP.%20IBC%20SOBRE%20S.%20INT.%20SOBRE%20EL%2070%25.%20INGRESOS%20QUE%20NO%20SUMAN.pdf.
   - Não foi possível guardar o PDF: o site tem verificação anti-bot e o download pelo curl voltou só a página de bloqueio, que foi apagada.
5. **UGPP, Acuerdo 1035/2015, Sección II, num. 4** (local `2026-10-30-UGPP-Acuerdo-1035-2015-copia-crconsultores.pdf`, p. 6): só trata do 70% (*"se liquiden sobre el 70% del mismo, aunque el ingreso base de cotización resulte inferior a los 10 SMLMV"*). **Não há exemplo numérico** que combine integral e 40%, nem no Acuerdo nem no anexo técnico (local `...-AnexoTecnico-copia-cijuf.pdf`).
   - Uma busca na web atribuiu ao Acuerdo o exemplo "(salário + excesso) × 70% = 9.240.000". Esse exemplo **não está** no texto oficial lido e foi descartado.
   - Os num. 2 e 3 da Sección II (regras da Ley 1393) foram **anulados** pelo CE, Sección Segunda, em 17/09/2020 (rad. 11001-03-25-000-2016-00724-00, CP Gabriel Valbuena Hernández). ⚠️ Lido só em fonte secundária (asuntoslegales.com.co, vlex.com.co/vid/851732005). O texto da sentença não foi baixado.

**Exemplo numérico** (SMMLV 2026 de 1.750.905, como no ABC UGPP 2026; teto de 25 SMMLV = 43.772.625):

| Item | Valor (COP) |
|---|---|
| Salário integral pactado | 30.000.000 |
| Não salarial desalarizado por pacto (NS) | 25.000.000 |
| Total da remuneração | 55.000.000 |
| Limite de 40% | 22.000.000 |
| Excesso | 3.000.000 |
| **(a) 70% × 30.000.000 + 3.000.000** | **24.000.000** |
| (b) 70% × (30.000.000 + 3.000.000), a ordem "clamp 40% e depois 70%" do CCG v1.4 | 23.100.000 |

A leitura (b) aplica o redutor de 70% a um valor que não é salário integral e subestima o IBC. É o caso dos 2 empregados do Test 4, com IBC 1,55 M e 2,51 M menor.

**Confiança: 80%.** Não existe norma nem sentença que trate expressamente da combinação. A decisão vem da leitura literal de "dicho salario" (Ley 100 art. 18) somada à estrutura "salário + excesso" da SU 25185. O provedor faz igual.

**Impacto na research:**
- **CCG v1.4** (dump `revisao/_check/CCG_accept.txt` l. 481): trocar "the 40% non-salary clamp, the 70% rule…" por "70% of the all-inclusive salary, then add the non-salary excess over 40% of total remuneration (excess not reduced to 70%), then floor/ceiling/round-up".
- **Oráculo** (`oracle.py` l. 160): no integral, hoje faz `salary_pay × 0,7` e ignora o excesso. Deve passar a `salary_pay × 0,7 + exceso`.
- **PILA-003/WTC:** conferir a mesma redação.

---

## 3. Indenização por demissão sem justa causa (CST art. 64): base e fração de ano

**Decisão.**
- **Base:** é o salário de CST art. 127, com as partes variáveis (comissões, horas extras habituais etc.).
  - Salário fixo: o último salário.
  - Salário variável: **a média do que foi efetivamente recebido na última anualidade de serviço efetivamente prestado**, por analogia com o CST art. 253. Os períodos de suspensão do contrato ficam fora e a conta é proporcional ao tempo trabalhado; não é dividir por 12.
  - A mesma base escolhe a faixa (< 10 SMMLV ou ≥ 10 SMMLV).
- **Fração de ano:** proporcional ("proporcionalmente por fracción"), em dias, sem truncar. Fórmula: `dias = 30 + 20 × (dias de serviço − 360)/360` para menos de 10 SMMLV; `20 + 15 × …` para 10 SMMLV ou mais. Com até 1 ano: 30 dias (ou 20).
- Quem tinha 10 anos ou mais de serviço contínuo em 27/12/2002 segue a tabela transitória da Ley 50/1990 art. 6, literais b-d (parágrafo transitório do art. 64). O comparador do Test 4 já exclui esses casos (`scripts/comparar.py` l. 252).

**Fontes:**

1. **CST art. 64** (Ley 789/2002 art. 28), cópia local `2026-10-22-CST-pr001-SecretariaSenado.html`: *"a) Para trabajadores que devenguen un salario inferior a diez (10) salarios mínimos mensuales legales: 1. Treinta (30) días de salario cuando el trabajador tuviere un tiempo de servicio no mayor de un (1) año. 2. … veinte (20) días adicionales de salario sobre los treinta (30) básicos del numeral 1, por cada uno de los años de servicio subsiguientes al primero y proporcionalmente por fracción"*.
   - A Ley 2466/2025 (reforma laboral) não altera o art. 64 do CST: a busca na cópia local `2026-10-30-Ley-2466-2025-FuncionPublica.html` não acha mudança; o "Artículo 64" dela é outro assunto.
2. **CST art. 127:** *"Constituye salario no sólo la remuneración ordinaria, fija o variable, sino todo lo que recibe el trabajador… como primas, sobresueldos, bonificaciones habituales, valor del trabajo suplementario o de las horas extras… porcentajes sobre ventas y comisiones."*
3. **CSJ, Sala de Casación Laboral, SL1659-2025** (26/03/2025, rad. 25899-31-05-001-2021-00355-01), cópia local `2026-10-13-CSJ-SL1659-2025.pdf`, pp. ~17-19:
   - *"de acuerdo con la aplicación armónica de los artículos 64, 127 y 253 del CST, el salario promedio no corresponde al último período de 12 meses, sino… a la sumatoria de lo devengado en el último año de servicios, lo que debe entenderse como el promedio de lo efectivamente devengado… que se divide por el tiempo laborado en el mismo término"*;
   - reitera a CSJ SL2282-2022 e a SL de 31/05/2011, rad. 38226;
   - períodos de suspensão *"no puede integrar el promedio"*.
   - Comunicado da Corte: https://cortesuprema.gov.co/corte-suprema-precisa-el-salario-base-para-liquidar-la-indemnizacion-por-despido-sin-justa-causa/.

**Hierarquia:** lei (CST 64 e 127) > jurisprudência reiterada da CSJ (doctrina probable). Não há sentença de unificação; a linha é de casación e é estável desde 2011.

**Confiança:** 90% para "o variável entra na base"; 85% para "fração proporcional em dias de calendário 360" (o art. 64 diz "proporcionalmente" sem fixar a convenção de dias; o 360 segue a prática do CST, como nos arts. 249 e 253); 80% para "média da última anualidade efetiva" na forma da SL1659.

**Impacto na research:**
- **CCG/WTC:** acrescentar a definição da base da indenização (salário fixo = último; variável = média da última anualidade efetiva, CST 253 por analogia, CSJ SL1659-2025) e manter o pró-rata, que já está no CCG.
- **Oráculo** (`terminacion`, l. 297-308): já faz o pró-rata. Recebe `salary` pronto, e quem chama precisa passar básico + média do variável, como o comparador já faz. Isso confirma o achado #8 do Test 4 (provedor multiplica só o básico) como erro do provedor, com confiança de 85%.

---

## 4. Excesso da Ley 1393: só saúde e pensão, ou também ARL e parafiscais?

**Decisão.** O excesso entra no IBC de **saúde, pensão e ARL**. **Não** entra na base de **SENA, ICBF e CCF**.

**Fontes:**

1. **Ley 1393 art. 30:** o limite vale *"para los efectos relacionados con los artículos 18 y 204 de la Ley 100 de 1993"*, isto é, a base de pensão (art. 18) e de saúde (art. 204).
2. **ARL, Decreto-Ley 1295/1994 art. 17** (https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=2629, local `2026-10-30-Decreto-Ley-1295-1994-FuncionPublica.html`): *"La base para calcular las cotizaciones del Sistema General de Riesgos Profesionales, es la misma determinada para el Sistema General de Pensiones, establecida en los artículos 18 y 19 de la ley 100 de 1993"*.
   - O excesso muda a base do art. 18 e chega à ARL por remissão legal. Não depende do Acuerdo 1035, cujo num. 2, que dizia "salud, pensión y riesgos laborales", foi anulado em 2020.
   - A Ley 1955/2019 não é necessária para essa conclusão.
3. **Parafiscais, Ley 21/1982 art. 17** (local `2026-10-21-Ley-21-1982-FuncionPublica.html`): a base é a *"nómina mensual de salarios… los diferentes elementos integrantes del salario… y además, los verificados por descansos remunerados"*.
   - A Ley 344/1996 art. 17 exclui da base de SENA, ICBF, ESAP e CCF os pagos pactados como não salariais.
   - A Ley 1393 não alcança a Ley 21/1982.
4. **UGPP, ABC Empleadores 2025** (https://www.ugpp.gov.co/wp-content/uploads/2025/02/ABC_empleadores2025.pdf, local `2026-10-22-UGPP-ABC-Empleadores-2025.pdf`, exemplo): salário de 5.000.000 e não salarial de 4.000.000 dão excesso de 400.000, e *"IBC en salud, Pensión y ARL $ 5.400.000 / IBC en CCF, SENA e ICBF $ 5.000.000"*. O ABECE V1 traz o mesmo exemplo.

**Confiança: 95%.**

**Impacto na research:**
- **Oráculo:** a ARL usa `ib`, que inclui o excesso (`oracle.py` l. 190), e isso está certo. ⚠️ Já `para_base = max(ibc_raw, lo)` (l. 191) usa `ibc_raw`, que **inclui o excesso** no caso não integral. Para CCF, SENA e ICBF a base deve ser `salary_pay` mais os descansos remunerados, sem o excesso e sem o redutor de 70% no caso não integral.
  - Falta conferir se isso afetou os 5 empregados com excesso do Test 4. Hoje há 1 divergência e 3 lacunas na linha CCF.
- **CCG/PILA-003:** deixar explícito "excess → health, pension, occupational-risk base only; never SENA/ICBF/CCF".

---

## Fora do pedido (não incluí nas decisões; vai para Pendências do hub)

- **Alcance do limite de 40% (SU CE 25185/2021, regra 1, reiterada no exp. 25907/2022):** o pagamento que não é salário por natureza (CST 128, primeira parte: ocasional por mera liberalidade, ou para desempenhar as funções, como auxílio extralegal de transporte e de alimentação) **não entra no IBC nem no limite de 40%**. O limite só vale para o pagamento salarial que as partes **desalarizaram por pacto**.
  - Trecho do 25907: *"si el pago no es salario porque no retribuye el servicio, no integrará el IBC y no está sometido a límite legal alguno."*
  - A UGPP (ABC 2025) aplica o limite a "todos pagos NO salariales pactados".
  - Impacto: o oráculo e a research precisam classificar o "NS" em "desalarizado" × "não salarial por natureza".
- **Possível ajuste na trava do campo 76 da PILA** (ver ponto 1). Pode haver empregados com salário abaixo de 10 SMMLV e IBC de saúde ≥ 10 SMMLV (excesso ou férias). Esses casos ficam como "revisão manual".

## Bloco de prova
- **Pedido → resposta:** ponto 1 (decisão + DUR + DIAN + UGPP + CE + campo 76), ponto 2 (ordem + exemplo), ponto 3 (base variável + fração), ponto 4 (ARL sim, parafiscais não). Todos os 4 foram respondidos.
- **Fontes:** cada afirmação aponta um arquivo local em `raw/docs/oficiais/CO/` ou uma URL oficial. Exceções:
  - a nulidade do Acuerdo 1035 (2020), lida só em fonte secundária (⚠️);
  - o CE 25907, lido no navegador numa cópia de terceiro.
- **Teste:** busca no DUR inteiro (zero "totalidad de lo devengado"; art. 1.5.1.4.1 eliminado); conta do exemplo do ponto 2 refeita; leitura do código do oráculo (l. 160, 184-194, 297-308) sem alterá-lo.
- **Confiança por ponto:** 1 = 90%; 2 = 80%; 3 = 85-90%; 4 = 95%.

## Arquivos baixados nesta pesquisa (`raw/docs/oficiais/CO/`)
- `2026-10-30-DIAN-Oficio-8380_2024-normograma.htm`, `...-7196_2025-...`, `...-5299_2026-...`, `...-914965_2021-...`
- `2026-10-30-UGPP-Acuerdo-1035-2015-copia-crconsultores.pdf` (cópia de terceiro), `2026-10-30-UGPP-Acuerdo-1035-2015-AnexoTecnico-copia-cijuf.pdf` (cópia de terceiro)
- `2026-10-30-UGPP-ABECE-Pago-Correcto-Empleadores-V1.pdf`, `2026-10-30-UGPP-ABC-salario-integral-2026.pdf`
- `2026-10-30-Decreto-Ley-1295-1994-FuncionPublica.html`
