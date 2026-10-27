# Erros e soluções: grupo OUT (Colômbia, Chile, China, Holanda, Irlanda, Lituânia, Singapura, Espanha-sem-país-no-título)

- **Grupo:** OUT
- **Data da análise:** 2026-10-08
- **Nota:** Análise de erros e soluções; complementa a extração factual de 2026-10-02.
- **Arquivos lidos** (`raw/tickets/txt-utf8/`; cada ticket tem um único snapshot neste grupo, então "todos os snapshots" = 1 arquivo por ticket):
  - `12 - Ticket - SR-316 - CN_Payslip.txt` (exportado 2026-08-10)
  - `34 - Ticket - HRBS-13860 - Naersa file failing again this month.txt` (2026-08-27)
  - `52 - Ticket - HRBS-10563 - Update Required Wage Type Configurations, Taxability Matrix, and Statutory Leave Logic Gaps.txt` (2026-09-08)
  - `68 - Ticekt - HRBS-12487 - Automation of Vacation Pay Calculation - Offcycle.txt` (2026-09-16)
  - `69 - Ticket - HRBS-12491 - Explanation of Garnishment Calculation.txt` (2026-09-16)
  - `70 - Ticekt - HRBS-12492 - SSecurity Contribution Rules (Employee & Employer) – Colombia.txt` (2026-09-16)
  - `71 - Ticket - HRBS-13627 - Explanation of Income Tax Withholding Calculation.txt` (2026-09-16)
  - `72 - Ticekt - HRBS-13692 - Accruals Severance Pay and Severance Interest Calculation.txt` (2026-09-16)
  - `78 - Ticket - HRBS-14675 - Netherlands standard reports- Need to update SSI percentage as per 2026.txt` (2026-09-21)
  - `90 - Ticket - SR-232 CL-PRV-001-Previred-PlanillaMensual-Spec.txt` (2026-09-28)
  - `94 - Ticekt - SR-221 - CL-DT-001-LRE-LibroRemuneracionesElectronico-Spec.txt` (2026-09-28)
  - `99 - Ticket - HRBS-15253 - ACCENTURE LITHUANIA  Compliance (Calculation & Reporting) Check.txt` (2026-09-28)
  - `102 - Ticket - HRBS-15630 - Urgent GWM Singapore REF-P202-936 ... .txt` (2026-10-07)
- **Fontes cruzadas:** `extracao/2026-10-02-tickets-OUT.md`, `correcoes.md`, `mercans-pipeline/shared/country_failure_log.md` (F1–F47).
- **Convenções:** datas "aprox." derivam de "X days ago" relativo à data de exportação do snapshot (±1 dia). Nomes/IDs de empregados e valores individuais foram omitidos. Trechos "Show more" dos PDFs vêm cortados no texto (HRBS-12487, HRBS-10563); o que ficou cortado está marcado como "não consta". Observações de "conferência aritmética" ou de base legal que não vêm do ticket são minhas e estão marcadas [INCERTO].
- **Observação geral:** o HRBS-10563 é da **Espanha** (campo País = Spain), embora o título não diga o país. Os tickets Colômbia 12491/12492/13627/13692 e o 12487 pertencem ao cliente Philip Morris International (PMI), com a transição para Instaroll como pano de fundo (comentário de Romano Fusana, aprox. 2026-09-03: "tickets levantados pela PMI que precisam ser tratados antes de o cliente migrar para o Instaroll").

---

## HRBS-12487 — Colômbia: automação do vacation bonus offcycle (limite de 95 UVT)
- **País / Cliente / Tipo / Prioridade:** Colômbia / Philip Morris International (Compañía Colombiana de Tabaco SAS, REF-LE-00-505) / Incident (Tier 1 "New Development Item") / Medium. Fase Live/BAU, Production.
- **Snapshots lidos:** 68 (exportado 2026-09-16). O texto tem trecho cortado ("Show more") no meio da simulação enviada pelo cliente.
- **Estado no último snapshot:** Pending on reporter; assignee Wallisson; Resolution Time "Paused". Sem solução.
- **Linha do tempo:**
  - aprox. 2026-07-16: Jose Quiroga (cliente) abre o ticket: com a mudança para Instaroll, passos antes manuais do cálculo do vacation bonus precisam ser automatizados. Quando o bônus passa de 95 UVT, devem ser descontados seguridade social e retención en la fuente; hoje o time calcula por fora e ajusta no passo 3. Dias de férias ficam no código 63123; o valor do bônus no 62837 (aparece no G2N).
  - aprox. 2026-07-16: Romano Fusana (Support) confirma recebimento.
  - aprox. 2026-08-16: Romano pede simulação passo a passo (contexto do empregado, dias em 63123 e bônus em 62837, UVT e limite em COP, deduções esperadas, resultado esperado no G2N).
  - aprox. 2026-08-16/18: Jose envia planilha (`95UVT_Automation_Spec.xlsx`, abas Parameters, Art383, Example, Validation) e exemplo real do offcycle da semana 31/2026. Regras de escopo dadas por ele: Salario Integral sempre excluído (só Personnel Area CO = Ordinario); o procedimento de retención (1 ou 2) já está no sistema (opção 6 do cartão do empregado) e, no Procedimento 2, o percentual fixo fica no WT 52552; Total Días = Days Taken + Cash Out (somar os dois; usar só Days Taken é fonte de erro conhecida); bônus bruto = ROUND(Total Días x 2,8 x (salário base mensal / 30), 0), "o que o HRBlizz já produz hoje e está correto". Resto da simulação cortado.
  - aprox. 2026-08-18: Jose pergunta se há atualização.
  - aprox. 2026-08-20: Sohail Ahmad: em call ficou definido que precisa de apoio de Compliance para automatizar seguridade social e imposto sobre esses bônus.
  - aprox. 2026-08-21: Romano registra cliente/entidade/ambiente.
  - aprox. 2026-08-25: Mohit Jain (Head of Compliance Product): "Colômbia requer redesenho ou, no mínimo, grande correção de lacunas".
  - aprox. 2026-09-03: ticket atualizado por Mohit (atribuição a Wallisson; Mohit comentou nos tickets-irmãos "análise de gap durante a pesquisa da Colômbia" e o mesmo vale aqui [INCERTO]: este ticket não tem esse comentário literal).
- **Problema relatado:** o sistema não deduz seguridade social e retención sobre vacation bonus acima de 95 UVT em offcycle; o cálculo é manual fora do sistema.
- **Erro identificado:** lacuna funcional da regulation de Colômbia (não há regra automática para SS e retención sobre o vacation bonus offcycle). Não é erro de valor num artefato nosso; é lacuna de design/regulation. O ticket não dá base legal para os 95 UVT ("sem fonte no ticket"). [INCERTO]: 95 UVT coincide com o primeiro tramo (0%) da tabela do Art. 383 E.T. citada no HRBS-13627, mas o ticket 12487 não explica a ligação. Responsável: regulation/implementação (design), não o cliente.
- **Causa raiz:** [INCERTO] o design da Colômbia tratou férias/bônus de férias como valor carregado (63123 -> 62837) sem regra de base de SS e de retención para o pagamento offcycle; a própria Mohit reconhece necessidade de redesenho. Etapa: design (regulation), derivado de research incompleto sobre pagamentos offcycle.
- **Solução aplicada:** não resolvido no último snapshot. Nenhuma resposta de Compliance consta; houve só coleta de simulação e escalada para Compliance.
- **O que não aconteceu / ficou aberto:** definição da regra (qual tabela/percentual na retención do bônus; bases de pensão/saúde no bônus); se a dedução reduz o 62837 ou entra em linhas separadas (pergunta 5 do Support, sem resposta visível); ETA; validação contra o resultado manual.
- **Tipo de erro:** T6 (escopo/regra de pagamento offcycle ausente), T7 (método de cálculo ausente), T11 (coleta de simulação).
- **Lição para o pipeline:** F43 (Special populations not covered systematically) cobre "férias" e "verbas rescisórias" na coverage matrix, mas não obriga a descrever o tratamento de SS e imposto de **pagamentos offcycle de verbas variáveis**; F46 (design não derivado da pesquisa) explica por que o design da Colômbia não herdou isso. NOVO: "Pagamento offcycle de bônus/férias sem regra de base e retención" -> teria sido pego por uma linha da coverage matrix "pagamento offcycle/extra-ciclo por tipo de verba" com SS + imposto + fonte.

