# Lote B, rodada 6: seguridade social, incapacidade, Res. 2708 e SMMLV (02/11/2026)

> Frente Validação CO · ligado a [[PLANO-92]], [[TABELA-RODADA5]], [[LOTE-B-SEGURIDADE]], [[CONFERENCIA]] e [[Colombia]].
> **Nenhum artefato foi alterado.** Finais conferidos (leitura por script): `final/CO-CCG-001-v1.6.docx`, `final/CO-WTC-001-v1.8.xlsx`, `final/specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx`.
> A research CO **não** está em produção, então não há ticket ao Development. Fontes web acessadas em 02/11/2026. Cópias locais em `raw/docs/oficiais/CO/`.

## Resumo

| # | Ponto | Decisão | Muda artefato? | Conf. (antes → agora) |
|---|---|---|---|---|
| 5 | P-06: tarifa da ARL no PILA | Decimal com ponto: "0.0052200" (9 posições). Não há decimal implícito. | **Não.** A R5 já aplicou a mudança: PILA-003 J131/K131/P131 e `Population Rules`!C17 estão em decimal. | 80% → **92%** |
| 6 | D5: parafiscais sobre incapacidade | **No** para SENA, ICBF e CCF. Incapacidade (T123, T326:T329): fechado. Licenças (T330:T333): mantidas em No, com risco. | **Não.** | 85% → **92%** incapacidade; **86%** licenças |
| 7 | Incapacidade comum, dias 1–2 | Empregador paga **66,67% (2/3) do salário**, com **piso de 1 SMMLV** (proporcional aos dias). | **Não** nos valores. Opcional: somar a 2ª fonte do MinSalud (2024) e a T-291/2020 a CCG P904/P905, WTC `Employer Sick Pay`!A57 e `Global WTC Coverage`!C16. | sem fonte → **93%** |
| 8 | Res. MinTrabajo 2708/2026 | Arts. 1 (1.1), 3, 5.4, 8, 9 e 10 confirmados pelo próprio MinTrabajo, em resposta oficial à Câmara. A resolução **revoga** (não substitui) a Circular Externa 0101/2025. | **Não.** O CCG v1.6 já trata a 101 como revogada e tirou as "objective causes". | 90% → **93%** |
| 9 | SMMLV 2026: qual instrumento | Citar o **Decreto 1469 de 2025, art. 1** (COP 1.750.905). O Decreto 0159/2026 ficou **sem efeitos** pelo auto do CE de 9/7/2026, ordinal 3º. A nulidade de fundo segue pendente. | **Não** no valor nem no instrumento (CCG P297, T34R1C2 e WTC C12 já citam o 1469). Ajuste fino em P297: ver §9. **O hub `paises/Colombia.md` está defasado** (cita o 0159 nas l. 48, 78 e 121). | B × B → **94%** |

---

## 5. P-06: formato da tarifa da ARL (T2R2-061) no PILA

**Decisão.** O campo 61 do registro tipo 2 tem 9 posições, é numérico e vai em **decimal com ponto**, alinhado à esquerda e completado com zeros à direita:
- classe I, 0,522% → `0.0052200`;
- classe V, 6,960% → `0.0696000`.

É o mesmo padrão das tarifas de 7 posições (pensão 46, saúde 54, CCF 64, SENA 66, ICBF 68, ESAP 70, MEN 72): `0.16000`, `0.04000`. Não há base para "000005220" com decimal implícito.

**Por que fecha em 92% (4 provas independentes no mesmo anexo e no anexo irmão)**
1. **A saída para as ARL copia o campo 61 "en decimales".** AT2 v30, saída para as ARL, campo 28, 7 posições (p.210; local `.txt` l.12373): "28 7 167 173 N Tarifa. En decimales. El registrado en el campo 61 del registro tipo 2 del archivo tipo 2."
   - Um "000005220" de decimal implícito, cortado para 7 posições, não seria "en decimales".
   - "0.0052200" vira "0.00522" sem perder nada, porque só caem zeros à direita.
