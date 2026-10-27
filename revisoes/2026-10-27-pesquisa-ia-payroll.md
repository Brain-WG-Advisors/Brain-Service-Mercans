# Pesquisa: IA e redes neurais em payroll + "brain de IA" (2026-10-27)

> Pedido do usuário (27/10): "pesquisas profundas de redes neurais… todas relacionadas com payroll. Outra coisa brain de IA?" · Plano: [[PLANO]] (Fase R) · Sessão: [[sessoes/2026-10-27]] · Uso de IA na Mercans: [[uso-de-ia]]
> Três pesquisas paralelas (agentes, só leitura na web). Anexos com todas as fontes: [[revisoes/2026-10-27-pesquisa-ia-payroll/1-ia-na-folha|1. IA na folha]] · [[revisoes/2026-10-27-pesquisa-ia-payroll/2-grafos-compliance|2. Grafos para compliance]] · [[revisoes/2026-10-27-pesquisa-ia-payroll/3-brain-de-ia|3. Brain de IA]].
> **Conferência:** os 4 números-chave abaixo foram reabertos na fonte pela janela geral em 27/10 (✔). O resto vem dos agentes; o que é só marketing de fornecedor está marcado [não confirmado] nos anexos.

## 1. Conclusões

1. **LLM não calcula folha com segurança.** É o "gabarito" (nossos artefatos) que dá valor à IA na folha.
   - ✔ Remote PayMark (21/10/2026): 2.000 payslips reais de 50 países. O melhor modelo (GPT-6 Astra, esforço alto) acertou por completo 26%; as deduções do empregado causam a maioria dos erros. No HRmark (perguntas de RH), o melhor foi Claude Fable 5.1, com 69%. https://remote.com/blog/ai-payroll-benchmark
   - TaxCalcBench (2025): menos de 1/3 das declarações certas. https://arxiv.org/abs/2507.16126v1
   - **Confirma o nosso método:** fonte primária + conta refeita por script.
2. **Caso quase igual ao nosso trabalho.**
   - ✔ SEGER-ES (Governo do ES, 2026): agentes de IA (ChatGPT, Copilot, Claude Code) fizeram engenharia reversa de centenas de rubricas sem documentação, numa folha com mais de 20 anos, e estruturaram as regras num template.
   - "O Claude Code se destacou como a ferramenta mais eficaz" (resumo do artigo).
   - https://seger.es.gov.br/media/Gestao_do_conhecimento/2026/2_trabalho_ia-aplicada-a-folha-de-pagamento-da-extracao-a-estruturacao-de-regras.pdf
3. **Detecção de anomalia antes de fechar a folha** é o que todos os grandes anunciam: ADP, Oracle, Workday, Dayforce, Deel, Papaya, UKG.
   - Quase tudo é [não confirmado].
   - A técnica real aparece na patente SAP US11276124 (detectores não supervisionados + rede neural → auditor humano) e em artigos com autoencoders e Isolation Forest, cujo problema conhecido é o excesso de falsos positivos.
   - **Para nós:** os alertas viram tickets do tipo "isto está certo pela lei?".
4. **Leitura de holerite:** os modelos prontos (Azure `prebuilt-payStub.us`, Google Payslip Parser) servem aos EUA. Para outros países é preciso um esquema próprio, e o Payslip Spec + WTC é esse esquema.
5. **Regulação.** ✔ O Regulamento (UE) 2026/1744 (Digital Omnibus, JO de 24/07/2026) adiou as obrigações de alto risco do Anexo III (emprego) de 02/08/2026 para **02/12/2027**. GDPR e as regras nacionais continuam valendo. https://www.cuatrecasas.com/en/global/labor-and-employment/art/digital-omnibus-on-ai-how-does-it-impact-employment-relations
6. **Grafo gerado solto pela IA não basta em domínio legal.**
   - ✔ Stanford (23/05/2024): Lexis+ AI e Ask Practical Law AI erraram mais de 17% das vezes; Westlaw AI-Assisted Research, mais de 34%. https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries
   - O ganho do grafo está em achar o trecho certo da fonte, não em escrever a resposta.
   - **Conclusão:** o esquema deve ser fixo e curado, com fonte e nível A/B/C/D em cada fato.
7. **O padrão do mercado para lei com vigência é o das nossas regras 1 e 2.**
   - A lei tem identificador fixo e versões datadas (Akoma Ntoso/ELI).
   - Cada parâmetro tem valor por data e referência legal (OpenFisca).
   - O valor antigo é encerrado, nunca apagado (Graphiti: dois tempos).
8. **"Brain de IA": a arquitetura do cérebro já é a recomendada.**
   - É o padrão "LLM wiki" (Karpathy): `raw/` → notas mantidas pelo LLM → lint ("revisa o cérebro").
   - O ganho está na **consulta** e na **visualização**, não em trocar de ferramenta.
   - Acima de cerca de 20 nós, matriz se lê melhor que grafo de bolinhas (Ghoniem e Fekete, 2004).

