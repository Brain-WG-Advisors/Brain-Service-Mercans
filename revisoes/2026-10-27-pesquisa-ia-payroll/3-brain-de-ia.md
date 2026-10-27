# Pesquisa 3: formas de montar um "brain de IA" para o time de compliance de payroll

> Anexo de [[revisoes/2026-10-27-pesquisa-ia-payroll|Pesquisa: IA e redes neurais em payroll]] (relatório único). Números-chave reabertos na fonte em 2026-10-27 pela janela geral.

Data: 2026-10-27. Só leitura na web; nada foi instalado e nada no vault foi alterado.
Contexto lido: `CLAUDE.md`, `00-INDEX.md` do brain-service (cerca de 1.400 notas .md fora de `raw/`) e `graphify-out/` (graph.json, GRAPH_REPORT.md, mapa-3d.html, mapa-processo.html). Também li a referência local da skill graphify (`~/.claude/skills/graphify/references/exports.md`), que documenta o modo `--mcp`.

> **Premissa de privacidade usada em toda a comparação.** O time já manda conteúdo do cofre para a Anthropic (Claude Code e claude.ai). Então a pergunta prática não é "sai ou não sai da máquina", e sim "**entra um novo terceiro** (fornecedor de embeddings, SaaS de busca, nuvem de banco de grafo)?". Uma opção só fica 100% local com modelo local (Ollama/LM Studio). Antes de qualquer opção nova, conferir contra [[uso-de-ia]] (regras da Mercans para uso de IA).

---

## 1. Abordagens: como funcionam, custo, privacidade, manutenção, citação

### 1.1 Second brain no Obsidian com plugin de IA

**Smart Connections**
- **Como funciona:** gera embeddings **locais**, com modelo embutido e sem chave de API. Mostra as notas semanticamente parecidas com a que está aberta (Connections view) e faz busca semântica (Lookup). O chat com as notas virou outro plugin (Smart Chat) e usa provedores externos (OpenAI, Anthropic etc.).
- **Custo:** o núcleo é gratuito. O Pro acrescenta conexões inline, coluna de similaridade nos Bases e reranking.
- **Privacidade:** embeddings ficam no aparelho, na pasta `.smart-env`. A pasta merece cuidado, porque o embedding codifica o conteúdo semântico. O chat manda trechos ao provedor que você configurar.
- **Manutenção:** baixa; o índice se atualiza sozinho quando o cofre muda.
- **Citação:** aponta notas relacionadas, não responde perguntas. É bom para **manter a rede ligada**: sugere links que faltam.
- **Fontes:** https://community.obsidian.md/plugins/smart-connections ; https://forum.obsidian.md/t/data-privacy-with-smart-connections/95208

**Copilot for Obsidian (logancyang)**
- **Como funciona:** o modo "Vault QA" monta um índice vetorial local do cofre, recupera trechos e responde **citando as notas**. Aceita sua própria chave (BYOK) ou modelo local via Ollama/LM Studio, o que permite rodar 100% offline.
- **Custo:** a versão gratuita cobre chat, Projects, busca local e skills/comandos. O plano Plus (pago) traz multiagente e modelos hospedados.
- **Privacidade:** no uso gratuito, o prompt vai só ao provedor que você configurar; a Brevilabs não recebe nada.
- **Manutenção:** baixa a média (reindexar, escolher modelo de embedding).
- **Citação:** sim, cita as notas de origem.
- **Fontes:** https://github.com/logancyang/obsidian-copilot ; https://myhub.ai/items/using-copilot-for-obsidian-with-a-local-llm-and-vector-store-by-pkm-explorer-medium

**Khoj**
- **Como funciona:** servidor de "AI second brain" auto-hospedado (busca semântica, chat e agentes), com plugin para Obsidian.
- **Custo:** gratuito se auto-hospedado, mas exige rodar um servidor (Docker/pip). A versão em nuvem está sendo descontinuada.
- **Privacidade:** pode ser 100% local.
- **Manutenção:** média a alta, porque é mais um serviço para manter de pé no Windows.
- **Fontes:** https://docs.khoj.dev/ ; https://community.obsidian.md/plugins/khoj ; https://blog.khoj.dev/posts/obsidian-ux-revamp/