2. **A cotização é o IBC multiplicado pelo campo 61, sem fator de escala.** AT2 v30 §2.1.2.3.27, campo 63 (p.160): "Se debe validar el cálculo de esta cotización, multiplicando el valor del campo 44 – 'IBC Riesgos Laborales' … por el valor del campo 61 – 'Tarifa de aportes a Riesgos Laborales'". O mesmo texto aparece no cap. de cálculo (p.280, l.17337). O anexo não declara decimal implícito em campo nenhum: a busca por "implícit" e "punto decimal" no AT2 e no AT3 não achou nada.
3. **O anexo irmão traz exemplo explícito.** AT3 v15 §2.2.2.25, campo 51, p.63 (l.3415), mesmo ministério, mesma Res. 2388/2016, campo N de 7 posições: "El valor del campo debe ser en decimal, justificado a la izquierda y completando la longitud del campo con ceros a la derecha, por ejemplo 2.0% sería 0.02000."
4. **As tarifas da ARL têm 3 casas no percentual.** AT2 v30, tabela de cotizações, p.120 (l.6893): "I 0,348% 0,443% 0,522% …". Como fração, isso dá 5 casas (0.00522), que cabem nas 7 posições da saída. O formato decimal é o único em que a cópia 61 → 28 fecha.

**Leiaute de entrada** (AT2 v30 p.93–95; l.5288, 5382, 5437, 5463–5482):
- "46 7 238 244 N Tarifa de aportes pensiones"
- "54 7 308 314 N" (saúde)
- "61 9 381 389 N Tarifa de aportes a Riesgos Laborales. La suministra el aportante y la valida el operador de información de acuerdo con las tarifas vigentes en el periodo a liquidar."
- "64 7 408 414 N" (CCF), "66 7 424 430 N" (SENA), "68 7 440 446 N" (ICBF)

**Regra geral × exemplo.** A regra geral do AT2, "Los campos tipo numérico 'N', se reportarán justificados a la derecha y rellenados con ceros a la izquierda" (p.9, l.395), cede ao exemplo específico do AT3, que é norma especial para tarifa. O AT3 também tem essa regra geral e mesmo assim manda alinhar à esquerda.

**A Res. MSPS 1529/2026** (local `2026-10-29-Res-MSPS-1529-2026-PILA.txt`) modifica os AT2 e AT3, mas não toca nos campos 46/54/61/64–72 nem no campo 28 da saída. A busca por "381", "389", "Tarifa. En" e "justificad" não achou nada.

**Muda artefato?** Não. O final atual já está certo:
- PILA-003 `PILA Spec`!J131 = "N(9) - rate as a decimal with a point … (e.g. 0.0052200)", K131 = `0.0052200`, P131 com a justificativa;
- `Population Rules`!C17 já diz que T2R2-061 "follows the same rule".

**Fontes**
- AT2 v30 (24/07/2026): `raw/docs/oficiais/CO/2026-10-29-MinSalud-AT2-v30-2026-07-24-PILA-activos.pdf` (+ `.txt`). https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/OT/anexo-tecnico2-cotizantes.pdf
- AT3 v15: `raw/docs/oficiais/CO/2026-10-29-MinSalud-AT3-v15-2026-07-24-PILA-pensionados.pdf` (+ `.txt`). https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/OT/anexo-tecnico3-pensionados.pdf
- Res. MSPS 1529/2026: `raw/docs/oficiais/CO/2026-10-29-Res-MSPS-1529-2026-PILA.pdf`.

**Confiança: 92%.**

**Para 100%:** um exemplo impresso do campo 61 de entrada num documento oficial (o AT2 não tem), ou o validador ou arquivo de teste de um operador (SOI, Aportes en Línea, Mi Planilla) aceitando `0.0052200`. Na web só achei material de fornecedores (pista, sem valor de fonte). Confirmar com o operador na implantação, como a spec já diz.

---

## 6. D5: parafiscais (SENA, ICBF, CCF) sobre incapacidade e licenças

**Decisão.** Mantido **No** em toda a coluna T do WTC.

