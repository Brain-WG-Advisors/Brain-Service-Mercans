# Lote A, rodada 6: retenção (A-2, NE-18, SIM-07, A-1), 02/11/2026

Ligado a [[PLANO-92]], [[TABELA-RODADA5]], [[LOTE-A-RETENCAO]], [[LOTE-C-PRESTACOES-NE]] e [[Colombia]]. Só pesquisa: **nenhum artefato foi alterado**, nada foi gravado em Drive, ticket ou e-mail. A research CO não está em produção, então não há ticket ao Development. Todas as URLs foram acessadas em 02/11/2026.

**Achado de contexto.** Os finais liberados em 02/11 já trazem as decisões da rodada 5 para A-1, A-2 e SIM-07. Conferi célula a célula, só lendo:
- CCG v1.6: Version Control 1.6; T86R4C2; T150R3C2.
- WTC v1.8: N/P 120–122 e 321–322 = No; Tax Credit A41, A65–A68.
- Spec 004 v1.2: Example Analysis A26 = 12.000.000; changelog itens 1–15.
- Spec 005: A28 e A35 = 12000000.

Por isso, nesta rodada, "muda o artefato?" quer dizer "precisa mudar **além** do que já está na v1.6/v1.8/v1.2?".

## Tabela

| # | Ponto | Decisão | Muda artefato além da R5? | Confiança (antes → agora) |
|---|---|---|---|---|
| 1 | A-2 cesantías e intereses, inclusive de não residente | Sem retenção na fonte para ninguém. O ET 408 não alcança cesantías. Na declaração do não residente, a isenção do ET 206 num. 4 vale: deixa de ser "interpretação" e passa a ser doutrina DIAN (Concepto 577/2020) | Valor: não. Texto (opcional): tirar "(an interpretation)" e citar C-397/1994 e DIAN Concepto 577/2020 em CCG T150R3C2 e T86R4C2, e na spec 004 Report Matrix A34 e Example Analysis D34 | 80% → **90%** (não chega a 92%; motivo abaixo) |
| 2 | NE-18 tipo de incapacidade (NIE126: 2 Profesional / 3 Laboral) | Mantém D68/D69 como interpretação e opção configurável. Não existe definição oficial. Consulta à DIAN redigida (rascunho, §2.5) | Não | 75% → **75%** (não chega a 92% sem resposta da DIAN) |
| 3 | SIM-07 média da casilla 59 | 12.000.000 confirmado: seis meses do ano anterior à consignação, só salário, sem prima | Não (já aplicado na R5) | 88% → **93%** |
| 4 | A-1 tetos de 790 / 1.340 / 3.800 UVT | Anuais, controlados pelo acumulado do ano por empregado, sem 1/12 | Não (já aplicado na R5) | 90% → **92%** |

---

## 1. A-2: cesantías e intereses sobre cesantías, inclusive de não residente

### Distinção pedida
- **Retenção na fonte** (o que a folha calcula): nenhuma, para residente e não residente.
- **Renda tributável na declaração** (fora da folha):
  - As cesantías são renda do trabalho gravada, com isenção parcial pelo ET 206 num. 4. Pelo par. 1 do art. 206, a isenção vale só sobre o mínimo legal.
  - O não residente que recebeu cesantía sem retenção não cumpre o ET 592 num. 2 e fica obrigado a declarar (ET 26, tarifa de 35% do ET 247). Na declaração, aplica a isenção do 206.

### Fontes e trechos literais
1. **Ley 100/1993 art. 135 par. 3.** Local: `raw/docs/oficiais/CO/2026-10-21-Ley-100-1993-FuncionPublica.html` (Función Pública). *"PARÁGRAFO 3. En ningún caso los pagos efectuados por concepto de cesantía serán sujetos de retención en la fuente por parte de la Nación."*
2. **Corte Constitucional C-397/1994, 08/09/1994, M.P. Hernando Herrera Vergara (fonte nova).** Local: `2026-11-02-CorteConstitucional-C-397-1994.htm`. URL: https://www.corteconstitucional.gov.co/relatoria/1994/C-397-94.htm.
   - Decisão: *"DECLARAR INEXEQUIBLE la expresión "por parte de la Nación" contenida en el parágrafo tercero del artículo 135 de la Ley 100 de 1993."*
   - Razão: *"mientras que los pagos por concepto de cesantías, siempre que el retenedor sea la Nación, no estarían sujetos a retención en la fuente, los pagos por concepto de cesantías que efectuen otros agentes retenedores sí estarían sujetos a retención, con lo que se transgrede el artículo 13 superior."*
   - Leitura: a Corte tirou o único recorte subjetivo que a regra tinha, por igualdade. Hoje a regra vale para qualquer pagador e não tem recorte por beneficiário.