## 2. Recomendação (ordem)

| # | O quê | Custo | Situação |
|---|---|---|---|
| 1 | **Campos fixos (properties) no cabeçalho dos hubs** + **painel 2D gerado** (Obsidian Bases): países × etapa × artefato (versão e data). Substitui o 3D e o painel feito à mão | 0 | **Piloto Colômbia em 27/10** (abaixo) |
| 2 | **Ligações com nome** na cadeia lei → regra → artefato → ticket → correção (`fundamentada_em`, `implementa`, `corrige`, `substitui`), em campos que o Graphify lê. Modelo de dados no anexo 2, §6 | 0 | próximo passo, depois do piloto |
| 3 | **MCP do Graphify** no Claude Code (`python -m graphify.serve graphify-out/graph.json`): o Claude consulta a rede como ferramenta | 0 | não testado; não chega ao claude.ai web |
| 4 | Smart Connections (plugin, embeddings locais) para sugerir ligações que faltam | 0 | opcional; conferir [[uso-de-ia]] |

**Descartados por ora:** GraphRAG da Microsoft (indexar custa de 100 a 1.000 vezes mais), Glean (cerca de 100 usuários no mínimo), Notion AI (exige migrar). LightRAG e Neo4j ficam como plano B; o Graphify já exporta para Neo4j.

## 3. Piloto Colômbia (2026-10-27)

- **Feito:**
  - [[Colombia]] ganhou properties no cabeçalho: etapa e data de cada serviço, versão e data de cada artefato vigente, e tickets abertos conferidos na API.
  - Painel gerado em `paineis/paises.base` (Obsidian Bases), aberto a partir do [[00-INDEX]].
- **Achado do piloto:** a linha Suporte da Colômbia dizia "5 tickets sem resposta" (snapshot de 16/09). Na API (27/10), os 5 estão Resolved, e a linha foi corrigida. É o tipo de defasagem que o painel gerado evita.
- **Para estender aos outros hubs:**
  1. o usuário aprova o formato no Obsidian;
  2. script com as regras de lote do [[CLAUDE]];
  3. o `modelos/pais.md` ganha o mesmo cabeçalho;
  4. o `scripts/mapa_processo.py` passa a ler as properties.

## 3b. Extensão aos 51 hubs (2026-10-27)
- **Como foi feito:**
  - Etapas e artefatos foram lidos dos próprios hubs por agentes (só o que o hub diz; versão vigente = maior número, regra 8).
  - Suporte foi calculado pelo estado na API (`raw/tickets/api/2026-10-27/`) dos tickets citados na seção Suporte: Resolved, Done e Rejected contam como fechados.
  - Campo vazio = o hub não registra.
- **Resultado:**
  - 35 hubs sem ticket citado; 9 sem ticket aberto (inclui a Colômbia).
  - 8 com ticket aberto: Taiwan 6, Ucrânia 5, Espanha 3 e outros.
  - 3 tickets com estado vazio na API: CT-4619, CT-4457 e CT-4321.
- **Divergência:** o painel feito à mão do [[00-INDEX]] e a linha Suporte da Situação de cada hub podem divergir das properties. O painel gerado vale como o mais novo; o alinhamento do corpo dos hubs fica para depois.

**Dúvidas registradas pelos agentes** (campos deixados vazios ou com ressalva; conferir ao atualizar cada hub):