**Incapacidade (T123, T326, T327, T328, T329): 92%.**
1. **A base da lei** é "salario" + "descansos remunerados". Ley 21/1982 art. 17 (local `2026-10-21-Ley-21-1982-FuncionPublica.html`): "se entiende por nómina mensual de salarios la totalidad de los pagos hechos por concepto de los diferentes elementos integrantes del salario en los términos de la Ley Laboral, cualquiera que sea su denominación y además, los verificados por descansos remunerados de ley y convencionales o contractuales."
2. **O auxílio de incapacidade não é salário** (CST arts. 227 e 128; Ley 776 art. 3). O CE disse isso de forma expressa:
   - CE S4, 19/08/2021, rad. 25000-23-37-000-2015-00353-01 (23856), p.17 (local `2026-10-22-CE-Seccion4-23856-2021-copia-actualicese.pdf`): "Comoquiera que el auxilio que recibe el trabajador incapacitado, en los términos de la ley laboral, no constituye salario, es claro que tampoco integra la nómina mensual de salarios y, en consecuencia, se excluye de la base para calcular los aportes con destino al SENA, ICBF y CCF."
   - Na mesma sentença, p.11, o problema jurídico (iii): "si durante el periodo de incapacidad … no se debían pagar aportes al sistema parafiscal (SENA, ICBF y CCF)".
   - Na SU 25185/2021 (ficha local), a UGPP liquidou "sin que se hubieran tenido en cuenta las incapacidades".
3. **A Ley 789/2002 art. 3** separa "descanso o permiso remunerado de ley" de "períodos de incapacidad por motivo de enfermedad no profesional, maternidad…" (local `2026-10-21-Ley-789-2002-SecretariaSenado.html`). O dispositivo trata do direito ao subsídio, não da base, mas mostra que a lei não põe a incapacidade dentro de "descanso remunerado".
4. **O Decreto 780 art. 3.2.1.10** manda pagar, na incapacidade e na licença de maternidade, só "los aportes a los Sistemas de Salud y de Pensiones" (local `2026-10-22-Decreto-780-2016-funcionpublica.htm`). Não fala de SENA, ICBF nem CCF.
5. **O AT2 v30 não decide a questão.**
   - Campo 25 (IGE) só afasta a ARL (p.165–166): "El aportante no realizará aportes al Sistema General de Riesgos Laborales".
   - Sobre o IBC nas novidades (p.103): "Es responsabilidad del aportante hacer el cálculo del ingreso base de cotización que afecta las novedades".
   - Campo 45 (IBC CCF) diz só "Lo suministra el aportante" (p.92).
6. **CE S2, Subseção A, 18/08/2022, rad. 11001-03-25-000-2015-00232-00 (0434-15)** (nova; local `2026-11-02-CE-S2-0434-15-2022-08-18-Decreto806-art70-Colpensiones.htm`). Confirma que a base parafiscal (nómina, Ley 21 art. 17) é distinta da base da seguridade social, que cobre "los beneficios económicos que se conceden por concepto de licencia de maternidad e incapacidades". Trecho: "los aportes a la seguridad social no tienen que coincidir necesariamente con los denominados parafiscales que paga exclusivamente el empleador … su referente de cálculo es la nómina mensual de la empresa y no el salario".

**A posição da UGPP pedida (Res. 1702/2021 mod. Res. 205/2024) não trata do tema.** O anexo técnico da Res. 205/2024 tem o título "ESTÁNDARES DE PROCESOS DE COBRO DE CARTERA MOROSA" (local `2026-10-21-UGPP-Res-205-2024-modifica-Res-1702-2021.pdf`, p.7). A busca por "incapacidad", "maternidad", "IBC" e "ingreso base" não achou regra de base. A única fonte da UGPP contra é o ABC Empleadores 2025, p.7, já afastado na R5: é guia sem força normativa e contradiz a própria p.6 e o ABECE Pago Correcto V1.

**Licenças maternidade, paternidade, parental e cuidado da infância (T330 a T333): 86%.**
- **A favor:** o CE 23856 (p.14) qualifica a licença como "prestación económica del sistema de salud en seguridad social". A Ley 789 art. 3 a separa de "descanso remunerado". O Decreto 780 art. 3.2.1.10 só manda pagar saúde e pensão.
- **Contra:** o CST art. 236 chama a licença de "descanso remunerado", e o texto da Ley 21 art. 17 inclui "descansos remunerados de ley". Não achei sentença da Seção Quarta que decida expressamente parafiscais sobre licença de maternidade:
  - a CE 19736/2016, citada pela imprensa, não foi localizada em fonte oficial;
  - o documento do CE `csamal.consejodeestado.gov.co/.../IBCMat.pdf` não abriu: o certificado TLS do site não confere, e baixar sem verificação foi bloqueado pela política da sessão;
  - o normograma da Supersalud (CE 27671/2023) estava fora do ar.

