# Resíduos do Test 0: decisões (30/10/2026)

Ligado a [[TEST0]], [[RELEASE-CROSSCHECK]] e [[CONFERENCIA]]. Instrução do usuário (30/10): ponto estatutário aberto não volta para ele; decidir com fonte primária e confiança.

**Método:** as edições estão declaradas em `final/scripts/residuos_corrections.py` e foram fundidas em `release_edits.py`, como no Test 0. Depois rodei `release.py` (cirurgia XML, sem openpyxl.save) e `release_crosscheck.py`. O cross-check aceita agora a operação `formula`, usada no Payslip H36. Também rodei `build_changelogs.py`, que acrescentou a seção "Post-release review 2026-10-30" em cada changelog. Mesma versão e mesma data de emissão.

## Resumo

| ID | Veredito | Decisão | Aplicado em | Confiança |
|---|---|---|---|---|
| T0-09 | Procede | Auxílio-nascimento e auxílio-casamento por mera liberalidade: "Non-Salary - non-remunerative"; Q/R/S/U = No; observação reescrita | WTC Q:V228:229, AB228, D229 | 85% |
| T0-10 (175–176) | Procede | Copiar 173–174: Salary, todas as bases Yes; AB vazio | WTC Q:X175:176, AB175:176 | 95% |
| T0-10 (carro: 201–206, 214–216) | Procede, com ajuste | Uma natureza por conceito: "Non-Salary - pacted" (regra do próprio WTC para natureza incerta), Yes/No; variante "meio de transporte" documentada em AB; Y = AuxilioNS/AuxilioS conforme o pacto | WTC V, Q:X, Y, AB | 80% |
| T0-10 (217, 226) | Procede | Reembolso ou meio de trabalho: Q/R/S/U = No, igual às linhas 218–225; AB reescrito | WTC Q:U, AB | 85% |
| T0-10 (267) | Procede | Bônus contratual (é salário salvo pacto): "Non-Salary - pacted" | WTC V267 | 90% |
| T0-11 | Procede | U260–U264 = Yes/No, igual às linhas 255–259 | WTC U260:U264 | 95% |
| T0-18 | Não procede (refinado) | Mantido o arredondamento para o múltiplo de 100 acima, agora feito separadamente nos campos 51 e 52 da PILA; o valor não muda (192.000) | Payslip H36 EN/ES (fórmula) | 85% |
| T0-20 | Procede | Ressalva: os 72 UVT só valem na declaração anual | DD W46 | 95% |
| T0-21 | Procede | O teste de 40% só vale com pacto escrito do art. 128; o bônus por mera liberalidade fica fora | NE M135 | 90% |
| C1 | Procede | Período que cruza dois anos: residente a partir do 2º ano | CCG, 4 parágrafos | 95% |
| C2 | Procede | O 184º dia é 31/12/2026, não "por volta de 30/12" | CCG, Exemplo 3 | 99% |
| C3 | Procede | "CST Art. 236A" não existe: o certo é o art. 236 par. 2 (Ley 2114/2021 art. 2) | Payslip A84 EN/ES, Population Range C7 | 95% |
| C4 | Não procede | 4% / 10% / 12% a partir de 2024 confere | sem mudança | 95% |
| C5 | Não procede | Auxílio de transporte integral para meio período confere | sem mudança | 85% |
| C6 | Não procede | NIT final 6 → 12º dia útil confere | sem mudança | 98% |
| C7 | Procede (base) | Parafiscais = No mantido; fundamento completado com o CE 23856/2021 | WTC D123 | 85% |

**Aberto:** nenhum ponto ficou sem decisão de fonte oficial.

## Detalhe por item