---

## HRBS-12491 — Colômbia: explicação do cálculo de embargos (garnishment)
- **País / Cliente / Tipo / Prioridade:** Colômbia / Philip Morris International (Compañía Colombiana de Tabaco SAS) / Incident (Tier 1 Instaroll) / Medium.
- **Snapshots lidos:** 69 (2026-09-16).
- **Estado no último snapshot:** Pending on reporter; assignee Wallisson; Resolution Time "Paused". Sem solução.
- **Linha do tempo:**
  - aprox. 2026-07-16: Heidy Ballesteros Puyo (cliente) abre o ticket explicando a metodologia e um caso de exemplo (empregado não identificado aqui): ganhos salariais de COP 15.428.991 (salário 12.135.162 + bônus de férias 2.427.032 + pagamento de férias 866.797); descontados SS e imposto (COP 3.314.882 segundo o Support), base líquida COP 12.114.109; acima do SMMLV aplica-se 1/5 do excedente. O valor gerado pelo sistema é "preliminar", pois a configuração não reflete a metodologia; o time revisa e ajusta manualmente.
  - aprox. 2026-07-16: Romano acusa recebimento.
  - aprox. 2026-08-16: Romano confirma a cadeia e nota a divergência: 1/5 do excedente seria COP 2.072.641; o item 21125 aplicado foi COP 1.548.190; o cálculo preliminar do sistema foi COP 1.536.309. Pergunta: (1) para valores fixados em juízo, o sistema calcula o teto legal (1/5) como validação ou aplica o valor da ordem; (2) sem valor fixo, aplicar 1/5 automaticamente; (3) qual SMMLV (a planilha usa 1.750.905); (4) lista de itens (21125, 64993) e quantidade de embargos por período.
  - aprox. 2026-08-16/18: Cintia Torres avisa que Heidy está de férias; Romano faz follow-up.
  - aprox. 2026-08-18/20: Heidy responde: (1) para embargo judicial o sistema deve calcular automaticamente 1/5 do excedente sobre o SMMLV: ganhos conforme a ordem judicial, menos 2552 (imposto), 2553 (fundo solidariedade pensão), 2554 (saúde empregado), 2556 (pensão obrigatória), menos SMMLV 2026 de COP 1.750.905, 1/5 do resultado; o cálculo não pode ser modificado manualmente antes da folha; há variantes: base só salário básico; valor fixo definido pelo juiz (sem cálculo, aplicar o valor cadastrado); base <= SMMLV gera zero, nunca negativo.
  - aprox. 2026-09-03: Romano/Mohit: ticket entra na lista da PMI para transição ao Instaroll; Mohit atribui a Wallisson para análise de gap na pesquisa da Colômbia.
- **Problema relatado:** o sistema gera um valor preliminar de embargo que não reflete a metodologia correta; hoje é ajustado manualmente.
- **Erro identificado:** lacuna/erro na regulation de embargos da Colômbia: não calcula por tipo de ordem (base salário total, base só salário básico, valor fixo), nem respeita o piso zero. Responsável: regulation/implementação; o cliente também mantém uma divergência não explicada (valor da ordem 1.548.190 vs 1/5 de 2.072.641). Não se sabe qual artefato nosso (CCG/WTC/DD) cobre embargos.
- **Causa raiz:** [INCERTO] o design não modelou tipos de embargo; o SMMLV não está num parâmetro mantido (Support pediu que "referencie um parâmetro mantido", dado que muda por decreto todo janeiro). Etapa: research/design.
- **Solução aplicada:** não resolvido. Houve especificação da regra pelo cliente (Heidy), sem validação de Compliance e sem alteração de artefato.
- **O que não aconteceu / ficou aberto:** a divergência 2.072.641 x 1.548.190 nunca foi explicada (Support supôs "valor fixado pelo juiz", Heidy não confirmou literalmente, e a regra que ela descreve diz que valor fixo = sem cálculo, o que contradiz o ajuste manual descrito no ticket original); pergunta 4 (lista de itens, volume) sem resposta; valor do SMMLV 2026 (COP 1.750.905) está **sem fonte no ticket** (decreto não citado); a base legal do 1/5 também **sem fonte no ticket**; prioridade das deduções (2552/2553/2554/2556) não validada contra lei.
- **Tipo de erro:** T7 (fórmula/método), T6 (tipos de embargo fora do escopo do sistema), T1 [INCERTO] (SMMLV precisa de parâmetro com vigência), T12 (sem base legal), T11.
- **Lição para o pipeline:** F44 (Single-pass research: números nunca re-verificados) e F43 (populações especiais: nenhuma linha para "descontos judiciais"). NOVO: "Deduções judiciais/embargos sem modelo no WTC/CCG" e "parâmetro salarial anual (SMMLV) hard-coded"; teria sido pego por linha da coverage matrix "embargos/pensão alimentícia" e por um check que exija valores anuais em tabela com vigência (Regra 1/2 do cérebro).

---

## HRBS-12492 — Colômbia: regras de seguridade social (empregado e empregador)
- **País / Cliente / Tipo / Prioridade:** Colômbia / Philip Morris International (REF-LE-00-505) / Incident (Tier 1 Instaroll) / Medium.
- **Snapshots lidos:** 70 (2026-09-16).
- **Estado no último snapshot:** Pending on reporter; assignee Wallisson; Resolution Time "Paused". Sem solução.
- **Linha do tempo:**
  - aprox. 2026-07-16: Cintia Torres (cliente) abre o ticket pedindo que o sistema calcule corretamente saúde, pensão, ARL e parafiscales, listando as regras: IBC mín. 1 SMLMV, máx. 25 SMLMV; regra dos 40% (Lei 1393/2010): pagamentos não salariais acima de 40% da remuneração total voltam ao IBC; saúde 12,5% (4% empregado + 8,5% empregador; 8,5% isento até 10 SMLMV); pensão 16% (4% + 12%); ARL só empregador por classe de risco; Fundo de Solidariedade Pensional a partir de 4 SMLMV, só empregado, percentual crescente; parafiscales só sobre salário: Caja 4%, ICBF 3%, SENA 2%, isentos ICBF/SENA/saúde até 10 SMLMV; regra especial de férias: IBC = salário do mês imediatamente anterior ao início das férias (Art. 3, Decreto 1072/2015 e diretrizes PILA). Anexos: validador (xlsx) e Word com tabelas e exemplos.
  - aprox. 2026-07-16: Romano acusa recebimento.
  - aprox. 2026-08-16: Romano pede 2–3 casos concretos (ordinário até 10 SMMLV, integral com regra 70% do IBC e Fundo de Solidariedade, caso com férias), observa um caso com 4 dias de licença em que as contribuições parecem calculadas sobre o bruto do mês e não sobre a base do mês anterior, e pergunta quais conceitos são não salariais (lista de códigos) para validar o teto de 40%.
  - aprox. 2026-08-16/18: follow-up de Romano; Heidy anexa o validador de seguridade social de julho (todos os casos).
  - aprox. 2026-08-18: Cintia cobra; aprox. 2026-08-20: Heidy reenvia (cópia) e link Google Sheets.
  - aprox. 2026-09-03: Mohit atribui a Wallisson para análise de gap.