### 1.2 RAG vetorial "clássico"
- **Como funciona:** quebra os documentos em pedaços (chunks), gera embeddings, recupera os k trechos mais próximos e passa ao LLM. A variante **Contextual Retrieval** da Anthropic acrescenta a cada pedaço um contexto do documento e combina com BM25. Pelo estudo da Anthropic, as falhas de recuperação caem 49%, e 67% com reranking (de 5,7% para 1,9% no top-20).
- **Custo:** baixo para indexar.
- **Complexidade:** média, porque é preciso montar o pipeline (ou usar um plugin como o Copilot).
- **Fraqueza no nosso caso:** perde a estrutura. Exemplos: "vigência", "versão maior vale", ligação país↔artefato↔ticket. Também não responde bem perguntas do tipo "o que todos os países têm em comum".
- **Citação:** sim, por trecho.
- **Fontes:** https://www.maginative.com/article/anthropics-contextual-retrieval-technique-enhances-rag-accuracy-by-67 ; https://gradientflow.com/contextual-retrieval-rag/

### 1.3 GraphRAG (Microsoft)
- **Como funciona:** um LLM extrai entidades e relações, monta comunidades hierárquicas e resume cada uma. Tem quatro modos de busca:
  - Global: perguntas sobre o corpus inteiro.
  - Local: uma entidade e a vizinhança dela.
  - DRIFT: local com contexto da comunidade.
  - Basic: vetorial.
- **Custo:** alto. A indexação completa custa **100 a 1.000 vezes mais** que RAG vetorial. Num benchmark, a busca global gastou cerca de 331 mil tokens de prompt por pergunta, contra cerca de 900 no RAG vetorial. A Microsoft recomenda ajustar os prompts (prompt tuning), e versão nova pode exigir reindexar. O **LazyGraphRAG** indexa ao custo de RAG vetorial e deixa o LLM para a hora da consulta.
- **Privacidade:** depende do LLM usado na extração; com Azure/OpenAI, entra um terceiro novo.
- **Manutenção:** alta.
- **Citação:** sim, por comunidade e trecho.
- **Fontes:** https://microsoft.github.io/graphrag/ ; https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/ ; https://www.beri.net/article/graphrag-vs-vector-rag-indexing-query-cost-lightrag-lazygraphrag-2026

### 1.4 LightRAG (HKUDS)
- **Como funciona:** grafo mais vetores, com recuperação em dois níveis: entidades específicas (baixo nível) e temas amplos (alto nível). Aceita vários backends (Neo4j, PostgreSQL, MongoDB...) e LLM local.
- **Custo:** bem menor que o GraphRAG por consulta. Gratuito e open source (cerca de 37 mil estrelas no GitHub).
- **Complexidade:** média a alta; é Python e serviço.
- **Privacidade:** pode ser 100% local com Ollama.
- **Manutenção:** média.
- **Fontes:** https://github.com/HKUDS/LightRAG ; https://arxiv.org/html/2410.05779v3

### 1.5 Neo4j com LLM
- **Como funciona:** banco de grafo de verdade, consultado em Cypher. O **LLM Knowledge Graph Builder** (Neo4j Labs, Apache-2.0) importa documentos, cria chunks, embeddings e entidades, e oferece chat GraphRAG. Aceita Anthropic, OpenAI e Ollama.
- **Custo:** gratuito em instância local (Neo4j Desktop/Docker). A versão AuraDB em nuvem é paga.
- **Complexidade:** alta, porque exige modelar e manter o esquema.
- **Privacidade:** local, se auto-hospedado.
- **Para nós:** o Graphify já exporta para Neo4j (`--neo4j` / `--neo4j-push`, segundo a skill local). Dá para testar sem montar o pipeline do zero.
- **Fontes:** https://neo4j.com/developer-blog/graphrag-ecosystem-tools/ ; https://neo4j.com/news/the-neo4j-llm-knowledge-graph-builder