**Muda artefato?** Não. WTC v1.8 coluna T (T123, T326:T333) = No. Opcional: na nota D123/D330, citar a CE 0434-15/2022 e registrar que a Res. UGPP 1702/2021 (mod. 205/2024) trata de cobrança, não de base.

**Fontes:** as listadas acima, mais https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=4827 (Ley 21), https://normativa.colpensiones.gov.co/colpens/compilacion/docs/11001-03-25-000-2015-00232-00(0434-15)_20220818.htm (md5 5b5231748f18ed0a71b2b54e32643f67) e https://www.ugpp.gov.co/wp-content/uploads/2025/02/ABC_empleadores2025.pdf.

**Confiança:** incapacidade **92%**; licenças **86%**; D5 no conjunto **~90%**.

**Para 100% nas licenças:** ler uma sentença da Seção Quarta do CE que exclua expressamente a licença de maternidade da base SENA/ICBF/CCF (rad. 19736/2016 ou outra), em cópia oficial (SAMAI, ou normograma oficial quando voltar ao ar). Alternativa: um conceito da UGPP posterior a 2021 sobre licença. Até lá, manter "No" com nota de risco, configurável.

---

## 7. Incapacidade de origem comum, dias 1–2: taxa e piso

**Decisão**
- **Taxa:** o empregador paga **2/3 do salário (66,67%)** nos dias 1 e 2.
- **Piso:** o valor **não pode ser inferior ao SMMLV**. Na prática, o valor diário fica ≥ SMMLV/30 = COP 58.363,50 em 2026.
- **Fórmula:** `max(S/30 × 2/3, SMMLV/30) × d`.
- **Salário variável:** média do último ano (CST art. 228).
- O pagamento de 100% é liberalidade ou convenção, não lei.

**Cadeia de fontes**
1. **Quem paga.** Decreto 780/2016 art. 3.2.1.10 par. 1 (Decreto 2943/2013 art. 1): "En el Sistema General de Seguridad Social en Salud serán a cargo de los respectivos empleadores las prestaciones económicas correspondientes a los dos (2) primeros días de incapacidad originada por enfermedad general y de las Entidades Promotoras de Salud a partir del tercer (3) día y de conformidad con la normatividad vigente." O decreto não dá taxa: "las prestaciones económicas" remete à prestação legal.
2. **A taxa legal.** CST art. 227 (local `2026-10-22-CST-pr007-SecretariaSenado.html`): "el trabajador tiene derecho a que el empleador le pague un auxilio monetario hasta por ciento ochenta (180) días, así: las dos terceras (2/3) partes del salario durante los primeros noventa (90) días y la mitad del salario por el tiempo restante."
3. **O piso.** Corte Constitucional C-543/2007, parte resolutiva (local `2026-10-22-CorteConstitucional-C-543-2007.htm`): "Declarar EXEQUIBLE el artículo 227 del Código Sustantivo del Trabajo … en el entendido que el auxilio monetario por enfermedad no profesional no podrá ser inferior al salario mínimo legal vigente." A sentença tem efeito *erga omnes* e condiciona o próprio art. 227, que é a norma da taxa dos dias 1–2.
4. **A Corte reitera 66,67% e o piso.** T-291/2020 (nova; local `2026-11-02-CorteConstitucional-T-291-2020.htm`, md5 a149a6ccf18276ca8550063e9077b57b): "el trabajador que tenga una incapacidad comprobada, ocasionada por enfermedad no profesional, tiene derecho a que el empleador le pague un auxilio monetario del 66,67% del salario base de cotización en los primeros 90 días … En cuanto a los porcentajes en comento … deben soportar una alteración cuando el ingreso base de cotización del afiliado no supera el salario mínimo."
5. **O MinSalud aplica o art. 227 aos dias 1–2, em dois conceitos:**
   - **Concepto 202311602174531 (2023)** (já citado nos finais; local `2026-10-30-MinSalud-Concepto-202311602174531-2023-normograma-Supersalud.htm`): "los dos (2) primeros días de incapacidad serán asumidos por el empleador teniendo en cuenta el 66.6% del salario."
   - **Concepto Jurídico 2024116001238451 (2024)** (novo; local `2026-11-02-MinSalud-Concepto-2024116001238451-2024-incapacidad.pdf`, md5 b49e37e3e9a71112a8330f4436371cf4), p.4: "se concluye, que los dos primeros días de incapacidad le corresponden al empleador y, de otra parte, el artículo 227 del Código Sustantivo del Trabajo, prevé que respecto al auxilio de incapacidad corresponde un pago de las dos terceras (2/3) partes, es decir, un porcentaje equivalente al 66.6% del salario". E p.5: "se aclara que el cálculo para la liquidación del auxilio por incapacidad no pueda dar como resultado un monto inferior al salario mínimo legal vigente".
