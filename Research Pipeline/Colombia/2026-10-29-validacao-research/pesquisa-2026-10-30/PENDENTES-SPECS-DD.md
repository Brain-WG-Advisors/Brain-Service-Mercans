# Pendentes da research CO: specs, DD, Payslip, SIR (pesquisa de 30/10/2026)

> Frente Validação CO · Base: [[mudancas-PENDENTES]] (revisao/) · Liga: [[CONFERENCIA]] · [[Colombia]]
> Escopo deste lote: todo item cujo artefato **não** é CCG v1.4 nem WTC v1.6 (F-12, que toca CCG e WTC, ficou fora).
> Nenhum artefato foi alterado. "Decisão" = texto proposto (EN) para a célula; aplicar só com ok do usuário (Colômbia ativa → regra 9, ticket ao Development).
> Fontes baixadas hoje: `raw/docs/oficiais/CO/2026-10-30-*` (lista no fim). Data de acesso de toda URL abaixo: **2026-10-30**.

## Resumo

| Veredito | Qtd | Itens |
|---|---|---|
| CONFIRMADO muda | 21 | P-06, P-17, DD-10, DD-15, DD-16, DD-21, DD-24, NE-03, NE-04, NE-10, NE-18, F-06, SIM-07 (já aplicado no DRAFT), F-11 (006), F-10 (006), PS-06, PS-11, PS-13, S-03, S-04, S-05 |
| CONFIRMADO não muda (só nota) | 3 | P-01, NE-15, DD-23 (com ressalva para casillas 79–81) |
| Continua aberto | 1 | S-07 (divisão R/N exata; decisão provisória: tirar a divisão) |
| Já CONFIRMADO antes (linha quebrada no PENDENTES) | 2 | DD-08, NE-05 (NE-05 já aplicada na rodada 2) |
| **Total** | **27** | |

---

## PILA (CO-PILA-003 / 007)

### P-06 · formato da tarifa (003 PILA Spec!K114/P114/K123/P143/P145; Population Rules!C17)
- **Veredito:** CONFIRMADO muda · **Confiança 75%**
- **Decisão (EN):** "Rate written as a decimal with a point, left-justified and zero-filled to 7 positions (e.g. 16% = `0.16000`, 4% = `0.04000`), as AT3 v15 prints for the same ministry and length and as the AT2 output layout states ('En decimales'). Confirm with the information operator during set-up."
- **Fonte:**
  - AT3 v15 (24/07/2026), §2.2.2.25 campo 51, p.63: "El valor del campo debe ser en decimal, justificado a la izquierda y completando la longitud del campo con ceros a la derecha, por ejemplo 2.0% sería 0.02000." (`raw/docs/oficiais/CO/2026-10-29-MinSalud-AT3-v15-2026-07-24-PILA-pensionados.txt` l.3415)
  - AT2 v30 (24/07/2026), saída, p.210: "28 7 167 173 N Tarifa. En decimales."; p.9: "Los campos tipo numérico 'N', se reportarán justificados a la derecha y rellenados con ceros a la izquierda." (local, l.12373 e l.395)
- **Por que não 100%:** o AT2 v30 não imprime exemplo da tarifa de entrada; a regra geral do p.9 (N = à direita, zeros à esquerda) e o exemplo do AT3 (à esquerda, zeros à direita) não coincidem. Busquei guia público de operador (Aportes en Línea, SOI, Mi Planilla) e exemplo de arquivo: nada oficial achado. O decimal implícito ("0160000") não tem base em nenhum anexo.

### P-17 · centro de trabalho (003 PILA Spec!G132)
- **Veredito:** CONFIRMADO muda · **Confiança 90%**
- **Decisão (EN):** "Mandatory whenever an ARL code is reported; value = the work-centre code defined by the ARL (AT2 v30 §2.1.2.3.26). The VCT novelty (field 29) is reported when the work centre changes in the period."
- **Fonte:** AT2 v30 §2.1.2.3.26, p.160: "Campo 62 - Centro de trabajo - CT. Debe existir cuando exista código de ARL. Debe ser suministrado por el aportante con base en los códigos de centros de trabajo definidos por la ARL". p.95: "62 9 390 398 N Centro de trabajo CT. Lo suministra el aportante." p.89: "29 … VCT: Variación centros de trabajo. Puede ser un blanco o X."
- A condição atual ("populated where the employer has more than one work centre") contradiz o anexo: o campo é obrigatório sempre que há ARL.

