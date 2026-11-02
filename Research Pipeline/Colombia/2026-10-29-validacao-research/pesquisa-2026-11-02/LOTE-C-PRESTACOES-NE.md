# Lote C: prestações, Nómina Electrónica, SIR e WTC (pesquisa de 02/11/2026)

Frente Validação CO, ligada a [[Colombia]] e à `CONFERENCIA.md` da pasta `2026-10-29-validacao-research`. Antecedentes: `pesquisa-2026-10-30/PENDENTES-CCG-WTC.md` §11 (D9), `pesquisa-2026-10-30/PENDENTES-SPECS-DD.md` (NE-18, SIM-07, S-07) e `final/test0/RESIDUOS-DECISOES.md` ("Fora do pedido", coluna Y).

**Nenhum artefato foi alterado.** Este relatório só registra as decisões. Colômbia ativa: cada mudança precisa de ticket de alteração ao Development (regra 9).

## Tabela

| ID | Como está nos finais (célula) | Decisão | Muda artefato? Onde | Fonte primária | Confiança |
|---|---|---|---|---|---|
| D9 | WTC v1.7 `Wage Type Catalogue!W156` e `!W324` = **No** (V = "Paid Rest") | **Mantém fora.** A compensação de férias em dinero não é fator salarial, logo não entra na base de cesantía (CST 249/253) nem de prima (CST 306). Isso é doutrina reiterada da CSJ (rad. 16974/2002, rad. 33082/2009, SL467-2019, AL475-2022). | Não muda valor. Opcional: citar a CSJ na nota da linha (sem efeito no cálculo). | CSJ SL467-2019 (rad. 71281, 06/02/2019); CST 189 num. 3, 249, 253, 306 | **90%** (era 70%) |
| NE-18 | NE Spec `Field Options!D68` ("2 Profesional - interpretation: occupational disease…") e `!D69` ("3 Laboral - interpretation: occupational accident…") | **Mantém o texto atual, marcado como interpretação.** O anexo só traz "1 Común / 2 Profesional / 3 Laboral", sem definição. O XSD não restringe o valor (`xsd:integer`). Não há oficio da DIAN que defina os códigos. | Não | Anexo Técnico NE v1.0, tabela 5.5.6, p. 180; XSD 1.0.6 l. 592; Ley 1562/2012 arts. 3 e 4 | **75%** (era 65%) |
| SIM-07 | Spec 004 `Example Analysis!A26/C26` = 13.000.000 e `!A34` = 13.000.000; Spec 005 `Example Analysis!A28/C28` = 13000000 e `!A35` = 13000000. Conta atual: (6 × 12.000.000 + 6.000.000 de prima) ÷ 6. | **Muda para 12.000.000.** (1) Janela: com o contrato em curso, contam os seis meses do ano anterior à consignação (fev/2026 → jul–dez/2025), não os "últimos seis meses" de 2026. (2) Composição: só salário. A DIAN diz que entram "las sumas que habitual y periódicamente recibe el trabajador … como contraprestación directa del servicio", e a prima de servicios não é salário (CST 307). O ET 386 (procedimiento 2) não tem relação com esta casilla. | **Sim:** 004 A26, C26, A34; 005 A28, C28, A35 (valor e texto). A isenção não muda (continua abaixo de 350 UVT). | Instrutivo do Form. 220 (Res. DIAN 22/2024), casilla 59; DIAN Concepto 1302 [28563] de 2019; DIAN Concepto 4443/2025; CST 307 | **88%** (era 75%) |
| S-07 | SIR v1.2 texto final, Seção 4 l. 33: "more than 430 validation rules (R = rejection, N = notification), Anexo Técnico NE v1.0 §6" | **Trocar pela contagem exata.** O §6 do anexo tem 519 regras: 3 gerais (R), NominaIndividual 198 (189 R + 9 N), NominaIndividualDeAjuste 239 (219 R + 20 N), assinatura 56 (54 R + 2 sem marcação), conexão 23 (21 R + 2 N). Os dois documentos de nómina somam 437 (408 R + 29 N). Total: 486 R, 31 N, 2 sem marcação. O "433 = 406 + 27" não fecha por nenhum recorte. | **Sim:** SIR l. 33 (o texto atual não está errado, porque 437 > 430, mas é impreciso) | Anexo Técnico NE v1.0 §6, pp. 182–232 (contado por dois métodos) | **90%** |
| WTC-Y | WTC v1.7 `Y255`–`Y264` (V = "Non-Salary - pacted"): "Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183)…" | **Corrigir as 10 linhas** com o mesmo texto condicional já aplicado à família do carro (Y201–206, Y214–216): AuxilioNS (NIE142) quando há pacto não salarial; sem pacto, AuxilioS (NIE141). Na varredura completa apareceram também 13 linhas "Salary" com elemento NS (Y114–116, Y124–133) e 3 linhas "pacted" com S/NS sem condição (Y267, Y347, Y351). Lista abaixo. | **Sim:** Y255–Y264 (+ espelho na skill `references/02-wtc.md`, 10 linhas); recomendado Y114–116, Y124–133 e o cabeçalho V1; opcional Y267, Y347, Y351 | Anexo Técnico NE v1.0, NIE141/NIE142 p. 37, NIE139/140 pp. 36–37, NIE118/119 pp. 32–33, NIE147/148 p. 39; CST 127, 128 | **92%** (255–264); 80% (114–133) |

