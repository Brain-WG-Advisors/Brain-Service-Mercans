# Validação da research CO no modelo da França: proposta (rodada 1)

> 2026-10-29 · frente Validação CO · **proposta, nada construído.** Esperando o ok do usuário (oráculo + suíte). Conferência: [[CONFERENCIA]] · Hub: [[Colombia]] · Modelo: `fr-research-validation/fr-research-validation/` (só leitura).

## 1. O que do método da França se aplica à Colômbia

| Peça da França | Na Colômbia | Como |
|---|---|---|
| Motor de terceiro oficial, grátis e programável (URSSAF `modele-social` v11.1.0) | **Não existe equivalente.** A DIAN, a UGPP e o MinTrabajo não publicam motor de cálculo de folha programável | Trocar por oráculo próprio montado da lei + saída real do provedor da PMI (ver §2) |
| Oráculo (`oracle.py`) + `suite/params.json` / `rules.json` (fonte única dos parâmetros, cada um com fonte) | Aplica igual | Parâmetros CO com vigência e fonte (SMMLV 0159/2026, UVT 238/2025, auxílio 1470/2025, divisores 220/210, dominical 80/90 %) |
| `run_suite.py` (um comando: motor → oráculo → comparação → regras → regressão → workbook) | Aplica igual | `CO-TEST-001` no mesmo formato (Parameters, Test Cases, Expected, Terceiro, Comparison, Traceability, Defect Log, Summary) |
| Gates G1–G7 e critérios (precisão por linha ≥ 95 %, zero S1 aberto, zero regressão antes do baseline) | Aplica igual | Tolerância por linha a fixar no G1 conforme os três regimes de arredondamento do CCG §11 (PILA, XML da nómina, formulários DIAN) |
| Test 0 (amostra de 30–50 afirmações por artefato contra a fonte primária) | Aplica igual | CCG v1.4, WTC v1.6, DD v1.3 |
| Test 1 DSN-Val (validador de formato) | **Parcial.** Nómina electrónica: XSD do Anexo Técnico (offline) sim; set de pruebas da habilitação DIAN exige cadastro → decisão Mercans (G7). PILA: sem validador público (só os operadores) | XSD local para CO-DIAN-001; PILA campo a campo contra o anexo técnico (Res. 2388/2016) |
| Test 4 (comparar com a saída de folha real, mascarada) | **Aplica, e é o mais forte**: temos a saída de setembro do provedor atual da PMI já mascarada (`co-report-crosscheck/03-client-reports-masked/`: Base of Withholding, Detail IBC per Employee S.S., Leave/Absence, Accumulated) | Recalcular IBC, aportes e retención pelo oráculo a partir das entradas mascaradas e comparar linha a linha |
| Test 5 (simuladores oficiais de desligamento/imposto) | Parcial | Calculadora Laboral do MinTrabajo (prestaciones) só para conferência pontual; site do MinTrabajo não abriu desta máquina em 29/10 (timeout) |
| Correção = redline / `-DRAFT-`, nunca no artefato vivo; entregáveis em inglês | Aplica igual + **regra 9**: Colômbia ativa (PMI em BAU) → cada correção confirmada vira ticket de alteração ao Development | |
| Time de agentes (runner Haiku, test-engineer/legal-researcher Sonnet, auditor Opus só nos gates) | Aplica igual | |

## 2. Oráculo: opções

