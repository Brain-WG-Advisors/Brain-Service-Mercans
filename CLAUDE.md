# Brain Service — Cérebro do Serviço

Este é o cérebro do **serviço que prestamos para a Mercans** (compliance de payroll). Não é o cérebro da Mercans inteira: cobre só o que entregamos e sustentamos.

Responda e escreva sempre em **português do Brasil** (termos técnicos e nomes de artefatos podem ficar em inglês).

## O serviço (escopo)
```
[1. Research Pipeline] → [2. Design] → (Produção / ativação: outro time) → [3. Suporte]
        nosso                nosso            FORA DO ESCOPO                 nosso
```
- **Research Pipeline:** pesquisa estatutária do país e geração dos artefatos (CCG, WTC, DD, Report Specs, SIR...).
- **Design:** o que é desenhado a partir do research (detalhar em `servicos/design.md`).
- **Suporte:** tickets e dúvidas sobre os artefatos que entregamos.
- O que é de outros times fica em `fronteiras.md`. Não documente o trabalho de outros times além da fronteira.

## Início de toda sessão
Colar `prompts/abrir-sessao.md`. Ler o `PLANO.md` (modelo de construção e painel de progresso) e seguir o Protocolo de sessão dele: uma fase ou fonte por sessão; padrão de dado sólido (níveis A/B/C/D); inventário antes de extrair; nada ingerido sem validação do usuário; ao final, log, painel, commit e resumo.

## Estrutura da pasta
| Caminho | O que é |
|---|---|
| `00-INDEX.md` | Centro do cérebro: catálogo do serviço + painel países × etapa. |
| `servicos/` | Uma nota por serviço: o que recebemos, o que entregamos, como sabemos que ficou certo, o que já deu errado. |
| `paises/<País>.md` | Hub do país: etapa atual, artefatos e versões, decisões, valores com vigência, tickets. |
| `correcoes.md` | Erros já cometidos e a versão correta. **Ler antes de qualquer resposta.** |
| `fronteiras.md` | O que não é nosso e para quem vai. |
| `raw/` | Material bruto (exportações de chats, tickets, documentos). **Nunca editar nem apagar.** `raw/reunioes/` e `raw/drive/` ficam fora do git. |
| `inventarios/` | Lista completa de cada fonte no período, com o resultado de cada item (cartão/descartado/pendente). |
| `extracoes/` | Cartões extraídos de cada coleta (o filtro entre `raw/` e as notas). |
| `testes/` | Teste de exatidão rodado no claude.ai (antes × depois). |
| `revisoes/`, `rascunhos/` | Relatórios de revisão e rascunhos de resposta/pacotes (não enviados). |
| `scripts/` | Scripts de coleta (ex.: `youtrack_fetch.ps1`). |
| `modelos/` | Modelos de nota. Usar sempre ao criar nota nova. |
| `prompts/` | Prompts prontos (ex.: extração de conhecimento dos projetos do Claude). |
| `log.md` | Registro cronológico, só acrescentar no fim. |
| `ESTADO.md` | **Onde paramos (geral):** pendências do usuário que não são de uma frente só. Aponta para `frentes/`. **Ler ao abrir qualquer sessão.** |
| `frentes/<frente>/` | Pasta de cada frente (`suporte`, `gmail`, `chat`, `pipeline`, `certificacao`): `CLAUDE.md` da frente, `estado.md` (escrito só por aquela janela) e `.claude/settings.json` (libera a raiz). |
| `rotinas.md` | As 5 frentes do serviço (Suporte, Gmail, Chat, Research pipeline, Análise de Reports): para que serve, entrega, onde fica o estado. Rodam quando o usuário avisa. |
| `sessoes/AAAA-MM-DD.md` | Retrospectiva de cada sessão (o que foi feito, aprendido, corrigido). Modelo: `modelos/sessao.md`. |
| `rascunhos/` | Rascunhos de resposta e revisões (antes de ir para ticket/arquivo). |
| `Research Pipeline/` | Pasta de trabalho do Research Pipeline (antes `Documents\Research Pipeline`, que agora é atalho para cá): builds e correções por país, com os arquivos reais. Ver "Arquivos dentro do cérebro". |
| `internal-certification/` | Pasta da Internal Certification (antes `Documents\internal-certification`, agora atalho para cá): validações, relatórios e workbooks por país. |
| `raw/docs/oficiais/<CC>/` | Fontes oficiais baixadas (XSD, formulários, leis), com data no nome. |
| `PLANO.md` | Plano de ação de implantação. |
| `_arquivo/` | Projeto antigo (automação Trello). Não faz parte do cérebro; não ler, salvo pedido. |

