# Lote C, rodada 6: S-07, WTC coluna Y, DD-21, D9 e auxílios de carro (02/11/2026)

Frente Validação CO, ligado a [[PLANO-92]], [[TABELA-RODADA5]], [[LOTE-C-PRESTACOES-NE]] e [[Colombia]].

**Nenhum artefato foi alterado.** A research CO não está em produção, então não há ticket ao Development. Conferi os finais atuais em `final/`: WTC v1.8 (md5 `8e05d1c4306a55331c93190af3316747`), DD v1.5 e SIR v1.3. Várias trocas da rodada 5 **já estão aplicadas** neles. Nesta rodada eu confirmo essas trocas na fonte e aponto só o que ainda falta.

## Tabela

| # | Ponto | Decisão | Muda artefato? | Conf. |
|---|---|---|---|---|
| 10 | S-07: regras da NE | **519 confirmadas por script**: 3 gerais (R); NominaIndividual 198 (189 R + 9 N); Ajuste 239 (219 R + 20 N); firma 56 (54 R + 2 sem marcação); conexão 23 (21 R + 2 N). No total, 486 R, 31 N e 2 sem marcação. | Não. O SIR v1.3 (l. 35 do texto final, l. 220 do export) já traz a contagem certa. | **97%** |
| 11 | WTC coluna Y: AuxilioS/AuxilioNS | As trocas da rodada 5 **estão certas e já estão no v1.8**: Y255–264 com AuxilioNS e, sem pacto, AuxilioS; Y114–116 e Y124–133 = BonificacionS; cabeçalho V1 alinhado. A skill `02-wtc.md` também já foi trocada (10 ocorrências). | Nenhuma troca obrigatória. Opcional: 16 linhas "pacted" sem condicional (§11.4). | **95%** (255–264, 124–133); **90%** (114–116) |
| 12 | DD-21: dados bancários | O Anexo **não lista** quais códigos são "bancários". Só diz *"Si el método de pago se realiza de forma bancaria"*, e as regras NIE066–068 e NIAE066–068 são **N** (só notificam, não rejeitam). Por isso a lista positiva do DD é interpretação nossa, e o DD já a declara assim. 42/45/47/98 estão certos. O **46** (Transferencia Débito Interbancario) também é bancário, mas não está no mapper. | Não obrigatório. Opcional: incluir 46 no Mapper (C97–C104) e em H7. | **93%** |
| 13 | D9: férias compensadas | **Fora da base de seguridade social (Q, R, S, U = No): confirmado.** **Fora dos parafiscais: não.** Elas **entram** na base de SENA, ICBF e CCF (Ley 21 art. 17, "descansos remunerados"). O WTC v1.8 já está assim (T = Yes). A premissa "fora de parafiscais" do pedido está errada; o artefato está certo. | Não muda valor. Opcional: atualizar a nota D156/D324, que ainda diz "no express Supreme Court ruling located". | **94%** |
| 14 | Auxílio de carro / rodamiento | **Depende da finalidade, não do nome nem do pacto.** Se é pago para o trabalhador fazer o trabalho (meio de transporte), não é salário por natureza (CST 128) e fica fora do IBC e do teste dos 40% (CE SU 25185/2021). Se retribui o serviço, é salário (CST 127), e um pacto não muda isso (CSJ SL5159-2018 §3.3). Se é um benefício que não retribui e foi pactado como não salarial, conta como "pacted" e entra no teste dos 40%. O WTC v1.8 (201–206, 214–216) segue esse modelo: padrão "pacted" e reconfiguração para "non-remunerative". | Não muda valor. Opcional: reescrever a 1.ª frase de AB201–206/AB214–216 (§14). | **92%** |

---

## 10. S-07: contagem das regras de validação da NE

**Fonte:** Anexo Técnico Documento Soporte de Pago de Nómina Electrónica v1.0 (Res. DIAN 000013 de 11/02/2021), §6, pp. 182–232.
- Local: `Research Pipeline/Colombia/CO-compliance/00-official-sources/pdfs/AnexoTecnico-NominaElectronica-V1.0.pdf`, md5 `f848b528e1ca5871c881bc23bd42baab`. É idêntico ao PDF da Caja de Herramientas em `CO-compliance/integration-sources/dian-ne/caja/.../Anexo Tecnico Documento Soporte de Pago de Nómina Electrónica - V1.0.pdf`.
- URL: micrositio DIAN de documentação técnica da nómina (Caja-de-Herramientas-Nomina-Electronica-V1-0.zip; página salva em `raw/docs/oficiais/CO/2026-10-21-DIAN-micrositio-documentacion-tecnica-nomina.html`).