| Opção | O que é | A favor | Contra | Nota |
|---|---|---|---|---|
| **A. Oráculo próprio da lei** (Python, parâmetros com fonte, escrito a partir do ET/CST/Ley 100, **não** do CCG) | Papel do `modele-social` | Programável, cobre tudo (IBC, FSP, retención proc. 1, prima, cesantías, incapacidades, desligamento), reproduzível | Mesmo time que fez a research → independência só se escrito do texto legal e auditado por agente separado | Base da suíte |
| **B. Saída real do provedor da PMI (set/2026, mascarada)** | "Motor de terceiro" de verdade, como pediu o weekly de 07/10 ("comparisons with other payroll vendors") | Software de folha em produção na Colômbia, dados reais, já mascarados e sem PII | Só os cenários que aconteceram em setembro; não dá para escolher caso; provedor também erra (classificar: software × research × prática) | Test 4 |
| C. Calculadoras reconhecidas (Gerencie, Actualícese/Siempre al Día proc. 1, Buk) | Calculadoras web/Excel privadas | Grátis, rápidas | Não oficiais, não programáveis, caso a caso | Conferência pontual |
| D. Calculadora Laboral MinTrabajo | Oficial, pedagógica (cesantías, intereses, prima, vacaciones) | Oficial | Não cobre aportes nem retención; manual; não abriu daqui | Conferência pontual |
| E. Odoo `l10n_co_payroll_full` (módulo de terceiro, Odoo 18) | Software de folha | Motor completo | Módulo de terceiro (provável custo), instalação e configuração pesadas; mesma dor citada no weekly de 07/10 | Descartar |
| F. Software comercial (Siigo, Aleluya, Buk) em teste | Motor comercial | Independente | Conta/contrato; a implementação teria de configurar (weekly 07/10) | Só se A+B deixarem lacuna relevante |

**Recomendação: A + B** (C e D só para conferir pontos soltos). A substitui o motor da França; B é o terceiro independente que a França não tinha (lá o Test 4 ficou fora do escopo).
Se não responder, faço A + B.

## 3. Suíte de casos (proposta)

Período: **março/2026** (antes da reforma) e **agosto/2026** (depois), mais **julho/2026** (mês dividido: divisor 220→210 em 15/07, dominical 80→90 % em 01/07). Linhas comparadas por caso: devengos, auxílio de transporte, IBC, saúde EE/ER, pensão EE/ER, FSP (solidaridad + subsistencia), ARL, CCF, SENA, ICBF, base e valor de retención, neto, provisões (prima, cesantías, intereses, vacaciones), `Redondeo`.

| # | Classe | Casos (limites = valor −1 / exato / +1) |
|---|---|---|
| 1 | Mínimo | 1 SMMLV com auxílio; meio período (15 dias); admissão no meio do mês; fevereiro |
| 2 | Auxílio de transporte | 2 SMMLV exato e 2 SMMLV + 1 |
| 3 | FSP | 4 SMMLV −1 / exato; 16, 17, 18, 19, 20 SMMLV (escada da subcuenta) |
| 4 | Exoneração ET 114-1 | 10 SMMLV −1 / exato ($17.509.050 perde) |
| 5 | Teto IBC | 25 SMMLV exato; 30 SMMLV |
| 6 | Salário integral | 13 SMMLV (mínimo integral, IBC 70 %); integral acima de 25 SMMLV; integral + vacaciones |
| 7 | Retención proc. 1 | base 95 UVT −1 / exato; troca de faixa 150 e 360 UVT; dependente (72 UVT); AFC/pensión voluntaria; prepagada; vivienda; limite 40 %/1.340 UVT ativo; renta exenta 25 % com teto 790 UVT |
| 8 | Horas extras e recargos | diurna, noturna, recargo noturno, dominical/festivo em março (80 %), julho (mês dividido) e agosto (90 %, divisor 210) |
| 9 | Ley 1393 art. 30 | não salariais 40 % exato e acima (excesso vai ao IBC) |
| 10 | Prima de servicios | junho e dezembro; salário variável; com auxílio de transporte na base (C31: prática, não lei) |
| 11 | Cesantías e intereses | anual (12 %); liquidação no desligamento |
| 12 | Vacaciones | gozadas; compensadas em dinheiro (WTC v1.6: fora de saúde/FSP/ARL/pensão) |
| 13 | Incapacidad comum | dias 1–2; 3–90 (66,67 %, piso SMMLV: Q-6/Q-7 abertos → resultado esperado "pendente"); 91–180; 541+ |
| 14 | Licenças | maternidade; paternidade; não remunerada (Q-8 aberto → "pendente") |
| 15 | Desligamento | indefinido sem justa causa abaixo e acima de 10 SMMLV (CST art. 64); termo fixo; renúncia |
| 16 | Mesadas adicionais (pensionistas) | junho e dezembro; saúde/FSP ficam "pendente" (com terceiros, ver [[revisoes/2026-10-28-CO-mesadas-adicionais-saude-fsp]]) |
| 17 | ARL e aprendiz | risco I e V; aprendiz SENA (Q-5, 45 % → "pendente") |