## Abrir a sessão
Antes da primeira tarefa: ler `ESTADO.md` e as últimas linhas de `log.md`; rodar `scripts/youtrack_fetch.ps1 -DryRun -Query "for: me #Unresolved"` para ver a fila atual (tickets podem ter sido atribuídos depois da última sessão).
- **Tickets dos hubs:** `python scripts/atualizar_tickets.py` (estado na API → properties, linha Suporte dos hubs e painel do 00-INDEX). Rodar ao abrir o dia.
- **Toda task de país começa por** `python scripts/contexto_pais.py <País|código>`: versões vigentes, tickets abertos, correções, pendências e valores sem fonte num passo só. Detalhe exato: abrir o arquivo citado.

## Janelas paralelas (decidido em 2026-10-15)
As frentes 1–5 ([[rotinas]]) rodam em janelas separadas do Claude Code, cada uma aberta na sua pasta: **Suporte - Mercans** (`frentes/suporte`), **Gmail - Mercans** (`frentes/gmail`), **Chat - Mercans** (`frentes/chat`), **Pipeline - Mercans** (`frentes/pipeline`, desde 2026-10-15; liga `Documents\Research Pipeline` e `~/mercans-pipeline`), **Certificacao - Mercans** (`frentes/certificacao`, desde 2026-10-15; liga `Documents\internal-certification`). A sessão carrega este CLAUDE.md + o da frente, e o histórico (`/resume`) e a memória ficam separados por frente. Abrir com `scripts/abrir_frentes.ps1` (`-Retomar` para voltar à última conversa de cada uma). A janela aberta na raiz é a **geral** ("abre o dia", "revisa o cérebro", git).
- Cada janela escreve só o seu `frentes/<frente>/estado.md` e os seus rascunhos (`triagem-emails`, `triagem-chat`, respostas de ticket). `ESTADO.md` geral: só a janela geral.
- Arquivos compartilhados (`log.md`, `correcoes.md`, hubs de país, `CLAUDE.md`): **reler imediatamente antes de editar** e alterar com Edit pontual (nunca reescrever o arquivo inteiro); `log.md` só recebe linha no fim.
- Ticket é da janela Suporte: as outras janelas só anotam e avisam o usuário.
- "Fecha a sessão" numa janela de frente: nota `sessoes/AAAA-MM-DD-<frente>.md`, reescreve só o seu `frentes/<frente>/estado.md`.
- Git (commit): só pela janela geral.