---

## 1. D9: compensação de férias em dinheiro na base de prima e cesantías

**Como está:** WTC v1.7 `W156` ("Annual leave payout", F = "Compensacion en dinero de vacaciones - up to HALF the accrued leave, on the employee's PRIOR WRITTEN request (CST art. 189 num. 1)") = **No**. `W324` ("Vacation compensated in cash") = **No**. A coluna T (parafiscais) continua Yes nas duas linhas. Não faz parte deste ponto.

**Lei (base de cálculo = salário):**
- CST art. 249 (`2026-11-02-CST-pr008-SecretariaSenado.html`, http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr008.html, acesso em 02/11/2026): *"Todo {empleador} esta obligado a pagar a sus trabajadores … como auxilio de cesantía, un mes de salario por cada año de servicios y proporcionalmente por fracción de año."*
- CST art. 253 (mesmo arquivo): *"Para liquidar el auxilio de Cesantía se toma como base el último salario mensual devengado por el trabajador … En el caso contrario y en el de los salarios variables, se tomará como base el promedio de lo devengado en el último año de servicios…"*
- CST art. 306 (`2026-10-30-CST-pr010-SecretariaSenado-notas.js`): *"…como prestación especial, una prima de servicios, así: … un mes de salario pagadero por semestres del calendario…"*
- CST art. 189 num. 1 e 3 (`2026-10-21-CST-pr006-SecretariaSenado.html`): *"Empleador y trabajador, podrán acordar por escrito, previa solicitud del trabajador, que se pague en dinero hasta la mitad de las vacaciones. … 3. Para la compensación de dinero de estas vacaciones … se tomará como base el último salario devengado por el trabajador."* O CST manda calcular a compensação **sobre** o salário, mas não diz que ela **é** salário.

**Jurisprudência (CSJ, Sala de Casación Laboral):**
- **CSJ SL467-2019**, rad. 71281, 06/02/2019, M.P. Clara Cecilia Dueñas Quevedo. Ficha oficial da Relatoria: `2026-11-02-CSJ-SL467-2019-ficha.pdf`, https://www.cortesuprema.gov.co/corte/wp-content/uploads/relatorias/la/bfeb2019/Ficha%20SL467-2019.pdf (acesso em 02/11/2026), pp. 9–10. A Sala transcreve e aplica sua doutrina anterior:
  > *"en sentencia CSJ SL 33082, 2 jun. 2009, la Sala adoctrinó que las vacaciones compensadas tienen una naturaleza indemnizatoria: '… no retribuyen el servicio y no están comprendidas dentro de las prestaciones especiales comprendidas en los capítulos VIII y IX del Código Sustantivo del Trabajo. … ese derecho compensatorio tiene una naturaleza jurídica diferente a las vacaciones y de manera pacífica ha sido catalogado como una indemnización, tal como esta Sala de la Corte lo precisó, entre muchas otras, en la sentencia del 27 de febrero de 2002, Rad. 16974, en los siguientes términos: "(…) también es verdad que tratándose de la compensación de vacaciones, tal rubro no puede tenerse como factor de salario (…) pues es indiscutible que la misma, tal y como lo ha precisado la Corte, es una especie de indemnización que el empleador paga al trabajador cuando por las circunstancias excepcionales, que la propia ley consagra, no puede disfrutar del descanso remunerado y reparador, que las vacaciones implican"'."*

  No caso, a condenação cassada era a "diferencia de la compensación de vacaciones dejada de cancelar a la accionante **durante la vigencia de la relación laboral**". A doutrina vale, portanto, também para a compensação paga com o contrato em curso, que é o caso do CST 189 num. 1 (W156/W324), e não só para a paga no desligamento.
