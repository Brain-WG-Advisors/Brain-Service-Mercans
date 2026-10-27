# Padrões nos prompts do usuário (Claude Code, 2026-09-25 a 2026-10-27)

> Análise de 2026-10-27 (janela geral): mensagens do usuário em 47 conversas do Claude Code (25/09–27/10). As 12 propostas foram aprovadas pelo usuário e aplicadas no [[CLAUDE]] (seção "Respostas eficientes"), nas frentes [[frentes/gmail/CLAUDE|Gmail]] e [[frentes/chat/CLAUDE|Chat]] (roteiro do Chrome) e em `scripts/` (achar_versao, conferir_import, onde_estamos).

**Base:** 2.082 mensagens, 61 sessões. Fora da análise: `<browser_instruction>` e o projeto Tentencias. Sobram **1.981**. Sessões retomadas repetem mensagens, então as contagens usam:
- **1.621 únicas** (dedupe global por texto) para padrões e retrabalho;
- **1.865** (dedupe por sessão) para aprovações e handoffs.

**Como foi medido:** a classificação é por expressões regulares, e uma mensagem pode cair em mais de um padrão. Os números são ordem de grandeza, não contagem exata.

**Volume por janela (1.981):**

| Janela | Mensagens |
|---|---|
| geral | 900 |
| chat | 302 |
| fr-research-validation | 201 |
| gmail | 178 |
| suporte | 154 |
| pipeline | 118 |
| certificação | 19 + 14 |

Mediana: 64 caracteres por mensagem. **985 mensagens (50%) têm até 60 caracteres**, a maioria aprovações, checagens e handoffs.

---

## 1. Padrões de pedido recorrentes

| # | Padrão | Freq. (únicas) | Onde aparece | Exemplos (parafraseados) | Pedido implícito |
|---|---|---|---|---|---|
| 1 | **Analisar mensagem colada do chat ou de gestor** | ~250 | chat 119, geral 61, gmail 30 | "veja o que a gerente respondeu"; "analise o que a AUTOMATION respondeu e o chat"; "mandei para o chat, analise" | Dizer o que ela pede, o que é nosso e o próximo passo, com o rascunho de resposta já pronto |
| 2 | **Checagem "100% de confiança?"** | 165 | geral 78, gmail 27, suporte 23, chat 23 | "tem 100% de confiança nesse texto?"; "estamos fazendo literalmente o que ela pediu?"; "de 0 a 100, quanto estamos?" | Mostrar a prova: cada afirmação com fonte, pergunta → resposta, e o que ainda não está provado |
| 3 | **Tratar e-mail** (analisar, responder, decidir se envia) | ~125 | geral 77, pipeline 17, gmail 15 | "o e-mail sobre a ferramenta está certo? posso enviar?"; "o que a primeira mensagem pede?"; "qual e-mail ainda precisamos tratar?" | Fila de e-mails com status (agir, aguardando, pronto para enviar) e rascunho já feito |
| 4 | **Artefato (DD/WTC/Spec/CCG/SIR)** | ~123 | geral 63, chat 18 | "já fizemos CCG, WTC e DD?"; "já subiu as specs e o DD para o Drive?"; "fizemos algo de report spec para a Lituânia?" | Situação de cada artefato por país (versão vigente, local, alterado/pendente) sem precisar perguntar |
| 5 | **Drive / Chrome / navegador** | ~106 | geral 58, chat 16 | "navegue no Drive e faça as importações"; "use o Claude in Chrome para ler o DM"; "pode atualizar o Sheet no Drive" | Executar no navegador e devolver o link ou a prova; Drive só quando ele manda |
| 6 | **Rascunho / draft** (gravar, trocar, deixar pronto) | ~83 | geral 39, pipeline 16, gmail 10 | "grave o rascunho do que foi perguntado no ticket"; "deixe tudo em draft para eu analisar"; "pode trocar o texto do rascunho por essa versão" | Rascunho gravado, nunca enviado, com o link para ele conferir |
| 7 | **Registrar no cérebro / hub / skill** | ~57 | geral 27, chat 8 | "registra no hub e fecha a sessão"; "você atualizou a skill, certo?"; "registre isso no chat AUTOMATION" | Registro automático ao fim de cada entrega, com confirmação curta |
| 8 | **Pesquisa em fonte oficial / lei** | ~55 | geral 24, suporte 8, gmail 8 | "com base em fontes oficiais, qual a melhor saída para as duas dúvidas?"; "faça a busca para chegar aos 100%" | Decisão já fundamentada em fonte primária, sem ele precisar pedir |
| 9 | **Responder ticket / comentário do YouTrack** | ~47 | geral 22, gmail 10, chat 7, suporte 5 | "analise as respostas dos tickets direcionados a mim"; "cole a resposta final no comentário"; "separe o que vai para o chat do que vai para o ticket" | Protocolo de ticket completo, com o rascunho no ticket para ele aprovar |
| 10 | **Simulação FR / validação de reports** | ~42 | fr-research-validation 20, chat 9 | "atualize o fr_simulation_2026"; "deixe as planilhas organizadas"; "conseguimos realizar a validação?" | Planilha final no formato pedido, sem idas e vindas de layout |
| 11 | **Ir por etapas, grupos ou itens** | ~40 | geral 25, gmail 7 | "vamos para o grupo 2"; "parta para o 3 e o 4"; "pronto, 1 enviado, agora o dois" | Seguir sozinho para o próximo item e só parar no que exige ok |
| 12 | **Pipeline / build de país / skill** | ~37 | geral 21 | "o e-mail da Colômbia aponta gaps do pipeline, conserte"; "isso inclui a versão nova do pipeline?" | Correção no pipeline e na skill, com registro, sem ele acompanhar cada passo |
| 13 | **Status, progresso, próximo passo** | ~35 | geral 14, chat 5, gmail 5 | "o que precisamos fazer agora?"; "em porcentagem, quanto avançamos?"; "o que falta para fechar 100%?" | Painel curto com pronto, espera você e espera outros, mais o % de avanço |
| 14 | **"Por quê?" / "o que é isso?"** | ~34 | geral 18, chat 6 | "por que precisamos responder sobre o Líbano?"; "quais são os três caminhos?"; "o que seria esse remark?" | A resposta anterior não trouxe o motivo nem definiu o termo |
| 15 | **Arquivo em Downloads / versão ativa** | ~33 | geral 17 | "a versão ativa do DD está em Downloads"; "os dois transcripts estão em download"; "analise a imagem em downloads" | Procurar em Downloads/Drive a versão mais nova antes de usar a do pipeline |
| 16 | **Abrir, fechar ou delegar para frentes** | ~31 | geral 11, gmail 7, chat 6 | "manda a correção da skill do Egito para a frente Pipeline"; "separe Gmail de YouTrack"; "fecha a sessão" | Roteamento automático para a frente certa |
| 17 | **É nosso? (escopo / fronteira)** | ~19 | geral 10, suporte 3 | "não podemos sair do escopo de compliance"; "isso é para nós fazermos ou não?" | Classificar nosso / outro time antes de redigir |
| 18 | **Certificação / Audit Report** | ~18 | certificação 7, geral 4 | "temos quantos audit reports prontos das validações?"; "use o modelo de audit report como base" | Contagem e estado por país; só validar, não corrigir |
| 19 | **Autonomia explícita** | 11 | geral 5, validação 3 | "faça sempre o recomendado"; "resolva tudo o que consegue sem mim"; "você não conseguiria decidir por mim?" | Menos perguntas: seguir a recomendação e só parar em gravar ou enviar |

