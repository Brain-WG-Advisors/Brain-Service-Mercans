# Integração do cérebro ao Claude Desktop e ao claude.ai (método, 2026-10-27)

> Sessão aberta em 2026-10-27, logo depois de [[sessoes/2026-10-27]]. Objetivo: levar o ganho medido no Claude Code (exatidão 28/28, contra 20/28 no claude.ai; [[testes/exatidao]]) para onde o time trabalha. Ver também [[PLANO]] (Fase 2, pausada), [[uso-de-ia]] e [[revisoes/2026-10-27-pesquisa-ia-payroll|pesquisa brain de IA]].

## O ponto de partida
- No **Claude Code** o cérebro funciona por inteiro: lê as notas, roda os scripts (`contexto_pais`, `achar_versao`, `atualizar_tickets`), alcança o Drive (G:) e a API do YouTrack.
- O **claude.ai web** não alcança a máquina. Só vê o que for **enviado** para lá (Projeto, skill) ou o que estiver num conector **remoto**. Por isso tirou 20/28: faltavam WTC, design e correções internas.
- O **Claude Desktop** (instalado aqui pela Microsoft Store) tem duas portas: a aba de código (Claude Code dentro do app) e o chat, que aceita **servidores MCP locais**.

## Caminhos (do mais completo ao mais simples)

| # | Caminho | Onde vale | O que o Claude passa a ver | Esforço | Fica atualizado? | Risco |
|---|---|---|---|---|---|---|
| A | **Aba Code do Claude Desktop** aberta na pasta `brain-service` | Desktop, nesta máquina | Tudo (é o Claude Code: CLAUDE.md, scripts, Drive, API) | nenhum | sim (é a própria pasta) | nenhum novo |
| B | **Chat do Desktop + MCP local "brain"**: um servidor pequeno (Python) que expõe `contexto_pais`, `achar_versao`, `onde_estamos`, busca nas notas e o Graphify como ferramentas, **só leitura** | Desktop, nesta máquina | Hubs, correções, versões, tickets e grafo, sob pedido | ~1 sessão | sim | baixo (local, só leitura; `raw/` e `.env` fora) |
| C | **Skill "brain-service" (.zip)** em Configurações → Capacidades: SKILL.md com o protocolo (bloco de prova, regras de resposta, fronteiras) + `references/` gerado por script (correções, ficha e versões vigentes de cada país, pendências abertas) | **web, Desktop e celular**; o time todo, se o admin provisionar | Retrato do cérebro na data da geração | ~1 sessão + regerar semanal | não sozinho: script `gerar_pacote.py` regera; upload manual | baixo (dados internos da Mercans dentro da conta da Mercans; sem dado pessoal de cliente, regra 3) |
| D | **Projeto "Brain Service"** (já criado) com o mesmo pacote gerado em arquivos | web e Desktop, dentro do projeto | Retrato, com busca automática (RAG) | baixo (o projeto existe) | upload manual semanal (integração GitHub só no plano Enterprise e o repositório é pessoal: não usar sem ok da Mercans) | baixo |
| E | Conector remoto (MCP na internet) | web | Ao vivo | alto | sim | **alto: expõe o cofre na internet. Descartado** ([[uso-de-ia]], "nada sai da máquina") |

## Recomendação
1. **Hoje, custo zero (A):** usar a aba Code do Claude Desktop aberta em `brain-service` como "Claude com cérebro". Tem o mesmo efeito de 28/28.
2. **Para o web e para o time (C + D com um pacote só):**
   - Criar `scripts/gerar_pacote.py`. Ele gera, do cérebro, a skill `brain-service.zip` e os arquivos do Projeto, com data no nome e sem `raw/`, rascunhos, credenciais nem dado pessoal.
   - Subir a skill na conta.
   - Medir com a rodada 3 do teste de exatidão no claude.ai: meta de 20/28 para pelo menos 26/28.
   - Regerar e subir toda segunda, junto com o `medir_eficiencia`.
3. **Depois, se o chat do Desktop for usado no dia a dia (B):** criar o MCP local "brain", só leitura.

## Decisão e implantação (2026-10-27)
- **Decisão do usuário:** caminhos 2 (skill + Projeto) e 3 (MCP local), de **uso pessoal**. Pode ficar na conta da Mercans, mas só para ele: skill pessoal, sem provisionar para o time.
- **2, pronto:**
  - `scripts/gerar_pacote.py` gera `publicar/skill/brain-service.zip`, a skill pessoal. Ela contém SKILL.md com a ordem de leitura e as regras de resposta, mais `references/`: correções, fronteiras, serviços, 52 hubs e `painel-paises.md`.
  - Gera também `publicar/AAAA-MM-DD/` (os mesmos 60 arquivos para o Projeto).
  - Checagem de credenciais embutida.
  - Pacote de 2026-10-27: cerca de 111 mil palavras, 324 KB.
- **3, pronto:**
  - `scripts/mcp_brain.py` (servidor MCP "brain", só leitura). Ferramentas: `contexto_pais`, `achar_versao`, `onde_estamos`, `buscar`, `ler_nota` e `grafo`. Estão bloqueados `.env`, `.git`, `.obsidian`, `publicar/` e o que estiver fora da pasta.
  - Registrado em `%LOCALAPPDATA%\Claude-Data\claude_pzs8sxrjxfjjc\claude_desktop_config.json` (`mcpServers.brain`, via `uv run --with "mcp<2"`; o mcp 2.x renomeou o FastMCP).
  - Teste de handshake: as 6 ferramentas responderam.
- **Falta (usuário):**
  - fechar o Claude Desktop por completo e reabrir;
  - subir a skill;
  - depois, rodada 3 do teste de exatidão no claude.ai, com a skill ligada.

## Perguntas ao usuário (respondidas em 2026-10-27)
- O time vai usar o cérebro, ou só você? Se for o time, a skill precisa ser provisionada pelo admin da Mercans; as skills `mercans-*` já são provisionadas assim.
- Pode subir na conta da Mercans, como skill/Projeto, o conteúdo interno do cérebro (hubs, correções, versões)? Os nomes de clientes que já estão nos hubs entram também. Sem isso, o pacote leva só as regras e as fichas, sem os tickets.

## Fontes
- Skills em .zip no claude.ai e no Desktop (Configurações → Capacidades; requer execução de código): https://support.claude.com/en/articles/12512180-use-skills-in-claude
- Integração GitHub em Projetos (plano Enterprise): https://support.claude.com/en/articles/10167454-use-the-github-integration
- MCP local no Claude Desktop (`claude_desktop_config.json`, `mcpServers`; extensões em Configurações → Extensões): https://modelcontextprotocol.info/docs/development/connect-local-servers/
- Conector remoto exige servidor na internet: https://support.claude.com/en/articles/11175166-about-custom-connectors-remote-mcp-servers (citado na pesquisa de 27/10)
