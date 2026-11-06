# Onde paramos

> Atualizado em 2026-11-03 (sessão [[sessoes/2026-11-03]]; blocos de 02/11 e anteriores sem mudança). Reescrever a cada "fecha a sessão". Ler ao abrir a sessão.

## Reuniões de 04/11 (bi-weekly com o Marko + call Dev × Research com Mohit/Ram/Lily)
Fontes: `raw/reunioes/2026-11-04-research-team-biweekly.txt` e `raw/reunioes/2026-11-04-collaboration-dev-design.txt`. Itens de país nos hubs [[Colombia]], [[Espanha]], [[Ucrania]], [[Franca]].
- **Change management do Dev:** regra 10 do CLAUDE.md (submeteu = congela; mudança grande = retirar e reenviar, prazo recomeça). Marko pediu para alinhar com o Mohit; call semanal Manju/Mohit criada (Dinamarca na próxima).
- ⏳ Usuário: **agendar call com Chris, Martin e Marko** (AI pod) — encaixar no roadmap o que falta da automação de tickets (~60–70% feita) e os outros loops (manter skills atualizadas; ~100 países × 2–3 artefatos).
- ⏳ Usuário: Colômbia, mandar ao Mohit/Ram a lista consolidada das mudanças v1.4 → v1.7 (prometido na call).
- ⏳ Usuário: França, conectar com a Vanessa Suarez (teste da regulation, CBAs/CLAs).
- ⏳ Usuário: Ucrânia, comparar a lógica de indexação da Natalia (pasta Ukraine › regulation guide) com o CCG.
- 🔄 **Teste do design no produto:** o Marko aprovou testar o design feito pelo Claude, começando pelos EUA. O Mohit avisa que acceptance e produção são ambiente vivo, aprovados pelo Andre, e que staging é só dele e dos devs da Estônia. Falta conversar com o Andre (e Marko/Andy). Afeta as frentes EUA e Chade.
- Para saber (sem ação): Accenture traz Bulgária, Hungria, Turquia, Grécia (tetos EFKA, abandonada 3×) e Marrocos para o roadmap 27/28, ainda sem kickoff. Suíça (Enaakshi) em revisão, alvo esta ou a próxima semana; apoio em italiano: Simone Chiccarelli. Vietnã/Taiwan (Manju): o Marko exige XML gerado pelo sistema, nunca digitação manual.

## Parada para migração de conta (03/11) — LER PRIMEIRO
- **Todas as tarefas paradas** a pedido do usuário para migrar o Claude Code para a **conta corporativa da Mercans**. Estado salvo no git (commit + push de 03/11).
- **GitHub novo:** `Brain-WG-Advisors/Brain-Service-Mercans` (privado; dona da organização: conta ViniCerqueira, depois passa ao diretor da WG Advisors; `wgomes-adv` é membro com **leitura** — subir para Admin em Settings → Collaborators). Remote local já aponta para lá. Pasta local continua `Documents\brain-service`.
- **Ao abrir na conta nova, conferir:** (1) memória em `~/.claude/projects/c--Users-instituto-Documents-brain-service/memory/` (é local, deve continuar); (2) skills Mercans (`mercans-compliance-workflow`, `mercans-pipeline-methodology`, `payroll-compliance-*`) vinham da organização da conta antiga — ver se aparecem na conta nova, senão reinstalar/publicar; (3) conectores do claude.ai (monday etc.) e artifacts privados ficam na conta antiga; (4) `gh auth status` (git continua pela conta ViniCerqueira); (5) reabrir as frentes **sem** `-Retomar` (conversa nova; regra de 03/11).
- **Feito hoje (03/11):** memória única + grafo para todas as janelas (CLAUDE.md); radar de esquecidos (`scripts/radar_esquecidos.py`) + faxina (9 fechadas, 19 decisões do usuário listadas na sessão); lei × mercado ([[servicos/lei-x-mercado]], caso STG seguro 41,67); grafo limpo (26.360 → 2.022 nós) e `buscar.py` com fontes `pipeline`/`certificacao`.
- **Pendente do usuário:** responder as 19 decisões do radar ([[sessoes/2026-11-03]]); Samuel dos Passos no GitHub (usuário dele); STG: limite com dois empregadores (consulta DGT) e ajuste de fim de ano no motor (Lily); itens de 02/11 abaixo.