---

## 2. Ciclos de retrabalho

A exportação tem só as mensagens do usuário. O "tipo de resposta anterior" foi deduzido da mensagem que ele mandou antes e do teor da correção.

| Causa | Ocorrências (únicas) | O que veio antes | Causa provável |
|---|---|---|---|
| **Checagem de confiança** ("tem 100%?", "agora sim temos 100%?") | **165**, em 22 de 47 sessões; **28 cadeias** de 2+ checagens seguidas | 74 vieram logo após um pedido de resposta, rascunho ou e-mail; 13 após alteração de arquivo | A resposta foi apresentada sem prova à vista (fonte por afirmação, pergunta → resposta) e sem o que falta. Ele precisa perguntar para descobrir |
| **Fora do pedido / escopo** ("responder só o que ela pediu", "não precisa falar disso", "simplesmente não responda X") | **59** | Rascunho para gestor ou SBC com assuntos a mais (reports já prontos, outro país, blue-collar) | Achado fora do pedido entrou na resposta em vez de ir para o hub |
| **Verbosidade** ("mais direto", "muita coisa", "ela sabe o que é óbvio") | **38**, chat 14, geral 13 | Mensagem para a gerente ou o diretor; apresentação longa ao usuário | Faltou formato curto fixo para mensagens internas e para o usuário |
| **Incompreensão** ("não entendi", "1. não entendi 2. não entendi") | **37** | Perguntas numeradas técnicas (configuração, bloqueios, decisões de pipeline) | Opções sem contexto, jargão, ou decisão sem recomendação |
| **Repetição de instrução** ("como já disse", "de novo", "ainda não") | **35** | Pedido de layout de planilha (FR simulation) repetido 5 vezes; "esquecer os idiomas da Bélgica" repetido | Instrução de sessão não virou regra persistente; layout pedido não foi seguido de primeira |
| **Base / arquivo / contexto errado** ("respondemos no arquivo errado?", "e-mail já respondido", "a versão ativa está em Downloads") | **20** | Trabalho sobre uma versão defasada ou item já resolvido | Faltou checar a versão mais nova e o estado atual antes de agir |
| **"Por que você fez X?"** | **15** | Ação sem justificativa visível (responder algo já respondido, sem 100%) | Faltou explicar a decisão em 1 linha |
| **Confusão do próprio usuário** ("confundi", "pode esquecer o SR-x") | 8 | — | Não é falha nossa; um painel de itens ativos ajuda |
| **Atrito de ferramenta** (Chrome, interrupção, "tentar novamente", "reiniciei") | ~70 menções (amplo) | Claude in Chrome sem conexão; execução interrompida | Infraestrutura. Diagnóstico padrão evita "como faço?" |

