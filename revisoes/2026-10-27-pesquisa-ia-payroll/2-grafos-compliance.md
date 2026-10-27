# Pesquisa 2 — Grafos de conhecimento para compliance de payroll multipaís

> Anexo de [[revisoes/2026-10-27-pesquisa-ia-payroll|Pesquisa: IA e redes neurais em payroll]] (relatório único). Números-chave reabertos na fonte em 2026-10-27 pela janela geral.

> Data: 2026-10-27. Pesquisa só leitura na web (WebSearch/WebFetch). Contexto lido no vault: `CLAUDE.md`, `correcoes.md`, `paises/Colombia.md`, `servicos/research-pipeline.md`, `servicos/design.md`, `servicos/suporte.md`.
> Convenção: **[não confirmado]** = afirmação de marketing/divulgação do próprio fornecedor, sem verificação independente. Onde não achei fonte, digo isso.

---

## Resumo executivo

1. **Para lei com vigência, o padrão maduro é "obra × versão no tempo"** (FRBR/Akoma Ntoso/ELI): a lei tem um identificador fixo e cada versão consolidada tem data. OpenFisca aplica a mesma ideia ao *valor* (cada parâmetro tem valores por data, cada um com a sua referência legal). É exatamente a nossa Regra 1/Regra 2 (vigência + fonte; nunca sobrescrever).
2. **Rules as code (OpenFisca, Catala, Blawx, RegelSpraak)** mostra que vale separar **parâmetro** (alíquota, teto, faixa — muda todo ano) de **regra** (lógica — muda pouco), e testar a regra com casos. Não precisamos virar "rules as code", mas o modelo de dados deve ter esses dois tipos de nó.
3. **GraphRAG/LightRAG/Neo4j LLM Graph Builder** extraem entidades automaticamente com LLM; o ganho de exatidão em QA regulatório é modesto e depende de cada fato manter **link para o trecho de origem** (proveniência). Em domínio legal, até ferramentas comerciais com RAG erram 17–34% (Stanford, 2024). Conclusão: grafo do cérebro deve ser **curado (esquema fixo)**, não "extração livre", e cada aresta factual deve carregar fonte e nível de evidência.
4. **Rastreabilidade** (fonte → obrigação → controle/artefato → evidência → incidente) é o modelo usado por GRC/RegTech (obligations register) e por engenharia regulada (matriz de rastreabilidade bidirecional). Para nós: Fonte legal → Regra/Valor → Artefato (CCG/WTC/DD/Spec/SIR/Payslip/Skill) → Ticket → Correção.
5. **Fornecedores** (Deel, Papaya, ADP, Vertex, SAP) organizam por país com time de monitoramento legislativo, conteúdo datado e "legal change" por país; quase tudo o que dizem sobre IA é marketing **[não confirmado]**. O padrão concreto e verificável é o do SAP (anúncio de mudança legal por país/componente/data planejada) e o de Vertex (regras "efetivas" por jurisdição, atualização mensal).
6. **Para gestão**: matriz país × etapa (já temos), matriz país × artefato com versão/data, cobertura "regra sem fonte", "artefato sem regra rastreada", "correções por artefato" — todas deriváveis do grafo.

---

## 1. Grafos de conhecimento e ontologias legais; rules as code

### 1.1 Ontologias e padrões de documento legal