### T0-09: WTC 228–229, auxílio-nascimento e auxílio-casamento
- **Fonte:** CST art. 128, cópia local `raw/docs/oficiais/CO/2026-10-22-CST-pr004-SecretariaSenado.html` (http://www.secretariasenado.gov.co/senado/basedoc/codigo_sustantivo_trabajo_pr004.html, baixada em 22/10/2026): *"No constituyen salario las sumas que ocasionalmente y por mera liberalidad recibe el trabajador del empleador, como primas, bonificaciones o gratificaciones ocasionales…"*.
- **Fonte:** CE Sección Cuarta, SU 25185 de 9/12/2021, ficha local `2026-10-22-CE-S4-SU-25185-2021-ficha.pdf`.
  - Regra 1: *"El IBC de aportes … únicamente lo componen los factores constitutivos de salario, en los términos del artículo 127 del CST"*.
  - Regra 3: *"El pacto de 'desalarización' no puede exceder el límite previsto en el artículo 30 de la Ley 1393 de 2010"*.
- **Decisão:** a coluna F diz "mera liberalidad" e AB228 diz "granted at the employer's discretion". Pela lei, isso não é salário, então o pagamento fica fora do IBC e do teste de 40%. A observação do AB indica "pacted" quando o pagamento é devido por convenção ou contrato.

### T0-10: linhas 175–176, 201–217, 226 e 267
- **175–176** (atrasado e ajuste do auxílio de expatriado): a linha-base (173–174) é Salary.
  - CST art. 127: *"…cualquiera que sea la forma o denominación que se adopte"*.
  - O atrasado e o ajuste têm a natureza do pagamento que corrigem.
- **Família do carro** (201–206, 214–216). F é igual em todas: "Cash car / fuel / maintenance allowance per contract".
  - Pelo CST art. 128, não é salário o que se recebe *"para desempeñar a cabalidad sus funciones, como gastos de representación, medios de transporte…"*. Já o auxílio contratual fixo, sem ligação com o deslocamento a trabalho, é salário (art. 127), salvo pacto.
  - O próprio WTC (cabeçalho V1) manda: *"Where the nature is unclear the row is 'pacted' and the DD non-salary pact flag decides"*.
  - Antes, a família estava dividida: 203–205 = Salary e o resto = non-remunerative com Yes/No, o que é contraditório. Unifiquei em "pacted": sem pacto, o motor trata como salário, então não há perda de contribuição.
  - O caso "só para deslocamento a trabalho" ficou documentado em AB (non-remunerative, Q:U = No).
  - Y passou para AuxilioNS/AuxilioS conforme o pacto. O cabeçalho V diz que os dois valores NS vão para o elemento NS.
- **217 e 226** (mudança): F diz "Genuine reimbursement … or an amount given to enable the work".
  - Pelo CST art. 128 e pela regra 1 da SU 25185, é não salarial por natureza.
  - CE 25907/2022 (já aprovado em T4-5): *"si el pago no es salario porque no retribuye el servicio, no integrará el IBC y no está sometido a límite legal alguno"*.
  - Q:U = No, igual às linhas irmãs 218–225.
- **267** (prêmio de reconhecimento): F diz *"SALARY where habitual, non-salary only under an express written CST art. 128 pact"*. Essa é exatamente a definição de "pacted".

### T0-11: WTC U260–U264
- **Fonte:** Ley 1393/2010 art. 30, local `2026-10-21-Ley-1393-2010-SecretariaSenado.html`: o limite vale *"para los efectos relacionados con los artículos 18 y 204 de la Ley 100"*, ou seja, pensão e saúde.
- **Decisão:** pensão, como saúde, entra só no excesso sobre os 40%, então Yes/No, igual às linhas 255–259.

### T0-18: Payslip H36 (FSP)
- **Fonte:** Decreto 780/2016 art. 3.2.1.5, com a redação do Decreto 1990/2016 art. 1. Local `2026-10-30-Decreto-1990-2016-Colpensiones.htm`: *"2. El valor de los aportes liquidados por cada cotizante … deberá aproximarse al múltiplo de 100 superior más cercano"*.
- **Fonte:** AT2 v30, campo 51, local `2026-10-29-MinSalud-AT2-v30-2026-07-24-PILA-activos.txt`: *"…multiplicar el valor del campo '42 – IBC Pensión' … por 0.5% … El valor incluido en este campo debe cumplir las reglas de redondeo o aproximación para las cotizaciones"*. O campo 52 (subsistência) recebe o restante.
- **Decisão:** o FSP é só do empregado e é pago pelo valor da PILA. Por isso o desconto continua arredondado para o múltiplo de 100 acima, e não ao peso, como propunha o revisor.
  - Refinei o arredondamento: agora é feito por subconta, `ROUNDUP(0,5%)+ROUNDUP(0,5%)`.
  - Valor do exemplo: 192.000 (sem mudança).
- **Ressalva:** a fórmula usa 1% fixo, porque o exemplo está abaixo de 16 SMMLV.

### T0-20: DD W46
- **Fonte:** DIAN Concepto 011383/2024, IV.2, local `2026-10-30-DIAN-Oficio-11383-2024-dependientes-retencion.htm` (decisão A-08 já aprovada e aplicada no CCG e no WTC).
- **Decisão:** a ressalva entrou em W46.

### T0-21: NE M135
- **Fonte:** SU 25185, regra 3 (acima), e CST art. 128.
- **Decisão:** o bônus entra no limite de 40% só com pacto escrito do art. 128. O bônus ocasional por mera liberalidade fica fora (mesma linha de T4-5).

### C1: residência quando o período cruza dois anos
- **Fonte:** ET art. 10 num. 1, baixado hoje em `raw/docs/oficiais/CO/2026-10-30-ET-pr001-art10-SecretariaSenado.html` (http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario.html, 30/10/2026): *"…cuando la permanencia continúa o discontinúa en el país recaiga sobre más de un año o periodo gravable, se considerará que la persona es residente a partir del segundo año o periodo gravable."*
- **Fonte:** DIAN Concepto 011108 de 29/06/2026, item 13, local: *"…que cubra dos años calendario, la residencia fiscal se adquiere desde el segundo año de acuerdo con lo previsto en el numeral 1 del artículo 10 del E.T."*
- **Por que muda:** "o ano em que cai o 183º dia" diverge da lei no limite. Exemplo: com entrada em 2/7, o 183º dia é 31/12, mas os 183 dias só são superados em 1/1 do ano seguinte.
- **Onde:** 4 parágrafos do CCG (tabela do Módulo 2.2, teste de residência do Módulo 3, FAQ de rendimentos anteriores à chegada e requisitos de configuração). O P6894 já estava certo.

### C2: Exemplo 3 do CCG
- **Fonte:** ET art. 10 num. 1, *"incluyendo días de entrada y salida del país"*.
- **Conta:** entrada em 1/7/2026; 1/7 a 31/12 = 31+31+30+31+30+31 = 184 dias. Portanto o 184º dia é 31/12/2026, não "on or about 30 December".

### C3: CST "236A"
- **Fonte:** CST, local `2026-10-22-CST-pr007-SecretariaSenado.html`. Entre o art. 236 e o art. 237 não existe art. 236A. O art. 236 traz a nota *"<Artículo modificado por el artículo 2 de la Ley 2114 de 2021>"* e diz: *"PARÁGRAFO 2o. El padre tendrá derecho a dos (2) semanas de licencia remunerada de paternidad."*
- **Ley 2466/2025:** sem ocorrência de "patern" no texto local, então a reforma não mudou esse ponto.

### C4: saúde do pensionista (CCG P2999) — confere
- **Fonte:** Res. MSPS 1271/2023 art. 1, local `2026-10-21-Res-MSPS-1271-2023-colpensiones.htm`: *"5. A partir del año 2024 … 1 SMLMV 4% / >1 SMLMV y hasta 3 SMLMV 10% / >3 SMLMV 12%"*.
- **Fonte:** AT3 v15 de 24/07/2026, local: o período *"1 de enero de 2020 a la fecha"* mantém 4% / 10% / 12%.
- **Nota:** a lei (Ley 2294/2023 art. 78) fala em *"entre 2 y 3 salarios mínimos"*. A faixa >1 a 2 SMMLV já era de 10% desde 2020 pela própria resolução.

### C5: auxílio de transporte integral no meio período (CCG P7157) — confere
- **Fonte:** Ley 15/1959 art. 2 par.: *"se pagará exclusivamente por los días trabajados"*. Paga-se por dia trabalhado, não por hora.
- **Fonte:** Función Pública, Concepto 247751 de 14/07/2021, baixado hoje em `2026-10-30-FuncionPublica-Concepto-247751-2021-auxilio-transporte-medio-tiempo.pdf` (https://www.funcionpublica.gov.co/eva/gestornormativo/norma_pdf.php?i=169409): *"ni la normativa o la jurisprudencia citada excluyen a los trabajadores de medio tiempo … el trabajador de medio tiempo sí tienen derecho a percibir el auxilio de transporte"*. O conceito cita no mesmo sentido os conceitos MinTrabajo 4093/2006 e 257/2020.
- **No exemplo:** 900.000 está abaixo de 2 SMMLV. Mesmo pelo critério do DAFP (remuneração equivalente em tempo integral: 900.000 × 42/20 = 1.890.000), continua abaixo do limite.
- **Por que 85%:** o conceito é do DAFP, para servidores públicos; não localizei um conceito do MinTrabajo em fonte oficial.

### C6: vencimento do Form. 350 para NIT final 6 — confere
- **Fonte:** DUR 1625/2016 art. 1.6.1.13.2.33, substituído pelo Decreto 2229/2023 art. 1, local `2026-10-13-DUR-1625-2016-DIAN.htm`: *"6 Décimo segundo día hábil"*, plazo *"abril de 2024 y en adelante para cada año subsiguiente"*.

### C7: WTC linha 123, parafiscais sobre o complemento de incapacidade
- **Fonte:** CE Sección Cuarta, 19/08/2021, rad. 25000-23-37-000-2015-00353-01 (23856). Texto integral em cópia de terceiro (PwC), local `2026-10-22-CE-Seccion4-23856-2021-copia-actualicese.pdf`: *"Comoquiera que el auxilio que recibe el trabajador incapacitado, en los términos de la ley laboral, no constituye salario, es claro que tampoco integra la nómina mensual de salarios y, en consecuencia, se excluye de la base para calcular los aportes con destino al SENA, ICBF y CCF."*
- **Decisão:** parafiscais = No mantido. O D123 deixou de ser "interpretação a confirmar com a UGPP" e passou a citar o CE.
- **Por que 85%:** a cópia oficial do CE não foi localizada na web; o texto lido é integral, com rad. e data. Além disso, a UGPP (ABC 2025) orienta o contrário, e isso continua dito na nota.

## Fora do pedido (não incluí)
- WTC coluna Y das linhas "pacted" de educação (255–264) e de outras: aponta "AuxilioS (NIE141)", enquanto o cabeçalho V diz que "pacted" vai para o elemento NS. É o mesmo ajuste feito na família do carro. Vai para Pendências do hub.

## Bloco de prova
- **Pedido → resposta:**
  - T0-09, T0-10, T0-11, T0-18, T0-20 e T0-21: decididos.
  - C1–C7: decididos (4 com mudança, 3 confirmados).
  - Aplicado nos finais com o mesmo método.
  - Changelogs com a seção "Post-release review 2026-10-30".
  - MD5 atualizado.
- **Fontes:** citadas acima, com trecho literal; todas lidas por mim no arquivo local. Baixadas hoje (30/10): ET art. 10 e o Concepto DAFP 247751/2021.
- **Teste:**
  - `release_crosscheck.py`: PASS, 0 falhas; WTC com 109 edições declaradas conferidas; 2 edições de fórmula conferidas no Payslip.
  - `validate_workbook`: PASS nos 10 xlsx.
  - `validate.py` do docx com `--original` (DRAFT): PASS.
  - Antes de mexer, rodei `release.py` sem mudanças e os md5 bateram, o que confirma que o script é determinístico.
- **Confiança:** varia de 80% a 99% por item (tabela acima). A menor é a da família do carro (80%): a natureza real depende do contrato do cliente, e o padrão "pacted" + nota é a posição mais defensável.
- **Não tocados:** Drive, `~/mercans-pipeline`, `final/design/`, `final/simulations/`.