3. **DUR 1625/2016 art. 1.2.4.1.11** (Decreto 841/1998 art. 22). Local: `2026-10-13-DUR-1625-2016-DIAN.htm`. *"en ningún caso los pagos efectuados por concepto de cesantías o intereses sobre las mismas, estarán sujetos a retención en la fuente, sin perjuicio del tratamiento previsto en el numeral 4 del artículo 206 del Estatuto Tributario."*
4. **DIAN Oficio 8899/2015.** Local: `2026-11-02-DIAN-Oficio-8899-2015-cesantias-sin-retencion.htm`. URL: https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_8899_2015.htm.
   - *"El artículo 388 del Estatuto Tributario, que establecía el procedimiento para determinar la retención sobre cesantías, se entiende derogado tácitamente en virtud de lo dispuesto por el parágrafo 3o del artículo 135 de la Ley 100"*.
   - Ou seja, a própria DIAN já reconheceu que a regra da Ley 100 prevaleceu sobre uma regra de retenção do ET.
5. **DIAN Oficio 4358/2019.** Local: `2026-11-02-DIAN-Oficio-4358-2019-cesantias-base-retencion.htm`. URL: https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_4358_2019.htm. *"los ingresos por este concepto no hacen parte de la base de retención"*.
6. **ET art. 406.** Local: `2026-10-30-ET-pr016-art408-SecretariaSenado.html`. *"Deberán retener … quienes hagan pagos o abonos en cuenta por concepto de rentas sujetas a impuesto en Colombia, a favor de: … 2. Personas naturales extranjeras sin residencia en Colombia."*
7. **ET art. 408** (Ley 2010/2019 art. 98), mesmo arquivo. *"En los casos de pagos o abonos en cuenta por concepto de … compensaciones por servicios personales … la tarifa de retención será del veinte por ciento (20%) del valor nominal"*. É regra de **tarifa**. A Ley 2010 só mudou a tarifa (de 15% para 20%); não trata de cesantías.
8. **DIAN Concepto 011108 int. 1129, de 29/06/2026.** Local: `2026-10-30-DIAN-Concepto-11108-2026-no-residentes-408.htm`.
   - §10: *"hasta tanto la persona natural no adquiera la residencia fiscal, los pagos o abonos en cuenta que se hagan a su favor, estarán sometidos a retención en la fuente de acuerdo con las reglas previstas en los artículos 408 a 415"*.
   - §14: *"los términos empleados en las normas citadas son claros … por lo tanto, estos elementos deben entenderse en su tenor literal."*
   - Não fala de cesantías (busquei "cesant" no texto: zero ocorrências).
9. **DIAN Concepto 100202208-0577 [9510], de 28/10/2020 (fonte nova; publicado no Diario Oficial 51.496).** Local: `2026-11-02-DIAN-Concepto-577-2020-normograma.htm`. URL: https://normograma.dian.gov.co/dian/compilacion/docs/concepto_tributario_dian_0000577_2020.htm.
   - Retenção do não residente: *"Las retenciones en la fuente aplicables (artículos 406 a 416 del Estatuto Tributario) se aplican sobre pago o abono en cuenta y no admiten depuración."*
   - Declaração do não residente obrigado: *"deberá dar aplicación a lo dispuesto en el artículo 26 del Estatuto Tributario, el cual debe interpretarse de manera armónica con el artículo 178 y el inciso primero del artículo 235-2 de este Estatuto respecto a las rentas exentas de personas naturales"*.
   - O ET 235-2 citado no concepto ressalva *"las rentas exentas de las personas naturales de los artículos 126-1, 126-4, 206 y 206-1"*.
   - O concepto revogou o Oficio 25073/2019, que negava ao não residente as rendas isentas, inclusive as de "fondos de cesantías".