- **CSJ AL475-2022**, rad. 85051, 16/02/2022 (Sala de Descongestión n.º 3), `2026-11-02-CSJ-SL-85051-2022-desc.pdf` (o nome do arquivo diz SL, mas é auto AL475-2022), https://cortesuprema.gov.co/corte/wp-content/uploads/not/laboraldesc22/prov/85051(16-02-2022).pdf, p. 3–4: *"es una compensación, que no el pago del derecho propiamente dicho, por tanto, se trata de un rubro que enmarca en el concepto genérico de indemnizaciones"*. Repete a mesma citação de 33082/2009 e 16974/2002.
- **CSJ SL16794-2015**, rad. 40907 (`2026-11-02-CSJ-SL16794-2015.pdf`), p. 14: registra que o Tribunal se apoiou em *"CSJ SL, 23 mar. 2011, rad. 34510 … para precisar que ni las vacaciones ni su compensación constituyen salario"*. Fica como reforço, porque a frase é do Tribunal, citada pela Corte.

**Doctrina probable:** são três sentenças de casación uniformes sobre o mesmo ponto (16974/2002, 33082/2009 e SL467-2019, mais AL475-2022). Não li a íntegra de 16974 nem de 33082: os trechos vêm transcritos pela própria CSJ em SL467-2019 e AL475-2022.

**Decisão:** W156 = No e W324 = No **ficam**. A cesantía e a prima se calculam sobre "salario" (CST 249, 253, 306), e a CSJ diz expressamente que a compensação "no puede tenerse como factor de salario". Os parafiscais (T = Yes, Ley 21 art. 17) seguem uma regra própria e não fazem parte deste ponto.

**O que falta para 100%:** ler a íntegra de rad. 16974/2002 e rad. 33082/2009 no site da CSJ. Nenhuma das duas trata da prima especificamente; a conclusão sobre a prima sai do art. 306 ("un mes de salario"). Conceito do MinTrabajo: não localizei texto oficial sobre o ponto (só resumos de terceiros), e ele ficaria abaixo da jurisprudência de qualquer forma.

---

## 2. NE-18: tipo de incapacidade (NIE126)

**Como está:** NE Spec `Field Options!D67` "1 Comun / General illness…", `!D68` "2 Profesional - interpretation: occupational disease ('enfermedad profesional', the pre-Ley 1562 de 2012 term for 'enfermedad laboral'); the annex (table 5.5.6) gives no definition. Funded by the ARL from day one at 100%. Confirm with DIAN.", `!D69` "3 Laboral - interpretation: occupational accident ('accidente de trabajo')…".

**Fontes:**
- Anexo Técnico NE v1.0 (Res. DIAN 000013/2021; caixa de ferramentas oficial `Caja-de-Herramientas-Nomina-Electronica-V1-0.zip`, a única ligada no micrositio DIAN de documentação técnica, conforme `2026-10-21-DIAN-micrositio-documentacion-tecnica-nomina.html`). Cópia local: `frentes/pipeline/mercans-pipeline/CO-compliance/integration-sources/dian-ne/caja/.../Anexo Tecnico Documento Soporte de Pago de Nómina Electrónica - V1.0.pdf` (md5 f848b528e1ca5871c881bc23bd42baab).
  - p. 180, **tabela 5.5.6 "Tipo de Incapacidad: Tipo"**: *"Código | Tipo de Incapacidad — 1 Común — 2 Profesional — 3 Laboral"*. Não há outra coluna nem definição.
  - p. 34, NIE126 `Tipo`: *"Se debe indicar el codigo al cual corresponda el tipo de incapacidad del Empleado"* / Observaciones: *"Se debe colocar el Codigo que corresponda de la tabla 5.5.6"*. NIE125: *"Número de días que el trabajador o aprendiz estuvo inactivo por incapacidad (sin importar su origen)"*. NIE127: *"Valor de la prestación económica pagada al trabajador por consecuencia de la falta de capacidad laboral sin importar su origen"*.