- **Problema relatado:** o sistema não calcula corretamente SS/parafiscales segundo as regras do IBC (40%, isenções por faixa, IBC em férias).
- **Erro identificado:** o ticket não mostra um caso de erro concreto confirmado. Hipótese do Support (observação, não confirmada): IBC de férias calculado sobre o bruto do mês e não sobre o salário do mês anterior. Responsável: implementação/regulation [INCERTO]. Os valores/percentuais do ticket são do cliente e vêm com as bases legais acima; nenhum foi verificado por nós.
- **Causa raiz:** [INCERTO] regulation sem as três regras (40%, isenção até 10 SMLMV, IBC de férias). Etapa: design/research.
- **Solução aplicada:** não resolvido; nenhuma resposta de Compliance consta; as perguntas do Support (casos, lista de códigos não salariais) foram parcialmente atendidas só com o anexo do validador.
- **O que não aconteceu / ficou aberto:** lista de conceitos não salariais; comparação sistema x esperado por conceito; confirmação do caso de férias; se a base legal do IBC de férias (Decreto 1072/2015 Art. 3, citada pelo cliente) é a correta [INCERTO: decreto 1072/2015 é o Decreto Único do Setor Trabalho; vale conferir a norma específica de IBC em férias]; conteúdo do Word anexo e das tabelas ARL/Fundo de Solidariedade (não aparece no texto).
- **Tipo de erro:** T7, T1 [INCERTO] (percentuais/faixas a validar), T2 (tratamento contributivo de conceitos salariais/não salariais), T12 (base legal do IBC de férias a confirmar), T11.
- **Lição para o pipeline:** F43 (casos especiais: férias, integral, faixas) e F41 (research não testada contra oráculo independente: aqui existe um oráculo, o validador do cliente, que poderia ter sido usado antes da entrega). NOVO: "Regra de IBC em ausências/férias" não coberta -> teria sido pega por linha "ausências remuneradas e base de SS" na coverage matrix + C40.

---

## HRBS-13627 — Colômbia: explicação do cálculo de retención en la fuente
- **País / Cliente / Tipo / Prioridade:** Colômbia / Philip Morris International (Compañía Colombiana de Tabaco SAS) / Question/Inquiry (Tier 1) / Medium.
- **Snapshots lidos:** 71 (2026-09-16).
- **Estado no último snapshot:** Open; assignee Wallisson; Resolution Time -20d (SLA já estourado).
- **Linha do tempo:**
  - aprox. 2026-08-23: Heidy Ballesteros Puyo (cliente) abre o ticket: o sistema deve calcular o imposto automaticamente com Método 1 ou 2 (percentual fixo). Conceitos: 2552 Income Tax (Employee), 21330 Personal Income Tax Withholding (Theoretical) para Expat Home. Hoje o cálculo padrão roda para todos e os Expat Home são revisados e ajustados depois; a retenção é reclassificada ao conceito correspondente. Anexo: validador mensal em Excel (julho/2026) e descrição completa dos passos, limites e tabela.
  - aprox. 2026-09-03: Romano Fusana: ticket faz parte da lista PMI antes da transição ao Instaroll. Mohit Jain: atribui a Wallisson para análise de gap na pesquisa da Colômbia.
- **Problema relatado:** pedido de explicação/validação do cálculo de retención feito pelo validador do cliente e requisito de automação no sistema (incluindo Expat Home e rendimentos contingentes).
- **Erro identificado:** nenhum erro de artefato nosso comprovado (pedido de informação/gap). Pontos do próprio texto do ticket que merecem verificação (conferência minha, [INCERTO]):
  - Aritmética do ticket com UVT 2026 = COP 52.374: 790 UVT/12 = 65,83 UVT x 52.374 = COP 3.447.955 (ticket: 3.446.732); 1.340 UVT/12 = 111,67 UVT x 52.374 = COP 5.848.430 (ticket: 5.847.117); limite de 945 UVT = COP 49.493.430 (ticket: 49.483.530). Os demais valores em pesos conferem. Só afeta a coluna de referência, o ticket diz que o cálculo real é feito em UVT.
  - O limite de 40%/1.340 UVT é citado como Art. 388 E.T.; a meu conhecimento esse limite vem do Art. 336 E.T. (Art. 388 trata da depuração da base de retención) [INCERTO, conferir].
  - A regra de 30% das aportaciones AFC/VFP (Art. 126-1) não menciona o teto anual de UVT [INCERTO].
  - Tratamento de "Expat/Non-resident": 20% direto sobre o total dos rendimentos, sem deduções, **sem base legal citada** ("sem fonte no ticket"); o nome do conceito (21330, "Expat Home", Theoretical) e a descrição (não residente, 20%) não coincidem claramente.
  - Limite de 1.340 UVT aplicado como 1.340/12 por mês sem acumulado anual: o próprio ticket admite risco de subretenção e mantém controle manual para quem recebeu o benefício via bônus IC.
- **Causa raiz:** pedido de documentação/gap; o ticket revela limites de design: validador externo (Excel) em vez de cálculo nativo; ausência de acumulado anual do limite de 1.340 UVT; reclassificação manual para Expat Home; Procedimento 2 recalculado só em junho e dezembro.
- **Solução aplicada:** não resolvido; nenhuma resposta de Compliance consta. Valores estatutários citados pelo ticket: UVT 2026 = COP 52.374 (Resolução DIAN 000238 de 2025-12-15, variação do IPC de 5,17%); tabela Art. 383 E.T. (faixas 0–95: 0%; 95–150: 19%; 150–360: 28% +10 UVT; 360–640: 33% +69; 640–945: 35% +162; 945–2.300: 37% +268; >2.300: 39% +770); isenção de 25% (Art. 206 nº 10, até 790 UVT/ano); alimentação 41 UVT/mês (Art. 387-1, salário <= 310 UVT); juros de moradia 100 UVT/mês, saúde 16 UVT/mês, dependentes 32 UVT/mês (Art. 387).
- **O que não aconteceu / ficou aberto:** a análise de gap; verificação independente do validador do cliente; automação do Método 2, do contingente, do prima de serviços e do Expat; decisão sobre o limite anual.
- **Tipo de erro:** T11, T7 (método sem acumulado anual), T6 (Expat/contingente fora do sistema), T12 (Expat 20% sem fonte; citação do Art. 388 a conferir), T1 [INCERTO] (aritmética em COP).
- **Lição para o pipeline:** F37 (taxa/valor em prosa contradizendo o próprio cálculo) e F42 (exemplos digitados e não calculados) descrevem o padrão das inconsistências aritméticas; F44 (sem varredura final de boletim). NOVO: "Limites anuais aplicados em base mensal sem acumulador" -> check de design que, para cada limite anual, exija o acumulador YTD ou justificativa.

---