10. **DIAN Concepto 57622/2003.** Local: `2026-11-02-DIAN-Concepto-57622-2003-normograma.htm`. *"por expreso mandato legal, según el parágrafo 3 del artículo 135 de la ley 100 de 1993, en ningún caso estos pagos están sometidos a retención en la fuente … Lo anterior no quiere decir que las cesantías no sean gravables, pues si el beneficiario es declarante debe liquidarse el impuesto correspondiente."*
11. **ET art. 206 num. 4 e par. 1.** Local: `2026-10-22-ET-pr008-SecretariaSenado.html`.
    - O art. 206 não exige residência para a isenção.
    - Par. 1: *"La exención prevista en los numerales 1, 2, 3, 4, y 6 de este artículo, opera únicamente sobre los valores que correspondan al mínimo legal de que tratan las normas laborales"*.

### Busca sem resultado
Não existe concepto, oficio ou sentença sobre retenção de cesantías pagas **a não residente**. Busquei no normograma DIAN, em buscas abertas e nos documentos locais. Conferi nesta rodada, sem o tema: 903232/2022, 23852/1996, 57622/2003, 577/2020, 011108/2026, 14740/2016, 26487/2018 e 28380/2019.

### Decisão
- **Não reter** sobre cesantías e intereses de nenhum empregado. Os motivos:
  - a regra especial e posterior ao ET original diz "en ningún caso";
  - a Corte tirou dela o único recorte, por igualdade (C-397/1994);
  - o DUR a repete;
  - a DIAN já a aplicou contra uma regra de retenção do próprio ET (Oficio 8899/2015, sobre o art. 388).
- O ET 408 é norma geral de tarifa. A Ley 2010 só mudou o percentual e não revoga a regra especial (critério da especialidade). O próprio Concepto 011108/2026 manda ler as normas de retenção "en su tenor literal", e o tenor literal da Ley 100 é "en ningún caso".
- **Declaração:** a isenção do 206 num. 4 vale para o não residente obrigado a declarar (Concepto 577/2020). Os finais chamam isso de "an interpretation"; dá para trocar pela citação.

### Muda artefato?
- **Valores: não.** CCG v1.6, WTC v1.8 (N e P = No) e spec 004 v1.2 (A33 = 31.200.000) já estão com a decisão.
- **Texto (opcional, só citação):**
  - CCG T150R3C2: trocar "(an interpretation: art. 206 does not …)" por "(DIAN Concepto 577 of 2020: a non-resident who must file applies Tax Code arts. 26, 178 and 235-2, which preserves the art. 206 exemptions)".
  - Acrescentar "Constitutional Court C-397 of 1994" à base legal em T86R4C2 e T150R3C2.
  - Mesma troca na spec 004 Report Matrix A34 e Example Analysis D34.

### Confiança: 90%
- **Por que não chega a 92%:** a DIAN nunca disse, para o caso do não residente, que a regra da Ley 100 afasta o ET 408. O Concepto 577/2020 dá um argumento contrário possível: a retenção do não residente "se aplica sobre pago o abono en cuenta y no admite depuración". A resposta a esse argumento é nossa leitura, não está escrita pela DIAN: excluir a cesantía não é "depurar" a base, é um pagamento que a lei tira da retenção.
- **O que falta para 100%:** resposta da DIAN a uma consulta formal. Incluí a pergunta como 2.ª pergunta opcional no rascunho do §2.5. Até lá, os 20% continuam como opção configurável conservadora.

---

## 2. NE-18: tipo de incapacidade (NIE126, tabela 5.5.6)

### O que é
O campo `Tipo` do grupo Incapacidades da Nómina Electrónica tem três códigos: 1 Común, 2 Profesional, 3 Laboral. Nossa spec (CO-DIAN-001 Field Options D68/D69) lê 2 = doença ocupacional e 3 = acidente de trabalho, marcadas como "interpretation … Confirm with DIAN".

