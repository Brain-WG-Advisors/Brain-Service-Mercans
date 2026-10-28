# Sodra — SAM v07: instrução de preenchimento e estrutura MXFD (lidos em 2026-10-27 pelo navegador; sodra.lt bloqueia script)

## Página do SAM
- https://sodra.lt/formos-ir-sablonai/sam-pranesimo-pildymas-ir-pateikimas — "Atnaujinimo data: 2026 m. gegužės 11 d."
- Texto: "SAM pranešimas apie priskaičiuotus atlyginimus ir įmokas „Sodrai“. Už einamąjį mėnesį SAM pranešimą reikia pateikti iki kito mėnesio 15 d."
- Downloads: PDF `/wp-content/uploads/2025/07/sam-pdf.pdf`; ZIP `/wp-content/uploads/2026/02/SAM-v07.zip`; MXFD `/wp-content/uploads/2025/07/sam-v07.mxfd` (lido em memória no navegador, 2.303.961 bytes; não salvo em disco).
- "Bendrosios SD pranešimų teikimo nuostatos" → e-tar TAR.34A6775CE75B (regras gerais dos SD; não lidas).

## Instrução (sodra.lt/…/sam-pranesimo-pateikimas-ir-pildymas, "Atnaujinimo data: 2025 m. liepos 31 d."), pontos literais
- 48: mensalmente, SAM + anexos: 48.1 **SAM3SD** "apie apdraustųjų (be atleistųjų) valstybinio socialinio draudimo įmokas"; 48.2 **SAM3SDP** "apie apdraustųjų valstybinio socialinio draudimo laikotarpius ir įmokas".
- 49: pode não entregar se no período não havia contribuições a calcular para nenhum segurado (exceto quem teve 2-SD no mês) e foram entregues 9-SD e/ou 12-SD para todo o período. 49.1: um SAM com categorias/tarifas diferentes, ou SAM separado para parte dos segurados.
- 50: não se entrega SAM sobre estagiários (praktikantai), clérigos e oficiais.
- 51.1: SAM3SD = todos os segurados (sem os que tiveram 2-SD no mês): renda do mês sobre a qual se calculam contribuições e as contribuições.
- 51.2: SAM3SDP = períodos/dias concretos, códigos de motivo 01–10 (01 compensação a ex-servidores; 02 militares voluntários/reserva; 03 reabilitação; 04 conselheiros municipais até 2021-12-31; 05 cursos de oficiais; 06 gestores de pequenas sociedades por contrato civil; 07 peritos/participantes de processo; 08 outros pagamentos por pagador sem vínculo de trabalho; 09 cargos eletivos com PSD; 10 cargos eletivos sem PSD).
- 51.4: férias que passam de um mês para outro: valores e contribuições repartidos por mês de competência no SAM3SD. 51.5: não é obrigatório corrigir quando as férias prorrogadas por doença não são recalculadas.
- 51.6: prêmios, auxílios e outros pagamentos são informados no SAM3SD no período em que foram calculados (apskaičiuotos).
- 51.7: salário determinado por comissão/tribunal: no período a que se refere; se indeterminável, rateado por mês proporcional aos dias úteis (semana de 5 dias).
- 52: entrega "iki kito kalendorinio mėnesio 15 dienos".
- 53: ordem de preenchimento: dados dos pontos 13.2–13.9 (regras gerais); P14 e P17 (ano e mês); anexos; conclusão.
- 54: SAM principal: P20.1/P21.1 "x" se há SAM3SD/SAM3SDP; P20.2/P21.2 nº de folhas; P23 total de folhas; P20.3/P21.3 nº de segurados; P20.4/P21.4 soma da renda; P20.5/P21.5 soma das contribuições.
- 55 (SAM3SD): A11 renda do mês sobre a qual se calculam contribuições, em euros com centavos, **exceto** renda de esporte/artista, direitos autorais, e tantiemas/remuneração de conselhos e comitê de crédito; A12 contribuições calculadas com a tarifa do P3 sobre o A11; P7 soma dos A11 da folha; P8 soma dos A12 da folha; **P3 = tarifa total aplicada ao segurado no início do mês**.
- 56 (SAM3SDP): A5 código do motivo; A6 motivo; A21 início e A22 fim do período no mês; A11 renda do período (exceto esporte/artista/autoral); A12 contribuições; P7/P8 somas da folha; P3 tarifa total do período.

## Estrutura MXFD sam-v07 (FormDef criado 2021-12-22; FFDataCollectServer draudejai.sodra.lt/AuthServiceWS)
- Página **SAM** (FormCode "SAM", FormVersion "07"): InsurerName (68), InsurerCode (7, num), JuridicalPersonCode (9, num), InsurerPhone (15), InsurerAddress (68), DocDate (data), DocNumber (16), CycleYear (4; 2010–2099), CycleMonth (2; 1–12), RevisedDocument (checkmark "Patikslintas pranešimas"), RevisedCycleYear (4), RevisedCycleMonth (2), Appendixes2 (checkmark SAM3SD), Apdx2PageCount (4), Apdx2PersonCount (5), Apdx2InsIncomeSum (12, 2 dec), Apdx2PaymentSum (12, 2 dec), Appendixes3 (checkmark SAM3SDP), Apdx3PageCount, Apdx3PersonCount, Apdx3InsIncomeSum, Apdx3PaymentSum, ApdxPageCountTotal (4), ManagerFullName (68), PreparatorDetails (68).
- Página **SAM3SD** (FormVersion "07"), **6 linhas por folha** (_1…_6): RowNumber (5), PersonCode (11, num), InsuranceSeries (2, texto) + InsuranceNumber (7, num) = nº do seguro social, InsIncomeSum (11, 2 dec), **TaxRate (5, 2 dec, "Bendras tarifas")**, PaymentSum (11, 2 dec), PersonFirstName (68), PersonLastName (68); rodapé: InsIncomePage, PaymentPage, InsurerCode, PageNumber, PageTotal, DocDate, DocNumber.
- Página **SAM3SDP** (FormVersion "07"), **3 linhas por folha**: RowNumber, PersonCode, InsuranceSeries, InsuranceNumber, PersonFirstName, PersonLastName, PeriodStartDate, PeriodEndDate, InsIncomeSum, TaxRate, PaymentSum, ReasonCode (2; lista 01–10), ReasonText (65); rodapé igual ao SAM3SD.
- Nenhum campo separa a contribuição do empregado e a do empregador, nem traz grupo de acidentes, tipo de contrato ou PSD em separado: só renda, **tarifa total** e contribuição total por segurado.