## HRBS-13692 — Colômbia: provisões de cesantías e juros sobre cesantías
- **País / Cliente / Tipo / Prioridade:** Colômbia / Philip Morris International (Compañía Colombiana de Tabaco SAS) / Question/Inquiry (Tier 1) / Medium.
- **Snapshots lidos:** 72 (2026-09-16).
- **Estado no último snapshot:** Open; assignee Wallisson; Resolution Time -19d.
- **Linha do tempo:**
  - aprox. 2026-08-25: Heidy Ballesteros Puyo (cliente) abre o ticket: o sistema não gera automaticamente a provisão de cesantías nem a de juros; hoje são calculadas por fora e carregadas por Excel; também não existe o relatório de consolidação exigido no fechamento da folha e na entrega ao cliente. Requisitos: provisão em 22110 (Provision Severance - Social Benefits Provision Accrual 1), juros em 22112 (Provision Interest Severance Pay), cálculo por data de admissão, dias acumulados, base salarial (salário + média dos conceitos salariais, Art. 253 CST: média do último ano ou do tempo trabalhado se variável), juros de 12% a.a. proporcionais (juros = cesantías acumuladas x 12% x dias / 360), considerar pagamentos anteriores, e relatório de consolidação com ~16 colunas mínimas.
  - aprox. 2026-09-03: Romano (lista PMI) e Mohit atribuem a Wallisson para gap analysis.
- **Problema relatado:** ausência de cálculo automático de provisão de cesantías/juros e do relatório de consolidação.
- **Erro identificado:** lacuna funcional e de relatório (report spec inexistente para a consolidação). Não é erro de valor. Responsável: regulation/relatórios; o ticket não identifica artefato nosso.
- **Causa raiz:** [INCERTO] o design da Colômbia não contemplou provisões de benefícios sociais nem o relatório de consolidação; escopo de Report Specs e WTC não incluiu esses itens. Etapa: research/design (escopo).
- **Solução aplicada:** não resolvido; a análise de gap está pendente.
- **O que não aconteceu / ficou aberto:** análise de gap; spec do relatório de consolidação; confirmação dos WTs 22110/22112 no WTC da Colômbia; tratamento de salario integral (sem cesantías) e depósito no fundo de cesantías não aparecem no ticket (não consta). Percentuais e fórmula do ticket (12%, /360, Art. 253 CST) vêm do cliente, sem verificação nossa; o prazo de pagamento dos juros ("geralmente em janeiro") é impreciso no ticket (sem data legal; sem fonte).
- **Tipo de erro:** T5 (spec de relatório ausente), T6 (escopo de provisões), T3 [INCERTO] (conferir WTs 22110/22112), T7, T12 (sem fonte para 12% e prazo).
- **Lição para o pipeline:** F19 (relatório HR-scope no handover) é o inverso; o caso aqui é relatório estatutário-contábil esperado pelo cliente e não mapeado. F43 (rescisão/verbas) ajuda parcialmente. NOVO: "Provisões contábeis de benefícios sociais e relatório de consolidação" -> check "para cada benefício legal, existe WT de provisão e relatório de saldo?".

---

## SR-221 — Chile: Report Spec LRE (Libro de Remuneraciones Electrónico)
- **País / Cliente / Tipo / Prioridade:** Chile / sem cliente (Statutory Reports; Redesign of old country: No) / spec de relatório (projeto SR) / Major. Due date 2026-07-31.
- **Snapshots lidos:** 94 (2026-09-28).
- **Estado no último snapshot:** In Progress; assignee Wallisson (Research Analyst); BA: Ruchi Gupta; atrasado em relação ao due date.
- **Linha do tempo:**
  - aprox. 2026-04: ticket criado por Wallisson (5 meses antes de 2026-09-28).
  - aprox. 2026-05-28: Ruchi Gupta pede para verificar os campos destacados em amarelo.
  - aprox. 2026-05-28/30: Wallisson responde: a versão anterior foi apagada e esta é "melhorada", para revisão.
  - aprox. 2026-05-28/30: Ruchi: "você não pode simplesmente apagar; eu já trabalhei nesse arquivo; não é assim que se atualizam documentos."
  - aprox. 2026-09-15: Ruchi: link não abre; Wallisson: link atualizado.
  - 2026-09-28: Ruchi pede adicionar no WTC uma coluna com o código de relatório aplicável.
- **Problema relatado:** (a) versão anterior da spec foi apagada em vez de versionada, perdendo o trabalho de revisão da BA; (b) link da spec inacessível; (c) WTC não indica a qual relatório cada WT se aplica.
- **Erro identificado:** (a) erro de processo nosso (versionamento; já registrado em `correcoes.md` em 2026-09-15); (b) erro nosso de acesso/entrega do link; (c) lacuna de estrutura do WTC (falta coluna Report Code).
- **Causa raiz:** (a) substituição do arquivo em vez de nova versão [comunicação/processo]; (b) link com permissão restrita ou sem acesso [INCERTO]; (c) o WTC foi construído sem o mapeamento WT -> relatório (sincronização entre artefatos). Etapa: construção do artefato e entrega.
- **Solução aplicada:** (b) link atualizado (aprox. 2026-09-15). (a) e (c) não resolvidos no snapshot (nenhuma confirmação de que a coluna foi adicionada).
- **O que não aconteceu / ficou aberto:** adição da coluna no WTC; restauração/recuperação da versão anterior; resultado da revisão dos campos amarelos [INCERTO]; due date já passou.
- **Tipo de erro:** T8 (versão/sincronização entre WTC e Report Spec), T5, T3.
- **Lição para o pipeline:** F25 (Report-Specs construídas antes do DD: deriva de nomes) e F45 (sem consistência entre artefatos) cobrem o padrão; escapou porque o requisito "WTC com coluna de Report Code" não está no contrato do WTC. NOVO: "Coluna Report Code no WTC" -> check automático: para cada WT usado numa Report Spec, existe o mapeamento no WTC (e vice-versa); NOVO: "Artefato versionado: nunca apagar versão revisada" (próximo de F15, mas sobre versionamento).

---

## SR-232 — Chile: Report Spec Previred (Planilla Mensual)
- **País / Cliente / Tipo / Prioridade:** Chile / sem cliente / spec de relatório (projeto SR) / Major. Due date 2026-07-31.
- **Snapshots lidos:** 90 (2026-09-28).
- **Estado no último snapshot:** Open; assignee Wallisson; BA: Ruchi Gupta.
- **Linha do tempo:**
  - aprox. 2026-04: criado por Wallisson (5 meses antes).
  - aprox. 2026-09-15: Ruchi: link não abre; pede a Wallisson e Manju Shetija que atualizem a descrição com o link compartilhado em chat (Google Sheets); Wallisson: link atualizado.
  - 2026-09-28: Ruchi pede a mesma coluna no WTC com o código de relatório.
- **Problema relatado:** link inacessível e falta de coluna de report code no WTC.
- **Erro identificado:** igual ao SR-221: erro nosso de entrega do link e lacuna de estrutura no WTC.
- **Causa raiz:** igual ao SR-221 (permissão do link [INCERTO]; WTC sem mapeamento WT -> relatório).
- **Solução aplicada:** link atualizado (aprox. 2026-09-15). Coluna do WTC: não resolvido no snapshot.
- **O que não aconteceu / ficou aberto:** coluna no WTC; due date vencido; estado permanece Open.
- **Tipo de erro:** T8, T5.
- **Lição para o pipeline:** mesmas de SR-221 (F25, F45; NOVO: coluna Report Code no WTC). Nota: o pedido apareceu nos dois tickets no mesmo dia, o que sugere requisito de formato da BA para todo o pacote do Chile.

---

## SR-316 — China: Payslip (conversão para o formato Compliance)
- **País / Cliente / Tipo / Prioridade:** China / sem cliente / spec/payslip (projeto SR, subtarefa de CT-4457 "CN_China_Compliance Artifacts for development") / Normal. Due date 2026-08-31.
- **Snapshots lidos:** 12 (2026-08-10).
- **Estado no último snapshot:** Open; assignee Wallisson; Research Analyst: Enaakshi Vats. O estado posterior a 2026-08-10 não consta.
- **Linha do tempo:**
  - aprox. 2026-07: ticket criado por Enaakshi Vats (cerca de 1 mês antes de 2026-08-10), apontando o "China Cn Payslip generator v1.0" (Google Sheets).
  - aprox. 2026-08-04: Lily Li pede a Enaakshi que converta o payslip da China para o formato Compliance.
  - aprox. 2026-08-09/10: Enaakshi pede a Wallisson que ajude com o payslip da China.