### Fontes conferidas
1. **Anexo Técnico NE v1.0** (Res. DIAN 000013/2021), p. 180, tabela 5.5.6. Só "1 Común / 2 Profesional / 3 Laboral", sem definição. A p. 34, NIE126, diz só *"Se debe colocar el Codigo que corresponda de la tabla 5.5.6"*. Cópia local e md5 em [[LOTE-C-PRESTACOES-NE]] §2.
2. **XSD 1.0.6**, l. 592: `Tipo` = `xsd:integer`, sem enumeração. A DIAN não rejeita por domínio.
3. **DIAN Oficio 901708/2022.** Local: `2026-11-02-DIAN-Oficio-901708-2022-normograma.htm`. *"Dentro de la información a reportar se incluye el tipo de incapacidad"*. Não define os códigos.
4. **DIAN, procedimento interno PR-TAH-0352 "Gestión de incapacidades y/o licencias", v3 (fonte nova).** Local: `2026-11-02-DIAN-PR-TAH-0352-gestion-incapacidades.pdf`. URL: https://www.dian.gov.co/atencionciudadano/LMDP/Talento-Humano/Gestion-del-Empleo/Procedimientos/PR-TAH-0352.pdf.
   - Na própria folha da DIAN, os tipos são *"enfermedad general, licencia de maternidad, paternidad, accidente de trabajo o enfermedad laboral"*.
   - Não usa "profesional" e não liga os códigos da tabela 5.5.6. Não resolve o ponto.
5. **Ley 1562/2012**, arts. 3 e 4. Local: `2026-11-02-Ley-1562-2012-SecretariaSenado.html`. "Accidente de trabajo" e "enfermedad laboral" (que substituiu "enfermedad profesional" do Decreto-Ley 1295/1994).
6. **Buscas sem resultado:**
   - normograma DIAN (Res. 13/2021, Abecé DSNE, micrositio de documentação técnica);
   - busca aberta por "tipo de incapacidad" + tabela 5.5.6;
   - versão nova do anexo: a Res. 227/2025 compila a Res. 13/2021 e não vi novo anexo NE; a Res. 12/2026 trata dos formatos 2833–2835 (exógena), não da NE.
   - Só há leitura de mercado (miNómina, Senior, TFHKA), igual à nossa. É pista, não fonte.

### Decisão
- Fica como está: D68 = "2 Profesional", doença de origem laboral; D69 = "3 Laboral", acidente de trabalho. Leitura marcada como interpretação e mapeamento configurável.
- **Para o cálculo não muda nada:** os dois casos são de origem laboral e a ARL paga 100% desde o 1.º dia (Ley 776/2002 art. 3). O risco é só informativo: código trocado no XML, que a DIAN não rejeita.

### Muda artefato?
Não.

### Confiança: 75%
**Por que não chega a 92%:** não existe fonte oficial que defina os códigos. A leitura inversa (Profesional = acidente; Laboral = doença, porque a Ley 1562 trocou "profesional" por "laboral" justamente para a doença) é linguisticamente possível. Só fecha com resposta da DIAN.

### 2.5 Rascunho da consulta formal à DIAN (não enviado; envio só com ok do usuário)

