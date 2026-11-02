# Lote B — seguridade social / PILA (pesquisa de 02/11/2026)

> Frente Validação CO · alimenta [[CONFERENCIA]] e [[TABELA-CONSOLIDADA]] · base: [[PENDENTES-CCG-WTC]] (§9 D5, §12 A-14) e [[PENDENTES-SPECS-DD]] (P-06, DD-21) · hub [[Colombia]].
> **Nenhum artefato foi alterado.** Finais conferidos: `final/CO-CCG-001-v1.5.docx`, `final/CO-WTC-001-v1.7.xlsx`, `final/CO-DD-001-v1.4.xlsx`, `final/specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx`.
> Data de acesso das fontes web: **2026-11-02**. Cópias locais em `raw/docs/oficiais/CO/` (nome na coluna Fonte).

## Resumo

| ID | Como está nos finais (célula) | Decisão | Muda artefato? Onde | Fonte primária | Conf. |
|---|---|---|---|---|---|
| D5 | WTC v1.7 `Wage Type Catalogue`!T123 = No; T326:T333 = No; nota em D123 cita Ley 21 art. 17, CE SU 25185/2021, CE 23856/2021 e a divergência do ABC UGPP 2025 | **Confirmado: parafiscais (SENA, ICBF, CCF) = No** em incapacidade (EPS, ARL, dias 1-2 do empregador, > 180 dias), licença maternidade/paternidade/parental, licença cuidado da infância e T123. O ABC UGPP 2025 não prevalece (guia sem força normativa, contraditório na própria p.6, contra a lei e o CE). | **Não** (valores já certos). Opcional: acrescentar à nota D123/D330 os 3 argumentos novos (ABC p.6 × p.7; Ley 789 art. 3 separa "descanso remunerado" de "incapacidad/maternidad"; na própria liquidação julgada em 23856 a UGPP excluiu as incapacidades). | Ley 21/1982 art. 17; CST arts. 128, 227; Ley 789/2002 art. 3; CE S4 23856 (19/08/2021); CE S4 SU 25185 (09/12/2021); Decreto 780 arts. 3.2.1.10 e 3.2.5.1 (só saúde e pensão) | 85% (incapacidade 90%; maternidade/paternidade 80%) |
| A-14 | CCG v1.5 T66R5: escala da Ley 2381 art. 20 (1,5/1,8/2,5/2,8/3,0%) + nota "AT2 v30 aplica 3,0% já em exatamente 20 SMMLV… vigente só a partir de 1/4/2027 (C-264 of 2026)"; T65R3: "C-264 of 25 August 2026 (case D-15989)"; T70R3-R7: faixas no formato do AT2 | **Confirmado.** Art. 20 foi declarado exequível (resolutivo 1º) e entra em vigor em **1/4/2027** (resolutivo 4º). Faixas da lei: 2,8% para ≥ 19 e **≤ 20** SMMLV; 3,0% para > 20. AT2 v30 dá 3,0% em exatamente 20. A lei prevalece; até 31/3/2027 vale Ley 100 art. 27 (Ley 797 art. 8), que é o que T70 já mostra. | **Não.** | Ley 2381/2024 art. 20; Corte Constitucional C-264-26 (25/08/2026, D-15989); AT2 v30 p.157-158 | 95% |
| P-06 | PILA-003 `PILA Spec`!K114/P114, K123/P123, K137, K139, K141, K143/P143, K145/P145 = "0.16000"-style (decimal com ponto, à esquerda, zeros à direita, 7 posições). **Mas** K131/J131 (T2R2-061, ARL, 9 posições) = "000005220", "Rate with implied decimals"; `Population Rules`!C17: "T2R2-061 (nine positions) keeps its own format" | **Confirmado o formato decimal "0.16000"** para os campos de 7 posições. **Novo: o ARL (T2R2-061) também vai em decimal**, "0.0052200" (à esquerda, zeros à direita até 9). O decimal implícito não tem base: o AT2 v30 copia o campo 61 para o arquivo de saída das ARL como "Tarifa. **En decimales**" (7 posições). Não é "0.16" nem "16". | **Sim (só ARL):** PILA-003 `PILA Spec`!J131, K131, P131 → decimal "0.0052200"; `Population Rules`!C17 → tirar "T2R2-061 keeps its own format". Os demais campos ficam. | AT2 v30 p.9, p.93-95, p.210; AT3 v15 §2.2.2.25 p.63 | 80% |
| DD-21 | DD v1.4 `Country Option Mappers`!C95:F103 = 10, 20, 42, 45, 47, 48, 49, 71, 72; C92 = Contado; `ID Information`!H7: banco obrigatório para "every code … except 1, 10, 20 and ZZZ; 98 counts as account-based" | **Códigos conferidos e corretos** (posição no PDF: 42 Consignación bancaria, 45 Transferencia Crédito Bancario, 47 Transferencia Débito Bancaria, 48 Tarjeta Crédito, 49 Tarjeta Débito, 71 Bonos, 72 Vales). **Muda a regra do H7:** "todos menos 1/10/20/ZZZ" puxa banco para cheques (23, 25, 26, 92), bonos (71), vales (72), notas e giros, que não são pagamento em conta. Usar lista positiva. Acrescentar o 98 (CATS: Nequi, Daviplata) ao mapper. | **Sim:** DD `ID Information`!H7 (e H8/H9 por coerência) → "Bank attributes expected for account-crediting codes only: 42, 45, 46, 47, 98 (and 2, 3, 30, 31 if used); not for 10, 20, 23, 25, 26, 71, 72, ZZZ. Annex: NIE066-NIE068 are 0-1"; `Country Option Mappers` → nova linha 98 CATS. | Res. DIAN 000013/2021, Anexo Técnico NE v1.0, NIE064-NIE068 (p.23-24), tabelas 5.3.3.1 e 5.3.3.2 (p.130-131) | 85% |
| Res. 2708 | CCG v1.5 cita a Circular 101/2025 em 12 lugares, todos já com "(revoked by Resolution 2708 of 2026)": P115, P356, P416, P425, P433, T12R3, T34R3, T35R3, T35R4, T52R7 (+ T2R6 do histórico) | Res. MinTrabajo 2708 de 20/08/2026, art. 1 num. 1.1, derroga a Circular Externa 0101 de 22/09/2025 a partir da publicação no Diário Oficial; art. 8: sem reviviscência; art. 5.4: nenhuma fórmula da 101 serve de fundamento autônomo. **Fica errado no CCG:** (a) T12R3 diz que a troca do dia de descanso é "limited to objective, demonstrable causes" — isso só existia na circular; a lei (CST art. 179 par. 3) exige só acordo escrito; (b) T35R3/R4 têm a circular revogada como única base dos divisores ÷220/÷210. Nenhum valor muda. | **Sim (texto):** T12R3 → tirar a frase das "objective causes"; T35R3/R4 coluna Basis → "Law 2101 of 2021 art. 3 (CST art. 161): 44 h/week to 14 July 2026, 42 h from 15 July 2026; divisor = weekly hours × 5 (derived)"; T34R3/T52R7 → base CST arts. 132 num. 1 e 161; P416 → "derived from CST art. 161 + art. 22"; P433 pode sair (assunto morto). | Res. MinTrabajo 2708/2026 arts. 1, 5.4, 8, 10 (cópia cerlatam, PDF imagem lido página a página); Ley 2466/2025 art. 14 | 90% |