- **Problema relatado:** payslip generator v1.0 da China não está no formato Compliance (modelo Spain/Mercans).
- **Erro identificado:** artefato (Payslip v1.0) fora do padrão Mercans/Spain; origem do v1.0 não consta no ticket. Responsável: nosso artefato / quem produziu o v1.0 [INCERTO].
- **Causa raiz:** [INCERTO] v1.0 produzido fora da etapa 7 do pipeline ou sem o padrão de formatação; etapa: construção do artefato (Payslip).
- **Solução aplicada:** não resolvido no snapshot (apenas pedido de ajuda a Wallisson).
- **O que não aconteceu / ficou aberto:** conversão; versão nova do payslip; confirmação de conformidade.
- **Tipo de erro:** T9.
- **Lição para o pipeline:** a skill `mercans-compliance-workflow` e o `mercans-artifact-toolkit` (contrato estrutural do Payslip e gate de pré-voo) já existem para isso; o caso escapou porque o artefato chegou de fora do pipeline [INCERTO]. NOVO (se for o caso): "Payslip externo sem passar pelo gate de formato" -> executar o pre-flight do toolkit em qualquer payslip antes de entrar num pacote.

---

## HRBS-14675 — Holanda: relatório padrão netherland-ssc-pdf com percentuais de SSI desatualizados (2026)
- **País / Cliente / Tipo / Prioridade:** Países Baixos / Omnicom (todas as entidades NL: 5 entidades listadas) / Question/Inquiry (Tier 1) / Medium.
- **Snapshots lidos:** 78 (2026-09-21).
- **Estado no último snapshot:** Pending on reporter; assignee Wallisson; Resolution Time "Paused".
- **Linha do tempo:**
  - aprox. 2026-09-15: Suresh Jalihal abre o ticket: o relatório `netherland-ssc-pdf` traz percentuais de SSI antigos. Lista os de 2026: ZVW 6,10%; AOF Laag 6,27%; AOF Hoog 7,63%; AOF Uit 7,63%; AWF Laag 2,74%; AWF Hoog 7,74% (escrito "Haag"); WKO 0,50%; ZW Flex e WGA conforme o campo do Legal Entity. Anexa PDF com os percentuais incorretos. Fonte dos percentuais: não consta.
  - aprox. 2026-09-16: Suresh pede a Abarna Khaliq verificar; Abarna: não trata relatórios e pede a Crina Lorincz que encaminhe a quem trata.
  - aprox. 2026-09-21: Shaik Jani Sharif (Reports) acusa recebimento, pede o arquivo de especificação e observa que o relatório está em **Custom Reports**, não em Statutory Reports. Suresh: deveria ser relatório padrão (consta no BPQ e na report matrix), é do país e não de cliente, e ele não tem especificação. Shaik pergunta a Mohit se é de Compliance. Mohit pede a Wallisson que verifique se é relatório estatutário de Compliance.
- **Problema relatado:** percentuais de contribuições sociais de 2025 ainda impressos no relatório de SSC.
- **Erro identificado:** relatório com percentuais desatualizados (T1). Artefato: relatório `netherland-ssc-pdf` (sem spec conhecida, configurado como Custom Report). Responsável: [INCERTO] ninguém definido; pode não ser artefato do nosso serviço. Valores: "sem fonte no ticket" (nenhuma lei/ portal citado).
- **Causa raiz:** percentuais aparentemente fixos no relatório, sem rotina de troca anual; ausência de dono e de spec (relatório classificado como Custom). Etapa: construção/manutenção de relatório, fora do pipeline.
- **Solução aplicada:** não resolvido; ticket circulou por 5 pessoas sem decisão de dono.
- **O que não aconteceu / ficou aberto:** decisão se é statutory; spec; validação dos percentuais com fonte oficial (Belastingdienst/UWV, não citados); definição do mecanismo de atualização anual; ZW Flex/WGA por entidade.
- **Tipo de erro:** T1, T5, T6 (o relatório está fora do catálogo statutory), T12 (sem fonte).
- **Lição para o pipeline:** F18 (referências legais obsoletas no CCG) e F44 (sem varredura final de boletim). NOVO: "Relatório padrão cliente-visível sem dono e sem spec; taxas hard-coded" -> check: toda taxa impressa em relatório vem de parâmetro com vigência; Report Matrix com dono por relatório.

---

## HRBS-13860 — Irlanda: arquivo NAERSA falhando de novo (classes PRSI incorretas)
- **País / Cliente / Tipo / Prioridade:** Irlanda / Omnicom (entidades Clavis e OMG; afeta todas) / Incident (Tier 1, L2 Support) / Medium.
- **Snapshots lidos:** 34 (2026-08-27).
- **Estado no último snapshot:** In Progress; assignee Romano Fusana (não é Wallisson); Resolution Time 5d.
- **Linha do tempo:**
  - 2026-08-27 (cerca de 1 h antes da exportação): Philippa O'Reilly (cliente) abre: submissão NAERSA falhou de novo neste mês para todas as entidades; a payroll submission falhou para Clavis e OMG por classes PRSI incorretas; pede corrigir as classes e submeter o arquivo de agosto no mesmo dia.
  - 2026-08-27: Romano acusa recebimento e, 43 min antes, anexa tabela de processos da entidade Clavis Technologies Ltd (REF-LE-01-699): dois processos "NAERSA Contribution Submission with Reconciliation Details" e "Irish Tax Payroll Submission", ambos com status errored; último passo `API_Error_Details` / `Submit_Report_ErrorBrak` [texto como no PDF].
- **Problema relatado:** falha recorrente do envio mensal; causa apontada pelo cliente: classes PRSI incorretas.
- **Erro identificado:** classes PRSI incorretas em dados de entrada/configuração dos empregados das entidades Clavis e OMG; o que de fato gerou o erro de API não consta. Não é possível atribuir ao nosso artefato ou ao cliente; "recorrente" ("again this month") indica falha repetida.
- **Causa raiz:** não consta; [INCERTO] dado mestre do empregado (classe PRSI) fora dos valores aceitos ou mapeamento DD de classes PRSI incompleto.
- **Solução aplicada:** não resolvido no snapshot (apenas diagnóstico inicial com IDs de processo).
- **O que não aconteceu / ficou aberto:** correção das classes; reenvio de agosto; análise do motivo da recorrência; causa das falhas nas outras entidades.
- **Tipo de erro:** T4 [INCERTO] (opções/obrigatoriedade de PRSI class), T10 [INCERTO] (cliente x artefato).
- **Lição para o pipeline:** F1 (option mapper DD x specs) é o padrão mais próximo se as classes PRSI do DD divergirem das aceitas; F8/F21 (mecânica de submissão). NOVO: "Pré-validação de campos enumerados (PRSI class) antes do envio estatutário" -> check de DD que liste valores aceitos e validação do arquivo antes do submit.

---