## Pipeline v2.12 para o time (02/11)
- ✅ Enviados pelo usuário: e-mail a todos com a pasta do Drive `02. AI Pipelines/pipeline v2.12`; Chat à Manju com os passos da NAV via `si_runbook.sh` (zip v2.12.1) e a pergunta se ainda falta algo.
- ✅ Corrigido: zip v2.12.1 com os arquivos da etapa 6 (verificador `scripts/conferir_pacote.py`: 0 faltando; avaliação prévia ok). `~/mercans-pipeline` também completo.
- 🔄 Esperando a Manju responder (rodada da NAV / `nav.log`).
- ⏳ Usuário: enviar o rascunho de e-mail a todos sobre o v2.12.1 (no fio "Mercans compliance skills updated to v2.12") **depois** da resposta da Manju; ok para tirar o `si-runbook-generator.zip` repetido da pasta; pasta "Pipeline v3.0" (11/09/2026) no Drive — quem criou.
- ⏳ Usuário: SIR da França e da Colômbia fora do modelo oficial ([[revisoes/2026-11-02-sir-fr-co-x-modelo-oficial]]) — refazer agora ou quando usar; a França está ativa? (regra 9).

## 2026-10-29 — 5 demandas em paralelo (usuário) — acompanhar em `paineis/frentes.html`
- **Janelas no Maestri:** Chade, EUA, Validação CO (novas), Certificação, Process Lithuania (= Pipeline). O usuário trata direto com cada uma; a geral atualiza o painel a cada retorno. `frentes/lituania` apagada em 29/10 (sem uso).
- **Ferramentas novas:** `scripts/buscar.py` (busca local por trecho) e `scripts/painel_frentes.py` (painel).
| # | Demanda | Frente | Escopo decidido pelo usuário |
|---|---|---|---|
| 1 | Teste do design do Chade no HRBlizz (teste) | **Chade** (nova) | Design do Dev × nosso design; login do usuário, Chrome só leitura |
| 2 | Research EUA | **EUA** (nova) | Uma research por estado, 50 + DC (origem: weekly 29/09, biweekly Marko 21/10) |
| 3 | Internal Certification | Certificação | Seguir as análises e, no fim, propor melhorias |
| 4 | Lituânia | Pipeline (no Maestri: "Process Lithuania"; a pasta `frentes/lituania` criada por engano não é usada) | Validação de 28/10 reprovou SAM v1.0, GPM313/312 v1.1 e SIR v1.0 → corrigir localmente (ok do usuário, 29/10), revalidar, depois Drive/tickets (novo ok) e só então o pedido ao Kevin (HRBS-15253, iniciativa nossa) |
| 5 | Validar a research da Colômbia | **Validação CO** (nova) | Mesmo método da França (oráculo + suíte + redlines) |

**Escopo esclarecido pelo usuário (29/10, mandado a cada frente):**
1. Chade: achar no claude.ai (Chrome) a última conversa sobre o design + contexto do cérebro → pacote de contexto para o chat que vai tratar o projeto; HRBlizz de teste depois.
2. EUA: iniciar a Research Pipeline com o que está no MD da frente Pipeline (sem usar a janela Pipeline), cobrindo todos os estados (variação de lei estado a estado).
3. Certificação: destino já definido pelo Marko; entregar o caminho mais rápido e eficiente do 0 ao 100% + o relatório + melhorias.
4. Lituânia: mesmo processo de validação com o BAU feito na Colômbia, para specs e SIR, meta de 0 erros (depois das correções locais).
5. Colômbia: validar cada artefato com simulações, como na França, meta de 100% de acertos.

## Hoje (2026-10-28) — ver [[sessoes/2026-10-28]]
- **Pronto:**
  - resposta à Heidy (Colômbia, PMI Review) enviada pelo usuário; nota [[revisoes/2026-10-28-CO-mesadas-adicionais-saude-fsp]];
  - skill brain-service de 28/10 no claude.ai (conferida);
  - tudo enviado ao GitHub (`main` = `origin/main`).
  - busca local por trecho `scripts/buscar.py` (reuniões, leis, tickets, chats, extrações; sem rede), ainda sem commit.