- [[Argelia]]: Hub so cita Spec DAS (v2.1 vigente; v2.2 Draft local nao promovida, 2026-10-27); sem data da v2.1; sem skill
- [[Australia]]: Research marcado [INCERTO] no hub; sem data
- [[Belgica]]: Hub tem colisao de rotulos pipeline x Drive x brain. CCG: v1.2 pipeline (maior numero) mas Drive e mais novo em conteudo. WTC v1.3 so citado como vigente no texto, sem data. SIR: arquivo 29/09 vs VC 17/08, data deixada vazia. Report specs: equivalencia nao verificada, vigente indefinida; snapshot 2026-08 nao e AAAA-MM-DD completo.
- [[Botsuana]]: CCG data '2026-02' (so mes) deixada vazia; WTC/DD sem data; design em producao mas Producao '—'
- [[Bulgaria]]: Datas 'snapshot 2026-08' mantidas como 2026-08 (sem dia). DD v2.1 e 'base do design', unica versao citada. Skill: nao ha.
- [[Canada]]: Data = snapshot 2026-08 (sem dia). Design [INCERTO] no hub. Hub nao traz versoes de CCG/WTC/DD/specs (versao n/a). Payslip: so correcao mencionada, sem versao.
- [[Cazaquistao]]: Hub diz 'Skill: nao ha'. Sem artefatos. Internal Certification validada 2026-10-19 (fora dos campos).
- [[Chade]]: Datas de CCG/WTC/DD/specs vazias na tabela de artefatos. Versao da skill [INCERTO].
- [[Chile]]: Datas so mes/ano (mai/2026, jun/2026). Specs sem versao; data = link atualizado ~2026-09-15 (aproximada). Skill com 7 discrepancias de taxa em aberto.
- [[China]]: Data do research era ~2026-08-10 (til removido). Hub diz 'Skill: nao ha'. Payslip v1.0 ~2026-07-10; SR-316 Done 2026-10-14 (Pendencias). Resto [INCERTO].
- [[Chipre]]: Data do research '[data?]' (vazia). Tabela de artefatos vazia.
- [[Congo]]: CCG/WTC/report specs 'sem versao citada' ([INCERTO]); deixei ccg/wtc/dd vazios. Congo-Brazzaville, nao RD Congo.
- [[Costa-Rica]]: Data do research '[data?]' (vazia). Tabela de artefatos vazia.
- [[Costa-do-Marfim]]: Versao CCG/WTC/DD nao citada [INCERTO]. Data do research e snapshot 2026-08-12. Specs prontas para upload, sem versao.
- [[Espanha]]: DD V5.1 é Draft (2026-10-20). Report specs: datas variam por spec, data deixada vazia. SIR e payslip não aparecem no hub.
- [[Filipinas]]: Data do research '[data?]' no hub.
- [[Franca]]: Reemissão 2026-10-06 com numeração reiniciada (v1.0 vigente, exceção à regra 8). Payslip: hub diz v1.0 x v1.1 INCERTO, deixado vazio. Validação humana pendente (F6-20261027). Skill do hub: fr-compliance (roteadora) além de payroll-compliance-france.
- [[Gabao]]: WTC v3.1 é DRAFT; hub diz 'sem skill' e INCERTO se CCG/DD existem; payslip ~2026-08-10 sem versão.
- [[Guine-Equatorial]]: Data do research '[data?]' no hub.
- [[Holanda]]: Data research 'até 2026-09' (sem dia) -> vazio; CCG NL reconstruída sem versão e sem data exata; design marcado [INCERTO].
- [[Hungria]]: Hub sem skill. Etapa design tem data aproximada ~2026-06-25. Report specs 'em andamento'; SIR aguardando feedback.
- [[India]]: Hub só tem Global WTC Taxability Display (2 cópias, sem versão); não tratei como WTC. Sem skill. Research [INCERTO].
- [[Indonesia]]: Data do research '[data?]'; ficha de artefatos vazia.
- [[Irlanda]]: Research 'data 2025 (base)' -> vazio; CCG 'IE 2025' sem versão; datas das versões não informadas.
- [[Kuwait]]: Research e design [INCERTO]; sem artefatos.
- [[Libano]]: Data 2026-09-11 é do relatório QA.
- [[Lituania]]: Tabela de artefatos diz 'nenhum citado', mas 'Consolidado 2026-10-13' lista baseline (CCG 2026 sem versão, WTC V3.0, DD V3.0, specs v1.0, jun/jul 2025); usei isso, sem datas exatas. Research marcado aguardando apesar do baseline. Sem skill.
- [[Malasia]]: Data do research '[data?]'; ficha vazia.
- [[Marrocos]]: Data do research é [data?] no hub; artefatos não listados.
- [[Mocambique]]: Artefatos não listados no hub.
- [[Namibia]]: Data research ~2026-07 [INCERTO] no hub (mantido 2026-07, sem dia); artefatos sem versão e sem data; sem skill.
- [[Noruega]]: Artefatos não listados no hub.
- [[Portugal]]: Data do research é [data?]; artefatos não listados.
- [[RD-Congo]]: Data do research é [data?]; artefatos não listados.
- [[Reino-Unido]]: Directors' NI (KB) sem versão, não é um dos artefatos do modelo.
- [[Romenia]]: Hub marca research e design como [INCERTO]; sem artefatos; sem skill.
- [[Singapura]]: Data do research é [data?]; artefatos não listados.
- [[Taiwan]]: Payslip (SR-109 v1.2, 2026-10-27) e specs são Draft só local; sem skill no hub
- [[Tchequia]]: Data da pesquisa vem como [data?] no hub; deixada vazia
- [[Ucrania]]: Data da pesquisa só 2026-09 (sem dia); CCG/DD datas aproximadas (~); WTC V4.4 em Draft (VC 26/10); skill 'não há'; produção só 'Ver fronteiras'

## 4. O que isso significa para o serviço
- Escrever nos artefatos **regras de validação explícitas e testáveis** (campo obrigatório se…, base = soma dos WT com flag…, teto com vigência). São elas que os agentes de anomalia dos fornecedores usam.
- Guardar no hub de cada país as **causas de variação legítima** (retroativos, troca de teto ou alíquota, pagamentos sazonais), para os tickets de alerta que vão crescer.
- Não repetir números de fornecedor ("100% compliance", "4x mais rápido") em entregáveis.
