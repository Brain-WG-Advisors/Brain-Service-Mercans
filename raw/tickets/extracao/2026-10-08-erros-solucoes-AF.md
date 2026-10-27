# Erros e soluções — Grupo AF (África: Namíbia, Congo, Gabão, Côte d'Ivoire)

- **Grupo:** AF (Namíbia, Congo-Brazzaville, Gabão, Côte d'Ivoire), cliente quase único: Baker Hughes.
- **Data da análise:** 2026-10-08
- **Nota:** Análise de erros e soluções; complementa a extração factual de 2026-10-02 (`2026-10-02-tickets-AF.md`).
- **Arquivos lidos** (`raw/tickets/txt-utf8/`, números = ordem de exportação):
  - 01 (HRBS-12483) e 02 (HRBS-12072): .txt vazio; lidos a partir dos PDFs originais em `youtrack_tickets/`.
  - 06 e 10 (HRBS-12111); 13 (HRBS-12472); 16 (HRBS-12101); 20 (HRBS-12110); 21 (CT-A-620); 32 (HRBS-13602); 33 e 35 (HRBS-13841); 37 (HRBS-14054); 38 (HRBS-14055); 75 (HRBS-14714); 80, 88 e 91 (HRBS-14996); 86 (HRBS-14605).
- **Fontes cruzadas:** `correcoes.md` (linhas Congo/Gabão/Costa do Marfim) e `mercans-pipeline/shared/country_failure_log.md` (F1–F47).
- **Convenções:** datas aproximadas derivadas de "X days ago" (±1 dia) e marcadas "~". Sem nomes ou IDs de empregados, nem salários individuais. [INCERTO] = inferência. Quase nenhum ticket do grupo traz versão de artefato; quando não consta, está escrito "não consta".
- **Observação geral:** em vários tickets o texto exportado tem só comentários parciais (cabeçalho "1 of 6", "2 of 3" etc. indica páginas do navegador não exportadas). O que não aparece pode existir no YouTrack [INCERTO].

---

# NAMÍBIA

## HRBS-12072 — Mais códigos de pay element para Namíbia (combinações Tax/SSNC/ECF/Pension)
- **País / Cliente / Tipo / Prioridade:** Namíbia / Baker Hughes / Service Request / Medium (Tier 1, Implementation, Production). Vinculado a HRBS-12074 "Configure Entity using the WTC for Baker Hughes Namibia".
- **Snapshots lidos:** 02 (PDF; exportação 2026-08-04).
- **Estado no último snapshot:** SLA Exempt (First Reply e Resolution Time "Paused"); assignee Wallisson.
- **Linha do tempo:**
  - ~2026-07-20: Daniel Kelvin Balogun (implementação) pede mais pay elements para dois padrões: (a) Tax=Yes / SSNC=Yes / Pension=No; (b) SSNC=No / ECF=Yes / Pension=No (exemplos: Overtime Normal Workday 1,5x, Overtime). Pede a lista completa de códigos aplicáveis da WTC de compliance (link para planilha).
  - ~2026-07-28: Mohit Jain responde que a combinação (b) já existe na WTC.
  - ~2026-07-28: Mohit Jain diz duvidar que a combinação (a) exista e pede que o solicitante confirme com Wallisson.
  - ~2026-07-28: Pradeep Duraisamy atualiza o ticket (sem texto visível).
- **Problema relatado:** o WTC de compliance não teria nenhum código com Tax=Yes/SSNC=Yes/Pension=No; o WTC do cliente tem códigos assim (overtime). Pede confirmação se existem.
- **Erro identificado:** não confirmado. Pode haver divergência entre WTC do cliente e a de compliance nos flags de pensão do overtime. Quem tem razão não consta. Nenhum erro nosso foi demonstrado (pedido de informação, com suspeita de divergência cliente × artefato).
- **Causa raiz:** [INCERTO] o WTC do cliente (legado) usa uma combinação de flags que o WTC de compliance não modela (ou modela com outros flags). Não há análise no ticket.
- **Solução aplicada:** parcial: combinação (b) confirmada como existente (Mohit). Combinação (a): não resolvido.
- **O que não aconteceu / ficou aberto:** nenhuma resposta de Wallisson nos snapshots; lista completa de códigos não enviada; combinação (a) sem veredito; não consta decisão de criar/não criar o código.
- **Tipo de erro:** T11 (pedido de informação); possível T2 (flags WTC) e T10.
- **Lição para o pipeline:** F20 (WTC gaps and invalid tax codes) cobre ausência de wage types/flags ambíguos, mas aqui o problema é de reconciliação com o WTC do cliente, que o pipeline não faz. NOVO: "WTC de compliance sem matriz de combinações de flags (Tax × SSNC × ECF × Pension) por categoria de wage type". Um check que liste as combinações presentes e justifique as ausentes (ex.: overtime sempre Tax+SS) teria respondido o ticket sem precisar de humano.

## HRBS-12483 — WTC Namíbia: flag de pensão divergente entre compliance e cliente
- **País / Cliente / Tipo / Prioridade:** Namíbia / Baker Hughes / Service Request / Medium (Production, Implementation).
- **Snapshots lidos:** 01 (PDF; exportação 2026-08-04).
- **Estado no último snapshot:** Open; Resolution Time "-11h" (já vencido). Assignee Wallisson.
- **Linha do tempo:**
  - ~2026-07-29: Daniel Kelvin Balogun relata que na WTC de compliance os códigos 62100, 62148, 62149, 62147, 62146 e 62961 são "Pension = YES", mas na WTC do cliente a pensão está "NO". Pede orientação.
  - ~2026-07-30: Ruchi Gupta pede ao Wallisson para verificar.
- **Problema relatado:** divergência de flag de pensão em 6 códigos entre nossa WTC e a do cliente.
- **Erro identificado:** não determinado. Pode ser erro nosso (flag Pension = Yes indevido) ou divergência do cliente (T10). O ticket não traz a base legal. Versão da WTC: não consta.
- **Causa raiz:** [INCERTO] indefinição sobre o que é "pensionável" na Namíbia (pensão de empregador/fundo privado vs SSC): o termo "Pension" na WTC pode estar sendo lido pelo cliente como outra coisa que SSC/ECF. Sem evidência no ticket.
- **Solução aplicada:** não resolvido no último snapshot.
- **O que não aconteceu / ficou aberto:** resposta de Wallisson; decisão sobre o flag; eventual versão nova da WTC; fonte legal.
- **Tipo de erro:** T2 (flag WTC), T10, T12 (sem fonte).
- **Lição para o pipeline:** F7 (WTC wage type tax codes wrong) e F20 cobrem flags/códigos de WTC, mas só verificam contra a autoridade tributária; não há coluna de "base legal por flag" para responder quando o cliente discorda. NOVO: "Flag de WTC sem base legal citada por linha". Um check que exija fonte para cada flag Yes de pensão teria permitido responder em minutos.

## HRBS-12101 — Amostras dos relatórios estatutários da Namíbia
- **País / Cliente / Tipo / Prioridade:** Namíbia / Baker Hughes / Service Request / Medium (Production, Implementation).
- **Snapshots lidos:** 16 (exportação 2026-08-12).
- **Estado no último snapshot:** Open; First Reply "-22d" e Resolution Time "-19d" (SLA estourado).
- **Linha do tempo:**
  - ~2026-07-21: Daniel Kelvin Balogun pede amostras ("urgente") de SSC Form Ten, PAYE 5 certificate e ETX; os dois links do Drive só têm arquivos de spec, sem samples.
  - ~2026-07-26: Manju Shetija atualiza o ticket (sem comentário visível).
- **Problema relatado:** não há samples dos formulários nas pastas entregues; só specs.
- **Erro identificado:** nenhum (pedido de informação/sample). Lacuna de entrega: o conjunto entregue não traz exemplos do formulário oficial.
- **Causa raiz:** [INCERTO] pipeline gera Report Specs, não samples; o cliente espera modelos preenchidos/em branco do formulário oficial.
- **Solução aplicada:** não resolvido; nenhuma resposta visível.
- **O que não aconteceu / ficou aberto:** resposta com samples ou explicação de que não existem; decisão sobre incluir samples de formulário oficial na entrega.
- **Tipo de erro:** T11.
- **Lição para o pipeline:** nenhum F-xx cobre isso. NOVO: "Entrega de Report Spec sem o formulário/sample oficial de referência". Um item de checklist no handover (link para o modelo oficial da autoridade, ou nota "não publicado") teria evitado o ticket. Obs.: o conjunto de relatórios aqui (SSC Form 10, PAYE 5, ETX) difere do que está em configuração (PAYE Return, G2N, SSC Return, ver HRBS-14605): ver padrões recorrentes.

## HRBS-12111 — Revisão da report matrix da Namíbia
- **País / Cliente / Tipo / Prioridade:** Namíbia / Baker Hughes / Service Request / Medium.
- **Snapshots lidos:** 06 (exportação 2026-08-06) e 10 (2026-08-10); conteúdo idêntico, só mudam os "days ago".
- **Estado no último snapshot:** Open; Resolution Time "-16d" (vencido). Assignee Wallisson.
- **Linha do tempo:**
  - ~2026-07-21: Daniel Kelvin Balogun pede revisão da report matrix (xlsx do cliente, ~102 kB), "em especial os relatórios estatutários".
  - ~2026-07-21: Pradeep Duraisamy acusa o recebimento e pede que Manju Shetija revise e apoie.
  - ~2026-07-22: Ruchi Gupta atualiza o ticket (sem texto).
- **Problema relatado:** pede revisão da matriz de relatórios do cliente; foco nos estatutários.
- **Erro identificado:** nenhum identificado (pedido de revisão); o conteúdo da matriz não consta no ticket.
- **Causa raiz:** não aplicável / não consta.
- **Solução aplicada:** não resolvido; nenhuma revisão registrada nos dois snapshots.
- **O que não aconteceu / ficou aberto:** parecer sobre a matriz; relatórios estatutários não confirmados como completos.
- **Tipo de erro:** T11; potencial T6 (escopo de relatórios) [INCERTO].
- **Lição para o pipeline:** nenhum F-xx. Em HRBS-14605 (mesmo cliente) descobriu-se que VET Levy e IT12E não existem, o que sugere que a matriz do cliente listava relatórios fora do que entregamos. NOVO: "Reconciliação entre report matrix do cliente e o escopo de report specs entregue". Um check "relatório da matriz ↔ spec entregue/descoped" (parente de F15) teria exposto isso em julho.

## HRBS-13602 — Contribuição SS do empregado (WT 2551) não reduz a base do Payroll Tax (Namíbia)
- **País / Cliente / Tipo / Prioridade:** Namíbia (entidade REF-LE-03-060) / Baker Hughes (BH Namibia) / Service Request / Medium.
- **Snapshots lidos:** 32 (exportação 2026-08-24).
- **Estado no último snapshot:** Open; Resolution Time "2d"; assignee Wallisson (reatribuído por Mohit).
- **Linha do tempo:**
  - ~2026-08-21: Daniel Kelvin Balogun abre o ticket: WT 2551 (SS Employee Share, teto NAD 99/mês) reduz o líquido, mas não a base do Payroll Tax (WT 2552). Alega que o próprio WTC documenta "Taxable base = Basic + Housing ... − SS Ee Pension Add" e que é prática padrão do PAYE namibiano. Evidência: caso isolado de março/2026; diferença de 29,70/mês = 99 × 30% (alíquota marginal), reproduzida em 4 empregados com dados limpos. Pede (1) confirmar se 2551 está flagado para reduzir a base, (2) corrigir, (3) reprocessar. Cita duas outras pendências abertas na mesma população: metodologia de anualização e constante de faixas desatualizada.
  - ~2026-08-24: Pradeep acusa o recebimento e pede a Mohit para revisar.
  - ~2026-08-24: Mohit Jain: "com a informação atual, não é dedução pré-imposto. 2551 = MSD EE Contribution" (cita CCG, link do Google Docs, e screenshot). Reatribui a Wallisson para checar e resolver.
- **Problema relatado:** PAYE calculado sem deduzir a contribuição SS do empregado (diferença de 29,70 por empregado = 99 × 30%).
- **Erro identificado:** conflito entre artefatos, não resolvido: o WTC do cliente/descrição do WT diz que a SS Ee reduz a base; o CCG (segundo Mohit) diz que 2551 é MSD EE e não pré-imposto. Quem está certo não foi demonstrado no ticket. Sem fonte legal em nenhum dos lados. Versões dos artefatos: não constam.
- **Causa raiz:** [INCERTO] ou o WTC/design descreve uma fórmula (SS Ee Pension Add) que não bate com o CCG, ou o cliente confunde a contribuição MSD (que Mohit afirma não ser pré-imposto) com uma dedução previdenciária. Fórmula citada pelo cliente vem do "WTC" (de quem não está claro: "Baker Hughes's own WTC" vs WTC de compliance). Em termos de etapa: sincronização entre artefatos/pesquisa.
- **Solução aplicada:** não resolvida. Posição provisória de Mohit: não é pré-imposto.
- **O que não aconteceu / ficou aberto:** resposta de Wallisson; base legal (Income Tax Act da Namíbia, tratamento de contribuições SSC/MSD na base do PAYE); verificação se o texto da fórmula no WTC precisa ser corrigido; os tickets de anualização e de constante de faixas não constam neste grupo.
- **Tipo de erro:** T2, T7, T8, T12; T10 possível.
- **Lição para o pipeline:** F45 (No cross-artifact consistency on facts and versions) e F37 (taxa/regra reescrita em prosa contradizendo o próprio cálculo) são os mais próximos; F7 cobre tax codes. Escapou porque nada compara a fórmula descrita no WTC com a regra do CCG para cada deduction que reduz base. NOVO: "Dedução pré-imposto: tratamento no CCG × fórmula do WTC × flag do WT". Um check que, para cada WT de contribuição do empregado, compare os três e exija fonte teria pegado a divergência.

## HRBS-14605 — Namíbia: confirmação de configuração dos relatórios estatutários
- **País / Cliente / Tipo / Prioridade:** Namíbia / Baker Hughes (BH Namibia) / Service Request / Medium.
- **Snapshots lidos:** 86 (exportação 2026-09-25).
- **Estado no último snapshot:** Open; Resolution Time "-7d" (vencido); assignee Wallisson.
- **Linha do tempo:**
  - ~2026-09-15: Daniel Kelvin Balogun pergunta o status de configuração de: Monthly PAYE Return (NamRA, 20 dias após o fim do mês, ano fiscal mar-fev); SSC Contribution Return (taxa/teto: "0,9%/0,9% até ~NAD 11.000" vs "valor fixo"); VET Levy Return (1% empregador, Namibia Training Authority); IT12E e IT14E (até 30/jun).
  - ~2026-09-15: Mohit Jain: "está em desenvolvimento".
  - ~2026-09-15: Daniel pede data de entrega esperada.
  - ~2026-09-18: Katrin Rudi: em configuração Monthly PAYE Return, Gross to Net e SSC Contribution Return; Payslip já configurado e em revisão com Compliance; relatórios em configuração previstos para 25/set, depois revisão de Compliance. Pede que Mohit confirme VET Levy e IT12E.
  - ~2026-09-18: Mohit Jain: "só temos esses relatórios; não temos VET Levy Return nem IT12E".
  - ~2026-09-24: Manju Shetija atualiza o ticket (sem texto visível).
- **Problema relatado:** o cliente quer saber o status dos relatórios e a taxa/teto da SSC aplicada pela Mercans.
- **Erro identificado:** nenhum erro de artefato demonstrado; lacunas de cobertura: VET Levy Return, IT12E (e, por omissão, IT14E) não existem. A pergunta da taxa/teto SSC (0,9% sobre teto ~NAD 11.000 segundo o cliente) e a do ano fiscal mar-fev não foram respondidas. Nota: 2551 tem teto NAD 99/mês (HRBS-13602), compatível com 0,9% × 11.000 = 99, mas o ticket não confirma isso.
- **Causa raiz:** [INCERTO] o escopo de relatórios da Namíbia (SSC Form 10, PAYE 5, ETX, HRBS-12101) não coincide com a lista que o cliente espera (PAYE Return, SSC Return, VET Levy, IT12E, IT14E): nomes e escopo divergem desde a etapa de definição de escopo.
- **Solução aplicada:** não resolvido; informação de status prestada por Mohit e Katrin.
- **O que não aconteceu / ficou aberto:** confirmação da taxa/teto SSC (com fonte); confirmação do alinhamento ao ano fiscal mar-fev; VET Levy (aplicabilidade e limite de folha) e IT12E/IT14E sem decisão de escopo; prazo de entrega; "o que é necessário do lado do cliente" não respondido.
- **Tipo de erro:** T6 (escopo), T11, T12.
- **Lição para o pipeline:** F15 (Removed artifact without descoping decision) e F24 (Stale scope/mandate document) são os mais próximos: a decisão de não cobrir VET Levy/IT12E/IT14E não estava registrada de forma que o suporte pudesse citar. NOVO: "Relatórios estatutários do país sem lista pública de 'coberto / não coberto + motivo'". Um check C20 aplicado à lista de relatórios do país (CCG) teria gerado a resposta pronta.

---

# CONGO (CONGO-BRAZZAVILLE) E GABÃO

## HRBS-12110 — Revisão da report matrix do Congo
- **País / Cliente / Tipo / Prioridade:** Congo / Baker Hughes (Baker Hughes Congo) / Service Request / Medium.
- **Snapshots lidos:** 20 (exportação 2026-08-13).
- **Estado no último snapshot:** Open; Resolution Time "-20d" (vencido); assignee Wallisson.
- **Linha do tempo:**
  - ~2026-07-21: Daniel Kelvin Balogun pede revisão da "Reporting Matrix – Congo" (xlsx, ~417 kB) para dizer se está boa para ir ao cliente para revisão.
  - ~2026-07-21: Pradeep Duraisamy atribui a Wallisson.
- **Problema relatado:** validação de uma matriz de relatórios antes de enviar ao cliente.
- **Erro identificado:** nenhum identificado (conteúdo da matriz não consta).
- **Causa raiz:** não consta.
- **Solução aplicada:** não resolvido; sem resposta nos snapshots.
- **O que não aconteceu / ficou aberto:** parecer go/no-go; qualquer ajuste à matriz.
- **Tipo de erro:** T11.
- **Lição para o pipeline:** mesmo caso de HRBS-12111: NOVO "Reconciliação entre report matrix do cliente e escopo de report specs", ver acima.

## HRBS-12472 — Payslips Congo e Gabão: campos situação familiar, filhos e partes
- **País / Cliente / Tipo / Prioridade:** Congo e Gabão / Baker Hughes / Service Request / Medium.
- **Snapshots lidos:** 13 (exportação 2026-08-11).
- **Estado no último snapshot:** SLA Exempt; Resolution Time "Paused"; assignee Wallisson (reatribuído por Manju para o Congo).
- **Linha do tempo:**
  - ~2026-07-29: Daniel Kelvin Balogun: o assessor tributário do cliente confirmou que estado civil, número de filhos e número de partes devem constar no payslip de Congo e Gabão "por recomendação do país". Pede que a equipe estatutária confirme se pode adicionar.
  - ~2026-07-29: Pradeep pede a Manju para confirmar se são obrigatórios.
  - ~2026-07-30: Daniel cobra resposta.
  - ~2026-08-10: Manju Shetija: para o Gabão serão exibidos estado civil e nº de partes; nº de filhos não é mencionado nem exigido, e pede o motivo. Atribui o ticket a Wallisson para confirmação no Congo.
- **Problema relatado:** payslips sem campos que o cliente diz serem recomendados/obrigatórios.
- **Erro identificado:** nenhum identificado; requisito do cliente (T10/T9). Quem decide a obrigatoriedade legal de cada campo não consta; a posição do Gabão (Manju) foi dada sem fonte no ticket.
- **Causa raiz:** o payslip padrão não prevê esses campos; a necessidade vem do assessor do cliente. O ticket não traz base legal para Congo.
- **Solução aplicada:** Gabão: decisão de exibir estado civil e partes (sem filhos), por Manju (~2026-08-10). Congo: não resolvido.
- **O que não aconteceu / ficou aberto:** resposta do Wallisson para o Congo; resposta do cliente sobre por que "nº de filhos" é necessário; base legal da obrigatoriedade em ambos; versão do payslip alterada: não consta.
- **Tipo de erro:** T9, T10, T11.
- **Lição para o pipeline:** nenhum F-xx direto. Relacionado a F43 (populações/campos especiais) e F45 (consistência entre artefatos): `correcoes.md` (Congo, design, 2026-08-28) registra que o design CG usava 58204 como flag bilateral e que 58204 = "No Child" (0,5 parte) falta no CCG do Congo. Ou seja, o conceito filhos/partes estava subdocumentado no CCG também. NOVO: "Campos que alimentam o cálculo (estado civil, filhos, partes) sem espelho no Payslip Spec". Um check CCG → DD → Payslip para campos que entram no imposto teria incluído "partes" no payslip por padrão.

## HRBS-13841 — CAMU ausente no WTC de compliance do Congo
- **País / Cliente / Tipo / Prioridade:** Congo / Baker Hughes / Service Request / Medium.
- **Snapshots lidos:** 33 (exportação 2026-08-27) e 35 (2026-08-31).
- **Estado no último snapshot:** Pending on reporter (Resolution Time "Paused"); assignee Wallisson.
- **Linha do tempo:**
  - ~2026-08-27: Daniel Kelvin Balogun: o WTC do cliente tem "CAMU Health Insurance (Employee)" aplicado como % de uma base (efetivo ~0,5% sobre ganhos regulares, ~0,46-0,47% em nov/25 no GATSE); a base exata exige confirmação; o WTC de compliance não tem CAMU. Pergunta se é o mesmo que "CG Health Insurance EE" do WTC de compliance.
  - ~2026-08-27: Pradeep atualiza o ticket.
  - ~2026-08-27: Wallisson responde (autoria dele): é a CAMU solidarité (0,5% sobre a fração do salário acima de 500.000 XAF), não a CAMU empregado de 2,27%. Fonte: autoridade CAMU Congo (camu-congo.fr): são dois fluxos separados: contribuição 4,55% empregador / 2,27% empregado (6,82% combinados) e, separadamente, 0,5% de "contribution de solidarité nationale" sobre a fração acima de 500.000 XAF. A fórmula do cliente bate exatamente com a segunda.
  - ~2026-08-31: Daniel pergunta se os 4,55%/2,27% são estatutários, já que o G2N do cliente não os tem mas o G2N do HRB sim.
- **Problema relatado:** a CAMU do WTC do cliente não tem correspondente óbvio no WTC de compliance.
- **Erro identificado:** dois pontos. (1) O WTC do cliente rotula a solidarité 0,5% como "CAMU Health Insurance (Employee)", rótulo errado do cliente (T10/T3). (2) O ticket não esclarece se nosso WTC contém o item "solidarité" separado; a pergunta implica que não, mas Wallisson não diz que será adicionado [INCERTO]. O WTC/G2N do HRB aplica 2,27%, que o cliente não aplica; se 2,27% é estatutário está sem resposta final (Wallisson já citou a fonte CAMU, mas Daniel perguntou de novo).
- **Causa raiz:** o WTC do cliente nomeia contribuição de nome diferente; nossa WTC separa os dois fluxos de forma que o cliente não reconhece. Etapa: comunicação/mapeamento WTC cliente ↔ compliance. Relação com `correcoes.md` (Congo, design, 2026-08-28): o design CG usava limiar de solidariedade anualizado (6.000.000) e divisor 12, corrigido para 500.000, o mesmo limiar deste ticket, um dia depois da resposta do Wallisson.
- **Solução aplicada:** esclarecimento por Wallisson (~2026-08-27); design corrigido em 2026-08-28 conforme `correcoes.md` (relação [INCERTO]).
- **O que não aconteceu / ficou aberto:** confirmar para o solicitante que 2,27%/4,55% são estatutários (pergunta de 08-31); decisão de adicionar WT de solidarité na WTC de compliance; correção do rótulo no WTC do cliente.
- **Tipo de erro:** T3, T10, T12.
- **Lição para o pipeline:** F20 (WTC gaps) cobre ausência de wage type; F18 (stale law references) não se aplica. Escapou porque nosso WTC não tinha uma coluna "nome comum usado por clientes/local" para mapear CAMU solidarité. NOVO: "Contribuição com duas camadas (taxa geral + solidarité com limiar) sem WT separado e sem nota de equivalência". Um check de ' toda contribuição com limiar tem WT próprio' teria pegado.

## HRBS-14054 — TUS subestimado: gross-up do car allowance ausente no g2n do cliente (Congo)
- **País / Cliente / Tipo / Prioridade:** Congo / Baker Hughes (BH Congo; campos Client/Environment não preenchidos no ticket) / Service Request / Medium.
- **Snapshots lidos:** 37 (exportação 2026-09-02).
- **Estado no último snapshot:** Open; assignee Wallisson; Mohit Jain atualizou ~7h antes (sem comentário visível).
- **Linha do tempo:**
  - ~2026-09-01: Daniel Kelvin Balogun abre o ticket: TUS (7,5% do Taxable Total) menor que o esperado para empregados com car allowance de valor líquido garantido (500.000/625.000/750.000 por grau). O HRB faz o gross-up corretamente; o cliente rastreia o gross-up numa coluna separada ("Gross up"). Em 2 empregados a coluna está vazia e o car allowance fica em 500.000 sem gross-up, subestimando Taxable Total e TUS. Outros achados: 2 empregados com problema de taxa de produtividade já sinalizado; 3 com "SS Employee Arrears" (dado do cliente, não levantado). Pergunta: "o gross-up deve ser somado ao Unique tax para o Congo?"
  - ~2026-09-02: Mohit Jain atualiza o ticket (sem texto).
- **Problema relatado:** diferença de TUS entre g2n do HRB e do cliente.
- **Erro identificado:** erro de dados do cliente (gross-up ausente em 2 empregados) = T10. Nosso artefato calcula corretamente, segundo o próprio ticket. A pergunta aberta (T7) é se o gross-up compõe a base do TUS (a resposta lógica seria sim, pois entra no Taxable Total, mas não consta no ticket). Taxa de 7,5%: sem fonte no ticket.
- **Causa raiz:** estrutura diferente entre g2n do cliente (coluna separada) e do HRB (gross-up embutido) + dado faltando no cliente. Etapa: comunicação/dados do cliente.
- **Solução aplicada:** não resolvido; diagnóstico no próprio texto do ticket.
- **O que não aconteceu / ficou aberto:** resposta formal à pergunta; fonte da base do TUS; os dois outros achados ficaram fora do ticket.
- **Tipo de erro:** T10, T7, T12.
- **Lição para o pipeline:** F43 (Special populations not covered systematically) é o mais próximo (benefício com net-guaranteed/gross-up); F42 (worked examples typed instead of computed) seria o check: um exemplo calculado de net-to-gross de allowance com TUS na CCG teria respondido. NOVO se não houver exemplo: "Base do TUS: inclusão de gross-up de benefícios com líquido garantido".

## HRBS-14055 — Taxa de ocupação e taxa regional são regulatórias no Congo?
- **País / Cliente / Tipo / Prioridade:** Congo / Baker Hughes (BH Congo) / Service Request / Medium.
- **Snapshots lidos:** 38 (exportação 2026-09-02).
- **Estado no último snapshot:** Open; assignee Wallisson; Pradeep atualizou ~8h antes (sem texto).
- **Linha do tempo:**
  - ~2026-09-01: Daniel Kelvin Balogun pergunta se "occupancy tax" e "region tax" são regulatórios no Congo; aparecem no g2n do cliente (anexo: pay register jan/26, 3 MB; link do WTC).
  - ~2026-09-02: Pradeep atualiza o ticket.
- **Problema relatado:** itens do g2n do cliente sem correspondente conhecido no WTC de compliance.
- **Erro identificado:** nenhum (pedido de informação), possível lacuna do WTC se forem estatutários [INCERTO].
- **Causa raiz:** não consta.
- **Solução aplicada:** não resolvido.
- **O que não aconteceu / ficou aberto:** veredito estatutário com fonte; decisão de incluir/excluir da WTC; eventual regra de escopo. Resposta de Wallisson não consta.
- **Tipo de erro:** T11, T6 possível, T12.
- **Lição para o pipeline:** F20 e F2 (out-of-scope codes leaked): os dois lados do mesmo risco (faltar vs sobrar). NOVO se confirmado: "Tributos locais/municipais (ocupação, regional) fora do radar da pesquisa estatutária de nível nacional". Um domínio "taxas locais/regionais" no sweep de 13 domínios do hunter teria cobrado.

---

# CÔTE D'IVOIRE

## CT-A-620 — CI: Specifications (artigo de KB, não é ticket de erro)
- **País / Cliente / Tipo / Prioridade:** Côte d'Ivoire / sem cliente / artigo da Knowledge Base do projeto Compliance / n.a.
- **Snapshots lidos:** 21 (exportação 2026-08-14). Autor Mohit Jain; criado ~2026-08-05, atualizado ~2026-08-07. Sub-artigos CT-A-621 (Taxable Gross), CT-A-622 (Gross), CT-A-623 (Tax Table), atualizados em 05/08/2026.
- **Estado no último snapshot:** publicado ("Visible to article readers").
- **Linha do tempo:** só a criação/atualização acima. Não há comentários.
- **Problema relatado:** nenhum (documento de especificação das regulações CI no motor, IDs 9384011 a 9384181 e flags 58238, 58202, 58295, 58203, 58215, 58216 e Family Situation Factor 58205).
- **Erro identificado:** nenhum no artigo. Duas observações para uso posterior: (a) o texto exportado da tabela é fragmentado; leitura de valores exige o original [INCERTO]. (b) A leitura dos valores é consistente com os números dados em HRBS-14996: pensão com piso 900.000 (12 × 75.000) e teto 40.500.000 (12 × 3.375.000) anuais; base PF/maternidade/AT 840.000 (12 × 70.000); apprentice (58216 = 2) com piso = teto = 450.000. Sem fonte legal no artigo.
- **Causa raiz:** n.a. Mas ver HRBS-14996: o comportamento do GTN para um empregado acima do teto bate exatamente com a linha de apprentice (450.000/12 = 37.500 × 6,3% = 2.362,5 ≈ 2.363; × 7,7% = 2.887,5 ≈ 2.888; × 5% = 1.875; × 0,75% = 281; × 3% = 1.125). [INCERTO] ou o HR field 58216 foi preenchido como 2 para esse empregado, ou a asserção de banda escolheu a regra errada.
- **Solução aplicada:** n.a. `correcoes.md` (2026-08-14, Costa do Marfim / design) registra que o design CI v1.0 teve defeito de 12× em faixas/pisos/tetos, corrigido na v1.1 com valores anuais declarados. Se o artigo reflete v1.0 ou v1.1 não consta [INCERTO].
- **O que não aconteceu / ficou aberto:** vigência e fonte dos valores não estão no artigo; confirmar que o CE (9,2% expatriados, asserção Worker Type = 1 na linha 131 da spec) está implementado como wage type no GTN (Wallisson diz que não existe linha de CE).
- **Tipo de erro:** nenhum direto; contexto para T3/T7/T8 de HRBS-14996.
- **Lição para o pipeline:** F46 (Technical design not derived from the research) e F37: o design/spec foi escrito sem checagem automática de valores contra os fatos. NOVO: "Teste de regressão do design CI com um caso de empregado acima do teto". Um caso de teste de cada banda (inclusive apprentice vs local) teria exposto o comportamento antes de ir a produção.

## HRBS-14714 — Aplicabilidade do ITS e faixas/RICF para Baker Hughes Côte d'Ivoire
- **País / Cliente / Tipo / Prioridade:** Côte d'Ivoire / Baker Hughes / Service Request / Medium (Production, Live/BAU).
- **Snapshots lidos:** 75 (exportação 2026-09-16).
- **Estado no último snapshot:** Open; First Reply "6h"; Resolution Time "4d"; assignee Wallisson. Header do PDF indica "1 of 6": o snapshot pode estar incompleto [INCERTO].
- **Linha do tempo:**
  - ~2026-09-15/16: Sivaranjani Subbarayula pede confirmação se o ITS é aplicável/deve ser retido, e as faixas/alíquotas atuais e o tratamento do RICF, para validar a config do WTC. Anexo: pay register de janeiro (24 kB).
  - ~2026-09-16: Mohit Jain atualiza o ticket (sem texto visível).
- **Problema relatado:** o cliente/BAU quer validar a WTC do ITS contra posição confirmada de compliance. Observação: o ticket expande ITS como "Import sur les Treatments et Salaries", o nome correto é Impôt sur les Traitements et Salaires.
- **Erro identificado:** nenhum identificado neste ticket. A mesma questão aparece em HRBS-14996 (aberto ~6 dias depois pela mesma pessoa), onde nossa resposta confirmou o ITS e o cálculo (1.940.670,66 → 417.760,96 − RICF 11.000 = 406.760,96).
- **Causa raiz:** não aplicável. [INCERTO] houve duplicação de tickets (14714 e 14996) sobre o mesmo tema.
- **Solução aplicada:** não consta resposta neste ticket. Na prática respondido em HRBS-14996 [INCERTO se vinculados].
- **O que não aconteceu / ficou aberto:** resposta formal (faixas e RICF com fonte) neste ticket; fechamento/vinculação.
- **Tipo de erro:** T11.
- **Lição para o pipeline:** nenhum F-xx. NOVO (processo): "Tickets duplicados sobre o mesmo assunto entre triagem e Compliance". Não é falha do pipeline de artefatos; teria sido evitado por busca prévia de tickets abertos do mesmo cliente/país.

## HRBS-14996 — CI: "Single Tax Regime" e isenção de ITS; tetos CNPS; defeitos do GTN
- **País / Cliente / Tipo / Prioridade:** Côte d'Ivoire (entidade REF-LE-03-105; campo Client "No client" no ticket) / Baker Hughes (Baker Hughes EHO Ltd / sucursal) / Service Request / Medium.
- **Snapshots lidos:** 80 (exportação 2026-09-23), 88 (2026-09-25) e 91 (2026-09-28). Comentários acumulam de forma consistente entre os três.
- **Estado no último snapshot:** Pending on reporter (Resolution Time "Paused"); assignee Wallisson; cliente escalou "ao Marko".
- **Linha do tempo:**
  - ~2026-09-22: Sivaranjani Subbarayula abre: o sistema calcula ITS, mas a população estaria no "Single Tax Regime" (impôt synthétique/régime simplifié), sem retenção de PIT na folha. Pede a lógica de flag para distinguir empregados STR dos do regime padrão. Anexa GTN do sistema e pay register do cliente. Pede atribuição a Wallisson.
  - ~2026-09-22: Sivaranjani acrescenta: teto CNAMGS/FNH é 70.000 no sistema Mercans e 75.000 no pay register do cliente. Govind Thakur anexa os pay registers de jan e fev/2026.
  - ~2026-09-22/23: Wallisson (resposta 1): (1) não configurar flag STR; ITS continua devido: o impôt des microentreprises (e o régime de l'entreprenant) é "libératoire des autres impôts et taxes, à l'exclusion de l'ITS ... aussi bien à la charge des salariés que de l'employeur" (DGI, Le Système Fiscal Ivoirien); substitui patente, BIC/BNC e TVA da entidade; além disso, inaplicável de fato: teto de 200.000.000 XOF de faturamento anual vs 18 empregados e 46.100.070 XOF de remuneração só em janeiro. Se o cliente insistir, pedir o instrumento específico (convention d'établissement, agrément ou ruling DGI): "nome de regime não é isenção". (2) Teto 70.000 correto para PF (5%), maternidade (0,75%) e AT/MP (2–5%); 75.000 é o SMIG, piso da assiette; pensão com teto 3.375.000 (45 × SMIG); fonte CLEISS CI, atualizada 2025-01-01. O arquivo do cliente é inconsistente (17 empregados a 75.000, 1 a 70.000); "CNAMGS" e "FNH" são órgãos do Gabão; os valores são AT/MP 3% e PF+AM 5,75%. (3) Defeitos do GTN (REF-P201-861, janeiro), a abrir em tickets separados: ver "Erro identificado".
  - ~2026-09-23: Sivaranjani: "isto é o que recebemos do cliente sobre confirmação de ITS".
  - ~2026-09-23: Wallisson (resposta 2): precisa do cliente: (1) "Déclaration du Prestataire de service" trimestral (Impôt BIC Pétrole/Gaz, e-impots.gouv.ci), (2) prova de "nationalité étrangère" (Annexe fiscale 2019, art. 26), para confirmar se a entidade se enquadra no régime des prestataires de services pétroliers e não no impôt synthétique. Confirmado, configura-se o flag.
  - ~2026-09-25: Sivaranjani anexa 3 PDFs (declaração de existência fiscal; resolução de 24/11/2023; resposta a pedido de reembolso) e pede para habilitar o flag. Govind Thakur: um documento ainda pendente no cliente.
  - ~2026-09-25: Wallisson (resposta 3): nacionalidade estrangeira confirmada (sucursal, D1020, sede nas Bermudas; resolução do board de 24/11/2023: Baker Hughes EHO FZE, Jebel Ali Free Zone, EAU). Regime confirmado para 2025: carta DGI n° 0984/MFB/DGI/DGE de 19/08/2025 aceita o IFPGAZ declarado e pago por Baker Hughes EHO Ltd (NCC 0211442C) sob o régime des prestataires de services pétroliers. Confirmação do flag virá com a declaração IFPGAZ de 2026.
  - ~2026-09-28: Sivaranjani pede a versão detalhada em inglês ("não precisamos da resposta de IA"), pergunta se os documentos são necessários todo ano, e diz que o cliente está firme na isenção e escalou para Marko.
- **Problema relatado:** premissa do cliente de que o regime fiscal único isenta os empregados de ITS; pedido de flag; teto 70.000 vs 75.000.
- **Erro identificado:**
  1. Cliente: "Single Tax Regime isenta ITS" é errado (impôt synthétique exclui ITS por lei). A posição possível é outra: régime des prestataires de services pétroliers (IFPGAZ), cuja consequência legal para o ITS dos empregados não é explicada no ticket (sem fonte no ticket do porquê da isenção) [INCERTO]. Wallisson mudou o enquadramento entre resposta 1 e 3 (de "ITS devido, sem flag" para "regime confirmado para 2025; flag a confirmar"), o que o solicitante viu como inconsistência.
  2. Cliente: teto 75.000 errado (é o SMIG, piso). Rótulos "CNAMGS/FNH" do cliente são do Gabão.
  3. Nosso GTN/WTC (referência REF-P201-861, janeiro), conforme Wallisson: (a) pensão CNPS lançada e estornada (2517 +122.262 e 2556 −122.262; 2537 +149.432 e 2566 −149.432), logo nenhuma pensão cobrada de nenhum lado (o cliente cobra 120.372,25/147.121,64); (b) empregado acima do teto de pensão com valores errados (sistema EE 2.363, ER 2.888, PF 1.875, AM 281, AT/MP 1.125; correto 212.625/259.875/3.500/525/2.100); (c) rótulos de WT errados: 2531 diz 5,75% mas paga PF 5%; 2538 diz Work Accident 0,75% mas paga Maternité; 2560 paga o AT/MP real; 2569 rotulado "EIS" (inexistente na CI) paga o CN empregador 1,2%; (d) sem linha CE: expatriados (9,2%) subcobrados; (e) bases: o cliente exclui 30.000 de transporte das bases ITS/CNPS (Abidjan, arrêté de 30/01/2020) e a ajuda de moradia da base ITS; o motor não aplica nenhum. Aritmética do ITS correta.
- **Causa raiz:** (1) cliente confunde nome de regime com isenção; (2) cliente conflita piso e teto; (3) [INCERTO] defeitos do GTN têm origem na configuração do motor/design CI (spec CT-A-620) e não na pesquisa: os números de (b) batem com a linha "apprentice" da spec, o que sugere flag 58216 = 2 ou asserção errada. Etapa: design/configuração e QA do GTN (a pesquisa/CCG estava certa nos tetos). Rótulos errados = construção do WTC/WT.
- **Solução aplicada:** parcial. Respostas 1 a 3 do Wallisson; teto 70.000 confirmado com fonte; flag de isenção não criado; defeitos do GTN apontados "para tickets separados" (abertura não consta).
- **O que não aconteceu / ficou aberto:** declaração IFPGAZ 2026 e documento ainda pendente no cliente; resposta em inglês mais detalhada; resposta sobre exigência anual de documentos; tickets de defeito do GTN; correção de rótulos; criação de WT para CE; parametrização do transporte por localidade e decisão sobre moradia; base legal escrita da isenção do ITS sob o regime petroleiro; resolução da escalação (Marko).
- **Tipo de erro:** T10, T1 (cliente: teto errado), T2, T3, T7, T8, T12.
- **Lição para o pipeline:** F41 (Research never tested against an independent oracle) e F43 (Special populations not covered) são os mais próximos: população especial (prestador petroleiro estrangeiro, expatriados, apprentice) sem testes. F46 (design não derivado da pesquisa) cobre os números errados na faixa apprentice. Escapou porque o GTN foi liberado sem comparação com pay register de um cliente. NOVO: "GTN sem teste de conservação (lançamento e estorno que zeram contribuição) e sem rótulo ↔ taxa paga". Um check automático que verifique que Total Deductions/Employer Contributions incluem cada WT de contribuição configurado, e que rótulo = taxa efetivamente aplicada, teria pegado (a)-(d).

---

# Tabela-resumo

| ID | País | Tipo(s) | Artefato | Resolvido? | F-xx / NOVO |
|---|---|---|---|---|---|
| HRBS-12072 | Namíbia | T11, T2, T10 | WTC compliance | Parcial (combinação b confirmada; a em aberto) | F20 + NOVO: matriz de combinações de flags |
| HRBS-12483 | Namíbia | T2, T10, T12 | WTC compliance (flags pensão 62100/62146-9/62961) | Não | F7 + NOVO: flag sem base legal |
| HRBS-12101 | Namíbia | T11 | Report Specs (SSC Form 10, PAYE 5, ETX) | Não | NOVO: spec sem sample/formulário oficial |
| HRBS-12111 | Namíbia | T11, T6 [INCERTO] | Report matrix do cliente | Não | NOVO: reconciliação matriz × escopo |
| HRBS-13602 | Namíbia | T2, T7, T8, T12 | CCG vs WTC (WT 2551/2552) | Não (posição provisória: não é pré-imposto) | F45, F37, F7 + NOVO: dedução pré-imposto |
| HRBS-14605 | Namíbia | T6, T11, T12 | Report Specs/relatórios (PAYE, SSC, VET, IT12E/IT14E) | Parcial (status informado; VET/IT12E inexistentes) | F15, F24 + NOVO: lista coberto/não coberto |
| HRBS-12110 | Congo | T11 | Report matrix do cliente | Não | NOVO: reconciliação matriz × escopo |
| HRBS-12472 | Congo / Gabão | T9, T10, T11 | Payslip | Gabão sim (estado civil + partes); Congo não | F43/F45 + NOVO: campos de cálculo sem espelho no payslip |
| HRBS-13841 | Congo | T3, T10, T12 | WTC compliance (CAMU solidarité) | Parcial (esclarecimento dado; pergunta 2,27% e inclusão no WTC abertas) | F20 + NOVO: contribuição em duas camadas |
| HRBS-14054 | Congo | T10, T7, T12 | WTC/G2N (TUS e gross-up car allowance) | Não | F43, F42 + NOVO: base do TUS |
| HRBS-14055 | Congo | T11, T6, T12 | WTC (occupancy/region tax) | Não | F20/F2 + NOVO: taxas locais |
| CT-A-620 | Côte d'Ivoire | n.a. (spec; contexto de T3/T7/T8) | Spec CI (regulações) | n.a. | F46 + NOVO: teste de regressão por banda |
| HRBS-14714 | Côte d'Ivoire | T11 | WTC (ITS, RICF) | Não (tratado em 14996) | NOVO (processo): ticket duplicado |
| HRBS-14996 | Côte d'Ivoire | T10, T1, T2, T3, T7, T8, T12 | GTN/WTC CI, flag de isenção ITS | Parcial | F41, F43, F46 + NOVO: teste de conservação e rótulo ↔ taxa |

Total: 14 tickets + 1 artigo de KB (CT-A-620).

# Padrões recorrentes no grupo

- **Divergência WTC do cliente × WTC de compliance sem mapeamento de nomes e flags:** 12072, 12483, 13841, 14055, 14996. O cliente usa rótulos próprios ("CAMU Health Insurance (Employee)" para solidarité; "CNAMGS/FNH" na CI, órgãos do Gabão) e flags diferentes (pensão). O erro quase nunca é nosso; o custo de triagem é alto. Falta uma coluna de equivalências e uma base legal por flag.
- **Escopo de relatórios sem lista pública "coberto / não coberto":** 12101, 12111, 12110, 14605. Namíbia entrega SSC Form 10/PAYE 5/ETX em specs e o status fala em PAYE Return/SSC Return/G2N; VET Levy e IT12E não existem e só foi dito depois de ~2 meses.
- **Piso, teto e anualização (12×) confundidos:** 14996 (75.000 SMIG = piso vs 70.000 teto); CT-A-620 e `correcoes.md` de 2026-08-14 (defeito de 12× em pisos/tetos do design CI) e 2026-08-28 (limiar de solidariedade do Congo anualizado). O GTN da CI mostra valor de linha "apprentice" (450.000/12) aplicado a empregado acima do teto. Falta teste por banda no design.
- **Defeitos do GTN encontrados só por conferência manual contra pay register do cliente:** pensão CNPS lançada e estornada, rótulos de WT não batendo com a taxa, CE ausente (14996); conflito de fórmula entre CCG e WTC (13602). Nenhum check automático de conservação/consistência rótulo ↔ taxa.
- **Pedidos de isenção/regra baseados no nome do regime, não em instrumento:** 14996. A resposta correta exigiu o instrumento (carta DGI, IFPGAZ) e é por ano (2025 confirmado, 2026 pendente). Cuidado: a mudança de enquadramento entre as respostas 1 e 3, sem explicar a consequência legal para o ITS, gerou atrito com o solicitante.
- **Fila sem dono ou sem resposta visível:** 12072, 12101, 12110, 12111, 12483, 14055, 14054 (e metade de 14714) com SLA negativo e sem comentário do Wallisson nos snapshots; duplicação 14714 × 14996. Não é falha de pesquisa; é de processo.
- **Perguntas de "é estatutário?" sem base citada no ticket:** 13841 (2,27%/4,55%), 14054 (TUS 7,5%, gross-up), 14055 (ocupação/região), 14605 (SSC 0,9%/NAD 11.000). Em 13841 e 14996 a fonte foi dada (camu-congo.fr; CLEISS, DGI), mas nas outras não consta.
- **Campos que alimentam o cálculo e sumiram do Payslip/CCG:** 12472 (estado civil, filhos, partes), com a correção de 2026-08-28 em `correcoes.md` (58204 "No Child" falta no CCG do Congo).