**Tendência das checagens de 100%** (% das mensagens da semana):

| Semana ISO | Checagens | % |
|---|---|---|
| 41 | 6 | 4% |
| 42 | 71 | **16%** |
| 43 | 69 | 9% |
| 44 | 19 | 7% |

Caiu depois da memória "100% antes de apresentar", mas continua sendo a maior causa de ida e volta.

---

## 3. Aprovações em série

Há **120 mensagens só de aprovação**:

| Tipo de aprovação | Quantas | Pergunta que a gerou |
|---|---|---|
| "sim / ok / pode / siga" puro | 70 | Plano de passos, pergunta "posso seguir?" |
| "vamos para o próximo / grupo 2 / item 3" | 30 | Fim de um item numa lista |
| "pode gravar / trocar o rascunho / incluir a frase" | 20 | Ok para gravar o rascunho |

A palavra "pronto" sozinha aparece 28 vezes (bruto).

**Viram "fazer sem perguntar":**
- Passar ao próximo item de uma lista já aprovada (grupo 2 → 3).
- Ler, analisar e pesquisar fonte oficial; baixar arquivo pelo Chrome **para leitura**.
- Atualizar notas do cérebro: hub, `correcoes.md`, `log.md` e estado da frente.
- Delegar à frente certa.
- Escolher a opção recomendada quando a decisão é técnica e reversível. Ele pediu isso 11 vezes: "faça sempre o recomendado", "aprovo as recomendações".
- Revisar o próprio rascunho até a prova completa antes de apresentar (hoje ele pede).

**Continuam pedindo ok:**
- Gravar ou trocar o rascunho no YouTrack (draftComment) e o rascunho no Gmail.
- Enviar ou postar qualquer coisa.
- Subir ou importar no Drive.
- Alterar artefato de terceiro ou de país ativo (exige ticket ao Development).
- Commit e git.
- Decisão de escopo diante da gerente ou do diretor.

---

## 4. Handoffs manuais

| Handoff | Quantas | Fluxo típico | O que antecipar |
|---|---|---|---|
| **Enviei / mandei / postei / publiquei** | 57 (chat 22) | Ele envia o rascunho aprovado e volta com "enviei, agora o dois" | Já deixar o próximo item analisado e o registro (hub e log) pronto para gravar com o "enviei" |
| **"X respondeu"** (resposta de terceiro) | 41 (chat 24) | "a gerente respondeu", "veja se a SBC respondeu" | Ao receber: diff contra o que perguntamos, o que mudou e o rascunho da próxima resposta, numa só mensagem |
| **Arquivo em Downloads** | 39 | "está em download", "a versão ativa do DD está em Downloads" | Varrer Downloads por padrão (o mais recente por país e artefato) antes de pedir arquivo e dizer qual vai usar |
| **"Pronto"** (fez o passo pedido) | 32 | Exportou, autorizou, reiniciou, importou | Ao pedir um passo manual, dizer já o que será feito depois do "pronto" e fazer direto, sem nova pergunta |
| **Exportei / importei / baixei / subi** | 14 | Exporta o Sheet para xlsx, importa a versão nova no Drive | Depois do "importei": conferir sozinho (md5 / export csv do gid) e registrar; antes, deixar o checklist do import |

---

## 5. Propostas concretas (máx. 12)