**Trecho literal (p. 182):** *"La Columna 'Y' contiene, la definición si una regla determina rechazo ('R') o notificación ('N'). Un documento solamente puede recibir el sello de 'validado' si no falla en ninguna validación identificada por 'R'."*

**Método (reprodutível), em `pesquisa-2026-11-02-r6/scripts/`:**
1. `contar_regras_ne.py` (md5 `f2ec2a1d087fbf28d0a0d327c425ec1d`). Trabalha pela posição das palavras (PyMuPDF):
   - cada ID na coluna esquerda (`90`, `92`, `VLR01`, `NIE…`, `NIAE…`, `DC..`, `ZA..`–`ZE..`) conta como uma regra;
   - o R ou N vem da coluna "Y" na faixa vertical da linha; quando a página não repete o cabeçalho, a coluna é herdada da página anterior;
   - a seção é dada pelos títulos "Se informa la incorporación", 6.1.1, 6.1.2, 6.1.3 e 6.2.
   - Uso: `python -I contar_regras_ne.py <PDF> --detalhe`.
2. `conferir_regras_ne.py` (md5 `20838f0e9abc620094de589c3714ae1f`). Conferência independente:
   - (a) conta todo R/N isolado na coluna Y **sem olhar o ID**;
   - (b) conta os IDs únicos que aparecem em qualquer posição do texto.

**Resultado:**

| Seção | Regras | R | N | Sem Y |
|---|---|---|---|---|
| Gerais (p. 182: 90, 92, VLR01) | 3 | 3 | 0 | 0 |
| 6.1.1 NominaIndividual | 198 | 189 | 9 | 0 |
| 6.1.2 NominaIndividualDeAjuste | 239 | 219 | 20 | 0 |
| 6.1.3 ds:Signature | 56 | 54 | 0 | 2 (DC34 CertDigest, DC36 DigestValue, p. 226) |
| 6.2 Conexão | 23 | 21 | 2 (ZA02, ZA03) | 0 |
| **Total** | **519** | **486** | **31** | **2** |

**Teste:**
- O método (a) dá 486 R + 31 N = 517, sem nenhum R/N "órfão".
- O método (b) dá NIE 198, NIAE 239, DC 56, ZA–ZE 23 e VLR 1, mais 90 e 92: 519.
- DC34 e DC36 sem marcação foram conferidos visualmente na imagem da p. 226.
- Durante o desenvolvimento, o script errou duas vezes: DC08–DC56 sem cabeçalho na página, e DC56 lido com a coluna da seção 6.2. As duas falhas foram corrigidas e explicadas antes do resultado final. A contagem bate com a do agente da rodada 5 em todos os números.

**O que falta para 100%:**
- conferir visualmente as ~50 páginas (só as diferenças foram vistas);
- confirmar que a DIAN não publicou anexo posterior à v1.0 com regras novas. A coluna Y do WTC cita "Res. DIAN 000227 de 2025, Anexo Técnico v1.0"; se houver versão nova do anexo, recontar com o mesmo script.

---

## 11. WTC coluna Y: AuxilioS (NIE141) × AuxilioNS (NIE142)

**Anexo NE v1.0 (mesmo PDF), trechos literais:**
- p. 37, NIE141 `AuxilioS`: *"Son beneficios, ayudas o apoyos económicos, pagados al trabajador de forma habitual o pactados entre las partes como factor salarial."* (Observaciones: "Valor Pagado por Auxilios Salariales").
- p. 37, NIE142 `AuxilioNS`: *"…pagados al trabajador de forma ocasional y por mera liberalidad o los pactados entre las partes de forma expresa como pago no salarial."*
- p. 36, NIE139 `BonificacionS`: *"Son valores pagados al trabajador en forma de incentivo o recompensa por la contraprestación directa del servicio."*
- p. 37, NIE140 `BonificacionNS`: *"…de forma ocasional y por mera liberalidad o los pactados entre las partes de forma expresa como pago no salarial."*
- p. 32, NIE118 `Primas/Pago`: Observaciones *"Valor Pagado por Prima Legal con respecto a Cantidad de Dias"*. p. 33, NIE119 `PagoNS`: *"Valor Pagado por Prima No Salarial"*.
- p. 39, NIE147 `ConceptoS`: *"…que remuneren en dinero o en especie como contraprestación directa del servicio … (Salarial)"*.

