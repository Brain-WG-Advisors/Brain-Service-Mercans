# Onde paramos

> Atualizado em 2026-10-28 (sessão [[sessoes/2026-10-28]]; demais blocos sem mudança desde 2026-10-27). Reescrever a cada "fecha a sessão". Ler ao abrir a sessão.

## Hoje (2026-10-28) — ver [[sessoes/2026-10-28]]
- **Pronto:**
  - resposta à Heidy (Colômbia, PMI Review) enviada pelo usuário; nota [[revisoes/2026-10-28-CO-mesadas-adicionais-saude-fsp]];
  - skill brain-service de 28/10 no claude.ai (conferida);
  - tudo enviado ao GitHub (`main` = `origin/main`).
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
  - **Junto, do mesmo pedido:** compliance calendar no ambiente de produção, uns 60 países, 1 a 2 por semana, prioridade aos que têm clientes ativos (BAU master list).
  - **Junto, do mesmo pedido:** plano do projeto de automação (status enviado em 28/10, cerca de 60%).
  - **Dono:** Vinícius executa (call de 27/10, secundário depois de Lituânia e Espanha). Sem início registrado.
  - **Decisão do usuário (28/10):** o projeto fica na frente **Certificação**. Transcrições e nota mandadas à janela em 28/10. Plano, decisões e execução ficam com ela e com o usuário, na janela dela. A janela geral não acompanha; o estado fica em `frentes/certificacao/estado.md`.
- **Lituânia:** validação das correções do SIR e das specs com o BAU (Kevin) mandada à janela Gmail em 28/10 (rascunho, não enviado).
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
- Enviar: feedback Montage P09 à Manju (`rascunhos/2026-10-20-feedback-manju-montage-P09.md`), Muhammad e Shruti (`rascunhos/2026-10-20-*`).
- Ruchi (Canadá, K2): bônus pago sozinho e a isenção de $3.500 (T4127), sem resposta.

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
- **Migração do brain (concluída 2026-10-27):** esta máquina e o GitHub iguais (merge com a outra máquina, pacote do pen drive restaurado, dados de clientes fora do git; branch local `backup/pre-limpeza-2026-10-27` tem dados de clientes: nunca enviar, apagar quando o usuário quiser). Outra máquina: `git pull` antes de mexer.
- **F6 Pipeline (2026-10-27):** 112 cartões (BE 40, CO 32, FR 40) ingeridos nos hubs, 9 entradas em [[correcoes]], `servicos/research-pipeline.md` e [[fronteiras]], tudo "validação humana pendente". **Usuário:** validar 2 lotes (67 risco alto + 5 sorteados) em `extracoes/2026-10-27-pipeline-*.md`. Destaques: hub BE tinha o 697,61/697,42 invertido (corrigido, C25); CO com dois decretos do SMMLV em conflito (C21) e CCG v1.4 contraditório sobre não residente (C22); FR pacote vigente = reemissão v1.0 de 06/10 promovida em 09/10. Pendentes: origem do `CO-compliance/colombia-artifacts-20261026-1016.zip`; `~/mercans-pipeline` sem remote (só ler).

## Ao abrir a próxima sessão
1. Ler este arquivo e o fim de [[log]].
2. Frentes 1–5: abrir com `scripts/abrir_frentes.ps1` (cada janela abre na sua pasta `frentes/<frente>/` e lê o seu `estado.md`).