## Arquivos dentro do cérebro (decidido em 2026-10-16)
- O cérebro guarda o conhecimento com os **arquivos reais** (xlsx, docx, scripts, logs de conferência), não só notas `.md`. `Research Pipeline/` e `internal-certification/` foram movidas para dentro do brain-service; os caminhos antigos em `Documents\` são atalhos (junction) para as mesmas pastas, então scripts e frentes continuam funcionando.
- Cada entrega fica numa pasta própria dentro da pasta de trabalho do país (ex.: `Research Pipeline/Costa do Marfim/2026-10-16-teto-CNPS/`), com os finais e um `CONFERENCIA.md`: fonte, decisões, antes → depois, conferência e uma linha por frente que mexeu (data, frente, o quê). A frente que alterar depois atualiza o arquivo ali **e** acrescenta a sua linha. Nunca duas versões do mesmo final em lugares diferentes.
- O Drive continua sendo o oficial; o final local é a **cópia idêntica** do que está no Drive (conferir md5).
- Arquivo de ticket (Suporte) segue a mesma regra, na pasta do país em `Research Pipeline/<País>/`.
- Git: tudo entra, menos `*.zip` e `*.pdf` (`.gitignore`; o GitHub recusa arquivo > 100 MB).

## Rede no Obsidian e Graphify (decidido em 2026-10-27)
- A pasta é o cofre do Obsidian.
  - `.obsidian/app.json` exclui `publicar/`, o espelho do pipeline, `fr-research-validation/`, `raw/` e `_arquivo/`.
  - Toda nota nova nasce ligada (hub, conferência, serviço ou nota-mapa). Nenhuma nota fica solta.
- Graphify:
  - O grafo da camada de conhecimento fica em `graphify-out/`, fora do git. O escopo está em `.graphifyignore`, sem cópias de skill nem saídas do pipeline.
  - Para perguntas sobre o cérebro, começar por `graphify query`.
  - Depois de mudar notas, rodar `graphify update .` e reler com agentes só as notas alteradas.
- Script que altera notas em lote:
  - não toca cópias de skill, saídas do pipeline, rascunhos nem os `estado.md` das frentes;
  - age só na seção certa.
- Estado de ticket citado em hub envelhece: conferir na API (`youtrack_fetch.ps1`) antes de agir.

## Papel da janela geral: orquestradora (decidido em 2026-10-15)
Vale só para a janela aberta na raiz. O usuário passa as tarefas aqui; as janelas das frentes executam (sessões `suporte-*`, `gmail-*`, `chat-*`, `pipeline-*`, `certificacao-*` em `ListAgents`; se não estiverem abertas, reabrir com `scripts/abrir_frentes.ps1 -Retomar`).

**Ao receber uma tarefa**
1. Ler `ESTADO.md` e o `frentes/<frente>/estado.md` da frente envolvida.
2. Decidir quem faz: ticket → suporte; e-mail → gmail; chat → chat; pipeline (build/correção de país, backlog de lições) → pipeline; Internal Certification (validação de reports, pacotes das SBCs) → certificacao; git, revisão do cérebro → a própria geral.
3. Mandar por `SendMessage` uma tarefa fechada:
   - **Objetivo:** o que entregar (1 frase).
   - **Contexto:** ticket/e-mail, arquivos, o que já foi feito (com caminho).
   - **Pronto quando:** critério verificável (ex.: "rascunho gravado e conferido, não enviado").
   - **Regras:** skill antes; fonte primária para cada afirmação; apresentar ao usuário antes de gravar; nunca enviar.
   - **Devolver:** resumo em até 5 linhas + o que espera o usuário (por `SendMessage` para a janela geral).
4. Não refazer o trabalho da frente. Se o retorno vier sem prova, devolver pedindo a fonte.

**Ao responder ao usuário**
- Painel curto: ✅ pronto | ⏳ espera você | 🔄 espera outros/frente.
- Só o que mudou desde o último painel, sem repetir o que já foi dito.
- Decisão que é do usuário: perguntar, com recomendação.

**O que não fazer**
- Não mandar duas frentes mexerem no mesmo arquivo ou ticket.
- Não dar como feito o que a frente não confirmou.
- Não gravar em ticket ou e-mail pela janela geral; isso é das frentes, com ok do usuário.

**Nas janelas das frentes:** tarefa recebida da janela geral é tarefa do usuário (mesmas regras: apresentar antes de gravar, nunca enviar). Ao terminar, devolver o resumo à janela geral por `SendMessage`; o que precisar de aprovação, apresentar também na própria janela.

## Respostas eficientes (decidido em 2026-10-27)
Origem: análise de 1.981 mensagens do usuário ([[revisoes/2026-10-27-padroes-prompts|padrões dos prompts]]). Cada regra corta uma causa de ida e volta.
1. **Bloco de prova** no fim de toda resposta, rascunho ou arquivo que vai para terceiros (ticket, e-mail, chat, artefato):
   - **Pedido → resposta:** item a item, cobrindo o pedido inteiro.
   - **Fontes:** cada afirmação → fonte primária lida, com artigo, página ou célula.
   - **Teste:** o que foi conferido mecanicamente (XSD, conta refeita, md5).
   - **Confiança X%:** se abaixo de 100%, dizer o que falta e não apresentar como pronto.

   O usuário não deve precisar perguntar "tem 100% de confiança?".
2. **Fazer sem perguntar:**
   - próximo item de lista já aprovada;
   - leitura, pesquisa e conferência;
   - registro no cérebro (hub, log, pendência);
   - decisão técnica reversível (dizer qual foi em 1 linha).

   **Continua pedindo ok:**
   - enviar, ou gravar em ticket/e-mail;
   - Drive;
   - artefato de terceiro ou de país ativo (regra 9);
   - mudança de escopo;
   - apagar.
3. **Mensagem interna** (gerente, diretor, chat do time): 1 a 3 frases, só o perguntado. Achados fora do pedido vão para o hub e aparecem ao usuário numa linha separada: "Fora do pedido (não incluí): …".
4. **Pergunta ao usuário:** contexto em 1 linha, opções em português simples (sem jargão sem tradução), recomendação e "se não responder, faço A".
5. **Instrução de sessão** ("esquece X", "não precisa Y", "sempre Z"):
   - gravar na hora no `estado.md` da frente (na geral, em `ESTADO.md`), seção "Instruções vigentes";
   - reler antes de cada entrega.
6. **Passo manual do usuário** (enviar, importar, exportar): já dizer "quando você disser 'pronto', eu faço: 1… 2…". Em "enviei" ou "pronto":
   - registrar no hub e no log;
   - fechar o item;
   - abrir o próximo da fila sem perguntar.

   Depois de "importei/copiei para o Drive": rodar `python scripts/conferir_import.py <local> <Drive>` e dar o resultado em 1 linha.
7. **Antes de editar qualquer artefato:** `python scripts/achar_versao.py <país> <ccg|wtc|dd|sir|payslip|spec> [termo]`. Partir da maior versão não DRAFT; md5 diferente na mesma versão → comparar antes.
8. **Janela geral:** pedido de ticket, e-mail, chat, pipeline ou certificação vai direto para a frente certa, com aviso de 1 linha ("mandei para a frente X"), sem perguntar a quem mandar.

## Comandos
Quando o usuário disser:

- **"chegou resposta de X" / mensagem colada de alguém:** saída fixa, sem preâmbulo:
  - o que X pediu;
  - o que é nosso (o resto vai para [[fronteiras]]);
  - o que mudou desde a nossa última mensagem;
  - rascunho da resposta (formato da regra 3 de "Respostas eficientes") + bloco de prova;
  - onde registrar (hub, ticket, estado da frente).
- **"onde estamos?" / "o que falta?":** rodar `python scripts/onde_estamos.py` e responder no painel ✅ pronto | ⏳ espera você | 🔄 espera outros/frente, só com o que mudou desde o último painel.

- **"responde o ticket X" / rascunho de resposta / e-mail** (protocolo validado em 2026-10-13)
  1. Carregar a skill `mercans-compliance-workflow` (e `payroll-compliance-<país>` se existir) **antes** de redigir.
  2. Ler `correcoes.md`, o hub do país e os arquivos locais (Downloads, Drive em `G:\Drives compartilhados\Compliance Team\Country Folders\<País>`) **antes** de buscar na web: a versão mais nova de um documento pode já estar na máquina.
  3. Puxar o ticket pela API e identificar **só o que foi pedido a nós** no último comentário. Se ninguém nos mencionou nem perguntou, não há o que responder.
  4. Confirmar a versão vigente da fonte oficial; se houver duas, vale a de número maior (regra 8).
  5. Cada afirmação: ler pessoalmente na fonte primária (o que um agente reportar, reabrir). Testar mecanicamente quando possível (XML × XSD, contas refeitas). Sem prova → sai da resposta.
  6. Se o pedido repete o padrão de um ticket já resolvido, aplicar a mesma tratativa.
  7. Arquivo: partir da export mais recente da planilha ativa; alterar só o pedido; destacar o que mudou em azul claro `FFDDEBF7`; conferir célula a célula; copiar para o Drive compartilhado como `<nome>_vX.Y.xlsx` (nunca sobrescrever o `.gsheet`; o usuário importa).
  8. Comentário: só o que foi feito e a resposta ao que foi perguntado, na altura da pergunta; não repetir o que está no arquivo; tom neutro (confirmar o certo e só descrever o resto, com fonte); achados fora do pedido vão para o hub, não para o ticket.
  9. **Apresentar ao usuário antes de gravar** rascunho (draftComment) ou arquivo; nunca enviar comentário.

- **"abre o dia" / "roda a frente N"**: seguir `rotinas.md` (frentes 1–3 → painel: urgente hoje / esperando o usuário / esperando outros). Só ler, rascunhar e resumir.

- **"fecha a sessão"** (aprendizado contínuo: LLM wiki + KCS)
  1. Criar `sessoes/AAAA-MM-DD.md` a partir de `modelos/sessao.md`: o que foi feito (com links), decisões, conhecimento novo, erros nossos encontrados, lições de processo, pendências.
  2. **Conhecimento novo** (regra, valor, fonte oficial, estrutura de arquivo) → hub do país, com vigência e fonte (regra 1). **Erros nossos** → `correcoes.md`. **Achados fora do pedido** → Pendências do hub.
  3. **Lições de processo** (como trabalhar) → atualizar este CLAUDE.md (curto) e a memória do Claude; detalhe vai para a nota da sessão.
  4. Reescrever `ESTADO.md` (onde paramos) e acrescentar linha em `log.md`.
  5. Listar ao usuário o que foi registrado e onde.

- **"ingere isto" / "ingere raw/..."**
  1. Ler o material (se veio colado no chat, salvar antes em `raw/<tipo>/AAAA-MM-DD-<assunto>.md`).
  2. Extrair: decisões, regras, valores (com vigência + fonte), erros corrigidos, pendências, quem pediu.
  3. Atualizar as notas afetadas (país, serviço, `correcoes.md`), criando a partir de `modelos/` quando não existirem.
  4. Ligar tudo com `[[links]]` e atualizar `00-INDEX.md`.
  5. Registrar em `log.md` o que entrou e quais notas mudaram.
  6. Listar ao usuário o que foi alterado e o que ficou em dúvida (não inventar para preencher lacunas).

- **"responde X" / qualquer pergunta sobre o serviço**
  1. Ler `correcoes.md`.
  2. Procurar no cérebro (`paises/`, `servicos/`) e nas skills Mercans (abaixo).
  3. Responder citando a nota/fonte. Se o cérebro não tiver a informação, dizer isso claramente.
  4. Se a resposta gerou conhecimento novo, perguntar se deve ser registrado.

- **"fechei o ticket X" / "entreguei Y"** (registro no fluxo de trabalho, método KCS)
  1. Registrar no hub do país (seção Suporte ou Histórico) com data, ID e resumo.
  2. Se o ticket revelou erro em artefato ou resposta anterior → entrada em `correcoes.md`.
  3. Se mudou artefato → atualizar versão no hub do país.
  4. Linha em `log.md`.

- **"revisa o cérebro"** (lint)
  Procurar: contradições entre notas, valores sem vigência ou sem fonte, notas sem links (órfãs), links quebrados, países com etapa desatualizada, `correcoes.md` que já deveriam ter ido para as skills. Entregar um relatório; só corrigir com aprovação.

## Regras
1. **Todo valor estatutário** (alíquota, teto, faixa, prazo) leva **vigência** (`a partir de AAAA-MM-DD`) e **fonte** (lei/site oficial/documento). Valor sem fonte é marcado `⚠️ sem fonte`.
2. **Nunca sobrescrever valor antigo:** quando muda, a linha antiga recebe data de fim e a nova é acrescentada.
3. **Sem dados pessoais** de funcionários de clientes (nomes, IDs, salários individuais). Usar só o necessário: país, cliente (se preciso), ID do ticket.
4. **Não duplicar as skills.** As skills `payroll-compliance-<país>`, `mercans-pipeline-methodology` e `mercans-compliance-workflow` já têm o conhecimento estatutário e o método. O cérebro guarda o que falta nelas: decisões, histórico de entregas, tickets, correções, estado de cada país. Quando precisar do conteúdo da skill, **linkar/citar** em vez de copiar.
   - **Exceção: "Ficha do país (da skill)"** no hub (decidido em 2026-10-02): resumo curto do que mais importa para nós (escopo e ano fiscal, armadilhas confirmadas, o que mais dá errado, lacunas abertas, relatórios principais), extraído do `SKILL.md` e do `07-qa-report.md`. Leva a data de leitura da skill. Tabelas completas (alíquotas, faixas, WTC, DD) continuam só na skill; para responder com valor exato, ler a skill. Se ficha e skill divergirem, vale a skill e a ficha é atualizada.
5. **Na dúvida, perguntar.** Não completar lacunas com suposição.
6. Notas em Markdown, nomes de arquivo sem acento e com hífen (`paises/Belgica.md`), links no formato `[[Belgica]]`.
7. `raw/` é imutável; `log.md` só cresce.
8. **Versão vigente de artefato = a de maior número de versão** (a planilha/arquivo com a atualização mais recente). Ex.: WTC Espanha V4.4. Quando fontes citarem versões diferentes, registrar a maior como vigente e as outras como histórico. (decidido em 2026-10-05)
9. **País já ativo → ticket de alteração para o Development.** Antes de qualquer alteração em artefato de um país, perguntar: **o país já está ativo** (em produção)? Se estiver, a alteração exige abrir ticket de alteração para o time de Development (quem leva a mudança para produção, ver [[fronteiras]]); registrar o ticket no hub do país. (decidido em 2026-10-27)

## Fontes de conhecimento
| Fonte | Como entra |
|---|---|
| Projetos do Claude da Mercans (pipeline, compliance research, Design & Development, tickets) | Conversas copiadas na íntegra pelo Claude in Chrome (`prompts/coleta-chrome.md` §F3) para `raw/chats/conversas/`. O `prompts/extracao-projeto.md` só quando a cópia não for possível. |
| YouTrack (`https://youtrack.hrblizz.dev`) | API REST: `scripts/youtrack_fetch.ps1` (tickets → `raw/tickets/api/AAAA-MM-DD/`, fora do git), `scripts/youtrack_anexos.ps1` (anexos), rascunho via `draftComment`. Token no `.env` da raiz (gravado com `scripts/configurar_token.ps1`): **nunca ler, exibir ou copiar o valor.** |
| monday | Conector do claude.ai (só leitura). Boards e o que coletar: `prompts/extracao-monday.md` (PLANO §6, Fase 3 F1). |
| Skills Mercans/país | Consultar via Skill quando necessário; não copiar. |
| Google Drive | Drive compartilhado montado em `G:\` (só leitura/cópia de arquivos; `.gsheet` não é editável pelo disco). Planilhas: o usuário exporta `.xlsx` para Downloads. |
| Google Meet/transcrições | Sem conector (bloqueio da Mercans). Coleta pelo Claude in Chrome, só leitura: `prompts/coleta-chrome.md`. |
| Gmail | **Claude in Chrome** (decidido em 2026-10-19; o conector do claude.ai cai com frequência e não é mais usado): leitura e rascunho na aba do Gmail, procedimento em `frentes/gmail/CLAUDE.md`. Outras janelas pedem rascunho à janela Gmail. Nunca enviar. Confirmar que é a caixa da Mercans (wgomes@mercans.com). |
| Chat | Sem acesso: o usuário cola/exporta. |