**CST** (`raw/docs/oficiais/CO/2026-10-22-CST-pr004-SecretariaSenado.html`; http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr004.html):
- art. 127: *"Constituye salario … todo lo que recibe el trabajador … como contraprestación directa del servicio … como primas, sobresueldos, bonificaciones habituales…"*
- art. 128: *"…ni los beneficios o auxilios habituales u ocasionales acordados convencional o contractualmente u otorgados en forma extralegal por el {empleador}, cuando las partes hayan dispuesto expresamente que no constituyen salario … tales como la alimentación, habitación o vestuario, las primas extralegales, de vacaciones, de servicios o de navidad."*

**Conferência linha a linha (WTC v1.8, `Wage Type Catalogue`):**

| Linhas | V | Y no v1.8 | Certo? | Por quê |
|---|---|---|---|---|
| 255–264 (education / schooling) | Non-Salary - pacted | AuxilioNS (NIE142) com pacto; sem pacto, AuxilioS (NIE141); Educacion (NIE183) para dívida | **Sim** | NIE142 = "pactados … como pago no salarial"; sem pacto o auxílio habitual é salário (CST 127) → NIE141 |
| 124–133 (bonus annual / referral) | Salary | BonificacionS (NIE139) | **Sim** | Bônus habitual = salário (CST 127, "bonificaciones habituales"); NIE139 = "contraprestación directa del servicio". O não salarial tem linhas próprias (134–153, 316) |
| 114–116 (holiday allowance) | Salary | BonificacionS (NIE139) | **Sim, por escolha nossa** | Prima de férias extralegal sem pacto é salário. NIE118 é só a prima legal e NIE119 é a não salarial, então nenhum dos dois serve. O anexo não tem "prima extralegal salarial"; BonificacionS e ConceptoS (NIE147) são as duas leituras possíveis |
| V1 (cabeçalho) | — | "…'Non-Salary - pacted' maps to the NS element where the non-salary pact holds (DD pact flag set) and, without the pact, to the S element (salary under CST art. 127)." | **Sim** | Coerente com NIE141/142 e CST 127/128 |

Registro: CHANGELOG `final/changelogs/CO-WTC-001-v1.8-CHANGELOG.md`, itens 30–53. A skill espelho `final/skill/payroll-compliance-colombia/references/02-wtc.md` tem 10 ocorrências do texto novo e 0 do antigo.

### 11.4 Fora do pedido: varredura V × Y no v1.8
- **Sem a condicional "otherwise S":** são linhas "pacted" que só apontam para o elemento NS. Isso contradiz o próprio V1 ("without the pact, to the S element"). As linhas são:
  - 230 (COVID-19), 231–237 (medical insurance), 253–254 (benefits plan): Y = "Auxilio (AuxilioNS, NIE142)";
  - 348 (medicina prepagada): "Auxilio - AuxilioNS (NIE142)";
  - 349–350 (aportes voluntários de pensão): "Auxilio - AuxilioNS (NIE142)".

  Sugestão: o mesmo texto condicional de 201–206.
- **S/NS listados sem condição:** 267 (Recognition Award), 347 (vouchers) e 351 (equity). Sugestão de texto já está no LOTE-C r5 §5.3.
- Nada disso muda cálculo, só o elemento da NE quando não há pacto. Deixo como opcional.

**O que falta para 100%:** a DIAN não define onde vai a "prima extralegal salarial" (114–116). Fechar só com PQSR, ou deixar configurável entre NIE139 e NIE147.

---

## 12. DD-21: forma e meio de pagamento, dados bancários