6. **A T-891/2013 (local) não trata do tema.** É sobre embargo de salário e mínimo vital. Descartada como fonte.

**Arredondamento da taxa.** 2/3 = 66,666…%. "66,67%" é o arredondamento usado pela Corte (T-291/2020). A fórmula exata "× 2/3", que é a que o WTC usa, é a mais fiel à lei.

**Muda artefato?** Não nos valores. CCG v1.6 P904/P905, T136R4C1, T139R1C1 e T142; WTC v1.8 `Employer Sick Pay`!A7, A20, A30–A41 e F326 já dizem 66,67%/2/3 com o piso C-543. Melhorias opcionais de fonte:
- **CCG P904** e **WTC `Employer Sick Pay`!A34–A35/A57** e **`Global WTC Coverage`!C16(1):** somar o Concepto MinSalud 2024116001238451/2024 e a T-291/2020;
- **CCG P905** e **`Employer Sick Pay`!A38–A39:** trocar "market practice and settled administrative doctrine top the payment up" por "Constitutional Court C-543 of 2007 (resolutive part, erga omnes) conditions Labour Code art. 227 so that the benefit may not fall below the minimum wage; applied by Concepto MinSalud 2024116001238451 of 2024". O piso vem da Corte, não da prática.
- Os itens "OPEN ITEM 1/2" da Q-6/Q-7 (C25, no hub) podem ser fechados.

**Fontes:** locais acima. URLs:
- https://www.corteconstitucional.gov.co/relatoria/2007/C-543-07.htm
- https://www.corteconstitucional.gov.co/relatoria/2020/T-291-20.htm
- https://minsalud.gov.co/Normatividad_Nuevo/Concepto%20Jur%C3%ADdico%20%202024116001238451%20de%202024.pdf
- https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=77813

**Confiança: 93%.**

**Para 100%:** nenhuma norma de hierarquia legal diz com todas as letras que o empregador paga 2/3 nos dias 1–2. A conclusão vem da leitura conjunta "prestaciones económicas" (Decreto 780) + CST 227 + C-543. Fecharia com:
- uma sentença da CSJ Sala Laboral que decida a taxa dos dias 1–2; ou
- um conceito do MinTrabajo, que é a autoridade laboral (os dois conceitos achados são do MinSalud).

Convenção coletiva ou contrato pode prever 100%: manter configurável.

---

## 8. Res. MinTrabajo 2708 de 20/08/2026

**Decisão.** O texto lido na cópia (cerlatam, imagem com assinatura e carimbo "20 AGO 2026") está confirmado por **fonte oficial do próprio MinTrabajo**: a resposta da Ministra à Comissão Sétima da Câmara, de 14/09/2026, publicada no site da Câmara. Ponto por ponto:
- **Art. 1:** revoga e deixa sem efeito 11 circulares, entre elas a **Circular Externa 0101 de 22/09/2025** (num. 1.1), com efeito para o futuro a partir da publicação.
- **Art. 3:** atuações em curso não se arquivam nem se anulam automaticamente.
- **Art. 5.4:** nenhuma fórmula ou metodologia da 101 serve de fundamento autônomo. A resolução manda revisar as normas de redução de jornada e de remuneração a destajo.
- **Art. 8:** não há reviviscência.
- **Art. 9:** publicação no Diario Oficial.
- **Art. 10:** vigência a partir da publicação.
- **Revoga ou substitui?** **Revoga**, sem substituir. A 101 não é trocada por outra circular. O art. 5.4 só manda estudar "si subsiste la necesidad de un instrumento" e, até lá, valem a lei e o regulamento.

