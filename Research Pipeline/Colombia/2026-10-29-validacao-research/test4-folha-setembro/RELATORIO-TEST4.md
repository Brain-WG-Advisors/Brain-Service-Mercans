# Test 4 — folha real de setembro/2026 (PMI) × oráculo da lei

Data: 2026-10-30 · Frente: Validação CO · Aprovado pelo usuário em 30/10 · Ligações: [[Colombia]], [[CONFERENCIA]] (pasta `2026-10-29-validacao-research`)

**Pergunta.** As specs foram ajustadas a esta mesma folha em 16–26/10, por isso a folha não prova a research. O que este teste responde é outra coisa: (1) o oráculo, que foi escrito só a partir da lei, concorda com o provedor? (2) Quando não concorda, o que a nossa research manda fazer?

**Fontes.** Só as cópias mascaradas em `co-report-crosscheck/03-client-reports-masked/`:
- Detail IBC per Employees;
- Base of Withholding;
- Vertical G2N Dynamic (wage types por empregado);
- Leave Absence;
- Master Data (classe ARL e procedimento de retenção);
- Accumulated Report (só para pegar a descrição dos WT e o indicador salarial, porque no G2N a coluna "WT Name" saiu mascarada);
- Severance Massive Calculation.

Os empregados aparecem como E001…E261 e as linhas de indenização como S001…S372. Este relatório não traz nenhum ID, nome ou salário individual. O `resultados.json` traz só a diferença e a classe de cada linha.

**Oráculo.** `oracle/oracle.py` + `params.json`, sem nenhuma alteração. Foram importados `monthly`, `retencion`, `terminacion`, `days360` e `ceil_peso`.

## Números

| | Linhas | Bate (≤ 1 COP) | Tolerância (≤ 100 COP) | Sem dado | Divergência | Lacuna do oráculo | Sem efeito |
|---|---|---|---|---|---|---|---|
| Folha (261 empregados: IBC, aportes, retenção, licenças) | 5.232 | 4.502 | 342 | 324 | **55** | 7 | 2 |
| Indenização art. 64 (372 linhas do relatório) | 726 | 24 | 0 | 18 | **684** | 0 | 0 |
| **Total** | **5.958** | 4.526 | 342 | 342 | 739 | 7 | 2 |

O que cada bloco mostra:
- **IBC:** 188 empregados são calculáveis. Em 184 o valor bate, incluindo 73 com salário integral, o teto de 25 SMMLV e o excesso da Ley 1393 (5 empregados com excesso, todos batem). Os outros 4 caem em lacuna do oráculo (ver abaixo).
- **Aportes:** saúde 4%, pensão 4% e 12% e FSP (com as faixas de 16–20 SMMLV) batem em 238–239 de 239 empregados. A exoneração da saúde patronal e de SENA/ICBF bate em 231.
- **Retenção:** batem 133 de 136 no procedimento 1 (tabela do art. 383) e 95 de 96 no procedimento 2 (base × %).
- **Tolerância:** a maior diferença é de 3,24 COP. Vem de três coisas:
  - o 25% isento: o provedor usa 3.447.953 e a conta exata dá 790 × 52.374 / 12 = 3.447.955,50;
  - o IBC com centavos (,5), que o provedor não arredonda para o peso de cima;
  - aportes arredondados ao peso, contra o valor sem arredondamento no oráculo.

## Divergências reais, por mecanismo