- **Esperando o usuário:**
  - ok para apagar o CSV "Columbia Regulation Plan  - Plan .csv" (Downloads) e o Google Doc 1akwVTqv (conversão da Lituânia com erro);
  - reiniciar o Claude Desktop (MCP "brain");
  - validar os 2 lotes F6 (bloco abaixo);
  - mandar à frente Pipeline: instalar a skill `payroll-compliance-colombia` recompilada (pedido do Ram; pronta em `Research Pipeline/Colombia/2026-10-28-skill/`), corrigir no WTC da Colômbia a licença maternidade/paternidade ainda isenta e o EG-8003 do Egito ("public sector only");
  - decidir se a regra das mesadas entra no CCG v1.4 (Colômbia ativa → ticket ao Development).
- **Instrução vigente (28/10):** toda transcrição de reunião vai para o cérebro. A cópia fica em `raw/reunioes/AAAA-MM-DD-<assunto>.<ext>` (`.docx` do Gemini com um `.txt` extraído ao lado) e o conteúdo é ingerido: cartões em `extracoes/`, depois hubs e pendências. A procura é em Downloads. Em 28/10 entraram 27 reuniões novas (25/06 a 22/10).
  - **Pendente:** extrair os cartões dessas 27 + `2026-10-27-research-team-weekly` e `2026-10-27-spain-transition-to-HRB` (nunca ingeridas).
- **Projeto do Marko, mapa das entregas estatutárias**. Explicação completa: [[revisoes/2026-10-28-pedido-marko-fluxo-entregas]] (pedido do Marko, repassado pela Manju; reuniões [[raw/reunioes/2026-10-27-research-team-weekly.txt|weekly 27/10]] 04:31–13:59 e [[raw/reunioes/2026-10-27-call-wallisson-lituania-espanha.txt|call com o Vinícius 27/10]] 59:38–01:06:14):
  - escopo: toda entrega ao governo de cada país em produção, e não só as specs. O passo a passo vem com o que o sistema faz, o que o cliente faz e o que a autoridade faz;
  - meta: tudo sai do sistema e é transmitido de forma automática (registro da Mercans como agente, XML, API), sem passo manual nem terceiro;
  - processo atual: pedido ao BAU de cada país (board "BAU master clients") só para entender. O manual não é base; o que vale é a nossa pesquisa do jeito certo, comparada com o que acontece hoje;
  - começar pela Europa; o modelo é o Vietnã da Manju;
  - entregar ao Marko um plano com status e datas, e no fim um relatório com gráfico por país.
  - **Junto, do mesmo pedido:** compliance calendar no ambiente de produção, uns 60 países, 1 a 2 por semana, prioridade aos que têm clientes ativos (BAU master list). **Desde 2026-11-05 (decisão do usuário): passou para a frente Alertas** ([[frentes/alertas/estado|estado da frente Alertas]]).
  - **Junto, do mesmo pedido:** plano do projeto de automação (status enviado em 28/10, cerca de 60%).
  - **Dono:** Vinícius executa (call de 27/10, secundário depois de Lituânia e Espanha). Sem início registrado.
  - **Decisão do usuário (28/10):** o projeto fica na frente **Certificação**. Transcrições e nota mandadas à janela em 28/10. Plano, decisões e execução ficam com ela e com o usuário, na janela dela. A janela geral não acompanha; o estado fica em `frentes/certificacao/estado.md`.
- **Lituânia:** validação das alterações de 27/10 com o BAU (Kevin) é decisão do usuário (nenhum pedido de terceiros nas transcrições); e-mail parado na janela Gmail e assunto passado à **Pipeline** (28/10). Usuário: descartar o Compose vazio (Para: Kevin) na janela Gmail.
- **Cinthya / "New test entity PMI":** resposta de escopo enviada pelo usuário em 28/10 ([[Colombia]] Decisões; [[fronteiras]]).
- **Obsidian:** 1 nota solta (validação da Pipeline em andamento, `Research Pipeline/Lithuania/2026-10-28-validacao/`).
- **Esperando outros:** Heidy (BAU) com o WT de cada faixa de saúde, tipo de pensão, tipo 5/6 e a confirmação de junho pela PMI ([[Colombia]] Pendências).

