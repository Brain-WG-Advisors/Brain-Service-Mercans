# Rodada 6: confiança por ponto, fontes reabertas por mim (02/11/2026)

Ligado a [[PLANO-92]], [[LOTE-A-R6]], [[LOTE-B-R6]], [[LOTE-C-R6]] e [[CONFERENCIA]]. Regra: ≥ 92% com a fonte primária reaberta por mim.

## Lote A (retenção)

| # | Ponto | Decisão | Muda artefato? | Confiança | Fonte que reabri (trecho) |
|---|---|---|---|---|---|
| 1 | A-2 cesantías sem retenção, inclusive de não residente | Sem retenção na fonte para qualquer pagador e qualquer beneficiário; a tributação (ET 206 num. 4) é feita na declaração, se o empregado for obrigado a declarar | Valor não. Texto opcional: tirar "(an interpretation)" de CCG T150R3C2 e da spec 004 (Report Matrix A34; Example Analysis D34) | **92%** (antes 80%) | C-397/1994 RESUELVE: "DECLARAR INEXEQUIBLE la expresión 'por parte de la Nación'" → Ley 100 art. 135 par. 3 vale para todos: "En ningún caso los pagos efectuados por concepto de cesantía serán sujetos de retención en la fuente". DUR 1.2.4.1.11: "en ningún caso … cesantías o intereses sobre las mismas, estarán sujetos a retención en la fuente". DIAN 57622/2003: "por expreso mandato legal … en ningún caso estos pagos están sometidos a retención en la fuente … si el beneficiario es declarante debe liquidarse el impuesto". |
| 2 | NE-18 tipo de incapacidade (códigos 2/3) | Fica como interpretação configurável. Rascunho de consulta formal à DIAN em [[LOTE-A-R6]] §2.5 (não enviado) | Não | **75%: fora do alcance** | Nenhuma fonte oficial define os códigos: anexo NE, XSD, Oficio 901708/2022 e PR-TAH-0352, segundo o agente. Só a DIAN fecha. |
| 3 | SIM-07 casilla 59 = 12.000.000 | Confirmado | Não (já na spec 004/005 v1.2) | **93%** | DIAN Concepto 1302/2019: "(ii) cuando la relación laboral … no ha finalizado … los seis meses del año inmediatamente anterior del momento en que las cesantías se consignan"; o ingresso conta só o que o empregado recebe "como contraprestación directa del servicio". |
| 4 | A-1 tetos 790/1.340/3.800 UVT anuais | Anuais, controlados pelo acumulado do ano, sem 1/12 | Não (já no CCG v1.6/WTC v1.8) | **92%** | ET 206 num. 10: "limitada anualmente a setecientos noventa (790) UVT"; ET 336 num. 3 e Decreto 2231/2023: "(1.340) UVT anuales"; CE 24047 FALLA: "ANULAR el aparte 'es decir cuatrocientos veinte (420) … UVT mensuales'"; DIAN 11383/2024 IV.1: o agente de retenção deve observar "su límite anual en los pagos realizados a cada persona natural". Ressalva: a sentença diz que o 1/12 "armoniza" a retenção com o período mensal; quem aplica 1/12 só retém a mais. |

A-2: a confiança subiu porque a regra é de lei expressa ("en ningún caso") e a C-397 a estendeu a qualquer pagador. O argumento contrário (Concepto 577/2020: a retenção do não residente "no admite depuración") trata da base de pagamentos sujeitos a retenção, não de um pagamento que a lei exclui da retenção.

## Lote B (seguridade)

| # | Ponto | Decisão | Muda artefato? | Confiança | O que reabri |
|---|---|---|---|---|---|
| 5 | P-06 tarifa ARL em decimal | Decimal com ponto (classe I = 0.0052200), igual às outras tarifas | Não (PILA-003 já está assim) | **92%** | AT2 v30, saída ARL, campo 28: "Tarifa. En decimales. El registrado en el campo 61"; AT3 v15 §2.2.2.25: "el valor del campo debe ser en decimal … por ejemplo 2.0% sería 0.02000". |
| 6a | D5 parafiscais sobre **incapacidade** = No | Mantido No | Não | **92%** | CE S4 23856/2021: "el auxilio que recibe el trabajador incapacitado … no constituye salario … se excluye de la base para calcular los aportes con destino al SENA, ICBF y CCF". SU 25185 (ficha): a UGPP liquidou "sin que se hubieran tenido en cuenta las incapacidades". Contra: UGPP ABC 2025 p. 7 manda incluir "incapacidades y/o licencia de maternidad o paternidad", mas a tabela da p. 6 do mesmo guia põe as novedades só na coluna da seguridade social. É guia sem força normativa e cede à Seção Quarta. |
| 6b | D5 parafiscais sobre **licenças** (maternidade/paternidade/parental/cuidado) | No (fora de SENA/ICBF/CCF). Parental flexível: as horas trabalhadas são salário comum (Yes) | Não (WTC T330–T333 já = No). Texto opcional: nota T330 ([[LOTE-B2-D5-LICENCAS]]) | **92%** (antes 86%) | Superintendência do Subsídio Familiar, Concepto 2-2018-083606: "Como quiera que su pago no lo realiza el empleador sino la EPS … no se pagan aportes parafiscales sobre ella". Ley 1822/2017 art. 1: o novo CST 236 fala em "licencia … remunerada con el salario" (sai "descanso remunerado"). Cuidado da niñez: Res. MSPS 467/2025 a reporta na mesma novedad IGE da incapacidade (campo 25 = "L"), mesmo regime que a 6a. Para 100%: sentença CE S4 19736/2016 no SAMAI (captcha). |
| 7 | Incapacidade dos dias 1–2: 66,67% e piso de 1 SMMLV | Confirmado: 2/3, com piso do salário mínimo proporcional aos dias | Valor não. Texto opcional: CCG P905 (piso pela C-543, não por "market practice") e WTC Employer Sick Pay A35–A39/A57/C16 (fechar OPEN ITEM 1 e 2) | **93%** | C-543/2007: o auxílio "no podrá ser inferior al salario mínimo legal vigente". Segundo o agente: Decreto 780 art. 3.2.1.10 par. 1, CST 227 e MinSalud 2024116001238451. |
| 8 | Res. 2708/2026 | Confirmada: arts. 1, 5.4, 8 e 10; revoga a Circular 0101/2025 sem substituí-la | Não (CCG v1.6 certo) | **93%** | Resposta da Ministra à Câmara (14/09/2026), item 10: "Circular Externa 0101 … Defecto identificado y fundamento de la derogatoria". |
| 9 | SMMLV 2026: instrumento | Citar o Decreto 1469/2025 art. 1 (COP 1.750.905) | Valor não. Texto opcional: CCG P297 ("0159 spent" → "left without effect"); hub l. 48/78/121 | **94%** | Auto do CE de 9/7/2026, RESUELVE: "Primero. REVOCAR el auto del doce (12) de febrero … suspensión provisional de los efectos del Decreto 1469"; "Segundo. NEGAR la medida cautelar"; "Tercero. DEJAR SIN EFECTOS la medida cautelar innominada … y en consecuencia el acto que se dictó en cumplimiento de esta" (o Decreto 0159). |
## Lote C (NE e prestações)