> **Señores**
> Dirección de Impuestos y Aduanas Nacionales – DIAN
> Subdirección de Normativa y Doctrina
> Bogotá D.C.
>
> **Asunto:** Consulta. Interpretación de la tabla 5.5.6 "Tipo de Incapacidad" del Anexo Técnico del Documento Soporte de Pago de Nómina Electrónica (Resolución 000013 de 2021, compilada en la Resolución 000227 de 2025).
>
> Respetados señores:
>
> En ejercicio del derecho de petición (artículo 23 de la Constitución Política) y conforme al numeral 4 del artículo 56 del Decreto 1742 de 2020, formulamos la siguiente consulta.
>
> **Hechos.**
> 1. El elemento NIE126 ("Tipo") del grupo "Incapacidades" del Anexo Técnico del Documento Soporte de Pago de Nómina Electrónica, versión 1.0, ordena: "Se debe colocar el Código que corresponda de la tabla 5.5.6".
> 2. La tabla 5.5.6 (página 180 del anexo) contiene los códigos "1 Común", "2 Profesional" y "3 Laboral", sin definición de cada uno.
> 3. La Ley 1562 de 2012 (artículos 3 y 4) define el "accidente de trabajo" y la "enfermedad laboral", esta última antes denominada "enfermedad profesional" en el Decreto Ley 1295 de 1994.
>
> **Preguntas.**
> 1. ¿Cuál código de la tabla 5.5.6 debe reportarse en NIE126 para (a) la incapacidad derivada de un accidente de trabajo y (b) la incapacidad derivada de una enfermedad laboral, en los términos de los artículos 3 y 4 de la Ley 1562 de 2012?
> 2. ¿El código "2 Profesional" corresponde a la enfermedad laboral (antes "enfermedad profesional") y el código "3 Laboral" al accidente de trabajo, o a la inversa?
> 3. *(Opcional, sobre otro tema)* Respecto de una persona natural extranjera sin residencia fiscal en Colombia, vinculada mediante contrato de trabajo y que presta sus servicios en el país: ¿los pagos por concepto de auxilio de cesantía e intereses sobre cesantías están excluidos de retención en la fuente en virtud del parágrafo 3 del artículo 135 de la Ley 100 de 1993 (Sentencia C-397 de 1994) y del artículo 1.2.4.1.11 del Decreto 1625 de 2016, o están sometidos a la tarifa del veinte por ciento (20%) del artículo 408 del Estatuto Tributario?
>
> Agradecemos la atención y quedamos atentos a su respuesta en la dirección de notificación indicada.
>
> Atentamente,
> [Nombre, identificación, dirección de notificación, correo]

Pendências antes de enviar:
- confirmar o número da norma de competência da Subdirección de Normativa y Doctrina na data do envio (citei o Decreto 1742/2020 art. 56 num. 4 sem reabrir o texto: ⚠️ sem fonte nesta rodada);
- canal: PQSR da DIAN;
- remetente: decisão do usuário.

---

## 3. SIM-07: média da casilla 59 do Form. 220 = 12.000.000

### Fontes e trechos literais
1. **Instrutivo do Form. 220** (Res. DIAN 000022/2024, anexo). Local: `2026-10-30-Res-DIAN-0022-2024-Form220-com-anexo-normograma.txt`, l. 240–260; também `2026-10-21-Res-DIAN-0022-2024-guia-220.htm`.
   - *"59. Ingreso laboral promedio de los últimos seis meses anteriores (numeral 4 art. 206 E.T.): … (ii) cuando la relación laboral o legal y reglamentaria no ha finalizado …"*
   - *"En el caso de que la relación laboral o legal y reglamentaria no haya finalizado, este término tomará en consideración los seis meses del año inmediatamente anterior del momento en que las cesantías se consignan o se consolidan y quedan disponibles en las cuentas individuales; esto último para el caso de los servidores públicos cuyo régimen corresponde al de cesantías anualizadas. Este criterio tiene como fundamento lo dispuesto en el numeral 3 del artículo 27 del Estatuto Tributario y el artículo 1.2.1.20.7 del Decreto 1625 de 2016."*
2. **DIAN Concepto 1302 [28563], de 25/11/2019** (adição ao Concepto General Unificado 0912/2018; publicado no Diario Oficial 51.151). Local: `2026-11-02-DIAN-Concepto-1302-2019-normograma.htm`. URL: https://normograma.dian.gov.co/dian/compilacion/docs/concepto_tributario_dian_0001302_2019.htm.
   - Afasta o art. 103 ET como critério: *"los elementos mencionados en el artículo 103 del Estatuto Tributario, no pueden orientar el cálculo del ingreso mensual para efectos de determinar qué porcentaje del auxilio de cesantía se considera exento."*
   - Composição: *"este ingreso corresponderá a las sumas que habitual y periódicamente recibe el trabajador en dinero o en especie como contraprestación directa del servicio, pues la norma lo que busca es establecer es el salario mensual promedio."*
   - Janela: o mesmo texto do instrutivo (situações i, ii e iii).