| Padrão | O que é | Fonte | Como se aplica a nós |
|---|---|---|---|
| **LKIF / LKIF-Core** | Formato de intercâmbio de conhecimento jurídico do projeto europeu ESTRELLA; OWL-DL + SWRL, com ontologia de conceitos jurídicos básicos (norma, ação, papel, tempo). | https://en.wikipedia.org/wiki/Legal_Knowledge_Interchange_Format · https://dare.uva.nl/id/bd48bad5-d85f-4576-842c-2ff4c128a811 | Acadêmico e pesado. Útil só como vocabulário de referência (ex.: distinguir *norma* de *documento*). Não adotar. |
| **Akoma Ntoso / OASIS LegalDocML** | XML para documentos legislativos, com identificação FRBR: **Work** (a lei abstrata), **Expression** (versão num idioma numa data), **Manifestation** (o PDF/XML publicado). | https://diff.parlamento.ai/docs/akn/frbr · Exemplo real (Laws.Africa): obra `/akn/za/act/1998/55`, versão em inglês consolidada em 17/01/2014 `/akn/za/act/1998/55/eng@2014-01-17` — https://developers.laws.africa/get-started/works-and-expressions | **Ideia central para o nosso `raw/docs/oficiais/<CC>/`**: separar "a lei" (Work) de "a versão baixada em data X" (Expression/Manifestation). Já fazemos parcialmente (data no nome do arquivo). |
| **ELI (European Legislation Identifier)** | Identificador e ontologia de metadados de legislação na UE; relações como *amends*, *is consolidated by*; versões temporais. Espanha (BOE) publica com ELI. | https://interoperable-europe.ec.europa.eu/collection/eli-european-legislation-identifier/solution/eli-i · https://boe.es/legislacion/eli.php?lang=en | Quando o país tem ELI (ES, FR, IE, LU, BE...), usar o URI ELI como ID da fonte no grafo. Aresta `altera`/`consolida` entre leis. |
| **Modelo diacrônico de normas (LRMoo, 2025)** | Artigo que decompõe normas em componentes (artigos/parágrafos) com versões datadas e eventos de alteração, para responder "qual era a regra na data X" em RAG. | https://arxiv.org/pdf/2506.07853 | Justifica versionar **no nível do artigo** (ex.: "Orden PJC/297/2026 Art. 6.1"), não do documento inteiro — é como já citamos em `correcoes.md`. |
| **LegalRuleML (OASIS, 2021)** | Marcação de regras jurídicas: deôntica (obrigação/permissão/proibição), parâmetros temporais de validade, jurisdição, URI da fonte oficial, derrotabilidade (regra que excepciona outra). | https://www.oasis-open.org/?p=7649 | Os **atributos** valem para nós (jurisdição, vigência, fonte, "exceção de"); a sintaxe XML não. |
| **FIBO (EDM Council)** | Ontologia do setor financeiro (entidades legais, instrumentos, processos). | https://spec.edmcouncil.org/fibo/ · https://edmcouncil.org/frameworks/industry-models/fibo/ | Pouca aderência a payroll. Só como exemplo de governança de ontologia aberta. Não adotar. |
| **W3C PROV-O** | Recomendação W3C (2013) de proveniência: Entity, Activity, Agent; `wasDerivedFrom`, `wasGeneratedBy`, `wasAttributedTo`. | https://www.w3.org/blog/2012/the-prov-ontology-an-update (e spec PROV-O) | **Modelo de proveniência para o cérebro**: Artefato v1.4 `wasDerivedFrom` Artefato v1.3; `wasGeneratedBy` Sessão/Build; `wasAttributedTo` Frente/Pessoa. |
| **Ontologia de remuneração (OntoPiA, Itália)** | Extensão de ontologia pública italiana com `SalaryRecord`, `SalaryComponent`. | https://ricerca.uniparthenope.it/handle/11367/159758 | Exemplo raro de "wage type" como classe; confirma que componente salarial é nó próprio. Não verifiquei o texto completo. |