**Anexo NE v1.0, trechos literais:**
- p. 23, NIE064 `Forma`: *"Se debe colocar el Codigo de la tabla 5.3.3.1"* (1-1).
- p. 24, NIE065 `Metodo`: *"Se debe colocar el Codigo de la tabla 5.3.3.2"* (1-1).
- p. 24, NIE066 `Banco`, NIE067 `TipoCuenta` e NIE068 `NumeroCuenta`: ocorrência **0-1**, *"Si el método de pago se realiza de forma bancaria. Se debe colocar el nombre de la entidad bancaria donde el trabajador tiene su cuenta para pago de nómina."*
- p. 61, NIAE066–068 (Ajuste): *"Si el Metodo de Pago se realiza de forma Bancaria, este campo es obligatorio."*
- pp. 188–189, regras: *"NIE066 N Banco…"*, *"NIE067 N TipoCuenta…"*, *"NIE068 N NumeroCuenta…"*. No Ajuste, NIAE066/067/068 também são **N** (saída do script do ponto 10). O texto diz "obligatorio", mas a falha **não rejeita** o documento.
- p. 130, tabela 5.3.3.1: só *"1 Contado"*.
- p. 130, tabela 5.3.3.2: 1–98 + ZZZ, entre eles:
  - *"10 Efectivo"*, *"20 Cheque"*;
  - *"42 Consignación bancaria"*, *"45 Transferencia Crédito Bancario"*, *"46 Transferencia Débito Interbancario"*, *"47 Transferencia Débito Bancaria"*;
  - *"48 Tarjeta Crédito"*, *"49 Tarjeta Débito"*, *"71 Bonos"*, *"72 Vales"*;
  - *"98 Cuentas de Ahorro de Tramite Simplificado (CATS)(Nequi, Daviplata, etc)"*.

  A tabela **não tem** coluna "bancário sim/não".
- XSD `NominaIndividualElectronicaXSDV1.0.6.xsd`, l. 267–275 (`achados/ne-work/val/XSD/`): `Forma` e `Metodo` são `use="required"`; `Banco` e `TipoCuenta` não têm `use`, ou seja, são opcionais.

**DD v1.5:**
- `ID Information!H7`: *"Partial list. … populated only for account-crediting payment methods … 42 …, 45 …, 47 … and 98 (CATS: Nequi, Daviplata); left empty for 10 …, 20 …, 71 … and 72 …. Cards (48, 49) … an interpretation. … The bank / non-bank classification of each code is an interpretation; confirm with DIAN."*
- H8 e H9 remetem a H7.
- `Country Option Mappers!C95:C104` (Payment Method) traz 10, 20, 42, 45, 47, 48, 49, 71, 72 e 98. A linha 98 já foi acrescentada (F104: "Account-based: the bank attributes are populated").

**Decisão:**
- A lista positiva 42/45/47/98 está certa e o DD v1.5 já a aplica. A classificação é nossa, porque o anexo só diz "forma bancaria" e o DD já declara isso.
- O código **46** (Transferencia Débito Interbancario) é tão bancário quanto o 47. Não está no mapper, então hoje nem pode ser escolhido. Incluir é opcional: Mapper nova linha 46 e menção em H7.
- 48/49 continuam como interpretação condicional, sem mudança.
- Risco prático baixo: se a classificação errar, a DIAN só notifica (N) e não rejeita.

**O que falta para 100%:** não há fonte oficial que liste os códigos "bancários". Só uma PQSR à DIAN fecharia; para o cálculo e a validação isso não muda nada.

---

## 13. D9: férias compensadas em dinheiro e as bases de contribuição

**Como está (WTC v1.8, linhas 156 "Annual leave payout" e 324 "Vacation compensated in cash"):**

| Coluna | Q Saúde | R FSP | S ARL | T Parafiscais | U Pensão | V | W Prestações |
|---|---|---|---|---|---|---|---|
| Valor | No | No | No | **Yes** | No | Paid Rest | No |

A nota D156/D324 diz: *"Payroll levies stay Yes (Ley 21 de 1982 art. 17, paid rest). This is an interpretation (no express Supreme Court ruling located)…"*

**Decisão:**
1. **Seguridad social (saúde, pensão, ARL e FSP) = fora: confirmado.**
   - O IBC só tem fatores salariais (CE SU 25185/2021, regra 1).
   - A compensação de férias *"no puede tenerse como factor de salario"* (CSJ SL467-2019).
   - A UGPP só manda cotizar sobre as férias **desfrutadas** (Decreto 806/1998 art. 70) e tira os "pagos por vacaciones" do total remunerado.
2. **Parafiscais (SENA, ICBF, CCF) = dentro.** A premissa do pedido ("fora de … parafiscais") **não procede**. O Consejo de Estado (Sala de Consulta e Sección Cuarta, reiterada) e a UGPP dizem que as férias compensadas, durante o contrato ou no desligamento, integram a "nómina mensual de salarios" da Ley 21 art. 17 como "descansos remunerados". O T = Yes do WTC está certo.