### P-01 · arredondamento da cotização (007 M108, P108; Population Rules!C9, C18)
- **Veredito:** CONFIRMADO não muda · **Confiança 92%**
- **Decisão (EN):** manter "rounded UP to the next multiple of 100 (Decreto 780 de 2016 art. 3.2.1.5 num. 2)"; acrescentar nota: "AT3 v15 p.63 says 'múltiplo de cien más cercano' but refers to the same art. 3.2.1.5, which says 'superior'."
- **Fonte:** Decreto 780/2016 art. 3.2.1.5 num. 2: "El valor de los aportes liquidados por cada cotizante y el valor de los intereses, deberá aproximarse al múltiplo de 100 superior más cercano" (`2026-10-22-Decreto-780-2016-funcionpublica.htm`). AT3 v15 §2.2.2.23, p.63: "se aproximará al múltiplo de cien más cercano de acuerdo con lo establecido en el artículo 3.2.1.5 del Decreto 780 de 2016." O próprio anexo remete ao decreto; não há conflito real.

## DD (CO-DD-001 v1.3)

### DD-10 · aprendiz lectiva × produtiva (Mappers!F60, F65, F66)
- **Veredito:** CONFIRMADO muda · **Confiança 85%**
- **Decisão (EN):** "Add field 'Apprentice phase' (LECTIVA / PRACTICA). PILA cotizante type: lectiva → 19 (health + ARL, IBC 1 SMMLV) for health periods from Aug-2025; practica → 1 Dependiente (all systems), per Ley 2466/2025 art. 21 (CST art. 81). Before Aug-2025: lectiva → 12, productiva → 19. NE TipoTrabajador (Anexo NE v1.0 table 5.5.3, unchanged): 12 = etapa lectiva, 19 = etapa productiva — the two catalogues use code 19 for different phases."
- **Fonte:**
  - Ley 2466/2025 art. 21 (modifica CST art. 81): "Durante la fase práctica o durante toda la formación dual, el aprendiz estará afiliado a riesgos laborales y al sistema de seguridad social integral en pensiones y salud conforme al régimen de trabajadores dependientes." (https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=260676)
  - AT2 v30 p.108: "A partir del periodo de cotización a salud del mes de agosto de 2025, este tipo de cotizante [19] se utiliza para el pago de aportes a los Sistemas Generales de Salud y Riesgos Laborales de los aprendices en etapa lectiva"; p.107 (tipo 12): "solamente es permitido … de periodos de cotización a salud anteriores al mes de agosto de 2025."
  - Anexo NE v1.0 tabela 5.5.3, p.179: "12 Aprendices del Sena en etapa lectiva … 19 Aprendices del SENA en etapa productiva".
- A "lacuna oficial" do F60 não existe: a fase prática não tem código próprio porque a lei a põe no regime de dependente (tipo 1). Fica aberto só o rótulo 19 da NE (DIAN não atualizou a tabela; Res. 227/2025 manteve os anexos).

### DD-15 · medicina prepagada / AFC / AVC (Country Fields, ausente)
- **Veredito:** CONFIRMADO muda · **Confiança 80%**
- **Decisão (EN):** "Add employee inputs used by the withholding base: (a) monthly prepaid-medicine / supplementary health plan payment (cap 16 UVT/month; supported by the provider's certificate — entity supervised by Supersalud); (b) voluntary RAIS contributions, AFC and AVC deposits (WTC wage types; certificate from the fund). Store the certificate period (from/to)."
- **Fonte:** DUR 1625/2016 art. 1.2.4.1.6 num. 4.2: "sobre los pagos por salud señalados en los literales a) y b) del artículo 387 … siempre que el valor a disminuir mensualmente, no supere dieciséis (16) Unidades de Valor (UVT) mensuales, y se cumplan las condiciones de control indicadas en las normas reglamentarias vigentes"; par. 1: "son los pagos efectuados por contratos de prestación de servicios a empresas de medicina prepagada, vigiladas por la Superintendencia Nacional de Salud…"; num. 3.2 (aportes voluntários RAIS, 25%/2.500 UVT). (`2026-10-13-DUR-1625-2016-DIAN.htm`)
- Não achei no DUR o texto das "condiciones de control" (certificado); a forma do suporte fica como prática, não como regra citada.