---

## 1. D5 — parafiscais sobre incapacidade, licenças e T123

### Como está
WTC v1.7, aba `Wage Type Catalogue`, coluna T ("Subject to Payroll Levies - CCF 4% / SENA 2% / ICBF 3% (Ley 21/1982 base, NO ceiling)"): T123 (Long Term Disability) = No; T326 (incapacidade dias 1-2, empregador), T327 (EPS desde o dia 3), T328 (ARL), T329 (> 180 dias), T330 (maternidade), T331 (paternidade), T332 (parental compartilhada/flexível), T333 (cuidado da infância) = No. A nota D123 já registra a divergência do ABC UGPP 2025.

### Fontes e trechos
1. **Ley 21/1982 art. 17** (lei; local `2026-10-21-Ley-21-1982-FuncionPublica.html`; https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=4827):
   > "Para efectos de la liquidación de los aportes al Régimen del Subsidio Familiar, Servicio Nacional de Aprendizaje (SENA), Escuela Superior de Administración (ESAP), Escuelas Industriales e Institutos Técnicos, se entiende por nómina mensual de salarios la totalidad de los pagos hechos por concepto de los diferentes elementos integrantes del salario en los términos de la Ley Laboral, cualquiera que sea su denominación y además, los verificados por descansos remunerados de ley y convencionales o contractuales."