### 1.6 SaaS corporativos: Notion AI, Confluence com Rovo, Glean
- **Notion AI:** o plano Business custa US$ 20 por usuário/mês e inclui "Ask Notion" (perguntas sobre o workspace), agentes e conectores. Exigiria **migrar** o cofre para o Notion e perder os arquivos .md locais e o git. Fonte: https://userjot.com/blog/notion-pricing-2025-plans-ai-costs-explained
- **Confluence com Rovo:** o Rovo vem incluído nos planos Cloud pagos (Standard desde out/2025) e tem residência de dados. Só vale se a Mercans já usar Confluence; o conector Atlassian aparece no ambiente, mas não confirmei se há um Confluence da Mercans. Fontes: https://www.cprime.com/blog/atlassian-rovo-faq/ ; https://www.atlassian.com/software/confluence/ai
- **Glean:** busca corporativa que respeita permissões. Não tem preço público; relatos indicam **mínimo de cerca de 100 assentos**, US$ 50–75 por usuário/mês e contrato de US$ 50–60 mil/ano. **Fora de escala** para um time pequeno. Fonte: https://www.gosearch.ai/blog/glean-pricing-explained (fonte de concorrente, tratar como indicativa)
- **Ponto comum dos três:** entra um terceiro novo. Além disso, a empresa bloqueia conectores Google, o que mostra uma TI restritiva com conectores.

### 1.7 Servidores MCP que dão ao Claude acesso às notas
- **MCP do Graphify:** `python -m graphify.serve graphify-out/graph.json` sobe um servidor MCP stdio **local**. Ferramentas: `query_graph`, `get_node`, `get_neighbors`, `get_community`, `god_nodes`, `graph_stats`, `shortest_path`. Funciona no Claude Desktop e no Claude Code (`.mcp.json`). Fontes: referência local da skill (`exports.md`, Step 7d) e https://github.com/yasinyaman/graphify-mcp (implementação de terceiros, só citada).
- **MCP do cofre Obsidian:**
  - `mcp-obsidian` (MarkusPfundstein) usa o plugin Local REST API, que sobe HTTPS em 127.0.0.1:27124 com chave.
  - Há servidores que leem a pasta direto, sem plugin, por stdio, sem abrir porta.
  - Também existe o plugin "MCP Tools".
  - Fontes: https://github.com/MarkusPfundstein/mcp-obsidian ; https://community.obsidian.md/plugins/mcp-tools ; https://github.com/dojicreates/Local-Obsidian-MCP-Server-with-Claude
- **Limitação importante:** MCP **local** (stdio) só funciona no **Claude Desktop e no Claude Code**. **No claude.ai web não funciona.** Os "custom connectors" do claude.ai são MCP **remotos**, chamados a partir da nuvem da Anthropic, o que exigiria publicar o cofre na internet e não serve para nós. Fontes: https://support.claude.com/en/articles/11175166-about-custom-connectors-remote-mcp-servers ; https://mer.vin/2026/08/local-vs-remote-mcp-how-claude-custom-connectors-work/
- **Custo:** zero.
- **Privacidade:** igual à de hoje, sem terceiro novo.
- **Manutenção:** baixa.
- **Citação:** o Claude cita o nó ou arquivo devolvido.

### 1.8 Projetos do claude.ai
- **Como funciona:** os arquivos ficam no "Project knowledge". Quando passam do limite de contexto, o Claude liga **RAG automático** nos planos pagos, com até cerca de 10 vezes mais capacidade e sem configuração. A Anthropic recomenda uma base menor e focada, nomes de arquivo descritivos e citar o documento pelo nome.
- **Fraquezas:** o upload é manual, então os arquivos se desatualizam em relação ao cofre. O suporte não documenta citação explícita.
- **Fontes:** https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects ; https://simonwillison.net/2024/Jun/25/claude-projects

### 1.9 Padrão "LLM wiki" (Karpathy): o que já fazemos
- **Como funciona:** o LLM **escreve e mantém** uma wiki em Markdown a partir de `raw/`; o humano lê no Obsidian. Passadas de "lint" consertam links e lacunas. Karpathy resume assim: "Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase".
- **Para nós:** é exatamente o modelo do brain-service (`raw/` → extrações → hubs, `revisa o cérebro` = lint). Confirma que a base está certa; a melhoria está na **consulta** e na **visualização**, não em trocar de arquitetura.
- **Fontes:** https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an ; https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-obsidian-ai-second-brain