## Rede de conhecimento (Fase R) e teste de exatidão (2026-10-27)
- **Prioridade:** a rede no Obsidian vem antes (Fase R do [[PLANO]]); a Fase 2 (fumaça e rodada 2 no projeto "Brain Service" do claude.ai) está pausada. O objetivo continua a eficiência da entrega no dia a dia.
- **Pronto:**
  - cofre `brain-service` no Obsidian, com as cópias excluídas em `.obsidian/app.json`;
  - 0 notas soltas;
  - hubs novos [[Taiwan]], [[Argelia]] e [[Cazaquistao]];
  - grafo do Graphify em `graphify-out/` (abrir `graph.html`; consultar com `graphify query`).
- **Manter o grafo:** `graphify update .` para a estrutura; para notas alteradas, releitura com agentes (skill graphify, `--update`).
- **Tickets dos hubs:** conferidos na API em 27/10. Antes de agir sobre ticket citado em hub, conferir o estado na API.
- **Esperando o usuário:**
  - ~~religar os 5 conectores do claude.ai~~ ✅ religados em 2026-10-27 pela janela geral (Chrome);
  - ~~push dos commits `a924890`, `afc11c8`, `5110bf5`~~ ✅ enviados (conferido em 28/10).
- **Esperando frente Suporte:** conferir o teto SSC da Namíbia (GN 236/2026 × N$99 dito no HRBS-12111), em [[Namibia]] Pendências.

## Eficiência (2026-10-27, tarde) — ver [[sessoes/2026-10-27]]
- **Pronto:**
  - properties e painel gerado nos 52 hubs (`paineis/paises.base`);
  - scripts `contexto_pais`, `atualizar_tickets`, `achar_versao`, `conferir_import`, `onde_estamos` e `medir_eficiencia`;
  - regras "Respostas eficientes" no [[CLAUDE]];
  - exatidão no Claude Code: 28/28.
- **Integração Desktop/web (sessão aberta 27/10):** método em [[revisoes/2026-10-27-integracao-desktop-web]]; esperando o usuário: quem usa e se o conteúdo interno pode subir na conta.
- **Segunda (S45):** `medir_eficiencia.py` → [[testes/eficiencia]].
- **Esperando o usuário:**
  - reabrir as frentes (`abrir_frentes.ps1 -Retomar`);
  - conferir França CCG/WTC v1.1 e Bélgica (hub > Drive).