### DD-16 · causa de término (Country Fields!24)
- **Veredito:** CONFIRMADO muda · **Confiança 88%**
- **Decisão (EN):** "Add 'Termination reason' (list), mandatory when Termination Date is filled: CST art. 61 num. 1 a)–i) (death, mutual consent, fixed-term expiry, end of work, closure, suspension >120 days, court ruling, unilateral decision, non-return); just cause by employer (CST art. 62); without just cause by employer or employee-triggered just cause (CST art. 64 → indemnity)."
- **Fonte:** CST art. 61 (Ley 50/1990 art. 5): "1. El contrato de trabajo termina: a). Por muerte del trabajador; b). Por mutuo consentimiento; c). Por expiración del plazo fijo pactado; …". CST art. 64 (Ley 789/2002 art. 28): "En caso de terminación unilateral del contrato de trabajo sin justa causa comprobada, por parte del empleador o si éste da lugar a la terminación unilateral por parte del trabajador por alguna de las justas causas contempladas en la ley, el primero deberá al segundo una indemnización…" (`2026-10-22-CST-pr001-SecretariaSenado.html`)

### DD-21 · meios de pagamento (Mappers!95-103; ID Information!H7)
- **Veredito:** CONFIRMADO muda · **Confiança 75%**
- **Decisão (EN):** "Partial list. Engine rule: Banco / TipoCuenta / NumeroCuenta are filled when the payment is made to an account ('de forma bancaria'), i.e. every code of table 5.3.3.2 except 1 (Instrumento no definido), 10 (Efectivo), 20 (Cheque) and ZZZ (Acuerdo mutuo); code 98 (CATS: Nequi, Daviplata) counts as account-based. The three attributes are optional (0-1) in the annex."
- **Fonte:** Anexo NE v1.0 p.24, NIE066–NIE068: "0-1 Si el método de pago se realiza de forma bancaria. Se debe colocar el nombre de la entidad bancaria…"; tabela 5.3.3.2, p.131: "98 Cuentas de Ahorro de Tramite Simplificado (CATS)(Nequi, Daviplata, etc) … ZZZ Acuerdo mutuo". A classificação "bancário × não bancário" de cada código é nossa (o anexo não a dá).