---

## 2. Tabela comparativa (com o nosso setup atual)

Legenda: ●●● alto · ●● médio · ● baixo. "Terceiro novo" = algum fornecedor além da Anthropic recebe conteúdo.

| Opção | Pergunta → resposta com fonte | Mantém rede ligada | Processo por país | Custo | Complexidade/manutenção (Windows) | Terceiro novo? | Veredito para nós |
|---|---|---|---|---|---|---|---|
| **Setup atual** (Obsidian + Graphify CLI + Claude Code + Projetos claude.ai + skills) | ●●● no Claude Code (lê os .md e cita o caminho); ●● no claude.ai (upload manual) | ●● (links manuais + "revisa o cérebro" + grafo) | ●● (painel em `00-INDEX.md` à mão; `mapa-processo.html`) | já pago | ● | não | Base sólida (é o padrão "LLM wiki") |
| MCP do Graphify | ●●● consulta estruturada (vizinhos, caminho, comunidades) | ●● | ● | 0 | ● (um bloco no `.mcp.json`) | não | **Fazer** |
| MCP do cofre (stdio, sem porta) | ●●● leitura e busca de notas no Claude Desktop | ● | ● | 0 | ● | não | **Fazer** (para quem usa Claude Desktop) |
| Smart Connections (núcleo grátis) | ● (não responde) | ●●● sugere links que faltam | ● | 0 | ● | não (embedding local) | **Fazer** (barato e útil para a rede) |
| Copilot for Obsidian + Ollama | ●● Vault QA com citação, offline | ● | ● | 0 (hardware) | ●● (Ollama no Windows; qualidade do modelo local inferior) | não | Opcional, para quem não usa Claude |
| Khoj auto-hospedado | ●● | ● | ● | 0 | ●●● (mais um servidor) | não | Não agora |
| RAG vetorial próprio | ●● | ● | ● | ● | ●● | depende do embedding | Redundante com Claude Code + Graphify |
| LightRAG local | ●●● (local + global) | ●● | ● | ● | ●●● | não (se Ollama) | Só se o corpus crescer muito |
| GraphRAG (Microsoft) | ●●● em perguntas globais | ●● | ● | ●●● (indexação cara) | ●●● | sim (se Azure/OpenAI) | Não (custo e complexidade fora de escala) |
| Neo4j + LLM Graph Builder | ●●● (Cypher) | ●●● | ●● (consultas por etapa) | ● (local) | ●●● | não (local) | Só para teste via export do Graphify |
| Notion AI | ●● | ● | ●● (bancos de dados) | US$ 20/usuário/mês | ●● (migração) | sim | Não (perde .md, git e localidade) |
| Confluence + Rovo | ●● | ● | ●● | incluso se já houver Cloud pago | ●● | sim (Atlassian) | Só se a Mercans já padronizar Confluence |
| Glean | ●●● | ● | ● | cerca de 100 assentos no mínimo | ●● | sim | Não (escala) |
| Projetos claude.ai (do jeito de hoje) | ●● (RAG automático) | ● | ● | já pago | ● (mas o upload manual desatualiza) | não | Manter, com pacote gerado |

---

## 3. Recomendação: as 3 melhorias de melhor custo-benefício

**1) Servidor MCP do Graphify no Claude Code e no Claude Desktop (custo zero, cerca de 15 minutos)**
- **O que é:** registrar `graphify.serve` no `.mcp.json` da raiz, usando o caminho absoluto do Python em `graphify-out/.graphify_python`.
- **Ganho:** o Claude passa a chamar `get_neighbors("Colombia")` e `shortest_path("ticket X", "correcoes")` como **ferramenta**, sem depender de lembrar a regra do CLAUDE.md de rodar `graphify query` no terminal. Isso vale também para as 5 janelas de frente.
- **Custo:** nenhum terceiro novo.
- **Complemento:** o MCP do cofre (stdio, sem Local REST API, portanto sem porta aberta) para quem consulta pelo Claude Desktop.
- **Atenção:** **nenhum MCP local chega ao claude.ai web.** Para o web, ver o item 3.