3. **DIAN Concepto 4443/2025.** Local: `2026-10-21-DIAN-Concepto-4443-2025.htm`. *"ii) La relación laboral o reglamentaria no ha finalizado: Se debe tomar los 6 meses del año inmediatamente anterior al momento de la consignación de las cesantías…"*
4. **CST art. 307.** Local: `2026-10-30-CST-pr010-SecretariaSenado.html`. *"La prima anual no es salario, ni se computará como factor del salario en ningún caso."*
5. **ET art. 206 num. 4.** Local: `2026-10-22-ET-pr008-SecretariaSenado.html`. *"…cuyo ingreso mensual promedio en los seis (6) últimos meses de vinculación laboral no exceda de 350 UVT. Cuando el salario mensual promedio…"*

### Decisão
**12.000.000 confirmado.**
- **Composição:** só o salário. A prima de servicios não é "contraprestación directa del servicio" com habitualidade mensal e não é salário (CST 307). Logo, sai.
- **Janela:** seis meses de 2025, o ano anterior à consignação de fev/2026.
- O texto do instrutivo ("los seis meses del año inmediatamente anterior") não diz expressamente quais seis meses. Para o exemplo isso não importa, porque o cenário tem salário constante de 12.000.000.
- **Conta:** 6 × 12.000.000 ÷ 6 = 12.000.000, menor que 350 UVT × 52.374 = 18.330.900. Isenção total. A conclusão não muda com a UVT de 2025, que é menor e ainda fica acima de 12.000.000.

### Muda artefato?
Não. Já está aplicado:
- spec 004 v1.2: A26/A34 = 12.000.000; C26 com a fonte; Formulario 220 Spec K51; Sample File A78/A123;
- spec 005: A28/A35 = 12000000; C28.

### Confiança: 93%
O que falta para 100%:
- (a) norma de hierarquia superior (lei ou decreto) que liste os itens da média; hoje a composição vem de doutrina DIAN, embora seja um concepto unificado publicado no Diario Oficial e reiterado em 2025;
- (b) a DIAN dizer quais seis meses do ano anterior contam quando o salário varia. Isso não afeta o exemplo.
- Sugestão opcional de texto em C26/C28: acrescentar "the salary is constant, so which six months of 2025 are taken does not change the result".

---

## 4. A-1: tetos de 790 / 1.340 / 3.800 UVT anuais, pelo acumulado do ano

### Fontes e trechos literais
1. **ET art. 206 num. 10** (Ley 2277/2022 art. 2). Local: `2026-10-22-ET-pr008-SecretariaSenado.html`. *"El veinticinco por ciento (25%) del valor total de los pagos laborales limitada anualmente a setecientos noventa (790) UVT."* O texto anterior dizia "limitada mensualmente a 240 UVT" (DIAN 11383/2024, abaixo).
2. **ET art. 336 num. 3** (Ley 2277 art. 7). Local: `2026-10-22-ET-pr014-SecretariaSenado.html`. *"…que en todo caso no puede exceder de mil trescientas cuarenta (1.340) UVT anuales."*
3. **ET arts. 126-1 e 126-4** (Ley 1819/2016 arts. 15 e 16) (fonte nova). Local: `2026-11-02-ET-pr005-art126-SecretariaSenado.html`. URL: http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr005.html.
   - *"no harán parte de la base para aplicar la retención en la fuente y serán considerados como una renta exenta, hasta una suma que … no exceda del treinta por ciento (30%) del ingreso laboral o ingreso tributario del año, según el caso, y hasta un monto máximo de tres mil ochocientas (3.800) UVT por año."*
   - DUR 1.2.1.22.41 e 1.2.1.22.43 repetem "(3.800) Unidades de Valor (UVT) por año" (local: `2026-10-13-DUR-1625-2016-DIAN.htm`).
4. **DUR 1625 art. 1.2.4.1.6 par. 3**, texto do Decreto 2231/2023 art. 9. Locais: `2026-11-02-Decreto-2231-2023-normograma-DIAN.htm` e o DUR. URL: https://normograma.dian.gov.co/dian/compilacion/docs/decreto_2231_2023.htm.
   - *"Para todos los fines previstos, las rentas exentas y deducciones no pueden superar los límites particulares que establezca cada uno de esos beneficios fiscales, ni el límite del cuarenta por ciento (40%) y el valor absoluto de mil trescientas cuarenta (1.340) Unidades de Valor Tributario (UVT) anuales."*
   - Não há equivalente mensal.