**Trechos (resposta oficial, local `2026-11-02-MinTrabajo-Respuesta-Camara-Prop04-2026-09-14-Res2708.pdf`, md5 6675bf0e3f13b089989b0a136a152cef)**
- p.1: "Deroga once circulares del ordenamiento institucional del Ministerio hacia el futuro (artículo 1); dispone que esas circulares no podrán invocarse como fundamento jurídico autónomo … (artículo 2); … y no reviviscencia de instrumentos anteriores (artículo 8)."
- p.3: "La derogatoria opera hacia el futuro, a partir de la publicación (artículo 1, inciso final, y artículo 10). … la derogatoria de las once circulares no revive automáticamente instrumentos anteriores que hubieran sido sustituidos por ellas (artículo 8, principio de no reviviscencia)." E: "La Resolución 2708 de 2026 se publicará en el Diario Oficial … (artículo 9 de la resolución)."
- Bloco "10. Circular Externa 0101 del 22 de septiembre de 2025" (l.2642 do texto extraído) e a resposta à pergunta 6: "Mientras se adopta el instrumento que resulte procedente conforme a la revisión del numeral 5.4 del artículo 5, ninguna fórmula, metodología o criterio de liquidación contenido en la Circular 0101 podrá utilizarse como fundamento jurídico autónomo para exigir una obligación económica, determinar una liquidación o sustentar una consecuencia sancionatoria."
- Os inspetores verificam "con fundamento directo en la Ley 2466 de 2025, la Ley 2101 de 2021 y el Código Sustantivo del Trabajo".

**Diario Oficial.** Consultei a Imprenta Nacional (busca: tipo Resolución, número 2708, publicação de 20/08 a 02/11/2026). Voltou **um** resultado: **Diario Oficial nº 53.646, de 02/10/2026**. Não confirmei que é a resolução do MinTrabajo: o PDF do Diário exige login, e o filtro de entidade não restringiu a busca. Fica como **indício**, não como fato.
- Se for ela, a revogação vale a partir de 02/10/2026.
- Não muda o CCG, que diz só "revoked by Resolution 2708 of 2026", sem data.
- Os sites do MinTrabajo e do SISJUR (Alcaldía de Bogotá) recusaram conexão desta máquina.

**Muda artefato?** Não. CCG v1.6 P114, P355 e P424 tratam a 101 como revogada. A busca por "objective, demonstrable" no CCG v1.6 não achou nada: a frase já saiu. As bases citadas são legais.