**2) Painel de gestão gerado das notas: Obsidian Bases + script que já existe (custo zero)**
- **Bases** é plugin **nativo** do Obsidian (sem plugin de terceiro). Monta visões Tabela, Cards, **Kanban** e Lista a partir das *properties* das notas.
- **Passo 1:** colocar no frontmatter de cada `paises/<País>.md` campos como `etapa_research`, `etapa_design`, `etapa_suporte`, `ultima_revisao`, `tickets_abertos`.
- **Resultado:** o painel países × etapa, hoje mantido à mão no `00-INDEX.md`, vira **gerado** e para de divergir dos hubs (problema citado no último commit, "Painel de países alinhado aos hubs").
- **Passo 2:** o `scripts/mapa_processo.py` (que gera `mapa-processo.html`) passa a ler as mesmas properties. Assim, uma única fonte alimenta o painel do Obsidian e o HTML.
- **Fontes:** https://obsidian.md/help/bases ; https://www.dsebastien.net/how-i-turned-20-000-notes-into-live-dashboards-with-obsidian-bases/

**3) Smart Connections (núcleo grátis) para "manter a rede ligada" e um "pacote claude.ai" gerado do cofre**
- **Smart Connections:** embeddings locais, sem terceiro novo. Mostra notas parecidas sem link entre si, o que encontra órfãs e conexões que faltam. Alimenta o "revisa o cérebro".
- **Pacote para o claude.ai:** como o web não alcança o cofre, um script gera um pacote por país ou serviço para subir no Projeto. Exemplos de conteúdo: hub do país, correções daquele país, `fronteiras.md`, com data no nome. Isso troca o upload "de memória" por um pacote reproduzível, e o RAG automático do Projeto cuida do volume.
- **Não recomendado agora:** GraphRAG, Glean e Notion (custo ou terceiro novo, sem ganho sobre Claude Code + Graphify). LightRAG e Neo4j ficam como "plano B" se o corpus crescer muito além das cerca de 1.400 notas atuais.

---

## 4. Exemplos reais de times de compliance, jurídico e RH com "AI brain"

| Organização | O que fez | Resultado declarado | Fonte |
|---|---|---|---|
| **Neeyamo (payroll global)** | "Compass": sistema multiagente que lê mudanças regulatórias, interpreta o impacto por folha e gera a configuração; revisores humanos aceitam ou corrigem | mais de 11.000 mudanças monitoradas desde 2024; da publicação à recomendação em 48 h em vez de 3 semanas; 94% das interpretações aceitas sem mudança | https://gpa.net/blogs/global/global-neeyamo-announces-ai-system-for-global-payroll-compliance ; https://theprint.in/ani-press-releases/neeyamos-global-payroll-compliance-ai-enters-its-third-generation-with-multi-agent-compass/3057545/ (comunicado de imprensa) |
| **Kontek (payroll/HR, Suécia)** | Assistente "Sally" (fornecedor Unless) responde dúvidas de regras de payroll e trabalhistas dentro do produto | cada conversa "seria um ticket" para o suporte (depoimento) | https://9adb4c28-fe75-4802-9653-ae3d301c69e9.unless.com/en/customers/hr-payroll/ (case do fornecedor) |
| **IBM AskHR** | Agente de RH sobre cerca de 7.000 páginas de política; classifica a dúvida, responde ou escala para um humano | 94% de contenção; -75% de tickets desde 2016; -40% de custo operacional de RH em 4 anos | https://www.ibm.com/case-studies/ibm-askhr |
| **Jurídico da Anthropic** | "Skill" com a orientação histórica do jurídico para autoavaliação de material de marketing (Slack), redlining de contratos e privacy impact assessments; advogado revisa tudo | revisão de dias para horas | https://claude.com/blog/how-anthropic-uses-claude-for-legal |
| **A&O Shearman (Allen & Overy)** | Harvey (GPT) com o conhecimento interno do escritório | 3.500 advogados, cerca de 40.000 consultas no piloto; o escritório não usa métricas de tempo porque a revisão do output pesa | https://www.lawnext.com/2023/02/as-allen-overy-deploys-gpt-based-legal-app-harvey-firmwide-founders-say-other-firms-will-soon-follow.html |
| **GC AI (jurídico interno)** | Plataforma sobre Claude com playbooks e conhecimento institucional da empresa | mais de 1.500 empresas; cerca de 14 h por semana economizadas por advogado (declarado) | https://claude.com/customers/gc-ai |
| **Freshfields** | Claude para 5.700 pessoas, com co-desenvolvimento de workflows jurídicos | (acordo plurianual) | https://insights.munich-startup.de/news/feed/freshfields-deploys-anthropic-s-claude-ai-to-5-700-staff-globally-usage-surges-500-in-six-weeks |