| # | Padrão que resolve | Mudança | Ganho estimado | Risco |
|---|---|---|---|---|
| 1 | Checagem de 100% (165) | **Formato fixo "Bloco de prova"** no fim de toda resposta, rascunho ou alteração para terceiros: (a) pergunta → resposta, item a item; (b) afirmação → fonte primária lida (link ou página); (c) teste mecânico feito; (d) **Confiança: 100% / X% – falta: …**. Regra no CLAUDE.md: abaixo de 100%, não apresentar como pronto; dizer o que falta e já ir buscar | ~120 msgs (fim da maioria das cadeias "tem 100%? → agora sim?") | Respostas mais longas. Mitigar: bloco em 3–6 linhas, tabela só se mais de 3 itens |
| 2 | Fora do pedido (59) + verbosidade (38) | **Formato fixo para mensagens internas** (gerente, diretor, chat): 1–3 frases, só o perguntado, sem explicar o óbvio. Achados extras vão para o hub e aparecem numa linha separada "fora do pedido (não incluído): …" só para o usuário | ~70 msgs | Omitir algo que ele queria. A linha "fora do pedido" deixa ele puxar de volta |
| 3 | Aprovações "próximo item" (30) + autonomia (11) + "sim/ok" (70) | **Regra "fazer sem perguntar"** no CLAUDE.md, com a lista do §3. Em lista aprovada, seguir item a item e parar só em gravar, enviar, Drive, artefato de terceiro ou escopo. Decisão técnica reversível: aplicar a recomendada e avisar | ~80 msgs | Agir em algo que ele queria revisar. Mitigar: lista explícita do que sempre para, e cada passo registrado |
| 4 | "X respondeu" (41) + mensagem colada (250) | **Comando "chegou resposta de X"** com saída fixa: o que pediu / o que é nosso / o que mudou vs. nossa última mensagem / rascunho da resposta + Bloco de prova / onde registrar | ~40 msgs (fim do "o que ela pede? → e o que respondemos? → é nosso?") | Baixo |
| 5 | Downloads / versão ativa (33) + base errada (20) | **Script `achar_versao.py <país> <artefato>`**: varre Downloads, Drive (G:) e `Research Pipeline/`, lista as versões com data e md5 e aponta a maior (regra 8). Regra: rodar antes de editar qualquer artefato e dizer qual base será usada | ~35 msgs | Nome fora do padrão escapar da busca. Mitigar: listar candidatos por data também |
| 6 | Status / progresso (35) + "o que precisamos fazer agora?" | **Comando "onde estamos?"** com resposta fixa: ✅ / ⏳ espera você / 🔄 espera outros + % por frente ou entrega (itens fechados / total), a partir dos `estado.md` | ~30 msgs | % enganoso se o total mudar. Mostrar "x de y" |
| 7 | Incompreensão (37) em perguntas numeradas | **Regra de pergunta**: toda pergunta ao usuário vem com contexto em 1 linha, recomendação e "se não responder, faço A". Nada de jargão sem tradução (settings, hooks, bloqueios) | ~30 msgs | Baixo |
| 8 | Repetição de instrução (35) | **Captura imediata**: quando ele diz "esquece X", "não precisa Y" ou "sempre Z", gravar na hora no `estado.md` da frente (seção "Instruções vigentes da sessão") e reler antes de cada entrega. Layout de planilha pedido vira modelo em `modelos/` | ~25 msgs | Estado inflado. Limpar no "fecha a sessão" |
| 9 | Handoff "enviei / pronto" (57 + 32) | **Pós-handoff automático**: ao pedir um passo manual, já dizer "quando você disser 'pronto', eu faço: 1…2…". No "enviei": registrar no hub e log, marcar o item como fechado e abrir o próximo item da fila | ~40 msgs | Registrar envio que não aconteceu. Só registrar com "enviei" explícito |
| 10 | Importei / exportei (14) + checagem pós-Drive | **Script de conferência pós-import** (md5 local × Drive; export csv por gid para Sheets) rodando sozinho depois do "importei", com resultado em 1 linha | ~10 msgs | Baixo (só leitura) |
| 11 | Delegação para frentes (31) | **Roteamento automático** na janela geral: classificar o pedido (ticket, e-mail, chat, pipeline, certificação) e já mandar a tarefa fechada, com aviso de 1 linha, sem perguntar a quem mandar | ~15 msgs | Frente errada ou ocupada. Avisar e permitir "não, faz aqui" |
| 12 | Atrito Chrome (~70) | **Checklist de diagnóstico** no CLAUDE.md da frente Gmail/Chat: `list_connected_browsers`, então `tabs_context`, então "reabra a aba X"; em 1 mensagem, com a ação exata que ele deve fazer | ~20 msgs | Baixo |

### As 5 de maior retorno

1. **Bloco de prova + confiança declarada** (proposta 1)
2. **Fazer sem perguntar** em listas aprovadas e decisões reversíveis (proposta 3)
3. **Formato curto para mensagens internas** com a linha "fora do pedido" (proposta 2)
4. **Comando "chegou resposta de X"** (proposta 4)
5. **Script de versão vigente antes de editar** (proposta 5)

Todas respeitam: nada enviado sem ok; Drive só quando ele manda; artefato de terceiro com confirmação.