**Não encontrei** ontologia pública específica de payroll multipaís (wage types × tributos × relatórios estatutários). O mais próximo é o HR-XML `WageType` (https://schemas.liquid-technologies.com/HR-XML/2007-04-15/wagetype.html), que é só um elemento de intercâmbio.

### 1.2 Rules as code

| Projeto | O que é | Exemplo real com fonte | Como se aplica |
|---|---|---|---|
| **OpenFisca** | Motor open source (Etalab/beta.gouv, França) que codifica legislação tributária e de benefícios. "Country package" por país com **Parameters** (valores datados), **Variables** (fórmulas) e **Entities**. Usado em ~10 países. | Docs: https://openfisca.readthedocs.io/ · Parâmetro YAML com valores por data e `reference` legal por valor: https://openfisca.readthedocs.io/en/latest/coding-the-legislation/legislation_parameters.html · Whitepaper OCDE: https://oecd-opsi.org/wp-content/uploads/2022/09/Whitepaper-Attachment-02-About-OpenFisca.pdf | **Modelo direto para valores estatutários**: `teto_CNPS: {2025-01-01: {value: X, reference: <decreto>}, 2026-01-01: {...}}`. Uma linha por vigência, nunca sobrescreve, referência por valor — idêntico às nossas Regras 1 e 2. |
| **Catala** | Linguagem (Inria/Microsoft Research) que traduz lei em código executável, escrita *ao lado do texto legal* (programação literária). Avaliada no US IRC §121 e nos benefícios familiares franceses (achou bug na implementação oficial); projeto com a DGFiP (imposto de renda francês) desde 2023. | https://www.microsoft.com/en-us/research/publication/catala-a-programming-language-for-the-law/ · https://arxiv.org/abs/2103.03198v2 | Lição: **texto legal e regra lado a lado** — no CCG, cada regra cita o artigo literal. Codificar em Catala é fora do nosso escopo. |
| **Blawx** | Ferramenta web visual (blocos) para codificar regras (answer set programming); exemplo com o Old Age Security Act (Canadá). Protótipo. | https://law.mit.edu/pub/blawxrulesascodedemonstration · https://popl23.sigplan.org/details/prolala-2023-papers/12/Blawx-User-friendly-Goal-Directed-Answer-Set-Programming-for-Rules-as-Code | Bom para mostrar a não técnicos "por que" uma regra deu o resultado (explicação). Protótipo; não adotar. |
| **RegelSpraak + ALEF (Belastingdienst, NL)** | Linguagem natural controlada para regras fiscais, a partir de **análise jurídica sistemática da lei (wetsanalyse)** com anotações ligando regra ao trecho legal; o ALEF (JetBrains MPS) gera código. Usado inclusive no cálculo das **tabelas de imposto sobre salários**. | https://research.vu.nl/en/publications/regelspraak-a-cnl-for-executable-tax-rules-specification/ · https://resources.jetbrains.com/storage/products/mps/docs/MPS_DTO_Case_Study.pdf | **Caso mais próximo de payroll em produção.** Lição: anotar a lei → regra em linguagem controlada → artefato, com link de anotação. Mapeia bem para "fonte → regra (CCG) → WTC/DD". |
| **Payroll com raciocínio automático (KU Leuven + Teal Partners, AAAI 2021)** | Legislação fiscal belga traduzida para representação formal e compilada em restrições (SMT/otimização) para explorar políticas de remuneração; "implantado por um fundo de seguro social". | https://ojs.aaai.org/index.php/AAAI/article/view/17774 | Prova de que regras de payroll cabem em representação formal; não é nosso foco (nós documentamos, não calculamos). |
| **OCDE — Cracking the Code (2020)** | Primer da OCDE sobre Rules as Code: versão de máquina convivendo com o texto natural. | https://oecd-opsi.org/publications/cracking-the-code/ | Referência conceitual para explicar à gestão. |
| **DMN (OMG)** | Notação de decisão com tabelas (entradas, saídas, regras, hit policy). Caso real: regras fiscais de artistas visitantes na Bélgica. | https://www.inf.unibz.it/~calvanese/papers-html/BPM-2016.html · https://lirias.kuleuven.be/bitstream/123456789/642718/2/KAIS_2020.pdf | Faixas de IR, regras de isenção e "qual relatório leva qual wage type" são tabelas de decisão; o WTC já é quase uma tabela DMN. |

---

## 2. GraphRAG, KG + LLM, RAG em regulação

| Abordagem | O que é | Fonte | Achado relevante |
|---|---|---|---|
| **Microsoft GraphRAG** | LLM extrai entidades/relações do corpus, gera grafo, detecta comunidades e resume cada comunidade; consulta "local" (entidade) e "global" (temas). | Blog MSR (13/02/2024): https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/ · Docs: https://microsoft.github.io/graphrag/ | Bom para perguntas amplas ("o que mudou em contribuições sociais nos países africanos"); caro para indexar; o grafo extraído é livre (sem esquema). |
| **LightRAG (HKU)** | Alternativa leve: grafo de entidades + recuperação em dois níveis (específico e temático), **atualização incremental** sem reindexar tudo. | https://arxiv.org/abs/2410.05779v3 · https://github.com/HKUDS/LightRAG | A atualização incremental importa para nós (o cérebro muda todo dia). |
| **Neo4j LLM Knowledge Graph Builder** | App (Neo4j Labs) que transforma PDF/web/docs em **grafo léxico** (documento → chunks com embeddings) + **grafo de entidades**; aceita **esquema customizado**; chat sobre o grafo. | https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/ · https://github.com/neo4j-labs/llm-graph-builder | O par "grafo léxico + grafo de entidades" é o desenho certo: o trecho da fonte (chunk) fica ligado ao fato. Esquema customizado = nosso modelo abaixo. |
| **RAGulating Compliance (2025)** | Multiagente: extrai triplas sujeito–predicado–objeto de regulação (eCFR/FDA), **cada tripla com link ao texto de origem**, guarda em vetor + grafo. | https://arxiv.org/html/2508.09893v1 | Ganho real foi em **achar a seção certa** (0,29 vs 0,17 de acerto de seção no limiar 0,75); a nota da resposta quase não mudou (4,73 vs 4,71). Ou seja: grafo ajuda rastreabilidade mais que "inteligência". |
| **Graphiti / Zep** | Grafo temporal para memória de agentes; **bitemporal** nas arestas: `valid_at`/`invalid_at` (verdade no mundo) + tempo de registro; fato contraditório invalida a aresta antiga em vez de apagar. | https://blog.getzep.com/beyond-static-knowledge-graphs/ · https://pypi.org/project/graphiti-core/ | **Exatamente a nossa regra de vigência**: valor antigo recebe data de fim, novo é acrescentado. Adotar os dois tempos: vigência legal × data em que soubemos/registramos. |
| **Survey Graph RAG (2025)** | Revisão de GraphRAG em domínios customizados, incluindo compliance legal. | https://arxiv.org/pdf/2501.13958 | Contexto geral. |
| **Alerta: alucinação em IA jurídica (Stanford RegLab/HAI, 2024)** | Ferramentas comerciais com RAG (Lexis+ AI, Westlaw AI-Assisted Research, Ask Practical Law AI) erraram/alucinaram em 17% a 33% das consultas de benchmark. | https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries | Confirma a nossa regra "fonte primária para cada afirmação; o que o agente reportar, reabrir". RAG/grafo **não** substitui a conferência. |

**Implicação para o cérebro:** já existe `graphify-out/graph.json` (grafo extraído das notas). O próximo passo não é um GraphRAG genérico, e sim **tipar** os nós/arestas com um esquema fixo (seção 6) e exigir `fonte` + `nivel_evidencia` em toda aresta factual.

---

## 3. Como fornecedores e consultorias organizam conhecimento estatutário de payroll

| Fornecedor | O que divulgam | Fonte | Status |
|---|---|---|---|
| **Deel** | Knowledge Hub com country guides "escritos por 350+ profissionais jurídicos/RH/contábeis", newsfeed de mudanças regulatórias em ~150 países, alertas; Deel AI responde "a partir da base de conhecimento jurídica verificada". | https://www.deel.com/blog/introducing-deel-knowledge-hub/ · https://www.deel.com/solutions/compliance/ | Números e "verificado" = **[não confirmado]**. Vagas confirmam papéis de "Payroll Product Compliance" por região (https://builtin.com/job/regional-lead-payroll-product-compliance-apac/4453983). |
| **Papaya Global** | "Motor de compliance e validação" por país; agente de validação de ciclo; lançou "ONE" (2026), que trabalha a partir de políticas, CBAs e dados de folha do cliente. | https://www.pymnts.com/payroll/2025/ai-shakes-up-global-payroll-by-bridging-compliance-chaos · https://ipsnews.net/business/2026/06/29/papaya-global-launches-one-an-agentic-compliance-intelligence-platform-tailored-to-each-organization/?amp=1 | **[não confirmado]** (press release). Ideia útil: separar conhecimento **legal** do **contratual do cliente** (CBA/política) — no nosso caso, o cliente fica fora do escopo/PII. |
| **Remote** | Remote AI sobre "base global de conhecimento de RH"; time jurídico com subtimes (Product, Employment, Regulatory). | https://remote.com/blog/introducing-remote-ai | **[não confirmado]**. |
| **ADP Global Payroll** | Times locais de "legal & regulatory watch"; 700+ boletins legislativos de payroll em 2024; 3.000+ profissionais de compliance/payroll; 140+ países. | https://uk.adp.com/what-we-offer/products/adp-global-payroll.aspx · https://uk.adp.com/about-adp/press-centre/adp-empowers-midsize-companies-with-scalable-global-payroll-solutions-in-over-140-countries.aspx | Números **[não confirmado]**. Padrão útil: **boletim legislativo** como objeto (mudança → impacto → data de implementação). |
| **Vertex Payroll Tax** | Base proprietária de "regras efetivas" mantida por time de pesquisa; atualização mensal; contato com as jurisdições. | https://www.vertexinc.com/sites/default/files/2022-03/vertex-payroll-tax-data-sheet.pdf · https://developer.vertexinc.com/payroll/docs/vertex-payroll-tax-api-implementation | "300 mi de regras / 19 mil jurisdições" = **[não confirmado]**. Padrão concreto: regra com **data efetiva** por jurisdição + ciclo fixo de atualização. |
| **SAP (HCM / SuccessFactors Employee Central Payroll)** | "Announcement of Legal Change" filtrável por **país/região, componente, data planejada de entrega**; Legal Change Patches; SAP Notes por mudança legal por country version (ex.: newsletter de payroll Colômbia). | https://learning.sap.com/courses/sap-successfactors-employee-central-payroll-project-team-orientation/accessing-announcement-of-legal-changes-application_ff04ff94-5395-4a3c-9e1a-4b45abec4761 · https://blogs.sap.com/2020/09/18/how-to-find-legal-changes-using-the-announcement-of-legal-change-application/ · https://blogs.sap.com/2022/10/10/hcm-colombia-sap-hcm-payroll-colombia-newsletter/ | **O exemplo verificável mais útil**: a "mudança legal" é um objeto com país, componente afetado, data legal e data de entrega. Mapeia para nosso nó `MudancaLegal` → afeta `Artefato`. |
| **Thomson Reuters (Checkpoint Edge com CoCounsel)** | Assistente de IA para pesquisa tributária com links para conteúdo editorial e fontes. | https://www.thomsonreuters.com/en/press-releases/2024/april/thomson-reuters-unveils-checkpoint-edge-with-cocounsel-featuring-its-generative-ai-assistant-for-tax-research.html | **[não confirmado]**; ver alerta Stanford acima (produtos TR testados). |
| **Wolters Kluwer (CCH AnswerConnect)** | GenAI sobre conteúdo de especialistas (federal, estadual, internacional), SmartCharts (tabelas comparativas por jurisdição), resumo de documentos. | https://www.businesswire.com/news/home/20240506811985/en/Wolters-Kluwer-launches-GenAI-functionality-within-CCH-AnswerConnect | **[não confirmado]**. Padrão útil: **SmartCharts** = matriz jurisdição × tema, mesma ideia da matriz país × artefato. |
| **LexisNexis (Lexis+ AI / Practical Guidance)** | Guias práticos de emprego + assistente Protégé. | https://www.lexisnexis.co.uk/products/lexis-plus-practical-guidance.html | **[não confirmado]**. |
| **PwC Worldwide Tax Summaries / EY Worldwide Personal Tax and Immigration Guide** | Resumos por país com estrutura fixa de seções (residência, renda, deduções, retenções, administração); EY ~150 jurisdições, "vigente em 1/10/2024". | https://www.pwc.com/taxsummaries · https://www.ey.com/en_gl/technical/tax-guides/worldwide-personal-tax-and-immigration-guide | Fonte secundária (nível C para nós). Padrão útil: **mesma estrutura de seções em todos os países + data de corte declarada**. |
| **Mercer, KPMG Global Payroll Guide, Avalara** | — | Não encontrei material específico e verificável sobre como organizam conhecimento estatutário de payroll. | Não confirmado; não citar. |

**Padrão comum (o que é verificável):** (1) estrutura fixa por país; (2) conteúdo datado (data de corte/efetiva); (3) objeto "mudança legal" com país, área afetada e data; (4) time humano de monitoramento; (5) IA por cima, como camada de pergunta, nunca como origem do dado.

---

## 4. Processo e rastreabilidade num grafo

### 4.1 Referências de modelo
- **Obligations register / mapeamento regulatório (GRC/RegTech):** registro de obrigações no nível da linha da norma, mapeado para políticas, procedimentos, controles e evidências; mudança regulatória propaga para os controles afetados. https://www.ascentregtech.com/blog/reg-mapping-is-key-to-compliance-are-you-doing-it-effectively/ · https://www.smartsuite.com/grc-foundation/how-to-connect-regulatory-obligations-to-policies-controls-and-evidence · https://www.corlytics.com/solutions/regulatory-controls-mapping/ (fornecedores; o *modelo* é padrão, os ganhos são **[não confirmado]**).
- **Matriz de rastreabilidade bidirecional (engenharia regulada: FDA, ISO 26262, DO-178C):** requisito ↔ teste ↔ defeito, nos dois sentidos, para análise de impacto. https://blog.testlodge.com/requirement-traceability-matrix/ · https://admhelp.microfocus.com/alm/en/15.5/online_help/Content/UG/t_use_traceability_matrix.htm
- **W3C PROV-O** (proveniência: o que derivou de quê, gerado por qual atividade, atribuído a quem) — seção 1.1.
- **FRBR/ELI** (lei × versão datada) e **Graphiti** (bitemporal) — seções 1.1 e 2.
- **KCS v6 (Consortium for Service Innovation):** artigo de conhecimento nasce e melhora no atendimento ("reuse is review"); já é o método do cérebro. https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030

### 4.2 Boas práticas que valem para nós
1. **Identidade estável + versão datada** para tudo que muda: Lei (Work) × Versão da lei; Artefato × Versão do artefato (v1.3, v1.4); Valor × vigência.
2. **Dois tempos**: `vigencia_inicio/fim` (quando vale na lei) e `registrado_em` (quando o cérebro soube). Permite responder "o que dissemos em julho" × "o que era verdade em julho" — essencial para explicar correções.
3. **Nunca apagar aresta**: invalidar com data (Graphiti; nossa Regra 2).
4. **Proveniência em toda aresta factual**: fonte (URI/arquivo + artigo), nível de evidência A/B/C/D (já definido no PLANO), quem registrou, sessão.
5. **Granularidade de artigo**, não de documento (modelo LRMoo; nosso `correcoes.md` já cita "Art. 6.1").
6. **Rastreabilidade nos dois sentidos**: da lei para os artefatos (impacto de mudança legal) e do ticket para a lei (por que o artefato diz isso).
7. **Correção como nó de primeira classe**: liga o erro (versão errada do artefato), a versão correta, a fonte e o ticket de origem — é o que o `correcoes.md` já faz em tabela.

---

## 5. Apresentação para gestão — exemplos

| Visão | O que mostra | Exemplo real | Para nós |
|---|---|---|---|
| **Matriz jurisdição × tema** | Comparação lado a lado por país. | Wolters Kluwer CCH SmartCharts (acima); PwC/EY guias com seções fixas. | Matriz **país × artefato** (CCG/WTC/DD/Specs/SIR/Payslip/Skill) com versão vigente e data. |
| **Painel de mudanças legais** | Lista filtrável por país, componente, data legal, data de entrega. | SAP Announcement of Legal Change (acima). | Lista `MudancaLegal` por país com status: detectada → avaliada → artefato atualizado → entregue. |
| **Matriz de rastreabilidade com cobertura** | % de requisitos com teste; lacunas (linked/unlinked) por versão. | Relatórios de rastreabilidade de ferramentas de teste (Testsigma, Micro Focus ALM, Qase). | % de valores estatutários com fonte nível A; regras do CCG sem uso em WTC/DD; artefatos sem conferência registrada. |
| **Mapa de cobertura de rules-as-code** | O que está e não está modelado por país/programa. | PolicyEngine mantém um *coverage tracker* público de programas modelados (repo `policyengine-coverage-tracker`, visto em https://github.com/PolicyEngine/policyengine-coverage-tracker/pull/18/files — não abri em detalhe). | Painel países × etapa (já existe em `00-INDEX.md` e `graphify-out/mapa-processo.html`). |
| **Funil de qualidade/correções** | Erros por artefato/país ao longo do tempo. | Prática de RTM: defeitos ligados a requisitos. | Correções por artefato/país/mês; tempo ticket → correção; reincidência do mesmo padrão. |

---

## 6. Proposta de modelo de dados para o cérebro

> Baseado em: FRBR/ELI (lei × versão), OpenFisca (valor datado com referência), Graphiti (bitemporal, invalidar sem apagar), PROV-O (derivação/autoria), obligations register e RTM (rastreabilidade bidirecional), KCS (correção como conhecimento). Implementável como frontmatter YAML nas notas `.md` + `[[links]]` tipados, lidos pelo graphify. Não exige banco de grafo.

### 6.1 Tipos de nó

| Nó | Exemplo | Atributos mínimos |
|---|---|---|
| `Pais` | Colômbia (CO) | código ISO, moeda, ano fiscal, etapa atual (pipeline/design/produção/suporte) |
| `Orgao` | DIAN, UGPP, CNPS | país, sigla, site oficial |
| `FonteLegal` (Work) | Estatuto Tributario Art. 383; Orden PJC/297/2026 | país, tipo (lei/decreto/resolução/manual técnico/XSD), identificador oficial (ELI/URI), artigo |
| `VersaoFonte` (Expression/arquivo) | `raw/docs/oficiais/CO/2026-10-12-Res-000013.pdf` | data de publicação, data de download, md5, URL de origem, **nível de evidência** (A oficial / B oficial secundária / C terceiro / D sem fonte) |
| `Regra` | "Base de cotização continua durante licença" | país, domínio (IR, seg. social, trabalhista, relatório), texto curto, `vigencia_inicio`, `vigencia_fim` |
| `Parametro` (Valor) | Teto CNPS; UVT 2026 | unidade, valor, `vigencia_inicio`, `vigencia_fim`, `registrado_em` |
| `RelatorioEstatutario` | PILA, Formulario 350, CO-RPT-001 | órgão, periodicidade, formato (XML/SOAP/TXT) |
| `WageType` | 62983 (ES) | país, código, classificação fiscal/previdenciária |
| `CampoDD` | campo do Data Dictionary | país, nome, tipo, obrigatório? |
| `Artefato` (Work) | CO-CCG, CO-WTC, ES-CRA-001 (Report Spec), SIR, Payslip, skill `payroll-compliance-colombia` | tipo, país, dono |
| `VersaoArtefato` | CO-WTC v1.6 | número, data, caminho local, caminho Drive, md5, `CONFERENCIA.md`, vigente? (Regra 8: maior número) |
| `EtapaServico` | Research Pipeline, Design, Produção (fronteira), Suporte | dono, entradas, saídas |
| `Entrega` | "2026-10-16-teto-CNPS" | data, pasta, frente, artefatos entregues |
| `Ticket` | HRBS-10563, SR-79, CT-4593 | sistema (YouTrack/monday), país, tipo, status, datas |
| `Correcao` | linha de `correcoes.md` | data, errado, correto, fonte, origem |
| `MudancaLegal` | reforma, nova resolução | país, data publicação, data efeito, status (detectada/avaliada/aplicada) |
| `Decisao` | "CO-RPT-007 fora do escopo (HRMS)" | data, quem decidiu, fonte (e-mail/chat/reunião) |
| `Pessoa`/`Time` | Manju, Mohit, frente Suporte | papel (sem dados de funcionários de cliente — Regra 3) |
| `Sessao` | `sessoes/2026-10-27.md` | data, frente |
| `Pendencia` | item aberto no hub | país, dono, desde quando |

### 6.2 Tipos de ligação (arestas)

**Legal / temporal**
- `VersaoFonte —versao_de→ FonteLegal`
- `FonteLegal —altera / revoga / regulamenta→ FonteLegal` (com data de efeito)
- `FonteLegal —emitida_por→ Orgao`
- `Regra —fundamentada_em→ FonteLegal` *(atributos: artigo, trecho, nível de evidência)*
- `Parametro —definido_em→ FonteLegal` *(idem)*
- `Parametro —substitui→ Parametro` (versão anterior; a antiga ganha `vigencia_fim`, nunca é apagada)
- `Regra —excecao_de→ Regra` (derrotabilidade, à la LegalRuleML)
- `MudancaLegal —origina→ FonteLegal` e `MudancaLegal —afeta→ Regra | Parametro | Artefato`

**Artefatos (rastreabilidade para frente)**
- `VersaoArtefato —versao_de→ Artefato`
- `VersaoArtefato —derivada_de→ VersaoArtefato` (PROV `wasDerivedFrom`)
- `VersaoArtefato —implementa→ Regra | Parametro` (ex.: CCG §x; WTC linha 62983; DD campo y)
- `WageType —tratado_por→ Regra` e `WageType —reportado_em→ RelatorioEstatutario` (o "qual WT entra em qual relatório")
- `CampoDD —exigido_por→ RelatorioEstatutario | FonteLegal` (regra "Form × DD = necessidade": só entra campo que a fonte prova necessário)
- `Artefato —pertence_a→ Pais` e `Artefato —produzido_em→ EtapaServico`
- `Entrega —entrega→ VersaoArtefato`; `Entrega —gerada_por→ Sessao/Frente` (PROV `wasGeneratedBy` / `wasAttributedTo`)

**Suporte e correções (rastreabilidade para trás)**
- `Ticket —pergunta_sobre→ Artefato | Regra | Parametro`
- `Ticket —resolvido_com→ VersaoArtefato | Correcao`
- `Correcao —corrige→ VersaoArtefato` (a errada) e `Correcao —resulta_em→ VersaoArtefato` (a certa)
- `Correcao —fundamentada_em→ FonteLegal`
- `Correcao —mesmo_padrao_de→ Correcao` (reincidência; regra 6 do protocolo de ticket)
- `Decisao —define→ Regra | Escopo`; `Decisao —tomada_por→ Pessoa`
- `Pendencia —bloqueia→ EtapaServico | Artefato`

**Processo**
- `EtapaServico —seguida_de→ EtapaServico` (Pipeline → Design → Produção → Suporte)
- `Pais —esta_em→ EtapaServico` *(com data; histórico preservado)*
- `Artefato —consumido_por→ EtapaServico` (CCG alimenta Design; WTC/DD documentam o design)

### 6.3 Atributos obrigatórios em toda aresta factual
`fonte` (arquivo/URI + artigo) · `nivel_evidencia` (A/B/C/D) · `vigencia_inicio` / `vigencia_fim` · `registrado_em` · `registrado_por` (frente/sessão) · `status` (vigente/substituída/invalidada). Sem `fonte` → marca `⚠️ sem fonte` (Regra 1).

### 6.4 Consultas que o modelo passa a responder
- "Saiu nova resolução da DIAN: quais regras, WT, campos DD e specs da Colômbia mudam?" (`MudancaLegal → afeta → ... ← implementa ← VersaoArtefato`).
- "Por que o WTC ES diz clave L05 para 62983?" (`WageType → tratado_por → Regra → fundamentada_em → Art. 7.e LIRPF`, + `Correcao` HRBS-10563).
- "Qual era o teto vigente em 2025-06 e o que nós dissemos na época?" (bitemporal).
- "Quais valores estatutários estão sem fonte nível A?" / "Quais regras do CCG não aparecem em nenhum artefato?" (cobertura).
- "Que padrões de erro se repetem entre países?" (`Correcao —mesmo_padrao_de→`).

### 6.5 Como implantar sem quebrar o que existe (sugestão; decisão do usuário)
1. Frontmatter YAML com `tipo:` e campos acima nos hubs, notas de serviço e `CONFERENCIA.md`; links tipados no corpo (ex.: `implementa:: [[...]]`, padrão Dataview/inline field) para o graphify tipar as arestas.
2. `correcoes.md` ganha colunas `artefato_errado`, `artefato_certo`, `nivel_evidencia` (ou cada linha vira nó).
3. Valores estatutários no hub em tabela "estilo OpenFisca" (uma linha por vigência + referência).
4. Painéis derivados do grafo: país × etapa (já existe), país × artefato (versão/data), cobertura de fonte, correções por artefato.

---

## Fontes principais (todas citadas acima)
- Laws.Africa works/expressions: https://developers.laws.africa/get-started/works-and-expressions
- Akoma Ntoso FRBR: https://diff.parlamento.ai/docs/akn/frbr
- ELI: https://interoperable-europe.ec.europa.eu/collection/eli-european-legislation-identifier/solution/eli-i
- LRMoo legal norms: https://arxiv.org/pdf/2506.07853
- LegalRuleML: https://www.oasis-open.org/?p=7649
- LKIF: https://en.wikipedia.org/wiki/Legal_Knowledge_Interchange_Format
- FIBO: https://spec.edmcouncil.org/fibo/
- OpenFisca parâmetros: https://openfisca.readthedocs.io/en/latest/coding-the-legislation/legislation_parameters.html
- Catala: https://www.microsoft.com/en-us/research/publication/catala-a-programming-language-for-the-law/
- Blawx: https://law.mit.edu/pub/blawxrulesascodedemonstration
- RegelSpraak: https://research.vu.nl/en/publications/regelspraak-a-cnl-for-executable-tax-rules-specification/
- AAAI payroll: https://ojs.aaai.org/index.php/AAAI/article/view/17774
- OCDE Cracking the Code: https://oecd-opsi.org/publications/cracking-the-code/
- GraphRAG: https://www.microsoft.com/en-us/research/blog/graphrag-unlocking-llm-discovery-on-narrative-private-data/
- LightRAG: https://arxiv.org/abs/2410.05779v3
- Neo4j LLM Graph Builder: https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/
- RAGulating Compliance: https://arxiv.org/html/2508.09893v1
- Graphiti/Zep: https://blog.getzep.com/beyond-static-knowledge-graphs/
- Stanford hallucination study: https://hai.stanford.edu/news/ai-trial-legal-models-hallucinate-1-out-6-or-more-benchmarking-queries
- PROV-O: https://www.w3.org/blog/2012/the-prov-ontology-an-update
- SAP Legal Change: https://blogs.sap.com/2020/09/18/how-to-find-legal-changes-using-the-announcement-of-legal-change-application/
- Vertex: https://www.vertexinc.com/sites/default/files/2022-03/vertex-payroll-tax-data-sheet.pdf
- Deel: https://www.deel.com/blog/introducing-deel-knowledge-hub/
- ADP: https://uk.adp.com/what-we-offer/products/adp-global-payroll.aspx
- Ascent RegTech (obligations mapping): https://www.ascentregtech.com/blog/reg-mapping-is-key-to-compliance-are-you-doing-it-effectively/
- KCS v6: https://library.serviceinnovation.org/KCS/KCS_v6/KCS_v6_Practices_Guide/030