### DD-23 · seção do empregado no Form. 220 (Country Fields!I45)
- **Veredito:** CONFIRMADO não muda para as casillas 61–78; muda para 79–81 · **Confiança 90%**
- **Decisão (EN):** "Casillas 61–78 ('Datos a cargo del trabajador o pensionado') are completed by the employee, not from payroll. Casillas 79–81 (economic dependant) come from the dependant certificate the employee gave the employer (DUR 1.2.4.1.18 par.) and are populated by payroll when the dependant deduction was applied."
- **Fonte:** Res. DIAN 22/2024 (Form. 220, anexo), instrutivo p.2: "Importante: esta sección solo debe ser diligenciada por aquel trabajador o pensionado que no esté obligado a declarar impuesto sobre la renta"; p.3: "79. … 81. Estas casillas deberán ser diligenciadas con la información correspondiente al dependiente económico para efectos de disminuir la base mensual de retención en la fuente". (https://normograma.com/documentospdf/PDF/R_DIAN_0022_2024.pdf; ligada a https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0022_2024.htm)

### DD-24 · centro de trabalho como entidade (Country Fields!22, 95)
- **Veredito:** CONFIRMADO muda · **Confiança 85%**
- **Decisão (EN):** "Model 'Work centre' as an entity: ARL work-centre code, risk class (I–V), economic activity code, ARL. Employee → work centre (effective-dated). Risk class may differ by centre only under Decreto 1072 art. 2.2.4.3.9."
- **Fonte:** Decreto 1072/2015 art. 2.2.4.3.9: "se entiende por Centro de Trabajo a toda edificación o área a cielo abierto destinada a una actividad económica en una empresa determinada. Cuando una empresa tenga más de un centro de trabajo podrán clasificarse los trabajadores de uno o más de ellos en una clase de riesgo diferente…" (`2026-10-13-Decreto-1072-2015-FuncionPublica.html`); AT2 v30 §2.1.2.3.26 (ver P-17).

### DD-08 · regex dos códigos de administradora — já CONFIRMADO (VERIFICADO-2, 92%)
- Linha quebrada no PENDENTES. Reconferido: AT2 v30 l.9144 "Administradora Colpensiones identificada con el código 25-14"; l.1991 "administradora con código MIN001". Decisão já registrada: retirar o regex e validar contra o catálogo do MinSalud.

## Nómina Electrónica (CO-DIAN-001)
Base: Anexo Técnico NE v1.0 (Res. DIAN 13/2021), compilado pela Res. 227/2025 sem nova versão (pesquisa de 29/10). Cópia local: `achados/verif2-work/anexo_ne_v2.txt`; XSD 1.0.6.

### NE-03 · DiasTrabajados (Population Rules!C9; Spec!M85)
- **Veredito:** CONFIRMADO muda · **Confiança 85%**
- **Decisão (EN):** "DiasTrabajados = days the worker actually worked in the settlement period. Days of incapacity, maternity/paternity leave, paid and unpaid leave and vacation are NOT counted here; they are reported in their own blocks (Incapacidad/@Cantidad, LicenciaMP, LicenciaR, LicenciaNR, Vacaciones)."
- **Fonte:** Anexo NE p.25, NIE069: "Número de días que el trabajador o aprendiz efectivamente estuvo ejecutando sus labores en la empresa"; p.180 NIE125: "Número de días que el trabajador o aprendiz estuvo inactivo por incapacidad (sin importar su origen)"; NIE130/134/138: "efectivamente estuvo inactivo por licencia…". O anexo separa dias trabalhados de dias inativos.

### NE-04 · valores negativos (Spec!Q211; Population Rules!C17)
- **Veredito:** CONFIRMADO muda · **Confiança 88%**
- **Decisão (EN):** "No monetary value may be negative, Redondeo (NIE186) included (rule VLR01, rejection). A downward difference for a past period is corrected with a NominaIndividualDeAjuste (Reemplazar) of that period, never with a negative amount."
- **Fonte:** Anexo NE p.9 §1.1.3.1: "Todos los valores monetarios deberán ser expresados en valores positivos. La naturaleza del signo negativo o positivo la otorga el concepto de campo, mas no está incluido en el valor. Se informa la generación de la regla VLR01."; p.182 VLR01 (R). DIAN, Concepto 014745 (int. 1793) de 28/10/2025, §15: "el DSNE no admite valores negativos, conforme al Concepto Unificado de Facturación Electrónica 0106 de 2022, numeral 4.2.4.15 (adicionado por el Oficio 908261 de 2022)" (https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_14745_2025.htm).
- O XSD tipa Redondeo como `xsd:decimal` (aceita sinal), mas a regra VLR01 e a doutrina valem acima do tipo.

### NE-10 · limite de 500 KB (File Structure!B7; Sample File!A33)
- **Veredito:** CONFIRMADO muda · **Confiança 85%**
- **Decisão (EN):** "Maximum 500 KB per XML document (rule ZA01, rejection: 'Tamaño del mensaje superior al límite establecido')."
- **Fonte:** Anexo NE §6.2.1, p.231: "ZA01 Verificar si el tamaño del archivo XML es superior a 500 KB R Tamaño del mensaje superior al límite establecido [Máximo: 500 KB]".

### NE-15 · FechaIngreso (Spec!M78)
- **Veredito:** CONFIRMADO não muda (acrescentar nota) · **Confiança 80%**
- **Decisão (EN):** manter "Constant across every document for that relationship" + nota: "The annex description says to fill it only in the hiring month, but the attribute is required (1-1, use='required' in XSD 1.0.6) and TiempoLaborado (NIE006, §8.4.1) is counted from it, so the hire date is sent in every document."
- **Fonte:** Anexo NE p.15, NIE002: "Este dato se debe diligenciar solamente en el registro del mes en que el trabajador o aprendiz presenta ingreso… | Periodo | 1-1 | Se debe indicar la Fecha de Ingreso del trabajador a la empresa"; XSD 1.0.6 l.50: `<xsd:attribute name="FechaIngreso" type="xsd:date" use="required" />`; NIE006 TiempoLaborado: "Cantidad de Tiempo que lleva laborando el Trabajador en la empresa … Definido en el numeral 8.4.1". Sem FAQ DIAN sobre o ponto (buscados oficios 902972/903367 de 2022: tratam de férias, não deste campo).

### NE-18 · tipo de incapacidade (Field Options!D68, D69)
- **Veredito:** CONFIRMADO muda (rotulagem) · **Confiança 65%**
- **Decisão (EN):** D68 "2 Profesional — interpretation: occupational disease ('enfermedad profesional', the pre-Ley 1562/2012 term for 'enfermedad laboral'); the annex gives no definition." D69 "3 Laboral — interpretation: occupational accident ('accidente de trabajo'); the annex gives no definition."
- **Fonte:** Anexo NE tabela 5.5.6, p.180: "1 Común 2 Profesional 3 Laboral" (sem definição). Busquei FAQ/caixa de ferramentas DIAN e oficios: nenhuma definição oficial. Rótulo marcado como interpretação.

### NE-05 · nomes do XSD — já CONFIRMADO e aplicado (rodada 2, `CONFERENCIA-DRAFTS-R2.md` linha 49). Sem ação.

## Formulários DIAN (CO-DIAN-002 / 004 / 005)

### F-06 · casilla 996 do Form. 350 (002)
- **Veredito:** CONFIRMADO muda · **Confiança 92%**
- **Decisão (EN):** "Casilla 996 — 'Espacio para el número interno de la DIAN / Adhesivo'. Display-only, not populated by payroll (same treatment as 997)."
- **Fonte:** Res. DIAN 31 de 29/02/2024 (prescreve o Form. 350, vigente desde 01/08/2024), anexo, p.1 rodapé: "996. Espacio para el número interno de la DIAN / Adhesivo"; instrutivo p.4: "996. Espacio para el número interno de la DIAN/Adhesivo. 997. Espacio exclusivo para el sello de la entidad recaudadora". (https://normograma.com/documentospdf/PDF/R_DIAN_0031_2024.pdf; https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0031_2024.htm). Nenhuma resolução nova prescreveu o 350 em 2026 (o comunicado DIAN de 10/07/2026 só habilitou ajustes de casillas 27/28/59).

### SIM-07 · casilla 59 / N33 (004 !A26/C26; 005 !C28)
- **Veredito:** CONFIRMADO muda — **já aplicado no DRAFT v1.1** (C26 e C28 = 13.000.000 com a conta) · **Confiança 75%**
- **Decisão (EN):** manter a derivação do DRAFT; acrescentar: "Composition of the six-month average (prima included) is our reading; neither ET art. 206 num. 4 nor DUR 1.2.1.22.5 lists which payments enter it."
- **Fonte:** Form. 220 (Res. 22/2024): "Ingreso laboral promedio de los últimos seis meses anteriores (numeral 4 art. 206 E.T.) 59"; DUR 1.2.1.22.5: "cuyo ingreso mensual promedio en los seis (6) últimos meses de vinculación laboral no exceda de 350 UVT". Conta: (6 × 12.000.000 + 6.000.000) ÷ 6 = 13.000.000.

## Cesantías (CO-CESANTIAS-006)

### F-11 (006) · regime da construção, CST 310 (Payroll Scope Summary!C49)
- **Veredito:** CONFIRMADO muda (texto) · **Confiança 88%**
- **Decisão (EN):** "Construction works (CST art. 310 a), art. 312): severance at three days' salary per complete month worked (vs. 30 days per year under CST art. 249), payable at termination for any cause. Since Corte Constitucional C-078/2023 there is no one-month minimum: it is recognised proportionally to the time actually worked. Same return record; only T14 changes."
- **Fonte:** CST art. 310 a) (Secretaría del Senado, com aparte tachado): "El auxilio de cesantía por todo el tiempo servido, a razón de tres (3) días de salario por cada mes completo de trabajo, ~~siempre que se haya servido siquiera un mes~~, y debe pagarse a la terminación del contrato por cualquier causa" (`2026-10-30-CST-pr010-SecretariaSenado.html` + notas `.js`). C-078/2023 (22/03/2023), Resuelve: "Primero. Declarar INEXEQUIBLE la expresión 'siempre que se haya servido siquiera un mes' contenida en el literal a) del artículo 310…"; síntese: "deberá entenderse que los trabajadores de la construcción tienen derecho a que las vacaciones y el auxilio de cesantía se les reconozca proporcionalmente por el tiempo efectivamente trabajado" (https://www.corteconstitucional.gov.co/relatoria/2023/C-078-23.htm).
- Ressalva: a sentença não decide se "3 dias por mês completo" se calcula pro rata dentro do mês; a leitura "proporcional" vem da própria síntese da Corte.

### F-10 (006) · citação do auxílio de transporte (Example Analysis!D5)
- **Veredito:** CONFIRMADO muda (citação) · **Confiança 92%**
- **Decisão (EN):** "SMMLV 2026 COP 1,750,905 — Decreto 1469 de 2025; transport allowance COP 249,095 — Decreto 1470 de 2025. Decreto 1469 was provisionally suspended (auto of 12-Feb-2026); Decreto 159 de 2026 then fixed the same 23% / COP 1,750,905 provisionally; the Consejo de Estado (Sección Segunda, auto of 9-Jul-2026, rad. 11001-03-25-000-2026-00004-00) revoked the suspension and voided the measure, so Decreto 1469 applies; the annulment case is still pending."
- **Fonte:**
  - Decreto 1469/2025 art. 1: "Fijar a partir del primero (1o) de enero de 2026 como Salario Mínimo Legal Mensual, la suma de UN MILLÓN SETECIENTOS CINCUENTA MIL NOVECIENTOS CINCO PESOS ($1.750.905)" (https://normativa.colpensiones.gov.co/colpensiones/compilacion/docs/decreto_1469_2025.htm).
  - Decreto 1470/2025 art. 1: "el auxilio de transporte … en la suma de DOSCIENTOS CUARENTA Y NUEVE MIL NOVENTA Y CINCO PESOS ($249.095)" (…/decreto_1470_2025.htm).
  - Auto CE de 09/07/2026, Resuelve: "Primero. REVOCAR el auto del doce (12) de febrero de dos mil veintiséis (2026), mediante el cual se decretó la suspensión provisional de los efectos del Decreto 1469 del 29 de diciembre de 2025 … Segundo. NEGAR la medida cautelar … Tercero. DEJAR SIN EFECTOS la medida cautelar innominada … y en consecuencia el acto que se dictó en cumplimiento de esta."; §84: "el Gobierno Nacional expidió el Decreto 159 de 2026 … resolvió fijar provisionalmente el incremento … en 23% y en un valor de $1.750.905".
- **Ressalva da fonte do auto:** a cópia oficial no SIDN (Rama Judicial) devolve 403 (WAF). Li a cópia integral publicada por Valora Analitik (PDF com cabeçalho e assinaturas eletrônicas do Consejo de Estado): `2026-10-30-CE-SeccionSegunda-auto-2026-07-09-Decreto-1469-copia-valoraanalitik.pdf`. Por isso 92%, não 100%.

## Payslip (v1.1-DRAFT)

### PS-06 · histórico do Decreto 1469 (Colombia (EN)!A83)
- **Veredito:** CONFIRMADO muda (data e forma) · **Confiança 92%**
- **Decisão (EN):** "Decreto 1469 de 2025 (SMMLV COP 1,750,905). Provisional suspension of 12-Feb-2026 revoked by the Consejo de Estado, Sección Segunda, auto of 9-Jul-2026 (rad. 11001-03-25-000-2026-00004-00); annulment case pending."
- **Fonte:** as de F-10 (006). A data "9-Jul-2026" do Payslip está certa (data do auto; a imprensa noticiou em 17/07).

### PS-11 · exoneração ET 114-1 (Colombia (EN)!A81)
- **Veredito:** CONFIRMADO muda · **Confiança 95%**
- **Decisão (EN):** "Exoneration under ET art. 114-1 (added by Ley 1819 de 2016 art. 65): companies and legal persons filing income tax, for workers earning individually less than 10 SMMLV — SENA, ICBF and employer health. Natural-person employers are exonerated only if they employ two or more workers."
- **Fonte:** ET art. 114-1: "<Artículo adicionado por el artículo 65 de la Ley 1819 de 2016> Estarán exoneradas del pago de los aportes parafiscales a favor del Servicio Nacional del Aprendizaje (SENA), del Instituto Colombiano de Bienestar Familiar (ICBF) y las cotizaciones al Régimen Contributivo de Salud, las sociedades y personas jurídicas y asimiladas contribuyentes declarantes del impuesto sobre la renta… Lo anterior no aplicará para personas naturales que empleen menos de dos trabajadores…" (`2026-10-22-ET-pr004-SecretariaSenado.html`). A origem Ley 1607/2012 (antigo art. 25) foi substituída; citar a 1819.

### PS-13 · IBC em tempo parcial e repetição (Population Range!C3, C9)
- **Veredito:** CONFIRMADO muda · **Confiança 88%**
- **Decisão (EN):** C3: "IBC floor 1 SMMLV (Ley 100 art. 18). Exception: dependent part-time worker hired for less than 30 days in the month and paid less than 1 SMMLV (Decreto 1072 art. 2.2.1.6.4.2) is reported as cotizante 51: pension and CCF IBC in quarters of SMMLV by days worked (1–7 = ¼, 8–14 = ½, 15–21 = ¾, 22–30 = 1); ARL IBC = 1 SMMLV for 30 days." C9: "No separate prima / cesantías / intereses lines (already included)."
- **Fonte:** Ley 100/1993 art. 18: "En ningún caso la base de cotización podrá ser inferior al monto del salario mínimo legal mensual vigente"; Decreto 1072 art. 2.2.1.6.4.2: "2. Que el contrato sea a tiempo parcial, es decir, que en un mismo mes, sea contratado por periodos inferiores a treinta (30) días. 3. Que el valor que resulte como remuneración en el mes, sea inferior a un (1) salario mínimo"; AT2 v30 p.117 (tipo 51): "Entre 1 y 7 días Un cuarto de un salario mínimo … Entre 22 y 30 días Un salario mínimo"; "'IBC Riesgos Laborales' debe ser igual a un salario mínimo legal mensual vigente". "Per full-time equivalent" não tem base.

## SIR (CO-SIR-001 v1.1)

### S-03 · juros de mora e sanção UGPP (Captura l.39)
- **Veredito:** CONFIRMADO muda · **Confiança 92%**
- **Decisão (PT, SIR):** "PILA: juros de mora à taxa do imposto de renda (Ley 100/1993 art. 23); sanções da UGPP por omissão, mora e inexatidão (Ley 1607/2012 art. 179, mod. Ley 1819/2016 art. 314; num. 3 mod. Ley 2010/2019 art. 121)."
- **Fonte:** Ley 100 art. 23: "Los aportes que no se consignen dentro de los plazos señalados para el efecto, generarán un interés moratorio a cargo del empleador, igual al que rige para el impuesto sobre la renta y complementarios." Ley 1607 art. 179: "<Artículo modificado por el artículo 314 de la Ley 1819 de 2016> La UGPP será la entidad competente para imponer las sanciones de que trata el presente artículo … 1. … sanción por no declarar equivalente al 5% del valor dejado de liquidar y pagar por cada mes o fracción de mes de retardo, sin que exceda el 100% … 2. … sanción equivalente al 35% de la diferencia…" (http://www.secretariasenado.gov.co/senado/basedoc/ley_1607_2012_pr004.html).

### S-04 · prazos PILA e juros das cesantías (Captura l.43, 48)
- **Veredito:** CONFIRMADO muda (citação; datas certas) · **Confiança 93%**
- **Decisão (PT, SIR):** "PILA: do 2º ao 16º dia útil pelos dois últimos dígitos do NIT/documento (00–07 = 2º … 94–99 = 16º), Decreto 780/2016 art. 3.2.2.1 (subst. Decreto 1990/2016 art. 2). Juros das cesantías (12% a.a.): pagos no mês de janeiro, ou na saída / liquidação parcial (Ley 52/1975 art. 1; Decreto 1072/2015 art. 2.2.1.3.4)."
- **Fonte:** Decreto 1990/2016 art. 2 (tabela com a coluna de dias): "Día hábil | 2o 00 al 07 | 3o 08 al 14 | … | 16o 94 al 99" (https://normativa.colpensiones.gov.co/colpensiones/compilacion/docs/decreto_1990_2016.htm). Decreto 1072 art. 2.2.1.3.4 (Decreto 116/1976 art. 1): "Los intereses de que trata el inciso anterior deberán pagarse en el mes de enero del año siguiente a aquel en que se causaron; o en la fecha de retiro del trabajador o dentro del mes siguiente a la liquidación parcial de cesantía".

### S-05 · formato do arquivo de cesantías (Captura l.34)
- **Veredito:** CONFIRMADO muda · **Confiança 85%**
- **Decisão (PT, SIR):** "Formato (TXT 258 posições / XLS / CSV) = regra de cada fundo de cesantías; não há esquema publicado pelo governo. A consignação anual não passa pela PILA (o AT2 v30 não tem registro de cesantías)."
- **Fonte:** AT2 v30 (busca por "cesant": só "Mecanismo de Protección al Cesante"); Ley 2466/2025 art. 64 par. 1 manda o MinSalud regulamentar a PILA só para a consignação **mensal antecipada** opcional ("el Ministerio de Salud y Protección Social hará las reglamentaciones correspondientes respecto de la Planilla Integrada…"), ainda não refletida no AT2 v30 nem na Res. 1529/2026.

### S-07 · contagem de regras NE (Captura l.33)
- **Veredito:** continua aberto · **Decisão provisória (PT):** trocar "433 regras: 406 R + 27 N" por "mais de 430 regras de validação (R = rechazo, N = notificación), Anexo NE §6" · **Confiança na decisão 80%**
- **O que fiz:** contei IDs com marcador R/N no texto do anexo: §6.1.1 NominaIndividual 198 (189 R, 9 N); §6.1.2 Ajuste 239 (219 R, 20 N); §6.1.3 Firma 56; §6.2 Conexión 23. A extração de tabela por texto é ruidosa (IDs e marcadores em linhas soltas) e não reproduz 433/406/27 por nenhum recorte. Fechar só com a planilha de regras da caixa de ferramentas DIAN ou leitura da tabela no PDF.

---

## Bloco de prova
- **Pedido → resposta:** 27 itens do lote (todos os não-CCG/não-WTC do PENDENTES, incluindo os 4 do SIR e as 2 linhas quebradas DD-08/NE-05) — cada um com veredito, decisão, trecho literal, fonte e confiança.
- **Fontes novas gravadas (`raw/docs/oficiais/CO/`):** `2026-10-30-DIAN-Oficio-14745-2025-valores-negativos-DSNE.htm`, `2026-10-30-Ley-2466-2025-FuncionPublica.html`, `2026-10-30-Res-MSPS-2064-2025-cancilleria.htm`, `2026-10-30-CST-pr010-SecretariaSenado.html` (+ `-notas.js`), `2026-10-30-CorteConstitucional-C-078-2023-CST310.htm`, `2026-10-30-Decreto-1469-2025-Colpensiones.htm`, `2026-10-30-Decreto-1470-2025-Colpensiones.htm`, `2026-10-30-CE-SeccionSegunda-auto-2026-07-09-Decreto-1469-copia-valoraanalitik.pdf` (+ `.txt`), `2026-10-30-Res-DIAN-0031-2024-Form350-*.pdf/.txt`, `2026-10-30-Res-DIAN-0022-2024-Form220-com-anexo-normograma.pdf/.txt`, `2026-10-30-Ley-1607-2012-pr004-art179-SecretariaSenado.html`, `2026-10-30-Decreto-1990-2016-Colpensiones.htm`, `2026-10-30-Decreto-116-1976-FuncionPublica.html`.
- **Teste mecânico:** XSD 1.0.6 conferido para FechaIngreso (required) e Redondeo (decimal); conta SIM-07 refeita (78.000.000 ÷ 6 = 13.000.000); tabela de dias PILA conferida contra o Decreto 1990/2016 (15 faixas = 2º a 16º dia).
- **Confiança média do lote:** ~86%. Abaixo de 80%: P-06 (operador), DD-21 (classificação nossa), NE-18 (sem definição oficial), SIM-07 (composição da média), S-07 (aberto).