**Fontes**
- Resposta oficial: https://www.camara.gov.co/wp-content/uploads/2026/09/control_politico/respuestas/8048/Respuesta-Mintrabajo-Prop.-No.-04-sep.-15-26.pdf
- Cópia do texto: `raw/docs/oficiais/CO/2026-10-30-Res-MinTrabajo-2708-2026-copia-cerlatam.pdf` (https://www.cerlatam.com/normatividad/mintrabajo-resolucion-2708-de-2026-20-ago-26/)
- Diario Oficial: https://svrpubindc.imprenta.gov.co/diario/

**Confiança: 93%.**

**Para 100%:** o texto no Diario Oficial (confirmar se o DO 53.646 de 02/10/2026 é este ato e ler os arts. 1, 5.4, 8 e 10 ali) ou o PDF no normograma do MinTrabajo. Precisa de acesso pelo navegador (Claude in Chrome) ou de login na Imprenta.

---

## 9. SMMLV 2026: instrumento vigente

**Decisão.** Citar o **Decreto 1469 de 29/12/2025, art. 1** (Diario Oficial 53.350 de 29/12/2025): COP 1.750.905 a partir de 1/1/2026. Nota de histórico:
- o decreto ficou **suspenso** de 12/02/2026 a 09/07/2026;
- nesse período valeu o **Decreto 0159 de 19/02/2026**, com o mesmo valor (fixação transitória);
- o **auto de 9/7/2026** revogou a suspensão, **negou** a medida cautelar e **deixou sem efeitos** o Decreto 0159;
- a ação de nulidade (rad. 11001-03-25-000-2026-00004-00) segue sem sentença;
- o valor **nunca** mudou.

**Trechos**
- **Decreto 1469/2025** (local `2026-10-30-Decreto-1469-2025-Colpensiones.htm`):
  - art. 1: "Fijar a partir del primero (1o) de enero de 2026 como Salario Mínimo Legal Mensual, la suma de UN MILLÓN SETECIENTOS CINCUENTA MIL NOVECIENTOS CINCO PESOS ($1.750.905)";
  - cabeçalho: "Diario Oficial No. 53.350 de 29 de diciembre de 2025 <Rige a partir del 1o. de enero de 2026>".
- **Auto do CE, Seção Segunda (Sala), 9/7/2026, C.P. Jorge Iván Duque Gutiérrez**, rad. 11001-03-25-000-2026-00004-00 (0004-2026). Tema: "Resuelve recurso de súplica contra el auto que decretó la medida cautelar de suspensión provisional. REVOCA". Local `2026-10-30-CE-SeccionSegunda-auto-2026-07-09-Decreto-1469-copia-valoraanalitik.txt` (cópia integral do documento assinado em SAMAI). Parte resolutiva:
  > "Primero. REVOCAR el auto del doce (12) de febrero de dos mil veintiséis (2026), mediante el cual se decretó la suspensión provisional de los efectos del Decreto 1469 del 29 de diciembre de 2025 … Segundo. NEGAR la medida cautelar de suspensión provisional formulada por la parte demandante respecto del Decreto 1469 de 2025 que fijó en 23% el porcentaje de incremento del salario mínimo para 2026 … Tercero. DEJAR SIN EFECTOS la medida cautelar innominada decretada en el ordinal tercero de dicha providencia, y en consecuencia el acto que se dictó en cumplimiento de esta."

  O §84 identifica o ato: "el Gobierno Nacional expidió el Decreto 159 de 2026 … fijar provisionalmente el incremento … en 23% y en un valor de $1.750.905, cifras que coinciden con las reglamentadas en el Decreto 1469 de 2025." A súplica é o recurso final contra o auto cautelar. Votação: 3 × 2 (dois salvamentos de voto).
- **Situação atual:** a cópia do auto (ambitojuridico.com, `.../2026-07/Auto-11001032500020260000400(00042026)-26.pdf`) e a imprensa de 17/07/2026 confirmam a revogação. A nota de 2/10/2026 no hub (publimetro: processos acumulados, fase de provas encerrada) segue sem sentença. A busca de hoje (02/11) não achou sentença de fundo.

**Muda artefato?**
- **Valor e instrumento: não.** CCG v1.6 T34R1C2 = "Decree 1469 of 29 December 2025 art. 1"; P297–P298 trazem o histórico; WTC v1.8 `Global WTC Coverage`!C12 e `Wage Type Catalogue`!F302 citam o 1469.
- **Ajuste fino opcional na CCG P297:**
  - (a) trocar "with Decree 0159 of 2026 spent" por "with Decree 0159 of 2026 left without effect by ordinal 3 of the same order";
  - (b) o auto de 9/7 é da **Sala da Seção Segunda** (5 conselheiros), não da Subseção A. A P297 atribui à "Section Two, Subsection A" a suspensão de 12/02. Essa decisão foi do despacho do conselheiro ponente (auto de 9/7, antecedente 2: "el despacho del consejero ponente accedió a la medida cautelar"). Sugiro "by order of the reporting councillor of Section Two".
- **Fora dos artefatos:** o hub `paises/Colombia.md` ainda diz "Decreto 0159 … (transitório)" nas l. 48, 78 e 121, e a pendência F6-…-C21 (l. 207) está aberta. Pelo que foi lido, a pendência pode ser fechada a favor do 1469. Não editei o hub, porque o pedido era só o relatório.

**Fontes**
- Decreto 1469: https://normativa.colpensiones.gov.co/colpens/docs/decreto_1469_2025.htm
- Auto: https://www.ambitojuridico.com/sites/default/files/2026-07/Auto-11001032500020260000400(00042026)-26.pdf (local: cópia valoraanalitik, mesmo documento assinado)

**Confiança: 94%.**

**Para 100%:**
- ler o auto na própria SAMAI (consejodeestado.gov.co), pois as cópias são da imprensa, embora integrais e com assinaturas eletrônicas;
- conferir o andamento do processo na SAMAI (sentença ou nova cautelar depois de 2/10/2026);
- se houver sentença de nulidade antes de 31/12/2026, rever a nota (o valor pago fica protegido como situação consolidada).

---

## Fontes novas baixadas nesta rodada (`raw/docs/oficiais/CO/`)
| Arquivo | Origem | md5 |
|---|---|---|
| `2026-11-02-MinSalud-Concepto-2024116001238451-2024-incapacidad.pdf` | minsalud.gov.co | b49e37e3e9a71112a8330f4436371cf4 |
| `2026-11-02-CorteConstitucional-T-291-2020.htm` | corteconstitucional.gov.co | a149a6ccf18276ca8550063e9077b57b |
| `2026-11-02-MinTrabajo-Respuesta-Camara-Prop04-2026-09-14-Res2708.pdf` | camara.gov.co | 6675bf0e3f13b089989b0a136a152cef |
| `2026-11-02-CE-S2-0434-15-2022-08-18-Decreto806-art70-Colpensiones.htm` | normativa.colpensiones.gov.co | 5b5231748f18ed0a71b2b54e32643f67 |

Não foi possível baixar (registrado):
- **Supersalud normograma (CE 27671/2023):** host fora do ar.
- **SISJUR Alcaldía de Bogotá e mintrabajo.gov.co:** conexão recusada.
- **csamal.consejodeestado.gov.co (IBCMat.pdf):** o certificado TLS não confere. O download sem verificação foi bloqueado pela política da sessão e não foi contornado.
- **PDF do Diario Oficial 53.646:** exige login.

## Bloco de prova
**Pedido → resposta**
- P-06: AT2 v30 campo 61 (posições 381–389, tamanho 9, N) + saída ARL campo 28 ("En decimales") + campo 63 (multiplicação direta) + comparação com 46/54/64–72 + Res. 1529 sem alteração → §5.
- D5: Ley 21 art. 17, Ley 789 art. 3, Decreto 780 art. 3.2.1.10, AT2 (IGE/IBC CCF), UGPP Res. 1702/2021 mod. 205/2024 (não trata do tema) → §6.
- Dias 1–2: Decreto 780 art. 3.2.1.10 (Decreto 2943), CST 227, C-543, T-891 (descartada), T-291/2020 e dois conceitos do MinSalud; taxa e piso decididos → §7.
- Res. 2708: fonte oficial do MinTrabajo confirma os arts. 1, 5.4, 8 e 10 (e o 3 e o 9); revoga, não substitui; DO em indício → §8.
- SMMLV: 1469 × 0159, auto de 9/7 lido na parte resolutiva, situação atual, instrumento decidido → §9.

**Teste (mecânico)**
- Busca por "decimal", "implícit" e "Tarifa" no AT2 v30/AT3 v15/Res. 1529 (texto extraído).
- Leitura por script das células finais: PILA-003 J/K/P131, linhas 114/123/137, `Population Rules`!C17; WTC v1.8 `Employer Sick Pay`!A1–A59, `Global WTC Coverage`!C12/C16, F302/F326; CCG v1.6 P297/P298/P902–P905, T34R1C2, T136–T142 e as menções à Circular 101/Res. 2708.
- md5 de cada fonte nova.
- Conta do piso: 1.750.905 ÷ 30 = 58.363,50 por dia.

**Confiança por ponto:** P-06 92% · D5 incapacidade 92%, licenças 86% · dias 1–2 93% · Res. 2708 93% · SMMLV 94%. **Abaixo de 92%: só as licenças em D5.** O que falta está no §6.