**Fontes e trechos:**
- **CE, Sala de Consulta y Servicio Civil, concepto 2027 de 04/10/2010**, rad. 11001-03-06-000-2010-00090-00, C.P. William Zambrano Cetina.
  - Local: `raw/docs/oficiais/CO/2026-10-22-CE-SalaConsulta-2027-2010-vacaciones-compensadas-FuncionPublica.html`; URL: Gestor Normativo da Función Pública.
  - Resposta: *"Las vacaciones pagadas en dinero a la terminación de la relación laboral hacen parte de la base para la liquidación y pago de los aportes parafiscales al SENA, ICFB y Cajas de Compensación Familiar."*
  - Considerações: *"su referente de cálculo es la nómina mensual de la empresa y no el salario como ocurre en la liquidación de aportes a la Seguridad Social en salud y pensiones"*.
- **CE, Sección Cuarta, sentença de 11/05/2023**, rad. 25000-23-37-000-2020-00048-01 [27226], C.P. Stella Jeannette Carvajal Basto, Soluciones Automáticas Ltda. × UGPP.
  - Local (novo): `raw/docs/oficiais/CO/2026-11-02-CE-S4-27226-2023-vacaciones-compensadas-parafiscales-copiaPwC.pdf`, md5 `4d7dbb21811f626f8e94f8dabaf77176`. É **cópia** do repositório PwC (https://legalytributarioenlinea.co.pwc.com/Repositorio%20PwC/PDF/Jurisprudencia/Consejo%20de%20Estado/Secci%C3%B3n%204/2023/SEN-Exp-027226-23.pdf), com o cabeçalho oficial www.consejodeestado.gov.co.
  - Trecho da sentença (p. 7): *"el valor de las vacaciones pagadas en dinero después de terminada la relación laboral hace parte de los descansos remunerados de ley de que trata el artículo 17 de la Ley 21 de 1982 y, en consecuencia, integran la base para liquidar los aportes al SENA, ICBF y CCF."*
  - A sentença cita os exp. 24466/2020 e 24735/2021.
  - Posição da UGPP no processo (p. 3): *"mientras se aporta a salud y pensión, esto se realiza sobre el último salario base de cotización reportado con anterioridad a la fecha en la que inició el descanso (art. 70 del Decreto 806 de 1998). Tratándose de los aportes al SENA, ICBF y CCF, cuando se disfrutan vacaciones o se compensan en dinero a lo largo de la relación laboral o al finalizar la misma, tal reconocimiento hace parte de los descansos remunerados de ley y, por lo tanto, integran la base gravable"*.
- **UGPP, ABC Empleadores 2025**, p. 7 (local `2026-10-22-UGPP-ABC-Empleadores-2025.pdf`): *"para liquidar la base de cotización del sistema de parafiscales (caja de compensación familiar, SENA e ICBF), debe tener en cuenta el valor reconocido al trabajador por las vacaciones disfrutadas, compensadas en dinero o pagadas en la liquidación del contrato."*
- **UGPP, IBC Empleadores 2021**, local `2026-10-21-UGPP-Empleadores-IBC-2021.pdf`:
  - p. 23: *"Incluir en el IBC el valor pagado de las vacaciones disfrutadas, compensadas en dinero o pagadas por liquidación de contrato, para el cálculo de los aportes parafiscales (Ley 21 de 1982, artículo 17)"*. A fórmula da mesma página separa "IBC SGSS = Total pagos salariales + … 40%" de "IBC PARAF = Total pagos salariales + Total pagado por Vacaciones".
  - p. 18: o total remunerado é *"…excluyendo … los pagos por vacaciones y las indemnizaciones"*.
- **CSJ SL467-2019**, rad. 71281, 06/02/2019.
  - Local `2026-11-02-CSJ-SL467-2019-ficha.pdf`; URL https://www.cortesuprema.gov.co/corte/wp-content/uploads/relatorias/la/bfeb2019/Ficha%20SL467-2019.pdf.
  - pp. 9–10: *"tratándose de la compensación de vacaciones, tal rubro no puede tenerse como factor de salario (…) pues es indiscutible que la misma … es una especie de indemnización"*.
- **CE SU 25185/2021**, regra 1 (local `2026-10-22-CE-S4-SU-25185-2021-ficha.pdf`): *"El IBC de aportes al Sistema de Seguridad Social … únicamente lo componen los factores constitutivos de salario, en los términos del artículo 127 del CST"*.

**Muda artefato?** Não muda valor. Opcional: a nota D156/D324 está desatualizada. Texto sugerido (EN): *"Statutory-benefit base and social-security IBC = No: cash compensation of vacation is not salary (CSJ SL467-2019; CE SU 25185 of 2021, rule 1). Payroll levies = Yes: it is a 'descanso remunerado' under Ley 21 de 1982 art. 17 (CE Sala de Consulta 2027 of 2010; CE Seccion Cuarta exp. 27226 of 11 May 2023; UGPP ABC Empleadores 2025)."*

**O que falta para 100%:**
- baixar a sentença 27226 do site oficial do CE (SAMAI/relatoria); hoje só temos a cópia da PwC;
- achar uma frase expressa da UGPP do tipo "vacaciones compensadas no son base de salud/pensión". A exclusão sai da fórmula do IBC da UGPP e da regra 1 do CE SU, não de um texto que diga isso diretamente.

---

## 14. Auxílio de carro / rodamiento

**Fontes e trechos:**
- **CSJ SL5159-2018**, rad. 68303, 14/11/2018, M.P. Clara Cecilia Dueñas Quevedo.
  - Local: `raw/docs/oficiais/CO/2026-11-02-CSJ-SL5159-2018-rodamiento.pdf` (íntegra, 45 pp.) e `2026-11-02-CSJ-SL5159-2018-ficha.pdf` (Relatoria CSJ, www.cortesuprema.gov.co).
  - p. 30: a CSJ manteve o rodamiento como não salarial porque *"el Tribunal también señaló que esa prestación se reconoció para facilitar la prestación del servicio de la demandante en función de su cargo, es decir, no estaba dirigida a retribuir el trabajo"*. Diz também que *"el artículo 30 de la Ley 1393 de 2010 no tiene relevancia en la definición de lo que es o no es salario"*.
  - p. 34: *"el criterio conclusivo o de cierre de si un pago es o no salario, consiste en determinar si su entrega tiene como causa el trabajo prestado u ofrecido"*.
  - §3.3, pp. 34–36: *"«la ley no autoriza a las partes para que dispongan que aquello que por esencia es salario, deje de serlo»"*, e o pacto do CST 128 recai sobre *"aquellos emolumentos que pese a no compensar directamente el trabajo, podrían llegar a ser considerados salario"*.
- **CST art. 128** (local `2026-10-22-CST-pr004-SecretariaSenado.html`): *"No constituyen salario … lo que recibe en dinero o en especie no para su beneficio, ni para enriquecer su patrimonio, sino para desempeñar a cabalidad sus funciones, como gastos de representación, medios de transporte, elementos de trabajo y otros semejantes."*
- **CE SU 25185/2021** (local `2026-10-22-CE-S4-SU-25185-2021-ficha.pdf`). Regra 1: o IBC só tem fatores salariais. Os pagos "para desempeñar a cabalidad sus funciones, como … medios de transporte" *"no son ingreso base de cotización de aportes porque, en esencia, no son salario"*. Regras 2 e 3: o pacto de "desalarización" fica sujeito ao limite dos 40%.
- **Posição da UGPP:**
  - ABC Empleadores 2025, p. 5: classifica como não salarial o pago *"otorgado para que el trabajador pueda desarrollar sus funciones y, en ningún caso retribuyen su servicio"* e o põe no teste dos 40%. A SU 25185 (regra 3, já citada no cabeçalho V1 do WTC) tira esses pagos do numerador, e o WTC segue a SU, que tem hierarquia maior.
  - Acuerdo UGPP 1035/2015, anexo (local `2026-10-30-UGPP-Acuerdo-1035-2015-AnexoTecnico-copia-cijuf.pdf`, cópia): transcreve o CST 128 e a Ley 344 art. 17 (*"los acuerdos … sobre los pagos que no constituyen salario y los pagos por auxilio de transporte no hacen parte de la base para liquidar los aportes"*).

**Decisão (quando é salarial):**

| Situação | Natureza | V no WTC | Bases |
|---|---|---|---|
| Valor pago para o trabalhador usar o carro **no serviço** (rodamiento, combustível e manutenção ligados à função; valor razoável e com destinação) | Não salarial por natureza (CST 128, "medios de transporte"; SL5159-2018) | Non-Salary - non-remunerative | Fora do IBC, dos parafiscais e das prestações; fora do teste dos 40% (SU 25185) |
| Valor de livre uso, sem relação com o serviço, que retribui o trabalho | Salário (CST 127); o pacto é ineficaz (SL5159-2018 §3.3) | Salary | Todas as bases = Yes |
| Benefício que não retribui (bem-estar) e foi pactado por escrito como não salarial | Não salarial por pacto (CST 128, 2.ª parte) | Non-Salary - pacted | Q/R/S/U só no excedente dos 40%; T e W = No (Ley 344 art. 17) |

**WTC v1.8 (201–206, 214–216):**
- V = "Non-Salary - pacted"; Q/R/S/U = "Yes/No"; T = No; W = No; Y condicional (AuxilioNS/AuxilioS).
- AB201: *"Default 'Non-Salary - pacted': a cash car / fuel / maintenance allowance paid under the contract is salary (CST art. 127) unless a written CST art. 128 pact excludes it … Where the amount is paid only so that the employee can travel for the job … configure it as 'Non-Salary - non-remunerative' …"*
- O desenho atende os três casos, e as linhas 207–213 já são o caso "non-remunerative" para transporte.

**Muda artefato?** Não muda valor. Opcional: a 1.ª frase de AB201–206/AB214–216 sugere que o pacto tira o caráter salarial de qualquer valor, e a CSJ diz o contrário. Texto sugerido (EN): *"Default 'Non-Salary - pacted'. The test is the purpose of the payment (CSJ SL5159-2018): paid so the employee can use the car for the job (means of transport, CST art. 128) → 'Non-Salary - non-remunerative', outside the contribution base and the 40% test (CE SU 25185 of 2021); a non-remunerative benefit excluded by a written CST art. 128 pact → 'pacted', inside the 40% test; a payment that remunerates the service is salary (CST art. 127) whatever the pact says."*

**Fora do pedido (registro):** as linhas "pacted" têm W = No e T = No fixos. Isso está certo quando o pacto vale. Quando o pacto não vale (pagamento salarial), W e T deveriam virar Yes, e o WTC não mostra quem faz essa troca (só Y e o teste dos 40% dependem da flag do DD). Vale conferir na regra do engine/DD.

**O que falta para 100%:**
- a natureza depende do fato (finalidade e razoabilidade do valor), então o WTC só pode dar o padrão e a regra;
- não achei conceito da UGPP específico sobre "rodamiento". A SU 2022CE-SUJ-4-001 (exp. 24724, cooperativas) que a cita não abriu no site da UGPP (HTTP 404) e trata de outro regime.

---

## Bloco de prova
- **Pedido → resposta:**
  - 10: recontagem por script, com conferência independente; 519 = 486 R + 31 N + 2.
  - 11: definições pp. 32–39 lidas; as 25 linhas pedidas foram conferidas no v1.8 e estão certas; varredura extra em §11.4.
  - 12: NIE064–068 e as tabelas lidas; lista conferida contra H7–H9 e o Mapper.
  - 13: CSJ SL467-2019, CE 2027/2010, CE 27226/2023 e UGPP lidos; parafiscais = dentro.
  - 14: CSJ SL5159-2018, CST 128, CE SU 25185 e UGPP lidos; WTC conferido.
- **Fontes:** todas abertas por mim nesta rodada, com página, regra ou artigo indicado acima. Fonte nova gravada: `2026-11-02-CE-S4-27226-2023-vacaciones-compensadas-parafiscales-copiaPwC.pdf`, que é cópia e não original do CE.
- **Teste:**
  - dois scripts de contagem convergentes (517 R/N na coluna Y; 517 IDs + 90/92);
  - imagem da p. 226;
  - md5 do anexo;
  - leitura com openpyxl (`read_only`) do WTC v1.8 (V, Y, Q–W e AB das linhas citadas, mais a varredura V × Y em todas as linhas) e do DD v1.5 (H7–H9, Mapper C92–C107);
  - XSD 1.0.6 l. 267–275;
  - SIR v1.3 com "519" nas l. 21, 35, 220 e 355.
- **Confiança:** 10 = 97%, 11 = 95% (90% em 114–116), 12 = 93%, 13 = 94%, 14 = 92%. Todos ≥ 92%.