## HRBS-15253 — Lituânia: verificação de cobertura de cálculo e reporting (Accenture)
- **País / Cliente / Tipo / Prioridade:** Lituânia / Accenture (Accenture Lithuania, REF-LE-04-359) / Question/Inquiry (Tier 1) / Medium. Resolution Time 2d.
- **Snapshots lidos:** 99 (2026-09-28).
- **Estado no último snapshot:** Open; assignee Wallisson.
- **Linha do tempo:**
  - aprox. 2026-09-28 (cerca de 10 h antes da exportação): Kevin Gunawan abre o ticket: cliente novo na Lituânia; quer confirmar que cálculo e reporting estatutário e tributário (mensal e anual) estão acomodados. Anexa questionário em 5 partes pedindo marcar cada linha como S (suportado e configurado), C (precisa de configuração), M (workaround manual) ou N (não suportado), com dono/roadmap para M e N.
  - cerca de 8 h antes: Lavanya Balamurugan (Product Support) acusa recebimento.
  - cerca de 7 h antes: ticket atualizado por Manju Shetija (conteúdo não consta no texto).
- **Problema relatado:** pedido de matriz de cobertura para a Lituânia, sem validação de números nesta fase. Partes: (1) cálculo: bases GPM e Sodra separadas; contribuições de empregado e empregador (Sodra); GPM com faixas alteradas em 2026-01-01; NPD; tetos e pisos; ausências; arredondamento e retro; (2) relatórios mensais: SAM/SAM3SD/SAM3SDP (.ffdata, EDAS) até dia 15, GPM313 (VMI/EDS) até dia 15, data de pagamento do imposto derivada da data real de pagamento; payslip, arquivo bancário, GL, reconciliação; (3) eventos: 1-SD, 2-SD, 9-SD, 12-SD, 13-SD, NP-SD, PT; (4) anuais: GPM312 (até 15 de fevereiro), GPM312L, GPM312U, provisão de férias, virada de parâmetros; (5) cinco perguntas (quem mantém as estruturas .ffdata versionadas, dry-run de upload, correções, parameter sheet assinada, se a Mercans já entregou Lituânia).
- **Erro identificado:** nenhum (pedido de informação). Prazos e formulários citados pelo cliente estão "sem fonte no ticket".
- **Causa raiz:** não se aplica; novo país/cliente sem baseline conhecido nesta amostra (não consta se existe dossiê para a Lituânia; dossiês de outros países estão em `~/.claude/skills`).
- **Solução aplicada:** não resolvido no snapshot; apenas acknowledgments.
- **O que não aconteceu / ficou aberto:** a matriz S/C/M/N; respostas às cinco perguntas, em especial a existência de parameter sheet assinada e de cliente de referência (resposta depende de existir ou não research da Lituânia); o que Manju atualizou.
- **Tipo de erro:** T11 (T6 potencial: escopo de eventos 1-SD etc. entre payroll e HR).
- **Lição para o pipeline:** F21 (mecânica de filing mensal/trimestral/anual mal entendida), F43 (populações especiais: joiners/leavers, múltiplos contratos, A1/EU) e F46 (design derivado da pesquisa) são os padrões que o questionário testa; a lista do cliente já é um bom checklist para uma coverage matrix da Lituânia. Se não houver dossiê, a lição é NOVO: "Pergunta de cobertura de cliente novo sem dossiê do país" -> o scaffolder (compliance-scaffolder) deveria produzir a matriz S/C/M/N como saída padrão.

---

## HRBS-15630 — Singapura: CPF com teto de AW usando salário de outubro ainda não pago (OT Run)
- **País / Cliente / Tipo / Prioridade:** Singapura / GSK (Glaxo Wellcome Manufacturing Pte Ltd, entidade REF-3-083) / Service Request (Tier 1) / Medium no cabeçalho; "High" no corpo ("bloqueia o sign-off do OT Run"; fase de testes).
- **Snapshots lidos:** 102 (2026-10-07).
- **Estado no último snapshot:** In Progress; assignee Wallisson; Resolution Time 4d. Sem solução.
- **Linha do tempo:**
  - aprox. 2026-10-06: Deepak Domala (cliente) abre o ticket urgente: o OT Run (off-cycle, payroll OCP-202-936, Jurong, período 01–31/10/2026) rodou antes do Main Run de outubro (REF-P202-937); o teto de AW do CPF usa o salário de outubro do Main Run (calculado, não pago; aparece no relatório YTD CR16). Para três empregados o CPF no OT saiu zero ou reduzido (GTN CPF EE/ER 0/0, 0/0 e 316/268), enquanto o esperado, calculando só sobre o OT, seria 326/279, 0/71 e 604/514. Tentou recalcular e destravar/travar a folha sem sucesso. Esperado: OW de outubro tratado como zero no OT Run; teto de AW usa OW acumulado jan–set mais OW projetado, excluindo salário de outubro ainda não rodado. Observação: o assunto/título usa REF-P202-936 e o corpo REF-P202-859 (identificadores inconsistentes).
  - aprox. 2026-10-06: Crina Lorincz (Support) acusa recebimento; Khoi Pham descreve que no Main Run o EE já foi excluído, mas no OT Run a contribuição CPF EE "sempre fica menos algo do mesmo valor", e o EE fica sem nada no GTN; Crina comenta "o sistema não está calculando a contribuição como 2553" [sentido não claro].
  - aprox. 2026-10-06 (tarde): Crina escala a Wallisson e pede para investigar por que a contribuição do empregador não é paga para os 3 empregados.
  - aprox. 2026-10-07 (cerca de 5 h antes da exportação): Kevin Gunawan cobra atualização urgente de Wallisson e Crina.
- **Problema relatado:** CPF no OT Run (primeiro run do mês) é limitado pelo teto de AW com base em salário de outubro ainda não pago.
- **Erro identificado:** comportamento de cálculo (teto de AW/OW em run off-cycle anterior ao main run) não condiz com a expectativa do cliente. Se é erro do nosso design/CCG/regulation, do sistema ou de configuração: não consta; [INCERTO] regulation (implementação) tratando como "pago" um valor apenas calculado. Observação minha [INCERTO]: os valores esperados pelo cliente são coerentes com 20% empregado / 17% empregador com arredondamento do total ao dólar, empregado arredondado para baixo e empregador = total menos empregado, mas o ticket não cita taxas nem a fonte; o texto do pedido é ambíguo ("OW de outubro = 0" e também "mais OW projetado"), e o teto anual de AW depende da definição legal de OW do ano (não consta no ticket).
- **Causa raiz:** [INCERTO] o acumulador YTD de OW usado no teto de AW inclui o resultado calculado do Main Run (status calculated) em vez de só pagamentos efetivados; falta regra de ordem de runs/off-cycle. Etapa: design da regulation/sistema (cálculo).
- **Solução aplicada:** não resolvido no último snapshot.
- **O que não aconteceu / ficou aberto:** diagnóstico da causa; correção e recálculo; decisão sobre como tratar o teto quando o Main Run for pago depois (reajuste do teto de AW); esclarecer o significado da fala de Crina sobre "2553"; inconsistência de IDs (REF-P202-859 x -936).
- **Tipo de erro:** T7 (método/ordem de cálculo e acumuladores), T10 [INCERTO].
- **Lição para o pipeline:** F43 (populações especiais: overtime e "annual regularisation" estão na coverage matrix, mas não "off-cycle antes do main run") e F42 (exemplos computados) teriam ajudado se houvesse exemplo de OT Run. NOVO: "Acumulador YTD que mistura valores calculados e pagos / ordem de runs" -> check de design: para cada teto acumulado (OW/AW), declarar a fonte do acumulador (pago x calculado) e testar com cenário "off-cycle antes do main".

---

