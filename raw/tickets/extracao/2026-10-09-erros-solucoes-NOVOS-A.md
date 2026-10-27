# Erros e soluções: lote NOVOS-A (43 tickets: CT-* e HRBS-*)

- **Lote:** NOVOS-A
- **Data da análise:** 2026-10-09
- **Nota:** Tickets atribuídos a nós obtidos pela API do YouTrack em 2026-10-09; não constavam da análise de 2026-10-08.
- **Fonte:** `raw/tickets/api/2026-10-09/<ID>.md` (metadados, descrição, todos os comentários, nomes dos anexos). Anexos e links do Google Docs não foram abertos: o que está só no link aparece como "não consta".
- **IDs (43):** CT-3116, CT-3271, CT-3344, CT-3349, CT-3402, CT-3428, CT-3510, CT-3608, CT-3648, CT-3661, CT-3700, CT-3701, CT-3792, CT-3842, CT-3887, CT-3892, CT-3920, CT-3929, CT-3932, CT-3943, CT-3945, CT-3957, CT-4005, CT-4008, CT-4039, CT-4076, CT-4078, CT-4136, CT-4169, CT-4322, CT-4391, CT-617, CT-70, HRBS-10915, HRBS-11413, HRBS-117, HRBS-11736, HRBS-11790, HRBS-118, HRBS-11806, HRBS-11814, HRBS-11864, HRBS-11891.
- **Convenções:** "Estado atual" = campo Status do YouTrack. Sem nomes/IDs de empregados (não aparecem neste lote). Afirmações jurídicas que são só do texto do ticket vêm com a fonte que o ticket dá; o que é opinião minha está marcado [INCERTO]. Os CT-* são tickets internos de research (muitas respostas são só link para Google Docs que não consta aqui).
- **Tickets sem conteúdo analisável** (só título/metadados): ver lista no fim; as seções abaixo cobrem os 33 restantes. Os tickets com só um link no comentário têm seção curta.

---

## CT-3116 — PT: Youngster Tax (IRS Jovem) e redução de SS por primeiro emprego / desemprego de longa duração
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** PT / sem cliente / Research task (epic Regulation Gap) / Analysis Completed / 2025-04-15 / 2025-08-08
- **Linha do tempo:**
  - 2025-04-15, Bazil Marema: abre a pergunta (elegibilidade, processamento em folha, simulações, relatórios afetados) e cita três links (gov.pt redução SS jovens à procura do primeiro emprego; PwC tax guide 2025 SS; gov.pt "novo modelo de IRS Jovem em 2025").
  - 2025-08-08, Wallisson: entrega documento próprio sobre Youngster Tax e SS em Portugal e pede revisão ao Mohit Jain (designer).
  - 2025-08-12, Mohit Jain: aponta o Freshdesk 39417 ("PT social security gap").
  - 2025-10-17, Wallisson: atualiza o documento "com input do ICE" e anexa "PT - Retro Payroll Calculations 1.0".
- **Problema relatado:** lacuna de regulamentação: não havia regra documentada para IRS Jovem (isenção de 100% a 25% em cinco anos) nem para a redução de SS do empregador por primeiro emprego/desemprego de longa duração.
- **Erro identificado:** não consta erro de artefato; é lacuna de cobertura (research que não existia).
- **Causa raiz:** cobertura inicial do PT não incluiu regimes especiais (isenção/redução). [INCERTO]: o ticket não diz por que não estava no CCG.
- **Solução aplicada:** documento de research em Google Docs (conteúdo não consta no ticket); atualizado com ICE em 2025-10-17. Valores/percentuais: não constam no ticket.
- **O que não aconteceu / ficou aberto:** não consta se o CCG/WTC/DD foram atualizados; o ticket foi "resolvido" em 2025-08-08 (antes do input do ICE de outubro), ou seja, o documento foi revisado depois de fechar. Simulações pedidas não constam.
- **Tipo de erro:** T6, T11, T12 (sem fonte consolidada no ticket).
- **Lição para o pipeline:** F43 (populações especiais não cobertas) e F52 (resposta fica em documento solto, não no artefato). Check: regime de incentivo/isenção por população entra no CCG como módulo, com base legal.

## CT-3608 — NG: mudanças do ano fiscal 2026 (tabela de IR, fim do CRA, relief de aluguel)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** NG / "All Egypt Clients" (inconsistente: o país é NG) / Research task (Regulation Update) / Analysis Completed / 2025-07-02 / 2025-09-08
- **Linha do tempo:**
  - 2025-07-02, Vedant Pachisia: recebe do ICE três mudanças (tabela de IR, CRA abolido, sistema de rent relief) e anexa PDF "Nigeria New tax 2026".
  - 2025-07-02, Bazil Marema: cria planilha para rastrear mudanças com vigência futura.
  - 2025-09-08, Wallisson: entrega alerta "Nigeria - Finance Act 2025 Changes to Tax Rates - January 2026" (Google Doc).
- **Problema relatado:** mudança legal futura (a partir de janeiro de 2026) a ser comunicada em alerta.
- **Erro identificado:** nenhum erro de artefato; mudança legal a incorporar. Higiene do ticket: campo Cliente diz "All Egypt Clients" num ticket NG.
- **Causa raiz:** mudança de lei com vigência futura recebida via ICE; o rastreio dependia de planilha paralela. [INCERTO] sobre qualquer falha.
- **Solução aplicada:** alerta com a Finance Act 2025 (valores de faixas/alíquotas não constam no ticket; ficam no Google Doc e no PDF).
- **O que não aconteceu / ficou aberto:** não consta confirmação de que WTC/CCG/regulation foram alterados; critério de aceite só pedia o alerta, "após confirmação".
- **Tipo de erro:** T1 (mudança de valor com vigência futura), T11.
- **Lição para o pipeline:** F44 (varredura final de boletins) e NOVO: **calendário de vigências futuras com dono** (a planilha criada pelo Bazil é o embrião). Check: toda mudança com vigência futura tem linha com data de entrada em vigor, artefatos afetados e status de atualização.

## CT-3648 — MY: EPF obrigatório para empregados não malaios (a partir dos salários de outubro de 2025)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** MY / ISOS (levantado por) / Research task (Regulation Update) / Verified on Production / 2025-07-07 / 2025-10-13
- **Linha do tempo:**
  - 2025-07-07, Ruchi Gupta: KWSP anuncia EPF obrigatório para não cidadãos com employment pass válido, salários de outubro de 2025 (mês de contribuição novembro/2025), 2% empregado e 2% empregador (fontes: kwsp.gov.my, páginas "non-malaysian-citizen-employees" e news "epf-expands-mandatory-contribution-to-non-malaysians").
  - 2025-07-14, Bazil Marema: perguntas abertas: o que é "monthly wages", requisitos de relatório, cálculo para admissões/rescisões no meio do mês.
  - 2025-08-18, Ruchi pede prioridade. 2025-08-19, Wallisson entrega "Malaysia - Finance Act 2025 Changes to Statutory Contributions - October 2025".
  - 2025-09-04, Ruchi: estrangeiros que já optaram pela taxa malaia: calcular sobre base real ou base arredondada (tabela)? Exemplo 2.334 vs 2.340. Wallisson: 11% sobre o salário real (2.334 gera 256,74), sem usar base arredondada; a regra de 2% vale para quem não contribuía.
  - 2025-09-04/05: Ruchi pergunta se os 11% são todos "EPF obrigatório" (há dedução pré-imposto diferente para voluntário). Wallisson: os 11% inteiros são obrigatórios; mapear tudo ao código de dedução pré-imposto obrigatória.
- **Problema relatado:** configuração do novo regime de 2% e dúvida sobre estrangeiros já na taxa malaia (base e classificação obrigatório/voluntário).
- **Erro identificado:** não houve erro confirmado. Pontos frágeis na resposta: (a) a premissa de "base arredondada" da pergunta (2.340) indica que a configuração usava a tabela de faixas (Third Schedule), e a resposta "usar o salário real" contradiz isso sem citar o dispositivo; (b) "arredondado para o Ringgit mais próximo" não tem fonte no ticket [INCERTO: o EPF costuma arredondar para cima ao próximo Ringgit; verificar]; (c) a resposta cita "12-13% empregador" sem fonte.
- **Causa raiz:** regra nova sem definição de "monthly wages", proporcionalidade e transição; perguntas só foram respondidas depois de a configuração já estar feita (Ruchi: "We have done the changes").
- **Solução aplicada:** 2025-09-04/05: 2% novos contribuintes; quem já estava na taxa malaia mantém 11% sobre salário real, todo mapeado como EPF obrigatório. Base legal: só os dois links do KWSP e o dito "EPF confirmou" (sem número de circular). Documento de research em Google Doc.
- **O que não aconteceu / ficou aberto:** definição de "monthly wages", relatório (Form A/arquivo KWSP) e proporcionalidade de admissão/rescisão (perguntas do Bazil de 2025-07-14) não têm resposta no ticket.
- **Tipo de erro:** T1, T2, T7, T12.
- **Lição para o pipeline:** F51 (limite/base sem definição) e F50 (flag obrigatório/voluntário decidido sem base legal). Escapou porque a configuração foi feita antes de o research responder base e mid-month. Check: toda contribuição nova declara base (real × faixa), arredondamento (direção) e regra de proporcionalidade, com artigo/circular.