2. **Ley 789/2002 art. 3** (lei; local `2026-10-21-Ley-789-2002-SecretariaSenado.html`; http://www.secretariasenado.gov.co/senado/basedoc/ley_0789_2002.html). Trata do direito ao subsídio em dinheiro, não da base, mas mostra que a lei **separa** "descanso remunerado" de "incapacidad/maternidad":
   > "El trabajador beneficiario tendrá derecho a recibir el subsidio familiar en dinero durante el período de vacaciones anuales y en los días de descanso o permiso remunerado de ley, convencionales o contractuales; períodos de incapacidad por motivo de enfermedad no profesional, maternidad, accidentes de trabajo y enfermedad profesional."
3. **CE Sección Cuarta, 19/08/2021, rad. 25000-23-37-000-2015-00353-01 (23856), C.P. Stella Jeannette Carvajal Basto** (local `2026-10-22-CE-Seccion4-23856-2021-copia-actualicese.pdf`, cópia PwC/actualicese da sentença; p.17):
   > "Según los artículos 227 del CST y 3 de la Ley 776 de 2002, durante los periodos de incapacidad temporal el trabajador no recibe salario, sino un auxilio o subsidio por incapacidad que, tratándose de enfermedad de origen común es reconocido por la EPS y, de enfermedad laboral por la ARL. […] Comoquiera que el auxilio que recibe el trabajador incapacitado, en los términos de la ley laboral, no constituye salario, es claro que tampoco integra la nómina mensual de salarios y, en consecuencia, se excluye de la base para calcular los aportes con destino al SENA, ICBF y CCF."
   
   E (p.18) a própria UGPP, na liquidação julgada, **não** incluiu as incapacidades: "está probado que en los actos demandados la UGPP no liquidó los aportes con destino al SENA, ICBF y CCF incluyendo en la base los pagos por concepto de incapacidades".
   
   Sobre a licença-maternidade, a mesma sentença (p.14) a qualifica como "prestación económica del sistema de salud en seguridad social" (citando a Corte Constitucional T-998/2008).
4. **CE Sección Cuarta, SU rad. 05001-23-33-000-2016-02496-01 (25185), 09/12/2021** (ficha local `2026-10-22-CE-S4-SU-25185-2021-ficha.pdf`): a UGPP somou ao IBC de ARL, SENA, ICBF e CCF "lo recibido por concepto de salario, sin que se hubieran tenido en cuenta las incapacidades", e a Sala manteve.
5. **Decreto 780/2016 art. 3.2.1.10** (decreto; local `2026-10-22-Decreto-780-2016-funcionpublica.htm`; https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=77813). O IBC na incapacidade é regulado **só** para saúde e pensão:
   > "Durante los períodos de incapacidad por riesgo común o de licencia de maternidad, habrá lugar al pago de los aportes a los Sistemas de Salud y de Pensiones. Para efectos de liquidar los aportes correspondientes al período por el cual se reconozca al afiliado una incapacidad por riesgo común o una licencia de maternidad, se tomará como Ingreso Base de Cotización el valor de la incapacidad o licencia de maternidad según sea el caso."
   
   O art. 3.2.5.1 repete a regra para saúde. Nenhum dos dois trata de SENA/ICBF/CCF.
6. **Decreto 1072/2015**: só o art. 2.2.4.2.1.6 (sem ARL durante a novidade). Busquei "incapacidad"/"maternidad" junto de "subsidio familiar", "SENA", "ICBF" e "nómina mensual" no arquivo local: nenhuma regra de base parafiscal.
7. **Ley 1393/2010**: o art. 30 trata só do limite de 40% dos pagamentos não salariais. Não fala de incapacidade.
8. **AT2 v30** (Res. MSPS 1529/2026; local `2026-10-29-MinSalud-AT2-v30-2026-07-24-PILA-activos.txt`): campos 64/66/68 (tarifas CCF/SENA/ICBF): "Los valores válidos son los legalmente vigentes para el período que se está pagando" (p.161-162). Campos 25 (IGE) e 26 (LMA) só afastam a ARL (p.165-166). Sobre o IBC das novidades (p.103): "Es responsabilidad del aportante hacer el cálculo del ingreso base de cotización que afecta las novedades que se presentan durante el periodo." **O anexo não decide** a base parafiscal na incapacidade.
9. **O texto da UGPP que diverge.** ABC Empleadores 2025 (local `2026-10-22-UGPP-ABC-Empleadores-2025.pdf`; https://www.ugpp.gov.co/wp-content/uploads/2025/02/ABC_empleadores2025.pdf), p.7:
   > "Novedad por incapacidades o licencia de maternidad/paternidad: para liquidar la base de cotización del sistema de parafiscales (caja de compensación familiar, SENA e ICBF), debe tener en cuenta el valor reconocido al trabajador por las incapacidades y/o licencia de maternidad o paternidad."
   
   Mas a p.6 do **mesmo** ABC monta o IBC parafiscal assim: "Contribuciones Parafiscales (SENA, ICBF y CCF): Todos los pagos salariales + Lo pagado por vacaciones o descansos remunerados". As "novedades del periodo (incapacidades <Riesgo común, laboral, maternidad, paternidad>, licencia remunerada)" ficam só na coluna "Sistema Seguridad Social Integral (Salud, pensiones y ARL)". E o ABECE Pago Correcto Empleadores V1 da UGPP (local `2026-10-30-UGPP-ABECE-Pago-Correcto-Empleadores-V1.pdf`; https://www.ugpp.gov.co/sites/default/files/Parafiscales/ABECE-Pago-Correcto-Empleadores-V1.pdf), p.4: "Para el caso de las incapacidades y licencias de maternidad: Para el cálculo de la base de cotización en salud y pensión debo tener en cuenta el valor reconocido por las administradoras correspondientes." Ali não há menção a parafiscais.

### Decisão
- **Incapacidades (T326, T327, T328, T329) e T123 = No.** A lei (Ley 21 art. 17) só põe na base salário e descanso remunerado. O auxílio de incapacidade não é salário (CST arts. 128 e 227; Ley 776 art. 3). O CE decidiu isso expressamente (23856/2021), e a própria UGPP excluiu as incapacidades nas liquidações julgadas (23856; SU 25185). T123 (complemento de invalidez/longa duração, quando pago pela folha) tem a mesma natureza: não é salário nem descanso. → 90%.
- **Maternidade, paternidade, parental e cuidado da infância (T330 a T333) = No.** É prestação econômica do sistema de saúde paga pela EPS (CE 23856, p.14). A Ley 789 art. 3 trata "maternidad" como algo distinto de "descanso o permiso remunerado de ley". **Risco:** o CST art. 236 chama a licença de "descanso remunerado" e "remunerada con el salario". Uma notícia (Ámbito Jurídico) atribui ao CE S4, rad. 25000-23-27-000-2011-00288-01 (19736), de 25/04/2016, a regra "incapacidades y licencias de maternidad no conforman base gravable de parafiscales", mas **não li a sentença** (403 no site; não achei cópia oficial). → 80%.
- **Por que o ABC 2025 não prevalece:** (i) é guia de divulgação, abaixo da lei e do decreto na hierarquia, e não pode criar base de contribuição; (ii) contradiz a própria p.6; (iii) contradiz o ABECE V1 da mesma UGPP e a prática da UGPP confirmada pelo CE; (iv) contradiz a jurisprudência da Seção Quarta, que é o juiz das liquidações da UGPP. Risco prático: a UGPP pode autuar com base na p.7. O CE tende a anular. Manter "Configurable".

---

## 2. A-14 — Fundo de Solidaridad Pensional (Ley 2381 art. 20) × AT2 v30

### Fontes e trechos
1. **Ley 2381/2024 art. 20** (local `2026-10-30-Ley-2381-2024-SecretariaSenado.html`; http://www.secretariasenado.gov.co/senado/basedoc/ley_2381_2024.html). Faixas exatas:
   > "1. … igual o superior a cuatro (4) salarios mínimos legales mensuales vigentes (smlmv) y menor a siete (7) smlmv … uno punto cinco por ciento (1.5 %) … 2. … igual o superior a siete (7) smlmv y menor a once (11) smlmv … uno punto ocho por ciento (1.8%) … 3. … igual o superior a once (11) smlmv y menor a diez y nueve (19) smlmv … dos punto cinco por ciento (2.5%) … 4. … igual o superior a diez y nueve (19) smlmv y menor o igual a veinte (20) smlmv … dos punto ocho por ciento (2.8%) … 5. … superior a veinte (20) smlmv … tres por ciento (3.0%) de su Ingreso Base de Cotización."
   
   Cabeçalho da compilação: "<Los artículos declarados exequibles entran en vigencia a partir del 1 de abril de 2027. Sentencia C-264-26>".
2. **Corte Constitucional, Sentencia C-264 de 2026**, Expediente D-15989, M.P. Paola Andrea Meneses Mosquera, "Bogotá, D. C., veinticinco (25) de agosto de dos mil veintiséis (2026)". **Baixada nesta sessão:** `2026-11-02-CorteConstitucional-C-264-2026.htm`, https://www.corteconstitucional.gov.co/relatoria/2026/C-264-26.htm (md5 9defa626e8193087cfb8ca48b184f8fe).
   > "PRIMERO. Declarar la EXEQUIBILIDAD, exclusivamente por los vicios de procedimiento examinados en esta providencia, de los artículos 1, 2, … 19 con excepción del literal (k), 20, 21, 22, 23 con excepción del parágrafo transitorio, … y 95 de la Ley 2381 de 2024"
   
   > "CUARTO. DECLARAR la EXEQUIBILIDAD del artículo 94 de la Ley 2381 de 2024, en el entendido de que las disposiciones declaradas exequibles en el resolutivo primero entrarán en vigencia a partir del 1 de abril de 2027."
   
   O art. 20 **não** está entre os devolvidos à Câmara (11 inc. 4, 14, 19 lit. k, 23 par. trans., 36, 63 inc. 2, 84 num. 5, 92 inc. 1, 93).
3. **AT2 v30** p.157-158 (campo 52, subconta de subsistência). Cotizantes "S" (Ley 797 art. 8): "Igual a 16 hasta 17 0.2% / Mayor a 17 hasta 18 0.4% / Mayor a 18 hasta 19 0.6% / Mayor a 19 hasta 20 0.8% / Mayor a 20 1.0%". Cotizantes "N" (Ley 2381 art. 20): "Igual o mayor a 4 menor a 7 1.0% / Igual o mayor a 7 menor a 11 1.3% / Igual o mayor a 11 menor a 19 2.0% / Igual o mayor a 19 menor a 20 2.3% / Igual o mayor a 20 2.5%". Campo 51 (p.156): "por 0.5%, factor correspondiente a la Subcuenta de Solidaridad".

### Conta
AT2 "N" + 0,5% = 1,5 / 1,8 / 2,5 / 2,8 / 3,0%, igual à lei, **salvo na borda**. Com IBC exatamente 20 SMMLV, o AT2 dá 2,5 + 0,5 = **3,0%** ("Igual o mayor a 20") e a lei dá **2,8%** ("menor o igual a veinte"). O AT2 v30 é de 24/07/2026, anterior à C-264 (25/08/2026).

### Decisão
O CCG v1.5 já está certo e não muda: T66R5 traz a escala da lei, a nota da borda e a vigência de 1/4/2027; T65R3 traz número, data e expediente corretos; T70 mostra a regra atual (Ley 100 art. 27, mod. Ley 797 art. 8), com as faixas redigidas como no AT2. Até 31/3/2027 o motor usa a Ley 797. A partir de 1/4/2027 usa a lei (2,8% em exatamente 20) e confirma com o operador PILA. **Fora do pedido:** o AT2 v30 manda aplicar a tabela "N" "de julio de 2025 en adelante", data anterior à C-264. Quando o MinSalud ajustar o anexo à nova vigência, conferir se a borda de 20 SMMLV foi corrigida.

---

## 3. P-06 — formato da tarifa no arquivo PILA

### Fontes e trechos (AT2 v30, local)
- p.9: "Los campos tipo numérico 'N', se reportarán justificados a la derecha y rellenados con ceros a la izquierda."
- Leiaute de entrada (p.93-95): "46 7 238 244 N Tarifa de aportes pensiones." · "54 7 308 314 N Tarifa de aportes salud" · "61 9 381 389 N Tarifa de aportes a Riesgos Laborales." · "64 7 408 414 N" (CCF) · "66 7 424 430 N" (SENA) · "68 7 440 446 N Tarifa aportes ICBF" · "70 7 456 462 N" (ESAP) · "72 7 472 478 N Tarifa aportes MEN".
- Saída para as ARL (p.210): "28 7 167 173 N Tarifa. En decimales. El registrado en el campo 61 del registro tipo 2 del archivo tipo 2."
- Campo 64 (p.161): "Los valores válidos son los legalmente vigentes para el período que se está pagando." O anexo **não** imprime exemplo da tarifa de entrada. Conferi também o AT2 de 2016 (minsalud.gov.co/…/Anexo-tecnico-2-2016-pila.pdf, acessado em 02/11, não arquivado): só "Tarifa. En decimales.", sem exemplo.
- **AT3 v15** §2.2.2.25 campo 51, p.63 (local `2026-10-29-MinSalud-AT3-v15-2026-07-24-PILA-pensionados.txt` l.3415), mesmo ministério, campo N de 7 posições: "El valor del campo debe ser en decimal, justificado a la izquierda y completando la longitud del campo con ceros a la derecha, por ejemplo 2.0% sería 0.02000." O AT3 também tem a regra geral "justificados a la derecha" (l.284), e o exemplo específico a afasta.

### Decisão
- "16" está descartado (o campo é "En decimales"). "0.16" sem preenchimento não cumpre o comprimento fixo. Já "0016000" ou "0000016" (decimal implícito) não têm base em nenhum anexo. Fica **"0.16000"**, como o AT3 imprime, para os campos de 7 posições: K114, K123, K137, K139, K141, K143, K145. **Já está assim na v1.0 final.**
- **ARL (T2R2-061, 9 posições):** a spec diz "000005220" com decimal implícito (K131/J131/P131) e `Population Rules`!C17 diz que o campo "keeps its own format". Isso contradiz o AT2: o operador copia o campo 61 para a saída das ARL como "Tarifa. En decimales" em 7 posições. Logo, a entrada também é decimal com ponto, preenchida até 9: **"0.0052200"** (0,522%). Classe V 6,960% → "0.0696000".
- Por que 80% e não 100%: nenhum anexo traz exemplo do campo de entrada do AT2. Apoio-me no exemplo do AT3 (mesmo ministério e mesmo tipo) e no "En decimales" da saída. Confirmar com o operador de informação na implantação, como a spec já diz.

---

## 4. DD-21 — meios de pagamento (Nómina Electrónica)

### Fontes e trechos
- **Res. DIAN 000013/2021, Anexo Técnico Documento Soporte de Pago de Nómina Electrónica v1.0** (PDF oficial da caixa de ferramentas DIAN: `Research Pipeline/Colombia/CO-compliance/integration-sources/dian-ne/caja/…/Anexo Tecnico Documento Soporte de Pago de Nómina Electrónica - V1.0.pdf`, sha256 e6a058d4…; https://www.dian.gov.co/impuestos/factura-electronica/Documents/Caja-de-Herramientas-Nomina-Electronica-V1-0.zip). O micrositio DIAN (local `2026-10-21-DIAN-micrositio-documentacion-tecnica-nomina.html`) ainda aponta só esta versão (V1-0). A Res. 13/2021 foi compilada na Res. DIAN 000227 de 23/09/2025 (Resolución Única); **não li** o texto da 227.
- NIE064 (p.23): "Formas de Pago del Documento … 1-1 Se debe colocar el Codigo de la tabla 5.3.3.1". NIE065: "Metodos de Pago del Documento … 1-1 Se debe colocar el Codigo de la tabla 5.3.3.2". NIE066/067/068 (p.24): "0-1 Si el método de pago se realiza de forma bancaria. Se debe colocar el nombre de la entidad bancaria donde el trabajador tiene su cuenta para pago de nómina." (e "el tipo de cuenta", "el número de la cuenta").
- Tabela 5.3.3.1 (p.130): "1 Contado" (valor único).
- Tabela 5.3.3.2 (p.130-131). A extração de texto simples desalinha a coluna da direita, então conferi pela **posição** das palavras (pdfplumber): "42 Consignación bancaria", "45 Transferencia Crédito Bancario", "46 Transferencia Débito Interbancario", "47 Transferencia Débito Bancaria", "48 Tarjeta Crédito", "49 Tarjeta Débito", "71 Bonos", "72 Vales", "92 Cheque local trasferible", "93 Giro referenciado", "98 Cuentas de Ahorro de Tramite Simplificado (CATS)(Nequi, Daviplata, etc)", "ZZZ Acuerdo mutuo". Coluna da esquerda: "10 Efectivo", "20 Cheque", "23 Cheque bancario", "25 Cheque certificado", "26 Cheque Local", "30 Transferencia Crédito", "31 Transferencia Débito".

### Decisão
- Mapper (`Country Option Mappers`!C95:F103): os 9 códigos e nomes **conferem**, e C92 (Contado) também. Acrescentar **98 CATS**, meio comum de pagamento de folha na Colômbia que o próprio H7 já cita.
- `ID Information`!H7: a regra "todos os códigos menos 1, 10, 20 e ZZZ" está **errada por excesso**. Cheques (23, 25, 26, 92), bonos (71), vales (72), notas promissórias (60-67) e giros (93-95) não são "de forma bancaria" em conta do trabalhador. Texto (EN) proposto: "Bank name, account type and account number are populated only for account-crediting media: 42, 45, 46, 47 and 98 (also 2, 3, 30, 31 if used); left empty for 10, 20, 23, 25, 26, 71, 72 and ZZZ. The annex makes the three attributes optional (0-1, NIE066-NIE068); requiring all three for account media is an engine rule." 48/49 (cartões): pagamento em cartão de folha ligado a conta → tratar como conta só se o cliente usar; marcar como interpretação.
- A regra "where 10 (cash) the bank attributes MUST BE ABSENT" (G95, W30) é compatível com o anexo (0-1). Fica.

---

## 5. Res. MinTrabajo 2708 de 20/08/2026 (revoga a Circular 101/2025)

### Fonte
Local `2026-10-30-Res-MinTrabajo-2708-2026-copia-cerlatam.pdf` (22 páginas, PDF imagem, com assinatura da Ministra Natalia Eugenia López Fuentes e carimbo "20 AGO 2026"); https://www.cerlatam.com/normatividad/mintrabajo-resolucion-2708-de-2026-20-ago-26/. **Não há OCR na máquina** (sem tesseract/ocrmypdf/pytesseract). Converti as páginas em imagem (PyMuPDF, 110 dpi) e li visualmente as p.1, 3, 5, 6, 13-15 e 17-22. Não achei versão em texto no site do MinTrabajo nem o número do Diário Oficial.

### Trechos (transcritos da imagem)
- Título (p.1): "Por la cual se derogan y se dejan sin efectos unas circulares expedidas por el Ministerio del Trabajo y se adoptan medidas de depuración de lineamientos administrativos".
- Art. 1 (p.18): "Derogar y dejar sin efectos, a partir de la publicación de la presente resolución, las siguientes circulares expedidas por el Ministerio del Trabajo: 1.1. Circular Externa 0101 del 22 de septiembre de 2025. 1.2. Circular Interna 0120 de 2025. 1.3. Circular 0031 del 17 de marzo de 2026. […] 1.11. Circular 0089 del 29 de julio de 2026." Mais: "La derogación y pérdida de efectos dispuesta en el presente artículo opera hacia el futuro, sin perjuicio de las situaciones jurídicas consolidadas…"
- Considerando sobre a 101 (p.14): a circular tratava da "aplicación de la Ley 2466 de 2025 en materias relacionadas con jornada máxima, trabajo doméstico, remuneración a destajo, registro y control de horas extras, límites al trabajo suplementario y remuneración del trabajo en días de descanso obligatorio" e "formula reglas de conducta, criterios de liquidación y consecuencias concretas dirigidas a sus destinatarios". P.15: "procede retirar la Circular Externa 0101 de 2025 […] A partir de la entrada en vigencia de la presente resolución, las fórmulas o metodologías contenidas en la circular derogada no podrán ser utilizadas como criterio administrativo autónomo de exigibilidad o sanción."
- P.17: "la derogación de las Circulares […] Externa 0101 de 2025 no produce un vacío normativo, por cuanto permanecen plenamente vigentes las disposiciones constitucionales, legales y reglamentarias y la jurisprudencia aplicable".
- Art. 5.4 (p.21): "ninguna fórmula, metodología o criterio de liquidación contenido en la Circular Externa 0101 de 2025 podrá utilizarse como fundamento jurídico autónomo para exigir una obligación económica, determinar una liquidación o sustentar una consecuencia sancionatoria, sin perjuicio de la aplicación directa de las disposiciones legales y reglamentarias vigentes que regulen la jornada de trabajo, el salario y la remuneración a destajo."
- Art. 8 (p.22): "No reviviscencia. La derogación de las circulares señaladas en el artículo 1 no revive automáticamente circulares, instrucciones o criterios administrativos anteriores…"
- Art. 10 (p.22): "La presente resolución rige a partir de la fecha de su publicación en el Diario Oficial…"

### O que fica errado no CCG v1.5
A v1.5 já marca a circular como revogada nos 12 lugares. Nenhum **valor** depende só da circular. O que fica errado ou frágil:
1. **T12R3**: "Circular 101 of 2025 §5 … stressed that the substitution is not a discretionary employer choice: it is limited to objective, demonstrable causes…". A regra só existia na circular. A lei diz apenas (Ley 2466 art. 14, CST art. 179 par. 3; local `2026-10-30-Ley-2466-2025-SecretariaSenado.html`): "Las partes del contrato de trabajo podrán convenir por escrito que su día de descanso sea distinto al domingo. En caso de que las partes no lo hagan expreso en el contrato u otro sí, se presumirá como día de descanso obligatorio el domingo." → **Tirar a frase das "objective causes"** (com a circular revogada e o art. 8, ela não é mais regra).
2. **T35R3/T35R4** (coluna Basis): a única base citada é a circular revogada. → "Law 2101 of 2021 art. 3 / Labour Code art. 161: 44-hour week to 14 July 2026 (÷ 220), 42-hour week from 15 July 2026 (÷ 210); divisor = weekly hours × 5 (30 days ÷ 6 working days), derived." Os valores 7.958,66 e 8.337,64 ficam.
3. **T34R3, T52R7** (destajo "confirmed expressly"): trocar a base por CST art. 132 num. 1 (salário "por unidad de tiempo, por obra, o a destajo y por tarea") e art. 161. O CCG não usa a fórmula de compensação do destajo que o art. 5.4 proíbe. Conferido: só T40R1 e T245R4 falam de destajo, ambos com base no CST.
4. **P416**: os máximos de 56 h e 54 h são conta da lei (44 + 12; 42 + 12; CST art. 161 + art. 22 mod. Ley 2466 art. 13). Atribuir a conta à lei, não à circular.
5. **P115, P356, P425**: menções históricas certas, sem efeito. **P433** ("A defect in the official guidance…") perdeu o objeto. Pode sair.
6. WTC v1.7, DD v1.4, specs, Payslip e SIR v1.2: **0** menções à Circular 101 (busca mecânica).

---

## Bloco de prova

**Pedido → resposta**
1. D5: Ley 21 art. 17, Ley 789, Ley 1393, Decretos 1072 e 780, AT2 v30, UGPP e CE S4 → §1; decisão No mantida, ABC 2025 lido e afastado com motivo → feito.
2. A-14: faixas exatas do art. 20 × AT2 v30, número, data e vigência da C-264-26, texto do CCG → §2 → feito (já certo na v1.5).
3. P-06: tipo, comprimento e decimais dos campos de tarifa no AT2 v30, decisão → §3 → feito, com achado novo no ARL (T2R2-061).
4. DD-21: tabela oficial 5.3.3.1/5.3.3.2, códigos e classificação → §4 → feito.
5. Res. 2708: texto lido (imagem), o que revoga, o que fica errado no CCG → §5 → feito.

**Fontes:** cada afirmação acima tem fonte primária com trecho literal. Local quando já estava baixada; URL e data de acesso 02/11/2026 nas novas. Hierarquia aplicada: lei > decreto > resolução/anexo > guia UGPP.

**Teste (mecânico)**
- Células lidas por script nos finais: WTC T123, T326:T333 (coluna T) e D123; CCG T65, T66R5, T70, T12R3, T34R3, T35, T52R7, P115, P356, P416, P425 e P433; PILA-003 linhas 114, 123, 131, 137, 139, 141, 143, 145 e `Population Rules`!C17; DD `ID Information`!H7:H9 e `Country Option Mappers`!92-103.
- Conta da borda FSP: AT2 "N" ≥ 20 → 2,5 + 0,5 = 3,0; lei ≤ 20 → 2,8.
- Códigos 5.3.3.2 conferidos pela posição x/y no PDF oficial.
- Busca de "Circular 101/0101" em todos os finais (12 no CCG, 0 nos demais).
- md5 da C-264-26 baixada.

**Confiança: 87% média.** Abaixo de 100%:
- D5 maternidade (80%): não li a sentença CE 19736/2016, só a notícia.
- P-06 (80%): falta exemplo oficial do campo de entrada do AT2; confirmar com o operador.
- DD-21 (85%): a lista "conta × não conta" é nossa, porque o anexo só diz "de forma bancaria".
- Res. 2708 (90%): lida em cópia (cerlatam) por imagem; número do Diário Oficial não localizado.