## HRBS-10563 — Espanha: wage types, matriz de tributação e lacunas na lógica de licenças estatutárias
- **País / Cliente / Tipo / Prioridade:** Espanha / "All Spain" (sem cliente; sem fase) / Service Request / Medium. Inward mention: CT-4433 ES: Spain Regulation Support.
- **Snapshots lidos:** 52 (2026-09-08). Dois trechos "Show more" cortados: resposta 1 (final do ponto 5) e resposta de correção (final do cálculo de piso/teto diário).
- **Estado no último snapshot:** Open; assignee Lily Li; SLA Breached; Resolution Time 1d. Gulnaaz Parveen (Implementação) reportou em 2026-09-08 que a lógica de licença médica ainda não funciona em produção.
- **Linha do tempo:**
  - aprox. 2026-06: Gulnaaz Parveen abre o ticket a partir de reunião: 6 ações sobre Espanha (série 62960–62969 tributável e não SS; série 6298 não tributável e não SS; severance do cliente (62180, 62983) prevalece sobre o calculado; licenças estatutárias faltantes (aborto, menstruação incapacitante, interrupção da gravidez) com a lógica de base de licença médica (BCC/BCCP do mês anterior); lógica dia 1 x dia 2 de acidente de trabalho (79411/79412); décima quinta paga com período de acumulação diferente por CBA). Anexos: 3 G2N Espanha, planilha de licenças e códigos de pagamento.
  - aprox. 2026-06: Lily Li: edite no WTC V3.9 e DD V3.7 (não finalizados, In Progress); roxo = alterações dela; ponto 3 será tratado nos regulation steps; pontos 1 e 2: atualizou colunas T–AC do WTC; renomeou 62920 para Pay in Lieu of Notice; pergunta o "ponto 7" (condição de aplicação da lógica de base de licença quando há licenças de tipos diferentes no mesmo mês).
  - aprox. 2026-06: Wallisson (1ª resposta, WTC V3.9, alterações em laranja): ponto 1 confirmado, com ressalva do Art. 147 LGSS; ponto 2 corrigiu metadados AEAT/190 (62983 -> clave L/L05, exento Art. 7.e LIRPF, fora de 111/216; demais 6298 -> L/L01); ponto 3 sem mudança no WTC; ponto 4 acrescentou 3 leave units (79022, 79024, 79028) mirando 79008; ponto 5 esclareceu: 79411 = salário integral do dia da baja pago pelo empregador (Art. 173.1 LGSS), 79412 = 75% da base reguladora a partir do dia 2, pagamento delegado; diferença para menstruação incapacitante, paga pela SS desde o dia 1; payouts 79420–79428 existem com nome genérico "Other Leave Payout", não renomeados sem aval da Lily.
  - aprox. 2026-06/07: Gulnaaz pede o DD e o WTC atualizados; Lily: é mudança grande da regulation Espanha, precisa de análise completa, regulation design, reports mapping e desenvolvimento; ETA com Mohit. Lily pergunta se o CRA do 62983 deve ser 54 e lista licenças que não estão no WTC (ERE parcial/total, maternidade/paternidade/parental parciais, parental, risco na gravidez/lactação, aborto, menstruação incapacitante, interrupção da gravidez) e pede lógica detalhada do ponto 7 com perguntas sobre base BCCC/BCCP e dias por contingência. Lily também explica o campo "Extra Pay Month N (Accrual Month)" para o ponto 6.
  - aprox. 2026-06/07: Wallisson (2ª resposta): 62983 = CRA 0054, indicador E (TGSS/SILTRA) e clave L/L05 (AEAT/190), sistemas diferentes que coexistem, mesmo critério de ES-CRA-001 (58184, 58186, 62180); adicionou leave units Risk During Pregnancy/Lactation/Parental Leave e payouts nos slots 79416/79417/79418 (BCCC/BCCP = No, AEAT B.01); não adicionou parciais (coeficiente de jornada) nem ERE (ERTE: suspensão; SEPE paga). Ponto 7: "100% BR" é só payout; nascimento/cuidado cota sobre BCCC do M-2 (Orden PJC/297/2026); corrigiu Lily: o mecanismo por dia e por contingência vale também para a base de cotização; Seção 5 do documento BCCC/BCCP Base Logic estaria errada (BOE-A-2026-7296).
  - aprox. 2026-07: Lily pergunta a Wallisson sobre payouts que não existem no WTC e propõe resumo das bases por tipo de licença e 5 perguntas; Wallisson (3ª resposta): ÷30 só para grupo mensal, grupo diário ÷ dias reais do mês, tempo parcial: soma dos 3 últimos meses ÷ dias do período (RDL 11/2024); segmentação do mês com bases separadas; exemplos A–C. Lily faz 4 perguntas adicionais (como chegar a 30 com mais de um tipo de licença; um payout por licença; worked-day base só em BCCC; gatilho da segmentação; piso/teto só sobre worked-day base).
  - aprox. 2026-07 (4ª resposta, autocorreção): as bases BCCC e BCCP continuam durante qualquer licença (Orden PJC/297/2026 Art. 6.1, 6.3, 6.5); worked-day base entra nas duas; piso e teto (teto 2026 EUR 5.101,20/mês) valem para as bases mensais, não proporcionais; trecho final sobre piso/teto diário truncado no texto.
  - aprox. 2026-07/08: Lily adiciona os payouts novos (79417–79424) e pede confirmação das colunas N a AA e dos nomes; Wallisson (5ª resposta): taxabilidade OK; AEAT/190 corrigido de clave B/pago directo/"Not in 111" para clave A, subclave em branco, Work_Cash_Gross, 111 Work-Cash; 216 Scope N/A nas 6 linhas de subsídio e "Subject to withholding" nos dois payouts de dia 1 (79417, 79422); 296 indevido removido de 79422; 79419 renomeado para "75% day 21+"; bandas conforme Art. 173 LGSS.
  - 2026-09-08: Gulnaaz reporta que a lógica de licença médica ainda não funciona (licença de abril a maio; deveria usar a base de SS de março), anexa G2N de março/abril/maio e payslip correto do A3.
- **Problema relatado:** configuração de WTs/matriz de tributação e da lógica de licenças e acidentes na regulation da Espanha; depois, sick leave contínua ainda calculada errado em produção.
- **Erro identificado:**
  - WTC V3.9: AEAT/190 da série 6298 com clave A (inconsistente com não tributável): corrigido.
  - Payouts novos (79417–79424): AEAT B/pago directo/"Not in 111" em vez de pago delegado (clave A): corrigido. 79422 com campos 296 indevidos: removidos. 79419 com nome inconsistente: renomeado.
  - Exemplos A–C da 3ª resposta de Wallisson zeravam BCCP/BCCC durante licença: **erro nosso (resposta anterior)**, autocorrigido antes do desenvolvimento.
  - Entendimento da Lily (por-dia só no payout) e Seção 5 do doc BCCC/BCCP Base Logic: corrigidos por Wallisson com base no BOE (autoria do doc [INCERTO]).
  - Código de WT: slot 79416 aparece como payout "Risk During Pregnancy" na 2ª resposta e como payout de licença médica (79414/79415/79416) na 5ª resposta; também há leave units propostos 79022/79024/79028 na 1ª resposta e payouts 79417–79424 na 5ª; [INCERTO] colisão ou renumeração de WT.
  - Em produção (2026-09-08): para licença que atravessa meses, o sistema não usa a base do último mês trabalhado inteiro (março), o que sugere que a regra "mês anterior" não cobre o caso em que o mês anterior já é de licença [INCERTO].