5. **CE Sección Cuarta, 28/10/2021, rad. 11001-03-27-000-2018-00041-00 (24047), C.P. Stella Jeannette Carvajal Basto.** Local: `2026-11-02-CE-S4-24047-2021-nulidad-420UVT-par3-DUR-1.2.4.1.6.pdf`. URL: https://www.consejodeestado.gov.co/documentos/boletines/251/11001-03-27-000-2018-00041-00(24047).pdf.
   - Falla: *"1.- ANULAR el aparte 'es decir cuatrocientos veinte (420) Unidades de Valor Tributario - UVT mensuales', contenido en el parágrafo 3 del artículo 1.2.4.1.6. del Decreto 1625 de 2016"*.
   - Razão decisória (p. 12): *"se evidencia que la aplicación del límite de 420 UVT mensuales para retenciones en la fuente sobre eventuales aportes a cuentas AFC y Fondos de Pensiones que superen ese límite restringiría los beneficios asociados a dichos aportes, respecto de la parte que exceda el límite mensual de UVT y, en esa medida, la Sala estima que la norma reglamentaria acusada conllevaría un efecto inequitativo … En consideración a tal incidencia práctica transgresora del principio de equidad tributaria consagrado en el artículo 363 de la Constitución Política, se anulará el aparte normativo demandado."*
   - Alcance (p. 10): os "fines" do par. 3 são *"los relacionados con la propia regulación del artículo 1.2.4.1.6 sobre depuración de la base de retención en la fuente de las rentas de trabajo"*.
   - **Nuance nova:** antes de anular, a Sala disse que o 1/12 *"constituiría un complemento para la reglamentación de la depuración de la base de retención, porque la armoniza con su propio periodo de causación"* (p. 12). A anulação veio pela equidade, não por ilegalidade do rateio em si. O efeito prático é o mesmo: não existe mais norma que imponha 1/12.
6. **DIAN Concepto 011383 int. 433, de 11/06/2024** (compilação Ley 2277, 4.ª versão; o próprio documento diz *"únicamente informativo. Consultar desde los llamados los oficios o conceptos"*), IV.1. Local: `2026-10-30-DIAN-Oficio-11383-2024-dependientes-retencion.htm`. URL: https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_11383_2024.htm. *"la renta exenta en comento antes estaba «limitada mensualmente a doscientas cuarenta (240) UVT». Los agentes de retención … deberán observar disposiciones normativas como el numeral 10 del mencionado artículo 206, en particular su límite anual en los pagos realizados a cada persona natural."*
7. **Busca por concepto DIAN posterior a 2021 sobre o controle mês a mês:**
   - Não há concepto que descreva a mecânica do acumulado.
   - O Decreto 572/2025 (retenção) não mexe no art. 1.2.4.1.6, conferido no normograma DIAN.
   - Só a imprensa especializada (gerencie) cita o 1/12 (65,83 / 111,67 UVT) como "prudência" de alguns agentes. Não é fonte.

### Decisão
- **790, 1.340 e 3.800 UVT são anuais e são controlados pelo acumulado do ano por empregado, sem 1/12.** A lei diz "anualmente" (206-10), "anuales" (336-3) e "por año" (126-1, 126-4). O único 1/12 regulamentar foi anulado. O DIAN 11383 IV.1 manda o agente observar o limite anual "en los pagos realizados a cada persona natural".
- O 40% do ET 388 continua mensal.
- **Divergência registrada, que não muda esta decisão:** o 11383 IV.2 diz que o 1.340 não entra na retenção. Nossos finais o aplicam pelo DUR par. 3 (Decreto 2231/2023) e pela leitura do CE 24047 (decisão A-08). Isso decide **se** o 1.340 entra na retenção, não **como** se conta. Se entra, entra anual.

### Muda artefato?
Não. Já está aplicado:
- WTC v1.8 Tax Credit A41, A65–A68;
- CCG v1.6 (Version Control 1.6; T27R7; T228R5 com o 3.800 YTD);
- spec 004 v1.2 Field Options D22/D23.