**Padrões em comum, todos aplicáveis a nós:**
- O conhecimento do time vira **skill ou playbook** (como as nossas `payroll-compliance-<país>`).
- **Humano revisa antes de sair.**
- A métrica é tempo ou contenção.
- A Neeyamo é o caso mais próximo do nosso serviço: mudança regulatória → impacto por país → artefato.

---

## 5. Visualizações úteis de redes de conhecimento (além das "bolinhas")

1. **Matriz países × etapas/artefatos (heatmap de status).** Linhas = países; colunas = Research / Design / Suporte, ou CCG / WTC / DD / Report Specs / SIR. A cor indica o status e a data da última revisão. É o painel do `00-INDEX.md`, mas gerado pelas properties via Bases ou pelo `mapa_processo.py`. Pela pesquisa de Ghoniem, Fekete e Castagliola (InfoVis 2004), **matriz supera nó-e-aresta em grafos acima de cerca de 20 vértices** na maioria das tarefas; nó-e-aresta só ganha em seguir caminho. Com mais de 40 países, a matriz é a escolha certa. Fonte: https://hal.archives-ouvertes.fr/hal-00343819
2. **Matriz de adjacência país × tema** (ex.: país × "correção registrada", "valor sem fonte", "ticket aberto"). Mostra **lacunas** (células vazias em vermelho), na linha de "onde a ontologia não foi aplicada". Fonte: https://docs.open-metadata.org/v2.1.x-SNAPSHOT/how-to-guides/ontology/knowledge-graph/explore
3. **Kanban por etapa** (Bases, visão Kanban): cada país é um cartão que anda entre Research → Design → Suporte. Fonte: https://obsidian.md/help/bases
4. **Mapa de processo (fluxograma/Mermaid)** por serviço, com os países como contagem em cada caixa. Mermaid é nativo no Obsidian, mas **não tem swimlane nativo**; para raias, usar Canvas ou HTML gerado (o `mapa-processo.html` já existe). Fontes: https://simonecarletti.com/blog/2026/02/obsidian-mermaid-view/ ; https://github.com/Mermaid-Chart/issue-tracker/issues/128
5. **Linha do tempo de vigências e versões** por país (Gantt Mermaid ou HTML): valores estatutários com início e fim (regra 1 e 2 do CLAUDE.md) e versões de artefato (regra 8). Mostra rápido o que está para vencer ou mudar.
6. **Tabela de "saúde do cérebro"** gerada pelo lint: notas órfãs, links quebrados, valores sem fonte, hubs sem revisão há mais de 30 dias, por país. É o relatório de "revisa o cérebro" em formato de painel.
7. **Ego-network de um país** (em vez do grafo inteiro): só o país, os vizinhos de 1 a 2 saltos (artefatos, tickets, correções), via `get_neighbors` do MCP do Graphify. É legível porque é pequeno.

Base conceitual para escolher o formato de visualização conforme o objetivo de gestão do conhecimento: Eppler e Burkhard, "Visual representations in knowledge management: framework and cases" (J. Knowledge Management, 2007), https://dx.doi.org/10.1108/13673270710762756

---

## Ressalvas
- Os preços de Glean e Notion vêm de fontes secundárias ou de concorrentes; tratar como indicativos.
- Os casos Neeyamo e Kontek são comunicados ou cases de fornecedor, não auditorias independentes.
- Não testei nenhuma ferramenta. O modo `--mcp` do Graphify foi confirmado só pela documentação da skill instalada.
- Tudo o que adiciona terceiro novo precisa ser checado contra [[uso-de-ia]] e a TI da Mercans antes.