Cerca de **60 casos**. O que está aberto na skill (Q-5/6/7/8, mesadas, C21 SMMLV) entra como caso com resultado "pendente", não como erro. Os casos do Test 4 vêm da folha de setembro (mascarada), sem escolha.

## 4. Cobertura por artefato (o usuário pediu em 29/10: validar **cada** artefato com simulações)

A suíte do §3 gera, para cada caso, as entradas, o cálculo e as saídas. Cada artefato é validado pelo que ele diz que deveria sair dessa simulação. O que nenhuma simulação executa vai para o Test 0 (afirmação × fonte primária). A validação com o BAU de 26 a 28/10 (`co-report-crosscheck/04-output/CONFIRMACAO-PROCESSOS-CO-2026-10-26.xlsx`, resposta à Heidy de 28/10) **não é repetida**: entra como resultado esperado já decidido.

| Artefato | Como a simulação valida | Mede |
|---|---|---|
| **CCG v1.4** | Cada regra do CCG vira linha(s) da suíte (matriz de rastreabilidade, como no E2 da França). O oráculo da lei calcula, o CCG manda calcular, e as duas coisas são comparadas. Regra que não dá para calcular (prazo, órgão, texto) vai para o Test 0 | % das regras com teste automático; regras passando ÷ regras rastreadas |
| **WTC v1.6** | Cada WT usado nos casos tem as suas marcações aplicadas pelo oráculo (salarial, IBC, parafiscal, retención, base de prestaciones, FSP/ARL). Se a marcação do WTC der resultado diferente da lei, é defeito. Meta: todo WT com marcação ser exercitado por pelo menos um caso; o que sobrar vai para o Test 0 | WTs exercitados ÷ total; acertos por marcação |
| **DD v1.3** | Lista dos campos de que a suíte precisa como entrada (tipo de contrato, salário integral, risco ARL, dependentes, AFC, datas, tipo de planilla PILA...) e dos que as specs exigem como saída. Cada campo é conferido contra o DD (existe? tipo e lista de valores certos?). Campo que falta ou está errado é defeito | Campos exigidos presentes e corretos ÷ exigidos |
| **CO-DIAN-001 Nómina electrónica** | Gerar o XML de cada caso pela spec → validar contra o XSD da Caja de Herramientas da DIAN (já local: `CO-compliance/integration-sources/dian-ne/caja/...V1-0/Schemes/`; antes, conferir se é a versão do Anexo Técnico vigente pela Res. 227/2025) → totais do XML = oráculo → CUNE recalculado (o exemplo oficial não reproduz, D-2: não usar como teste) | Zero erro de XSD; totais batendo |
| **CO-DIAN-002 Formulario 350** | Somar a retención dos casos do mês → casillas de salários da spec = soma do oráculo; regra da casilla 93 (WT 2552 + 21330, já reconciliada na rodada 3) | Casillas batendo |
| **CO-DIAN-004 Formulario 220** | Acumular o ano dos casos (pagamentos, aportes, renta exenta, retención) → casillas do certificado = oráculo | Casillas batendo |
| **CO-DIAN-005 Formato 2276** | Mesmo acumulado anual → campos da spec. Layout marcado DERIVED (Q-11, C28): sem XSD oficial ainda → validação só de valores; o formato fica como lacuna aberta | Valores batendo; formato = lacuna |
| **CO-PILA-003 Aportes (planilla E)** | Gerar as linhas de cada caso → posição/tamanho/valores contra o anexo técnico vigente da PILA (local: `raw/docs/oficiais/CO/2026-10-13-Res-MSPS-467-2025-PILA.pdf`; confirmar que é a versão vigente antes de usar) → IBC, aportes e arredondamento PILA = oráculo; comparar com o relatório de IBC mascarado da PMI (oráculo B, se aprovado) | Campos e valores batendo |
| **CO-PILA-007 Pensionados (planilla P)** | Casos de mesada (classe 16) → linhas da spec. Saúde/FSP na mesada de junho continuam com terceiros (pendente) | Idem; pendências declaradas |
| **CO-CESANTIAS-006 Consignação** | Classe 11 (cesantías anuais) → valor consignado e campos da spec = oráculo; base com auxílio de transporte é prática, não lei (C31): resultado esperado "decisão" | Valores batendo |
| **SIR v1.1** | Não calcula: cada passo, prazo, canal e órgão vai para o Test 0, e a sequência é seguida com os arquivos simulados acima (o que o SIR manda gerar existe e passa?) | Afirmações corretas ÷ conferidas |
| **Payslip (v1.1 no pipeline, sem versão no hub)** | Gerar o payslip de 3 a 5 casos → 13 itens da Res. DIAN 227/2025 presentes e valores = oráculo. Antes, achar a versão vigente com `achar_versao.py` | Itens e valores batendo |