| # | Ponto | Decisão | Muda artefato? | Confiança | O que reabri |
|---|---|---|---|---|---|
| 10 | S-07, 519 regras da NE | Confirmado: 519 = 486 R + 31 N + 2 sem marcação; nómina 437 (198 + 239) | Não (o SIR v1.3 já tem esse texto) | **97%** | Rodei `scripts/contar_regras_ne.py` no Anexo NE v1.0 (md5 f848b528…). Saída: geral 3, NominaIndividual 198 (189/9), Ajuste 239 (219/20), Signature 56 (54/0/2), Conexão 23 (21/2), total 519. |
| 11 | WTC coluna Y (AuxilioNS/AuxilioS) | Certo no v1.8 nas linhas 255–264, 124–133, 114–116 e V1 | Valor não. Texto opcional: as linhas "pacted" 230–237, 253–254 e 348–350 só citam AuxilioNS, sem "otherwise AuxilioS"; 267, 347 e 351 listam S/NS sem condição | **95%** (90% nas linhas 114–116, escolha nossa entre BonificacionS e ConceptoS) | WTC v1.8: Y255 "AuxilioNS, NIE142, where non-salary under the pact; otherw…"; Y230 "AuxilioNS, NIE142" sem o senão. |
| 12 | DD-21 dados bancários | A lista 42/45/47/98 está certa; as regras NIE066–068 são N (só notificam) | Opcional: incluir o código 46 no mapper | **93%** | Anexo NE v1.0, NIE066–068: "Pago 0-1 Si el método de pago se realiza de forma bancaria"; tabela 5.3.3.1 tem "46 Transferencia Débito Interbancario". |
| 13 | D9 férias compensadas | Fora de saúde, pensão, ARL e FSP. **Dentro** de SENA, ICBF e CCF (corrige a premissa do plano) | Não: o WTC já tem T = Yes (linhas 156 e 324). Texto opcional: nota D156/D324 ("no express Supreme Court ruling located") | **94%** | UGPP ABC 2025 p. 7: "para liquidar la base de cotización del sistema de parafiscales (caja de compensación familiar, SENA e ICBF), debe tener en cuenta el valor reconocido … por las vacaciones disfrutadas, compensadas en dinero o pagadas en la liquidación del contrato." WTC v1.8: T156 = Yes e T324 = Yes. |
| 14 | Auxílio de carro / rodamiento | Decide a finalidade: (a) para o serviço = não salarial e fora dos 40%; (b) retribuição = salário; (c) benefício pactado = "pacted", dentro dos 40% | Valor não; texto opcional na primeira frase da nota AB | **92%** | CSJ SL5159-2018: não são salário as somas entregues "no para su beneficio personal … sino para desempeñar a cabalidad sus funciones, tales como … medios de transporte". WTC Y201 conferido. |

Fora do pedido (Lote C): nas linhas "pacted" do WTC, W e T ficam fixos em No. Sem pacto válido, deveriam virar Yes. Confirmar se é o engine ou o DD que faz essa troca.

## Fechamento (02/11)
- **Todos os pontos ≥ 92%, menos NE-18 (75%).** O NE-18 só a DIAN fecha: fica configurável, com rascunho de consulta em [[LOTE-A-R6]] §2.5 (envio só com ok).
- **Nenhum valor muda nos finais.** Os ajustes opcionais são só de texto:
  - CCG T150R3C2, P297, P905 e spec 004 A34/D34 (sem "an interpretation");
  - WTC: "senão AuxilioS" nas linhas 230–237, 253–254 e 348–350, notas AB, D156/D324, D123/D330, T330 e Employer Sick Pay;
  - DD: código 46 no mapper.
- **SIR v1.4** (seções 0/2): [[SIR-R6-secoes-0-2]].
- **Fora do pedido:** colunas W/T fixas em No nas linhas "pacted" sem pacto válido (engine/DD).