### Confiança: 92%
O que falta para 100%:
- (a) concepto DIAN que descreva a mecânica mês a mês, por exemplo o que acontece com o saldo em mudança de empregador ou em migração no meio do ano;
- (b) o próprio CE disse que o 1/12 harmonizava com a periodicidade mensal. Um agente que aplique 1/12 por prudência não viola regra expressa, só retém a mais. Por isso o 1/12 pode ficar como opção configurável, com o anual-acumulado como padrão.

---

## Bloco de prova

**Pedido → resposta**
1. A-2 → decidido; já aplicado nos finais; sobe para 90% (não atinge 92%; falta doutrina DIAN para não residente; pergunta incluída no rascunho).
2. NE-18 → sem fonte oficial; mantido como interpretação configurável; consulta em espanhol redigida (§2.5), não enviada; 75%.
3. SIM-07 → 12.000.000 confirmado no instrutivo e no Concepto 1302/2019; 93%.
4. A-1 → anual e acumulado, sem 1/12, confirmado na parte decisória do CE 24047, no Decreto 2231 art. 9, no DUR vigente e no 11383/2024; 92%.

**Fontes lidas por mim nesta rodada** (texto extraído do arquivo local, não de resumo):
- Ley 100 art. 135;
- C-397/1994 (razão e parte resolutiva);
- DUR 1.2.4.1.11, 1.2.4.1.6 par. 3, 1.2.1.22.41 e 1.2.1.22.43;
- ET 206, 406, 408 e 126-1/126-4;
- DIAN 011108/2026 (íntegra), 577/2020 (íntegra), 57622/2003, 14740/2016, 26487/2018, 1302/2019, 4443/2025 e 11383/2024 IV.1–IV.2;
- instrutivo da casilla 59;
- CE 24047 (pp. 10–12 e falla);
- Decreto 2231 art. 9;
- PR-TAH-0352.

Os resumos do WebFetch e as notícias (gerencie, minomina, incp, asuntoslegales) só serviram para achar fontes. O resumo automático da C-397 trouxe um "efecto" invertido; descartei e li a sentença.

**Teste**
- Contas: 6 × 12.000.000 ÷ 6 = 12.000.000; 350 × 52.374 = 18.330.900; 790 × 52.374 = 41.375.460; 1.340 × 52.374 = 70.181.160; 3.800 × 52.374 = 199.021.200 (confere com CCG T116R3C1).
- Finais lidos só para conferir (python-docx e openpyxl, sem salvar): CO-CCG-001-v1.6.docx (T1, T86, T150), CO-WTC-001-v1.8.xlsx (N/P 120–122 e 321–322; Tax Credit A41/A65–A68), specs 004 (A26/C26/A34) e 005 (A28/C28/A35), spec 001 Field Options D66–D69, changelog da spec 004.

**Fontes novas baixadas** (`raw/docs/oficiais/CO/`, md5):

| Arquivo | md5 |
|---|---|
| `2026-11-02-CorteConstitucional-C-397-1994.htm` | `142a84a7f4d1632d3a569ea7908226f1` |
| `2026-11-02-DIAN-Concepto-577-2020-normograma.htm` | `7424e07c5fd28ec749a85bcda5c84056` |
| `2026-11-02-DIAN-Concepto-57622-2003-normograma.htm` | `727014a7a6cb1c180ed1399c77503267` |
| `2026-11-02-ET-pr005-art126-SecretariaSenado.html` | `e41c28434a6b4b1f039ae708aea05f92` |
| `2026-11-02-DIAN-PR-TAH-0352-gestion-incapacidades.pdf` | `9f938347b1efd3052fe94e625f0083c0` |

**Confiança por ponto:** A-2 90% · NE-18 75% · SIM-07 93% · A-1 92%.
- Abaixo de 92%: A-2 e NE-18. Os dois só sobem com resposta da DIAN; a consulta está redigida e só vai com ok do usuário.
- Pela regra "Fora do alcance" do PLANO-92, os dois ficam como opção configurável, com a nossa posição e a fonte.