## 5. Meta "100 % de acertos": como medir
- Mesma conta da França: checagens passando ÷ checagens rodadas (por linha), regras passando ÷ rastreadas, mais o Test 0 por artefato.
- **100 %** = toda checagem passa **ou** toda diferença foi resolvida pela lei e corrigida (DRAFT + ticket ao Development, regra 9). A França fechou em 97,6 %, com o resto explicado por defeitos do motor; aqui não há motor de terceiro para culpar, então cada diferença é nossa até prova em contrário.
- **Aviso honesto:** hoje há pontos abertos que impedem 100 % sem decisão: Q-5 (aprendizes), Q-6/Q-7 (incapacidade, dias 1–2 e piso), Q-8 (licença não remunerada), saúde/FSP na mesada de junho, C21 (instrumento do SMMLV), formato do 2276 (Q-11). Cada um tem de ser fechado com fonte ou retirado do escopo por você, registrado no relatório.

## 5b. Revisão crítica (29/10, pedido do usuário): o equivalente colombiano do motor da URSSAF
- Não há motor oficial programável na Colômbia. A solução gratuita da DIAN só gera e transmite a NE, sem calcular. O COLMOD (Externado/OFiscal) é uma microssimulação de domicílios, não uma folha. A calculadora do MinTrabajo cobre só prestaciones.
- **Substituto recomendado: software de folha colombiano completo em teste grátis**, rodando os mesmos casos numa empresa fictícia. Aleluya (15 dias, sem cartão) e Alegra Nómina (15 dias). Os dois calculam aportes, parafiscales, prestaciones, retención e liquidação, e geram a NE e a PILA. Isso faz o papel do `modele-social`.
- **Validadores de cada autoridade:** simulador de planilla dos operadores PILA (aportes e arredondamento oficiais); set de pruebas da habilitação DIAN + XSD (NE); calculadora do MinTrabajo (prestaciones).
- O oráculo da lei (A) passa a ser a terceira voz; quando houver divergência, decide a lei. A folha da PMI (B) vira um teste extra, não o principal (é parcialmente circular com o cross-check de 16–26/10).
- A verificar antes: termos de uso (empresa fictícia, NIT de teste), importação em lote, se 60 casos cabem em 15 dias, e se a Mercans aceita usar trial de um concorrente.

## 6. Pede o ok do usuário
1. Oráculo **A + B** (ou outra).
2. Suíte do §3 e cobertura por artefato do §4.
3. Habilitação DIAN (set de pruebas) fica fora, como na França (G7)?
4. Os 6 pontos abertos do §5: fechar com pesquisa antes de rodar (recomendo) ou rodar e marcar "pendente"?

Quando você disser "ok", eu faço: 1. `suite/params.json` CO com fonte por parâmetro; 2. oráculo A; 3. leitor das saídas mascaradas (B); 4. primeira rodada e relatório no formato do runbook (números, defeitos propostos, gate).