## CT-3661 — CZ: checklist de handover de regulamentação
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** CZ / sem cliente / Development task, Critical / Won't Do / 2025-07-09 / 2026-08-13
- **Linha do tempo:**
  - 2025-07-09, Mohit Jain: checklist (inputs do ICE, de Advisory, verificação com research próprio, verificação com software de terceiros).
  - 2025-08-25, Wallisson: ICE completo; verificação com research própria completa; simulações em software de terceiros em andamento (contatou o provedor externo de folha na Tchéquia por orientação do Marko). Publica link dos "Compliance Artifacts" (board no monday).
  - 2025-08-26, Devshree Vyas: Design de CZ não foi iniciado porque o research não está completo.
  - 2026-08-13: fechado como Won't Do (motivo não consta).
- **Problema relatado:** gate de handover research para design sem confirmação formal; design bloqueado.
- **Erro identificado:** nenhum erro de artefato; atraso de processo (ticket Critical aberto por mais de um ano).
- **Causa raiz:** dependência de simulações de terceiros que não chegaram [INCERTO]; ticket não registra desfecho.
- **Solução aplicada:** não resolvido no ticket (Won't Do); simulações de CZ aparecem como "resolvidas" em CT-3701 sem conteúdo.
- **O que não aconteceu / ficou aberto:** confirmação final do item 4 (software de terceiros); motivo do Won't Do.
- **Tipo de erro:** T6 (escopo/processo), T11.
- **Lição para o pipeline:** NOVO: gate de handover sem critério de saída verificável (o item "verificado com terceiros" não tem dono nem prazo). Check: handover aceito com evidência anexada por item; se bloqueado, registrar decisão explícita de seguir sem a verificação.

## CT-3792 — NL: desenvolvimento do 30% ruling
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** NL / sem cliente / Research task (Regulation Update) / Analysis Completed / 2025-08-05 / 2025-09-19
- **Linha do tempo:** 2025-08-11, Wallisson: um link de Google Doc (conteúdo não consta). Designer: Mohit Jain.
- **Problema relatado:** não consta além do título; desenvolvimento do 30% ruling.
- **Erro identificado:** não consta.
- **Causa raiz:** não consta.
- **Solução aplicada:** documento de especificação (link) e fechamento em 2025-09-19.
- **O que não aconteceu / ficou aberto:** a aplicabilidade das deduções pré-imposto ao 30% ruling continuou sem desenho (CT-4136, nov/2025, diz que "foi identificado nos tickets recentes que precisa ser desenvolvido"). Ver CT-3932 e CT-4136.
- **Tipo de erro:** T7 (lacuna de fórmula, [INCERTO] por inferência da sequência de tickets).
- **Lição para o pipeline:** F52 (resposta/doc fora do artefato) e F45. Check: o 30% ruling tem um único documento de regra (base, limiar proporcional, reconciliação mensal, pré-impostos) referenciado por todos os tickets.

## CT-3842 — PT: atualização da tabela de retenção, vigência 1 de agosto e 1 de outubro de 2025
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** PT / todos os clientes PT / Research task, Critical (Regulation Support) / Analysis Completed / 2025-08-18 / 2025-08-18
- **Linha do tempo:**
  - 2025-08-18, Vedant Pachisia: pede alerta da atualização das tabelas de retenção com vigência 1/ago e 1/out (fonte: Portal das Finanças, página das tabelas de retenção).
  - 2025-08-18, Wallisson (mesmo dia): entrega "Portugal_Finance Act 2025 Changes to Tax Rates_August 2025".
- **Problema relatado:** alerta de tabela de retenção. O pedido saiu depois da vigência de 1/ago, o que sugere atualização perdida (ver CT-3887).
- **Erro identificado:** tabela de retenção de PT com vigência 1/ago/2025 não estava atualizada [INCERTO: inferido de CT-3887, cujo conteúdo não consta].
- **Causa raiz:** monitoramento da fonte oficial sem alarme para publicações com vigência futura (ver CT-3887). [INCERTO]
- **Solução aplicada:** alerta/documento em 2025-08-18, valores não constam no ticket. Fonte: Portal das Finanças (link).
- **O que não aconteceu / ficou aberto:** a mudança de 1/out foi tratada como pedido repetido em CT-4039 (ver abaixo).
- **Tipo de erro:** T1.
- **Lição para o pipeline:** F44 + NOVO (calendário de vigências; ver CT-3608).

## CT-3887 — PT: RCA da atualização de tabela de retenção não feita
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** PT / todos os clientes PT / Research task (Regulation Support) / Analysis Completed / 2025-08-28 / 2025-08-28
- **Linha do tempo:** 2025-08-28, Vedant: o QCRM pediu RCA (Freshdesk 48868) sobre a atualização de tabela de PT perdida; pede que Wallisson complete os itens 8 a 10 do RCA (Google Doc). Wallisson (mesmo dia): itens 8-10 atualizados.
- **Problema relatado:** a tabela de retenção de PT não foi atualizada a tempo para os clientes.
- **Erro identificado:** atualização perdida de tabela de retenção (artefato e config do cliente); detalhes do RCA não constam (estão no Google Doc).
- **Causa raiz:** não consta (RCA fora do ticket).
- **Solução aplicada:** RCA entregue; correção da tabela vem em CT-3842.
- **O que não aconteceu / ficou aberto:** ações preventivas não constam.
- **Tipo de erro:** T1.
- **Lição para o pipeline:** F44. Check: varredura mensal das tabelas oficiais de retenção (PT publica atualizações em meses diferentes de janeiro) com registro de data da última verificação.

## CT-3892 — NL: checagem do mapeamento de WTs no XML (cliente Mammoet)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** NL / Mammoet / Reporting task / Verified on Production / 2025-09-02 / 2025-10-15
- **Linha do tempo:**
  - 2025-09-02, Vedant: Report Spec do XML do Loonaangifte inclui os campos PrlnAwfAnwHz (RANGE 64556, prêmio fundo de desemprego de alto risco) e PrLnUfo (RANGE 64557, prêmio de pessoal do setor público). Há pedido para remover esses WTs; pergunta quando são usados e o valor reportado. Freshdesk 48933.
  - 2025-09-08, Wallisson: 64556 aplica-se a contratos permanentes em setores de alta rotatividade; 64557 é exclusivo do setor público. Para Mammoet (empresa privada), 64557 é erro de configuração e 64556 provavelmente também. O valor reportado é o prêmio monetário calculado no período.
  - 2025-09-24, Brenet Õispuu (designer): WTs removidos conforme pedido.
- **Problema relatado:** WTs de prêmio presentes no cliente que não deveriam estar.
- **Erro identificado:** configuração do cliente/implementação (WTs setoriais atribuídos a empresa privada). Nosso artefato (spec) mantém os campos para quem for do setor aplicável [INCERTO].
- **Causa raiz:** WTs setoriais colocados na configuração padrão sem condição de elegibilidade; o cliente notou por pedido de remoção.
- **Solução aplicada:** WTs removidos da config pelo designer (2025-09-24). Base legal: sem fonte no ticket (a elegibilidade por setor vem do próprio texto da resposta; Belastingdienst/UWV não citados).
- **O que não aconteceu / ficou aberto:** não consta se os campos do XML ficam condicionais por setor na spec; não consta como a remoção afeta outros clientes de setor de risco.
- **Tipo de erro:** T3, T5, T10.
- **Lição para o pipeline:** F49 (código de WT retirado sem varredura nas specs) e F50. Check: WT setorial documenta a condição de elegibilidade e a spec lista o campo do XML como condicional.

## CT-3932 — NL: dúvidas do cliente sobre o 30% ruling (Omnicom)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** NL / Omnicom / Research task, Major (Regulation Support) / Analysis Completed / 2025-09-11 / 2025-09-11
- **Linha do tempo:**
  - 2025-09-11, Vedant: cliente revisou o documento de escopo do 30% ruling e levantou cinco dúvidas (anexo docx "NL 30 Percent Ruling SOW including client questions"; Freshdesk 49175).
  - 2025-09-11, Wallisson: respostas (resumo abaixo) + PDFs de exemplo de holerites.
- **Problema relatado:** (1) proporção do limiar: dividir pelos dias do ano ou do mês? (2) salário bruto deve descontar pensão/invalidez? (3) "White special base" no cenário vs "Green" no texto; (4) reconciliação mensal só vale para salário variável? (5) como evitar déficit acumulado de 15.000 euros em outubro?
- **Erro identificado:** inconsistência no nosso documento SOW: o cenário citava "Green" onde deveria ser "White special base" (Wallisson confirma que o 30% ruling não se aplica à base Green, só a White e White-Special). O resto são dúvidas de entendimento, sem erro de cálculo confirmado.
- **Causa raiz:** rótulo incorreto no documento (comunicação); lógica de proporção e do déficit descrita sem a regra de bloqueio/alerta.
- **Solução aplicada (2025-09-11):**
  - Limiar proporcional = limiar anual ÷ dias do ano (365/366) × dias trabalhados, para manter taxa diária constante (sem fonte legal no ticket).
  - "Gross salary" para elegibilidade/cálculo = componentes tributáveis (básico, férias/13º, bônus, comissão), antes de deduções de pensão e invalidez (sem fonte no ticket) [INCERTO]: CT-4136 (nov/2025) volta ao tema das deduções pré-imposto como lacuna.
  - Reconciliação mensal cumulativa é prática recomendada para todos, não só variáveis; o sistema deve checar o acumulado em cada rodada (não checar à mão).
- **O que não aconteceu / ficou aberto:** o que o sistema faz, de fato, quando há déficit (o cliente perguntou "como o sistema permite isso?") fica como "deve ser configurado"; não consta regra de bloqueio. Correção do documento (Green para White special) não consta como feita.
- **Tipo de erro:** T7, T10, T11, T12.
- **Lição para o pipeline:** F42 (exemplos digitados) e F51 (limite sem definição de período/acumulador). Ver também correcoes.md (30% ruling com lente de consultoria fiscal): resposta aqui adota lente de sistema. Check: documento de regra com exemplo calculado, glossário (White/Green/White-special) e regra de déficit.

## CT-3943 — NL: taxas Green e White para o ano fiscal de 2025
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** NL / sem cliente / Research task (Regulation Build) / Analysis Completed / 2025-09-12 / 2025-09-15
- **Linha do tempo:** 2025-09-12, Mohit Jain: pede as taxas Green e White de 2025, anexa planilha própria (para conferência, "não alterar sem falar comigo"). 2025-09-15, Wallisson: link de Google Doc.
- **Problema relatado:** faltavam as tabelas de retenção Green e White de NL 2025 para o design.
- **Erro identificado:** lacuna de research (tabelas não estavam no pacote). Valores não constam no ticket.
- **Causa raiz:** [INCERTO] ficaram fora do CCG original.
- **Solução aplicada:** documento com as tabelas (conteúdo não consta). Fonte: sem fonte no ticket.
- **O que não aconteceu / ficou aberto:** conferência cruzada com a planilha do Mohit não consta.
- **Tipo de erro:** T1, T6.
- **Lição para o pipeline:** F44 e F41 (oráculo independente). A planilha do Mohit é um oráculo; check: tabelas oficiais (Belastingdienst) comparadas linha a linha com a versão do design.

## CT-3945 — TR: confirmação do cálculo de seguro privado (vida)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** TR / todos os clientes TR / Research task, Major (Regulation Gap) / Analysis Completed / 2025-09-15 / 2025-09-19
- **Linha do tempo:**
  - 2025-09-15, Vedant: BAU enviou uma lógica para o prêmio de seguro privado; pede confirmação do research antes de aplicar (Freshdesk 41297; Excel "Life Insurance_2025").
  - 2025-09-15, Mohit: lógica do BAU = mínimo de (15% do bruto, salário mínimo mensal acumulado até o anual, prêmio real); a equipe acha que os três limites devem ser cumulativos, o BAU diz que só o limite do salário mínimo é cumulativo.
  - 2025-09-15, Wallisson: mínimo de três valores (prêmio real do mês, 15% do bruto do mês, teto anual = salário mínimo bruto anual de 2025, 312.066 TRY = 12 x 26.005,50); "os três limites devem ser aplicados cumulativamente"; prêmio pago pelo empregador é benefício tributável sujeito a SSI e a parcela dentro dos limites pode ser deduzida da base de IR.
  - 2025-09-17, Vedant: aponta contradição (cumulativo só no teto ou nos três?). 2025-09-18, Wallisson: mínimo de (prêmio, 15% do bruto mensal, saldo ainda não deduzido do mínimo anual).
  - 2025-09-19, Mohit: o cálculo de IR turco é totalmente cumulativo; os dois primeiros limites devem ser cumulativos ou mensais? 2025-09-19, Wallisson: resposta final com fontes: apenas o teto anual é cumulativo; 15% é teste mensal "no mês do pagamento"; elegível 50% para vida com poupança e 100% para risco; fontes GİB (folheto 2025 "Hayat ve Şahıs Sigortası Primleri"), EY Turkey Tax Guide 2025, PwC Worldwide Tax Summaries (Turkey).
- **Problema relatado:** como aplicar os limites de dedução de prêmio de seguro de vida privado e se vale o mesmo quando o empregador paga.
- **Erro identificado:** resposta anterior nossa (2025-09-15) contradizia a lei: afirmou que os três limites são cumulativos. Corrigida duas vezes (09-18 e 09-19) até o enunciado final.
- **Causa raiz:** resposta inicial dada antes de ler a fonte oficial; misturou "IR cumulativo" (tabela progressiva) com os limites da dedução. Resposta de pesquisa, sem checagem contra o oráculo (folheto GİB).
- **Solução aplicada:** regra final em 2025-09-19 (Wallisson) com fontes oficiais/Big-4:
  - dedução mensal = mínimo(prêmio elegível do mês [50% poupança, 100% risco], 15% do bruto do mês, saldo restante do teto anual);
  - teto anual 2025 = 312.066 TRY (12 x 26.005,50), cumulativo YTD; 15% não é cumulativo.
  - Empregador paga: tratamento declarado como "benefício tributável e sujeito a SSI, com dedução do IR na mesma regra" — sem fonte específica no ticket [INCERTO].
- **O que não aconteceu / ficou aberto:** não consta confirmação formal do BAU/Mohit sobre a resposta final; a parte "empregador paga" não teve fonte. Pagamento antecipado de apólice multi-mês deve ser rateado (nota do GİB) — não consta se virou regra.
- **Tipo de erro:** T2, T7, T12.
- **Lição para o pipeline:** F51 (limite/acumulador sem definição do período) e F41. Check: todo limite descreve "período do teste" (mensal × YTD) e vem com linha da fonte oficial; resposta de ticket só sai depois do cotejo com a fonte primária.

## CT-3957 — NL: relatório "Wage Tax Company Overview" com total geral duplicando retro
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** NL / todos os clientes NL / Reporting task (Statutory Reports) / Analysis Completed / 2025-09-17 / 2025-09-25
- **Linha do tempo:**
  - 2025-09-17, Vedant (Freshdesk 48436): em "Wage Tax Company Overview" (código wage-tax-overview), o "Totaal Generaal" soma de novo o retro, que já aparece separado em "Correctie over vorige tijdvak(ken)".
  - 2025-09-22, Vedant: segundo Brenet, o relatório não é de compliance e não pode ser confirmado por compliance; fecha.
  - 2025-09-25, Vedant: ticket voltou, haverá call; pergunta se é relatório estatutário. Wallisson: o problema são dois relatórios custom que não batem com o estatutário (XML de imposto), principalmente com retro; o cliente os usa para validar.
- **Problema relatado:** totais divergentes entre relatórios custom e o XML estatutário quando há retro.
- **Erro identificado:** relatório custom (não nosso) soma o retro duas vezes; nosso artefato (XML estatutário) não é apontado como errado.
- **Causa raiz:** fronteira de responsabilidade não esclarecida (estatutário × custom); lógica de retro nos custom.
- **Solução aplicada:** esclarecimento de escopo em 2025-09-25; correção do relatório custom não consta (fora do nosso escopo).
- **O que não aconteceu / ficou aberto:** quem corrige os custom; resultado da call.
- **Tipo de erro:** T5, T10.
- **Lição para o pipeline:** F54 (lista de relatórios cobertos/não cobertos não publicada). Check: matriz de cobertura distingue relatório estatutário (nosso) de custom, e custom que valida contra o estatutário tem teste de reconciliação com retro.

## CT-4005 — AU: SAFF (SuperStream Alternative File Format) é padrão ou custom?
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** AU / todos os clientes AU / Research task (Regulation Support) / Analysis Completed / 2025-09-26 / 2025-10-13
- **Linha do tempo:**
  - 2025-09-26, Vedant (Freshdesk 49968): com o Payday Super (1/7/2026) a super deve ser paga no mesmo dia do pagamento; o cliente quer o SAFF no mesmo dia do arquivo de banco; padrão ou custom?
  - 2025-10-06, Wallisson: SuperStream define o padrão de dados/pagamento; SAFF é uma alternativa CSV da ATO, não obrigatória; Payday Super muda o prazo, não o formato; a maioria usa clearing houses (SuperChoice, Beam). Decisão: SAFF não vai como relatório padrão; exportação sob demanda para quem sobe a um clearing house; priorizar integrações embutidas; onde habilitado, gerado na finalização do pagamento junto do arquivo de banco.
- **Problema relatado:** expectativa do cliente de receber SAFF no pagamento.
- **Erro identificado:** nenhum erro; decisão de escopo (nenhum artefato errado).
- **Causa raiz:** [INCERTO] lacuna na lista de relatórios de AU quanto ao formato de super.
- **Solução aplicada:** decisão de escopo: SAFF fora do padrão, sob demanda. Base legal: sem fonte no ticket além do documento de research (link). Payday Super 1/7/2026 é a data informada pelo ticket.
- **O que não aconteceu / ficou aberto:** quem desenvolve o SAFF sob demanda; integração com clearing house; data.
- **Tipo de erro:** T6, T11, T12.
- **Lição para o pipeline:** F54. Decisão de escopo ("SAFF sob demanda") deve entrar na matriz de cobertura de AU e no registro de decisões.

## CT-4008 — AU: payslip em formato Mercans (GSK)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** AU / GSK / Research task (Regulation Support) / Analysis Completed / 2025-09-26 / 2025-10-13
- **Linha do tempo:**
  - 2025-09-26, Vedant (Freshdesk 49967): pede ETA do payslip AU em formato Mercans (link do generator).
  - 2025-10-02, Wallisson: entrega o "AU Compliance_Payslip_Generator".
  - 2025-10-06, Vedant: pede para não fechar; o payslip está em USD e a Austrália usa AUD; quer o correto e em PDF.
  - 2025-10-06, Wallisson: link do "AU - Payslip" (PDF).
- **Problema relatado:** payslip entregue com moeda errada (USD).
- **Erro identificado:** nosso artefato (Payslip Generator AU) com moeda USD em vez de AUD.
- **Causa raiz:** template copiado de outro país sem trocar moeda e formatos [INCERTO]; construção do artefato.
- **Solução aplicada:** novo PDF em 2025-10-06 (versão e conferência da moeda no generator não constam).
- **O que não aconteceu / ficou aberto:** não consta se o próprio generator foi corrigido, nem versão nova.
- **Tipo de erro:** T9.
- **Lição para o pipeline:** F57 (payslip divergente da Payslip Spec). Check: moeda, locale e formato numérico do payslip batem com a moeda do país no manifest (AUD) antes de entregar.

## CT-4039 — PT: tabela de retenção, vigência 1 de agosto e 1 de outubro de 2025
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** PT / todos os clientes PT / Research task, Critical / Analysis Completed / 2025-10-06 / 2025-10-06
- **Linha do tempo:** 2025-10-06, Mohit Jain: abre pedido de alerta com o mesmo texto de CT-3842, e o ticket é resolvido no mesmo minuto, sem comentário.
- **Problema relatado:** alerta das tabelas de retenção de PT (agosto e outubro).
- **Erro identificado:** não consta; parece duplicata de CT-3842 [INCERTO].
- **Causa raiz:** [INCERTO] reabertura para Design (Mohit é designer) sem referência ao alerta anterior; o ticket anterior ficou fechado em agosto.
- **Solução aplicada:** não consta; presumivelmente reutilizou o alerta de CT-3842.
- **O que não aconteceu / ficou aberto:** não consta confirmação de que a mudança de 1/out foi incluída no alerta de agosto.
- **Tipo de erro:** T1, T8.
- **Lição para o pipeline:** F52. Check: ticket duplicado aponta o artefato/versão vigente; alerta de vigência futura é reaberto quando chega a data.

## CT-4076 — AU: Workers' Compensation Expense no WTC (GSK)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** AU / GSK / Research task (Regulation Support) / Analysis Completed / 2025-10-13 / 2025-10-23
- **Linha do tempo:** 2025-10-13, Vedant (Freshdesk 50483): o "Workers Compensation Expense" existe no sistema/WTC regulatório? É calculado automaticamente por estado? 2025-10-23, Wallisson: não existe, é prêmio de seguro do empregador (despesa), não WT do WTC; não é calculado pela folha. A folha só reporta o total de salários; finanças calcula pelo percentual da seguradora estadual.
- **Problema relatado:** expectativa de GSK de que a folha calcule o custo de seguro por estado.
- **Erro identificado:** nenhum; divergência de expectativa (cliente × escopo).
- **Causa raiz:** escopo do WTC (WT do empregado) × despesa do empregador.
- **Solução aplicada:** esclarecimento de escopo. Sem fonte no ticket (alíquotas por estado não são citadas).
- **O que não aconteceu / ficou aberto:** se o relatório de base salarial para o cálculo do seguro (G2N com on-costs) existe: perguntado em HRBS-117; não consta decisão.
- **Tipo de erro:** T6, T10.
- **Lição para o pipeline:** NOVO: **fronteira "custo do empregador/seguro não faz parte do WTC"**. Check: lista de encargos do empregador fora do motor de folha, publicada com o hub do país (AU: workers' comp, payroll tax).

## CT-4078 — IE: mudança de razão social do cliente e impacto em relatórios inbound/outbound (Omnicom)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** IE / Omnicom / Research task, Major (Statutory Reports) / Analysis Completed / 2025-10-13 / 2025-10-23
- **Linha do tempo:** 2025-10-13, Vedant (Freshdesk 50419): uma entidade legal muda o nome para "Omnicom Advertising Group Ireland Limited" no ROS e no Companies Registration Office; o que muda em RPN (tax cards) e PSR (submissões)? 2025-10-23, Wallisson: ambos são impactados: (1) RPN: o ROS Digital Certificate é identidade digital ligada ao nome legal; o certificado antigo deixa de valer; (2) PSR: autenticação falha e o nome legal é campo obrigatório no arquivo, e será rejeitado se enviado antes de o Revenue atualizar (ou depois, se não atualizarmos). Análise completa em Google Doc.
- **Problema relatado:** impacto da mudança de razão social nas integrações com o ROS.
- **Erro identificado:** nenhum erro de artefato; risco operacional de timing.
- **Causa raiz:** n/a.
- **Solução aplicada:** análise. Base legal/oficial: sem fonte no ticket (só o documento). [INCERTO]: afirmação de que o certificado ROS "fica inválido" ao mudar o nome é forte e sem citação de Revenue; verificar se o certificado é emitido para o PAYE registration e não para o nome.
- **O que não aconteceu / ficou aberto:** sequência recomendada (quando trocar o nome, novo certificado, janela entre mudança no CRO e ROS) não consta; teste em ambiente não consta.
- **Tipo de erro:** T11, T12.
- **Lição para o pipeline:** NOVO: **mudança de identidade do empregador (nome, CNPJ/PAYE, certificado)** como evento do ciclo de vida do cliente. Check: runbook com sequência, dono e janela, validado com o regulador antes de responder ao cliente.

## CT-4136 — NL: desenvolver aplicabilidade de deduções pré-imposto ao 30% ruling
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** NL / sem cliente / Development task, Major (Regulation Gap) / Analysis Completed / 2025-11-11 / 2025-12-17
- **Linha do tempo:** 2025-11-11, Wallisson: "como identificado nos tickets recentes, as deduções pré-imposto do 30% ruling precisam ser desenvolvidas"; link para análise ("Netherlands 30% Ruling: A Definitive Analysis of Pre-Tax Deduction Applicability and Calculation Base"). 2025-11-12, Mohit Jain: requisitos pouco claros; pede sessão de KT conforme RACI.
- **Problema relatado:** o 30% ruling não tratava as deduções pré-imposto (pensão etc.) como parte da base.
- **Erro identificado:** lacuna de design do 30% ruling (nosso artefato/desenho); em conflito com a resposta ao cliente em CT-3932 (setembro), que dizia que o ruling é aplicado antes das deduções [INCERTO: conflito inferido, o conteúdo da análise não consta].
- **Causa raiz:** regra de base de cálculo não definida na primeira versão (CT-3792).
- **Solução aplicada:** análise entregue; resolvido em 2025-12-17, mas o desenvolvimento e o KT não constam.
- **O que não aconteceu / ficou aberto:** KT solicitado; implementação não consta.
- **Tipo de erro:** T7, T2.
- **Lição para o pipeline:** F46 (design não derivado da research) e F51. Check: spec de design traz tabela "base de cálculo × componente" e exemplos calculados.

## CT-4169 — AU: parâmetros do Medicare levy (Schedules 1 e 9) com taxas antigas no Guide
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** AU / sem cliente / Development task (Regulation Build) / Analysis Completed / 2025-11-19 / 2025-11-19
- **Linha do tempo:** 2025-11-19, Devshree Vyas: o Final Regulation Guide ainda tinha a tabela antiga de parâmetros do medical levy nos Schedules 1 e 9; pede atualizar lógica e exemplos. Mesmo dia, Wallisson: nova versão "Australia Country Regulations Guide - 2025_2026 FINAL (ML Parameters Update)".
- **Problema relatado:** CCG/Guide com parâmetros desatualizados.
- **Erro identificado:** valor estatutário desatualizado no Regulation Guide (nosso artefato). Valores novos e antigos não constam.
- **Causa raiz:** research não incorporou a atualização dos parâmetros publicada no ano; Guide marcado FINAL já saiu sem a varredura de boletins. [INCERTO]
- **Solução aplicada:** nova versão do Guide em 2025-11-19, no mesmo dia. Fonte (ATO) não consta no ticket.
- **O que não aconteceu / ficou aberto:** confirmação de que WTC/DD e simulações usam os novos parâmetros (propagação).
- **Tipo de erro:** T1, T8.
- **Lição para o pipeline:** F18 (referência legal desatualizada), F44 e F27 (artefato posterior não re-sincronizado). A versão "FINAL (ML Parameters Update)" também alerta para F59 (rótulo de versão).

## CT-4322 — AU: WTC 3.1, novos wage codes para GSK (revisão em WTC 3.2)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** AU / GSK (via HRBS-3316, fora deste lote) / Development task, Major (Regulation Build) / Analysis Completed / 2026-01-13 / 2026-01-23
- **Linha do tempo:**
  - 2026-01-13, Devshree Vyas: a equipe de configuração pediu novos wage codes para GSK AU; pede aprovação do RA sobre a natureza dos códigos e a precisão (linha nova em verde, campo alterado em vermelho quando o mapeamento de tributação muda).
  - 2026-01-22, Wallisson: lista de mudanças no WTC 3.2 (ver abaixo). "Os WTs foram revisados."
- **Problema relatado:** códigos novos do WTC 3.1 com flags de tributação/super/STP incorretos.
- **Erro identificado:** nosso artefato (WTC 3.1): vários flags errados. Corrigidos no 3.2:
  - 62200 (RX Strive Bonus): STP de "Excluded" para "BC Bonus and commissions"; Include in STP Gross de N para Y.
  - 62530-62532 (Company Car Payment): Subject to Super de No para Yes (OTE, SGR 2009/2).
  - 65580-65660 (Car Allow Taxed No Super): Super de No para Yes.
  - 65661: Super de No para Yes.
  - 79410 (Income Protection Payment): Super de No para Yes e STP Gross de N para Y.
  - 79411-79418 (PPL pago): STP Gross de N para Y.
  - 79419, 79422, 79448 (licenças sem remuneração): Taxable de Yes para No; Table Tax de Yes para NA.
  - 79421 (Worker Cover Leave pago): Super de Yes para No (SGR 2009/2).
- **Causa raiz:** flags de WT atribuídos por analogia na criação do 3.1 (sem base legal por flag); revisão posterior contra regras ATO STP/SGR 2009/2. [INCERTO] sobre quais alterações do 3.2 também são discutíveis: a mudança de 79410 para "Super Yes" (income protection) e a de 79421 para "No" não citam ruling específico além do SGR 2009/2 geral.
- **Solução aplicada:** WTC 3.2 em 2026-01-22. Base legal: ATO STP guidance, SGR 2009/2 (OTE) — como citado; sem artigo.
- **O que não aconteceu / ficou aberto:** aprovação do RA e impacto nos Regulations para GSK (a nota diz que haverá impacto, e o ticket não registra a conferência); versão do WTC na pasta final.
- **Tipo de erro:** T2, T3.
- **Lição para o pipeline:** F50 (flag sem base legal). Check: coluna "base legal" por flag no WTC; combinações (OTE, STP, table tax) com exemplo.

## CT-4391 — BG: esclarecimentos sobre o CCG
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** BG / sem cliente / Research task (Regulation Build) / Analysis Completed / 2026-04-15 / 2026-04-28
- **Linha do tempo:** 2026-04-15, Ruchi Gupta: links para CCG e para documento de queries do design. Mesmo dia, Wallisson: "queries reverted"; pede que as próximas dúvidas sejam levantadas dentro do CCG conforme a metodologia Research x Development.
- **Problema relatado:** design precisava de respostas para prosseguir.
- **Erro identificado:** nenhum erro de artefato; desvio de processo (queries em documento separado).
- **Causa raiz:** canal de dúvidas fora do CCG.
- **Solução aplicada:** respostas dadas no documento de queries; regra de processo reafirmada. Conteúdo não consta.
- **O que não aconteceu / ficou aberto:** ver respostas (fora do ticket).
- **Tipo de erro:** T11.
- **Lição para o pipeline:** F6 (queries abertas sem resposta). Decisão de processo reutilizável: queries do design ficam no CCG.

## CT-617 — CO: arredondamento da base de seguridade social (PILA)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** CO / todos os clientes CO / Research task (Regulation Gap) / Analysis Completed / 2024-10-11 / 2025-10-27
- **Linha do tempo:**
  - 2024-10-11, Vedant (Freshdesk 37043): cita o Decreto 1990 de 2016 (Min. Salud), que modifica o artigo 3.2.1.5 do Decreto 780/2016: no formulário PILA, (1) o IBC de cada cotizante é aproximado ao peso superior mais próximo; (2) o valor das contribuições pagas e dos juros é aproximado ao múltiplo de 100 mais próximo. Exemplo do ticket: base 2.145.078 vira 2.145.100. Critério de aceite: base "aproximada ao peso superior de 100".
  - 2025-01-22, Srikanth Subramanian: sprint removido, ticket em espera.
  - 2025-10-27, Vedant: remete a HRBS-182 (FD#37043, ajuste de aproximações da seguridade social).
- **Problema relatado:** o sistema não arredonda como o PILA exige.
- **Erro identificado:** o próprio ticket é inconsistente: o texto legal diz IBC ao peso superior (inteiro) e as contribuições a múltiplo de 100; o título e o exemplo arredondam a base para 100 (2.145.078 → 2.145.100). O arredondamento a 100 vale para o valor da contribuição, não para a base, segundo o texto do decreto citado.
- **Causa raiz:** descrição do requisito mal resumida (título "base arredondada para 100") em contradição com a norma citada; ticket ficou parado um ano em espera.
- **Solução aplicada:** não resolvido neste ticket; remetido a HRBS-182 (conteúdo não consta). Fonte: Decreto 1990/2016, art. 3.2.1.5 do Decreto 780/2016 (como citado no ticket).
- **O que não aconteceu / ficou aberto:** qual regra foi implementada em HRBS-182 não consta; o exemplo do ticket ficou sem correção.
- **Tipo de erro:** T7, T12.
- **Lição para o pipeline:** F37 (taxa/regra em prosa contradizendo o próprio cálculo) e F42 (exemplo digitado). Check: regra de arredondamento declara objeto (base × contribuição), direção (cima/mais próximo) e unidade (peso/100), com exemplo calculado.

## CT-70 — PT: configuração de imposto e SSC negativos
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** PT / sem cliente / Research task (Regulation Gap) / Analysis Completed / 2024-05-27 / 2025-11-02
- **Linha do tempo:** 2024-05-27, Mpho Mokhoro (Freshdesk 31433): confirmação do tratamento de imposto e contribuições sociais negativos. 2025-11-02, Wallisson: link "Portugal: Payroll Software Configuration for Negative Tax and SSC Adjustments (2025) - ICE Reviewed".
- **Problema relatado:** lacuna de regra para valores negativos de retenção e SSC (ex.: retro, correções).
- **Erro identificado:** lacuna de research; resposta só 17 meses depois. Conteúdo não consta.
- **Causa raiz:** não consta.
- **Solução aplicada:** documento revisado pelo ICE; regra não consta no ticket.
- **O que não aconteceu / ficou aberto:** a regra propriamente dita não consta; confirmação de adoção na configuração não consta.
- **Tipo de erro:** T7, T12.
- **Lição para o pipeline:** F58 (ciclos especiais, retro) e F52. Check: CCG tem módulo de ajustes/retro com tratamento de negativos.

## HRBS-10915 — ES: amostras dos relatórios estatutários
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** ES / todos (Report Matrix) / Service Request / resolvido (SLA Met) / 2026-06-18 / 2026-06-24
- **Linha do tempo:** 2026-06-18, Gulnaaz Parveen: pede amostras de todos os relatórios estatutários da Espanha, sem dados de empregados, para a Report Matrix dos clientes em implementação. 2026-06-22, Wallisson: juntando os arquivos do ICE. 2026-06-24: compartilhado por e-mail.
- **Problema relatado:** falta de amostras sanitizadas dos relatórios estatutários.
- **Erro identificado:** nenhum erro; mas o conjunto entregue não era completo (ver HRBS-11736).
- **Causa raiz:** amostras não existiam num pacote organizado; dependiam do ICE.
- **Solução aplicada:** envio por e-mail (lista de arquivos não consta).
- **O que não aconteceu / ficou aberto:** lista dos relatórios entregues não consta; o Certificado de Retenciones anual ficou fora (HRBS-11736).
- **Tipo de erro:** T11, T5.
- **Lição para o pipeline:** F54 e F55. Check: matriz de cobertura por país com amostra sanitizada para cada relatório.

## HRBS-11736 — ES: Certificado de Retenciones anual faltando na lista
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** ES / todos Espanha / Service Request (SLA Breached) / resolvido (no YouTrack) / 2026-07-13 / 2026-08-04
- **Linha do tempo:**
  - 2026-07-13, Gulnaaz Parveen: com base em HRBS-10915, faltam o Certificado de Retenciones anual para residentes e não residentes; envia exemplo.
  - 2026-07-14, Wallisson: abre SR-342 "ES: Employee Tax Certificate - SPEC" para Lily Li.
  - 2026-07-21 a 08-03: Gulnaaz pede manter aberto e ETA; Wallisson pede para fechar; Gulnaaz pergunta se foi desenvolvido.
  - 2026-08-18, Lily Li: em desenvolvimento por Brenet.
- **Problema relatado:** relatório estatutário anual ausente da lista entregue.
- **Erro identificado:** lacuna de escopo no nosso conjunto de relatórios ES (Certificado de Retenciones não estava no catálogo).
- **Causa raiz:** o relatório não constava da lista de relatórios cobertos (nem dos arquivos do ICE) [INCERTO].
- **Solução aplicada:** SR-342 aberto para spec; desenvolvimento em curso em 2026-08-18. Base legal: não consta no ticket (certificado de retenciones: ver spec).
- **O que não aconteceu / ficou aberto:** entrega do relatório; ETA nunca informado; fechamento do ticket de solicitação antes de a entrega acontecer causou perda de rastreio.
- **Tipo de erro:** T5, T6.
- **Lição para o pipeline:** F54. Solução reutilizável: ticket do pedido fica aberto até a entrega do SR, referenciado pelo SR.

## HRBS-11790 — ES: dependant relief (descendente ≤ 3 anos) e campo "Descendants Year of Birth"
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** ES / sem cliente / Incident / resolvido (SLA Met) / 2026-07-14 / 2026-07-14
- **Linha do tempo:** 2026-07-14, Gulnaaz Parveen: no DD v1.0 havia o campo "Descendants Year of Birth", usado para o alívio de descendente ≤ 3 anos; agora não existe; pergunta por que foi removido. Mesmo dia, Wallisson: campo substituído por `$hr.child_count_under_3`; segue a lógica do Modelo 145 (autodeclaração); art. 58.2 LIRPF: +2.800 euros/ano por descendente < 3 anos (1.400/1.400 se casal); regras de exceção: descendente que falece no ano ainda conta; adotado/acogido conta por 3 anos fiscais desde a inscrição no Registro Civil, independentemente da idade; ano de nascimento sozinho não resolveria; não é preciso reinserir.
- **Problema relatado:** suspeita de campo do DD removido sem explicação.
- **Erro identificado:** nenhum erro de cálculo; falha de comunicação: a mudança do DD não estava explicada onde o suporte olha (changelog/ficha).
- **Causa raiz:** decisão de design (campo derivado → contagem declarada) não registrada em local visível ao suporte.
- **Solução aplicada:** explicação por escrito; sem mudança. Fonte: art. 58.2 LIRPF e Modelo 145 (como citados no ticket).
- **O que não aconteceu / ficou aberto:** não consta como o contador `child_count_under_3` é atualizado quando o filho completa 3 anos (virada de ano) [INCERTO]; não consta fonte do valor 2.800 além do artigo.
- **Tipo de erro:** T4, T11.
- **Lição para o pipeline:** F59 (changelog não explica a mudança) e F52. Check: remoção/troca de campo do DD tem linha de justificativa e base legal no Version Control.

## HRBS-117 — AU: estrutura do G2N (Gross-to-Net) para GSK
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** AU / GSK / Question / Inquiry, High / resolvido / 2025-10-13 / 2025-12-29
- **Linha do tempo:** 2025-10-13, Saravanan Ekambaram: como o G2N mostra Gross Taxable Wage e pré-tax deductions (cabeçalho separado?) e se inclui custos do empregador (payroll tax, workers' comp). 2025-10-21, Wallisson: link do documento "Gross-to-Net (G2N) Report Structure for Australian Payroll" (conteúdo não consta). Resolvido em 2025-12-29 (provavelmente fechamento pelo cliente, [INCERTO]).
- **Problema relatado:** dúvida de conteúdo do relatório G2N.
- **Erro identificado:** nenhum.
- **Causa raiz:** n/a.
- **Solução aplicada:** documento de estrutura. Se o G2N inclui on-costs: não consta (veja CT-4076: custo do empregador não é calculado).
- **O que não aconteceu / ficou aberto:** resposta direta sobre on-costs não consta.
- **Tipo de erro:** T11, T5.
- **Lição para o pipeline:** F54. Ver CT-4076 (on-costs fora do motor).

## HRBS-118 — AU: indenização por acidente de trabalho paga após o desligamento (GSK)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** AU / GSK / Question / Inquiry, High / resolvido / 2025-10-13 / 2025-12-29
- **Linha do tempo:** 2025-10-13, Saravanan Ekambaram: pagamentos de workers' compensation continuam por anos após o desligamento; será suportado? 2025-10-21, Wallisson: link "Processing Workers' Compensation Payments for Terminated Employees in Australia" (conteúdo não consta).
- **Problema relatado:** processar pagamentos a ex-empregados.
- **Erro identificado:** nenhum erro; possível lacuna de cobertura (população de ex-empregados com pagamento contínuo).
- **Causa raiz:** n/a.
- **Solução aplicada:** documento de processamento (conteúdo e decisão não constam).
- **O que não aconteceu / ficou aberto:** se o produto suporta (resposta sim/não) não consta.
- **Tipo de erro:** T6, T11.
- **Lição para o pipeline:** F43 (populações especiais: ex-empregados com pagamento contínuo). Relaciona-se com WTs 79421/79422 do CT-4322.

## HRBS-11806 — Congo (República do Congo): "SS Company Part 2" e "Part 3" no WTC (Baker Hughes)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Congo (Brazzaville; o campo País do ticket diz "Democratic Republic of the Congo", inconsistente com título, CNSS e XAF) / Baker Hughes / Service Request / resolvido (SLA Met) / 2026-07-14 / 2026-07-16
- **Linha do tempo:**
  - 2026-07-14, Daniel Kelvin Balogun: revisão interna pede validar nomes, fórmulas (alíquota, base com/sem teto, base igual entre partes, teto mensal), taxa setorial (petróleo e gás) e código GL das partes 2 e 3.
  - 2026-07-14, Mohit Jain: desenvolvimento foi "exatamente como no CCG".
  - 2026-07-16, Wallisson: lacuna no WTC, corrigida no arquivo; CCG está correto. O WTC tinha 3 linhas "SS Company Part 1/2/3" duplicadas com a mesma fórmula combinada.
- **Problema relatado:** nomes/fórmulas das partes de SS patronal inconsistentes com o CNSS.
- **Erro identificado:** nosso artefato (WTC): três linhas com a mesma fórmula combinada em vez de um ramo CNSS cada. CCG correto.
- **Causa raiz:** construção do WTC (linhas duplicadas; fórmula combinada copiada) [INCERTO sobre o mecanismo], escapou da checagem WTC × CCG.
- **Solução aplicada (2026-07-16, WTC v1.1, com histórico de versão):**
  - Part 1 = PVID empregador 8%, teto 1.200.000 XAF;
  - Part 2 = Prestações familiares (PF) empregador 10,03%, teto 600.000 XAF;
  - Part 3 = Acidente de trabalho (AT-MP) empregador 2,25%, teto 600.000 XAF.
  - Taxa AT-MP: confirmada diretamente com a CNSS Congo como fixa de 2,25% para todos os setores, sem diferenciação para óleo e gás.
  - GL: os 3 ramos são pagos juntos num único borderô CNSS, então um GL único não é problema de compliance; separar é decisão de produto/finanças.
  - Fonte: confirmação verbal/escrita da CNSS (sem documento no ticket); o CCG é a fonte formal.
- **O que não aconteceu / ficou aberto:** não consta se a configuração do HRBlizz foi alterada no cliente; desfecho da separação de GL.
- **Tipo de erro:** T3, T7.
- **Lição para o pipeline:** NOVO: linhas de WT distintas com a mesma fórmula/base devem ser justificadas (check de unicidade de fórmula no WTC). Também F45 (WTC × CCG não reconciliados) e F20.

## HRBS-11814 — Gabon e Congo: número de seguridade social no payslip (Baker Hughes)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Gabon (e Congo) / Baker Hughes / Service Request (SLA Breached) / resolvido / 2026-07-14 / 2026-07-20
- **Linha do tempo:** 2026-07-14, Daniel Kelvin Balogun: o nº de registro de SS aparece no payslip e é obrigatório? 2026-07-15, Manju Shetija: payslip de Gabon cobre número CNSS de empregador e de empregado; pede confirmação para Congo ao Wallisson. 2026-07-20, Wallisson: Congo também mostra os dois ("Matricule Employeur CNSS" e "Numéro d'Assuré CNSS du Salarié"), mesmo padrão do Gabon; ambos os cadastros são obrigatórios por lei (empregador antes de contratar, empregado antes de começar), e são referenciados nos borderôs mensais.
- **Problema relatado:** dúvida se o número de SS deve ou não constar no payslip.
- **Erro identificado:** nenhum. Mas a pergunta "é obrigatório no payslip?" ficou sem resposta jurídica direta: a resposta fala da obrigatoriedade do cadastro e da prática.
- **Causa raiz:** n/a.
- **Solução aplicada:** confirmação de que o payslip já tem os dois campos para Gabon e Congo. Base legal: sem artigo no ticket; exemplos de formato (CNSS-EMP-..., CNSS-INS-...) são ilustrativos.
- **O que não aconteceu / ficou aberto:** se a lei exige a menção no payslip não consta.
- **Tipo de erro:** T9, T11, T12.
- **Lição para o pipeline:** F57 (checklist de campos legais do payslip). Check: cada campo do payslip tem coluna "obrigatório por lei? base" separando "cadastro obrigatório" de "menção no payslip obrigatória".

## HRBS-11864 — IE: opt-out do auto-enrolment (NAERSA/MyFutureFund) e reembolso na folha
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** IE / agências OMG Ireland (Live/BAU) / Question / Inquiry (SLA Met) / resolvido / 2026-07-15 / 2026-07-17
- **Linha do tempo:**
  - 2026-07-15, cliente: confirmar se o HR Blizz está configurado para reembolsar, no salário do mês, quem optou por sair do auto-enrolment.
  - 2026-07-17, Mohit Jain: o reembolso das contribuições do empregado é feito pela NAERSA, não pelo empregador. Yojana Bonagir: as especificações técnicas da NAERSA não preveem reembolso pela folha; compliance escreveu à NAERSA e aguarda resposta. O cliente pede confirmação no mesmo dia (folha do mês).
  - 2026-07-17, Wallisson: confirma. Fonte: FAQ do empregador da NAERSA (myfuturefund.ie/employer-faq): NAERSA reembolsa o empregado direto na conta; contribuições do empregador e do Estado ficam investidas; a folha só para as deduções futuras quando o AEPN é atualizado.
- **Problema relatado:** expectativa do cliente de que a folha reembolse contribuições do empregado após opt-out.
- **Erro identificado:** nenhum; divergência de expectativa do cliente (T10). Risco: cliente pressionou por resposta no dia do fechamento da folha; SLA interno quase perdido (Yojana pede urgência).
- **Causa raiz:** regra de opt-out não documentada ao cliente [INCERTO].
- **Solução aplicada:** resposta com base na FAQ da NAERSA (2026-07-17). Mensagem do HR Blizz "já para as deduções a cada rodada" não tem evidência no ticket.
- **O que não aconteceu / ficou aberto:** resposta da NAERSA à consulta formal da compliance não consta.
- **Tipo de erro:** T10, T11.
- **Lição para o pipeline:** F43 / F58 (ciclo de opt-out/cessação). Solução reutilizável abaixo.

## HRBS-11413 — Chad: payslip em francês (Baker Hughes)
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** Chad / Baker Hughes (Implementation) / Question / Inquiry (SLA Breached) / resolvido / 2026-07-02 / 2026-07-22
- **Linha do tempo:** 2026-07-02, Hayat Harmy: a entidade está em discovery; o cliente exige payslip em francês; pede desenvolvimento do payslip do país conforme amostras anexas (zip). 2026-07-16: reports team pergunta se há CR; resposta: não é CR, é payslip país-específico conforme o artefato de compliance (link). 2026-07-20/21: Mohit pede a Wallisson abrir SR se necessário. 2026-07-22, Wallisson: SR-371 "TD: Payslip".
- **Problema relatado:** não existia payslip padrão de Chad em francês para a entidade.
- **Erro identificado:** lacuna de entrega (payslip do país não existia no momento); o ticket de implementação esperou 14 dias por triagem.
- **Causa raiz:** Chad ainda sem payslip aprovado; pedido caiu como "CR?" por falta de roteamento claro.
- **Solução aplicada:** SR-371 aberto; em HRBS-11891 (2026-08-13) Wallisson confirma payslip padrão de Chad desenvolvido em inglês e francês.
- **O que não aconteceu / ficou aberto:** não consta se o payslip de SR-371 usa as amostras do cliente; versão não consta.
- **Tipo de erro:** T9, T6.
- **Lição para o pipeline:** F57 e F54. Ver HRBS-11891.

## HRBS-11891 — Idioma do payslip (Côte d'Ivoire, Chad, Moçambique, Guiné Equatorial) para Baker Hughes
- **País / Cliente / Tipo / Estado atual / Criado / Resolvido:** CI (também TD, MZ, GQ) / Baker Hughes (Implementation) / Question / Inquiry (SLA Breached) / resolvido / 2026-07-15 / 2026-08-14
- **Linha do tempo:**
  - 2026-07-15, Sivaranjani Subbarayula: é possível gerar payslip em francês (CI, Chad), português (Moçambique), espanhol (Guiné Equatorial)? É exigido por lei?
  - 2026-07-18, Wallisson: nenhum dos quatro códigos de trabalho contém artigo explícito sobre o idioma do payslip; a exigência vem do regime de línguas oficiais: CI: francês efetivamente obrigatório (Décret 96-287, art. 4 exige contrato em francês; bulletin de paie no art. 32.5 do Code du travail, Loi 2015-532); Moçambique: português (Lei 13/2023, art. 123, em vigor desde 21/2/2024, substituiu a Lei 23/2007; sem idioma explícito; português é a língua oficial); Guiné Equatorial: espanhol (Ley 4/2021, que substituiu a Ley 10/2012); Chad: francês aceitável, mas não o único (francês e árabe oficiais, Constituição art. 9; Loi 038/PR/96 art. 263 sobre payslip silencia sobre idioma). Corrige uma fonte secundária que citava "art. 125" do Chad como exigência de contrato em francês; esse artigo trata de reemprego de deficientes.
  - 2026-07-21, Sivaranjani: cliente quer o desenvolvimento no sistema; pergunta se o payslip padrão de Chad já existe e em que idioma.
  - 2026-08-13, Wallisson: payslip padrão de Chad desenvolvido, inglês e francês (TD_Compliance_Payslip_Generator).
- **Problema relatado:** requisito de idioma do payslip e disponibilidade.
- **Erro identificado:** nenhum erro; uma fonte secundária errada (art. 125 do Chad) foi descartada. Lacuna: payslips por idioma dos outros países (CI, MZ, GQ) não existem como artefato.
- **Causa raiz:** payslips padrão dos países da África/Lusófona em inglês apenas; pedido de idioma só surge na implementação.
- **Solução aplicada:** parecer jurídico sobre idioma (2026-07-18) e confirmação do payslip de Chad (2026-08-13).
- **O que não aconteceu / ficou aberto:** payslips de CI (francês), MZ (português), GQ (espanhol): "o cliente também espera o desenvolvimento" e o ticket não mostra desfecho. [INCERTO] sobre as leis de GQ e Chad citadas (não verificadas aqui).
- **Tipo de erro:** T9, T12, T6.
- **Lição para o pipeline:** F57 (payslip) e NOVO: **idioma legal do payslip por país** na ficha do país (campo "idioma exigido/aceito").

---

## Sem conteúdo analisável (só título/metadados, sem descrição ou comentários)

- **CT-3271** — CZ: WTC (Documentation; resolvido 2025-09-05).
- **CT-3344** — BR: Payroll Regulation Guide (resolvido 2025-07-17).
- **CT-3349** — BR: Standard Operating Procedures (resolvido 2025-07-17).
- **CT-3402** — BR: eSocial SOP (resolvido 2025-07-17).
- **CT-3428** — BR: reunir e traduzir toda a legislação de folha do Brasil (resolvido 2025-07-17).
- **CT-3510** — BR: revisão dos campos de cada evento do eSocial (descrição de uma linha; resolvido 2025-07-17).
- **CT-3700** — AU: simulações em software de terceiros (resolvido 2025-07-29).
- **CT-3701** — CZ: simulações em software de terceiros (resolvido 2025-09-05); relacionado ao item pendente de CT-3661.
- **CT-3920** — PT: entrevistas com o ICE ("Get ICE onboarded"; resolvido 2025-09-22).
- **CT-3929** — NL: payslips de agosto, campo "Original Hire Date" aparecendo como Hire date (título aponta T9/T4; só tem o link do Freshdesk 48778; resolvido 2025-09-09).

Observação: os tickets CT-3271, 3344, 3349, 3402, 3428, 3510 são tarefas de construção de pacote (Regulation Build/Statutory Reports), fechados em lote entre 2025-07-17 e 2025-09-05.

---

## Resumo

| ID | País | Tipo(s) | Artefato | Resolvido? | F-xx / NOVO |
|---|---|---|---|---|---|
| CT-3116 | PT | T6, T11, T12 | Regulation (IRS Jovem, SS) | Parcial (doc, sem artefato) | F43, F52 |
| CT-3608 | NG | T1, T11 | Alerta Finance Act 2026 | Sim (alerta) | F44, NOVO calendário de vigências |
| CT-3648 | MY | T1, T2, T7, T12 | WTC/config EPF | Sim | F51, F50 |
| CT-3661 | CZ | T6, T11 | Handover checklist | Não (Won't Do) | NOVO gate sem critério |
| CT-3792 | NL | T7 | Regra 30% ruling | Sim (doc) | F52, F45 |
| CT-3842 | PT | T1 | Tabela de retenção (alerta) | Sim | F44 |
| CT-3887 | PT | T1 | RCA de tabela perdida | Sim (RCA) | F44 |
| CT-3892 | NL | T3, T5, T10 | Report Spec XML / config WT | Sim | F49, F50 |
| CT-3932 | NL | T7, T10, T11, T12 | Doc SOW 30% ruling | Sim (esclarecido) | F42, F51 |
| CT-3943 | NL | T1, T6 | Tabelas Green/White 2025 | Sim | F44, F41 |
| CT-3945 | TR | T2, T7, T12 | Resposta anterior / regra de dedução | Sim (após 3 correções) | F51, F41 |
| CT-3957 | NL | T5, T10 | Relatório custom × XML | Esclarecido, correção não consta | F54 |
| CT-4005 | AU | T6, T11, T12 | Relatório SAFF | Sim (decisão de escopo) | F54 |
| CT-4008 | AU | T9 | Payslip Generator | Sim | F57 |
| CT-4039 | PT | T1, T8 | Alerta tabela (duplicata) | Sim (sem conteúdo) | F52 |
| CT-4076 | AU | T6, T10 | WTC (workers' comp) | Sim | NOVO custo do empregador fora do WTC |
| CT-4078 | IE | T11, T12 | Integração ROS | Sim (análise) | NOVO mudança de identidade do empregador |
| CT-4136 | NL | T2, T7 | Design 30% ruling | Parcial (KT pendente) | F46, F51 |
| CT-4169 | AU | T1, T8 | Regulation Guide | Sim | F18, F44, F27, F59 |
| CT-4322 | AU | T2, T3 | WTC 3.1 → 3.2 | Sim | F50 |
| CT-4391 | BG | T11 | CCG (queries) | Sim | F6 |
| CT-617 | CO | T7, T12 | Regra de arredondamento PILA | Remetido a HRBS-182 | F37, F42 |
| CT-70 | PT | T7, T12 | Regulation (negativos) | Sim (doc) | F58, F52 |
| HRBS-10915 | ES | T11, T5 | Amostras de relatórios | Sim | F54, F55 |
| HRBS-11736 | ES | T5, T6 | Report Spec (Cert. Retenciones) | Em desenvolvimento (SR-342) | F54 |
| HRBS-11790 | ES | T4, T11 | DD (child_count_under_3) | Sim | F59, F52 |
| HRBS-117 | AU | T11, T5 | G2N report | Sim | F54 |
| HRBS-118 | AU | T6, T11 | Regulation (workers' comp pós-desligamento) | Sim (doc) | F43 |
| HRBS-11806 | CG | T3, T7 | WTC (SS patronal) | Sim (WTC v1.1) | NOVO fórmula duplicada, F45 |
| HRBS-11814 | GA/CG | T9, T11, T12 | Payslip | Sim | F57 |
| HRBS-11864 | IE | T10, T11 | Config NAERSA / resposta | Sim | F43/F58 |
| HRBS-11413 | TD | T9, T6 | Payslip país | Sim (SR-371) | F57, F54 |
| HRBS-11891 | CI/TD/MZ/GQ | T9, T12, T6 | Payslip (idioma) | Parcial (só Chad) | F57, NOVO idioma legal |

(Mais 10 tickets sem conteúdo listados acima: total 43.)

## Padrões recorrentes no lote

- **Respostas viram "Google Doc solto":** em 14 dos 33 tickets o resultado é só um link de documento, sem atualizar o CCG/WTC e sem registrar a decisão no ticket (CT-3116, 3608, 3792, 3842, 3943, 4005, 4078, 4136, 70, HRBS-117/118...). É a F52 em escala; a fonte única de verdade falta.
- **Limites e acumuladores definidos tarde ou errado:** TR seguro privado (3 versões da regra), 30% ruling (limiar por dias, base com/sem pré-imposto), MY EPF (base real × faixa, arredondamento), CO PILA (base × contribuição). Todos são F51/F37.
- **Flags de WT sem base legal:** WTC 3.1 de AU precisou alterar 15+ linhas (super, STP, table tax) e o WTC de Congo tinha 3 linhas com a mesma fórmula (F50, nova).
- **Vigência futura/atualização de tabela:** PT tabelas de retenção perdidas (CT-3842/3887/4039), NG 2026, MY Oct/2025, AU Medicare levy. Falta calendário de vigências com dono.
- **Fronteira de escopo mal comunicada:** custo do empregador (workers' comp), relatórios custom × estatutário (NL), SAFF (AU), reembolso NAERSA (IE) — cliente espera algo que a folha não faz. Sem lista pública de "o que não é nosso" por país (F54).
- **Payslip por país:** moeda errada (AU USD), campos legais (Gabon/Congo), idioma (CI/MZ/GQ/TD); F57 aparece em 4 tickets.
- **Tickets longevos ou "resolvidos" cedo demais:** CT-70 (17 meses), CT-617 (12 meses em espera), CT-3661 (Won't Do), HRBS-11736 (fechado antes da entrega).

## Soluções reutilizáveis

1. **TR, seguro de vida privado (dedução do IR):** dedução mensal = mínimo(prêmio elegível do mês [50% em vida com poupança, 100% em risco], 15% do bruto **do mês** [teste mensal, não cumulativo], saldo restante do teto anual). Teto anual 2025 = 312.066 TRY (12 x 26.005,50), cumulativo YTD. Fonte: folheto GİB 2025 (seguros de vida e pessoais), EY Turkey Tax Guide 2025, PwC Worldwide Tax Summaries (CT-3945). "IR cumulativo" refere-se à tabela progressiva, não aos limites da dedução. Empregador pagando: tratamento como benefício tributável sujeito a SSI [sem fonte específica].
2. **MY, EPF para não cidadãos (salários a partir de outubro/2025):** 2% empregado e 2% empregador sobre salário mensal (fonte KWSP, páginas oficiais; sem circular no ticket). Quem já contribui na taxa malaia mantém 11% sobre salário real e a decisão do ticket é mapear os 11% inteiros como EPF obrigatório (não 2% + 9% voluntário). Pendente [INCERTO]: base em faixas × salário real, arredondamento e mid-month.
3. **CO, arredondamento PILA (Decreto 1990/2016, art. 3.2.1.5 do Decreto 780/2016):** IBC ao peso superior; valor das contribuições e juros ao múltiplo de 100 mais próximo. O exemplo do ticket (base arredondada a 100) contradiz o texto legal citado.
4. **Congo (CNSS), SS patronal em três ramos distintos:** PVID empregador 8% (teto 1.200.000 XAF); Prestações familiares 10,03% (teto 600.000 XAF); AT-MP 2,25% (teto 600.000 XAF), sem diferenciação por setor (confirmado com a CNSS Congo); os três ramos são pagos num único borderô. O WTC v1.1 corrige linhas duplicadas.
5. **IE, opt-out do auto-enrolment (NAERSA/MyFutureFund):** a folha não reembolsa; NAERSA devolve ao empregado direto; contribuições do empregador e do Estado ficam investidas; a folha só para as deduções quando o AEPN é atualizado (FAQ do empregador myfuturefund.ie/employer-faq).
6. **AU, flags de WTC (WTC 3.2):** bônus = STP "BC Bonus and commissions" e entra no GrossA; car allowances tributáveis e payments de income protection = OTE (super Yes); licença sem remuneração = Taxable No / Table Tax NA; workers' comp pago = super No (SGR 2009/2). Verificar [INCERTO] os dois últimos antes de absorver (sem ruling específico).
7. **AU, escopo:** custo de workers' comp e payroll tax do empregador não é WT nem cálculo da folha; SAFF não é relatório padrão (sob demanda; Payday Super a partir de 1/7/2026 muda o prazo, não o formato); payslip deve usar AUD.
8. **ES, descendente ≤ 3 anos:** o DD usa `$hr.child_count_under_3` (autodeclarado, como o Modelo 145) em vez de ano de nascimento; art. 58.2 LIRPF, +2.800 euros/ano por descendente (1.400/1.400 se casal); exceções de falecimento e adoção/acogimiento (3 anos fiscais).
9. **NL, 30% ruling:** o ruling não se aplica à base Green, só a White e White-Special; limiar proporcional = anual ÷ dias do ano × dias trabalhados; reconciliação mensal cumulativa é para todos. Deduções pré-imposto: lacuna aberta (CT-4136).
10. **Idioma do payslip:** nenhum código de trabalho de CI, MZ, GQ ou TD exige idioma de forma expressa; CI e MZ efetivamente em francês e português; GQ espanhol; Chad francês ou árabe (payslip padrão de Chad entregue em inglês e francês). Payslips de CI, MZ, GQ ainda sem confirmação.
11. **Processo:** queries do design vão dentro do CCG (CT-4391); ticket de pedido fica aberto até a entrega do SR (HRBS-11736).