- **Causa raiz:** (a) metadados de reporting (AEAT/190) não sincronizados com as colunas de taxabilidade e copiados do padrão "pago directo" em vez de "pago delegado" (sincronização entre colunas do WTC); (b) documentos internos com seção contraditória (Seção 5); (c) respostas dadas por etapas, com correção posterior, antes de haver exemplos computados contra a Orden; (d) licença contínua entre meses é caso especial não detalhado nos exemplos (todos os exemplos A–C são de mês isolado). Etapas: construção do WTC, design e comunicação.
- **Solução aplicada:** Wallisson, em WTC V3.9 (alterações em laranja): correções de AEAT/190, CRA 0054/E em 62983, três leave units + payouts novos, renomeação 79419, remoção de 296 em 79422; respostas com base em Art. 147/144/173/186–187 LGSS, Orden PJC/297/2026 (BOE-A-2026-7296), RDL 11/2024, RDL 9/2025, Modelo 190, ES-CRA-001 Table 84. DD V3.7 listado como editável; não consta o que mudou no DD.
- **O que não aconteceu / ficou aberto:** análise completa e desenvolvimento por Lily/Dev; ETA via Mohit; ponto 3 (override de severance nos regulation steps); ponto 6 (15ª paga/CBA): campo "Extra Pay Month N (Accrual Month)" criado por Lily, sem confirmação nossa; gatilho da segmentação (query 4) com resposta truncada; renomear payouts genéricos 79420–79428; ticket de sick leave contínua (setembro) sem resposta nossa; SLA Breached; texto "ponto 7" não está na descrição original do ticket [INCERTO sobre onde foi definido].
- **Tipo de erro:** T2, T3, T7, T8, T12 [Seção 5 do doc], T4 [INCERTO] (DD V3.7 não detalhado).
- **Lição para o pipeline:** F7 (WTC com tax codes errados na Espanha: AEAT L x A) é o mesmo padrão; F20 (WTC com lacunas e códigos inválidos), F27 (artefato posterior não re-sincronizado) e F37 (taxa em prosa contradizendo o próprio cálculo; aqui, documento com seção contraditória) cobrem o resto. Escapou porque a validação do WTC não cruza as colunas de taxabilidade com as de reporting AEAT/190 e porque não há cenário "licença que atravessa meses". NOVO: "Colunas de taxabilidade x metadados de reporting (AEAT/SILTRA) incoerentes" -> check C9 ampliado: regra por WT (não tributável => clave L, fora de 111/216; pago delegado => clave A); NOVO: "Regra de base de licença sem caso contínuo entre meses".

---

## Tabela-resumo

| ID | País | Tipo(s) | Artefato | Resolvido? | F-xx / NOVO |
|---|---|---|---|---|---|
| HRBS-12487 | Colômbia | T6, T7, T11 | Regulation/WTC (vacation bonus offcycle) | Não (Mohit: redesenho/grande correção de lacunas) | F43, F46 / NOVO: offcycle de bônus/férias sem regra de SS e retención |
| HRBS-12491 | Colômbia | T7, T6, T1 [INCERTO], T12, T11 | Regulation/WTC (embargos 21125) | Não (regra descrita pelo cliente, sem validação) | F43, F44 / NOVO: embargos sem modelo; SMMLV sem parâmetro com vigência |
| HRBS-12492 | Colômbia | T7, T1 [INCERTO], T2, T12, T11 | Regulation (IBC, 40%, isenções, férias) | Não | F43, F41 / NOVO: IBC em ausências/férias |
| HRBS-13627 | Colômbia | T11, T7, T6, T12, T1 [INCERTO] | Regulation (retención; validador do cliente) | Não (gap analysis pendente) | F37, F42, F44 / NOVO: limite anual aplicado em base mensal sem acumulador |
| HRBS-13692 | Colômbia | T5, T6, T3 [INCERTO], T7, T12 | Report Spec ausente; WTs 22110/22112 | Não (gap analysis pendente) | F19 (inverso), F43 / NOVO: provisões de benefícios sociais + relatório de consolidação |
| SR-221 | Chile | T8, T5, T3 | Report Spec LRE; WTC | Parcial (link corrigido; coluna no WTC e versionamento pendentes) | F25, F45, F15 / NOVO: coluna Report Code no WTC; não apagar versão revisada |
| SR-232 | Chile | T8, T5 | Report Spec Previred; WTC | Parcial (link corrigido; coluna no WTC pendente) | F25, F45 / NOVO: coluna Report Code no WTC |
| SR-316 | China | T9 | Payslip v1.0 | Não (no snapshot de 2026-08-10) | NOVO: payslip externo sem gate de formato (toolkit) [INCERTO] |
| HRBS-14675 | Países Baixos | T1, T5, T6, T12 | Relatório netherland-ssc-pdf (Custom Report; sem spec) | Não | F18, F44 / NOVO: relatório sem dono com taxas fixas |
| HRBS-13860 | Irlanda | T4 [INCERTO], T10 [INCERTO] | Envio NAERSA / dado PRSI | Não (em diagnóstico) | F1, F8/F21 / NOVO: pré-validação de classes PRSI |
| HRBS-15253 | Lituânia | T11 (T6 potencial) | Nenhum (cobertura do país) | Não | F21, F43, F46 / NOVO: matriz de cobertura para cliente novo |
| HRBS-15630 | Singapura | T7, T10 [INCERTO] | Regulation (teto OW/AW do CPF) | Não | F43, F42 / NOVO: acumulador YTD calculado x pago; ordem de runs |
| HRBS-10563 | Espanha | T2, T3, T7, T8, T12, T4 [INCERTO] | WTC V3.9, DD V3.7, doc BCCC/BCCP Base Logic | Parcial (WTC corrigido; regulation, dev e sick leave contínua abertos) | F7, F20, F27, F37 / NOVO: taxabilidade x metadados AEAT; licença contínua entre meses |

## Padrões recorrentes no grupo

- **Gaps de regulation de Colômbia em bloco (cinco tickets PMI):** embargos, SS/IBC, retención, vacation bonus e provisões chegaram como "explique/valide", mas todos revelam que o sistema não implementa o cálculo e que o time faz por fora (Excel, ajuste manual). Mohit já os agrupou como "redesenho ou correção grande" antes da migração PMI -> Instaroll. A pesquisa/CO-compliance ainda não parece cobrir essas rotinas [INCERTO].
- **Valores e limites sem fonte ou com aritmética inconsistente:** SMMLV 2026, taxas de SSI da Holanda, regra de 20% de expat, prazos da Lituânia, e erros de conversão UVT -> COP no HRBS-13627. O ticket sozinho não permite verificar; os valores precisam entrar com vigência e fonte (Regras 1 e 2 do cérebro).
- **Limites e acumuladores:** limite anual de 1.340 UVT aplicado como 1/12 mensal (Colômbia) e teto de AW baseado em YTD que inclui salário calculado mas não pago (Singapura) são o mesmo problema: acumulador mal definido (fonte, período, status calculado x pago).
- **Sincronização entre colunas/artefatos:** WTC com taxabilidade correta mas reporting AEAT/190 incoerente (Espanha), WTC sem coluna de Report Code exigida pela BA (SR-221 e SR-232 no mesmo dia), e códigos de WT em conflito entre respostas (79416). Padrões F7, F25, F27, F45.
- **Processo e versionamento de artefatos:** spec apagada em vez de versionada (SR-221), links de spec inacessíveis em dois tickets (SR-221, SR-232), respostas corrigidas em etapas na Espanha (exemplos A–C zerando bases). Falta checagem de acesso do link e regra de "não apagar versão revisada".
- **Dono indefinido de relatório/ticket:** HRBS-14675 passou por cinco pessoas até chegar a Compliance; o relatório é "Custom" mas tratado como padrão. Ticket da Irlanda segue com Support L2, sem ligação a artefato nosso.
- **Casos especiais fora da coverage matrix:** off-cycle antes do main run, vacation bonus offcycle, licença que atravessa meses, embargos, expat. A F43 cobre bem populações, mas não ordem de runs nem pagamentos extra-ciclo.
- **Cliente novo sem baseline (Lituânia):** a matriz S/C/M/N pedida é a saída natural do scaffolder e deveria existir antes do ticket.