## Colômbia PMI — pesquisa concluída (2026-10-26)
- Encerrada em 26/10: artefatos finais no Drive/Monday (7 specs v1.0, CCG v1.4, WTC v1.6, DD v1.3, SIR v1.1); delta ao design e e-mail de encerramento enviados pelo usuário; registros no chat "Research Pipeline II". Resumo: [[sessoes/2026-10-26]]; planilha [[Research Pipeline/Colombia/co-report-crosscheck/04-output/CONFIRMACAO-PROCESSOS-CO-2026-10-26.xlsx|CONFIRMACAO-PROCESSOS-CO-2026-10-26.xlsx]].
- YouTrack CT-4593/SR-470: o usuário decidiu não editar (27/10, janela Suporte); levantamento em `rascunhos/2026-10-26-youtrack-links-CO.md`.
- Depois: timeline do Andy quando o Mohit confirmar datas; skill `payroll-compliance-colombia` (#17). Com terceiros, sem bloquear: #54/#55 (cliente/BAU; #55 respondido à Heidy em 28/10, aguarda retorno), #41/#51 (Manju/DIAN); dúvidas do design nas colunas T/U = suporte.

## Esperando o usuário (2026-10-20)
- #13037 (TI, Manette): ok para responder "VPN instalada; pasta = link de 13/10 ao Merlin (https://drive.google.com/drive/folders/1BArVL5SGDH1NbkLa0DJ-SR1sqnRz6Uo6); expiração 20/11/2026" → rascunho pela frente Chat. Apuração em `raw/chats/2026-10-20-manette-ti-vpn-pasta.md`.
- Enviar: feedback Montage P09 à Manju (`rascunhos/2026-10-20-feedback-manju-montage-P09.md`), Muhammad e Shruti (`rascunhos/2026-10-20-*`). _(✅ fechada em 2026-11-03 pelo radar: O feedback do Montage P09 ficou superado: as versões P09 a P13 foram refeitas e entregues e Manju, Muhammad e Shruti já foram tratados depois; prova: log.md:241 (pasta Wallisson - P09-P13), log.md:315 (Manju respondida), log.md:375 (Muhammad), log.md:507 (tickets da Shruti devolvidos))_
- Ruchi (Canadá, K2): bônus pago sozinho e a isenção de $3.500 (T4127), sem resposta. _(✅ fechada em 2026-11-03 pelo radar: A resposta à Ruchi sobre bônus e isenção no CPP do Canadá foi postada pelo usuário em 21/10; prova: log.md:226 -)_

## Frentes (desde 2026-10-15, cada uma na sua janela)
- Suporte (tickets): `frentes/suporte/estado.md`
- Gmail: `frentes/gmail/estado.md`
- Chat: `frentes/chat/estado.md`
- Pipeline: `frentes/pipeline/estado.md`
- Certificação (Internal Certification): `frentes/certificacao/estado.md`
- HRBS-14255 (Ucrânia, call de migração de 12/10, feriado): usuário confirmar se há algo pendente (o ticket saiu da fila).

## Em descanso (retomar quando o usuário escrever "descanso")
- **Mammoet NL (Nederland + Montage, P09–P13): solução para o caso inteiro** — gate pré-Marko + 4 combinados + crítica de especialista + motor de reconciliação + plano em fases. Pausado de novo em 2026-10-20. Só análise, sem execução até o usuário aprovar. Próximo passo: o usuário aprova a proposta → pauta da fase 0 (Manju/Yojana) e desenho técnico do motor. Tudo em `rascunhos/2026-10-20-DESCANSO-gate-pre-marko.md`.

## Em aberto (decisões do usuário)
- Padrões F48–F66 para o pipeline (`revisoes/2026-10-09-catalogo-erros-tickets-v2.md`).
- Levar às skills: erros da skill do Congo e do CCG/Alerta 2026 da Lituânia ([[correcoes]]).
- Achados fora do pedido nas specs da Ucrânia ([[Ucrania]] → Pendências).
- **Migração do brain (concluída 2026-10-27):** esta máquina e o GitHub iguais (merge com a outra máquina, pacote do pen drive restaurado, dados de clientes fora do git; branch local `backup/pre-limpeza-2026-10-27` tem dados de clientes: nunca enviar, apagar quando o usuário quiser). Outra máquina: `git pull` antes de mexer. _(✅ fechada em 2026-11-03 pelo radar: A migração do brain foi concluída em 27/10; resta apenas o branch local de backup, que fica até o usuário mandar apagar; prova: ESTADO.md:110)_
- **F6 Pipeline (2026-10-27):** 112 cartões (BE 40, CO 32, FR 40) ingeridos nos hubs, 9 entradas em [[correcoes]], `servicos/research-pipeline.md` e [[fronteiras]], tudo "validação humana pendente". **Usuário:** validar 2 lotes (67 risco alto + 5 sorteados) em `extracoes/2026-10-27-pipeline-*.md`. Destaques: hub BE tinha o 697,61/697,42 invertido (corrigido, C25); CO com dois decretos do SMMLV em conflito (C21) e CCG v1.4 contraditório sobre não residente (C22); FR pacote vigente = reemissão v1.0 de 06/10 promovida em 09/10. Pendentes: origem do `CO-compliance/colombia-artifacts-20261026-1016.zip`; `~/mercans-pipeline` sem remote (só ler).

## Ao abrir a próxima sessão
1. Ler este arquivo e o fim de [[log]].
2. Frentes 1–5: abrir com `scripts/abrir_frentes.ps1` (cada janela abre na sua pasta `frentes/<frente>/` e lê o seu `estado.md`).