| # | Mecanismo | Linhas / empregados | Diferença | Norma | O que a research manda | Impacto |
|---|---|---|---|---|---|---|
| 1 | **Teste da exoneração do art. 114-1 ET.** O provedor soma salarial + não salarial + férias. Com isso, 8 empregados com pagamento salarial abaixo de 10 SMMLV perdem a exoneração e pagam saúde patronal 8,5%, ICBF e SENA. | 24 / 8 | O empregador paga a mais cerca de 16,7 M COP no mês | ET art. 114-1. O Decreto 1828/2013 art. 7 fala em "totalidad de lo devengado", mas o Consejo de Estado, Sección 4.ª (exp. 25302/2022, citado na sentencia exp. 26984/2024), diz que "devengo" são **só os pagamentos com conotação salarial** (cópia local: `raw/docs/oficiais/CO/2026-10-22-CE-S4-26984-2024-SENA-normograma.htm`) | **Contraditório.** A PILA-003 v1.0 (M150), repetida na v1.1-DRAFT, segue o provedor: "total devengado… salary and non-salary alike", com base no Decreto 1828 art. 7. O CCG v1.4 segue o oráculo: "exempt, salary < 10 minimum wages" (dump `revisao/_check/CCG_accept.txt`, l. 463 e 2055). | **NOVO ACHADO.** Não está no comparativo. Alinhar PILA-003 e CCG e citar o CE. |
| 2 | **Retenção sem nenhum benefício.** A base gravável = renda − INCRNGO, sem o 25%, sem dependentes e sem AFC/APV, embora a própria planilha calcule o alívio (coluna TOTAL TAX RELIEF). | 14 / 5 | Retém a mais 7,69 M COP em 4 empregados. O quinto está no "procedimento 3" e o valor não foi recalculado | ET art. 206 num. 10 (25% isento), art. 336 num. 3 (limite de 40% / 1.340 UVT), DUR 1625 art. 1.2.4.1.6 | A research aplica o 25% e o limite sempre. Os passos de retenção dos exemplos do CCG batem com o oráculo (`achados/SIMULACAO.md`). | Nenhum na research. É um erro do provedor (vale um aviso ao BAU). |
| 3 | **Classe ARL.** A taxa aplicada difere da classe do Master Data: 9 empregados "Class 2" pagam a taxa da classe I (0,522%) e 1 "Class 1" paga a da classe II (1,044%). | 10 / 10 | −0,37 M COP no líquido | Decreto 1072/2015 art. 2.2.4.3.5 (taxa por classe) | Já coberto no comparativo: DD-24 (#119), sobre o centro de trabalho e a classe ainda sem vínculo com o empregado. | Já no comparativo. Esta folha confirma o risco. |
| 4 | **Base do empregador menor que a do trabalhador.** Pensão 12%, ARL e CCF são calculados sobre o WT 64990, que é menor que o IBC usado no desconto do trabalhador. | 4 / 2 | 35 mil COP | Ley 100 arts. 18 e 20 (uma só base de cotização) | A research usa uma base só. | Nenhum. Inconsistência interna do provedor. |
| 5 | **Incapacidade dos dias 1–2 e de EPS paga a 100%.** | 3 / 2 | Paga 2,93 M COP a mais | CST art. 227 (2/3, com piso de 1 SMLDV) | CCG v1.4: padrão de 66,67%, configurável, e cita a prática minoritária de 100%. | Nenhum. É mais favorável ao trabalhador (CST art. 13). |
| 6 | **Indenização com tabela de dias acima do art. 64.** Afeta empregados de salário ordinário abaixo de 10 SMMLV. Em média, +274 dias. | 380 / 190 | Acima da lei | CST art. 64 (Ley 789/2002 art. 28) | A research segue o art. 64. Sem a convenção coletiva, não dá para conferir a tabela do provedor. | Nenhum. É mais favorável (CST art. 13). |
| 7 | **Indenização com a fração de ano truncada em dias inteiros.** | 159 dias + 9 valores (os outros entram no #8) / 150 | Até 1 dia a menos por empregado. Nos 9 sem parte variável, −10,6 M COP | CST art. 64 b): "proporcionalmente por fracción" | O CCG faz o pró-rata (exemplo de 100 dias com 20 × 180 / 360). | Nenhum na research. Erro do provedor. |
| 8 | **Valor da indenização sobre o salário básico só.** O próprio relatório monta BASE INDEMNIZACION = básico + variável e usa essa base para escolher a faixa (≥ 10 SMMLV), mas multiplica os dias só pelo básico. | 335 / 335 | Fica abaixo da base com variável | CST art. 127 (o variável é salário) + art. 64 | A research não define a base da indenização (silêncio no CCG e no WTC). | **Possível lacuna nova**, de gravidade baixa: o relatório é operacional, fora do escopo estatutário. Confiança de 70%. |

## Lacunas do oráculo (o provedor está certo ou o ponto está aberto, não é erro dele)

1. **Salário integral com excesso da Ley 1393** (4 empregados). O provedor faz IBC = 70% do salário + o excesso de não salariais acima de 40%. O oráculo só faz 70% do salário e ignora o excesso no integral. Ley 1393 art. 30 vale para "trabajadores particulares", sem exceção para o integral. **Ponto aberto:** o CCG v1.4 manda "40% clamp, depois 70%" (dump, l. 481), o que dá 0,7 × (salário + excesso). Em 2 empregados isso difere do provedor: o IBC fica 1,55 M e 2,51 M COP menor. Nenhuma fonte local decide a ordem → **novo ponto aberto** para o CCG. Confiança de 50% sobre qual leitura está certa.
2. **Base de parafiscais (CCF/SENA/ICBF)** (3 empregados). O oráculo soma o excesso da Ley 1393 nessa base. Só que a Ley 1393 art. 30 vale "para los efectos relacionados con los artículos 18 y 204 de la Ley 100", ou seja, pensão e saúde (texto lido em `raw/docs/oficiais/CO/2026-10-21-Ley-1393-2010-SecretariaSenado.html`). **O provedor está certo e o oráculo tem erro.** É preciso corrigir `para_base` no oráculo; o arquivo não foi alterado neste teste. O CCG lista só duas diferenças da base de parafiscais (sem teto; inclui descansos remunerados) e não diz que o excesso fica fora. Esclarecimento opcional.
3. **Sem efeito** (2 linhas): a coluna AFC/APV passa do teto de 30% / 3.800 UVT, mas o limite de 1.340 UVT já corta o total.

## Sem dado (342 linhas; não é erro)

| Linhas | Motivo |
|---|---|
| 96 | O % semestral do procedimento 2 precisa dos 12 meses anteriores. Foi conferida só a conta base × %. |
| 59 | Valor de férias: depende da média de 12 meses quando há variável e da contagem de dias úteis × corridos. |
| 51 + 51 | Mês com ausência: o oráculo não tem a regra de IBC e ARL dos dias de férias ou incapacidade. |
| 20 | Estagiários/aprendizes INKOMPASS (WT 62149): o oráculo não tem a regra de aporte de aprendiz. |
| 20 + 2 + 2 + 14 | Empregado sem linha ou sem IBC num dos relatórios, ou excesso não derivável. |
| 9 | "Procedimento 3" do provedor (20% fixo + 1.565.043 constante). Não é o procedimento 1 nem o 2 do DUR. Pode ser retenção voluntária maior; a norma não foi conferida. |
| 12 + 3 + 2 + 1 | Indenização: período de prova (CST arts. 76–80), tabela transitória da Ley 789 art. 28, contrato a prazo fixo, falta de dado. |

## Limites
- **A classificação salarial × não salarial de cada WT é do provedor** (indicador "Salary Payment Indicator" e as colunas Salary/Non-Wage Value). O teste confere as regras aplicadas sobre essa classificação, não a natureza de cada pagamento (CST arts. 127/128).
- O campo "Regime = AReg" do Master Data não indica isenção de pensão: o provedor desconta pensão nesses casos. Ele foi tratado como cotizante normal.
- **Vacaciones compensadas na base de parafiscais** (o provedor parece excluí-las) e o IBC de meses com ausência não foram testados sistematicamente.
- **A indenização foi simulada com data de corte em 30/09/2026** e salário = básico + variável. A tabela convencional não está disponível.

## Reproduzir
```
python -I scripts/leitor.py "<…>/co-report-crosscheck/03-client-reports-masked" <scratch>/entradas.json
python -I scripts/comparar.py <scratch>/entradas.json resultados.json
```
O `entradas.json` fica fora da pasta porque tem valores por empregado.

## Bloco de prova
- **Pedido → resposta:**
  1. Entradas por empregado: `leitor.py` (261 empregados mais 372 linhas de indenização).
  2. Recálculo pelo oráculo: IBC, Ley 1393, integral, teto e piso, arredondamentos, aportes, exoneração, retenção (procedimentos 1 e 2, 25%, limite de 40% / 1.340 UVT) e art. 64.
  3. Comparação linha a linha com as classes (a), (b) e (c).
  4. Circularidade: tratada na pergunta do início.
  5. Relatório sem dados pessoais.
  6. Nada alterado: nenhum artefato, nada no Drive, nenhum acesso à rede.
- **Fontes lidas:**
  - Ley 1393/2010 art. 30 (texto local);
  - CE Secc. 4.ª exp. 26984/2024 (texto local, que cita exp. 25302/2022 e o Decreto 1828 art. 7);
  - PILA-003 v1.1-DRAFT, célula M150 (aberta);
  - CCG v1.4 (dump `revisao/_check/CCG_accept.txt`: l. 463, 481, 1946–1948, 2055, 4675, 4837, 5595–5610);
  - comparativo `COMPARATIVO-FINAL-CO-v1.0.xlsx` (DD-24 #119; não há item sobre os mecanismos 1, 2, 7 e 8).
- **Teste mecânico:** os 4.526 "bate" e os 342 "tolerância" vêm de conta refeita pelo oráculo, não de leitura. A regra de exoneração do provedor foi conferida em 239 empregados: o provedor cobra sempre que salarial + não salarial ≥ 10 SMMLV (8 de 9 casos limítrofes).
- **Confiança:**
  - Números e mecanismos: 95%.
  - #1 (exoneração): 85%. O CE anulou atos concretos, mas a linha da Sección 4.ª é reiterada; o Decreto 1828 continua com o texto literal.
  - #8 (variável na indenização): 70%.
  - Ordem 70% × Ley 1393 no integral: 50%. Ponto aberto, sem fonte decisiva.