- XSD `NominaIndividualElectronicaXSDV1.0.6.xsd`, l. 592–594: `<xsd:attribute name="Tipo" type="xsd:integer" use="required" />`. Não há enumeração.
- DIAN Oficio 266 [901708] de 07/03/2022 (`2026-11-02-DIAN-Oficio-901708-2022-normograma.htm`, https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_901708_2022.htm, acesso em 02/11/2026): *"Dentro de la información a reportar se incluye el tipo de incapacidad, el valor pagado, las fechas de incapacidad y la cantidad de días."* Não define os códigos.
- Ley 1562/2012 (`2026-11-02-Ley-1562-2012-SecretariaSenado.html`, http://www.secretariasenado.gov.co/senado/basedoc/ley_1562_2012.html): art. 3 *"ACCIDENTE DE TRABAJO. Es accidente de trabajo todo suceso repentino que sobrevenga por causa o con ocasión del trabajo…"*; art. 4 *"ENFERMEDAD LABORAL. Es enfermedad laboral la contraída como resultado de la exposición a factores de riesgo inherentes a la actividad laboral…"*. O Decreto-Ley 1295/1994 (local) usava "enfermedad profesional".
- Prática de mercado (não é fonte oficial, só indício): miNómina, https://soporte.minomina.com/hc/es-419/articles/4406114775956 (acesso em 02/11/2026). *"Incapacidad Profesional: Enfermedad que se va generando paulatinamente a consecuencia de la prestación constante y diaria de las funciones de trabajo"*; *"Incapacidad Laboral: Es el accidente de trabajo que se produce en un momento puntual."* É a mesma leitura dos nossos D68/D69.

**Decisão:** D68 e D69 ficam como estão, já marcados como interpretação. Busquei no anexo, no XSD, na Res. 13/2021, no Abecé DSPNE, no oficio 901708/2022 e na busca do normograma DIAN, e não existe definição oficial. A leitura 2 = doença ocupacional e 3 = acidente de trabalho é a de mercado. Para o cálculo dá no mesmo: os dois são de origem laboral, pagos pela ARL a 100% desde o 1.º dia. Se o código errar, a DIAN não rejeita, porque o XSD aceita qualquer inteiro e não há regra de validação de domínio para NIE126. O efeito fica só na informação.

**Confiança 75%:** sem fonte oficial, não passa de 75–80%. O risco residual é a DIAN ter querido dizer "Profesional" = acidente e "Laboral" = doença, já que a Ley 1562 trocou "profesional" por "laboral" justamente para a doença. Fechar só com consulta formal à DIAN (PQSR).

---

## 3. SIM-07: casilla 59 (Form. 220) / numeral 33 (Formato 2276)

**Como está:**
- Spec 004 `Example Analysis!A26` = "13.000.000"; `!C26` = "The rolling six-month average of labour income, of the last six months, (6 x 12,000,000 salary + 6,000,000 December prima instalment) / 6 = 13,000,000. Composition … is an interpretation … Confirm with DIAN."; `!A34` (não residente) = "13.000.000".
- Spec 005 `Example Analysis!A28` = "13000000"; `!C28` com a mesma conta; `!A35` (não residente) = "13000000".
- Cenário (004 `!A5–A6`, `!A20`): empregado ativo o ano inteiro de 2026, salário de 12.000.000 por mês, cesantías de 2025 consignadas até 14/02/2026, juros pagos em janeiro de 2026.

**Qual formulário e qual norma:** a casilla 59 é do **Formulário 220** (Res. DIAN 000022/2024) e o numeral 33 é do **Formato 2276** (Res. 162/2023 art. 51 num. 33, hoje compilada na Res. 227/2025). As duas remetem ao **ET art. 206 num. 4** (isenção de cesantías). Nenhuma remete ao ET art. 386 / DUR 1.2.4.1.x ("procedimiento 2", média de 12 meses para o percentual de retenção), que é outro instituto.

**Fontes:**
- ET art. 206 num. 4 (`2026-10-22-ET-pr008-SecretariaSenado.html`): *"El auxilio de cesantía y los intereses sobre cesantías, siempre y cuando sean recibidos por trabajadores cuyo ingreso mensual promedio en los seis (6) últimos meses de vinculación laboral no exceda de 350 UVT. Cuando el salario mensual promedio a que se refiere este numeral exceda de 350 UVT…"*
- **Instrutivo oficial do Form. 220** (Res. DIAN 22/2024, anexo; `2026-10-30-Res-DIAN-0022-2024-Form220-com-anexo-normograma.txt`, l. 240–266): *"59. Ingreso laboral promedio de los últimos seis meses anteriores (numeral 4 art. 206 E.T.): … (ii) cuando la relación laboral o legal y reglamentaria no ha finalizado … En el caso de que la relación laboral o legal y reglamentaria no haya finalizado, este término tomará en consideración los seis meses del año inmediatamente anterior del momento en que las cesantías se consignan o se consolidan y quedan disponibles en las cuentas individuales…"*
- **DIAN Concepto 1302 [28563] de 25/11/2019** (adiciona o Concepto General Unificado 0912/2018; `2026-11-02-DIAN-Concepto-1302-2019-normograma.htm`, https://normograma.dian.gov.co/dian/compilacion/docs/concepto_tributario_dian_0001302_2019.htm, acesso em 02/11/2026): *"…se considera oportuno precisar que este ingreso corresponderá a las sumas que habitual y periódicamente recibe el trabajador en dinero o en especie como contraprestación directa del servicio, pues la norma lo que busca es establecer es el salario mensual promedio."* O conceito afasta expressamente o art. 103 ET (definição ampla de renda do trabalho) como critério. Ele aclara o Concepto 17602/2005 (`2026-11-02-DIAN-Concepto-17602-2005-normograma.htm`), que já dizia: *"por regla general será el salario la base sobre la cual se liquiden las cesantías y el porcentaje de exención"*.
- **DIAN Concepto 4443 de 09/04/2025** (local `2026-10-21-DIAN-Concepto-4443-2025.htm`), sobre o numeral 33 do 2276 e a casilla 59: *"…debe tener en cuenta el promedio salarial de este término. 8. Promedio salarial que para efectos del diligenciamiento del ingreso laboral promedio de los últimos 6 meses anteriores (numeral 4 art. 206 E.T.) correspondiente al renglón 59 del Formulario 220 … ii) La relación laboral o reglamentaria no ha finalizado: Se debe tomar los 6 meses del año inmediatamente anterior al momento de la consignación de las cesantías…"*
- CST art. 307 (`2026-10-30-CST-pr010-SecretariaSenado.html`): *"La prima anual no es salario, ni se computará como factor del salario en ningún caso."*

**Decisão:** a média do exemplo está errada em dois pontos.
1. **Janela:** o contrato está em curso e a consignação foi em fevereiro de 2026, então a janela é **jul–dez de 2025**, não "os últimos seis meses" de 2026.
2. **Composição:** só o salário. A prima de servicios sai (CST 307 + DIAN 1302/2019 + 4443/2025).

Com o salário de 12.000.000 também em jul–dez de 2025 (o cenário não diz o contrário), a média é **12.000.000**. A conclusão não muda: 12.000.000 < 350 UVT × 52.374 = 18.330.900, isenção total.

**Texto proposto (EN), 004 C26 / 005 C28:** "Employment is ongoing, so the window is the six months of 2025, the year before the February 2026 deposit (Form 220 instructions, casilla 59, case (ii); DIAN Concepto 1302 of 2019; DIAN Concepto 4443 of 2025). Only salary counts: 'las sumas que habitual y periódicamente recibe el trabajador … como contraprestación directa del servicio' (DIAN Concepto 1302 of 2019); the service bonus is not salary (CST art. 307). Assuming the same COP 12,000,000 monthly salary in July–December 2025: average = 12,000,000. For a leaver, use the last six months of employment."
A26 / A28 → 12.000.000; A34 / A35 (não residente) → 12.000.000.

**Por que 88%:** a composição vem de doutrina DIAN (concepto, abaixo de lei e decreto), mas ela é geral, reiterada em 2025 e coerente com o texto da lei ("salario mensual promedio"). A janela vem do instrutivo oficial do formulário. O que falta: nenhuma norma de hierarquia superior lista os itens da média.

---

## 4. S-07: contagem das regras de validação da NE (SIR l. 33)

**Como está:** SIR v1.2 texto final, Seção 4 (l. 33–36): "more than 430 validation rules (R = rejection, N = notification), Anexo Técnico NE v1.0 §6". A versão anterior trazia "433: 406 R + 27 N".

**Fonte:** Anexo Técnico NE v1.0, §6 "Reglas y Mensajes de Validación", pp. 182–232 (mesmo PDF oficial do item 2). p. 182: *"La Columna 'Y' contiene, la definición si una regla determina rechazo ('R') o notificación ('N'). Un documento solamente puede recibir el sello de 'validado' si no falla en ninguna validación identificada por 'R'."*

**Contagem (IDs únicos, por seção):**

| Seção (página) | Regras | R | N | Sem Y |
|---|---|---|---|---|
| §6 "Se informa la incorporación de las siguientes reglas" (p. 182): 90, 92, VLR01 | 3 | 3 | 0 | 0 |
| §6.1.1 NominaIndividual (pp. 182–198) | 198 | 189 | 9 | 0 |
| §6.1.2 NominaIndividualDeAjuste (pp. 198–220) | 239 | 219 | 20 | 0 |
| §6.1.3 ds:Signature (pp. 221–230), DC01–DC56 | 56 | 54 | 0 | 2 (DC34 CertDigest, DC36 DigestValue, p. 226) |
| §6.2 Conexão (pp. 231–232): ZA01–ZE03 | 23 | 21 | 2 (ZA02, ZA03) | 0 |
| **Total** | **519** | **486** | **31** | **2** |

Os dois documentos de nómina somam 437 regras (408 R + 29 N). Nenhum recorte dá 433/406/27.

**Teste mecânico:** contei por dois métodos independentes. (a) Texto com layout (PyMuPDF), regex `ID + R|N` linha a linha. (b) Extração de tabelas (pdfplumber). As diferenças entre os dois foram conferidas uma a uma: NIE901, DC01–DC07 e a seção 6.2 escaparam do método (b) por causa do layout; o "R" de DC01–DC07 foi confirmado pela posição da palavra na p. 221. DC34/DC36 não têm R nem N nos dois métodos. Também procurei IDs (NIE/NIAE/DC/Z*) no começo de linha que tivessem ficado de fora da contagem: só faltavam esses dois.

**Decisão:** trocar pelo número exato. Texto proposto (EN, SIR l. 33): "Anexo Técnico NE v1.0 §6 lists 519 validation rules: 437 for the payroll documents (NominaIndividual 198 = 189 R + 9 N; NominaIndividualDeAjuste 239 = 219 R + 20 N), 56 for the digital signature (54 R; 2 without a flag), 23 for the connection (21 R + 2 N) and 3 general rules (R). R = rejection, N = notification." O texto atual ("more than 430") não está errado, mas é impreciso.

**Por que 90%:** a contagem foi feita por máquina sobre um PDF de tabelas com quebras de linha. Os dois métodos convergem e as diferenças foram explicadas, mas não houve conferência visual página a página.

---

## 5. WTC v1.7, coluna Y: "pacted" → elemento S/NS

**Regra do cabeçalho:** `V1`: *"Salary or Non-Salary (CST arts. 127 / 128) - hard flag for the nomina electronica S / NS elements. … Where the nature is unclear the row is 'pacted' and the DD non-salary pact flag decides. Both values map to the nomina electronica NS element."*

**Anexo Técnico NE v1.0 (o que é cada elemento):**
- p. 37, NIE141 `AuxilioS`: *"Son beneficios, ayudas o apoyos económicos, pagados al trabajador de forma habitual o pactados entre las partes como factor salarial."* / "Valor Pagado por Auxilios Salariales".
- p. 37, NIE142 `AuxilioNS`: *"Son beneficios, ayudas o apoyos económicos, pagados al trabajador de forma ocasional y por mera liberalidad o los pactados entre las partes de forma expresa como pago no salarial."* / "Valor Pagado por Auxilios No Salariales".
- p. 36, NIE139 `BonificacionS`: *"Son valores pagados al trabajador en forma de incentivo o recompensa por la contraprestación directa del servicio."*; p. 37, NIE140 `BonificacionNS`: *"…de forma ocasional y por mera liberalidad o los pactados entre las partes de forma expresa como pago no salarial."*
- p. 32, NIE118 `Primas/Pago`: Observaciones *"Valor Pagado por Prima Legal con respecto a Cantidad de Dias"*; p. 33, NIE119 `PagoNS`: *"…de forma ocasional y por mera liberalidad o los pactados entre las partes de forma expresa como pago no salarial."* / "Valor Pagado por Prima No Salarial".
- p. 39, NIE147 `ConceptoS`: *"…pagos fijos o variables realizados al trabajador que remuneren … como contraprestación directa del servicio … (Salarial)"*; NIE148 `ConceptoNS`: *"…ocasionalmente y por mera liberalidad … (No Salarial)"*.
- CST art. 128 (`2026-10-21-CST-pr004-SecretariaSenado.html`): *"…Tampoco las prestaciones sociales …, ni los beneficios o auxilios habituales u ocasionales acordados convencional o contractualmente u otorgados en forma extralegal por el {empleador}, cuando las partes hayan dispuesto expresamente que no constituyen salario…"*

**Conclusão:** um auxílio não salarial por pacto expresso (CST 128) vai em **AuxilioNS (NIE142)**. AuxilioS (NIE141) é o auxílio habitual sem pacto, que é salário (CST 127). Precedente já aplicado no v1.7: família do carro, `Y201–206`, `Y214–216` (CHANGELOG WTC v1.7, itens 84–100).

**Varredura completa** (script em todas as linhas: V começa com "Non-Salary" e Y tem elemento S, ou V = "Salary" e Y tem elemento NS):

### 5.1 Corrigir (pedido): "pacted" apontando só para S

| Linha | B (nome) | Y atual | Y proposto |
|---|---|---|---|
| 255 | Education allowance | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Devengados / Auxilio (AuxilioNS, NIE142, where non-salary under the pact; otherwise AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| 256 | Schooling allowance | idem | idem |
| 257 | Arrears - Schooling allowance | idem | idem |
| 258 | Education & Schooling allowance 2 | idem | idem |
| 259 | Arrears - Education & Schooling allowance 2 | idem | idem |
| 260 | Education & Schooling allowance 3 | idem | idem |
| 261 | Education & Schooling allowance 4 | idem | idem |
| 262 | Arrears - Education & Schooling allowance 4 | idem | idem |
| 263 | Education & Schooling allowance 5 | idem | idem |
| 264 | Arrears - Education & Schooling allowance 5 | idem | idem |

O mesmo texto aparece em `final/skill/payroll-compliance-colombia/references/02-wtc.md` (10 ocorrências), que precisa da mesma troca para não divergir do WTC.

### 5.2 Recomendado: "Salary" apontando também para NS (incoerência inversa)

| Linha | B | V | Y atual | Y proposto |
|---|---|---|---|---|
| 114 | Holiday Allowance | Salary | Devengados / Primas - PagoNS (NIE119) or Bonificacion (NIE139 / NIE140) | Devengados / OtroConcepto - ConceptoS (NIE147) or Bonificacion - BonificacionS (NIE139) |
| 115 | Arrears - Holiday Allowance | Salary | idem | idem |
| 116 | Adjustment - Holiday Allowance | Salary | idem | idem |
| 124–133 (10 linhas) | Bonus (annual, referral, etc) | Salary | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Devengados / Bonificacion - BonificacionS (NIE139) |

Motivo: V é "hard flag". Uma linha "Salary" não pode cair em PagoNS, que o anexo define como "Prima No Salarial". NIE118 (`Pago`) é só da prima legal, por isso a prima de férias extralegal salarial vai em ConceptoS ou BonificacionS. O bônus não salarial já tem linha própria ("pacted", ex. 267 e CO-BONIF-NOSALARIAL). Confiança 80%: a escolha entre ConceptoS e BonificacionS para a linha 114 é nossa, porque o anexo não traz "prima extralegal salarial".

### 5.3 Opcional (coerente, mas com redação diferente da família do carro)

| Linha | B | Y atual | Sugestão |
|---|---|---|---|
| 267 | Recognition Award | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Devengados / Bonificacion (BonificacionNS, NIE140, where non-salary under the pact; otherwise BonificacionS, NIE139) |
| 347 | Voucher, card or non-cash instrument payment | Devengados / BonoEPCTV - PagoS (NIE151) / PagoNS (NIE152) | Devengados / BonoEPCTV (PagoNS, NIE152, where non-salary under the pact; otherwise PagoS, NIE151) |
| 351 | Equity and share-incentive awards | Devengados / OtroConcepto - ConceptoS or ConceptoNS (NIE146-NIE148) | Devengados / OtroConcepto (ConceptoNS, NIE148, where non-salary under the pact; otherwise ConceptoS, NIE147) |

### 5.4 Cabeçalho V1
A última frase ("Both values map to the nomina electronica NS element") contradiz a família do carro e a proposta 5.1. Sugestão (EN): "Both values map to the nomina electronica NS element where the non-salary pact holds (DD pact flag set); without the pact the payment is salary under CST art. 127 and maps to the S element."

### 5.5 Pendência (sem proposta de troca)
- Linha 346 "Third-party meal payments": V = "Non-Salary - non-remunerative", Y = "BonoEPCTV - PagoAlimentacionS (NIE153) / PagoAlimentacionNS (NIE154)". O conflito é real, mas a questão está em **V**: alimentação é salário em espécie salvo pacto (CST 128/129), e por isso V não deveria ser "non-remunerative". Precisa de decisão sobre V antes de mexer em Y. Vai para Pendências do hub.

**Confiança:** 92% para 255–264. As definições do anexo são literais e o precedente da família do carro já está aplicado. 80% para 114–133.

---

## Bloco de prova

- **Pedido → resposta:**
  1. D9: decidido (mantém fora), com sentença da CSJ explícita, 90%.
  2. NE-18: códigos confirmados na tabela 5.5.6, p. 180, e no XSD; não há definição oficial; texto atual mantido, 75%.
  3. SIM-07: formulário certo (220 casilla 59 / 2276 num. 33, ET 206 num. 4; ET 386 não se aplica); janela e composição decididas, valor muda para 12.000.000, 88%.
  4. S-07: contagem exata de 519 (486 R / 31 N / 2 sem Y), com páginas, 90%.
  5. WTC Y: varredura completa; 10 linhas a corrigir (255–264), 13 recomendadas (114–116, 124–133), 3 opcionais (267, 347, 351), cabeçalho V1 e 1 pendência (346).
- **Fontes novas gravadas em `raw/docs/oficiais/CO/`** (só criados, nada editado):
  - `2026-11-02-CSJ-SL467-2019-ficha.pdf` (md5 e8b82cc89b11f1d8dd3b7689afc11208)
  - `2026-11-02-CSJ-SL-85051-2022-desc.pdf` (= AL475-2022; md5 7078de19266d4c3a298ced75e912f39e)
  - `2026-11-02-CSJ-SL16794-2015.pdf` (md5 d6fc6a3d8192b56b2e35c48da8ebc535)
  - `2026-11-02-CST-pr008-SecretariaSenado.html` (CST 249/253; md5 9a8125fd0d6eb297a43b95ae7fdabc8e)
  - `2026-11-02-CST-pr009-SecretariaSenado.html` (baixado por engano de faixa, arts. 268+; não citado; md5 214e0e4b2a1309706c41e88101281975)
  - `2026-11-02-DIAN-Concepto-1302-2019-normograma.htm` (md5 a4d2adc0fcec35c09b7282c0b7524ad5)
  - `2026-11-02-DIAN-Concepto-17602-2005-normograma.htm` (md5 8cfce3091b893967cd5239935ab9b51a)
  - `2026-11-02-DIAN-Oficio-901708-2022-normograma.htm` (md5 6486bc091c55c13c3424841d397623eb)
  - `2026-11-02-Ley-1562-2012-SecretariaSenado.html` (md5 66444db23bce30328812db44f5ae62a0)
- **Teste mecânico:**
  - S-07: contagem por dois métodos com as diferenças reconciliadas.
  - WTC: script de varredura V × Y nas 1.000 linhas.
  - SIM-07: conta refeita (6 × 12.000.000 ÷ 6 = 12.000.000; 350 × 52.374 = 18.330.900).
  - NE-18: XSD conferido (`xsd:integer`, sem enumeração).
  - Células citadas lidas com openpyxl nos finais (WTC v1.7, specs 001/004/005) e na l. 33 do SIR v1.2.
- **Confiança média do lote:** ~87%. Abaixo de 80%: só NE-18 (75%), por falta de definição oficial; fechar com PQSR à DIAN.
